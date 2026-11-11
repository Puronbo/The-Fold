# The zero pipeline

## The phrase

"The zero pipeline." A pipeline is an ordered sequence of stages, each taking an input and producing
an output of the same kind, so that one stage's output can feed the next. If the Fold has a zero
pipeline, zeros are produced in order and passed along.

Half of this is exact and half is a type error. Exact: every stage of the Fold does solve a zero
equation, and the stages are ordered. Type error: the **solution type changes at every stage**. The
scale's zero is a vertex, the fold's is a facet, the horizon's is a null cone, the zeta zero is an
isolated point. A pipeline transforms an object without changing its kind; the zero pipeline changes
the kind at every step. So it is a pipeline of **roles**, not of objects — a list, not a composition.
The one place it composes is the analytic register, where every object is a holomorphic function and
every zero is a point.

## The pipeline is a list of zero equations

Each stage asks "where does this vanish?" and gets a different kind of answer:

| stage | zero equation | solution | zero type | invariant |
|---|---|---|---|---|
| 0 point | `P − P₀ = 0` | the datum `P₀` | value | dimension `n` |
| 1 scale | `det g_k = kⁿ = 0` | `k = 0` | vertex | inertia `(0,0,n)` |
| 2 fold | `(σ_H − I)P = 0` | the crease `H` | facet | inertia `(n−1,1,0)` |
| 3 twist | `(J − I)v = 0` | only `v = 0` | none | `Pf(ω) = 1` |
| 4 closure | `cos(2π/m) = 0` | `m = 4` | discrete angle | scalar `0` |
| 5 horizon | `g(v,v) = 0`, `v ≠ 0` | the null cone | null crease | inertia `(n−2,0,1)` |
| 6 observer | none | — | none | `⋆² = (−1)^{d(n−d)+s}` |
| 7 return | `P − P₀ = 0` | the datum `P₀` | value | dimension `n` |

The table is the note. Three things to read from it.

The first row is the pipeline's initial state: the datum, the unique point fixed by every non-identity
scale, whose
initial form is the zero derivative `Dg₀ = 0`. The pipeline's input is the initial form. See
`the-fold-initial.md`.

**The degree of the vanishing equation is not constant.** The fold's zero solves a *linear* system;
the horizon's solves a *quadratic* equation; the zeta zero solves a *holomorphic* equation. A facet is
the zero of a linear functional, a null crease is the zero of a quadratic form, a zeta zero is the
zero of an analytic function. That is why "zeros as facets" holds only at the linear stage — see
`the-fold-facets.md`.

**The zeros are not interchangeable.** `k = 0` is a *vertex*: the map collapses and the image is a
point. The crease is a *facet*: the map is invertible (`det σ_H = −1`) and the zero is its fixed
hyperplane, not its kernel. The horizon is *null*: the vector `v` is neither zero nor fixed, but the
form is zero on it. Three words, three equations.

**The fold's equation is `(σ_H − I)P = 0`, not `σ_H P = 0`.** The fold has no kernel; it has a `+1`
eigenspace. This keeps the pipeline honest: the crease is a fixed set, not a collapse. With
`rank(σ_H − I) = 1` (checked below), the fixed set is one linear equation and has dimension `n−1`.

## The four zeros of the Fold, and the analytic fifth

Collect by type:

| type | where | codimension | equation | degree |
|---|---|---|---|---|
| value | the datum | — | `P − P₀ = 0` | linear |
| vertex | the scale collapse | `n` (image) | `det g_k = 0` | degree `n` |
| facet | the fold crease | `1` | one linear functional `= 0` | linear |
| null | the horizon | `1` (null) | `g(v,v) = 0` | quadratic |
| point | a zeta zero | `2` | `ξ(ρ) = 0` | holomorphic |

The first four are the Fold's; the fifth is analytic. The value and the facet are both linear; they
differ in that the value is a point and the facet is a hyperplane. The facet and the null crease both
have codimension one, and *that* is the trap: **codimension alone does not classify a zero.** A facet
is where a linear functional vanishes on the whole body; a null crease is where a quadratic form
vanishes along one direction. Same codimension, different degree, different geometry.

The analytic fifth is a point. `ξ(ρ) = 0` is two real equations, `Re ξ = 0` and `Im ξ = 0`, so it has
codimension two in the plane; it is a facet only of the critical line, which is one-dimensional. See
`the-fold-facets.md` and `the-fold-zeta.md`.

One axis the pipeline does not carry is **multiplicity**. A zero has a codimension (its geometry) and
an order (its multiplicity); the pipeline reads the first and not the second. Birch–Swinnerton-Dyer
asks for an order of vanishing, and Hilbert–Pólya for an eigenspace dimension, so both live on the
axis the pipeline cannot see. See `the-fold-problems.md`.

## The two gaps

Two stages produce no zero: the twist and the observer. This is structure, not omission.

