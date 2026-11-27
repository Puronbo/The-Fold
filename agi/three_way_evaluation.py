"""Three-way discovery/validation/test protocol for relational candidates."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
from agi.relation_selection import RelationCandidate, CandidateComparison, compare_relation_candidates
from agi.relation_validation import ValidationObservation, ValidationReport, validate_composed_path

@dataclass(frozen=True)
class CandidateOrigin:
    candidate: RelationCandidate
    discovery_keys: tuple[str, ...]

@dataclass(frozen=True)
class ThreeWayResult:
    status: str
    selected_candidate_id: str | None
    validation_comparison: CandidateComparison | None
    final_test_report: ValidationReport | None
    discovery_rows: int
    validation_rows: int
    test_rows: int

def _unique_keys(rows: Sequence[ValidationObservation], label: str) -> set[str]:
    keys = [row.key for row in rows]
    if len(keys) != len(set(keys)):
        raise ValueError(f"{label} observation keys must be unique")
    return set(keys)

def run_three_way_protocol(discovery: Sequence[ValidationObservation],
                           validation: Sequence[ValidationObservation],
                           test: Sequence[ValidationObservation],
                           candidates: Sequence[CandidateOrigin]) -> ThreeWayResult:
    """Select using validation only, then evaluate only the frozen winner on test.

    Candidate construction is upstream and must use discovery observations only.
    `discovery_keys` is an auditable provenance declaration, not a proof that
    candidate parameters were honestly derived from those rows.
    """
    if not discovery or not validation or not test:
        return ThreeWayResult("insufficient_partition_data", None, None, None,
                              len(discovery), len(validation), len(test))
    dkeys = _unique_keys(discovery, "discovery")
    vkeys = _unique_keys(validation, "validation")
    tkeys = _unique_keys(test, "test")
    if dkeys & vkeys or dkeys & tkeys or vkeys & tkeys:
        raise ValueError("discovery, validation, and test keys must be disjoint")
    if not candidates:
        raise ValueError("at least one candidate is required")
    ids = [origin.candidate.candidate_id for origin in candidates]
    if len(ids) != len(set(ids)):
        raise ValueError("candidate IDs must be unique")
    for origin in candidates:
        if not origin.discovery_keys or len(origin.discovery_keys) != len(set(origin.discovery_keys)):
            raise ValueError("each candidate needs unique discovery provenance keys")
        if not set(origin.discovery_keys) <= dkeys:
            raise ValueError("candidate provenance must refer only to discovery rows")
    comparison = compare_relation_candidates(tuple(x.candidate for x in candidates), validation)
    if comparison.status != "compared_on_independent_observations" or not comparison.ranking:
        return ThreeWayResult("insufficient_validation_data", None, comparison, None,
                              len(discovery), len(validation), len(test))
    # Freeze selection before touching the final test observations.
    selected_id = comparison.ranking[0]
    selected = next(x.candidate for x in candidates if x.candidate.candidate_id == selected_id)
    final_report = validate_composed_path(selected.steps, test)
    return ThreeWayResult("evaluated_on_untouched_test_set", selected_id, comparison,
                          final_report, len(discovery), len(validation), len(test))
