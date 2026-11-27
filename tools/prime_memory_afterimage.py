from __future__ import annotations

"""Prime-sensitive memory paths and exact arithmetic/spectral afterimages."""
from fractions import Fraction
from typing import Sequence
from tools.prime_spectral_profile import prime_spectral_profile


def _is_prime(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def _fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def prime_sensitive_memory_path(
    primes: Sequence[int],
    residue_moduli: Sequence[int],
    matrix: Sequence[Sequence[int]] | None = None,
    decay: Fraction = Fraction(1, 2),
) -> dict:
    """Build a lossless prime path plus exact exponentially weighted afterimage.

    decay multiplies prior memory before each new record is added. Residues
    are recorded for each modulus. If matrix is supplied, its exact
    finite-field Frobenius profile is computed separately modulo each prime.
    """
    if not primes:
        raise ValueError("primes must be non-empty")
    if any(not _is_prime(p) for p in primes):
        raise ValueError("every path label must be prime")
    if any(left >= right for left, right in zip(primes, primes[1:])):
        raise ValueError("primes must be strictly increasing")
    if not residue_moduli or any(
        not isinstance(m, int) or isinstance(m, bool) or m < 2
        for m in residue_moduli
    ):
        raise ValueError("residue_moduli must contain integers >= 2")
    if len(set(residue_moduli)) != len(residue_moduli):
        raise ValueError("residue_moduli must be distinct")
    if not isinstance(decay, Fraction) or not (0 <= decay <= 1):
        raise ValueError("decay must be a Fraction in [0, 1]")

    spectral = prime_spectral_profile(matrix, primes) if matrix is not None else None
    spectral_by_prime = {
        item["prime"]: item for item in spectral["profiles"]
    } if spectral else {}
    records = []
    for index, p in enumerate(primes):
        gap = None if index == 0 else p - primes[index - 1]
        record = {
            "index": index + 1,
            "prime": p,
            "gap_from_previous": gap,
            "residues": {str(m): p % m for m in residue_moduli},
        }
        if p in spectral_by_prime:
            profile = spectral_by_prime[p]
            record["spectral"] = {
                "rank": profile["rank"],
                "frobenius_orbit_degree_histogram":
                    profile["frobenius_orbit_degree_histogram"],
                "factorization_complete": profile["factorization_complete"],
                "extension_profiles_complete":
                    profile["extension_profiles_complete"],
            }
        records.append(record)

    memory: dict[str, Fraction] = {}
    for record in records:
        features: dict[str, int] = {
            f"residue_mod_{m}_{record['residues'][str(m)]}": 1
            for m in residue_moduli
        }
        if record["gap_from_previous"] is not None:
            features["prime_gap"] = record["gap_from_previous"]
        if "spectral" in record:
            features["spectral_rank"] = record["spectral"]["rank"]
            for degree, count in record["spectral"][
                "frobenius_orbit_degree_histogram"
            ].items():
                features[f"spectral_orbit_degree_{degree}"] = count
        keys = set(memory) | set(features)
        memory = {
            key: decay * memory.get(key, Fraction(0))
            + Fraction(features.get(key, 0))
            for key in keys
        }

    return {
        "schema": "the-fold-prime-sensitive-memory-path-v1",
        "primes": list(primes),
        "residue_moduli": list(residue_moduli),
        "decay": _fraction_record(decay),
        "path": records,
        "afterimage": {
            key: _fraction_record(value)
            for key, value in sorted(memory.items())
        },
        "spectral_matrix_dependent": matrix is not None,
        "spectral_schema": spectral["schema"] if spectral else None,
        "interpretation": (
            "The ordered path is lossless for the listed records. The "
            "afterimage is a lossy, exact-rational weighted feature summary. "
            "Spectral channels, when present, depend on the supplied matrix "
            "and finite-field reduction."
        ),
    }
