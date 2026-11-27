# Stage 21 — Compositional abstraction

## Goal

Represent a concept as a sequence of reusable transformations, distinguish path structure from endpoint behavior, and transfer the entire path across changed representations.

## Composition

For affine edges

\[
f_i(x)=a_i x+b_i,
\]

their composition is affine. The implementation retains the original ordered steps and also derives the endpoint map. For example, the three-edge path

\[
x\mapsto 2x+3\mapsto 3(2x+3)-1\mapsto \tfrac12(3(2x+3)-1)+4
\]

has endpoint map

\[
F(x)=3x+\tfrac{11}{2}.
\]

A direct one-step law with this endpoint map is endpoint-equivalent, but not structurally equivalent to the three-step path. The distinction matters when intermediate states carry meaning or constraints.

## Layered representation transfer

Give each layer its own invertible affine coordinate map:

\[
\phi_i(x)=s_i x+t_i,\qquad s_i\ne0.
\]

For each edge (f_i:X_i\to X_{i+1}), derive

\[
f'_i=\phi_{i+1}\circ f_i\circ\phi_i^{-1}.
\]

The required commuting identity is

\[
\boxed{\phi_{i+1}(f_i(x))=f'_i(\phi_i(x)).}
\]

The implementation derives every transformed edge algebraically and checks every intermediate layer for each supplied input. It does not refit from target examples.

## API

- `CompositionalAffineConcept`: immutable ordered path of affine concepts.
- `composed`: endpoint relation, without discarding the original path.
- `compare_compositional_structure`: reports structural equivalence, endpoint-only equivalence, or non-equivalence.
- `transfer_compositional_concept`: transfers all edges through one coordinate map per layer and checks every commuting square.

## Limits

- Scalar affine maps only; no nonlinear or multivariate paths.
- Coordinate maps are caller-supplied, not inferred.
- Supplied inputs test the commuting identity but do not prove semantic correspondence of representations.
- The path representation is preserved, but this stage does not infer what intermediate states mean.
- No causal discovery, noisy learning, open-world concept discovery, or AGI claim follows.
