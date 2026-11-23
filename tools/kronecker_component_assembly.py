"""Compose certified regular and singular Kronecker components.

The caller supplies a proposed component partition. Singular components are
recovered structurally and regular components canonicalized, then the direct
sums and block-diagonal strict-equivalence witnesses are assembled.
This does not discover a partition of an arbitrary unsplit pencil.
"""
from __future__ import annotations

from typing import Sequence

from tools.regular_pencil_canonical_witness import regular_pencil_canonical_witness
from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit
from tools.structural_singular_block import recover_single_singular_block_structurally
from tools.rectangular_pencil import _validate_pair
from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness


def _block_diag(matrices):
    if not matrices:
        raise ValueError("at least one component matrix is required")
    row_sizes = [len(matrix) for matrix in matrices]
    col_sizes = [len(matrix[0]) for matrix in matrices]
    out = [[0] * sum(col_sizes) for _ in range(sum(row_sizes))]
    ro = co = 0
    for matrix, height, width in zip(matrices, row_sizes, col_sizes):
        for i in range(height):
            for j in range(width):
                out[ro + i][co + j] = int(matrix[i][j])
        ro += height
        co += width
    return out


def _component_report_consistency_audit(
    reports, source_q, source_k, target_q, target_k, source_shape, canonical_shape
):
    """Cross-check component metadata against the actual assembled blocks."""
    count = len(reports)
    source_shapes = []
    canonical_shapes = []
    source_pairs_match = []
    canonical_pairs_match = []
    kind_shapes_match = []
    for report, sq, sk, tq, tk in zip(reports, source_q, source_k, target_q, target_k):
        source_shape_q = [len(sq), len(sq[0])]
        source_shape_k = [len(sk), len(sk[0])]
        target_shape_q = [len(tq), len(tq[0])]
        target_shape_k = [len(tk), len(tk[0])]
        source_shapes.append(source_shape_q)
        canonical_shapes.append(target_shape_q)
        source_pairs_match.append(source_shape_q == source_shape_k == report["shape"])
        canonical_pairs_match.append(target_shape_q == target_shape_k)
        kind = report["kind"]
        if kind == "right":
            kind_shapes_match.append(
                target_shape_q[0] == report["minimal_index"]
                and target_shape_q[1] == report["minimal_index"] + 1
            )
        elif kind == "left":
            kind_shapes_match.append(
                target_shape_q[0] == report["minimal_index"] + 1
                and target_shape_q[1] == report["minimal_index"]
            )
        elif kind == "regular":
            kind_shapes_match.append(target_shape_q[0] == target_shape_q[1])
        else:
            kind_shapes_match.append(False)

    source_dimension_sums_match = (
        sum(shape[0] for shape in source_shapes) == source_shape[0]
        and sum(shape[1] for shape in source_shapes) == source_shape[1]
    )
    canonical_dimension_sums_match = (
        sum(shape[0] for shape in canonical_shapes) == canonical_shape[0]
        and sum(shape[1] for shape in canonical_shapes) == canonical_shape[1]
    )
    checks = {
        "component_count_matches_all_block_lists": (
            count == len(source_q) == len(source_k) == len(target_q) == len(target_k)
        ),
        "source_coefficient_shapes_match_reports": all(source_pairs_match),
        "canonical_coefficient_shapes_match": all(canonical_pairs_match),
        "canonical_shapes_match_component_kinds": all(kind_shapes_match),
        "source_dimensions_sum_to_assembled_shape": source_dimension_sums_match,
        "canonical_dimensions_sum_to_assembled_shape": canonical_dimension_sums_match,
    }
    return {
        "schema": "the-fold-kronecker-component-consistency-audit-v1",
        "component_count": count,
        "source_block_shapes": source_shapes,
        "canonical_block_shapes": canonical_shapes,
        "checks": checks,
        "consistency_verified": all(checks.values()),
        "scope": (
            "Checks reported component metadata and ordered block dimensions "
            "against the concrete source and canonical matrices. It does not "
            "independently classify components or discover a decomposition."
        ),
    }


