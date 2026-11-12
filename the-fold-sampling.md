# Sampling, closure, and the horizon window

## The claim

The observer note makes the observer a pair `(d, w)`: a form degree and a window. The closure note makes
the object's pattern a number `m = π/α`. This note adds the discrete dual of the window — a sampling
lattice, or `N` samples per turn — and reads the horizon as the same observer at the null limit.

| stage | object parameter | probe parameter | exact relation |
|---|---|---|---|
| closure | `m = π/α` | `N` samples per turn | resolved iff `N > 2m` |
| observer | degree `p` of the quantity | `d` (form), `w` (window) | `h^{p−d}` |
| horizon | null crease | `d = n−1`, causal window | boundary of the cone |

The claim is not that the closure *is* a sampling lattice. The closure is the object's symmetry; the
sampling is the probe's discretization; they are dual, and the Nyquist relation is the exact bridge.

## Nyquist: the closure's discrete dual

An `m`-fold pattern has angular frequency `m`: its finest harmonic is `cos(mθ)`. A probe with `N` samples
per turn sees

```
cos(m · 2πn/N) = cos(2πmn/N),   n = 0, …, N−1
```

The apparent frequency is

```
m_app = min(r, N − r),   r = m mod N
```

and the sampled sequence is identical to its alias: no probe with `N` points can distinguish `m` from
`m_app`. The pattern is resolved exactly when `m` is below the Nyquist frequency `N/2`:

```
N > 2m
```

For `m = 5`:

| `N` | `m mod N` | apparent | residual | resolved |
|---|---|---|---|---|
| 6 | 5 | 1 | `3.2e−15` | no |
| 7 | 5 | 2 | `1.4e−15` | no |
| 8 | 5 | 3 | `3.3e−15` | no |
| 9 | 5 | 4 | `4.3e−15` | no |
| 10 | 5 | 5 | `0` | no — at Nyquist |
| 11 | 5 | 5 | `0` | yes |
| 12 | 5 | 5 | `0` | yes |

The residual is zero because the alias is exact, not approximate. `N = 10` is the marginal case: the
samples alternate, `cos(πn) = (−1)ⁿ`, and the harmonic sits exactly at Nyquist. The strict inequality
`N > 2m` is the condition for resolving it as a wave.

On a circle of radius `R`, the sample spacing is `a = 2πR/N` and the half-sector arc is `πR/m`. The
Nyquist condition is exactly

```
a < πR/m
```

so the probe must be finer than the half-sector it is trying to see.

## The window's discrete dual

The continuous window of the observer note is a Gaussian in angle, with standard deviation `σ = w/R`.
It multiplies the `m`-th harmonic by

```
e^{−m²σ²/2} = e^{−m²w²/(2R²)}
```

At the half-sector width `σ = π/m`, the attenuation is

```
e^{−m²(π/m)²/2} = e^{−π²/2} = 7.1919e−3
```

the same `0.72%` threshold as the folded-line note at `w = ℓ`. The closure number enters squared: a finer
pattern (larger `m`) is attenuated faster.

| `m` | `σ = π/m` | attenuation |
|---|---|---|
| 3 | `1.047198` | `7.1919e−3` |
| 4 | `0.785398` | `7.1919e−3` |
| 5 | `0.628319` | `7.1919e−3` |
| 6 | `0.523599` | `7.1919e−3` |
| 8 | `0.392699` | `7.1919e−3` |
| 10 | `0.314159` | `7.1919e−3` |

The window and the sampling therefore share the same cutoff: both the window width `w` and the sample
spacing `a` must be below the half-sector arc `πR/m`. The coarser of the two sets the resolution. This is
the exact discrete dual of "the window resolves the fold."

On a higher-dimensional cross-section, uniform angle is not uniform area: on `S²` the area element is
`sin θ dθ dφ`, and equal `θ` octants have ratio `1 + √2`. The fair sampling is the area measure, not the
coordinate angle. See `the-fold-area.md`.

## The two lattices

There are two lattices in the sentence, and they must not be conflated:

- the **object's** lattice, which the closure `m` describes;
- the **probe's** lattice, which the sampling `N` describes.

The crystallographic restriction is a statement about the object's periodic lattice: a rotation by
`2π/n` is an integer matrix in a lattice basis only if `2cos(2π/n)` is an integer, which gives
`n ∈ {1,2,3,4,6}`. The probe is not restricted:

| object | closure | periodic lattice? | probe |
|---|---|---|---|
| crystal | `m ∈ {1,2,3,4,6}` | yes | `N > 2m` |
| quasicrystal | `m = 5, 8, 10, 12` | no | `N > 2m` still resolves the pattern |
| irrational | `m` irrational | no | no finite `N` closes; the orbit is dense |

The fivefold, eightfold, tenfold and twelvefold patterns cannot be periodic crystals, but a probe with
`N > 2m` samples their `m`-fold diffraction without aliasing. The quasicrystal is the case where the
object has no periodic lattice and the probe still has enough points. That is the exact content of the
closure note's "only some `n` survive in a lattice": the restriction is on the object, not on the
observer.

## The horizon: the null window

The observer note places the surface observer at `d = n−1`, edge-on, with `Ω = 2π`. The horizon note
reads the horizon as a null crease: `n·n = 0`, induced form `(n−2,0,1)`. This note adds the window.

A Gaussian window has support everywhere; it is the non-causal idealization. The causal window is the
retarded propagator, whose support is the future light cone. In one dimension the retarded Green's
function is

```
G(t, x) = ½ Θ(t − |x|)
```

constant inside the cone `|x| ≤ t` and zero outside; the boundary `|x| = t` is null. In three dimensions
the support collapses to the cone itself, `G ∝ δ(t − |x|)/|x|`. The horizon is the boundary of the
observer's causal past, i.e. the boundary of the causal window. That is a reading of the null signature
and the support property, not a derivation of the metric.

