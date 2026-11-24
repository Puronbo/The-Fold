import unittest

from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit


class StrictPencilEquivalenceTests(unittest.TestCase):
    def test_right_singular_block_identity_witness(self):
        q = [[1, 0, 0], [0, 1, 0]]
        k = [[0, 1, 0], [0, 0, 1]]
        result = strict_pencil_equivalence_audit(q, k, 5, q, k,
                                                 [[1, 0], [0, 1]],
                                                 [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(result["strict_equivalence_certified"])

    def test_nontrivial_constant_basis_change(self):
        q = [[1, 0, 0], [0, 1, 0]]
        k = [[0, 1, 0], [0, 0, 1]]
        s = [[1, 1], [0, 1]]
        t = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
        qi = [[sum(s[i][a] * q[a][b] * t[b][j] for a in range(2) for b in range(3)) % 7
               for j in range(3)] for i in range(2)]
        ki = [[sum(s[i][a] * k[a][b] * t[b][j] for a in range(2) for b in range(3)) % 7
               for j in range(3)] for i in range(2)]
        result = strict_pencil_equivalence_audit(q, k, 7, qi, ki, s, t)
        self.assertTrue(result["strict_equivalence_certified"])

    def test_polynomial_only_witness_is_not_accepted_as_constant(self):
        q, k = [[1]], [[0]]
        result = strict_pencil_equivalence_audit(q, k, 5, q, k, [[1]], [[1]])
        self.assertTrue(result["strict_equivalence_certified"])
        # A polynomial transform is not part of this API; nonconstant entries
        # are rejected by integer conversion rather than interpreted as polynomials.
        with self.assertRaises((TypeError, ValueError)):
            strict_pencil_equivalence_audit(q, k, 5, q, k, [[[1, 1]]], [[1]])

    def test_singular_candidate_rejected(self):
        q, k = [[1, 0], [0, 1]], [[0, 0], [0, 0]]
        result = strict_pencil_equivalence_audit(q, k, 3, q, k,
                                                 [[1, 0], [0, 0]],
                                                 [[1, 0], [0, 1]])
        self.assertFalse(result["left_transform_invertible"])
        self.assertFalse(result["strict_equivalence_certified"])

    def test_tampered_target_rejected(self):
        q, k = [[1, 0], [0, 1]], [[0, 1], [1, 0]]
        result = strict_pencil_equivalence_audit(q, k, 3, [[1, 0], [0, 0]], k,
                                                 [[1, 0], [0, 1]],
                                                 [[1, 0], [0, 1]])
        self.assertFalse(result["constant_strict_equivalence_Q_verified"])
        self.assertFalse(result["strict_equivalence_certified"])

    def test_shape_validation(self):
        with self.assertRaises(ValueError):
            strict_pencil_equivalence_audit([[1, 0]], [[0, 1]], 3,
                                             [[1, 0], [0, 1]], [[0, 1], [1, 0]],
                                             [[1]], [[1, 0], [0, 1]])


if __name__ == "__main__":
    unittest.main()
