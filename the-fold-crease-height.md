# The crease and its height

## The phrase

After the projection is dropped and the wall is mapped, what remains is a codimension-one crease and
one coordinate. The phrase is exact, but "height" has to be named, because it points in different
directions in different registers:

| register | the crease | the height | direction |
|---|---|---|---|
| affine | `H` | offset `c` | transverse |
| zeta zero | `Re s = 1/2` | `t = Im s` | longitudinal |
| zeta term | — | `h = ln n` | a scale |
| theta | `h = 0` (`t = 1`) | `h = ln t` | longitudinal |
| complexity | the instance | the witness | transverse |

In every geometric register the crease is codim 1. The height is whichever coordinate it leaves free —
and in the zeta register it leaves free the coordinate **along** the crease, not across it. That is the first
correction: the affine and analytic heights are different coordinates with the same name.

## The affine pair: a crease and its offset

An affine crease with unit normal `n` and height `c` is

```
H_{n,c} = { x : n·x = c }
```

`(n,c)` and `(−n,−c)` are the same crease: the signed distance flips sign, the line does not. The foot
point is `c n`, and the distance from the origin is `|c|`. So the pair `(crease, height)` is exactly an
affine hyperplane, and the space of them is the total space of the tautological line bundle over
`ℝPⁿ⁻¹`. In the plane that total space is the **open Möbius band**: going once around the circle of
directions returns the height with the opposite sign. The **direction** of the crease is the base; the
height is the fiber.
Orienting the crease would turn the band into a cylinder, so the Möbius twist **is** the "both sides"
identification of `the-fold-apex.md`.

The fold about the affine crease is

```
σ_{H,c}(x) = x − 2(n·x − c)n
```

Decompose `x = h + (c + s)n` with `h ∈ H` (the linear hyperplane through the origin) and
`s = n·x − c` (the signed height above the crease). Then

```
σ_{H,c}(h + (c+s)n) = h + (c−s)n
```

so the fold fixes `h` and flips `s`. The crease is `s = 0`; the fold is exactly the sign flip of the
height. This is the cleanest exact reading:

> **the fold is the height's sign change; the crease is the height's zero.**

**The line, not the arrow.** The identification `(n,c) ~ (−n,−c)` is the exact content of "left and
right do not exist." The crease knows its *line* — up/down — and its signed height; it does not know
which way along the normal is positive. The sign is not a spatial direction, it is the side: the two
layers. In the hexagon the six reflection axes are permuted transitively by `D₆`, so no axis is "up"
until a crease chooses one. The `30°` between adjacent creases is the fold angle `α`, not a lattice
rotation; the smallest rotation is `60°`. After the choice, the reflection acts on the normal
coordinate and fixes the tangent: the direction is the base, the height is the fiber.

"Only height matters" is exact for the fold's action — the reflection changes only the normal sign —
and false for the space: the tangent coordinate is the base, not nothing. The exact statement is that
the fold acts on the height; the direction is the base.

## Two double covers

The space of affine creases is the open Möbius band

```
M = { (n, c) : |n| = 1, c ∈ ℝ } / (n, c) ~ (−n, −c) .
```

Its orientation double cover is the annulus `M̃ = {(n,c)}`, the space of *oriented* creases. The
fold's two layers at a point are not the two sheets of `M̃`; they are the two signs of
`s = n·x − c`. Both are `ℤ/2` double covers, but over different bases: the height's absolute value and
the crease moduli. Same group, different bundle — that is the false friend.

The monodromy is the link. Going once around the direction circle in `M` returns `c` with the opposite
sign, so the holonomy is `−1`. In the twist's circle `k = e^{iθ}` that is `θ = π`: the point reflection.
Two turns return the height, and two half-turns are one full turn — the fold's `2` again. So the sign of
the height is a holonomy, not a left/right in space.

The linear part `I − 2nnᵀ` has determinant `−1`, `+1` eigenspace the crease of dimension `n−1`, and
`−1` eigenspace the normal line.

## The zeta pair: a crease and its height along it

