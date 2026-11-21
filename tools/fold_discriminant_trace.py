#!/usr/bin/env python3
"""UF-017 exact trace-discriminant verification (requires SymPy)."""
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
Ms = [I, Mx, My, Mx*My, Mx**2, Mx**2*My, Mx**3, Mx**3*My]
B = s.Matrix(8, 8, lambda i,j: s.trace(Ms[i]*Ms[j]))
expected = 2**16*q**4*(p**2-4*q)**4
assert Mx*My == My*Mx
assert Mx**2 + My**2 == p*I
assert Mx**2*My**2 == q*I
assert B == B.T
assert s.factor(B.det() - expected) == 0

x, y = s.symbols("x y")
jac = s.det(s.Matrix([
    [s.diff(x**2+y**2, v) for v in (x,y)],
    [s.diff(x**2*y**2, v) for v in (x,y)],
]))
assert s.factor(jac - 4*x*y*(x**2-y**2)) == 0
assert s.expand(jac**2 - 16*x**2*y**2*(x**2-y**2)**2) == 0
print("UF-017: PASS")
print("trace determinant =", s.factor(B.det()))
print("quotient Jacobian =", s.factor(jac))
