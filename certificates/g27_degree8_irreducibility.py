#!/usr/bin/env python3
"""Finite exact irreducibility certificate for the degree-eight Weil factor.

The input polynomial is the monic Frobenius polynomial Q*(X), whose roots
are Weil numbers of complex absolute value sqrt(2).

The Newton polygon has slopes -3/4 and -1/4, each of horizontal length 4.
For a rational factor, the multiplicity of either slope must be divisible
by 4. Thus a proper factorization of this degree-eight polynomial would
have to include a monic quartic factor.

By Gauss's lemma that factor has integer coefficients. If its roots are
four of the eight Weil roots, its coefficients satisfy
|a| <= 4 sqrt(2) < 6,
|b| <= 6 * 2 = 12,
|c| <= 4 * 2 sqrt(2) < 12,
and |d| = (sqrt(2))^4 = 4.

We exhaust these 12,650 candidates using integer polynomial division.
No candidate divides Q*, proving irreducibility over Q.
"""
from itertools import product

# Coefficients in descending order, represented by ascending powers below.
Q = [16, 32, 24, 8, 2, 4, 6, 4, 1]


def divide_exact(f, g):
    """Return quotient if g divides f in Z[X], else None.
    Lists use ascending coefficient order; g is monic.
    """
    r = f[:]
    q = [0] * (len(f) - len(g) + 1)
    for k in range(len(q) - 1, -1, -1):
        lead = r[k + len(g) - 1]
        q[k] = lead
        for j in range(len(g)):
            r[k + j] -= lead * g[j]
    if any(r):
        return None
    return q


tested = 0
for a, b, c, d in product(range(-5, 6), range(-12, 13),
                          range(-11, 12), (-4, 4)):
    # X^4 + a X^3 + b X^2 + c X + d
    candidate = [d, c, b, a, 1]
    tested += 1
    quotient = divide_exact(Q, candidate)
    assert quotient is None, (candidate, quotient)

assert tested == 12650
print("Candidates tested:", tested)
print("No monic quartic divisor exists.")
print("Together with the Newton-slope degree constraint, Q* is irreducible over Q.")
