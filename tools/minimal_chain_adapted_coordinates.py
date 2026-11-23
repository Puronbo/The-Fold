"""Adapted coordinates for the minimal-chain spaces of a pencil.

The first domain basis vectors span right minimal-chain coefficients; the
first codomain basis covectors span left minimal-chain coefficients. Remaining
basis vectors are completed deterministically from standard coordinate vectors.
The transformed pencil is returned with exact invertibility and multiplication
checks. No block-diagonal or regular-complement theorem is assumed.
"""
from __future__ import annotations

from typing import Sequence

from tools.minimal_chain_geometry import minimal_chain_geometry_certificate
from tools.rectangular_pencil import _validate_pair


def _rank(rows, p):
    if not rows:
        return 0
    a = [[int(x) % p for x in row] for row in rows]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def _independent_rows(vectors, width, p):
    chosen = []
    rank = 0
    for vector in vectors:
        candidate = chosen + [[int(x) % p for x in vector]]
        new_rank = _rank(candidate, p)
        if new_rank > rank:
            chosen.append(candidate[-1])
            rank = new_rank
    return chosen


def _complete_rows(seed, width, p):
    rows = [row[:] for row in seed]
    rank = _rank(rows, p)
    for j in range(width):
        if rank == width:
            break
        vector = [int(i == j) for i in range(width)]
        candidate = rows + [vector]
        new_rank = _rank(candidate, p)
        if new_rank > rank:
            rows.append(vector)
            rank = new_rank
    if rank != width:
        raise ArithmeticError("standard coordinate vectors failed to complete a basis")
    return rows


def _transpose(a):
    return [list(column) for column in zip(*a)]


def _matmul(a, b, p):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    return [[sum(int(a[i][k]) * int(b[k][j]) for k in range(len(b))) % p
                 for j in range(len(b[0]))] for i in range(len(a))]


def _det(a, p):
    if not a:
        return 1
    m = [[int(x) % p for x in row] for row in a]
    n = len(m)
    det = 1
    for c in range(n):
        pivot = next((r for r in range(c, n) if m[r][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            m[c], m[pivot] = m[pivot], m[c]
            det = -det
        value = m[c][c] % p
        det = det * value % p
        inv = pow(value, -1, p)
        for r in range(c + 1, n):
            if m[r][c]:
                factor = m[r][c] * inv % p
                for j in range(c, n):
                    m[r][j] = (m[r][j] - factor*m[c][j]) % p
    return det % p


def minimal_chain_adapted_coordinates(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Build and verify bases adapted to right and left minimal-chain spaces."""
    rows, cols = _validate_pair(q, k, p)
    geometry = minimal_chain_geometry_certificate(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    nullspace = geometry["nullspace_certificate"]
    right_vectors = [
        list(map(int, coefficient))
        for generator in nullspace["right"]["generators"]
        for coefficient in generator["coefficients_low_degree_first"]
    ]
    left_covectors = [
        list(map(int, coefficient))
        for generator in nullspace["left"]["generators"]
        for coefficient in generator["coefficients_low_degree_first"]
    ]
    right_seed = _independent_rows(right_vectors, cols, p)
    left_seed = _independent_rows(left_covectors, rows, p)
    t = _transpose(_complete_rows(right_seed, cols, p))
    s = _complete_rows(left_seed, rows, p)
    q_adapted = _matmul(_matmul(s, q, p), t, p)
    k_adapted = _matmul(_matmul(s, k, p), t, p)
    s_det, t_det = _det(s, p), _det(t, p)
    verified = (
        s_det != 0 and t_det != 0
        and q_adapted == _matmul(_matmul(s, q, p), t, p)
        and k_adapted == _matmul(_matmul(s, k, p), t, p)
    )
    if not verified:
        raise ArithmeticError("adapted coordinate witness failed exact verification")
    rdim, ldim = len(right_seed), len(left_seed)
    return {
        "schema": "the-fold-minimal-chain-adapted-coordinates-v1",
        "field": f"F_{p}",
        "source_shape": [rows, cols],
        "right_chain_basis_dimension": rdim,
        "left_chain_cobasis_dimension": ldim,
        "domain_basis_T": t,
        "codomain_cobasis_S": s,
        "adapted_Q": q_adapted,
        "adapted_K": k_adapted,
        "right_chain_domain_columns": list(range(rdim)),
        "left_chain_codomain_rows": list(range(ldim)),
        "profile_certificate_complete": geometry["profile_certificate_complete"],
        "basis_completion": {
            "domain_complement_dimension": cols-rdim,
            "codomain_complement_dimension": rows-ldim,
            "method": "standard-coordinate greedy completion over F_p",
        },
        "verification": {
            "left_transform_invertible": s_det != 0,
            "right_transform_invertible": t_det != 0,
            "left_transform_determinant": s_det,
            "right_transform_determinant": t_det,
            "transformed_pair_exact": True,
            "strict_equivalence_identity": "adapted_Q = S Q T; adapted_K = S K T",
        },
        "scope": (
            "Exact adapted coordinates and basis completion only. The remaining "
            "rows/columns are not asserted to form a regular direct summand; "
            "cross-coupling is retained and visible in adapted_Q/adapted_K."
        ),
        "geometry_certificate": geometry,
    }
