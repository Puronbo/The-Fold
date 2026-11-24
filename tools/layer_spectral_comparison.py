"""Layer-level comparison of prime-indexed projection fingerprints.

Input is explicitly grouped by snapshot, layer, and projection name. Square
operators receive Frobenius-orbit profiles; rectangular projections receive
rank-only diagnostics. All comparisons are finite-field/export-specific.
"""
from __future__ import annotations

from itertools import combinations
from typing import Mapping, Sequence

from tools.prime_spectral_profile import prime_spectral_profile
from tools.spectral_fingerprint import rank_mod


def _shape(matrix: Sequence[Sequence[int]]) -> tuple[int, int]:
    if not matrix:
        raise ValueError("projection matrices must be non-empty")
    width = len(matrix[0])
    if width < 1 or any(len(row) != width for row in matrix):
        raise ValueError("projection matrices must be non-empty and rectangular")
    return len(matrix), width


def analyze_layer_snapshots(
    snapshots: Mapping[str, Mapping[str, Mapping[str, Sequence[Sequence[int]]]]],
    primes: Sequence[int],
) -> dict:
    """Compare projection profiles within layers and across snapshots.

    Shape:
      snapshots[snapshot_name][layer_name][projection_name] = matrix

    For each prime, same-rank, same orbit-degree histogram, and exact
    irreducible-factor profile are reported as separate relations.
    """
    if not snapshots:
        raise ValueError("snapshots must be non-empty")
    if not primes:
        raise ValueError("primes must be non-empty")
    if any(not isinstance(x, str) or not x for x in snapshots):
        raise ValueError("snapshot names must be non-empty strings")

    computed: dict = {}
    shapes: dict = {}
    for snapshot_name, layers in snapshots.items():
        if not isinstance(layers, Mapping) or not layers:
            raise ValueError("each snapshot must contain at least one layer")
        computed[snapshot_name] = {}
        shapes[snapshot_name] = {}
        for layer_name, projections in layers.items():
            if not isinstance(layer_name, str) or not layer_name:
                raise ValueError("layer names must be non-empty strings")
            if not isinstance(projections, Mapping) or not projections:
                raise ValueError("each layer must contain projections")
            computed[snapshot_name][layer_name] = {}
            shapes[snapshot_name][layer_name] = {}
            for projection_name, matrix in projections.items():
                if not isinstance(projection_name, str) or not projection_name:
                    raise ValueError("projection names must be non-empty strings")
                shape = _shape(matrix)
                shapes[snapshot_name][layer_name][projection_name] = list(shape)
                if shape[0] == shape[1]:
                    computed[snapshot_name][layer_name][projection_name] = {
                        "kind": "square_spectral",
                        "profile": prime_spectral_profile(matrix, primes),
                    }
                else:
                    computed[snapshot_name][layer_name][projection_name] = {
                        "kind": "rectangular_rank_only",
                        "ranks": {
                            str(p): rank_mod(matrix, p) for p in primes
                        },
                        "shape": list(shape),
                    }

    within_layer = []
    for snapshot_name, layers in computed.items():
        for layer_name, projections in layers.items():
            for p in primes:
                entries = {}
                for projection_name, item in projections.items():
                    if item["kind"] == "square_spectral":
                        profile = next(
                            x for x in item["profile"]["profiles"]
                            if x["prime"] == p
                        )
                        entries[projection_name] = {
                            "kind": item["kind"],
                            "rank": profile["rank"],
                            "orbit_histogram":
                                profile["frobenius_orbit_degree_histogram"],
                            "factor_classes": profile["irreducible_orbit_classes"],
                        }
                    else:
                        entries[projection_name] = {
                            "kind": item["kind"],
                            "rank": item["ranks"][str(p)],
                        }
                pairwise = []
                for left, right in combinations(entries, 2):
                    a, b = entries[left], entries[right]
                    record = {
                        "left": left,
                        "right": right,
                        "same_rank": a["rank"] == b["rank"],
                    }
                    if a["kind"] == b["kind"] == "square_spectral":
                        record["same_orbit_histogram"] = (
                            a["orbit_histogram"] == b["orbit_histogram"]
                        )
                        record["same_exact_factor_profile"] = (
                            a["orbit_histogram"] == b["orbit_histogram"]
                            and a["factor_classes"] == b["factor_classes"]
                        )
                    else:
                        record["spectral_comparison"] = "not_comparable"
                    pairwise.append(record)
                within_layer.append({
                    "snapshot": snapshot_name,
                    "layer": layer_name,
                    "prime": p,
                    "projections": entries,
                    "pairwise": pairwise,
                })

    stability = []
    all_layers = sorted({layer for layers in computed.values() for layer in layers})
    all_projections = sorted({
        (layer, projection)
        for layers in computed.values()
        for layer, projections in layers.items()
        for projection in projections
    })
    for layer, projection in all_projections:
        present = [
            name for name, layers in computed.items()
            if layer in layers and projection in layers[layer]
        ]
        for p in primes:
            records = {}
            reference = None
            for name in present:
                item = computed[name][layer][projection]
                if item["kind"] == "square_spectral":
                    profile = next(x for x in item["profile"]["profiles"] if x["prime"] == p)
                    signature = (
                        profile["rank"],
                        profile["frobenius_orbit_degree_histogram"],
                        profile["irreducible_orbit_classes"],
                    )
                    records[name] = {
                        "kind": item["kind"],
                        "rank": profile["rank"],
                        "same_full_profile_as_reference": None,
                    }
                else:
                    signature = (item["ranks"][str(p)],)
                    records[name] = {
                        "kind": item["kind"],
                        "rank": item["ranks"][str(p)],
                        "same_full_profile_as_reference": None,
                    }
                if reference is None:
                    reference = signature
                records[name]["same_full_profile_as_reference"] = signature == reference
            stability.append({
                "layer": layer,
                "projection": projection,
                "prime": p,
                "reference_snapshot": present[0] if present else None,
                "snapshots": records,
            })

    return {
        "schema": "the-fold-layer-prime-profile-v1",
        "snapshots": computed,
        "within_layer_comparisons": within_layer,
        "cross_snapshot_stability": stability,
        "limitations": [
            "Only square projections receive Frobenius factor profiles; rectangular projections receive rank-only diagnostics.",
            "Profiles describe quantized matrices over selected finite fields, not original real-valued operators.",
            "Matching profiles do not imply equal functions, activations, outputs, or model quality.",
            "Projection names and layer groupings are supplied by the caller; this tool does not infer architecture semantics.",
        ],
    }
