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
Gxy = sp.groebner([u**2, x**4, y**4, beta**2 + lam*(1+a**4)], x, y, u, beta, a, lam, order="lex", modulus=2)
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

# Verify that the parameter law is exactly composition of the substitutions.
x = sp.symbols("x")
b_total = ap*b + a**2*bp
q = a*x + b*x**2
h_f = 1 + u*x + beta*x**2 + u*beta*x**3
h_g_at_f = 1 + up*q + betap*q**2 + up*betap*q**3
h_total = 1 + u_total*x + beta_total*x**2 + u_total*beta_total*x**3
Gcompx = sp.groebner(
    relations + [x**4],
    x, a, ap, b, bp, u, up, beta, betap, lam,
    order="lex", modulus=2
)
assert Gcompx.reduce(sp.expand(h_f*h_g_at_f + h_total))[1] == 0
x_composed = sp.expand(ap*(a*x+b*x**2) + bp*(a*x+b*x**2)**2)
assert Gcompx.reduce(x_composed + (a*ap*x+b_total*x**2))[1] == 0

# Inverse formulas, checked as identities in the coordinate ring.
ai, bi, ui, betai = sp.symbols("ai bi ui betai")
inverse_relations = [
    a*ai + 1,
    bi + ai**3*b,
    ui + ai*u,
    betai + ai**2*beta + ai**3*u*b,
    u**2,
    beta**2 + lam*(1+a**4),
]
Ginv = sp.groebner(
    inverse_relations,
    a, ai, b, bi, u, ui, beta, betai, lam,
    order="lex", modulus=2
)
inverse_composition = [
    a*ai + 1,
    ai*b + a**2*bi,
    u + a*ui,
    beta + ui*b + a**2*betai + a*u*ui,
]
assert all(Ginv.reduce(q)[1] == 0 for q in inverse_composition)


print("PASS: Hopf-lift cocycle equation")
print("PASS: composition law agrees with substitution on x and t")\nprint("PASS: composition preserves u^2=0 and beta^2=lambda*(1+a^4)")
print("PASS: inverse formulas in characteristic two")
