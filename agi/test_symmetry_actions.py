"""Tests for finite group actions and symmetry discovery."""
import unittest

from agi.symmetry_actions import analyze_finite_group_action, orbit_reconstruction_profiles


class SymmetryActionTests(unittest.TestCase):
    def test_two_state_swap_group_has_one_orbit(self):
        result = analyze_finite_group_action(
            ("a", "b"), (("e", (0, 1)), ("s", (1, 0))),
        )
        self.assertTrue(result.is_group_action)
        self.assertEqual(result.orbits, (("a", "b"),))
        self.assertEqual(dict(result.stabilizers), {"a": ("e",), "b": ("e",)})

    def test_trivial_group_has_singleton_orbits(self):
        result = analyze_finite_group_action(
            ("a", "b", "c"), (("e", (0, 1, 2)),),
        )
        self.assertEqual(result.orbits, (("a",), ("b",), ("c",)))

    def test_cyclic_three_action_is_transitive(self):
        result = analyze_finite_group_action(
            (0, 1, 2),
            (("e", (0, 1, 2)), ("r", (1, 2, 0)), ("r2", (2, 0, 1))),
        )
        self.assertTrue(result.is_group_action)
        self.assertEqual(result.orbits, ((0, 1, 2),))
        self.assertEqual(dict(result.stabilizers)[0], ("e",))

    def test_relation_preserved_by_swap(self):
        # Complete symmetric adjacency relation on two vertices.
        relation = (("a", "b"), ("b", "a"))
        result = analyze_finite_group_action(
            ("a", "b"), (("e", (0, 1)), ("s", (1, 0))), relation,
        )
        self.assertTrue(result.relation_preserved_by_all)
        self.assertEqual(result.relation_violations, ())

    def test_relation_not_preserved(self):
        relation = (("a", "b"),)
        result = analyze_finite_group_action(
            ("a", "b"), (("e", (0, 1)), ("s", (1, 0))), relation,
        )
        self.assertFalse(result.relation_preserved_by_all)
        self.assertEqual(result.relation_violations, (("s", ("b", "a")),))

    def test_missing_identity_rejected(self):
        result = analyze_finite_group_action(("a", "b"), (("s", (1, 0)),))
        self.assertFalse(result.is_group_action)

    def test_nonclosed_collection_rejected(self):
        result = analyze_finite_group_action(
            (0, 1, 2), (("e", (0, 1, 2)), ("r", (1, 2, 0))),
        )
        self.assertFalse(result.is_group_action)
        self.assertEqual(result.status, "transformations_not_closed_under_composition")

    def test_non_bijection_rejected(self):
        with self.assertRaises(ValueError):
            analyze_finite_group_action(("a", "b"), (("e", (0, 0)),))

    def test_duplicate_states_and_permutations_rejected(self):
        with self.assertRaises(ValueError):
            analyze_finite_group_action(("a", "a"), (("e", (0, 1)),))
        with self.assertRaises(ValueError):
            analyze_finite_group_action(("a", "b"), (("e", (0, 1)), ("e2", (0, 1))))

    def test_relation_must_use_known_states(self):
        with self.assertRaises(ValueError):
            analyze_finite_group_action(
                ("a", "b"), (("e", (0, 1)),), (("a", "outside"),),
            )


    def test_orbit_stabilizer_and_selector_bits_for_s3_action(self):
        profiles = orbit_reconstruction_profiles(
            (0, 1, 2),
            (
                ("e", (0, 1, 2)),
                ("t01", (1, 0, 2)),
                ("t12", (0, 2, 1)),
                ("t02", (2, 1, 0)),
                ("r", (1, 2, 0)),
                ("r2", (2, 0, 1)),
            ),
        )
        for profile in profiles:
            self.assertEqual(profile.group_size, 6)
            self.assertEqual(profile.orbit_size, 3)
            self.assertEqual(profile.stabilizer_size, 2)
            self.assertEqual(profile.group_size,
                             profile.orbit_size * profile.stabilizer_size)
            self.assertEqual(profile.selector_redundancy, 2)
            self.assertEqual(profile.minimum_fixed_length_bits, 2)

    def test_fixed_point_needs_zero_selector_bits(self):
        profiles = orbit_reconstruction_profiles(
            ("a", "b"),
            (("e", (0, 1)), ("s", (1, 0))),
        )
        # This action swaps the two states, so neither is fixed.
        self.assertEqual({p.minimum_fixed_length_bits for p in profiles}, {1})
        fixed_profiles = orbit_reconstruction_profiles(
            ("fixed", "a", "b"),
            (
                ("e", (0, 1, 2)),
                ("s", (0, 2, 1)),
            ),
        )
        fixed = next(p for p in fixed_profiles if p.state == "fixed")
        self.assertEqual(fixed.orbit_size, 1)
        self.assertEqual(fixed.stabilizer_size, 2)
        self.assertEqual(fixed.minimum_fixed_length_bits, 0)

    def test_reconstruction_profile_rejects_non_group(self):
        with self.assertRaises(ValueError):
            orbit_reconstruction_profiles(
                (0, 1, 2), (("e", (0, 1, 2)), ("r", (1, 2, 0))),
            )


if __name__ == "__main__":
    unittest.main()
