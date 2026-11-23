import unittest

from tools.minimal_chain_adapted_coordinates import minimal_chain_adapted_coordinates
from tools.residual_pencil_diagnostic import residual_pencil_diagnostic


def transpose(a):
    return [list(row) for row in zip(*a)]


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


class ResidualPencilDiagnosticTests(unittest.TestCase):
    def test_square_residual_profile_is_reported_but_not_overclaimed(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        q, k = block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])
        result = residual_pencil_diagnostic(q, k, 5, max_degree=2)
        self.assertEqual(result["residual_shape"], [2, 2])
        self.assertTrue(result["residual_is_square"])
        self.assertTrue(result["residual_is_nonempty"])
        self.assertIsNotNone(result["residual_kronecker_profile"])
        self.assertTrue(result["residual_kronecker_profile"]["complete_kronecker_structure_data"])
        self.assertIn("not a source-pencil invariant", result["residual_profile_scope"])

    def test_nonsquare_residual_does_not_attempt_square_profile(self):
        rq, rk = right_block(1)
        q, k = rq, rk
        result = residual_pencil_diagnostic(q, k, 5, max_degree=2)
        self.assertEqual(result["residual_shape"], [1, 0])
        self.assertFalse(result["residual_is_square"])
        self.assertIsNone(result["residual_kronecker_profile"])


if __name__ == "__main__":
    unittest.main()
