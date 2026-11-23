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


def _matrix_equal_mod(a, b, p):
    return len(a) == len(b) and all(
        len(x) == len(y) and all((int(u) - int(v)) % p == 0 for u, v in zip(x, y))
        for x, y in zip(a, b)
    )


def _validate_component_matrix(matrix, label):
    """Reject malformed matrix containers and non-integral field entries."""
    if not isinstance(matrix, (list, tuple)) or not matrix:
        raise ValueError(f"{label} must be a nonempty matrix")
    if any(not isinstance(row, (list, tuple)) for row in matrix):
        raise ValueError(f"{label} must contain matrix rows")
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise ValueError(f"{label} must be rectangular with nonzero dimensions")
    for row in matrix:
        for value in row:
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValueError(f"{label} entries must be integers (booleans are not accepted)")
    return len(matrix), width


def _validate_component_pair(q, k, p):
    """Validate one supplied component pair before modular arithmetic."""
    q_shape = _validate_component_matrix(q, "component Q")
    k_shape = _validate_component_matrix(k, "component K")
    if q_shape != k_shape:
        raise ValueError("component Q and K must have identical dimensions")
    return _validate_pair(q, k, p)


def _validate_component_transform(matrix, label):
    """Require a nonempty, rectangular, square local basis transformation."""
    if not isinstance(matrix, (list, tuple)) or not matrix:
        raise ValueError(f"{label} must be a nonempty square matrix")
    if any(not isinstance(row, (list, tuple)) for row in matrix):
        raise ValueError(f"{label} must contain matrix rows")
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise ValueError(f"{label} must be rectangular and nonempty")
    if len(matrix) != width:
        raise ValueError(f"{label} must be square")
    for row in matrix:
        for value in row:
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValueError(f"{label} entries must be integers (booleans are not accepted)")
    return matrix


def _component_witness_composition_audit(
    component_audits, assembled_s, assembled_t, source_q, source_k,
    canonical_q, canonical_k, p, source_q_blocks, source_k_blocks,
    canonical_q_blocks, canonical_k_blocks
):
    """Rebuild transforms and re-verify each certificate against its own block pair."""
    if not isinstance(component_audits, (list, tuple)) or not component_audits:
        raise ValueError("component_audits must be a nonempty ordered sequence")
    block_lists = (source_q_blocks, source_k_blocks, canonical_q_blocks, canonical_k_blocks)
    if any(not isinstance(blocks, (list, tuple)) for blocks in block_lists):
        raise ValueError("component matrix blocks must be ordered sequences")
    if any(len(blocks) != len(component_audits) for blocks in block_lists):
        raise ValueError("component certificate and matrix-block counts must agree")
    left_transforms, right_transforms, local_replays = [], [], []
    for index, item in enumerate(component_audits):
        if not isinstance(item, dict):
            raise ValueError(f"component audit {index} must be a dictionary")
        left = _validate_component_transform(
            item.get("left_transform"), f"component {index} left_transform"
        )
        right = _validate_component_transform(
            item.get("right_transform"), f"component {index} right_transform"
        )
        left_transforms.append(left)
        right_transforms.append(right)
        local_replays.append(strict_pencil_equivalence_audit(
            source_q_blocks[index], source_k_blocks[index], p,
            canonical_q_blocks[index], canonical_k_blocks[index], left, right
        ))
    local_verified = [item["strict_equivalence_certified"] for item in local_replays]
    reconstructed_s = _block_diag(left_transforms)
    reconstructed_t = _block_diag(right_transforms)
    replay = strict_pencil_equivalence_audit(
        source_q, source_k, p, canonical_q, canonical_k, reconstructed_s, reconstructed_t
    )
    checks = {
        "component_count_matches_matrix_block_lists": all(
            len(blocks) == len(component_audits) for blocks in block_lists
        ),
        "every_local_certificate_reverified_against_its_bound_pair": all(local_verified),
        "reconstructed_left_transform_matches_assembled": _matrix_equal_mod(reconstructed_s, assembled_s, p),
        "reconstructed_right_transform_matches_assembled": _matrix_equal_mod(reconstructed_t, assembled_t, p),
        "reconstructed_global_strict_equivalence_verified": replay["strict_equivalence_certified"],
    }
    return {
        "schema": "the-fold-kronecker-component-witness-composition-audit-v1",
        "component_count": len(component_audits),
        "per_component_replayed_audits": local_replays,
        "reconstructed_left_transform_S": reconstructed_s,
        "reconstructed_right_transform_T": reconstructed_t,
        "checks": checks,
        "composition_verified": all(checks.values()),
        "replayed_global_strict_equivalence_audit": replay,
        "scope": (
            "Reconstructs global block-diagonal transforms from ordered local "
            "strict-equivalence certificates, compares them with returned global "
            "transforms, and replays both pencil identities. It does not discover "
            "components or establish uniqueness of the partition."
        ),
    }


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
        rows, cols = _validate_component_pair(q, k, p)
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
        component_witness_audits.append({
            **component_audit,
            "left_transform": [[int(x) % p for x in row] for row in s],
            "right_transform": [[int(x) % p for x in row] for row in t],
        })
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

    # G-EP63: rebuild global transforms from ordered local certificates.
    composition_audit = _component_witness_composition_audit(
        component_witness_audits, full_s, full_t, full_q, full_k,
        canonical_q, canonical_k, p, source_q, source_k, target_q, target_k
    )
    if not composition_audit["composition_verified"]:
        raise ArithmeticError("component witness composition audit failed")

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
        "component_witness_composition_audit": composition_audit,
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
            "component_witness_composition_verified": composition_audit["composition_verified"],
            "component_witnesses_rebound_to_source_and_target_blocks": composition_audit["checks"]["every_local_certificate_reverified_against_its_bound_pair"],
        },
        "scope": (
            "Constructive assembly and global verification conditional on the supplied "
            "component partition. The multi-block audit independently verifies every "
            "cross-component zero. Does not discover the partition or prove uniqueness "
            "of the decomposition for an arbitrary unsplit pencil."
        ),
    }


