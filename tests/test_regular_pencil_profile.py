import unittest

from tools.regular_pencil_profile import (
    compare_regular_pencils, regular_pencil_similarity_profile,
)


class RegularPencilProfileTests(unittest.TestCase):
    def test_identity_coefficient_recovers_operator_profile(self):
        result = regular_pencil_similarity_profile(
            [[1, 0], [0, 1]], [[0, 1], [0, 0]], 5
        )
        self.assertEqual(result["normalized_operator"], [[0, 1], [0, 0]])
        self.assertEqual(
            result["operator_rational_canonical_profile"]
                ["invariant_factors_coefficients_descending"],
            [[1, 0, 0]],
        )
        self.assertTrue(result["complete_strict_equivalence_fingerprint_in_Q_invertible_chart"])

    def test_nonidentity_q_is_normalized_exactly(self):
        result = regular_pencil_similarity_profile(
            [[1, 1], [0, 1]], [[2, 0], [1, 3]], 5
        )
        self.assertEqual(result["normalized_operator"], [[1, 2], [1, 3]])

    def test_strictly_equivalent_pairs_compare_equal(self):
        q = [[1, 0], [0, 1]]
        k = [[1, 1], [0, 2]]
        # S and T are invertible; apply the same pair of basis changes.
        s = [[1, 1], [0, 1]]
        t = [[1, 0], [1, 1]]
        def mm(a, b):
            return [[sum(a[i][r] * b[r][j] for r in range(2)) % 5
                     for j in range(2)] for i in range(2)]
        q2, k2 = mm(mm(s, q), t), mm(mm(s, k), t)
        result = compare_regular_pencils(q, k, q2, k2, 5)
        self.assertTrue(result["strictly_equivalent"])

    def test_same_dimension_but_different_similarity_classes(self):
        result = compare_regular_pencils(
            [[1, 0], [0, 1]], [[1, 0], [0, 1]],
            [[1, 0], [0, 1]], [[1, 1], [0, 1]], 5
        )
        self.assertFalse(result["strictly_equivalent"])

    def test_rejects_singular_q_and_nonsquare_inputs(self):
        with self.assertRaises(ValueError):
            regular_pencil_similarity_profile([[1, 0], [0, 0]], [[0, 0], [0, 1]], 5)
        with self.assertRaises(ValueError):
            regular_pencil_similarity_profile([[1, 0, 0]], [[0, 1, 0]], 5)

    def test_rejects_composite_modulus(self):
        with self.assertRaises(ValueError):
            regular_pencil_similarity_profile([[1]], [[2]], 4)


if __name__ == "__main__":
    unittest.main()
