"""Exact finite-field interaction profiles for paired Q/K projections.

For equal-shaped Q and K (out_features x in_features), the module profiles
Q K^T in output space and Q^T K in input space. With row-vector inputs X,
(X Q^T)(X K^T)^T = X (Q^T K) X^T.
"""
from __future__ import annotations

from typing import Sequence

from tools.prime_spectral_profile import prime_spectral_profile
from tools.spectral_fingerprint import rank_mod


def _validate_pair(q: Sequence[Sequence[int]],
                   k: Sequence[Sequence[int]]) -> tuple[int, int]:
    if not q or not k:
        raise ValueError("Q and K must be non-empty matrices")
    q_width = len(q[0])
    k_width = len(k[0])
    if q_width < 1 or k_width < 1:
        raise ValueError("Q and K must have non-empty rows")
    if any(len(row) != q_width for row in q):
        raise ValueError("Q must be rectangular")
    if any(len(row) != k_width for row in k):
        raise ValueError("K must be rectangular")
    if (len(q), q_width) != (len(k), k_width):
        raise ValueError("Q and K must have identical shapes")
    return len(q), q_width


def _transpose(matrix: Sequence[Sequence[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def _matmul(a: Sequence[Sequence[int]],
            b: Sequence[Sequence[int]]) -> list[list[int]]:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix product dimensions")
    bt = _transpose(b)
    return [
        [sum(int(x) * int(y) for x, y in zip(row, col)) for col in bt]
        for row in a
    ]


def _profile(matrix: list[list[int]], primes: Sequence[int]) -> dict:
    return {
        "shape": [len(matrix), len(matrix[0])],
        "rank_by_prime": {str(p): rank_mod(matrix, p) for p in primes},
        "spectral_profile": (
            prime_spectral_profile(matrix, primes)
            if len(matrix) == len(matrix[0]) else None
        ),
    }


def analyze_qk_interaction(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    primes: Sequence[int],
) -> dict:
    """Profile the two natural square products formed from equal-shaped Q,K."""
    output_dim, input_dim = _validate_pair(q, k)
    if not primes:
        raise ValueError("primes must be non-empty")
    qk_transpose = _matmul(q, _transpose(k))
    qt_k = _matmul(_transpose(q), k)
    output_profile = _profile(qk_transpose, primes)
    input_profile = _profile(qt_k, primes)

    q_square_profile = (
        prime_spectral_profile(q, primes) if output_dim == input_dim else None
    )
    k_square_profile = (
        prime_spectral_profile(k, primes) if output_dim == input_dim else None
    )
    return {
        "schema": "the-fold-qk-interaction-profile-v1",
        "projection_shape": [output_dim, input_dim],
        "products": {
            "output_space_qk_transpose": {
                "definition": "Q K^T",
                **output_profile,
            },
            "input_space_q_transpose_k": {
                "definition": "Q^T K",
                **input_profile,
            },
        },
        "individual_square_projection_profiles": {
            "q": q_square_profile,
            "k": k_square_profile,
        },
        "attention_identity": (
            "(X Q^T)(X K^T)^T = X (Q^T K) X^T for row-vector inputs X"
        ),
        "limitations": [
            "Q and K must have identical two-dimensional shapes in this initial interface.",
            "Products are formed exactly over integers, then reduced by the finite-field profile engine.",
            "Profiles depend on the already-quantized Q and K entries and selected primes.",
            "A product fingerprint is not invariant under arbitrary basis changes and does not establish equal attention outputs.",
            "No softmax, value projection, residual path, or model forward pass is evaluated.",
        ],
    }
