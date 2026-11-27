"""Tests for affine concept transfer across coordinate representations."""
import unittest
from fractions import Fraction

from agi.representation_transfer import (
    AffineCoordinateMap, AffineRelationConcept, PairedObservation,
    transfer_affine_concept,
)


class RepresentationTransferTests(unittest.TestCase):
    def setUp(self):
        self.concept = AffineRelationConcept(Fraction(2), Fraction(3))
        self.rows = (
            PairedObservation.create("r1", 0, 3),
            PairedObservation.create("r2", 1, 5),
            PairedObservation.create("r3", 4, 11),
        )

    def test_transfer_between_scaled_and_shifted_coordinates(self):
        result = transfer_affine_concept(
            self.concept,
            AffineCoordinateMap(Fraction(10), Fraction(5)),
            AffineCoordinateMap(Fraction(1, 100), Fraction(-2)),
            self.rows,
        )
        self.assertEqual(result.concept.slope, Fraction(1, 500))
        self.assertEqual(result.concept.intercept, Fraction(-99, 50))
        self.assertEqual(result.status, "transferred")
        self.assertTrue(result.invariant_preserved)

    def test_zero_residual_stays_zero(self):
        result = transfer_affine_concept(
            self.concept, AffineCoordinateMap(3, 7),
            AffineCoordinateMap(5, -4), self.rows,
        )
        self.assertTrue(all(value == 0 for _, value in result.source_zero_residuals))
        self.assertTrue(all(value == 0 for _, value in result.target_zero_residuals))

    def test_nonzero_residual_scales_but_does_not_become_zero(self):
        rows = (PairedObservation.create("bad", 1, 6),)
        result = transfer_affine_concept(
            self.concept, AffineCoordinateMap(2, 9),
            AffineCoordinateMap(-3, 4), rows,
        )
        source = result.source_zero_residuals[0][1]
        target = result.target_zero_residuals[0][1]
        self.assertEqual(source, 1)
        self.assertEqual(target, -3)
        self.assertNotEqual(target, 0)

    def test_round_trip_coordinate_conversion(self):
        transform = AffineCoordinateMap(Fraction(3, 2), Fraction(-7, 4))
        for value in (Fraction(-2), Fraction(0), Fraction(5, 3)):
            self.assertEqual(transform.inverse(transform.forward(value)), value)

    def test_transferred_prediction_matches_mapped_observation(self):
        result = transfer_affine_concept(
            self.concept, AffineCoordinateMap(4, 2),
            AffineCoordinateMap(7, -3), self.rows,
        )
        for row in result.transformed_observations:
            self.assertEqual(result.concept.predict(row.x), row.y)

    def test_rejects_noninvertible_coordinate_map(self):
        with self.assertRaises(ValueError):
            AffineCoordinateMap(0, 1)

    def test_rejects_float_and_boolean(self):
        with self.assertRaises(TypeError):
            AffineCoordinateMap(0.5, 1)
        with self.assertRaises(TypeError):
            AffineRelationConcept(True, 0)

    def test_duplicate_observation_keys_rejected(self):
        duplicate = (self.rows[0], self.rows[0])
        with self.assertRaises(ValueError):
            transfer_affine_concept(
                self.concept, AffineCoordinateMap(1, 0),
                AffineCoordinateMap(1, 0), duplicate,
            )

    def test_negative_coordinate_scale_is_valid(self):
        result = transfer_affine_concept(
            self.concept, AffineCoordinateMap(-2, 1),
            AffineCoordinateMap(-3, 4), self.rows,
        )
        self.assertEqual(result.concept.slope, Fraction(3))
        self.assertTrue(result.invariant_preserved)


if __name__ == "__main__":
    unittest.main()
