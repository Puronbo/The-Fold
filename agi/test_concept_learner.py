"""Unit tests for the task-scoped concept learner."""

import unittest

from agi.concept_learner import ConceptLearner, UnknownInstance


class ConceptLearnerTests(unittest.TestCase):
    def setUp(self):
        self.learner = ConceptLearner("length")
        self.learner.add_instance("m1", {"value": 1, "unit": "m"})
        self.learner.add_instance("cm100", {"value": 100, "unit": "cm"})
        self.learner.add_instance("cm200", {"value": 200, "unit": "cm"})
        self.learner.add_instance("red", {"colour": "red"})

    def test_equivalence_is_reflexive_symmetric_and_transitive(self):
        self.learner.propose_equivalence("m1", "cm100", 0.9, "unit conversion")
        self.learner.propose_equivalence("cm100", "cm200", 0.8, "same scale family")
        self.assertTrue(self.learner.equivalent("m1", "m1"))
        self.assertTrue(self.learner.equivalent("m1", "cm100"))
        self.assertTrue(self.learner.equivalent("cm100", "m1"))
        self.assertTrue(self.learner.equivalent("m1", "cm200"))

    def test_counterexample_splits_a_previous_class(self):
        self.learner.propose_equivalence("m1", "cm100", 0.9, "unit conversion")
        self.learner.propose_equivalence("cm100", "red", 0.4, "weak surface match")
        self.assertTrue(self.learner.equivalent("m1", "red"))
        self.learner.add_counterexample("m1", "red", "different semantic type")
        self.assertFalse(self.learner.equivalent("m1", "red"))
        self.assertTrue(self.learner.equivalent("m1", "cm100"))
        self.assertEqual(len(self.learner.rejected_candidates), 1)

    def test_stronger_evidence_wins_but_counterexample_is_respected(self):
        self.learner.propose_equivalence("m1", "cm100", 0.95, "conversion")
        self.learner.propose_equivalence("cm100", "red", 0.2, "surface match")
        self.learner.add_counterexample("m1", "red", "different type")
        self.assertTrue(self.learner.equivalent("m1", "cm100"))
        self.assertFalse(self.learner.equivalent("cm100", "red"))

    def test_payload_is_preserved_as_residual(self):
        payload = {"value": 100, "unit": "cm", "measurement_error": 0.1}
        self.learner.add_instance("extra", payload)
        self.assertEqual(self.learner.residual("extra"), payload)

    def test_unknown_instances_are_rejected(self):
        with self.assertRaises(UnknownInstance):
            self.learner.propose_equivalence("m1", "missing", 0.5, "bad evidence")

    def test_bad_confidence_is_rejected(self):
        with self.assertRaises(ValueError):
            self.learner.propose_equivalence("m1", "cm100", 1.5, "bad score")

    def test_context_is_required(self):
        with self.assertRaises(ValueError):
            ConceptLearner("  ")


if __name__ == "__main__":
    unittest.main()
