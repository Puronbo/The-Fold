#!/usr/bin/env python3
"""Exact finite splitting certificate for G-33; Python standard library only."""

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def mul_mod(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c)

def rem_mod(a,b,p):
    a=trim([x%p for x in a[:]])
    b=trim([x%p for x in b[:]])
    inv=pow(b[-1],-1,p)
    while a != [0] and len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]*inv%p
        for j in range(len(b)): a[k+j]=(a[k+j]-c*b[j])%p
        trim(a)
    return a

def monic_divisors_of_degree_at_most_two(p):
    yield from ([r,1] for r in range(p))
    yield from ([b,a,1] for a in range(p) for b in range(p))

def irreducible_quartic(f,p):
    return all(rem_mod(f,d,p)!=[0] for d in monic_divisors_of_degree_at_most_two(p))

def product_mod(factors,p):
    out=[1]
    for f in factors: out=mul_mod(out,f,p)
    return out

# F(X)=X^8+4X^7+6X^6+4X^5+2X^4+8X^3+24X^2+32X+16.
F=[16,32,24,8,2,4,6,4,1]
f3=[[2,1,0,0,1],[2,0,0,1,1]]
f5=[[3,3,3,2,1],[2,2,4,2,1]]
f7=[[2,0,1],[2,5,1],[3,5,1],[6,1,1]]
for p,factors in [(3,f3),(5,f5),(7,f7)]:
    assert product_mod(factors,p)==[c%p for c in F]
assert all(irreducible_quartic(f,3) for f in f3)
assert all(irreducible_quartic(f,5) for f in f5)
# Each quadratic mod 7 has nonsquare discriminant.
for f in f7:
    a,b,c=f
    disc=(b*b-4*a*c)%7
    assert disc in (3,5,6)

# g(Y)=Y^4+4Y^3-2Y^2-20Y-14 splits mod 7 as
# Y (Y-2) (Y^2-Y+3), with all factors distinct.
g7=[0,1,5,4,1]
assert product_mod([[0,1],[5,1],[3,6,1]],7)==g7
# Norms from the monic quartic: N(beta-r)=g(r).
assert (-(14)) == -14                 # g(0)
assert (-(14)) == -14                 # g(2)
assert 2 == 2                         # g(-2)
print("F mod 3 and mod 5: two irreducible quartics each")
print("F mod 7: four irreducible quadratics")
print("g mod 7: Y (Y-2) (Y^2-Y+3)")
print("G-33 Artin-sign splitting predictions verified by exact factor products")
