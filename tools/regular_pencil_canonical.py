"""Canonical block representatives for regular pencils over prime fields."""
from __future__ import annotations

from typing import Sequence

from tools.regular_pencil_classification import regular_pencil_complete_profile
from tools.rectangular_pencil import _validate_pair


def _trim(poly):
    out = [int(x) for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def _companion_from_low(poly, p):
    """Companion matrix of a monic polynomial, coefficients low-degree first."""
    coeffs = [x % p for x in _trim(poly)]
    if coeffs[-1] != 1 or len(coeffs) < 2:
        raise ValueError("companion polynomial must be monic and nonconstant")
    n = len(coeffs) - 1
    matrix = [[0] * n for _ in range(n)]
    for i in range(1, n):
        matrix[i][i - 1] = 1
    for i in range(n):
        matrix[i][n - 1] = (-coeffs[i]) % p
    return matrix


def _nilpotent_jordan(size):
    block = [[0] * size for _ in range(size)]
    for i in range(size - 1):
        block[i][i + 1] = 1
    return block


def _block_diag(blocks):
    size = sum(len(block) for block in blocks)
    result = [[0] * size for _ in range(size)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                result[offset + i][offset + j] = value
        offset += len(block)
    return result


def _identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def regular_pencil_canonical_form(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
    *,
    max_minors: int = 2000,
) -> dict:
    """Assemble a Weierstrass-type canonical representative for a regular pencil.

    For each nonconstant finite Smith invariant factor d(t), append the
    block (-C(d), I), so det(tI-C(d))=d(t). For each infinity divisor size e,
    append (I, N_e), where N_e is a nilpotent Jordan block. Unit invariant
    factors contribute no finite block.
    """
    rows, cols = _validate_pair(q, k, p)
    if rows != cols:
        raise ValueError("canonical regular-pencil form requires square matrices")
    profile = regular_pencil_complete_profile(q, k, p, max_minors=max_minors)
    finite_factors = profile["finite_smith_invariant_factors_low_degree_first"]
    finite_blocks = []
    for factor in finite_factors:
        coeffs = _trim(factor)
        if len(coeffs) == 1:
            if coeffs[0] % p != 1:
                raise ArithmeticError("Smith invariant factor is not normalized to one")
            continue
        companion = _companion_from_low(coeffs, p)
        finite_blocks.append({
            "polynomial_coefficients_low_degree_first": coeffs,
            "dimension": len(coeffs) - 1,
            "Q_block": [[(-x) % p for x in row] for row in companion],
            "K_block": _identity(len(coeffs) - 1),
        })
    infinity_blocks = [
        {"size": size, "Q_block": _identity(size),
         "K_block": _nilpotent_jordan(size)}
        for size in profile["infinity_elementary_divisor_sizes"]
    ]
    q_blocks = [item["Q_block"] for item in finite_blocks] + [
        item["Q_block"] for item in infinity_blocks
    ]
    k_blocks = [item["K_block"] for item in finite_blocks] + [
        item["K_block"] for item in infinity_blocks
    ]
    canonical_q, canonical_k = _block_diag(q_blocks), _block_diag(k_blocks)
    dimension = sum(len(block) for block in q_blocks)
    if dimension != rows:
        raise ArithmeticError("canonical block dimensions do not sum to pencil dimension")
    canonical_profile = regular_pencil_complete_profile(
        canonical_q, canonical_k, p, max_minors=max_minors
    )
    same = (
        canonical_profile["finite_smith_invariant_factors_low_degree_first"]
        == profile["finite_smith_invariant_factors_low_degree_first"]
        and canonical_profile["infinity_elementary_divisor_sizes"]
        == profile["infinity_elementary_divisor_sizes"]
    )
    if not same:
        raise ArithmeticError("assembled canonical pencil failed profile verification")
    return {
        "schema": "the-fold-regular-pencil-canonical-form-v1",
        "field": f"F_{p}",
        "dimension": rows,
        "canonical_Q": canonical_q,
        "canonical_K": canonical_k,
        "finite_blocks": finite_blocks,
        "infinity_blocks": infinity_blocks,
        "source_profile": profile,
        "canonical_profile": canonical_profile,
        "checks": {
            "block_dimensions_sum_to_n": dimension == rows,
            "canonical_profile_matches_source": same,
        },
        "scope": (
            "Constructs and independently verifies a canonical block representative. "
            "It does not yet construct constant left/right transformations from "
            "the original pencil to this representative."
        ),
    }
