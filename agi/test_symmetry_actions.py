"""Tests for finite group actions and symmetry discovery."""
import unittest

from agi.symmetry_actions import analyze_finite_group_action


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


if __name__ == "__main__":
    unittest.main()
