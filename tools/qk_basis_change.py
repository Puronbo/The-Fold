"""Basis-change tests for the Q/K input-space interaction.

For Q,K in Z^(d_o x d_i), an integer unimodular B acts by
Q' = Q B and K' = K B^(-T). Then Q'^T K' = B^T (Q^T K) B^(-T),
so the input-space interaction is similar over every prime field.
"""
from __future__ import annotations

from typing import Sequence

from tools.qk_interaction import _matmul, _transpose, _profile, _validate_pair


def _identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def _validate_basis(b: Sequence[Sequence[int]],
                    inverse_transpose: Sequence[Sequence[int]],
                    dimension: int) -> None:
    if len(b) != dimension or any(len(row) != dimension for row in b):
        raise ValueError("basis matrix must be square with input dimension")
    if (len(inverse_transpose) != dimension
            or any(len(row) != dimension for row in inverse_transpose)):
        raise ValueError("inverse-transpose matrix has incompatible shape")
    # B^T C = I and C B^T = I; requiring exact integer inverses
    # ensures the transformation is unimodular over every prime.
    bt = _transpose(b)
    if _matmul(bt, inverse_transpose) != _identity(dimension):
        raise ValueError("supplied matrix is not the exact integer B^(-T)")
    if _matmul(inverse_transpose, bt) != _identity(dimension):
        raise ValueError("supplied matrix is not the exact integer B^(-T)")


def _rank_signature(matrix: Sequence[Sequence[int]], primes: Sequence[int]) -> dict:
    from tools.spectral_fingerprint import rank_mod
    return {str(p): rank_mod(matrix, p) for p in primes}


def analyze_qk_basis_change(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    basis: Sequence[Sequence[int]],
    inverse_transpose: Sequence[Sequence[int]],
    primes: Sequence[int],
) -> dict:
    """Check interaction-profile invariance under an integer unimodular basis."""
    output_dim, input_dim = _validate_pair(q, k)
    if not primes:
        raise ValueError("primes must be non-empty")
    _validate_basis(basis, inverse_transpose, input_dim)

    qt_k = _matmul(_transpose(q), k)
    q_new = _matmul(q, basis)
    k_new = _matmul(k, inverse_transpose)
    qt_k_new = _matmul(_transpose(q_new), k_new)

    before = _profile(qt_k, primes)
    after = _profile(qt_k_new, primes)
    q_rank_before = _rank_signature(q, primes)
    q_rank_after = _rank_signature(q_new, primes)
    k_rank_before = _rank_signature(k, primes)
    k_rank_after = _rank_signature(k_new, primes)

    return {
        "schema": "the-fold-qk-basis-change-v1",
        "projection_shape": [output_dim, input_dim],
        "basis": [list(row) for row in basis],
        "inverse_transpose": [list(row) for row in inverse_transpose],
        "interaction": {
            "definition": "Q^T K",
            "before": before,
            "after": after,
            "same_full_finite_field_profiles": (
                before["spectral_profile"] == after["spectral_profile"]
                and before["rank_by_prime"] == after["rank_by_prime"]
            ),
        },
        "individual_projection_ranks": {
            "q": {
                "before": q_rank_before,
                "after": q_rank_after,
                "preserved": q_rank_before == q_rank_after,
            },
            "k": {
                "before": k_rank_before,
                "after": k_rank_after,
                "preserved": k_rank_before == k_rank_after,
            },
        },
        "algebraic_identity": "Q'^T K' = B^T (Q^T K) B^(-T)",
        "guarantee": (
            "Because B and its supplied inverse transpose are integer inverses, "
            "B is unimodular and remains invertible modulo every prime."
        ),
        "limitations": [
            "This tests a specific coordinated change of feature coordinates, not arbitrary Q/K perturbations.",
            "Only the input-space product Q^T K is guaranteed similar; QK^T and individual spectra need not be preserved.",
            "A finite-field similarity invariant does not by itself imply equality of real-valued model behavior under arbitrary activation-coordinate changes.",
        ],
    }
