# UF-036 — The integral unipotent subgroup and flatness of the full automorphism scheme

## 1. The integral algebra

Let
\[
C_{\mathbb Z}=\mathbb Z[x,y]/(x^2+y^2,x^4)
\]
with basis \(1,x,x^2,x^3,y,xy,x^2y,x^3y\). The seven-parameter identity-linear substitutions from UF-026 make sense over an arbitrary commutative ring \(A\):
\[
\begin{aligned}
X={}&x+a x^2+bxy+c x^3+d x^2y+f x^3y,\\
Y={}&y-bx^2+a xy-dx^3+e x^2y+g x^3y.
\end{aligned}
\]
Here \((a,b,c,d,e,f,g)\in A^7\).

The defining identities hold integrally, not merely after inverting 2. Direct reduction using \(y^2=-x^2\) and \(x^4=0\) gives \(X^2+Y^2=0\) with no division by an integer; then
\[
X^2Y^2=-X^4=0.
\]
The induced map on the associated graded algebra is the identity. In the displayed basis its matrix is triangular with diagonal entries one, so its determinant is one over every ring. Thus every parameter tuple defines an automorphism of \(C_A\), functorially in \(A\).

## 2. Theorem UF-036.1 — Integral group scheme

The seven-parameter family is represented by an affine group scheme
\[
U_{\mathbb Z}\cong\mathbb A^7_{\mathbb Z}.
\]
For outer coordinates \(\theta=(a,b,c,d,e,f,g)\) and inner coordinates
\(\Theta=(A,B,C,D,E,F,G)\), the product corresponding to
\(\Phi_\theta\circ\Phi_\Theta\) is
\[
\begin{aligned}
a'&=a+A, & b'&=b+B,\\
c'&=c+C+2Aa-2Bb, & d'&=d+D+2Ab+2Ba,\\
e'&=e+E+2Aa-2Bb,\\
f'&=f+F+2Aab+2Ad+Ba^2-Bb^2+Bc+Be+3Cb+3Da,\\
g'&=g+G+Aa^2-Ab^2+Ac+Ae-2Bab-2Bd-3Db+3Ea.
\end{aligned}
\]
All structure polynomials have integer coefficients. The identity is the zero tuple, and the inverse of \((a,b,c,d,e,f,g)\) is
\[
\begin{aligned}
A={}&-a, & B={}&-b,\\
C={}&-c+2a^2-2b^2, & D={}&-d+4ab,\\
E={}&-e+2a^2-2b^2,\\
F={}&-f-15a^2b+5ad+5b^3+4bc+be,\\
G={}&-g-5a^3+15ab^2+ac+4ae-5bd.
\end{aligned}
\]
Consequently \(U_{\mathbb Z}\) is a smooth, flat affine group scheme over \(\mathbb Z\), with every geometric fiber an affine seven-dimensional group. It is unipotent: the substitutions act as the identity on the associated-graded pieces, hence by upper-unitriangular matrices in a degree-ordered basis.

**Proof.** The substitution calculation giving the product is UF-027; its formulas contain only integers and therefore define multiplication over \(\mathbb Z\). Solving the triangular equations \(\theta\star\Theta=0\) gives the displayed inverse, again with integer coefficients. These are polynomial maps, so the group axioms hold over \(\mathbb Z\) because they hold as identities of universal substitution polynomials (equivalently, by associativity of composition). The underlying scheme is affine seven-space, hence smooth and flat over \(\mathbb Z\). The coefficient map into the affine space of endomorphisms is a closed immersion: the seven parameters are seven distinct coefficients of \(X,Y\), and all other coefficients are fixed or prescribed by them. Its image lies in the automorphism locus by the determinant-one argument. \(\square\)

## 3. Theorem UF-036.2 — Schematic closure

