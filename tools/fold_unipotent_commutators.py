#!/usr/bin/env python3
"""Symbolic verifier for UF-028 Lie and group commutators. Requires SymPy."""
import sympy as sp

x, y = sp.symbols("x y")
a,b,c,d,e,u,v,A,B,C,D,E,U,V = sp.symbols(
    "a b c d e u v A B C D E U V"
)

def red(expr):
    p = sp.Poly(sp.expand(expr), x, y)
    out = 0
    for (i,j), coeff in p.terms():
        q,r = divmod(j,2)
        ni = i + 2*q
        if ni < 4:
            out += coeff*(-1)**q*x**ni*y**r
    return sp.expand(out)

def deriv(expr, z):
    aa,bb,cc,dd,ee,uu,vv = z
    dx = aa*x**2+bb*x*y+cc*x**3+dd*x**2*y+uu*x**3*y
    dy = -bb*x**2+aa*x*y-dd*x**3+ee*x**2*y+vv*x**3*y
    return red(sp.diff(expr,x)*dx+sp.diff(expr,y)*dy)

def phi(z):
    aa,bb,cc,dd,ee,uu,vv=z
    return (x+aa*x**2+bb*x*y+cc*x**3+dd*x**2*y+uu*x**3*y,
            y-bb*x**2+aa*x*y-dd*x**3+ee*x**2*y+vv*x**3*y)

def mul(t,s):
    a,b,c,d,e,f,g=t
    A,B,C,D,E,F,G=s
    return (
      a+A, b+B,
      c+C+2*A*a-2*B*b,
      d+D+2*A*b+2*B*a,
      e+E+2*A*a-2*B*b,
      f+F+2*A*a*b+2*A*d+B*a**2-B*b**2+B*c+B*e+3*C*b+3*D*a,
      g+G+A*a**2-A*b**2+A*c+A*e-2*B*a*b-2*B*d-3*D*b+3*E*a
    )

def inv(t):
    a,b,c,d,e,f,g=t
    return (-a,-b,-c+2*a**2-2*b**2,-d+4*a*b,-e+2*a**2-2*b**2,
      -15*a**2*b+5*a*d+5*b**3+4*b*c+b*e-f,
      -5*a**3+15*a*b**2+a*c+4*a*e-5*b*d-g)

def main():
    # Lie bracket on generators.
    z1=(a,b,c,d,e,u,v); z2=(A,B,C,D,E,U,V)
    bx=red(deriv(deriv(x,z2),z1)-deriv(deriv(x,z1),z2))
    by=red(deriv(deriv(y,z2),z1)-deriv(deriv(y,z1),z2))
    wu=a*D-A*d+2*b*C-b*E-2*B*c+B*e
    wv=-a*C+2*a*E+A*c-2*A*e-b*D+B*d
    assert red(bx-wu*x**3*y)==0
    assert red(by-wv*x**3*y)==0

    # Exact group commutator from the UF-027 coordinate law.
    t=(a,b,c,d,e,u,v); s=(A,B,C,D,E,U,V)
    comm=mul(mul(mul(t,s),inv(t)),inv(s))
    ku=(-A**2*b-2*A*B*a+2*A*a*b-A*d+B**2*b+B*a**2-B*b**2
        -2*B*c+B*e+2*C*b+D*a-E*b)
    kv=(-A**2*a+2*A*B*b+A*a**2-A*b**2+A*c-2*A*e+B**2*a
        -2*B*a*b+B*d-C*a-D*b+2*E*a)
    assert [sp.expand(q) for q in comm[:5]] == [0]*5
    assert sp.expand(comm[5]-ku)==0
    assert sp.expand(comm[6]-kv)==0

    # Every central translation is a commutator of the indicated form.
    test=mul(mul(mul((1,0,0,0,0,0,0),(0,0,C,D,0,0,0)),
                 inv((1,0,0,0,0,0,0))),inv((0,0,C,D,0,0,0)))
    assert test == (0,0,0,0,0,D,-C)
    print("UF-028 symbolic checks: PASS")
    print("Lie bracket, inverse, group commutator, and derived subgroup verified")

if __name__ == "__main__":
    main()
