# The Fold in engineering: geometry, similarity, and the limits of transfer

## The claim

Engineering is the discipline of the dimensional: a design has a length, a material, a load, a
tolerance, and a factor of safety. The Fold has one dimensionless number `k` and one determinant
`det g_k = kⁿ`. The question is what that number can carry into a design and what it cannot.

The answer is a zoning map. The Fold is an **exponent engine** and a **compatibility checker**, not a
constitutive theory. It supplies the geometry of similitude, the exponents of isometric scaling, the
closure of creases, the Nyquist bound, and the lattice restriction. It does not supply material laws,
dynamics, units, safety factors, or a computational model.

| zone | criterion | engineering examples |
|---|---|---|
| exact | the Fold's geometric object is the engineering object, re-described | geometric similitude; square–cube exponents; loop closure; Nyquist; crystallographic restriction; apparent contour |
| rhyme | the same shape or group appears, but the object or the law differs | deployable structures; metamaterials; analogue horizons; finite-size scaling; polarization devices; control observers |
| false friend | the same symbol or word, different object | `J` complex structure vs polar second moment; observer vs state estimator; horizon vs planning window; dimension vs physical dimension; entropy vs area law |

The exact anchors are geometric similitude, crease kinematics, sampling/Nyquist, the crystallographic
lattice restriction, and the apparent-contour geometry. Everything else in this note is labelled.

## 1. Geometric similitude: the exact core

The Fold's map is

```
g_k(P) = P₀ + k(P − P₀),          det g_k = kⁿ
```

For any two points,

```
|g_k(P) − g_k(Q)| = |k| |P − Q|
```

so lengths scale by `|k|`, `d`-volumes by `|k|^d`, and angles are unchanged. In `n` dimensions the
top volume scales by `kⁿ`, an `(n−1)`-surface by `k^{n−1}`, and a curvature by `1/|k|`. In three
dimensions: length `k`, area `k²`, volume `k³`, curvature `1/k`.

That is the exact content of geometric similitude: a homothety preserves shape and changes only size.
It is also the exact limit of the transfer. A physical model is geometrically similar when its
dimensions are in the ratio `k`; whether it is *dynamically* similar is a separate question, and the
Fold does not answer it.

### The exponent table

The Fold's `g_k` acts on space, not on time. A quantity's exponent therefore depends on how time is
scaled with length. Write the length degree as `p`; then:

| quantity | length degree `p` | `x → kx`, `t → t` | `x → kx`, `t → kt` | `x → kx`, `t → √k t` |
|---|---|---|---|---|
| length | 1 | `k` | `k` | `k` |
| area | 2 | `k²` | `k²` | `k²` |
| volume | 3 | `k³` | `k³` | `k³` |
| velocity | 1 | `k` | `1` | `√k` |
| acceleration | 1 | `k` | `1/k` | `1` |
| frequency | 0 | `1` | `1/k` | `1/√k` |
| curvature | −1 | `1/k` | `1/k` | `1/k` |

The three time columns are the three common choices: time held, time proportional to length (constant
velocity), and time proportional to `√length` (free fall under fixed gravity). The Fold fixes the
length column; the time column is a modelling choice, and a dimensionless group is what selects it.

### Buckingham Pi, and why geometry is not enough

Buckingham's theorem is exact: a physical relation among `n` dimensional variables with `r`
independent dimensions reduces to `n − r` dimensionless groups. Geometric similitude fixes the groups
that are pure length ratios. It does not fix the rest.

The ship model is the clean example. Resistance depends on `ρ, v, L, g, μ`: five variables, three
dimensions, two groups,

```
Re = ρvL/μ,          Fr = v/√(gL)
```

A model at length ratio `k` can match one group or the other, not both with the same fluid unless
`k = 1`:

| similarity | velocity ratio | `Re` ratio | `Fr` ratio |
|---|---|---|---|
| Froude | `√k` | `k^{3/2}` | `1` |
| Reynolds | `1/k` | `1` | `k^{−3/2}` |
| Mach | `1` | `k` | `k^{−1/2}` |

Froude scaling is used for ships because wave resistance dominates; Reynolds scaling for pipelines
because viscosity dominates; the choice is physical, not geometric. The Fold's `k` is the length
ratio in every row. It cannot choose the row.

