# G-EP52 — Minimal-chain adapted coordinates

G-EP52 extends the G-EP51 rank diagnostic into an explicit coordinate
construction. Given a rectangular pencil (Q+tK) over (mathbb F_p), it:

1. Recovers the bounded-degree polynomial right and left nullspace generators.
2. Extracts independent coefficient vectors from the right chains and
   independent coefficient covectors from the left chains.
3. Greedily completes each family to a full basis using standard coordinate
   vectors over the field.
4. Forms the domain basis matrix (T) and codomain row-basis matrix (S).
5. Computes (Q'=SQT) and (K'=SKT), and verifies both identities and
   invertibility of (S,T) exactly.

The first columns of (T) span the right-chain coefficient space; the first
rows of (S) span the left-chain coefficient-covector space. The remaining
rows and columns are chosen complements, not canonical regular summands.
The complete transformed matrices are returned so that cross-coupling is
visible rather than silently discarded.

## Scope boundary

This is a certified adapted-coordinate construction, not a mixed Kronecker
decomposition algorithm. In particular, it does not assert that the
bottom-right residual block is regular or that off-diagonal blocks vanish.
Profile completeness remains bounded by the explicit polynomial degree and
minor-search limits of the nullspace certificate.

## Tests

Tests cover a right + left + regular canonical direct sum and an arbitrary
invertible row/column scrambling of that example over (mathbb F_5).
