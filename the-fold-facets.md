# Zeros as facets

## The phrase

"Zeros as facets to reality." A facet is a face of codimension one. The phrase is exact for some
zeros and false for others, and the difference is the codimension. Once the codimension is counted,
the sentence becomes a small classification: the fold's zero is a facet, the scale's zero is a vertex,
and a zeta zero is a point on a facet.

## What a facet is

A convex polyhedron `P` in `ℝⁿ` is the intersection of half-spaces:

```
P = { x : a_i·x ≤ b_i,  i = 1 … m }
```

The `i`-th facet is

```
F_i = P ∩ { x : a_i·x = b_i }
```

It is the zero set, on `P`, of the slack

```
s_i(x) = b_i − a_i·x
```

So a facet is a zero of a **supporting functional**: the functional is nonnegative on the body and
vanishes exactly on the face. A vertex is a face of dimension `0`; it is the intersection of at least
`n` facets. The body is the intersection of the half-spaces, not the union of the facets; the facets
are its boundary conditions.

| zero | codimension | face | Fold name |
|---|---|---|---|
| zero of one supporting functional | `1` | facet | crease `H` |
| zero of `n` functionals | `n` | vertex | scale collapse `g₀` |
| zero of a holomorphic function in `ℂ` | `2` | point | zeta zero |
| zero on a line | `1` in the line | facet of the line | RH zero |

The table is the whole note. The rest is what each row means.

## The Fold's two zeros

The fold's zero is the crease. The fold is

```
σ_H(P) = P − 2((P − P_H)·n) n
```

and its fixed set is the hyperplane `H`, of dimension `n−1`. That is codimension one: a facet. The
normal is the one direction the fold flips; the crease is the facet it fixes. The signature
`(n−1,1,0)` is the facet's normal form: `n−1` directions along the face, one normal.

The scale's zero is not a facet. `g₀` collapses every direction; its image is a point, and a point is a
vertex, codimension `n`. The tangent space collapses to `0`; the signature is `(0,0,n)`. The scale's
zero is where all the facets meet, not one of them.

This is the two-ledger distinction in geometric form:

- **Fold ledger:** zeros are creases — facets. Each fold has its own facet, and the facets are
  distinct objects.
- **Scale ledger:** zeros are collapses — vertices. Each division point has its own vertex, and the
  vertices are distinct values.

"Zeros as facets" is the fold ledger's sentence, not the scale ledger's.

## The zeta case

A zero of `ζ` is a point in `ℂ`: it is where `Re ζ = 0` and `Im ζ = 0` simultaneously. Two real
equations, codimension two. In the plane it is a **vertex**, not a facet. The critical line is the
facet: it is the crease of the reflection `R(s) = 1 − s̄`, codimension one in the plane.

The zeros lie on the facet — that is the hypothesis. Relative to the critical line, which is
one-dimensional, each zero is a point that cuts the line into intervals: a **facet of the line**. So
the phrase is true one dimension down. In the plane, the zeros are points on the critical-line facet;
on the line, they are its facets.

Codimension alone does not classify a zero: a facet is the zero of a linear functional, a null crease
is the zero of a quadratic form, and a zeta zero is the zero of an analytic function. The same
codimension can carry a different degree. See `the-fold-pipeline.md`.

The facet's position is not arbitrary: `Re s = 1/2` is the half-density exponent of the theta fold,
and the functional equation is its Mellin shadow. See `the-fold-theta.md`.

The explicit formula is the same picture in arithmetic:

```
ψ(x) = x − Σ_ρ x^ρ/ρ − ½ ln(1 − x^{−2}) − ln(2π)
```

The zeros are the frequencies; the primes are the events. The facet is the critical line; the zeros
are its punctures.

## Reality as the cell

The facets bound the cell; the vertices are where they meet. The body is the intersection of the
half-spaces, not the union of the facets. The zeros are not holes in reality; they are the boundary
conditions that give it a boundary at all. Without them, the body is the whole space.

In the Fold, the cell is the scaled body; the facets are the creases; the vertex is the collapse. The
body is what the facets cut out. The crease is a facet at every point of the surface, and the local
front/back is the sign of its normal. Globally there are many facets; the solid is one. The "illusion
of two" is the local normal sign; the polyhedron is the global many; the solid is the one.

That is the precise sense in which zeros are facets to reality: they are the cuts that make a body
finite. A facet is not a hole in the body; it is the body's edge.

## What is not exact

- **Not every zero is a facet.** A facet has codimension one. A zeta zero has codimension two; a
  scale zero has codimension `n`. Only the crease is a facet.
- **A zero of a function is not automatically a facet.** It is a facet only when its zero set is a
  hypersurface and the function is a supporting functional. A holomorphic zero is isolated; it is a
  point.
- **The critical line is not a boundary of the critical strip.** The strip's boundary is `Re s = 0`
  and `Re s = 1`; the critical line is the crease of the fold `R`, not a boundary of the strip.
- **The facet language does not prove RH.** It classifies the zeros by codimension. The hypothesis is
  still that the points lie on the facet.

## The one sentence

**A facet is a zero of a supporting functional: the fold's crease is a facet, the scale's zero is a
vertex, and a zeta zero is a point on the critical-line facet — so the phrase is true one dimension
down, not in the plane.**

## Files

`the-fold-facets.md` (this note). The crease and the two sides are in `the-fold-occlusion.md`; the
critical line is in `the-fold-zeta.md`; the signature at the zero is in `the-fold-signature.md`; the
two ledgers are in `the-fold-key.md`.
