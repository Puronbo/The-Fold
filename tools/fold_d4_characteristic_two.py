#!/usr/bin/env python3
"""Exact characteristic-two checks for UF-032."""
from itertools import product

# Coordinates (a,b,c,d,e,u,v); matrices act on column vectors.
T = [
    [0, 1, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, -1, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, -1, 0],
]
S = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 1],
]

def mm(A, B, p=None):
    C = [[sum(A[i][k]*B[k][j] for k in range(len(B)))
          for j in range(len(B[0]))] for i in range(len(A))]
    return C if p is None else [[x % p for x in row] for row in C]

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def rank_mod(A, p):
    a = [[x % p for x in row] for row in A]
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x*inv) % p for x in a[r]]
        for i in range(m):
            if i != r:
                q = a[i][c]
                a[i] = [(x-q*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r

# Integral D4 relations.
T2 = mm(T, T)
T4 = mm(T2, T2)
S2 = mm(S, S)
STS = mm(mm(S, T), S)
Tinv = mm(T2, T2)  # T^4=I, hence T^{-1}=T^3; checked explicitly below.
T3 = mm(T2, T)
assert T4 == ident(7)
assert S2 == ident(7)
assert STS == T3

# Reduce generators modulo 2.
t = [[x % 2 for x in row] for row in T]
s = [[x % 2 for x in row] for row in S]
assert s == ident(7)
assert mm(t, t, 2) == ident(7)
assert rank_mod([[ (t[i][j] - int(i == j)) for j in range(7)]
                 for i in range(7)], 2) == 3

# Bracket tables, keyed by i<j, outputs in (u,v).
# Index order: a,b,c,d,e,u,v.
br = {
    (0, 3): (1, 0), (1, 2): (2, 0), (1, 4): (-1, 0),
    (0, 2): (0, -1), (0, 4): (0, 2), (1, 3): (0, -1),
}
def bracket_basis(i, j):
    if i == j:
        return (0, 0)
    if i > j:
        x, y = bracket_basis(j, i)
        return (-x, -y)
    return br.get((i, j), (0, 0))

# Build the 10x5 radical equation matrix over F2: B(z,e_j)=0.
rad = []
for j in range(5):
    for out in range(2):
        row = []
        for i in range(5):
            val = bracket_basis(i, j)[out]
            row.append(val % 2)
        rad.append(row)
assert rank_mod(rad, 2) == 5

# Surviving bracket table mod 2.
survivors = {(i, j): tuple(x % 2 for x in val)
             for (i, j), val in br.items()
             if any(x % 2 for x in val)}
assert survivors == {
    (0, 3): (1, 0),  # [a,d]=u
    (1, 4): (1, 0),  # [b,e]=u
    (0, 2): (0, 1),  # [a,c]=v
    (1, 3): (0, 1),  # [b,d]=v
}

# Check equivariance on all 49 pairs of basis vectors.
def act_basis(G, i):
    return [(j, G[j][i] % 2) for j in range(7) if G[j][i] % 2]

def bracket_vectors(x, y):
    out = [0, 0]
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            if i < j:
                val = bracket_basis(i, j)
                out[0] += xi*yj*val[0]
                out[1] += xi*yj*val[1]
            elif i > j:
                val = bracket_basis(j, i)
                out[0] -= xi*yj*val[0]
                out[1] -= xi*yj*val[1]
    return tuple(z % 2 for z in out)

def act_output(G, uv):
    # The output center coordinates are positions 5,6.
    return (G[5][5]*uv[0] + G[5][6]*uv[1],
            G[6][5]*uv[0] + G[6][6]*uv[1])

for G in (t, s):
    for i, j in product(range(7), repeat=2):
        x = [0]*7; x[i] = 1
        y = [0]*7; y[j] = 1
        lhs = act_output(G, bracket_vectors(x, y))
        gx = [sum(G[row][col]*x[col] for col in range(7)) % 2
              for row in range(7)]
        gy = [sum(G[row][col]*y[col] for col in range(7)) % 2
              for row in range(7)]
        rhs = bracket_vectors(gx, gy)
        assert lhs == rhs, (G, i, j, lhs, rhs)

print("UF-032 exact checks passed over F_2.")
print("D4 action factors through C2; module = 3 J2 + J1.")
print("Bracket image = center = span(u,v), dimension 2.")
print("Quotient radical is zero; bracket remains D4-equivariant.")
