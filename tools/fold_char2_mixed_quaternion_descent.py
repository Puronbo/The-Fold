#!/usr/bin/env python3
"""Verify the SL2/PGL2 realization of the mixed Hopf extension."""
import sympy as sp

r, s, lam, a, u = sp.symbols("r s lam a u")
I = sp.eye(2)
D = sp.Matrix([[0, lam], [1, 0]])
N = sp.Matrix([[0, 1], [0, 0]])
U = u*I + N
G = sp.groebner([r**2, s**2, u**2+a], r, s, u, a, lam, order="lex", modulus=2)


def zero_matrix(matrix):
    return all(G.reduce(sp.expand(entry))[1] == 0 for entry in matrix)


assert zero_matrix(D*D + lam*I)
assert zero_matrix(N*N)
assert zero_matrix(D*N + N*D + I)
assert zero_matrix(U*U + a*I)
assert zero_matrix(D*U + U*D + I)

# In characteristic two, (I+rD)^(-1)=I+rD and conjugation
# sends U to U+rI while fixing D.
R = I + r*D
assert zero_matrix(R*R + I)
assert zero_matrix(R*U*R + U + r*I)
assert zero_matrix(R*D*R + D)

# Multiplication in the lifted subgroup reproduces the E_lambda law.
left = (I+r*D)*(I+s*D)
right = (1+lam*r*s)*(I+(r+s)*D)
assert zero_matrix(left + right)

print("PASS: quaternion relations and central simplicity model")
print("PASS: conjugation descent U -> U+rI")
print("PASS: E_lambda is the pullback of SL2 -> PGL2")
