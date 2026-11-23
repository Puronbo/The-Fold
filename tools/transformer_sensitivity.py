"""Reproducible sensitivity checks for finite-field weight fingerprints.

This is an audit utility: it measures whether exported fingerprints change
under caller-supplied checkpoint/perturbation snapshots and parameter choices.
It does not infer model quality or semantic similarity.
"""
from __future__ import annotations

from typing import Any, Mapping, Sequence

from tools.spectral_fingerprint import automatic_full_spectral_fingerprint
from tools.transformer_adapter import export_weight_matrix
from tools.spectral_fingerprint import rank_mod


def _spectral_signature(result: dict) -> dict:
    """Keep the discrete spectral data needed for exact equality comparison."""
    base_profiles = [
        {
            "eigenvalue": profile["eigenvalue"],
            "block_sizes_descending": profile["block_sizes_descending"],
        }
        for profile in result["profiles"]
    ]
    extension_profiles = [
        {
            "factor": item["factor_coefficients_descending"],
            "block_sizes_descending": item["profile"]["block_sizes_descending"],
        }
        for item in result["extension_eigenvalue_classes"]
    ]
    return {
        "factorization": result["factorization"],
        "base_profiles": base_profiles,
        "extension_profiles": extension_profiles,
    }


def compare_snapshots(
    snapshots: Mapping[str, Any],
    primes: Sequence[int],
    scales: Sequence[float],
    *,
    include_square_spectra: bool = False,
) -> dict:
    """Compare modular rank and optional square spectral signatures.

    The first snapshot in mapping iteration order is the reference. Every
    snapshot must have the same 2-D shape. Each prime/scale pair is evaluated
    independently; a stable result means exact equality of the selected
    finite-field signature under that particular preprocessing choice.
    """
    if not isinstance(snapshots, Mapping) or not snapshots:
        raise ValueError("snapshots must be a non-empty mapping")
    if not primes or not scales:
        raise ValueError("primes and scales must be non-empty")

    names = list(snapshots)
    if any(not isinstance(name, str) or not name for name in names):
        raise ValueError("snapshot names must be non-empty strings")
    exported_shapes = {}
    for name, weights in snapshots.items():
        # Validate shape without selecting a particular field.
        rows = getattr(weights, "tolist", None)
        raw = rows() if callable(rows) else weights
        try:
            matrix_rows = [list(row) for row in raw]
        except (TypeError, ValueError) as exc:
            raise ValueError(f"snapshot {name!r} is not a 2-D matrix") from exc
        if not matrix_rows or not matrix_rows[0]:
            raise ValueError(f"snapshot {name!r} must be non-empty")
        width = len(matrix_rows[0])
        if any(len(row) != width for row in matrix_rows):
            raise ValueError(f"snapshot {name!r} has ragged rows")
        exported_shapes[name] = [len(matrix_rows), width]
    if len({tuple(shape) for shape in exported_shapes.values()}) != 1:
        raise ValueError("all snapshots must have the same matrix shape")

    shape = exported_shapes[names[0]]
    if include_square_spectra and shape[0] != shape[1]:
        raise ValueError("square spectral comparison requires square snapshots")

    configurations = []
    for p in primes:
        for scale in scales:
            entries = {}
            reference_signature = None
            for name in names:
                exported = export_weight_matrix(snapshots[name], p, scale=scale)
                matrix = exported["matrix"]
                signature = {"rank": rank_mod(matrix, p)}
                if include_square_spectra:
                    spectral = automatic_full_spectral_fingerprint(matrix, p)
                    signature["spectrum"] = _spectral_signature(spectral)
                if reference_signature is None:
                    reference_signature = signature
                entries[name] = {
                    "rank": signature["rank"],
                    "stable_vs_reference": signature == reference_signature,
                }
                if include_square_spectra:
                    entries[name]["spectral_signature"] = signature["spectrum"]
            configurations.append({
                "prime": p,
                "scale": float(scale),
                "shape": shape,
                "reference_snapshot": names[0],
                "snapshots": entries,
            })

    return {
        "method": "finite-field fingerprint sensitivity audit",
        "comparison_scope": (
            "modular rank and square spectral/Jordan signature"
            if include_square_spectra else "modular rank only"
        ),
        "interpretation": (
            "Stability is exact equality of exported finite-field signatures "
            "for the specified prime and scale; it is not semantic or "
            "functional equivalence of the original neural networks."
        ),
        "configurations": configurations,
    }