This is the sharp boundary of the engineering transfer: **the Fold supplies the geometric ratio; the
dimensionless groups are the governing theory's.**

## 2. The square–cube law and the exponent engine

The oldest engineering consequence of `det g_k = kⁿ` is Galileo's square–cube law. Scale a body
isometrically by `k` at fixed density:

```
mass      ∝ k³
weight    ∝ k³
section   ∝ k²
stress    = weight / section ∝ k
```

A structure scaled up by `k` sees its self-weight stress rise by `k`; scaled down, the stress falls.
That is exact within the isometric model. It is not a failure criterion: yield, fatigue, creep,
fracture, and buckling are material and structural laws, and the safety factor is a decision under
uncertainty.

The same bookkeeping gives the exponents of common design quantities. The exponent is geometry; the
coefficient is external:

| quantity | isometric exponent | external factor |
|---|---|---|
| mass, weight | `k³` | density `ρ`, gravity `g` |
| load-bearing area | `k²` | — |
| self-weight stress | `k` | `ρg` |
| beam deflection (self-weight) | `k²` | `ρg/E` |
| beam natural frequency | `k^{−1}` | `√(E/ρ)` |
| Euler buckling load | `k²` | `E` |
| thermal diffusion time | `k²` | `1/α` |
| pendulum frequency | `k^{−1/2}` | `√g` |

For example, a geometrically similar beam under its own weight deflects as `δ ∝ L²`; its natural
frequency falls as `ω ∝ 1/L`; its Euler buckling load rises as `P_cr ∝ L²`. The Fold gives the
powers `2`, `−1`, `2`; the governing theory gives `ρg/E`, `√(E/ρ)`, `E`.

This is the most useful engineering face of the Fold. It is a **scaling calculator**, not a stress
analysis. It tells you how a quantity moves when the drawing is enlarged; it does not tell you
whether the enlarged drawing survives.

## 3. Crease kinematics and deployable structures

A crease pattern is a planar graph with mountain/valley labels; a folded state is an isometric map on
the facets, folding along the creases. Rigid foldability asks whether the facets move as rigid plates.
Akitaya, Demaine, Horiyama, Hull, Ku, and Tachi prove that deciding rigid foldability is weakly
NP-hard with all creases and strongly NP-hard with optional creases.

The Fold's exact contribution is the angular closure. Two folds at half-angle `α` compose to a
rotation by `2α`:

```
σ_{H₂} ∘ σ_{H₁} = R(2α)
```

A ring of `m` identical folds closes when `R(2α)^m = I`, i.e. `2mα ∈ 2πℤ`. The minimal closure is

```
R(2α)^m = I     ⇔     mα = π     ⇔     m = π/α
```

That is the Fold's closure law, and it is exact for coaxial rotations in the plane. In three
dimensions, a general rotation is a unit quaternion `q = cos α + sin α n`, and the closure condition
for a ring of folds is

```
q₁ q₂ … q_m = ±1
```

The scalar `m = π/α` is the case in which all axes coincide. A general crease pattern has
non-coaxial folds, and then the quaternion product, not the scalar angle sum, is the compatibility
condition. The Fold gives the planar bookkeeping; the full rigid-foldability problem is external.

The second exact contribution is the developed-length penalty. A line crossing a crease at slope `m`
becomes a V whose path exceeds its shadow by

```
L m² + O(m⁴)
```

and a pleated line of amplitude `a` and half-period `ℓ` has excess

```
2a²/ℓ² + O(a⁴)
```

per unit of shadow. These are the geometric cost of folding: the deployed surface needs more material
than its projection suggests. The formulas are asymptotic, exact at second order, and independent of
the material.

What this does **not** give is the crease pattern itself, the panel stiffness, the hinge stiffness,
bistability, deployment dynamics, fatigue at the hinges, or the stowed volume. The standard Miura-ori
is a one-degree-of-freedom deployable pattern; the Fold's closure describes the angular bookkeeping
of a ring of folds, not the Miura map. The metamaterial literature supplies the kinematics and the energy
landscape; the Fold supplies the closure condition and the length penalty.

## 4. Sampling, sensing, and lattices

