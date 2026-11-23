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
        self.assertEqual(len(composition["per_component_replayed_audits"]), 3)
        self.assertTrue(all(a["strict_equivalence_certified"] for a in composition["per_component_replayed_audits"]))
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
            [rq, [[1]]], [rk, [[0]]],
            [right_block(1)[0], [[1]]], [right_block(1)[1], [[0]]],
        )
        self.assertFalse(audit["composition_verified"])
        self.assertFalse(
            audit["checks"]["reconstructed_left_transform_matches_assembled"]
        )
        self.assertFalse(
            audit["checks"]["reconstructed_global_strict_equivalence_verified"]
        )

    def test_composition_audit_replays_changed_source_and_canonical_blocks(self):
        rq, rk = right_block(1)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        audits = copy.deepcopy(result["component_witness_audits"])
        # A forged stored success flag cannot rescue a changed source block.
        audits[1]["strict_equivalence_certified"] = True
        changed_source = [rq, [[2]]]
        source_audit = _component_witness_composition_audit(
            audits, result["left_transform_S"], result["right_transform_T"],
            result["source_Q"], result["source_K"],
            result["canonical_Q"], result["canonical_K"], 5,
            changed_source, [rk, [[0]]],
            [right_block(1)[0], [[1]]], [right_block(1)[1], [[0]]],
        )
        self.assertFalse(source_audit["per_component_replayed_audits"][1]["strict_equivalence_certified"])
        self.assertFalse(source_audit["checks"]["every_local_certificate_reverified_against_its_bound_pair"])
        self.assertFalse(source_audit["composition_verified"])

        # The same witness must also fail when only its canonical partner changes.
        changed_canonical = [right_block(1)[0], [[2]]]
        canonical_audit = _component_witness_composition_audit(
            copy.deepcopy(result["component_witness_audits"]),
            result["left_transform_S"], result["right_transform_T"],
            result["source_Q"], result["source_K"],
            result["canonical_Q"], result["canonical_K"], 5,
            [rq, [[1]]], [rk, [[0]]],
            changed_canonical, [right_block(1)[1], [[0]]],
        )
        self.assertFalse(canonical_audit["per_component_replayed_audits"][1]["strict_equivalence_certified"])
        self.assertFalse(canonical_audit["composition_verified"])

    def test_composition_audit_ignores_forged_stored_failure_flag(self):
        rq, rk = right_block(1)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        audits = copy.deepcopy(result["component_witness_audits"])
        audits[1]["strict_equivalence_certified"] = False
        audit = _component_witness_composition_audit(
            audits, result["left_transform_S"], result["right_transform_T"],
            result["source_Q"], result["source_K"],
            result["canonical_Q"], result["canonical_K"], 5,
            [rq, [[1]]], [rk, [[0]]],
            [right_block(1)[0], [[1]]], [right_block(1)[1], [[0]]],
        )
        self.assertTrue(audit["per_component_replayed_audits"][1]["strict_equivalence_certified"])
        self.assertTrue(audit["composition_verified"])

    def test_composition_audit_checks_block_list_cardinality_before_replay(self):
        rq, rk = right_block(1)
        result = assemble_kronecker_components([
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ], 5)
        with self.assertRaisesRegex(ValueError, "counts must agree"):
            _component_witness_composition_audit(
                result["component_witness_audits"],
                result["left_transform_S"], result["right_transform_T"],
                result["source_Q"], result["source_K"],
                result["canonical_Q"], result["canonical_K"], 5,
                [rq], [rk, [[0]]],
                [right_block(1)[0], [[1]]], [right_block(1)[1], [[0]]],
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
                [rq, [[1]]], [rk, [[0]]],
                [right_block(1)[0], [[1]]], [right_block(1)[1], [[0]]],
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
            [rq, [[1]]], [rk, [[0]]],
            [right_block(1)[0], [[1]]], [right_block(1)[1], [[0]]],
        )
        with self.assertRaisesRegex(ValueError, "nonempty ordered sequence"):
            _component_witness_composition_audit([], *args)
        malformed = [{"left_transform": [[1, 0]], "right_transform": [[1, 0], [0, 1]]}]
        malformed_args = args[:7] + (
            [rq], [rk], [right_block(1)[0]], [right_block(1)[1]]
        )
        with self.assertRaisesRegex(ValueError, "left_transform.*square"):
            _component_witness_composition_audit(malformed, *malformed_args)

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

    def test_rejects_malformed_component_matrix_containers_and_entries(self):
        malformed_pairs = [
            (1, [[0]]),
            ([[1], [0, 1]], [[0], [0, 0]]),
            ([[1.5]], [[0]]),
            ([[True]], [[0]]),
            ([[1]], [[False]]),
            ([[1]], [0]),
            ([[]], [[]]),
        ]
        for q, k in malformed_pairs:
            with self.subTest(q=q, k=k):
                with self.assertRaises(ValueError):
                    assemble_kronecker_components(
                        [{"kind": "regular", "q": q, "k": k}], 5
                    )

    def test_rejects_invalid_field_parameters_before_component_work(self):
        for p in (True, 2.5, "5", 1, 9):
            with self.subTest(p=p):
                with self.assertRaises(ValueError):
                    assemble_kronecker_components(
                        [{"kind": "regular", "q": [[1]], "k": [[0]]}], p
                    )

    def test_rejects_inconsistent_component_coefficient_dimensions(self):
        with self.assertRaisesRegex(ValueError, "identical dimensions"):
            assemble_kronecker_components(
                [{"kind": "regular", "q": [[1, 0]], "k": [[0]]}], 5
            )

    def test_requires_nonempty_component_list(self):
        with self.assertRaises(ValueError):
            assemble_kronecker_components([], 3)

    def test_independent_reconstruction_verifier_accepts_fresh_result(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_certificate
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        result = assemble_kronecker_components(components, 5)
        audit = verify_kronecker_component_assembly_certificate(components, 5, result)
        self.assertTrue(audit["verified"])
        self.assertTrue(all(audit["checks"].values()))

    def test_independent_reconstruction_verifier_detects_mutated_certificate_fields(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_certificate
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        original = assemble_kronecker_components(components, 5)
        mutations = [
            ("source_Q", lambda r: r["source_Q"][0].__setitem__(0, 4)),
            ("source_K", lambda r: r["source_K"][0].__setitem__(0, 4)),
            ("canonical_Q", lambda r: r["canonical_Q"][0].__setitem__(0, 4)),
            ("canonical_K", lambda r: r["canonical_K"][0].__setitem__(0, 4)),
            ("left_transform_S", lambda r: r["left_transform_S"][0].__setitem__(0, (r["left_transform_S"][0][0] + 1) % 5)),
            ("right_transform_T", lambda r: r["right_transform_T"][0].__setitem__(0, (r["right_transform_T"][0][0] + 1) % 5)),
            ("canonical_block_shapes", lambda r: r["canonical_block_shapes"][0].__setitem__(0, 99)),
            ("source_shape", lambda r: r["source_shape"].__setitem__(0, 99)),
            ("canonical_shape", lambda r: r["canonical_shape"].__setitem__(1, 99)),
            ("component_count", lambda r: r.__setitem__("component_count", 99)),
            ("component_reports", lambda r: r["component_reports"][0].__setitem__("kind", "regular")),
            ("component_witness_audits", lambda r: r["component_witness_audits"][0]["left_transform"][0].__setitem__(0, (r["component_witness_audits"][0]["left_transform"][0][0] + 1) % 5)),
            ("component_witness_composition_audit", lambda r: r["component_witness_composition_audit"].__setitem__("component_count", 99)),
            ("global_strict_equivalence_audit", lambda r: r["global_strict_equivalence_audit"].__setitem__("strict_equivalence_certified", False)),
            ("multi_block_direct_sum_audit", lambda r: r["multi_block_direct_sum_audit"].__setitem__("block_shapes", [[99, 99]])),
            ("component_consistency_audit", lambda r: r["component_consistency_audit"].__setitem__("consistency_verified", False)),
            ("checks", lambda r: r["checks"].__setitem__("global_strict_equivalence_verified", False)),
        ]
        for field, mutate in mutations:
            with self.subTest(field=field):
                altered = copy.deepcopy(original)
                mutate(altered)
                audit = verify_kronecker_component_assembly_certificate(components, 5, altered)
                self.assertFalse(audit["verified"])
                self.assertFalse(audit["checks"][field])


    def test_algebraic_certificate_audit_accepts_fresh_assembly(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        result = assemble_kronecker_components(components, 5)
        audit = verify_kronecker_component_assembly_algebraically(components, 5, result)
        self.assertTrue(audit["verified"], audit["checks"])
        self.assertTrue(all(audit["checks"].values()))

    def test_algebraic_certificate_audit_detects_matrix_and_transform_tampering(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        original = assemble_kronecker_components(components, 5)
        mutations = [
            ("source_Q", lambda r: r["source_Q"][0].__setitem__(0, (r["source_Q"][0][0] + 1) % 5)),
            ("source_K", lambda r: r["source_K"][0].__setitem__(0, (r["source_K"][0][0] + 1) % 5)),
            ("canonical_Q", lambda r: r["canonical_Q"][0].__setitem__(0, (r["canonical_Q"][0][0] + 1) % 5)),
            ("canonical_K", lambda r: r["canonical_K"][0].__setitem__(0, (r["canonical_K"][0][0] + 1) % 5)),
            ("left_transform_S", lambda r: r["left_transform_S"][0].__setitem__(0, (r["left_transform_S"][0][0] + 1) % 5)),
            ("right_transform_T", lambda r: r["right_transform_T"][0].__setitem__(0, (r["right_transform_T"][0][0] + 1) % 5)),
            ("cross_block_entry", lambda r: r["canonical_Q"][0].__setitem__(2, 1)),
        ]
        for field, mutate in mutations:
            with self.subTest(field=field):
                altered = copy.deepcopy(original)
                mutate(altered)
                audit = verify_kronecker_component_assembly_algebraically(components, 5, altered)
                self.assertFalse(audit["verified"])
        forged = copy.deepcopy(original)
        forged["global_strict_equivalence_audit"]["strict_equivalence_certified"] = False
        forged["component_witness_composition_audit"]["composition_verified"] = False
        forged["checks"]["global_strict_equivalence_verified"] = False
        self.assertTrue(
            verify_kronecker_component_assembly_algebraically(components, 5, forged)["verified"]
        )

    def test_algebraic_certificate_audit_rejects_malformed_block_shape(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        result = assemble_kronecker_components(components, 5)
        altered = copy.deepcopy(result)
        altered["canonical_block_shapes"] = [[0, 2]]
        audit = verify_kronecker_component_assembly_algebraically(components, 5, altered)
        self.assertFalse(audit["verified"])
        self.assertFalse(audit["checks"]["canonical_block_shapes_well_formed"])


    def test_algebraic_verifier_fails_closed_on_malformed_nested_certificates(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        original = assemble_kronecker_components(components, 5)
        malformed_results = []
        malformed = copy.deepcopy(original)
        malformed["component_witness_audits"][0] = None
        malformed_results.append(malformed)
        malformed = copy.deepcopy(original)
        malformed["component_witness_audits"][0]["left_transform"] = [[True, 0], [0, 1]]
        malformed_results.append(malformed)
        malformed = copy.deepcopy(original)
        malformed["canonical_Q"] = [[1], ["bad"]]
        malformed_results.append(malformed)
        malformed = copy.deepcopy(original)
        malformed["canonical_K"] = [[1.5, 0, 0, 0]]
        malformed_results.append(malformed)
        malformed = copy.deepcopy(original)
        malformed["left_transform_S"] = [[0]]
        malformed_results.append(malformed)
        malformed = copy.deepcopy(original)
        malformed["right_transform_T"] = [[1, 0], [0]]
        malformed_results.append(malformed)
        malformed = copy.deepcopy(original)
        malformed.pop("canonical_K")
        malformed_results.append(malformed)
        for index, candidate in enumerate(malformed_results):
            with self.subTest(index=index):
                audit = verify_kronecker_component_assembly_algebraically(
                    components, 5, candidate
                )
                self.assertFalse(audit["verified"])

    def test_algebraic_verifier_rejects_noninvertible_local_witnesses(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        components = [
            {"kind": "right", "q": rq, "k": rk},
            {"kind": "regular", "q": [[1]], "k": [[0]]},
        ]
        result = assemble_kronecker_components(components, 5)
        altered = copy.deepcopy(result)
        altered["component_witness_audits"][1]["left_transform"] = [[0]]
        altered["left_transform_S"][-1][-1] = 0
        audit = verify_kronecker_component_assembly_algebraically(
            components, 5, altered
        )
        self.assertFalse(audit["verified"])
        self.assertFalse(audit["checks"]["every_local_strict_equivalence_identity_verified"])

    def test_algebraic_verifier_rejects_invalid_field_and_component_inputs(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        components = [{"kind": "right", "q": rq, "k": rk}]
        result = assemble_kronecker_components(components, 5)
        for invalid_p in (True, 2, 5.0, "5"):
            with self.subTest(p=invalid_p):
                with self.assertRaises(ValueError):
                    verify_kronecker_component_assembly_algebraically(
                        components, invalid_p, result
                    )
        for invalid_components in (
            [{"kind": "right", "q": [[True]], "k": [[1]]}],
            [{"kind": "right", "q": [[1, 2], [3]], "k": [[1, 2], [3, 4]]}],
            [None],
        ):
            with self.subTest(components=invalid_components):
                with self.assertRaises(ValueError):
                    verify_kronecker_component_assembly_algebraically(
                        invalid_components, 5, result
                    )

    def test_algebraic_verifier_rejects_non_dictionary_result(self):
        from tools.kronecker_component_assembly import verify_kronecker_component_assembly_algebraically
        rq, rk = right_block(1)
        with self.assertRaises(ValueError):
            verify_kronecker_component_assembly_algebraically(
                [{"kind": "right", "q": rq, "k": rk}], 5, []
            )



if __name__ == "__main__":
    unittest.main()
