"""Tests for exact relational concept proposal generation."""
import unittest
from decimal import Decimal
from fractions import Fraction

from agi.relation_discovery import RelationalConceptProposer


class RelationalConceptTests(unittest.TestCase):
    def build(self, pairs):
        proposer = RelationalConceptProposer()
        for key, x, y in pairs:
            proposer.add_observation(key, x, y)
        return proposer.propose()

    def test_proportional_relation(self):
        result = self.build([("a", 1, 3), ("b", 2, 6), ("c", 4, 12)])
        prop = next(item for item in result if item.relation == "proportional")
        self.assertEqual(prop.parameters, (Fraction(3),))
        self.assertEqual(prop.status, "supported_on_supplied_observations")

    def test_inverse_relation(self):
        result = self.build([("a", 1, 12), ("b", 2, 6), ("c", 3, 4)])
        inverse = next(item for item in result if item.relation == "inverse")
        self.assertEqual(inverse.parameters, (Fraction(12),))
        self.assertFalse(inverse.counterexamples)

    def test_affine_relation_requires_three_rows_and_fits_exactly(self):
        proposer = RelationalConceptProposer()
        proposer.add_observation("a", 0, 5)
        proposer.add_observation("b", 1, 7)
        self.assertFalse(any(x.relation == "affine" for x in proposer.propose()))
        proposer.add_observation("c", 2, 9)
        affine = next(x for x in proposer.propose() if x.relation == "affine")
        self.assertEqual(affine.parameters, (Fraction(2), Fraction(5)))
        self.assertEqual(affine.status, "supported_on_supplied_observations")

    def test_counterexample_is_retained_and_reported(self):
        result = self.build([("a", 1, 2), ("b", 2, 4), ("c", 3, 8)])
        prop = next(item for item in result if item.relation == "proportional")
        self.assertEqual(prop.counterexamples, ("c",))
        self.assertEqual(prop.support, ("a", "b"))
        self.assertEqual(prop.status, "refuted")

    def test_zero_input_is_checked_for_proportionality(self):
        result = self.build([("a", 0, 0), ("b", 2, 6), ("c", 3, 9)])
        prop = next(item for item in result if item.relation == "proportional")
        self.assertFalse(prop.counterexamples)

    def test_inverse_law_rejects_zero_input(self):
        result = self.build([("a", 0, 0), ("b", 1, 4), ("c", 2, 2)])
        inverse = next(item for item in result if item.relation == "inverse")
        self.assertIn("a", inverse.counterexamples)

    def test_exact_decimal_and_float_rejection(self):
        proposer = RelationalConceptProposer()
        proposer.add_observation("a", Decimal("0.1"), Decimal("0.3"))
        proposer.add_observation("b", Decimal("0.2"), Decimal("0.6"))
        prop = next(x for x in proposer.propose() if x.relation == "proportional")
        self.assertEqual(prop.parameters, (Fraction(3),))
        with self.assertRaises(ValueError):
            proposer.add_observation("float", 0.1, 0.3)

    def test_duplicate_keys_and_invalid_values_are_rejected(self):
        proposer = RelationalConceptProposer()
        proposer.add_observation("a", 1, 2)
        with self.assertRaises(ValueError):
            proposer.add_observation("a", 2, 4)
        with self.assertRaises(ValueError):
            proposer.add_observation("bad", True, 2)

    def test_two_points_do_not_claim_affine_discovery(self):
        result = self.build([("a", 1, 4), ("b", 2, 7)])
        self.assertFalse(any(x.relation == "affine" for x in result))


if __name__ == "__main__":
    unittest.main()
