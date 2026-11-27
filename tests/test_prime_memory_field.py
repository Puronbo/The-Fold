import unittest
from fractions import Fraction

from tools.prime_memory_field import prime_memory_field


class PrimeMemoryFieldTests(unittest.TestCase):
    def test_three_layers_remain_separate(self):
        result = prime_memory_field(
            [3, 5, 7, 11], omega=0.0, residue_moduli=[2, 3],
            decay=Fraction(1, 2), angle_tolerance=0.0,
            radial_relative_tolerance=1.0, gap_relative_tolerance=0.0,
        )
        self.assertEqual(len(result["geometry"]["path"]), 4)
        self.assertEqual(result["arithmetic"]["path"][1]["gap_from_previous"], 2)
        self.assertEqual(result["geometry"]["recurrence_match_count"], 6)
        self.assertEqual(len(result["alignment"]["events"]), 2)
        self.assertEqual(
            result["alignment"]["channel_totals"]["geometry_gap_alignment"],
            {"numerator": 1, "denominator": 1},
        )
        self.assertEqual(
            result["alignment"]["channel_totals"]["geometry_residue_alignment"],
            {"numerator": 1, "denominator": 1},
        )
        self.assertEqual(
            result["alignment"]["memory"]["geometry_gap_alignment"],
            {"numerator": 1, "denominator": 4},
        )
        self.assertIn("shifts", result["controls"])

    def test_matrix_spectral_alignment_is_optional(self):
        result = prime_memory_field(
            [3, 5, 7], omega=0.0, residue_moduli=[2],
            decay=Fraction(1, 1), angle_tolerance=0.0,
            radial_relative_tolerance=1.0,
            matrix=[[0, -1], [1, 0]],
        )
        self.assertIn("geometry_spectral_alignment", result["alignment"]["channel_totals"])
        self.assertTrue(result["arithmetic"]["spectral_matrix_dependent"])

    def test_decay_validation(self):
        with self.assertRaises(ValueError):
            prime_memory_field([3, 5], 0.1, [2], decay=0.5)


if __name__ == "__main__":
    unittest.main()
