#!/usr/bin/env python3
"""Exact generic degree-three pair-product certificate for UF-072I.

Requires SymPy. Uses K=GF(2)(A,B,C,D,E,G,J), with a,b,i retained
as Laurent monomial exponents. The source truncation is c^4=d^2=h^2=0.
"""
from itertools import combinations_with_replacement
import sympy as sp

A, B, C, D, E, G, J = sp.symbols("A B C D E G J")
params = (A, B, C, D, E, G, J)
L = {
    2: ({}, {(0,1,-1):A, (0,0,0):C}, {}),
    3: ({(-1,1,0):A, (-1,0,1):C},
        {(-1,2,-1):A, (-1,1,0):C}, {}),
    5: ({}, {(1,0,-1):A}, {}),
    6: ({(0,0,0):A}, {(0,1,-1):A}, {}),
    7: ({(2,0,-1):G}, {(2,0,-1):B+G}, {}),
    8: ({(1,0,0):B, (1,1,-1):G},
        {(1,1,-1):B+G, (1,0,0):D}, {}),
    9: ({(2,0,0):J}, {(2,0,0):E, (3,0,-1):J},
        {(2,1,-2):G, (2,0,-1):G}),
}
indices = (2,3,5,6,7,8,9)
triples = list(combinations_with_replacement(indices,3))

def add_poly(p, q):
    out = dict(p)
    for e, x in q.items():
        out[e] = sp.expand(out.get(e,0) + x)
        if out[e] == 0:
            del out[e]
    return out

def mul_poly(p, q):
    out = {}
    for e, x in p.items():
        for f, y in q.items():
            ef = tuple(e[k]+f[k] for k in range(3))
            out[ef] = sp.expand(out.get(ef,0) + x*y)
            if out[ef] == 0:
                del out[ef]
    return out

def multiply_triple(triple):
    product = None
    for j in triple:
        factor = {}
        for source_index, polynomial in enumerate(L[j]):
            for exponent, coefficient in polynomial.items():
                source = tuple(int(q == source_index) for q in range(3))
                factor[(source, exponent)] = coefficient
        if product is None:
            product = factor
            continue
        new = {}
        for (s,e), x in product.items():
            for (t,f), y in factor.items():
                ss = tuple(s[q]+t[q] for q in range(3))
                if ss[0]>=4 or ss[1]>=2 or ss[2]>=2:
                    continue
                ee = tuple(e[q]+f[q] for q in range(3))
                key=(ss,ee)
                new[key]=sp.expand(new.get(key,0)+x*y)
        product={k:v for k,v in new.items() if v!=0}
    return product or {}

def encode_degree3(c3, c2d, c2h, cdh):
    out={}
    for source, poly in [((3,0,0),c3),((2,1,0),c2d),
                         ((2,0,1),c2h),((1,1,1),cdh)]:
        for exponent, coefficient in poly.items():
            if coefficient:
                out[(source,exponent)] = coefficient
    return out

triple_cols=[multiply_triple(t) for t in triples]

# Quadratic initial parts:
# n1 = (A/a)c^2 + (Ab/(ai)+C/a)cd + higher;
# n4 = (A/i)cd + higher.
q1_c2={(-1,0,0):A}
q1_cd={(-1,1,-1):A,(-1,0,0):C}
q4_cd={(0,0,-1):A}

pair_cols=[]
pair_labels=[]
for j in indices:
    lc,ld,lh=L[j]
    c3=mul_poly(q1_c2,lc)
    c2d=add_poly(mul_poly(q1_c2,ld),mul_poly(q1_cd,lc))
    c2h=mul_poly(q1_c2,lh)
    cdh=mul_poly(q1_cd,lh)
    pair_cols.append(encode_degree3(c3,c2d,c2h,cdh))
    pair_labels.append("n1*n"+str(j))
for j in indices:
    lc,ld,lh=L[j]
    c2d=mul_poly(q4_cd,lc)
    cdh=mul_poly(q4_cd,lh)
    pair_cols.append(encode_degree3({},c2d,{},cdh))
    pair_labels.append("n4*n"+str(j))

# Corrected cubic initial vector of n2*n5.
n2n5={( (2,1,0),(1,0,-1) ):A*B+C*G}

# Cubic initial vector of n2*n6+n3*n5.
combo={}
def add(src,exp,coef):
    key=(src,exp)
    combo[key]=sp.expand(combo.get(key,0)+coef)
    if combo[key]==0:
        del combo[key]
add((3,0,0),(0,0,0),A*B+C*G)
add((2,1,0),(0,0,0),A*D+B*C+C*G)
for exp,coef in [((0,1,-1),A**2),((-1,1,-1),A**2),
                 ((0,0,0),A*C),((-1,0,0),A*C)]:
    add((2,0,1),exp,coef)
for exp,coef in [((0,2,-2),A**2),((-1,2,-2),A**2),
                 ((0,1,-1),A*C),((-1,1,-1),A*C)]:
    add((1,1,1),exp,coef)

all_cols=triple_cols+pair_cols+[n2n5,combo]
all_labels=[str(t) for t in triples]+pair_labels+["n2*n5","n2*n6+n3*n5"]
all_rows=sorted(set(k for col in all_cols for k in col))
matrix=sp.MutableDenseMatrix(len(all_rows),len(all_cols),
    lambda r,c: all_cols[c].get(all_rows[r],0))
field=sp.GF(2).frac_field(*params)
dm=sp.polys.matrices.DomainMatrix.from_Matrix(matrix).convert_to(field)
rref,pivots=dm.rref()
base=sp.polys.matrices.DomainMatrix.from_Matrix(
    sp.MutableDenseMatrix(len(all_rows),len(triple_cols),
        lambda r,c: all_cols[c].get(all_rows[r],0))).convert_to(field)
print("triple map rank:",base.rank())
print("plus 14 n1/n4 pair columns:",dm.rank() if False else
      sp.polys.matrices.DomainMatrix.from_Matrix(
        sp.MutableDenseMatrix(len(all_rows),len(triple_cols)+len(pair_cols),
            lambda r,c: all_cols[c].get(all_rows[r],0))).convert_to(field).rank())
print("plus all 14 and n2*n5:",sp.polys.matrices.DomainMatrix.from_Matrix(
    sp.MutableDenseMatrix(len(all_rows),len(triple_cols)+len(pair_cols)+1,
        lambda r,c: all_cols[c].get(all_rows[r],0))).convert_to(field).rank())
print("plus all 14 and both corrected relation vectors:",dm.rank())
print("independent added columns:",[all_labels[k] for k in pivots if k>=len(triple_cols)])
