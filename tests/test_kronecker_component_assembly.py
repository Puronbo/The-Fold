import unittest

from tools.kronecker_component_assembly import assemble_kronecker_components


def transpose(a):
    return [list(row) for row in zip(*a)]


def right_block(e):
    return (
        [[int(i == j) for j in range(e + 1)] for i in range(e)],
        [[int(j == i + 1) for j in range(e + 1)] for i in range(e)],
    )


class KroneckerComponentAssemblyTests(unittest.TestCase):
    def test_assembles_right_left_and_regular_components(self):
        rq, rk = right_block(1)
        rleft_q, rleft_k = right_block(1)
        lq, lk = transpose(rleft_q), transpose(rleft_k)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk, "minimal_index": 1},
            {"kind": "left", "q": lq, "k": lk, "minimal_index": 1},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        self.assertTrue(result["assembly_complete"])
        self.assertEqual(result["component_count"], 3)
        self.assertEqual(result["source_shape"], [4, 4])
        self.assertTrue(result["checks"]["global_strict_equivalence_verified"])
        self.assertTrue(result["global_strict_equivalence_audit"]["strict_equivalence_certified"])

    def test_rejects_incorrect_declared_minimal_index(self):
        q, k = right_block(1)
        with self.assertRaises(ValueError):
            assemble_kronecker_components([
                {"kind": "right", "q": q, "k": k, "minimal_index": 2},
            ], 3)

    def test_reports_component_recovery_failure(self):
        # A regular square pencil is not a single right singular block.
        result = assemble_kronecker_components([
            {"kind": "right", "q": [[1]], "k": [[0]]},
        ], 3)
        self.assertFalse(result["assembly_complete"])
        self.assertEqual(result["failed_component_index"], 0)

    def test_requires_nonempty_component_list(self):
        with self.assertRaises(ValueError):
            assemble_kronecker_components([], 3)


if __name__ == "__main__":
    unittest.main()
