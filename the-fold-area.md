# The horizon's measure: area, not volume

## The claim

A horizon is a null surface. Null surfaces are special: the normal is also tangent, the induced metric is
degenerate, and there is no invariant volume. What survives is the area of a spacelike cross-section. So a
horizon's "pixels" are area pixels, not volume pixels.

The Fold's horizon table has `A_H ∝ k²` and `S ∝ k²`. The exponent is the geometry; the coefficient is
external. The area law `S = A/4ℓ_P²` is a reading: the Fold gives `S ∝ A`, not `1/4ℓ_P²`.

The exact content of this note is narrower and sharper: the same exponent `n−2` governs the area and the
number of independent modes on the cross-section. The horizon's area and its mode count share an
exponent.

## The null gauge

Let `H` be a null hypersurface with null normal `n`, `n·n = 0`. On `H`:

- `n` is tangent as well as normal;
- the induced form `q = g|_H` is degenerate, with radical spanned by `n`;
- the signature is `(n−2,0,1)`.

A volume form from `q` would need `det q ≠ 0`; it is zero. A volume form on `H` needs an extra choice — a
transverse null vector — and changes under `n → e^f n`; only `ε_S` on a cross-section `S` is invariant.

| object | formula | status |
|---|---|---|
| induced form | `q = g\|_H` | degenerate; radical `n` |
| metric volume element | `√(det q)` | `0`: no volume form |
| cross-section area | `A[S] = ∫_S √(det q_S)` | invariant |
| affine parameter | `ξ = ∂_λ` | gauge (`λ → aλ + b`) |
| expansion | `θ` | gauge-dependent |

The signature has one null direction. That direction is the radical. The `d = n−1` observer of the
observer note also forgets one direction; the two statements are the same codimension read twice:

| reading | statement |
|---|---|
| signature | `(n−2,0,1)`: one null direction |
| observer | `d = n−1`: one forgotten direction |
| measure | the null direction is the radical; volume is gauge, area is not |

The occlusion note's forgotten direction and the null radical are not merely analogous. Both are the
one direction the surface cannot measure; one is stated as a kernel, the other as a degeneracy. See
`the-fold-occlusion.md` and `the-fold-signature.md`.

## The area exponent is the mode count

For a round cross-section of radius `r`,

```
A[S^{n−2}] = Ω_{n−2} r^{n−2},   r → kr  ⇒  A → k^{n−2} A
```

The independent modes on `S^{n−2}` of degree at most `m` have the same exponent:

| n (spacetime) | cross-section | `A` | modes of degree ≤ m | exponent |
|---|---|---|---|---|
| 3 | S¹ | `2πr` | `2m+1` | 1 |
| 4 | S² | `4πr²` | `(m+1)²` | 2 |
| 5 | S³ | `2π²r³` | `(m+1)(m+2)(2m+3)/6` | 3 |
| 6 | S⁴ | `8π²r⁴/3` | `~m⁴/12` | 4 |

The area scales as `r^{n−2}` and the mode count as `m^{n−2}`. The constants differ; the exponent is the
same. In 4D, area is `∝ r²` and modes are `∝ m²`, so the pixel count `N_A = A/a₀` and the angular
resolution `m` satisfy

```
N_A ~ m²        m ~ √N_A
```

The Fold's `k²` is the 4D-spacetime row. The paper's `n` is the spatial dimension (3 in its examples), so
its horizon is a 2-surface and the exponent is `n_space − 1 = 2`; in the Lorentzian reading the spacetime
dimension is 4 and the exponent is `n_spacetime − 2 = 2`. The two expressions are the same number; the
exponent is the cross-section dimension, not a dynamical input. The coefficient `Ω_{n−2}` is the
round-sphere area; a distorted horizon replaces it by `∫√(det q_S)`.

## Sampling: angle is not area

On a circle, uniform angle is uniform arc length: the 1D sampling note's `N` is area-fair. On a sphere it
is not. The area element is

```
dA = r² sin θ dθ dφ = r² d(cos θ) dφ
```

so equal `θ` bins are not equal area. The two octants `[0, π/4]` and `[π/4, π/2]` have area ratio

```
cos(π/4) / (1 − cos(π/4)) = 1 + √2 = 2.414214
```

