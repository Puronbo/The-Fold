"""Complete strict-equivalence fingerprints for pencils with invertible Q."""
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
            raise ValueError("Q must be invertible over F_p")
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


def regular_pencil_similarity_profile(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int
) -> dict:
    """Classify Q+tK under constant strict equivalence when Q is invertible.

    Left-normalization gives (Q,K) ~ (I,Q^{-1}K). Two normalized pairs
    (I,A), (I,B) are strictly equivalent exactly when A and B are similar.
    Thus the invariant factors of Q^{-1}K are a complete strict-equivalence
    fingerprint in this Q-invertible chart.
    """
    rows, cols = _validate_pair(q, k, p)
    if rows != cols:
        raise ValueError("Q-invertible regular-pencil profile requires square Q")
    q_mod = [[int(x) % p for x in row] for row in q]
    k_mod = [[int(x) % p for x in row] for row in k]
    q_inverse = _inverse_mod(q_mod, p)
    n = rows
    operator = [[
        sum(q_inverse[i][r] * k_mod[r][j] for r in range(n)) % p
        for j in range(n)
    ] for i in range(n)]
    profile = rational_canonical_profile(operator, p)
    return {
        "schema": "the-fold-regular-pencil-similarity-profile-v1",
        "field": f"F_{p}",
        "shape": [n, n],
        "normalization": "left multiply by Q^{-1}: (Q,K) -> (I,Q^{-1}K)",
        "normalized_operator": operator,
        "operator_rational_canonical_profile": profile,
        "complete_strict_equivalence_fingerprint_in_Q_invertible_chart": True,
        "scope": (
            "Complete for constant strict equivalence of ordered pairs (Q,K) "
            "with Q invertible over F_p. It does not cover regular pencils "
            "whose Q coefficient is singular, and it does not allow mixing "
            "the two pencil coefficients."
        ),
    }


def compare_regular_pencils(
    q_a: Sequence[Sequence[int]], k_a: Sequence[Sequence[int]],
    q_b: Sequence[Sequence[int]], k_b: Sequence[Sequence[int]], p: int,
) -> dict:
    """Compare two Q-invertible ordered pencils by complete strict-equivalence data."""
    left = regular_pencil_similarity_profile(q_a, k_a, p)
    right = regular_pencil_similarity_profile(q_b, k_b, p)
    same = (
        left["operator_rational_canonical_profile"]
            ["invariant_factors_coefficients_descending"]
        == right["operator_rational_canonical_profile"]
            ["invariant_factors_coefficients_descending"]
    )
    return {
        "schema": "the-fold-regular-pencil-comparison-v1",
        "field": f"F_{p}",
        "strictly_equivalent": same,
        "comparison_basis": "equality of complete rational-canonical invariant factors of Q^{-1}K",
        "left_profile": left,
        "right_profile": right,
        "scope": (
            "The equivalence decision is complete for ordered square pencils "
            "whose first coefficient is invertible over the selected prime field."
        ),
    }
