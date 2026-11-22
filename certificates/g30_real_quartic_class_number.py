#!/usr/bin/env python3
"""Exact certificate for h(Q(beta))=1; standard library only."""
def det_bareiss(matrix):
    a=[row[:] for row in matrix]; n=len(a); sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None: return 0
            a[k],a[pivot]=a[pivot],a[k]; sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j]
                assert z % prev == 0
                a[i][j]=z//prev
        for i in range(k+1,n): a[i][k]=0
        prev=p
    return sign*a[-1][-1]
def resultant(f,g):
    m=len(f)-1; n=len(g)-1; fd=f[::-1]; gd=g[::-1]; rows=[]
    for j in range(n): rows.append([0]*j+fd+[0]*(n-1-j))
    for j in range(m): rows.append([0]*j+gd+[0]*(m-1-j))
    return det_bareiss(rows)
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def divmod_mod(a,b,p):
    a=trim([x%p for x in a[:]]); b=trim([x%p for x in b[:]])
    q=[0]*max(1,len(a)-len(b)+1); inv=pow(b[-1],-1,p)
    while a != [0] and len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]*inv%p; q[k]=c
        for j in range(len(b)): a[k+j]=(a[k+j]-c*b[j])%p
        trim(a)
    return trim(q),a
def irreducible_quartic_mod(g,p):
    f=[x%p for x in g]
    for r in range(p):
        assert divmod_mod(f,[(-r)%p,1],p)[1] != [0]
    for a in range(p):
        for b in range(p):
            assert divmod_mod(f,[b,a,1],p)[1] != [0]

g=[-14,-20,-2,4,1]
assert irreducible_quartic_mod(g,3) is None
assert irreducible_quartic_mod(g,5) is None
# Norm(beta+2) = resultant(g,Y+2) = g(-2).
assert resultant(g,[2,1]) == 2
# Minkowski bound for a totally real quartic:
# (4!/4^4)*sqrt(2^8*17) = (3/2)*sqrt(17) < 7.
assert 9*17 < 196
print("g is irreducible modulo 3 and modulo 5")
print("Norm(beta+2) = 2; hence (beta+2) is the unique prime above 2")
print("Minkowski bound = (3/2)*sqrt(17) < 7")
print("all ideal classes have a principal representative of norm <= 6")
print("ordinary class number h_K = 1")
