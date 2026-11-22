#!/usr/bin/env python3
"""Exact residue-feature dataset for rational differentials over GF(2)(S).

A sample is built from a monic irreducible Q and alpha in k_Q=GF(2)[S]/(Q):
    omega = alpha * Q'(S)/Q(S) dS.
It is encoded in Fold coordinates omega=(x/S)dS with
    x = S*alpha*Q'/Q.
The finite residue at Q is alpha; the residue at infinity is its field trace.
No floating point arithmetic or external packages are used.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Iterable


def degree(a: int) -> int:
    return a.bit_length() - 1


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


def mod(a: int, q: int) -> int:
    dq = degree(q)
    while a and degree(a) >= dq:
        a ^= q << (degree(a) - dq)
    return a


def mul_mod(a: int, b: int, q: int) -> int:
    return mod(mul(a, b), q)


def square_mod(a: int, q: int) -> int:
    return mul_mod(a, a, q)


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, mod(a, b)
    return a


def derivative(a: int) -> int:
    out = 0
    i = 1
    while (1 << i) <= a:
        if (a >> i) & 1 and (i & 1):
            out |= 1 << (i - 1)
        i += 1
    return out


def prime_divisors(n: int) -> list[int]:
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def is_irreducible(q: int) -> bool:
    """Rabin irreducibility test over GF(2), for monic q of positive degree."""
    n = degree(q)
    if n < 1:
        return False
    x = mod(0b10, q)
    for prime in prime_divisors(n):
        y = x
        for _ in range(n // prime):
            y = square_mod(y, q)
        if gcd(add(y, x), q) != 1:
            return False
    y = x
    for _ in range(n):
        y = square_mod(y, q)
    return y == x


def irreducibles(max_degree: int) -> list[int]:
    result = []
    for d in range(1, max_degree + 1):
        for q in range(1 << d, 1 << (d + 1)):
            if is_irreducible(q):
                result.append(q)
    return result


def field_trace(alpha: int, q: int) -> int:
    """Absolute trace GF(2^d) -> GF(2), represented as a polynomial bitmask."""
    d = degree(q)
    value = mod(alpha, q)
    trace = 0
    for _ in range(d):
        trace = add(trace, value)
        value = square_mod(value, q)
    if trace not in (0, 1):
        raise ArithmeticError("computed field trace did not land in GF(2)")
    return trace



def inverse_frobenius(alpha: int, j: int, q: int) -> int:
    """Apply Frob^(-j) in the finite field GF(2)[S]/(q)."""
    d = degree(q)
    steps = (-j) % d
    value = mod(alpha, q)
    for _ in range(steps):
        value = square_mod(value, q)
    return value


def orbit_residue(alphas: list[int], q: int) -> int:
    """Frobenius-normalized sum over an exponent-doubling orbit."""
    total = 0
    for j, alpha in enumerate(alphas):
        total = add(total, inverse_frobenius(alpha, j, q))
    return mod(total, q)


def orbit_sample(q: int, root_q: int, alphas: list[int]) -> dict:
    if root_q < 1 or root_q % 2 == 0:
        raise ValueError("orbit root must be a positive odd integer")
    d = degree(q)
    stages = [mod(a, q) for a in alphas]
    return {
        "task": "frobenius_orbit_residue",
        "Q_bits": q,
        "Q": poly_string(q),
        "residue_degree": d,
        "odd_root_q": root_q,
        "exponents": [-root_q * (1 << j) for j in range(len(stages))],
        "stage_residues": stages,
        "normalized_orbit_residue": orbit_residue(stages, q),
    }


def poly_string(a: int) -> str:
    if a == 0:
        return "0"
    terms = []
    i = 0
    while a:
        if a & 1:
            terms.append("1" if i == 0 else ("S" if i == 1 else f"S^{i}"))
        i += 1
        a >>= 1
    return " + ".join(reversed(terms))


def exact_div(a: int, b: int) -> int:
    quotient = 0
    while a and degree(a) >= degree(b):
        shift = degree(a) - degree(b)
        quotient |= 1 << shift
        a ^= b << shift
    if a:
        raise ArithmeticError("non-exact polynomial division")
    return quotient


def residue_sample(q: int, alpha: int) -> dict:
    """Return a coprime rational x=N/D with omega=(x/S)dS."""
    if not is_irreducible(q):
        raise ValueError("Q must be monic irreducible")
    d = degree(q)
    alpha = mod(alpha, q)
    if alpha == 0:
        raise ValueError("alpha must be nonzero")
    qprime = derivative(q)
    if mod(qprime, q) == 0:
        raise ArithmeticError("irreducible Q over GF(2) must be separable")

    # x = S*alpha*Q'/Q. Reduce the rational function.
    numerator = mul(mul(0b10, alpha), qprime)
    denominator = q
    common = gcd(numerator, denominator)
    numerator = exact_div(numerator, common)
    denominator = exact_div(denominator, common)
    if gcd(numerator, denominator) != 1:
        raise ArithmeticError("rational coefficient was not reduced")

    return {
        "task": "rational_differential_residue",
        "Q_bits": q,
        "Q": poly_string(q),
        "degree_Q": d,
        "alpha_bits": alpha,
        "alpha": poly_string(alpha),
        "numerator_bits": numerator,
        "denominator_bits": denominator,
        "finite_residue_bits": alpha,
        "infinity_residue_bits": field_trace(alpha, q),
    }


def self_test() -> None:
    qs = irreducibles(5)
    assert all(is_irreducible(q) for q in qs)
    assert 0b10 in qs                 # Q=S
    assert 0b11 in qs                 # Q=S+1
    assert 0b111 in qs                # Q=S^2+S+1

    tested = 0
    for q in qs:
        d = degree(q)
        qprime = derivative(q)
        assert gcd(q, qprime) == 1
        for j in range(d):
            alpha = 1 << j
            sample = residue_sample(q, alpha)
            n = sample["numerator_bits"]
            den = sample["denominator_bits"]
            assert gcd(n, den) == 1
            # The defining differential is alpha*Q'/Q dS, whose local
            # parameter is z=Q(S), so its residue at Q is alpha mod Q.
            assert sample["finite_residue_bits"] == alpha
            trace = field_trace(alpha, q)
            assert sample["infinity_residue_bits"] == trace
            tested += 1

    for q in qs:
        d = degree(q)
        for a in range(1 << d):
            for b in range(1 << d):
                assert field_trace(add(a, b), q) == add(
                    field_trace(a, q), field_trace(b, q)
                )

    # Frobenius-normalized orbit sums kill every adjacent Cartier relation:
    # alpha at stage j and alpha^2 at stage j+1.
    for q in qs:
        d = degree(q)
        for alpha in range(1 << d):
            for j in range(4):
                stages = [0] * (j + 2)
                stages[j] = alpha
                stages[j + 1] = square_mod(alpha, q)
                assert orbit_residue(stages, q) == 0
        # The normalized sum is additive and invariant after adding a
        # relation pair at any adjacent pair of stages.
        for alpha in range(1 << d):
            for beta in range(1 << d):
                base = [alpha, beta, 0, 0]
                augmented = base[:]
                augmented[1] = add(augmented[1], alpha)
                augmented[2] = add(augmented[2], square_mod(alpha, q))
                assert orbit_residue(base, q) == orbit_residue(augmented, q)
    print(
        f"self-test: {len(qs)} irreducibles and {tested} exact residue basis cases passed",
        file=sys.stderr,
    )


def generate(max_degree: int, samples_per_point: int, seed: int) -> Iterable[dict]:
    rng = random.Random(seed)
    for q in irreducibles(max_degree):
        d = degree(q)
        for _ in range(samples_per_point):
            alpha = rng.randrange(1, 1 << d)
            yield residue_sample(q, alpha)


def generate_orbits(
    max_degree: int, samples_per_point: int, max_stages: int, seed: int
) -> Iterable[dict]:
    rng = random.Random(seed ^ 0x5A17)
    roots = [1, 3, 5, 7, 9, 11, 13, 15]
    for q in irreducibles(max_degree):
        d = degree(q)
        for _ in range(samples_per_point):
            count = 1 + rng.randrange(max_stages)
            alphas = [rng.randrange(1 << d) for _ in range(count)]
            root_q = roots[rng.randrange(len(roots))]
            yield orbit_sample(q, root_q, alphas)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-degree", type=int, default=5)
    parser.add_argument("--samples-per-point", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--orbit-samples", type=int, default=0,
                        help="also emit this many Frobenius-orbit samples per irreducible")
    parser.add_argument("--max-orbit-stages", type=int, default=5)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.max_degree < 1 or args.samples_per_point < 1:
        parser.error("max-degree and samples-per-point must be positive")
    if args.orbit_samples < 0 or args.max_orbit_stages < 1:
        parser.error("orbit-samples must be nonnegative and max-orbit-stages positive")
    if args.self_test:
        self_test()
    for row in generate(args.max_degree, args.samples_per_point, args.seed):
        print(json.dumps(row, sort_keys=True))
    if args.orbit_samples:
        for row in generate_orbits(
            args.max_degree, args.orbit_samples,
            args.max_orbit_stages, args.seed
        ):
            print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
