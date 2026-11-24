"""Bounded exhaustive and deterministic sampled irreducibility audits."""
from __future__ import annotations

import math
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
    # Count omega(n) directly by trial division; this remains transparent
    # for prime powers and avoids counting squarefree divisors individually.
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

    divisor_bound = Fraction(2 ** omega - 1, 2 ** (degree // 2))
    uniform_bound = Fraction(degree - 1, 2 ** (degree // 2))
    return_float_bound = (degree - 1) * (2 ** (-degree / 2))
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
        "uniform_prime_field_bound": return_float_bound,
        "uniform_bound_rational_envelope": str(uniform_bound),
        "uniform_bound_holds": abs(error) <= uniform_bound,
    }


def irreducible_density_factorization(p: int, degree: int) -> dict:
    """Resolve the leading Möbius correction from the prime factors of n.

    If q1 < q2 are the two smallest distinct prime factors, then
    R_p(n)-1 = -p**(-n(1-1/q1)) + remainder, with
    |remainder| <= (2**omega(n)-2) p**(-n(1-1/q2)).
    For a prime-power degree, the leading term is the entire correction.
    """
    if isinstance(p, bool) or not isinstance(p, int) or not _is_prime(p):
        raise ValueError("p must be a prime integer")
    if (isinstance(degree, bool) or not isinstance(degree, int)
            or degree < 1):
        raise ValueError("degree must be a positive integer")

    remaining = degree
    prime_factors = []
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            prime_factors.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1 if candidate == 2 else 2
    if remaining > 1:
        prime_factors.append(remaining)

    omega = len(prime_factors)
    if not prime_factors:
        # n=1: R_p(1)=1 exactly.
        leading_exponent = None
        leading_term = Fraction(0, 1)
        remainder_bound = Fraction(0, 1)
        exact_leading = True
    else:
        q1 = prime_factors[0]
        leading_exponent = degree * (q1 - 1) // q1
        leading_term = -Fraction(1, p ** leading_exponent)
        exact_leading = omega == 1
        if exact_leading:
            remainder_bound = Fraction(0, 1)
        else:
            q2 = prime_factors[1]
            next_exponent = degree * (q2 - 1) // q2
            remainder_bound = Fraction(
                2 ** omega - 2, p ** next_exponent
            )

    normalized = Fraction(
        degree * count_monic_irreducibles(p, degree), p ** degree
    )
    actual_correction = normalized - 1
    remainder = actual_correction - leading_term
    return {
        "schema": "the-fold-irreducible-density-factorization-v1",
        "field_prime": p,
        "degree": degree,
        "distinct_prime_factors": prime_factors,
        "distinct_prime_factor_count": omega,
        "smallest_prime_factor": (
            prime_factors[0] if prime_factors else None
        ),
        "second_smallest_prime_factor": (
            prime_factors[1] if omega > 1 else None
        ),
        "leading_correction_exponent": leading_exponent,
        "leading_correction_numerator": leading_term.numerator,
        "leading_correction_denominator": leading_term.denominator,
        "actual_correction_numerator": actual_correction.numerator,
        "actual_correction_denominator": actual_correction.denominator,
        "remainder_numerator": remainder.numerator,
        "remainder_denominator": remainder.denominator,
        "remainder_absolute_bound_numerator": remainder_bound.numerator,
        "remainder_absolute_bound_denominator": remainder_bound.denominator,
        "leading_term_is_exact": exact_leading,
        "remainder_bound_holds": abs(remainder) <= remainder_bound,
    }



def irreducible_density_composition(p: int, left_degree: int,
                                    right_degree: int) -> dict:
    """Audit whether normalized irreducible density composes multiplicatively.

    For coprime positive degrees a,b, compares R_p(ab) with
    R_p(a) R_p(b). The returned defect is exact; no multiplicative law
    is assumed.
    """
    if isinstance(p, bool) or not isinstance(p, int) or not _is_prime(p):
        raise ValueError("p must be a prime integer")
    for name, degree in (("left_degree", left_degree),
                         ("right_degree", right_degree)):
        if (isinstance(degree, bool) or not isinstance(degree, int)
                or degree < 1):
            raise ValueError(f"{name} must be a positive integer")
    if math.gcd(left_degree, right_degree) != 1:
        raise ValueError("degrees must be coprime")

    def normalized(degree: int) -> Fraction:
        return Fraction(
            degree * count_monic_irreducibles(p, degree), p ** degree
        )

    left = normalized(left_degree)
    right = normalized(right_degree)
    combined = normalized(left_degree * right_degree)
    product = left * right
    defect = combined - product
    return {
        "schema": "the-fold-irreducible-density-composition-v1",
        "field_prime": p,
        "left_degree": left_degree,
        "right_degree": right_degree,
        "combined_degree": left_degree * right_degree,
        "degrees_coprime": True,
        "left_density_numerator": left.numerator,
        "left_density_denominator": left.denominator,
        "right_density_numerator": right.numerator,
        "right_density_denominator": right.denominator,
        "combined_density_numerator": combined.numerator,
        "combined_density_denominator": combined.denominator,
        "product_density_numerator": product.numerator,
        "product_density_denominator": product.denominator,
        "composition_defect_numerator": defect.numerator,
        "composition_defect_denominator": defect.denominator,
        "multiplicative": defect == 0,
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


def audit_coprime_density_defect_sign(primes, max_degree: int) -> dict:
    """Exactly survey the sign of R_p(ab)-R_p(a)R_p(b) on a finite grid.

    This is a bounded computational audit, not a proof of a universal sign
    law. Every unordered coprime pair 2 <= a < b <= max_degree is checked
    using exact rational arithmetic.
    """
    if not isinstance(primes, (list, tuple)) or not primes:
        raise ValueError("primes must be a non-empty list or tuple")
    if (isinstance(max_degree, bool) or not isinstance(max_degree, int)
            or max_degree < 3):
        raise ValueError("max_degree must be an integer of at least 3")
    checked_primes = []
    for p in primes:
        if isinstance(p, bool) or not isinstance(p, int) or not _is_prime(p):
            raise ValueError("every entry in primes must be a prime integer")
        if p in checked_primes:
            raise ValueError("primes must not contain duplicates")
        checked_primes.append(p)

    positive = negative = zero = pair_count = 0
    first_nonpositive = None
    minimum = None
    minimum_record = None
    for p in checked_primes:
        def normalized(degree: int) -> Fraction:
            return Fraction(degree * count_monic_irreducibles(p, degree),
                            p ** degree)
        for left in range(2, max_degree + 1):
            for right in range(left + 1, max_degree + 1):
                if math.gcd(left, right) != 1:
                    continue
                defect = normalized(left * right) - normalized(left) * normalized(right)
                pair_count += 1
                if defect > 0:
                    positive += 1
                elif defect < 0:
                    negative += 1
                    if first_nonpositive is None:
                        first_nonpositive = {"field_prime": p, "left_degree": left,
                                             "right_degree": right,
                                             "defect_numerator": defect.numerator,
                                             "defect_denominator": defect.denominator}
                else:
                    zero += 1
                    if first_nonpositive is None:
                        first_nonpositive = {"field_prime": p, "left_degree": left,
                                             "right_degree": right,
                                             "defect_numerator": 0,
                                             "defect_denominator": 1}
                if minimum is None or defect < minimum:
                    minimum = defect
                    minimum_record = {"field_prime": p, "left_degree": left,
                                      "right_degree": right,
                                      "defect_numerator": defect.numerator,
                                      "defect_denominator": defect.denominator}
    return {
        "schema": "the-fold-coprime-density-defect-sign-audit-v1",
        "primes": checked_primes,
        "max_degree": max_degree,
        "coprime_pair_count": pair_count,
        "positive_count": positive,
        "negative_count": negative,
        "zero_count": zero,
        "all_checked_defects_positive": pair_count > 0 and positive == pair_count,
        "first_nonpositive_defect": first_nonpositive,
        "minimum_defect": minimum_record,
        "interpretation": "finite-grid evidence only; no universal sign theorem is asserted",
    }
