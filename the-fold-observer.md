# The observer: dimension and window

## The claim

The Fold's order ends `horizon → observer → point`. The observer has been read as a dimension: a 0D
observer sees a scalar, a 1D observer a derivative, a 2D observer a flux, a 3D observer a density. The
folded-line note adds a second fact: what an observer sees also depends on its **resolution**. The claim
of this note is that these are two independent parameters:

```
observer = (d, w)
```

`d` is the dimension — the degree of the form it can measure — and `w` is the window — the smallest
feature it can resolve. The paper's table is the `w → 0` slice; "from afar" is the same `d` with `w`
larger than the fold's height. Neither parameter is a transformation of the object; both are properties
of the probe.

| parameter | selects | exact object | idealization |
|---|---|---|---|
| `d` | the form degree | `d`-form; exponent `p − d` | `d` fixed |
| `w` | the scale | Gaussian window; attenuation `e^{−π²w²/(2ℓ²)}` | `w → 0` |

## Dimension: the form degree

A `d`-dimensional observer measures a `d`-form. A homogeneous quantity of degree `p` scales as
`O ∝ h^p`; measured per `d`-volume, it becomes

```
O_d ∝ h^{p−d}
```

because the unit `d`-volume scales as `k^d`. The determinant `k^n` is the top case, `d = n`.

| observer | measurement | exponent |
|---|---|---|
| 0D | scalar — curvature, potential, temperature | `p` |
| 1D | derivative, direction, rate | `p − 1` |
| 2D | flux (needs an oriented area) | `p − 2` |
| 3D | density, integral | `p − 3` |

The density row is the check: mass has `p = 1`, so a 3D density has exponent `1 − 3 = −2`, the `1/h²`
of the height table. The observer adds no new law; it selects how many powers of the height are divided
out.

The form reading is exact on the signature side. The Hodge star on an `n`-dimensional space with `s`
negative directions obeys

```
⋆² = (−1)^{d(n−d)+s}
```

In four Lorentzian dimensions `s = 1`, so a 1-form and a 3-form square to `+1`, while a 0-form, a 2-form
and a 4-form square to `−1`. The observer's `d` selects the form; the signature selects the star's
square. This is the footprint of the signature on measurement.

A point is `d = 0`: it measures a value, not a flow. It has no tangent space, so it cannot host a vector;
time is undefined there rather than zero. The surface is `d = n−1`: `Ω = 2π`, a half-space, edge-on. That
is the horizon case.

## Window: the resolution

The measurement is a window, not a point evaluation:

```
(O * G_w)(x) = ∫ O(y) G_w(x − y) dy,   G_w(x) = (2πw²)^{−n/2} e^{−|x|²/(2w²)}
```

The Gaussian is the kernel selected by the standard scale-space axioms (linearity, isotropy, causality),
and its semigroup is exact:

```
G_{w1} * G_{w2} = G_{√(w1² + w2²)}
```

The window composes by quadrature. Its frequency width is `1/w`, and it is the minimizer of the
uncertainty product: the sharpest window at a given scale.

A periodic feature of half-period `ℓ` has its first Fourier mode multiplied by `e^{−π²w²/(2ℓ²)}`. For
the triangle wave of amplitude `a`, the residual is

```
(8a/π²) e^{−π²w²/(2ℓ²)}
```

At `w = ℓ = 1`: `e^{−π²/2} = 7.1919e−3`, and `8/π² = 0.81057`, so the residual is `5.8295e−3`. The
fold is resolved when `w < ℓ`; at `w = ℓ` the first mode is already at `0.72%` of its amplitude.

The scale `k` changes the height and the shadow together; if the observer scales with the object, the
window `w` scales too and `h/w` is invariant. If the observer's window is fixed, `h/w` changes with `k`,
and that is the far-view limit. "From afar" is `w` fixed and `h` falling, i.e. the ratio `h/D`, not
`k → 0`. This is the exact reconciliation of the paper's table with the folded-line note.

## The two parameters are independent

`d` and `w` act on different axes, and neither compensates for the other:

| blind to | because | fix |
|---|---|---|
| the form | `d` is too low: a 0D observer has no oriented area to flux through | raise `d` |
| the feature | `w` is too wide: the window averages the fold away | lower `w` |

A 2D observer with `w > h` sees a flux but not the fold; a 0D observer with `w → 0` sees the fold's
value but not its flux. The paper's table is the first column; the folded-line note is the second. The
full observer is the pair, not either slice.

## The three viewpoints

The sphere is the exact model. An observer outside at distance `D` sees the cap subtended by the sphere:

```
Ω/4π = (1 − cos α)/2,   sin α = r/D
```

| viewpoint | `Ω/4π` | exact statement |
|---|---|---|
| outside, `D = 2.281 r` | `5.061%` | `(1−cos α)/2`; the paper rounds to `5.060%` |
| outside, `D = 2.281 r/k` | `1.216%` at `k=0.5`; `0.301%` at `k=0.25` | same formula |
| centre | `100%` | conformal, every `k` |
| surface | `50%` | half-space, `d = n−1` |

At `D = 2r` the fraction is `6.699%`; at `D = 10r`, `0.2506%`. The small-angle limit is `r²/(4D²)`,
which is the paper's `k²` fall when `D ∝ 1/k`. The exact values at `k = 0.5, 0.25` are not exactly `k²`
times the first row; the difference is the curvature of the cap. A cone of aperture `θ` is the same
computation with a rim: it covers `Ω/4π = sin²(θ/2)`, so the sphere is `θ = π` and a `90°` cone is half
the sky.

