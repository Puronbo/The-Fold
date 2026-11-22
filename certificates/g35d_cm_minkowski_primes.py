#!/usr/bin/env python3
"""Exact modular factorization certificate for the G-35D CM Minkowski search.

The primitive element theta=pi/(beta+2) has polynomial
H=X^8-8X^7+26X^6-44X^5+53X^4-68X^3+64X^2-24X+4.
Its index in O_L is a power of 2, so factorization modulo odd p gives
the actual residue-degree pattern in O_L.
All polynomial lists below use ascending coefficients.
"""
def det_bareiss(matrix):
    a=[row[:] for row in matrix]; n=len(a); sign=1; previous=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None: return 0
            a[k],a[pivot]=a[pivot],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value % previous == 0
                a[i][j]=value//previous
        for i in range(k+1,n): a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def resultant(f,g):
    m=len(f)-1; n=len(g)-1; fd=f[::-1]; gd=g[::-1]; rows=[]
    for j in range(n): rows.append([0]*j+fd+[0]*(n-1-j))
    for j in range(m): rows.append([0]*j+gd+[0]*(m-1-j))
    return det_bareiss(rows)

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b,p):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]=(c[i]+x)%p
    for i,x in enumerate(b): c[i]=(c[i]+x)%p
    return trim(c)

def sub(a,b,p):
    return add(a,[(-x)%p for x in b],p)

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c)

def divmod_poly(a,b,p):
    a=a[:]; b=trim([x%p for x in b])
    assert b[-1] != 0
    inv=pow(b[-1],-1,p)
    q=[0]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b) and a != [0]:
        k=len(a)-len(b); c=a[-1]*inv%p; q[k]=c
        for j in range(len(b)): a[k+j]=(a[k+j]-c*b[j])%p
        trim(a)
    return trim(q),trim(a)

def modmul(a,b,f,p):
    return divmod_poly(mul(a,b,p),f,p)[1]

def modpow(a,n,f,p):
    out=[1]; a=divmod_poly(a,f,p)[1]
    while n:
        if n&1: out=modmul(out,a,f,p)
        a=modmul(a,a,f,p); n//=2
    return out

def gcd_poly(a,b,p):
    while b != [0]:
        _,r=divmod_poly(a,b,p); a,b=b,r
    if a == [0]: return a
    inv=pow(a[-1],-1,p)
    return [(x*inv)%p for x in a]

def irreducible(f,p):
    n=len(f)-1
    if n==1: return True
    X=[0,1]
    # Rabin criterion: X^(p^n)=X and gcd(X^(p^(n/q))-X,f)=1
    z=X
    for _ in range(n): z=modpow(z,p,f,p)
    if sub(z,X,p) != [0]: return False
    m=n
    q=2
    while q*q<=m:
        if m%q==0:
            z=X
            for _ in range(n//q): z=modpow(z,p,f,p)
            if len(gcd_poly(sub(z,X,p),f,p))>1: return False
            while m%q==0: m//=q
        q+=1
    if m>1:
        z=X
        for _ in range(n//m): z=modpow(z,p,f,p)
        if len(gcd_poly(sub(z,X,p),f,p))>1: return False
    return True

H=[4,-24,64,-68,53,-44,26,-8,1]
Hprime=[-24,128,-204,212,-220,156,-56,8]
assert resultant(H,Hprime) == 2**38 * 17**2
# Q*(pi) and the transformed polynomial for -pi/(pi+1).
Qstar=[16,32,24,8,2,4,6,4,1]
transformed=[16,96,248,360,322,180,62,12,1]
assert resultant(Qstar,transformed) == 2**44
# Hence theta=pi^2/(pi^2+2*pi+2) has eight distinct conjugates:
# f(x)=f(y) implies x=y or xy+x+y=0, and the latter would make
# x a common root of Q*(x) and (x+1)^8 Q*(-x/(x+1)).
# The resultant above is nonzero. The field discriminant is
# disc(F)^2=2^16*17^2, so [O_L:Z[theta]]=2^11.
data={
 11:[([-2,5,-3,1,1],1),([-2,-4,5,2,1],1)],
 13:[([2,0,1],1),([6,-4,1],1),([-6,-3,1],1),([5,-1,1],1)],
 17:[([2,1],2),([-4,1],2),([2,1,1],1),([8,-5,1],1)],
 19:[([-7,1,1],1),([3,7,1],1),([2,8,1],1),([-1,-5,1],1)],
 23:[([-10,6,1],1),([6,-10,1],1),([5,-2,1],1),([-4,-2,1],1)]
}
for p,factors in data.items():
    product=[1]
    for f,e in factors:
        f=[x%p for x in f]
        assert irreducible(f,p), (p,f,"factor not irreducible")
        for _ in range(e): product=mul(product,f,p)
    assert [x%p for x in product] == [x%p for x in H], (p,product)
    degrees=[(len(f)-1,e) for f,e in factors]
    print(p, degrees)
print("disc(H) =",2**38*17**2)
print("[O_L:Z[theta]] = 2^11")
print("primitive-element resultant =",2**44)
print("All five modular factorizations and irreducibility checks passed.")
