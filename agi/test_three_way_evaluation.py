"""Tests for strict three-way model evaluation."""
import unittest
from fractions import Fraction as F
from agi.relation_composition import ComposedRelation
from agi.relation_selection import RelationCandidate
from agi.relation_validation import ValidationObservation
from agi.three_way_evaluation import CandidateOrigin, run_three_way_protocol

class ThreeWayEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.discovery = (ValidationObservation.create("d1", 1, 3),
                          ValidationObservation.create("d2", 2, 5))
        self.validation = (ValidationObservation.create("v1", 3, 7),
                           ValidationObservation.create("v2", 4, 9))
        self.test = (ValidationObservation.create("t1", 5, 11),
                     ValidationObservation.create("t2", 6, 13))
        self.good = RelationCandidate("good", (ComposedRelation((F(2),F(1),F(0),F(1))),))
        self.bad = RelationCandidate("bad", (ComposedRelation((F(2),F(0),F(0),F(1))),))

    def test_validation_selects_then_test_evaluates_only_winner(self):
        origins = (CandidateOrigin(self.bad, ("d1",)), CandidateOrigin(self.good, ("d1","d2")))
        result = run_three_way_protocol(self.discovery, self.validation, self.test, origins)
        self.assertEqual(result.status, "evaluated_on_untouched_test_set")
        self.assertEqual(result.selected_candidate_id, "good")
        self.assertEqual(result.final_test_report.output_matches, 2)
        self.assertEqual(result.final_test_report.checked_rows, 2)

    def test_test_set_does_not_change_validation_selection(self):
        origins = (CandidateOrigin(self.good, ("d1",)), CandidateOrigin(self.bad, ("d2",)))
        altered_test = (ValidationObservation.create("t9", 100, -1),)
        first = run_three_way_protocol(self.discovery, self.validation, self.test, origins)
        second = run_three_way_protocol(self.discovery, self.validation, altered_test, origins)
        self.assertEqual(first.selected_candidate_id, second.selected_candidate_id)
        self.assertEqual(first.validation_comparison.ranking, second.validation_comparison.ranking)

    def test_partition_overlap_rejected(self):
        overlap = (ValidationObservation.create("d1", 3, 7),)
        with self.assertRaises(ValueError):
            run_three_way_protocol(self.discovery, overlap, self.test,
                                   (CandidateOrigin(self.good, ("d1",)),))

    def test_invalid_discovery_provenance_rejected(self):
        with self.assertRaises(ValueError):
            run_three_way_protocol(self.discovery, self.validation, self.test,
                                   (CandidateOrigin(self.good, ("v1",)),))

    def test_duplicate_candidate_ids_rejected(self):
        duplicate = RelationCandidate("good", self.bad.steps)
        with self.assertRaises(ValueError):
            run_three_way_protocol(self.discovery, self.validation, self.test,
                                   (CandidateOrigin(self.good, ("d1",)),
                                    CandidateOrigin(duplicate, ("d2",))))

    def test_missing_partition_returns_insufficient_without_winner(self):
        result = run_three_way_protocol(self.discovery, (), self.test,
                                        (CandidateOrigin(self.good, ("d1",)),))
        self.assertEqual(result.status, "insufficient_partition_data")
        self.assertIsNone(result.selected_candidate_id)
        self.assertIsNone(result.final_test_report)

    def test_candidate_requires_discovery_provenance(self):
        with self.assertRaises(ValueError):
            run_three_way_protocol(self.discovery, self.validation, self.test,
                                   (CandidateOrigin(self.good, ()),))

if __name__ == "__main__":
    unittest.main()