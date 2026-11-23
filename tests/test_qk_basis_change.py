import unittest

from tools.qk_basis_change import analyze_qk_basis_change


class QKBasisChangeTests(unittest.TestCase):
    def test_unimodular_shear_preserves_interaction_profile(self):
        q = [[1, 2, 0], [0, 1, 1]]
        k = [[2, 0, 1], [1, 1, 0]]
        # B = [[1,1,0],[0,1,0],[0,0,1]], det(B)=1.
        b = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
        # B^(-T) = [[1,0,0],[-1,1,0],[0,0,1]].
        inverse_transpose = [[1, 0, 0], [-1, 1, 0], [0, 0, 1]]
        result = analyze_qk_basis_change(q, k, b, inverse_transpose, [2, 3, 5, 7])
        self.assertTrue(result["interaction"]["same_full_finite_field_profiles"])
        self.assertTrue(result["individual_projection_ranks"]["q"]["preserved"])
        self.assertTrue(result["individual_projection_ranks"]["k"]["preserved"])

    def test_square_projection_profiles_need_not_be_invariant(self):
        q = [[1, 2], [0, 1]]
        k = [[2, 0], [1, 1]]
        b = [[1, 1], [0, 1]]
        inverse_transpose = [[1, 0], [-1, 1]]
        result = analyze_qk_basis_change(q, k, b, inverse_transpose, [3, 5])
        self.assertTrue(result["interaction"]["same_full_finite_field_profiles"])
        # Individual matrices are changed by right multiplication, not similarity.
        self.assertEqual(result["individual_projection_ranks"]["q"]["before"],
                         result["individual_projection_ranks"]["q"]["after"])
        self.assertEqual(result["individual_projection_ranks"]["k"]["before"],
                         result["individual_projection_ranks"]["k"]["after"])

    def test_rejects_non_inverse_and_non_unimodular_basis(self):
        with self.assertRaises(ValueError):
            analyze_qk_basis_change([[1]], [[1]], [[2]], [[1]], [3])
        with self.assertRaises(ValueError):
            analyze_qk_basis_change([[1]], [[1]], [[1, 0]], [[1]], [3])

    def test_requires_primes(self):
        with self.assertRaises(ValueError):
            analyze_qk_basis_change([[1]], [[1]], [[1]], [[1]], [])


if __name__ == "__main__":
    unittest.main()
