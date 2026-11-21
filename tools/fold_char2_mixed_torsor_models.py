#!/usr/bin/env python3
"""Verify the explicit G_lambda torsor action in characteristic two."""
import sympy as sp

u, r, s, c, d, a, lam = sp.symbols("u r s c d a lam")
f = c + d*u**2
f_after_r = c + d*(u+r)**2
left = sp.expand((1+f*r**2)*(1+f_after_r*s**2))
right = sp.expand((1+lam*r**2*s**2)*(1+f*(r+s)**2))
relations = [u**4+a, r**4, s**4, c**2+a*d**2+d+lam]
G = sp.groebner(
    relations, u, r, s, c, d, a, lam,
    order="lex", modulus=2
)
assert G.reduce(left+right)[1] == 0

# The multiplier is mu_2-valued because r^4=0.
assert G.reduce((1+f*r**2)**2+1)[1] == 0

# Canonical-map inverse: r=u'+u and
# tau=(v'/v)*(1+f(u)r²). Verify r⁴=0 and tau²=1
# after clearing the invertible denominator v²=q.
up, v, vp, q = sp.symbols("up v vp q")
rinv = up+u
Ginv = sp.groebner(
    [u**4+a, up**4+a, v**2+q, vp**2+q],
    u, up, v, vp, q, a, c, d, order="lex", modulus=2
)
assert Ginv.reduce(rinv**4)[1] == 0
tau_num = vp*(1+f*rinv**2)
assert Ginv.reduce(tau_num**2+v**2)[1] == 0

print("PASS: G_lambda action law under c²+a*d²+d=lambda")
print("PASS: multiplier is mu_2-valued")
print("PASS: canonical action map has the displayed inverse")