So the horizon is the `d = n−1` observer whose window is the causal cone; the null crease is its
boundary. The Gaussian and the causal window agree in the interior and differ at the boundary: the
Gaussian leaks, the retarded propagator does not.

The causal window's Euclidean period is `2πc/κ`, and the surface gravity sets the temperature
`T = ħκ/(2πck_B)`. See `the-fold-clock.md`. The accelerated observer's window is the Rindler wedge, with
period `2πc/a`; see `the-fold-unruh.md`. The wedge's entanglement entropy is in
`the-fold-entanglement.md`.

## The probe is `(d, w, a)`

The observer is `(d, w)`; a discrete probe adds `a`, the sample spacing, or `N = 2πR/a`, the number of
samples per turn. The closure `m` is not a third probe parameter: it is the object's angular frequency,
and `N` is its dual. The full probe is

```
(d, w, a),   resolution = max(w, a),   closure dual N = 2πR/a
```

The observer note's `(d, w)` is the continuous slice `a → 0`; the closure note's `m` is the object's
side. The horizon is the `d = n−1` case with the causal window. One pair of parameters describes the
probe; one number describes the object; the Nyquist relation is the bridge.

## Adjacent research: sampling and quasicrystals

The Nyquist–Shannon theorem is the exact statement behind `N > 2m`: a signal band-limited to `m` is
determined by samples spaced finer than the half-period. Whittaker gave the interpolation formula;
Nyquist the telegraph rate; Shannon the modern form. The quasicrystal is the object-side counterpart:
Shechtman's diffraction pattern has long-range orientational order and no translational symmetry, which
is exactly an `m`-fold pattern with no periodic lattice. The crystallographic restriction and the
Nyquist condition are different theorems about the two lattices.

| topic | reference | link |
|---|---|---|
| sampling | Nyquist, *Certain topics in telegraph transmission theory*, Trans. AIEE 47 (1928), 617–644 | — |
| sampling | Shannon, *Communication in the presence of noise*, Proc. IRE 37 (1949), 10–21 | — |
| sampling | Whittaker, *On the functions represented by the expansions of the interpolation theory*, Proc. Roy. Soc. Edinburgh 35 (1915), 181–194 | — |
| quasicrystals | Shechtman, Blech, Gratias, Cahn, *Metallic phase with long-range orientational order and no translational symmetry*, Phys. Rev. Lett. 53 (1984), 1951 | [DOI](https://doi.org/10.1103/PhysRevLett.53.1951) |
| causal window | *Retarded potential* | [Wikipedia](https://en.wikipedia.org/wiki/Retarded_potential) |

## Checks

| check | value |
|---|---|
| alias, `m=5`, `N=6/7/8/9` | apparent `1/2/3/4`; residual `≤ 4.3e−15` |
| Nyquist, `m=5`, `N=10` | apparent `5`, residual `0`; not resolved |
| resolved, `m=5`, `N=11/12` | `N > 2m` |
| Gaussian, `m=5`, `σ=0.2/0.5/π/5` | `0.606531 / 0.043937 / 0.007192` |
| half-sector, `σ=π/m`, `m=3…10` | `e^{−π²/2} = 7.1919e−3` |
| crystallographic `2cos(2π/n)` | integer only for `n=2,3,4,6` |
| horizon signature, `n=4` | `(3,1,0) → (2,0,1)` |
| retarded support | `\|x\| ≤ t`; boundary `\|x\| = t` |

The alias and attenuation values are floating-point confirmations of the formulas; the crystallographic
and signature rows are the closure and horizon notes' exact statements, restated.

## What this does and does not say

- It **does** give the discrete dual of the observer's window: a sampling lattice `a`, or `N` samples
  per turn.
- It **does** state the exact Nyquist condition for an `m`-fold closure: `N > 2m`, equivalently
  `a < πR/m`.
- It **does** give the alias formula `m_app = min(m mod N, N − m mod N)` and the exact Gaussian
  attenuation `e^{−m²σ²/2}`; both cutoffs are the half-sector arc.
- It **does** separate the object's lattice from the probe's: the crystallographic restriction limits
  `m` for a periodic crystal, not `N` for the probe.
- It **does** read the horizon as the `d = n−1` observer with the causal window, and identify the null
  crease as the boundary of its support.
- It **does not** claim the closure is a sampling lattice; it is the object's symmetry, dual to the
  probe's `N`.
- It **does not** claim the crystallographic restriction limits the observer; it limits the object's
  periodic lattice.
- It **does not** derive the horizon from the window; the causal-support reading is a reading of the
  null signature.
- It **does not** claim the Gaussian is causal; it is the non-causal idealization, and the retarded
  propagator is the causal window.
- It **does not** make the sampling theorem a statement about the Fold's dynamics; it is the exact
  discrete dual of resolution.

## The one sentence

**The closure `m` and the probe `N` are dual: an `m`-fold pattern is resolved exactly when the probe
takes more than `2m` samples per turn, the Gaussian window and the sample spacing share the half-sector
cutoff `πR/m`, and the horizon is the `d = n−1` observer whose window is the causal cone, so the null
crease is its boundary.**

## Files

`the-fold-sampling.md` (this note). The observer pair is in `the-fold-observer.md`; the closure law
`m = π/α` and the crystallographic restriction are in `the-fold-closure.md`; the null crease and the
horizon signature are in `the-fold-horizon.md` and `the-fold-signature.md`; the window attenuation is in
`the-fold-afar.md`; the form degree is in `the-fold-matter.md`; the order is in `the-fold-creation.md`;
the lookup is `the-fold-key.md`.
