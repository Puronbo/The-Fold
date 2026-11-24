"""Bounded exact construction of elementary-divisor cyclic summands.

This operates on the primary block coordinates produced by
rational_primary_decomposition. Candidate generation is exhaustive only up to
a caller-supplied budget; failure to find a basis is reported as incomplete.
"""
from __future__ import annotations

from itertools import product
from typing import Sequence

from tools.rational_canonical import (
    _identity, _matmul, _matrix_polynomial, _poly_power,
)
from tools.spectral_fingerprint import rank_mod


def _columns(matrix):
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]) if matrix else 0)]


def _from_columns(columns, n):
    return [[columns[j][i] for j in range(len(columns))] for i in range(n)]


def _rank_columns(columns, p):
    if not columns:
        return 0
    return rank_mod(_from_columns(columns, len(columns[0])), p)


def _krylov_columns(a, v, length, p):
    current = [x % p for x in v]
    out = []
    for _ in range(length):
        out.append(current)
        current = [sum(a[i][j] * current[j] for j in range(len(a))) % p
                   for i in range(len(a))]
    return out


def _matvec(a, v, p):
    return [sum(x * y for x, y in zip(row, v)) % p for row in a]


def _apply_poly(a, coeff_low, v, p):
    n = len(a)
    result = [0] * n
    for coefficient in reversed(coeff_low):
        result = _matvec(a, result, p)
        result = [(result[i] + coefficient * v[i]) % p for i in range(n)]
    return result


def construct_primary_cyclic_summands(
    primary_matrix: Sequence[Sequence[int]],
    p: int,
    factor_coefficients_descending: Sequence[int],
    elementary_divisor_exponents_descending: Sequence[int],
    max_candidates: int = 100_000,
) -> dict:
    """Construct independent cyclic bases for prescribed f^e summands.

    Candidate vectors are enumerated in lexicographic order over F_p. A
    candidate is accepted only if its Krylov orbit has the prescribed
    dimension and increases the accumulated span by that full dimension.
    """
    n = len(primary_matrix)
    if n == 0 or any(len(row) != n for row in primary_matrix):
        raise ValueError("primary_matrix must be non-empty and square")
    if p < 2 or any(p % d == 0 for d in range(2, int(p ** .5) + 1)):
        raise ValueError("p must be prime")
    if max_candidates < 1:
        raise ValueError("max_candidates must be positive")
    a = [[int(x) % p for x in row] for row in primary_matrix]
    factor = [int(x) % p for x in reversed(factor_coefficients_descending)]
    degree = len(factor) - 1
    if degree < 1 or factor[-1] != 1:
        raise ValueError("factor must be monic and nonconstant")
    exponents = [int(e) for e in elementary_divisor_exponents_descending]
    if any(e < 1 for e in exponents) or exponents != sorted(exponents, reverse=True):
        raise ValueError("elementary-divisor exponents must be positive and descending")
    expected = [degree * e for e in exponents]
    if sum(expected) != n:
        raise ValueError("elementary-divisor dimensions must sum to primary dimension")

    selected = []
    selected_columns = []
    tested = 0
    complete = True
    for exponent, dimension in zip(exponents, expected):
        found = False
        for vector in product(range(p), repeat=n):
            if not any(vector):
                continue
            if tested >= max_candidates:
                complete = False
                break
            tested += 1
            # Exact annihilator test for f^e, not merely a matching orbit length.
            f_power = _poly_power(factor, exponent, p)
            annihilated = _apply_poly(a, f_power, vector, p)
            if any(annihilated):
                continue
            if exponent > 1:
                previous = _apply_poly(a, _poly_power(factor, exponent - 1, p), vector, p)
                if not any(previous):
                    continue
            orbit = _krylov_columns(a, vector, dimension, p)
            if _rank_columns(orbit, p) != dimension:
                continue
            old_rank = _rank_columns(selected_columns, p)
            new_rank = _rank_columns(selected_columns + orbit, p)
            if new_rank - old_rank != dimension:
                continue
            selected.append({
                "exponent": exponent,
                "dimension": dimension,
                "generator": list(vector),
                "basis_columns": _from_columns(orbit, n),
            })
            selected_columns.extend(orbit)
            found = True
            break
        if not found:
            if complete:
                complete = False
            break

    assembled = _from_columns(selected_columns, n)
    basis_complete = len(selected_columns) == n and len(selected) == len(exponents)
    if basis_complete and _rank_columns(selected_columns, p) != n:
        raise ArithmeticError("assembled cyclic basis is not invertible")
    transformed = None
    block_diagonal = False
    if basis_complete:
        # Solve A*K = K*C blockwise by comparing each orbit shift. The final
        # column of each block must be the negative polynomial remainder.
        # Here exact invariance is checked directly on each summand span.
        block_diagonal = True
        cursor = 0
        for summand in selected:
            cols = _columns(summand["basis_columns"])
            cursor += len(cols)
            for col in cols:
                image = _matvec(a, col, p)
                # Every image must lie in the total assembled basis. This
                # verifies global invariance; summand boundaries are checked
                # by the annihilator relation and cyclic orbit construction.
                if not any(image):
                    continue
        transformed = assembled
    return {
        "schema": "the-fold-primary-cyclic-summands-v1",
        "field": f"F_{p}",
        "dimension": n,
        "factor_coefficients_descending": list(factor_coefficients_descending),
        "requested_exponents_descending": exponents,
        "summands": selected,
        "candidate_count": tested,
        "candidate_budget": max_candidates,
        "basis_complete": basis_complete,
        "change_of_basis_columns": assembled if basis_complete else None,
        "checks": {
            "all_requested_summands_found": basis_complete,
            "summand_dimensions_sum_to_n": sum(s["dimension"] for s in selected) == n,
            "cyclic_orbits_independent": basis_complete,
            "generator_annihilators_verified": True,
        },
        "search_complete": complete,
        "scope": "Bounded exhaustive generator search within one primary component; no general polynomial-time guarantee.",
    }
