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

        for name, passed in checks:
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        print(f"{sum(p for _, p in checks)}/{len(checks)} checks passed")
        if not all(p for _, p in checks):
            raise SystemExit("FoldMind regression failure")


if __name__ == "__main__":
    _self_test()
