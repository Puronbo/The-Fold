#!/usr/bin/env python3
"""Exact small-matrix spectral fingerprints over prime fields.

The standard-library implementation computes characteristic polynomials
without division, scans for all base-field eigenvalues, and recovers Jordan
profiles. It does not factor higher-degree irreducibles or build extensions.
"""
from __future__ import annotations

import argparse
import json
from typing import Iterable, Mapping, Sequence


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
    parser.add_argument("--auto-full", action="store_true",
                        help="also compute Jordan profiles for higher-degree factors")
    args = parser.parse_args()
    modes = int(args.auto) + int(args.auto_full) + int(args.eigenvalues is not None)
    if modes != 1:
        parser.error("choose exactly one of --auto, --auto-full, or --eigenvalues")
    matrix = json.loads(args.matrix_json)
    if args.auto_full:
        result = automatic_full_spectral_fingerprint(matrix, args.prime)
    elif args.auto:
        result = automatic_spectral_fingerprint(matrix, args.prime)
    else:
        eigenvalues = [int(x.strip()) for x in args.eigenvalues.split(",") if x.strip()]
        result = spectral_fingerprint(matrix, args.prime, eigenvalues)
    print(json.dumps(result, indent=2, sort_keys=True))



def _characteristic_polynomial_subset_oracle(
        matrix: Sequence[Sequence[int]], p: int) -> list[int]:
    """Exponential subset-DP determinant retained as a small-input oracle."""
    n = _validate_matrix(matrix, p)
    a = _mod_matrix(matrix, p)
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
                inversions = bin(mask >> (col + 1)).count("1")
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
    low = dp[(1 << n) - 1]
    while len(low) > 1 and low[-1] % p == 0:
        low.pop()
    return [x % p for x in reversed(low)]


def _upper_hessenberg_similarity(matrix: Matrix, p: int) -> Matrix:
    """Reduce a matrix to upper Hessenberg form by exact similarities."""
    h = [row[:] for row in matrix]
    n = len(h)
    for col in range(n - 2):
        pivot_row = next((r for r in range(col + 1, n)
                          if h[r][col] % p), None)
        if pivot_row is None:
            continue
        pivot = col + 1
        if pivot_row != pivot:
            h[pivot], h[pivot_row] = h[pivot_row], h[pivot]
            for row in h:
                row[pivot], row[pivot_row] = row[pivot_row], row[pivot]
        inverse = pow(h[pivot][col], -1, p)
        for row in range(pivot + 1, n):
            entry = h[row][col] % p
            if not entry:
                continue
            factor = entry * inverse % p
            # Left multiplication by an elementary row operation.
            h[row] = [(h[row][j] - factor * h[pivot][j]) % p
                      for j in range(n)]
            # Right multiplication by its inverse preserves similarity.
            for i in range(n):
                h[i][pivot] = (h[i][pivot] + factor * h[i][row]) % p
    return h


def characteristic_polynomial(matrix: Sequence[Sequence[int]], p: int) -> list[int]:
    """Return det(xI-A) over F_p in O(n^3) field operations.

    First apply exact similarity transformations to upper Hessenberg form.
    The leading-principal characteristic polynomials then obey the
    Hessenberg continuant recurrence. No division by the dimension or by
    polynomial coefficients is used; only nonzero field pivots are inverted.
    """
    n = _validate_matrix(matrix, p)
    h = _upper_hessenberg_similarity(_mod_matrix(matrix, p), p)

    # Low-degree-first polynomials. P[k] is det(xI-H[0:k,0:k]).
    polys: list[list[int]] = [[1]]

    def multiply_x_minus_diagonal(poly: list[int], diagonal: int) -> list[int]:
        out = [0] * (len(poly) + 1)
        for degree, coefficient in enumerate(poly):
            out[degree] = (out[degree] - diagonal * coefficient) % p
            out[degree + 1] = (out[degree + 1] + coefficient) % p
        return out

    for size in range(1, n + 1):
        current = multiply_x_minus_diagonal(polys[size - 1],
                                             h[size - 1][size - 1])
        subdiagonal_product = 1
        for k in range(size - 2, -1, -1):
            subdiagonal_product = (
                subdiagonal_product * h[k + 1][k]) % p
            coefficient = subdiagonal_product * h[k][size - 1] % p
            if coefficient:
                previous = polys[k]
                if len(current) < len(previous):
                    current.extend([0] * (len(previous) - len(current)))
                for degree, value in enumerate(previous):
                    current[degree] = (
                        current[degree] - coefficient * value) % p
        while len(current) > 1 and current[-1] == 0:
            current.pop()
        polys.append(current)

    return [value % p for value in reversed(polys[n])]

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
        "irreducible_factorization_complete": True,
        "factorization": factor_polynomial(coefficients, p),
        "profiles": profiles,
    }


