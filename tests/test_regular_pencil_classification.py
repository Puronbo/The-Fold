import unittest

from tools.regular_pencil_classification import (
    compare_regular_pencils_complete, regular_pencil_complete_profile,
)


def mm(a, b, p):
    return [[sum(a[i][r] * b[r][j] for r in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


class RegularPencilClassificationTests(unittest.TestCase):
    def test_classifies_regular_pencil_with_invertible_q(self):
        result = regular_pencil_complete_profile(
            [[1, 0], [0, 1]], [[0, 1], [0, 0]], 5
        )
        self.assertTrue(result["complete_regular_strict_equivalence_invariant"])
        self.assertEqual(result["total_elementary_divisor_degree"], 2)

    def test_classifies_regular_pencil_with_singular_q(self):
        q = [[0, 0], [0, 1]]
        k = [[1, 0], [0, 0]]
        result = regular_pencil_complete_profile(q, k, 5)
        self.assertTrue(result["checks"]["finite_chart_normal_rank_is_full"])
        self.assertTrue(result["checks"]["reversed_chart_normal_rank_is_full"])
        self.assertEqual(result["finite_elementary_divisor_degree_sum"], 1)
        self.assertEqual(result["infinity_elementary_divisor_degree_sum"], 1)

    def test_classifies_regular_pencil_without_rational_invertible_member(self):
        # det(aQ+bK)=a*b*(a+b): regular over F_2, zero on P^1(F_2).
        q = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        k = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = regular_pencil_complete_profile(q, k, 2)
        self.assertEqual(result["dimension"], 3)
        self.assertEqual(result["total_elementary_divisor_degree"], 3)
        self.assertEqual(result["finite_elementary_divisor_degree_sum"], 2)
        self.assertEqual(result["infinity_elementary_divisor_degree_sum"], 1)
        self.assertEqual(result["infinity_elementary_divisor_sizes"], [1])

    def test_strict_equivalence_preserves_both_charts(self):
        q = [[1, 2], [0, 1]]
        k = [[0, 1], [1, 1]]
        s = [[0, 1], [1, 0]]
        t = [[1, 4], [0, 1]]
        q2, k2 = mm(mm(s, q, 5), t, 5), mm(mm(s, k, 5), t, 5)
        result = compare_regular_pencils_complete(q, k, q2, k2, 5)
        self.assertTrue(result["decision_complete"])
        self.assertTrue(result["strictly_equivalent"])

    def test_infinity_block_partition_is_not_just_total_degree(self):
        # Both pencils have no finite elementary divisors, but different
        # infinity Jordan partitions: [2] versus [1,1].
        result = compare_regular_pencils_complete(
            [[1, 0], [0, 1]], [[0, 1], [0, 0]],
            [[1, 0], [0, 1]], [[0, 0], [0, 0]], 5
        )
        self.assertTrue(result["finite_elementary_divisors_equal"])
        self.assertFalse(result["infinity_elementary_divisors_equal"])
        self.assertFalse(result["strictly_equivalent"])
        self.assertEqual(result["left_profile"]["infinity_elementary_divisor_sizes"], [2])
        self.assertEqual(result["right_profile"]["infinity_elementary_divisor_sizes"], [1, 1])

    def test_distinguishes_finite_elementary_divisors(self):
        result = compare_regular_pencils_complete(
            [[1, 0], [0, 1]], [[0, 0], [0, 1]],
            [[1, 0], [0, 1]], [[1, 0], [0, 1]], 5
        )
        self.assertFalse(result["strictly_equivalent"])

    def test_rejects_singular_pencil(self):
        with self.assertRaisesRegex(ValueError, "pencil is singular"):
            regular_pencil_complete_profile(
                [[1, 0], [0, 0]], [[0, 0], [0, 0]], 3
            )

    def test_rejects_rectangular_input(self):
        with self.assertRaises(ValueError):
            regular_pencil_complete_profile([[1, 0]], [[0, 1]], 3)

    def test_rejects_composite_modulus(self):
        with self.assertRaises(ValueError):
            regular_pencil_complete_profile([[1]], [[0]], 4)


if __name__ == "__main__":
    unittest.main()
