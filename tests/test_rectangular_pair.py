import unittest

from tools.rectangular_pair import analyze_rectangular_pair


def matmul(a, b, p):
    return [[sum(x * y for x, y in zip(row, col)) % p
             for col in zip(*b)] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


class RectangularPairTests(unittest.TestCase):
    def test_rectangular_pair_has_projective_profile(self):
        q = [[1, 0, 0], [0, 1, 0]]
        k = [[0, 1, 0], [1, 0, 1]]
        result = analyze_rectangular_pair(q, k, 3)
        self.assertEqual(result["shape"], [2, 3])
        self.assertEqual(result["individual_ranks"], {"q": 2, "k": 2})
        self.assertEqual(len(result["projective_pencil_rank_profile"]), 4)
        self.assertEqual(sum(result["projective_rank_histogram"].values()), 4)

    def test_same_individual_ranks_can_have_different_pencil_profiles(self):
        identity = [[1, 0], [0, 1]]
        swap = [[0, 1], [1, 0]]
        same = analyze_rectangular_pair(identity, identity, 3)
        different = analyze_rectangular_pair(identity, swap, 3)
        self.assertEqual(same["individual_ranks"], different["individual_ranks"])
        self.assertNotEqual(same["projective_pencil_rank_profile"],
                            different["projective_pencil_rank_profile"])

    def test_invariant_under_shared_left_and_right_basis_changes(self):
        p = 5
        q = [[1, 2, 0], [0, 1, 1]]
        k = [[0, 1, 1], [2, 0, 1]]
        # S is 2x2 invertible; T is 3x3 invertible over F_5.
        s = [[1, 1], [0, 1]]
        t = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
        t_inv = [[1, 4, 1], [0, 1, 4], [0, 0, 1]]
        s_inv = [[1, 4], [0, 1]]
        self.assertEqual(matmul(s, s_inv, p), [[1, 0], [0, 1]])
        self.assertEqual(matmul(t, t_inv, p), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        def transform(a):
            return matmul(matmul(s, a, p), t_inv, p)

        original = analyze_rectangular_pair(q, k, p)
        changed = analyze_rectangular_pair(transform(q), transform(k), p)
        self.assertEqual(original["individual_ranks"], changed["individual_ranks"])
        self.assertEqual(original["joint_ranks"], changed["joint_ranks"])
        self.assertEqual(original["projective_pencil_rank_profile"],
                         changed["projective_pencil_rank_profile"])

    def test_rejects_shape_mismatch_and_invalid_prime(self):
        with self.assertRaises(ValueError):
            analyze_rectangular_pair([[1, 0]], [[1], [0]], 3)
        with self.assertRaises(ValueError):
            analyze_rectangular_pair([[1]], [[1]], 4)
        with self.assertRaises(ValueError):
            analyze_rectangular_pair([[]], [[]], 3)


if __name__ == "__main__":
    unittest.main()