The observer is a pair `(d, w)`: a form degree and a window. The closure is a number `m = π/α`. The
discrete dual of the window is a sampling lattice with `N` samples per turn. An `m`-fold pattern has
angular frequency `m`; its finest harmonic is `cos(mθ)`.

A probe with `N` samples per turn resolves the pattern exactly when

```
N > 2m          equivalently          a < πR/m
```

where `a = 2πR/N` is the sample spacing on a circle of radius `R`. At `N = 2m` the harmonic sits at
Nyquist and the samples alternate; the strict inequality is the condition for resolving it as a
wave. The Gaussian window attenuates the `m`-th harmonic by

```
e^{−m²σ²/2},          σ = w/R
```

and at the half-sector width `σ = π/m` the attenuation is

```
e^{−π²/2} = 7.1919e−3
```

so the window width and the sample spacing share the same cutoff `πR/m`. The coarser of the two sets
the resolution.

There are two lattices in the sentence, and engineering design must not conflate them:

- the **object's** lattice, described by the closure `m`; a periodic crystal admits only
  `2cos(2π/n) ∈ ℤ`, hence `n ∈ {1, 2, 3, 4, 6}`;
- the **probe's** lattice, described by `N`; it is not crystallographically restricted.

A fivefold pattern has no periodic crystal, but a probe with `N > 10` samples its fivefold diffraction
without aliasing. The restriction is on the object, not on the sensor.

Engineering instances are direct: a rotating sensor ring with `N` samples per turn; a modal sensor
array for an `m`-fold symmetric structure; an image of a patterned surface; a spherical sampling
scheme. On a sphere the area element is `R² sin θ dθ dφ`, so uniform angle is not uniform area: equal
`θ` octants have area ratio `1 + √2`. Area-fair sampling uses uniform `cos θ`, not uniform `θ`.

Shannon's theorem is exact: a signal band-limited to `m` is determined by samples spaced finer than
the half-period. What the theorem does not supply is noise, SNR, estimator design, calibration, or
sensor dynamics. Nyquist is a necessary resolution condition, not a reconstruction algorithm in a
noisy instrument.

## 5. Visibility, occlusion, and the horizon

The fold's apparent contour is the image of the critical set of the projection. For a smooth surface,
the apparent contour is where the view ray is tangent; the projection rank drops there. For the sheet
fold `F(x, y) = (x, |y|)`, the singular set is the crease `y = 0`, and the image is the boundary of
the half-plane. The exact shared object is the **rank drop of the projection**, not the surface
itself: a sphere's silhouette is a projection artifact, while the sheet fold's crease is a crease of
the surface.

This is the geometry behind occlusion boundaries, silhouette extraction, and range sensing. The back
of a surface is the sign of its normal; a quadratic measurement forgets the sign, and the crease is
the only place the two sides meet. An engineering visibility algorithm can compute the boundary; it
does not thereby see both faces at once.

The horizon is the null analogue of a visibility boundary. A causal window is the retarded propagator,
whose support is the future light cone; the horizon is the boundary of the observer's causal past. The
null crease has induced form `(n−2, 0, 1)`, and the horizon's temperature is set by the surface
gravity,

```
T = ħκ/(2πck_B),          κ = c⁴/(4GM)
```

The Fold's homothetic family gives `T ∝ 1/k`; the coefficient is the gravitational theory's. An
acoustic or optical analogue horizon has the same form `T ∝ κ`, with its own `κ`; the analogue
gravity literature supplies the field equation, and the Fold's `T ∝ 1/k` is the homothetic-family
exponent.

A rendering horizon, a surveyor's horizon, and a planning horizon are **not** null surfaces. The first
is a visibility boundary, the second a reference plane, the third a time window. They share the word
and the idea of a boundary; they do not share the null signature.

## 6. Polarization and the letter J

The Fold's twist is a complex structure:

```
J² = −I,          det J = 1,          Pf(J) = 1
```

A quarter turn is `J`; two folds at angle `α` give `R(2α)`. The same group appears in polarization
optics, but on a different space. A half-wave plate acts on the Poincaré sphere as a reflection; two
such reflections compose to a rotation by twice the angle between their axes. That is the Fold's
`σ_{H₂} ∘ σ_{H₁} = R(2α)`, with `α` the angle between the reflection axes. The physical plate angle
is a coordinate on the representation, not the Fold's spatial angle.

