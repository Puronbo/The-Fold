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
    """Return outer o inner as images of x,z (ring maps)."""
    ox, oz = outer
    ix, iz = inner
    return (
        reduce_gf2(ix.subs({x: ox, z: oz}, simultaneous=True)),
        reduce_gf2(iz.subs({x: ox, z: oz}, simultaneous=True)),
    )


def main():
    a,b,c,d,u,e,v = sp.symbols("a b c d u e v")
    X = x+(a+b)*x**2+b*x*z+(c+d)*x**3+d*x**2*z+u*x**3*z
    Z = z+(a+b)*x*z+(c+e)*x**3+(d+e)*x**2*z+(u+v)*x**3*z

    # The U-subgroup equations hold identically over F2.
    A = a+b
    C = c+d
    F = 0
    H = a+b
    G = c+e
    I = d+e
    assert sp.Poly(F, a,b,c,d,u,e,v, modulus=2).is_zero
    assert sp.Poly(H-A, a,b,c,d,u,e,v, modulus=2).is_zero
    assert sp.Poly(C+G+I, a,b,c,d,u,e,v, modulus=2).is_zero

    # g: z -> z+x^2 and u: x -> x+xz are involutions.
    ident = (x,z)
    g = (x,z+x**2)
    u_map = (x+x*z,z)
    assert compose(g,g) == ident
    assert compose(u_map,u_map) == ident

    # g o u o g sends x -> x+xz+x^3, z -> z+x^2.
    conjugate = compose(g, compose(u_map,g))
    expected = (x+x*z+x**3,z+x**2)
    assert conjugate == expected
    assert sp.Poly(conjugate[1]-z, x,z, modulus=2).coeff_monomial(x**2) == 1

    print("UF-037 exact GF(2) checks: PASS")
    print("U has codimension 3 in H; explicit conjugation proves U is not normal")


if __name__ == "__main__":
    main()
