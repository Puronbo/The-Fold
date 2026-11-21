# Translation normalizer of the imperfect mixed Hopf group

Let \(G_\lambda\) be the rank-eight commutative group scheme on
\[
A=k[x,t]/(x^4,t^2-1),\qquad
\Delta(t)=(t\otimes t)(1+\lambda x^2\otimes x^2).
\]

## Theorem 1. Centralizer and normalizer

Inside the full automorphism group scheme of the underlying finite affine scheme \(\operatorname{Spec}A\),
\[
C_{\operatorname{Aut}(\operatorname{Spec}A)}(G_\lambda)=G_\lambda,
\]
and
\[
N_{\operatorname{Aut}(\operatorname{Spec}A)}(G_\lambda)
\cong G_\lambda\rtimes\operatorname{Aut}_{\mathrm{grp}}(G_\lambda).
\]

### Proof

The general argument is functorial over every k-algebra R. If an R-automorphism \(f\) commutes with every left translation \(L_g\), then
\[
f\circ L_g=L_g\circ f.
\]
Evaluating at the identity gives \(f(g)=g+f(e)\). Since \(G_\lambda\) is commutative, this is translation by \(f(e)\), proving the centralizer statement.

If \(f\) normalizes translations, conjugation induces an automorphism \(\phi\) of the group functor:
\[
f\circ L_g=L_{\phi(g)}\circ f.
\]
Evaluating at the identity gives \(f(g)=\phi(g)+f(e)\). Thus \(f\) is a translation followed by a group-scheme automorphism. Conversely, every such affine group-scheme automorphism normalizes translations. This identifies the normalizer as the indicated semidirect product.

## 2. Explicit automorphism factor

The mixed-family calculation gives
\[
\operatorname{Aut}_{\mathrm{grp}}(G_\lambda)
=\operatorname{Spec}
k[a,a^{-1},b,u,\beta]/
(u^2,\ \beta^2+\lambda(1+a^4)).
\]
Its reduced dimension is two and its tangent dimension at the identity is four.

The translation group scheme \(G_\lambda\) is finite of rank eight, so its reduced dimension is zero. Its tangent dimension is two, since the cotangent space of \(A\) at the identity has basis \(x,z\). Therefore the normalizer has
\[
\dim_{\mathrm{red}}N=2,\qquad
\dim T_eN=2+4=6.
\]
The centralizer has reduced dimension zero and tangent dimension two.

The semidirect-product description is scheme-theoretic. In particular, the nilpotent automorphism coordinate \(u\) and the nonreduced equation for \(\beta\) are retained; replacing the automorphism group by its field-valued points would give the wrong normalizer tangent dimension.
