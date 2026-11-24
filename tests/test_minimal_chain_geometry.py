import unittest

from tools.minimal_chain_geometry import minimal_chain_geometry_certificate


def transpose(a):
    return [list(row) for row in zip(*a)]


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


class MinimalChainGeometryTests(unittest.TestCase):
    def test_mixed_canonical_chain_families_are_independent(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        q, k = block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])
        result = minimal_chain_geometry_certificate(q, k, 5, max_degree=2)
        self.assertTrue(result["profile_certificate_complete"])
        self.assertTrue(result["both_chain_families_independent"])
        self.assertEqual(result["right_domain_chain"]["rank"], 2)
        self.assertEqual(result["left_codomain_cochain"]["rank"], 2)
        self.assertFalse(result["right_domain_chain"]["full_domain_span"])
        self.assertFalse(result["left_codomain_cochain"]["full_codomain_cospan"])

    def test_regular_pencil_has_empty_chain_families(self):
        result = minimal_chain_geometry_certificate([[1, 0], [0, 1]],
                                                     [[0, 0], [0, 1]], 5,
                                                     max_degree=1)
        self.assertEqual(result["right_domain_chain"]["rank"], 0)
        self.assertEqual(result["left_codomain_cochain"]["rank"], 0)
        self.assertTrue(result["both_chain_families_independent"])


if __name__ == "__main__":
    unittest.main()
