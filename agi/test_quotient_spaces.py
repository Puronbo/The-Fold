"""Tests for finite orbit quotients and relation descent."""
import unittest

from agi.quotient_spaces import construct_orbit_quotient


class OrbitQuotientTests(unittest.TestCase):
    def test_swap_collapses_two_states(self):
        report = construct_orbit_quotient(("a", "b"), (("id", (0, 1)), ("swap", (1, 0))))
        self.assertTrue(report.valid_group_action)
        self.assertEqual(report.equivalence_classes, (("a", "b"),))
        self.assertEqual(report.representatives, ("a",))
        self.assertEqual(report.state_to_class, (("a", 0), ("b", 0)))
        self.assertEqual(report.class_sizes, (2,))
        self.assertEqual(report.information_collapsed, 1)

    def test_trivial_group_has_singleton_classes(self):
        report = construct_orbit_quotient((1, 2, 3), (("id", (0, 1, 2)),))
        self.assertEqual(report.equivalence_classes, ((1,), (2,), (3,)))
        self.assertEqual(report.quotient_state_count, 3)
        self.assertEqual(report.information_collapsed, 0)

    def test_cyclic_three_action(self):
        report = construct_orbit_quotient(
            ("a", "b", "c"),
            (("id", (0, 1, 2)), ("r", (1, 2, 0)), ("r2", (2, 0, 1))),
        )
        self.assertEqual(report.equivalence_classes, (("a", "b", "c"),))

    def test_full_relation_descends(self):
        states = ("a", "b")
        relation = tuple((x, y) for x in states for y in states)
        report = construct_orbit_quotient(
            states, (("id", (0, 1)), ("swap", (1, 0))), relation
        )
        self.assertTrue(report.diagonal_relation_invariant)
        self.assertTrue(report.quotient_relation_well_defined)
        self.assertEqual(report.quotient_relation, ((0, 0),))

    def test_empty_relation_descends(self):
        report = construct_orbit_quotient(
            ("a", "b"), (("id", (0, 1)), ("swap", (1, 0))), ()
        )
        self.assertTrue(report.quotient_relation_well_defined)
        self.assertEqual(report.quotient_relation, ())

    def test_diagonal_invariance_does_not_guarantee_descent(self):
        states = (0, 1)
        equality = ((0, 0), (1, 1))
        report = construct_orbit_quotient(
            states, (("id", (0, 1)), ("swap", (1, 0))), equality
        )
        self.assertTrue(report.diagonal_relation_invariant)
        self.assertFalse(report.quotient_relation_well_defined)
        self.assertIsNone(report.quotient_relation)

    def test_noninvariant_relation_does_not_descend(self):
        report = construct_orbit_quotient(
            ("a", "b"), (("id", (0, 1)), ("swap", (1, 0))), (("a", "b"),)
        )
        self.assertFalse(report.diagonal_relation_invariant)
        self.assertFalse(report.quotient_relation_well_defined)
        self.assertIsNone(report.quotient_relation)

    def test_invalid_group_returns_unconstructed_quotient(self):
        invalid = construct_orbit_quotient(("a", "b"), (("swap", (1, 0)),))
        self.assertFalse(invalid.valid_group_action)
        self.assertEqual(invalid.status, "not_a_group_action")
        self.assertEqual(invalid.equivalence_classes, ())

    def test_duplicate_states_rejected(self):
        with self.assertRaises(ValueError):
            construct_orbit_quotient(("a", "a"), (("id", (0, 1)),))

    def test_relation_unknown_endpoint_rejected(self):
        with self.assertRaises(ValueError):
            construct_orbit_quotient(("a",), (("id", (0,)),), (("a", "b"),))

    def test_representative_convention_depends_on_input_order(self):
        transforms = (("id", (0, 1)), ("swap", (1, 0)))
        first = construct_orbit_quotient(("a", "b"), transforms)
        second = construct_orbit_quotient(("b", "a"), transforms)
        self.assertEqual(set(first.equivalence_classes[0]), set(second.equivalence_classes[0]))
        self.assertEqual(first.representatives, ("a",))
        self.assertEqual(second.representatives, ("b",))


if __name__ == "__main__":
    unittest.main()
