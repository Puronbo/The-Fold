# The general coefficient: Wald entropy and the Noether charge

## The claim

The area note gave the horizon `S = A/4ℓ_P²` and separated the exponent from the coefficient. The
entanglement note showed that the wedge's coefficient is the cutoff's. The holography note gave the one
case where the coefficient is fixed: `1/4G_N` on the minimal surface. This note asks the general question:
for an arbitrary gravitational action, what is the horizon entropy?

Wald's answer is that the entropy is the Noether charge of the horizon Killing field:

```
S_Wald = (2π/κ) ∫_Σ Q[ξ] = −2π ∫_Σ (∂L/∂R_{abcd}) ε_{ab}ε_{cd} √h d^{n−2}x
```

It is still an integral over the codimension-two cross-section `Σ`, not the 3-volume. The `2π` is the same
thermal period as the Euclidean and modular `2π`. The coefficient is the action's: `A/4G` only for
Einstein–Hilbert. For `f(R)` it is `f'(R)A/4G`; for Gauss–Bonnet and Lovelock it is an integral of
intrinsic curvature over `Σ`.

The Fold's `S ∝ A` supplies the exponent `n−2` and the codimension-two locus. The action, the Riemann
tensor, the binormal, and the coefficient are external. In higher-curvature gravity even the "area law" is
not universal: the entropy is an integral of a local density over the cross-section, and only in the
Einstein–Hilbert case is that density the universal constant `1/4G`.

## The formula

Let the theory be described by a diffeomorphism-invariant Lagrangian `L(g, R, ∇R, ψ)`, with `ψ` the matter
fields. For a stationary black hole with horizon Killing field `ξ` and surface gravity `κ`, the Noether
charge `(n−2)`-form `Q[ξ]` gives

```
S_Wald = (2π/κ) ∫_Σ Q[ξ]
```

where `Σ` is any cross-section of the horizon. Normalizing `ξ` to unit surface gravity absorbs the `κ` and
gives `2π∫Q`. For a Lagrangian that depends on the Riemann tensor but not its derivatives, the charge
evaluates to the local expression

```
S_Wald = −2π ∫_Σ (∂L/∂R_{abcd}) ε_{ab}ε_{cd} √h d^{n−2}x
```

with `ε_{ab}` the binormal to `Σ`, normalized by `ε_{ab}ε^{ab} = −2`, and `h` the induced metric on `Σ`.
The two expressions are the same entropy: the first is the definition, the second is the evaluation on a
stationary horizon.

| object | formula | role |
|---|---|---|
| Lagrangian | `L(g, R, ∇R, ψ)` | diffeomorphism invariant |
| horizon Killing field | `ξ` | stationary symmetry |
| surface gravity | `κ` | normalized at infinity |
| Noether charge | `Q[ξ]` | `(n−2)`-form |
| binormal | `ε_{ab}`, `ε² = −2` | normal-plane projector |
| entropy | `S_Wald` | cross-section integral |

The formula is local on the horizon and independent of the cross-section chosen: Jacobson, Kang, and
Myers showed that evaluating it on an arbitrary cross-section gives the same result, and that the Noether
charge ambiguities do not affect the entropy. That is what makes it a property of the horizon rather than
of a particular slice.

## The checks

The Einstein–Hilbert case fixes the normalization. With

```
L = R/(16πG)
```

the derivative is

```
∂L/∂R_{abcd} = (1/16πG)(1/2)(g^{ac}g^{bd} − g^{ad}g^{bc})
```

and the contraction is

```
(∂L/∂R_{abcd}) ε_{ab}ε_{cd} = (1/32πG)(2 ε·ε) = −1/(8πG)
```

using `ε·ε = −2`. Then

```
S = −2π (−1/(8πG)) A = A/(4G)
```

which is the area note's coefficient. The `1/4` is not put in by hand; it is the normalization of the
Einstein–Hilbert action.

The simplest modification is `f(R)` gravity:

```
L = f(R)/(16πG)        ⇒        S = f'(R) A/(4G)
```

The area is multiplied by `f'(R)`. For `f(R) = R` this is `A/4G`; for `f(R) = R + βR²` it is
`(1 + 2βR)A/4G`. On a vacuum horizon with `R = 0`, the correction vanishes for this particular `f`; the
formula is exact, but the example needs `R ≠ 0` to show a nonzero shift. That is already enough to see
that the entropy is not the area: it is the area times a function of the curvature.

Gauss–Bonnet gravity makes the point without a vacuum accident. With

```
L = (1/16πG)(R + α L_GB),        L_GB = R_{abcd}R^{abcd} − 4R_{ab}R^{ab} + R²
```

the Wald entropy is

```
S = A/(4G) + (α/2G) ∫_Σ √h R̃
```

