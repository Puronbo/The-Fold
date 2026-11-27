# Stage 22 — Exact invariant discovery for affine transformations

## Purpose

Extract structural properties from an affine self-transformation and verify which properties survive a change of coordinates. This is a first controlled invariant-discovery engine, not unrestricted invariant search.

## Transformation and conjugacy

Let

\[
f(x)=ax+b
\]

and let the invertible coordinate change be

\[
\phi(x)=sx+t,\qquad s\ne0.
\]

The transformed self-map is the conjugate

\[
g=\phi\circ f\circ\phi^{-1},
\]

which simplifies exactly to

\[
g(x)=ax+sb+t(1-a).
\]

Thus the multiplier (a) is invariant. If (a\ne1), the unique fixed point is

\[
x_* = \frac{b}{1-a},
\]

and its coordinate changes covariantly:

\[
x_*' = \phi(x_*).
\]

The fixed point's numerical coordinate is not itself invariant; its existence and uniqueness are.

When (a=1), the map is a translation. It is the identity if (b=0), otherwise a nonzero translation with no fixed point. Under conjugacy the translation amount becomes (sb), so its exact magnitude is not invariant, but the identity/nonzero-translation distinction is preserved.

## API

- `discover_affine_invariants`: returns multiplier, identity status, unique-fixed-point status and location, and nonzero-translation status.
- `conjugate_affine_transformation`: derives the transformed map algebraically.
- `verify_affine_conjugacy`: checks the exact conjugacy equation and the corresponding invariant/covariant properties.

## Proposition

For every affine map (f(x)=ax+b) and every invertible affine coordinate change (phi(x)=sx+t), the conjugate (phi f\phi^{-1}) has multiplier (a). If (a\ne1), its unique fixed point is the image under (phi) of the source fixed point.

**Proof.** Since (phi^{-1}(x)=(x-t)/s),

\[
\phi(f(\phi^{-1}(x)))
=s\left(a\frac{x-t}{s}+b\right)+t
=ax+sb+t-at.
\]

The multiplier is (a). The source fixed point satisfies (x_*=ax_*+b); applying (phi) gives a fixed point of the conjugate. Since (a\ne1), the affine fixed-point equation has exactly one solution. Therefore that solution is (phi(x_*)). \(\square\)

## Limits

- Only one-dimensional affine self-maps over exact rational numbers.
- The transformation family is specified in advance; the system does not search all possible functions or invariants.
- Coordinate maps must be invertible and caller-declared.
- Finite examples do not establish arbitrary nonlinear invariants.
- This stage is exact symbolic analysis, not a general theory of intelligence.
