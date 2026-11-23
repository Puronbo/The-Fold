# G-EP54 — Exact residual-pencil decoupling certificates

G-EP54 adds `tools/residual_pencil_decoupling_certificate.py`, building on
the four-block partition returned by G-EP53.

The certificate inspects both off-diagonal blocks in both coefficient
matrices. It reports their exact ranks and nonzero entries over the supplied
finite field. If all four off-diagonal blocks vanish, it reconstructs the
block-diagonal pair and checks exact equality with the G-EP52 adapted pair.
The result carries the exact left/right basis matrices and the verified
strict-equivalence identities.

If coupling is present, the result is negative: it exposes the obstruction
entries and ranks, but does not claim a direct-sum decomposition. The
reconstructed block pair is still included as an audit artifact, and its
equality checks will fail when the original adapted pair contains coupling.

## Scope boundary

A positive certificate proves a direct-sum decomposition in the computed
adapted coordinates. It does not establish that the bottom-right block is
regular, nor that the bounded minimal-chain search found every chain in every
input. Residual regularity remains a separate question answered only when
supported by the residual profile and its own completeness conditions.

## Tests

Tests cover a canonical mixed right/left/regular pencil and a synthetic
coupled block partition. The former checks the exact reconstructed identities
and carried basis witnesses; the latter checks that nonzero coupling is
reported with ranks and explicit entries, without a decomposition claim.
