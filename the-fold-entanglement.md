# The wedge's entropy: the observer's causal window and the area law

## The claim

The observer note gave the probe a causal window. The Unruh note showed that the window's flat-space
model is the Rindler wedge. This note asks what the observer loses by having a window at all. The answer
is the wedge's **entanglement entropy**: trace out the other wedge, and the Minkowski vacuum becomes a
thermal state whose entropy scales with the area of the null crease.

The exact content is the modular Hamiltonian and the area law's exponent. The wedge's reduced state is

```
ρ_W = e^{−2πK}/Z
```

where `K` is the boost generator. The `2π` is the same modular period as the Unruh clock. The entropy's
leading UV behavior is

```
S_EE = −Tr(ρ_W ln ρ_W) = c A/ε^{n−2} + subleading
```

The exponent `n−2` is the horizon's area exponent and the mode-count exponent. The coefficient `c` is the
UV cutoff's and the field content's, not the Fold's. The Fold's `k` is a homothety, not the modular boost,
so the Fold does not derive the area law. It gives the exponent; the coefficient is external.

Here "modular" is the Tomita–Takesaki modular operator, not the theta modular factor of
`the-fold-theta.md`.

## The wedge and the modular Hamiltonian

The Rindler wedge is

```
W = {x > |t|},        W′ = {x < −|t|}
```

with the boost Killing vector `ξ = a(x ∂_t + t ∂_x)`. The modular flow `σ_s` is the boost with rapidity
`2πs`, and the Bisognano–Wichmann theorem says the Minkowski vacuum restricted to `W` is the thermal state

```
ρ_W = e^{−2πK}/Z,        K = ∫_W x T_{00} d^{n−1}x
```

in `c = 1` units. The generator `K` is the unit-surface-gravity boost; the physical boost is `aK`, and the
Unruh temperature is `a/(2π)`. The modular Hamiltonian is `H_mod = 2πK`; its `2π` is the period. The KMS
condition is

```
⟨A B(s)⟩ = ⟨B(s + i2π) A⟩
```

in the modular flow parameter, so the modular temperature is `1/(2π)` in boost units. The Unruh
temperature is the same statement in proper time: `T = ħ a/(2πck_B)`. See `the-fold-unruh.md`.

| object | formula | role |
|---|---|---|
| wedge | `x > \|t\|` | the causal window |
| physical boost | `ξ = a(x ∂_t + t ∂_x)` | proper acceleration `a` |
| modular generator | `K = ∫_W x T_{00} d^{n−1}x` | unit-surface-gravity boost |
| modular Hamiltonian | `H_mod = 2πK` | `ρ_W = e^{−H_mod}/Z` |
| KMS period | `2π` | thermal circle |
| Unruh temperature | `ħ a/(2πck_B)` | proper-time reading |

The entropy of the thermal state is exact:

```
S_EE = −Tr(ρ_W ln ρ_W) = 2π⟨K⟩ + ln Z
```

This is the thermodynamic entropy of the wedge; the area law is its UV behavior.

## The entanglement entropy and the area law

Trace out `W′` and the entropy diverges with the UV cutoff:

```
S_EE = c A/ε^{n−2} + subleading
```

where `A` is the area of the entangling surface (the null crease between `W` and `W′`) and `ε` is the
short-distance cutoff. The divergence is the price of the continuum: the number of modes straddling the
surface is infinite without a cutoff. Callan and Wilczek state it directly: the entropy diverges in
quantum field theory in the absence of an ultraviolet cutoff.

| n (spacetime) | entangling surface | `A` | `S_EE` |
|---|---|---|---|
| 2 | point | constant | `~ log(R/ε)` |
| 3 | line | `~ R` | `~ R/ε` |
| 4 | surface | `~ R²` | `~ R²/ε²` |
| 5 | 3-surface | `~ R³` | `~ R³/ε³` |

In 4D the area law is `S_EE ~ R²/ε²`, the same exponent as the horizon's `A ∝ R²`. The surface's area
measure is the horizon's measure: on a sphere, uniform angle is not uniform area, and the octant ratio is
`1 + √2`. The entanglement entropy is proportional to the area, so the fair measure is the area measure,
not the coordinate angle. See `the-fold-area.md`.

The coefficient `c` is not universal. It depends on the number of fields, their spin and mass, and the
regularization. The scaling `A/ε^{n−2}` is the generic behavior of local fields; the number is the
cutoff's.

