#!/usr/bin/env python3
"""Exact GF(2)[S] data generator for the Fold section-change action.

Polynomials are encoded as nonnegative integers: bit i is the coefficient
of S**i. The script emits certified first/second-diagonal, pure-scaling
Hasse/Frobenius, and bracket/composition targets. It does not guess
higher quotient maps or claim coverage of rational denominators.
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
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def square(a: int) -> int:
    """Frobenius square in GF(2)[S]."""
    out = 0
    i = 0
    while a:
        if a & 1:
            out |= 1 << (2 * i)
        i += 1
        a >>= 1
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



def frobenius_power(a: int, h: int) -> int:
    """Return a^(2^h) in GF(2)[S]."""
    for _ in range(h):
        a = square(a)
    return a


def binomial_odd(n: int, k: int) -> bool:
    """Lucas' theorem: binomial(n,k) is odd iff k's bits are in n."""
    return (n & k) == k


def scaling_hasse_coefficient(x: int, j: int) -> int:
    r"""Coefficient of q^j in x(S/(1+q)) over GF(2)[S].

    For a monomial S^d the coefficient is
      binomial(d+j-1,j) S^d,
    with the constant monomial contributing zero for j>0.
    """
    if j < 1:
        raise ValueError("j must be positive")
    out = 0
    degree = 0
    while (1 << degree) <= x:
        if (x >> degree) & 1 and binomial_odd(degree + j - 1, j):
            out |= 1 << degree
        degree += 1
    return out


def max_frobenius_depth_polynomial(x: int) -> int | None:
    """Largest h with x in GF(2)[S]^(2^h); None for constants."""
    if x == 0 or x == 1:
        return None
    depth = 10**9
    degree = 0
    while (1 << degree) <= x:
        if (x >> degree) & 1 and degree:
            depth = min(depth, (degree & -degree).bit_length() - 1)
        degree += 1
    return depth if depth != 10**9 else None


def square_root_polynomial(a: int) -> int:
    """Return the polynomial square root, raising if a is not a square."""
    out = 0
    i = 0
    while a:
        if a & 1:
            if i & 1:
                raise AssertionError("polynomial is not a square")
            out |= 1 << (i // 2)
        i += 1
        a >>= 1
    return out


def scaling_leading_term(a: int, h: int, e: int = 1) -> int:
    """Leading coefficient of a^(2^h)(S/(1+q*e^2))-a^(2^h)(S).

    The first possible term is q^(2^h) (S*e^2*a')^(2^h).
    """
    return frobenius_power(mul(mul(S, square(e)), derivative(a)), h)


def p_basis_decompose(a: int) -> tuple[int, int]:
    """Return (a0,a1) with a = a0**2 + S*a1**2 uniquely."""
    a0 = 0
    a1 = 0
    i = 0
    while a:
        if a & 1:
            if i & 1:
                a1 |= 1 << ((i - 1) // 2)
            else:
                a0 |= 1 << (i // 2)
        i += 1
        a >>= 1
    return a0, a1


def odd_layer_raw(r: int, e: int, f: int, x: int, y: int):
    """Raw p^r correction for odd representative (x,t*y)."""
    eps = r & 1
    delta_a = (0, mul(f, x))
    delta_b = (
        add(mul(S, mul(f, y)), mul(eps, mul(e, x))),
        add(mul(e, y), mul(eps, mul(f, x))),
    )
    return delta_a, delta_b


def odd_layer_action(r: int, e: int, f: int, x: int, y: int):
    da, db = odd_layer_raw(r, e, f, x, y)
    if r & 1:
        return {"target_type": "Q_even", "target": db[1]}
    return {
        "target_type": "Q_odd",
        "target": [da[0], add(da[1], db[1])],
    }


def even_layer_raw(e: int, f: int, d: int):
    """Raw correction for even representative (0,t*d)."""
    return (0, 0), (mul(S, mul(f, d)), mul(e, d))


def even_layer_action(r: int, e: int, f: int, d: int):
    da, db = even_layer_raw(e, f, d)
    if r & 1:
        return {"target_type": "Q_odd", "target": [0, mul(e, d)]}
    return {"target_type": "Q_even", "target": mul(e, d)}


def second_odd_diagonal(e: int, f: int, x: int, y: int):
    """Correct p^(2r) diagonal on an odd layer.

    If x=a^2+S*b^2 and y=c^2+S*d^2, then
      N_odd(x,y) = (S*(f*a+e*b)^2, (e*c)^2+(S*f*d)^2).
    """
    a, b = p_basis_decompose(x)
    c, d = p_basis_decompose(y)
    first = mul(S, square(add(mul(f, a), mul(e, b))))
    second = add(square(mul(e, c)), square(mul(S, mul(f, d))))
    return first, second


def second_even_diagonal(e: int, f: int, d: int) -> int:
    """Correct p^(2r) diagonal on an even layer."""
    a, b = p_basis_decompose(d)
    return add(square(mul(e, a)), square(mul(S, mul(f, b))))


def bracket_parameter(v: tuple[int, int], u: tuple[int, int]):
    """Parameter of [X_v,X_u]=X_{t(e_v*f_u+e_u*f_v)}."""
    ev, fv = v
    eu, fu = u
    return (0, add(mul(ev, fu), mul(eu, fv)))


def leading_mixed_parameter(v: tuple[int, int], u: tuple[int, int]):
    """Mixed coefficient e_u*v for the specified G-4cc composition order."""
    ev, fv = v
    eu, _fu = u
    return (mul(eu, ev), mul(eu, fv))


def random_poly(rng: random.Random, max_degree: int) -> int:
    return rng.randrange(1 << (max_degree + 1))

def self_test() -> None:
    values = [0, 1, S, 1 ^ S, 1 ^ (1 << 2), 1 ^ S ^ (1 << 3)]

    # Unique p-basis decomposition and derivative extraction.
    for x in values:
        a, b = p_basis_decompose(x)
        assert x == add(square(a), mul(S, square(b)))
        assert derivative(x) == square(b)

    # Exact first-diagonal projections in both parity cases.
    for r in (1, 2, 3, 4):
        for e in values:
            for f in values:
                for x in values:
                    for y in values:
                        got = odd_layer_action(r, e, f, x, y)
                        value = add(mul(f, x), mul(e, y))
                        if r & 1:
                            assert got == {"target_type": "Q_even", "target": value}
                        else:
                            assert got == {"target_type": "Q_odd", "target": [0, value]}
                for d in values:
                    got = even_layer_action(r, e, f, d)
                    if r & 1:
                        assert got == {"target_type": "Q_odd", "target": [0, mul(e, d)]}
                    else:
                        assert got == {"target_type": "Q_even", "target": mul(e, d)}

    # Second diagonal and its image description.
    for e in values:
        for f in values:
            for x in values:
                for y in values:
                    first, second = second_odd_diagonal(e, f, x, y)
                    a, b = p_basis_decompose(x)
                    c, d = p_basis_decompose(y)
                    assert first == mul(S, square(add(mul(f, a), mul(e, b))))
                    assert second == add(square(mul(e, c)), square(mul(S, mul(f, d))))
                    assert first % 2 == 0  # divisible by S
                    square_root_polynomial(second)  # second component is a square
            for d in values:
                square_root_polynomial(second_even_diagonal(e, f, d))

    # The odd first-coordinate image is exactly S*F^2 on polynomials.
    for b in values:
        first, _ = second_odd_diagonal(1, 0, mul(S, square(b)), 0)
        assert first == mul(S, square(b))

    # Hasse coefficients of the pure-scaling substitution.
    for h in range(5):
        j = 1 << h
        for a in values:
            x = frobenius_power(a, h)
            observed = scaling_hasse_coefficient(x, j)
            predicted = scaling_leading_term(a, h)
            assert observed == predicted, (h, a, observed, predicted)
        for a in values:
            x = frobenius_power(a, h)
            depth = max_frobenius_depth_polynomial(x)
            if a not in (0, 1):
                assert depth is not None and depth >= h
        for a in values:
            x = frobenius_power(a | S, h)
            assert max_frobenius_depth_polynomial(x) == h

    # Every nonzero leading parameter is detected by the corrected first arrow.
    for e in values:
        for f in values:
            if e == 0 and f == 0:
                continue
            x, y = (1, 0) if f else (0, 1)
            for r in (1, 2, 3, 4):
                target = odd_layer_action(r, e, f, x, y)["target"]
                assert target != 0 and target != [0, 0]

    for v in [(e, f) for e in values for f in values]:
        assert bracket_parameter(v, v) == (0, 0)
    for v, u in [((1, 0), (0, 1)), ((S, 1), (1, S))]:
        assert bracket_parameter(v, u) != (0, 0)


def generate(count: int, max_degree: int, seed: int) -> Iterable[dict]:
    rng = random.Random(seed)
    for _ in range(count):
        r = 1 + rng.randrange(8)
        e, f, x, y, d = (random_poly(rng, max_degree) for _ in range(5))
        yield {
            "task": "odd_layer_transition", "depth": r,
            "e": e, "f": f, "x": x, "y": y,
            **odd_layer_action(r, e, f, x, y),
        }
        yield {
            "task": "even_layer_transition", "depth": r,
            "e": e, "f": f, "d": d,
            **even_layer_action(r, e, f, d),
        }
        n1, n2 = second_odd_diagonal(e, f, x, y)
        yield {
            "task": "second_odd_diagonal", "e": e, "f": f,
            "x": x, "y": y, "target": [n1, n2],
        }
        yield {
            "task": "second_even_diagonal", "e": e, "f": f,
            "d": d, "target": second_even_diagonal(e, f, d),
        }
        h = rng.randrange(5)
        # The S term guarantees a is not a square, so h is the exact
        # Frobenius depth of x_scale rather than merely a chosen root level.
        a = random_poly(rng, max_degree) | S
        e_scale = 1
        x_scale = frobenius_power(a, h)
        assert max_frobenius_depth_polynomial(x_scale) == h
        yield {
            "task": "pure_scaling_frobenius_tower",
            "frobenius_level": h,
            "source_polynomial": a,
            "coefficient": x_scale,
            "first_nonzero_depth_for_r1": 1 << (h + 1),
            "leading_coefficient": scaling_leading_term(a, h, e_scale),
        }
        ue, uf = random_poly(rng, max_degree), random_poly(rng, max_degree)
        yield {
            "task": "bracket_and_composition", "v": [e, f], "u": [ue, uf],
            "bracket_parameter": list(bracket_parameter((e, f), (ue, uf))),
            "ordered_mixed_parameter": list(leading_mixed_parameter((e, f), (ue, uf))),
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
        print("self-test: all exact GF(2)[S] checks passed", file=sys.stderr)
    for row in generate(args.count, args.max_degree, args.seed):
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
