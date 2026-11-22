#!/usr/bin/env python3
"""Finite exact basis/dual-coordinate benchmark for the Fold coinvariant.

The full algebraic coinvariant is
  F/wp(F) + sum_{q odd>0} sum_Q GF(2)[S]/(Q),
with F=GF(2)(S), Q monic irreducible.

This script emits finite cutoffs:
  * zero-mode Artin-Schreier basis elements of height <= H;
  * residue basis elements for odd roots q <= q_max and deg(Q) <= d_max;
  * trace-dual readout coefficients for each finite residue-field basis.

All arithmetic is exact over GF(2); no external packages are required.
A finite cutoff is a benchmark window, not a replacement for the infinite
algebraic direct sum or its unrestricted algebraic dual.
"""
from __future__ import annotations

import argparse
import json
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


def exact_div(a: int, b: int) -> int:
    quotient = 0
    while a and degree(a) >= degree(b):
        shift = degree(a) - degree(b)
        quotient |= 1 << shift
        a ^= b << shift
    if a:
        raise ArithmeticError("polynomial division was not exact")
    return quotient


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, mod(a, b)
    return a


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
    """Rabin irreducibility test for monic polynomials over GF(2)."""
    n = degree(q)
    if n < 1:
        return False
    x = mod(0b10, q)
    for ell in prime_divisors(n):
        y = x
        for _ in range(n // ell):
            y = square_mod(y, q)
        if gcd(add(y, x), q) != 1:
            return False
    y = x
    for _ in range(n):
        y = square_mod(y, q)
    return y == x


def irreducibles(max_degree: int) -> list[int]:
    return [
        q
        for d in range(1, max_degree + 1)
        for q in range(1 << d, 1 << (d + 1))
        if is_irreducible(q)
    ]


def field_trace(a: int, q: int) -> int:
    d = degree(q)
    value = mod(a, q)
    result = 0
    for _ in range(d):
        result ^= value
        value = square_mod(value, q)
    if result not in (0, 1):
        raise ArithmeticError("trace did not land in GF(2)")
    return result


def trace_dual_basis(q: int) -> list[int]:
    """Return c_i with Tr(c_i*S^j)=delta_ij in GF(2)[S]/(q)."""
    d = degree(q)
    gram = [
        [field_trace(mod(1 << (i + j), q), q) for j in range(d)]
        for i in range(d)
    ]
    augmented = [
        gram[i][:] + [1 if i == j else 0 for j in range(d)]
        for i in range(d)
    ]
    row = 0
    for col in range(d):
        pivot = next((r for r in range(row, d) if augmented[r][col]), None)
        if pivot is None:
            raise ArithmeticError("trace pairing is degenerate")
        augmented[row], augmented[pivot] = augmented[pivot], augmented[row]
        for r in range(d):
            if r != row and augmented[r][col]:
                augmented[r] = [
                    x ^ y for x, y in zip(augmented[r], augmented[row])
                ]
        row += 1
    inverse = [r[d:] for r in augmented]
    dual = [
        sum(bit << i for i, bit in enumerate(row_values))
        for row_values in inverse
    ]
    for i, c in enumerate(dual):
        for j in range(d):
            assert field_trace(mul_mod(c, 1 << j, q), q) == (1 if i == j else 0)
    return dual


def poly_power(q: int, n: int) -> int:
    result = 1
    for _ in range(n):
        result = mul(result, q)
    return result


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


def as_basis(height: int) -> Iterable[dict]:
    """The standard basis of F/wp(F), truncated by total pole height."""
    yield {
        "task": "zero_mode_as_basis",
        "kind": "constant",
        "numerator_bits": 1,
        "denominator_bits": 1,
        "label": "1",
    }
    for n in range(1, height + 1, 2):
        yield {
            "task": "zero_mode_as_basis",
            "kind": "polynomial_odd_pole_at_infinity",
            "numerator_bits": 1 << n,
            "denominator_bits": 1,
            "label": f"S^{n}",
            "height": n,
        }
    for q in irreducibles(height):
        d = degree(q)
        for pole_order in range(1, height // d + 1, 2):
            denominator = poly_power(q, pole_order)
            for j in range(d):
                numerator = 1 << j
                assert gcd(numerator, denominator) == 1
                yield {
                    "task": "zero_mode_as_basis",
                    "kind": "finite_place_odd_pole",
                    "Q_bits": q,
                    "Q": poly_string(q),
                    "Q_degree": d,
                    "odd_pole_order": pole_order,
                    "numerator_bits": numerator,
                    "denominator_bits": denominator,
                    "label": f"S^{j}/{poly_string(q)}^{pole_order}",
                    "height": d * pole_order,
                }


def residue_basis(q_max: int, degree_max: int) -> Iterable[dict]:
    qs = irreducibles(degree_max)
    for root in range(1, q_max + 1, 2):
        for q in qs:
            d = degree(q)
            dual = trace_dual_basis(q)
            for i in range(d):
                alpha = 1 << i
                yield {
                    "task": "coinvariant_residue_basis",
                    "odd_orbit_root": root,
                    "Q_bits": q,
                    "Q": poly_string(q),
                    "residue_degree": d,
                    "basis_index": i,
                    "residue_basis_bits": alpha,
                    "residue_basis": poly_string(alpha),
                    "trace_dual_readout_bits": dual[i],
                    "trace_dual_readout": poly_string(dual[i]),
                }


def dimension_formula(height: int, q_max: int, degree_max: int) -> dict:
    zero_dim = sum(1 for _ in as_basis(height))
    residue_dim = sum(1 for _ in residue_basis(q_max, degree_max))
    return {
        "zero_mode_basis_dimension": zero_dim,
        "odd_roots_count": len(range(1, q_max + 1, 2)),
        "finite_irreducible_points_count": len(irreducibles(degree_max)),
        "residue_basis_dimension": residue_dim,
        "total_benchmark_dimension": zero_dim + residue_dim,
    }


def self_test() -> None:
    qs = irreducibles(6)
    assert len(qs) == 23
    assert sum(degree(q) for q in qs) == 106
    count_dual = 0
    for q in qs:
        dual = trace_dual_basis(q)
        assert len(dual) == degree(q)
        count_dual += degree(q)
    zero = list(as_basis(5))
    assert len(zero) == 60
    residues = list(residue_basis(7, 4))
    assert len(residues) == 4 * 22
    assert dimension_formula(5, 7, 4)["total_benchmark_dimension"] == 148

    # Each trace-dual readout selects exactly one member of the residue basis.
    for q in qs:
        dual = trace_dual_basis(q)
        d = degree(q)
        for i, c in enumerate(dual):
            for j in range(d):
                assert field_trace(mul_mod(c, 1 << j, q), q) == (i == j)
    print(
        f"self-test: {len(qs)} irreducibles, {count_dual} trace-dual coordinates, "
        f"{len(zero)} AS basis elements, {len(residues)} residue basis elements passed",
        file=sys.stderr,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--height", type=int, default=5)
    parser.add_argument("--q-max", type=int, default=7)
    parser.add_argument("--degree-max", type=int, default=4)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.height < 0 or args.q_max < 0 or args.degree_max < 1:
        parser.error("height/q-max must be nonnegative and degree-max positive")
    if args.self_test:
        self_test()
    for row in as_basis(args.height):
        print(json.dumps(row, sort_keys=True))
    for row in residue_basis(args.q_max, args.degree_max):
        print(json.dumps(row, sort_keys=True))
    print(
        json.dumps(
            {"task": "dimension_summary", **dimension_formula(
                args.height, args.q_max, args.degree_max
            )},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
