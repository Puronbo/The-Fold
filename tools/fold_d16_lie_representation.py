#!/usr/bin/env python3
"""Symbolic verifier for UF-029 D16 action and bracket equivariance."""
import sympy as sp

q = sp.sqrt(2)
a,b,c,d,e,u,v = sp.symbols("a b c d e u v")
A,B,C,D,E,U,V = sp.symbols("A B C D E U V")

R = sp.Matrix([
 [1/q, 1/q, 0, 0, 0, 0, 0],
 [-1/q,1/q, 0, 0, 0, 0, 0],
 [0,0,-sp.Rational(1,2),1,sp.Rational(1,2),0,0],
 [0,0,-sp.Rational(1,2),0,-sp.Rational(1,2),0,0],
 [0,0,sp.Rational(1,2),1,-sp.Rational(1,2),0,0],
 [0,0,0,0,0,-1/q,-1/q],
 [0,0,0,0,0,1/q,-1/q],
])
S = sp.diag(1,-1,1,-1,1,-1,1)
I = sp.eye(7)

def bracket(p, z):
    aa,bb,cc,dd,ee,uu,vv = p
    AA,BB,CC,DD,EE,UU,VV = z
    wu = aa*DD-AA*dd+2*bb*CC-bb*EE-2*BB*cc+BB*ee
    wv = -aa*CC+2*aa*EE+AA*cc-2*AA*ee-bb*DD+BB*dd
    return sp.Matrix([0,0,0,0,0,sp.expand(wu),sp.expand(wv)])

def main():
    assert R**8 == I
    assert S**2 == I
    assert S*R*S == R.inv()

    # Invariant decomposition: E1=(a,b), E2=(c,d,e=c),
    # chi=span((-1,0,1)) in cubic coordinates, E3=(u,v).
    w = sp.Matrix([0,0,-1,0,1,0,0])
    assert R*w == -w and S*w == w

    p = sp.Matrix([a,b,c,d,e,u,v])
    z = sp.Matrix([A,B,C,D,E,U,V])
    for M in (R,S):
        lhs = bracket(M*p, M*z)
        rhs = M*bracket(p,z)
        assert all(sp.simplify(t) == 0 for t in lhs-rhs)

    # Cubic E2 plane e=c is invariant under both generators.
    w1 = sp.Matrix([0,0,1,0,1,0,0])
    w2 = sp.Matrix([0,0,0,1,0,0,0])
    for M in (R,S):
        for wv in (w1,w2):
            out=M*wv
            assert sp.simplify(out[4]-out[2]) == 0

    print("UF-029 symbolic checks: PASS")
    print("D16 relations, invariant summands, and bracket equivariance verified")

if __name__ == "__main__":
    main()
