import unittest

from tools.pencil_nullspace_certificate import rectangular_pencil_nullspace_certificate


def right_block(e):
    q = [[0] * (e + 1) for _ in range(e)]
    k = [[0] * (e + 1) for _ in range(e)]
    for i in range(e):
        q[i][i + 1] = -1
        k[i][i] = 1
    return q, k


def left_block(e):
    q, k = right_block(e)
    return [list(c) for c in zip(*q)], [list(c) for c in zip(*k)]


def block_diag_rect(blocks):
    m = sum(len(q) for q, _ in blocks)
    n = sum(len(q[0]) for q, _ in blocks)
    qo, ko = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
    i0 = j0 = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qo[i0+i][j0+j], ko[i0+i][j0+j] = q[i][j], k[i][j]
        i0 += len(q)
        j0 += len(q[0])
    return qo, ko


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
