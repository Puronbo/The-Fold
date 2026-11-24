# G-EP29 — Independent unimodularity audit for pencil transformations

G-EP28 constructs (U(t),V(t),D(t)) with (U(Q+tK)V=D) using elementary polynomial row and column operations. G-EP29 adds an independent verifier that does not rely on the operation log's assertion that the transformations are unimodular.

For square polynomial matrices (U,V) over (mathbb F_p[t]), unimodularity is equivalent to their determinants being nonzero constants (units) in (mathbb F_p[t]). The audit computes both determinants by exact Leibniz expansion, checks they are units, and independently recomputes (UPV) to compare it with the supplied reduced matrix.

API:
`audit_polynomial_smith_transform(q,k,p,transform,max_determinant_terms=100000)`

The determinant calculation has an explicit permutation budget because its cost grows factorially with transform dimension. If the budget is exceeded, the audit raises a clear error rather than returning an unverified result.

This is an independent certificate for the polynomial Smith transforms. It does not transform singular blocks into Kronecker canonical form, and it does not upgrade Smith equivalence into strict equivalence of pencils. The distinction remains essential: polynomial unimodular equivalence of (Q+tK) and constant strict equivalence of the pencil are different classification problems.

Tests include valid transforms, tampering, a non-unimodular candidate, rectangular pencils, shape validation, and budget exhaustion.
