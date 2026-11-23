import copy
import unittest

from tools.pencil_smith_transform import polynomial_smith_transform
from tools.pencil_transform_audit import audit_polynomial_smith_transform


class PolynomialTransformAuditTests(unittest.TestCase):
    def test_valid_transform_has_unit_determinants(self):
        q, k = [[0, 1], [1, 0]], [[1, 0], [0, 1]]
        transform = polynomial_smith_transform(q, k, 5)
        audit = audit_polynomial_smith_transform(q, k, 5, transform)
        self.assertTrue(audit["independently_verified"])
        self.assertTrue(audit["U_determinant_is_nonzero_constant"])
        self.assertTrue(audit["V_determinant_is_nonzero_constant"])

    def test_tampered_transform_fails_identity(self):
        q, k = [[0, 1], [1, 0]], [[1, 0], [0, 1]]
        transform = copy.deepcopy(polynomial_smith_transform(q, k, 5))
        transform["left_transform_U"][0][0] = [2]
        audit = audit_polynomial_smith_transform(q, k, 5, transform)
        self.assertFalse(audit["transformation_identity_verified"])
        self.assertFalse(audit["independently_verified"])

    def test_nonunimodular_matrix_rejected_as_transform(self):
        q, k = [[1]], [[0]]
        transform = polynomial_smith_transform(q, k, 5)
        transform["left_transform_U"] = [[ [0, 1] ]]
        audit = audit_polynomial_smith_transform(q, k, 5, transform)
        self.assertFalse(audit["U_determinant_is_nonzero_constant"])
        self.assertFalse(audit["both_transforms_unimodular"])

    def test_rectangular_transforms_have_correct_determinant_sizes(self):
        q, k = [[0, -1]], [[1, 0]]
        transform = polynomial_smith_transform(q, k, 3)
        audit = audit_polynomial_smith_transform(q, k, 3, transform)
        self.assertTrue(audit["independently_verified"])

    def test_budget_and_shape_validation(self):
        transform = polynomial_smith_transform([[1, 0], [0, 1]], [[0, 0], [0, 0]], 3)
        with self.assertRaises(ValueError):
            audit_polynomial_smith_transform([[1, 0], [0, 1]], [[0, 0], [0, 0]], 3,
                                             transform, max_determinant_terms=1)
        transform["right_transform_V"] = [[ [1] ]]
        with self.assertRaises(ValueError):
            audit_polynomial_smith_transform([[1, 0], [0, 1]], [[0, 0], [0, 0]], 3,
                                             transform)


if __name__ == "__main__":
    unittest.main()
