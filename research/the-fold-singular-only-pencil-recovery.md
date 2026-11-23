# G-EP33 — Structural recovery of pure singular-only pencils

G-EP32 handled one right or left singular block. G-EP33 extends the basis construction to a direct sum of several blocks on one side.

For a right minimal-basis generator
\[
x_i(t)=x_{i,0}+x_{i,1}t+\cdots+x_{i,\epsilon_i}t^{\epsilon_i},
\]
the coefficient equations are
\[
Qx_{i,0}=0,\quad Qx_{i,j}=-Kx_{i,j-1},\quad Kx_{i,\epsilon_i}=0.
\]
Reverse each chain and alternate signs, setting
\[
z_{i,j}=(-1)^{\epsilon_i-j}x_{i,\epsilon_i-j}.
\]
Then \(Qz_{i,j}=Kz_{i,j+1}\). Concatenate all chain vectors as columns of \(T\), and concatenate \(Kz_{i,1},\ldots,Kz_{i,\epsilon_i}\) as columns of \(B\). If these are bases of the full domain and codomain, respectively, \(S=B^{-1}\) yields the direct sum of canonical right singular blocks:
\[
SQT=\bigoplus_i[I_{\epsilon_i}\ 0],\qquad
SKT=\bigoplus_i[0\ I_{\epsilon_i}].
\]

The implementation uses G-EP27 to certify all polynomial nullspace generators and bounded-degree spans, verifies the two aggregate basis determinants, constructs \(S,T\), and independently checks the final identities with G-EP30. The left-only case is handled by transposition.

This is a genuine constructive extension beyond a single block, and does not enumerate general linear groups. It still refuses mixed left/right pencils and any pencil with a regular part. It is not a general Kronecker decomposition; it inherits the exact polynomial-minor budget and dense finite-field limitations of G-EP24/G-EP27.
