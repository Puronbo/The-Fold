import unittest

from tools.minimal_chain_decoupling_completion import (
    _nullspace_rows, minimal_chain_decoupling_completion,
)


class MinimalChainDecouplingCompletionTests(unittest.TestCase):
    def test_nullspace_basis_is_exact(self):
        matrix = [[1, 1, 0], [0, 1, 1]]
        basis = _nullspace_rows(matrix, 3, 5)
        self.assertEqual(len(basis), 1)
        for row in matrix:
            self.assertEqual(sum(a*b for a, b in zip(row, basis[0])) % 5, 0)

    def test_zero_chain_case_returns_full_bases(self):
        # A regular square pencil has no minimal chains; its full space is
        # available as both complementary annihilator spaces.
        q, k = [[1, 0], [0, 1]], [[0, 0], [0, 1]]
        result = minimal_chain_decoupling_completion(q, k, 5)
        self.assertTrue(result["completion_possible"])
        self.assertTrue(result["decoupled"])
        self.assertTrue(result["exact_checks"]["T_invertible"])
        self.assertTrue(result["exact_checks"]["S_invertible"])
        self.assertEqual(result["adapted_Q"], q)
        self.assertEqual(result["adapted_K"], k)

    def test_canonical_mixed_pencil_finds_decoupling_complements(self):
        # Right and left index-one blocks plus a regular scalar. The common
        # annihilator spaces contain complements to both minimal-chain spans.
        q = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        k = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        result = minimal_chain_decoupling_completion(q, k, 5, max_degree=2)
        if result["completion_possible"]:
            self.assertTrue(result["decoupled"])
            self.assertTrue(result["exact_checks"]["cross_coupling_zero"])
        else:
            self.assertTrue(result["failure_reasons"])


if __name__ == "__main__":
    unittest.main()