on the round sphere. Equal area requires uniform `cos θ`, not uniform `θ`.

| cross-section | coordinate-uniform | area-uniform |
|---|---|---|
| S¹ | `θ` | `θ` (the same) |
| S² | `θ, φ` | `cos θ, φ` |
| S^{n−2} | angles | the measure `√(det q_S)` |

The exterior observer adds a second Jacobian. The projection has a local `cos` of the incidence angle, which
falls to zero at the limb; the total is `Ω/4π = (1 − cos α)/2` with `sin α = r/D`. At `D = r` (the surface
observer) it is `1/2`; at `D = 2.281 r` it is `5.061%`. Equal angular bins over-sample the limb relative to
area.

The causal window's fair sampling is the area measure, not the coordinate angle. This is the exact
correction to "uniform `N` samples": uniform on the circle, but on a higher-dimensional cross-section the
fair grid is uniform in area. See `the-fold-sampling.md`.

## The affine clock

Along the null generators, `ξ = ∂_λ`; the affine parameter is defined up to `λ → aλ + b`. A spherical
congruence has cross-section area

```
A(λ) = A₀ λ^{n−2}        A = 4πλ²  in 4D
```

The label `λ` changes under rescaling; the area of a **given** cross-section does not.

| quantity | depends on affine normalization? |
|---|---|
| `λ` | yes |
| `A(λ)` as a function of the label | yes |
| `A[S]` for a fixed cross-section `S` | no |
| `N_A = A[S]/a₀` | no, given `a₀` |

The horizon has a clock and a pixel count, and only the second is gauge-invariant. This is the horizon's
version of the observer's `(d, w)`: `w` is a coordinate scale, `A` is the invariant. The sampling note's
`N` is dual to the object's `m`; the area is dual to the mode count.

The other clock is the Killing one, normalized at infinity. Its rate is the surface gravity `κ`, and its
Euclidean period `2πc/κ` is the temperature. See `the-fold-clock.md`.

## The Bekenstein saturation

In 4D Planck units (`G = c = ħ = k_B = 1`), the bound is `S_B = 2π R M`. At `R = r_s = 2M`,

```
S_B = 4πM²,        S = A/4 = πr_s² = 4πM²
```

so `S = S_B` exactly. In SI the same identity is

```
S = A/4ℓ_P² = 4πGM²/(ħc) = 2π r_s M c/ħ = S_B
```

| body | `r_s` (m) | `A_H` (m²) | `S/k_B` | `S_B/k_B` |
|---|---|---|---|---|
| Earth | 8.870e−3 | 9.887e−4 | 9.462e65 | 9.462e65 |
| Sun | 2.953e3 | 1.096e8 | 1.049e77 | 1.049e77 |
| 70 kg water | 1.040e−25 | 1.358e−49 | 1.300e20 | 1.300e20 |

The ratio is `1.000000000000` for all three. For the same mass, the horizon entropy `S = 4πM²` is below the
bound `S_B(R) = 4πRM` when `R > r_s`, so the bound is not saturated outside; at `R = r_s` it is saturated.
The body's own entropy is a separate quantity, bounded by `S_B(R)`. Inside the horizon the bound's premises
fail; the exterior area law is not a statement about the interior. In the homothetic family, `S ∝ M²` and
`S_B ∝ MR`; saturation is `R = r_s = 2GM/c²`, the horizon member, not the whole family (which has `R ∝ M`
but a different constant).

This is the static spherical case. Rotating and charged horizons have different relations, and the Fold's
`k*` is the static spherical ratio. The equality is exact arithmetic, not a derivation of the area law's
coefficient.

## Adjacent research

The null geometry is standard: the induced metric is degenerate, the null normal is tangent, and the area
of cross-sections is the invariant. The Bekenstein bound is the entropy-to-energy bound; at the
Schwarzschild radius it is saturated. The holographic principle reads the area as the information
capacity; the entanglement area law and the loop-quantum-gravity area spectrum are independent area
laws. This note borrows the area/gauge distinction and the saturation arithmetic. It does not borrow the
dynamics.