A nontrivial zero is `ρ = σ + it`. The functional equation `ξ(s) = ξ(1−s)` and reality
`ξ(s̄) = conj ξ(s)` compose to the fold `R(s) = 1 − s̄`, whose fixed set is the crease `Re s = 1/2`.
The functional equation alone fixes only the point `s = 1/2`; it is the pair that gives the line. On
the crease `ξ(1/2 + it)` is **real**, so the complex equation `ξ = 0` collapses to one real equation in
the single variable `t`:

```
ξ(1/2 + it) = 0          t ∈ ℝ
```

The zeros are the heights `t_n` at which this real function vanishes:

```
ρ_n = 1/2 + i t_n
```

The first five heights are `14.1347…`, `21.0220…`, `25.0109…`, `30.4249…`, `32.9351…`. RH is the
statement that every zero is of this form; the crease is fixed, and the heights are the free data. This
is the literal reading of the phrase: after the fold `R`, the crease is the location and the
height is the only coordinate left.

Note the direction: `t` runs **along** the crease, not across it. The zeta height is longitudinal; the
affine height is transverse. Same word, different coordinate — the second correction.

## The two heights are not the same

| register | the crease | the height | which way | what the fold does |
|---|---|---|---|---|
| affine | `H_{n,c}` | offset `c` | transverse | flips `s = n·x − c` |
| zeta zero | `Re s = 1/2` | `t = Im s` | longitudinal | fixes the crease; `t` is free |
| complexity | the instance `x` | the witness `w` | transverse | verifier checks; solver chooses |
| theta | `h = 0` (`t = 1`) | `h = ln t` | longitudinal | `h ↦ −h`, fixed `0` |
| matter | the shape/aperture | the linear height | a scale | `h ↦ k h` |

The affine and complexity heights are the two sides of the same projection: `π_H` drops the transverse
coordinate; a section restores it. The zeta and theta heights are parameters along a fold's fixed line.
The word "height" is a false friend unless the register is named.

There is also a third zeta height: the Dirichlet term `n^{-s}` is the Fold's `k` at height `h = ln n`.
That is the height of a **term**, not of a zero; it measures the prime's scale, not the zero's position.
The explicit formula sums over the zero heights `t_n`, while the Euler product sums over the term
heights `ln n`. Keeping them apart is the difference between the two ledgers of the analytic pipeline.

## The Fold's stages: a basis, not a generator

Read through the chain:

| stage | crease data | height data |
|---|---|---|
| point | all creases (none selected) | `0` |
| scale | none | `k` |
| fold | one crease `H` | transverse `0` (through the datum) |
| twist | two creases | none (direction only) |
| closure | the angle between two creases | none |
| horizon | a null crease | scale height `k*` |
| observer | dimension `d` | scale height `k` |

So the crease and the height are the **primitive kinds**, but not a generating pair. One crease and one
height give one affine hyperplane, not the Fold. The twist needs two creases; the closure needs their
angle; the observer needs a dimension; the horizon needs a null normal. The phrase is exact as "the
irreducible data are a crease and a height," not as "one crease and one height generate everything."

This is the same correction as the apex note's "the point does not extend": the primitive is a
coordinate system, not a single object. A point is `(h, s)` — a crease coordinate and a transverse
height. A zero is `(1/2, t)` — a crease coordinate and a longitudinal height. In both cases the pair is
the whole coordinate, and the crease alone is not.

The folded line from afar is the simplest picture of the same pair: the V's shadow is the crease, and
the length remembers the height at second order. See `the-fold-afar.md`.

## Complexity: the witness is the height

The projection/section diagram is the same pair. The instance is the crease coordinate `h`; the witness
is the transverse height `s`; a solver is a section, i.e., a height function

```
S : h ↦ s(h),        π_H(S(h)) = h
```

`P = NP` asks whether every verifier's height function is polynomial-time computable. The wall says the
Fold cannot bound the cost of the height function: its own invariants are polynomial-time, so they can
only collapse the classes. This is the exact sense in which, after the wall, "what's left is the crease
and its height" — the instance and the witness, with the cost of the height function as the open
question. See `the-fold-complexity.md`.

