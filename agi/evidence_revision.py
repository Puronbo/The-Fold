"""Append-only observation feedback and exact relational hypothesis revision."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from agi.relation_composition import ComposedRelation
from agi.relation_discovery import RelationalConceptProposer
from agi.relation_selection import RelationCandidate


@dataclass(frozen=True)
class Evidence:
    key: str
    input_value: Fraction
    observed_output: Fraction


@dataclass(frozen=True)
class CandidateAssessment:
    candidate_id: str
    predicted_output: Fraction | None
    status: str
    error: str | None


@dataclass(frozen=True)
class FeedbackRecord:
    evidence: Evidence
    assessments: tuple[CandidateAssessment, ...]


@dataclass(frozen=True)
class RevisionResult:
    status: str
    history: tuple[FeedbackRecord, ...]
    retained_candidates: tuple[RelationCandidate, ...]
    refuted_candidates: tuple[str, ...]
    proposed_candidates: tuple[RelationCandidate, ...]
    new_hypothesis_families: tuple[str, ...]


@dataclass(frozen=True)
class EvidenceLedger:
    """Immutable ledger: append returns a new ledger; prior records never mutate."""
    records: tuple[FeedbackRecord, ...] = ()

    @property
    def evidence_keys(self) -> tuple[str, ...]:
        return tuple(record.evidence.key for record in self.records)

    def append(
        self,
        input_value: int | Fraction,
        observed_output: int | Fraction,
        candidates: Sequence[RelationCandidate],
        key: str,
    ) -> RevisionResult:
        if not isinstance(key, str) or not key.strip():
            raise ValueError("evidence key must be non-empty")
        if key in self.evidence_keys:
            raise ValueError("evidence keys must be unique and append-only")
        if isinstance(input_value, bool) or not isinstance(input_value, (int, Fraction)):
            raise TypeError("input must be an exact integer or Fraction")
        if isinstance(observed_output, bool) or not isinstance(observed_output, (int, Fraction)):
            raise TypeError("observation must be an exact integer or Fraction")
        ids = [candidate.candidate_id for candidate in candidates]
        if len(ids) != len(set(ids)):
            raise ValueError("candidate IDs must be unique")
        evidence = Evidence(key, Fraction(input_value), Fraction(observed_output))
        assessments = []
        retained = []
        refuted = []
        for candidate in candidates:
            try:
                predicted = candidate.composed.evaluate(evidence.input_value)
                matches = predicted == evidence.observed_output
                assessments.append(CandidateAssessment(
                    candidate.candidate_id, predicted,
                    "consistent_with_observation" if matches else "refuted_by_observation",
                    None,
                ))
                (retained if matches else refuted).append(candidate)
            except (ZeroDivisionError, ValueError) as exc:
                assessments.append(CandidateAssessment(
                    candidate.candidate_id, None, "undefined_on_observation", str(exc)
                ))
                refuted.append(candidate)
        record = FeedbackRecord(evidence, tuple(assessments))
        new_history = self.records + (record,)

        # Re-propose only from the accumulated, explicitly supplied input/output
        # evidence. These are candidates, not silently accepted replacements.
        proposer = RelationalConceptProposer()
        for item in new_history:
            proposer.add_observation(item.evidence.key,
                                     item.evidence.input_value,
                                     item.evidence.observed_output)
        generated = []
        families = []
        for hypothesis in proposer.propose():
            if hypothesis.status != "supported_on_supplied_observations":
                continue
            relation = ComposedRelation.from_hypothesis(hypothesis)
            candidate_id = f"revision-{hypothesis.relation}-{len(new_history)}"
            if candidate_id not in ids:
                generated.append(RelationCandidate(candidate_id, (relation,)))
                families.append(hypothesis.relation)
        return RevisionResult(
            "evidence_appended",
            new_history,
            tuple(retained),
            tuple(candidate.candidate_id for candidate in refuted),
            tuple(generated),
            tuple(families),
        )
