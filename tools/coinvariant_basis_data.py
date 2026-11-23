#!/usr/bin/env python3
"""Finite exact basis/dual-coordinate benchmark for the Fold coinvariant.

The full algebraic coinvariant is
  direct_sum_Q GF(2)  +  direct_sum_{q odd>0,Q} GF(2)[S]/(Q),
where Q runs over monic irreducibles in GF(2)[S].

The zero-mode factor is identified by residue traces on
Omega_F^1/dF modulo Cartier coinvariants, not by F/wp(F).
This script emits finite cutoffs and exact trace-dual readouts.
All arithmetic is over GF(2); no external packages are required.
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


def zero_mode_basis(degree_max: int) -> Iterable[dict]:
    """One trace-one rational differential generator for each Q.

    In the zero mode, F/(wp(F)+S*F^2) has one F_2 coordinate per
    finite irreducible Q, given by Tr_{k_Q/F_2}(res_Q((x/S)dS)).
    Choose alpha with trace one and set x=S*alpha*Q'/Q.
    """
    for q in irreducibles(degree_max):
        d = degree(q)
        alpha = next(
            (a for a in range(1, 1 << d) if field_trace(a, q) == 1),
            None,
        )
        if alpha is None:
            raise ArithmeticError("finite-field trace map was not surjective")
        qprime = 0
        i = 1
        while (1 << i) <= q:
            if (q >> i) & 1 and (i & 1):
                qprime |= 1 << (i - 1)
            i += 1
        raw_numerator = mul(mul(0b10, alpha), qprime)
        common = gcd(raw_numerator, q)
        numerator = exact_div(raw_numerator, common)
        denominator = exact_div(q, common)
        assert gcd(numerator, denominator) == 1
        yield {
            "task": "zero_mode_residue_trace_basis",
            "Q_bits": q,
            "Q": poly_string(q),
            "Q_degree": d,
            "trace_one_residue_bits": alpha,
            "trace_one_residue": poly_string(alpha),
            "numerator_bits": numerator,
            "denominator_bits": denominator,
            "differential": "(x/S)dS = alpha*Q'(S)/Q(S) dS",
            "zero_mode_readout": 1,
            "height": d,
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


def dimension_formula(
    zero_degree_max: int, q_max: int, degree_max: int
) -> dict:
    zero_dim = len(irreducibles(zero_degree_max))
    residue_dim = sum(1 for _ in residue_basis(q_max, degree_max))
    return {
        "zero_mode_residue_basis_dimension": zero_dim,
        "zero_mode_degree_cutoff": zero_degree_max,
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

    zero = list(zero_mode_basis(4))
    assert len(zero) == 8
    for row in zero:
        q = row["Q_bits"]
        alpha = row["trace_one_residue_bits"]
        assert field_trace(alpha, q) == 1
        numerator = row["numerator_bits"]
        denominator = row["denominator_bits"]
        assert gcd(numerator, denominator) == 1
        # x/S = alpha*Q'/Q, so its Q-residue is alpha and has trace one.
        assert row["zero_mode_readout"] == field_trace(alpha, q)

    residues = list(residue_basis(7, 4))
    assert len(residues) == 4 * 22
    assert dimension_formula(4, 7, 4)["total_benchmark_dimension"] == 96

    # Every finite-field trace-one residue represents the nonzero F_2
    # coinvariant class; trace-zero residues are precisely Artin-Schreier
    # differences alpha^2+alpha.
    for q in qs:
        d = degree(q)
        values = range(1 << d)
        image = {add(a, square_mod(a, q)) for a in values}
        assert image == {a for a in values if field_trace(a, q) == 0}
        assert len(image) == (1 << d) // 2

    for q in qs:
        dual = trace_dual_basis(q)
        d = degree(q)
        for i, value in enumerate(dual):
            for j in range(d):
                assert field_trace(mul_mod(value, 1 << j, q), q) == (i == j)
    print(
        f"self-test: {len(qs)} irreducibles, {count_dual} trace-dual coordinates, "
        f"{len(zero)} zero-mode residue generators, {len(residues)} orbit-residue "
        "basis elements passed",
        file=sys.stderr,
    )

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zero-degree-max", type=int, default=4)
    parser.add_argument("--q-max", type=int, default=7)
    parser.add_argument("--degree-max", type=int, default=4)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.zero_degree_max < 1 or args.q_max < 0 or args.degree_max < 1:
        parser.error("zero-degree-max and degree-max must be positive; q-max nonnegative")
    if args.self_test:
        self_test()
    for row in zero_mode_basis(args.zero_degree_max):
        print(json.dumps(row, sort_keys=True))
    for row in residue_basis(args.q_max, args.degree_max):
        print(json.dumps(row, sort_keys=True))
    print(
        json.dumps(
            {"task": "dimension_summary", **dimension_formula(
                args.zero_degree_max, args.q_max, args.degree_max
            )},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
