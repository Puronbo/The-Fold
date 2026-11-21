# UF-034 — The full automorphism functor across characteristics

## 1. Integral algebra and its functor of points

Let
\[
C_{\mathbb Z}=\mathbb Z[x,y]/(x^2+y^2,x^2y^2)
\cong \mathbb Z[x,y]/(y^2+x^2,x^4).
\]
It is free of rank eight with basis
\[
1,x,x^2,x^3,y,xy,x^2y,x^3y.
\]
For any commutative ring A, an A-algebra endomorphism is specified by X,Y in C_A satisfying
\[
X^2+Y^2=0,\qquad X^2Y^2=0.
\]
The automorphism functor is the open subscheme where the induced A-linear map C_A to C_A has invertible determinant. This full-module criterion is valid over arbitrary base rings, including nonreduced rings.

## 2. Derivation equations

A derivation is specified by P=D(x) and Q=D(y). Differentiating the defining relations gives
\[
2(xP+yQ)=0,\qquad 2(xy^2P+x^2yQ)=0.
\]
Using y^2=-x^2, the second expression becomes
\[
2(-x^3P+x^2yQ)=0.
\]
Let Phi:C_Z^2 to C_Z^2 be the integral linear map
\[
\Phi(P,Q)=(xP+yQ,\;-x^3P+x^2yQ).
\]
In the rank-eight basis, its 16-by-16 matrix has rank eight over Q and Smith invariants
\[
\boxed{1,1,1,1,1,1,1,2.}
\]
Thus the actual differentiated-relation matrix 2Phi has eight nonzero Smith invariants 2,2,2,2,2,2,2,4. In particular, Phi has rank seven modulo two and rank eight modulo every odd prime. The actual map 2Phi is zero modulo two.

**Theorem UF-034.1.**
\[
\boxed{
\dim_k\operatorname{Der}_k(C_k)=
\begin{cases}
16,&\operatorname{char}k=2,\\
8,&\operatorname{char}k\ne2.
\end{cases}}
\]
In odd characteristic, 2 is invertible and Phi has rank eight, so its kernel has dimension 16-8=8. In characteristic two, both differentiated relations vanish, so P,Q are arbitrary and the dimension is 16.

There is no characteristic-three jump in the dimension of the full derivation algebra. The characteristic-three center enlargement in UF-030/031 concerns the bracket radical of a particular seven-dimensional integral Lie algebra, not this full derivation kernel.

## 3. Tangent dimensions versus group dimensions

The derivation calculation determines the identity tangent dimension of the full automorphism group scheme: eight in odd characteristic and sixteen in characteristic two. In characteristic zero this agrees with the established structure Aut(C)=U semidirect G_gr, where U is seven-dimensional and G_gr has a one-dimensional scalar factor with finite orthogonal subgroup D16.

In characteristic two, UF-033 gives the stronger scheme-level result: reduced dimension 13 and tangent dimension 16, hence non-smoothness. The odd-characteristic reduced group and the schematic closure of the characteristic-zero seven-dimensional unipotent subgroup remain open.

## 4. Verifier and scope

Run `python3 tools/fold_full_automorphism_characteristics.py`. The standard-library verifier constructs Phi from the multiplication table, checks its exact rational rank and modular ranks at 2, 3, and 5, and verifies the derivation dimensions. The Smith invariants above are an exact integer-matrix calculation; the script is not presented as a general Smith-normal-form implementation.

## Open problem UF-035

Classify the reduced automorphism group in odd characteristic, determine smoothness, and identify the schematic closure over Z of the characteristic-zero seven-dimensional unipotent subgroup.
