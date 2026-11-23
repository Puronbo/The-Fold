import unittest

from tools.spectral_fingerprint import (
    automatic_full_spectral_fingerprint, automatic_spectral_fingerprint,
    characteristic_polynomial, factor_polynomial,
    extension_jordan_profile, is_irreducible_polynomial,
    jordan_profile, rank_mod, spectral_fingerprint,
)


class SpectralFingerprintTests(unittest.TestCase):
    def test_rank_over_prime_field(self):
        self.assertEqual(rank_mod([[1, 2], [2, 1]], 3), 1)
        self.assertEqual(rank_mod([[1, 0], [0, 1]], 5), 2)

    def test_single_nilpotent_block_size_three(self):
        a = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
        result = jordan_profile(a, 5, 0)
        self.assertEqual(result["nullities"], [0, 1, 2, 3])
        self.assertEqual(result["blocks_exactly"], {"3": 1})
        self.assertEqual(result["block_sizes_descending"], [3])

    def test_partition_three_two_one(self):
        # Direct sum of nilpotent Jordan blocks of sizes 3, 2, and 1.
        a = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        result = jordan_profile(a, 7, 0)
        self.assertEqual(result["nullities"], [0, 3, 5, 6, 6])
        self.assertEqual(result["blocks_exactly"], {"1": 1, "2": 1, "3": 1})
        self.assertEqual(result["block_sizes_descending"], [3, 2, 1])

    def test_diagonalizable_repeated_eigenvalue(self):
        a = [[2, 0, 0], [0, 2, 0], [0, 0, 4]]
        result = jordan_profile(a, 5, 2)
        self.assertEqual(result["blocks_exactly"], {"1": 2})
        self.assertEqual(result["algebraic_multiplicity"], 2)
        self.assertEqual(result["geometric_multiplicity"], 2)

    def test_non_eigenvalue_has_empty_profile(self):
        result = jordan_profile([[0, 1], [0, 0]], 3, 1)
        self.assertEqual(result["nullities"], [0, 0])
        self.assertEqual(result["block_sizes_descending"], [])

    def test_ramified_cyclotomic_quarter_turn(self):
        # C_4 mod 2 has characteristic polynomial (x+1)^2 and one
        # Jordan block of size 2 at eigenvalue 1.
        a = [[0, 1], [1, 0]]
        result = jordan_profile(a, 2, 1)
        self.assertEqual(result["blocks_exactly"], {"2": 1})

    def test_validation(self):
        with self.assertRaises(ValueError):
            jordan_profile([[1, 2]], 5, 1)
        with self.assertRaises(ValueError):
            jordan_profile([[1]], 4, 1)

    def test_fingerprint_metadata(self):
        result = spectral_fingerprint([[1, 0], [0, 1]], 3, [1, 1, 2])
        self.assertEqual(result["field"], "F_3")
        self.assertEqual(len(result["profiles"]), 2)
        self.assertFalse(result["automatic_factorization"])

    def test_characteristic_polynomial_exact(self):
        self.assertEqual(characteristic_polynomial([[0, 1], [1, 0]], 5),
                         [1, 0, 4])
        self.assertEqual(characteristic_polynomial([[1, 0], [0, 1]], 2),
                         [1, 0, 1])

    def test_characteristic_polynomial_in_small_characteristic(self):
        # det(xI-A) = x^2 + 1 is irreducible over F_3.
        self.assertEqual(characteristic_polynomial([[0, 2], [1, 0]], 3),
                         [1, 0, 1])

    def test_automatic_base_field_scan_and_jordan_profile(self):
        result = automatic_spectral_fingerprint([[0, 1], [1, 0]], 2)
        self.assertEqual(
            result["characteristic_polynomial_coefficients_descending"],
            [1, 0, 1],
        )
        self.assertEqual(result["base_field_eigenvalues"],
                         [{"value": 1, "algebraic_multiplicity": 2}])
        self.assertEqual(result["profiles"][0]["blocks_exactly"], {"2": 1})

    def test_automatic_scan_can_find_no_base_field_eigenvalues(self):
        result = automatic_spectral_fingerprint([[0, 2], [1, 0]], 3)
        self.assertEqual(result["base_field_eigenvalues"], [])
        self.assertEqual(result["profiles"], [])
        self.assertTrue(result["irreducible_factorization_complete"])

    def test_berlekamp_factorization_irreducible_and_split(self):
        self.assertEqual(
            factor_polynomial([1, 0, 1], 3),
            [{"coefficients_descending": [1, 0, 1],
              "multiplicity": 1, "degree": 2}],
        )
        self.assertEqual(
            factor_polynomial([1, 0, 1], 5),
            [
                {"coefficients_descending": [1, 2],
                 "multiplicity": 1, "degree": 1},
                {"coefficients_descending": [1, 3],
                 "multiplicity": 1, "degree": 1},
            ],
        )

    def test_factorization_repeated_and_inseparable_factors(self):
        self.assertEqual(
            factor_polynomial([1, 0, 1], 2),
            [{"coefficients_descending": [1, 1],
              "multiplicity": 2, "degree": 1}],
        )
        self.assertEqual(
            factor_polynomial([1, 0, 1, 0, 1], 2),
            [{"coefficients_descending": [1, 1, 1],
              "multiplicity": 2, "degree": 2}],
        )

    def test_automatic_scan_includes_complete_factorization(self):
        result = automatic_spectral_fingerprint([[0, 2], [1, 0]], 3)
        self.assertTrue(result["irreducible_factorization_complete"])
        self.assertEqual(result["factorization"], [
            {"coefficients_descending": [1, 0, 1],
             "multiplicity": 1, "degree": 2},
        ])

    def test_rabin_irreducibility_over_prime_fields(self):
        self.assertTrue(is_irreducible_polynomial([1, 0, 1], 3))
        self.assertFalse(is_irreducible_polynomial([1, 0, 1], 5))
        self.assertTrue(is_irreducible_polynomial([1, 1, 1], 2))

    def test_extension_field_jordan_profile(self):
        # x^2+1 is irreducible over F_3. The companion matrix has
        # eigenvalue alpha in F_9, with a one-dimensional eigenspace.
        result = extension_jordan_profile(
            [[0, 2], [1, 0]], 3, [1, 0, 1], [0, 1]
        )
        self.assertEqual(result["field"], "F_9")
        self.assertEqual(result["base_field"], "F_3")
        self.assertEqual(result["extension_degree"], 2)
        self.assertEqual(result["nullities"], [0, 1, 1])
        self.assertEqual(result["blocks_exactly"], {"1": 1})
        self.assertEqual(result["block_sizes_descending"], [1])

    def test_extension_field_rejects_reducible_modulus(self):
        with self.assertRaises(ValueError):
            extension_jordan_profile([[0, 1], [1, 0]], 5,
                                     [1, 0, 1], [0, 1])

    def test_automatic_extension_eigenvalue_class(self):
        result = automatic_full_spectral_fingerprint([[0, 2], [1, 0]], 3)
        self.assertEqual(result["base_field_eigenvalues"], [])
        self.assertTrue(result["extension_classes_complete"])
        self.assertEqual(len(result["extension_eigenvalue_classes"]), 1)
        eigenclass = result["extension_eigenvalue_classes"][0]
        self.assertEqual(eigenclass["extension_degree"], 2)
        self.assertEqual(eigenclass["frobenius_conjugate_count"], 2)
        self.assertEqual(eigenclass["profile"]["blocks_exactly"], {"1": 1})


if __name__ == "__main__":
    unittest.main()
