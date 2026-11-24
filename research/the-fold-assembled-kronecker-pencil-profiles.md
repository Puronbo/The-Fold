# G-EP26 — Assembled Kronecker structure data for linear pencils

For P(t)=Q+tK over F_p[t], G-EP24 computes nonzero Smith invariant
factors in the finite chart and reversed chart K+tQ. G-EP25 recovers right
and left polynomial minimal indices. G-EP26 assembles these pieces and
checks the dimension identities of the Kronecker block decomposition.

## Data assembled

- Finite regular elementary divisors: factor data encoded by Smith invariant
  factors of Q+tK.
- Infinite regular elementary divisors: corresponding data from K+tQ.
- Right minimal indices epsilon_i from bounded-degree polynomial right
  nullspaces.
- Left minimal indices eta_j from bounded-degree polynomial left nullspaces.

If r is the normal rank, the regular-part dimension n0 is
n0 = r - sum(epsilon_i) - sum(eta_j).

For a Kronecker decomposition, row and column dimensions obey
m = n0 + sum(epsilon_i) + sum(eta_j+1),
n = n0 + sum(epsilon_i+1) + sum(eta_j).

The total degree of finite regular elementary divisors plus the total degree
of infinite regular elementary divisors must equal n0. The implementation
checks these identities independently of minimal-index recovery.

## Implementation

The module tools/pencil_kronecker.py exposes
rectangular_pencil_kronecker_profile(Q,K,p,max_degree=8,max_minors=2000).
It combines G-EP24 and G-EP25 outputs. The report is complete only if both
minimal-index lists are recovered within the requested degree cap and all
dimension/degree identities pass. A too-small degree cap yields an
explicitly incomplete report.

Tests cover a regular pencil, right and left singular blocks, a direct sum
of regular and singular blocks, and incomplete recovery under a low degree
bound.

## Scope

This is complete Kronecker block-size data when all checks pass, but not a
canonical-form transformation: no unimodular polynomial matrices are
constructed. The polynomial Smith calculation remains combinatorial and
uses a minor budget; it is intended for small dense pencils. Arithmetic is
exact over prime fields. This algebraic descriptor does not establish
transformer functional or semantic equivalence.
