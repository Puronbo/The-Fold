# A sixth, non-product Hopf structure: nilpotent restricted Lie 2-map

Let k have characteristic two and
\[
A=k[x,z]/(x^4,z^2).
\]
Define
\[
\Delta(x)=x\otimes1+1\otimes x+z\otimes z,\qquad
\Delta(z)=z\otimes1+1\otimes z,
\]
with counit zero on x,z and antipode S(x)=x, S(z)=z.

## 1. Hopf structure

The relations are preserved:
\[
\Delta(x)^4=x^4\otimes1+1\otimes x^4+z^4\otimes z^4=0,
\qquad \Delta(z)^2=0.
\]
Coassociativity on x reduces to the 2-cocycle identity for C(z,z')=zz':
\[
C(z,z')+C(z+z',w)=C(z',w)+C(z,z'+w).
\]
Both sides equal \(zz'+zw+z'w\). Coassociativity on z is immediate. The antipode identities hold because
\[
m(S\otimes1)\Delta(x)=x+x+z^2=0,\qquad
m(S\otimes1)\Delta(z)=z+z=0.
\]
Thus this is a commutative Hopf algebra. Its group law is
\[
(x,z)+(x',z')=(x+x'+zz',\,z+z').
\]

It is a central extension
\[
0\longrightarrow\alpha_4\longrightarrow G_D
\longrightarrow\alpha_2\longrightarrow0.
\]
The cocycle zz' is not a coboundary of a polynomial in z, because z²=0 and every normalized polynomial f(z) is linear, so f(z+z')+f(z)+f(z')=0.

## 2. Invariants and non-isomorphism

The primitive subspace is
\[
P(A)=kz\oplus kx^2.
\]
Thus its dimension is two, unlike alpha_4 x alpha_2, whose primitive space has dimension three.

The relative Frobenius image is alpha_2: x maps to x², z maps to zero, and
\[
\Delta(x^2)=x^2\otimes1+1\otimes x^2
\]
because z²=0. This separates G_D from both product structures with Frobenius image mu_2.

The invariant derivations are
\[
D_x=\partial_x,\qquad D_z=\partial_z+z\partial_x.
\]
They satisfy
\[
D_x^{[2]}=0,\qquad D_z^{[2]}=D_x,\qquad D_x^{[2]}=0.
\]
Thus the restricted 2-power map is nonzero nilpotent of Jordan type two. This separates G_D from G_C, whose restricted 2-power map is zero, and from alpha_4 x mu_2, whose restricted 2-power map has a nonzero semisimple direction. Together these invariants show that G_D is pairwise non-isomorphic to the four product structures and to G_C.

## 3. Full automorphism group scheme

The primitive subspace forces the image of z to be
\[
Z=az+bx^2.
\]
Hopf compatibility for the image X of x requires
\[
\Delta(X)-X\otimes1-1\otimes X=Z\otimes Z.
\]
Comparing reduced coproducts of the eight basis monomials gives
\[
X=a^2x+abx^2z+cz+dx^2,\qquad b^2=0.
\]
The cotangent determinant is a³, so the substitution is an automorphism exactly when a is a unit. Therefore
\[
\operatorname{Aut}_{\mathrm{grp}}(G_D)
=\operatorname{Spec}k[a,a^{-1},b,c,d]/(b^2).
\]
It has reduced dimension three and tangent dimension four.

For composition f=(a,b,c,d) after g=(a',b',c',d'), the exact law is
\[
(aa',\ a'b+a^4b',\ (a')^2c+ac',\ (a')^2d+bc'+a^4d').
\]
The inverse is
\[
(a,b,c,d)^{-1}
=(a^{-1},\,ba^{-5},\,ca^{-3},\,da^{-6}+bc\,a^{-7}).
\]

## 4. Translation normalizer

The general affine-normalizer theorem gives
\[
C_{\operatorname{Aut}(\operatorname{Spec}A)}(G_D)=G_D,\qquad
N_{\operatorname{Aut}(\operatorname{Spec}A)}(G_D)
=G_D\rtimes\operatorname{Aut}_{\mathrm{grp}}(G_D).
\]
The centralizer is the rank-eight translation group. The normalizer has reduced dimension three and tangent dimension six.

The exact standard-library verifier is tools/fold_char2_nilpotent_pmap_hopf.py. It checks the Hopf identities and primitive-space dimension over F₂.

## 5. Classification consequence

There are now at least six pairwise non-isomorphic commutative Hopf structures on the same Fold algebra: four product laws and two non-product central extensions. The Frobenius-kernel reduction note explains how to organize the remaining classification. The fppf torsors of G_D and the search for further Hopf structures remain open.


## 6. Fixed central-extension cocycle calculation

For the extension alpha_4 -> G_D -> alpha_2 with a chosen global product-coordinate section, a normalized symmetric polynomial cocycle C(z,z') has only one possible term:
```
C(z,z') = lambda z z'
```
because z²=z'²=0. It satisfies the cocycle identity. A section change f(z) is linear, f(z)=a z, and its additive coboundary is zero. Thus the split class lambda=0 and the non-split class lambda≠0 are the only classes in this fixed polynomial-cocycle model; any nonzero lambda is normalized to 1 by scaling the alpha_4 coordinate x. This does not classify extensions without a chosen global section.
