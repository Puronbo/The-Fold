"""Tests for exact affine invariant discovery and conjugacy."""
import unittest
from fractions import Fraction as F

from agi.representation_transfer import AffineCoordinateMap as Map, AffineRelationConcept as Law
from agi.invariant_discovery import (
    conjugate_affine_transformation, discover_affine_invariants,
    verify_affine_conjugacy,
)


class InvariantDiscoveryTests(unittest.TestCase):
    def test_multiplier_and_fixed_point_are_extracted(self):
        profile = discover_affine_invariants(Law(2, 3))
        self.assertEqual(profile.multiplier, 2)
        self.assertTrue(profile.has_unique_fixed_point)
        self.assertEqual(profile.fixed_point, -3)
        self.assertFalse(profile.is_identity)
        self.assertFalse(profile.is_nonzero_translation)

    def test_identity_has_every_point_fixed_not_unique(self):
        profile = discover_affine_invariants(Law(1, 0))
        self.assertTrue(profile.is_identity)
        self.assertFalse(profile.has_unique_fixed_point)
        self.assertIsNone(profile.fixed_point)

    def test_nonzero_translation_has_no_fixed_point(self):
        profile = discover_affine_invariants(Law(1, 7))
        self.assertTrue(profile.is_nonzero_translation)
        self.assertFalse(profile.has_unique_fixed_point)
        self.assertIsNone(profile.fixed_point)

    def test_conjugacy_preserves_multiplier_and_maps_fixed_point(self):
        source = Law(2, 3)
        phi = Map(5, -4)
        target = conjugate_affine_transformation(source, phi)
        report = verify_affine_conjugacy(source, target, phi)
        self.assertTrue(report.conjugate)
        self.assertEqual(target.slope, source.slope)
        self.assertEqual(report.expected_target_fixed_point, phi.forward(-3))
        self.assertTrue(report.fixed_point_covariant)

    def test_fractional_conjugacy_exact(self):
        source = Law(F(1, 3), F(2, 7))
        phi = Map(F(5, 2), F(-3, 4))
        target = conjugate_affine_transformation(source, phi)
        self.assertTrue(verify_affine_conjugacy(source, target, phi).conjugate)

    def test_nonconjugate_target_rejected(self):
        source = Law(2, 3)
        phi = Map(5, -4)
        target = Law(3, 1)
        report = verify_affine_conjugacy(source, target, phi)
        self.assertFalse(report.conjugate)
        self.assertEqual(report.status, "not_conjugate")

    def test_fixed_point_covariance_is_not_numeric_invariance(self):
        source = Law(2, 3)
        phi = Map(10, 5)
        target = conjugate_affine_transformation(source, phi)
        source_fixed = discover_affine_invariants(source).fixed_point
        target_fixed = discover_affine_invariants(target).fixed_point
        self.assertNotEqual(source_fixed, target_fixed)
        self.assertEqual(target_fixed, phi.forward(source_fixed))

    def test_translation_amount_changes_but_translation_class_survives(self):
        source = Law(1, 2)
        phi = Map(3, 7)
        target = conjugate_affine_transformation(source, phi)
        self.assertEqual(target, Law(1, 6))
        self.assertTrue(discover_affine_invariants(target).is_nonzero_translation)

    def test_coordinate_map_must_be_invertible(self):
        with self.assertRaises(ValueError):
            Map(0, 1)


if __name__ == "__main__":
    unittest.main()
