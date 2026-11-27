"""Tests for exact pairwise affine relationship discovery."""
import unittest
from fractions import Fraction as F

from agi.representation_transfer import AffineRelationConcept as Law
from agi.affine_relationships import (
    analyze_affine_pair, compose_affine, discover_affine_relationships,
)


class AffineRelationshipTests(unittest.TestCase):
    def test_composition_respects_order(self):
        f, g = Law(2, 3), Law(5, 7)
        self.assertEqual(compose_affine(f, g), Law(10, 17))
        self.assertEqual(compose_affine(g, f), Law(10, 22))

    def test_two_translations_commute(self):
        result = analyze_affine_pair("f", Law(1, 2), "g", Law(1, 9))
        self.assertTrue(result.commute)
        self.assertEqual(result.commutator_offset, 0)
        self.assertTrue(result.same_fixed_point_set)  # both have empty fixed sets

    def test_same_fixed_point_maps_commute(self):
        # Both maps fix x=4.
        result = analyze_affine_pair("f", Law(2, -4), "g", Law(3, -8))
        self.assertEqual(result.shared_unique_fixed_point, F(4))
        self.assertTrue(result.commute)

    def test_noncommuting_maps_have_exact_commutator(self):
        result = analyze_affine_pair("f", Law(2, 3), "g", Law(5, 7))
        self.assertFalse(result.commute)
        self.assertEqual(result.commutator_offset, F(-5))
        self.assertTrue(result.composition_order_matters)

    def test_identical_fixed_point_set_detects_identity(self):
        result = analyze_affine_pair("id", Law(1, 0), "id2", Law(1, 0))
        self.assertTrue(result.same_fixed_point_set)
        self.assertIsNone(result.shared_unique_fixed_point)

    def test_identity_and_nonzero_translation_have_different_fixed_sets(self):
        result = analyze_affine_pair("id", Law(1, 0), "t", Law(1, 2))
        self.assertFalse(result.same_fixed_point_set)
        self.assertTrue(result.commute)

    def test_discovery_enumerates_each_unordered_pair(self):
        result = discover_affine_relationships((
            ("a", Law(1, 1)), ("b", Law(1, 2)), ("c", Law(2, 0)),
        ))
        self.assertEqual(len(result.relationships), 3)
        self.assertEqual(result.commuting_pairs, (("a", "b"),))
        self.assertEqual(result.noncommuting_pairs, (("a", "c"), ("b", "c")))

    def test_single_map_is_explicitly_insufficient(self):
        result = discover_affine_relationships((("only", Law(2, 1)),))
        self.assertEqual(result.status, "insufficient_transformations")
        self.assertEqual(result.relationships, ())

    def test_duplicate_and_blank_keys_rejected(self):
        with self.assertRaises(ValueError):
            discover_affine_relationships((("x", Law(1, 0)), ("x", Law(2, 0))))
        with self.assertRaises(ValueError):
            analyze_affine_pair(" ", Law(1, 0), "y", Law(2, 0))

    def test_fractional_coefficients_exact(self):
        result = analyze_affine_pair(
            "f", Law(F(1, 2), F(1, 3)),
            "g", Law(F(3, 2), F(-1, 4)),
        )
        self.assertEqual(result.commutator_offset, F(-1, 24))


if __name__ == "__main__":
    unittest.main()
