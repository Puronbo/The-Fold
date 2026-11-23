#!/usr/bin/env python3
"""Exact small-matrix spectral fingerprints over prime fields.

The standard-library implementation computes characteristic polynomials
without division, scans for all base-field eigenvalues, and recovers Jordan
profiles. It does not factor higher-degree irreducibles or build extensions.
"""
from __future__ import annotations

import argparse
import json
from typing import Iterable, Sequence


Matrix = list[list[int]]


def _is_prime(p: int) -> bool:
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2
    return True


def _validate_matrix(matrix: Sequence[Sequence[int]], p: int) -> int:
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be non-empty and square")
    return n


def _mod_matrix(matrix: Sequence[Sequence[int]], p: int) -> Matrix:
    return [[int(x) % p for x in row] for row in matrix]


def _identity(n: int, p: int) -> Matrix:
    return [[1 % p if i == j else 0 for j in range(n)] for i in range(n)]


def _matmul(a: Matrix, b: Matrix, p: int) -> Matrix:
    n, inner, m = len(a), len(b), len(b[0])
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(inner):
            aik = a[i][k] % p
            if aik:
                for j in range(m):
                    out[i][j] = (out[i][j] + aik * b[k][j]) % p
    return out


def rank_mod(matrix: Sequence[Sequence[int]], p: int) -> int:
    """Return exact row rank over F_p using modular Gaussian elimination."""
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have equal length")
    a = [[int(x) % p for x in row] for row in matrix]
    rows = len(a)
    pivot_row = 0
    for col in range(width):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(x * inv) % p for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row:
                factor = a[r][col] % p
                if factor:
                    a[r] = [(a[r][j] - factor * a[pivot_row][j]) % p
                            for j in range(width)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def _subtract_scalar_identity(a: Matrix, lam: int, p: int) -> Matrix:
    n = len(a)
    return [[(a[i][j] - (lam if i == j else 0)) % p
             for j in range(n)] for i in range(n)]


def jordan_profile(matrix: Sequence[Sequence[int]], p: int,
                   eigenvalue: int) -> dict:
    """Recover Jordan block sizes for eigenvalue in F_p.

    K_r = nullity((A-lambda I)^r). The output includes K_r, first
    differences (blocks of size >= r), and exact block-size multiplicities.
    """
    n = _validate_matrix(matrix, p)
    a = _mod_matrix(matrix, p)
    lam = int(eigenvalue) % p
    nil = _subtract_scalar_identity(a, lam, p)

    power = _identity(n, p)
    nullities = [0]
    for _r in range(1, n + 1):
        power = _matmul(power, nil, p)
        nullities.append(n - rank_mod(power, p))
        if nullities[-1] == nullities[-2]:
            break

    increments = [nullities[r] - nullities[r - 1]
                  for r in range(1, len(nullities))]
    # If stabilization happened early, all later increments are zero.
    exact = {}
    for r, current in enumerate(increments, start=1):
        following = increments[r] if r < len(increments) else 0
        count = current - following
        if count:
            exact[r] = count

    block_sizes = []
    for size, count in sorted(exact.items(), reverse=True):
        block_sizes.extend([size] * count)

    return {
        "eigenvalue": lam,
        "nullities": nullities,
        "blocks_at_least": increments,
        "blocks_exactly": {str(k): v for k, v in sorted(exact.items())},
        "block_sizes_descending": block_sizes,
        "geometric_multiplicity": nullities[1] if len(nullities) > 1 else 0,
        "algebraic_multiplicity": nullities[-1],
    }


def spectral_fingerprint(matrix: Sequence[Sequence[int]], p: int,
                         eigenvalues: Iterable[int]) -> dict:
    """Build profiles for a caller-supplied list of F_p eigenvalues."""
    n = _validate_matrix(matrix, p)
    vals = sorted({int(x) % p for x in eigenvalues})
    return {
        "field": f"F_{p}",
        "dimension": n,
        "scope": "Jordan profiles for supplied eigenvalues in the base field",
        "automatic_factorization": False,
        "profiles": [jordan_profile(matrix, p, lam) for lam in vals],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--matrix-json", required=True,
                        help="JSON array of equal-length matrix rows")
    parser.add_argument("--eigenvalues",
                        help="comma-separated eigenvalues in F_p (manual mode)")
    parser.add_argument("--auto", action="store_true",
                        help="compute the characteristic polynomial and scan F_p")
    args = parser.parse_args()
    if args.auto == (args.eigenvalues is not None):
        parser.error("choose exactly one of --auto or --eigenvalues")
    matrix = json.loads(args.matrix_json)
    if args.auto:
        result = automatic_spectral_fingerprint(matrix, args.prime)
    else:
        eigenvalues = [int(x.strip()) for x in args.eigenvalues.split(",") if x.strip()]
        result = spectral_fingerprint(matrix, args.prime, eigenvalues)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()


def characteristic_polynomial(matrix: Sequence[Sequence[int]], p: int) -> list[int]:
    """Return det(xI-A) coefficients, highest degree first, in F_p.

    A subset dynamic program evaluates the determinant in F_p[x] without
    division. It is exponential in matrix dimension, so it is intended as
    an exact small-matrix reference implementation.
    """
    n = _validate_matrix(matrix, p)
    a = _mod_matrix(matrix, p)

    # Polynomials are stored low-degree first. dp[S] is the signed sum
    # assigning the first |S| rows to the columns in S.
    dp: dict[int, list[int]] = {0: [1]}
    for row in range(n):
        nxt: dict[int, list[int]] = {}
        for mask, poly in dp.items():
            for col in range(n):
                bit = 1 << col
                if mask & bit:
                    continue
                entry = [-a[row][col]]
                if row == col:
                    entry.append(1)
                # Appending col creates one inversion for every previously
                # selected column larger than col.
                inversions = bin(mask >> (col + 1)).count('1')
                sign = -1 if inversions % 2 else 1
                term = [0] * (len(poly) + len(entry) - 1)
                for i, x in enumerate(poly):
                    for j, y in enumerate(entry):
                        term[i + j] = (term[i + j] + sign * x * y) % p
                target = mask | bit
                current = nxt.setdefault(target, [0] * len(term))
                if len(current) < len(term):
                    current.extend([0] * (len(term) - len(current)))
                for i, value in enumerate(term):
                    current[i] = (current[i] + value) % p
        dp = nxt

    low_first = dp[(1 << n) - 1]
    while len(low_first) > 1 and low_first[-1] % p == 0:
        low_first.pop()
    return [x % p for x in reversed(low_first)]


def _evaluate_polynomial(coefficients: Sequence[int], value: int, p: int) -> int:
    result = 0
    for coefficient in coefficients:
        result = (result * value + int(coefficient)) % p
    return result


def _linear_root_multiplicity(coefficients: Sequence[int], root: int,
                              p: int) -> int:
    """Multiplicity of x-root, using exact synthetic division."""
    current = [int(x) % p for x in coefficients]
    multiplicity = 0
    while len(current) > 1:
        quotient = [current[0]]
        for coefficient in current[1:-1]:
            quotient.append((coefficient + root * quotient[-1]) % p)
        remainder = (current[-1] + root * quotient[-1]) % p
        if remainder:
            break
        multiplicity += 1
        current = quotient
    return multiplicity


def automatic_spectral_fingerprint(matrix: Sequence[Sequence[int]],
                                    p: int) -> dict:
    """Compute charpoly and all base-field eigenvalue/Jordan profiles.

    This is complete only for eigenvalues in F_p. Irreducible factors of
    degree > 1 and their roots in extension fields are not computed here.
    """
    n = _validate_matrix(matrix, p)
    coefficients = characteristic_polynomial(matrix, p)
    roots = []
    profiles = []
    for value in range(p):
        multiplicity = _linear_root_multiplicity(coefficients, value, p)
        if multiplicity:
            profile = jordan_profile(matrix, p, value)
            roots.append({
                "value": value,
                "algebraic_multiplicity": multiplicity,
            })
            profiles.append(profile)
    return {
        "field": f"F_{p}",
        "dimension": n,
        "characteristic_polynomial_coefficients_descending": coefficients,
        "base_field_eigenvalues": roots,
        "scope": "all eigenvalues in the base prime field",
        "irreducible_factorization_complete": False,
        "profiles": profiles,
    }
