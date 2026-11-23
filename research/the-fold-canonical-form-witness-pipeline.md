# G-EP41 — canonical-form transformation certificates

G-EP41 connects canonical block assembly (G-EP40) with exact strict-equivalence witnesses (G-EP38/39) through a single API.

## Workflow

For a regular square pencil ((Q,K)):

1. Compute the complete finite/infinity elementary-divisor profile.
2. Assemble the canonical block pair ((Q_{can},K_{can})).
3. Independently verify that the canonical pair has the same complete profile.
4. Invoke the strict-equivalence witness constructor on the source and canonical pairs.
5. Return constant matrices (S,T) only if the exact witness verifier confirms
   [
   SQT=Q_{can},\qquad SKT=K_{can},
   ]
   and both matrices are invertible.

The API is `regular_pencil_canonical_witness` in `tools/regular_pencil_canonical_witness.py`.

## Two execution paths

- If a shared invertible projective member exists over the base field, the operator-intertwiner method is used.
- Otherwise, the G-EP39 direct finite-field search is used. It enumerates left transforms and solves linearly for right transforms.

## Guarantees and limitations

The canonical target and its profile check are deterministic. Returned transformations are exact, constant, and independently verified. The no-chart fallback is exponential and budget-bounded. If its budget is exhausted, the API reports that no witness was found without asserting non-equivalence. Thus G-EP41 is an integrated certificate pipeline, not yet the hoped-for scalable blockwise reduction algorithm.

This distinction is important: matching complete profiles prove strict equivalence for regular pencils, while finding a compact explicit certificate can remain computationally expensive.
