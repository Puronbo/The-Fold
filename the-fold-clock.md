# The horizon's clock: surface gravity, imaginary time, and the k-law

## The claim

The area note showed that a null horizon has no invariant volume but does have an invariant area. The
same split holds for time. The affine parameter along the null generators is gauge; the **Killing** time,
normalized at infinity, is not. Its rate at the horizon is the surface gravity `κ`, and the Euclidean
period `2πc/κ` gives the temperature

```
T = ħκ/(2π c k_B)
```

The Fold's `T ∝ 1/k` is the exponent of this law. The coefficient `ħc³/(8πGk_B)` is external, like the
`1/4ℓ_P²` in the area law. The static spherical horizon is where the clock, the area, and the mass close:
`M = κA/(4πG)` and `dM = κ dA/(8πG)`.

## The two clocks

Along a null generator, the affine parameter is defined by `ξ = ∂_λ` and `∇_ξ ξ = 0`; it is fixed only up
to `λ → aλ + b`. The Killing time is defined by `ξ = ∂_t` with the normalization `ξ² → −c²` at infinity.
The normalization is the asymptotic observer's, and it is what makes the temperature a frame-dependent but
well-defined quantity.

| clock | vector | normalization | status |
|---|---|---|---|
| affine | `ξ = ∂_λ`, `∇_ξ ξ = 0` | `λ → aλ + b` | gauge |
| Killing | `ξ = ∂_t` | `ξ² → −c²` at infinity | fixed |
| relation | `λ` and `t` are exponential in each other near the horizon | — | different clocks |

For a static exterior observer the Killing time diverges at the horizon, while the affine parameter along
the generator does not. That is the exact sense in which the horizon has a clock but not a universal one:
the affine clock is a coordinate, the Killing clock is the asymptotic observer's.

## Surface gravity

For the static spherical metric

```
ds² = −f(r) c² dt² + f(r)^{-1} dr² + r² dΩ²,   f = 1 − r_s/r
```

the surface gravity is

```
κ = ½ c² f'(r_s) = c⁴/(4GM)
```

with units of acceleration. The Hawking temperature is

```
T = ħκ/(2π c k_B) = ħc³/(8πGMk_B)
```

| body | `r_s` (m) | `κ` (m/s²) | `T` (K) | period `2πc/κ` (s) |
|---|---|---|---|---|
| Earth | 8.870e−3 | 5.066e18 | 2.054e−2 | 3.718e−10 |
| Sun | 2.953e3 | 1.522e13 | 6.170e−8 | 1.238e−4 |
| 70 kg water | 1.040e−25 | 4.322e41 | 1.753e21 | 4.358e−33 |

The product `T·M` is the same for all three: `1.2269e23 K·kg`. That is the exact content of `T ∝ 1/M`.
The 70 kg sphere is the hottest horizon in the table by more than 28 orders of magnitude, because
`T ∝ 1/M`.

## Imaginary time

Continue `t → −iτ`. Near the horizon the Euclidean metric becomes a cone,

```
ds²_E ≈ (κ/c)² ρ² dτ² + dρ² + r_s² dΩ²
```

and regularity at `ρ = 0` requires `τ` to be periodic with period

```
τ_period = 2π c/κ
```

so that

```
T = ħ/(k_B τ_period) = ħκ/(2π c k_B)
```

The `2π` is the circle's period: the same `2π` that closes a full turn. The Euclidean geometry is a cone;
the conical singularity is removed by choosing the period, and the temperature is the inverse period. This
is exact for the static spherical horizon. For a general stationary horizon the zeroth law makes `κ`
constant on the horizon, and the same period applies once the Killing vector is normalized at infinity.

## The Fold's law

In the homothetic family `M ∝ k`, so `T ∝ 1/M ∝ 1/k`. In the collapse `M` is fixed, so `T` is constant.
The exponent `−1` is exact; the coefficient `ħc³/(8πGk_B)` is external. The Fold gives the direction and
the power, not the `8π`.

| regime | `M` | `T` | `S` | `T·S` |
|---|---|---|---|---|
| homothetic | `∝ k` | `∝ 1/k` | `∝ k²` | `∝ k` |
| collapse | constant | constant | constant | constant |

The `T·S ∝ k` row is the horizon's energy: `T dS` balances `dM` in the family, and both sides vanish in
the collapse once the horizon exists. The entropy is not accumulated during the fall; the clock starts
with the horizon.

## The first law and Smarr

In natural units the first law is

```
dM = κ dA/(8πG)
```

and the Smarr formula for the Schwarzschild horizon is

```
M = κA/(4πG)
```

Both are exact. With `S = A/(4G)` and `T = κ/(2π)`,

```
T dS = (κ/(2π))(dA/(4G)) = κ dA/(8πG) = dM
```

which is the identity the horizon note checked by finite differences. In SI the right-hand side of
`T dS = dM` carries `c²`; the geometric identity above is the `c = 1` form.

The Smarr formula ties the clock to the pixel: the surface gravity and the area are not independent
horizon data. For Kerr or Reissner–Nordström there are extra `ΩJ` and `ΦQ` terms, and the Fold's `k*` is
the static spherical ratio.

## The clock and the pixel

The horizon's invariant pair is `(κ, A)`, or `(T, S)`. The gauge pair is `(λ, volume)`. The area note
establishes the area half; this note establishes the clock half.

