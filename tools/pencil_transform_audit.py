"""Independent determinant and identity audit for polynomial Smith transforms."""
from __future__ import annotations
from itertools import permutations
from typing import Sequence

from tools.pencil_smith import _trim, _add, _mul
from tools.pencil_smith_transform import _matmul, _poly_matrix_equal
from tools.rectangular_pencil import _validate_pair


def _determinant(matrix, p, max_terms):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square polynomial matrix")
    if n == 0:
        return [1]
    terms = 0
    total = [0]
    for perm in permutations(range(n)):
        terms += 1
        if terms > max_terms:
            raise ValueError("determinant permutation budget exceeded")
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        product = [1]
        for i, j in enumerate(perm):
            product = _mul(product, matrix[i][j], p)
        if inversions % 2:
            product = [(-x) % p for x in product]
        total = _add(total, product, p)
    return _trim(total, p)


def _constant_nonzero(poly, p):
    poly = _trim(poly, p)
    return len(poly) == 1 and poly[0] % p != 0


def audit_polynomial_smith_transform(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int,
    transform: dict, *, max_determinant_terms: int = 100000,
) -> dict:
    """Independently verify U P V = D and det(U), det(V) are units in F_p[t]."""
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(max_determinant_terms, int) or max_determinant_terms < 1:
        raise ValueError("max_determinant_terms must be a positive integer")
    u = transform.get("left_transform_U")
    v = transform.get("right_transform_V")
    d = transform.get("reduced_matrix_low_degree_first")
    if not isinstance(u, list) or len(u) != rows or any(len(row) != rows for row in u):
        raise ValueError("left transform has the wrong shape")
    if not isinstance(v, list) or len(v) != cols or any(len(row) != cols for row in v):
        raise ValueError("right transform has the wrong shape")
    if not isinstance(d, list) or len(d) != rows or any(len(row) != cols for row in d):
        raise ValueError("reduced matrix has the wrong shape")
    p_matrix = [[[
        int(q[i][j]) % p, int(k[i][j]) % p
    ] for j in range(cols)] for i in range(rows)]
    p_matrix = [[_trim(entry, p) for entry in row] for row in p_matrix]
    u = [[_trim(entry, p) for entry in row] for row in u]
    v = [[_trim(entry, p) for entry in row] for row in v]
    d = [[_trim(entry, p) for entry in row] for row in d]
    reconstructed = _matmul(_matmul(u, p_matrix, p), v, p)
    identity_ok = _poly_matrix_equal(reconstructed, d, p)
    det_u = _determinant(u, p, max_determinant_terms)
    det_v = _determinant(v, p, max_determinant_terms)
    u_unit = _constant_nonzero(det_u, p)
    v_unit = _constant_nonzero(det_v, p)
    return {
        "schema": "the-fold-polynomial-transform-audit-v1",
        "field": f"F_{p}", "shape": [rows, cols],
        "determinant_U_low_degree_first": det_u,
        "determinant_V_low_degree_first": det_v,
        "U_determinant_is_nonzero_constant": u_unit,
        "V_determinant_is_nonzero_constant": v_unit,
        "transformation_identity_verified": identity_ok,
        "both_transforms_unimodular": u_unit and v_unit,
        "independently_verified": identity_ok and u_unit and v_unit,
        "determinant_method": "exact Leibniz expansion over F_p[t]",
        "determinant_term_budget": max_determinant_terms,
    }
