import copy
import unittest

from tools.kronecker_component_assembly import (
    _component_witness_composition_audit,
    assemble_kronecker_components,
)


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
        self.assertEqual(result["canonical_block_shapes"], [[1, 2], [2, 1], [1, 1]])
        self.assertTrue(result["checks"]["global_strict_equivalence_verified"])
        self.assertTrue(result["checks"]["multi_block_direct_sum_verified"])
        self.assertTrue(result["checks"]["component_consistency_verified"])
        self.assertTrue(result["checks"]["all_component_witnesses_verified"])
        self.assertTrue(result["checks"]["component_witness_composition_verified"])
        self.assertEqual(len(result["component_witness_audits"]), 3)
        self.assertTrue(all(a["strict_equivalence_certified"] for a in result["component_witness_audits"]))
        consistency = result["component_consistency_audit"]
        self.assertTrue(consistency["consistency_verified"])
        self.assertEqual(consistency["component_count"], 3)
        self.assertEqual(consistency["source_block_shapes"], [[1, 2], [2, 1], [1, 1]])
        self.assertEqual(consistency["canonical_block_shapes"], result["canonical_block_shapes"])
        self.assertTrue(all(consistency["checks"].values()))
        multi = result["multi_block_direct_sum_audit"]
        self.assertTrue(multi["verification"]["direct_sum_verified"])
        self.assertEqual(multi["block_shapes"], result["canonical_block_shapes"])
        self.assertTrue(result["global_strict_equivalence_audit"]["strict_equivalence_certified"])
        composition = result["component_witness_composition_audit"]
        self.assertTrue(composition["composition_verified"])
        self.assertTrue(all(composition["checks"].values()))
        self.assertEqual(composition["reconstructed_left_transform_S"], result["left_transform_S"])
        self.assertEqual(composition["reconstructed_right_transform_T"], result["right_transform_T"])
        self.assertTrue(composition["replayed_global_strict_equivalence_audit"]["strict_equivalence_certified"])


    def test_composition_audit_detects_a_tampered_local_transform(self):
        rq, rk = right_block(1)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        altered = copy.deepcopy(result["component_witness_audits"])
        altered[0]["left_transform"][0][0] = (
            altered[0]["left_transform"][0][0] + 1
        ) % 5
        audit = _component_witness_composition_audit(
            altered, result["left_transform_S"], result["right_transform_T"],
            result["source_Q"], result["source_K"],
            result["canonical_Q"], result["canonical_K"], 5,
        )
        self.assertFalse(audit["composition_verified"])
        self.assertFalse(
            audit["checks"]["reconstructed_left_transform_matches_assembled"]
        )
        self.assertFalse(
            audit["checks"]["reconstructed_global_strict_equivalence_verified"]
        )

    def test_composition_audit_rejects_dimension_incompatible_certificate(self):
        rq, rk = right_block(1)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        altered = copy.deepcopy(result["component_witness_audits"])
        altered[0]["left_transform"].append([0])
        with self.assertRaisesRegex(ValueError, "must be square"):
            _component_witness_composition_audit(
                altered, result["left_transform_S"], result["right_transform_T"],
                result["source_Q"], result["source_K"],
                result["canonical_Q"], result["canonical_K"], 5,
            )

    def test_composition_audit_rejects_empty_or_malformed_certificate_lists(self):
        rq, rk = right_block(1)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        args = (
            result["left_transform_S"], result["right_transform_T"],
            result["source_Q"], result["source_K"],
            result["canonical_Q"], result["canonical_K"], 5,
        )
        with self.assertRaisesRegex(ValueError, "nonempty ordered sequence"):
            _component_witness_composition_audit([], *args)
        malformed = [{"left_transform": [[1, 0]], "right_transform": [[1, 0], [0, 1]]}]
        with self.assertRaisesRegex(ValueError, "left_transform.*square"):
            _component_witness_composition_audit(malformed, *args)

    def test_rejects_incorrect_declared_minimal_index(self):
        q, k = right_block(1)
        with self.assertRaises(ValueError):
            assemble_kronecker_components([
                {"kind": "right", "q": q, "k": k, "minimal_index": 2},
            ], 3)

    def test_reports_component_recovery_failure_without_audit(self):
        result = assemble_kronecker_components([
            {"kind": "right", "q": [[1]], "k": [[0]]},
        ], 3)
        self.assertFalse(result["assembly_complete"])
        self.assertEqual(result["failed_component_index"], 0)
        self.assertNotIn("multi_block_direct_sum_audit", result)
        self.assertNotIn("component_consistency_audit", result)
        self.assertNotIn("component_witness_audits", result)
        self.assertNotIn("component_witness_composition_audit", result)

    def test_requires_nonempty_component_list(self):
        with self.assertRaises(ValueError):
            assemble_kronecker_components([], 3)


if __name__ == "__main__":
    unittest.main()
