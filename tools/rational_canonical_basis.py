"""Full rational-canonical bases and exact operator similarity witnesses.

The construction composes primary invariant-subspace bases with bounded cyclic
summand generators. Every returned basis is checked against its companion
block matrix by the exact identity A K = K C over F_p.
"""
from __future__ import annotations

from typing import Sequence

from tools.rational_canonical import (
    _identity, _matmul, _poly_power, rational_canonical_profile,
)
from tools.rational_primary_decomposition import rational_primary_decomposition
from tools.rational_primary_cyclic import construct_primary_cyclic_summands
from tools.regular_pencil_profile import _inverse_mod


def _block_diag(blocks):
    n = sum(len(block) for block in blocks)
    out = [[0] * n for _ in range(n)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = value
        offset += len(block)
    return out


def _companion_low(poly, p):
    coeffs = [int(x) % p for x in poly]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    if len(coeffs) < 2 or coeffs[-1] != 1:
        raise ValueError("companion polynomial must be monic and nonconstant")
    n = len(coeffs) - 1
    out = [[0] * n for _ in range(n)]
    for i in range(1, n):
        out[i][i - 1] = 1
    for i in range(n):
        out[i][n - 1] = (-coeffs[i]) % p
    return out


def _matrix_equal(a, b, p):
    return len(a) == len(b) and all(
        len(a[i]) == len(b[i]) and
        all((a[i][j] - b[i][j]) % p == 0 for j in range(len(a[i])))
        for i in range(len(a))
    )


def _mat_sub(a, b, p):
    return [[(a[i][j] - b[i][j]) % p for j in range(len(a[0]))]
            for i in range(len(a))]


def construct_rational_canonical_basis(
    matrix: Sequence[Sequence[int]],
    p: int,
    *,
    max_candidates: int = 100_000,
) -> dict:
    """Return K,C with K invertible and K^-1 A K = C, when search succeeds.

    Elementary-divisor generators are found independently in each primary
    component. The returned C is the direct sum of companion matrices for
    the elementary divisors f^e. Candidate search is bounded and may return
    an incomplete result without asserting nonexistence.
    """
    profile = rational_canonical_profile(matrix, p)
    n = profile["dimension"]
    a = [[int(x) % p for x in row] for row in matrix]
    primary = rational_primary_decomposition(a, p)
    transformed = primary["transformed_operator"]
    component_results = []
    basis_blocks = []
    companion_blocks = []
    all_complete = True
    for component, (lo, hi) in zip(
        primary["components"], primary["component_offsets"]
    ):
        d = hi - lo
        primary_matrix = [row[lo:hi] for row in transformed[lo:hi]]
        factor_desc = component["factor_coefficients_descending"]
        profile_item = next(
            item for item in profile["irreducible_primary_components"]
            if item["factor_coefficients_descending"] == factor_desc
        )
        exponents = profile_item["elementary_divisor_exponents_descending"]
        cyclic = construct_primary_cyclic_summands(
            primary_matrix, p, factor_desc, exponents,
            max_candidates=max_candidates,
        )
        component_results.append(cyclic)
        if not cyclic["basis_complete"]:
            all_complete = False
            continue
        local_basis = cyclic["change_of_basis_columns"]
        global_component_basis = component["basis_columns"]
        basis_blocks.append(_matmul(global_component_basis, local_basis, p))
        factor_low = list(reversed(factor_desc))
        for exponent in exponents:
            polynomial = _poly_power(factor_low, exponent, p)
            companion_blocks.append(_companion_low(polynomial, p))

    if not all_complete:
        return {
            "schema": "the-fold-rational-canonical-basis-v1",
            "field": f"F_{p}",
            "dimension": n,
            "basis_complete": False,
            "search_complete": all(item["search_complete"] for item in component_results),
            "component_results": component_results,
            "basis": None,
            "canonical_operator": None,
            "checks": {"basis_invertible": False, "similarity_identity": False},
            "scope": "Bounded exact cyclic-generator search; incomplete means no conclusion about existence.",
        }

    basis = [[0] * n for _ in range(n)]
    cursor = 0
    for block in basis_blocks:
        width = len(block[0])
        for i in range(n):
            basis[i][cursor:cursor + width] = block[i]
        cursor += width
    canonical = _block_diag(companion_blocks)
    if cursor != n or len(canonical) != n:
        raise ArithmeticError("assembled rational canonical dimensions do not sum to n")
    inverse = _inverse_mod(basis, p)
    conjugated = _matmul(_matmul(inverse, a, p), basis, p)
    identity = _matrix_equal(conjugated, canonical, p)
    if not identity:
        raise ArithmeticError("assembled cyclic basis failed A K = K C verification")
    return {
        "schema": "the-fold-rational-canonical-basis-v1",
        "field": f"F_{p}",
        "dimension": n,
        "basis_complete": True,
        "search_complete": all(item["search_complete"] for item in component_results),
        "basis": basis,
        "canonical_operator": canonical,
        "inverse_basis": inverse,
        "component_results": component_results,
        "rational_canonical_profile": profile,
        "checks": {
            "basis_invertible": True,
            "similarity_identity": identity,
            "operator_equals_basis_canonical_basis_inverse": identity,
            "elementary_divisor_blocks_match_profile": True,
        },
        "scope": "Exact certificate when bounded cyclic-generator searches succeed; generator discovery remains budget-bounded.",
    }


def construct_operator_similarity_witness(
    matrix_a: Sequence[Sequence[int]],
    matrix_b: Sequence[Sequence[int]],
    p: int,
    *,
    max_candidates: int = 100_000,
) -> dict:
    """Construct P with P A = B P using shared rational-canonical blocks."""
    profile_a = rational_canonical_profile(matrix_a, p)
    profile_b = rational_canonical_profile(matrix_b, p)
    if profile_a["dimension"] != profile_b["dimension"]:
        return {
            "schema": "the-fold-operator-similarity-witness-v1",
            "similar": False, "decision_complete": True, "witness_found": False,
            "reason": "dimension_mismatch",
        }
    if (profile_a["invariant_factors_coefficients_descending"] !=
            profile_b["invariant_factors_coefficients_descending"]):
        return {
            "schema": "the-fold-operator-similarity-witness-v1",
            "similar": False, "decision_complete": True, "witness_found": False,
            "reason": "rational_canonical_profiles_differ",
        }
    basis_a = construct_rational_canonical_basis(
        matrix_a, p, max_candidates=max_candidates
    )
    basis_b = construct_rational_canonical_basis(
        matrix_b, p, max_candidates=max_candidates
    )
    if not basis_a["basis_complete"] or not basis_b["basis_complete"]:
        return {
            "schema": "the-fold-operator-similarity-witness-v1",
            "similar": True, "decision_complete": True, "witness_found": False,
            "search_complete": basis_a["search_complete"] and basis_b["search_complete"],
            "reason": "similarity_decided_by_complete_rational_canonical_profile_but_basis_search_incomplete",
            "basis_a": basis_a, "basis_b": basis_b,
        }
    pmat = _matmul(basis_b["basis"], basis_a["inverse_basis"], p)
    a = [[int(x) % p for x in row] for row in matrix_a]
    b = [[int(x) % p for x in row] for row in matrix_b]
    left = _matmul(pmat, a, p)
    right = _matmul(b, pmat, p)
    verified = _matrix_equal(left, right, p)
    if not verified:
        raise ArithmeticError("constructed intertwiner failed P A = B P")
    return {
        "schema": "the-fold-operator-similarity-witness-v1",
        "similar": True,
        "decision_complete": True,
        "witness_found": True,
        "intertwiner": pmat,
        "canonical_operator": basis_a["canonical_operator"],
        "basis_a": basis_a["basis"],
        "basis_b": basis_b["basis"],
        "checks": {"intertwining_identity": verified, "basis_canonical_forms_equal": _matrix_equal(
            basis_a["canonical_operator"], basis_b["canonical_operator"], p
        )},
        "scope": "Exact finite-field similarity certificate; cyclic basis search is bounded.",
    }
