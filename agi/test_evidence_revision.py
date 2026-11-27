"""Tests for append-only evidence feedback and hypothesis revision."""
import unittest
from fractions import Fraction

from agi.evidence_revision import EvidenceLedger
from agi.relation_composition import ComposedRelation
from agi.relation_selection import RelationCandidate


def affine(a, b):
    return ComposedRelation((Fraction(a), Fraction(b), Fraction(0), Fraction(1)))


class EvidenceRevisionTests(unittest.TestCase):
    def test_observation_retains_consistent_and_refutes_inconsistent(self):
        candidates = (
            RelationCandidate("identity", (affine(1, 0),)),
            RelationCandidate("double", (affine(2, 0),)),
        )
        old = EvidenceLedger()
        result = old.append(3, 3, candidates, "obs-1")
        self.assertEqual([x.candidate_id for x in result.retained_candidates], ["identity"])
        self.assertEqual(result.refuted_candidates, ("double",))
        self.assertEqual(old.records, ())
        self.assertEqual(result.history[0].assessments[1].predicted_output, Fraction(6))

    def test_undefined_candidate_is_refuted_with_reason(self):
        inverse = ComposedRelation((0, 1, 1, 0), (Fraction(0),))
        candidate = RelationCandidate("inverse", (inverse,))
        result = EvidenceLedger().append(0, 1, (candidate,), "zero")
        self.assertEqual(result.refuted_candidates, ("inverse",))
        self.assertEqual(result.history[0].assessments[0].status, "undefined_on_observation")

    def test_new_affine_hypothesis_proposed_from_accumulated_evidence(self):
        ledger = EvidenceLedger()
        first = ledger.append(0, 1, (), "a")
        second_ledger = EvidenceLedger(first.history)
        second = second_ledger.append(1, 3, (), "b")
        third_ledger = EvidenceLedger(second.history)
        third = third_ledger.append(2, 5, (), "c")
        affine_candidates = [c for c in third.proposed_candidates
                             if c.candidate_id.startswith("revision-affine")]
        self.assertEqual(len(affine_candidates), 1)
        self.assertEqual(affine_candidates[0].composed.evaluate(4), Fraction(9))

    def test_duplicate_evidence_key_rejected(self):
        ledger = EvidenceLedger().append(1, 2, (), "same")
        with self.assertRaises(ValueError):
            EvidenceLedger(ledger.history).append(2, 4, (), "same")

    def test_exact_values_only(self):
        with self.assertRaises(TypeError):
            EvidenceLedger().append(0.5, 1, (), "float")
        with self.assertRaises(TypeError):
            EvidenceLedger().append(True, 1, (), "bool")

    def test_candidate_ids_must_be_unique(self):
        one = RelationCandidate("dup", (affine(1, 0),))
        two = RelationCandidate("dup", (affine(2, 0),))
        with self.assertRaises(ValueError):
            EvidenceLedger().append(1, 1, (one, two), "obs")

    def test_prior_prediction_records_are_immutable(self):
        candidate = RelationCandidate("identity", (affine(1, 0),))
        ledger = EvidenceLedger()
        first = ledger.append(2, 2, (candidate,), "first")
        second = EvidenceLedger(first.history).append(3, 4, (candidate,), "second")
        self.assertEqual(first.history[0].assessments[0].predicted_output, Fraction(2))
        self.assertEqual(second.history[0].assessments[0].predicted_output, Fraction(2))
        self.assertEqual(second.history[1].assessments[0].predicted_output, Fraction(3))


if __name__ == "__main__":
    unittest.main()
