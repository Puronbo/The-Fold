#!/usr/bin/env python3
"""Symbolic checks for UF-036. Requires SymPy."""
import sympy as sp

x, y = sp.symbols("x y")
a,b,c,d,e,f,g = sp.symbols("a b c d e f g")
A,B,C,D,E,F,G = sp.symbols("A B C D E F G")


def reduce_fold(expr):
    poly = sp.Poly(sp.expand(expr), x, y)
    out = 0
    for (i,j), coeff in poly.terms():
        q, rem = divmod(j, 2)
        power = i + 2*q
        if power < 4:
            out += coeff * (-1)**q * x**power * y**rem
    return sp.expand(out)


def images(t):
    aa,bb,cc,dd,ee,ff,gg = t
    return (x+aa*x**2+bb*x*y+cc*x**3+dd*x**2*y+ff*x**3*y,
            y-bb*x**2+aa*x*y-dd*x**3+ee*x**2*y+gg*x**3*y)


def law(t, T):
    aa,bb,cc,dd,ee,ff,gg=t
    AA,BB,CC,DD,EE,FF,GG=T
    return (
        aa+AA, bb+BB,
        cc+CC+2*AA*aa-2*BB*bb,
        dd+DD+2*AA*bb+2*BB*aa,
        ee+EE+2*AA*aa-2*BB*bb,
        ff+FF+2*AA*aa*bb+2*AA*dd+BB*aa**2-BB*bb**2
          +BB*cc+BB*ee+3*CC*bb+3*DD*aa,
        gg+GG+AA*aa**2-AA*bb**2+AA*cc+AA*ee
          -2*BB*aa*bb-2*BB*dd-3*DD*bb+3*EE*aa,
    )


def main():
    theta=(a,b,c,d,e,f,g)
    inv=(-a,-b,-c+2*a**2-2*b**2,-d+4*a*b,
         -e+2*a**2-2*b**2,
         -f-15*a**2*b+5*a*d+5*b**3+4*b*c+b*e,
         -g-5*a**3+15*a*b**2+a*c+4*a*e-5*b*d)
    assert all(sp.expand(v)==0 for v in law(theta,inv))
    assert all(sp.expand(v)==0 for v in law(inv,theta))

    # Universal substitutions preserve the two integral defining relations.
    X,Y=images(theta)
    assert reduce_fold(X**2+Y**2)==0
    assert reduce_fold(X**4)==0
    assert reduce_fold(X**2*Y**2)==0

    # The structure and inverse polynomials are integral by construction.
    for value in law(theta,(A,B,C,D,E,F,G))+inv:
        assert all(coef.is_Integer for coef in sp.Poly(value, a,b,c,d,e,f,g,A,B,C,D,E,F,G).coeffs())

    print("UF-036 symbolic checks: PASS")
    print("two-sided inverse, integral group law, and defining-relation preservation verified")


if __name__ == "__main__":
    main()