The quarter-wave plate is a 90° rotation on the Poincaré sphere, not the matrix `J` on the spatial
plane. Its Jones matrix in principal axes is, up to global phase,

```
Q = diag(1, i),          Q² = diag(1, −1) ≠ −I
```

so two quarter-wave plates make a half-wave plate, not `−I`. The paper's `diag(1, i)` is exactly this
retarder; it *instantiates* the quarter-turn and the algebra `i² = −1`, not the Fold's matrix. The
group is the same; the space is not.

The false friend is the letter `J` itself. In torsion of a shaft, the angle of twist is

```
φ = TL/(GJ)
```

where `J` is the polar second moment of area, with units `L⁴`. The Fold's `J` is a dimensionless
complex structure with `J² = −I`. Same letter, different object, different units, different algebra.
A design note that reads `J² = −I` as a torsional stiffness has made the false-friend error.

## 7. Observers, control, and estimation

The Fold's observer is a measurement aperture `(d, w)`: `d` selects the form degree, `w` the smallest
resolvable feature. It has no state, no dynamics, no feedback, and no gain.

A control observer is a dynamical estimator. A Luenberger observer has

```
x̂̇ = A x̂ + B u + L(y − C x̂),          ė = (A − LC)e
```

and observability is the rank condition

```
rank [C; CA; …; CA^{n−1}] = n
```

The two objects share the word and the measurement setting, not the object. The Fold's observer is a
projection or an aperture; the control observer is a dynamical system with a stability condition. The Fold has no `A`, `B`, `C`, or `L`, so
it has no observability, no Kalman gain, and no error dynamics.

The same caution applies to "rank." The Fold's rank drop is `det g_k = 0` at `k = 0`; the control
rank is the rank of the observability matrix. Both are linear algebra, but the matrices are
different.

What does transfer is the measurement geometry: a `d`-dimensional probe measures a `d`-form, and a
window `w` sets the smallest feature it can resolve. That is a sensor-model statement, not a
controller design.

## 8. Entropy, information, and the area law

Three entropies meet in engineering, and they are not the same object:

- **thermodynamic:** `dS = δQ_rev/T`, an extensive state function;
- **information:** `H = −Σ p ln p`, a measure of uncertainty;
- **entanglement:** `S = −Tr ρ_A ln ρ_A`, the von Neumann entropy of a reduced state.

For a Gibbs state `ρ = e^{−βH}/Z`, the von Neumann entropy is exactly the thermodynamic entropy up to
`k_B`:

```
S_vN = −Tr ρ ln ρ = β⟨H⟩ + ln Z = S_th/k_B
```

That is an exact bridge, and it is the reason the same formula appears in both fields. The area law
used in this thread is a further statement: for a region of size `R` with UV cutoff `ε`,

```
S_EE ~ A/ε^{n−2}
```

so in four dimensions `S_EE ~ R²/ε²`. The exponent `n−2` is the horizon's area exponent and the
mode-count exponent. The coefficient is the cutoff's and the field content's, not the Fold's.

The contrast with engineering thermodynamics is sharp: for an ordinary bulk system, a thermodynamic
entropy is extensive, `S_th ∝ V ∝ k³`; the entanglement entropy is an area law, `S_EE ∝ A ∝ k²`; the
Bekenstein–Hawking entropy is also `S_BH = A/4ℓ_P² ∝ k²`. The exponents differ, so the area law is not thermodynamic
extensivity. The Fold supplies the `A` scaling, not the state, the temperature, or the `1/4ℓ_P²`.

## 9. Logs, finite-size scaling, and false periodicity

The one term in the entanglement entropy's UV expansion that is not a power of the cutoff is the
logarithm. For a smooth sphere in even spacetime dimension `n`,

```
S_EE = … + g_0 ln(ε/R) + …,          g_0 = (−1)^{n/2} 4a_n
```

with `g_0 = −1/3, 1/90, −1/756, 23/113400` at `n = 2, 4, 6, 8` for one scalar. The coefficient of
`ln(R/ε)` is `c/3` in 2D and `−4a` in 4D. In odd dimensions the anomaly vanishes and there is no log.
The log is universal in the sense that the cutoff does not set it; it is not theory-independent.

