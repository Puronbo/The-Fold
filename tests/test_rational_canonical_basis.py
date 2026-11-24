import unittest

from tools.rational_canonical_basis import (
    construct_operator_similarity_witness,
    construct_rational_canonical_basis,
)
from tools.rational_canonical import _matmul
from tools.regular_pencil_profile import _inverse_mod


class RationalCanonicalBasisTests(unittest.TestCase):
    def test_full_basis_for_noncyclic_nilpotent_operator(self):
        # J_3(0) direct sum J_1(0): two elementary divisors x^3 and x.
        a = [[0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        result = construct_rational_canonical_basis(a, 2)
        self.assertTrue(result["basis_complete"])
        self.assertTrue(result["checks"]["basis_invertible"])
        self.assertTrue(result["checks"]["similarity_identity"])
        self.assertEqual(result["canonical_operator"], [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
        ])

    def test_mixed_primary_components(self):
        a = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = construct_rational_canonical_basis(a, 3)
        self.assertTrue(result["basis_complete"])
        self.assertTrue(result["checks"]["similarity_identity"])
        self.assertEqual(len(result["canonical_operator"]), 3)

    def test_constructs_intertwiner_for_similar_noncyclic_operators(self):
        a = [[0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        change = [[1, 1, 0, 0],
                  [0, 1, 1, 0],
                  [0, 0, 1, 1],
                  [0, 0, 0, 1]]
        inv = _inverse_mod(change, 2)
        b = _matmul(_matmul(change, a, 2), inv, 2)
        result = construct_operator_similarity_witness(a, b, 2)
        self.assertTrue(result["similar"])
        self.assertTrue(result["witness_found"])
        self.assertTrue(result["checks"]["intertwining_identity"])

    def test_profile_mismatch_proves_not_similar(self):
        a = [[0, 0], [0, 0]]
        b = [[0, 1], [0, 0]]
        result = construct_operator_similarity_witness(a, b, 2)
        self.assertFalse(result["similar"])
        self.assertTrue(result["decision_complete"])
        self.assertFalse(result["witness_found"])


if __name__ == "__main__":
    unittest.main()
