"""FoldMind: model-independent orchestration of Fold's symbolic components.

FoldMind coordinates observation capture, task-relative abstraction,
constraint-driven refinement, and append-only memory. It is deterministic:
an external model may propose observations/features/constraints, but this
module validates and records them rather than executing generated code.

Run:
    python tools/FoldMind.py
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import tempfile
from typing import Sequence

from FoldConcept import Context, Instance, build_concepts, check_equivalence_laws
from FoldLoop import PairConstraint, audit, refine_until_consistent
from FoldMemory import FoldMemory
from FoldHypothesis import Example as HypothesisExample, generate, evaluate, retain_audit
from FoldHypothesis import Hypothesis
from FoldExperiment import ExperimentCandidate, ExperimentSelection, choose_experiment as rank_experiments
try:
    from .FoldRetention import RetentionPlan, minimum_retention_features, verify_retention_plan, retention_plan_proves_optimality
except ImportError:  # pragma: no cover - direct script execution
    from FoldRetention import RetentionPlan, minimum_retention_features, verify_retention_plan


@dataclass(frozen=True)
class Observation:
    identifier: str
    features: tuple[tuple[str, str | int | float | bool | None], ...]
    source: str

    @classmethod
    def make(
        cls, identifier: str, features: dict[str, str | int | float | bool | None],
        source: str,
    ) -> "Observation":
        if not identifier or not source:
            raise ValueError("observation identifier and source are required")
        return cls(identifier, tuple(sorted(features.items())), source)


@dataclass(frozen=True)
class FoldProposal:
    """A model-neutral proposal; it contains data, never executable code."""
    task: str
    initial_features: tuple[str, ...]
    candidate_features: tuple[str, ...]
    constraints: tuple[PairConstraint, ...]


@dataclass(frozen=True)
class CycleReport:
    task: str
    observation_ids: tuple[str, ...]
    initial_features: tuple[str, ...]
    final_features: tuple[str, ...]
    concept_count: int
    constraints_satisfied: bool
    violations: tuple[PairConstraint, ...]
    refinements: tuple[str, ...]
    equivalence_laws_hold: bool
    memory_head: str



@dataclass(frozen=True)
class HypothesisCycleReport:
    task: str
    training_ids: tuple[str, ...]
    held_out_ids: tuple[str, ...]
    candidates: int
    falsified: int
    supported: int
    untested: int
    memory_head: str

class FoldMind:
    """A single auditable cycle joining FoldConcept, FoldLoop, and FoldMemory."""

    def __init__(self, memory: FoldMemory):
        self.memory = memory

    def process(
        self,
        observations: Sequence[Observation],
        proposal: FoldProposal,
    ) -> CycleReport:
        if not observations:
            raise ValueError("a cycle requires at least one observation")
        ids = [item.identifier for item in observations]
        if len(set(ids)) != len(ids):
            raise ValueError("observation identifiers must be unique")
        if not proposal.task:
            raise ValueError("task must be nonempty")
        instances = tuple(
            Instance.make(item.identifier, dict(item.features), item.source)
            for item in observations
        )
        # Validate all proposed features and all constraint references before
        # writing, so malformed proposals do not leave a partial cycle.
        known = set(ids)
        for item in instances:
            for feature in set(proposal.initial_features) | set(proposal.candidate_features):
                item.get(feature)
        for rule in proposal.constraints:
            if rule.left not in known or rule.right not in known:
                raise KeyError(f"constraint refers to unknown observation: {rule}")

        if not self.memory.verify():
            raise ValueError("memory integrity check failed; refusing cycle")

        for item in observations:
            self.memory.append(
                "observation", f"observation:{item.identifier}",
                json.dumps(dict(item.features), sort_keys=True, ensure_ascii=False),
                source=item.source, task=proposal.task,
                tags=("foldmind", "input"),
            )

        initial = Context(proposal.task, proposal.initial_features)
        concepts_before = build_concepts(instances, initial)
        self.memory.append(
            "abstraction", f"context:{proposal.task}",
            json.dumps({
                "features": list(initial.relevant_features),
                "concept_count": len(concepts_before),
                "concepts": [
                    {"signature": list(map(list, c.signature)),
                     "members": list(c.members)}
                    for c in concepts_before
                ],
            }, sort_keys=True, ensure_ascii=False),
            source="FoldConcept", task=proposal.task,
            tags=("foldmind", "initial-abstraction"),
        )

        result = refine_until_consistent(
            instances, initial, proposal.candidate_features, proposal.constraints
        )
        for index, refinement in enumerate(result.refinements, start=1):
            self.memory.append(
                "refinement", f"context:{proposal.task}",
                json.dumps({
                    "step": index,
                    "feature_added": refinement.feature,
                    "newly_separated": [list(pair) for pair in refinement.newly_separated],
                }, sort_keys=True),
                source="FoldLoop", task=proposal.task,
                tags=("foldmind", "counterexample-refinement"),
            )

        final_concepts = build_concepts(instances, result.context)
        remaining = audit(instances, result.context, proposal.constraints)
        laws_hold = check_equivalence_laws(instances, result.context)
        report_data = {
            "initial_features": list(initial.relevant_features),
            "final_features": list(result.context.relevant_features),
            "concept_count": len(final_concepts),
            "constraints_satisfied": result.satisfied,
            "violations": [asdict(rule) for rule in remaining],
            "unresolved_features": list(result.unresolved_features),
            "equivalence_laws_hold": laws_hold,
        }
        self.memory.append(
            "cycle-report", f"cycle:{proposal.task}",
            json.dumps(report_data, sort_keys=True, ensure_ascii=False),
            source="FoldMind", task=proposal.task,
            confidence=1.0 if result.satisfied and laws_hold else 0.0,
            tags=("foldmind", "verified" if result.satisfied and laws_hold else "needs-review"),
        )
        return CycleReport(
            task=proposal.task,
            observation_ids=tuple(ids),
            initial_features=initial.relevant_features,
            final_features=result.context.relevant_features,
            concept_count=len(final_concepts),
            constraints_satisfied=result.satisfied,
            violations=remaining,
            refinements=tuple(r.feature for r in result.refinements),
            equivalence_laws_hold=laws_hold,
            memory_head=self.memory.head,
        )



    def test_hypotheses(
        self,
        observations: Sequence[Observation],
        *,
        task: str,
        training_ids: Sequence[str],
        held_out_ids: Sequence[str],
    ) -> HypothesisCycleReport:
        """Generate on training data, falsify on held-out data, and retain every audit."""
        if not task:
            raise ValueError("task must be nonempty")
        by_id = {item.identifier: item for item in observations}
        if len(by_id) != len(observations):
            raise ValueError("observation identifiers must be unique")
        train_ids, test_ids = tuple(training_ids), tuple(held_out_ids)
        if not train_ids:
            raise ValueError("at least one training observation is required")
        if len(set(train_ids)) != len(train_ids) or len(set(test_ids)) != len(test_ids):
            raise ValueError("split identifiers must be unique")
        if set(train_ids) & set(test_ids):
            raise ValueError("training and held-out sets must be disjoint")
        missing = (set(train_ids) | set(test_ids)) - set(by_id)
        if missing:
            raise KeyError(f"unknown observations in split: {sorted(missing)}")
        if not self.memory.verify():
            raise ValueError("memory integrity check failed; refusing hypothesis cycle")
        training = tuple(HypothesisExample.make(
            key, dict(by_id[key].features), by_id[key].source
        ) for key in train_ids)
        held_out = tuple(HypothesisExample.make(
            key, dict(by_id[key].features), by_id[key].source
        ) for key in test_ids)
        candidates = generate(training, task)
        evaluated = evaluate(candidates, held_out)
        retained = retain_audit(self.memory, evaluated, "FoldMind/FoldHypothesis")
        if retained != len(evaluated):
            raise RuntimeError("not every hypothesis audit was retained")
        return HypothesisCycleReport(
            task=task, training_ids=train_ids, held_out_ids=test_ids,
            candidates=len(evaluated),
            falsified=sum(item.status == "falsified" for item in evaluated),
            supported=sum(item.status == "supported-on-held-out" for item in evaluated),
            untested=sum(item.status == "untested" for item in evaluated),
            memory_head=self.memory.head,
        )



    def plan_retention(
        self,
        observations: Sequence[Observation],
        *,
        task: str,
        base_features: Sequence[str],
        candidate_features: Sequence[str],
        must_link_pairs: Sequence[tuple[str, str]],
        cannot_link_pairs: Sequence[tuple[str, str]],
    ) -> RetentionPlan | None:
        """Find and audit a minimum safe residual feature set, then retain the plan."""
        if not task:
            raise ValueError("task must be nonempty")
        instances = tuple(
            Instance.make(item.identifier, dict(item.features), item.source)
            for item in observations
        )
        if len({item.identifier for item in instances}) != len(instances):
            raise ValueError("observation identifiers must be unique")
        if not self.memory.verify():
            raise ValueError("memory integrity check failed; refusing retention planning")
        context = Context(task, tuple(base_features))
        plan = minimum_retention_features(
            instances, context, tuple(candidate_features),
            tuple(must_link_pairs), tuple(cannot_link_pairs),
        )
        verified = (
            plan is not None
            and verify_retention_plan(
                instances, plan, tuple(must_link_pairs), tuple(cannot_link_pairs)
            )
        )
        optimality_certified = (
            plan is not None
            and retention_plan_proves_optimality(
                instances, context, tuple(candidate_features),
                tuple(must_link_pairs), tuple(cannot_link_pairs), plan,
            )
        )
        payload = {
            "base_features": list(base_features),
            "candidate_features": list(candidate_features),
            "retained_features": list(plan.retained_features) if plan else None,
            "final_features": list(plan.final_features) if plan else None,
            "minimum_cardinality": len(plan.retained_features) if plan else None,
            "independently_verified": verified,
            "lower_bound_pairs": [list(pair) for pair in plan.lower_bound_pairs] if plan else [],
            "lower_bound": len(plan.lower_bound_pairs) if plan else 0,
            "optimality_certified": optimality_certified,
            "status": ("optimality-certified" if optimality_certified else
                       "feasible-only" if verified else "no-safe-plan"),
            "scope": "finite supplied observations and candidate features",
        }
        self.memory.append(
            "retention-plan", f"retention:{task}",
            json.dumps(payload, sort_keys=True, ensure_ascii=False),
            source="FoldMind/FoldRetention", task=task,
            confidence=1.0 if optimality_certified else 0.5 if verified else 0.0,
            tags=("foldmind", "minimum-retention",
                  "optimality-certified" if optimality_certified else
                  "verified" if verified else "needs-review"),
        )
        if plan is not None and not verified:
            raise RuntimeError("retention plan failed independent verification")
        return plan

    def select_experiment(
        self,
        hypotheses: Sequence[Hypothesis],
        candidates: Sequence[ExperimentCandidate],
        *,
        task: str,
    ) -> ExperimentSelection | None:
        """Select a supplied candidate that best separates current hypotheses."""
        if not task:
            raise ValueError("task must be nonempty")
        if not self.memory.verify():
            raise ValueError("memory integrity check failed; refusing experiment selection")
        selection = rank_experiments(hypotheses, candidates)
        payload = {
            "selection": asdict(selection) if selection is not None else None,
            "candidate_pool": [item.example.identifier for item in candidates],
            "method": "disagreement-entropy-per-cost",
            "interpretation": "heuristic ranking, not Bayesian information gain",
        }
        subject = (f"experiment:{selection.candidate_id}"
                   if selection is not None else f"experiment:none:{task}")
        self.memory.append(
            "experiment-selection", subject,
            json.dumps(payload, sort_keys=True, ensure_ascii=False),
            source="FoldMind/FoldExperiment", task=task,
            tags=("foldmind", "active-experiment-selection",
                  "selected" if selection is not None else "no-discriminating-candidate"),
        )
        return selection


def _self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        memory = FoldMemory(Path(directory) / "mind.jsonl")
        mind = FoldMind(memory)
        observations = (
            Observation.make("red-ball", {"shape": "round", "colour": "red",
                                          "material": "rubber"}, "sensor:vision-1"),
            Observation.make("blue-ball", {"shape": "round", "colour": "blue",
                                           "material": "rubber"}, "sensor:vision-1"),
            Observation.make("red-box", {"shape": "square", "colour": "red",
                                         "material": "cardboard"}, "sensor:vision-1"),
            Observation.make("red-ball-copy", {"shape": "round", "colour": "red",
                                                "material": "rubber"}, "sensor:vision-2"),
        )
        proposal = FoldProposal(
            task="object-labeling",
            initial_features=("shape",),
            candidate_features=("colour", "material"),
            constraints=(
                PairConstraint("red-ball", "blue-ball", False, "different labels"),
                PairConstraint("red-ball", "red-ball-copy", True, "same label"),
                PairConstraint("red-ball", "red-box", False, "different labels"),
            ),
        )
        report = mind.process(observations, proposal)
        events = memory.recall(task="object-labeling", include_superseded=True)
        checks = [
            ("cycle distinguishes the required examples", report.constraints_satisfied),
            ("at least one counterexample drives refinement", bool(report.refinements)),
            ("the initial abstraction is recorded", any(e.event_type == "abstraction" for e in events)),
            ("all raw observations are retained", sum(e.event_type == "observation" for e in events) == 4),
            ("refinement history is retained", sum(e.event_type == "refinement" for e in events) == len(report.refinements)),
            ("final report is retained", any(e.event_type == "cycle-report" for e in events)),
            ("equivalence laws hold for final projection", report.equivalence_laws_hold),
            ("memory chain verifies after the cycle", memory.verify(report.memory_head)),
            ("report exposes final feature context", set(report.final_features) >= {"shape", "colour"}),
        ]

        # Contradictory model proposals must be reported as unresolved, not
        # silently accepted as a successful learning result.
        contradictory = FoldProposal(
            task="contradiction-check",
            initial_features=(),
            candidate_features=("shape", "colour"),
            constraints=(
                PairConstraint("red-ball", "blue-ball", True, "must-link"),
                PairConstraint("red-ball", "blue-ball", False, "cannot-link"),
            ),
        )
        blocked = mind.process(observations[:2], contradictory)
        checks.append(("contradictory constraints remain unresolved",
                       not blocked.constraints_satisfied and bool(blocked.violations)))
        checks.append(("unresolved cycle is marked for review",
                       any(e.task == "contradiction-check" and "needs-review" in e.tags
                           for e in memory.recall(task="contradiction-check"))))

        # Reject unknown identifiers before appending any event.
        before = len(memory._read())
        invalid = FoldProposal("invalid", (), ("shape",),
                               (PairConstraint("red-ball", "missing", False),))
        try:
            mind.process(observations[:1], invalid)
            rejected = False
        except KeyError:
            rejected = True
        checks.append(("invalid proposals are rejected", rejected))
        checks.append(("pre-validation prevents partial memory writes",
                       len(memory._read()) == before))


        # Hypothesis proposals must train and evaluate on disjoint observations.
        hypothesis_observations = (
            Observation.make("train-sun", {"weather": "sun", "play": "yes"}, "train:v1"),
            Observation.make("train-rain", {"weather": "rain", "play": "no"}, "train:v1"),
            Observation.make("test-sun", {"weather": "sun", "play": "yes"}, "test:v1"),
            Observation.make("test-rain-counterexample", {"weather": "rain", "play": "yes"}, "test:v1"),
        )
        hypothesis_report = mind.test_hypotheses(
            hypothesis_observations, task="weather-play",
            training_ids=("train-sun", "train-rain"),
            held_out_ids=("test-sun", "test-rain-counterexample"),
        )
        hypothesis_events = memory.recall(task="weather-play")
        checks.append(("FoldMind generates and evaluates hypotheses",
                       hypothesis_report.candidates > 0))
        checks.append(("FoldMind exposes held-out falsifications",
                       hypothesis_report.falsified > 0))
        checks.append(("FoldMind retains hypothesis audit events",
                       len(hypothesis_events) == hypothesis_report.candidates))
        before_hypothesis_error = len(memory._read())
        try:
            mind.test_hypotheses(
                hypothesis_observations, task="invalid-split",
                training_ids=("train-sun",), held_out_ids=("train-sun",),
            )
            split_rejected = False
        except ValueError:
            split_rejected = True
        checks.append(("overlapping train/test split is rejected", split_rejected))
        checks.append(("invalid hypothesis split causes no memory writes",
                       len(memory._read()) == before_hypothesis_error))


        # Minimum retention is integrated into the audited memory cycle.
        retention_observations = (
            Observation.make("retain-a", {"shape": "round", "colour": "red",
                                          "material": "rubber", "weight": 1}, "fixture"),
            Observation.make("retain-b", {"shape": "round", "colour": "blue",
                                          "material": "rubber", "weight": 1}, "fixture"),
            Observation.make("retain-c", {"shape": "round", "colour": "red",
                                          "material": "cardboard", "weight": 3}, "fixture"),
            Observation.make("retain-e", {"shape": "round", "colour": "red",
                                          "material": "rubber", "weight": 9}, "fixture"),
        )
        retention_plan = mind.plan_retention(
            retention_observations, task="retention-demo",
            base_features=("shape",),
            candidate_features=("colour", "material", "weight"),
            must_link_pairs=(("retain-a", "retain-e"),),
            cannot_link_pairs=(("retain-a", "retain-b"), ("retain-a", "retain-c")),
        )
        retention_events = memory.recall(task="retention-demo")
        checks.append(("FoldMind finds the minimum two-feature memory",
                       retention_plan is not None
                       and retention_plan.retained_features == ("colour", "material")))
        checks.append(("minimum retention plan is independently verified",
                       retention_plan is not None and verify_retention_plan(
                           tuple(Instance.make(o.identifier, dict(o.features), o.source)
                                 for o in retention_observations),
                           retention_plan, (("retain-a", "retain-e"),),
                           (("retain-a", "retain-b"), ("retain-a", "retain-c")),
                       )))
        checks.append(("retention plan is appended to auditable memory",
                       any(e.event_type == "retention-plan" for e in retention_events)))

        # Select the next supplied experiment that most separates hypotheses.
        h_sun = Hypothesis("h-sun", "weather-play", "weather", "sun",
                           "play", "yes", 2, ("t1", "t2"), (), None, "candidate")
        h_rain = Hypothesis("h-rain", "weather-play", "weather", "sun",
                            "play", "no", 2, ("t3", "t4"), (), None, "candidate")
        experiment_pool = (
            ExperimentCandidate(HypothesisExample.make(
                "candidate-sun", {"weather": "sun", "play": "yes"}), 1.0),
            ExperimentCandidate(HypothesisExample.make(
                "candidate-rain", {"weather": "rain", "play": "yes"}), 2.0),
        )
        selected_experiment = mind.select_experiment(
            (h_sun, h_rain), experiment_pool, task="weather-play"
        )
        checks.append(("FoldMind selects the best discriminating experiment",
                       selected_experiment is not None
                       and selected_experiment.candidate_id == "candidate-sun"))
        checks.append(("experiment choice is retained in memory",
                       any(e.event_type == "experiment-selection"
                           for e in memory.recall(task="weather-play"))))
        no_choice = mind.select_experiment(
            (h_sun,), experiment_pool, task="single-hypothesis"
        )
        checks.append(("no-disagreement pool is explicitly left unselected",
                       no_choice is None and any(
                           "no-discriminating-candidate" in e.tags
                           for e in memory.recall(task="single-hypothesis")
                       )))

        for name, passed in checks:
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        print(f"{sum(p for _, p in checks)}/{len(checks)} checks passed")
        if not all(p for _, p in checks):
            raise SystemExit("FoldMind regression failure")


if __name__ == "__main__":
    _self_test()
