#!/usr/bin/env python3
"""Finite-field check for the UF-072G cubic initial multiplication matrix.

No third-party packages are required.  Run with Python 3.
Field: F_256 = F_2[u]/(u^8+u^4+u^3+u^2+1).
Rows are sorted (source exponent, Laurent exponent); columns are sorted triples.
"""
from itertools import combinations_with_replacement

MOD = 0x11D
def mul(x, y):
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & 0x100:
            x ^= MOD
    return z

def power(x, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out

def inv(x):
    if not x:
        raise ZeroDivisionError
    return power(x, 254)

def rank_pivots(matrix):
    a = [row[:] for row in matrix]
    original_rows = list(range(len(a)))
    m, n = len(a), len(a[0]) if a else 0
    pivot_cols, pivot_rows = [], []
    r = 0
    for c in range(n):
        p = next((q for q in range(r, m) if a[q][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        original_rows[r], original_rows[p] = original_rows[p], original_rows[r]
        scale = inv(a[r][c])
        a[r] = [mul(x, scale) for x in a[r]]
        for q in range(m):
            if q != r and a[q][c]:
                factor = a[q][c]
                a[q] = [x ^ mul(factor, y) for x, y in zip(a[q], a[r])]
        pivot_cols.append(c)
        pivot_rows.append(original_rows[r])
        r += 1
        if r == m:
            break
    return pivot_cols, pivot_rows

def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    det = 1
    for c in range(n):
        p = next((q for q in range(c, n) if a[q][c]), None)
        if p is None:
            return 0
        if p != c:
            a[c], a[p] = a[p], a[c]
        pivot = a[c][c]
        det = mul(det, pivot)
        scale = inv(pivot)
        a[c] = [mul(x, scale) for x in a[c]]
        for q in range(c + 1, n):
            if a[q][c]:
                factor = a[q][c]
                a[q] = [x ^ mul(factor, y) for x, y in zip(a[q], a[c])]
    return det

# Parameter specialization (a,b,i,A,B,C,D,E,G,J).
v = dict(zip("ab i A B C D E G J".replace(" ", ""),
             [0xD9, 0xC5, 0xC3, 0xD7, 0x14, 0x84, 0xF8, 0xCF, 0x9B, 0xF4]))
a,b,i,A,B,C,D,E,G,J = (v[k] for k in "ab i A B C D E G J".replace(" ", ""))

# A Laurent polynomial is a dict {(exp_a,exp_b,exp_i): coefficient}.
# Each L_j is a triple (c,d,h) of Laurent polynomials.
L = {
    2: ({}, {(0,1,-1):A, (0,0,0):C}, {}),
    3: ({(-1,1,0):A, (-1,0,1):C},
        {(-1,2,-1):A, (-1,1,0):C}, {}),
    5: ({}, {(1,0,-1):A}, {}),
    6: ({(0,0,0):A}, {(0,1,-1):A}, {}),
    7: ({(2,0,-1):G}, {(2,0,-1):B^G}, {}),
    8: ({(1,0,0):B, (1,1,-1):G},
        {(1,1,-1):B^G, (1,0,0):D}, {}),
    9: ({(2,0,0):J}, {(2,0,0):E, (3,0,-1):J},
        {(2,1,-2):G, (2,0,-1):G}),
}
indices = (2,3,5,6,7,8,9)
triples = list(combinations_with_replacement(indices, 3))

def multiply_triple(triple):
    product = None
    for j in triple:
        factor = {}
        for source_index, polynomial in enumerate(L[j]):
            for exponent, coefficient in polynomial.items():
                source_exp = tuple(1 if q == source_index else 0 for q in range(3))
                factor[(source_exp, exponent)] = coefficient
        if product is None:
            product = factor
            continue
        new_product = {}
        for (s, e), x in product.items():
            for (t, f), y in factor.items():
                source = tuple(s[q] + t[q] for q in range(3))
                # c^4=d^2=h^2=0
                if source[0] >= 4 or source[1] >= 2 or source[2] >= 2:
                    continue
                exponent = tuple(e[q] + f[q] for q in range(3))
                key = (source, exponent)
                new_product[key] = new_product.get(key, 0) ^ mul(x, y)
                if not new_product[key]:
                    del new_product[key]
        product = new_product
    return product or {}

columns = [multiply_triple(t) for t in triples]
rows = sorted(set(key for column in columns for key in column))
base = [[column.get(row, 0) for column in columns] for row in rows]

# Correct cubic initial term of n_2*n_5:
# (0, a(AB+CG)/i, 0, 0), in (c^3,c^2d,c^2h,cdh).
pair_25 = {
    ((2,1,0), (1,0,-1)): mul(A,B) ^ mul(C,G)
}

# Cubic initial term of n_2*n_6+n_3*n_5, expanded in Laurent monomials.
pair_combo = {}
def add_pair(source, exponent, coefficient):
    key = (source, exponent)
    pair_combo[key] = pair_combo.get(key, 0) ^ coefficient
    if not pair_combo[key]:
        del pair_combo[key]

# c^3 coefficient AB+CG; c^2d coefficient AD+BC+CG.
add_pair((3,0,0), (0,0,0), mul(A,B) ^ mul(C,G))
add_pair((2,1,0), (0,0,0), mul(A,D) ^ mul(B,C) ^ mul(C,G))
# c^2h = A(Ab+Ci)(a+1)/(ai)
for e, coeff in [((0,1,-1),mul(A,A)),((-1,1,-1),mul(A,A)),
                 ((0,0,0),mul(A,C)),((-1,0,0),mul(A,C))]:
    add_pair((2,0,1), e, coeff)
# cdh = Ab(Ab+Ci)(a+1)/(ai^2)
for e, coeff in [((0,2,-2),mul(A,A)),((-1,2,-2),mul(A,A)),
                 ((0,1,-1),mul(A,C)),((-1,1,-1),mul(A,C))]:
    add_pair((1,1,1), e, coeff)

all_rows = sorted(set(rows) | set(pair_25) | set(pair_combo))
def matrix_with(*extra_columns):
    return [[column.get(row, 0) for column in columns] +
            [extra.get(row, 0) for extra in extra_columns]
            for row in all_rows]

m_base = [[column.get(row, 0) for column in columns] for row in all_rows]
m_25 = matrix_with(pair_25)
m_combo = matrix_with(pair_combo)
m_both = matrix_with(pair_25, pair_combo)

def certificate(matrix):
    pc, pr = rank_pivots(matrix)
    square = [[matrix[r][c] for c in pc] for r in pr]
    return len(pc), determinant(square)

print("triple map:", certificate(m_base))
print("with in_3(n2*n5):", certificate(m_25))
print("with in_3(n2*n6+n3*n5):", certificate(m_combo))
print("with both:", certificate(m_both))
