"""Exact verifier for supplied strict-equivalence certificates of matrix pencils."""
from __future__ import annotations
from typing import Sequence

from tools.rectangular_pencil import _validate_pair


def _det_mod(matrix, p):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")
    a = [[int(x) % p for x in row] for row in matrix]
    det = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = (-det) % p
        value = a[col][col]
        det = det * value % p
        inv = pow(value, -1, p)
        for r in range(col + 1, n):
            factor = a[r][col] * inv % p
            if factor:
                for c in range(col + 1, n):
                    a[r][c] = (a[r][c] - factor * a[col][c]) % p
                a[r][col] = 0
    return det % p


def _matmul(a, b, p):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    return [[sum(int(a[i][k]) * int(b[k][j]) for k in range(len(b))) % p
                for j in range(len(b[0]))] for i in range(len(a))]


def _matrix_equal(a, b, p):
    return len(a) == len(b) and all(
        len(x) == len(y) and all((int(u) - int(v)) % p == 0 for u, v in zip(x, y))
        for x, y in zip(a, b)
    )


def strict_pencil_equivalence_audit(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int,
    q_target: Sequence[Sequence[int]], k_target: Sequence[Sequence[int]],
    left_transform: Sequence[Sequence[int]],
    right_transform: Sequence[Sequence[int]],
) -> dict:
    """Verify S Q T=Q_target and S K T=K_target for constant invertible S,T.

    The supplied matrices are witnesses, not transformations constructed by
    this routine. Dimensions and invertibility are checked over F_p.
    """
    rows, cols = _validate_pair(q, k, p)
    target_rows, target_cols = _validate_pair(q_target, k_target, p)
    if (rows, cols) != (target_rows, target_cols):
        raise ValueError("source and target pencils must have the same shape")
    s = [[int(x) % p for x in row] for row in left_transform]
    t = [[int(x) % p for x in row] for row in right_transform]
    if len(s) != rows or any(len(row) != rows for row in s):
        raise ValueError("left transform must be square with pencil row dimension")
    if len(t) != cols or any(len(row) != cols for row in t):
        raise ValueError("right transform must be square with pencil column dimension")
    det_s, det_t = _det_mod(s, p), _det_mod(t, p)
    q_image = _matmul(_matmul(s, q, p), t, p)
    k_image = _matmul(_matmul(s, k, p), t, p)
    q_ok = _matrix_equal(q_image, q_target, p)
    k_ok = _matrix_equal(k_image, k_target, p)
    return {
        "schema": "the-fold-strict-pencil-equivalence-audit-v1",
        "field": f"F_{p}", "shape": [rows, cols],
        "left_determinant_mod_p": det_s,
        "right_determinant_mod_p": det_t,
        "left_transform_invertible": det_s != 0,
        "right_transform_invertible": det_t != 0,
        "constant_strict_equivalence_Q_verified": q_ok,
        "constant_strict_equivalence_K_verified": k_ok,
        "strict_equivalence_certified": det_s != 0 and det_t != 0 and q_ok and k_ok,
        "equivalence": "S Q T = Q_target and S K T = K_target",
        "scope": (
            "Verifies supplied constant transformation witnesses over F_p. "
            "Does not discover witnesses or infer a Kronecker canonical form."
        ),
    }
