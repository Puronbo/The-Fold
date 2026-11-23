#!/usr/bin/env python3
"""Exact residue-field data for Cartier classes over F_2(S).

Polynomial and residue-field elements are encoded as bitmasks. This script
builds rational differential examples a(S)/Q(S) dS, computes their closed-
point residue in F_2[S]/(Q), the forced residue at infinity, and the Cartier
inverse-Frobenius orbit. It uses only the Python standard library.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Iterable


def degree(poly: int) -> int:
    return poly.bit_length() - 1


def poly_add(a: int, b: int) -> int:
    return a ^ b


def poly_mul(a: int, b: int) -> int:
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def poly_divmod(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        raise ZeroDivisionError("polynomial division by zero")
    q = 0
    db = degree(b)
    while a and degree(a) >= db:
        shift = degree(a) - db
        q ^= 1 << shift
        a ^= b << shift
    return q, a


def poly_mod(a: int, modulus: int) -> int:
    return poly_divmod(a, modulus)[1]


def poly_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, poly_mod(a, b)
    return a


def poly_inverse_mod(a: int, modulus: int) -> int:
    """Extended Euclidean inverse in GF(2)[S]/(modulus)."""
    r0, r1 = modulus, poly_mod(a, modulus)
    t0, t1 = 0, 1
    while r1:
        q, r = poly_divmod(r0, r1)
        r0, r1 = r1, r
        t0, t1 = t1, poly_add(t0, poly_mul(q, t1))
    if r0 != 1:
        raise ZeroDivisionError("element is not invertible modulo modulus")
    return poly_mod(t0, modulus)


def poly_mul_mod(a: int, b: int, modulus: int) -> int:
    return poly_mod(poly_mul(a, b), modulus)


def poly_square_mod(a: int, modulus: int) -> int:
    return poly_mul_mod(a, a, modulus)


def derivative(poly: int) -> int:
    """Formal derivative in characteristic two."""
    out = 0
    i = 1
    while (1 << i) <= poly:
        if (poly >> i) & 1 and (i & 1):
            out |= 1 << (i - 1)
        i += 1
    return out


def is_irreducible(poly: int) -> bool:
    d = degree(poly)
    if d < 1 or not (poly & (1 << d)):
        return False
    for divisor_degree in range(1, d // 2 + 1):
        first = 1 << divisor_degree
        stop = 1 << (divisor_degree + 1)
        for divisor in range(first, stop):
            if degree(divisor) == divisor_degree and poly_mod(poly, divisor) == 0:
                return False
    return True


def irreducibles(max_degree: int) -> list[int]:
    result = []
    for d in range(1, max_degree + 1):
        for poly in range(1 << d, 1 << (d + 1)):
            if is_irreducible(poly):
                result.append(poly)
    return result


def field_frobenius(a: int, modulus: int) -> int:
    return poly_square_mod(a, modulus)


def inverse_frobenius(a: int, modulus: int) -> int:
    """Square root in the finite field F_(2^d), d=deg(modulus)."""
    d = degree(modulus)
    out = poly_mod(a, modulus)
    for _ in range(max(0, d - 1)):
        out = field_frobenius(out, modulus)
    assert field_frobenius(out, modulus) == poly_mod(a, modulus)
    return out


def field_trace(a: int, modulus: int) -> int:
    """Absolute trace F_(2^d) -> F_2, returned as bit 0 or 1."""
    d = degree(modulus)
    cur = poly_mod(a, modulus)
    total = 0
    for _ in range(d):
        total ^= cur
        cur = field_frobenius(cur, modulus)
    if total not in (0, 1):
        raise AssertionError("finite-field trace did not land in F_2")
    return total


def cartier_residue_cycle(a: int, modulus: int) -> list[int]:
    """Cartier acts on residues by inverse Frobenius."""
    cur = poly_mod(a, modulus)
    if cur == 0:
        return [0]
    cycle = []
    seen = set()
    while cur not in seen:
        seen.add(cur)
        cycle.append(cur)
        cur = inverse_frobenius(cur, modulus)
    if cur != cycle[0]:
        raise AssertionError("unexpected preperiod in finite-field Frobenius orbit")
    return cycle


def residue_example(modulus: int, residue: int) -> dict:
    """Construct omega = a(S)/Q(S) dS with prescribed residue at Q."""
    d = degree(modulus)
    qprime = derivative(modulus)
    if qprime == 0 or poly_gcd(qprime, modulus) != 1:
        raise ValueError("irreducible polynomial must be separable")
    residue = poly_mod(residue, modulus)
    numerator = poly_mul_mod(residue, poly_inverse_mod(qprime, modulus), modulus)
    recovered = poly_mul_mod(numerator, qprime, modulus)
    assert recovered == residue

    infinity_residue = field_trace(residue, modulus)
    cycle = cartier_residue_cycle(residue, modulus)
    return {
        "task": "closed_point_residue",
        "Q": modulus,
        "degree": d,
        "residue_field_element": residue,
        "differential_numerator": numerator,
        "differential_denominator": modulus,
        "differential": "a(S)/Q(S) dS",
        "infinity_residue": infinity_residue,
        "global_trace_sum": poly_add(field_trace(residue, modulus), infinity_residue),
        "cartier_inverse_frobenius_cycle": cycle,
        "cartier_nonnilpotent": residue != 0,
        "tower_coordinate_x_numerator": poly_mul(0b10, numerator),
        "tower_coordinate_x_denominator": modulus,
    }


def random_configuration(
    polynomials: list[int], rng: random.Random
) -> dict:
    points = []
    total_trace = 0
    for q in polynomials:
        d = degree(q)
        residue = rng.randrange(1 << d)
        trace = field_trace(residue, q)
        points.append({"Q": q, "residue": residue, "trace": trace})
        total_trace ^= trace
    return {
        "task": "global_residue_configuration",
        "finite_residues": points,
        "infinity_residue": total_trace,
        "global_trace_sum": total_trace ^ total_trace,
    }


def self_test() -> None:
    expected = {
        1: {0b10, 0b11},
        2: {0b111},
        3: {0b1011, 0b1101},
    }
    for d, polys in expected.items():
        got = {q for q in irreducibles(d) if degree(q) == d}
        assert got == polys, (d, got, polys)

    for q in irreducibles(6):
        d = degree(q)
        qprime = derivative(q)
        assert qprime != 0
        assert poly_gcd(qprime, q) == 1
        for residue in range(1 << d):
            root = inverse_frobenius(residue, q)
            assert field_frobenius(root, q) == residue
            trace = field_trace(residue, q)
            assert trace in (0, 1)
            example = residue_example(q, residue)
            assert example["global_trace_sum"] == 0
            assert example["cartier_nonnilpotent"] == (residue != 0)
            cycle = example["cartier_inverse_frobenius_cycle"]
            if residue:
                assert all(item != 0 for item in cycle)
            else:
                assert cycle == [0]

    q = 0b11  # S+1
    witness = residue_example(q, 1)
    assert witness["differential_numerator"] == 1
    assert witness["infinity_residue"] == 1
    assert witness["cartier_inverse_frobenius_cycle"] == [1]

    q = 0b111  # S^2+S+1, residue field F_4
    witness = residue_example(q, 0b10)
    assert witness["infinity_residue"] == 1  # Tr_{F_4/F_2}(S)=1


def generate(count: int, max_degree: int, seed: int) -> Iterable[dict]:
    rng = random.Random(seed)
    qs = irreducibles(max_degree)
    if not qs:
        return
    for _ in range(count):
        q = rng.choice(qs)
        d = degree(q)
        residue = rng.randrange(1 << d)
        yield residue_example(q, residue)
    yield random_configuration(qs, rng)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=500)
    parser.add_argument("--max-degree", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.count < 0 or args.max_degree < 1:
        parser.error("count must be nonnegative and max-degree at least one")
    if args.self_test:
        self_test()
        print("residue self-test: finite-field and global trace checks passed", file=sys.stderr)
    for row in generate(args.count, args.max_degree, args.seed):
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
