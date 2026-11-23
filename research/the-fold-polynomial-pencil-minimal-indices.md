# G-EP25 — Polynomial minimal indices of rectangular pencils

For Q,K in M(m,n,F_p), consider P(t)=Q+tK over F_p[t]. G-EP24 computes
regular Smith data but not singular Kronecker blocks. This milestone recovers
left and right polynomial minimal indices exactly, subject to an explicit
degree bound.

## Coefficient convolution

A polynomial right null vector of degree at most d is x(t)=x_0+...+x_d t^d.
Equating coefficients in P(t)x(t)=0 gives
Qx_0=0, Qx_j+Kx_(j-1)=0 for 1<=j<=d, and Kx_d=0.
These equations form a block convolution matrix with (d+2)m rows and
(d+1)n columns. Its nullity h_R(d) is the dimension of the vector space
of polynomial right null vectors of degree at most d. The left sequence
comes from Q^T,K^T.

## Recovering Forney indices

The polynomial right kernel is a free F_p[t]-module. A minimal reduced
polynomial basis has right minimal indices epsilon_1,...,epsilon_s.
Its predictable-degree property gives

h_R(d) = sum_i max(0, d-epsilon_i+1).

Therefore h_R(d)-h_R(d-1) counts indices epsilon_i <= d, and the second
difference at d counts indices equal to d. The transpose gives left indices.

The number of right indices is n-r and the number of left indices is m-r,
where r is the normal rank over F_p(t). The implementation gets r from
G-EP24's exact polynomial determinantal divisors. It reports a complete
index list only when the number recovered within the requested degree bound
equals the required count. Otherwise it returns partial recovery and marks
it incomplete; a low degree cap is never silently treated as complete.

## Implementation and limits

- tools/pencil_minimal_indices.py builds exact coefficient-convolution
  matrices and uses modular Gaussian elimination.
- tests/test_pencil_minimal_indices.py checks right indices 1 and 2, mixed
  right blocks, transposed left blocks, and incomplete degree bounds.
- max_degree controls the largest minimal index that can be recovered.
- max_minors is passed to the exact G-EP24 normal-rank computation.
- Arithmetic is exact over the selected prime field.

This recovers the left and right minimal-index lists, but does not construct
unimodular transformations or a canonical block decomposition. Combined
with regular Smith data, these indices supply singular block-size data for
Kronecker classification; the software still does not emit a full canonical
form certificate. No neural-network functional or semantic equivalence
is implied.
