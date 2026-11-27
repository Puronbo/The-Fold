import unittest
from fractions import Fraction

from tools.prime_memory_afterimage import prime_sensitive_memory_path


class PrimeMemoryAfterimageTests(unittest.TestCase):
    def test_lossless_path_and_exact_residue_gap_afterimage(self):
        result = prime_sensitive_memory_path(
            [2, 3, 5, 7], [2, 3, 5], decay=Fraction(1, 2)
        )
        self.assertEqual([r["prime"] for r in result["path"]], [2, 3, 5, 7])
        self.assertEqual(
            [r["gap_from_previous"] for r in result["path"]],
            [None, 1, 2, 2],
        )
        # Gap channel: ((0 * 1/2 + 1) * 1/2 + 2) * 1/2 + 2 = 13/4.
        self.assertEqual(
            result["afterimage"]["prime_gap"],
            {"numerator": 13, "denominator": 4},
        )
        self.assertFalse(result["spectral_matrix_dependent"])

    def test_matrix_dependent_frobenius_channels(self):
        result = prime_sensitive_memory_path(
            [3, 5, 7], [2, 3], matrix=[[0, -1], [1, 0]],
            decay=Fraction(0),
        )
        by_prime = {r["prime"]: r for r in result["path"]}
        self.assertEqual(
            by_prime[3]["spectral"]["frobenius_orbit_degree_histogram"],
            {"2": 2},
        )
        self.assertEqual(
            by_prime[5]["spectral"]["frobenius_orbit_degree_histogram"],
            {"1": 2},
        )
        self.assertTrue(result["spectral_matrix_dependent"])
        # Zero decay leaves exactly the last record's spectral features.
        self.assertEqual(
            result["afterimage"]["spectral_orbit_degree_1"],
            {"numerator": 2, "denominator": 1},
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            prime_sensitive_memory_path([2, 4], [3])
        with self.assertRaises(ValueError):
            prime_sensitive_memory_path([3, 2], [3])
        with self.assertRaises(ValueError):
            prime_sensitive_memory_path([2, 3], [1])
        with self.assertRaises(ValueError):
            prime_sensitive_memory_path([2, 3], [3], decay=Fraction(3, 2))


if __name__ == "__main__":
    unittest.main()
