# The range cone

## The object

Your description fixes the object exactly: the apex is the object's centre, the outer region is its
range. Formally, for a datum `P₀`, an axis `n`, an aperture `θ` and a range `R`:

```
C = { P₀ + t·u  :  angle(u, n) ≤ θ,  0 ≤ t ≤ R }
```

This is a **spherical sector**, not a Euclidean cone, and the difference is not cosmetic. A Euclidean
cone with the same apex and rim has a flat outer face; only its rim is at range `R`. The sector's
outer face is a piece of the sphere of radius `R`, so *every* point of the outer region is at range
`R` — which is what "the outer region is its range" says. The rim is the circle where the two meet:
`a = R sin θ` from the axis, at axial height `R cos θ`.

Two numbers describe it completely: `θ` is the **shape**, `R` is the **size**.

## Scaling moves one of them

`g_k` sends `R ↦ kR` and leaves `θ` alone. So the aperture is the invariant and the range is the
coordinate — the cleanest instance of the invariant thread's "shape survives, size does not".

Measured at `θ = 60°`:

| `k` | `R` | `Ω` | `V` | `A` | `V/A` | `(V/A)/k` |
|---|---|---|---|---|---|---|
| 1 | 1.000 | 3.1416 | 1.0472 | 5.8623 | 0.1786 | 0.17863 |
| 0.5 | 0.500 | 3.1416 | 0.1309 | 1.4656 | 0.0893 | 0.17863 |
| 2 | 2.000 | 3.1416 | 8.3776 | 23.4492 | 0.3573 | 0.17863 |

`Ω` constant, `V ∝ k³`, `A ∝ k²`, `V/A ∝ k` — the same ladder as the sphere, with one difference
worth stating: here `V/A` is not `R/3` but `RΩ/(3(Ω + π sin θ))`, and it depends on the aperture.
At `θ = 180°` it returns to `R/3`.

## The formulas, and the checks

```
Ω = 2π(1 − cos θ) = 4π sin²(θ/2)
V = (R³/3)·Ω                     (integrate r² dr dΩ over the sector)
A = R²(Ω + π sin θ)              (spherical cap R²Ω plus lateral πR² sin θ)
```

Checked against Monte Carlo at 2 × 10⁶ samples:

| `θ` | `Ω` exact | `Ω` MC | rel. err |
|---|---|---|---|
| 30° | 0.8418 | 0.8388 | 3.5e−3 |
| 60° | 3.1416 | 3.1395 | 6.6e−4 |
| 90° | 6.2832 | 6.2821 | 1.7e−4 |
| 180° | 12.5664 | 12.5664 | 0.0 |

Volume agrees to the same order (`θ = 90°`: `2.09361` measured, `2.09440` exact). Area has two exact
anchors: `θ = 90°` gives `3πR²` (half a ball: `2πR²` of dome plus `πR²` of disc), and `θ = 180°`
gives `4πR²`. Both match.

## The fold

`k = −1` keeps `R` and `θ` and reverses the axis, so the sector is carried to its **antipode**: same
aperture, opposite sky. It fixes the body only when there is no direction left to flip, i.e. at
`θ = 180°`, where the sector is a ball.

The overlap with its own antipode is exact:

```
V(C ∩ (−C)) / V(ball) = max(0, −cos θ)
```

| `θ` | measured | `max(0, −cos θ)` |
|---|---|---|
| 45° | 0.00000 | 0.00000 |
| 90° | 0.00000 | 0.00000 |
| 91° | 0.01727 | 0.01745 |
| 120° | 0.50113 | 0.50000 |
| 150° | 0.86642 | 0.86603 |
| 180° | 1.00000 | 1.00000 |

So proper cones are disjoint from their antipodes up to `90°`, overlap halfway at `120°`, and become
the whole ball at `180°`. The fold is a symmetry of the sphere and of nothing else in this family —
which is the cone's version of the previous note's "the fold moves direction".

## Where it belongs in the paper

Section 2 has the **tangent** cone: apex on or outside the surface, the cone that touches the body.
This is a different cone — the **range** cone: apex at the centre, rim on the surface. The paper's
sphere/cone distinction is about where the apex sits; this one is about what the apex is for.

Section 7 gains the measurement that matters here: from its own centre a body of aperture `θ` covers
`Ω/4π = sin²(θ/2)` of the sky, and that fraction does not move with `k`. For the sphere it is `1` —
the "sky fixed, distance shrinks" row of the existing table. For a proper cone it is less than `1`,
and the fold swaps which half of the sky it is.

---

## What follows

Five things fall out of the sector, and all five are checkable.

### 1. The observer table is one formula

The three rows of the paper's observer table — outside, at the centre, on the surface — are one
formula at three apertures:

| observer | aperture `θ` | `Ω/4π = sin²(θ/2)` |
|---|---|---|
| at the centre | `180°` | `1` |
| on the surface | `90°` | `½` |
| outside, distance `d`, radius `r` | `arcsin(r/d)` | `(1 − cos θ)/2` |

The outside row is the **tangent cone** of section 2, seen from the observer rather than at the
body. That is not an analogy: for a sphere the silhouette *is* the circle of tangency, so the solid
angle subtended equals the tangent cone's solid angle exactly.

It also pins a number the paper had only measured. Inverting `5.060%`:

