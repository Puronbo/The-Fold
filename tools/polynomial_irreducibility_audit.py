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




def _poly_trim(poly: list[Fraction]) -> list[Fraction]:
    """Trim trailing zero coefficients from an ascending-order polynomial."""
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def _poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return _poly_trim([
        Fraction(index) * poly[index]
        for index in range(1, len(poly))
    ])


def _poly_remainder(
    dividend: list[Fraction], divisor: list[Fraction]
) -> list[Fraction]:
    """Return the exact polynomial remainder over Q."""
    remainder = _poly_trim(list(dividend))
    divisor = _poly_trim(list(divisor))
    if divisor == [0]:
        raise ZeroDivisionError("polynomial divisor cannot be zero")
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        for index, coefficient in enumerate(divisor):
            remainder[index + shift] -= factor * coefficient
        remainder = _poly_trim(remainder)
    return remainder


def _sturm_sequence(poly: list[Fraction]) -> list[list[Fraction]]:
    """Build the exact Sturm sequence for a nonconstant polynomial."""
    first = _poly_trim(list(poly))
    second = _poly_derivative(first)
    if first == [0]:
        raise ValueError("polynomial cannot be zero")
    sequence = [first]
    if second == [0]:
        return sequence
    sequence.append(second)
    while sequence[-1] != [0]:
        remainder = _poly_remainder(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append([-coefficient for coefficient in remainder])
    return sequence


def _poly_one_sided_sign(
    poly: list[Fraction], point: Fraction, side: int
) -> int:
    """Return the polynomial sign infinitesimally to one side of point."""
    current = poly
    order = 0
    while True:
        value = sum(
            (coefficient * point ** index
             for index, coefficient in enumerate(current)),
            Fraction(0),
        )
        if value:
            sign = 1 if value > 0 else -1
            return sign if side > 0 or order % 2 == 0 else -sign
        if len(current) <= 1:
            return 0
        current = _poly_derivative(current)
        order += 1


def _sturm_variations(
    sequence: list[list[Fraction]], point: Fraction, side: int
) -> int:
    signs = [
        _poly_one_sided_sign(poly, point, side)
        for poly in sequence
    ]
    signs = [sign for sign in signs if sign]
    return sum(
        signs[index] != signs[index - 1]
        for index in range(1, len(signs))
    )


def coprime_composition_excess_global_sign_certificate(
    degrees: list[int],
) -> dict:
    """Use an exact Sturm count to certify sign on every real Q >= 2.

    With x=1/Q, factor H_Q=x**e0 P(x), where P has integer
    coefficients and P(0) is the nonzero leading spectrum coefficient.
    Sturm's theorem counts roots of P in (0, 1/2). A separate exact
    endpoint check handles Q=2. If there are no roots in (0, 1/2]
    then P has the sign of P(0) throughout that interval.
    """
    spectrum_data = coprime_composition_excess_spectrum(degrees)
    terms = spectrum_data["spectrum"]
    base_exponent = terms[0]["exponent"]
    polynomial = [Fraction(0)] * (
        max(term["exponent"] - base_exponent for term in terms) + 1
    )
    for term in terms:
        polynomial[term["exponent"] - base_exponent] = Fraction(
            term["coefficient"]
        )
    polynomial = _poly_trim(polynomial)
    endpoint = Fraction(1, 2)
    endpoint_value = sum(
        (coefficient * endpoint ** index
         for index, coefficient in enumerate(polynomial)),
        Fraction(0),
    )
    if len(polynomial) == 1:
        root_count_open = 0
    else:
        sequence = _sturm_sequence(polynomial)
        root_count_open = (
            _sturm_variations(sequence, Fraction(0), 1)
            - _sturm_variations(sequence, endpoint, -1)
        )
    endpoint_is_root = endpoint_value == 0
    global_sign_certified = root_count_open == 0 and not endpoint_is_root
    leading_coefficient = terms[0]["coefficient"]
    sign = "positive" if leading_coefficient > 0 else "negative"
    endpoint_sign = (
        "positive" if endpoint_value > 0 else
        "negative" if endpoint_value < 0 else "zero"
    )
    return {
        "schema": "the-fold-composition-excess-global-sign-sturm-v1",
        "degrees": degrees,
        "polynomial_coefficients_ascending": [
            coefficient.numerator if coefficient.denominator == 1
            else str(coefficient)
            for coefficient in polynomial
        ],
        "polynomial_degree": len(polynomial) - 1,
        "open_interval": "(0, 1/2)",
        "sturm_root_count_open_interval": root_count_open,
        "q_equals_two_value_sign": endpoint_sign,
        "q_equals_two_is_root": endpoint_is_root,
        "global_sign_certified_for_all_real_q_ge_2":
            global_sign_certified,
        "certified_sign": sign if global_sign_certified else None,
        "leading_sign": sign,
        "interpretation": (
            "zero roots on (0,1/2] prove the leading sign for every real "
            "Q >= 2; a positive root count is an exact obstruction to "
            "this simple global sign certificate, not a failure of the "
            "eventual-sign theorem"
        ),
        "spectrum": terms,
    }


def coprime_composition_excess_sign_certificate(
    degrees: list[int], field_size: int
) -> dict:
    """Certify the exact finite-Q sign and a conservative eventual threshold.

    The exact Laurent spectrum is evaluated over Fraction arithmetic. If
    its first nonzero term is c*Q**(-m), and L is the sum of absolute values
    of all later coefficients, then for Q > L/abs(c) the tail is strictly
    smaller than the leading term. Thus the leading coefficient determines
    the sign for every prime-power field size at or above the returned
    integer threshold.
    """
    if not _is_prime_power(field_size):
        raise ValueError("field_size must be a prime power")
    spectrum_data = coprime_composition_excess_spectrum(degrees)
    terms = spectrum_data["spectrum"]
    leading = terms[0]
    tail_l1 = sum(abs(term["coefficient"]) for term in terms[1:])
    threshold = max(
        2, tail_l1 // abs(leading["coefficient"]) + 1
    )
    value = sum(
        (Fraction(term["coefficient"],
                  field_size ** term["exponent"])
         for term in terms),
        Fraction(0, 1),
    )
    exact_sign = (
        "positive" if value > 0 else
        "negative" if value < 0 else "zero"
    )
    eventual_sign = (
        "positive" if leading["coefficient"] > 0 else "negative"
    )

    # The coefficient-tail bound certifies every integer Q >= threshold.
    # Inspect the finite interval below it to find the smallest integer
    # threshold that works for all Q thereafter. This is optimal over all
    # integers Q >= 2, hence also valid for prime-power field sizes.
    last_exception = 1
    for candidate_q in range(2, threshold):
        candidate_value = sum(
            (Fraction(term["coefficient"],
                      candidate_q ** term["exponent"])
             for term in terms),
            Fraction(0, 1),
        )
        candidate_sign = (
            "positive" if candidate_value > 0 else
            "negative" if candidate_value < 0 else "zero"
        )
        if candidate_sign != eventual_sign:
            last_exception = candidate_q
    exact_integer_threshold = max(2, last_exception + 1)
    return {
        "schema": "the-fold-composition-excess-sign-certificate-v1",
        "degrees": degrees,
        "field_size": field_size,
        "exact_value_numerator": value.numerator,
        "exact_value_denominator": value.denominator,
        "exact_sign": exact_sign,
        "leading_exponent": leading["exponent"],
        "leading_coefficient": leading["coefficient"],
        "tail_coefficient_l1_bound": tail_l1,
        "eventual_sign": eventual_sign,
        "sufficient_field_size_threshold": threshold,
        "smallest_integer_threshold": exact_integer_threshold,
        "threshold_scope": (
            "smallest integer Q0 >= 2 such that every integer Q >= Q0 "
            "has the eventual sign; therefore also valid for prime powers"
        ),
        "threshold_guarantee": (
            "for every prime-power Q >= threshold, the exact sign equals "
            "the leading coefficient sign"
        ),
        "threshold_proof_condition": (
            f"Q > {tail_l1}/{abs(leading['coefficient'])}"
        ),
        "spectrum": terms,
    }


def coprime_composition_excess_temporal_fold(
    two_steps_ago: list[int],
    one_step_ago: list[int],
    present: list[int],
) -> dict:
    """Return the exact second temporal difference of three excess spectra.

    Inputs are ordered chronologically. If H_t(Q) is the composition excess
    for the present tuple, the result is H_t - 2 H_(t-1) + H_(t-2).
    Exponents are aligned before coefficients are combined, and zero
    coefficients are removed. The zero polynomial is represented explicitly.
    """
    states = [
        coprime_composition_excess_spectrum(degrees)
        for degrees in (two_steps_ago, one_step_ago, present)
    ]
    coefficients: dict[int, int] = {}
    for multiplier, state in zip((1, -2, 1), states):
        for term in state["spectrum"]:
            exponent = term["exponent"]
            coefficients[exponent] = (
                coefficients.get(exponent, 0)
                + multiplier * term["coefficient"]
            )
    spectrum = [
        {"exponent": exponent, "coefficient": coefficients[exponent]}
        for exponent in sorted(coefficients)
        if coefficients[exponent]
    ]
    return {
        "schema": "the-fold-composition-excess-temporal-fold-v1",
        "chronological_degrees": [
            two_steps_ago, one_step_ago, present
        ],
        "temporal_operator": "H_t - 2*H_(t-1) + H_(t-2)",
        "spectrum": spectrum,
        "identically_zero": not spectrum,
        "leading_exponent": spectrum[0]["exponent"] if spectrum else None,
        "leading_coefficient": (
            spectrum[0]["coefficient"] if spectrum else 0
        ),
        "term_count": len(spectrum),
        "interpretation": (
            "exact second temporal difference of the three composition-"
            "excess Laurent spectra; zero means coefficient-wise affine "
            "evolution across these three states"
        ),
    }



def laurent_spectrum_global_sign_certificate(spectrum: list[dict]) -> dict:
    """Certify the sign of an integer Laurent spectrum for every real Q >= 2.

    Each term has integer exponent (positive, zero, or negative) and integer coefficient.
    Duplicate exponents are combined. The polynomial is normalized by
    factoring out its smallest power of x=1/Q, then an exact rational Sturm
    sequence counts roots on (0, 1/2). The endpoint x=1/2 is checked
    separately. The zero polynomial is reported explicitly.
    """
    if not isinstance(spectrum, list) or not spectrum:
        raise ValueError("spectrum must be a nonempty list of terms")
    coefficients: dict[int, int] = {}
    for term in spectrum:
        if not isinstance(term, dict) or set(term) != {"exponent", "coefficient"}:
            raise ValueError(
                "each spectrum term must contain exponent and coefficient"
            )
        exponent = term["exponent"]
        coefficient = term["coefficient"]
        if isinstance(exponent, bool) or not isinstance(exponent, int):
            raise ValueError("exponents must be integers")
        if (isinstance(coefficient, bool) or not isinstance(coefficient, int)):
            raise ValueError("coefficients must be integers")
        coefficients[exponent] = coefficients.get(exponent, 0) + coefficient

    normalized_terms = [
        {"exponent": exponent, "coefficient": coefficient}
        for exponent, coefficient in sorted(coefficients.items())
        if coefficient
    ]
    if not normalized_terms:
        return {
            "schema": "the-fold-laurent-global-sign-sturm-v1",
            "normalized_spectrum": [],
            "identically_zero": True,
            "global_sign_certified_for_all_real_q_ge_2": False,
            "certified_sign": None,
            "sturm_root_count_open_interval": None,
            "q_equals_two_value_sign": "zero",
            "q_equals_two_is_root": True,
            "interpretation": "the Laurent spectrum is identically zero",
        }

    base_exponent = normalized_terms[0]["exponent"]
    polynomial = [Fraction(0)] * (
        normalized_terms[-1]["exponent"] - base_exponent + 1
    )
    for term in normalized_terms:
        polynomial[term["exponent"] - base_exponent] = Fraction(
            term["coefficient"]
        )
    polynomial = _poly_trim(polynomial)
    endpoint = Fraction(1, 2)
    endpoint_value = sum(
        (coefficient * endpoint ** index
         for index, coefficient in enumerate(polynomial)),
        Fraction(0),
    )
    if len(polynomial) == 1:
        root_count_open = 0
    else:
        sequence = _sturm_sequence(polynomial)
        root_count_open = (
            _sturm_variations(sequence, Fraction(0), 1)
            - _sturm_variations(sequence, endpoint, -1)
        )
    endpoint_is_root = endpoint_value == 0
    certified = root_count_open == 0 and not endpoint_is_root
    leading_coefficient = normalized_terms[0]["coefficient"]
    leading_sign = "positive" if leading_coefficient > 0 else "negative"
    endpoint_sign = (
        "positive" if endpoint_value > 0 else
        "negative" if endpoint_value < 0 else "zero"
    )
    return {
        "schema": "the-fold-laurent-global-sign-sturm-v1",
        "normalized_spectrum": normalized_terms,
        "factored_minimum_exponent": base_exponent,
        "polynomial_coefficients_ascending": [
            value.numerator if value.denominator == 1 else str(value)
            for value in polynomial
        ],
        "polynomial_degree": len(polynomial) - 1,
        "open_interval": "(0, 1/2)",
        "sturm_root_count_open_interval": root_count_open,
        "q_equals_two_value_sign": endpoint_sign,
        "q_equals_two_is_root": endpoint_is_root,
        "identically_zero": False,
        "global_sign_certified_for_all_real_q_ge_2": certified,
        "certified_sign": leading_sign if certified else None,
        "leading_sign": leading_sign,
        "interpretation": (
            "zero roots on (0,1/2] prove the sign for every real Q >= 2; "
            "a positive root count or endpoint root means this certificate "
            "does not establish a global sign"
        ),
    }



def laurent_spectrum_family_uniform_sign_certificate(
    spectra: list[list[dict]],
) -> dict:
    """Certify one eventual sign for a finite family of integer Laurent spectra.

    Each member is certified by its leading coefficient and an exact L1
    bound on its remaining coefficients. For a member with leading term
    c*Q**(-e), its tail has magnitude at most L*Q**(-e-1), where L is the
    sum of absolute values of all later coefficients. Thus every integer
    Q >= floor(L/abs(c))+1 (and Q >= 2) has the leading sign.

    A common threshold is the maximum of these exact member thresholds,
    provided every member is nonzero and all leading signs agree.
    """
    if not isinstance(spectra, list) or not spectra:
        raise ValueError("spectra must be a nonempty list")
    members = []
    for index, spectrum in enumerate(spectra):
        certificate = laurent_spectrum_global_sign_certificate(spectrum)
        normalized = certificate["normalized_spectrum"]
        if certificate["identically_zero"]:
            members.append({
                "index": index,
                "identically_zero": True,
                "eventual_sign": None,
                "threshold": None,
                "leading_exponent": None,
                "leading_coefficient": 0,
                "tail_coefficient_l1_bound": None,
            })
            continue
        leading = normalized[0]
        tail_l1 = sum(abs(term["coefficient"]) for term in normalized[1:])
        threshold = max(2, tail_l1 // abs(leading["coefficient"]) + 1)
        members.append({
            "index": index,
            "identically_zero": False,
            "eventual_sign": (
                "positive" if leading["coefficient"] > 0 else "negative"
            ),
            "threshold": threshold,
            "leading_exponent": leading["exponent"],
            "leading_coefficient": leading["coefficient"],
            "tail_coefficient_l1_bound": tail_l1,
        })

    signs = {
        member["eventual_sign"]
        for member in members
        if member["eventual_sign"] is not None
    }
    all_nonzero = all(not member["identically_zero"] for member in members)
    common_sign = (
        next(iter(signs))
        if all_nonzero and len(signs) == 1
        else None
    )
    common_threshold = (
        max(member["threshold"] for member in members)
        if common_sign is not None
        else None
    )
    return {
        "schema": "the-fold-laurent-family-uniform-sign-v1",
        "member_count": len(members),
        "all_members_nonzero": all_nonzero,
        "common_eventual_sign": common_sign,
        "uniform_integer_field_size_threshold": common_threshold,
        "uniform_guarantee": (
            "every member has the common_eventual_sign for every real Q "
            "at or above the returned threshold"
            if common_sign is not None
            else None
        ),
        "members": members,
        "interpretation": (
            "finite-family uniform sign certificate; this proves a common "
            "sign beyond one threshold for every supplied snapshot, but "
            "does not by itself certify an infinite future sequence"
        ),
    }
