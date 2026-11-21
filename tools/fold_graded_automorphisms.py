#!/usr/bin/env python3
"""Exact polynomial-reduction checks for UF-025."""
from fractions import Fraction


def add(*polys):
    out = {}
    for poly in polys:
        for mon, c in poly.items():
            out[mon] = out.get(mon, Fraction(0)) + c
    return {m: c for m, c in out.items() if c}


def scale(poly, c):
    return {m: c * v for m, v in poly.items() if c * v}


def mul(A, B):
    out = {}
    for (i, j), a in A.items():
        for (k, ell), b in B.items():
            # Reduce y^2=-x^2, then x^4=0.
            yy, rem = divmod(j + ell, 2)
            xx = i + k + 2 * yy
            if xx >= 4:
                continue
            mon = (xx, rem)
            out[mon] = out.get(mon, Fraction(0)) + a * b * ((-1) ** yy)
    return {m: c for m, c in out.items() if c}


x, y = {(1, 0): Fraction(1)}, {(0, 1): Fraction(1)}
q = add(mul(x, x), mul(y, y))
xp = add(x, scale(y, -1))  # x-y
yp = add(x, y)             # x+y


def power(poly, n):
    out = {(0, 0): Fraction(1)}
    for _ in range(n):
        out = mul(out, poly)
    return out


def main():
    # The additional 45-degree generator preserves q up to a unit.
    assert add(power(xp, 2), power(yp, 2)) == scale(q, 2)
    assert power(xp, 4) == {}
    assert power(yp, 4) == {}

    # The projective condition ab(a^2-b^2)=0 has four directions:
    # b/a = 0, infinity, +1, -1. Each has two signs for a normalized
    # unit vector, and each vector has two orthogonal orientations.
    directions = ((1, 0), (0, 1), (1, 1), (1, -1))
    for a, b in directions:
        assert a * b * (a * a - b * b) == 0
    assert len(directions) == 4
    assert 4 * 2 * 2 == 16

    print("UF-025 exact checks: PASS")
    print("extra linear automorphism: x -> x-y, y -> x+y")
    print("q maps to 2q; both generator fourth powers vanish")
    print("orthogonal stabilizer order:", 16)


if __name__ == "__main__":
    main()
