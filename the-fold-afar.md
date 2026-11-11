# The folded line from afar

## The phrase

A line is folded. From a distance the fold is too small to resolve, and the folded line looks like a
**singular line** — one line, not two. The image is exact, but two words need names: "from afar" and
"singular."

"From afar" can mean three operations. The first and third are exact; the second is their limit.

| model | the folded line | "from afar" | what is left |
|---|---|---|---|
| orthographic | a V with vertex on the crease | the projection `π_H` along the normal | the crease |
| coarse-grained | a pleated line | a blur wider than the pleat | the mean line |
| quotient | the image of a line under the sheet fold | the fold's orbit space | the crease, the boundary |

"Singular" also has three exact readings, and they meet at the same crease: **one line** (the quotient),
**non-smooth** (the derivative jump), and **rank-deficient** (the projection). The note states each, then
the correction: **from afar is a projection, not a scale.**

## One fold: the V and its crease

The Fold's global fold is the involution

```
σ_H(x) = x − 2(n·x)n
```

It fixes the crease `H` and flips the normal. It maps a line to a line: a reflection has no corner. The
physical fold of a sheet is not `σ_H` on both sides; in the idealization it is the quotient map that
fixes one side and applies `σ_H` to the other. With `H = {y = 0}`:

```
F(x, y) = (x, |y|)
```

`F` is continuous, fixes `y ≥ 0`, reflects `y ≤ 0`, and its image is the half-plane `y ≥ 0`. The crease
is the boundary `y = 0`.

A line `ℓ: y = m x + b` with `m ≠ 0` crosses the crease at `x₀ = −b/m`. Its image is the V

```
F(ℓ):  y = |m x + b|
```

with vertex `(x₀, 0)` on the crease. The two rays have slopes `±m`, so the opening angle is

```
θ = 2 arctan |m|
```

The shadow is the projection `π_H(x, y) = (x, 0)`: the V maps to the crease line, both rays coincide,
and the image is one line. Over the window `[x₀ − L, x₀ + L]`:

| quantity | value |
|---|---|
| height at the window edge | `\|m\| L` |
| shadow length | `2L` |
| path length | `2L √(1 + m²)` |
| chord | `2L` |
| path / shadow | `√(1 + m²) = 1 + m²/2 + O(m⁴)` |
| length excess | `L m² + O(m⁴)` |

The fold's height is `|m| L`; the length excess is `L m²` — quadratic in the height. The shadow sees the
first power (the height is dropped); the length sees the second power (the height is squared). For
`m = 0.1` and `L = 1`, the ratio excess is `0.00498756` against `m²/2 = 0.005`, a relative error of
`−2.5e−3`; the length excess is `0.00997512` against `L m² = 0.01`.

The global fold `σ_H` maps the same line to `y = −m x − b`, another line, with no corner. The sheet fold
`F` maps it to the V. The difference is the quotient: `F` is the quotient map by `σ_H`, and the crease is
its boundary. This is the first correction: **the folded line is the image of the sheet fold (the
quotient), not of the global reflection.**

## Many folds: the pleats and the mean

A line folded repeatedly becomes a pleated line. In cross-section, a triangle wave of amplitude `a` and
half-period `ℓ`:

```
y(x) = a · tri(x/ℓ)
```

The creases are the peak and valley lines; the midplane `y = 0` is the mean. The projection onto the
midplane is the straight line. The path length per half-period is `√(ℓ² + 4a²)`, so

```
length / shadow = √(1 + (2a/ℓ)²) = 1 + 2a²/ℓ² + O(a⁴)
```

The excess is quadratic in the amplitude. For `a/ℓ = 0.1`, the ratio is `1.0198039`, the excess
`0.0198039`, and `2a²/ℓ² = 0.02` (relative error `−9.8e−3`). The mean is `0`; the variance is `a²/3`
(measured `0.333337 a²`). The first moment is the crease; the second moment is the fold.

The coarse-graining model: convolve the pleated line with a Gaussian of width `w`. The first Fourier mode
of the triangle wave has amplitude `8a/π²` and is multiplied by `exp(−π² w²/(2ℓ²))`, so the residual
amplitude is

