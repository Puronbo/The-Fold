import unittest

from tools.pencil_direct_sum_witness import verify_pencil_direct_sum_witness


class PencilDirectSumWitnessTests(unittest.TestCase):
    def test_verifies_scrambled_rectangular_direct_sum(self):
        # Source is a constant strict-equivalent scrambling of 1x2 plus 1x1.
        q0 = [[1, 0, 0], [0, 0, 1]]
        k0 = [[0, 1, 0], [0, 0, 1]]
        s = [[1, 1], [0, 1]]
        t = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
        # Inverse transformations over F_5.
        sinv = [[1, 4], [0, 1]]
        tinv = [[1, 4, 1], [0, 1, 4], [0, 0, 1]]
        q = _matmul(_matmul(sinv, q0, 5), tinv, 5)
        k = _matmul(_matmul(sinv, k0, 5), tinv, 5)
        result = verify_pencil_direct_sum_witness(q, k, 5, s, t, (1, 2))
        self.assertTrue(result["verification"]["direct_sum_verified"])
        self.assertEqual(result["second_block_shape"], [1, 1])
        self.assertEqual(result["Q_blocks"]["top_right"], [[0]])
        self.assertEqual(result["K_blocks"]["bottom_left"], [[0, 0]])

    def test_rejects_cross_coupling(self):
        q = [[1, 1], [0, 1]]
        k = [[0, 0], [0, 1]]
        result = verify_pencil_direct_sum_witness(
            q, k, 5, [[1, 0], [0, 1]], [[1, 0], [0, 1]], (1, 1)
        )
        self.assertFalse(result["verification"]["direct_sum_verified"])
        self.assertFalse(result["verification"]["Q_cross_blocks_zero"])

    def test_rejects_singular_transform(self):
        result = verify_pencil_direct_sum_witness(
            [[1]], [[0]], 5, [[0]], [[1]], (0, 0)
        )
        self.assertFalse(result["verification"]["left_transform_invertible"])
        self.assertFalse(result["verification"]["direct_sum_verified"])

    def test_validates_prime_and_partition(self):
        with self.assertRaises(ValueError):
            verify_pencil_direct_sum_witness(
                [[1]], [[0]], 4, [[1]], [[1]], (1, 1)
            )
        with self.assertRaises(ValueError):
            verify_pencil_direct_sum_witness(
                [[1]], [[0]], 5, [[1]], [[1]], (2, 0)
            )


def _matmul(a, b, p):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


if __name__ == "__main__":
    unittest.main()
