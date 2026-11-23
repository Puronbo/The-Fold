import unittest

from tools.layer_spectral_comparison import analyze_layer_snapshots


class LayerSpectralComparisonTests(unittest.TestCase):
    def setUp(self):
        identity = [[1, 0], [0, 1]]
        quarter_turn = [[0, -1], [1, 0]]
        self.snapshots = {
            "checkpoint_a": {
                "layer_0": {
                    "q_proj": identity,
                    "k_proj": identity,
                    "v_proj": quarter_turn,
                    "o_proj": identity,
                    "up_proj": [[1, 0], [0, 1], [1, 1]],
                }
            },
            "checkpoint_b": {
                "layer_0": {
                    "q_proj": identity,
                    "k_proj": quarter_turn,
                    "v_proj": quarter_turn,
                    "o_proj": identity,
                    "up_proj": [[1, 0], [0, 1], [1, 1]],
                }
            },
        }

    def test_square_and_rectangular_projections_are_handled_differently(self):
        result = analyze_layer_snapshots(self.snapshots, [3, 5])
        a = result["snapshots"]["checkpoint_a"]["layer_0"]
        self.assertEqual(a["q_proj"]["kind"], "square_spectral")
        self.assertEqual(a["up_proj"]["kind"], "rectangular_rank_only")
        self.assertEqual(a["up_proj"]["ranks"], {"3": 2, "5": 2})

    def test_within_layer_profiles_add_information_beyond_rank(self):
        result = analyze_layer_snapshots(self.snapshots, [3, 5])
        at_three = next(
            x for x in result["within_layer_comparisons"]
            if x["snapshot"] == "checkpoint_a" and x["prime"] == 3
        )
        pair = next(
            x for x in at_three["pairwise"]
            if {x["left"], x["right"]} == {"q_proj", "v_proj"}
        )
        self.assertTrue(pair["same_rank"])
        self.assertFalse(pair["same_orbit_histogram"])
        self.assertFalse(pair["same_exact_factor_profile"])

    def test_cross_snapshot_stability_is_projection_specific(self):
        result = analyze_layer_snapshots(self.snapshots, [3])
        k = next(
            x for x in result["cross_snapshot_stability"]
            if x["layer"] == "layer_0" and x["projection"] == "k_proj"
        )
        self.assertFalse(k["snapshots"]["checkpoint_b"]["same_full_profile_as_reference"])
        q = next(
            x for x in result["cross_snapshot_stability"]
            if x["layer"] == "layer_0" and x["projection"] == "q_proj"
        )
        self.assertTrue(q["snapshots"]["checkpoint_b"]["same_full_profile_as_reference"])
        v = next(
            x for x in result["cross_snapshot_stability"]
            if x["layer"] == "layer_0" and x["projection"] == "v_proj"
        )
        self.assertTrue(v["snapshots"]["checkpoint_b"]["same_full_profile_as_reference"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            analyze_layer_snapshots({}, [3])
        with self.assertRaises(ValueError):
            analyze_layer_snapshots(self.snapshots, [])
        with self.assertRaises(ValueError):
            analyze_layer_snapshots({"bad": {"layer": {"empty": []}}}, [3])


if __name__ == "__main__":
    unittest.main()
