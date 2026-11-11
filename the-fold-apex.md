# One point, both sides, all angles

## The phrase

"One point extending at both sides at all angles" separates into four claims, and each is exact if
read structurally:

| word | structure | mathematical object |
|---|---|---|
| one point | the apex | `P₀` |
| both sides | the antipodal identification `v ~ −v` | `ℝPⁿ⁻¹ = Sⁿ⁻¹/(±1)` |
| all angles | the whole pencil, no aperture selected | `ℝPⁿ⁻¹`; cones over all `α` |
| extending | the rays and cones from the point | `T_{P₀} = ℝⁿ`; the cone family |

The sentence is not about a point that grows. It is about the **pencil at a point**: the point is the
common apex of every ray, line, crease and cone, and "both sides" is the identification that makes the
pencil projective. The point does not extend; its tangent cone does. That distinction is the whole
note.

## Both sides: one crease, two normals

A crease through `P₀` with unit normal `n` is

```
H_n = { x : (x − P₀)·n = 0 }
```

and `H_n = H_{−n}`. So a crease is indexed by an **unoriented** normal — by a point of `ℝPⁿ⁻¹`. A fold
is determined by its crease (the reflection in `H_n` is unique), so the folds through the point are
exactly the points of the projective sphere:

```
folds through P₀  ≅  ℝPⁿ⁻¹
```

The two sides are not two folds; they are one fold seen from either side. That is the exact content of
"both sides": the sign of the normal is not observable, so the parameter space quotients `Sⁿ⁻¹` by
`±1`, with the 2-to-1 cover

```
Sⁿ⁻¹ → ℝPⁿ⁻¹,   v ↦ [v]          fiber {v, −v}
```

In the plane `ℝP¹ ≅ S¹`: the two sides of a line are the two preimages of one point of the circle of
creases, and `θ` and `θ + π` give the same line.

This also explains the occlusion note's side-blindness in one line. The metric `|·|²` cannot see the
sign of the normal; the fold **is** the sign change; the crease is the fixed set. "Both sides" is the
orbit `{P, σ_H P}` of a point, not a pair of objects.

The folded line from afar is the one-dimensional picture of the same identification: the V's two rays are
the two signs of the height, and its shadow is one line. See `the-fold-afar.md`.

## All angles: the pencil

The creases through `P₀` form the **pencil**

```
{H : P₀ ∈ H}  ≅  ℝPⁿ⁻¹
```

Every crease contains `P₀`, and every point of the pencil is a crease through it. In the plane the
pencil is a circle: a line's angle is defined mod `π`, and the map `θ ↦ 2θ` is the double cover
`S¹ → S¹` that identifies `θ` with `θ + π`. So "at all angles" is literally a circle's worth of creases
in two dimensions, and `ℝPⁿ⁻¹` in general.

The point is the **intersection** of its pencil and the pencil **covers** the space:

```
⋂_{H ∋ P₀} H = {P₀}              ⋃_{H ∋ P₀} H = ℝⁿ        (n ≥ 2)
```

The intersection is exact: a point `x ≠ P₀` is excluded by the crease with normal `x − P₀`, because
`(x − P₀)·(x − P₀) = |x − P₀|² ≠ 0`. So the point is both the source and the residue of all its
creases: everything is on some crease through it, and only it is on all of them. (In `n = 1` the only
crease is the point itself, and the pencil is a single point.)

This is the first exact reading of the phrase: **one point, a projective sphere of creases, each crease
extending both ways, and the point as the unique common point.**

## Extending: the cones

A cone with apex `P₀`, axis `n` and aperture `α` is the set of rays making angle at most `α` with `n`.
One nappe is a sector; the double cone is both:

```
D(n, α) = { x : |x_⊥| ≤ tan α · |x_∥| },        x = P₀ + x_∥ n + x_⊥
```

The two nappes are the two signs of `x_∥` — "both sides." The aperture ranges over `[0, π/2)`. On
the **surface** the crease is the limit `α → π/2` (where `x_∥ = 0`), and `α = 0` is the axis line; the
solid at `α = π/2` would be the whole space, which is why the family stops before the crease. So "at
all angles" is the whole family of proper apertures, with the fold as its boundary — not as a member.

For a fixed axis, the cone **surfaces** sweep out the space minus the apex: every `x ≠ P₀` has a
definite aperture relative to `n`,

```
α(x) = arctan( |x_⊥| / |x_∥| )          α = 0 on the axis, α → π/2 on the crease
```

with the crease as the limiting surface, not a member of the proper family. So "at all angles" is a
coordinate, not a heap: each point of space has a definite aperture relative to a chosen axis. Over all axes, the cones cover everything and intersect only at the point:

```
⋃_{n, 0≤α<π/2} D(n, α) = ℝⁿ              ⋂_{n, 0≤α<π/2} D(n, α) = {P₀}
```

The first holds because any `x` lies on the axis cone with `n = (x − P₀)/|x − P₀|` (and `P₀` is in
every `D`). The second holds
because any `x ≠ P₀` is excluded by an axis perpendicular to `x − P₀`: then `|x_∥| = 0` while
`|x_⊥| = |x − P₀| > 0`, so the inequality fails at every proper aperture. Again the point is the common
apex and the unique common point; its extensions cover the space, and only it survives all of them.

(Range cones are the bounded version of the same sector: the cone note's `C` adds `t ≤ R` and cuts the
outer face on a sphere. The apex and the aperture are the same data; the range is the size.)

### The double cone is an orbit

Fix `n` and `α`, and take one unit direction `u₀` at angle `α` from the axis. Rotating about `n`
sweeps the circle of directions at that aperture; flipping the axis gives the other nappe. The group
is `O(n−1) × {±1}`, and the **directions** of the double cone are one orbit:

