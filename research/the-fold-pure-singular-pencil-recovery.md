# G-EP48 — Multiple-chain pure singular pencil recovery

## Goal

G-EP47 composed already separated components. G-EP48 removes that limitation
for two important subclasses: a pencil that is purely right-singular, with
any number of right Kronecker blocks, or purely left-singular, with any
number of left blocks.

## Construction

The implementation first computes exact polynomial nullspace certificates
for both sides. It proceeds only if:
- the right minimal basis is complete through the requested degree bound;
- the opposite (left) polynomial kernel is empty;
- the recovered right minimal indices account for the full domain/codomain
  dimensions.

For each right minimal-vector generator
[
z(t)=z_0+z_1t+cdots+z_et^e,
]
the algorithm reverses the coefficient chain and applies alternating signs.
All resulting vectors are concatenated into a domain basis (T). The
corresponding shifted images (Kz_1,ldots,Kz_e), across all generators,
are concatenated into a codomain basis (B). It sets (S=B^{-1}), then
checks the exact identities against the direct sum of canonical right
Kronecker blocks. Left-only pencils use the transposed construction and
transpose the resulting witnesses back.

The routine never accepts a candidate merely because the dimensions look
right: bounded polynomial-kernel span certificates, both basis determinants,
and the final strict-equivalence audit must pass.

## API

`tools/pure_singular_pencil_recovery.py` provides
`recover_pure_singular_pencil_structurally(q,k,p,side=...)`. It returns the
recovered minimal-index list, canonical pair, explicit constant (S,T),
and independent audit.

## Boundary

This is genuine automatic block recovery for pure right-only and pure
left-only pencils, including multiple blocks after arbitrary constant
scrambling. It does not recover a regular summand, nor a pencil containing
both left and right singular blocks. Those require constructing compatible
singular subspaces and regular complements simultaneously; that remains the
next target rather than being inferred from dimension counts alone.

## Tests

Tests cover multiple blocks with unequal indices on both sides, a
nontrivially scrambled right-only direct sum, and rejection of a regular
pencil.