A scaling worth keeping: the period and the area are not independent,

```
period = 2π c/κ ∝ r_s ∝ A^{1/(n−2)}
```

In 4D, `period ∝ √A`, with the exact coefficient `2√π/c` for the round Schwarzschild horizon. The clock
period and the pixel count are two readings of the same scale.

The observer's window at the horizon is thermal: the KMS condition makes correlation functions periodic
in imaginary time with period `ħ/(k_B T)`, and the Gaussian window is the Euclidean heat kernel. The
period is the compactification radius of the Euclidean geometry. That is a reading of the same `2π`, not
a derivation of thermality from the Fold.

## Adjacent research

The black-hole laws are the exact ancestors: the zeroth law makes `κ` constant on a stationary horizon;
the first law is `dM = κ dA/(8πG) + ΩJ + ΦQ`; the second law is the area increase; the third is the
extremality limit. Hawking's calculation fixes the coefficient; the Euclidean period fixes it
geometrically. Unruh's effect is the same period for an accelerated observer in flat space. This note
borrows the clock/area distinction and the static arithmetic. It does not derive the radiation. The
accelerated observer's version is in `the-fold-unruh.md`.

| topic | reference | link |
|---|---|---|
| black-hole laws | Bardeen, Carter, Hawking, *The four laws of black hole mechanics*, Commun. Math. Phys. 31 (1973) 161–170 | [DOI](https://doi.org/10.1007/BF01645742) |
| entropy | Bekenstein, *Black holes and entropy*, Phys. Rev. D 7 (1973) 2333 | [DOI](https://doi.org/10.1103/PhysRevD.7.2333) |
| temperature | Hawking, *Particle creation by black holes*, Commun. Math. Phys. 43 (1975) 199–220 | [DOI](https://doi.org/10.1007/BF02345020) |
| imaginary time | Gibbons & Hawking, *Cosmological event horizons, thermodynamics, and particle creation*, Phys. Rev. D 15 (1977) 2738 | [DOI](https://doi.org/10.1103/PhysRevD.15.2738) |
| path integral | Hartle & Hawking, *Path-integral derivation of black-hole radiance*, Phys. Rev. D 13 (1976) 2188 | [DOI](https://doi.org/10.1103/PhysRevD.13.2188) |
| Unruh effect | Unruh, *Notes on black-hole evaporation*, Phys. Rev. D 14 (1976) 870 | [DOI](https://doi.org/10.1103/PhysRevD.14.870) |

## Checks

| check | value |
|---|---|
| `T·M`, Earth / Sun / 70 kg | `1.2269e23 K·kg` |
| Sun `T` | `6.170e−8 K` (matches the horizon note) |
| Earth / 70 kg `T` | `2.054e−2` / `1.753e21 K` |
| Sun `κ` | `1.522e13 m/s²` |
| Sun period `2πc/κ` | `1.238e−4 s` |
| period / `√A`, all three | `2√π/c = 1.182454e−8 s/m` |
| Smarr `M = κA/(4πG)` | ratio `1.000000000` |
| first law `κ dA/(8πG)` vs `dM` | `1.0000005` (finite difference) |
| `S·T` Sun | `6.472e69` |
| `T` ratio Earth/Sun | `3.329e5 = M_Sun/M_Earth` |

The temperature values are the horizon note's; the `T·M` constant, the period/area ratio, and Smarr are
the new exact checks. The first-law row is a finite difference; the identity is analytic.

## What this does and does not say

- It **does** identify the Killing clock as the invariant one and the affine parameter as gauge.
- It **does** derive the Euclidean period `2πc/κ` and the temperature `T = ħκ/(2πck_B)` for the static
  spherical horizon.
- It **does** show `T ∝ 1/M` exactly, hence `T ∝ 1/k` in the homothetic family and constant temperature
  in the collapse.
- It **does** close the first law and Smarr with the area: `dM = κ dA/(8πG)`, `M = κA/(4πG)`.
- It **does** show the period and the area are tied: `period ∝ A^{1/(n−2)}`, `∝ √A` in 4D.
- It **does not** derive the coefficient `1/8π` or Hawking radiation from the Fold; the Fold gives the
  exponent.
- It **does not** claim the Fold is a quantum field theory or that the KMS reading is a derivation.
- It **does not** treat rotating or charged horizons; those add the `ΩJ` and `ΦQ` terms.
- It **does not** claim the affine parameter is physical time; it is a gauge label.
- It **does not** claim the temperature is absolute; it is normalized by the asymptotic observer's
  Killing vector.

## The one sentence

**The horizon's affine clock is gauge, but its Killing clock is normalized at infinity; its rate is
`κ = c⁴/(4GM)`, the Euclidean period `2πc/κ` gives `T = ħκ/(2πck_B)`, and the Fold's `T ∝ 1/k` is the
exponent of that law, with `M = κA/(4πG)` closing the clock to the area.**

## Files

`the-fold-clock.md` (this note). The area measure and the affine clock are in `the-fold-area.md`; the two
horizon laws and the temperature column are in `the-fold-horizon.md`; the causal window is in
`the-fold-sampling.md`; the observer pair is in `the-fold-observer.md`; the null signature is in
`the-fold-signature.md`; the open-problem boundaries are in `the-fold-problems.md`; the order is in
`the-fold-creation.md`; the lookup is `the-fold-key.md`.
