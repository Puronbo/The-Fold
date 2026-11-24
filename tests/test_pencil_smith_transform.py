import unittest

from tools.pencil_smith_transform import polynomial_smith_transform


class PolynomialSmithTransformTests(unittest.TestCase):
    def test_regular_diagonal_pencil(self):
        q, k = [[0, 0], [0, 1]], [[1, 0], [0, 0]]
        result = polynomial_smith_transform(q, k, 5)
        self.assertTrue(result["verified_smith_form"])
        self.assertEqual(result["normal_rank"], 2)
        self.assertEqual(result["smith_diagonal_low_degree_first"], [[1], [0, 1]])

    def test_rectangular_singular_pencil(self):
        q, k = [[0, -1]], [[1, 0]]
        result = polynomial_smith_transform(q, k, 3)
        self.assertTrue(result["verified_smith_form"])
        self.assertEqual(result["normal_rank"], 1)
        self.assertEqual(result["smith_diagonal_low_degree_first"], [[1]])

    def test_nontrivial_polynomial_euclidean_reduction(self):
        q, k = [[1, 0], [0, 0]], [[0, 1], [1, 0]]
        result = polynomial_smith_transform(q, k, 7)
        self.assertTrue(result["verified_smith_form"])
        self.assertEqual(result["normal_rank"], 2)

    def test_singular_zero_matrix(self):
        result = polynomial_smith_transform([[0, 0]], [[0, 0]], 3)
        self.assertTrue(result["verified_smith_form"])
        self.assertEqual(result["normal_rank"], 0)
        self.assertEqual(result["smith_diagonal_low_degree_first"], [[0]])

    def test_unimodular_transforms_are_explicit(self):
        q, k = [[0, 1], [1, 0]], [[1, 0], [0, 1]]
        result = polynomial_smith_transform(q, k, 5)
        self.assertTrue(result["checks"]["U_times_P_times_V_equals_reduced_matrix"])
        self.assertTrue(result["checks"]["transforms_are_products_of_unimodular_elementary_operations"])
        self.assertTrue(result["operation_log"])


if __name__ == "__main__":
    unittest.main()
