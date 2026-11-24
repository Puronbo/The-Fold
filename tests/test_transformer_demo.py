import unittest

from tools.transformer_demo import build_synthetic_snapshots, run_demo


class TransformerDemoTests(unittest.TestCase):
    def test_fixture_is_deterministic_and_transformer_shaped(self):
        first = build_synthetic_snapshots()
        second = build_synthetic_snapshots()
        self.assertEqual(first, second)
        state = first["synthetic_reference"]
        self.assertEqual(len(state["encoder.attention.q_proj.weight"]), 4)
        self.assertEqual(len(state["encoder.mlp.up_proj.weight"]), 6)
        self.assertEqual(len(state["encoder.mlp.up_proj.weight"][0]), 4)
        self.assertEqual(len(state["encoder.norm.weight"]), 4)

    def test_end_to_end_report_scans_layers_and_skips_vectors(self):
        report = run_demo(primes=[5], scales=[1])
        self.assertEqual(report["status"], "synthetic_fixture_not_trained_model")
        for snapshot in report["reports"].values():
            self.assertEqual(len(snapshot["layers"]), 6)
            self.assertEqual(len(snapshot["skipped"]), 2)
            layers = {item["name"]: item for item in snapshot["layers"]}
            self.assertEqual(layers["encoder.mlp.up_proj.weight"]["shape"], [6, 4])
            self.assertIn(
                "spectral_fingerprint",
                layers["encoder.attention.q_proj.weight"]["configurations"][0],
            )
            self.assertNotIn(
                "spectral_fingerprint",
                layers["encoder.mlp.up_proj.weight"]["configurations"][0],
            )

    def test_controlled_rank_change_is_detected(self):
        report = run_demo(primes=[5], scales=[1])
        config = report["q_projection_sensitivity"]["configurations"][0]
        entries = config["snapshots"]
        self.assertTrue(entries["synthetic_small_perturbation"]["stable_vs_reference"])
        self.assertFalse(entries["synthetic_rank_changed"]["stable_vs_reference"])
        self.assertEqual(entries["synthetic_reference"]["rank"], 4)
        self.assertEqual(entries["synthetic_rank_changed"]["rank"], 3)

    def test_scale_and_prime_configurations_are_reported(self):
        report = run_demo(primes=[5, 7], scales=[1, 10])
        self.assertEqual(len(report["q_projection_sensitivity"]["configurations"]), 4)
        self.assertEqual(report["reports"]["synthetic_reference"]["parameters"]["primes"], [5, 7])


if __name__ == "__main__":
    unittest.main()
