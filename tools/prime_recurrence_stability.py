from __future__ import annotations
"""Stable-return analysis layered on first-return chronology."""
from fractions import Fraction
from typing import Sequence
from tools.prime_recurrence_comparison import compare_spiral_arithmetic_recurrence

CHANNELS = ("geometry", "gap", "residue", "spectral",
            "geometry_gap_alignment", "geometry_residue_alignment",
            "geometry_spectral_alignment", "any_alignment")


def prime_recurrence_stability(
    primes: Sequence[int], omega: float, residue_moduli: Sequence[int],
    required_consecutive: int = 2, decay: Fraction = Fraction(1, 2),
    angle_tolerance: float = 0.05, radial_relative_tolerance: float = 0.25,
    gap_relative_tolerance: float = 0.25,
    matrix: Sequence[Sequence[int]] | None = None,
) -> dict:
    """A stable return is a run of consecutive matching later indices."""
    if (not isinstance(required_consecutive, int) or isinstance(required_consecutive, bool)
            or required_consecutive < 2):
        raise ValueError("required_consecutive must be an integer >= 2")
    if not isinstance(decay, Fraction) or not 0 <= decay <= 1:
        raise ValueError("decay must be a Fraction in [0, 1]")
    comparison = compare_spiral_arithmetic_recurrence(
        primes, omega, residue_moduli, angle_tolerance=angle_tolerance,
        radial_relative_tolerance=radial_relative_tolerance,
        gap_relative_tolerance=gap_relative_tolerance, matrix=matrix)
    lookup = {(r["indices"][0], r["indices"][1]): r
              for r in comparison["pairwise_results"]}
    first = {c: [] for c in CHANNELS}
    stable = {c: [] for c in CHANNELS}
    for anchor in range(1, len(primes)):
        for channel in CHANNELS:
            run_start = None
            run = 0
            first_seen = None
            for arrival in range(anchor + 1, len(primes) + 1):
                pair = lookup[(anchor, arrival)]
                g = pair["geometric_recurrence"]
                gap = pair["gap_recurrence"] is True
                residue = pair["residue_recurrence"] is True
                spectral = pair.get("spectral_recurrence") is True
                matched = {
                    "geometry": g, "gap": gap, "residue": residue,
                    "spectral": spectral,
                    "geometry_gap_alignment": g and gap,
                    "geometry_residue_alignment": g and residue,
                    "geometry_spectral_alignment": g and spectral,
                    "any_alignment": g and (gap or residue or spectral),
                }[channel]
                if matched:
                    if first_seen is None:
                        first_seen = arrival
                        first[channel].append({
                            "anchor_index": anchor, "first_arrival_index": arrival,
                            "latency": arrival-anchor})
                    if run == 0:
                        run_start = arrival
                    run += 1
                    if run == required_consecutive:
                        stable[channel].append({
                            "anchor_index": anchor, "first_arrival_index": first_seen,
                            "stable_arrival_index": arrival, "run_start_index": run_start,
                            "consecutive_matches": run, "anchor_prime": primes[anchor-1],
                            "stable_arrival_prime": primes[arrival-1]})
                        break
                else:
                    run_start, run = None, 0

    by_arrival = {}
    for channel, events in stable.items():
        for event in events:
            counts = by_arrival.setdefault(event["stable_arrival_index"],
                                           {c: 0 for c in CHANNELS})
            counts[channel] += 1
    memory = {c: Fraction(0) for c in CHANNELS}
    trace = []
    for index in range(1, len(primes)+1):
        emitted = by_arrival.get(index, {c: 0 for c in CHANNELS})
        memory = {c: decay*memory[c] + emitted[c] for c in CHANNELS}
        trace.append({"arrival_index": index, "emitted_stable_returns": emitted,
                      "memory": {c: {"numerator": v.numerator, "denominator": v.denominator}
                                 for c, v in memory.items()}})
    return {
        "schema": "the-fold-prime-recurrence-stability-v1",
        "stability_rule": {"definition": "consecutive later-index matches for one anchor and channel",
                           "required_consecutive": required_consecutive,
                           "intervening_nonmatch": "resets the run"},
        "first_returns": first, "stable_returns": stable,
        "stable_arrival_counts": [{"arrival_index": i, "counts": v}
                                  for i, v in sorted(by_arrival.items())],
        "memory_by_index": trace,
        "final_memory": {c: {"numerator": v.numerator, "denominator": v.denominator}
                         for c, v in memory.items()},
        "parameters": {"decay": {"numerator": decay.numerator, "denominator": decay.denominator},
                       "angle_tolerance_radians": angle_tolerance,
                       "radial_relative_tolerance": radial_relative_tolerance,
                       "gap_relative_tolerance": gap_relative_tolerance,
                       "residue_moduli": list(residue_moduli),
                       "spectral_matrix_supplied": matrix is not None},
        "interpretation": ("Stability means consecutive matching later indices under the chosen "
                           "finite-sample predicates; it does not establish an infinite recurrence.")}


