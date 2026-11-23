import unittest

from tools.singular_block_recovery import (
    recover_single_singular_block_equivalence, right_singular_block,
)


def matmul(a, b, p):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse_2(a, p):
    det = (a[0][0]*a[1][1] - a[0][1]*a[1][0]) % p
    inv = pow(det, -1, p)
    return [[a[1][1]*inv % p, -a[0][1]*inv % p],
            [-a[1][0]*inv % p, a[0][0]*inv % p]]


class SingularBlockRecoveryTests(unittest.TestCase):
    def test_canonical_right_block(self):
        q, k = right_singular_block(2, 3)
        result = recover_single_singular_block_equivalence(q, k, 3)
        self.assertTrue(result["recovered"])
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_recover_scrambled_right_block(self):
        q0, k0 = right_singular_block(2, 2)
        s0 = [[1, 1], [0, 1]]
        t0 = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
        si, ti = inverse_2(s0, 2), t0  # This t0 is its own inverse over F2.
        q = matmul(matmul(si, q0, 2), ti, 2)
        k = matmul(matmul(si, k0, 2), ti, 2)
        result = recover_single_singular_block_equivalence(q, k, 2)
        self.assertTrue(result["recovered"])
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_recover_left_singular_block(self):
        q, k = right_singular_block(2, 2)
        qt = [list(row) for row in zip(*q)]
        kt = [list(row) for row in zip(*k)]
        result = recover_single_singular_block_equivalence(qt, kt, 2, side="left")
        self.assertTrue(result["recovered"])
        self.assertEqual(result["shape"], [3, 2])

    def test_pair_budget_refuses_unbounded_search(self):
        q, k = right_singular_block(2, 3)
        result = recover_single_singular_block_equivalence(q, k, 3, max_pairs=10)
        self.assertFalse(result["recovered"])
        self.assertFalse(result["search_complete"])

    def test_wrong_shape_is_not_misclassified(self):
        result = recover_single_singular_block_equivalence([[1, 0], [0, 1]],
                                                            [[0, 1], [1, 0]], 3)
        self.assertFalse(result["recovered"])
        self.assertIn("shape", result["reason"])

    def test_invalid_side_and_budget(self):
        q, k = right_singular_block(1, 2)
        with self.assertRaises(ValueError):
            recover_single_singular_block_equivalence(q, k, 2, side="mixed")
        with self.assertRaises(ValueError):
            recover_single_singular_block_equivalence(q, k, 2, max_pairs=0)


if __name__ == "__main__":
    unittest.main()
