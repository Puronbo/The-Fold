# Matter is the zero at a scale

## The claim

The claim has two halves, and they do not have the same status.

1. **"Matter is just a zero at different scales."** This is exact in the Fold's terms. The only zero
   is the map at `k = 0`, whose image is the datum `P₀`; a body is that zero with a scale `k`.
   Different masses are the same zero sampled at different `k`.
2. **"All matter is determined by the height aspect."** This is exact for every *dimensional
   magnitude*, not for the *dimensionless structure*. Height `h ∝ k` fixes size; area and volume are
   `h²` and `h³`; mass is `h` in the homothetic family. Shape `θ` and turn `arg k` are not heights.

The sharpened statement is:

> Matter is the zero at a scale. Height fixes every dimensional quantity by a power of `h`; the
> aperture fixes the shape, and the phase fixes the turn.

## The zero

The zero is the one map with no scale:

```
g₀(P) = P₀          rank 0          det 0          image = {P₀}
```

Read as a field, `h(P) = |P − P₀|` has a single zero at `P₀`. Matter is that zero; a body is a region
bounded by a level set `h = R` of the same field. The radial value is the scale; the angular cut is
the shape `θ`. Different scales are different level sets of one zero.

Mathematically the zero is a point defect: `h` vanishes there while the direction field around it
does not. The direction field is `Sⁿ⁻¹`; in the plane the winding is `1`. The Fold does not use the
winding number, but it is the natural topological label of the zero.

It is not empty. What survives is what was never a measure: the direction `Sⁿ⁻¹`, the dimension `n`,
and the tangent cone. The cone note gives the clean picture: at the vertex of a range cone with
`θ = 60°`, the solid angle stays `Ω/4π = 0.25` at every zoom (`k = 1`, `10⁻³`, `10⁻⁶`), while every
dimensional measure vanishes. The zero annihilates every dimensional quantity and preserves all of
the dimensionless data. Read as a signature, that is the null form `(0,0,n)`: `n` directions, none
signed. The first scale signs all `n`; the first fold splits off one. See `the-fold-signature.md`.

Under the full similarity group the orbit space of `ℝⁿ ∖ {P₀}` is a point and the invariant ring is
constants. The zero is the unique fixed point; every other point lies in one orbit. So the zero is
the common origin of every orbit. Its location is a choice of origin; the scale is a choice of
representative. Neither is an invariant of the group; matter is the symmetry-breaking choice.

## The height law

For real `k > 0`,

```
g_k(P) = P₀ + k(P − P₀)          det g_k = kⁿ
h = |P − P₀| ∝ k
```

Every dimensional quantity is a power of the height times a dimensionless factor:

```
O(h, θ, φ) = h^{p_O} · f_O(θ, φ)
```

The geometric exponents are the degrees of the determinant; the thermodynamic ones follow from the
horizon law. Each is fixed by the one before it:

| quantity | symbol | exponent `p` | in the homothetic family |
|---|---|---|---|
| height, radius | `h`, `R` | `1` | `∝ k` |
| area | `A` | `2` | `∝ k²` |
| volume | `V` | `3` | `∝ k³` |
| mass | `M` | `1` | `∝ k` |
| entropy | `S` | `2` | `∝ k²` |
| temperature | `T` | `−1` | `∝ 1/k` |
| density | `ρ = M/V` | `−2` | `∝ 1/k²` |
| horizon ratio | `k*` | `0` | constant |

This is the **scale** height: it is the linear size `h ∝ k`, not the transverse offset of a crease or
the longitudinal parameter of a zero. The three registers are named in `the-fold-crease-height.md`.

The exponents obey a small arithmetic, which is why the table is consistent:

```
p_A = 2 p_h = 2          p_V = 3 p_h = 3
p_M = p_h = 1            p_S = p_A = 2
p_T = −p_h = −1          p_ρ = p_M − p_V = −2
p_k* = p_M − p_h = 0
```

The law is concrete for a range cone of range `R = h` and aperture `θ`:

```
V = (h³/3) Ω(θ)          A = h²(Ω(θ) + π sin θ)          Ω(θ) = 2π(1 − cos θ)
```

At `θ = 60°`, `Ω = π`, so `V = πh³/3` and `A = πh²(1 + √3/2)`. Height sets the scale; the aperture
sets the dimensionless factor.

