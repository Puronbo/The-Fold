import unittest

from tools.pure_singular_pencil_recovery import recover_pure_singular_pencil_structurally


def transpose(a):
    return [list(row) for row in zip(*a)]


def block_diag_rect(blocks):
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
    return (
        [[int(i == j) for j in range(e+1)] for i in range(e)],
        [[int(j == i+1) for j in range(e+1)] for i in range(e)],
    )


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
        z = pow(x[c][c], -1, p)
        x[c] = [v*z % p for v in x[c]]
        for i in range(n):
            if i != c:
                z = x[i][c]
                x[i] = [(u-z*v) % p for u, v in zip(x[i], x[c])]
    return [row[n:] for row in x]


class PureSingularPencilRecoveryTests(unittest.TestCase):
    def test_multiple_right_blocks(self):
        q, k = block_diag_rect([right_block(1), right_block(2)])
        result = recover_pure_singular_pencil_structurally(q, k, 5, max_degree=3)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["minimal_indices"], [1, 2])
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_multiple_left_blocks(self):
        q, k = block_diag_rect([
            (transpose(right_block(1)[0]), transpose(right_block(1)[1])),
            (transpose(right_block(2)[0]), transpose(right_block(2)[1])),
        ])
        result = recover_pure_singular_pencil_structurally(q, k, 5, side="left", max_degree=3)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["minimal_indices"], [1, 2])
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_recovers_scrambled_multiple_right_blocks(self):
        p = 5
        q, k = block_diag_rect([right_block(1), right_block(2)])
        s = [[1,1,0],[0,1,1],[0,0,1]]
        t = [[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,1]]
        si, ti = inverse(s,p), inverse(t,p)
        q, k = mm(mm(si,q,p),ti,p), mm(mm(si,k,p),ti,p)
        result = recover_pure_singular_pencil_structurally(q,k,p,max_degree=3)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["minimal_indices"], [1,2])
        self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_rejects_regular_component(self):
        result = recover_pure_singular_pencil_structurally([[1]], [[0]], 3)
        self.assertFalse(result["recovered"])


if __name__ == "__main__":
    unittest.main()
