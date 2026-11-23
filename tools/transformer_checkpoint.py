"""Inspect 2-D model weights from a PyTorch checkpoint.

PyTorch is imported only by the CLI loader. The analysis functions accept a
plain state-dict-like mapping and use the dependency-free G-EP13 adapter.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from tools.transformer_adapter import analyze_weight_matrix, analyze_square_weight_operator


def _state_dict(checkpoint: Any) -> Mapping[str, Any]:
    if not isinstance(checkpoint, Mapping):
        raise ValueError("checkpoint must contain a mapping or state dictionary")
    for key in ("state_dict", "model_state_dict", "model"):
        candidate = checkpoint.get(key)
        if isinstance(candidate, Mapping):
            return candidate
    return checkpoint


def inspect_state_dict(
    state: Mapping[str, Any],
    primes: Sequence[int],
    scales: Sequence[float],
    *,
    max_elements: int = 250_000,
    include_square_spectra: bool = False,
    spectral_max_dimension: int = 32,
) -> dict:
    """Create a reproducible report for eligible 2-D weight tensors.

    Tensors larger than max_elements are skipped. Full spectral analysis is
    further restricted to square matrices no larger than spectral_max_dimension.
    """
    if not isinstance(state, Mapping):
        raise ValueError("state must be a mapping")
    if not primes or not scales:
        raise ValueError("primes and scales must be non-empty")
    if max_elements < 1 or spectral_max_dimension < 1:
        raise ValueError("size limits must be positive integers")

    layers = []
    skipped = []
    for name, tensor in state.items():
        shape = getattr(tensor, "shape", None)
        if shape is None:
            # Plain nested lists are useful in tests and small programmatic use.
            try:
                shape = (len(tensor), len(tensor[0]))
            except (TypeError, IndexError, KeyError):
                skipped.append({"name": str(name), "reason": "not a 2-D tensor"})
                continue
        try:
            dimensions = tuple(int(x) for x in shape)
        except (TypeError, ValueError):
            skipped.append({"name": str(name), "reason": "invalid tensor shape"})
            continue
        if len(dimensions) != 2 or min(dimensions, default=0) < 1:
            skipped.append({"name": str(name), "reason": "not a non-empty 2-D tensor"})
            continue
        rows, cols = dimensions
        if rows * cols > max_elements:
            skipped.append({
                "name": str(name), "shape": [rows, cols],
                "reason": f"exceeds max_elements={max_elements}",
            })
            continue
        if "weight" not in str(name).lower():
            skipped.append({"name": str(name), "shape": [rows, cols],
                            "reason": "not named as a weight"})
            continue

        configurations = []
        for p in primes:
            for scale in scales:
                report = analyze_weight_matrix(tensor, p, scale=scale)
                item = {
                    "prime": p,
                    "scale": float(scale),
                    "rank_over_field": report["rank_over_field"],
                    "rank_defect": report["rank_defect"],
                    "shape": report["shape"],
                }
                if (include_square_spectra and rows == cols
                        and rows <= spectral_max_dimension):
                    spectral = analyze_square_weight_operator(tensor, p, scale=scale)
                    item["spectral_fingerprint"] = spectral["spectral_fingerprint"]
                configurations.append(item)
        layers.append({
            "name": str(name),
            "shape": [rows, cols],
            "configurations": configurations,
        })

    return {
        "schema": "the-fold-transformer-checkpoint-report-v1",
        "method": "lossy quantization round(scale * weight) mod prime",
        "quantization": "Python round: nearest, ties-to-even",
        "interpretation": (
            "Ranks and spectra describe exported matrices over each selected "
            "finite field; they are not invariants of the original real-valued "
            "model and do not establish functional equivalence or model quality."
        ),
        "parameters": {
            "primes": list(primes),
            "scales": [float(x) for x in scales],
            "max_elements": max_elements,
            "include_square_spectra": include_square_spectra,
            "spectral_max_dimension": spectral_max_dimension,
        },
        "layers": layers,
        "skipped": skipped,
    }


def load_pytorch_checkpoint(path: str) -> Mapping[str, Any]:
    """Load a checkpoint using PyTorch's restricted weights-only mode."""
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError(
            "PyTorch is required only for checkpoint loading; install torch "
            "or call inspect_state_dict with an already-loaded state mapping."
        ) from exc
    # Do not fall back to unrestricted pickle loading for untrusted files.
    checkpoint = torch.load(path, map_location="cpu", weights_only=True)
    return _state_dict(checkpoint)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", help="PyTorch weights-only checkpoint path")
    parser.add_argument("--primes", default="101,103")
    parser.add_argument("--scales", default="100,1000")
    parser.add_argument("--max-elements", type=int, default=250_000)
    parser.add_argument("--include-square-spectra", action="store_true")
    parser.add_argument("--spectral-max-dimension", type=int, default=32)
    parser.add_argument("--output", default="-", help="JSON output path, or - for stdout")
    args = parser.parse_args(argv)

    primes = [int(value) for value in args.primes.split(",") if value.strip()]
    scales = [float(value) for value in args.scales.split(",") if value.strip()]
    state = load_pytorch_checkpoint(args.checkpoint)
    report = inspect_state_dict(
        state, primes, scales,
        max_elements=args.max_elements,
        include_square_spectra=args.include_square_spectra,
        spectral_max_dimension=args.spectral_max_dimension,
    )
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
