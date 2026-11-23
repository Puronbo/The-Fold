import unittest
from tools.pencil_kronecker import rectangular_pencil_kronecker_profile

def right_block(e):
    q = [[0]*(e+1) for _ in range(e)]
    k = [[0]*(e+1) for _ in range(e)]
    for i in range(e):
        q[i][i+1] = -1
        k[i][i] = 1
    return q, k

def left_block(e):
    q, k = right_block(e)
    return [list(c) for c in zip(*q)], [list(c) for c in zip(*k)]

def block_diag_rect(blocks):
    m, n = sum(len(q) for q, _ in blocks), sum(len(q[0]) for q, _ in blocks)
    qo, ko = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
    i0 = j0 = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qo[i0+i][j0+j], ko[i0+i][j0+j] = q[i][j], k[i][j]
        i0 += len(q); j0 += len(q[0])
    return qo, ko

class PencilKroneckerTests(unittest.TestCase):
    def test_regular_pencil(self):
        q, k = [[0,0],[0,1]], [[1,0],[0,0]]
        r = rectangular_pencil_kronecker_profile(q, k, 5, max_degree=2)
        self.assertTrue(r["complete_kronecker_structure_data"])
        self.assertEqual(r["regular_part"]["dimension"], 2)
        self.assertTrue(r["consistency_checks"]["all_checks_pass"])
        self.assertEqual(r["singular_part"]["right_minimal_indices"], [])
        self.assertEqual(r["singular_part"]["left_minimal_indices"], [])

    def test_right_and_left_singular_blocks(self):
        q, k = block_diag_rect([right_block(1), left_block(2)])
        r = rectangular_pencil_kronecker_profile(q, k, 3, max_degree=3)
        self.assertTrue(r["complete_kronecker_structure_data"])
        self.assertEqual(r["singular_part"]["right_minimal_indices"], [1])
        self.assertEqual(r["singular_part"]["left_minimal_indices"], [2])
        self.assertEqual(r["regular_part"]["dimension"], 0)

    def test_regular_plus_singular_components(self):
        regular = ([[0,0],[0,1]], [[1,0],[0,0]])
        q, k = block_diag_rect([regular, right_block(2)])
        r = rectangular_pencil_kronecker_profile(q, k, 5, max_degree=3)
        self.assertTrue(r["complete_kronecker_structure_data"])
        self.assertEqual(r["regular_part"]["dimension"], 2)
        self.assertEqual(r["singular_part"]["right_minimal_indices"], [2])

    def test_degree_cap_marks_report_incomplete(self):
        q, k = right_block(3)
        r = rectangular_pencil_kronecker_profile(q, k, 3, max_degree=1)
        self.assertFalse(r["complete_kronecker_structure_data"])
        self.assertIsNone(r["consistency_checks"]["all_checks_pass"])

if __name__ == "__main__":
    unittest.main()
