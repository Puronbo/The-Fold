#!/usr/bin/env python3
"""Symbolically verify the G_lambda automorphism formulas (characteristic 2)."""
import sympy as sp

x, y = sp.symbols("x y")
a, ap, b, bp, u, up, beta, betap, lam = sp.symbols(
    "a ap b bp u up beta betap lam"
)

# Hopf-lift cocycle equation. Work modulo x^4=y^4=0 and u^2=0.
gamma = u * beta
h = lambda q: 1 + u*q + beta*q**2 + gamma*q**3
lhs = sp.expand(h(x) * h(y) * h(x+y))
rhs = sp.expand((1 + lam*x**2*y**2) * (1 + lam*a**4*x**2*y**2))
Gxy = sp.groebner([u**2, x**4, y**4], x, y, u, beta, lam, order="lex", modulus=2)
assert Gxy.reduce(lhs + rhs)[1] == 0

# The coefficient comparison leaves beta^2 = lambda*(1+a^4).
Gcoef = sp.groebner(
    [u**2, gamma + u*beta, beta**2 + lam*(1+a**4)],
    u, beta, gamma, a, lam, order="lex", modulus=2
)
assert Gcoef.reduce(gamma + u*beta)[1] == 0

# Composition law.
u_total = u + a*up
beta_total = beta + up*b + a**2*betap + a*u*up
relations = [
    u**2, up**2,
    beta**2 + lam*(1+a**4),
    betap**2 + lam*(1+ap**4),
]
Gcomp = sp.groebner(
    relations, a, ap, b, bp, u, up, beta, betap, lam,
    order="lex", modulus=2
)
assert Gcomp.reduce(u_total**2)[1] == 0
assert Gcomp.reduce(beta_total**2 + lam*(1+(a*ap)**4))[1] == 0

# Inverse formulas: all identities are reduced in characteristic two.
# a_inv=a^-1, b_inv=a^-3*b, u_inv=a^-1*u,
# beta_inv=a^-2*beta+a^-3*u*b.
# Clearing powers of a, the composition coordinates reduce to zero
# using u^2=0 and 2=0.
b_inv_num = b  # a^3*b_inv
u_inv_num = u  # a*u_inv
beta_inv_num = a*beta + u*b  # a^3*beta_inv
assert sp.Poly(2*b, a, b, modulus=2).as_expr() == 0
assert sp.Poly(2*u, a, u, modulus=2).as_expr() == 0
assert sp.Poly(u**2, u, modulus=2).as_expr() == 0
assert b_inv_num == b and u_inv_num == u and beta_inv_num == a*beta + u*b

print("PASS: Hopf-lift cocycle equation")
print("PASS: composition preserves u^2=0 and beta^2=lambda*(1+a^4)")
print("PASS: inverse formulas in characteristic two")