def assemble_kronecker_components(
    components: Sequence[dict],
    p: int,
    *,
    max_candidates: int = 100_000,
    max_minors: int = 2_000,
) -> dict:
    """Build a verified global canonical form from a supplied component list.

    Each component dictionary contains kind and source matrices q, k.
    Singular kinds are right or left and may optionally include minimal_index.
    Regular components use kind='regular' and the existing regular-pencil
    canonical witness constructor.
    """
    if not isinstance(p, int) or isinstance(p, bool) or p < 2:
        raise ValueError("p must be a prime integer")
    if not isinstance(components, (list, tuple)) or not components:
        raise ValueError("components must be a nonempty sequence")
    source_q, source_k, target_q, target_k = [], [], [], []
    left_blocks, right_blocks, reports = [], [], []
    component_witness_audits = []
    for index, component in enumerate(components):
        if not isinstance(component, dict):
            raise ValueError("each component must be a dictionary")
        kind = component.get("kind")
        q, k = component.get("q"), component.get("k")
        rows, cols = _validate_pair(q, k, p)
        source_q.append([[int(x) % p for x in row] for row in q])
        source_k.append([[int(x) % p for x in row] for row in k])
        if kind in ("right", "left"):
            recovered = recover_single_singular_block_structurally(
                q, k, p, side=kind, max_minors=max_minors
            )
            if not recovered.get("recovered"):
                return {
                    "schema": "the-fold-kronecker-component-assembly-v1",
                    "field": f"F_{p}", "assembly_complete": False,
                    "failed_component_index": index,
                    "component_reports": reports + [recovered],
                    "reason": recovered.get("reason", "singular_component_recovery_failed"),
                    "scope": "The supplied component partition is not fully certified.",
                }
            if "minimal_index" in component and component["minimal_index"] != recovered["candidate_index"]:
                raise ValueError("declared minimal_index disagrees with recovered singular block")
            tq, tk = recovered["canonical_Q"], recovered["canonical_K"]
            witness = recovered["strict_equivalence_witness"]
            if kind == "right":
                s = witness["left_transform_S"]
                t = witness["right_transform_T"]
            else:
                s = witness["original_left_transform_S"]
                t = witness["original_right_transform_T"]
            report = {
                "kind": kind, "shape": [rows, cols],
                "minimal_index": recovered["candidate_index"],
                "recovered": True, "method": recovered["method"],
            }
        elif kind == "regular":
            if rows != cols:
                raise ValueError("regular component must be square")
            canonical = regular_pencil_canonical_witness(
                q, k, p, max_candidates=max_candidates, max_minors=max_minors
            )
            if not canonical["witness_found"]:
                return {
                    "schema": "the-fold-kronecker-component-assembly-v1",
                    "field": f"F_{p}", "assembly_complete": False,
                    "failed_component_index": index,
                    "component_reports": reports + [canonical],
                    "reason": "regular_component_canonical_witness_not_found",
                    "scope": "Regular component classification is known, but its explicit bounded witness was not found.",
                }
            tq, tk = canonical["canonical_Q"], canonical["canonical_K"]
            s, t = canonical["left_transform_S"], canonical["right_transform_T"]
            report = {
                "kind": "regular", "shape": [rows, cols],
                "recovered": True, "method": canonical["construction_method"],
                "canonical_profile_verified": canonical["canonical_profile_verified"],
            }
        else:
            raise ValueError("component kind must be 'right', 'left', or 'regular'")
        component_audit = strict_pencil_equivalence_audit(q, k, p, tq, tk, s, t)
        if not component_audit["strict_equivalence_certified"]:
            raise ArithmeticError(f"component {index} witness failed local strict-equivalence audit")
        component_witness_audits.append(component_audit)
        target_q.append(tq)
        target_k.append(tk)
        left_blocks.append(s)
        right_blocks.append(t)
        reports.append(report)

    full_q, full_k = _block_diag(source_q), _block_diag(source_k)
    canonical_q, canonical_k = _block_diag(target_q), _block_diag(target_k)
    full_s, full_t = _block_diag(left_blocks), _block_diag(right_blocks)
    audit = strict_pencil_equivalence_audit(
        full_q, full_k, p, canonical_q, canonical_k, full_s, full_t
    )
    if not audit["strict_equivalence_certified"]:
        raise ArithmeticError("assembled block-diagonal witnesses failed global strict-equivalence audit")

    # G-EP61: reconcile every component report with the concrete block matrices.
    consistency_audit = _component_report_consistency_audit(
        reports, source_q, source_k, target_q, target_k,
        [len(full_q), len(full_q[0])], [len(canonical_q), len(canonical_q[0])]
    )
    if not consistency_audit["consistency_verified"]:
        raise ArithmeticError("assembled component metadata failed consistency audit")

    # G-EP60: independently verify the supplied assembled transforms against
    # the ordered component partition, checking every cross-component block.
    canonical_block_shapes = [[len(matrix), len(matrix[0])] for matrix in target_q]
    multi_block_audit = verify_pencil_multi_direct_sum_witness(
        full_q, full_k, p, full_s, full_t, canonical_block_shapes
    )
    if not multi_block_audit["verification"]["direct_sum_verified"]:
        raise ArithmeticError("assembled component witnesses failed multi-block direct-sum audit")

    return {
        "schema": "the-fold-kronecker-component-assembly-v1",
        "field": f"F_{p}", "component_count": len(reports),
        "source_shape": [len(full_q), len(full_q[0])],
        "canonical_shape": [len(canonical_q), len(canonical_q[0])],
        "source_Q": full_q, "source_K": full_k,
        "canonical_Q": canonical_q, "canonical_K": canonical_k,
        "left_transform_S": full_s, "right_transform_T": full_t,
        "canonical_block_shapes": canonical_block_shapes,
        "component_reports": reports,
        "component_witness_audits": component_witness_audits,
        "global_strict_equivalence_audit": audit,
        "multi_block_direct_sum_audit": multi_block_audit,
        "component_consistency_audit": consistency_audit,
        "assembly_complete": True,
        "checks": {
            "component_count_matches_input": len(reports) == len(components),
            "global_strict_equivalence_verified": audit["strict_equivalence_certified"],
            "multi_block_direct_sum_verified": multi_block_audit["verification"]["direct_sum_verified"],
            "component_consistency_verified": consistency_audit["consistency_verified"],
            "all_component_witnesses_verified": all(
                item["strict_equivalence_certified"] for item in component_witness_audits
            ),
        },
        "scope": (
            "Constructive assembly and global verification conditional on the supplied "
            "component partition. The multi-block audit independently verifies every "
            "cross-component zero. Does not discover the partition or prove uniqueness "
            "of the decomposition for an arbitrary unsplit pencil."
        ),
    }
