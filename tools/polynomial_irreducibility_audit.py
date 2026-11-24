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


def audit_coprime_bad_proportion_order(primes, max_degree: int) -> dict:
    """Check E_p(ab) < min(E_p(a), E_p(b)) on a finite coprime grid.

    Here E_p(n)=1-R_p(n) is the proportion of elements of F_(p^n)
    contained in proper subfields. All comparisons use exact fractions.
    This is a finite audit, not a universal theorem.
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

    checked = 0
    strict_count = 0
    first_failure = None
    maximum_ratio = None
    maximum_ratio_record = None
    for p in checked_primes:
        def bad_proportion(degree: int) -> Fraction:
            return Fraction(p ** degree - degree * count_monic_irreducibles(p, degree),
                            p ** degree)
        for left in range(2, max_degree + 1):
            for right in range(left + 1, max_degree + 1):
                if math.gcd(left, right) != 1:
                    continue
                left_bad = bad_proportion(left)
                right_bad = bad_proportion(right)
                product_bad = bad_proportion(left * right)
                checked += 1
                smaller = min(left_bad, right_bad)
                holds = product_bad < smaller
                if holds:
                    strict_count += 1
                elif first_failure is None:
                    first_failure = {
                        "field_prime": p, "left_degree": left,
                        "right_degree": right,
                        "product_bad_numerator": product_bad.numerator,
                        "product_bad_denominator": product_bad.denominator,
                        "left_bad_numerator": left_bad.numerator,
                        "left_bad_denominator": left_bad.denominator,
                        "right_bad_numerator": right_bad.numerator,
                        "right_bad_denominator": right_bad.denominator,
                    }
                ratio = product_bad / smaller if smaller else Fraction(0, 1)
                if maximum_ratio is None or ratio > maximum_ratio:
                    maximum_ratio = ratio
                    maximum_ratio_record = {
                        "field_prime": p, "left_degree": left,
                        "right_degree": right,
                        "ratio_numerator": ratio.numerator,
                        "ratio_denominator": ratio.denominator,
                    }
    return {
        "schema": "the-fold-coprime-bad-proportion-order-v1",
        "primes": checked_primes,
        "max_degree": max_degree,
        "coprime_pair_count": checked,
        "strict_order_count": strict_count,
        "all_checked_pairs_strict": checked > 0 and strict_count == checked,
        "first_failure": first_failure,
        "largest_product_to_smaller_factor_bad_ratio": maximum_ratio_record,
        "interpretation": "finite exact evidence only; universal strict order remains unproved",
    }


def audit_coprime_bad_proportion_ratio_bound(primes, max_degree: int) -> dict:
    """Test the proposed sharp ratio bound on a finite coprime-degree grid.

    The conjectured bound is
        E_p(ab) / min(E_p(a), E_p(b)) <= (p**2+p-1)/p**3.
    All calculations and comparisons use exact rational arithmetic. A
    successful finite audit is evidence only, not a universal proof.
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

    checked = 0
    within_bound = 0
    first_failure = None
    maximum_ratio = None
    maximum_record = None
    for p in checked_primes:
        conjectured_bound = Fraction(p * p + p - 1, p ** 3)

        def bad_proportion(degree: int) -> Fraction:
            return Fraction(
                p ** degree - degree * count_monic_irreducibles(p, degree),
                p ** degree,
            )

        for left in range(2, max_degree + 1):
            for right in range(left + 1, max_degree + 1):
                if math.gcd(left, right) != 1:
                    continue
                denominator = min(bad_proportion(left), bad_proportion(right))
                combined = bad_proportion(left * right)
                ratio = combined / denominator if denominator else Fraction(0, 1)
                checked += 1
                holds = ratio <= conjectured_bound
                if holds:
                    within_bound += 1
                elif first_failure is None:
                    first_failure = {
                        "field_prime": p,
                        "left_degree": left,
                        "right_degree": right,
                        "ratio_numerator": ratio.numerator,
                        "ratio_denominator": ratio.denominator,
                        "bound_numerator": conjectured_bound.numerator,
                        "bound_denominator": conjectured_bound.denominator,
                    }
                if maximum_ratio is None or ratio > maximum_ratio:
                    maximum_ratio = ratio
                    maximum_record = {
                        "field_prime": p,
                        "left_degree": left,
                        "right_degree": right,
                        "ratio_numerator": ratio.numerator,
                        "ratio_denominator": ratio.denominator,
                        "bound_numerator": conjectured_bound.numerator,
                        "bound_denominator": conjectured_bound.denominator,
                        "attains_proposed_bound": ratio == conjectured_bound,
                    }

    return {
        "schema": "the-fold-coprime-bad-proportion-ratio-bound-v1",
        "primes": checked_primes,
        "max_degree": max_degree,
        "coprime_pair_count": checked,
        "within_bound_count": within_bound,
        "all_checked_pairs_within_bound": checked > 0 and within_bound == checked,
        "first_failure": first_failure,
        "largest_observed_ratio": maximum_record,
        "interpretation": (
            "finite exact evidence only; the proposed universal ratio bound "
            "is not proved"
        ),
    }