## Theta: the height that folds

The theta fold is a fold in its own height:

```
ϑ(1/t) = √t ϑ(t)          t ↦ 1/t          h = ln t:  h ↦ −h, fixed h = 0
```

The Mellin transform turns this into the functional equation `s ↦ 1−s`; with reality it becomes the
fold `R(s) = 1 − s̄`, whose fixed line is the crease `Re s = 1/2`. So theta is the bridge between the
longitudinal height and the crease: the theta height `h = ln t` is the modular parameter, and the fold
`h ↦ −h` together with the half-density factor `e^{h/2}` produces the `1/2`. The theta height is not
the zeta zero height `t = Im s`: one is logarithmic, the other linear. A third false friend, named. See
`the-fold-theta.md`.

## Checks (NumPy and mpmath at 30 digits)

| check | value |
|---|---|
| affine `σ² = I` | `≤ 9.0e−16` |
| `σ(h) = h` on the crease | `≤ 5.9e−16` |
| `σ(x) = h − s n` | `≤ 2.3e−16` |
| determinant of the linear part | `−1` |
| distance to the crease vs `\|c\|` | equal |
| `(n,c)` vs `(−n,−c)` | same line, signed distance opposite |
| theta `ϑ(1/t) = √t ϑ(t)` | `≤ 1.0e−16` |
| `Im ξ(1/2 + it)` for real `t` | `≤ 5e−32` |
| first five zeros: `Re ρ` | `0.5` |
| `\|ξ(ρ)\|` at the first five zeros | `≤ 1.1e−33` |
| `\|ξ(s) − ξ(1−s)\|` | `≤ 5e−32` |
| `π_H(h + s n) = h` | `≤ 3e−16` |

The first four rows are the affine fold: an involution that fixes the crease and flips the height. The
fifth and sixth are the Möbius identification: the same line from opposite normals, with opposite
signed heights. The theta row is the height fold. The zeta rows are the longitudinal reading: on the
crease the equation is real, and the zeros are the heights where it vanishes.

## What this does and does not say

- It **does** give the exact affine pair: an affine crease is a hyperplane, its height is the offset,
  and the fold is the height's sign flip; the space of affine lines in the plane is the Möbius band.
- It **does** give the exact zeta pair: on the crease `ξ` is real, the zero equation is one real
  equation, and the zeros are the heights `t_n`.
- It **does** use the correct fold: the crease is the fixed set of `R(s) = 1 − s̄`, not of `s ↦ 1−s`
  alone, which fixes only the point `s = 1/2`.
- It **does** distinguish three heights: transverse (affine, complexity), longitudinal (zeta zero,
  theta), and scale (matter, zeta term `ln n`).
- It **does** place the complexity witness as the transverse height over the crease.
- It **does not** identify the affine and zeta heights; they are different coordinates.
- It **does not** generate the Fold from one crease and one height; the twist, closure and observer need
  more.
- It **does not** prove RH; it says the zeros, if on the crease, are the heights of a real function.
- It **does not** resolve `P vs NP`; it says the witness is a height function and the wall is its cost.
- It **does not** make the crease a line in `n` dimensions; it is codim 1, a line only in the plane and
  in `ℂ`.

## The one sentence

**What is left is a crease and a height, but the height must be named: transverse in the affine fold
(the offset the fold flips, a Möbius band of lines in the plane), longitudinal in the zeta zero (the
imaginary part the crease leaves free), and transverse again in the verifier (the witness a solver must
supply) — the crease is one codimension, the heights are three registers, and together they are a
basis, not a generator.**

## Files

`the-fold-crease-height.md` (this note). The affine crease, the Möbius identification and the two sides
are in `the-fold-apex.md`; the projection `π_H` and the side-blindness are in
`the-fold-occlusion.md`; the critical line and the zeros are in `the-fold-zeta.md`; the theta fold and
the `1/2` are in `the-fold-theta.md`; the projection/section wall is in `the-fold-complexity.md`; the
height law and the scale are in `the-fold-matter.md` and `the-fold-cone.md`; the lookup is
`the-fold-key.md`.
