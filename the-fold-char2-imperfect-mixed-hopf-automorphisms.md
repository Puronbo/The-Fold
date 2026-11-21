# Automorphism group scheme of the imperfect mixed Hopf family

Let k have characteristic two and
\[
A=k[x,t]/(x^4,t^2-1),\qquad
\Delta(x)=x\otimes1+1\otimes x,\quad
\Delta(t)=(t\otimes t)(1+\lambda x^2\otimes x^2).
\]
Write \(G_\lambda=\operatorname{Spec}A\).

## Theorem 1. Full group-scheme automorphism functor

For every k-algebra R, every group-scheme automorphism of \((G_\lambda)_R\) is uniquely of the form
\[
x\longmapsto ax+bx^2,\qquad
t\longmapsto t(1+ux+\beta x^2+u\beta x^3),
\]
where \(a\in R^\times\), \(b,u,\beta\in R\), and
\[
u^2=0,\qquad \beta^2=\lambda(1+a^4).
\]
Consequently
\[
\operatorname{Aut}_{\rm grp}(G_\lambda)
=\operatorname{Spec}
k[a,a^{-1},b,u,\beta]/(u^2,\ \beta^2+\lambda(1+a^4)).
\]
It has dimension two and tangent dimension four at the identity. Its reduced support has dimension two. The parameters \(u,\beta\) record infinitesimal homomorphisms and lifts; they cannot be discarded by checking only field-valued points.

### Proof

The subgroup \(\mu_2=\ker(G_\lambda\to\alpha_4)\) is the unique subgroup of multiplicative type of rank two: every map \(\mu_2\to\alpha_4\) is trivial. It is therefore characteristic. The quotient is \(\alpha_4\), whose automorphisms over R have
\[
X=ax+bx^2,\qquad a\in R^\times.
\]
The restriction to the kernel is the identity because \(\operatorname{Aut}(\mu_2)\) is trivial.

Write the image of (t) initially as (p(x)+tq(x)), with (p(0)=0) and (q(0)=1). In the Hopf identity for this image, the component in the (1otimes t) summand is (p(x)otimes q(y)) times a unit. The coproduct of (p(x)+tq(x)) has no such mixed component. Since (q) is a unit, this forces (p=0). Thus the image is (t h(x)), where (h=q) is a normalized (mu_2)-valued function on (alpha_4). Write
\[
h(x)=1+ux+\beta x^2+\gamma x^3.
\]
The relation \(h^2=1\) gives \(u^2=0\). The Hopf condition is
\[
h(x)h(y)h(x+y)
=(1+\lambda x^2y^2)(1+\lambda a^4x^2y^2).
\]
Using \(u^2=0\), the left side is
\[
1+(u\beta+\gamma)(x^2y+xy^2)
+\beta^2x^2y^2+\gamma^2x^3y^3.
\]
Coefficient comparison gives
\[
\gamma=u\beta,\qquad \beta^2=\lambda(1+a^4);
\]
the remaining cubic equation follows from \(u^2=0\). Conversely these equations make the displayed substitution a Hopf map. Its cotangent determinant is \(a\), so it is an automorphism exactly when \(a\) is a unit. This proves the functorial description, including nonreduced R-points.

## Theorem 2. Composition and inverse

Here (f,g) denote the corresponding algebra substitutions (pullbacks), and (f\circ g) means ordinary composition of these ring maps: apply (g) to an algebra element, then (f). For geometric group-scheme maps the order is reversed, as usual for pullbacks. For
\(f=(a,b,u,\beta)\) and \(g=(a',b',u',\beta')\),
\[
f\circ g=
\left(
aa',\
a'b+a^2b',\
u+au',\
\beta+u'b+a^2\beta'+auu'
\right).
\]
The defining equations are preserved:
\[
(u+au')^2=0,\qquad
(\beta+u'b+a^2\beta'+auu')^2
=\lambda(1+(aa')^4).
\]
The identity is \((1,0,0,0)\), and
\[
f^{-1}=
\left(
a^{-1},\
a^{-3}b,\
a^{-1}u,\
a^{-2}\beta+a^{-3}ub
\right).
\]

## 3. Geometry

The two defining equations have zero differential at the identity in characteristic two. Thus the tangent space has dimension four, whereas the reduced support has dimension two. The group scheme is non-smooth. For \(\lambda\notin k^2\), the reduced curve in the \((a,\beta)\)-plane is a purely inseparable double cover of \(\mathbb G_m\); it becomes split after adjoining \(\sqrt\lambda\).

This computes automorphisms of the fixed Hopf group \(G_\lambda\), not automorphisms of the underlying Fold algebra that fail to preserve its coproduct.