where `R̃` is the intrinsic Ricci scalar of the cross-section. For a maximally symmetric cross-section of
curvature `k` and radius `r_+`,

```
R̃ = k(n−2)(n−3)/r_+²
```

so

```
S = (A/4G)[1 + 2αk(n−2)(n−3)/r_+²]
```

In five dimensions with `k = 1`, this is `S = (A/4G)(1 + 12α/r_+²)`. In four dimensions the Gauss–Bonnet
term is topological: the correction is proportional to the Euler characteristic of `Σ`, and for a spherical
cross-section `∫_Σ R̃ = 8π`, so the shift is the constant `4πα/G` and the area coefficient is unchanged.
The correction becomes a real modification of the coefficient only for `n ≥ 5`.

Lovelock gravity collects the pattern. For

```
L = (1/16πG) ∑_{q=1}^{P} α_q L_q,        L_0 = 1, L_1 = R, L_2 = L_GB, …
```

the entropy is

```
S_Lovelock = (1/4G) ∑_{q=1}^{P} q α_q ∫_Σ √h L_{q−1}(h)
```

where `L_{q−1}(h)` is the same Lovelock density built from the induced metric `h` on the cross-section.
The `q = 1` term is `A/4G`; the `q = 2` term is `2α∫R̃`; the `q = 3` term is `3α₃∫L_GB(h)`; and so on.
The sum is finite because `L_q` vanishes identically when `2q > n`.

| theory | Lagrangian | `S` |
|---|---|---|
| Einstein–Hilbert | `R/(16πG)` | `A/(4G)` |
| `f(R)` | `f(R)/(16πG)` | `f'(R)A/(4G)` |
| Gauss–Bonnet | `(R + αL_GB)/(16πG)` | `A/(4G) + (α/2G)∫√h R̃` |
| Lovelock | `(1/16πG)∑α_qL_q` | `(1/4G)∑qα_q∫√h L_{q−1}(h)` |
| general | `L(g,R,∇R)` | `−2π∫(∂L/∂R_{abcd})ε_{ab}ε_{cd}√h` |

The rows are the exact Wald entropies in the stated normalization. The Gauss–Bonnet coefficient is the
one that follows from `L_GB = R_{abcd}R^{abcd} − 4R_{ab}R^{ab} + R²`; changing the normalization of `α`
changes the number, not the structure.

## The Noether charge and the first law

The reason the entropy is a Noether charge is the first law. Wald proved that for any diffeomorphism-
invariant theory,

```
dM = (κ/2π) dS + Ω_H dJ + Φ_H dQ
```

for perturbations to nearby stationary black holes, with `S` the Noether-charge entropy. The entropy is
defined so that the first law holds; it is not an independent guess. In units `ħ = c = k_B = 1`, the
coefficient `κ/2π` is the temperature.

For Einstein–Hilbert, the check is the Schwarzschild arithmetic. With `κ = 1/(4GM)` and `A = 16πG²M²`,

```
(κ/2π) dS = (κ/8πG) dA = dM
```

and the Smarr relation is

```
M = κA/(4πG)
```

which is the clock note's closure. The general-coefficient version replaces `A/4G` by `S_Wald` and keeps
the same `κ/2π`.

For dynamical black holes, Iyer and Wald propose the same local expression evaluated on a dynamical
horizon cross-section. The proposal agrees with the stationary formula and is independent of the Noether
ambiguities, but whether it obeys a second law is open. That is a boundary of the classical statement, not
a Fold result.

## What happens to the area law

Write the entropy as a cross-section integral:

```
S = ∫_Σ s √h d^{n−2}x,        s = −2π (∂L/∂R_{abcd}) ε_{ab}ε_{cd}
```

In Einstein–Hilbert, `s = 1/4G` is a constant, so `S = A/4G` for any shape of cross-section. That is why
the area law is exact there: the integrand does not depend on the geometry.

In higher-curvature gravity, `s` depends on the curvature. For a spherically symmetric horizon, `s` is
constant on the cross-section, so `S` is still proportional to `A`; the exponent `n−2` survives and only
the coefficient changes. For a non-spherical cross-section, `s` varies, so `S` is not proportional to `A`
at all. The "area law" with the universal coefficient `1/4G` is the Einstein–Hilbert case; the general
statement is a codimension-two integral of a local density, and the symmetric case still scales as `A` with
a theory-dependent coefficient.

This sharpens the horizon note's measure argument. The cross-section area is invariant and the 3-volume is
gauge; Wald entropy is a codimension-two integral, so it inherits the invariance. The Fold's null crease
has signature `(n−2,0,1)`, and the integral runs over exactly those `n−2` dimensions.