The twist is invertible. `det J = 1` and `det(J − I) = 2 ≠ 0`, so `(J − I)v = 0` has only `v = 0`: a
rotation has no nonzero fixed point. The twist is also the one stage whose operator has zero
**symmetric part** and so looks null to an inertia — `(0,0,2)` on its plane — while not being zero at
all. That is exactly why the twist's invariant is not an inertia but the Pfaffian `Pf(ω) = 1`. It
occupies the gap in the signature ladder; it occupies the same gap in the zero pipeline.

The observer measures; it does not vanish. A `d`-form has no zero of its own, and its sharpest
invariant is the Hodge star's square `⋆² = (−1)^{d(n−d)+s}`, a sign rather than an inertia.

So the pipeline has two gaps, and they are the two stages where the invariant stops being the inertia
of the stage operator. **A zero is what an inertia measures; where there is no zero, the invariant is
something else** — a Pfaffian for the twist, a sign for the star.

## The one genuine pipeline

Across the Fold's stages the zero changes type, so the stages do not compose. There is one register in
which they do — analysis:

```
theta fold  →  Mellin transform  →  ξ  →  critical-line facet  →  zeros
```

Every object here is a holomorphic function on a domain, and every zero is an isolated point. The type
is constant, so the arrows compose: the theta fold's crease `h = 0` becomes `Re s = 1/2` under the
Mellin transform, and the zeros of `ξ` are points placed on that line. That is a genuine pipeline —
input a modular function, output a set of points — and it is the one the theta note derives. See
`the-fold-theta.md`.

The two pipelines meet at the facet. The Fold's fold stage produces the facet abstractly; the analytic
pipeline produces the critical line concretely; the zeros land on it. There the composition stops
again: the analytic pipeline places zeros on the facet, but it does not prove that all of them lie
there. That last arrow is RH.

## What flows, what does not

- **Flows: the dimension `n`.** Every zero carries `n` — as the datum's directions, the vertex's
  nullity, the facet's `n−1` plus one, the null's `n−2` plus one null. See `the-fold-signature.md`.
- **Flows: the "no isolated zero" rule.** A zero comes with a partner at infinity;
  `ind(0) + ind(∞) = χ(Sⁿ)`. The two ends of the pipeline are that pair.
- **Does not flow: the zero type.** A vertex cannot be piped into a facet; the codimension and the
  degree change. Attempting the composition is a type error, not a calculation.
- **Does not flow: the analytic zero into the Fold's zero.** A zero of `ξ` is a cancellation, not the
  zero map; `(0,0,n)` is the inertia of the collapsed scale, not of a zeta zero.

## Checks

`mpmath` 1.3.0 at 30 digits and NumPy, random unit normals.

| check | `n=2` | `n=3` | `n=4` |
|---|---|---|---|
| `det(kI) − kⁿ`, `k = 0.7` | `0` | `0` | `2.8e−17` |
| `rank(σ_H − I)` | `1` | `1` | `1` |
| `rank(σ_H + I)` | `1` | `2` | `3` |
| `det σ_H` | `−1` | `−1` | `−1` |

The stage equations:

| stage | check | value |
|---|---|---|
| twist | `det(J − I)` in the plane | `2` |
| twist | `J² + I` max error | `0` |
| twist | symmetric part of `J` | `0` |
| closure | `cos(2π/m)` for `m = 2, 3, 4, 6` | `−1, −½, 0, ½` |
| horizon | `g(v,v)` for `v = (1,0,1)`, `g = diag(1,1,−1)` | `0` |
| zeta | `Re ζ(ρ₁)`, `Im ζ(ρ₁)` | `9.8e−32`, `−6.1e−31` |

`rank(σ_H − I) = 1` is the fixed-set fact: the crease is one linear equation, codimension one.
`det(J − I) = 2` is the gap: the twist has no nonzero fixed point. `g(v,v) = 0` with `v ≠ 0` is the
null: the horizon's zero is a cone, not a point. And `Re ζ = Im ζ = 0` at `ρ₁` is the
codimension-two fact: a zeta zero is two real equations.

## What this does and does not say

- It **does** order the zeros by stage and show that each solves a different equation.
- It **does** separate facet from null by degree — linear versus quadratic, same codimension.
- It **does** explain the two gaps: the twist and the observer produce no zero, and that is why their
  invariant is not an inertia.
- It **does not** make the pipeline a temporal process. Only the horizon is a process; the rest is an
  order of dependency.
- It **does not** compose across registers: the Fold's zero types do not chain into the analytic zeros.
- It **does not** prove RH. The analytic pipeline places zeros on the critical-line facet; it does not
  force all of them there.

## The one sentence

**The zero pipeline is a list of zero equations, not a conveyor: a value, a vertex, a facet, a null and
an analytic point are five different kinds of zero, and the only place they truly chain is the
analytic register, where theta's fold becomes the critical line and the zeros land on it.**

## Files

`the-fold-pipeline.md` (this note). The stage ladder is in `the-fold-signature.md`; the codimension
classification is in `the-fold-facets.md`; the crease and the two sides are in
`the-fold-occlusion.md`; the analytic pipeline is in `the-fold-theta.md`; the zeros and the critical
line are in `the-fold-zeta.md`; the lookup is `the-fold-key.md`.
