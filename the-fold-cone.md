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

Files: `cone-range-3d.html` (3D sector, `θ` and `k` sliders, orbit by drag, readouts for `R`, `a`,
cap height, `Ω`, `Ω/4π`, `V`, `A`, `V/A` and whether the fold fixes the body, `?t=&k=` deep link),
`the-fold.tex` / `.md` / rebuilt `.pdf`.
