#!/usr/bin/env python3
"""Exact finite-window data for invariant linear readouts of the Fold quotient.

The full invariant linear-functional space is a product. This script samples
finite truncations: one F2 weight per zero-mode point Q and one k_Q weight
per odd orbit root q and finite closed point Q. Outputs are exact GF(2) labels.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Any

from coinvariant_basis_data import (
    degree,
    field_trace,
    irreducibles,
    mod,
    mul_mod,
    trace_dual_basis,
)


def coordinate_keys(
    zero_degree_max: int, q_max: int, degree_max: int
) -> tuple[list[int], list[tuple[int, int]]]:
    zero_qs = irreducibles(zero_degree_max)
    orbit_qs = irreducibles(degree_max)
    orbit_keys = [
        (q, Q)
        for q in range(1, q_max + 1, 2)
        for Q in orbit_qs
    ]
    return zero_qs, orbit_keys


def random_weights(
    zero_qs: list[int],
    orbit_keys: list[tuple[int, int]],
    rng: random.Random,
) -> tuple[dict[int, int], dict[tuple[int, int], int]]:
    zero = {Q: rng.randrange(2) for Q in zero_qs}
    orbit = {
        (q, Q): rng.randrange(1 << degree(Q))
        for q, Q in orbit_keys
    }
    return zero, orbit


def random_input(
    zero_qs: list[int],
    orbit_keys: list[tuple[int, int]],
    rng: random.Random,
) -> tuple[dict[int, int], dict[tuple[int, int], int]]:
    zero = {Q: rng.randrange(2) for Q in zero_qs}
    orbit = {
        (q, Q): rng.randrange(1 << degree(Q))
        for q, Q in orbit_keys
    }
    return zero, orbit


def evaluate(
    zero_weights: dict[int, int],
    orbit_weights: dict[tuple[int, int], int],
    zero_input: dict[int, int],
    orbit_input: dict[tuple[int, int], int],
) -> int:
    result = 0
    for Q, weight in zero_weights.items():
        result ^= weight & zero_input.get(Q, 0)
    for key, weight in orbit_weights.items():
        q, Q = key
        value = orbit_input.get(key, 0)
        result ^= field_trace(mul_mod(weight, value, Q), Q)
    return result


def serialize_weights(
    zero_weights: dict[int, int],
    orbit_weights: dict[tuple[int, int], int],
) -> dict[str, Any]:
    return {
        "zero_weights": [
            {"Q_bits": Q, "epsilon": weight}
            for Q, weight in sorted(zero_weights.items())
        ],
        "orbit_weights": [
            {"q": q, "Q_bits": Q, "c_bits": weight}
            for (q, Q), weight in sorted(orbit_weights.items())
        ],
    }


def serialize_input(
    zero_input: dict[int, int],
    orbit_input: dict[tuple[int, int], int],
) -> dict[str, Any]:
    return {
        "zero_coordinates": [
            {"Q_bits": Q, "z": value}
            for Q, value in sorted(zero_input.items())
        ],
        "orbit_coordinates": [
            {"q": q, "Q_bits": Q, "residue_bits": value}
            for (q, Q), value in sorted(orbit_input.items())
        ],
    }


def self_test() -> None:
    qs = irreducibles(4)
    roots = [1, 3]
    orbit_keys = [(q, Q) for q in roots for Q in qs]
    zero_weights = {Q: (i & 1) for i, Q in enumerate(qs)}
    orbit_weights = {
        key: (i + 1) % (1 << degree(key[1]))
        for i, key in enumerate(orbit_keys)
    }

    # Every zero-mode coordinate has its expected dual bit.
    for Q in qs:
        z = {P: int(P == Q) for P in qs}
        assert evaluate(zero_weights, {}, z, {}) == zero_weights[Q]

    # Trace-dual basis vectors recover all coordinates in every residue field.
    for key in orbit_keys:
        q, Q = key
        dual = trace_dual_basis(Q)
        d = degree(Q)
        for i in range(d):
            x = {key: 1 << i}
            got = evaluate({}, {(q, Q): dual[i]}, {}, x)
            assert got == 1
        # For every standard basis coordinate, its own dual coefficient
        # returns 1 and all other dual coefficients return 0.
        for i, c in enumerate(dual):
            for j in range(d):
                value = field_trace(mul_mod(c, 1 << j, Q), Q)
                assert value == int(i == j)

    # The readout is F2-linear in both the input and the weights.
    rng = random.Random(20261123)
    z0, o0 = random_input(qs, orbit_keys, rng)
    z1, o1 = random_input(qs, orbit_keys, rng)
    w0, v0 = random_weights(qs, orbit_keys, rng)
    w1, v1 = random_weights(qs, orbit_keys, rng)
    zsum = {Q: z0[Q] ^ z1[Q] for Q in qs}
    osum = {key: o0[key] ^ o1[key] for key in orbit_keys}
    wsum = {Q: w0[Q] ^ w1[Q] for Q in qs}
    vsum = {
        key: mod(v0[key] ^ v1[key], key[1])
        for key in orbit_keys
    }
    assert evaluate(w0, v0, zsum, osum) == (
        evaluate(w0, v0, z0, o0) ^ evaluate(w0, v0, z1, o1)
    )
    assert evaluate(wsum, vsum, z0, o0) == (
        evaluate(w0, v0, z0, o0) ^ evaluate(w1, v1, z0, o0)
    )


def generate(
    count: int,
    zero_degree_max: int,
    q_max: int,
    degree_max: int,
    seed: int,
):
    rng = random.Random(seed)
    zero_qs, orbit_keys = coordinate_keys(
        zero_degree_max, q_max, degree_max
    )
    zero_weights, orbit_weights = random_weights(
        zero_qs, orbit_keys, rng
    )
    yield {
        "task": "invariant_linear_readout_weights",
        **serialize_weights(zero_weights, orbit_weights),
    }
    for index in range(count):
        zero_input, orbit_input = random_input(
            zero_qs, orbit_keys, rng
        )
        label = evaluate(
            zero_weights, orbit_weights, zero_input, orbit_input
        )
        yield {
            "task": "invariant_linear_readout_sample",
            "sample_id": index,
            **serialize_input(zero_input, orbit_input),
            "label": label,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--zero-degree-max", type=int, default=4)
    parser.add_argument("--q-max", type=int, default=7)
    parser.add_argument("--degree-max", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.count < 0 or args.zero_degree_max < 1:
        parser.error("count must be nonnegative and zero-degree-max positive")
    if args.q_max < 0 or args.degree_max < 1:
        parser.error("q-max must be nonnegative and degree-max positive")
    if args.self_test:
        self_test()
        print(
            "self-test: product-dual evaluation, finite-field trace duality, "
            "and GF(2)-linearity passed",
            file=sys.stderr,
        )
    for row in generate(
        args.count,
        args.zero_degree_max,
        args.q_max,
        args.degree_max,
        args.seed,
    ):
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
