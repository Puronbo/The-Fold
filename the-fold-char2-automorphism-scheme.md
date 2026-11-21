# UF-033 — The full automorphism group scheme in characteristic two

## The algebra

Over a field k of characteristic two, put z=x+y. The vertex algebra is
\[
C=k[x,y]/(x^2+y^2,x^4)\cong k[x,z]/(x^4,z^2).
\]
Use the basis \(1,x,x^2,x^3,z,xz,x^2z,x^3z\).

## Theorem 1 — The full derivation algebra has dimension 16

A k-derivation is determined by the two arbitrary values D(x),D(z) in C. Indeed,
\[
D(x^4)=4x^3D(x)=0,\qquad D(z^2)=2zD(z)=0
\]
in characteristic two. There are no further defining relations. Hence
\[
\boxed{\operatorname{Der}_k(C)\cong C\oplus C,\quad
\dim_k\operatorname{Der}_k(C)=16.}
\]
This is the tangent space at the identity of the full automorphism group scheme, not merely the tangent space of the seven-dimensional characteristic-zero unipotent subgroup considered in UF-026–UF-029.

## Theorem 2 — Explicit automorphism group scheme

Write general images as
\[
X=c+a x+bz+c_2x^2+c_3x^3+c_{11}xz+c_{21}x^2z+c_{31}x^3z,
\]
\[
Z=d+h x+i z+d_2x^2+d_3x^3+d_{11}xz+d_{21}x^2z+d_{31}x^3z.
\]
Over a k-algebra, the assignments x↦X, z↦Z define an algebra endomorphism precisely when
\[
c^4=0,\qquad d^2=0,\qquad h^2=0.
\]
The endomorphism is an automorphism on the open locus where the induced linear map on the cotangent space is invertible:
\[
ai-bh\in A^\times.
\]

**Proof.** In characteristic two, fourth powers and squares are additive. Every nonconstant basis monomial has fourth power zero, so \(X^4=c^4\). Every nonconstant basis monomial except x has square zero, while x squares to x², so \(Z^2=d^2+h^2x^2\). The basis elements 1 and x² are independent, giving exactly the three equations. Invertibility of the induced map on the cotangent space is the usual local-algebra criterion for an automorphism; its linear coefficient matrix is \(\begin{psmallmatrix}a&b\\h&i\end{psmallmatrix}\). \(\square\)

## Theorem 3 — Dimension 13, tangent dimension 16: non-smoothness

The three equations \(c^4=d^2=h^2=0\) are nilpotent thickening equations. The underlying reduced scheme has
\[
c=d=h=0,\qquad ai\ne0,
\]
and is an open subset of affine 13-space. Therefore
\[
\boxed{\dim \operatorname{Aut}(C)_{\rm red}=13,\qquad
\dim T_1\operatorname{Aut}(C)=16.}
\]
The automorphism group scheme is not smooth.

At the identity, the differentials of all three equations vanish. The three extra tangent directions correspond to infinitesimal constant terms in X and Z and the infinitesimal x-component of Z. They exist over dual-number bases but not as ordinary automorphisms over a field.

For an ordinary field-valued automorphism, c=d=h=0 and a,i are nonzero. In particular, the image of z has no x-linear term. The group of field-valued automorphisms is thus the 13-dimensional reduced locus described above.

## Consequences for the earlier seven-dimensional kernel

The seven-dimensional Lie algebra in UF-028 is the characteristic-zero Lie algebra of a particular unipotent subgroup. Its integral bracket reduction in UF-030–UF-032 remains a well-defined seven-dimensional alternating Lie algebra in characteristic two. It is **not** the full derivation algebra of the characteristic-two vertex algebra: the latter has dimension 16.

This distinction prevents an invalid inference from reduction of the characteristic-zero subgroup to the full automorphism group scheme. Characteristic two introduces both additional ordinary automorphisms (the reduced group has dimension 13) and infinitesimal directions (tangent dimension 16).

## Exact verification

Run python3 tools/fold_char2_automorphism_scheme.py.

The standard-library verifier checks the basis-square and basis-fourth-power rules, the three scheme equations, the 13-dimensional reduced parameter count, the 16-dimensional tangent count, and the cotangent determinant condition. It is a finite structural verifier; the proofs above are algebraic and do not depend on sampling.

## Next question

**UF-034.** Determine the full automorphism group scheme in arbitrary characteristic and compare its fibers at 2, 3, and primes greater than 3. In particular, identify the integral group scheme whose characteristic-zero fiber gives the seven-dimensional unipotent kernel and explain how its closure sits inside the full automorphism scheme.
