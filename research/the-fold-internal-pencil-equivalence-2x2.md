# G-EP148: 2×2 internal pencil equivalence and joint-rank obstructions

This milestone extends the distinction between equal block dimensions and internal pencil equivalence from 1×1 to 2×2 blocks, while keeping the positive and negative claims separate.

For each field F₂, F₃, and F₅, a positive control starts from
\[
Q=I_2,\qquad K=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
It applies explicit nonidentity invertible matrices
\[
S=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
T=\begin{pmatrix}1&0\\1&1\end{pmatrix}
\]
and forms the target pair by exact multiplication. The production strict-pencil-equivalence auditor verifies both identities \(SQT=Q'\) and \(SKT=K'\), as well as invertibility of both transformations.

A negative control compares
\[
(Q,K_1)=(I_2,\operatorname{diag}(1,0)),\qquad
(Q,K_2)=\left(I_2,\begin{pmatrix}0&1\\0&0\end{pmatrix}\right).
\]
Both pairs have the same individual coefficient ranks: rank(Q)=2 and rank(Kᵢ)=1. Nevertheless, their joint pencil rank profiles differ. At \(\lambda=-1\), rank(Q+\lambda K_1)=1, while rank(Q+\lambda K_2)=2, over each tested field including characteristic two. For any common invertible S,T, the rank of every member is preserved because
\[
S(Q+\lambda K)T=SQ T+\lambda SKT.
\]
Thus the rank-profile mismatch is an exact obstruction to any simultaneous constant strict equivalence between these two pairs, rather than the failure of one proposed witness.

All arithmetic and rank calculations in the obstruction are test-local; the positive witness is checked by the existing production verifier. This is finite-field regression evidence for the stated 2×2 fixtures, not a complete classification of 2×2 pencils, a general equivalence-discovery routine, or a universal Kronecker-form algorithm.
