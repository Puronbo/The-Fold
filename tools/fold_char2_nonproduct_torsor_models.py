#!/usr/bin/env python3
"""Exact characteristic-two checks for explicit G_C and G_D torsor models."""
import sympy as sp


def zero_mod2(expr, variables, relations=()):
    if relations:
        groebner = sp.groebner(
            list(relations), *variables, order="lex", modulus=2
        )
        return groebner.reduce(sp.expand(expr))[1] == 0
    return sp.Poly(sp.expand(expr), *variables, modulus=2).is_zero


# G_C: law (r,s)+(r',s')=(r+r',s+s'+r²r'²),
# action (u,v).(r,s)=(u+r,v+s+u²r²).
u, v, r, s, rp, sp_, q, p = sp.symbols("u v r s rp sp q p")
vc1 = v + s + u**2*r**2
uc1 = u + r
vc2 = vc1 + sp_ + uc1**2*rp**2
vcombined = v + s + sp_ + r**2*rp**2 + u**2*(r+rp)**2
assert zero_mod2(vc2 + vcombined, [u,v,r,s,rp,sp_])

# The parameter change u'=u+q, v'=v+q²u²+p is equivariant.
up = u + q
vp = v + q**2*u**2 + p
vp_after = vc1 + q**2*uc1**2 + p
vp_target = vp + s + up**2*r**2
assert zero_mod2(vp_after + vp_target, [u,v,r,s,q,p])

# The contracted-product coordinates are invariant under the diagonal action.
u1, v1 = sp.symbols("u1 v1")
U = u + u1
V = v + v1 + u**2*u1**2
U_shift = (u+r) + (u1+r)
V_shift = (v+s+u**2*r**2) + (v1+s+u1**2*r**2) + (u+r)**2*(u1+r)**2
assert zero_mod2(U_shift + U, [u,u1,r])
assert zero_mod2(V_shift + V, [u,u1,r,v,v1,s], [r**4])

# Canonical-map inverse parameters satisfy r^4=s^2=0.
a, b, u2, v2 = sp.symbols("a b u2 v2")
r_inv = u2 + u
s_inv = v2 + v + u**2*r_inv**2
assert zero_mod2(r_inv**4, [u,u2,a], [u**4+a, u2**4+a])
assert zero_mod2(
    s_inv**2, [u,u2,v,v2,a,b],
    [u**4+a, u2**4+a, v**2+b, v2**2+b]
)

# G_D: law (r,s)+(r',s')=(r+r'+ss',s+s'),
# action (u,v).(r,s)=(u+s,v+r+us).
ud1 = u + s
vd1 = v + r + u*s
vd2 = vd1 + rp + ud1*sp_
vdcombined = v + r + rp + s*sp_ + u*(s+sp_)
assert zero_mod2(vd2 + vdcombined, [u,v,r,s,rp,sp_])

# The parameter change u'=u+q, v'=v+qu+p is equivariant.
up = u + q
vp = v + q*u + p
vp_after = vd1 + q*ud1 + p
vp_target = vp + r + up*s
assert zero_mod2(vp_after + vp_target, [u,v,r,s,q,p])

# The G_D contracted-product coordinates are invariant diagonally.
U = u + u1
V = v + v1 + u*u1
U_shift = (u+s) + (u1+s)
V_shift = (v+r+u*s) + (v1+r+u1*s) + (u+s)*(u1+s)
assert zero_mod2(U_shift + U, [u,u1,s])
assert zero_mod2(V_shift + V, [u,u1,v,v1,r,s], [s**2])

# Canonical-map inverse parameters satisfy s^2=r^4=0.
s_inv = u2 + u
r_inv = v2 + v + u*s_inv
assert zero_mod2(s_inv**2, [u,u2,a], [u**2+a, u2**2+a])
assert zero_mod2(
    r_inv**4, [u,u2,v,v2,a,b],
    [u**2+a, u2**2+a, v**4+b, v2**4+b]
)

print("PASS: G_C action, torsor inverse, parameter equivalence, and addition")
print("PASS: G_D action, torsor inverse, parameter equivalence, and addition")
