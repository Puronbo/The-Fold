"""Structural strict-equivalence recovery for a single singular pencil block."""
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


def _canonical_right_block(e, p):
    q = [[int(i == j) for j in range(e + 1)] for i in range(e)]
    k = [[int(j == i + 1) for j in range(e + 1)] for i in range(e)]
    return q, k


def _right_recovery(q, k, p, max_minors):
    rows, cols = _validate_pair(q, k, p)
    if cols != rows + 1:
        return {"recovered": False, "reason": "shape is not e by e+1"}
    e = rows
    certificate = rectangular_pencil_nullspace_certificate(
        q, k, p, max_degree=e, max_minors=max_minors
    )
    right = certificate["right"]
    left = certificate["left"]
    if (not certificate["complete"] or not right["complete"] or
            not left["complete"] or len(right["generators"]) != 1 or
            right["minimal_indices"] != [e] or left["minimal_indices"] != []):
        return {
            "recovered": False,
            "reason": "pencil is not certified as one right singular block of index e",
            "nullspace_certificate": certificate,
        }

    coeffs = right["generators"][0]["coefficients_low_degree_first"]
    if len(coeffs) != e + 1 or any(len(v) != cols for v in coeffs):
        return {"recovered": False, "reason": "minimal generator coefficient chain has unexpected shape"}
    # Reverse the chain and alternate signs. This aligns Q z_j = K z_(j+1).
    z = []
    for j in range(e + 1):
        sign = (-1) ** (e - j)
        z.append([(sign * int(x)) % p for x in coeffs[e-j]])

    # T has the reversed signed coefficient vectors as columns.
    t = _transpose(z)
    if _det_mod(t, p) == 0:
        return {
            "recovered": False,
            "reason": "minimal-vector coefficients do not form a domain basis",
            "nullspace_certificate": certificate,
        }
    # The images K z_1,...,K z_e must form a codomain basis.
    b = _matmul(k, _transpose(z[1:]), p)
    if _det_mod(b, p) == 0:
        return {
            "recovered": False,
            "reason": "shifted minimal-vector images do not form a codomain basis",
            "nullspace_certificate": certificate,
        }
    s = _inverse_mod(b, p)
    q0, k0 = _canonical_right_block(e, p)
    audit = strict_pencil_equivalence_audit(q, k, p, q0, k0, s, t)
    if not audit["strict_equivalence_certified"]:
        raise ArithmeticError("constructed structural witnesses failed strict-equivalence verification")
    return {
        "recovered": True, "candidate_index": e,
        "canonical_Q": q0, "canonical_K": k0,
        "left_transform_S": s, "right_transform_T": t,
        "minimal_vector_coefficients_low_degree_first": coeffs,
        "domain_basis_determinant_mod_p": _det_mod(t, p),
        "codomain_basis_determinant_mod_p": _det_mod(b, p),
        "nullspace_certificate": certificate,
        "verification": audit,
        "method": "polynomial minimal-vector coefficient chain and its shifted K-images",
    }


def recover_single_singular_block_structurally(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    side: str = "right", max_minors: int = 2000,
) -> dict:
    """Construct constant strict-equivalence witnesses from a minimal basis.

    Supports one right block or, by transposition, one left block. Unlike
    G-EP31 this does not enumerate GL groups. It requires the nullspace
    certificate to prove the one-block minimal-index pattern and then checks
    both constructed bases and the final strict-equivalence identities.
    """
    rows, cols = _validate_pair(q, k, p)
    if side not in ("right", "left"):
        raise ValueError("side must be 'right' or 'left'")
    if not isinstance(max_minors, int) or max_minors < 1:
        raise ValueError("max_minors must be a positive integer")
    if side == "right":
        result = _right_recovery(q, k, p, max_minors)
        source_shape = [rows, cols]
        if result.get("recovered"):
            result["strict_equivalence_witness"] = {
                "left_transform_S": result.pop("left_transform_S"),
                "right_transform_T": result.pop("right_transform_T"),
            }
    else:
        result = _right_recovery(_transpose(q), _transpose(k), p, max_minors)
        source_shape = [rows, cols]
        if result.get("recovered"):
            sr = result.pop("left_transform_S")
            tr = result.pop("right_transform_T")
            transposed_audit = result.pop("verification")
            original_s = _transpose(tr)
            original_t = _transpose(sr)
            q_target = _transpose(result["canonical_Q"])
            k_target = _transpose(result["canonical_K"])
            result["canonical_Q"] = q_target
            result["canonical_K"] = k_target
            result["strict_equivalence_witness"] = {
                "original_left_transform_S": original_s,
                "original_right_transform_T": original_t,
            }
            result["transposed_problem_verification"] = transposed_audit
            result["verification"] = strict_pencil_equivalence_audit(
                q, k, p, q_target, k_target, original_s, original_t
            )
    result.update({
        "schema": "the-fold-structural-singular-block-recovery-v1",
        "field": f"F_{p}", "side": side, "shape": source_shape,
        "scope": "One pure right or left singular Kronecker block; not a mixed pencil decomposition.",
    })
    return result
