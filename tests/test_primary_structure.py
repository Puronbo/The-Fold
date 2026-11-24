import unittest

from tools.primary_structure import compare_primary_structure


class PrimaryStructureTests(unittest.TestCase):
    def test_different_dimensions_share_primary_components(self):
        # A = diag(1,1,2), B = diag(1,2,2,3) over F_5.
        a = [[1, 0, 0], [0, 1, 0], [0, 0, 2]]
        b = [
            [1, 0, 0, 0], [0, 2, 0, 0],
            [0, 0, 2, 0], [0, 0, 0, 3],
        ]
        result = compare_primary_structure(a, b, 5)
        self.assertFalse(result["same_dimension"])
        self.assertFalse(result["same_similarity_class"])
        self.assertEqual(result["common_irreducible_factor_count"], 2)
        self.assertEqual(result["shared_primary_dimension"], 2)
        self.assertEqual(result["exact_elementary_divisor_dimension_overlap"], 2)

    def test_same_primary_support_but_different_block_sizes(self):
        # J_2(0) versus two 1x1 zero blocks: same primary dimension,
        # but no exact elementary divisor blocks in common.
        a = [[0, 1], [0, 0]]
        b = [[0, 0], [0, 0]]
        result = compare_primary_structure(a, b, 3)
        self.assertEqual(result["shared_primary_dimension"], 2)
        self.assertEqual(result["exact_elementary_divisor_dimension_overlap"], 0)

    def test_no_common_irreducible_support(self):
        a = [[1]]
        b = [[2]]
        result = compare_primary_structure(a, b, 5)
        self.assertEqual(result["common_irreducible_factor_count"], 0)
        self.assertEqual(result["shared_primary_dimension"], 0)

    def test_rejects_composite_modulus(self):
        with self.assertRaises(ValueError):
            compare_primary_structure([[1]], [[1]], 4)


if __name__ == "__main__":
    unittest.main()
