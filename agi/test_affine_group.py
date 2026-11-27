"""Tests for finite affine group recognition."""
import unittest
from fractions import Fraction as F

from agi.representation_transfer import AffineRelationConcept as Law
from agi.affine_group import recognize_finite_affine_group


class AffineGroupTests(unittest.TestCase):
    def test_trivial_group(self):
        result = recognize_finite_affine_group((("e", Law(1, 0)),))
        self.assertTrue(result.is_group)
        self.assertEqual(result.order, 1)
        self.assertEqual(result.identity_key, "e")

    def test_two_element_reflection_group(self):
        # r(x)=-x; r composed with itself is identity.
        result = recognize_finite_affine_group((
            ("e", Law(1, 0)), ("r", Law(-1, 0)),
        ))
        self.assertTrue(result.is_group)
        self.assertEqual(result.order, 2)
        self.assertIn(("r", "r"), result.inverse_pairs)

    def test_missing_identity(self):
        result = recognize_finite_affine_group((("r", Law(-1, 0)),))
        self.assertFalse(result.is_group)
        self.assertFalse(result.identity_present)

    def test_not_closed_under_composition(self):
        result = recognize_finite_affine_group((
            ("e", Law(1, 0)), ("r", Law(-1, 0)), ("t", Law(1, 1)),
        ))
        self.assertFalse(result.is_group)
        self.assertFalse(result.closure_holds)
        self.assertTrue(result.missing_compositions)

    def test_missing_inverse(self):
        result = recognize_finite_affine_group((
            ("e", Law(1, 0)), ("f", Law(2, 0)),
        ))
        self.assertFalse(result.is_group)
        self.assertFalse(result.inverses_present)
        self.assertEqual(result.missing_inverses[0][0], "f")

    def test_non_bijective_map_rejected(self):
        result = recognize_finite_affine_group((
            ("e", Law(1, 0)), ("constant", Law(0, 3)),
        ))
        self.assertFalse(result.is_group)
        self.assertFalse(result.all_elements_invertible)

    def test_exact_fractional_group(self):
        # h(x) = -x + 2 is an involution.
        result = recognize_finite_affine_group((
            ("e", Law(1, 0)), ("h", Law(-1, 2)),
        ))
        self.assertTrue(result.is_group)

    def test_empty_set_is_not_group(self):
        result = recognize_finite_affine_group(())
        self.assertFalse(result.is_group)
        self.assertEqual(result.status, "insufficient_transformations")

    def test_duplicate_keys_and_maps_rejected(self):
        with self.assertRaises(ValueError):
            recognize_finite_affine_group((("x", Law(1, 0)), ("x", Law(-1, 0))))
        with self.assertRaises(ValueError):
            recognize_finite_affine_group((("x", Law(1, 0)), ("y", Law(1, 0))))

    def test_non_group_reports_absent_inverse_exactly(self):
        result = recognize_finite_affine_group((
            ("e", Law(1, 0)), ("a", Law(F(2, 3), F(1, 7))),
        ))
        self.assertFalse(result.is_group)
        self.assertEqual(result.missing_inverses[0][2], repr((F(3, 2), F(-3, 14))))


if __name__ == "__main__":
    unittest.main()
