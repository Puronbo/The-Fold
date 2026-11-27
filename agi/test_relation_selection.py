"""Tests for competing relational candidate comparison."""
import unittest
from fractions import Fraction as F
from agi.relation_composition import ComposedRelation
from agi.relation_validation import ValidationObservation
from agi.relation_selection import RelationCandidate, compare_relation_candidates

class RelationSelectionTests(unittest.TestCase):
    def setUp(self):
        self.rows = (
            ValidationObservation.create("v1", 1, 3),
            ValidationObservation.create("v2", 2, 5),
            ValidationObservation.create("v3", 4, 9),
        )

    def test_correct_candidate_ranks_ahead_of_refuted(self):
        correct = RelationCandidate("correct", (ComposedRelation((F(2), F(1), F(0), F(1))),))
        wrong = RelationCandidate("wrong", (ComposedRelation((F(2), F(0), F(0), F(1))),))
        result = compare_relation_candidates((wrong, correct), self.rows)
        self.assertEqual(result.status, "compared_on_independent_observations")
        self.assertEqual(result.ranking[0], "correct")
        self.assertEqual(result.scores[0].output_mismatches, 0)

    def test_equivalent_paths_group_without_deleting_candidates(self):
        direct = RelationCandidate("direct", (ComposedRelation((F(1), F(1), F(0), F(1))),))
        split = RelationCandidate("split", (
            ComposedRelation((F(1), F(0), F(0), F(1))),
            ComposedRelation((F(1), F(1), F(0), F(1))),
        ))
        result = compare_relation_candidates((direct, split), self.rows)
        self.assertEqual(len(result.equivalence_groups), 1)
        self.assertEqual(set(result.equivalence_groups[0]), {"direct", "split"})
        self.assertEqual(len(result.scores), 2)

    def test_complexity_breaks_equal_evidence_tie(self):
        simple = RelationCandidate("simple", (ComposedRelation((F(1), F(1), F(0), F(1))),))
        redundant = RelationCandidate("redundant", (
            ComposedRelation((F(1), F(0), F(0), F(1))),
            ComposedRelation((F(1), F(1), F(0), F(1))),
        ))
        result = compare_relation_candidates((redundant, simple), self.rows)
        self.assertEqual(result.ranking[0], "simple")
        self.assertLess(result.scores[0].complexity, result.scores[1].complexity)

    def test_endpoint_accuracy_does_not_hide_intermediate_mismatch(self):
        path = RelationCandidate("bad-middle", (
            ComposedRelation((F(2), F(0), F(0), F(1))),
            ComposedRelation((F(1,2), F(0), F(0), F(1))),
        ))
        rows = (ValidationObservation.create("r", 2, 2, (3, 2)),)
        result = compare_relation_candidates((path,), rows)
        score = result.scores[0]
        self.assertEqual(score.output_matches, 1)
        self.assertEqual(score.intermediate_mismatches, 1)

    def test_domain_failure_counts_as_error(self):
        inverse = RelationCandidate("inverse", (ComposedRelation((F(0),F(1),F(1),F(0)), (F(0),)),))
        rows = (ValidationObservation.create("zero", 0, 0),)
        score = compare_relation_candidates((inverse,), rows).scores[0]
        self.assertEqual(score.domain_failures, 1)
        self.assertEqual(score.output_mismatches, 1)

    def test_empty_validation_and_invalid_candidates(self):
        candidate = RelationCandidate("id", (ComposedRelation((F(1),F(0),F(0),F(1))),))
        result = compare_relation_candidates((candidate,), ())
        self.assertEqual(result.status, "insufficient_validation_data")
        with self.assertRaises(ValueError):
            compare_relation_candidates((candidate, candidate), self.rows)
        with self.assertRaises(ValueError):
            RelationCandidate("empty", ())

if __name__ == "__main__":
    unittest.main()