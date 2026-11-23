import unittest

from tools.transformer_adapter import (
    analyze_square_weight_operator,
    analyze_weight_matrix,
    export_weight_matrix,
)


class FakeTensor:
    """Tiny stand-in for a tensor's detach/cpu/tolist protocol."""
    def __init__(self, values):
        self.values = values

    def detach(self):
        return self

    def cpu(self):
        return self

    def tolist(self):
        return self.values


class TransformerAdapterTests(unittest.TestCase):
    def test_export_rectangular_weights_and_metadata(self):
        result = export_weight_matrix([[0.2, -0.2, 1.1], [2.0, 0.0, -1.0]], 5,
                                      scale=10)
        self.assertEqual(result["matrix"], [[2, 3, 1], [0, 0, 0]])
        self.assertEqual(result["metadata"]["shape"], [2, 3])
        self.assertTrue(result["metadata"]["lossy_preprocessing"])
        self.assertEqual(result["metadata"]["quantization"],
                         "round-to-nearest, ties-to-even")

    def test_rounding_is_ties_to_even(self):
        result = export_weight_matrix([[0.5, 1.5, 2.5, -1.5]], 7)
        self.assertEqual(result["matrix"], [[0, 2, 2, 6]])

    def test_tensor_like_input_without_framework_dependency(self):
        result = export_weight_matrix(FakeTensor([[1, 2], [3, 4]]), 5)
        self.assertEqual(result["matrix"], [[1, 2], [3, 4]])

    def test_rectangular_layer_rank(self):
        result = analyze_weight_matrix([[1, 2, 3], [2, 4, 1]], 5)
        self.assertEqual(result["rank_over_field"], 2)
        self.assertEqual(result["rank_defect"], 0)

    def test_square_operator_full_spectral_profile(self):
        result = analyze_square_weight_operator([[0, 1], [1, 0]], 2)
        profile = result["spectral_fingerprint"]
        self.assertEqual(profile["base_field_eigenvalues"],
                         [{"value": 1, "algebraic_multiplicity": 2}])
        self.assertEqual(profile["profiles"][0]["blocks_exactly"], {"2": 1})

    def test_reject_rectangular_jordan_request(self):
        with self.assertRaises(ValueError):
            analyze_square_weight_operator([[1, 2, 3], [4, 5, 6]], 5)

    def test_reject_invalid_prime_scale_and_values(self):
        with self.assertRaises(ValueError):
            export_weight_matrix([[1]], 4)
        with self.assertRaises(ValueError):
            export_weight_matrix([[1]], 5, scale=0)
        with self.assertRaises(ValueError):
            export_weight_matrix([[float("nan")]], 5)
        with self.assertRaises(ValueError):
            export_weight_matrix([[1, 2], [3]], 5)


if __name__ == "__main__":
    unittest.main()
