import unittest

from tools.minimal_chain_adapted_coordinates import minimal_chain_adapted_coordinates


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b, p):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def block_diag(blocks):
    rows = sum(len(q) for q, _ in blocks)
    cols = sum(len(q[0]) for q, _ in blocks)
    qo, ko = [[0]*cols for _ in range(rows)], [[0]*cols for _ in range(rows)]
    ro = co = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qo[ro+i][co+j], ko[ro+i][co+j] = q[i][j], k[i][j]
        ro += len(q)
        co += len(q[0])
    return qo, ko


def right_block(e):
    return ([[int(i == j) for j in range(e+1)] for i in range(e)],
            [[int(j == i+1) for j in range(e+1)] for i in range(e)])


class MinimalChainAdaptedCoordinatesTests(unittest.TestCase):
    def test_mixed_canonical_pencil_gets_exact_adapted_bases(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        q, k = block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])
        result = minimal_chain_adapted_coordinates(q, k, 5, max_degree=2)
        self.assertTrue(result["verification"]["left_transform_invertible"])
        self.assertTrue(result["verification"]["right_transform_invertible"])
        self.assertEqual(result["right_chain_basis_dimension"], 2)
        self.assertEqual(result["left_chain_cobasis_dimension"], 2)
        self.assertEqual(result["adapted_Q"], matmul(matmul(result["codomain_cobasis_S"], q, 5), result["domain_basis_T"], 5))
        self.assertEqual(result["adapted_K"], matmul(matmul(result["codomain_cobasis_S"], k, 5), result["domain_basis_T"], 5))
        self.assertEqual(result["basis_completion"]["domain_complement_dimension"], 2)
        self.assertEqual(result["basis_completion"]["codomain_complement_dimension"], 2)

    def test_scrambled_mixed_pencil_still_has_certified_adapted_coordinates(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        q, k = block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])
        # Invertible elementary row and column operations over F_5.
        left = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [0,0,0,1]]
        right = [[1,0,0,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
        qs, ks = matmul(matmul(left, q, 5), right, 5), matmul(matmul(left, k, 5), right, 5)
        result = minimal_chain_adapted_coordinates(qs, ks, 5, max_degree=3)
        self.assertTrue(result["verification"]["transformed_pair_exact"])
        self.assertTrue(result["profile_certificate_complete"])
        self.assertEqual(result["right_chain_basis_dimension"], 2)
        self.assertEqual(result["left_chain_cobasis_dimension"], 2)


if __name__ == "__main__":
    unittest.main()