| reading | exact object | Fold's version |
|---|---|---|
| entropy | `S_Wald = −2π∫(∂L/∂R)εε` | `S ∝ A` (exponent only) |
| locus | codimension-two cross-section `Σ` | null crease `(n−2,0,1)` |
| measure | `√h d^{n−2}x` | area measure |
| period | `2π` (Euclidean/modular) | twist/closure's `2π` |
| coefficient | the action's | external |
| symmetry | horizon Killing field `ξ` | no Killing field |

## Holographic higher-derivative entropy

Wald entropy is the classical horizon entropy. It is not, in general, the entanglement entropy of the
horizon's degrees of freedom. In higher-derivative gravity, the holographic entanglement entropy is the
Dong–Camps functional:

```
S_EE = S_Wald + extrinsic-curvature corrections
```

The correction is quadratic in the extrinsic curvature of the bulk entangling surface, with a coefficient
that is a second derivative of the Lagrangian with respect to the Riemann tensor. For Gauss–Bonnet it
reduces to the Jacobson–Myers functional. The RT prescription is replaced by minimizing this functional,
not just the area.

This is the higher-derivative version of the entanglement note's coefficient caveat. The leading term is
gravitational and local on the surface; the corrections are the surface's extrinsic geometry. The Fold has
neither, so it cannot supply the functional. What survives is the codimension-two structure and the
exponent.

## The Fold's reading

The Fold's horizon is the null crease, a codimension-two locus with signature `(n−2,0,1)`. Wald entropy is
an integral over a codimension-two cross-section of that locus. The `2π` in Wald's formula is the same
`2π` as the Euclidean period and the modular period. The area exponent `n−2` is the Fold's exponent.

Those are the rhymes. The Fold has no Lagrangian, no Riemann tensor, no binormal, no Killing field, and no
`G`. It cannot distinguish `A/4G` from `f'(R)A/4G` or from the Gauss–Bonnet integral, because it has no
action to differentiate. Its `S ∝ A` is the statement that the entropy scales with the codimension-two
measure; the coefficient is the theory's. The universal log coefficient is a different kind of
coefficient: it is the A-type anomaly, not the Wald charge; see `the-fold-logarithm.md`.

| question | exact answer | Fold |
|---|---|---|
| why `A/4G`? | Einstein–Hilbert normalization | cannot say |
| why not `A/4G`? | higher-curvature density `s` | cannot say |
| why codimension two? | Noether charge of a Killing horizon | null crease |
| why `2π`? | Euclidean/modular period | twist/closure |
| why `S ∝ A`? | symmetric horizon, constant `s` | exponent `n−2` |

## Adjacent research

Wald's Noether-charge derivation is the origin of the general formula; Iyer and Wald extended it to
arbitrary perturbations and proposed the dynamical entropy; Jacobson, Kang, and Myers checked the
cross-section independence and the ambiguity freedom, and computed the higher-curvature examples; Visser
gave the Euclidean derivation and the surface-term form; Jacobson and Myers computed the Lovelock
entropy; Lovelock classified the higher-curvature Lagrangians that keep the field equations second order.
Dong and Camps gave the higher-derivative holographic functional. This note borrows the formula, the
Einstein–Hilbert and `f(R)` checks, the Gauss–Bonnet/Lovelock structure, and the first-law reading. It does
not derive the action, the Noether charge, or the holographic functional.

