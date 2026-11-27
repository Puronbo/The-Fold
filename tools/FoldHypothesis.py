"""FoldHypothesis: generate and falsify simple, auditable feature rules.

Rules are declarative equality predicates only; no generated code is executed.
Candidate generation uses a training split. Evaluation uses a separate held-out
split. The empirical score is descriptive, not a calibrated probability.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from typing import Mapping, Sequence

Value = str | int | float | bool | None


@dataclass(frozen=True)
class Example:
    identifier: str
    features: tuple[tuple[str, Value], ...]
    source: str = "unspecified"

    @classmethod
    def make(cls, identifier: str, features: Mapping[str, Value],
             source: str = "unspecified") -> "Example":
        if not identifier or not source:
            raise ValueError("identifier and source are required")
        return cls(identifier, tuple(sorted(features.items())), source)

    def get(self, name: str) -> Value:
        values = dict(self.features)
        if name not in values:
            raise KeyError(f"{self.identifier} lacks feature {name!r}")
        return values[name]


@dataclass(frozen=True)
class Hypothesis:
    identifier: str
    task: str
    if_feature: str
    equals: Value
    then_feature: str
    equals_value: Value
    training_support: int
    supporting_ids: tuple[str, ...]
    counterexample_ids: tuple[str, ...]
    score: float | None
    status: str


def _rule_id(task: str, left: str, value: Value,
             right: str, result: Value) -> str:
    payload = json.dumps([task, left, value, right, result],
                         sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def generate(training: Sequence[Example], task: str) -> tuple[Hypothesis, ...]:
    """Generate every observed one-feature equality implication from training."""
    if not task or not training:
        raise ValueError("task and nonempty training data are required")
    ids = [item.identifier for item in training]
    if len(set(ids)) != len(ids):
        raise ValueError("training identifiers must be unique")
    rules: dict[tuple[str, Value, str, Value], list[str]] = {}
    for item in training:
        values = dict(item.features)
        for left, antecedent in values.items():
            for right, consequent in values.items():
                if left != right:
                    rules.setdefault((left, antecedent, right, consequent), []).append(
                        item.identifier
                    )
    result = []
    for (left, antecedent, right, consequent), members in sorted(
        rules.items(), key=lambda pair: repr(pair[0])
    ):
        result.append(Hypothesis(
            identifier=_rule_id(task, left, antecedent, right, consequent),
            task=task, if_feature=left, equals=antecedent,
            then_feature=right, equals_value=consequent,
            training_support=len(members), supporting_ids=tuple(members),
            counterexample_ids=(), score=None, status="candidate",
        ))
    return tuple(result)


def predict(hypothesis: Hypothesis, example: Example) -> bool | None:
    """Return True/False when the antecedent applies; None otherwise."""
    if example.get(hypothesis.if_feature) != hypothesis.equals:
        return None
    return example.get(hypothesis.then_feature) == hypothesis.equals_value


def evaluate(hypotheses: Sequence[Hypothesis],
             held_out: Sequence[Example]) -> tuple[Hypothesis, ...]:
    """Falsify candidates on held-out examples; never train on this split."""
    ids = [item.identifier for item in held_out]
    if len(set(ids)) != len(ids):
        raise ValueError("held-out identifiers must be unique")
    evaluated = []
    for hypothesis in hypotheses:
        support, counter = [], []
        for item in held_out:
            outcome = predict(hypothesis, item)
            if outcome is True:
                support.append(item.identifier)
            elif outcome is False:
                counter.append(item.identifier)
        tested = len(support) + len(counter)
        score = len(support) / tested if tested else None
        status = ("untested" if not tested else
                  "falsified" if counter else "supported-on-held-out")
        evaluated.append(Hypothesis(
            **{**asdict(hypothesis),
               "supporting_ids": tuple(support),
               "counterexample_ids": tuple(counter),
               "score": score, "status": status}
        ))
    return tuple(evaluated)


def retain_audit(memory, hypotheses: Sequence[Hypothesis], source: str) -> int:
    """Append all evaluated candidates, including falsified ones, to FoldMemory."""
    count = 0
    for item in hypotheses:
        memory.append(
            "hypothesis-audit", f"hypothesis:{item.identifier}",
            json.dumps(asdict(item), sort_keys=True, ensure_ascii=False),
            source=source, task=item.task, confidence=(
                item.score if item.score is not None else 0.0
            ),
            tags=("fold-hypothesis", item.status),
        )
        count += 1
    return count


def _self_test() -> None:
    from pathlib import Path
    import tempfile
    from FoldMemory import FoldMemory

    train = (
        Example.make("t1", {"weather": "sun", "play": "yes"}),
        Example.make("t2", {"weather": "rain", "play": "no"}),
        Example.make("t3", {"weather": "sun", "play": "yes"}),
    )
    test = (
        Example.make("h1", {"weather": "sun", "play": "yes"}),
        Example.make("h2", {"weather": "sun", "play": "no"}),
        Example.make("h3", {"weather": "cloud", "play": "no"}),
    )
    candidates = generate(train, "outdoor-play")
    selected = next(h for h in candidates
                    if h.if_feature == "weather" and h.equals == "sun"
                    and h.then_feature == "play" and h.equals_value == "yes")
    results = evaluate((selected,), test)
    rule = results[0]
    checks = [
        ("candidate generated only from training observations",
         selected.training_support == 2 and selected.status == "candidate"),
        ("rule predicts when its antecedent applies",
         predict(selected, test[0]) is True),
        ("rule abstains when antecedent does not apply",
         predict(selected, test[2]) is None),
        ("held-out support is counted", rule.supporting_ids == ("h1",)),
        ("counterexample falsifies the candidate",
         rule.counterexample_ids == ("h2",) and rule.status == "falsified"),
        ("empirical score uses only applicable held-out cases",
         rule.score == 0.5),
        ("no applicable held-out examples remain untested",
         evaluate((selected,), (test[2],))[0].status == "untested"),
        ("generation is deterministic",
         generate(train, "outdoor-play") == candidates),
    ]
    with tempfile.TemporaryDirectory() as directory:
        memory = FoldMemory(Path(directory) / "hypotheses.jsonl")
        checks.append(("audit retains rejected candidates",
                       retain_audit(memory, results, "FoldHypothesis") == 1
                       and memory.recall(task="outdoor-play")[0].tags
                       == ("fold-hypothesis", "falsified")))
        checks.append(("audit chain verifies", memory.verify()))
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name}")
    print(f"{sum(p for _, p in checks)}/{len(checks)} checks passed")
    if not all(p for _, p in checks):
        raise SystemExit("FoldHypothesis regression failure")


if __name__ == "__main__":
    _self_test()