## The exponent and the mode count

The area law counts the modes straddling the surface. With `ε = R/m`, a sphere of radius `R` has

```
A/ε² = 4πR²/(R/m)² = 4πm²
```

and the independent modes on `S²` of degree at most `m` number `(m+1)²`. Their ratio approaches `4π`:

| `m` | `(m+1)²` | `4πm²` | ratio |
|---|---|---|---|
| 10 | 121 | 1256.6 | 10.385 |
| 100 | 10201 | 125663.7 | 12.319 |
| 1000 | 1002001 | 12566371 | 12.541 |
| `→∞` | `~m²` | `~4πm²` | `4π` |

The entropy is not the logarithm of the total mode count; each mode straddling the surface contributes
`O(1)`, so `S_EE ~ N_modes ~ A/ε²`. The area note's `N_A ~ m²` is this count. The exponent is the same;
the coefficient is the only free parameter.

## The Fold's reading: the observer's blindness

The `d = n−1` surface observer sees half the sky, `Ω = 2π`. The wedge is that observer's causal window,
and the other wedge is what the window cannot see. The entanglement entropy is the information the
observer loses by tracing out the other side. In that exact sense, the observer's blindness is the
entropy.

The window `w` is the observer's resolution; the area law's `ε` is the UV cutoff. The identification
`w ~ ε` is a reading: the observer cannot resolve below `w`, and the area law counts modes down to `ε`.
The Fold's `w` is not the Planck length, and the area law's coefficient is external.

The Fold's `k` is a homothety, not a boost. The modular flow is the boost; the Fold has no such Killing
vector. The shared objects are the null crease, the area measure, the `2π` modular period, and the causal
window. They are rhymes, not a derivation of the wedge's thermality or the area law.

| reading | exact object | Fold's version |
|---|---|---|
| entangling surface | null crease, area `A` | horizon's null crease |
| modular flow | boost, period `2π` | twist/closure's `2π` |
| UV cutoff | `ε` | window `w` |
| entropy | `S_EE ~ A/ε^{n−2}` | `S ∝ A` (exponent only) |

## The coefficient: `1/4` is not the wedge's coefficient

The Bekenstein–Hawking entropy is

```
S_BH = A/(4ℓ_P²)
```

and the wedge's entanglement entropy is

```
S_EE = c A/ε²        (4D)
```

They share the area scaling; they do not share the coefficient. The `1/4` is the gravitational coupling
in Planck units; `c` is the matter-sector coefficient. Setting `ε = ℓ_P` and `c = 1/4` makes them equal,
but that is a choice, not a derivation.

The **species problem** is the sharpest way to see the difference: `c` scales with the number of fields,
while `1/4G` does not. If one tries to identify the two, adding a species changes the entanglement
entropy but not Newton's constant. In induced gravity, `1/4G` can be generated by the entanglement
entropy of matter, but that is a model with a specific cutoff and field content, not a Fold theorem.

The Fold's contribution is the exponent: `S ∝ A`. The coefficient `1/4ℓ_P²` is external, exactly as in
`the-fold-area.md`. The one case where the coefficient is fixed is holographic; see
`the-fold-holography.md`.

## Adjacent research

The modular Hamiltonian is the Tomita–Takesaki operator; Bisognano and Wichmann identified it with the
boost for the Rindler wedge. Bombelli, Koul, Lee, and Sorkin found the area law for the entanglement
entropy of a scalar field; Srednicki confirmed it numerically for a free field; Callan and Wilczek gave
the geometric-entropy calculation and its UV divergence; Holzhey, Larsen, and Wilczek found the
logarithmic case in two dimensions; Ryu and Takayanagi gave the holographic area law. Jacobson used the
area law and the Unruh temperature to read the Einstein equation as an equation of state. This note
borrows the modular Hamiltonian, the area-law scaling, and the coefficient caveat. It does not derive
the area law, the `1/4`, or the Einstein equation.

