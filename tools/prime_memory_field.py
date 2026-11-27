from __future__ import annotations

"""Three-layer prime memory field: geometry, arithmetic, and alignment."""
import math
from fractions import Fraction
from typing import Sequence

from tools.prime_memory_afterimage import _fraction_record, _is_prime, prime_sensitive_memory_path
from tools.prime_recurrence_comparison import compare_spiral_arithmetic_recurrence


def prime_memory_field(
    primes: Sequence[int],
    omega: float,
    residue_moduli: Sequence[int],
    decay: Fraction = Fraction(1, 2),
    angle_tolerance: float = 0.05,
    radial_relative_tolerance: float = 0.25,
    gap_relative_tolerance: float = 0.25,
    matrix: Sequence[Sequence[int]] | None = None,
) -> dict:
    """Build separate path, arithmetic, and alignment-memory layers.

    The geometry layer is the index spiral z_n=n*exp(i*n*omega). The
    arithmetic layer is the prime-sensitive memory path. The alignment layer
    records only pairwise co-occurrences where geometric recurrence and an
    arithmetic recurrence both hold. Three exact rational accumulators keep
    these meanings separate; no scalar is presented as a universal score.
    """
    if not isinstance(decay, Fraction) or not 0 <= decay <= 1:
        raise ValueError("decay must be a Fraction in [0, 1]")
    arithmetic = prime_sensitive_memory_path(
        primes, residue_moduli, matrix=matrix, decay=decay
    )
    comparison = compare_spiral_arithmetic_recurrence(
        primes, omega, residue_moduli,
        angle_tolerance=angle_tolerance,
        radial_relative_tolerance=radial_relative_tolerance,
        gap_relative_tolerance=gap_relative_tolerance,
        matrix=matrix,
    )
    geometry_path = []
    for index, prime in enumerate(primes, start=1):
        theta = index * omega
        geometry_path.append({
            "index": index,
            "prime": prime,
            "radius": index,
            "angle_radians": theta,
            "x": index * math.cos(theta),
            "y": index * math.sin(theta),
        })

    channels = {
        "geometric_pair_recurrence": Fraction(0),
        "arithmetic_gap_recurrence": Fraction(0),
        "arithmetic_residue_recurrence": Fraction(0),
        "arithmetic_spectral_recurrence": Fraction(0),
        "geometry_gap_alignment": Fraction(0),
        "geometry_residue_alignment": Fraction(0),
        "geometry_spectral_alignment": Fraction(0),
    }
    alignment_events = []
    for pair in comparison["pairwise_results"]:
        geometric = pair["geometric_recurrence"]
        gap = pair["gap_recurrence"] is True
        residue = pair["residue_recurrence"] is True
        spectral = pair.get("spectral_recurrence") is True
        if geometric:
            channels["geometric_pair_recurrence"] += 1
        if gap:
            channels["arithmetic_gap_recurrence"] += 1
        if residue:
            channels["arithmetic_residue_recurrence"] += 1
        if spectral:
            channels["arithmetic_spectral_recurrence"] += 1
        if geometric and gap:
            channels["geometry_gap_alignment"] += 1
        if geometric and residue:
            channels["geometry_residue_alignment"] += 1
        if geometric and spectral:
            channels["geometry_spectral_alignment"] += 1
        if geometric and (gap or residue or spectral):
            alignment_events.append({
                "indices": pair["indices"],
                "prime_labels": pair["prime_labels"],
                "gap": gap,
                "residue": residue,
                "spectral": spectral,
            })

    # Fold each pairwise observation in order. This afterimage is a
    # fading memory over pair events, not over prime-index records.
    alignment_memory = {name: Fraction(0) for name in channels}
    for pair in comparison["pairwise_results"]:
        geometric = pair["geometric_recurrence"]
        gap = pair["gap_recurrence"] is True
        residue = pair["residue_recurrence"] is True
        spectral = pair.get("spectral_recurrence") is True
        emitted = {
            "geometric_pair_recurrence": geometric,
            "arithmetic_gap_recurrence": gap,
            "arithmetic_residue_recurrence": residue,
            "arithmetic_spectral_recurrence": spectral,
            "geometry_gap_alignment": geometric and gap,
            "geometry_residue_alignment": geometric and residue,
            "geometry_spectral_alignment": geometric and spectral,
        }
        alignment_memory = {
            name: decay * value + int(emitted[name])
            for name, value in alignment_memory.items()
        }
    return {
        "schema": "the-fold-prime-memory-field-v1",
        "geometry": {
            "embedding": "z_n = n * exp(i*n*omega)",
            "omega_radians": omega,
            "path": geometry_path,
            "recurrence_match_count": comparison["match_counts"]["geometric"],
        },
        "arithmetic": arithmetic,
        "alignment": {
            "definition": "pairwise geometric recurrence co-occurring with at least one arithmetic recurrence",
            "events": alignment_events,
            "channel_totals": {
                key: _fraction_record(value) for key, value in channels.items()
            },
            "memory": {
                key: _fraction_record(value)
                for key, value in alignment_memory.items()
            },
        },
        "controls": comparison["cyclic_shift_baseline"],
        "interpretation": (
            "Geometry, arithmetic, and their alignment are reported as separate "
            "layers. The alignment layer is relational and depends on the "
            "declared thresholds. The cyclic-shift control is finite and is "
            "not a p-value. No prime-distribution law is inferred."
        ),
    }
