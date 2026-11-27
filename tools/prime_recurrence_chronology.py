from __future__ import annotations

"""First-return chronology for the prime spiral memory field."""
from fractions import Fraction
from typing import Sequence

from tools.prime_recurrence_comparison import compare_spiral_arithmetic_recurrence

CHANNELS = (
    "geometry", "gap", "residue", "spectral",
    "geometry_gap_alignment", "geometry_residue_alignment",
    "geometry_spectral_alignment", "any_alignment",
)


def prime_recurrence_chronology(
    primes: Sequence[int], omega: float, residue_moduli: Sequence[int],
    decay: Fraction = Fraction(1, 2), angle_tolerance: float = 0.05,
    radial_relative_tolerance: float = 0.25,
    gap_relative_tolerance: float = 0.25,
    matrix: Sequence[Sequence[int]] | None = None,
) -> dict:
    """Keep each anchor's earliest later match; group equal arrivals."""
    if not isinstance(decay, Fraction) or not 0 <= decay <= 1:
        raise ValueError("decay must be a Fraction in [0, 1]")
    comparison = compare_spiral_arithmetic_recurrence(
        primes, omega, residue_moduli, angle_tolerance=angle_tolerance,
        radial_relative_tolerance=radial_relative_tolerance,
        gap_relative_tolerance=gap_relative_tolerance, matrix=matrix,
    )
    first: dict[str, dict[int, dict]] = {name: {} for name in CHANNELS}
    for pair in comparison["pairwise_results"]:
        i, j = pair["indices"]
        geometric = pair["geometric_recurrence"]
        gap = pair["gap_recurrence"] is True
        residue = pair["residue_recurrence"] is True
        spectral = pair.get("spectral_recurrence") is True
        predicates = {
            "geometry": geometric, "gap": gap, "residue": residue,
            "spectral": spectral,
            "geometry_gap_alignment": geometric and gap,
            "geometry_residue_alignment": geometric and residue,
            "geometry_spectral_alignment": geometric and spectral,
            "any_alignment": geometric and (gap or residue or spectral),
        }
        for channel, matched in predicates.items():
            if matched and i not in first[channel]:
                first[channel][i] = {
                    "anchor_index": i, "arrival_index": j, "latency": j-i,
                    "anchor_prime": pair["prime_labels"][0],
                    "arrival_prime": pair["prime_labels"][1],
                }

    by_arrival: dict[int, list[dict]] = {}
    for channel, anchors in first.items():
        for event in anchors.values():
            by_arrival.setdefault(event["arrival_index"], []).append(
                {"channel": channel, **event}
            )
    event_clock = [
        {"arrival_index": index,
         "events": sorted(events, key=lambda x: (x["anchor_index"], x["channel"]))}
        for index, events in sorted(by_arrival.items())
    ]

    memory = {name: Fraction(0) for name in CHANNELS}
    memory_by_index = []
    for arrival_index in range(1, len(primes)+1):
        emitted = {name: 0 for name in CHANNELS}
        for event in by_arrival.get(arrival_index, []):
            emitted[event["channel"]] += 1
        memory = {name: decay*value + emitted[name]
                  for name, value in memory.items()}
        memory_by_index.append({
            "arrival_index": arrival_index, "emitted": emitted,
            "memory": {name: {"numerator": value.numerator,
                              "denominator": value.denominator}
                       for name, value in memory.items()},
        })

    return {
        "schema": "the-fold-prime-recurrence-chronology-v1",
        "clock": "later prime index j; one update per index, independent of pair count",
        "first_returns": {
            channel: [anchors[i] for i in sorted(anchors)]
            for channel, anchors in first.items()
        },
        "event_clock": event_clock,
        "memory_by_index": memory_by_index,
        "final_memory": {
            name: {"numerator": value.numerator, "denominator": value.denominator}
            for name, value in memory.items()
        },
        "parameters": {
            "decay": {"numerator": decay.numerator, "denominator": decay.denominator},
            "angle_tolerance_radians": angle_tolerance,
            "radial_relative_tolerance": radial_relative_tolerance,
            "gap_relative_tolerance": gap_relative_tolerance,
            "residue_moduli": list(residue_moduli),
            "spectral_matrix_supplied": matrix is not None,
        },
        "interpretation": (
            "First return is defined separately for each anchor and channel. "
            "Events sharing an arrival index are simultaneous in this discrete "
            "clock. Results depend on the chosen spiral and thresholds."
        ),
    }
