"""Structural recovery for pure singular pencils with multiple blocks.

Unlike the single-block helper, this routine uses all certified polynomial
minimal-vector chains at once. It supports a pure right-singular direct sum
or a pure left-singular direct sum, but not a regular part or both sides.
"""
from __future__ import annotations

from typing import Sequence

from tools.pencil_nullspace_certificate import rectangular_pencil_nullspace_certificate
from tools.strict_pencil_equivalence import _det_mod, strict_pencil_equivalence_audit
from tools.rectangular_pencil import _validate_pair
from tools.structural_singular_block import _inverse_mod, _matmul, _transpose


def _block_diag_rectangular(blocks):
    if not blocks:
        raise ValueError("at least one singular block is required")
    rows = sum(len(q) for q, _ in blocks)
    cols = sum(len(q[0]) for q, _ in blocks)
    out_q, out_k = [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)]
    ro = co = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                out_q[ro+i][co+j] = q[i][j]
                out_k[ro+i][co+j] = k[i][j]
        ro += len(q)
        co += len(q[0])
    return out_q, out_k


def _canonical_right(e):
    return (
        [[int(i == j) for j in range(e+1)] for i in range(e)],
        [[int(j == i+1) for j in range(e+1)] for i in range(e)],
    )


def _recover_right_only(q, k, p, max_degree, max_minors):
    rows, cols = _validate_pair(q, k, p)
    certificate = rectangular_pencil_nullspace_certificate(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    right, left = certificate["right"], certificate["left"]
    if (not certificate["complete"] or not right["complete"] or
            not left["complete"] or not right["generators"] or
            left["generators"] or right["minimal_indices"] is None):
        return {
            "recovered": False,
            "reason": "pencil is not certified as a nonempty pure right-singular direct sum",
            "nullspace_certificate": certificate,
        }
    chains, blocks = [], []
    for generator in right["generators"]:
        e = generator["degree"]
        coeffs = generator["coefficients_low_degree_first"]
        if len(coeffs) != e+1 or any(len(v) != cols for v in coeffs):
            return {"recovered": False, "reason": "minimal-vector chain has invalid dimensions"}
        chain = []
        for j in range(e+1):
            sign = (-1) ** (e-j)
            chain.append([(sign*int(x)) % p for x in coeffs[e-j]])
        chains.append(chain)
        blocks.append(_canonical_right(e))
    t = _transpose([v for chain in chains for v in chain])
    b_columns = []
    for chain in chains:
        b_columns.extend([_matmul(k, [[x] for x in chain[j]], p)[i][0]
                          for j in range(1, len(chain)) for i in range(rows)])
    # Reassemble K z_1, ..., K z_e as columns in chain order.
    b = [[0] * rows for _ in range(rows)]
    col = 0
    for chain in chains:
        for vector in chain[1:]:
            image = _matmul(k, [[x] for x in vector], p)
            for i in range(rows):
                b[i][col] = image[i][0]
            col += 1
    if len(t) != cols or any(len(row) != cols for row in t) or _det_mod(t, p) == 0:
        return {"recovered": False, "reason": "right minimal-vector chains do not form a domain basis",
                "nullspace_certificate": certificate}
    if col != rows or _det_mod(b, p) == 0:
        return {"recovered": False, "reason": "shifted K-images do not form a codomain basis",
                "nullspace_certificate": certificate}
    s = _inverse_mod(b, p)
    q_can, k_can = _block_diag_rectangular(blocks)
    audit = strict_pencil_equivalence_audit(q, k, p, q_can, k_can, s, t)
    if not audit["strict_equivalence_certified"]:
        raise ArithmeticError("multi-chain right-singular witness failed exact audit")
    return {
        "recovered": True, "side": "right",
        "minimal_indices": right["minimal_indices"],
        "canonical_Q": q_can, "canonical_K": k_can,
        "left_transform_S": s, "right_transform_T": t,
        "nullspace_certificate": certificate, "verification": audit,
        "method": "all certified right minimal-vector coefficient chains and shifted K-images",
    }


def recover_pure_singular_pencil_structurally(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    side: str = "right", max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Recover a pure right-only or left-only singular pencil with many blocks."""
    rows, cols = _validate_pair(q, k, p)
    if side not in ("right", "left"):
        raise ValueError("side must be 'right' or 'left'")
    if not isinstance(max_degree, int) or isinstance(max_degree, bool) or max_degree < 0:
        raise ValueError("max_degree must be a non-negative integer")
    if not isinstance(max_minors, int) or isinstance(max_minors, bool) or max_minors < 1:
        raise ValueError("max_minors must be a positive integer")
    if side == "right":
        result = _recover_right_only(q, k, p, max_degree, max_minors)
    else:
        transposed = _recover_right_only(_transpose(q), _transpose(k), p, max_degree, max_minors)
        if transposed.get("recovered"):
            s = _transpose(transposed.pop("right_transform_T"))
            t = _transpose(transposed.pop("left_transform_S"))
            q_can, k_can = _transpose(transposed["canonical_Q"]), _transpose(transposed["canonical_K"])
            audit = strict_pencil_equivalence_audit(q, k, p, q_can, k_can, s, t)
            if not audit["strict_equivalence_certified"]:
                raise ArithmeticError("multi-chain left-singular witness failed exact audit")
            result = {
                "recovered": True, "side": "left",
                "minimal_indices": transposed["minimal_indices"],
                "canonical_Q": q_can, "canonical_K": k_can,
                "left_transform_S": s, "right_transform_T": t,
                "nullspace_certificate": transposed["nullspace_certificate"],
                "verification": audit,
                "method": "transposed all-chain structural recovery",
            }
        else:
            result = transposed
    result.update({
        "schema": "the-fold-pure-singular-pencil-recovery-v1",
        "field": f"F_{p}", "source_shape": [rows, cols],
        "scope": "Pure right-only or pure left-only singular pencils, including multiple blocks. No regular component or mixed left/right decomposition.",
    })
    return result
