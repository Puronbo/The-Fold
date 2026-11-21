#!/usr/bin/env python3
"""Exact UF-031 checks: integral D4 restriction and characteristic-three center."""
import sympy as sp

# Coordinates (a,b,c,d,e,u,v). t=r^2 and s are integral.
T = sp.Matrix([
 [0,1,0,0,0,0,0],
 [-1,0,0,0,0,0,0],
 [0,0,0,0,-1,0,0],
 [0,0,0,-1,0,0,0],
 [0,0,-1,0,0,0,0],
 [0,0,0,0,0,0,1],
 [0,0,0,0,0,-1,0],
])
S = sp.diag(1,-1,1,-1,1,-1,1)
I = sp.eye(7)
assert T**4 == I and S**2 == I and S*T*S == T.inv()

# The D4 character lines and the two standard planes.
chi_triv = sp.Matrix([0,0,-1,0,1,0,0])
chi_minus_plus = sp.Matrix([0,0,1,0,1,0,0])
chi_minus_minus = sp.Matrix([0,0,0,1,0,0,0])
assert T*chi_triv == chi_triv and S*chi_triv == chi_triv
assert T*chi_minus_plus == -chi_minus_plus
assert S*chi_minus_plus == chi_minus_plus
assert T*chi_minus_minus == -chi_minus_minus
assert S*chi_minus_minus == -chi_minus_minus

# Standard planes (a,b) and (u,v).
E1 = sp.Matrix([[0,1],[-1,0]])
E3 = sp.Matrix([[0,1],[-1,0]])
F1 = sp.diag(1,-1)
F3 = sp.diag(-1,1)
J = E1
assert J*E1 == E3*J and J*F1 == F3*J

# Bracket forms on W=(a,b,c,d,e), with rows ordered by test vector
# and output coordinate, as in UF-030.
Bu = sp.zeros(5)
Bv = sp.zeros(5)
for i,j,val in ((0,3,1),(1,2,2),(1,4,-1)):
    Bu[i,j], Bu[j,i] = val, -val
for i,j,val in ((0,2,-1),(0,4,2),(1,3,-1)):
    Bv[i,j], Bv[j,i] = val, -val
radical_map = sp.Matrix.vstack(
    *[sp.Matrix([[Bu[i,j] for i in range(5)]]) for j in range(5)],
    *[sp.Matrix([[Bv[i,j] for i in range(5)]]) for j in range(5)]
)

def rank_mod(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix.tolist()]
    m, n, rank = len(a), len(a[0]), 0
    for col in range(n):
        pivot = next((i for i in range(rank,m) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x*inv) % p for x in a[rank]]
        for i in range(m):
            if i != rank:
                f = a[i][col]
                a[i] = [(x-f*y) % p for x,y in zip(a[i],a[rank])]
        rank += 1
        if rank == min(m,n):
            break
    return rank

assert radical_map.rank() == 5

# Verify equivariance of the integral bracket under both D4 generators.
x1 = sp.symbols("a1 b1 c1 d1 e1 u1 v1")
x2 = sp.symbols("a2 b2 c2 d2 e2 u2 v2")
def bracket(p, q):
    a,b,c,d,e,u,v = p
    A,B,C,D,E,U,V = q
    wu = a*D-A*d+2*b*C-b*E-2*B*c+B*e
    wv = -a*C+2*a*E+A*c-2*A*e-b*D+B*d
    return sp.Matrix([0,0,0,0,0,wu,wv])
p1, p2 = sp.Matrix(x1), sp.Matrix(x2)
for M in (T,S):
    lhs = bracket(M*p1, M*p2)
    rhs = M*bracket(p1,p2)
    assert all(sp.expand(z) == 0 for z in lhs-rhs)
assert rank_mod(radical_map, 3) == 4
for p in (2,5,7,11,13):
    assert rank_mod(radical_map, p) == 5

# Characteristic-three kernel generator (-1,0,1,0,1).
w = sp.Matrix([0,0,-1,0,1])
assert all(sum(int(row[i])*int(w[i]) for i in range(5)) % 3 == 0 for row in radical_map.tolist())

print("UF-031 checks passed.")
print("D4 relations and integral generator matrices verified.")
print("Restriction: 2E + 1 + chi(-,+) + chi(-,-).")
print("Radical rank is 4 mod 3 and 5 in the tested other characteristics.")
print("The new characteristic-three central line is D4-trivial.")
