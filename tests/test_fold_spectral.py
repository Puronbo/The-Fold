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

    def test_rejects_zero_vector_and_invalid_modulus(self):
        self.assertFalse(verify_quarter_turn_eigenpair(
            ModularEigenpair(0, (0, 0)), 5
        ))
        with self.assertRaises(ValueError):
            quarter_turn_eigenpairs(1)


if __name__ == "__main__":
    unittest.main()
