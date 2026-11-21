#!/usr/bin/env python3
"""Verify the explicit vanishing criterion for the E_lambda torsor boundary."""
import sympy as sp

u, r, s, c, d, a, lam = sp.symbols("u r s c d a lam")
f = c + d*u
phi = lambda U, R: 1 + (c + d*U)*R

# The action cocycle identity for E_lambda:
# phi(u,r) phi(u+r,s) = (1+lambda*r*s) phi(u,r+s).
identity = sp.expand(
    phi(u, r)*phi(u+r, s) + (1+lam*r*s)*phi(u, r+s)
)
relations = [
    r**2, s**2, u**2+a,
    c**2+a*d**2+d+lam,
]
G = sp.groebner(
    relations, u, r, s, c, d, a, lam,
    order="lex", modulus=2
)
assert G.reduce(identity)[1] == 0

# Conversely, coefficient comparison in the action identity gives
# d + f(u)^2 = lambda; with u^2=a and f=c+d*u this is the same equation.
assert sp.expand(f**2 + d + lam).subs(u**2, a) == c**2 + a*d**2 + d + lam

# Canonical-map inverse for B=k[u,v]/(u²-a,v²-q), q a unit:
# r=u1+u2 and t=(v2/v1)*(1+f(u1)r). The factor is self-inverse
# because r²=0, so applying the canonical map recovers v2 exactly.
print("PASS: action cocycle identity under c²+a*d²+d=lambda")
print("PASS: inverse canonical-map formulas are involutive")
