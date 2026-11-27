"""Evidence-based comparison of competing composed relational paths."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence
from agi.relation_composition import ComposedRelation
from agi.relation_validation import ValidationObservation, validate_composed_path


@dataclass(frozen=True)
class RelationCandidate:
    candidate_id: str
    steps: tuple[ComposedRelation, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.candidate_id, str) or not self.candidate_id.strip():
            raise ValueError("candidate_id must be non-empty")
        if not self.steps:
            raise ValueError("candidate must contain at least one relation step")

    @property
    def complexity(self) -> int:
        """Transparent description-length proxy, not a universal complexity measure."""
        coefficient_cost = sum(sum(value != 0 for value in step.coefficients) for step in self.steps)
        exclusion_cost = sum(len(step.domain_exclusions) for step in self.steps)
        return coefficient_cost + exclusion_cost + len(self.steps)

    @property
    def composed(self) -> ComposedRelation:
        result = self.steps[0]
        for step in self.steps[1:]:
            result = result.then(step)
        return result


@dataclass(frozen=True)
class CandidateScore:
    candidate_id: str
    status: str
    checked_rows: int
    output_matches: int
    output_mismatches: int
    intermediate_checks: int
    intermediate_matches: int
    intermediate_mismatches: int
    domain_failures: int
    complexity: int
    equivalent_group: str

    @property
    def accuracy(self) -> Fraction | None:
        return None if self.checked_rows == 0 else Fraction(self.output_matches, self.checked_rows)


@dataclass(frozen=True)
class CandidateComparison:
    status: str
    scores: tuple[CandidateScore, ...]
    ranking: tuple[str, ...]
    equivalence_groups: tuple[tuple[str, ...], ...]
    validation_rows: int


def _signature(candidate: RelationCandidate) -> tuple[object, ...]:
    composed = candidate.composed
    return (composed.coefficients, composed.domain_exclusions)


def compare_relation_candidates(candidates: Sequence[RelationCandidate],
                                observations: Sequence[ValidationObservation]) -> CandidateComparison:
    """Score fixed candidates on identical held-out rows; do not refit candidates."""
    if not candidates:
        raise ValueError("at least one candidate is required")
    ids = [candidate.candidate_id for candidate in candidates]
    if len(set(ids)) != len(ids):
        raise ValueError("candidate IDs must be unique")
    if not observations:
        return CandidateComparison("insufficient_validation_data", (), (), (), 0)
    # Candidate equivalence means identical exact composed function and identical
    # excluded input set; different derivations are grouped but not discarded.
    grouped: dict[tuple[object, ...], list[str]] = {}
    for candidate in candidates:
        grouped.setdefault(_signature(candidate), []).append(candidate.candidate_id)
    groups = tuple(tuple(sorted(members)) for members in grouped.values())
    group_for = {member: f"eq-{index + 1}" for index, members in enumerate(groups) for member in members}
    scores = []
    for candidate in candidates:
        report = validate_composed_path(candidate.steps, observations)
        domain_failures = sum(row.error is not None for row in report.rows)
        scores.append(CandidateScore(
            candidate.candidate_id, report.status, report.checked_rows,
            report.output_matches, report.output_mismatches,
            report.intermediate_checks, report.intermediate_matches,
            report.intermediate_mismatches, domain_failures,
            candidate.complexity, group_for[candidate.candidate_id]))
    # Primary evidence: endpoint errors, then supplied intermediate errors.
    # Only then prefer lower explicit complexity. Ties remain tied in score data.
    scores.sort(key=lambda score: (score.output_mismatches, score.intermediate_mismatches,
                                   score.complexity, score.candidate_id))
    return CandidateComparison("compared_on_independent_observations", tuple(scores),
                               tuple(score.candidate_id for score in scores),
                               groups, len(observations))