| topic | reference | link |
|---|---|---|
| Noether charge | Wald, *Black hole entropy is the Noether charge*, Phys. Rev. D 48 (1993) R3427 | [arXiv](https://arxiv.org/abs/gr-qc/9307038) |
| dynamical entropy | Iyer & Wald, *Some properties of the Noether charge and a proposal for dynamical black hole entropy*, Phys. Rev. D 50 (1994) 846 | [arXiv](https://arxiv.org/abs/gr-qc/9403028) |
| cross-section independence | Jacobson, Kang, Myers, *On black hole entropy*, Phys. Rev. D 49 (1994) 6587 | [arXiv](https://arxiv.org/abs/gr-qc/9312023) |
| Euclidean surface term | Visser, *Dirty black holes: entropy as a surface term*, Phys. Rev. D 48 (1993) 5697 | [arXiv](https://arxiv.org/abs/hep-th/9307194) |
| Lovelock entropy | Jacobson & Myers, *Entropy of Lovelock black holes*, Phys. Rev. Lett. 70 (1993) 3684 | [arXiv](https://arxiv.org/abs/hep-th/9305016) |
| Lovelock gravity | Lovelock, *The Einstein tensor and its generalizations*, J. Math. Phys. 12 (1971) 498 | [DOI](https://doi.org/10.1063/1.1665613) |
| higher-derivative holography | Dong, *Holographic entanglement entropy for general higher derivative gravity*, JHEP 1401 (2014) 044 | [arXiv](https://arxiv.org/abs/1310.5713) |
| higher-derivative holography | Camps, *Generalized entropy and higher derivative gravity*, JHEP 1403 (2014) 070 | [arXiv](https://arxiv.org/abs/1310.6659) |
| review | Wald, *The thermodynamics of black holes*, Living Rev. Rel. 4 (2001) 6 | [arXiv](https://arxiv.org/abs/gr-qc/9912119) |

## Checks

| check | value |
|---|---|
| Einstein–Hilbert derivative | `(1/16πG)(1/2)(g^{ac}g^{bd} − g^{ad}g^{bc})` |
| contraction | `−1/(8πG)` |
| Einstein–Hilbert entropy | `−2π(−1/(8πG))A = A/(4G)` |
| `f(R)` entropy | `f'(R)A/(4G)` |
| `f(R) = R + βR²` | `f' = 1 + 2βR` |
| Gauss–Bonnet entropy | `A/(4G) + (α/2G)∫√h R̃` |
| maximally symmetric `R̃` | `k(n−2)(n−3)/r_+²` |
| Gauss–Bonnet, `n = 5`, `k = 1` | `(A/4G)(1 + 12α/r_+²)` |
| Gauss–Bonnet, `n = 4` | topological; for a sphere `∫R̃ = 8π`, shift `4πα/G` |
| Lovelock entropy | `(1/4G)∑qα_q∫√h L_{q−1}(h)` |
| first law | `dM = (κ/2π)dS + Ω_H dJ + Φ_H dQ` |
| Schwarzschild check | `(κ/8πG)dA = dM` |
| Smarr | `M = κA/(4πG)` |

The derivative, contraction, and Einstein–Hilbert rows are exact arithmetic. The `f(R)`, Gauss–Bonnet, and
Lovelock rows are exact in the stated normalization. The `n = 5` row uses `(n−2)(n−3) = 6` and
`2αk(n−2)(n−3) = 12α`. The Schwarzschild and Smarr rows are the clock note's arithmetic.

## What this does and does not say

- It **does** state the Wald entropy `S_Wald = −2π∫(∂L/∂R_{abcd})ε_{ab}ε_{cd}` and its Noether-charge
  form `(2π/κ)∫Q[ξ]`.
- It **does** show that `A/4G` is the Einstein–Hilbert normalization, not a universal coefficient.
- It **does** give the exact `f(R)` result `f'(R)A/4G` and the Gauss–Bonnet/Lovelock integrals.
- It **does** show that the entropy is a codimension-two integral and that the area law is the
  constant-density, Einstein–Hilbert case.
- It **does** connect the `2π` to the Euclidean and modular periods and the first law to `κ/2π`.
- It **does** state the higher-derivative holographic correction (Dong–Camps) as the boundary of the
  Wald formula.
- It **does not** derive the action, the Riemann tensor, the binormal, or the coefficient from the Fold.
- It **does not** claim the Fold's `S ∝ A` is the Wald entropy; it is the exponent.
- It **does not** claim the Wald entropy is the microscopic entropy or the entanglement entropy.
- It **does not** solve the second law for dynamical black holes; the Iyer–Wald proposal leaves it open.
- It **does not** treat derivatives of the Riemann tensor in the action beyond the stated local formula;
  those require the full Iyer–Wald decomposition.
- It **does not** claim the Fold has a horizon Killing field; it has a homothety.

## The one sentence

**For any diffeomorphism-invariant gravitational action the horizon entropy is the Noether charge of the
horizon Killing field — an integral over the codimension-two cross-section of the Lagrangian's derivative
with respect to the Riemann tensor — so `A/4G` is only the Einstein–Hilbert case, `f(R)` gives `f'(R)A/4G`,
Gauss–Bonnet and Lovelock add intrinsic-curvature integrals, and the Fold supplies the codimension-two
locus and the exponent `n−2`, not the action or the coefficient.**

## Files

`the-fold-wald.md` (this note). The horizon's area and the Bekenstein–Hawking coefficient are in
`the-fold-area.md`; the wedge's entropy and the coefficient caveat are in `the-fold-entanglement.md`; the
holographic coefficient and the minimal surface are in `the-fold-holography.md`; the surface gravity and
the first law are in `the-fold-clock.md`; the null crease and the signature are in `the-fold-horizon.md`
and `the-fold-signature.md`; the accelerated observer is in `the-fold-unruh.md`; the universal log term
and the A-type anomaly are in `the-fold-logarithm.md`; the open-problem boundaries are in
`the-fold-problems.md`; the order is in `the-fold-creation.md`; the lookup is `the-fold-key.md`.
