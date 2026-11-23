import unittest

from tools.singular_block_recovery import right_singular_block
from tools.structural_singular_block import recover_single_singular_block_structurally


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b, p):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a, p):
    n = len(a)
    x = [[v % p for v in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for c in range(n):
        r = next(i for i in range(c, n) if x[i][c])
        x[c], x[r] = x[r], x[c]
        z = pow(x[c][c], -1, p)
        x[c] = [v*z % p for v in x[c]]
        for i in range(n):
            if i != c:
                z = x[i][c]
                x[i] = [(u-z*v) % p for u, v in zip(x[i], x[c])]
    return [row[n:] for row in x]


class StructuralSingularBlockTests(unittest.TestCase):
    def test_canonical_right_blocks_multiple_indices(self):
        for e, p in ((1, 2), (2, 3), (3, 5)):
            q, k = right_singular_block(e, p)
            result = recover_single_singular_block_structurally(q, k, p)
            self.assertTrue(result["recovered"], result.get("reason"))
            self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_recover_nontrivially_scrambled_block(self):
        p = 5
        q0, k0 = right_singular_block(2, p)
        s = [[1, 2], [0, 1]]
        t = [[1, 1, 0], [0, 1, 2], [0, 0, 1]]
        q = matmul(matmul(inverse(s, p), q0, p), inverse(t, p), p)
        k = matmul(matmul(inverse(s, p), k0, p), inverse(t, p), p)
        result = recover_single_singular_block_structurally(q, k, p)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_recover_left_block(self):
        q, k = right_singular_block(2, 3)
        result = recover_single_singular_block_structurally(transpose(q), transpose(k), 3, side="left")
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["shape"], [3, 2])

    def test_mixed_pencil_refused(self):
        q, k = right_singular_block(1, 3)
        # Append a regular 1x1 block: no longer a single right singular block.
        q = [q[0] + [1], [0, 0, 0]]
        k = [k[0] + [0], [0, 0, 1]]
        result = recover_single_singular_block_structurally(q, k, 3)
        self.assertFalse(result["recovered"])

    def test_regular_square_pencil_refused(self):
        result = recover_single_singular_block_structurally([[1]], [[0]], 3)
        self.assertFalse(result["recovered"])

    def test_invalid_side_and_minor_budget(self):
        q, k = right_singular_block(1, 2)
        with self.assertRaises(ValueError):
            recover_single_singular_block_structurally(q, k, 2, side="both")
        with self.assertRaises(ValueError):
            recover_single_singular_block_structurally(q, k, 2, max_minors=0)


if __name__ == "__main__":
    unittest.main()
