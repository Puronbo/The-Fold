# Automorphism group and translation normalizer of the cocycle Hopf structure (G-3d)

Let G_C be the non-product group scheme on
\[
A=k[x,z]/(x^4,z^2)
\]
with
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(z)=z\otimes1+1\otimes z+x^2\otimes x^2.
\]
The primitive subspace is \(P(A)=kx\oplus kx^2\).

## 1. Theorem G-3d.1 — full group-scheme automorphism functor

For every characteristic-two k-algebra R, a group-scheme endomorphism has
\[
X=ax+bx^2,\qquad Z=a^4z+cx+dx^2.
\]
It is an automorphism exactly when a is a unit and c²=0. Hence
\[
\operatorname{Aut}_{\mathrm{grp}}(G_C)
=\operatorname{Spec}k[a,a^{-1},b,c,d]/(c^2).
\]
Its reduced dimension is three and its tangent dimension is four; it is non-smooth.

**Proof.** Hopf compatibility forces X to be primitive. Since \(P(A_R)=Rx\oplus Rx^2\), write \(X=ax+bx^2\). Then
\[
X^2=a^2x^2,\qquad X^2\otimes X^2=a^4x^2\otimes x^2.
\]
The required equation
\[
\Delta(Z)=Z\otimes1+1\otimes Z+X^2\otimes X^2
\]
therefore forces \(Z-a^4z\) to be primitive. Thus \(Z=a^4z+cx+dx^2\). The relation \(Z^2=0\) is equivalent to \(c^2=0\); \(X^4=0\) holds automatically. On the cotangent space \(m/m^2\), the linear matrix is triangular with diagonal entries a and a⁴, so it is invertible exactly when a is a unit. Conversely these conditions make the substitution a Hopf automorphism. \(\square\)

## 2. Composition law

Use composition \(f\circ g\), with f=(a,b,c,d) applied after g=(a',b',c',d'). Substitution gives
\[
(a,b,c,d)(a',b',c',d')
=\left(
aa',\ a'b+a^2b',\
(a')^4c+ac',\
(a')^4d+bc'+a^2d'
\right).
\]
The identity is (1,0,0,0). The inverse is
\[
(a,b,c,d)^{-1}
=\left(a^{-1},\,b a^{-3},\,c a^{-5},\,
d a^{-6}+bc a^{-7}\right).
\]
All formulas are regular on the open set a invertible and respect c²=0.

## 3. Theorem G-3d.2 — translation centralizer and normalizer

Let G_C act on itself by left translations. Then inside the automorphism group scheme of its underlying finite affine scheme,
\[
C(G_C)=G_C,\qquad
N(G_C)=G_C\rtimes\operatorname{Aut}_{\mathrm{grp}}(G_C).
\]
The proof is the functorial affine-normalizer argument: commuting with all translations forces an automorphism to be a translation; normalizing translations forces it to be a translation followed by a group-scheme automorphism.

Thus the fifth Hopf structure now has an explicit translation normalizer, including its infinitesimal automorphism direction c with c²=0.

## 4. Consequences and open directions

- The full automorphism functor of this non-product group law is non-smooth despite having reduced dimension three.
- Its translation centralizer is exactly the rank-eight group scheme G_C.
- Its translation normalizer has reduced dimension three and tangent dimension six (two tangent directions from G_C and four from Aut_grp(G_C)).
- The fppf torsor classes of G_C and the classification of further non-product Hopf structures remain open.