Let \(U_{\mathbb Q}\) be the characteristic-zero identity-linear subgroup inside
\(\operatorname{Aut}(C_{\mathbb Q})\). Its schematic closure in
\(\operatorname{Aut}(C_{\mathbb Z})\) is exactly the embedded copy of
\(U_{\mathbb Z}\cong\mathbb A^7_{\mathbb Z}\).

**Proof.** The coefficient parameterization above is a closed immersion over \(\mathbb Z\), and its generic fiber is precisely \(U_{\mathbb Q}\) by UF-026. Since \(\mathbb Z[a,b,c,d,e,f,g]\) is torsion-free over \(\mathbb Z\), the embedded subgroup is flat and has no vertical component. Equivalently, its defining ideal is already saturated with respect to every nonzero integer. Therefore it is the scheme-theoretic closure of its generic fiber. \(\square\)

This settles the integral closure question for the seven-dimensional subgroup. In particular, the closure has no extra components and no nonreduced thickening in characteristic two.

## 4. The characteristic-two fiber is a proper subgroup of the identity-linear kernel

In characteristic two, put \(z=x+y\), so
\[
C_{\mathbb F_2}=\mathbb F_2[x,z]/(x^4,z^2).
\]
UF-033 describes the full automorphism scheme: it has 13-dimensional reduced fiber and 16-dimensional identity tangent space. Its reduced field-valued automorphisms have ten nonlinear coefficients and three free linear coefficients (with the cotangent determinant invertible). Fixing the identity linear part leaves a ten-dimensional reduced identity-linear kernel.

By contrast, the special fiber \(U_{\mathbb F_2}\) of the integral closure remains seven-dimensional. It is therefore a proper closed subgroup of that ten-dimensional identity-linear kernel. This is not a contradiction: the seven-dimensional group is the flat closure of the characteristic-zero subgroup, not the full identity-linear automorphism group in characteristic two.

The three additional reduced directions arise because the differentiated quadratic relation loses its factor 2 in characteristic two. They are genuine extra automorphisms of the special fiber, not points of the flat closure \(U_{\mathbb Z}\).

## 5. Theorem UF-036.3 — The full automorphism scheme is not flat over Z

The full automorphism scheme \(\operatorname{Aut}(C_{\mathbb Z})\) is not flat over \(\mathbb Z\).

**Reason.** Its geometric generic fiber has dimension eight by UF-026 and UF-035. Its characteristic-two fiber has scheme dimension 13 by UF-033 (the three nilpotent equations \(c^4=d^2=h^2=0\) do not change the underlying reduced dimension). For a group scheme locally of finite presentation, flatness forces the fiber dimension to be locally constant on the base. The dimensions eight and thirteen therefore rule out flatness at the prime 2.

This identifies the exceptional prime for the full automorphism scheme: the seven-dimensional unipotent closure itself is flat at 2, but the full automorphism scheme is not. The failure belongs to the extra characteristic-two automorphisms and their infinitesimal structure, not to the integral model \(U_{\mathbb Z}\).

## 6. What remains open

1. Give an explicit ideal-level description of the full automorphism scheme over \(\mathbb Z\), and exhibit a concrete 2-torsion element in its coordinate ring (or an equivalent local flatness obstruction).
2. Determine the scheme-theoretic intersection of the full characteristic-two identity-linear kernel with the closure \(U_{\mathbb F_2}\), including its quotient group scheme.
3. Determine whether the extra three reduced identity-linear directions admit a natural filtration or normal-subgroup interpretation.
4. Study the integral closure of the full graded quotient \(G_{\rm gr}\). The normalized D16 matrices involve denominators at 2 and square roots, so the odd-characteristic semidirect-product description does not by itself provide a global integral model.

## Reproducibility

Run:
```sh
python3 tools/fold_integral_unipotent.py
```
The verifier checks the integer product and inverse identities symbolically, verifies the seven-parameter substitutions preserve the integral relations, and checks the dimension comparison recorded above. The script is a symbolic identity check; the scheme-theoretic closure and flatness arguments are proved in this note.
