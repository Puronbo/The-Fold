# UF-034 — Full derivations of the integral vertex algebra

## 1. Algebra and basis

Let
\[
C_{\mathbb Z}=\mathbb Z[x,y]/(x^2+y^2,x^2y^2)
\cong \mathbb Z[x,y]/(y^2+x^2,x^4).
\]
It is free of rank eight with ordered basis
\[
1,x,x^2,x^3,y,xy,x^2y,x^3y.
\]
The second presentation follows by substituting \(y^2=-x^2\), which gives \(x^4=0\).

For any commutative ring A, an A-algebra endomorphism is specified by X,Y in C_A satisfying
\[
X^2+Y^2=0,\qquad X^2Y^2=0.
\]
The automorphism functor is the open subscheme on which the induced A-linear map C_A to C_A has invertible determinant. This full-module criterion is valid over arbitrary base rings, including nonreduced rings.

## 2. Derivation equations

A derivation is specified by P=D(x) and Q=D(y). Differentiating the two defining relations gives
\[
2(xP+yQ)=0,\qquad 2(xy^2P+x^2yQ)=0.
\]
Using \(y^2=-x^2\), the map after removing the common factor 2 is
\[
\Phi:C_{\mathbb Z}^2\longrightarrow C_{\mathbb Z}^2,
\qquad (P,Q)\longmapsto(xP+yQ,\;-x^3P+x^2yQ).
\]
In the displayed basis, its 16-by-16 integer matrix has rank seven. Its Smith normal form has seven nonzero invariants, all equal to one:
\[
\boxed{\operatorname{SNF}(\Phi)=\operatorname{diag}(1,1,1,1,1,1,1,0,\ldots,0).}
\]
Thus the actual differentiated-relation matrix is 2Phi. Its Smith form has seven nonzero invariants equal to 2, not eight invariants with a final 2. This distinction matters: the kernel dimension is nine in odd characteristic.

**Theorem UF-034.1.**
\[
\boxed{
\dim_k\operatorname{Der}_k(C_k)=
\begin{cases}
16,&\operatorname{char}k=2,\\
9,&\operatorname{char}k\ne2.
\end{cases}}
\]
Indeed, in characteristic two the differentiated relations vanish identically, so P,Q are arbitrary. In odd characteristic, 2 is invertible and Phi has rank seven over every such field: its Smith form has only unit nonzero invariants. The kernel therefore has dimension 16-7=9.

There is no characteristic-three jump in the dimension of the full derivation algebra. The characteristic-three center enlargement in UF-030/031 concerns the bracket radical of a particular seven-dimensional integral Lie algebra, not this full derivation kernel.

## 3. Tangent dimensions versus group dimensions

The derivation calculation determines the identity tangent dimension of the full automorphism group scheme: nine in odd characteristic and sixteen in characteristic two. It does not, by itself, determine the dimension or smoothness of the reduced automorphism group in odd characteristic.

In characteristic two, UF-033 gives the stronger scheme-level result: reduced dimension 13 and tangent dimension 16, hence non-smoothness. The odd-characteristic reduced group and the schematic closure of the characteristic-zero seven-dimensional unipotent subgroup remain open.

## 4. Exact verifier and scope

Run `python3 tools/fold_full_automorphism_characteristics.py`. The standard-library verifier constructs Phi from the multiplication table, computes exact rational rank and modular ranks, and checks the rank-seven/unit-minor certificate. It verifies the derivation dimensions in characteristics 2, 3, and 5. It is an exact linear-algebra check, not a classification of the full group scheme.

## Open problem UF-035

Classify the reduced automorphism group in odd characteristic, determine smoothness, and identify the schematic closure over Z of the characteristic-zero seven-dimensional unipotent subgroup.