```
8a/π² · exp(−π² w²/(2ℓ²))
```

For `a = 1`, `ℓ = 1`, the measured residual at `w = 1` is `5.8295e−3`, and the formula gives
`8/π² · e^{−π²/2} = 5.8295e−3`. The log residual against `w²` has slope `−π²/2 = −4.9348` (measured
`−4.9348` from `w = 0.5` to `1`; `−5.06` over `[0.2, 2]`). The length density (blurred length over
shadow length) tends to `1`: `2.112` at `w = 0.05`, `1.126` at `w = 0.5`, `1.00008` at `w = 1`,
`1.000000` at `w = 2`. The pleats disappear from the image exponentially in `w²`; the length excess
disappears only when the blur resolves the pleats. The shadow is the mean; the fold is the variance.

## The singular line

"Singular" has three exact readings, and they meet at the crease:

| sense | object | exact statement |
|---|---|---|
| one line | the quotient | the sheet fold identifies the two sides; the orbit space is a half-plane; the crease is its boundary |
| non-smooth | the sheet fold `F` | `F` is continuous but not differentiable across `H`; the normal derivative jumps from `+1` to `−1` (jump `2`); the V has a corner on `H` |
| rank-deficient | the projection `π_H` | rank `n−1`, kernel the normal line; the image of the V is the crease |

The line itself is smooth; the singularity is created by the fold. The crease is the fixed set of `σ_H`,
the boundary of the quotient, and the image of the V. The rank deficiency is global, but its image is the
same crease.

The smooth model behind `F` is the fold catastrophe

```
(x, y) ↦ (x, y²)
```

Its Jacobian is `diag(1, 2y)`, so its rank drops from `2` to `1` exactly on `y = 0`; the critical line is
the crease, and its image is the boundary of the half-plane. `F` is the piecewise square root of this map.
In singularity theory the critical set is the singular line; in the Fold it is the crease. The three
readings meet at one object: the crease.

The derivative jump: for `F(x, y) = (x, |y|)`, the normal derivative is `+1` above and `−1` below, so the
jump is `2`. Numerically, `(|h| − 0)/h = +1` for `h > 0` and `−1` for `h < 0`, at
`h = 10⁻¹, 10⁻³, 10⁻⁶, 10⁻⁹`. The folded line's singular point is the vertex; the crease it lies on is
the singular line. In the line's own dimension the crease is a point (codim 1); in the ambient plane the
crease is a line; in `n` dimensions it is a hyperplane. The phrase names the ambient codimension-one
crease, not the point.

## From afar is a projection, not a scale

The tempting reading is "from afar = scaled to zero": `k → 0`, the fold shrinks, and the line becomes
straight. That is false. The scale `k` multiplies both the height and the shadow:

```
height → k h,   shadow → k L,   height/shadow = h/L,   opening angle invariant
```

For `m = 0.2`, the ratio `height/shadow` is `0.1`, the opening angle is `22.619865°`, and `path/chord` is
`1.019804` for `k = 0.01, 0.1, 1, 10, 1000`. The shape is scale-invariant; the fold does not disappear
under `k`. What disappears is the **transverse height in the observer's projection**; "from afar" is the
observer's resolution coarser than the height, i.e. the ratio `h/D`, not `k`. If the observer and the
object scale together, the fold is invariant; if the observer's resolution is fixed and the object is
far, the height falls below the resolution. The exact operation is the projection `π_H` (or the
coarse-graining), not the scale.

This is the same split as the matter note: the height fixes the magnitudes, the shape is invariant. And
the same split as the occlusion note: the projection drops the side, the metric squares it. The folded
line from afar is the shadow; the length is the quadratic measurement that remembers the fold. See
`the-fold-matter.md`, `the-fold-occlusion.md`, and `the-fold-crease-height.md`.

## Rhyme: the unresolved doublet

