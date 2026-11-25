#!/usr/bin/env python3
"""Exact finite sweep of the Section 35 Collatz sufficient obstruction.

Checks every admissible (period p, total valuation A, terminal valuation b)
for 3 <= p <= 200 using arbitrary-precision integer arithmetic.
This is a finite certificate, not an all-period proof.
"""

from math import gcd


def admissible_totals(p):
    """Integers A satisfying 3**p < 2**A and 2**A * 3**p < 10**p."""
    return [
        A
        for A in range(p + 1, 2 * p + 1)
        if 3**p < 2**A and 2**A * 3**p < 10**p
    ]


def least_positive_crt_representative(p, b):
    modulus = 2 ** (b + 2)
    assert gcd(3**p, modulus) == 1
    residue = ((3 * 2**b - 1) * pow(3**p, -1, modulus)) % modulus
    return residue if residue else modulus


def check_triple(p, A, b):
    kappa = least_positive_crt_representative(p, b)
    lhs = kappa * 3 ** (2 * p) * (2**A - 3**p)
    rhs = 3 * 2**b * (10**p - 3 ** (2 * p))
    return lhs >= rhs, kappa


def main():
    checked = 0
    for p in range(3, 201):
        for A in admissible_totals(p):
            for b in range(1, A - p + 2):
                ok, kappa = check_triple(p, A, b)
                assert ok, (p, A, b, kappa)
                checked += 1

    assert checked == 273119, checked
    print(f"PASS: {checked} admissible triples, periods 3..200")


if __name__ == "__main__":
    main()
