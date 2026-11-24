import unittest

from tools.pencil_smith import rectangular_pencil_smith_profile


class PencilSmithTests(unittest.TestCase):
    def test_regular_pencil_with_one_finite_elementary_divisor(self):
        q = [[0, 0], [0, 1]]
        k = [[1, 0], [0, 0]]
        result = rectangular_pencil_smith_profile(q, k, 5)
        finite = result["finite_chart"]
        self.assertEqual(finite["normal_rank_over_rational_function_field"], 2)
        self.assertEqual(finite["smith_invariant_factors_low_degree_first"],
                         [[1], [0, 1]])
        self.assertEqual(result["infinity_chart"][
            "normal_rank_over_rational_function_field"], 2)

    def test_singular_rectangular_pencil_reports_normal_rank(self):
        q = [[1, 0, 0], [0, 0, 0]]
        k = [[0, 1, 0], [0, 0, 0]]
        result = rectangular_pencil_smith_profile(q, k, 3)
        self.assertEqual(result["shape"], [2, 3])
        self.assertEqual(result["finite_chart"][
            "normal_rank_over_rational_function_field"], 1)
        self.assertEqual(result["finite_chart"][
            "smith_invariant_factors_low_degree_first"], [[1]])
        self.assertFalse(result["complete_kronecker_classification"])

    def test_constant_invertible_equivalence_preserves_smith_data(self):
        q = [[1, 2], [0, 1]]
        k = [[0, 1], [1, 1]]
        s = [[0, 1], [1, 0]]
        t_inv = [[1, 4], [0, 1]]
        def mm(a, b):
            return [[sum(a[i][z] * b[z][j] for z in range(len(b))) % 5
                     for j in range(len(b[0]))] for i in range(len(a))]
        q2, k2 = mm(mm(s, q), t_inv), mm(mm(s, k), t_inv)
        before = rectangular_pencil_smith_profile(q, k, 5)
        after = rectangular_pencil_smith_profile(q2, k2, 5)
        for chart in ("finite_chart", "infinity_chart"):
            for key in ("normal_rank_over_rational_function_field",
                        "determinantal_divisors_low_degree_first",
                        "smith_invariant_factors_low_degree_first"):
                self.assertEqual(before[chart][key], after[chart][key])

    def test_rejects_composite_field_and_minor_budget(self):
        with self.assertRaises(ValueError):
            rectangular_pencil_smith_profile([[1]], [[1]], 4)
        with self.assertRaises(ValueError):
            rectangular_pencil_smith_profile(
                [[1] * 5 for _ in range(5)], [[0] * 5 for _ in range(5)],
                3, max_minors=10
            )

    def test_rejects_invalid_budget(self):
        with self.assertRaises(ValueError):
            rectangular_pencil_smith_profile([[1]], [[0]], 3, max_minors=0)


if __name__ == "__main__":
    unittest.main()
