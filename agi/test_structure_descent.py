"""Tests for operation congruence and quotient homomorphisms."""
import unittest
from itertools import product
from agi.quotient_spaces import construct_orbit_quotient
from agi.structure_descent import descend_operations

class StructureDescentTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.group = (("id", (0, 1, 2, 3)), ("swap_pairs", (1, 0, 3, 2)))
        self.quotient = construct_orbit_quotient(self.states, self.group)

    def table(self, fn, arity):
        return tuple((args, fn(*args)) for args in product(self.states, repeat=arity))

    def test_unary_identity_descends(self):
        report = descend_operations(self.quotient, (("identity", self.table(lambda x: x, 1)),))
        self.assertTrue(report.operations[0].congruence_verified)
        self.assertEqual(report.operations[0].quotient_table, (((0,), 0), ((1,), 1)))
        self.assertTrue(report.quotient_projection_is_homomorphism)

    def test_unary_operation_fails(self):
        values = {0: 0, 1: 2, 2: 2, 3: 3}
        report = descend_operations(self.quotient, (("split", self.table(lambda x: values[x], 1)),))
        self.assertFalse(report.all_operations_descend)
        self.assertIsNone(report.operations[0].quotient_table)

    def test_addition_mod_four_fails(self):
        table = self.table(lambda x, y: (x + y) % 4, 2)
        report = descend_operations(self.quotient, (("add_mod_4", table),))
        self.assertFalse(report.operations[0].congruence_verified)

    def test_xor_descends(self):
        q = construct_orbit_quotient((0, 1, 2, 3), (("id", (0, 1, 2, 3)), ("xor1", (1, 0, 3, 2))))
        table = tuple(((x, y), x ^ y) for x, y in product(range(4), repeat=2))
        report = descend_operations(q, (("xor", table),))
        self.assertTrue(report.all_operations_descend)
        self.assertEqual(report.operations[0].quotient_table,
            (((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)))

    def test_incomplete_table_rejected(self):
        with self.assertRaises(ValueError):
            descend_operations(self.quotient, (("partial", self.table(lambda x: x, 1)[:-1]),))

    def test_duplicate_input_rejected(self):
        t = self.table(lambda x: x, 1)
        with self.assertRaises(ValueError):
            descend_operations(self.quotient, (("duplicate", t + (t[0],)),))

    def test_unknown_state_rejected(self):
        t = list(self.table(lambda x: x, 1)); t[0] = ((99,), 0)
        with self.assertRaises(ValueError):
            descend_operations(self.quotient, (("bad", tuple(t)),))

    def test_mixed_arity_rejected(self):
        with self.assertRaises(ValueError):
            descend_operations(self.quotient, (("mixed", (((0,), 0), ((0, 1), 1))),))

    def test_duplicate_names_rejected(self):
        t = self.table(lambda x: x, 1)
        with self.assertRaises(ValueError):
            descend_operations(self.quotient, (("same", t), ("same", t)))

    def test_invalid_quotient_rejected(self):
        q = construct_orbit_quotient((0, 1), (("swap", (1, 0)),))
        with self.assertRaises(ValueError):
            descend_operations(q, (("identity", (((0,), 0), ((1,), 1))),))

if __name__ == "__main__":
    unittest.main()
