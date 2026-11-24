import unittest

from tools.qk_interaction import analyze_qk_interaction


class QKInteractionTests(unittest.TestCase):
    def test_square_pair_profiles_both_products_and_individuals(self):
        q = [[1, 0], [0, 1]]
        k = [[0, -1], [1, 0]]
        result = analyze_qk_interaction(q, k, [3, 5, 7])
        products = result["products"]
        self.assertEqual(products["output_space_qk_transpose"]["shape"], [2, 2])
        self.assertEqual(products["input_space_q_transpose_k"]["shape"], [2, 2])
        self.assertEqual(
            products["output_space_qk_transpose"]["rank_by_prime"],
            {"3": 2, "5": 2, "7": 2},
        )
        self.assertIsNotNone(result["individual_square_projection_profiles"]["q"])
        self.assertIsNotNone(result["individual_square_projection_profiles"]["k"])
        # Q K^T = J^T and Q^T K = J for this fixture.
        out = products["output_space_qk_transpose"]["spectral_profile"]
        inp = products["input_space_q_transpose_k"]["spectral_profile"]
        self.assertEqual(out["profiles"][0]["frobenius_orbit_degree_histogram"], {"2": 2})
        self.assertEqual(inp["profiles"][0]["frobenius_orbit_degree_histogram"], {"2": 2})

    def test_rectangular_pair_yields_two_square_interactions(self):
        q = [[1, 0, 0], [0, 1, 0]]
        k = [[0, 1, 0], [1, 0, 1]]
        result = analyze_qk_interaction(q, k, [3, 5])
        output = result["products"]["output_space_qk_transpose"]
        input_ = result["products"]["input_space_q_transpose_k"]
        self.assertEqual(output["shape"], [2, 2])
        self.assertEqual(input_["shape"], [3, 3])
        self.assertIsNotNone(output["spectral_profile"])
        self.assertIsNotNone(input_["spectral_profile"])
        self.assertIsNone(result["individual_square_projection_profiles"]["q"])

    def test_shape_and_prime_validation(self):
        with self.assertRaises(ValueError):
            analyze_qk_interaction([[1, 0]], [[1], [0]], [3])
        with self.assertRaises(ValueError):
            analyze_qk_interaction([[1]], [[1]], [])
        with self.assertRaises(ValueError):
            analyze_qk_interaction([[]], [[]], [3])


if __name__ == "__main__":
    unittest.main()
