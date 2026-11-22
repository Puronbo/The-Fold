#!/usr/bin/env python3
"""Exact factorization and 2-adic Newton polygon for the genus-7 Jacobian.

Input: the Weil polynomial certified by g24_genus7_weil_polynomial.py.
All polynomial arithmetic and 2-adic valuations below use integers only.
"""
from fractions import Fraction

# Weil polynomial P(T), coefficients in increasing degree.
P = [1, 6, 20, 48, 90, 140, 196, 272, 392, 560, 720, 768, 640, 384, 128]

# P(T) = (1+2T^2)^2 (1+2T+2T^2) Q(T).
Q = [1, 4, 6, 4, 2, 8, 24, 32, 16]


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


factorization = multiply(
    multiply(multiply([1, 0, 2], [1, 0, 2]), [1, 2, 2]), Q
)
assert factorization == P


def v2(n):
    if n == 0:
        return float("inf")
    value = 0
    while n % 2 == 0:
        n //= 2
        value += 1
    return value


# F(X)=X^14 P(1/X) is the monic Frobenius characteristic polynomial.
# Its coefficient of X^i is P[14-i].
points = [(i, v2(P[14 - i])) for i in range(15)]


def cross(o, a, b):
    return ((a[0] - o[0]) * (b[1] - a[1])
            - (a[1] - o[1]) * (b[0] - a[0]))


# Lower convex hull, with collinear interior points removed.
hull = []
for point in points:
    while len(hull) >= 2 and cross(hull[-2], hull[-1], point) <= 0:
        hull.pop()
    hull.append(point)

expected_hull = [(0, 7), (4, 4), (10, 1), (14, 0)]
assert hull == expected_hull, (hull, expected_hull)

# Root valuations are the negatives of the Newton-polygon slopes.
slopes = []
for (x0, y0), (x1, y1) in zip(hull, hull[1:]):
    root_valuation = Fraction(y0 - y1, x1 - x0)
    slopes.extend([root_valuation] * (x1 - x0))

expected = [Fraction(1, 4)] * 4 + [Fraction(1, 2)] * 6 + [Fraction(3, 4)] * 4
assert sorted(slopes) == expected

print("Factorization verified:")
print("P(T) = (1+2T^2)^2 (1+2T+2T^2) Q(T)")
print("Q(T) =", Q)
print("2-adic coefficient valuations:", [y for _, y in points])
print("Newton polygon vertices:", hull)
print("Newton slopes:", sorted(slopes))
print("Conclusion: p-rank 0; not supersingular.")
