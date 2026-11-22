#!/usr/bin/env python3
"""Exact p-basis root operator on F_2(S) and its stable simple-pole part.

A rational function is a pair of GF(2)[S] polynomials (N,D), encoded
as bitmasks. The operator C0 is defined by the unique decomposition
f = a0^2 + S*a1^2, with C0(f)=a0. It is additive, surjective, and
ker(C0)=S*F^2. No floating-point arithmetic is used.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Iterable

S = 0b10


def padd(a: int, b: int) -> int:
    return a ^ b


def pmul(a: int, b: int) -> int:
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def pdivmod(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        raise ZeroDivisionError("polynomial division by zero")
    q, r = 0, a
    db = b.bit_length() - 1
    while r and r.bit_length() - 1 >= db:
        shift = r.bit_length() - 1 - db
        q ^= 1 << shift
        r ^= b << shift
    return q, r


def pgcd(a: int, b: int) -> int:
    while b:
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def pdivexact(a: int, b: int) -> int:
    q, r = pdivmod(a, b)
    if r:
        raise ArithmeticError("inexact polynomial division")
    return q


def pderiv(a: int) -> int:
    out = 0
    for i in range(1, a.bit_length()):
        if (a >> i) & 1 and (i & 1):
            out |= 1 << (i - 1)
    return out


def p_split(a: int) -> tuple[int, int]:
    """Unique a=A^2+S*B^2; return (A,B)."""
    even = odd = 0
    for i in range(a.bit_length()):
        if (a >> i) & 1:
            if i & 1:
                odd |= 1 << ((i - 1) // 2)
            else:
                even |= 1 << (i // 2)
    return even, odd


Rat = tuple[int, int]  # numerator, denominator; denominator is monic/nonzero


def rnorm(n: int, d: int) -> Rat:
    if d == 0:
        raise ZeroDivisionError("zero rational denominator")
    if n == 0:
        return (0, 1)
    g = pgcd(n, d)
    return (pdivexact(n, g), pdivexact(d, g))


def radd(x: Rat, y: Rat) -> Rat:
    n1, d1 = x
    n2, d2 = y
    return rnorm(padd(pmul(n1, d2), pmul(n2, d1)), pmul(d1, d2))


def rmul(x: Rat, y: Rat) -> Rat:
    return rnorm(pmul(x[0], y[0]), pmul(x[1], y[1]))


def rsquare(x: Rat) -> Rat:
    return rnorm(pmul(x[0], x[0]), pmul(x[1], x[1]))


def rderiv(x: Rat) -> Rat:
    n, d = x
    return rnorm(
        padd(pmul(pderiv(n), d), pmul(n, pderiv(d))),
        pmul(d, d),
    )


def c0(x: Rat) -> Rat:
    """Return a0 from x=a0^2+S*a1^2, using x=N/D."""
    n, d = x
    a0, _a1 = p_split(pmul(n, d))
    return rnorm(a0, d)


def c1(x: Rat) -> Rat:
    """Return a1 from x=a0^2+S*a1^2, using x=N/D."""
    n, d = x
    _a0, a1 = p_split(pmul(n, d))
    return rnorm(a1, d)


def p_irreducible(q: int) -> bool:
    if q <= 1:
        return False
    degree = q.bit_length() - 1
    if degree == 1:
        return True
    for d in range(1, degree // 2 + 1):
        for candidate in range(1 << d, 1 << (d + 1)):
            if pdivmod(q, candidate)[1] == 0:
                return False
    return True


def irreducibles(max_degree: int) -> list[int]:
    return [
        q
        for degree in range(1, max_degree + 1)
        for q in range(1 << degree, 1 << (degree + 1))
        if p_irreducible(q)
    ]


def rank_f2(columns: list[int]) -> int:
    pivots: dict[int, int] = {}
    for col in columns:
        value = col
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def simple_pole_rank(q: int) -> int:
    degree = q.bit_length() - 1
    columns = []
    for i in range(degree):
        out = c0((1 << i, q))
        numerator, denominator = out
        if denominator != q:
            return -1
        _, remainder = pdivmod(numerator, q)
        columns.append(remainder)
    return rank_f2(columns)


def divides(a: int, b: int) -> bool:
    return pdivmod(a, b)[1] == 0


def c0_iterates(x: Rat, count: int) -> list[Rat]:
    values = [x]
    for _ in range(count):
        values.append(c0(values[-1]))
    return values


def random_poly(rng: random.Random, max_degree: int) -> int:
    return rng.randrange(1 << (max_degree + 1))


def self_test(max_q_degree: int, max_pole_order: int) -> None:
    qs = irreducibles(max_q_degree)
    assert S in qs

    samples: list[Rat] = [
        (1, 1),
        (S, 1),
        (1, S),
        (1, 0b11),       # 1/(S+1), fixed by C0
        (1, 0b111),      # simple pole at an irreducible quadratic
        (1, 0b1011),     # simple pole at an irreducible cubic
        (S, 0b101),      # S/(S^2+1)
    ]

    # The p-basis decomposition and the differential identity:
    # C0(f)^2 = f + S*f'.
    for x in samples:
        a0, a1 = c0(x), c1(x)
        assert radd(rsquare(a0), rmul((S, 1), rsquare(a1))) == x
        rhs = radd(x, rmul((S, 1), rderiv(x)))
        assert rsquare(a0) == rhs
        assert c0(radd(x, x)) == (0, 1)
        assert c0(radd(x, samples[0])) == radd(c0(x), c0(samples[0]))

    # C0 is surjective: C0(g^2)=g.
    for x in samples:
        assert c0(rsquare(x)) == x

    # On simple-pole coefficients, C0 is invertible for Q != S,
    # and is zero for Q=S.
    for q in qs:
        rank = simple_pole_rank(q)
        degree = q.bit_length() - 1
        if q == S:
            assert rank == 0
        else:
            assert rank == degree

    # A Q-adic pole of order m is reduced to order <=ceil(m/2).
    # The denominator of C0(P/Q^m) therefore divides Q^ceil(m/2).
    for q in qs:
        degree = q.bit_length() - 1
        for m in range(1, max_pole_order + 1):
            bound = 1
            for _ in range((m + 1) // 2):
                bound = pmul(bound, q)
            # Deterministic nonzero numerator samples at all small degrees.
            for numerator in range(1, min(1 << (degree * m), 96)):
                out = c0((numerator, _poly_power(q, m)))
                assert divides(bound, out[1])

    # Representative stable/nonstable examples.
    assert c0((1, S)) == (0, 1)
    assert c0((1, 0b11)) == (1, 0b11)
    assert c0((1, 0b111)) != (0, 1)
    print(
        f"self-test: C0 identities, surjectivity, simple-pole ranks, "
        f"and pole contraction passed for Q degrees <= {max_q_degree}",
        file=sys.stderr,
    )


def _poly_power(base: int, exponent: int) -> int:
    out = 1
    while exponent:
        if exponent & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        exponent >>= 1
    return out


def generate(count: int, max_degree: int, max_q_degree: int, seed: int) -> Iterable[dict]:
    rng = random.Random(seed)
    qs = irreducibles(max_q_degree)
    for _ in range(count):
        q = rng.choice(qs)
        degree = q.bit_length() - 1
        pole_order = 1 + rng.randrange(6)
        numerator = random_poly(rng, max(0, degree * pole_order - 1))
        denominator = _poly_power(q, pole_order)
        x = rnorm(numerator, denominator)
        orbit = c0_iterates(x, 5)
        yield {
            "task": "p_basis_root_orbit",
            "Q": q,
            "Q_degree": degree,
            "pole_order": pole_order,
            "input": list(x),
            "C0_iterates": [list(z) for z in orbit],
            "C0_simple_pole_rank": simple_pole_rank(q),
            "Q_is_S": q == S,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--max-degree", type=int, default=5)
    parser.add_argument("--max-q-degree", type=int, default=5)
    parser.add_argument("--max-pole-order", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if min(args.count, args.max_degree, args.max_q_degree, args.max_pole_order) < 0:
        parser.error("count and degree bounds must be nonnegative")
    if args.self_test:
        self_test(args.max_q_degree, args.max_pole_order)
    for row in generate(args.count, args.max_degree, args.max_q_degree, args.seed):
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
