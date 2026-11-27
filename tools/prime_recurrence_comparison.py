from __future__ import annotations

"""Compare index-spiral proximity with independent prime-feature recurrence."""
import math
from typing import Sequence

from tools.prime_memory_afterimage import _is_prime
from tools.prime_spectral_profile import prime_spectral_profile


def compare_spiral_arithmetic_recurrence(
    primes: Sequence[int], omega: float, residue_moduli: Sequence[int],
    angle_tolerance: float = 0.05,
    radial_relative_tolerance: float = 0.25,
    gap_relative_tolerance: float = 0.25,
    matrix: Sequence[Sequence[int]] | None = None,
) -> dict:
    """Compare geometry and arithmetic pair recurrences on supplied primes.

    Uses z_n=n*exp(i*n*omega). Geometry requires both angular and radial
    proximity. Gaps are measured between supplied entries, not inferred
    consecutive primes. Spectral equality is matrix-dependent.
    """
    if not primes or any(not _is_prime(p) for p in primes):
        raise ValueError("primes must be a non-empty sequence of primes")
    if any(a >= b for a, b in zip(primes, primes[1:])):
        raise ValueError("primes must be strictly increasing")
    if not isinstance(omega, (int, float)) or not math.isfinite(omega):
        raise ValueError("omega must be a finite real number")
    if not residue_moduli or any(
        not isinstance(m, int) or isinstance(m, bool) or m < 2
        for m in residue_moduli
    ) or len(set(residue_moduli)) != len(residue_moduli):
        raise ValueError("residue_moduli must be distinct integers >= 2")
    for name, value, upper in (
        ("angle_tolerance", angle_tolerance, math.pi),
        ("radial_relative_tolerance", radial_relative_tolerance, 1.0),
        ("gap_relative_tolerance", gap_relative_tolerance, 1.0),
    ):
        if not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= upper:
            raise ValueError(f"{name} must lie in [0, {upper}]")

    gaps = [None] + [primes[i] - primes[i - 1] for i in range(1, len(primes))]
    spectral = prime_spectral_profile(matrix, primes) if matrix is not None else None
    spectral_profiles = spectral["profiles"] if spectral else None
    pairs = []
    counts = {key: 0 for key in (
        "geometric", "gap", "residue", "spectral",
        "geometric_and_gap", "geometric_and_residue", "geometric_and_spectral",
    )}
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            angular = abs(math.atan2(
                math.sin((j - i) * omega), math.cos((j - i) * omega)
            ))
            radial = (j - i) / j
            geometric = angular <= angle_tolerance and radial <= radial_relative_tolerance
            gap_match = None
            if gaps[i] is not None and gaps[j] is not None:
                gap_match = abs(gaps[i] - gaps[j]) / max(gaps[i], gaps[j]) <= gap_relative_tolerance
            residue_match = all(primes[i] % m == primes[j] % m for m in residue_moduli)
            spectral_match = None
            if spectral_profiles is not None:
                left, right = spectral_profiles[i], spectral_profiles[j]
                if left["factorization_complete"] and right["factorization_complete"]:
                    spectral_match = (
                        left["rank"] == right["rank"]
                        and left["frobenius_orbit_degree_histogram"]
                        == right["frobenius_orbit_degree_histogram"]
                    )
            row = {
                "indices": [i + 1, j + 1],
                "prime_labels": [primes[i], primes[j]],
                "angular_distance_radians": angular,
                "relative_radial_distance": radial,
                "geometric_recurrence": geometric,
                "gap_recurrence": gap_match,
                "residue_recurrence": residue_match,
            }
            if spectral_profiles is not None:
                row["spectral_recurrence"] = spectral_match
            pairs.append(row)
            for key, matched in (
                ("geometric", geometric), ("gap", gap_match),
                ("residue", residue_match), ("spectral", spectral_match),
                ("geometric_and_gap", geometric and gap_match),
                ("geometric_and_residue", geometric and residue_match),
                ("geometric_and_spectral", geometric and spectral_match),
            ):
                if matched:
                    counts[key] += 1
    return {
        "schema": "the-fold-spiral-arithmetic-recurrence-comparison-v1",
        "prime_count": len(primes), "pair_count": len(pairs),
        "parameters": {
            "spiral": "z_n = n * exp(i*n*omega)", "omega_radians": omega,
            "angle_tolerance_radians": angle_tolerance,
            "radial_relative_tolerance": radial_relative_tolerance,
            "gap_relative_tolerance": gap_relative_tolerance,
            "residue_moduli": list(residue_moduli),
            "spectral_matrix_supplied": matrix is not None,
        },
        "match_counts": counts, "pairwise_results": pairs,
        "interpretation": (
            "Geometric recurrence is angular and radial proximity in the "
            "chosen index spiral. Gap and residue recurrence are independent "
            "arithmetic tests. Spectral recurrence is relative to the supplied "
            "matrix modulo the compared primes. Finite pair counts do not "
            "establish an infinite prime law."
        ),
    }
