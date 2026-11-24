import unittest

from tools.transformer_checkpoint import inspect_state_dict, _state_dict


class FakeTensor:
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), len(values[0]))

    def detach(self):
        return self

    def cpu(self):
        return self

    def tolist(self):
        return self.values


class TransformerCheckpointTests(unittest.TestCase):
    def test_inspect_named_rectangular_and_square_weights(self):
        state = {
            "encoder.attention.q_proj.weight": FakeTensor([[1, 0], [0, 1]]),
            "encoder.mlp.up_proj.weight": FakeTensor([[1, 0], [0, 1], [1, 1]]),
            "encoder.norm.weight": [1, 1],
            "encoder.attention.q_proj.bias": [0, 0],
        }
        report = inspect_state_dict(
            state, primes=[5], scales=[1],
            include_square_spectra=True, spectral_max_dimension=4,
        )
        self.assertEqual(len(report["layers"]), 2)
        by_name = {layer["name"]: layer for layer in report["layers"]}
        self.assertIn("spectral_fingerprint",
                      by_name["encoder.attention.q_proj.weight"]["configurations"][0])
        self.assertNotIn("spectral_fingerprint",
                         by_name["encoder.mlp.up_proj.weight"]["configurations"][0])
        self.assertEqual(len(report["skipped"]), 2)

    def test_size_limit_skips_large_layer(self):
        report = inspect_state_dict(
            {"large.weight": [[1, 0, 0], [0, 1, 0]]},
            primes=[5], scales=[1], max_elements=5,
        )
        self.assertEqual(report["layers"], [])
        self.assertIn("exceeds max_elements", report["skipped"][0]["reason"])

    def test_checkpoint_wrapper_extraction(self):
        weights = {"layer.weight": [[1, 2], [3, 4]]}
        self.assertIs(_state_dict({"state_dict": weights, "epoch": 2}), weights)
        self.assertIs(_state_dict(weights), weights)

    def test_reject_invalid_configuration(self):
        with self.assertRaises(ValueError):
            inspect_state_dict({}, [], [1])
        with self.assertRaises(ValueError):
            inspect_state_dict({}, [5], [1], max_elements=0)


if __name__ == "__main__":
    unittest.main()
