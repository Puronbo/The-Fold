import unittest
from tools.pencil_minimal_indices import rectangular_pencil_minimal_indices

def right_singular_block(epsilon):
    q = [[0] * (epsilon + 1) for _ in range(epsilon)]
    k = [[0] * (epsilon + 1) for _ in range(epsilon)]
    for i in range(epsilon):
        q[i][i + 1] = -1
        k[i][i] = 1
    return q, k

def block_diagonal_rectangular(blocks):
    rows = sum(len(q) for q, _ in blocks)
    cols = sum(len(q[0]) for q, _ in blocks)
    qo, ko = [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)]
    r = c = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qo[r+i][c+j], ko[r+i][c+j] = q[i][j], k[i][j]
        r += len(q); c += len(q[0])
    return qo, ko

class PencilMinimalIndexTests(unittest.TestCase):
    def test_right_minimal_index_one(self):
        q, k = right_singular_block(1)
        result = rectangular_pencil_minimal_indices(q, k, 3, max_degree=2)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["minimal_indices"], [1])
        self.assertEqual(result["left"]["minimal_indices"], [])

    def test_right_minimal_indices_one_and_two(self):
        q, k = block_diagonal_rectangular([right_singular_block(1), right_singular_block(2)])
        result = rectangular_pencil_minimal_indices(q, k, 5, max_degree=3)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["minimal_indices"], [1, 2])
        self.assertEqual(result["left"]["minimal_indices"], [])

    def test_left_minimal_index_two(self):
        q, k = right_singular_block(2)
        qt, kt = [list(c) for c in zip(*q)], [list(c) for c in zip(*k)]
        result = rectangular_pencil_minimal_indices(qt, kt, 3, max_degree=3)
        self.assertTrue(result["complete"])
        self.assertEqual(result["right"]["minimal_indices"], [])
        self.assertEqual(result["left"]["minimal_indices"], [2])

    def test_degree_bound_never_claims_false_completeness(self):
        q, k = right_singular_block(3)
        result = rectangular_pencil_minimal_indices(q, k, 3, max_degree=1)
        self.assertFalse(result["complete"])
        self.assertFalse(result["right"]["complete"])
        self.assertIsNone(result["right"]["minimal_indices"])
        self.assertEqual(result["right"]["expected_number_of_indices_from_normal_rank"], 1)

    def test_rejects_invalid_degree_bound(self):
        with self.assertRaises(ValueError):
            rectangular_pencil_minimal_indices([[1]], [[0]], 3, max_degree=-1)

if __name__ == "__main__":
    unittest.main()