A spectral line split by a fold into two components is a doublet. A spectrometer whose resolution is
coarser than the splitting sees one line at the mean. The splitting is the transverse height; the mean is
the crease; the unresolved singlet is the shadow. The same first/second moment structure: the mean is the
first moment, the splitting is the second. This is a rhyme, not the Fold's object: a spectral line is a
frequency, not a geometric line, and the Fold models the splitting, not the spectrum.

## Checks

| check | value |
|---|---|
| V opening angle, `m = 0.1` | `11.421186°` |
| V path/chord, `m = 0.1` | `1.00498756` |
| V ratio excess vs `m²/2`, `m = 0.1` | `0.00498756` vs `0.005`, rel `−2.5e−3` |
| V length excess vs `L m²`, `m = 0.1, L = 1` | `0.00997512` vs `0.01` |
| V height/shadow, `m = 0.1` | `0.05` |
| projection residual, V → crease | `0` |
| global reflection image residual | `0` (a line, no corner) |
| sheet-fold corner residual | `≤ 3.3e−13` |
| triangle-wave length ratio, `a = 0.1` | `1.0198039` vs `1 + 2a² = 1.02` |
| triangle-wave variance | `0.333337 a²` vs `a²/3` |
| blur residual, `w = 1` | `5.8295e−3` |
| first-mode formula | `8/π² e^{−π²/2} = 5.8295e−3` |
| blur log-slope, `w = 0.5 → 1` | `−4.9348` vs `−π²/2` |
| length density, `w = 0.05 / 0.5 / 1 / 2` | `2.112 / 1.126 / 1.00008 / 1.000000` |
| derivative jump across the crease | `2` |
| fold-catastrophe rank, `y = 0` / `y ≠ 0` | `1` / `2` |
| scale invariance, `k = 0.01 … 1000` | angle `22.619865°`, path/chord `1.019804` |
| first / second moment, `a = 1` | `0` / `0.333335` vs `1/3` |

The first block is the V; the second is the pleats; the third is the singular set and the scale check.
The numbers are floating-point confirmations of the formulas, not new measurements.

## What this does and does not say

- It **does** give the exact one-fold picture: the sheet fold is the quotient, the V's vertex is on the
  crease, the opening angle is `2 arctan |m|`, and the shadow is the crease.
- It **does** give the exact many-fold picture: the pleats' mean is the crease, the variance is the fold,
  and the length excess is quadratic in the amplitude.
- It **does** distinguish three senses of "singular" — one line (quotient), non-smooth (derivative jump),
  rank-deficient (projection) — and locate all three at the crease.
- It **does** identify the smooth model: the fold catastrophe `(x, y) ↦ (x, y²)`, whose critical line is
  the crease.
- It **does** correct "from afar = scaled to zero": the scale is shape-invariant; the projection and the
  coarse-graining drop the transverse height.
- It **does** place the fold's height in the second moment: the shadow sees the first, the length sees the
  second.
- It **does not** claim that a real physical fold, material, or perceived line behaves exactly this way;
  it is a model of the Fold's geometry.
- It **does not** prove a theorem about singularities in algebraic geometry; "singular" here is the
  non-smooth and critical locus of the sheet fold.
- It **does not** identify the crease with a zeta zero, a horizon, or a facet; those are different
  registers.
- It **does not** make the global reflection `σ_H` a fold of a sheet; `σ_H` maps a line to a line, the
  quotient `F` makes the V.

## The one sentence

**A folded line looks like a singular line from afar because the fold's transverse height is dropped by
the projection, leaving the crease — the fixed set of the fold, the boundary of the quotient, and the
singular set of the sheet fold — while the fold survives only in the length, at second order in the
height.**

## Files

`the-fold-afar.md` (this note). The projection and the side-blindness are in `the-fold-occlusion.md`; the
transverse height and the crease are in `the-fold-crease-height.md`; the two sides as one fold and the
pencil are in `the-fold-apex.md`; the equalizer/coequalizer reading is in `the-fold-categorical.md`; the
length and angle invariants are in `the-fold-invariants.md`; the height law and the observer are in
`the-fold-matter.md`; the lookup is `the-fold-key.md`.
