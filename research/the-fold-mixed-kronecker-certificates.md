# G-EP34 — Mixed Kronecker decomposition certificates

G-EP34 adds a verifier for a *proposed* mixed decomposition. The declaration consists of right minimal indices, left minimal indices, an optional square regular pencil, and constant invertible witnesses \(S,T\).

For each right index \(\epsilon\), the target block is
\[
Q_\epsilon=[I_\epsilon\ 0],\qquad K_\epsilon=[0\ I_\epsilon].
\]
For each left index \(\eta\), the target block is its transpose. These are assembled with the supplied regular pair \((Q_r,K_r)\) by block diagonal sum. The verifier checks the regular pair is square and has full normal rank over \(\mathbb F_p(t)\), then verifies
\[
SQS=\text{(not used)},\qquad SQT=Q_{\rm target},\quad SKT=K_{\rm target}.
\]
(The first displayed expression is deliberately not part of the certificate; the two coefficient identities are the strict-equivalence conditions.)

The certificate therefore verifies the singular block sizes and their separation from a regular component, provided the supplied witnesses are correct. It does **not** discover \(S,T\), infer the block sizes, canonicalize the regular component, or prove uniqueness. Zero minimal-index blocks are currently excluded because the existing matrix-pair API requires positive row and column dimensions.

This is an independent verification layer for mixed candidates, not a general Kronecker decomposition algorithm.