The centre sees `Ω = 4π` for every `k`, because a homothety is conformal. The surface sees `Ω = 2π`: the
`d = n−1` observer, edge-on, and the horizon is its null limit.

The window adds the resolution: at distance `D`, the angular resolution is `w/D`, and the fold's angular
height is `h/D`. The fold is resolved when `h > w`; the distance cancels. The observer can be far away
and still resolve a tall fold; it can be close and still miss a shallow one. "From afar" is the second
case.

## The return

The observer measures; it does not vanish. A `d`-form has no Fold zero of its own, and the observer stage
produces none. The two parameters are probes, not transformations: `d` selects the form, `w` the scale.
The return is the object's collapse, not the probe's.

At `k = 0` the paper's three views coincide: the point, the shell, and the observer are the same place.
That is the object's limit. The probe's own limit is `(d, w) → (0, 0)`: a point-like observer with no
window, which sees a value at a point. The two limits meet at the point but are not the same operation.
The observer does not create the zero; it is the zero's last witness.

## Adjacent research: scale-space

The window is the scale-space parameter. Witkin introduced scale-space filtering; Koenderink derived the
Gaussian from causality and isotropy; Lindeberg's *Scale-Space Theory in Computer Vision* is the standard
reference. The exact content borrowed here is the semigroup `G_{w1} * G_{w2} = G_{√(w1²+w2²)}` and the
Fourier attenuation; the uniqueness of the Gaussian under the axioms is cited, not reproved.

The measurement is the pairing of a `d`-form with a smoothed `d`-current; the window smooths the
current. The Hodge star's square is the signature's footprint on that form. The horizon is the `d = n−1` case, edge-on. The
resolution criteria (Rayleigh, Sparrow) and the Airy `2/3` law are in `the-fold-afar.md`; this note adds
the two-parameter observer, not a new resolution theorem.

| topic | reference | link |
|---|---|---|
| scale-space | Witkin, *Scale-space filtering*, IJCAI 1983, 1019–1022 | — |
| scale-space | Koenderink, *The structure of images*, Biol. Cybern. 50 (1984), 363–370 | [DOI](https://doi.org/10.1007/BF00336961) |
| scale-space | Lindeberg, *Scale-Space Theory in Computer Vision*, Kluwer 1994 | — |
| Gaussian window | *Gaussian blur* | [Wikipedia](https://en.wikipedia.org/wiki/Gaussian_blur) |
| Hodge star | *Hodge star operator* | [Wikipedia](https://en.wikipedia.org/wiki/Hodge_star_operator) |

## Checks

| check | value |
|---|---|
| exterior solid angle, `D = 2.281 r` | `5.061%` (paper `5.060%`) |
| exterior, `D = 2r` / `10r` | `6.699%` / `0.2506%` |
| small-angle `r²/(4D²)`, `D = 10r` | `0.2500%` vs `0.2506%` |
| cone aperture, `θ = 90°` | `Ω/4π = 1/2` |
| centre / surface | `1` / `1/2` |
| exterior exact, `k = 0.5` / `0.25` | `1.216%` / `0.301%` |
| Gaussian semigroup, `(w1,w2) = (1,2)` | `2.23606798` vs `√5` |
| Fourier attenuation, `w = ℓ = 1` | `7.1919e−3` |
| triangle residual, `w = 1` | `5.8295e−3` |
| exponent shift, `p = 1, d = 3` | `h^{−2}` |
| star parity, `d = 0,1,2,3,4` | `−,+,−,+,−` |

The solid-angle values are the paper's geometry, rechecked; the semigroup and the attenuation are the new
checks. The numbers are floating-point confirmations of the formulas, not measurements.

## What this does and does not say

- It **does** make the observer the pair `(d, w)`: dimension for the form, window for the scale.
- It **does** reconcile the paper's observer table (the `w → 0` slice) with the folded-line note (the
  `d`-fixed, `w > 0` slice).
- It **does** identify the window with the Gaussian semigroup and the Fourier attenuation, and place the
  horizon at `d = n−1`, edge-on.
- It **does** distinguish two kinds of blindness: wrong dimension (cannot measure the form) and wrong
  window (cannot resolve the feature). Neither parameter fixes the other.
- It **does** separate the object's return `k = 0` from the probe's limit `(d, w) → (0, 0)`.
- It **does not** claim the observer creates the object or the zero; the observer is a probe.
- It **does not** derive the scale-space axioms from the Fold; the Gaussian is cited as the selected
  kernel, not deduced.
- It **does not** claim the window is a physical instrument; it is a model of resolution.
- It **does not** reprove the Rayleigh, Sparrow, or Airy results; those are in `the-fold-afar.md`.
- It **does not** make the `d`-form reading a theorem; it is the Fold's reading of the observer's
  dimension, consistent with the paper's table and the star.

## The one sentence

**An observer is a dimension and a window: `d` selects which form it can measure, `w` selects the
smallest feature it can resolve; the paper's table is the `w → 0` slice, and "from afar" is the same
observer with `w` larger than the fold's height.**

## Files

`the-fold-observer.md` (this note). The dimension table and the solid angle are in `the-fold.md` §7; the
exponent shift is in `the-fold-matter.md`; the star is in `the-fold-signature.md`; the resolution and the
fold are in `the-fold-afar.md`; the projection and side-blindness are in `the-fold-occlusion.md`; the
horizon is in `the-fold-horizon.md`; the order is in `the-fold-creation.md`; "the observer produces no
zero" is in `the-fold-pipeline.md`; the lookup is `the-fold-key.md`.
