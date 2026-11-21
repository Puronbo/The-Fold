# A fifth, non-product Hopf structure on the characteristic-two Fold algebra

Let k have characteristic two and
\[
A=k[x,z]/(x^4,z^2).
\]
The four product Hopf structures are not exhaustive. The same algebra supports the following non-product commutative Hopf structure:
\[
\boxed{
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(z)=z\otimes1+1\otimes z+x^2\otimes x^2.
}
\]
The counit is epsilon(x)=epsilon(z)=0 and the antipode is S(x)=x, S(z)=z.

## 1. Hopf-algebra verification

The defining relations are preserved:
\[
\Delta(x)^4=x^4\otimes1+1\otimes x^4=0,
\]
\[
\Delta(z)^2=z^2\otimes1+1\otimes z^2+x^4\otimes x^4=0.
\]
Coassociativity on x is immediate. For z, both iterated coproducts equal
\[
z\otimes1\otimes1+1\otimes z\otimes1+1\otimes1\otimes z
+x^2\otimes x^2\otimes1
+x^2\otimes1\otimes x^2
+1\otimes x^2\otimes x^2,
\]
because \(\Delta(x^2)=x^2\otimes1+1\otimes x^2\). The counit identities hold on generators. The antipode identities are
\[
m(S\otimes1)\Delta(x)=x+x=0,\quad
m(S\otimes1)\Delta(z)=z+z+x^4=0,
\]
and similarly on the other side. Thus these formulas define a commutative Hopf algebra.

Equivalently, the group law on points is
\[
(x,z)+(x',z')=(x+x',\,z+z'+x^2x'^2).
\]
The extra term is a symmetric normalized 2-cocycle. It satisfies
\[
C(x,y)+C(x+y,w)=C(y,w)+C(x,y+w),
\qquad C(x,y)=x^2y^2.
\]
To classify normalized symmetric polynomial 2-cocycles for this fixed extension, write
\[
C(x,y)=\lambda_{12}(x^2y+xy^2)+\lambda_{13}(x^3y+xy^3)
+\lambda_{22}x^2y^2+\lambda_{23}(x^3y^2+x^2y^3)
+\lambda_{33}x^3y^3.
\]
The relation z²=0 forces the coefficient of xy to vanish, since its square would contribute a nonzero x² tensor y² term. Substitution in the cocycle equation
\[
C(x,y)+C(x+y,w)=C(y,w)+C(x,y+w)
\]
forces \(\lambda_{13}=\lambda_{23}=\lambda_{33}=0\), leaving \(\lambda_{12},\lambda_{22}\) free. The term \(\lambda_{12}(x^2y+xy^2)\) is the coboundary of \(\lambda_{12}x^3\), so the extension-class space for this fixed problem is one-dimensional, represented by \(\lambda_{22}x^2y^2\). A nonzero value is normalized to 1 by rescaling z. Thus, among central extensions admitting this global product-coordinate section and represented by these normalized polynomial cocycles, there are exactly the split and non-split classes. This is not a classification of central extensions without such a section.

## 2. It is not one of the four product structures

Three intrinsic invariants distinguish this group scheme from the four products.

### Primitive elements

A direct coefficient comparison in
\[
\Delta(f)=f\otimes1+1\otimes f
\]
shows
\[
P(A)=kx\oplus kx^2.
\]
In particular, z is no longer primitive. For the product \(\alpha_4\times\alpha_2\), the primitive space is \(kx\oplus kx^2\oplus kz\), of dimension three. The primitive-space dimension therefore separates the cocycle group from the additive-additive product.

### Relative Frobenius image

The relative Frobenius pullback sends x to x² and z to z²=0. Its scheme-theoretic image has coordinate algebra k[x²]/(x⁴), and
\[
\Delta(x^2)=x^2\otimes1+1\otimes x^2.
\]
Thus the Frobenius image is \(\alpha_2\). This separates the cocycle group from both products whose Frobenius image is \(\mu_2\), namely \(\mu_4\times\alpha_2\) and \(\mu_4\times\mu_2\).

### Restricted Lie algebra

The invariant derivations dual to x,z in the cotangent space are
\[
D_x=\partial_x,\qquad D_z=\partial_z.
\]
The extra term \(x^2\otimes x^2\) contributes nothing to these invariant derivations because x² lies in the square of the augmentation ideal. Both derivations square to zero, so the restricted 2-power map on the Lie algebra is zero. This separates the cocycle group from \(\alpha_4\times\mu_2\), whose \(\mu_2\)-direction has nonzero restricted 2-power map.

Therefore the cocycle group scheme is pairwise non-isomorphic to all four product structures.

## 3. Extension interpretation

Projection to the x-coordinate gives an exact sequence
\[
0\longrightarrow\alpha_2\longrightarrow G_C
\longrightarrow\alpha_4\longrightarrow0.
\]
The kernel is the z-coordinate subgroup, and the extension is central. Its cocycle is C(x,y)=x²y². Within normalized symmetric polynomial 2-cocycles for this fixed extension problem, the cocycle equations leave the coboundary class represented by x²y²; a nonzero scalar multiple is normalized by rescaling z. This establishes a nontrivial extension class in this fixed presentation, not a classification of every Hopf structure on A.

## 4. Verification and open questions

The standard-library verifier tools/fold_char2_cocycle_hopf.py checks the defining relations, coassociativity on generators, counit and antipode identities, and computes the primitive subspace by exact linear algebra over F₂.

New open directions:
1. Compute the full group-scheme automorphism functor of this cocycle group and its translation normalizer.
2. Classify central extensions of alpha_4 by alpha_2 compatible with the fixed underlying algebra.
3. Compute fppf torsors for this non-product group scheme.
4. Search for further non-product Hopf structures and determine whether the total classification is finite or has moduli.
