import unittest

from tools.residual_pencil_decoupling_certificate import (
    _certificate_from_diagnostic,
    residual_pencil_decoupling_certificate,
)
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


class ResidualPencilDecouplingTests(unittest.TestCase):
    def test_canonical_mixed_pencil_reports_actual_basis_coupling(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        q, k = block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])
        result = residual_pencil_decoupling_certificate(q, k, 5, max_degree=2)
        self.assertFalse(result["decoupled"])
        self.assertTrue(result["exact_checks"]["adapted_strict_equivalence_verified"])
        self.assertFalse(result["exact_checks"]["certificate_verified"])
        self.assertTrue(any(
            item["Q_nonzero_entries"] or item["K_nonzero_entries"]
            for item in result["cross_coupling_obstructions"].values()
        ))
        self.assertEqual(result["residual_shape"], [2, 2])

    def test_zero_cross_coupling_certifies_exact_block_diagonal_pair(self):
        diagnostic = {
            "field": "F_5",
            "left_chain_cobasis_dimension": 1,
            "right_chain_basis_dimension": 1,
            "residual_shape": [1, 1],
            "Q_blocks": {
                "chain_to_chain": [[1]], "chain_to_domain_complement": [[]],
                "codomain_complement_from_chain": [[]], "residual": [[2]],
            },
            "K_blocks": {
                "chain_to_chain": [[0]], "chain_to_domain_complement": [[]],
                "codomain_complement_from_chain": [[]], "residual": [[3]],
            },
            "adapted_coordinates": {
                "adapted_Q": [[1, 0], [0, 2]],
                "adapted_K": [[0, 0], [0, 3]],
                "domain_basis_T": [[1, 0], [0, 1]],
                "codomain_cobasis_S": [[1, 0], [0, 1]],
                "verification": {"transformed_pair_exact": True},
            },
        }
        result = _certificate_from_diagnostic(diagnostic, 5)
        self.assertTrue(result["decoupled"])
        self.assertTrue(result["exact_checks"]["certificate_verified"])
        self.assertEqual(result["reconstructed_block_diagonal_Q"], [[1, 0], [0, 2]])
        self.assertEqual(result["reconstructed_block_diagonal_K"], [[0, 0], [0, 3]])

    def test_nonzero_coupling_is_reported_without_decomposition_claim(self):
        # A synthetic, exact diagnostic isolates the obstruction branch.
        empty = []
        diagnostic = {
            "field": "F_5",
            "left_chain_cobasis_dimension": 1,
            "right_chain_basis_dimension": 1,
            "residual_shape": [1, 1],
            "Q_blocks": {
                "chain_to_chain": [[1]], "chain_to_domain_complement": [[2]],
                "codomain_complement_from_chain": [[0]], "residual": [[3]],
            },
            "K_blocks": {
                "chain_to_chain": [[0]], "chain_to_domain_complement": [[0]],
                "codomain_complement_from_chain": [[4]], "residual": [[1]],
            },
            "adapted_coordinates": {
                "adapted_Q": [[1, 2], [0, 3]],
                "adapted_K": [[0, 0], [4, 1]],
                "domain_basis_T": [[1, 0], [0, 1]],
                "codomain_cobasis_S": [[1, 0], [0, 1]],
                "verification": {"transformed_pair_exact": True},
            },
        }
        result = _certificate_from_diagnostic(diagnostic, 5)
        self.assertFalse(result["decoupled"])
        self.assertEqual(result["cross_coupling_obstructions"][
            "chain_to_domain_complement"]["Q_rank"], 1)
        self.assertEqual(result["cross_coupling_obstructions"][
            "codomain_complement_from_chain"]["K_nonzero_entries"],
            [{"row": 0, "column": 0, "value": 4}])
        self.assertFalse(result["exact_checks"]["certificate_verified"])


if __name__ == "__main__":
    unittest.main()