At `h = 0` the three behaviours separate:

- `p > 0`: the quantity vanishes — height, area, volume, mass, entropy.
- `p < 0`: the quantity diverges — temperature, density.
- `p = 0`: the quantity survives — the horizon ratio, the aperture, the cross-ratio.

So the zero is the common origin of every dimensional quantity, and only the dimensionless
invariants remain at the zero. In this reading the Fold is dimensional analysis with one unit,
`h`: the geometric exponents are the degrees of `det g_k`, the thermodynamic ones follow from the
horizon law, and the dimensionless factors are the invariants `θ`, `arg k`, and the cross-ratio.

## The mass reading

In the paper's homothetic family `M ∝ k` and `R ∝ k`. Therefore

```
M ∝ h          k* = 2GM/(c²R) = constant
```

The mass hierarchy is a scale hierarchy. The horizon sits at the same relative place for every member
of the family; only the absolute size changes. Normalizing the horizon note's rows to `k = 1`:

| `k` | `M` | `R` | `A` | `S` | `T` | `k*` |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 0.5 | 0.5 | 0.5 | 0.25 | 0.25 | 2 | 1 |
| 0.1 | 0.1 | 0.1 | 0.01 | 0.01 | 10 | 1 |

The anchor row is the Sun: `M = 1.988e30 kg`, `R = 6.957e8 m`, `S = 1.049e77`, `T = 6.17e−8 K`,
`k* = 4.245134e−6`. The ratios are the height law: `p_M = p_R = 1`, `p_A = p_S = 2`, `p_T = −1`,
`p_k* = 0`.

One consequence: within the homothetic family, scaling alone cannot make a horizon. The Sun at
`k = 0.1` has the same `k* = 4.245134e−6` as at `k = 1`; a smaller member is not a black hole. A
horizon needs a larger `k*` — a different mass-to-radius ratio (a denser body) at the same scale, or
the fixed-mass collapse, which holds `M` and lets `R` fall. Height changes the size, not the
compactness.

The second column of the horizon table is the opposite reading. In the fixed-mass collapse `M` is
held while `R` falls, so `k* ∝ 1/R` grows and `M ∝ h` fails. The homothetic family is the spectrum
of masses; the collapse is the process. Both are needed: the first says what masses are, the second
says what happens to one.

At fixed `R`, the horizon law can be read as a definition of mass:

```
M = k* c² R / (2G)
```

Mass is the horizon scale. In the homothetic family the ratio is fixed; in the collapse the ratio
moves.

## What height does not fix

The height is one label, not the whole body. The remaining labels are dimensionless or discrete:

- **Shape** is the aperture `θ`. `g_k` sends `R ↦ kR` and leaves `θ` alone; the cone note's whole
  point is that the aperture is the invariant and the range is the coordinate.
- **Turn** is the phase `φ = arg k`. The height is real and does not see the phase; spin and
  chirality need `φ`.
- **Closure** is `m = π/α`, rational versus irrational phase. It selects the discrete pattern, not
  the scale.
- **Observer dimension** `d` fixes what can be measured: 0D scalar, 1D rate, 2D flux, 3D density.
- **Cross-ratio** is the dimensionless invariant of four division points, independent of `k`.

Two bodies of the same height can still behave differently. At a `45°` twist the cube's silhouette
changes `12.3%`; the sphere's changes `0.0%`. The cone's twist is `0.0%` at every angle, because its
fold group is the planes through its axis. Same scale, different shape — height cannot tell them
apart.

Conversely, height cannot change a dimensionless ratio. If two systems differ in a dimensionless
number — a mass ratio, a coupling, a critical exponent — the difference is in `θ`, `φ`, `m` or `d`,
never in `h`. Scale explains magnitudes; it never explains ratios.

Dimensional and dimensionless bookkeeping are different. The dimensional side changes with `h`; the
dimensionless side does not. "Nothing has happened" is exact for the ratios and false for the
magnitudes.

So the full matter label is `(h, θ, φ, m, d)`, not `h` alone. The continuous part of the label space
is `ℝ₊ × (0, π] × S¹`: one non-compact direction (scale) and two compact ones (shape, turn).
"Determined by height" means determined along the non-compact direction alone. It is the spinless,
shape-fixed, structureless sector — not the general case.

