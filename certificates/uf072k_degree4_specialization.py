#!/usr/bin/env python3
"""Corrected finite-field degree-four test for UF-072L. Requires SymPy.

Builds the complete degree-four initial span of N^3:
  (i) cubic products with one quadratic correction,
  (ii) n1 or n4 times two first-order generators,
  (iii) all fourfold products of first-order generators.
Then tests in_4(n1*n4). Ranks are specialization certificates only.
"""
from itertools import combinations_with_replacement
import sympy as sp

A,B,C,D,E,G,J=sp.symbols("A B C D E G J")
params=(A,B,C,D,E,G,J)
# Laurent exponents are ordered (a,b,i); source exponents are (c,d,h).
L={
2: ({},{(0,1,-1):A,(0,0,0):C},{}),
3: ({(-1,1,0):A,(-1,0,1):C},{(-1,2,-1):A,(-1,1,0):C},{}),
5: ({},{(1,0,-1):A},{}),
6: ({(0,0,0):A},{(0,1,-1):A},{}),
7: ({(2,0,-1):G},{(2,0,-1):B+G},{}),
8: ({(1,0,0):B,(1,1,-1):G},{(1,1,-1):B+G,(1,0,0):D},{}),
9: ({(2,0,0):J},{(2,0,0):E,(3,0,-1):J},
    {(2,1,-2):G,(2,0,-1):G})
}
idx=tuple(L)
# Quadratic source terms for n_j in source order c^2, cd, ch, dh.
Q={
2: [{(0,0,0):B,(0,1,-1):G},{},
    {(-1,1,-1):A,(-1,0,0):C},
    {(-1,2,-2):A,(-1,1,-1):C}],
3: [{(-1,0,1):D,(-1,2,-1):G,(-1,1,0):G},{},
    {(-2,2,-1):A,(-2,1,0):C},
    {(-2,2,-2):A,(-2,1,-1):C}],
5: [{(1,0,-1):G},{},{(0,0,-1):A},
    {(0,1,-2):A,(0,0,-1):C}],
6: [{(0,0,0):B+G,(0,1,-1):G},{},
    {(-1,1,-1):A,(-1,0,0):C},
    {(-1,2,-2):A,(-1,1,-1):C}],
7: [{},{(2,0,-1):J},
    {(1,0,-1):B,(1,1,-2):G},
    {(0,1,-1):D,(0,2,-2):B+G}],
8: [{(1,0,0):J},
    {(2,0,-1):E,(1,1,-1):J},
    {(0,1,-1):B,(0,2,-2):G},
    {(0,1,-1):D,(0,2,-2):B+G}],
9: [{},{},
    {(2,0,-1):J},
    {(2,0,-1):E,(2,1,-2):J}]
}
def clean(p):
    return {e:sp.expand(v) for e,v in p.items() if sp.expand(v)!=0}
def padd(p,q):
    z=dict(p)
    for e,v in q.items(): z[e]=z.get(e,0)+v
    return clean(z)
def pmul(p,q):
    z={}
    for e,v in p.items():
        for f,w in q.items():
            g=tuple(e[k]+f[k] for k in range(3))
            z[g]=z.get(g,0)+v*w
    return clean(z)
def sadd(p,q):
    z=dict(p)
    for k,v in q.items(): z[k]=z.get(k,0)+v
    return {k:sp.expand(v) for k,v in z.items() if sp.expand(v)!=0}
def smul(p,q):
    z={}
    for (s,e),v in p.items():
        for (t,f),w in q.items():
            u=tuple(s[k]+t[k] for k in range(3))
            if u[0]>=4 or u[1]>=2 or u[2]>=2: continue
            key=(u,tuple(e[k]+f[k] for k in range(3)))
            z[key]=z.get(key,0)+v*w
    return {k:sp.expand(v) for k,v in z.items() if sp.expand(v)!=0}
def lin(j):
    z={}
    for k,p in enumerate(L[j]):
        s=tuple(int(r==k) for r in range(3))
        for e,v in p.items(): z[(s,e)]=v
    return z
def quad(j):
    z={}
    src=((2,0,0),(1,1,0),(1,0,1),(0,1,1))
    for s,p in zip(src,Q[j]):
        for e,v in p.items():
            if v: z[(s,e)]=v
    return z
cols=[]
# Three-generator products: exactly one quadratic term contributes in degree four.
for tri in combinations_with_replacement(idx,3):
    z={}
    for k,j in enumerate(tri):
        others=[tri[r] for r in range(3) if r!=k]
        z=sadd(z,smul(smul(quad(j),lin(others[0])),lin(others[1])))
    cols.append(z)
# n1 and n4 leading quadratic terms times any pair of first-order generators.
n1={((2,0,0),(-1,0,0)):A,
    ((1,1,0),(-1,1,-1)):A,((1,1,0),(-1,0,0)):C}
n4={((1,1,0),(0,0,-1)):A}
for base in (n1,n4):
    for pair in combinations_with_replacement(idx,2):
        cols.append(smul(smul(base,lin(pair[0])),lin(pair[1])))
# Fourfold products are required because N^3 is an ideal.
for quadidx in combinations_with_replacement(idx,4):
    z=lin(quadidx[0])
    for j in quadidx[1:]: z=smul(z,lin(j))
    cols.append(z)
# in_4(n1*n4) = A^2/(a*i) c^3 d.
target={((3,1,0),(-1,0,-1)):A**2}
rows=sorted(set(k for col in cols+[target] for k in col))
# F_256 = F_2[u]/(u^8+u^4+u^3+u^2+1).
MOD=0x11D
def mul(x,y):
    z=0
    while y:
        if y&1:z^=x
        y>>=1; x<<=1
        if x&0x100:x^=MOD
    return z
def power(x,n):
    z=1
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x); n>>=1
    return z
def inv(x):
    if not x: raise ZeroDivisionError
    return power(x,254)
def evaluate(expr,values):
    out=0
    for mon,co in sp.Poly(expr,*params,modulus=2).terms():
        term=int(co)%2
        for x,n in zip(values,mon):
            if n: term=mul(term,power(x,n))
        out^=term
    return out
def rank(mat):
    a=[r[:] for r in mat]; m=len(a); n=len(a[0]); k=0
    for c in range(n):
        p=next((r for r in range(k,m) if a[r][c]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k]
        z=inv(a[k][c]); a[k]=[mul(x,z) for x in a[k]]
        for r in range(m):
            if r!=k and a[r][c]:
                z=a[r][c]
                a[r]=[x^mul(z,y) for x,y in zip(a[r],a[k])]
        k+=1
        if k==m: break
    return k
specializations=[
(0xD9,0xC5,0xC3,0xD7,0x14,0x84,0x9B),
(0x31,0x72,0xA4,0x5B,0xE1,0x93,0xC7),
(0xA1,0x3D,0x6F,0xE3,0x55,0xB2,0x19)]
for values in specializations:
    M=[[evaluate(col.get(row,0),values) for col in cols] for row in rows]
    Mv=[r+[evaluate(target.get(rows[k],0),values)]
        for k,r in enumerate(M)]
    print(values, "N^3 degree-four rank",rank(M),
          "with n1*n4",rank(Mv))
