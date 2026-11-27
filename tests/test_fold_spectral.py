import unittest

from tools.FoldSpectral import (
    ModularEigenpair,
    quarter_turn_eigenpairs,
    verify_quarter_turn_eigenpair,
)


class FoldSpectralTests(unittest.TestCase):
    def test_mod_five_eigenvalue_and_eigenvector(self):
        pairs = quarter_turn_eigenpairs(5)
        self.assertEqual(
            pairs,
            (
                ModularEigenpair(2, (2, 1)),
                ModularEigenpair(3, (3, 1)),
            ),
        )
        self.assertTrue(all(verify_quarter_turn_eigenpair(pair, 5) for pair in pairs))

    def test_mod_thirteen_has_two_roots(self):
        pairs = quarter_turn_eigenpairs(13)
        self.assertEqual(tuple(pair.eigenvalue for pair in pairs), (5, 8))
        self.assertTrue(all(verify_quarter_turn_eigenpair(pair, 13) for pair in pairs))

    def test_mod_three_has_no_eigenvalues(self):
        self.assertEqual(quarter_turn_eigenpairs(3), ())

    def test_mod_two_has_one_eigenvalue(self):
        pairs = quarter_turn_eigenpairs(2)
        self.assertEqual(pairs, (ModularEigenpair(1, (1, 1)),))
        self.assertTrue(verify_quarter_turn_eigenpair(pairs[0], 2))

    def test_root_primes_up_to_30(self):
        from tools.FoldSpectral import quarter_turn_root_primes

        self.assertEqual(quarter_turn_root_primes(30), (2, 5, 13, 17, 29))
        self.assertEqual(quarter_turn_root_primes(1), ())
        with self.assertRaises(ValueError):
            quarter_turn_root_primes(-1)

    def test_cyclotomic_polynomials(self):
        from tools.FoldSpectral import cyclotomic_polynomial

        self.assertEqual(cyclotomic_polynomial(1), (-1, 1))
        self.assertEqual(cyclotomic_polynomial(4), (1, 0, 1))
        self.assertEqual(cyclotomic_polynomial(6), (1, -1, 1))
        self.assertEqual(cyclotomic_polynomial(8), (1, 0, 0, 0, 1))

    def test_general_cyclotomic_roots(self):
        from tools.FoldSpectral import (
            cyclotomic_root_primes,
            cyclotomic_root_residues,
        )

        self.assertEqual(cyclotomic_root_residues(3, 7), (2, 4))
        self.assertEqual(cyclotomic_root_residues(4, 5), (2, 3))
        self.assertEqual(cyclotomic_root_primes(3, 20), (3, 7, 13, 19))
        self.assertEqual(cyclotomic_root_primes(4, 20), (2, 5, 13, 17))
        with self.assertRaises(ValueError):
            cyclotomic_root_residues(4, 9)

    def test_cyclotomic_spectral_degrees(self):
        from tools.FoldSpectral import (
            cyclotomic_factor_count,
            cyclotomic_spectral_degree,
            multiplicative_order,
        )

        self.assertEqual(cyclotomic_spectral_degree(3, 2), 2)
        self.assertEqual(cyclotomic_spectral_degree(3, 7), 1)
        self.assertEqual(cyclotomic_spectral_degree(4, 3), 2)
        self.assertEqual(cyclotomic_spectral_degree(4, 5), 1)
        self.assertEqual(cyclotomic_factor_count(3, 2), 1)
        self.assertEqual(cyclotomic_factor_count(3, 7), 2)
        self.assertEqual(multiplicative_order(7, 3), 1)
        with self.assertRaises(ValueError):
            cyclotomic_spectral_degree(4, 2)

    def test_exact_cyclotomic_rotation_matrices(self):
        from tools.FoldSpectral import (
            cyclotomic_rotation_matrix,
            verify_cyclotomic_rotation_matrix,
        )

        self.assertEqual(
            cyclotomic_rotation_matrix(4),
            ((0, -1), (1, 0)),
        )
        self.assertEqual(
            cyclotomic_rotation_matrix(3),
            ((0, -1), (1, -1)),
        )
        for order in range(1, 13):
            self.assertTrue(verify_cyclotomic_rotation_matrix(order))

    def test_modular_cyclotomic_spectral_profiles(self):
        from tools.FoldSpectral import (
            cyclotomic_eigenvalue_multiplicities,
            cyclotomic_rotation_matrix_mod,
            cyclotomic_spectral_profile,
            verify_cyclotomic_spectral_profile,
        )

        self.assertEqual(
            cyclotomic_rotation_matrix_mod(4, 5),
            ((0, 4), (1, 0)),
        )
        self.assertEqual(
            cyclotomic_eigenvalue_multiplicities(4, 5),
            ((2, 1), (3, 1)),
        )
        self.assertEqual(
            cyclotomic_spectral_profile(4, 3),
            {
                "dimension": 2,
                "factor_degree": 2,
                "factor_count": 1,
                "base_field_eigenvalue_count": 0,
                "base_field_eigenspace_dimension_sum": 0,
            },
        )
        self.assertEqual(
            cyclotomic_spectral_profile(4, 5),
            {
                "dimension": 2,
                "factor_degree": 1,
                "factor_count": 2,
                "base_field_eigenvalue_count": 2,
                "base_field_eigenspace_dimension_sum": 2,
            },
        )
        for order, prime in ((3, 2), (3, 7), (4, 3), (4, 5), (5, 2), (8, 3)):
            self.assertTrue(verify_cyclotomic_spectral_profile(order, prime))
        with self.assertRaises(ValueError):
            cyclotomic_eigenvalue_multiplicities(4, 2)

    def test_explicit_cyclotomic_factorization(self):
        from tools.FoldSpectral import (
            cyclotomic_factorization_mod,
            verify_cyclotomic_factorization,
        )

        self.assertEqual(cyclotomic_factorization_mod(4, 3), ((1, 0, 1),))
        self.assertEqual(
            cyclotomic_factorization_mod(4, 5),
            ((2, 1), (3, 1)),
        )
        self.assertEqual(
            cyclotomic_factorization_mod(3, 2),
            ((1, 1, 1),),
        )
        self.assertEqual(
            cyclotomic_factorization_mod(3, 7),
            ((3, 1), (5, 1)),
        )
        self.assertEqual(
            cyclotomic_factorization_mod(5, 2),
            ((1, 1, 1, 1, 1),),
        )
        for order, prime in ((3, 2), (3, 7), (4, 3), (4, 5), (5, 2), (8, 3), (12, 5)):
            self.assertTrue(verify_cyclotomic_factorization(order, prime))
        with self.assertRaises(ValueError):
            cyclotomic_factorization_mod(4, 2)


    def test_factorization_matches_frobenius_degrees(self):
        from tools.FoldSpectral import (
            _is_irreducible_mod,
            cyclotomic_factorization_mod,
            cyclotomic_polynomial,
            cyclotomic_spectral_degree,
            verify_cyclotomic_factorization,
        )

        primes = (2, 3, 5, 7, 11, 13)
        for order in range(1, 25):
            for prime in primes:
                if order % prime == 0:
                    continue
                factors = cyclotomic_factorization_mod(order, prime)
                expected_degree = cyclotomic_spectral_degree(order, prime)
                self.assertTrue(verify_cyclotomic_factorization(order, prime))
                self.assertTrue(all(
                    len(factor) - 1 == expected_degree for factor in factors
                ))
                self.assertEqual(
                    len(factors) * expected_degree,
                    len(cyclotomic_polynomial(order)) - 1,
                )

        self.assertTrue(_is_irreducible_mod([1, 1, 1], 2))
        self.assertFalse(_is_irreducible_mod([1, 0, 1], 2))
        self.assertFalse(_is_irreducible_mod([1, 0, 0, 1], 2))

    def test_rejects_zero_vector_and_invalid_modulus(self):
        self.assertFalse(verify_quarter_turn_eigenpair(
            ModularEigenpair(0, (0, 0)), 5
        ))
        with self.assertRaises(ValueError):
            quarter_turn_eigenpairs(1)


if __name__ == "__main__":
    unittest.main()
