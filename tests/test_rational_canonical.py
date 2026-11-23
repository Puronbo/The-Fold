import unittest

from tools.rational_canonical import rational_canonical_profile


class RationalCanonicalTests(unittest.TestCase):
    def test_identity_has_repeated_linear_invariant_factors(self):
        result = rational_canonical_profile([[1, 0], [0, 1]], 5)
        self.assertEqual(result["invariant_factors_coefficients_descending"],
                         [[4, 1], [4, 1]])
        self.assertTrue(result["similarity_class_complete_over_base_field"])

    def test_companion_of_x_squared_plus_one_is_cyclic(self):
        result = rational_canonical_profile([[0, -1], [1, 0]], 3)
        self.assertEqual(result["invariant_factors_coefficients_descending"],
                         [[1, 0, 1]])
        self.assertEqual(
            result["irreducible_primary_components"][0]
                ["elementary_divisor_exponents_descending"], [1]
        )

    def test_nilpotent_jordan_blocks_recovered(self):
        # J_3(0) direct sum J_1(0): elementary divisors x^3 and x.
        matrix = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        result = rational_canonical_profile(matrix, 2)
        primary = result["irreducible_primary_components"][0]
        self.assertEqual(primary["elementary_divisor_exponents_descending"],
                         [3, 1])
        self.assertEqual(result["invariant_factors_coefficients_descending"],
                         [[0, 1], [0, 0, 0, 1]])

    def test_similar_matrices_have_same_invariant_factors(self):
        a = [[1, 1], [0, 2]]
        # P=[[1,1],[1,0]], P^-1 exists over F_5.
        p = 5
        pinv = [[0, 1], [1, 4]]
        def mm(x, y):
            return [[sum(x[i][k] * y[k][j] for k in range(2)) % p
                     for j in range(2)] for i in range(2)]
        conjugate = mm(mm(pinv, a), [[0, 1], [1, 4]]) # P^-1 A P, P=P^-1 here
        left = rational_canonical_profile(a, p)
        right = rational_canonical_profile(conjugate, p)
        self.assertEqual(left["invariant_factors_coefficients_descending"],
                         right["invariant_factors_coefficients_descending"])

    def test_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            rational_canonical_profile([[1, 2]], 5)
        with self.assertRaises(ValueError):
            rational_canonical_profile([[1]], 4)


if __name__ == "__main__":
    unittest.main()
