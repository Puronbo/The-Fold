# G-EP24 — polynomial Smith profiles for rectangular pencils

G-EP23 sampled the rank of aQ+bK at every projective point over F_p. G-EP24 adds a polynomial-matrix viewpoint. For the affine chart, form P(t)=Q+tK over F_p[t]. For the projective point at infinity, use the reversed pencil K+tQ.

## Determinantal divisors

For each k, let Delta_k be the monic gcd of all k-by-k minors of P(t), with Delta_0=1. If the normal rank over F_p(t) is r, the nonzero Smith invariant factors are

d_k = Delta_k / Delta_(k-1), for 1 <= k <= r.

These factors satisfy d_1 | d_2 | ... | d_r. Their irreducible polynomial powers encode the finite elementary-divisor data visible in this chart. Reversing Q+tK exchanges the two coefficient matrices and exposes the corresponding data at infinity.

The implementation calculates polynomial determinants exactly by permutation expansion, then polynomial gcds and exact quotients. It has a configurable total-minor budget because the number of minors grows combinatorially.

## Scope and important limitation

This does **not** compute a complete Kronecker canonical form. In particular, when the pencil is singular, its left and right minimal indices are not recovered by the Smith factors alone. The output explicitly reports the normal rank and labels the result incomplete. A later step must compute polynomial nullspace bases with minimal degrees (minimal indices) before a full Kronecker classification can be claimed.

The finite and reversed charts are reported separately; they are not blindly combined into a single invariant list.

## Implementation

- `tools/pencil_smith.py`: `rectangular_pencil_smith_profile(Q,K,p)`.
- `tests/test_pencil_smith.py`: finite elementary-divisor example, singular rectangular example, strict-equivalence invariance, invalid prime, invalid budget.
- No square padding.
- Exact arithmetic over prime fields only.
- Default maximum: 2,000 minors per chart. Increase only for deliberately small matrices.

## Neural-network interpretation

For quantized rectangular projections, this supplies richer algebraic information than pointwise rank sampling. However, it is invariant under constant shared strict equivalence, not every attention-specific Q/K reparameterization. The polynomial parameter t is a formal pencil coordinate, not a model token, training step, or attention score. The fingerprints remain prime- and quantization-scale-dependent and do not imply functional or semantic similarity.
