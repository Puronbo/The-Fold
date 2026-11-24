# G-EP53 — Residual-pencil diagnostics

G-EP53 adds `tools/residual_pencil_diagnostic.py`. It starts from the exact
adapted coordinates constructed in G-EP52 and partitions both transformed
matrices into four coordinate blocks:

- chain rows against chain columns;
- chain rows against complementary domain columns;
- complementary codomain rows against chain columns;
- the bottom-right residual pencil.

The tool reports the dimensions of the residual block and whether either
cross-coupling block vanishes. If the residual is nonempty and square, it
computes the exact rectangular-pencil Kronecker profile of that displayed
coordinate block using the existing profile engine.

## Scope boundary

A profile of the bottom-right block is **not automatically** the regular
profile of the original pencil. Nonzero cross-coupling means the block
partition is not decoupled. Even when cross-coupling vanishes in the chosen
coordinates, the result is a coordinate-level decomposition diagnostic and
still relies on the completeness limits of the underlying minimal-chain
certificate. The routine never discards cross-coupling or labels the residual
as a regular summand without separate evidence.

## Tests

Tests cover a mixed right + left + regular canonical pencil, where the
residual block is square and its profile is complete, and a pure right
singular pencil, where the residual is nonsquare and no square profile is
attempted.
