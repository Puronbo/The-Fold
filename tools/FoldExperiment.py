"""FoldExperiment: choose supplied experiments that best separate hypotheses.

This is deterministic disagreement-based selection, not Bayesian information gain.
It selects among a caller-supplied candidate pool; it does not invent experiments.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math
from typing import Sequence

from FoldHypothesis import Example, Hypothesis, predict


@dataclass(frozen=True)
class ExperimentCandidate:
    example: Example
    cost: float = 1.0


@dataclass(frozen=True)
class ExperimentSelection:
    candidate_id: str
    predictions: tuple[tuple[str, bool], ...]
    support_count: int
    reject_count: int
    applicable_count: int
    disagreement_entropy: float
    utility: float


def _entropy(yes: int, no: int) -> float:
    total = yes + no
    if not total or not yes or not no:
        return 0.0
    p = yes / total
    q = no / total
    return -(p * math.log2(p) + q * math.log2(q))


def score_candidate(
    hypotheses: Sequence[Hypothesis], candidate: ExperimentCandidate
) -> ExperimentSelection:
    if not candidate.example.identifier:
        raise ValueError("candidate identifier is required")
    if not math.isfinite(candidate.cost) or candidate.cost <= 0:
        raise ValueError("experiment cost must be finite and positive")
    predictions = []
    for hypothesis in hypotheses:
        try:
            result = predict(hypothesis, candidate.example)
        except KeyError as exc:
            raise ValueError(
                f"candidate {candidate.example.identifier!r} is missing a required feature"
            ) from exc
        if result is not None:
            predictions.append((hypothesis.identifier, result))
    yes = sum(value for _, value in predictions)
    no = len(predictions) - yes
    entropy = _entropy(yes, no)
    return ExperimentSelection(
        candidate_id=candidate.example.identifier,
        predictions=tuple(predictions),
        support_count=yes,
        reject_count=no,
        applicable_count=len(predictions),
        disagreement_entropy=entropy,
        utility=entropy / candidate.cost,
    )


def choose_experiment(
    hypotheses: Sequence[Hypothesis],
    candidates: Sequence[ExperimentCandidate],
) -> ExperimentSelection | None:
    """Return the highest-disagreement candidate, or None if none separates rules."""
    if not hypotheses:
        raise ValueError("at least one hypothesis is required")
    if not candidates:
        raise ValueError("at least one candidate experiment is required")
    hypothesis_ids = [item.identifier for item in hypotheses]
    candidate_ids = [item.example.identifier for item in candidates]
    if len(set(hypothesis_ids)) != len(hypothesis_ids):
        raise ValueError("hypothesis identifiers must be unique")
    if len(set(candidate_ids)) != len(candidate_ids):
        raise ValueError("candidate identifiers must be unique")
    scored = [score_candidate(hypotheses, item) for item in candidates]
    discriminating = [item for item in scored
                      if item.support_count > 0 and item.reject_count > 0]
    if not discriminating:
        return None
    return min(
        discriminating,
        key=lambda item: (
            -item.utility, -item.disagreement_entropy,
            -item.applicable_count, item.candidate_id,
        ),
    )


def _self_test() -> None:
    from FoldMemory import FoldMemory
    from pathlib import Path
    import tempfile

    h1 = Hypothesis("h-sun", "weather", "weather", "sun", "play", "yes",
                    2, ("t1", "t2"), (), None, "candidate")
    h2 = Hypothesis("h-rain", "weather", "weather", "sun", "play", "no",
                    2, ("t3", "t4"), (), None, "candidate")
    h3 = Hypothesis("h-cloud", "weather", "weather", "cloud", "play", "no",
                    1, ("t5",), (), None, "candidate")
    balanced = ExperimentCandidate(
        Example.make("try-sun", {"weather": "sun", "play": "yes"}), 1.0
    )
    costlier = ExperimentCandidate(
        Example.make("try-rain", {"weather": "sun", "play": "yes"}), 2.0
    )
    checks = []
    scored = score_candidate((h1, h2), balanced)
    checks.append(("candidate separates opposing hypotheses",
                   scored.support_count == 1 and scored.reject_count == 1))
    checks.append(("balanced disagreement has one bit of entropy",
                   scored.disagreement_entropy == 1.0))
    checks.append(("cost reduces selection utility",
                   score_candidate((h1, h2), costlier).utility == 0.5))
    selected = choose_experiment((h1, h2), (costlier, balanced))
    checks.append(("highest utility candidate is selected",
                   selected is not None and selected.candidate_id == "try-sun"))
    checks.append(("ties resolve deterministically by identifier",
                   choose_experiment((h1, h2), (
                       ExperimentCandidate(Example.make("z", {"weather": "sun", "play": "yes"})),
                       ExperimentCandidate(Example.make("a", {"weather": "sun", "play": "yes"})),
                   )).candidate_id == "a"))
    checks.append(("non-discriminating pool returns no selection",
                   choose_experiment((h1,), (balanced,)) is None))
    try:
        choose_experiment((h1, h1), (balanced,))
        duplicate_rejected = False
    except ValueError:
        duplicate_rejected = True
    checks.append(("duplicate hypothesis identifiers are rejected", duplicate_rejected))
    try:
        score_candidate((h1,), ExperimentCandidate(
            Example.make("missing", {"weather": "sun"})
        ))
        missing_rejected = False
    except ValueError:
        missing_rejected = True
    checks.append(("incomplete experiment descriptions are rejected", missing_rejected))
    try:
        score_candidate((h1,), ExperimentCandidate(
            Example.make("bad-cost", {"weather": "sun", "play": "yes"}), 0
        ))
        cost_rejected = False
    except ValueError:
        cost_rejected = True
    checks.append(("nonpositive experiment costs are rejected", cost_rejected))
    with tempfile.TemporaryDirectory() as directory:
        memory = FoldMemory(Path(directory) / "experiment.jsonl")
        memory.append(
            "experiment-selection", "experiment:try-sun",
            json.dumps(asdict(selected), sort_keys=True),
            source="FoldExperiment", task="weather",
            tags=("experiment", "disagreement-selection"),
        )
        checks.append(("selection can be retained in auditable memory",
                       memory.verify() and len(memory.recall(task="weather")) == 1))
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name}")
    print(f"{sum(p for _, p in checks)}/{len(checks)} checks passed")
    if not all(p for _, p in checks):
        raise SystemExit("FoldExperiment regression failure")


if __name__ == "__main__":
    _self_test()