def coprime_defect_exponent_spectrum(left_degree: int,
                                      right_degree: int) -> dict:
    """Return the exact finite Laurent-polynomial spectrum of the defect.

    With x = 1/p, this returns integer coefficients c_k such that
    Delta_p(a,b) = sum_k c_k*x**k. Equal exponents are combined and
    zero coefficients are removed. The degrees must be coprime and > 1.
    """
    for name, value in (("left_degree", left_degree),
                        ("right_degree", right_degree)):
        if (isinstance(value, bool) or not isinstance(value, int)
                or value <= 1):
            raise ValueError(f"{name} must be an integer greater than one")
    if math.gcd(left_degree, right_degree) != 1:
        raise ValueError("degrees must be coprime")

    def error_terms(degree: int) -> dict[int, int]:
        terms: dict[int, int] = {}
        for divisor in range(2, degree + 1):
            if degree % divisor == 0:
                mu = _mobius(divisor)
                if mu:
                    exponent = degree - degree // divisor
                    terms[exponent] = terms.get(exponent, 0) - mu
        return terms

    left_terms = error_terms(left_degree)
    right_terms = error_terms(right_degree)
    product_degree_terms = error_terms(left_degree * right_degree)
    coefficients: dict[int, int] = {}

    def add(exponent: int, coefficient: int) -> None:
        coefficients[exponent] = coefficients.get(exponent, 0) + coefficient

    for exponent, coefficient in left_terms.items():
        add(exponent, coefficient)
    for exponent, coefficient in right_terms.items():
        add(exponent, coefficient)
    for left_exponent, left_coefficient in left_terms.items():
        for right_exponent, right_coefficient in right_terms.items():
            add(left_exponent + right_exponent,
                -left_coefficient * right_coefficient)
    for exponent, coefficient in product_degree_terms.items():
        add(exponent, -coefficient)

    spectrum = [
        {"exponent": exponent, "coefficient": coefficients[exponent]}
        for exponent in sorted(coefficients)
        if coefficients[exponent]
    ]
    if not spectrum:
        raise ArithmeticError("the coprime defect spectrum vanished")
    return {
        "schema": "the-fold-coprime-defect-exponent-spectrum-v1",
        "left_degree": left_degree,
        "right_degree": right_degree,
        "spectrum": spectrum,
        "leading_exponent": spectrum[0]["exponent"],
        "leading_coefficient": spectrum[0]["coefficient"],
        "second_nonzero_term": spectrum[1] if len(spectrum) > 1 else None,
        "term_count": len(spectrum),
        "interpretation": (
            "exact finite identity: Delta_p(a,b) is the sum of "
            "coefficient * p**(-exponent) over spectrum entries"
        ),
    }


def evaluate_coprime_defect_spectrum(field_size: int,
                                      left_degree: int,
                                      right_degree: int) -> Fraction:
    """Evaluate the exact defect spectrum at any integer field size >= 2."""
    if (isinstance(field_size, bool) or not isinstance(field_size, int)
            or field_size < 2):
        raise ValueError("field_size must be an integer at least two")
    spectrum = coprime_defect_exponent_spectrum(
        left_degree, right_degree
    )
    return sum(
        (Fraction(term["coefficient"], field_size ** term["exponent"])
         for term in spectrum["spectrum"]),
        Fraction(0, 1),
    )


