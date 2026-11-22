#!/usr/bin/env python3
"""Exact GF(2)[S] data generator for the Fold section-change action.

Polynomials are encoded as nonnegative integers: bit i is the coefficient
of S**i. This emits verified low-order graded examples only; it does not
fabricate the still-unknown higher-order quotient action.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Iterable

S = 0b10


def add(a: int, b: int) -> int:
    return a ^ b


def mul(a: int, b: int) -> int:
    """Polynomial multiplication in GF(2)[S], encoded by bitmasks."""
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def derivative(a: int) -> int:
    """Formal derivative d/dS in characteristic two."""
    out = 0
    i = 1
    while (1 << i) <= a:
        if (a >> i) & 1 and (i & 1):
            out |= 1 << (i - 1)
        i += 1
    return out


def e_mul(u: tuple[int, int], v: tuple[int, int]) -> tuple[int, int]:
    """Multiply a+b*t and c+d*t with t^2=S."""
    a, b = u
    c, d = v
    return (
        add(mul(a, c), mul(S, mul(b, d))),
        add(mul(a, d), mul(b, c)),
    )


def odd_layer_raw(r: int, e: int, f: int, x: int, y: int):
    """Raw p^r correction for the odd-layer representative (x,t*y)."""
    eps = r & 1
    delta_a = (0, mul(f, x))
    delta_b = (
        add(mul(S, mul(f, y)), mul(eps, mul(e, x))),
        add(mul(e, y), mul(eps, mul(f, x))),
    )
    return delta_a, delta_b


def odd_layer_action(r: int, e: int, f: int, x: int, y: int):
    """Reduced correction; the target quotient depends on depth parity."""
    da, db = odd_layer_raw(r, e, f, x, y)
    if r & 1:
        # Target Q_even: retain the t coefficient of the second entry.
        return {"target_type": "Q_even", "target": db[1]}
    # Target Q_odd: (A,B) -> (A_0,A_1+B_1).
    return {
        "target_type": "Q_odd",
        "target": [da[0], add(da[1], db[1])],
    }


def even_layer_raw(e: int, f: int, d: int):
    """Raw correction for the even-layer representative (0,t*d)."""
    return (0, 0), (mul(S, mul(f, d)), mul(e, d))


def even_layer_action(r: int, e: int, f: int, d: int):
    da, db = even_layer_raw(e, f, d)
    if r & 1:
        return {
            "target_type": "Q_odd",
            "target": [da[0], add(da[1], db[1])],
        }
    return {"target_type": "Q_even", "target": db[1]}


def bracket_parameter(
    v: tuple[int, int], u: tuple[int, int]
) -> tuple[int, int]:
    """Parameter of [X_v,X_u] = X_{t(e_v*f_u+e_u*f_v)}."""
    ev, fv = v
    eu, fu = u
    return (0, add(mul(ev, fu), mul(eu, fv)))


def leading_mixed_parameter(
    v: tuple[int, int], u: tuple[int, int]
) -> tuple[int, int]:
    """Mixed coefficient e_u*v for the composition order in G-4cc."""
    ev, fv = v
    eu, _fu = u
    return (mul(eu, ev), mul(eu, fv))


def random_poly(rng: random.Random, max_degree: int) -> int:
    return rng.randrange(1 << (max_degree + 1))


def self_test() -> None:
    values = [0, 1, S, 1 ^ S, 1 ^ (1 << 2)]
    assert derivative(1 ^ S ^ (1 << 2) ^ (1 << 3)) == 1 ^ (1 << 2)
    assert e_mul((1, 1), (1, 1)) == (1 ^ S, 0)

    # Verify reductions from raw coefficient pairs, for both depth parities.
    for r in (1, 2):
        for e in values:
            for f in values:
                for x in values:
                    for y in values:
                        da, db = odd_layer_raw(r, e, f, x, y)
                        expected = add(mul(f, x), mul(e, y))
                        got = odd_layer_action(r, e, f, x, y)["target"]
                        if r & 1:
                            assert got == expected
                            assert db[1] == expected
                        else:
                            assert got == [0, expected]
                            assert add(da[1], db[1]) == expected
                for d in values:
                    da, db = even_layer_raw(e, f, d)
                    got = even_layer_action(r, e, f, d)["target"]
                    if r & 1:
                        assert got == [0, mul(e, d)]
                    else:
                        assert got == mul(e, d)

    # Every nonzero leading parameter is detected on an odd-layer probe.
    for e in values:
        for f in values:
            if e == 0 and f == 0:
                continue
            x, y = (1, 0) if f else (0, 1)
            for r in (1, 2):
                got = odd_layer_action(r, e, f, x, y)["target"]
                assert got != 0 and got != [0, 0]

    # The bracket is alternating and detects these independent test pairs.
    for v in [(e, f) for e in values for f in values]:
        assert bracket_parameter(v, v) == (0, 0)
    for v, u in [((1, 0), (0, 1)), ((S, 1), (1, S))]:
        assert bracket_parameter(v, u) != (0, 0)

    print("self-test: all exact GF(2)[S] checks passed", file=sys.stderr)


def generate(count: int, max_degree: int, seed: int) -> Iterable[dict]:
    rng = random.Random(seed)
    for _ in range(count):
        r = 1 + rng.randrange(8)
        e, f, x, y, d = (
            random_poly(rng, max_degree) for _ in range(5)
        )
        yield {
            "task": "odd_layer_transition",
            "depth": r,
            "e": e,
            "f": f,
            "x": x,
            "y": y,
            **odd_layer_action(r, e, f, x, y),
        }
        yield {
            "task": "even_layer_transition",
            "depth": r,
            "e": e,
            "f": f,
            "d": d,
            **even_layer_action(r, e, f, d),
        }

        ue, uf = (
            random_poly(rng, max_degree),
            random_poly(rng, max_degree),
        )
        yield {
            "task": "bracket_and_composition",
            "v": [e, f],
            "u": [ue, uf],
            "bracket_parameter": list(bracket_parameter((e, f), (ue, uf))),
            "ordered_mixed_parameter": list(
                leading_mixed_parameter((e, f), (ue, uf))
            ),
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--max-degree", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20261122)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.count < 0 or args.max_degree < 0:
        parser.error("count and max-degree must be nonnegative")
    if args.self_test:
        self_test()
    for row in generate(args.count, args.max_degree, args.seed):
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
