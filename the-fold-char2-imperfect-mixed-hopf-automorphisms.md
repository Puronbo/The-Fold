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
t\longmapsto t(1+\beta x^2),
\]
where \(a\in R^\times\), \(b,\beta\in R\), and
\[
\boxed{\ \beta^2=\lambda(1+a^4)\ }.
\]
Consequently
\[
\operatorname{Aut}_{\rm grp}(G_\lambda)
=\operatorname{Spec}
k[a,a^{-1},b,\beta]/(\beta^2+\lambda(1+a^4)).
\]
It has dimension two and tangent dimension three at the identity. Its reduced support has dimension two. The parameter \(\beta\) records infinitesimal homomorphisms \(\alpha_4\to\mu_2\); it must not be discarded by checking only field-valued points.

### Proof

The subgroup \(\mu_2=\ker(G_\lambda\to\alpha_4)\) is the unique subgroup of multiplicative type of rank two: every map \(\mu_2\to\alpha_4\) is trivial. It is therefore characteristic. The quotient is \(\alpha_4\), whose automorphisms over R have
\[
X=ax+bx^2,\qquad a\in R^\times.
\]
The restriction to the kernel is the identity because \(\operatorname{Aut}(\mu_2)\) is trivial.

A lift of this quotient map must send \(t\) to \(t h(x)\), where \(h\) is a normalized \(\mu_2\)-valued function on \(\alpha_4\). Write
\[
h(x)=1+\beta x^2+\gamma x^3;
\]
the \(x\)-term is excluded by \(h^2=1\). The Hopf condition is
\[
h(x)h(y)h(x+y)
=(1+\lambda x^2y^2)(1+\lambda a^4x^2y^2).
\]
The left side is
\[
1+\beta^2x^2y^2+\gamma(x^2y+xy^2)+\gamma^2x^3y^3.
\]
Coefficient comparison gives \(\gamma=0\) and
\(\beta^2=\lambda(1+a^4)\). Conversely this equation makes the displayed substitution a Hopf map. Its cotangent determinant is \(a\), so it is an automorphism exactly when \(a\) is a unit. This proves the functorial description, including nonreduced R-points.

## Theorem 2. Composition and inverse

Use composition \(f\circ g\), meaning apply g first and then f. For
\(f=(a,b,\beta)\) and \(g=(a',b',\beta')\),
\[
f\circ g=
\left(aa',\ a'b+a^2b',\ \beta+a^2\beta'\right).
\]
The defining equation is preserved:
\[
(\beta+a^2\beta')^2
=\lambda(1+(aa')^4).
\]
The identity is \((1,0,0)\), and
\[
(a,b,\beta)^{-1}
=(a^{-1},a^{-3}b,a^{-2}\beta).
\]

## 3. Geometric meaning

The automorphism group is generally non-smooth: at the identity the equation for \(\beta\) has zero differential in characteristic two, so the tangent dimension is three while the reduced dimension is two. For \(\lambda\notin k^2\), the reduced curve in the \((a,\beta)\)-plane is geometrically a purely inseparable double cover of \(\mathbb G_m\); it becomes split after adjoining \(\sqrt\lambda\).

This computes automorphisms of the fixed Hopf group \(G_\lambda\), not automorphisms of the underlying Fold algebra that fail to preserve its coproduct.