| topic | reference | link |
|---|---|---|
| null geometry | Gourgoulhon & Jaramillo, *A 3+1 perspective on null hypersurfaces and isolated horizons*, Phys. Rep. 423 (2006) 159–294 | [arXiv](https://arxiv.org/abs/gr-qc/0503113) |
| Bekenstein bound | Bekenstein, *Universal upper bound on the entropy-to-energy ratio for bounded systems*, Phys. Rev. D 23 (1981) 287 | [DOI](https://doi.org/10.1103/PhysRevD.23.287) |
| holography | 't Hooft, *Dimensional reduction in quantum gravity*, arXiv:gr-qc/9310026 | [arXiv](https://arxiv.org/abs/gr-qc/9310026) |
| holography | Susskind, *The world as a hologram*, J. Math. Phys. 36 (1995) 6377–6396 | [DOI](https://doi.org/10.1063/1.531249) |
| area spectrum | Rovelli & Smolin, *Discreteness of area and volume in quantum gravity*, Nucl. Phys. B442 (1995) 593–622 | [arXiv](https://arxiv.org/abs/gr-qc/9411005) |
| causal diamond | Jacobson, *Entanglement equilibrium and the Einstein equation*, Phys. Rev. Lett. 116 (2016) 201101 | [arXiv](https://arxiv.org/abs/1505.04753) |
| entanglement area law | Bombelli, Koul, Lee, Sorkin, *Quantum source of entropy for black holes*, Phys. Rev. D 34 (1986) 373 | [DOI](https://doi.org/10.1103/PhysRevD.34.373) |

## Checks

| check | value |
|---|---|
| `S = S_B` at `R = r_s`, Earth / Sun / 70 kg | `1.000000000000` |
| analytic `4πGM²/(ħc)` vs `πr_s²/ℓ_P²` | diff `≤ 2.2e−16` |
| area scaling `r → kr` | `k²` in 4D |
| modes on `S²`, `m = 1,2,5,10` | `4, 9, 36, 121` |
| modes/area exponent, `n = 3,4,5` | `1, 2, 3` |
| sphere octant ratio | `1 + √2 = 2.414214` |
| spheroid `a = 1, b = 2`, same bins | `3.391933` |
| exterior `D = 2.281 r` | `Ω/4π = 5.061%` |
| limb `D = r` | `Ω/4π = 1/2` |
| affine area, 4D spherical congruence | `A = 4πλ²` |

The entropy rows are exact identities checked at machine precision; the octant ratio is exact; the
spheroid and solid-angle rows are numerical evaluations of the stated formulas.

## What this does and does not say

- It **does** identify the invariant measure on a null horizon as cross-sectional area, and show that the
  null-normal rescaling is the gauge that kills volume.
- It **does** show that the area exponent `n−2` equals the mode-count exponent; in 4D, area `∝ r²` and
  modes `∝ m²`.
- It **does** show that uniform angle is area-fair only on a circle; on `S²` equal `θ` bins have ratio
  `1 + √2`, and the exterior projection adds a `cos α` Jacobian that vanishes at the limb.
- It **does** identify the horizon as the saturation surface of the static Bekenstein bound, exactly.
- It **does** separate the exponent from the coefficient: the Fold gives `S ∝ A`, not `1/4ℓ_P²`.
- It **does not** derive the area-law coefficient, the Planck scale, or the value `1/4`.
- It **does not** claim the horizon is a Planck lattice; the pixel count requires an external `a₀`.
- It **does not** derive holography, the entanglement area law, or the loop area spectrum; those are
  rhymes.
- It **does not** treat rotating or charged horizons; the Fold's horizon is static spherical.
- It **does not** claim the affine parameter is physical time; it is a gauge label.

## The one sentence

**A horizon has no invariant volume — the null normal can be rescaled and the induced metric is
degenerate — but each cross-section has an invariant area; the Fold's `k²` is that area exponent, the
number of modes scales the same way, and the horizon is where the static Bekenstein bound is saturated.**

## Files

`the-fold-area.md` (this note). The horizon's two laws are in `the-fold-horizon.md`; the causal window and
sampling are in `the-fold-sampling.md`; the null signature is in `the-fold-signature.md`; the one
forgotten direction is in `the-fold-occlusion.md`; the exponent shift is in `the-fold-matter.md`; the
open-problem boundaries are in `the-fold-problems.md`; the order is in `the-fold-creation.md`; the lookup
is `the-fold-key.md`.
