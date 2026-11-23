import unittest

from tools.rational_primary_decomposition import rational_primary_decomposition
from tools.rational_primary_cyclic import construct_primary_cyclic_summands


class RationalPrimaryCyclicTests(unittest.TestCase):
    def test_constructs_two_nilpotent_elementary_divisors(self):
        # J_3(0) direct sum J_1(0), elementary divisors x^3 and x.
        a = [[0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        primary = rational_primary_decomposition(a, 2)
        block = primary["components"][0]["basis_columns"]
        # Component coordinates are already a basis of the full space here.
        result = construct_primary_cyclic_summands(
            primary["transformed_operator"], 2, [1, 0], [3, 1],
            max_candidates=100,
        )
        self.assertTrue(result["basis_complete"])
        self.assertEqual([s["dimension"] for s in result["summands"]], [3, 1])
        self.assertEqual(len(result["change_of_basis_columns"]), 4)

    def test_constructs_two_equal_linear_blocks(self):
        a = [[1, 0], [0, 1]]
        result = construct_primary_cyclic_summands(a, 5, [1, 4], [1, 1])
        self.assertTrue(result["basis_complete"])
        self.assertEqual([s["dimension"] for s in result["summands"]], [1, 1])

    def test_budget_exhaustion_is_explicit(self):
        a = [[0, 1], [0, 0]]
        result = construct_primary_cyclic_summands(a, 2, [1, 0], [2], max_candidates=1)
        self.assertFalse(result["basis_complete"])
        self.assertFalse(result["search_complete"])


if __name__ == "__main__":
    unittest.main()
