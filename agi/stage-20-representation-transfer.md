# Stage 20 — Reusable concepts across representations

## Goal

Test whether a learned relationship survives a declared change of representation. Stage 20 implements one exact family: affine relations under invertible affine coordinate changes.

## Mathematical rule

Suppose the learned source concept is

\[
y=ax+b
\]

and the new coordinates are

\[
x'=sx+t,\qquad y'=uy+v,
\]

where (s\ne0) and (u\ne0). Then

\[
y'=a'x'+b',
\qquad
a'=\frac{ua}{s},
\qquad
b'=ub+v-a't.
\]

The transformed model is computed algebraically, not refitted to the target observations.

A useful invariant is the residual:

\[
r(x,y)=y-(ax+b).
\]

Under the declared transformation,

\[
r'(x',y')=u\,r(x,y).
\]

Since (u\ne0), a zero residual remains zero, and a nonzero residual remains nonzero. Thus exact fit/refutation status is preserved even though the numerical residual changes.

## API

- `AffineCoordinateMap`: exact invertible one-dimensional coordinate map with forward and inverse operations.
- `AffineRelationConcept`: exact slope/intercept and prediction/residual operations.
- `transfer_affine_concept`: analytically transfers a concept and maps supplied observations, then checks residual covariance.

## Safeguards and scope

- Exact integers and `Fraction` values only; floats and booleans are rejected.
- Zero coordinate scales are rejected because they destroy invertibility.
- Duplicate observation keys are rejected.
- The target concept is derived from the source concept and declared maps, never fitted from target data.
- Residual zero/nonzero status is checked exactly.
- This stage covers scalar affine relationships only. It does not establish transfer for nonlinear, multivariate, noisy, causal, or semantic concepts.
- A declared coordinate map is an assumption supplied by the caller, not something inferred automatically.
- Transfer under one transformation family does not imply open-domain abstraction or AGI.

## Significance

This creates a concrete test for reusable structure: if the representation changes according to a declared invertible map, the learned law can be carried over without relearning its parameters from the target examples. The same pattern can later be generalized to dimensional analysis, matrix transformations, graph isomorphisms, and other invariant-preserving maps.
