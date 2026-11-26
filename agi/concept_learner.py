"""Task-scoped concept grouping with explicit positive and negative evidence.

This is a deterministic prototype, not an autonomous semantic learner. It
forms equivalence classes from candidate links while respecting counterexamples.
Run its standard-library tests with: python -m unittest agi.test_concept_learner
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Instance:
    """An observed instance; payload is retained as residual information."""

    key: str
    payload: Any


@dataclass(frozen=True)
class Candidate:
    """Evidence that two instances may be equivalent in this task context."""

    left: str
    right: str
    confidence: float
    source: str


@dataclass(frozen=True)
class Counterexample:
    """Evidence that two instances must remain in different concepts."""

    left: str
    right: str
    source: str


@dataclass(frozen=True)
class RejectedCandidate:
    candidate: Candidate
    blocking_counterexample: Counterexample


class UnknownInstance(KeyError):
    """Raised when evidence refers to an instance not in the learner."""


class ConceptLearner:
    """Build task-relative partitions from explicit evidence.

    Candidate links are processed in descending confidence order. A merge is
    rejected if it would put the endpoints of any counterexample in one class.
    Rebuilding from all evidence means a newly supplied counterexample can
    split a previously formed class without deleting the original observations.
    """

    def __init__(self, context: str) -> None:
        if not context.strip():
            raise ValueError("context must be non-empty")
        self.context = context
        self._instances: dict[str, Instance] = {}
        self._candidates: list[Candidate] = []
        self._counterexamples: list[Counterexample] = []
        self._groups: dict[str, frozenset[str]] = {}
        self._rejected: tuple[RejectedCandidate, ...] = ()

    @property
    def instances(self) -> dict[str, Instance]:
        return dict(self._instances)

    @property
    def rejected_candidates(self) -> tuple[RejectedCandidate, ...]:
        return self._rejected

    def add_instance(self, key: str, payload: Any) -> None:
        if not key:
            raise ValueError("instance key must be non-empty")
        if key in self._instances:
            raise ValueError(f"duplicate instance key: {key}")
        self._instances[key] = Instance(key, payload)
        self._rebuild()

    def propose_equivalence(
        self, left: str, right: str, confidence: float, source: str
    ) -> None:
        self._require_instances(left, right)
        if left == right:
            return
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if not source.strip():
            raise ValueError("source must be non-empty")
        self._candidates.append(Candidate(left, right, confidence, source))
        self._rebuild()

    def add_counterexample(self, left: str, right: str, source: str) -> None:
        self._require_instances(left, right)
        if left == right:
            raise ValueError("an instance cannot be a counterexample to itself")
        if not source.strip():
            raise ValueError("source must be non-empty")
        self._counterexamples.append(Counterexample(left, right, source))
        self._rebuild()

    def concept_of(self, key: str) -> frozenset[str]:
        self._require_instances(key)
        return self._groups[key]

    def equivalent(self, left: str, right: str) -> bool:
        self._require_instances(left, right)
        return self._groups[left] == self._groups[right]

    def concepts(self) -> tuple[frozenset[str], ...]:
        unique = set(self._groups.values())
        return tuple(sorted(unique, key=lambda group: tuple(sorted(group))))

    def residual(self, key: str) -> Any:
        """Return the original payload; abstraction never destroys it."""
        self._require_instances(key)
        return self._instances[key].payload

    def _require_instances(self, *keys: str) -> None:
        for key in keys:
            if key not in self._instances:
                raise UnknownInstance(key)

    def _rebuild(self) -> None:
        parent = {key: key for key in self._instances}
        members = {key: {key} for key in self._instances}

        def find(key: str) -> str:
            while parent[key] != key:
                parent[key] = parent[parent[key]]
                key = parent[key]
            return key

        def blocker(root_a: str, root_b: str) -> Counterexample | None:
            for item in self._counterexamples:
                a, b = find(item.left), find(item.right)
                if {a, b} == {root_a, root_b}:
                    return item
            return None

        rejected: list[RejectedCandidate] = []
        ordered = sorted(
            self._candidates,
            key=lambda item: (-item.confidence, item.left, item.right, item.source),
        )
        for candidate in ordered:
            root_a, root_b = find(candidate.left), find(candidate.right)
            if root_a == root_b:
                continue
            conflict = blocker(root_a, root_b)
            if conflict is not None:
                rejected.append(RejectedCandidate(candidate, conflict))
                continue

            # Deterministic representative: lexicographically smaller root.
            keep, drop = sorted((root_a, root_b))
            parent[drop] = keep
            members[keep].update(members.pop(drop))

        groups_by_root = {root: frozenset(group) for root, group in members.items()}
        self._groups = {
            key: groups_by_root[find(key)] for key in self._instances
        }
        self._rejected = tuple(rejected)


def _self_test() -> None:
    learner = ConceptLearner("same physical length")
    learner.add_instance("one_m", {"value": 1, "unit": "m"})
    learner.add_instance("hundred_cm", {"value": 100, "unit": "cm"})
    learner.add_instance("red", {"colour": "red", "length_m": 1})
    learner.propose_equivalence("one_m", "hundred_cm", 0.99, "unit conversion")
    assert learner.equivalent("one_m", "hundred_cm")
    assert not learner.equivalent("one_m", "red")

    # The counterexample revises the partition; raw observations remain.
    learner.propose_equivalence("hundred_cm", "red", 0.60, "shared numeral")
    assert learner.equivalent("one_m", "red")
    learner.add_counterexample("one_m", "red", "colour is not length")
    assert not learner.equivalent("one_m", "red")
    assert learner.equivalent("one_m", "hundred_cm")
    assert learner.residual("hundred_cm") == {"value": 100, "unit": "cm"}
    assert learner.rejected_candidates


if __name__ == "__main__":
    _self_test()
    print("concept learner self-test passed")
