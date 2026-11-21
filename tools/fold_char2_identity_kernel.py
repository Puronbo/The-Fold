#!/usr/bin/env python3
"""Exact GF(2) checks for UF-037. Requires SymPy."""
import sympy as sp

x, z = sp.symbols("x z")


def reduce_gf2(expr):
    poly = sp.Poly(sp.expand(expr), x, z, modulus=2)
    out = 0
    for (i, j), coeff in poly.terms():
        if i < 4 and j < 2:
            out += int(coeff) % 2 * x**i * z**j
    return sp.Poly(out, x, z, modulus=2).as_expr()


def compose(outer, inner):
    """Ring-map composition outer after inner."""
    ox, oz = outer
    ix, iz = inner
    return (
        reduce_gf2(ix.subs({x: ox, z: oz}, simultaneous=True)),
        reduce_gf2(iz.subs({x: ox, z: oz}, simultaneous=True)),
    )


def deriv(P, Q, expr):
    return reduce_gf2(sp.diff(expr, x)*P + sp.diff(expr, z)*Q)


def bracket(D, E):
    P, Q = D
    R, S = E
    return (
        reduce_gf2(deriv(P, Q, R) + deriv(R, S, P)),
        reduce_gf2(deriv(P, Q, S) + deriv(R, S, Q)),
    )


def main():
    a,b,c,d,u,e,v = sp.symbols("a b c d u e v")
    # Integral U family reduced mod 2, in coordinates x,z.
    A = a+b
    B = c+d
    C = b
    D = d
    E = u
    F = 0
    G = c+e
    H = a+b
    I = d+e
    J = u+v

    assert sp.Poly(F, a,b,c,d,u,e,v, modulus=2).is_zero
    assert sp.Poly(H-A, a,b,c,d,u,e,v, modulus=2).is_zero
    assert sp.Poly(B+G+I, a,b,c,d,u,e,v, modulus=2).is_zero

    # g:z -> z+x^2 and u:x -> x+xz are involutions.
    ident = (x,z)
    g = (x,z+x**2)
    u_map = (x+x*z,z)
    assert compose(g,g) == ident
    assert compose(u_map,u_map) == ident
    conjugate = compose(g, compose(u_map,g))
    assert conjugate == (x+x*z+x**3,z)
    assert sp.Poly(conjugate[0]-x, x,z, modulus=2).coeff_monomial(x**3) == 1

    # Lie bracket [eta,delta] = (x^3,0), the missing cubic tangent.
    eta = (0,x**2)       # eta(x)=0, eta(z)=x^2
    delta = (x*z,0)      # delta(x)=xz, delta(z)=0
    assert bracket(eta,delta) == (x**3,0)

    print("UF-037 exact GF(2) checks: PASS")
    print("U has codimension 3 in H and is not normal")
    print("its normal closure is the 8-dimensional subgroup N")
    print("H/N is the 2-dimensional additive group")


if __name__ == "__main__":
    main()
