"""Prime-indexed Frobenius-orbit profiles for exact matrix spectra.

For each prime, factor the characteristic polynomial over F_p. An
irreducible degree-d factor represents a Frobenius orbit of d conjugate
eigenvalues. This module reports those orbit degrees and multiplicities
alongside modular rank; it does not claim predictive value for neural nets.
"""
from __future__ import annotations

from typing import Mapping, Sequence

from tools.spectral_fingerprint import (
    _validate_matrix,
    automatic_full_spectral_fingerprint,
    rank_mod,
)


def prime_spectral_profile(matrix: Sequence[Sequence[int]],
                           primes: Sequence[int]) -> dict:
    """Build exact factor-degree/Frobenius-orbit profiles over each prime."""
    if not primes:
        raise ValueError("primes must be non-empty")
    dimension = _validate_matrix(matrix, primes[0])
    profiles = []
    for p in primes:
        result = automatic_full_spectral_fingerprint(matrix, p)
        factors = [
            {
                "degree": factor["degree"],
                "multiplicity_per_root": factor["multiplicity"],
                "frobenius_orbit_size": factor["degree"],
                "represented_root_count": (
                    factor["degree"] * factor["multiplicity"]
                ),
                "polynomial_coefficients_descending":
                    factor["coefficients_descending"],
            }
            for factor in result["factorization"]
            if "degree" in factor
        ]
        orbit_histogram: dict[str, int] = {}
        represented_dimension = 0
        for factor in factors:
            degree = factor["degree"]
            count = factor["represented_root_count"]
            key = str(degree)
            orbit_histogram[key] = orbit_histogram.get(key, 0) + count
            represented_dimension += count
        profiles.append({
            "prime": p,
            "rank": rank_mod(matrix, p),
            "characteristic_polynomial_coefficients_descending":
                result["characteristic_polynomial_coefficients_descending"],
            "frobenius_orbit_degree_histogram": dict(
                sorted(orbit_histogram.items(), key=lambda item: int(item[0]))
            ),
            "irreducible_orbit_classes": factors,
            "represented_eigenvalue_count_with_multiplicity":
                represented_dimension,
            "factorization_complete": result["irreducible_factorization_complete"],
            "extension_profiles_complete": result["extension_classes_complete"],
        })
    return {
        "schema": "the-fold-prime-frobenius-profile-v1",
        "dimension": dimension,
        "interpretation": (
            "A degree-d irreducible factor represents d Frobenius-conjugate "
            "roots. Histogram counts represented roots with algebraic "
            "multiplicity; irreducible_orbit_classes count factor classes."
        ),
        "profiles": profiles,
    }


def compare_prime_profiles(matrices: Mapping[str, Sequence[Sequence[int]]],
                           primes: Sequence[int]) -> dict:
    """Compare rank and Frobenius-orbit profiles against the first matrix."""
    if not matrices:
        raise ValueError("matrices must be a non-empty mapping")
    names = list(matrices)
    if any(not isinstance(name, str) or not name for name in names):
        raise ValueError("matrix names must be non-empty strings")
    dimensions = [_validate_matrix(matrices[name], primes[0]) for name in names]
    if len(set(dimensions)) != 1:
        raise ValueError("all matrices must have the same dimension")
    computed = {
        name: prime_spectral_profile(matrix, primes)
        for name, matrix in matrices.items()
    }
    comparisons = []
    for index, p in enumerate(primes):
        reference = computed[names[0]]["profiles"][index]
        entries = {}
        for name in names:
            current = computed[name]["profiles"][index]
            entries[name] = {
                "rank": current["rank"],
                "same_rank_as_reference": current["rank"] == reference["rank"],
                "same_orbit_degree_histogram_as_reference": (
                    current["frobenius_orbit_degree_histogram"]
                    == reference["frobenius_orbit_degree_histogram"]
                ),
                "same_full_frobenius_profile_as_reference": (
                    current["frobenius_orbit_degree_histogram"]
                    == reference["frobenius_orbit_degree_histogram"]
                    and current["irreducible_orbit_classes"]
                    == reference["irreducible_orbit_classes"]
                ),
            }
        comparisons.append({
            "prime": p,
            "reference": names[0],
            "matrices": entries,
        })
    return {
        "schema": "the-fold-prime-profile-comparison-v1",
        "reference_matrix": names[0],
        "profiles": computed,
        "comparisons": comparisons,
        "caution": (
            "These are invariants of each matrix after reduction modulo p. "
            "They are not invariant under arbitrary real-weight perturbations "
            "or quantization choices, and do not imply functional similarity."
        ),
    }