| topic | reference | link |
|---|---|---|
| modular / KMS | Bisognano & Wichmann, *On the duality condition for quantum fields*, J. Math. Phys. 17 (1976) 303 | [DOI](https://doi.org/10.1063/1.522898) |
| entanglement area law | Bombelli, Koul, Lee, Sorkin, *Quantum source of entropy for black holes*, Phys. Rev. D 34 (1986) 373 | [DOI](https://doi.org/10.1103/PhysRevD.34.373) |
| free-field area law | Srednicki, *Entropy and area*, Phys. Rev. Lett. 71 (1993) 666 | [arXiv](https://arxiv.org/abs/hep-th/9303048) |
| geometric entropy | Callan & Wilczek, *On geometric entropy*, Phys. Lett. B333 (1994) 55 | [arXiv](https://arxiv.org/abs/hep-th/9401072) |
| CFT logarithm | Holzhey, Larsen, Wilczek, *Geometric and renormalized entropy in conformal field theory*, Nucl. Phys. B424 (1994) 443 | [arXiv](https://arxiv.org/abs/hep-th/9403108) |
| holographic area law | Ryu & Takayanagi, *Holographic derivation of entanglement entropy from AdS/CFT*, Phys. Rev. Lett. 96 (2006) 181602 | [arXiv](https://arxiv.org/abs/hep-th/0603001) |
| induced gravity | Jacobson, *Black hole entropy and induced gravity*, arXiv:gr-qc/9404039 | [arXiv](https://arxiv.org/abs/gr-qc/9404039) |
| entanglement equilibrium | Jacobson, *Entanglement equilibrium and the Einstein equation*, Phys. Rev. Lett. 116 (2016) 201101 | [arXiv](https://arxiv.org/abs/1505.04753) |

## Checks

| check | value |
|---|---|
| modular period | `2π` |
| modular Hamiltonian | `H_mod = 2πK`, `K = ∫_W x T_{00}` |
| entropy identity | `S_EE = 2π⟨K⟩ + ln Z` |
| area-law exponent, `n = 2,3,4,5` | `0, 1, 2, 3` (with a log at `n = 2`) |
| 4D area law | `S_EE ~ R²/ε²` |
| mode count, `m = 10` | `(m+1)² = 121`, `4πm² = 1256.6`, ratio `10.385` |
| mode count, `m = 100` | ratio `12.319` |
| mode-count limit | `4π = 12.566` |
| area measure | octant ratio `1 + √2 = 2.414214` |
| `S_BH` vs `S_EE` | same `A` scaling, different coefficients |

The modular period and the entropy identity are exact. The area-law rows are scaling statements, not
numerical evaluations of a specific field's coefficient. The mode-count rows are exact integer counts and
their `4π` limit.

## What this does and does not say

- It **does** identify the observer's causal window with the Rindler wedge and its reduced state with the
  thermal state `ρ_W = e^{−2πK}/Z`.
- It **does** give the modular Hamiltonian `H_mod = 2πK`, the KMS period `2π`, and the entropy identity
  `S_EE = 2π⟨K⟩ + ln Z`.
- It **does** state the area law `S_EE ~ A/ε^{n−2}` and show that its exponent `n−2` is the horizon's area
  exponent and the mode-count exponent.
- It **does** show that the entropy counts modes straddling the surface, one `O(1)` per mode, and that
  the mode count approaches `4πm²` for a sphere.
- It **does** separate the wedge's coefficient `c` from the Bekenstein–Hawking `1/4`; they share the
  scaling, not the number.
- It **does** identify the observer's blindness — tracing out the other wedge — as the entropy.
- It **does not** derive the area law, the coefficient `c`, or the `1/4` from the Fold.
- It **does not** claim the Fold's `k` is the modular boost; `k` is a homothety.
- It **does not** claim the wedge entropy is the black hole entropy; the coefficients differ.
- It **does not** solve the species problem; it states it as the boundary of the identification.
- It **does not** treat interacting fields, the universal log term, or the holographic case beyond the
  citation.

## The one sentence

**The observer's causal window is a Rindler wedge; the Minkowski vacuum restricted to it is thermal with
modular Hamiltonian the boost and period `2π`, and its entanglement entropy scales as the area of the
null crease at the same exponent as the horizon's mode count — but the coefficient is the cutoff's, not
the Fold's.**

## Files

`the-fold-entanglement.md` (this note). The Rindler wedge and the Unruh period are in
`the-fold-unruh.md`; the area measure and the mode count are in `the-fold-area.md`; the observer's
`(d, w)` and the causal window are in `the-fold-observer.md` and `the-fold-sampling.md`; the horizon's
clock is in `the-fold-clock.md`; the null crease is in `the-fold-horizon.md`; the open-problem boundaries
are in `the-fold-problems.md`; the theta modular factor (a different "modular") is in
`the-fold-theta.md`; the order is in `the-fold-creation.md`; the lookup is `the-fold-key.md`.