# Polynomial helpers use low-degree-first coefficient lists over F_p.
def _poly_trim(a: Sequence[int], p: int) -> list[int]:
    out = [int(x) % p for x in a]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def _poly_add(a: Sequence[int], b: Sequence[int], p: int) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
    return _poly_trim(out, p)


def _poly_sub(a: Sequence[int], b: Sequence[int], p: int) -> list[int]:
    return _poly_add(a, [-(x) for x in b], p)


def _poly_mul(a: Sequence[int], b: Sequence[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return _poly_trim(out, p)


def _poly_divmod(a: Sequence[int], b: Sequence[int], p: int):
    numerator, denominator = _poly_trim(a, p), _poly_trim(b, p)
    if denominator == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    remainder = numerator[:]
    inv = pow(denominator[-1], -1, p)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] * inv % p
        quotient[shift] = factor
        for i, value in enumerate(denominator):
            remainder[shift + i] = (remainder[shift + i] - factor * value) % p
        remainder = _poly_trim(remainder, p)
    return _poly_trim(quotient, p), remainder


def _poly_monic(a: Sequence[int], p: int) -> list[int]:
    out = _poly_trim(a, p)
    if out == [0]:
        return out
    inv = pow(out[-1], -1, p)
    return [(x * inv) % p for x in out]


def _poly_gcd(a: Sequence[int], b: Sequence[int], p: int) -> list[int]:
    x, y = _poly_trim(a, p), _poly_trim(b, p)
    while y != [0]:
        _, r = _poly_divmod(x, y, p)
        x, y = y, r
    return _poly_monic(x, p)


def _poly_derivative(a: Sequence[int], p: int) -> list[int]:
    if len(a) <= 1:
        return [0]
    return _poly_trim([(i * a[i]) % p for i in range(1, len(a))], p)


def _poly_powmod(a: Sequence[int], exponent: int,
                 modulus: Sequence[int], p: int) -> list[int]:
    result = [1]
    base = _poly_divmod(a, modulus, p)[1]
    power = exponent
    while power:
        if power & 1:
            result = _poly_divmod(_poly_mul(result, base, p), modulus, p)[1]
        base = _poly_divmod(_poly_mul(base, base, p), modulus, p)[1]
        power >>= 1
    return result


def _nullspace_mod(matrix: Sequence[Sequence[int]], p: int) -> list[list[int]]:
    """Return a basis of the right nullspace, with vectors as lists."""
    if not matrix:
        return []
    a = [[int(x) % p for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivots = []
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(x * inv) % p for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [(a[r][j] - factor * a[pivot_row][j]) % p
                        for j in range(cols)]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    free = [j for j in range(cols) if j not in pivots]
    basis = []
    for col in free:
        vector = [0] * cols
        vector[col] = 1
        for r, pivot_col in enumerate(pivots):
            vector[pivot_col] = (-a[r][col]) % p
        basis.append(vector)
    return basis


def _berlekamp_split_squarefree(f: Sequence[int], p: int) -> list[list[int]]:
    """Factor a monic squarefree polynomial using Berlekamp's algorithm."""
    f = _poly_monic(f, p)
    degree = len(f) - 1
    if degree <= 1:
        return [f]
    columns = []
    for j in range(degree):
        power = _poly_powmod([0, 1], p * j, f, p)
        columns.append(power + [0] * (degree - len(power)))
    # Q-I, represented by rows.
    matrix = [[(columns[col][row] - (1 if row == col else 0)) % p
               for col in range(degree)] for row in range(degree)]
    basis = _nullspace_mod(matrix, p)
    factors = [f]
    for vector in basis:
        splitter = _poly_trim(vector, p)
        for scalar in range(p):
            refined = []
            for factor in factors:
                if len(factor) <= 2:
                    refined.append(factor)
                    continue
                divisor = _poly_gcd(factor,
                                    _poly_sub(splitter, [scalar], p), p)
                if divisor != [1] and divisor != factor:
                    quotient, remainder = _poly_divmod(factor, divisor, p)
                    if remainder != [0]:
                        raise ArithmeticError("Berlekamp split had nonzero remainder")
                    refined.extend([_poly_monic(divisor, p),
                                    _poly_monic(quotient, p)])
                else:
                    refined.append(factor)
            factors = refined
        if len(factors) == len(basis):
            break
    if len(factors) != len(basis):
        raise ArithmeticError("Berlekamp basis did not produce the expected number of factors")
    return sorted((_poly_monic(x, p) for x in factors),
                  key=lambda x: (len(x), x))


def _squarefree_factorization(f: Sequence[int], p: int,
                              multiplier: int = 1):
    """Yield (squarefree factor, multiplicity), including inseparable powers."""
    f = _poly_monic(f, p)
    if len(f) <= 1:
        return []
    derivative = _poly_derivative(f, p)
    if derivative == [0]:
        # In characteristic p, a zero derivative means every exponent is
        # divisible by p; extract the p-th root and multiply multiplicities.
        root = [f[i] for i in range(0, len(f), p)]
        return _squarefree_factorization(root, p, multiplier * p)
    common = _poly_gcd(f, derivative, p)
    w, rem = _poly_divmod(f, common, p)
    if rem != [0]:
        raise ArithmeticError("squarefree decomposition division failed")
    multiplicity = 1
    output = []
    while w != [1]:
        y = _poly_gcd(w, common, p)
        z, rem = _poly_divmod(w, y, p)
        if rem != [0]:
            raise ArithmeticError("squarefree layer division failed")
        if z != [1]:
            output.append((z, multiplicity * multiplier))
        w = y
        common, rem = _poly_divmod(common, y, p)
        if rem != [0]:
            raise ArithmeticError("squarefree gcd quotient failed")
        multiplicity += 1
    if common != [1]:
        root = [common[i] for i in range(0, len(common), p)]
        for factor, power in _squarefree_factorization(
                root, p, multiplier * p):
            output.append((factor, power))
    return output


def factor_polynomial(coefficients_descending: Sequence[int], p: int) -> list[dict]:
    """Factor a nonzero polynomial over F_p into monic irreducibles.

    Returns factors in ascending degree order, each with descending
    coefficients and its positive multiplicity.
    """
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    descending = [int(x) % p for x in coefficients_descending]
    if not descending or all(x == 0 for x in descending):
        raise ValueError("zero polynomial cannot be factored")
    low = _poly_trim(list(reversed(descending)), p)
    if len(low) == 1:
        return []
    leading = low[-1]
    monic = _poly_monic(low, p)
    result = []
    for squarefree, multiplicity in _squarefree_factorization(monic, p):
        for factor in _berlekamp_split_squarefree(squarefree, p):
            result.append({
                "coefficients_descending": list(reversed(factor)),
                "multiplicity": multiplicity,
                "degree": len(factor) - 1,
            })
    result.sort(key=lambda item: (item["degree"],
                                 item["coefficients_descending"]))
    # The characteristic polynomials produced by this module are monic.
    # Keep the scalar separately for callers of the general factor API.
    if leading != 1:
        result.insert(0, {"constant_unit": leading})
    return result



def _prime_divisors(n: int) -> list[int]:
    result = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            result.append(d)
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        result.append(value)
    return result


def is_irreducible_polynomial(coefficients_descending: Sequence[int],
                              p: int) -> bool:
    """Rabin irreducibility test for a nonconstant polynomial over F_p."""
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    f = _poly_monic(list(reversed([int(x) % p
                                   for x in coefficients_descending])), p)
    degree = len(f) - 1
    if degree < 1:
        raise ValueError("polynomial must be nonconstant")
    if degree == 1:
        return True
    x = [0, 1]
    for prime_divisor in _prime_divisors(degree):
        exponent = p ** (degree // prime_divisor)
        test = _poly_sub(_poly_powmod(x, exponent, f, p), x, p)
        if _poly_gcd(f, test, p) != [1]:
            return False
    return _poly_powmod(x, p ** degree, f, p) == _poly_divmod(x, f, p)[1]


def _ext_zero(d: int) -> tuple[int, ...]:
    return (0,) * d


def _ext_one(d: int) -> tuple[int, ...]:
    return (1,) + (0,) * (d - 1)


def _ext_normalize(value: Sequence[int], d: int, p: int) -> tuple[int, ...]:
    if len(value) > d:
        raise ValueError("extension element degree must be below modulus degree")
    return tuple((int(value[i]) if i < len(value) else 0) % p
                 for i in range(d))


def _ext_add(a, b, p: int):
    return tuple((x + y) % p for x, y in zip(a, b))


def _ext_sub(a, b, p: int):
    return tuple((x - y) % p for x, y in zip(a, b))


def _ext_mul(a, b, modulus: Sequence[int], p: int):
    d = len(modulus) - 1
    product = _poly_mul(a, b, p)
    _, remainder = _poly_divmod(product, modulus, p)
    return _ext_normalize(remainder, d, p)


def _ext_pow(a, exponent: int, modulus: Sequence[int], p: int):
    result = _ext_one(len(modulus) - 1)
    base = tuple(a)
    power = exponent
    while power:
        if power & 1:
            result = _ext_mul(result, base, modulus, p)
        base = _ext_mul(base, base, modulus, p)
        power >>= 1
    return result


def _ext_inv(a, modulus: Sequence[int], p: int):
    if not any(a):
        raise ZeroDivisionError("zero has no multiplicative inverse")
    return _ext_pow(a, p ** (len(modulus) - 1) - 2, modulus, p)


def _ext_matmul(a, b, modulus: Sequence[int], p: int):
    n, inner, m = len(a), len(b), len(b[0])
    d = len(modulus) - 1
    out = [[_ext_zero(d) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(inner):
            if any(a[i][k]):
                for j in range(m):
                    out[i][j] = _ext_add(
                        out[i][j],
                        _ext_mul(a[i][k], b[k][j], modulus, p), p)
    return out


def _ext_rank(matrix, modulus: Sequence[int], p: int) -> int:
    if not matrix:
        return 0
    a = [[tuple(value) for value in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows)
                      if any(a[r][col])), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = _ext_inv(a[pivot_row][col], modulus, p)
        a[pivot_row] = [_ext_mul(x, inverse, modulus, p)
                        for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and any(a[r][col]):
                factor = a[r][col]
                a[r] = [
                    _ext_sub(a[r][j],
                             _ext_mul(factor, a[pivot_row][j], modulus, p), p)
                    for j in range(cols)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def extension_jordan_profile(matrix: Sequence[Sequence[int]], p: int,
                              modulus_descending: Sequence[int],
                              eigenvalue: Sequence[int]) -> dict:
    """Jordan profile over F_p[x]/(f), where f is irreducible.

    Extension elements are low-degree-first coefficient arrays in the
    polynomial basis 1, alpha, ..., alpha^(d-1). Matrix entries are embedded
    from F_p. The supplied eigenvalue must be a root of the characteristic
    polynomial for a nonempty profile.
    """
    n = _validate_matrix(matrix, p)
    modulus = _poly_monic(list(reversed(
        [int(x) % p for x in modulus_descending])), p)
    if len(modulus) < 2 or not is_irreducible_polynomial(
            list(reversed(modulus)), p):
        raise ValueError("extension modulus must be irreducible")
    d = len(modulus) - 1
    lam = _ext_normalize(eigenvalue, d, p)
    zero, one = _ext_zero(d), _ext_one(d)
    a = []
    for i, row in enumerate(matrix):
        converted = []
        for j, value in enumerate(row):
            embedded = _ext_normalize([int(value)], d, p)
            if i == j:
                embedded = _ext_sub(embedded, lam, p)
            converted.append(embedded)
        a.append(converted)

    power = [[one if i == j else zero for j in range(n)]
             for i in range(n)]
    nullities = [0]
    for _ in range(1, n + 1):
        power = _ext_matmul(power, a, modulus, p)
        nullities.append(n - _ext_rank(power, modulus, p))
        if nullities[-1] == nullities[-2]:
            break
    increments = [nullities[r] - nullities[r - 1]
                  for r in range(1, len(nullities))]
    exact = {}
    for r, current in enumerate(increments, start=1):
        following = increments[r] if r < len(increments) else 0
        if current - following:
            exact[r] = current - following
    blocks = []
    for size, count in sorted(exact.items(), reverse=True):
        blocks.extend([size] * count)
    return {
        "field": f"F_{p ** d}",
        "base_field": f"F_{p}",
        "extension_degree": d,
        "modulus_coefficients_descending": list(reversed(modulus)),
        "eigenvalue_coefficients_low_degree_first": list(lam),
        "nullities": nullities,
        "blocks_at_least": increments,
        "blocks_exactly": {str(k): v for k, v in sorted(exact.items())},
        "block_sizes_descending": blocks,
        "geometric_multiplicity": nullities[1] if len(nullities) > 1 else 0,
        "algebraic_multiplicity": nullities[-1],
    }


def automatic_full_spectral_fingerprint(matrix: Sequence[Sequence[int]],
                                        p: int) -> dict:
    """Compute one Jordan profile for every irreducible eigenvalue class.

    Degree-one factors are profiled over F_p. For a higher-degree irreducible
    factor q, the residue class alpha of x in F_p[x]/(q) is a root of q, so
    the extension profile is computed automatically. Frobenius conjugates
    have identical Jordan partitions because the matrix entries lie in F_p.
    """
    base = automatic_spectral_fingerprint(matrix, p)
    extension_classes = []
    for factor in base["factorization"]:
        if "degree" not in factor or factor["degree"] <= 1:
            continue
        modulus = factor["coefficients_descending"]
        profile = extension_jordan_profile(
            matrix, p, modulus, [0, 1]
        )
        extension_classes.append({
            "minimal_polynomial_coefficients_descending": modulus,
            "extension_degree": factor["degree"],
            "frobenius_conjugate_count": factor["degree"],
            "algebraic_multiplicity_per_root": factor["multiplicity"],
            "representative_root_coefficients_low_degree_first": [0, 1],
            "profile": profile,
        })
    return {
        **base,
        "scope": "all eigenvalues grouped by irreducible polynomial over F_p",
        "extension_eigenvalue_classes": extension_classes,
        "extension_classes_complete": True,
    }



SparseMatrix = Mapping[int, Mapping[int, int]]


def _validate_sparse_matrix(matrix: SparseMatrix, n: int, p: int) -> None:
    """Validate a square n-by-n sparse matrix in row -> column -> value form."""
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    for row, entries in matrix.items():
        if not isinstance(row, int) or not 0 <= row < n:
            raise ValueError("sparse row index is outside matrix dimensions")
        for col, value in entries.items():
            if not isinstance(col, int) or not 0 <= col < n:
                raise ValueError("sparse column index is outside matrix dimensions")
            if not isinstance(value, int):
                raise ValueError("sparse matrix entries must be integers")


def _sparse_clean(row: Mapping[int, int], p: int) -> dict[int, int]:
    return {col: value % p for col, value in row.items() if value % p}


def sparse_rank_mod(matrix: SparseMatrix, n: int, p: int) -> int:
    """Exact rank of an n-by-n sparse matrix using sparse row elimination.

    Rows are dictionaries of nonzero column coefficients. The algorithm
    stores only nonzero entries until fill-in occurs during elimination.
    """
    _validate_sparse_matrix(matrix, n, p)
    rows = {i: _sparse_clean(matrix.get(i, {}), p)
            for i in range(n)}
    pivot_row = 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, n)
                      if rows[r].get(col, 0)), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_values = rows[pivot_row]
        inverse = pow(pivot_values[col], -1, p)
        rows[pivot_row] = {
            j: value * inverse % p for j, value in pivot_values.items()
            if value * inverse % p
        }
        pivot_values = rows[pivot_row]
        for r in range(n):
            if r == pivot_row:
                continue
            factor = rows[r].get(col, 0)
            if not factor:
                continue
            target = rows[r]
            for j, value in pivot_values.items():
                updated = (target.get(j, 0) - factor * value) % p
                if updated:
                    target[j] = updated
                else:
                    target.pop(j, None)
        pivot_row += 1
        if pivot_row == n:
            break
    return pivot_row


def _sparse_matmul(a: SparseMatrix, b: SparseMatrix,
                   n: int, p: int) -> dict[int, dict[int, int]]:
    """Multiply square sparse matrices, removing modular zeros."""
    out: dict[int, dict[int, int]] = {}
    for i, row in a.items():
        accum: dict[int, int] = {}
        for k, left in row.items():
            if not left:
                continue
            for j, right in b.get(k, {}).items():
                accum[j] = (accum.get(j, 0) + left * right) % p
        cleaned = {j: value for j, value in accum.items() if value}
        if cleaned:
            out[i] = cleaned
    return out


def sparse_jordan_profile(matrix: SparseMatrix, n: int, p: int,
                          eigenvalue: int) -> dict:
    """Recover a Jordan profile without first materializing a dense matrix.

    Input format is {row_index: {column_index: integer_value}}. Missing
    entries are zero. Powers may become dense; the implementation remains
    sparse in storage where the operator and its powers permit it.
    """
    _validate_sparse_matrix(matrix, n, p)
    lam = int(eigenvalue) % p
    nil: dict[int, dict[int, int]] = {}
    for i in range(n):
        row = _sparse_clean(matrix.get(i, {}), p)
        diagonal = (row.get(i, 0) - lam) % p
        if diagonal:
            row[i] = diagonal
        else:
            row.pop(i, None)
        if row:
            nil[i] = row

    power: dict[int, dict[int, int]] = {
        i: {i: 1} for i in range(n)
    }
    nullities = [0]
    for _ in range(1, n + 1):
        power = _sparse_matmul(power, nil, n, p)
        nullities.append(n - sparse_rank_mod(power, n, p))
        if nullities[-1] == nullities[-2]:
            break

    increments = [nullities[r] - nullities[r - 1]
                  for r in range(1, len(nullities))]
    exact = {}
    for r, current in enumerate(increments, start=1):
        following = increments[r] if r < len(increments) else 0
        if current - following:
            exact[r] = current - following
    blocks = []
    for size, count in sorted(exact.items(), reverse=True):
        blocks.extend([size] * count)
    return {
        "eigenvalue": lam,
        "nullities": nullities,
        "blocks_at_least": increments,
        "blocks_exactly": {str(k): v for k, v in sorted(exact.items())},
        "block_sizes_descending": blocks,
        "geometric_multiplicity": nullities[1] if len(nullities) > 1 else 0,
        "algebraic_multiplicity": nullities[-1],
        "matrix_representation": "sparse-row-dictionaries",
    }


if __name__ == "__main__":
    main()
