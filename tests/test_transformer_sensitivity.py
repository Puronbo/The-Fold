import unittest

from tools.transformer_sensitivity import compare_snapshots


class TransformerSensitivityTests(unittest.TestCase):
    def test_square_spectral_fingerprint_sensitivity(self):
        result = compare_snapshots(
            {
                "reference": [[1.0, 0.0], [0.0, 1.0]],
                "small_noise": [[1.01, 0.0], [0.0, 1.01]],
                "changed_eigenvalue": [[1.0, 0.0], [0.0, 2.0]],
            },
            primes=[5],
            scales=[1.0],
            include_square_spectra=True,
        )
        config = result["configurations"][0]
        self.assertTrue(config["snapshots"]["reference"]["stable_vs_reference"])
        self.assertTrue(config["snapshots"]["small_noise"]["stable_vs_reference"])
        self.assertFalse(config["snapshots"]["changed_eigenvalue"]["stable_vs_reference"])
        self.assertIn("spectral_signature",
                      config["snapshots"]["changed_eigenvalue"])

    def test_rectangular_rank_only_sensitivity(self):
        result = compare_snapshots(
            {
                "reference": [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                "same_rank": [[2.0, 0.0, 0.0], [0.0, 3.0, 0.0]],
                "rank_drop": [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            },
            primes=[3, 5],
            scales=[1.0, 10.0],
        )
        self.assertEqual(len(result["configurations"]), 4)
        for config in result["configurations"]:
            self.assertTrue(config["snapshots"]["same_rank"]["stable_vs_reference"])
            self.assertFalse(config["snapshots"]["rank_drop"]["stable_vs_reference"])

    def test_fingerprint_stability_depends_on_quantization_scale(self):
        result = compare_snapshots(
            {
                "reference": [[0.49]],
                "nearby": [[0.51]],
            },
            primes=[5],
            scales=[1.0, 10.0],
        )
        coarse, finer = result["configurations"]
        self.assertFalse(coarse["snapshots"]["nearby"]["stable_vs_reference"])
        self.assertTrue(finer["snapshots"]["nearby"]["stable_vs_reference"])

    def test_reject_shape_mismatch_and_rectangular_spectrum(self):
        with self.assertRaises(ValueError):
            compare_snapshots({"a": [[1, 2]], "b": [[1], [2]]}, [5], [1])
        with self.assertRaises(ValueError):
            compare_snapshots({"a": [[1, 2, 3]]}, [5], [1],
                              include_square_spectra=True)

    def test_reject_empty_configuration(self):
        with self.assertRaises(ValueError):
            compare_snapshots({"a": [[1]]}, [], [1])
        with self.assertRaises(ValueError):
            compare_snapshots({}, [5], [1])


if __name__ == "__main__":
    unittest.main()
