"""Finite modular spectral tools for the Fold quarter-turn.

The quarter-turn J(x, y) = (-y, x) satisfies J^2 = -I.  Over Z/pZ,
an eigenvalue therefore must satisfy lambda^2 = -1.  This module computes
and verifies such eigenpairs directly; it does not assume p is prime.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModularEigenpair:
    eigenvalue: int
    eigenvector: tuple[int, int]


def quarter_turn(vector: tuple[int, int], modulus: int) -> tuple[int, int]:
    """Apply J(x, y) = (-y, x) in Z/modulus Z."""
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    x, y = vector
    return (-y % modulus, x % modulus)


def quarter_turn_eigenpairs(modulus: int) -> tuple[ModularEigenpair, ...]:
    """Return all eigenpairs witnessed by v=(lambda, 1), for lambda²=-1."""
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    pairs = []
    for eigenvalue in range(modulus):
        if (eigenvalue * eigenvalue + 1) % modulus == 0:
            vector = (eigenvalue, 1)
            pairs.append(ModularEigenpair(eigenvalue, vector))
    return tuple(pairs)


def verify_quarter_turn_eigenpair(
    pair: ModularEigenpair, modulus: int
) -> bool:
    """Check J(v)=lambda*v and v is nonzero modulo the given modulus."""
    if modulus < 2:
        return False
    eigenvalue = pair.eigenvalue % modulus
    x, y = (coordinate % modulus for coordinate in pair.eigenvector)
    if x == 0 and y == 0:
        return False
    turned = quarter_turn((x, y), modulus)
    scaled = (eigenvalue * x % modulus, eigenvalue * y % modulus)
    return turned == scaled


def quarter_turn_root_primes(limit: int) -> tuple[int, ...]:
    """Return primes p <= limit for which x² + 1 has a root modulo p.

    By the finite-field criterion, these are exactly p=2 and primes
    p congruent to 1 modulo 4.  A sieve keeps the implementation simple
    and makes the primality condition explicit.
    """
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    if limit < 2:
        return ()
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0:2] = bytearray([0, 0])
    for candidate in range(2, int(limit ** 0.5) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            count = ((limit - start) // candidate) + 1
            is_prime[start:limit + 1:candidate] = bytearray([0]) * count
    return tuple(
        p for p in range(2, limit + 1)
        if is_prime[p] and (p == 2 or p % 4 == 1)
    )


def _poly_div_exact(
    dividend: tuple[int, ...], divisor: tuple[int, ...]
) -> tuple[int, ...]:
    """Divide integer polynomials in ascending coefficient order exactly."""
    remainder = list(dividend)
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    while len(remainder) >= len(divisor):
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
        if len(remainder) < len(divisor):
            break
        degree = len(remainder) - len(divisor)
        lead = remainder[-1]
        divisor_lead = divisor[-1]
        if lead % divisor_lead:
            raise ArithmeticError("non-integral polynomial quotient")
        coefficient = lead // divisor_lead
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[degree + index] -= coefficient * value
    if any(remainder):
        raise ArithmeticError("polynomial division was not exact")
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return tuple(quotient)


def cyclotomic_polynomial(order: int) -> tuple[int, ...]:
    """Return Phi_order coefficients, low degree first."""
    if order < 1:
        raise ValueError("order must be positive")
    polynomial = tuple([-1] + [0] * (order - 1) + [1])
    for divisor in range(1, order):
        if order % divisor == 0:
            polynomial = _poly_div_exact(
                polynomial, cyclotomic_polynomial(divisor)
            )
    return polynomial


def _evaluate_mod(coefficients: tuple[int, ...], value: int, modulus: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % modulus
    return result


def cyclotomic_root_residues(order: int, prime: int) -> tuple[int, ...]:
    """Return roots of Phi_order in F_prime; prime must be prime."""
    if order < 1:
        raise ValueError("order must be positive")
    if prime < 2:
        raise ValueError("prime must be at least 2")
    if any(prime % divisor == 0 for divisor in range(2, int(prime ** 0.5) + 1)):
        raise ValueError("modulus must be prime")
    coefficients = cyclotomic_polynomial(order)
    return tuple(
        value for value in range(prime)
        if _evaluate_mod(coefficients, value, prime) == 0
    )


def cyclotomic_root_primes(order: int, limit: int) -> tuple[int, ...]:
    """Primes p <= limit where Phi_order has a root in F_p.

    This literal polynomial-root definition also reports any roots at
    primes dividing order. For p not dividing order, such a root is a
    primitive order-th root of unity in F_p, so necessarily order | p-1.
    """
    if order < 1:
        raise ValueError("order must be positive")
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    if limit < 2:
        return ()
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0:2] = [0, 0]
    for candidate in range(2, int(limit ** 0.5) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            count = ((limit - start) // candidate) + 1
            is_prime[start:limit + 1:candidate] = [0] * count
    coefficients = cyclotomic_polynomial(order)
    return tuple(
        prime for prime in range(2, limit + 1)
        if is_prime[prime]
        and any(_evaluate_mod(coefficients, value, prime) == 0
                for value in range(prime))
    )


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, int(value ** 0.5) + 1))


def _euler_totient(value: int) -> int:
    result = value
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            while remaining % divisor == 0:
                remaining //= divisor
            result -= result // divisor
        divisor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def multiplicative_order(base: int, modulus: int) -> int:
    """Least positive k with base**k == 1 (mod modulus)."""
    if modulus < 1:
        raise ValueError("modulus must be positive")
    if modulus == 1:
        return 1
    base %= modulus
    if _gcd(base, modulus) != 1:
        raise ValueError("base and modulus must be coprime")
    value = 1
    for exponent in range(1, modulus + 1):
        value = value * base % modulus
        if value == 1:
            return exponent
    raise ArithmeticError("multiplicative order was not found")


def _gcd(left: int, right: int) -> int:
    while right:
        left, right = right, left % right
    return abs(left)


def cyclotomic_spectral_degree(order: int, prime: int) -> int:
    """Degree over F_p of a primitive order-th root, when p does not divide order.

    This equals ord_order(p), the Frobenius orbit length. The prime must
    be prime and coprime to order; the ramified case p | order is excluded.
    """
    if order < 1:
        raise ValueError("order must be positive")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if _gcd(order, prime) != 1:
        raise ValueError("prime must not divide the cyclotomic order")
    return multiplicative_order(prime, order)


def cyclotomic_factor_count(order: int, prime: int) -> int:
    """Number of irreducible factors of Phi_order over F_p for p not dividing order."""
    degree = cyclotomic_spectral_degree(order, prime)
    return _euler_totient(order) // degree


def cyclotomic_rotation_matrix(order: int) -> tuple[tuple[int, ...], ...]:
    """Return the integer companion matrix for multiplication by x mod Phi_order.

    In the power basis (1, x, ..., x^(phi(order)-1)), this matrix has
    characteristic and minimal polynomial Phi_order over Q. It satisfies
    A^order = I, so it is an exact finite-order Fold rotation representation.
    """
    coefficients = cyclotomic_polynomial(order)
    degree = len(coefficients) - 1
    if degree < 1:
        raise ArithmeticError("cyclotomic polynomial must have positive degree")
    matrix = [[0] * degree for _ in range(degree)]
    for column in range(degree - 1):
        matrix[column + 1][column] = 1
    for row in range(degree):
        matrix[row][degree - 1] = -coefficients[row]
    return tuple(tuple(row) for row in matrix)


def _matrix_multiply(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    if size == 0 or len(right) != size:
        raise ValueError("matrices must be nonempty and square")
    if any(len(row) != size for row in left + right):
        raise ValueError("matrices must be square and have equal dimensions")
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(size))
              for j in range(size))
        for i in range(size)
    )


def _matrix_identity(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(1 if row == column else 0 for column in range(size))
        for row in range(size)
    )


def _matrix_power(
    matrix: tuple[tuple[int, ...], ...], exponent: int
) -> tuple[tuple[int, ...], ...]:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    result = _matrix_identity(len(matrix))
    factor = matrix
    while exponent:
        if exponent & 1:
            result = _matrix_multiply(result, factor)
        factor = _matrix_multiply(factor, factor)
        exponent >>= 1
    return result


def _evaluate_polynomial_at_matrix(
    coefficients: tuple[int, ...],
    matrix: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    """Evaluate an integer polynomial at a square matrix by Horner's rule."""
    size = len(matrix)
    result = tuple(tuple(0 for _ in range(size)) for _ in range(size))
    identity = _matrix_identity(size)
    for coefficient in reversed(coefficients):
        result = _matrix_multiply(result, matrix)
        result = tuple(
            tuple(result[i][j] + coefficient * identity[i][j]
                  for j in range(size))
            for i in range(size)
        )
    return result


