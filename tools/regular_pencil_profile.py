"""Complete strict-equivalence fingerprints in rational invertible charts."""
from __future__ import annotations

from typing import Sequence

from tools.rational_canonical import rational_canonical_profile
from tools.rectangular_pencil import _validate_pair


def _inverse_mod(matrix, p):
    n = len(matrix)
    augmented = [
        [int(x) % p for x in row] +
        [int(i == j) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if augmented[r][col]), None)
        if pivot is None:
            raise ValueError("matrix must be invertible over F_p")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        inverse = pow(augmented[col][col], -1, p)
        augmented[col] = [(x * inverse) % p for x in augmented[col]]
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor:
                augmented[row] = [
                    (x - factor*y) % p
                    for x, y in zip(augmented[row], augmented[col])
                ]
    return [row[n:] for row in augmented]


def _matmul(a, b, p):
    n, inner, m = len(a), len(b), len(b[0])
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for r in range(inner):
            value = a[i][r] % p
            if value:
                for j in range(m):
                    out[i][j] = (out[i][j] + value*b[r][j]) % p
    return out


def _mod_pair(q, k, p):
    return ([[int(x) % p for x in row] for row in q],
            [[int(x) % p for x in row] for row in k])


def _add_scaled(q, k, scalar, p):
    return [[(q[i][j] + scalar*k[i][j]) % p
             for j in range(len(q[0]))] for i in range(len(q))]


def _chart_candidates(p):
    # Finite points [1:lambda], then the point at infinity [0:1].
    return [(lam, "finite") for lam in range(p)] + [(None, "infinity")]


def _chart_operator(q, k, p, chart):
    n = len(q)
    if chart["kind"] == "finite":
        lam = chart["lambda"]
        pivot = _add_scaled(q, k, lam, p)
        inverse = _inverse_mod(pivot, p)
        operator = _matmul(inverse, k, p)
    else:
        inverse = _inverse_mod(k, p)
        operator = _matmul(inverse, q, p)
    return operator


def _profile_for_chart(q, k, p, chart):
    operator = _chart_operator(q, k, p, chart)
    profile = rational_canonical_profile(operator, p)
    finite = chart["kind"] == "finite"
    return {
        "schema": "the-fold-regular-pencil-similarity-profile-v2",
        "field": f"F_{p}",
        "shape": [len(q), len(q)],
        "chart": dict(chart),
        "normalized_operator": operator,
        "operator_rational_canonical_profile": profile,
        "complete_strict_equivalence_fingerprint_in_chart": True,
        "normalization": (
            "left multiply by (Q+lambda*K)^-1; normalized pair is "
            "(I-lambda*A,A), A=(Q+lambda*K)^-1*K"
            if finite else
            "left multiply by K^-1; normalized pair is (A,I), A=K^-1*Q"
        ),
        "scope": (
            "Complete for constant strict equivalence of ordered square "
            "pencils when the selected projective member is invertible "
            "over F_p. The coefficient pair is not permuted or mixed in "
            "the equivalence relation; the chart is only a normalization."
        ),
    }


def regular_pencil_similarity_profile(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int
) -> dict:
    """Find an invertible projective member and return its complete profile.

    Searches Q+lambda*K for lambda in F_p, then K (the point at infinity).
    Raises ValueError if no projective member is invertible over F_p. This
    can happen even for a regular pencil whose determinant polynomial is
    nonzero, because that polynomial may vanish at every F_p-rational point.
    """
    rows, cols = _validate_pair(q, k, p)
    if rows != cols:
        raise ValueError("regular-pencil profile requires square Q and K")
    q_mod, k_mod = _mod_pair(q, k, p)
    for lam, kind in _chart_candidates(p):
        if kind == "finite":
            pivot = _add_scaled(q_mod, k_mod, lam, p)
            chart = {"kind": kind, "lambda": lam, "projective_point": [1, lam]}
        else:
            pivot = k_mod
            chart = {"kind": kind, "lambda": None, "projective_point": [0, 1]}
        try:
            _inverse_mod(pivot, p)
        except ValueError:
            continue
        return _profile_for_chart(q_mod, k_mod, p, chart)
    raise ValueError(
        "no invertible projective member over F_p; the pencil may still be "
        "regular, so extension-field or other classification is required"
    )


def compare_regular_pencils(
    q_a: Sequence[Sequence[int]], k_a: Sequence[Sequence[int]],
    q_b: Sequence[Sequence[int]], k_b: Sequence[Sequence[int]], p: int,
) -> dict:
    """Compare ordered pencils using a common invertible projective chart.

    A common chart exists whenever the two pencils are strictly equivalent
    and either has an invertible F_p-rational projective member. If no common
    chart exists, the function returns an explicitly inconclusive result.
    """
    rows_a, cols_a = _validate_pair(q_a, k_a, p)
    rows_b, cols_b = _validate_pair(q_b, k_b, p)
    if rows_a != cols_a or rows_b != cols_b or (rows_a, cols_a) != (rows_b, cols_b):
        raise ValueError("both pencils must be square and have the same shape")
    qa, ka = _mod_pair(q_a, k_a, p)
    qb, kb = _mod_pair(q_b, k_b, p)

    for lam, kind in _chart_candidates(p):
        if kind == "finite":
            pa, pb = _add_scaled(qa, ka, lam, p), _add_scaled(qb, kb, lam, p)
            chart = {"kind": kind, "lambda": lam, "projective_point": [1, lam]}
        else:
            pa, pb = ka, kb
            chart = {"kind": kind, "lambda": None, "projective_point": [0, 1]}
        try:
            _inverse_mod(pa, p)
            _inverse_mod(pb, p)
        except ValueError:
            continue
        left = _profile_for_chart(qa, ka, p, chart)
        right = _profile_for_chart(qb, kb, p, chart)
        same = (
            left["operator_rational_canonical_profile"]
                ["invariant_factors_coefficients_descending"]
            == right["operator_rational_canonical_profile"]
                ["invariant_factors_coefficients_descending"]
        )
        return {
            "schema": "the-fold-regular-pencil-comparison-v2",
            "field": f"F_{p}",
            "decision_complete": True,
            "strictly_equivalent": same,
            "common_chart": chart,
            "comparison_basis": (
                "equality of complete rational-canonical invariant factors "
                "of the normalized operator in the same projective chart"
            ),
            "left_profile": left,
            "right_profile": right,
            "scope": (
                "Complete strict-equivalence decision for ordered square "
                "pencils sharing an invertible projective member over F_p."
            ),
        }
    return {
        "schema": "the-fold-regular-pencil-comparison-v2",
        "field": f"F_{p}",
        "decision_complete": False,
        "strictly_equivalent": None,
        "reason": (
            "the two pencils have no common invertible projective member "
            "over F_p; no conclusion follows from this chart method"
        ),
        "scope": (
            "Inconclusive is not a non-equivalence result. A regular pencil "
            "can have no invertible F_p-rational member."
        ),
    }
