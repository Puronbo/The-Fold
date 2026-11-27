import unittest

from tools.prime_recurrence_comparison import compare_spiral_arithmetic_recurrence


class PrimeRecurrenceComparisonTests(unittest.TestCase):
    def test_geometry_and_arithmetic_channels_are_reported_separately(self):
        result = compare_spiral_arithmetic_recurrence(
            [3, 5, 7, 11], omega=0.0, residue_moduli=[2, 3],
            angle_tolerance=0.0, radial_relative_tolerance=1.0,
            gap_relative_tolerance=0.0,
        )
        self.assertEqual(result["pair_count"], 6)
        self.assertEqual(result["match_counts"]["geometric"], 6)
        # Supplied-list gaps are [None, 2, 2, 4], so exactly one pair matches.
        self.assertEqual(result["match_counts"]["gap"], 1)
        # 5 and 11 share residues modulo both 2 and 3.
        self.assertEqual(result["match_counts"]["residue"], 1)
        pair = next(p for p in result["pairwise_results"] if p["prime_labels"] == [5, 11])
        self.assertTrue(pair["geometric_recurrence"])
        self.assertFalse(pair["gap_recurrence"])
        self.assertTrue(pair["residue_recurrence"])

    def test_spectral_recurrence_is_matrix_relative(self):
        result = compare_spiral_arithmetic_recurrence(
            [3, 5, 7], omega=0.0, residue_moduli=[2],
            angle_tolerance=0.0, radial_relative_tolerance=1.0,
            matrix=[[0, -1], [1, 0]],
        )
        pair = next(p for p in result["pairwise_results"] if p["prime_labels"] == [3, 7])
        self.assertTrue(pair["spectral_recurrence"])
        self.assertIn("spectral", result["match_counts"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            compare_spiral_arithmetic_recurrence([], 0.1, [2])
        with self.assertRaises(ValueError):
            compare_spiral_arithmetic_recurrence([3, 2], 0.1, [2])
        with self.assertRaises(ValueError):
            compare_spiral_arithmetic_recurrence([3, 5], float("nan"), [2])
        with self.assertRaises(ValueError):
            compare_spiral_arithmetic_recurrence([3, 5], 0.1, [1])
        with self.assertRaises(ValueError):
            compare_spiral_arithmetic_recurrence([3, 5], 0.1, [2], angle_tolerance=4)


if __name__ == "__main__":
    unittest.main()
