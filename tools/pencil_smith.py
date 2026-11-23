"""Smith invariants for small rectangular linear matrix pencils over F_p[t].

For P(t)=Q+tK, determinantal divisors are gcds of all k-by-k minors.
Their monic quotients give the nonzero Smith invariant factors. Reversing
the pencil, K+tQ, records the corresponding chart at projective infinity.

This deliberately does not claim to recover Kronecker minimal indices.
"""
from __future__ import annotations

from itertools import combinations, permutations
from math import comb
from typing import Sequence

from tools.rectangular_pencil import _validate_pair
from tools.spectral_fingerprint import _is_prime

Poly = list[int]  # low-degree-first coefficients


def _trim(poly: Sequence[int], p: int) -> Poly:
    out = [int(x) % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def _add(a: Poly, b: Poly, p: int) -> Poly:
    return _trim([(a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))], p)


def _sub(a: Poly, b: Poly, p: int) -> Poly:
    return _add(a, [(-x) % p for x in b], p)


def _mul(a: Poly, b: Poly, p: int) -> Poly:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return _trim(out, p)


def _divmod(a: Poly, b: Poly, p: int) -> tuple[Poly, Poly]:
    numerator, denominator = _trim(a, p), _trim(b, p)
    if denominator == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    remainder = numerator[:]
    inverse = pow(denominator[-1], -1, p)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] * inverse % p
        quotient[shift] = factor
        for i, value in enumerate(denominator):
            remainder[shift + i] = (remainder[shift + i] -
                                    factor * value) % p
        remainder = _trim(remainder, p)
    return _trim(quotient, p), remainder


def _monic(poly: Poly, p: int) -> Poly:
    out = _trim(poly, p)
    if out == [0]:
        return out
    inverse = pow(out[-1], -1, p)
    return [(x * inverse) % p for x in out]


def _gcd(a: Poly, b: Poly, p: int) -> Poly:
    x, y = _trim(a, p), _trim(b, p)
    while y != [0]:
        _, remainder = _divmod(x, y, p)
        x, y = y, remainder
    return _monic(x, p)


def _determinant_polynomial(matrix: list[list[Poly]], p: int) -> Poly:
    n = len(matrix)
    if n == 0:
        return [1]
    result = [0]
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        term = [1]
        for row, col in enumerate(perm):
            term = _mul(term, matrix[row][col], p)
            if term == [0]:
                break
        if inversions % 2:
            term = [(-x) % p for x in term]
        result = _add(result, term, p)
    return _trim(result, p)


def _smith_data(q, k, p: int, max_minors: int) -> dict:
    rows, cols = len(q), len(q[0])
    limit = min(rows, cols)
    total_minors = sum(comb(rows, size) * comb(cols, size)
                       for size in range(1, limit + 1))
    if total_minors > max_minors:
        raise ValueError(
            f"pencil exceeds minor budget ({total_minors} > {max_minors})"
        )

    matrix = [
        [[int(q[i][j]) % p, int(k[i][j]) % p]
         for j in range(cols)]
        for i in range(rows)
    ]
    divisors: list[Poly] = [[1]]
    invariant_factors: list[Poly] = []
    normal_rank = 0
    minors_examined = 0

    for size in range(1, limit + 1):
        divisor = [0]
        for row_ids in combinations(range(rows), size):
            for col_ids in combinations(range(cols), size):
                minor = [[matrix[i][j] for j in col_ids]
                         for i in row_ids]
                determinant = _determinant_polynomial(minor, p)
                minors_examined += 1
                if determinant != [0]:
                    divisor = _gcd(divisor, determinant, p)
                    if divisor == [1]:
                        # gcd with further polynomials remains one
                        pass
        if divisor == [0]:
            break
        divisor = _monic(divisor, p)
        quotient, remainder = _divmod(divisor, divisors[-1], p)
        if remainder != [0]:
            raise ArithmeticError("determinantal divisors failed divisibility")
        divisors.append(divisor)
        invariant_factors.append(_monic(quotient, p))
        normal_rank = size

    return {
        "normal_rank_over_rational_function_field": normal_rank,
        "determinantal_divisors_low_degree_first": divisors[1:],
        "smith_invariant_factors_low_degree_first": invariant_factors,
        "minor_count": minors_examined,
        "minor_budget": max_minors,
    }


def rectangular_pencil_smith_profile(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
    *,
    max_minors: int = 2000,
) -> dict:
    """Compute finite and infinite Smith data for Q+tK, without padding.

    The nonzero Smith factors describe the regular elementary-divisor data
    visible in this polynomial presentation. Singular minimal indices are
    not computed; this is not a complete Kronecker canonical form.
    """
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(max_minors, int) or max_minors < 1:
        raise ValueError("max_minors must be a positive integer")

    finite = _smith_data(q, k, p, max_minors)
    infinite = _smith_data(k, q, p, max_minors)
    return {
        "schema": "the-fold-pencil-smith-v1",
        "field": f"F_{p}",
        "shape": [rows, cols],
        "pencil": "Q + t K",
        "finite_chart": finite,
        "infinity_chart": {
            **infinite,
            "pencil": "K + t Q (reversed pencil)",
        },
        "scope": (
            "Smith invariant factors in the finite and reversed polynomial "
            "charts; singular Kronecker minimal indices are not recovered"
        ),
        "complete_kronecker_classification": False,
        "method": (
            "exact polynomial determinants of all minors, polynomial gcds, "
            "and determinantal-divisor quotients over F_p[t]"
        ),
    }
