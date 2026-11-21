#!/usr/bin/env python3
"""Symbolic identity verifier for UF-026. Requires SymPy."""
import sympy as sp

x, y = sp.symbols("x y")
alpha, beta, gamma, delta, eta, u, v = sp.symbols(
    "alpha beta gamma delta eta u v"
)


def reduce_fold(expr):
    """Reduce using y^2=-x^2 and x^4=0."""
    poly = sp.Poly(sp.expand(expr), x, y)
    out = 0
    for (i, j), coeff in poly.terms():
        q, rem = divmod(j, 2)
        new_x = i + 2 * q
        if new_x < 4:
            out += coeff * (-1) ** q * x ** new_x * y ** rem
    return sp.expand(out)


X = (x + alpha*x**2 + beta*x*y + gamma*x**3
     + delta*x**2*y + u*x**3*y)
Y = (y - beta*x**2 + alpha*x*y - delta*x**3
     + eta*x**2*y + v*x**3*y)


def main():
    assert reduce_fold(X**2 + Y**2) == 0
    assert reduce_fold(X**4) == 0

    # Check the coefficient constraints are necessary and sufficient
    # for a general identity-linear pair.
    A, B, C, D = sp.symbols("A B C D")
    Xg = x + alpha*x**2 + beta*x*y + gamma*x**3 + delta*x**2*y + u*x**3*y
    Yg = y + A*x**2 + B*x*y + C*x**3 + D*x**2*y + v*x**3*y
    relation = sp.Poly(reduce_fold(Xg**2 + Yg**2), x, y)
    equations = [
        relation.coeff_monomial(x**3),
        relation.coeff_monomial(x**2*y),
        relation.coeff_monomial(x**3*y),
    ]
    assert equations == [
        2*(alpha - B),
        2*(beta + A),
        2*(alpha*beta + delta + A*B + C),
    ]
    assert sp.solve(equations, (A, B, C), dict=True) == [
        {A: -beta, B: alpha, C: -delta}
    ]

    print("UF-026 symbolic checks: PASS")
    print("identity-linear automorphism parameters: 7")
    print("relations X^2+Y^2 and X^4 vanish identically")


if __name__ == "__main__":
    main()
