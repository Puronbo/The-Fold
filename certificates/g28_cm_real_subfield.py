#!/usr/bin/env python3
"""Exact CM real-subfield certificate for the genus-seven simple Weil factor.

Uses only the Python standard library. Polynomials are coefficient lists in
ascending order. The resultant is computed by reducing F(X) modulo
X^2-Y*X+2 and taking the norm from the quadratic algebra.
"""
from itertools import product

def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out

def scale(a, c):
    return [c*x for x in a]

def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def mod_poly(a, p):
    return trim([x % p for x in a])

def divmod_mod(a, b, p):
    a = mod_poly(a[:], p); b = mod_poly(b[:], p)
    assert b != [0]
    q = [0] * max(1, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        k = len(a)-len(b); c = a[-1]*inv % p; q[k] = c
        for j in range(len(b)): a[k+j] = (a[k+j]-c*b[j]) % p
        trim(a)
    return mod_poly(q,p), a

def determinant_bareiss(M):
    A = [row[:] for row in M]
    n = len(A); sign = 1; prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            pivot_row = next((i for i in range(k+1,n) if A[i][k]), None)
            if pivot_row is None: return 0
            A[k], A[pivot_row] = A[pivot_row], A[k]; sign = -sign
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = A[i][j]*pivot - A[i][k]*A[k][j]
                assert numerator % prev == 0
                A[i][j] = numerator // prev
        for i in range(k+1,n): A[i][k] = 0
        prev = pivot
    return sign*A[-1][-1]

F = [16,32,24,8,2,4,6,4,1]
# X^n = A_n(Y) X + B_n(Y) modulo X^2-YX+2.
powers = [([0],[1]), ([1],[0])]
for n in range(1,8):
    A,B = powers[n]; Ap,Bp = powers[n-1]
    powers.append((add(mul([0,1],A),scale(Ap,-2)),
                   add(mul([0,1],B),scale(Bp,-2))))
A = [0]; B = [0]
for n,c in enumerate(F):
    A = add(A,scale(powers[n][0],c))
    B = add(B,scale(powers[n][1],c))
resultant = trim(add(add(scale(mul(A,A),2),mul(mul(A,B),[0,1])),mul(B,B)))
g = [-14,-20,-2,4,1]
assert resultant == scale(mul(g,g),16), (resultant,scale(mul(g,g),16))

# g mod 3 is Phi_5. Exclude all monic degree-one and degree-two divisors.
g3 = mod_poly(g,3)
for r in range(3):
    assert divmod_mod(g3,[(-r)%3,1],3)[1] != [0]
for a,b in product(range(3), repeat=2):
    assert divmod_mod(g3,[b,a,1],3)[1] != [0]
assert g3 == [2,1,1,1,1]

# Discriminant(g) = Res(g,g') (the degree-four sign is positive).
derivative = [i*g[i] for i in range(1,len(g))]
n = len(g)-1; m = len(derivative)-1
rows = []
for j in range(m): rows.append([0]*j + g[::-1] + [0]*(m-1-j))
for j in range(n): rows.append([0]*j + derivative[::-1] + [0]*(n-1-j))
disc = determinant_bareiss(rows)
assert disc == 4352 == 2**8*17

print("resultant identity: Res_X(F, X^2-YX+2) = 16*g(Y)^2")
print("g mod 3 = Phi_5; irreducible over F_3 and hence over Q")
print("polynomial discriminant(g) =", disc, "= 2^8 * 17")