Engineering meets logs in a different limit. Finite-size scaling writes a quantity near a critical
point as

```
Q(L) = Q_∞ + a L^{−ω} + b L^{−ω₂} + …
```

A log appears when a correction exponent is marginal, `ω = 0` — the `ω → 0` limit of `L^{−ω}` — or in
two dimensions at criticality, `Q ∼ ln L`. That is an infrared finite-size correction. The Fold's log
is an ultraviolet entanglement anomaly. Both are logs; the limits and the coefficients are different.

The false friends are easy to name:

- a **log-periodic antenna** is self-similar under a shift in `ln f`; it is a geometry, not a log
  correction;
- **`1/f` noise** is a power law in frequency, not a logarithmic term;
- a **log-normal** distribution is a distribution of a logarithm, not a log in an asymptotic
  expansion.

A log in a formula is a shape. The coefficient and the limit are the theory's.

## 10. What the Fold does not supply

The boundary is easiest to state as a list. The Fold does not supply:

- material laws: elasticity, plasticity, creep, fatigue, fracture, corrosion;
- dynamics: inertia, damping, waves, stability, control;
- units and dimensionful constants;
- safety factors, codes, tolerances, reliability, cost;
- boundary conditions and loads;
- manufacturing, assembly, and inspection;
- a computational model: no PDE, no mesh, no constitutive update, no solver;
- a design optimization method.

It does supply:

- the geometric exponents of similitude and the square–cube law;
- the beam, buckling, frequency, and diffusion exponents, with the coefficients left external;
- the crease closure `m = π/α` and the developed-length penalty;
- the Nyquist bound and the two-lattice distinction;
- the apparent-contour and occlusion geometry;
- a vocabulary for scale separation and for the limits of a model.

A practical workflow follows from the two lists:

1. Fix the geometry and the length ratio `k`.
2. List the dimensionless groups; decide which are invariant under `k` and which need a time or
   velocity scaling.
3. Use the Fold's exponents for the geometric quantities; use the governing theory for the
   coefficients.
4. Check closure, sampling, and lattice conditions for compatibility and resolution.
5. Do not use `k` as a safety factor, the area law as a thermodynamic potential, or the observer as a
   controller.

## References

