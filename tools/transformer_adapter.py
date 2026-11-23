"""Optional adapter for exporting neural-network weights to finite fields.

No NumPy or PyTorch dependency is imported. Tensor-like objects are accepted
through the common detach/cpu/tolist protocol.
"""
from __future__ import annotations

import math
from typing import Any

from tools.spectral_fingerprint import (
    automatic_full_spectral_fingerprint,
    rank_mod,
)


def _is_prime(p: int) -> bool:
    if isinstance(p, bool) or not isinstance(p, int) or p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    divisor = 3
    while divisor * divisor <= p:
        if p % divisor == 0:
            return False
        divisor += 2
    return True


def _to_rows(weights: Any) -> list[list[Any]]:
    value = weights
    # Duck typing avoids making a framework an installation requirement.
    if callable(getattr(value, "detach", None)):
        value = value.detach()
    if callable(getattr(value, "cpu", None)):
        value = value.cpu()
    if callable(getattr(value, "tolist", None)):
        value = value.tolist()
    try:
        rows = [list(row) for row in value]
    except (TypeError, ValueError) as exc:
        raise ValueError("weights must be a two-dimensional array or tensor") from exc
    if not rows or not rows[0]:
        raise ValueError("weights must be non-empty")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("weight rows must have equal length")
    return rows


def export_weight_matrix(
    weights: Any,
    p: int,
    *,
    scale: float = 1.0,
) -> dict:
    """Quantize a 2-D weight matrix and reduce it into F_p.

    Each entry is mapped as round(float(weight) * scale) mod p. Python's
    round uses ties-to-even. The operation is lossy for non-integral inputs;
    scale and policy are recorded in the returned metadata.
    """
    if not _is_prime(p):
        raise ValueError("p must be a prime")
    try:
        scale_value = float(scale)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("scale must be a finite positive number") from exc
    if not math.isfinite(scale_value) or scale_value <= 0:
        raise ValueError("scale must be a finite positive number")

    rows = _to_rows(weights)
    converted: list[list[int]] = []
    for row in rows:
        output_row = []
        for entry in row:
            if isinstance(entry, bool):
                numeric = float(entry)
            else:
                try:
                    numeric = float(entry)
                except (TypeError, ValueError, OverflowError) as exc:
                    raise ValueError("weight entries must be finite real numbers") from exc
            if not math.isfinite(numeric):
                raise ValueError("weight entries must be finite real numbers")
            scaled = numeric * scale_value
            if not math.isfinite(scaled):
                raise ValueError("scaled weight entries must remain finite")
            output_row.append(int(round(scaled)) % p)
        converted.append(output_row)

    return {
        "matrix": converted,
        "metadata": {
            "field": f"F_{p}",
            "prime": p,
            "shape": [len(converted), len(converted[0])],
            "scale": scale_value,
            "quantization": "round-to-nearest, ties-to-even",
            "mapping": "round(weight * scale) mod p",
            "lossy_preprocessing": True,
        },
    }


def analyze_weight_matrix(weights: Any, p: int, *, scale: float = 1.0) -> dict:
    """Export a layer and compute its exact modular rank.

    Rectangular layers are supported. Rank is an invariant of the exported
    finite-field matrix, not of the original real-valued layer.
    """
    exported = export_weight_matrix(weights, p, scale=scale)
    matrix = exported["matrix"]
    rank = rank_mod(matrix, p)
    return {
        **exported["metadata"],
        "rank_over_field": rank,
        "rank_defect": min(exported["metadata"]["shape"]) - rank,
    }


def analyze_square_weight_operator(
    weights: Any, p: int, *, scale: float = 1.0
) -> dict:
    """Run full spectral/Jordan analysis on a square exported weight matrix.

    This is intentionally separate from rectangular-layer rank analysis:
    eigenvalues and Jordan form require an endomorphism.
    """
    exported = export_weight_matrix(weights, p, scale=scale)
    rows, cols = exported["metadata"]["shape"]
    if rows != cols:
        raise ValueError("Jordan/spectral analysis requires a square weight matrix")
    result = automatic_full_spectral_fingerprint(exported["matrix"], p)
    return {
        "export_metadata": exported["metadata"],
        "spectral_fingerprint": result,
    }