```
dir(∂D(n, α)) = (O(n−1) × {±1}) · u₀          on Sⁿ⁻¹
```

The surface adds the radius: `∂D(n, α) ∖ {P₀} = ℝ₊ · dir(∂D(n, α))`. The solid is the union of the
surfaces at apertures `β ≤ α`, together with the apex. So the phrase is an **orbit statement**: one
ray, all rotations about the axis ("all angles"), both signs of the axis ("both sides"), the apex
fixed by all of them. That is the cleanest exact reading, and it is checked below: 200 random
rotations and flips stay on the cone, and every direction of the surface is reached.

## The correction: what the point does not have

"Extending" invites a category slip: the point does not extend; its **tangent cone** does. The Fold's
point has, and lacks, exactly this:

| it has | it does not have |
|---|---|
| the tangent space `ℝⁿ` | a metric: the form is `0`, inertia `(0,0,n)` |
| the direction sphere `Sⁿ⁻¹` (or `ℝPⁿ⁻¹`) | a selected direction: no axis, no aperture |
| the tangent cone `ℝⁿ` | a tangent *plane*: the limit of a surface at the vertex is a cone |
| zero of every measure | any size |

Two corpus statements sound contradictory and are both true:

- "the point carries all `n` unsigned directions, the sphere `Sⁿ⁻¹`" — the initial form;
- "the point has no tangent space" — the range cone.

Read the second as **no tangent plane**: the limit of the surface's tangent planes at the vertex is the
cone of apertures, not a single plane. The tangent *space* exists as the ambient `ℝⁿ`; the tangent
*cone* is the whole space; what fails is a unique plane. And the point lacks a metric, not directions.
This note's phrase is the reconciliation: all directions, both sides, no selected angle.

The corresponding sentence in the cone note — "the point has no directions" — needs the same
qualifier: it has no **selected** direction. That wording is corrected at the source.

## The light cone: an exact cousin

In Minkowski `ℝ^{1,n−1}` with `η = diag(−1, +1, …, +1)`, the null cone at an event is

```
N = { x : η(x, x) = 0 } = N₊ ∪ N₋
```

two nappes (`t > 0` and `t < 0`), each diffeomorphic to `S^{n−2}`. The identity component of the
Lorentz group acts transitively on the future null rays, so `N₊` is the orbit of one null ray — the
same sentence, one point, both sides, all angles, in Lorentzian signature. "Both sides" is future/past; "all angles" is the
`S^{n−2}` of spatial directions; "one point" is the event.

This is exact geometry, and it is a **cousin**, not a new Fold claim:

- the light cone is the set of null *directions* at a point;
- the horizon is a null *hyperplane* (the crease), with induced form `(n−2,0,1)`;
- they meet in the word "null," but the cone is not the horizon. See `the-fold-horizon.md` and
  `the-fold-signature.md`.

Do not read the Lorentzian signature back into the Euclidean Fold: the Fold's point carries the zero
form, not a Lorentzian one. The cousin is a rhyme of structure — double cone, two nappes, transitive
direction group — not an identification, and it proves nothing about the zeta case.

## Checks (NumPy)

| check | value |
|---|---|
| a point of `H_n` has signed distance `0` to `H_{−n}` | `0.0` |
| rank of 20 normals through `P₀`; `\|sol − P₀\|` | `3`; `6.7e−16` |
| `\|v(θ) + v(θ+π)\|` | `≤ 6.0e−16` |
| residual of `x` on its own aperture cone | `≤ 3.4e−16` |
| residual of `x` with axis `⊥ x` at `α = 0.3` | `1.0` (the exclusion) |
| orbit residual, 200 rotations and flips | `≤ 1.1e−16` |
| reachability miss, random point at the same aperture | `≤ 1.1e−16` |
| null-cone residual; signs of `t` | `≤ 1.2e−15`; `+`, `−` |

The first two rows are the pencil: one crease per unoriented normal, and only the point on all of them.
The middle rows are the cones: every point on exactly one aperture, everything on some axis cone,
nothing but the apex on all of them. The orbit rows are the phrase itself. The last row is the
Lorentzian cousin.

## What this does and does not say

- It **does** give an exact reading of all four claims: apex, `ℝPⁿ⁻¹`, the pencil, the cone family.
- It **does** identify the space of folds through the point as `ℝPⁿ⁻¹`: the two sides are one fold.
- It **does** prove the union/intersection law: the point is the source and the residue of all its
  extensions.
- It **does** reconcile "all directions" with "no tangent space": no tangent *plane*, no metric, but
  the tangent space and the direction sphere exist.
- It **does not** make the point extend, have size, or have a metric.
- It **does not** identify the light cone with the horizon; the cone is directions, the horizon is a
  null hyperplane.
- It **does not** fix a side of the normal: `ℝPⁿ⁻¹` is the quotient, not a choice.
- It **does not** say anything about the zeta zeros; the cone family is geometric.

## The one sentence

**One point extending at both sides at all angles is the point as the common apex of its pencil: rays
are `Sⁿ⁻¹`, lines and creases are `ℝPⁿ⁻¹` with the two sides identified, the cones at all apertures
cover the space and intersect only at the point, and the extension belongs to the tangent cone, not to
the point.**

## Files

`the-fold-apex.md` (this note). The range cone and the vertex's solid angle are in
`the-fold-cone.md`; the initial state, the null form and the direction sphere are in
`the-fold-initial.md`; the side-blindness and the crease are in `the-fold-occlusion.md`; the
Lorentzian crease and the horizon signature are in `the-fold-horizon.md` and
`the-fold-signature.md`; the fold's parameter and the ledger are in `the-fold-key.md`; orbits and
universal constructions are in `the-fold-categorical.md`.
