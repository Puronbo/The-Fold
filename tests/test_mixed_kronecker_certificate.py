import unittest

from tools.mixed_kronecker_certificate import verify_mixed_kronecker_decomposition


def transpose(a):
    return [list(row) for row in zip(*a)]


def block_diag(qs):
    rows, cols = sum(len(q) for q in qs), sum(len(q[0]) for q in qs)
    out = [[0]*cols for _ in range(rows)]
    ro = co = 0
    for q in qs:
        for i in range(len(q)):
            for j in range(len(q[0])):
                out[ro+i][co+j] = q[i][j]
        ro += len(q)
        co += len(q[0])
    return out


def right_block(e):
    return ([[int(i == j) for j in range(e+1)] for i in range(e)],
            [[int(j == i+1) for j in range(e+1)] for i in range(e)])


def left_block(e):
    q, k = right_block(e)
    return transpose(q), transpose(k)


def block_pencil(qs, ks):
    return block_diag(qs), block_diag(ks)


class MixedKroneckerCertificateTests(unittest.TestCase):
    def test_mixed_right_left_and_regular_component(self):
        r1, r2 = right_block(1), right_block(2)
        l1 = left_block(1)
        regq, regk = [[1, 0], [0, 1]], [[0, 1], [1, 1]]
        q, k = block_pencil([r1[0], l1[0], regq], [r1[1], l1[1], regk])
        result = verify_mixed_kronecker_decomposition(
            q, k, 5, right_minimal_indices=[1], left_minimal_indices=[1],
            regular_q=regq, regular_k=regk,
            left_transform=[[1]*0] if False else [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],
            right_transform=[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]],
        )
        self.assertTrue(result["decomposition_certified"])
        self.assertEqual(result["decomposition"]["regular_dimension"], 2)

    def test_nontrivial_constant_equivalence(self):
        rq, rk = right_block(1)
        lq, lk = left_block(1)
        regq, regk = [[1]], [[1]]
        q0, k0 = block_pencil([rq, lq, regq], [rk, lk, regk])
        # Apply S^{-1} on rows and T^{-1} on columns, then supply S,T.
        s = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]]
        t = [[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,1]]
        si = [[1,4,1,4],[0,1,4,1],[0,0,1,4],[0,0,0,1]]
        ti = [[1,4,1,4,1],[0,1,4,1,4],[0,0,1,4,1],[0,0,0,1,4],[0,0,0,0,1]]
        def mm(a,b):
            return [[sum(a[i][z]*b[z][j] for z in range(len(b)))%5 for j in range(len(b[0]))] for i in range(len(a))]
        q, k = mm(mm(si,q0),ti), mm(mm(si,k0),ti)
        result = verify_mixed_kronecker_decomposition(
            q,k,5,right_minimal_indices=[1],left_minimal_indices=[1],
            regular_q=regq,regular_k=regk,left_transform=s,right_transform=t)
        self.assertTrue(result["decomposition_certified"])

    def test_singular_regular_component_rejected(self):
        q, k = [[1]], [[0]]
        with self.assertRaises(ValueError):
            verify_mixed_kronecker_decomposition(
                q,k,3,regular_q=q,regular_k=k,
                left_transform=[[1]],right_transform=[[1]])

    def test_wrong_dimension_rejected(self):
        q, k = [[1]], [[0]]
        with self.assertRaises(ValueError):
            verify_mixed_kronecker_decomposition(
                q,k,3,right_minimal_indices=[1],
                left_transform=[[1]],right_transform=[[1,0],[0,1]])

    def test_tampered_witness_not_certified(self):
        rq,rk=right_block(1)
        result=verify_mixed_kronecker_decomposition(
            rq,rk,3,right_minimal_indices=[1],
            left_transform=[[1]],right_transform=[[0,1],[1,0]])
        self.assertFalse(result["decomposition_certified"])

    def test_zero_minimal_index_rejected_explicitly(self):
        q,k=right_block(1)
        with self.assertRaises(ValueError):
            verify_mixed_kronecker_decomposition(
                q,k,3,right_minimal_indices=[0],
                left_transform=[[1]],right_transform=[[1,0],[0,1]])


if __name__ == "__main__":
    unittest.main()
