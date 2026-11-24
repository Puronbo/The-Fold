# G-EP42 — cyclic Krylov construction of regular-pencil witnesses

G-EP42 adds a structured fast path for the important cyclic-operator case in a shared invertible projective chart.

## Mathematical construction

Suppose the chart normalization produces operators (A,B\in M_n(\mathbb F_p)) with the same single rational-canonical invariant factor of degree (n). Both operators are cyclic. Choose cyclic vectors (v_A,v_B), so their Krylov matrices
[
K_A=[v_A,Av_A,\ldots,A^{n-1}v_A],\qquad
K_B=[v_B,Bv_B,\ldots,B^{n-1}v_B]
]
are invertible. Define
[
P=K_BK_A^{-1}.
]
Then (PA=BP), because both operators act by the same companion relation in their respective Krylov bases. The implementation nevertheless checks this intertwining identity and invertibility exactly before using (P) to recover the pencil transformations.

This replaces enumeration of the full (n^2)-dimensional intertwiner space by finding two cyclic vectors and one matrix inverse.

## Search and fallback

The implementation tries vectors in deterministic finite-field order, subject to the existing candidate budget. If it cannot find cyclic vectors within that budget, or the operators are not cyclic, it falls back to the existing general intertwiner-space algorithm. The no-rational-chart case still uses the G-EP39 direct search.

The witness result reports `intertwiner_construction_method` and the number of cyclic-vector candidates examined. The canonical-witness API propagates the actual method.

## Scope

This is a guaranteed construction once cyclic vectors are found, but it is not yet a full primary-block decomposition algorithm for arbitrary noncyclic operators. The next step is to extend the Krylov construction to a direct sum of primary cyclic modules and assemble the maps blockwise.