def _is_prime_power(value: int) -> bool:
    """Return whether value is a positive power of exactly one prime."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    remaining = value
    distinct_factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            distinct_factors += 1
            if distinct_factors > 1:
                return False
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        distinct_factors += 1
    return distinct_factors == 1


def count_monic_irreducibles_over_field(field_size: int,
                                         degree: int) -> int:
    """Count monic irreducibles over F_Q for any prime-power Q."""
    if not _is_prime_power(field_size):
        raise ValueError("field_size must be a prime power")
    if (isinstance(degree, bool) or not isinstance(degree, int)
            or degree < 1):
        raise ValueError("degree must be a positive integer")
    numerator = sum(
        _mobius(divisor) * field_size ** (degree // divisor)
        for divisor in range(1, degree + 1)
        if degree % divisor == 0
    )
    quotient, remainder = divmod(numerator, degree)
    if remainder:
        raise ArithmeticError("irreducible-count formula was not integral")
    return quotient


def irreducible_density_over_field(field_size: int,
                                    degree: int) -> dict:
    """Return exact normalized irreducible density data over F_Q."""
    count = count_monic_irreducibles_over_field(field_size, degree)
    normalized = Fraction(degree * count, field_size ** degree)
    return {
        "schema": "the-fold-prime-power-field-density-v1",
        "field_size": field_size,
        "degree": degree,
        "irreducible_count": count,
        "normalized_density_numerator": normalized.numerator,
        "normalized_density_denominator": normalized.denominator,
        "bad_proportion_numerator": (1 - normalized).numerator,
        "bad_proportion_denominator": (1 - normalized).denominator,
    }


def coprime_composition_excess_spectrum(degrees: list[int]) -> dict:
    """Return E_Q(product(degrees)) - product(E_Q(degree_i)) exactly.

    The input must contain at least two pairwise-coprime integers > 1.
    Coefficients are integer and exponents are nonnegative integers.
    """
    if not isinstance(degrees, list) or len(degrees) < 2:
        raise ValueError("degrees must be a list containing at least two values")
    for degree in degrees:
        if (isinstance(degree, bool) or not isinstance(degree, int)
                or degree <= 1):
            raise ValueError("every degree must be an integer greater than one")
    for index, degree in enumerate(degrees):
        if any(math.gcd(degree, other) != 1
               for other in degrees[index + 1:]):
            raise ValueError("degrees must be pairwise coprime")

    def error_terms(degree: int) -> dict[int, int]:
        terms: dict[int, int] = {}
        for divisor in range(2, degree + 1):
            if degree % divisor == 0:
                mu = _mobius(divisor)
                if mu:
                    exponent = degree - degree // divisor
                    terms[exponent] = terms.get(exponent, 0) - mu
        return terms

    product_degree = math.prod(degrees)
    composite_terms = error_terms(product_degree)
    product_terms = {0: 1}
    for degree in degrees:
        next_terms: dict[int, int] = {}
        for exponent, coefficient in product_terms.items():
            for error_exponent, error_coefficient in error_terms(degree).items():
                total_exponent = exponent + error_exponent
                next_terms[total_exponent] = (
                    next_terms.get(total_exponent, 0)
                    + coefficient * error_coefficient
                )
        product_terms = next_terms

    coefficients: dict[int, int] = {}
    for exponent, coefficient in composite_terms.items():
        coefficients[exponent] = coefficients.get(exponent, 0) + coefficient
    for exponent, coefficient in product_terms.items():
        coefficients[exponent] = coefficients.get(exponent, 0) - coefficient
    spectrum = [
        {"exponent": exponent, "coefficient": coefficients[exponent]}
        for exponent in sorted(coefficients)
        if coefficients[exponent]
    ]
    if not spectrum:
        raise ArithmeticError("composition excess spectrum vanished")
    return {
        "schema": "the-fold-coprime-composition-excess-spectrum-v1",
        "degrees": degrees,
        "composite_degree": product_degree,
        "spectrum": spectrum,
        "leading_exponent": spectrum[0]["exponent"],
        "leading_coefficient": spectrum[0]["coefficient"],
        "sign_for_sufficiently_large_field": (
            "positive" if spectrum[0]["coefficient"] > 0 else "negative"
        ),
        "term_count": len(spectrum),
    }


def irreducible_density_convergence_over_field(field_size: int,
                                                degree: int) -> dict:
    """Return exact density error and a field-uniform bound over F_Q."""
    count = count_monic_irreducibles_over_field(field_size, degree)
    normalized = Fraction(degree * count, field_size ** degree)
    error = 1 - normalized

    remaining = degree
    omega = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            omega += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        omega += 1

    divisor_bound = Fraction(2 ** omega - 1, 2 ** (degree // 2))
    uniform_bound = Fraction(degree - 1, 2 ** (degree // 2))
    return {
        "schema": "the-fold-prime-power-density-convergence-v1",
        "field_size": field_size,
        "degree": degree,
        "normalized_density_numerator": normalized.numerator,
        "normalized_density_denominator": normalized.denominator,
        "signed_error_numerator": error.numerator,
        "signed_error_denominator": error.denominator,
        "absolute_error": float(abs(error)),
        "distinct_prime_divisor_count": omega,
        "divisor_bound": float(divisor_bound),
        "uniform_bound": (degree - 1) * (2 ** (-degree / 2)),
        "uniform_bound_holds": abs(error) <= uniform_bound,
    }


def coprime_composition_excess_asymptotic(degrees: list[int]) -> dict:
    """Classify the leading large-Q term of E_Q(prod n_i)-prod E_Q(n_i).

    For n>1, write A(n)=n(1-1/q(n)), where q(n) is its smallest
    prime divisor. The first term of E_Q(n) is Q**(-A(n)). This routine
    compares A(product(degrees)) with sum(A(degree)); exact spectrum
    collection resolves the only possible two-factor resonance.
    """
    if not isinstance(degrees, list) or len(degrees) < 2:
        raise ValueError("degrees must be a list containing at least two values")
    for degree in degrees:
        if (isinstance(degree, bool) or not isinstance(degree, int)
                or degree <= 1):
            raise ValueError("every degree must be an integer greater than one")
    for index, degree in enumerate(degrees):
        if any(math.gcd(degree, other) != 1
               for other in degrees[index + 1:]):
            raise ValueError("degrees must be pairwise coprime")

    def first_exponent(value: int) -> tuple[int, int]:
        remaining = value
        prime = 2
        while prime * prime <= remaining and remaining % prime:
            prime += 1 if prime == 2 else 2
        smallest = prime if remaining % prime == 0 else remaining
        return value - value // smallest, smallest

    product_degree = math.prod(degrees)
    product_exponent, product_prime = first_exponent(product_degree)
    input_data = [first_exponent(value) for value in degrees]
    input_exponent_sum = sum(item[0] for item in input_data)
    spectrum_data = None
    if product_exponent < input_exponent_sum:
        regime = "positive_without_leading_cancellation"
        leading_exponent = product_exponent
        leading_coefficient = 1
    elif product_exponent > input_exponent_sum:
        regime = "negative_without_leading_cancellation"
        leading_exponent = input_exponent_sum
        leading_coefficient = -1
    else:
        regime = "leading_resonance"
        spectrum_data = coprime_composition_excess_spectrum(degrees)
        leading_exponent = spectrum_data["leading_exponent"]
        leading_coefficient = spectrum_data["leading_coefficient"]

    two_factor_resonance = False
    if len(degrees) == 2:
        smaller, larger = sorted(degrees)
        two_factor_resonance = smaller == 2 and _is_prime(larger)
    return {
        "schema": "the-fold-coprime-composition-excess-asymptotic-v1",
        "degrees": degrees,
        "product_degree": product_degree,
        "smallest_prime_factor_of_product": product_prime,
        "input_first_exponents": [item[0] for item in input_data],
        "product_first_exponent": product_exponent,
        "sum_of_input_first_exponents": input_exponent_sum,
        "leading_regime": regime,
        "leading_exponent_after_cancellation": leading_exponent,
        "leading_coefficient_after_cancellation": leading_coefficient,
        "two_factor_resonance_iff_two_and_odd_prime": two_factor_resonance,
        "exact_spectrum": spectrum_data,
    }