def verify_kronecker_component_assembly_certificate(
    components: Sequence[dict],
    p: int,
    assembly_result: dict,
    *,
    max_candidates: int = 100_000,
    max_minors: int = 2_000,
) -> dict:
    """Reconstruct an assembly from original inputs and compare its certificate.

    The verifier does not trust matrices, reports, audit booleans, or dimensions
    stored in assembly_result. It deterministically reruns the component
    constructors from the original ordered inputs, then compares every
    certificate-bearing output field. This checks reproducibility and mutation
    integrity; it is not a second Kronecker classifier or a proof that the
    supplied partition is the unique decomposition.
    """
    if not isinstance(assembly_result, dict):
        raise ValueError("assembly_result must be a dictionary")
    reconstructed = assemble_kronecker_components(
        components, p, max_candidates=max_candidates, max_minors=max_minors
    )
    fields = (
        "schema", "field", "assembly_complete", "component_count",
        "source_shape", "canonical_shape", "source_Q", "source_K",
        "canonical_Q", "canonical_K", "left_transform_S", "right_transform_T",
        "canonical_block_shapes", "component_reports", "component_witness_audits",
        "component_witness_composition_audit", "global_strict_equivalence_audit",
        "multi_block_direct_sum_audit", "component_consistency_audit", "checks",
    )
    checks = {
        field: field in assembly_result and assembly_result[field] == reconstructed.get(field)
        for field in fields
    }
    return {
        "schema": "the-fold-kronecker-component-independent-reconstruction-audit-v1",
        "verified": all(checks.values()),
        "checks": checks,
        "reconstructed_component_count": reconstructed.get("component_count"),
        "reconstructed_source_shape": reconstructed.get("source_shape"),
        "reconstructed_canonical_shape": reconstructed.get("canonical_shape"),
        "scope": (
            "Rebuilds the deterministic component assembly from the original "
            "ordered component inputs and compares all certificate-bearing "
            "outputs. Detects altered matrices, transforms, dimensions, reports, "
            "and stored audit metadata. This is implementation-level replay, "
            "not an independent classification algorithm, partition discovery, "
            "or uniqueness proof."
        ),
    }


