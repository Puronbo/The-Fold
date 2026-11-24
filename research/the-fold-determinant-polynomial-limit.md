# G-EP150: Equal determinant polynomials do not imply strict equivalence

This milestone establishes a limitation of the 2×2 homogeneous determinant polynomial from G-EP149.

Over F₂, F₃, and F₅, compare
\[
(Q,K_1)=(I_2,I_2),\qquad
(Q,K_2)=\left(I_2,\begin{pmatrix}1&1\\0&1\end{pmatrix}\right).
\]
Both pencils have the same homogeneous determinant polynomial:
\[
\det(xQ+yK_1)=\det(xQ+yK_2)=(x+y)^2.
\]
Both coefficient matrices are invertible, and the polynomial coefficient triples agree exactly, not merely up to scale.

However, constant strict equivalence would require invertible S,T satisfying both coefficient identities. Since both Q coefficients are I₂, the identity \(S I_2 T=I_2\) forces \(T=S^{-1}\). The K identity would therefore make K₁ and K₂ similar. Similarity preserves the rank of K−I₂, but this rank is zero for K₁ and one for K₂. Hence no constant strict-equivalence witness exists.

This exact counterexample shows that the homogeneous determinant polynomial is a necessary projective invariant, not a complete invariant, even for these 2×2 pencils. The argument and tests are finite-field regression evidence for the stated family; they do not provide a complete classification.
