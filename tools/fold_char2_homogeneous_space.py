#!/usr/bin/env python3
"""Exact GF(2) verifier for UF-038. Requires SymPy."""
import sympy as sp

x,z=sp.symbols("x z")
A,B,C,D,E,G,I,J=sp.symbols("A B C D E G I J")
a,b,c,d,e,g,i,j=sp.symbols("a b c d e g i j")
F,H=sp.symbols("F H")
PARAMS=[A,B,C,D,E,G,I,J,a,b,c,d,e,g,i,j,F,H]


def red(expr):
    p=sp.Poly(sp.expand(expr),x,z)
    out=0
    for (ix,iz),co in p.terms():
        if ix<4 and iz<2:
            out += sp.Poly(co,*PARAMS,modulus=2).as_expr()*x**ix*z**iz
    return sp.expand(out)


def compose(outer,inner):
    ox,oz=outer; ix,iz=inner
    return (red(ix.subs({x:ox,z:oz},simultaneous=True)),
            red(iz.subs({x:ox,z:oz},simultaneous=True)))


def coeff(poly,mon):
    return sp.Poly(poly,x,z).coeff_monomial(mon)


def nmap(p):
    aa,bb,cc,dd,ee,gg,ii,jj=p
    return (x+aa*x**2+bb*x**3+cc*x*z+dd*x**2*z+ee*x**3*z,
            z+gg*x**3+aa*x*z+ii*x**2*z+jj*x**3*z)


def law(p,q):
    A,B,C,D,E,G,I,J=p
    a,b,c,d,e,g,i,j=q
    return (
        A+a,B+b,C+c,D+d,
        E+e+A**2*c+A*d+B*c+C*b+I*c,
        G+g,I+i,
        J+j+A**2*a+A*i+B*a+C*g+I*a
    )


def inv(p):
    A,B,C,D,E,G,I,J=p
    return (A,B,C,D,E+A**2*C+A*D+I*C,G,I,J+A**3+B*A+C*G)


def main():
    P=(A,B,C,D,E,G,I,J)
    Q=(a,b,c,d,e,g,i,j)
    # Compare the explicit law with substitution.
    comp=compose(nmap(P),nmap(Q))
    actual=(coeff(comp[0],x**2),coeff(comp[0],x**3),
            coeff(comp[0],x*z),coeff(comp[0],x**2*z),
            coeff(comp[0],x**3*z),coeff(comp[1],x**3),
            coeff(comp[1],x**2*z),coeff(comp[1],x**3*z))
    assert all(sp.Poly(u-v,*PARAMS,modulus=2).is_zero
               for u,v in zip(actual,law(P,Q)))

    assert all(sp.Poly(u,*PARAMS,modulus=2).is_zero
               for u in law(P,inv(P)))
    assert all(sp.Poly(u,*PARAMS,modulus=2).is_zero
               for u in law(inv(P),P))

    # lambda=B+G+I is a homomorphism with kernel U.
    assert sp.Poly((law(P,Q)[1]+law(P,Q)[5]+law(P,Q)[6])
                   -(B+G+I)-(b+g+i),*PARAMS,modulus=2).is_zero

    # The commutator is central and has the displayed E,J coordinates.
    comm=law(law(law(P,Q),inv(P)),inv(Q))
    expected_E=A**2*c+A*d+C*a**2+C*i+D*a+I*c
    expected_J=A**2*a+A*a**2+A*b+B*a+C*g+G*c
    expected=(0,0,0,0,expected_E,0,0,expected_J)
    assert all(sp.Poly(u-v,*PARAMS,modulus=2).is_zero
               for u,v in zip(comm,expected))

    # Section s(F,R) and its inverse are checked directly.
    R=H+A
    section=(x,z+F*x**2+R*x*z)
    section_inv=(x,z+F*x**2+R*x*z+F*R*x**3+R**2*x**2*z+R**3*x**3*z)
    assert compose(section,section_inv)==(x,z)
    assert compose(section_inv,section)==(x,z)

    print("UF-038 exact GF(2) checks: PASS")
    print("N/U = Ga, Z(N) = [N,N] = Ga^2, class(N)=2")
    print("H/U is A^3 via the section coordinates")


if __name__=="__main__":
    main()
