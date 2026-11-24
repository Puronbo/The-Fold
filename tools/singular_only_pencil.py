"""Structural recovery of a direct sum of right/left singular Kronecker blocks."""
from __future__ import annotations
from typing import Sequence

from tools.pencil_nullspace_certificate import rectangular_pencil_nullspace_certificate
from tools.strict_pencil_equivalence import _det_mod, strict_pencil_equivalence_audit
from tools.rectangular_pencil import _validate_pair


def _transpose(a):
    return [list(row) for row in zip(*a)]


def _inverse_mod(matrix, p):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix inverse requires a square matrix")
    a = [[int(x) % p for x in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            raise ValueError("matrix is singular over the selected prime field")
        a[col], a[pivot] = a[pivot], a[col]
        inv = pow(a[col][col], -1, p)
        a[col] = [(x * inv) % p for x in a[col]]
        for r in range(n):
            if r != col and a[r][col]:
                factor = a[r][col]
                a[r] = [(x - factor*y) % p for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a]


def _matmul(a, b, p):
    return [[sum(int(a[i][k]) * int(b[k][j]) for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def _right_canonical(indices, p):
    rows, cols = sum(indices), sum(e + 1 for e in indices)
    q = [[0] * cols for _ in range(rows)]
    k = [[0] * cols for _ in range(rows)]
    row_offset = col_offset = 0
    for e in indices:
        for j in range(e):
            q[row_offset+j][col_offset+j] = 1
            k[row_offset+j][col_offset+j+1] = 1
        row_offset += e
        col_offset += e + 1
    return q, k


def _recover_right_only(q, k, p, max_degree, max_minors):
    rows, cols = _validate_pair(q, k, p)
    if cols <= rows:
        return {"recovered": False, "reason": "right-singular-only pencils must have more columns than rows"}
    certificate = rectangular_pencil_nullspace_certificate(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    right, left = certificate["right"], certificate["left"]
    if (not certificate["complete"] or not right["complete"] or
            not left["complete"] or left["minimal_indices"] != []):
        return {"recovered": False, "reason": "pencil is not certified as right-singular-only", "nullspace_certificate": certificate}
    indices = right["minimal_indices"]
    if not indices or sum(indices) != rows or sum(e + 1 for e in indices) != cols:
        return {"recovered": False, "reason": "recovered right minimal indices do not account for the full pencil dimensions", "nullspace_certificate": certificate}
    generators = right["generators"]
    if len(generators) != len(indices):
        return {"recovered": False, "reason": "generator count does not match the right minimal-index list", "nullspace_certificate": certificate}

    # For each generator x(t), reverse and alternate its coefficient chain.
    domain_columns = []
    image_columns = []
    block_chains = []
    for generator, e in zip(generators, indices):
        coeffs = generator["coefficients_low_degree_first"]
        if generator["degree"] != e or len(coeffs) != e + 1:
            return {"recovered": False, "reason": "minimal-vector degree and coefficient count disagree", "nullspace_certificate": certificate}
        z = [[((-1) ** (e-j) * int(x)) % p for x in coeffs[e-j]]
             for j in range(e + 1)]
        domain_columns.extend(z)
        image_columns.extend(z[1:])
        block_chains.append({"index": e, "coefficients_low_degree_first": coeffs})

    t = _transpose(domain_columns)
    b = _matmul(k, _transpose(image_columns), p)
    if _det_mod(t, p) == 0:
        return {"recovered": False, "reason": "combined minimal-vector coefficients do not form a domain basis", "nullspace_certificate": certificate}
    if _det_mod(b, p) == 0:
        return {"recovered": False, "reason": "combined shifted K-images do not form a codomain basis", "nullspace_certificate": certificate}
    s = _inverse_mod(b, p)
    q0, k0 = _right_canonical(indices, p)
    audit = strict_pencil_equivalence_audit(q, k, p, q0, k0, s, t)
    if not audit["strict_equivalence_certified"]:
        raise ArithmeticError("constructed direct-sum witnesses failed strict-equivalence verification")
    return {
        "recovered": True, "right_minimal_indices": indices,
        "canonical_Q": q0, "canonical_K": k0,
        "strict_equivalence_witness": {"left_transform_S": s, "right_transform_T": t},
        "domain_basis_determinant_mod_p": _det_mod(t, p),
        "codomain_basis_determinant_mod_p": _det_mod(b, p),
        "minimal_vector_chains": block_chains,
        "nullspace_certificate": certificate, "verification": audit,
        "method": "concatenated reversed signed minimal-vector chains and their shifted K-images",
    }


def recover_singular_only_pencil_structurally(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    side: str = "right", max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Recover a direct sum of pure right or pure left singular blocks.

    Mixed pencils and regular parts are deliberately refused. The routine
    constructs constant strict-equivalence witnesses, not a general Kronecker
    decomposition with regular blocks.
    """
    rows, cols = _validate_pair(q, k, p)
    if side not in ("right", "left"):
        raise ValueError("side must be 'right' or 'left'")
    if not isinstance(max_degree, int) or max_degree < 0:
        raise ValueError("max_degree must be a non-negative integer")
    if not isinstance(max_minors, int) or max_minors < 1:
        raise ValueError("max_minors must be a positive integer")
    if side == "right":
        result = _recover_right_only(q, k, p, max_degree, max_minors)
    else:
        transposed = _recover_right_only(_transpose(q), _transpose(k), p, max_degree, max_minors)
        if transposed.get("recovered"):
            sr = transposed["strict_equivalence_witness"]["left_transform_S"]
            tr = transposed["strict_equivalence_witness"]["right_transform_T"]
            original_s, original_t = _transpose(tr), _transpose(sr)
            q0, k0 = _transpose(transposed["canonical_Q"]), _transpose(transposed["canonical_K"])
            audit = strict_pencil_equivalence_audit(q, k, p, q0, k0, original_s, original_t)
            result = {
                **transposed, "canonical_Q": q0, "canonical_K": k0,
                "strict_equivalence_witness": {
                    "left_transform_S": original_s, "right_transform_T": original_t,
                },
                "verification": audit,
            }
        else:
            result = transposed
    result.update({
        "schema": "the-fold-singular-only-pencil-recovery-v1",
        "field": f"F_{p}", "side": side, "shape": [rows, cols],
        "scope": "Direct sums of pure right or pure left singular blocks only; no regular part or mixed left/right decomposition.",
    })
    return result
