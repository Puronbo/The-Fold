"""Deterministic synthetic transformer-shaped checkpoint experiment.

This is a plumbing/demo fixture, not a trained model or empirical AI result.
It uses only Python's standard library and the G-EP13–G-EP15 analysis APIs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from tools.transformer_checkpoint import inspect_state_dict
from tools.transformer_sensitivity import compare_snapshots


def build_synthetic_snapshots() -> dict[str, dict[str, list]]:
    """Return three reproducible snapshots with attention and MLP-shaped weights."""
    identity = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    q_perturbed = [
        [1.01, 0.0, 0.0, 0.0],
        [0.0, 1.01, 0.0, 0.0],
        [0.0, 0.0, 1.01, 0.0],
        [0.0, 0.0, 0.0, 1.01],
    ]
    q_changed = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ]
    up = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 1.0],
    ]
    down = [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    ]

    def state(q_matrix: list[list[float]]) -> dict[str, list]:
        return {
            "encoder.attention.q_proj.weight": q_matrix,
            "encoder.attention.k_proj.weight": identity,
            "encoder.attention.v_proj.weight": identity,
            "encoder.attention.o_proj.weight": identity,
            "encoder.mlp.up_proj.weight": up,
            "encoder.mlp.down_proj.weight": down,
            "encoder.norm.weight": [1.0, 1.0, 1.0, 1.0],
            "encoder.attention.q_proj.bias": [0.0, 0.0, 0.0, 0.0],
        }

    return {
        "synthetic_reference": state(identity),
        "synthetic_small_perturbation": state(q_perturbed),
        "synthetic_rank_changed": state(q_changed),
    }


def run_demo(primes: Sequence[int] = (5, 7),
             scales: Sequence[float] = (1.0, 10.0)) -> dict:
    """Analyze each fixture and compare the Q projection across snapshots."""
    snapshots = build_synthetic_snapshots()
    reports = {
        name: inspect_state_dict(
            state, primes, scales,
            include_square_spectra=True,
            spectral_max_dimension=8,
        )
        for name, state in snapshots.items()
    }
    q_snapshots = {
        name: state["encoder.attention.q_proj.weight"]
        for name, state in snapshots.items()
    }
    sensitivity = compare_snapshots(
        q_snapshots, primes, scales, include_square_spectra=True,
    )
    return {
        "schema": "the-fold-synthetic-transformer-demo-v1",
        "status": "synthetic_fixture_not_trained_model",
        "purpose": (
            "Exercise checkpoint scanning, rectangular MLP rank analysis, "
            "small square attention spectra, skipped vectors/biases, and "
            "snapshot sensitivity end to end."
        ),
        "reports": reports,
        "q_projection_sensitivity": sensitivity,
        "limitations": [
            "All weights are hand-constructed synthetic values, not learned parameters.",
            "Finite-field conversion is lossy and depends on prime and scale.",
            "No model forward pass, prediction, benchmark, or quality metric is evaluated.",
            "Fingerprint agreement does not imply functional equivalence.",
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", default="5,7")
    parser.add_argument("--scales", default="1,10")
    parser.add_argument("--output", default="-", help="JSON path, or - for stdout")
    args = parser.parse_args(argv)
    primes = [int(value) for value in args.primes.split(",") if value.strip()]
    scales = [float(value) for value in args.scales.split(",") if value.strip()]
    report = run_demo(primes, scales)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
