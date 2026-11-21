#!/usr/bin/env python3
"""UF-018 exact fiber-stratum checks. Requires SymPy."""
import sympy as s

p, q = s.symbols("p q")
I = s.eye(8)
Mx = s.Matrix([
[0,0,0,0,0,0,-q,0],
[1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,-q],
[0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,p,0],
[0,0,0,1,0,0,0,p],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
])
My = s.Matrix([
[0,0,p,0,0,q,0,0],
[0,0,0,p,0,0,0,q],
[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,-1,0,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,-1,0,0,0,0],
[0,0,0,0,0,0,1,0],
])
basis_ops = [I, Mx, My, Mx*My, Mx**2, Mx**2*My, Mx**3, Mx**3*My]
G = s.Matrix(8, 8, lambda i,j: s.trace(basis_ops[i]*basis_ops[j]))

def jordan_sizes(A):
    return sorted([cell.rows for cell in A.jordan_cells()[1]], reverse=True)

def check(p0, q0, expected_rank, expected_x, expected_y):
    subs = {p:p0, q:q0}
    X, Y = Mx.subs(subs), My.subs(subs)
    assert G.subs(subs).rank() == expected_rank
    assert jordan_sizes(X) == expected_x
    assert jordan_sizes(Y) == expected_y

check(1, 0, 4, [2,2,1,1,1,1], [2,2,1,1,1,1])
check(2, 1, 4, [2,2,2,2], [2,2,2,2])
check(0, 0, 1, [4,4], [4,4])

# At the vertex y^2=-x^2 and x^4=0, giving a basis of eight monomials.
# Verify both specialized multiplication operators are nilpotent of index 4.
assert Mx.subs({p:0,q:0})**4 == s.zeros(8)
assert Mx.subs({p:0,q:0})**3 != s.zeros(8)
assert My.subs({p:0,q:0})**4 == s.zeros(8)
assert My.subs({p:0,q:0})**3 != s.zeros(8)

print("UF-018: PASS")
print("q=0 branch: trace rank 4, Jordan [2,2,1,1,1,1]")
print("p^2=4q branch: trace rank 4, Jordan [2,2,2,2]")
print("vertex: trace rank 1, Jordan [4,4]")
