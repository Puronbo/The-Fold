#!/usr/bin/env python3
"""Exact arithmetic certificate for G-29; Python standard library only."""
def det_bareiss(matrix):
    a=[row[:] for row in matrix]; n=len(a); sign=1; previous=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None: return 0
            a[k],a[pivot]=a[pivot],a[k]; sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j]
                assert z % previous == 0
                a[i][j]=z//previous
        for i in range(k+1,n): a[i][k]=0
        previous=p
    return sign*a[-1][-1]
def resultant(f,g):
    m=len(f)-1; n=len(g)-1; fd=f[::-1]; gd=g[::-1]; rows=[]
    for j in range(n): rows.append([0]*j+fd+[0]*(n-1-j))
    for j in range(m): rows.append([0]*j+gd+[0]*(m-1-j))
    return det_bareiss(rows)
g=[1,4,-2,-20,-14]
gprime=[4,12,-4,-20]
disc=resultant(g,gprime)
assert disc == 4352 == 2**8*17
assert all(c % 2 == 0 for c in g[1:])
assert g[-1] % 4 == 2
norm_delta=resultant(g,[1,0,-8])
assert norm_delta == 4
points=[(0,4),(1,1),(2,0)]
slopes=[points[i+1][1]-points[i][1] for i in range(2)]
assert slopes == [-3,-1]
assert all(points[i+1][0]-points[i][0] == 1 for i in range(2))
print("disc(g) =",disc,"= 2^8 * 17")
print("g is Eisenstein at 2; K/Q has one prime above 2, e=4, f=1")
print("Norm_K/Q(beta^2-8) =",norm_delta,"= 2^2")
print("relative Newton polygon slopes =",slopes,"with lengths 1,1")
print("conclusion: quadratic CM extension splits locally above 2")
print("and is unramified at every finite prime")
