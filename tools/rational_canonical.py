"""Rational canonical forms over prime fields via primary kernel growth.

For each irreducible factor f of chi_A, nullities of f(A)^k recover
the elementary-divisor exponents. These assemble into invariant factors.
All polynomial and matrix arithmetic is exact over F_p.
"""
from __future__ import annotations

from typing import Sequence

from tools.spectral_fingerprint import (
    _is_prime, _poly_mul, _poly_trim, _poly_add, _poly_sub,
    _poly_powmod, factor_polynomial, characteristic_polynomial, rank_mod,
)


def _validate(matrix: Sequence[Sequence[int]], p: int) -> int:
    if not _is_prime(p):
        raise ValueError("p must be prime")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be non-empty and square")
    return n


def _identity(n: int, p: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def _matmul(a, b, p):
    n, m = len(a), len(b[0])
    inner = len(b)
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(inner):
            x = a[i][k] % p
            if x:
                for j in range(m):
                    out[i][j] = (out[i][j] + x * b[k][j]) % p
    return out


def _matrix_polynomial(matrix, coefficients_low, p):
    """Evaluate sum c_i A^i by Horner's rule."""
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    identity = _identity(n, p)
    for coefficient in reversed(coefficients_low):
        result = _matmul(result, matrix, p)
        c = int(coefficient) % p
        if c:
            for i in range(n):
                result[i][i] = (result[i][i] + c) % p
    return result


def _poly_power(a, exponent, p):
    result = [1]
    base = list(a)
    while exponent:
        if exponent & 1:
            result = _poly_mul(result, base, p)
        base = _poly_mul(base, base, p)
        exponent >>= 1
    return result


def _elementary_divisors(matrix, factor_desc, p):
    n = len(matrix)
    f_low = list(reversed(factor_desc))
    degree = len(f_low) - 1
    operator = _matrix_polynomial(matrix, f_low, p)
    power = _identity(n, p)
    nullities = [0]
    exponents = []
    for k in range(1, n // degree + 1):
        power = _matmul(power, operator, p)
        nullity = n - rank_mod(power, p)
        if nullity % degree:
            raise ArithmeticError("primary nullity is not divisible by factor degree")
        nullities.append(nullity)
        scaled = nullity // degree
        previous = nullities[-2] // degree
        exponents.append(scaled - previous)
        if nullities[-1] == nullities[-2]:
            break
    # Difference sequence counts blocks of size >= k.
    exact = {}
    for k, at_least in enumerate(exponents, start=1):
        next_value = exponents[k] if k < len(exponents) else 0
        if at_least - next_value:
            exact[k] = at_least - next_value
    blocks = []
    for size, count in sorted(exact.items(), reverse=True):
        blocks.extend([size] * count)
    return {
        "factor_coefficients_descending": list(factor_desc),
        "factor_degree": degree,
        "primary_nullities_over_base_field": nullities,
        "kernel_dimensions_over_extension_degree_units": [
            value // degree for value in nullities
        ],
        "blocks_at_least": exponents,
        "elementary_divisor_exponents_descending": blocks,
        "elementary_divisors": [
            {"factor_power": size, "multiplicity": count}
            for size, count in sorted(exact.items())
        ],
    }


def rational_canonical_profile(matrix: Sequence[Sequence[int]], p: int) -> dict:
    """Return elementary divisors and invariant factors for A over F_p."""
    n = _validate(matrix, p)
    a = [[int(x) % p for x in row] for row in matrix]
    char_desc = characteristic_polynomial(a, p)
    factors = factor_polynomial(char_desc, p)
    primary = [
        _elementary_divisors(a, item["coefficients_descending"], p)
        for item in factors if "degree" in item
    ]

    # Align each irreducible's elementary-divisor list on the right.
    count = max((len(item["elementary_divisor_exponents_descending"])
                 for item in primary), default=0)
    invariant_factors = [[1] for _ in range(count)]
    for item in primary:
        factor_low = list(reversed(item["factor_coefficients_descending"]))
        exponents = list(reversed(
            item["elementary_divisor_exponents_descending"]
        ))
        offset = count - len(exponents)
        for index, exponent in enumerate(exponents):
            invariant_factors[offset + index] = _poly_mul(
                invariant_factors[offset + index],
                _poly_power(factor_low, exponent, p), p
            )

    invariant_desc = [list(reversed(_poly_trim(poly, p)))
                      for poly in invariant_factors]
    return {
        "schema": "the-fold-rational-canonical-profile-v1",
        "field": f"F_{p}",
        "dimension": n,
        "characteristic_polynomial_coefficients_descending": char_desc,
        "irreducible_primary_components": primary,
        "invariant_factors_coefficients_descending": invariant_desc,
        "invariant_factor_count": count,
        "similarity_class_complete_over_base_field": True,
        "interpretation": (
            "For matrices over F_p, the invariant factors determine the "
            "rational canonical form and the similarity class."
        ),
    }