```
cos θ = 1 − 2(0.0506) = 0.89880     θ = 25.9992°
r/d   = sin θ        = 0.438359     d = 2.2812 r
```

and that single ratio reproduces the rest of the table with no further input:

| `k` | `r/d` | `θ` | predicted | paper |
|---|---|---|---|---|
| 1 | 0.438359 | 25.9992° | 5.060% | 5.060% |
| 0.5 | 0.219180 | 12.6615° | 1.216% | 1.216% |
| 0.25 | 0.109590 | 6.2899° | 0.301% | 0.301% |

The `k²` law is the small-angle limit `sin²(θ/2) ≈ θ²/4 ≈ (r/2d)²`.

### 2. The fold group loses a dimension

A fold is a reflection in a plane through the datum. Which ones fix a range cone?

- A plane **containing the axis** fixes it, exactly: the reflection preserves both the angle to the
  axis and the range. Measured residual `0.0` over 2 × 10⁴ points.
- A plane **not containing the axis** does not: measured residual `2.07 rad` (the image leaves the
  sector).
- At `θ = 180°` every plane fixes it, because every plane fixes a ball. Residual `0.0` again.

So the cone's fold group is a **circle's worth of creases** (the pencils of planes through the axis),
while the ball's is every plane. The aperture does not shrink that circle — it is the same `ℝP¹` for
every `θ < 180°` — and then at `180°` it jumps to the whole Grassmannian. The point reflection
`−I` is not in the circle: it fixes the sector only at `180°`, which is the overlap law
`max(0, −cos θ)` from the previous section, read at `θ = 180°` alone.

So "how much fold survives" is governed by the *axis*, not the aperture. That is the opposite of
the twist, where the aperture is the only thing that matters.

### 3. The twist is the identity, not merely invisible

The twist `J` is a quarter turn about an axis through the datum. Put the cone's axis there and `J`
maps the sector to itself — as a set, exactly, for every `θ`. So the quotient `U(1)/Sym(B)` of
section 3 is trivial for a cone, and the observable twist is `0` at every angle:

| body | 30° | 45° | 90° | why |
|---|---|---|---|---|
| sphere | 0.0% | 0.0% | 0.0% | continuous symmetry |
| range cone | 0.0% | 0.0% | 0.0% | continuous symmetry |
| cube | 1.4% | **12.3%** | 0.0% | finite symmetry `C₄` |

The zeros are not small — they are exact, and they come from the same cause as the sphere's. The
twist needs a **finite** symmetry group to be observable at all; a solid of revolution has none. So
the cone changes nothing in section 3, and that is the result: the ladder is sphere = cone < cube,
and the useful body is the one with the cube's discrete symmetry.

### 4. The collapse kills the range and keeps the aperture

`C_k = k·C` for `k > 0`, so the set of *directions* of `C_k` is the same set for every `k ≠ 0`.
Measured over 2 × 10⁵ sampled points:

| `k` | max range | max angle from the axis |
|---|---|---|
| 1 | 1.00 | 59.986° |
| 10⁻³ | 9.99 × 10⁻⁴ | 59.986° |
| 10⁻⁶ | 9.99 × 10⁻⁷ | 59.986° |

Six orders of magnitude of size, and the aperture does not move (the `59.986°` against `60°` is the
sampling floor, not drift). So at `k = 0` the range is gone and the aperture is not — but it is not
a subset of the point either: the point has no directions. It survives as a **limit of directions**,
which is why section 6 can say "no tangent space" and still be precise. The point has no tangent
space; the *family* has a tangent cone, and that cone is the aperture. Shape outlives size, all the
way down to `k = 0`.

### 5. The cap alone is the whole data

`A_cap = R²Ω` is one equation in two unknowns, and `Ω = 2π(1 − cos θ)` is another, so the boundary
determines the body:

```
θ = 2 arcsin √(Ω/4π)          R = √(A_cap / Ω)
```

Exact to rounding in every case tried (`R = 1, θ = 60°` → `R = 1.000000000000000`;
`R = 0.4, θ = 150°` → `0.400000000000000`). The lateral surface `πR² sin θ` adds nothing: it is
fixed once `(R, θ)` are. This is the holographic statement with no analogy left in it — the cap is
not a stand-in for the bulk, it is a complete set of coordinates for it.

### What this changes in the paper

Three sentences, not three sections:

- §3's symmetry table gains a `cone` row: `O(2)`, no observable twist at any aperture. The silhouette
  paragraph notes that the cone's zeros are exact for a stronger reason than the sphere's.
- §7 gains one sentence: read backwards, `Ω/4π = sin²(θ/2)` generates the observer table at
  `θ = 180°, 90°, arcsin(r/d)`, so `5.060%` is exactly `d = 2.281 r`.
- Everything else — the fold group, the collapse, the cap as coordinates — stays in this note.

Floats were tightened (`\intextsep` 7pt, `\textfloatsep` 10pt) to hold the paper at six pages while
the two additions went in.

Files: `cone-range-3d.html` (3D sector, `θ` and `k` sliders, orbit by drag, readouts for `R`, `a`,
cap height, `Ω`, `Ω/4π`, `V`, `A`, `V/A` and whether the fold fixes the body, `?t=&k=` deep link),
`the-fold.tex` / `.md` / rebuilt `.pdf`.