def _verify_kronecker_component_assembly_algebraically(
    components: Sequence[dict], p: int, assembly_result: dict
) -> dict:
    """Verify an assembly certificate directly from input blocks and identities.

    Unlike the deterministic reconstruction verifier, this routine does not
    rerun singular recovery or regular canonicalization. It rebuilds the source
    direct sum from the caller's inputs, extracts the claimed canonical blocks,
    checks all cross-block entries, replays each local strict-equivalence
    identity using the supplied local transforms, and independently checks the
    assembled global identities and block-diagonal transform composition.
    """
    if not isinstance(components, (list, tuple)) or not components:
        raise ValueError("components must be a nonempty sequence")
    if not isinstance(p, int) or isinstance(p, bool) or p < 2:
        raise ValueError("p must be a prime integer")
    if not isinstance(assembly_result, dict):
        raise ValueError("assembly_result must be a dictionary")
    if not assembly_result.get("assembly_complete"):
        return {
            "schema": "the-fold-kronecker-component-algebraic-audit-v1",
            "verified": False,
            "checks": {"assembly_marked_complete": False},
            "scope": "Only complete assembly certificates can be algebraically verified.",
        }

    source_q_blocks, source_k_blocks, source_shapes = [], [], []
    for component in components:
        if not isinstance(component, dict):
            raise ValueError("each component must be a dictionary")
        q, k = component.get("q"), component.get("k")
        rows, cols = _validate_component_pair(q, k, p)
        source_q_blocks.append([[int(x) % p for x in row] for row in q])
        source_k_blocks.append([[int(x) % p for x in row] for row in k])
        source_shapes.append([rows, cols])

    expected_source_q = _block_diag(source_q_blocks)
    expected_source_k = _block_diag(source_k_blocks)
    checks = {
        "assembly_marked_complete": True,
        "field_matches_input": assembly_result.get("field") == f"F_{p}",
        "component_count_matches_input": assembly_result.get("component_count") == len(components),
        "source_shape_matches_input": assembly_result.get("source_shape") == [
            len(expected_source_q), len(expected_source_q[0])
        ],
        "source_Q_rebuilt_from_original_components": _matrix_equal_mod(
            assembly_result.get("source_Q", []), expected_source_q, p
        ),
        "source_K_rebuilt_from_original_components": _matrix_equal_mod(
            assembly_result.get("source_K", []), expected_source_k, p
        ),
    }

    shapes = assembly_result.get("canonical_block_shapes")
    valid_shapes = (
        isinstance(shapes, (list, tuple)) and len(shapes) == len(components)
        and all(isinstance(s, (list, tuple)) and len(s) == 2
                and all(isinstance(x, int) and not isinstance(x, bool) and x > 0 for x in s)
                for s in shapes)
    )
    checks["canonical_block_shapes_well_formed"] = valid_shapes
    if not valid_shapes:
        checks.update({
            "canonical_shape_matches_blocks": False,
            "canonical_Q_is_block_diagonal_with_claimed_blocks": False,
            "canonical_K_is_block_diagonal_with_claimed_blocks": False,
            "every_local_strict_equivalence_identity_verified": False,
            "assembled_transforms_equal_local_block_diagonal_transforms": False,
            "global_strict_equivalence_identities_verified": False,
        })
        return {
            "schema": "the-fold-kronecker-component-algebraic-audit-v1",
            "verified": False, "checks": checks,
            "scope": "Malformed block dimensions prevent algebraic certificate replay.",
        }

    canonical_q = assembly_result.get("canonical_Q", [])
    canonical_k = assembly_result.get("canonical_K", [])
    try:
        canonical_q_shape = _validate_component_matrix(canonical_q, "canonical_Q")
        canonical_k_shape = _validate_component_matrix(canonical_k, "canonical_K")
        if canonical_q_shape != canonical_k_shape:
            raise ValueError("canonical coefficient matrices must have identical dimensions")
    except (TypeError, ValueError):
        checks.update({
            "canonical_shape_matches_blocks": False,
            "canonical_Q_is_block_diagonal_with_claimed_blocks": False,
            "canonical_K_is_block_diagonal_with_claimed_blocks": False,
            "every_local_strict_equivalence_identity_verified": False,
            "assembled_transforms_equal_local_block_diagonal_transforms": False,
            "global_strict_equivalence_identities_verified": False,
            "canonical_matrices_well_formed": False,
        })
        return {
            "schema": "the-fold-kronecker-component-algebraic-audit-v1",
            "verified": False, "checks": checks,
            "scope": "Malformed canonical matrices prevent algebraic certificate replay.",
        }
    checks["canonical_matrices_well_formed"] = True
    try:
        canonical_shape = [sum(s[0] for s in shapes), sum(s[1] for s in shapes)]
        checks["canonical_shape_matches_blocks"] = (
            assembly_result.get("canonical_shape") == canonical_shape
            and len(canonical_q) == canonical_shape[0]
            and len(canonical_k) == canonical_shape[0]
            and all(len(row) == canonical_shape[1] for row in canonical_q)
            and all(len(row) == canonical_shape[1] for row in canonical_k)
        )
        q_blocks, k_blocks = [], []
        row_offset = col_offset = 0
        for height, width in shapes:
            q_block = [list(row[col_offset:col_offset + width])
                       for row in canonical_q[row_offset:row_offset + height]]
            k_block = [list(row[col_offset:col_offset + width])
                       for row in canonical_k[row_offset:row_offset + height]]
            q_blocks.append(q_block)
            k_blocks.append(k_block)
            row_offset += height
            col_offset += width
        expected_canonical_q = _block_diag(q_blocks)
        expected_canonical_k = _block_diag(k_blocks)
        checks["canonical_Q_is_block_diagonal_with_claimed_blocks"] = (
            _matrix_equal_mod(canonical_q, expected_canonical_q, p)
        )
        checks["canonical_K_is_block_diagonal_with_claimed_blocks"] = (
            _matrix_equal_mod(canonical_k, expected_canonical_k, p)
        )
    except (IndexError, TypeError, ValueError):
        q_blocks, k_blocks = [], []
        checks["canonical_shape_matches_blocks"] = False
        checks["canonical_Q_is_block_diagonal_with_claimed_blocks"] = False
        checks["canonical_K_is_block_diagonal_with_claimed_blocks"] = False

    local_items = assembly_result.get("component_witness_audits")
    local_ok, left_blocks, right_blocks = [], [], []
    if isinstance(local_items, (list, tuple)) and len(local_items) == len(components) and len(q_blocks) == len(components):
        for i, item in enumerate(local_items):
            try:
                if not isinstance(item, dict):
                    raise ValueError("local witness audit must be a dictionary")
                s = _validate_component_transform(item["left_transform"], f"component {i} left transform")
                t = _validate_component_transform(item["right_transform"], f"component {i} right transform")
                audit = strict_pencil_equivalence_audit(
                    source_q_blocks[i], source_k_blocks[i], p,
                    q_blocks[i], k_blocks[i], s, t
                )
                local_ok.append(bool(audit["strict_equivalence_certified"]))
                left_blocks.append(s)
                right_blocks.append(t)
            except (KeyError, TypeError, ValueError):
                local_ok.append(False)
    checks["every_local_strict_equivalence_identity_verified"] = (
        len(local_ok) == len(components) and all(local_ok)
    )
    try:
        assembled_s = _validate_component_transform(assembly_result.get("left_transform_S"), "assembled left transform")
        assembled_t = _validate_component_transform(assembly_result.get("right_transform_T"), "assembled right transform")
        rebuilt_s, rebuilt_t = _block_diag(left_blocks), _block_diag(right_blocks)
        checks["assembled_transforms_equal_local_block_diagonal_transforms"] = (
            _matrix_equal_mod(assembled_s, rebuilt_s, p)
            and _matrix_equal_mod(assembled_t, rebuilt_t, p)
        )
        global_audit = strict_pencil_equivalence_audit(
            expected_source_q, expected_source_k, p,
            canonical_q, canonical_k, assembled_s, assembled_t
        )
        checks["global_strict_equivalence_identities_verified"] = bool(
            global_audit["strict_equivalence_certified"]
        )
    except (TypeError, ValueError):
        checks["assembled_transforms_equal_local_block_diagonal_transforms"] = False
        checks["global_strict_equivalence_identities_verified"] = False
        global_audit = None

    return {
        "schema": "the-fold-kronecker-component-algebraic-audit-v1",
        "verified": all(checks.values()),
        "checks": checks,
        "per_component_strict_equivalence_verified": local_ok,
        "replayed_global_strict_equivalence_audit": global_audit,
        "scope": (
            "Directly rebuilds source blocks from caller inputs; checks canonical "
            "off-block zeros; replays local and global S Q T and S K T identities; "
            "and binds the global transforms to the local block-diagonal witnesses. "
            "Does not rerun canonical constructors, discover a partition, or prove "
            "uniqueness of the supplied decomposition."
        ),
    }

    
def verify_kronecker_component_assembly_algebraically(
    components: Sequence[dict], p: int, assembly_result: dict
) -> dict:
    """Fail closed on malformed certificate structures and replay exceptions."""
    try:
        return _verify_kronecker_component_assembly_algebraically(components, p, assembly_result)
    except (AttributeError, IndexError, KeyError, OverflowError, TypeError, ValueError):
        return {
            "schema": "the-fold-kronecker-component-algebraic-audit-v1",
            "verified": False,
            "checks": {"certificate_structure_well_formed": False},
            "scope": (
                "Malformed certificate structures or invalid witness matrices are "
                "rejected without treating cached audit metadata as evidence."
            ),
        }
