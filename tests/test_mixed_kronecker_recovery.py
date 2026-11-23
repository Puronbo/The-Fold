import unittest

from tools.mixed_kronecker_recovery import recover_mixed_kronecker_pencil


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b, p):
    return [[sum(a[i][z]*b[z][j] for z in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a, p):
    n = len(a)
    x = [[v % p for v in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for c in range(n):
        pivot = next(i for i in range(c, n) if x[i][c])
        x[c], x[pivot] = x[pivot], x[c]
        inv = pow(x[c][c], -1, p)
        x[c] = [v*inv % p for v in x[c]]
        for i in range(n):
            if i != c and x[i][c]:
                f = x[i][c]
                x[i] = [(u-f*v) % p for u, v in zip(x[i], x[c])]
    return [row[n:] for row in x]


def block_diag(blocks):
    rows = sum(len(q) for q, _ in blocks)
    cols = sum(len(q[0]) for q, _ in blocks)
    qout, kout = [[0]*cols for _ in range(rows)], [[0]*cols for _ in range(rows)]
    ro = co = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qout[ro+i][co+j], kout[ro+i][co+j] = q[i][j], k[i][j]
        ro += len(q)
        co += len(q[0])
    return qout, kout


def right_block(e):
    return ([[int(i == j) for j in range(e+1)] for i in range(e)],
            [[int(j == i+1) for j in range(e+1)] for i in range(e)])


class MixedKroneckerRecoveryTests(unittest.TestCase):
    def mixed_pair(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        return block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])

    def test_recovers_unscrambled_mixed_pencil(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["right_minimal_indices"], [1])
        self.assertEqual(result["left_minimal_indices"], [1])
        self.assertEqual(result["regular_dimension"], 1)
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_recovers_after_left_basis_shear(self):
        p = 5
        q, k = self.mixed_pair()
        scramble = [[1, 1, 0, 0], [0, 1, 0, 0],
                    [0, 0, 1, 0], [0, 0, 0, 1]]
        right_scramble = [[1, 0, 0, 0], [0, 1, 1, 0],
                          [0, 0, 1, 0], [0, 0, 0, 1]]
        si, ti = inverse(scramble, p), inverse(right_scramble, p)
        q = mm(mm(si, q, p), ti, p)
        k = mm(mm(si, k, p), ti, p)
        result = recover_mixed_kronecker_pencil(q, k, p, max_degree=2)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertTrue(result["verification"]["strict_equivalence_certified"])


    def test_exhaustive_mode_finds_exact_witness(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=2, max_candidates=1000,
            search_mode="exhaustive",
        )
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["search_mode"], "exhaustive")
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_exhaustive_budget_exhaustion_is_inconclusive(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=2, max_candidates=1,
            search_mode="exhaustive",
        )
        self.assertFalse(result["recovered"])
        self.assertFalse(result["decision_complete"])

    def test_rejects_unknown_search_mode(self):
        q, k = self.mixed_pair()
        with self.assertRaises(ValueError):
            recover_mixed_kronecker_pencil(
                q, k, 5, max_degree=2, search_mode="approximate"
            )

    def test_incomplete_profile_is_not_claimed_as_recovery(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=0, max_candidates=20
        )
        self.assertFalse(result["recovered"])
        self.assertFalse(result["decision_complete"])


if __name__ == "__main__":
    unittest.main()
