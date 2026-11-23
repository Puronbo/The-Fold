import unittest

from tools.singular_only_pencil import recover_singular_only_pencil_structurally
from tools.strict_pencil_equivalence import _det_mod


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


def direct_sum_right(indices):
    m, n = sum(indices), sum(e+1 for e in indices)
    q, k = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
    ro = co = 0
    for e in indices:
        for j in range(e):
            q[ro+j][co+j] = 1
            k[ro+j][co+j+1] = 1
        ro += e
        co += e+1
    return q, k


class SingularOnlyPencilTests(unittest.TestCase):
    def test_single_and_multiple_right_blocks(self):
        for indices, p in (([1], 2), ([1, 2], 3), ([2, 2, 3], 5)):
            q, k = direct_sum_right(indices)
            result = recover_singular_only_pencil_structurally(q, k, p, max_degree=max(indices))
            self.assertTrue(result["recovered"], result.get("reason"))
            self.assertEqual(result["right_minimal_indices"], indices)
            self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_scrambled_multiple_blocks(self):
        p = 5
        q0, k0 = direct_sum_right([1, 2])
        s = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
        t = [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]
        q = matmul(matmul(inverse(s, p), q0, p), inverse(t, p), p)
        k = matmul(matmul(inverse(s, p), k0, p), inverse(t, p), p)
        result = recover_singular_only_pencil_structurally(q, k, p, max_degree=2)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_multiple_left_blocks(self):
        q, k = direct_sum_right([1, 2])
        result = recover_singular_only_pencil_structurally(transpose(q), transpose(k), 3,
                                                           side="left", max_degree=2)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["side"], "left")
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_mixed_left_right_refused(self):
        # Right L_1 direct sum with transpose(L_1).
        qr, kr = direct_sum_right([1])
        ql, kl = transpose(qr), transpose(kr)
        q = [[qr[0][0], qr[0][1], 0], [0, 0, ql[0][0]], [0, 0, ql[1][0]]]
        k = [[kr[0][0], kr[0][1], 0], [0, 0, kl[0][0]], [0, 0, kl[1][0]]]
        result = recover_singular_only_pencil_structurally(q, k, 3, max_degree=2)
        self.assertFalse(result["recovered"])

    def test_regular_component_refused(self):
        q, k = direct_sum_right([1])
        q = [q[0] + [1], [0, 0, 0]]
        k = [k[0] + [0], [0, 0, 1]]
        result = recover_singular_only_pencil_structurally(q, k, 3, max_degree=2)
        self.assertFalse(result["recovered"])

    def test_invalid_parameters(self):
        q, k = direct_sum_right([1])
        with self.assertRaises(ValueError):
            recover_singular_only_pencil_structurally(q, k, 2, side="both")
        with self.assertRaises(ValueError):
            recover_singular_only_pencil_structurally(q, k, 2, max_degree=-1)
        with self.assertRaises(ValueError):
            recover_singular_only_pencil_structurally(q, k, 2, max_minors=0)


if __name__ == "__main__":
    unittest.main()
