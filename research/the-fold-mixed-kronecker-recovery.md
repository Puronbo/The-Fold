# G-EP49 — Bounded automatic mixed Kronecker recovery

## Goal

G-EP48 recovered pure right-only and pure left-only pencils. G-EP49
extends recovery to an unsplit pencil with right singular blocks, a regular
part, and left singular blocks.

## Construction

1. Compute the complete finite-field Kronecker profile: both lists of
   polynomial minimal indices, the normal rank, finite Smith invariant
   factors, and infinity t-adic elementary-divisor sizes.
2. Assemble the corresponding canonical mixed target from right and
   transposed-left Kronecker blocks plus finite companion and infinity
   nilpotent regular blocks.
3. Search a structured, bounded family of invertible left transformations.
   For each candidate S, solve the equations
   `S Q T = Q_can` and `S K T = K_can` simultaneously as one affine
   linear system in the entries of T.
4. Test invertibility of T and independently audit both strict-equivalence
   identities and both determinants over F_p.

This avoids pretending that the polynomial minimal-vector chains alone
supply compatible complementary bases in the mixed case. The profile
determines the target; the explicit constant witness is constructed by the
bounded linear-algebra search.

## API

`tools/mixed_kronecker_recovery.py` exposes
`recover_mixed_kronecker_pencil(q,k,p,...)`.

A successful result includes the discovered right and left minimal indices,
regular dimension, canonical target, explicit S and T, profile, and exact
audit. If the profile is incomplete or the structured search budget is
exhausted, the routine returns `recovered=false` and
`decision_complete=false`. Search failure is not treated as inequivalence.

## Limitations

This is a bounded constructive recovery algorithm, not a polynomial-time
general Kronecker canonical-form algorithm. The left-transform candidate
family is structured (permutations, diagonal scalings, and one elementary
shear); arbitrary mixed pencils may require transformations outside the
searched family. The profile calculation is itself bounded by the configured
minimal-index degree and minor budgets. Every positive result is exact and
independently verified; negative/incomplete search results are inconclusive.

## Tests

Tests cover an unsplit direct sum containing a right block, a left block,
and a regular block; recovery after a nontrivial left-basis shear; and
explicit rejection of an incomplete bounded profile.
