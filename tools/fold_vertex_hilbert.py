#!/usr/bin/env python3
"""UF-019 checks for the Hilbert function at the Fold vertex."""
import sympy as s

# Basis: 1, x, y, xy, x^2, x^2y, x^3, x^3y.
X = s.Matrix([
[0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
])
Y = s.Matrix([
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,-1,0,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,-1,0,0,0,0],
[0,0,0,0,0,0,1,0],
])
unit = s.eye(8)[:,0]
layers = [[unit]]
for d in range(1,6):
    layers.append([w for v in layers[-1] for w in (X*v,Y*v)])
mdims=[]
for d in range(6):
    cols=[v for layer in layers[d:] for v in layer]
    mat=s.Matrix.hstack(*cols) if cols else s.zeros(8,0)
    mdims.append(mat.rank())
hilbert=[mdims[d]-mdims[d+1] for d in range(5)]
assert hilbert == [1,2,2,2,1]
assert mdims == [8,7,5,3,1,0]
assert X**4 == s.zeros(8) and Y**4 == s.zeros(8)
assert X**3*Y != s.zeros(8)
print("UF-019: PASS")
print("m-adic dimensions:", mdims)
print("Hilbert function:", hilbert)
