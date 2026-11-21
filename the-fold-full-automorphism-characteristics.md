# UF-034 — The full automorphism functor across characteristics

## 1. Integral algebra and its functor of points

Let
\[
C_{\mathbb Z}=\mathbb Z[x,y]/(x^2+y^2,x^2y^2).
\]
It is free of rank eight with basis
\[
1,x,y,xy,x^2,x^2y,x^3,x^3y.
\]
For any commutative ring A, an A-algebra endomorphism is specified by two elements
\(X,Y\in C_A=C_{\mathbb Z}\otimes A\), each with eight coefficients, subject exactly to
\[
X^2+Y^2=0,\qquad X^2Y^2=0.
\]
This gives a finite-type affine endomorphism scheme in 16 coefficient variables, with equations obtained by expanding these two elements in the displayed basis. The automorphism group scheme is the open subscheme where the induced 8-by-8 matrix of the A-linear map \(C_A\to C_A\) has unit determinant. This determinant criterion is valid over arbitrary base rings and avoids an unjustified cotangent-space criterion on nonreduced bases.

Composition of substitutions gives the group law. This is an exact functorial presentation over \(\mathbb Z\), even when a compact list of expanded coefficient equations would obscure characteristic-dependent cancellations.

## 2. Tangent algebra at the identity

A derivation is determined by \(P=D(x)\) and \(Q=D(y)\), each in C. Differentiating the defining relations gives
\[
2(xP+yQ)=0,\qquad 2(xy^2P+x^2yQ)=0.
\]
In the rank-eight basis, this is a 16-by-16 integer coefficient matrix. After removing its common factor 2, its nonzero Smith invariants are
\[
\boxed{1,1,1,1,1,1,1,2.}
\]
Thus the rank of the relation matrix is eight in every odd characteristic, while it is zero in characteristic two. Consequently
\[
\boxed{\dim_k\operatorname{Der}_k(C_k)=
\begin{cases}
8,&\operatorname{char}k\ne2,\\
16,&\operatorname{char}k=2.
\end{cases}}
\]
This independently recovers the 16-dimensional characteristic-two tangent space from UF-033. The exceptional prime in this tangent calculation is exactly 2; prime 3 does not appear in the Smith invariants.

## 3. Distinguish the characteristic-three bracket phenomenon

UF-030 and UF-031 found a characteristic-three enlargement of the center of a particular seven-dimensional, integral class-two Lie algebra associated with the characteristic-zero unipotent subgroup. That is a statement about the radical of that bracket lattice.

It is not a jump in the full derivation dimension: the full tangent dimensions are 8 in characteristic three and in every other odd characteristic, and 16 in characteristic two. Thus the prime 3 is detected by the restricted bracket lattice, while the prime 2 is detected by the full automorphism tangent functor.

## 4. What this establishes — and what it does not

The universal substitution presentation and the tangent calculation are proved directly from the defining relations. They do not yet classify the geometric connected components, the reduced group structure, or the integral closure of the characteristic-zero seven-dimensional unipotent subgroup. In particular, the dimension of the full reduced automorphism group in every odd characteristic still requires a separate proof; it should not be inferred solely from the tangent dimension.

The characteristic-two reduced dimension 13 and tangent dimension 16 are computed in UF-033 using the coordinates \(z=x+y\). The present note places that result in the integral family and confirms that characteristic three does not create a corresponding tangent jump.

## 5. Verifier

Run \`python3 tools/fold_full_automorphism_characteristics.py\`. It checks the integer relation matrix, its Smith invariants, and its ranks modulo 2, 3, and 5. The matrix calculation is exact; the geometric group classification remains an explicitly open task.

## Open problem UF-035

Determine the reduced automorphism group over every algebraically closed field of odd characteristic, prove or disprove smoothness there, and identify the schematic closure over \(\mathbb Z\) of the characteristic-zero seven-dimensional unipotent subgroup.
