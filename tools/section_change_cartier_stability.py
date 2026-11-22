#!/usr/bin/env python3
"""Exact truncated pullback tests for the section-change Cartier tower.

Uses cartier_stable_part.py for rational arithmetic over GF(2)(S).
The q-series variable q represents p^(2r), and only exact rational
coefficients are used. The first two pullback coefficients are theorem
checks; higher Cartier-torsion bounds are explicitly exploratory.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Iterable

from cartier_stable_part import (
    S, c0, c1, irreducibles, padd, pmul, radd, rderiv, rmul,
    rnorm, rsquare,
)

Rat = tuple[int, int]
Series = list[Rat]
ZERO: Rat = (0, 1)
ONE: Rat = (1, 1)
S_RAT: Rat = (S, 1)


def rdiv(x: Rat, y: Rat) -> Rat:
    if y[0] == 0:
        raise ZeroDivisionError("rational-function division by zero")
    return rmul(x, (y[1], y[0]))


def s_add(a: Series, b: Series) -> Series:
    return [radd(x, y) for x, y in zip(a, b)]


def s_mul(a: Series, b: Series, order: int) -> Series:
    out = [ZERO for _ in range(order)]
    for i, x in enumerate(a[:order]):
        for j, y in enumerate(b[:order - i]):
            out[i + j] = radd(out[i + j], rmul(x, y))
    return out


def s_inv(a: Series, order: int) -> Series:
    if not a or a[0][0] == 0:
        raise ZeroDivisionError("series has zero constant coefficient")
    out = [ZERO for _ in range(order)]
    out[0] = (a[0][1], a[0][0])
    for n in range(1, order):
        value = ZERO
        for i in range(1, n + 1):
            value = radd(value, rmul(a[i], out[n - i]))
        out[n] = rdiv(value, a[0])
    return out


def s_pow(a: Series, exponent: int, order: int) -> Series:
    out = [ONE] + [ZERO for _ in range(order - 1)]
    base = a[:order]
    n = exponent
    while n:
        if n & 1:
            out = s_mul(out, base, order)
        base = s_mul(base, base, order)
        n >>= 1
    return out


def poly_eval_series(poly: int, base: Series, order: int) -> Series:
    """Evaluate a GF(2)[S] bitmask polynomial at a q-series base."""
    out = [ZERO for _ in range(order)]
    for degree in range(poly.bit_length()):
        if (poly >> degree) & 1:
            term = s_pow(base, degree, order)
            out = s_add(out, term)
    return out


def rational_substitution(a: Rat, base: Series, order: int) -> Series:
    numerator = poly_eval_series(a[0], base, order)
    denominator = poly_eval_series(a[1], base, order)
    return s_mul(numerator, s_inv(denominator, order), order)


def s_square(a: Series, order: int) -> Series:
    """Frobenius square: q^i coefficients move to q^(2i)."""
    out = [ZERO for _ in range(order)]
    for i, coefficient in enumerate(a):
        if 2 * i < order:
            out[2 * i] = rsquare(coefficient)
    return out


def pullback_first_coordinate(
    a: Rat, e: Rat, f: Rat, order: int
) -> tuple[Series, Rat]:
    r"""For s=t(1+p^r(e+ft)), q=p^(2r):
       S_new = S(1+q(e^2+S f^2)),
       A'_0 = a(S_new)^2 (1+q e^2)/(1+q(e^2+S f^2)).
    Returns A'_0-a^2 and u=e^2+S f^2.
    """
    u = radd(rsquare(e), rmul(S_RAT, rsquare(f)))
    base = [S_RAT, rmul(S_RAT, u)] + [ZERO for _ in range(order - 2)]
    b = rational_substitution(a, base, order)
    numerator = [ONE, rsquare(e)] + [ZERO for _ in range(order - 2)]
    denominator = [ONE, u] + [ZERO for _ in range(order - 2)]
    kappa = s_mul(numerator, s_inv(denominator, order), order)
    transformed = s_mul(s_square(b, order), kappa, order)
    transformed[0] = radd(transformed[0], rsquare(a))
    return transformed, u


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 is defined here for positive integers")
    return (n & -n).bit_length() - 1


def c0_torsion_index(x: Rat, limit: int = 32) -> int | None:
    current = x
    for step in range(1, limit + 1):
        current = c0(current)
        if current == ZERO:
            return step
    return None


def random_rational(rng: random.Random, max_degree: int, qs: list[int]) -> Rat:
    numerator = rng.randrange(1 << (max_degree + 1))
    denominator = 1
    if rng.randrange(4):
        q = rng.choice(qs)
        exponent = 1 + rng.randrange(3)
        denominator = 1
        base = q
        n = exponent
        while n:
            if n & 1:
                denominator = pmul(denominator, base)
            base = pmul(base, base)
            n >>= 1
    return rnorm(numerator, denominator)


def self_test(
    samples: int, max_degree: int, max_q_degree: int, order: int, seed: int
) -> None:
    rng = random.Random(seed)
    qs = irreducibles(max_q_degree)
    if not qs:
        raise ValueError("max_q_degree must include at least one irreducible")
    for _ in range(samples):
        a = random_rational(rng, max_degree, qs)
        e = random_rational(rng, max_degree, qs)
        f = random_rational(rng, max_degree, qs)
        delta, u = pullback_first_coordinate(a, e, f, order)

        # Exact q and q^2 identities.
        expected_q = rmul(rmul(S_RAT, rsquare(f)), rsquare(a))
        assert delta[1] == expected_q

        expected_q2 = radd(
            rsquare(rmul(rmul(S_RAT, u), rderiv(a))),
            rmul(rmul(S_RAT, rsquare(f)), rmul(u, rsquare(a))),
        )
        assert delta[2] == expected_q2

        # p-basis proof check: C0(delta_2)=S(e*a1+f*a0)^2, then zero.
        a0, a1 = c0(a), c1(a)
        root = rmul(
            S_RAT,
            rsquare(radd(rmul(e, a1), rmul(f, a0))),
        )
        assert c0(delta[2]) == root
        assert c0(root) == ZERO
        assert c0(delta[1]) == ZERO

        # Exploratory higher-order bound; recorded separately from theorem checks.
        for m in range(1, order):
            current = delta[m]
            for _step in range(v2(m) + 1):
                current = c0(current)
            assert current == ZERO, (
                "higher-order torsion bound counterexample",
                m, a, e, f, delta[m], current,
            )

    print(
        f"self-test: {samples} exact rational pullbacks; q,q^2 identities "
        f"and exploratory v2-torsion bounds through q^{order - 1} passed",
        file=sys.stderr,
    )


def generate(
    count: int, max_degree: int, max_q_degree: int, order: int, seed: int
) -> Iterable[dict]:
    rng = random.Random(seed)
    qs = irreducibles(max_q_degree)
    if not qs:
        raise ValueError("max_q_degree must include at least one irreducible")
    for _ in range(count):
        a = random_rational(rng, max_degree, qs)
        e = random_rational(rng, max_degree, qs)
        f = random_rational(rng, max_degree, qs)
        delta, _u = pullback_first_coordinate(a, e, f, order)
        torsion = [
            c0_torsion_index(delta[m], max(32, 2 * order))
            for m in range(1, order)
        ]
        yield {
            "task": "section_change_cartier_tower",
            "a": list(a),
            "e": list(e),
            "f": list(f),
            "q_coefficients": [list(x) for x in delta[1:]],
            "C0_torsion_indices": torsion,
            "suggested_bound": [v2(m) + 1 for m in range(1, order)],
            "labels_scope": "exact truncated pullback; higher torsion bound is exploratory",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--samples", type=int, default=12)
    parser.add_argument("--max-degree", type=int, default=4)
    parser.add_argument("--max-q-degree", type=int, default=3)
    parser.add_argument("--order", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if min(args.count, args.samples, args.max_degree, args.order) < 0:
        parser.error("count, samples, degree and order must be nonnegative")
    if args.order < 3 or args.max_q_degree < 1:
        parser.error("order must be at least 3 and max-q-degree at least 1")
    if args.self_test:
        self_test(
            args.samples, args.max_degree, args.max_q_degree, args.order, args.seed
        )
    for row in generate(
        args.count, args.max_degree, args.max_q_degree, args.order, args.seed
    ):
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
