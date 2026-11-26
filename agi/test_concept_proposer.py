"""Tests for deterministic unit-aware concept proposal generation."""

import unittest
from decimal import Decimal
from fractions import Fraction

from agi.concept_learner import ConceptLearner
from agi.concept_proposer import UnitQuantityProposer, parse_quantity


class UnitQuantityProposerTests(unittest.TestCase):
    def setUp(self):
        self.learner = ConceptLearner("physical quantity equality")
        self.learner.add_instance("one_metre", {"value": 1, "unit": "m"})
        self.learner.add_instance("hundred_cm", {"value": 100, "unit": "cm"})
        self.learner.add_instance("thousand_mm", {"value": 1000, "unit": "mm"})
        self.learner.add_instance("one_second", {"value": 1, "unit": "s"})
        self.learner.add_instance("one_kg", {"value": 1, "unit": "kg"})
        self.learner.add_instance("one_thousand_g", {"value": 1000, "unit": "g"})
        self.proposer = UnitQuantityProposer()

    def test_discovers_equivalence_from_observations(self):
        batch = self.proposer.apply(self.learner)
        self.assertTrue(self.learner.equivalent("one_metre", "hundred_cm"))
        self.assertTrue(self.learner.equivalent("hundred_cm", "thousand_mm"))
        self.assertEqual(len(batch.equivalences), 4)

    def test_discovers_hard_negative_across_dimensions(self):
        batch = self.proposer.apply(self.learner)
        self.assertFalse(self.learner.equivalent("one_metre", "one_second"))
        self.assertTrue(any(
            {item.left, item.right} == {"one_metre", "one_second"}
            for item in batch.counterexamples
        ))

    def test_equal_mass_in_different_units_is_equivalent(self):
        self.proposer.apply(self.learner)
        self.assertTrue(self.learner.equivalent("one_kg", "one_thousand_g"))

    def test_decimal_and_fraction_are_exact(self):
        self.assertEqual(
            parse_quantity({"value": Decimal("0.1"), "unit": "m"}).base_value,
            Fraction(1, 10),
        )
        self.assertEqual(
            parse_quantity({"value": Fraction(1, 10), "unit": "m"}).base_value,
            Fraction(1, 10),
        )

    def test_unknown_units_and_inexact_floats_are_skipped(self):
        self.assertIsNone(parse_quantity({"value": 1, "unit": "parsec"}))
        self.assertIsNone(parse_quantity({"value": 0.1, "unit": "m"}))
        self.assertIsNone(parse_quantity({"value": True, "unit": "m"}))
        self.assertIsNone(parse_quantity({"value": Decimal("NaN"), "unit": "m"}))
        self.assertIsNone(parse_quantity({"value": Decimal("Infinity"), "unit": "m"}))

    def test_malformed_payload_is_skipped(self):
        self.assertIsNone(parse_quantity(["1", "m"]))
        self.assertIsNone(parse_quantity({"value": "1", "unit": "m"}))

    def test_refuses_wrong_task_context(self):
        other = ConceptLearner("visual similarity")
        other.add_instance("a", {"value": 1, "unit": "m"})
        with self.assertRaises(ValueError):
            self.proposer.propose(other)

    def test_invalid_observations_do_not_create_proposals(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("a", {"value": 1.0, "unit": "m"})
        learner.add_instance("b", {"value": 100, "unit": "cm"})
        batch = self.proposer.propose(learner)
        self.assertEqual(batch.equivalences, ())
        self.assertEqual(batch.counterexamples, ())


if __name__ == "__main__":
    unittest.main()