| topic | reference | link |
|---|---|---|
| dimensional analysis | Buckingham, *On physically similar systems*, Phys. Rev. 4 (1914), 345–376 | [DOI](https://doi.org/10.1103/PhysRev.4.345) |
| square–cube law | Galileo, *Discorsi* (1638); *Square–cube law* | [Wikipedia](https://en.wikipedia.org/wiki/Square%E2%80%93cube_law) |
| geometric folding | Demaine and O'Rourke, *Geometric Folding Algorithms*, CUP 2007 | — |
| rigid foldability | Akitaya, Demaine, Horiyama, Hull, Ku, Tachi, *Rigid foldability is NP-hard*, J. Comput. Geom. 11 (2020), 93–124 | [arXiv](https://arxiv.org/abs/1812.01160) |
| sampling | Nyquist, Trans. AIEE 47 (1928), 617–644; Shannon, Proc. IRE 37 (1949), 10–21 | — |
| time–bandwidth | Gabor, *Theory of communication*, J. IEE 93 (1946), 429–457 | [DOI](https://doi.org/10.1049/ji-3-2.1946.0074) |
| origami metamaterials | Silverberg et al., *Origami structures with a critical transition to bistability*, Nat. Mater. 13 (2014), 389–393 | [DOI](https://doi.org/10.1038/nmat3890) |
| analogue gravity | Barceló, Liberati, Visser, *Analogue gravity*, Living Rev. Relativ. 14 (2011), 3 | [arXiv](https://arxiv.org/abs/gr-qc/0505065) |
| finite-size scaling | Cardy, *Scaling and Renormalization in Statistical Physics*, CUP 1996 | — |
| materials selection | Ashby, *Materials Selection in Mechanical Design*, 5th ed., Butterworth-Heinemann 2017 | — |
| torsion | *Torsion (mechanics)* | [Wikipedia](https://en.wikipedia.org/wiki/Torsion_%28mechanics%29) |
| observability | *Observability* | [Wikipedia](https://en.wikipedia.org/wiki/Observability) |
| log-periodic antenna | *Log-periodic antenna* | [Wikipedia](https://en.wikipedia.org/wiki/Log-periodic_antenna) |

## Checks

| check | value |
|---|---|
| `det g_k = kⁿ`, `k=2`, `n=2/3/4` | `4 / 8 / 16` |
| square–cube, `k=2` | mass `8`, area `4`, stress `2` |
| Froude, `k=4` | velocity `2`, `Re` ratio `8` |
| Reynolds, `k=4` | velocity `0.25`, `Fr` ratio `0.125` |
| V excess, `m=0.1`, `L=1` | `0.00997512` vs `L m²=0.01` |
| pleat excess, `a/ℓ=0.1` | `0.0198039` vs `2a²/ℓ²=0.02` |
| Nyquist, `m=5`, `N=10/11` | `5`, not resolved / `5`, resolved |
| Gaussian half-sector | `e^{−π²/2}=7.1919e−3` |
| crystallographic `2cos(2π/n)` | integer only `n=2,3,4,6` |
| log coefficients, `n=2/4/6/8` | `−1/3 / 1/90 / −1/756 / 23/113400` |
| beam exponents, `k=2` | deflection `4`, frequency `0.5`, buckling `4` |
| `J²` and `Pf(J)` | `−I`, `1` |
| Jones matrices | `diag(1,i)²=diag(1,−1)`, not `−I` |

The determinant, square–cube, Froude/Reynolds, and excess rows are arithmetic confirmations of the
formulas. The Nyquist and crystallographic rows restate the sampling note's exact conditions. The log
row restates the logarithm note's coefficient table. The last two rows separate the Fold's `J` from
the Jones matrices; they are the check that the rhyme is not mistaken for an identity.

## What this does and does not say

- It **does** give exact geometric similitude: lengths `k`, areas `k²`, volumes `k³`, angles fixed,
  curvature `1/k`.
- It **does** give the square–cube law and the engineering exponents for stress, deflection,
  frequency, buckling, and diffusion, with the coefficients left to the material.
- It **does** give the crease closure `m = π/α` for coaxial folds, the quaternion condition for
  general folds, and the developed-length penalties `L m²` and `2a²/ℓ²`.
- It **does** give the Nyquist condition `N > 2m`, the half-sector cutoff `πR/m`, and the
  crystallographic restriction `n ∈ {1,2,3,4,6}` for the object's periodic lattice.
- It **does** give the apparent-contour and occlusion geometry, and the horizon as a null crease.
- It **does not** supply material laws, dynamics, units, safety factors, tolerances, cost, or a
  computational model.
- It **does not** make geometric similitude into dynamic similitude; Reynolds, Froude, and Mach
  matching are external constraints.
- It **does not** identify the quarter-wave plate's Jones matrix with `J`; the group is the same, the
  space is not.
- It **does not** identify the area law with thermodynamic extensivity; `S_EE ∝ A` and `S_th ∝ V` are
  different exponents.
- It **does not** claim the log coefficient is theory-independent; it is universal in the cutoff, not
  across theories.
- It **does not** turn the Fold into a design method, a metamaterial theory, or a controller.

## The one sentence

**The Fold supplies geometry and sampling — the exponents of similitude, the square–cube law, crease
closure, the Nyquist bound, the lattice restriction, and the visibility boundary — while material
laws, dynamics, units, and safety factors remain the engineer's.**

## Files

`the-fold-engineering.md` (this note). The folded line, the V, the pleats, and rigid foldability are
in `the-fold-afar.md`; the closure `m = π/α` and the crystallographic restriction are in
`the-fold-closure.md`; the Nyquist condition and the two lattices are in `the-fold-sampling.md`; the
observer `(d, w)` is in `the-fold-observer.md`; the entropy's coefficient caveat is in
`the-fold-entanglement.md`; the universal logarithm is in `the-fold-logarithm.md`; the
exact/rhyme/false-friend vocabulary is in `the-fold-problems.md`; the lookup is `the-fold-key.md`.
