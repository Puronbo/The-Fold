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
        self.assertEqual(result["chart"]["projective_point"], [1, 0])
        self.assertEqual(
            result["operator_rational_canonical_profile"]
                ["invariant_factors_coefficients_descending"],
            [[1, 0, 0]],
        )
        self.assertTrue(result["complete_strict_equivalence_fingerprint_in_chart"])

    def test_nonidentity_q_is_normalized_exactly(self):
        result = regular_pencil_similarity_profile(
            [[1, 1], [0, 1]], [[2, 0], [1, 3]], 5
        )
        self.assertEqual(result["normalized_operator"], [[1, 2], [1, 3]])

    def test_singular_q_uses_another_finite_projective_member(self):
        result = regular_pencil_similarity_profile(
            [[1, 0], [0, 0]], [[0, 0], [0, 1]], 5
        )
        self.assertEqual(result["chart"]["projective_point"], [1, 1])
        self.assertEqual(result["normalized_operator"], [[0, 0], [0, 1]])

    def test_singular_q_and_q_plus_k_can_fall_back_to_infinity(self):
        result = regular_pencil_similarity_profile(
            [[1, 0], [0, 0]], [[1, 0], [0, 1]], 2
        )
        self.assertEqual(result["chart"]["kind"], "infinity")
        self.assertEqual(result["normalized_operator"], [[1, 0], [0, 0]])

    def test_strictly_equivalent_pairs_compare_equal(self):
        q = [[1, 0], [0, 1]]
        k = [[1, 1], [0, 2]]
        s = [[1, 1], [0, 1]]
        t = [[1, 0], [1, 1]]
        def mm(a, b):
            return [[sum(a[i][r] * b[r][j] for r in range(2)) % 5
                     for j in range(2)] for i in range(2)]
        q2, k2 = mm(mm(s, q), t), mm(mm(s, k), t)
        result = compare_regular_pencils(q, k, q2, k2, 5)
        self.assertTrue(result["decision_complete"])
        self.assertTrue(result["strictly_equivalent"])

    def test_same_dimension_but_different_similarity_classes(self):
        result = compare_regular_pencils(
            [[1, 0], [0, 1]], [[1, 0], [0, 1]],
            [[1, 0], [0, 1]], [[1, 1], [0, 1]], 5
        )
        self.assertFalse(result["strictly_equivalent"])

    def test_regular_pencil_can_have_no_rational_invertible_member(self):
        # det(aQ+bK)=a*b*(a+b), nonzero as a polynomial over F_2,
        # but it vanishes at all three points of P^1(F_2).
        q = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        k = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        with self.assertRaisesRegex(ValueError, "no invertible projective member"):
            regular_pencil_similarity_profile(q, k, 2)

    def test_comparison_without_common_chart_is_inconclusive(self):
        q_a = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        k_a = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        q_b = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        k_b = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = compare_regular_pencils(q_a, k_a, q_b, k_b, 2)
        self.assertFalse(result["decision_complete"])
        self.assertIsNone(result["strictly_equivalent"])

    def test_rejects_nonsquare_and_shape_mismatch(self):
        with self.assertRaises(ValueError):
            regular_pencil_similarity_profile([[1, 0, 0]], [[0, 1, 0]], 5)
        with self.assertRaises(ValueError):
            compare_regular_pencils([[1]], [[1]], [[1, 0]], [[0, 1]], 5)

    def test_rejects_composite_modulus(self):
        with self.assertRaises(ValueError):
            regular_pencil_similarity_profile([[1]], [[2]], 4)


if __name__ == "__main__":
    unittest.main()