def verify_cyclotomic_rotation_matrix(order: int) -> bool:
    """Check A^order=I and Phi_order(A)=0 for the canonical companion matrix."""
    if order < 1:
        return False
    matrix = cyclotomic_rotation_matrix(order)
    identity = _matrix_identity(len(matrix))
    return (
        _matrix_power(matrix, order) == identity
        and _evaluate_polynomial_at_matrix(
            cyclotomic_polynomial(order), matrix
        ) == tuple(tuple(0 for _ in row) for row in matrix)
    )


def cyclotomic_rotation_matrix_mod(
    order: int, prime: int
) -> tuple[tuple[int, ...], ...]:
    """Reduce the exact cyclotomic companion matrix modulo a prime."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    matrix = cyclotomic_rotation_matrix(order)
    return tuple(tuple(value % prime for value in row) for row in matrix)


def _matrix_rank_mod(
    matrix: tuple[tuple[int, ...], ...], prime: int
) -> int:
    """Compute row rank by Gaussian elimination over F_prime."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have equal length")
    work = [[value % prime for value in row] for row in matrix]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(work))
             if work[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [
            value * inverse % prime for value in work[pivot_row]
        ]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    (work[row][index] - factor * work[pivot_row][index]) % prime
                    for index in range(width)
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def cyclotomic_eigenvalue_multiplicities(
    order: int, prime: int
) -> tuple[tuple[int, int], ...]:
    """Return (eigenvalue, geometric multiplicity) pairs over F_p.

    For p not dividing order, Phi_order is separable, so every eigenvalue
    in F_p has algebraic multiplicity one. The nullity computation checks
    the eigenspace dimension directly from the reduced companion matrix.
    """
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if _gcd(order, prime) != 1:
        raise ValueError("prime must not divide the cyclotomic order")
    matrix = cyclotomic_rotation_matrix_mod(order, prime)
    size = len(matrix)
    result = []
    for eigenvalue in cyclotomic_root_residues(order, prime):
        shifted = tuple(
            tuple((matrix[row][column] -
                   (eigenvalue if row == column else 0)) % prime
                  for column in range(size))
            for row in range(size)
        )
        multiplicity = size - _matrix_rank_mod(shifted, prime)
        result.append((eigenvalue, multiplicity))
    return tuple(result)


def cyclotomic_spectral_profile(order: int, prime: int) -> dict[str, int]:
    """Return the predicted irreducible-factor profile over F_p.

    Valid for prime p not dividing order. Since the p-Frobenius acts on
    primitive order-th roots with orbit length ord_order(p), every
    irreducible factor has that degree and there are phi(order)/degree
    factors.
    """
    degree = cyclotomic_spectral_degree(order, prime)
    factor_count = _euler_totient(order) // degree
    roots = cyclotomic_eigenvalue_multiplicities(order, prime)
    return {
        "dimension": _euler_totient(order),
        "factor_degree": degree,
        "factor_count": factor_count,
        "base_field_eigenvalue_count": len(roots),
        "base_field_eigenspace_dimension_sum": sum(
            multiplicity for _, multiplicity in roots
        ),
    }


def verify_cyclotomic_spectral_profile(order: int, prime: int) -> bool:
    """Cross-check Frobenius prediction against exact matrix eigenspaces."""
    profile = cyclotomic_spectral_profile(order, prime)
    if profile["base_field_eigenvalue_count"] != (
        profile["factor_count"] if profile["factor_degree"] == 1 else 0
    ):
        return False
    return all(
        multiplicity == 1
        for _, multiplicity in cyclotomic_eigenvalue_multiplicities(order, prime)
    )
