#!/usr/bin/env python3
"""Exact CRT/minimum-member filter for periods 3 through 100."""
from math import gcd


def inverse_mod(a, modulus):
    # Python's modular inverse is exact and raises if the inverse does not exist.
    return pow(a, -1, modulus)


def admissible_totals(p):
    # Strict average-valuation window:
    # 3**p < 2**A and 2**A * 3**p < 10**p.
    return [
        A for A in range(p + 1, 2 * p + 1)
        if 3**p < 2**A and 2**A * 3**p < 10**p
    ]


def check_pair(p, A, b):
    modulus = 2 ** (b + 2)
    assert gcd(3**p, modulus) == 1
    kappa = ((3 * 2**b - 1) * inverse_mod(3**p, modulus)) % modulus
    if kappa == 0:
        kappa = modulus

    # Exact form of:
    # kappa >= 2**b / (3**p * (2**(A/p) - 3)).
    left = 2**A * (kappa * 3**p) ** p
    right = (3 * kappa * 3**p + 2**b) ** p
    return left >= right, kappa


checked = 0
for p in range(3, 101):
    for A in admissible_totals(p):
        for b in range(1, A - p + 2):
            ok, kappa = check_pair(p, A, b)
            assert ok, (p, A, b, kappa)
            checked += 1

assert checked == 34_838
print("periods checked: 3..100")
print("terminal-valuation pairs checked:", checked)
print("all exact CRT/minimum inequalities hold")
print("certificate: PASS")
