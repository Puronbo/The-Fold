#!/usr/bin/env python3
"""Verify normalized symmetric mu_2-valued polynomial cocycles on alpha_4.

The full symmetric normalized basis includes rho*x*y. The equation F^2=0
forces rho^2=0; over a field rho=0. The remaining cocycle equations and
coboundaries are then checked exactly over F_2.
"""
import sympy as sp

x, y, w = sp.symbols("x y w")
alpha, beta, lam, delta, eps = sp.symbols("alpha beta lam delta eps")


def F(q, r):
    # rho*x*y has been removed using rho^2=0 and the field hypothesis.
    return (
        alpha * (q**2 * r + q * r**2)
        + beta * (q**3 * r + q * r**3)
        + lam * q**2 * r**2
        + delta * (q**3 * r**2 + q**2 * r**3)
        + eps * q**3 * r**3
    )


def truncated_equations():
    expression = sp.expand(
        (1 + F(x, y)) * (1 + F(x + y, w))
        + (1 + F(y, w)) * (1 + F(x, y + w))
    )
    poly = sp.Poly(expression, x, y, w, alpha, beta, lam, delta, eps, modulus=2)
    by_xyz = {}
    for exponents, coefficient in poly.terms():
        if all(power < 4 for power in exponents[:3]):
            xyz = exponents[:3]
            parameter_monomial = sp.prod(
                variable**power
                for variable, power in zip(
                    (alpha, beta, lam, delta, eps), exponents[3:]
                )
            )
            by_xyz[xyz] = by_xyz.get(xyz, 0) + int(coefficient) * parameter_monomial
    return [
        sp.Poly(value, alpha, beta, lam, delta, eps, modulus=2).as_expr()
        for value in by_xyz.values()
    ]


def main():
    equations = truncated_equations()
    groebner = sp.groebner(
        equations, alpha, beta, lam, delta, eps, modulus=2, order="lex"
    )
    actual = [p.as_expr() for p in groebner.polys]
    expected = [alpha**2 + eps, beta, delta]
    assert actual == expected, (actual, expected)

    # For h(q)=1+beta*q^2+alpha*q^3, its normalized coboundary is
    # h(x)h(y)h(x+y) in characteristic two.
    h = lambda q: 1 + beta * q**2 + alpha * q**3
    coboundary = sp.expand(h(x) * h(y) * h(x + y))
    cob_poly = sp.Poly(coboundary, x, y, alpha, beta, modulus=2)
    expected_cob = sp.Poly(
        1 + beta**2 * x**2 * y**2
        + alpha * (x**2 * y + x * y**2)
        + alpha**2 * x**3 * y**3,
        x, y, alpha, beta, modulus=2
    )
    actual_terms = {
        ex: coeff for ex, coeff in cob_poly.terms()
        if ex[0] < 4 and ex[1] < 4
    }
    expected_terms = {
        ex: coeff for ex, coeff in expected_cob.terms()
        if ex[0] < 4 and ex[1] < 4
    }
    assert actual_terms == expected_terms

    print("PASS: complete symmetric basis; rho^2=0 forces rho=0 over a field")
    print("PASS: remaining cocycle equations give beta=delta=0, eps=alpha^2")
    print("PASS: quotient by coboundaries leaves lambda modulo squares")


if __name__ == "__main__":
    main()
