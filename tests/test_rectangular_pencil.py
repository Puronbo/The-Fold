import unittest

from tools.rectangular_pencil import rectangular_pencil_fingerprint


def matmul(a, b, p):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


class RectangularPencilTests(unittest.TestCase):
    def test_same_individual_ranks_different_pencil_profiles(self):
        identity = [[1, 0], [0, 1]]
        swap = [[0, 1], [1, 0]]
        same_pair = rectangular_pencil_fingerprint(identity, identity, 2)
        distinct_pair = rectangular_pencil_fingerprint(identity, swap, 2)
        self.assertEqual(same_pair["rank_q"], distinct_pair["rank_q"])
        self.assertEqual(same_pair["rank_k"], distinct_pair["rank_k"])
        self.assertEqual(
            [x["rank"] for x in same_pair["projective_rank_profile"]],
            [2, 0, 2],
        )
        self.assertEqual(
            [x["rank"] for x in distinct_pair["projective_rank_profile"]],
            [2, 1, 2],
        )

    def test_shared_left_and_right_basis_changes_preserve_profile(self):
        q = [[1, 2], [0, 1]]
        k = [[0, 1], [1, 1]]
        s = [[0, 1], [1, 0]]
        t_inverse = [[1, 4], [0, 1]]
        q2 = matmul(matmul(s, q, 5), t_inverse, 5)
        k2 = matmul(matmul(s, k, 5), t_inverse, 5)
        before = rectangular_pencil_fingerprint(q, k, 5)
        after = rectangular_pencil_fingerprint(q2, k2, 5)
        for key in (
            "rank_q", "rank_k", "horizontal_concatenation_rank",
            "vertical_stack_rank", "projective_rank_profile",
            "projective_rank_distribution",
        ):
            self.assertEqual(before[key], after[key])

    def test_rectangular_maps_are_not_padded(self):
        q = [[1, 0, 1], [0, 1, 1]]
        k = [[0, 1, 0], [1, 0, 1]]
        result = rectangular_pencil_fingerprint(q, k, 3)
        self.assertEqual(result["shape"], [2, 3])
        self.assertEqual(result["projective_point_count"], 4)
        self.assertEqual(len(result["projective_rank_profile"]), 4)

    def test_rejects_shape_mismatch_and_composite_modulus(self):
        with self.assertRaises(ValueError):
            rectangular_pencil_fingerprint([[1, 0]], [[1]], 5)
        with self.assertRaises(ValueError):
            rectangular_pencil_fingerprint([[1]], [[1]], 4)

    def test_rejects_ragged_and_empty_matrices(self):
        with self.assertRaises(ValueError):
            rectangular_pencil_fingerprint([[1], [1, 0]], [[1], [0, 1]], 3)
        with self.assertRaises(ValueError):
            rectangular_pencil_fingerprint([], [], 3)


if __name__ == "__main__":
    unittest.main()
