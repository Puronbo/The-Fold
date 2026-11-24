"""Bounded exhaustive and deterministic sampled irreducibility audits."""
from __future__ import annotations

import random
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


def audit_irreducibility_agreement(
    p: int,
    degree: int,
    *,
    max_cases: int = 100_000,
    sample_count: int = 10_000,
    seed: int = 0,
) -> dict:
    """Compare the irreducibility predicate and factorizer over monic degree-n polynomials.

    Exhaust every polynomial when p**degree <= max_cases. Otherwise check
    sample_count distinct polynomials using a reproducible pseudorandom sample.
    Sampled agreement is not a certificate for the untested domain.
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

    return {
        "schema": "the-fold-irreducibility-audit-v1",
        "field_prime": p,
        "degree": degree,
        "domain_size": total,
        "checked_count": checked,
        "mode": "exhaustive" if exhaustive else "deterministic_sample",
        "seed": None if exhaustive else seed,
        "complete": checked == total,
        "agreement": mismatch_count == 0,
        "mismatch_count": mismatch_count,
        "mismatches_first_20": mismatches,
        "predicate_irreducible_count_in_checked_set": irreducible_count,
        "sample_count_requested": None if exhaustive else sample_count,
    }
