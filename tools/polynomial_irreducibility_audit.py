"""Bounded exhaustive and deterministic sampled irreducibility audits."""
from __future__ import annotations

import random
from fractions import Fraction
from typing import Iterator

from tools.spectral_fingerprint import (
    _is_prime,
    factor_polynomial,
    is_irreducible_polynomial,
)


def _digits_base_p(value: int, degree: int, p: int) -> tuple[int, ...]:
    """Decode one integer as exactly degree base-p coefficients."""
    digits = [0] * degree
    for index in range(degree - 1, -1, -1):
        value, digits[index] = divmod(value, p)
    return tuple(digits)


def _indices(total: int, exhaustive: bool, sample_count: int,
             seed: int) -> Iterator[int]:
    if exhaustive:
        yield from range(total)
    else:
        rng = random.Random(seed)
        yield from rng.sample(range(total), min(sample_count, total))


def _mobius(value: int) -> int:
    """Return the Möbius function for a positive integer."""
    remaining = value
    prime_factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            prime_factors += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def count_monic_irreducibles(p: int, degree: int) -> int:
    """Return the exact number of monic irreducibles of degree n over F_p.

    Uses I_p(n) = (1/n) * sum_{d|n} mu(d) * p**(n/d).
    """
    if isinstance(p, bool) or not isinstance(p, int) or not _is_prime(p):
        raise ValueError("p must be a prime integer")
    if (isinstance(degree, bool) or not isinstance(degree, int)
            or degree < 1):
        raise ValueError("degree must be a positive integer")
    numerator = sum(
        _mobius(divisor) * p ** (degree // divisor)
        for divisor in range(1, degree + 1)
        if degree % divisor == 0
    )
    quotient, remainder = divmod(numerator, degree)
    if remainder:
        raise ArithmeticError("irreducible-count formula was not integral")
    return quotient



def irreducible_density_convergence(p: int, degree: int) -> dict:
    """Return the exact normalized density error and a uniform analytic bound.

    R_p(n) = n I_p(n) / p**n and
    |R_p(n) - 1| <= (2**omega(n) - 1) p**(-n/2)
                  <= (n - 1) 2**(-n/2),
    where omega(n) counts distinct prime factors. The latter bound is
    uniform over every prime p.
    """
    if isinstance(p, bool) or not isinstance(p, int) or not _is_prime(p):
        raise ValueError("p must be a prime integer")
    if (isinstance(degree, bool) or not isinstance(degree, int)
            or degree < 1):
        raise ValueError("degree must be a positive integer")

    normalized_density = Fraction(
        degree * count_monic_irreducibles(p, degree), p ** degree
    )
    error = 1 - normalized_density
    distinct_prime_factors = sum(
        1 for divisor in range(2, degree + 1)
        if degree % divisor == 0 and _mobius(divisor) != 0
        and all(divisor % prime != 0
                for prime in range(2, divisor)
                if _mobius(prime) == -1)
    ) if degree > 1 else 0
    # Count omega(n) directly by trial division; unlike divisor counting,
    # this remains transparent for prime powers.
    remaining = degree
    omega = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            omega += 1
            while remaining % prime == 0:
                remaining //= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        omega += 1

    divisor_bound = Fraction((2 ** omega - 1), 1) * Fraction(1, p) ** (degree / 2)
    # Use an exact rational relaxation: p^(-n/2) is represented by
    # p^(-ceil(n/2)) for odd n only as a stronger-than-needed exponent is
    # invalid, so retain the square-root expression as a float for reporting.
    uniform_bound = (degree - 1) * (2 ** (-degree / 2))
    return {
        "schema": "the-fold-irreducible-density-convergence-v1",
        "field_prime": p,
        "degree": degree,
        "normalized_irreducible_density_numerator":
            normalized_density.numerator,
        "normalized_irreducible_density_denominator":
            normalized_density.denominator,
        "normalized_irreducible_density": float(normalized_density),
        "signed_error_numerator": error.numerator,
        "signed_error_denominator": error.denominator,
        "absolute_error": float(abs(error)),
        "distinct_prime_divisor_count": omega,
        "divisor_count_bound": float(divisor_bound),
        "uniform_prime_field_bound": uniform_bound,
        "uniform_bound_holds": abs(error) <= Fraction.from_float(
            uniform_bound
        ),
    }

def audit_irreducibility_agreement(
    p: int,
    degree: int,
    *,
    max_cases: int = 100_000,
    sample_count: int = 10_000,
    seed: int = 0,
) -> dict:
    """Compare predicate and factorizer, and benchmark counts against theory.

    Exhaust every monic degree-n polynomial when p**degree <= max_cases.
    Otherwise check sample_count distinct polynomials reproducibly. The
    theoretical irreducible count is exact in either mode; observed counts
    describe only the checked set unless the returned domain is complete.
    """
    for name, value in (("p", p), ("degree", degree),
                        ("max_cases", max_cases),
                        ("sample_count", sample_count), ("seed", seed)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    if degree < 1:
        raise ValueError("degree must be positive")
    if max_cases < 1:
        raise ValueError("max_cases must be positive")
    if sample_count < 1:
        raise ValueError("sample_count must be positive")

    total = p ** degree
    exhaustive = total <= max_cases
    mismatches = []
    mismatch_count = 0
    irreducible_count = 0
    checked = total if exhaustive else min(sample_count, total)
    theoretical_count = count_monic_irreducibles(p, degree)
    complete = checked == total

    for index in _indices(total, exhaustive, checked, seed):
        polynomial = (1,) + _digits_base_p(index, degree, p)
        factors = factor_polynomial(list(polynomial), p)
        factorizer_says_irreducible = (
            len(factors) == 1
            and factors[0].get("degree") == degree
            and factors[0].get("multiplicity") == 1
            and factors[0].get("coefficients_descending") == list(polynomial)
        )
        predicate_says_irreducible = is_irreducible_polynomial(
            list(polynomial), p
        )
        if predicate_says_irreducible:
            irreducible_count += 1
        if predicate_says_irreducible != factorizer_says_irreducible:
            mismatch_count += 1
            if len(mismatches) < 20:
                mismatches.append({
                    "polynomial_coefficients_descending": list(polynomial),
                    "predicate": predicate_says_irreducible,
                    "factorizer": factorizer_says_irreducible,
                })

    observed_density = irreducible_count / checked
    theoretical_density = theoretical_count / total
    return {
        "schema": "the-fold-irreducibility-audit-v2",
        "field_prime": p,
        "degree": degree,
        "domain_size": total,
        "checked_count": checked,
        "mode": "exhaustive" if exhaustive else "deterministic_sample",
        "seed": None if exhaustive else seed,
        "complete": complete,
        "agreement": mismatch_count == 0,
        "mismatch_count": mismatch_count,
        "mismatches_first_20": mismatches,
        "predicate_irreducible_count_in_checked_set": irreducible_count,
        "observed_irreducible_density_in_checked_set": observed_density,
        "observed_normalized_irreducible_density": degree * observed_density,
        "theoretical_irreducible_count": theoretical_count,
        "theoretical_irreducible_density": theoretical_density,
        "theoretical_normalized_irreducible_density":
            degree * theoretical_density,
        "expected_irreducibles_in_checked_set":
            checked * theoretical_density,
        "theoretical_count_match": (
            irreducible_count == theoretical_count if complete else None
        ),
        "sample_count_requested": None if exhaustive else sample_count,
    }
