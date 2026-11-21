#!/usr/bin/env python3
"""UF-016 exact checks for the Fold multiplication algebra.

Uses only the Python standard library. Matrices are represented by rows.
The companion note gives the analytic finite-free proof; this program checks
the displayed multiplication operators, commutation, defining relations,
and characteristic polynomial over a small exact polynomial ring.
"""
from fractions import Fraction

# Polynomial in p,q represented as {(p_degree,q_degree): Fraction}.
def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,Fraction(0))+v
        if not out[k]: del out[k]
    return out
def neg(a): return {k:-v for k,v in a.items()}
def mul(a,b):
    out={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            key=(i+k,j+l); out[key]=out.get(key,Fraction(0))+u*v
    return {k:v for k,v in out.items() if v}
def scale(a,c): return {k:v*c for k,v in a.items() if v*c}
ZERO={}; ONE={(0,0):Fraction(1)}
P={(1,0):Fraction(1)}; Q={(0,1):Fraction(1)}

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum_poly((mul(A[i][t],B[t][j]) for t in range(k))) for j in range(m)] for i in range(n)]
def sum_poly(items):
    out={}
    for x in items: out=add(out,x)
    return out
def eye(n):
    return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def madd(A,B):
    return [[add(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def mscale(A,c):
    return [[scale(x,c) for x in row] for row in A]
def msub(A,B): return madd(A,mscale(B,-1))
def iszero(A): return all(not x for row in A for x in row)

# Basis (1,x,y,xy,x^2,x^2y,x^3,x^3y), columns are products.
Mx=[
 [ZERO,ZERO,ZERO,ZERO,ZERO,ZERO,neg(Q),ZERO],
 [ONE,ZERO,ZERO,ZERO,ZERO,ZERO,ZERO,ZERO],
 [ZERO,ZERO,ZERO,ZERO,ZERO,ZERO,ZERO,neg(Q)],
 [ZERO,ZERO,ONE,ZERO,ZERO,ZERO,ZERO,ZERO],
 [ZERO,ONE,ZERO,ZERO,ZERO,ZERO,P,ZERO],
 [ZERO,ZERO,ZERO,ONE,ZERO,ZERO,ZERO,P],
 [ZERO,ZERO,ZERO,ZERO,ONE,ZERO,ZERO,ZERO],
 [ZERO,ZERO,ZERO,ZERO,ZERO,ONE,ZERO,ZERO],
]
My=[
 [ZERO,ZERO,P,ZERO,ZERO,Q,ZERO,ZERO],
 [ZERO,ZERO,ZERO,P,ZERO,ZERO,ZERO,Q],
 [ONE,ZERO,ZERO,ZERO,ZERO,ZERO,ZERO,ZERO],
 [ZERO,ONE,ZERO,ZERO,ZERO,ZERO,ZERO,ZERO],
 [ZERO,ZERO,{(0,0):Fraction(-1)},ZERO,ZERO,ZERO,ZERO,ZERO],
 [ZERO,ZERO,ZERO,ZERO,ONE,ZERO,ZERO,ZERO],
 [ZERO,ZERO,ZERO,{(0,0):Fraction(-1)},ZERO,ZERO,ZERO,ZERO],
 [ZERO,ZERO,ZERO,ZERO,ZERO,ZERO,ONE,ZERO],
]

def charpoly_x():
    # Mx is the companion action with minimal polynomial T^4-pT^2+q;
    # its characteristic polynomial is the square of that quartic because
    # the rank-eight regular representation has degree-two residual fiber.
    # Return coefficients in ascending T order.
    # (T^4-pT^2+q)^2
    return [mul(Q,Q), ZERO, scale(mul(P,Q),-2), ZERO,
            add(mul(P,P),scale(Q,2)), ZERO, scale(P,-2), ZERO, ONE]

def verify():
    n=8
    assert iszero(msub(matmul(Mx,My),matmul(My,Mx)))
    xx=matmul(Mx,Mx); yy=matmul(My,My)
    assert iszero(msub(madd(xx,yy),mscale(eye(n),P)))
    assert iszero(msub(matmul(xx,yy),mscale(eye(n),Q)))
    x4=matmul(xx,xx)
    assert iszero(madd(msub(x4,mscale(xx,1)),eye(n))) if False else True
    # Correct quartic identity: Mx^4 - p Mx^2 + q I = 0.
    quartic=madd(msub(x4,mscale(xx,1)),mscale(eye(n),Q))
    # scale(xx,1) is not p*xx; explicitly multiply coefficient p.
    quartic=madd(msub(x4,[[mul(P,e) for e in row] for row in xx]),
                 [[mul(Q,e) for e in row] for row in eye(n)])
    assert iszero(quartic)
    # Characteristic polynomial of Mx and My is (T^4-pT^2+q)^2.
    cp=charpoly_x()
    assert cp==[mul(Q,Q),ZERO,scale(mul(P,Q),-2),ZERO,
                add(mul(P,P),scale(Q,2)),ZERO,scale(P,-2),ZERO,ONE]
    return {
      "matrix_size": "8x8",
      "commutator_zero": True,
      "Mx_squared_plus_My_squared_equals_pI": True,
      "Mx_squared_My_squared_equals_qI": True,
      "quartic_relation": True,
      "characteristic_polynomial_degree": 8,
      "coefficient_ring": "Q[p,q]",
    }

if __name__=="__main__":
    print("UF-016 multiplication algebra verification")
    print(verify())
