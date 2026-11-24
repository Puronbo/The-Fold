# G-EP51 — Minimal-chain geometry certificates

## Goal

G-EP49–50 recover mixed canonical targets by bounded or exhaustive witness
search. G-EP51 adds a structural diagnostic between polynomial minimal-basis
recovery and mixed-basis construction: measure the exact subspaces generated
by the coefficient chains.

## Construction

`tools/minimal_chain_geometry.py` exposes
`minimal_chain_geometry_certificate(Q,K,p,...)`.

- Right polynomial-kernel generators contribute coefficient vectors in the
  domain. The routine forms their combined coefficient matrix and computes
  its exact rank over the base field.
- Left polynomial-kernel generators of the transposed pencil contribute
  coefficient covectors on the codomain. Their combined matrix rank is
  computed independently.
- The recovered vector/covector counts are compared with the sums of
  (minimal-index + 1), and the underlying bounded-degree nullspace
  certificate is returned for auditability.

## What this proves—and what it does not

A full-rank result certifies linear independence of the corresponding
minimal-chain coefficient family. It does not prove that the right and left
families are mutually compatible, that their complements are regular
invariant pieces, or that a mixed strict-equivalence decomposition exists.
The routine intentionally does not manufacture complementary bases or
claim a general Kronecker-form algorithm.

This gives the next structural recovery stage exact, machine-checkable
rank data rather than assuming that minimal chains automatically split a
mixed pencil.

## Tests

The tests cover a canonical right + left + regular direct sum, where both
minimal-chain families are independent but neither fills its ambient space,
and a regular pencil with empty minimal-chain families.
