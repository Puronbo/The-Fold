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
    is_prime = bytearray(b"\\x01") * (limit + 1)
    is_prime[0:2] = b"\\x00\\x00"
    for candidate in range(2, int(limit ** 0.5) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            count = ((limit - start) // candidate) + 1
            is_prime[start:limit + 1:candidate] = b"\\x00" * count
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
