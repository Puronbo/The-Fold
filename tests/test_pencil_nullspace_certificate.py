import unittest

from tools.pencil_nullspace_certificate import rectangular_pencil_nullspace_certificate
from tests.test_pencil_kronecker import right_block, left_block, block_diag_rect


class PencilNullspaceCertificateTests(unittest.TestCase):
    def test_right_and_left_generators_are_exact(self):
        q, k = block_diag_rect([right_block(1), left_block(2)])
        result = rectangular_pencil_nullspace_certificate(q, k, 3, max_degree=3)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["minimal_indices"], [1])
        self.assertEqual(result["left"]["minimal_indices"], [2])
        for side in ("right", "left"):
            self.assertTrue(result[side]["all_polynomial_products_verified_zero"])
            self.assertTrue(all(x["spans_entire_bounded_kernel"] for x in result[side]["bounded_span_checks"]))

    def test_multiple_generators_same_degree(self):
        q, k = block_diag_rect([right_block(1), right_block(1)])
        result = rectangular_pencil_nullspace_certificate(q, k, 5, max_degree=2)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["minimal_indices"], [1, 1])
        self.assertEqual(result["right"]["recovered_generator_count"], 2)

    def test_zero_minimal_index(self):
        q, k = [[0]], [[0]]
        result = rectangular_pencil_nullspace_certificate(q, k, 3, max_degree=0)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["minimal_indices"], [0])
        self.assertEqual(result["left"]["minimal_indices"], [0])

    def test_degree_cap_is_not_silently_complete(self):
        q, k = right_block(3)
        result = rectangular_pencil_nullspace_certificate(q, k, 3, max_degree=1)
        self.assertFalse(result["complete"])
        self.assertIsNone(result["right"]["minimal_indices"])

    def test_regular_pencil_has_empty_kernel_bases(self):
        q, k = [[0, 0], [0, 1]], [[1, 0], [0, 0]]
        result = rectangular_pencil_nullspace_certificate(q, k, 5, max_degree=1)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["generators"], [])
        self.assertEqual(result["left"]["generators"], [])


if __name__ == "__main__":
    unittest.main()
