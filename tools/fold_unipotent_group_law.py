#!/usr/bin/env python3
"""Symbolic verifier for the UF-027 composition law. Requires SymPy."""
import sympy as sp

x, y = sp.symbols("x y")
a, b, c, d, e, f, g = sp.symbols("a b c d e f g")
A, B, C, D, E, F, G = sp.symbols("A B C D E F G")


def reduce_fold(expr):
    poly = sp.Poly(sp.expand(expr), x, y)
    out = 0
    for (i, j), coeff in poly.terms():
        q, rem = divmod(j, 2)
        new_x = i + 2*q
        if new_x < 4:
            out += coeff * (-1)**q * x**new_x * y**rem
    return sp.expand(out)


def images(params):
    aa, bb, cc, dd, ee, ff, gg = params
    return (
        x + aa*x**2 + bb*x*y + cc*x**3 + dd*x**2*y + ff*x**3*y,
        y - bb*x**2 + aa*x*y - dd*x**3 + ee*x**2*y + gg*x**3*y,
    )


def compose_outer_after_inner(outer, inner):
    xo, yo = images(outer)
    xi, yi = images(inner)
    return (
        reduce_fold(xi.subs({x: xo, y: yo}, simultaneous=True)),
        reduce_fold(yi.subs({x: xo, y: yo}, simultaneous=True)),
    )


def coeff(poly, monomial):
    return sp.Poly(poly, x, y).coeff_monomial(monomial)


def main():
    X, Y = compose_outer_after_inner(
        (a, b, c, d, e, f, g), (A, B, C, D, E, F, G)
    )
    predicted = {
        (x, x**2): a + A,
        (x, x*y): b + B,
        (x, x**3): c + C + 2*A*a - 2*B*b,
        (x, x**2*y): d + D + 2*A*b + 2*B*a,
        (x, x**3*y): (
            f + F + 2*A*a*b + 2*A*d + B*a**2 - B*b**2
            + B*c + B*e + 3*C*b + 3*D*a
        ),
        (y, x**2): -b - B,
        (y, x*y): a + A,
        (y, x**3): -(d + D + 2*A*b + 2*B*a),
        (y, x**2*y): e + E + 2*A*a - 2*B*b,
        (y, x**3*y): (
            g + G + A*a**2 - A*b**2 + A*c + A*e
            - 2*B*a*b - 2*B*d - 3*D*b + 3*E*a
        ),
    }
    for (which, mon), expected in predicted.items():
        actual = coeff(X if which == x else Y, mon)
        assert sp.expand(actual - expected) == 0, (which, mon, actual, expected)

    assert reduce_fold(X**2 + Y**2) == 0
    assert reduce_fold(X**4) == 0
    print("UF-027 symbolic checks: PASS")
    print("all ten coordinate coefficient identities verified")


if __name__ == "__main__":
    main()
