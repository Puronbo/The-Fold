import unittest

from tools.rational_primary_decomposition import rational_primary_decomposition


class RationalPrimaryDecompositionTests(unittest.TestCase):
    def test_splits_distinct_linear_primary_components(self):
        a = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
        result = rational_primary_decomposition(a, 5)
        self.assertEqual(sorted(c["dimension"] for c in result["components"]), [1, 2])
        self.assertTrue(result["checks"]["change_of_basis_invertible"])
        self.assertTrue(result["checks"]["operator_is_block_diagonal_by_primary_component"])

    def test_keeps_repeated_irreducible_in_one_primary_component(self):
        # A single nilpotent Jordan block has only the irreducible factor x.
        a = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
        result = rational_primary_decomposition(a, 3)
        self.assertEqual(len(result["components"]), 1)
        self.assertEqual(result["components"][0]["dimension"], 3)
        self.assertEqual(result["transformed_operator"], a)

    def test_splits_quadratic_and_linear_components(self):
        # x^2+1 is irreducible over F_3.
        a = [[0, 2, 0], [1, 0, 0], [0, 0, 1]]
        result = rational_primary_decomposition(a, 3)
        self.assertEqual(sorted(c["dimension"] for c in result["components"]), [1, 2])
        self.assertTrue(result["checks"]["operator_is_block_diagonal_by_primary_component"])


if __name__ == "__main__":
    unittest.main()
