"""Primary decomposition of a finite-field operator into invariant subspaces.

The decomposition is exact over the base prime field.  It supplies a
block-diagonal coordinate system, but does not by itself choose rational
canonical cyclic generators inside each primary component.
"""
from __future__ import annotations

from typing import Sequence

from tools.rational_canonical import (
    _matrix_polynomial, _poly_power, _identity, _matmul,
    rational_canonical_profile,
)
from tools.regular_pencil_profile import _inverse_mod
from tools.spectral_fingerprint import factor_polynomial, characteristic_polynomial
from tools.regular_pencil_witness import _nullspace


def _columns_to_matrix(columns, n):
    return [[columns[j][i] for j in range(len(columns))] for i in range(n)]


def _kernel_basis(matrix, p):
    """Return a column basis for the kernel of a square matrix."""
    n = len(matrix)
    null_vectors = _nullspace(matrix, p, n)
    return _columns_to_matrix(null_vectors, n)


def _matrix_power(matrix, exponent, p):
    n = len(matrix)
    result = _identity(n, p)
    base = [[int(x) % p for x in row] for row in matrix]
    while exponent:
        if exponent & 1:
            result = _matmul(result, base, p)
        base = _matmul(base, base, p)
        exponent >>= 1
    return result


def rational_primary_decomposition(
    matrix: Sequence[Sequence[int]], p: int
) -> dict:
    """Return a verified primary invariant-subspace decomposition of A.

    For every irreducible factor f of the characteristic polynomial, the
    corresponding component is ker(f(A)^n).  The returned change-of-basis
    matrix has these component bases as consecutive column blocks.
    """
    profile = rational_canonical_profile(matrix, p)
    n = profile["dimension"]
    a = [[int(x) % p for x in row] for row in matrix]
    factors = factor_polynomial(characteristic_polynomial(a, p), p)
    components = []
    column_blocks = []
    for item in factors:
        if "degree" not in item:
            continue
        factor_desc = item["coefficients_descending"]
        factor_low = list(reversed(factor_desc))
        f_of_a = _matrix_polynomial(a, factor_low, p)
        annihilator = _matrix_power(f_of_a, n, p)
        basis = _kernel_basis(annihilator, p)
        dimension = len(basis[0]) if basis else 0
        if dimension == 0:
            continue
        column_blocks.append(basis)
        components.append({
            "factor_coefficients_descending": list(factor_desc),
            "dimension": dimension,
            "basis_columns": basis,
        })

    columns = [column for block in column_blocks for column in
               [[block[i][j] for i in range(n)]
                for j in range(len(block[0]) if block else 0)]]
    if sum(component["dimension"] for component in components) != n:
        raise ArithmeticError("primary component dimensions do not sum to n")
    change = _columns_to_matrix(columns, n)
    inverse = _inverse_mod(change, p)
    transformed = _matmul(_matmul(inverse, a, p), change, p)

    offsets = []
    cursor = 0
    for component in components:
        offsets.append((cursor, cursor + component["dimension"]))
        cursor += component["dimension"]
    off_block_zero = True
    for i in range(n):
        for j in range(n):
            block_i = next(k for k, (lo, hi) in enumerate(offsets) if lo <= i < hi)
            block_j = next(k for k, (lo, hi) in enumerate(offsets) if lo <= j < hi)
            if block_i != block_j and transformed[i][j] % p:
                off_block_zero = False
    if not off_block_zero:
        raise ArithmeticError("computed primary subspaces are not jointly invariant")
    return {
        "schema": "the-fold-rational-primary-decomposition-v1",
        "field": f"F_{p}",
        "dimension": n,
        "components": components,
        "change_of_basis_columns": change,
        "transformed_operator": transformed,
        "component_offsets": [list(pair) for pair in offsets],
        "checks": {
            "component_dimensions_sum_to_n": cursor == n,
            "change_of_basis_invertible": True,
            "operator_is_block_diagonal_by_primary_component": off_block_zero,
        },
        "rational_canonical_profile": profile,
        "scope": (
            "Exact primary invariant-subspace decomposition over F_p. "
            "It does not yet construct cyclic generators or a complete "
            "noncyclic pencil witness."
        ),
    }
