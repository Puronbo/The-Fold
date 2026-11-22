#!/usr/bin/env python3
"""Exact generic-field certificate for UF-072H. Requires SymPy.

Computes the cubic initial multiplication matrix over
K = GF(2)(A,B,C,D,E,G,J), retaining Laurent exponents in a,b,i.
"""
from itertools import combinations_with_replacement
import sympy as sp

A, B, C, D, E, G, J = sp.symbols("A B C D E G J")
params = (A, B, C, D, E, G, J)
L = {
    2: ({}, {(0, 1, -1): A, (0, 0, 0): C}, {}),
    3: ({(-1, 1, 0): A, (-1, 0, 1): C},
        {(-1, 2, -1): A, (-1, 1, 0): C}, {}),
    5: ({}, {(1, 0, -1): A}, {}),
    6: ({(0, 0, 0): A}, {(0, 1, -1): A}, {}),
    7: ({(2, 0, -1): G}, {(2, 0, -1): B + G}, {}),
    8: ({(1, 0, 0): B, (1, 1, -1): G},
        {(1, 1, -1): B + G, (1, 0, 0): D}, {}),
    9: ({(2, 0, 0): J},
        {(2, 0, 0): E, (3, 0, -1): J},
        {(2, 1, -2): G, (2, 0, -1): G}),
}
indices = (2, 3, 5, 6, 7, 8, 9)
triples = list(combinations_with_replacement(indices, 3))

def multiply_triple(triple):
    product = None
    for j in triple:
        factor = {}
        for source_index, polynomial in enumerate(L[j]):
            for exponent, coefficient in polynomial.items():
                source_exp = tuple(int(q == source_index) for q in range(3))
                factor[(source_exp, exponent)] = coefficient
        if product is None:
            product = factor
            continue
        new_product = {}
        for (source, exponent), x in product.items():
            for (other_source, other_exponent), y in factor.items():
                ss = tuple(source[q] + other_source[q] for q in range(3))
                if ss[0] >= 4 or ss[1] >= 2 or ss[2] >= 2:
                    continue
                ee = tuple(exponent[q] + other_exponent[q] for q in range(3))
                key = (ss, ee)
                new_product[key] = sp.expand(new_product.get(key, 0) + x*y)
        product = {k: v for k, v in new_product.items() if v != 0}
    return product or {}

columns = [multiply_triple(t) for t in triples]
triple_rows = sorted(set(k for col in columns for k in col))

# Corrected in_3(n2*n5) = (0, a(AB+CG)/i, 0, 0).
# The Laurent exponent already records a/i; its coefficient is AB+CG.
n2n5 = {((2, 1, 0), (1, 0, -1)): A*B + C*G}

# in_3(n2*n6+n3*n5), in (c^3,c^2d,c^2h,cdh) order.
combo = {}
def add(src, exp, coeff):
    key = (src, exp)
    combo[key] = sp.expand(combo.get(key, 0) + coeff)
    if combo[key] == 0:
        del combo[key]

add((3, 0, 0), (0, 0, 0), A*B + C*G)
add((2, 1, 0), (0, 0, 0), A*D + B*C + C*G)
for exp, coeff in [
    ((0, 1, -1), A**2), ((-1, 1, -1), A**2),
    ((0, 0, 0), A*C), ((-1, 0, 0), A*C)
]:
    add((2, 0, 1), exp, coeff)
for exp, coeff in [
    ((0, 2, -2), A**2), ((-1, 2, -2), A**2),
    ((0, 1, -1), A*C), ((-1, 1, -1), A*C)
]:
    add((1, 1, 1), exp, coeff)

all_rows = sorted(set(triple_rows) | set(n2n5) | set(combo))
def build_matrix(extra=()):
    all_columns = columns + list(extra)
    return sp.MutableDenseMatrix(
        len(all_rows), len(all_columns),
        lambda r, c: all_columns[c].get(all_rows[r], 0)
    )

field = sp.GF(2).frac_field(*params)
def exact_rank(extra=()):
    dm = sp.polys.matrices.DomainMatrix.from_Matrix(build_matrix(extra)).convert_to(field)
    return dm.rank()

print("triple columns:", len(columns))
print("source/Laurent rows:", len(all_rows))
print("triple map rank:", exact_rank())
print("plus corrected in_3(n2*n5):", exact_rank((n2n5,)))
print("plus in_3(n2*n6+n3*n5):", exact_rank((combo,)))
print("plus both:", exact_rank((n2n5, combo)))
