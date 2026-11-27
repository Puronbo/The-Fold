import unittest

from agi.restricted_three_colouring import (
    InvalidInstance,
    is_three_colourable,
    verify_three_colouring,
)


class RestrictedThreeColouringTests(unittest.TestCase):
    def test_k4_is_not_three_colourable_with_one_width_three_bag(self):
        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        self.assertFalse(is_three_colourable(4, edges, [[0, 1, 2, 3]], []))

    def test_path_is_three_colourable(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
        bags = [[0, 1], [1, 2], [2, 3], [3, 4]]
        tree = [(0, 1), (1, 2), (2, 3)]
        self.assertTrue(is_three_colourable(5, edges, bags, tree))

    def test_triangle_is_three_colourable(self):
        edges = [(0, 1), (1, 2), (0, 2)]
        self.assertTrue(is_three_colourable(3, edges, [[0, 1, 2]], []))

    def test_disconnected_graph_with_empty_root_bag(self):
        edges = [(0, 1), (2, 3)]
        bags = [[], [0, 1], [2, 3]]
        tree = [(0, 1), (0, 2)]
        self.assertTrue(is_three_colourable(4, edges, bags, tree))

    def test_rejects_bag_larger_than_four(self):
        with self.assertRaises(InvalidInstance):
            is_three_colourable(5, [], [[0, 1, 2, 3, 4]], [])

    def test_rejects_missing_edge_coverage(self):
        with self.assertRaises(InvalidInstance):
            is_three_colourable(3, [(0, 1)], [[0], [1], [2]], [(0, 1), (1, 2)])

    def test_rejects_running_intersection_failure(self):
        bags = [[0, 1], [1, 2], [0, 2]]
        tree = [(0, 1), (1, 2)]
        with self.assertRaises(InvalidInstance):
            is_three_colourable(3, [], bags, tree)

    def test_rejects_non_tree_decomposition_index_graph(self):
        bags = [[0], [0], [0]]
        tree = [(0, 1), (1, 2), (2, 0)]
        with self.assertRaises(InvalidInstance):
            is_three_colourable(1, [], bags, tree)

    def test_certificate_verifier(self):
        edges = [(0, 1), (1, 2), (0, 2)]
        self.assertTrue(verify_three_colouring(3, edges, [0, 1, 2]))
        self.assertFalse(verify_three_colouring(3, edges, [0, 0, 1]))
        self.assertFalse(verify_three_colouring(3, edges, [0, 1]))


if ( __name__ == "__main__" ):
    unittest.main()