## The observer shifts the exponent

The observer table is the height law differentiated. A 0D observer measures a scalar `O ∝ h^p`; a
`d`-dimensional observer measures the same quantity per `d`-volume, so the exponent shifts:

```
O_d ∝ h^{p − d}
```

| observer | measurement | exponent |
|---|---|---|
| 0D | scalar | `p` |
| 1D | derivative / per length | `p − 1` |
| 2D | flux / per area | `p − 2` |
| 3D | density / per volume | `p − 3` |

The shift is the Jacobian: a `d`-volume scales as `k^d`, so a quantity of degree `p` measured per
`d`-volume scales as `k^{p−d}`. The determinant `k^n` is the top case, `d = n`. In form language, the
observer measures a `d`-form: a scalar, a gradient, a flux, a density.

The density row is the check: mass has `p = 1`, so a 3D density has `p = 1 − 3 = −2`, exactly the
`1/h²` in the height table. The observer adds no new law; it selects how many powers of the height
are divided out. A time rate is not in this table: it needs the twist period (stage 3) or the
horizon clock (stage 5). The horizon clock is `T = ħκ/(2πck_B)`; see `the-fold-clock.md`. The observer has
a second parameter, the resolution window; the pair `(d, w)` is in `the-fold-observer.md`.

## The matter ladder

Read the creation chain as a material hierarchy:

| stage | what it adds to matter | label |
|---|---|---|
| 0 the point | the zero, the datum | `P₀` |
| 1 the scale | size and shape; every dimensional quantity is `h^p` | `h ∝ k`, `θ` |
| 2 the fold | crease and orientation; the mirror | `σ_H` |
| 3 the twist | turn, spin, chirality | `φ = arg k` |
| 4 the closure | discrete pattern, rational vs irrational | `m` |
| 5 the horizon | the horizon scale and its thermodynamics | `k*` |
| 6 the observer | what can be measured | `d` |
| 7 the return | the zero again | — |

**Matter is stages 0–1; the rest is what the zero does at that scale.** That is the precise sense in
which matter is "just a zero at different scales." The zero supplies the origin; the scale supplies
the size and the aperture; the fold, twist, closure, horizon and observer supply orientation, turn,
pattern, thermodynamics and measurement.

## Checks

No new measurements. The ratios above come from the existing horizon rows:

| check | result |
|---|---|
| `M/h` across `k = 1, 0.5, 0.1` | constant (`1`) |
| `R/h` across `k = 1, 0.5, 0.1` | constant (`1`) |
| `S/h²` across `k = 1, 0.5, 0.1` | constant (`1`) |
| `T·h` across `k = 1, 0.5, 0.1` | constant (`1`) |
| `k*` across `k = 1, 0.5, 0.1` | constant (`4.245134e−6`) |
| `Ω/4π` at the cone vertex, `θ = 60°` | `0.25` at every zoom |
| `k = 0` | every `p > 0` vanishes; every `p < 0` diverges; `p = 0` survives |

The vertex check is the matter claim at the zero: the dimensional measures vanish, the aperture
survives. That is why the zero still has a shape.

## The caveat

- The height law assumes a **single scale**. A system with several independent lengths has several
  heights; their ratios are dimensionless and are not fixed by either one. The Fold's homothetic
  family is one-scale by construction.
- The Fold does **not** predict a discrete mass spectrum. The scale `k` is continuous; the closure
  quantizes angle, not scale. A discrete spectrum would need an extra condition on `k`, which the
  framework does not supply.
- It does **not** predict mass ratios. A ratio is `(h₁/h₂)(f₁/f₂)`; only the first factor is height.
  `m_p/m_e` would be `k_p/k_e` only if the two bodies shared shape and phase, and no derivation
  follows.
- It does **not** add matter fields or interactions. It is a scaling law, not the Standard Model.
- The physical reading is an **analogy**; the mathematics is the homothetic family and the
  similarity group.

## Files

`the-fold-matter.md` (this note). The order is `the-fold-creation.md`; the lookup is
`the-fold-key.md`.

## The one sentence

**Matter is the zero at a scale: height fixes every dimensional magnitude by a power of `h`, while
shape, turn, closure and observer dimension are the dimensionless structure that height cannot see.**
