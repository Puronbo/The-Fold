# The Fold

**Scale, twist, collapse — and what is left at the centre.**

Scaling about a datum is the one-parameter family `g_k(P) = P₀ + k(P − P₀)`. Everything in this
paper follows from one determinant, `det(g_k) = kⁿ`: heights scale like `k`, areas like `k²`,
volumes like `k³`. A real `k` changes size, an imaginary one twists, and a twist is the product of
two folds.

**The four zones.** Every claim in this corpus is labelled by how it sits against the mathematics:

- **exact** — the Fold's object is the problem's object, re-described; the statement can be checked.
- **reformulation** — the problem becomes a statement about the Fold, with nothing proved.
- **rhyme** — the same shape appears, but the objects are different.
- **false friend** — the same symbol appears, and it means something else.

A rhyme is a place to look, never a proof; a rhyme written as a proof is the one error that matters.
The full statement is in `the-fold-problems.md`, and the engineering instance is in
`the-fold-engineering.md`.

**Start here:** `the-fold-key.md` — the master key. Give it a value of `k`; it returns the stage,
the operation, what appears, what survives, and the note that proves it.

**Formal core:** `lake build` compiles a dependency-free Lean 4 library in `Fold/` — the fold as an
involution, its fixed set and quotient, the observer as a cut, the scale action, the cap/puncture
ledger, the calendar arithmetic, the wheel's closure, and four finite counterexamples. The build
proves the skeleton, not the rhymes; the map is `the-fold-lean.md`.

**Matter reading:** matter is the zero at a scale — stages 0–1 of the chain. In the homothetic
family `h ∝ k`, `M ∝ h`, `A ∝ h²`, `V ∝ h³`, `S ∝ h²`, `T ∝ 1/h`, while the horizon ratio `k*`
stays constant. Shape is the aperture `θ`; turn is `arg k`. A `d`-dimensional observer measures
`h^{p−d}` — scalar, derivative, flux, density for `d = 0, 1, 2, 3`. See `the-fold-matter.md`.

**Observer:** the observer is a pair `(d, w)` — dimension and window. `d` selects the form
(`h^{p−d}`) and `w` selects the smallest resolvable feature (the Gaussian window, with semigroup
`G_{w1} * G_{w2} = G_{√(w1²+w2²)}`). The paper's table is the `w → 0` slice; "from afar" is `w` larger
than the fold's height. See `the-fold-observer.md`.

**Sampling and closure:** the observer's window has a discrete dual. An `m`-fold closure has angular
frequency `m`, and a probe with `N` samples per turn resolves it only when `N > 2m`; the Gaussian window
and the sample spacing share the half-sector cutoff `πR/m`. The crystallographic restriction limits the
object's periodic lattice, not the probe's. The horizon is the `d = n−1` observer whose window is the
causal cone. See `the-fold-sampling.md`.

**Horizon measure:** a null surface has no invariant volume — the null normal is tangent and can be
rescaled, and the induced metric is degenerate — but each cross-section has an invariant area. The area
exponent `n−2` is the mode-count exponent: in 4D, `A ∝ r²` and the modes grow as `m²`, so the pixel
count and the angular resolution are dual. Uniform angle is area-fair only on a circle; on `S²` equal `θ`
octants have ratio `1 + √2`, and the exterior projection adds a `cos α` Jacobian vanishing at the limb.
The horizon saturates the static Bekenstein bound: `S = A/4ℓ_P² = 4πGM²/(ħc)`. See `the-fold-area.md`.

**Horizon clock:** the affine parameter along a null generator is gauge; the Killing time, normalized at
infinity, is not. Its rate is the surface gravity `κ = c⁴/(4GM)`, and the Euclidean period `2πc/κ` gives
`T = ħκ/(2πck_B) = ħc³/(8πGMk_B)`. The Fold's `T ∝ 1/k` is the exponent; the coefficient is external. The
static horizon closes the clock to the area: `M = κA/(4πG)` and `dM = κ dA/(8πG)`. See
`the-fold-clock.md`.

**Observer thermometer:** an accelerated observer in the Minkowski vacuum sees a thermal bath at
`T = ħa/(2πck_B)`, with Euclidean period `2πc/a`. The detector's detailed balance is `e^{−E/(k_B T)}`,
and at `E = k_B T` the ratio is `e^{−1} = 0.367879`. The local Unruh temperature and the Tolman-redshifted
Hawking temperature agree only near the horizon: `T_U = T_H(r_s/r)²/√f` versus `T_H/√f`. The Fold's `k`
is a homothety, not a boost, so the shared object is the null crease and the `2π`, not a derivation. See
`the-fold-unruh.md`.

**Wedge entropy:** the observer's causal window is a Rindler wedge. The Minkowski vacuum restricted to it
is thermal, `ρ_W = e^{−2πK}/Z`, with `K` the unit-surface-gravity boost and modular period `2π`. The
entanglement entropy is an area law, `S_EE ~ A/ε^{n−2}`; in 4D, `S_EE ~ R²/ε²`. The exponent `n−2` is the
horizon's area exponent and the mode-count exponent. The coefficient is the cutoff's and the field
content's, not the Fold's: the `1/4` in `S_BH = A/4ℓ_P²` and the wedge's `c` share the scaling but not
the number, and the species problem is why. See `the-fold-entanglement.md`.

**Holographic coefficient:** in the AdS/CFT correspondence, the wedge's entropy is
`S_EE = A_min/(4G_N)`, the area of the minimal bulk surface divided by four times the bulk Newton
constant. This is the one case in this thread where the coefficient is exactly the Bekenstein–Hawking
`1/4G_N`; the boundary's species count `~N_c²` is tied to the bulk's `ℓ^{d−1}/G_N`. The Fold's `S ∝ A`
supplies the exponent, but the bulk geometry and the coefficient are the holographic theory's. See
`the-fold-holography.md`.

**General coefficient:** for an arbitrary diffeomorphism-invariant gravitational action, the horizon
entropy is the Noether charge of the horizon Killing field,
`S_Wald = (2π/κ)∫Q[ξ] = −2π∫(∂L/∂R_{abcd})ε_{ab}ε_{cd}√h`. It is still a codimension-two cross-section
integral, so the Fold's exponent survives; the coefficient is the action's. `A/4G` is only
Einstein–Hilbert; `f(R)` gives `f'(R)A/4G`; Gauss–Bonnet and Lovelock add intrinsic-curvature integrals.
See `the-fold-wald.md`.

**Universal logarithm:** the one term in the entanglement entropy's UV expansion that is not a power of
the cutoff is the logarithm. For a smooth sphere in even spacetime dimension `n`,
`S_EE = … + g_0 ln(ε/R) + …` with `g_0 = (−1)^{n/2} 4a_n`, the A-type conformal anomaly. One scalar gives
`g_0 = −1/3, 1/90, −1/756, 23/113400` at `n = 2, 4, 6, 8`; the coefficient of `ln(R/ε)` is `c/3` in 2D
and `−4a` in 4D. In odd dimensions the log vanishes. The Fold's `ln` height is the additive rhyme; the
coefficient is the anomaly's, not the Fold's, and the `1/2` of the critical line is a different object.
See `the-fold-logarithm.md`.

**Engineering:** the Fold is an exponent engine and a compatibility checker, not a constitutive
theory. Geometric similitude is exact (`k`, `k²`, `k³`, curvature `1/k`), and so is the square–cube
law (`mass ∝ k³`, `section ∝ k²`, `stress ∝ k`). Crease closure `m = π/α`, Nyquist `N > 2m`, and the
crystallographic restriction are exact; dynamic similitude, material laws, units, and safety factors
are external. See `the-fold-engineering.md`.

**Two nothings:** `k = 1` is the identity — nothing changed; `k = 0` is the collapse — nothing has
size. The creation loop returns the second, not the first.

**Two ledgers:** the fold ledger is additive — zero is a crease `H`, one is its unit normal `n`, and
each fold has its own pair, so `0 → 1 → 0 → 1` can be a chain of distinct terms. The scale ledger is
multiplicative — its zeros `k_t` are distinct but its one `k = 1` is unique. See `the-fold-key.md`.

**Signature of nothing:** the zero is totally null, inertia `(0,0,n)` — `n` directions, none signed.
Its scalar signature is `0`, but so is the planar fold's; the nullity is the fingerprint. A
continuous sign change must cross a degenerate form, and `k = 0` is that crossing. By stage: point
`(0,0,n)`, scale `(n,0,0)`, fold `(n−1,1,0)`, twist symplectic (`Pf=1`), horizon null. See
`the-fold-signature.md`.

**Occlusion:** the back of a surface is not a place; it is the sign of the normal that a quadratic
measurement forgets. The fold flips it, the projection drops it, and the crease is the only place the
two sides meet. Mathematics can see the axis, not both faces; the one-way surface is the horizon, not
the twist. See `the-fold-occlusion.md`.

**Critical line:** the Dirichlet term `n^{-s}` is the Fold's complex `k` at height `ln n`: modulus
`n^{-σ}`, angle `−t ln n`. The functional equation plus reality is a fold `R(s) = 1 − s̄`, and the
critical line is its crease. RH says the zeros lie on the crease — an exact reformulation, not a
proof. The primes and the zeros are dual, not illusion. See `the-fold-zeta.md`.

**Facets:** a facet is a zero of a supporting functional — codimension one. The fold's crease is a
facet; the scale's zero is a vertex; a zeta zero is a point on the critical-line facet, a facet only of
the line. The phrase "zeros as facets" is the fold ledger's sentence, not the scale's. See
`the-fold-facets.md`.

**Theta fold:** the functional equation is not an axiom. The theta identity `ϑ(1/t) = √t ϑ(t)` is a
fold in height `h = ln t`; its half-density exponent is `1/2`, and that is the real part of the
critical line. A general exponent `α` puts the axis at `Re s = α`. The fold gives the axis, not the
zeros. See `the-fold-theta.md`.

**Zero pipeline:** every stage solves a zero equation, and each solution is a different kind of zero —
a value, a vertex, a facet, a null, and an analytic point. The twist and the observer produce no zero,
which is why their invariant is not an inertia. The only pipeline that composes is analytic: theta's
fold becomes the critical line, and the zeros land on it. See `the-fold-pipeline.md`.

**Problems:** the Fold reformulates RH exactly and rhymes with a dozen other problems, but the map is
the point: positivity needs a surface, Hilbert–Pólya needs an operator, de Bruijn–Newman needs a bound,
and the explicit formula needs a parity breaker — four known walls, one crease. The hole field adds one
exact classifier — multiplicity as a residue of `d log` — and five limits: count vs placement,
coefficient vs existence, period vs parity, puncture vs singularity, flow vs map. See
`the-fold-problems.md`.

**Initial form:** the initial state is the datum — the unique point fixed by every non-identity
scale; its form is
the derivative there, `Dg₀ = 0`, the null form `(0,0,n)`; and its object is the zero object, initial
and terminal at once. The form is the derivative of the state. See `the-fold-initial.md`.

**Categorical:** every object is a morphism in disguise exactly when a functor is named — the arrow
category makes it trivial, Yoneda makes it deep, duality makes it reverse. The Fold makes it concrete:
`k` is an endomorphism, the crease is an equalizer, the orbit space is a coequalizer, and the point is
a zero object. See `the-fold-categorical.md`.

**Composition:** `1_a + 1_b = 2_{ab}` reads three ways — folds add and the parameter
multiplies (the mixed law); the indicators agree on the overlap (the crease); and the reciprocals balance
when the midpoint is `1` (the identity). It is exact because it is mixed: additive in the fold ledger,
multiplicative in the scale ledger. See `the-fold-composition.md`.

**Apex:** one point extending at both sides at all angles is the pencil at the datum: rays are
`Sⁿ⁻¹`, lines and creases are `ℝPⁿ⁻¹` with the two sides identified, and the cones at all apertures
cover the space while intersecting only at the point. The point does not extend; its tangent cone does.
See `the-fold-apex.md`.

**P and NP:** `NP` is an existential projection and a solver is a section; the Fold's linear projection
is the simplest instance, and it is always split, so the hardness is the cost of the section, not its
existence. The Fold has no computational model, and every invariant it can compute is polynomial-time —
so it can map the wall but not cross it. See `the-fold-complexity.md`.

**Crease and height:** the geometric crease is always codimension one, but "height" is three coordinates with one
name: transverse in the affine fold (the offset `c` the fold flips; affine lines in the plane are a
Möbius band), longitudinal in the zeta zero (the imaginary part `t` the crease leaves free), and a scale
in matter and the Dirichlet term (`h = ln n`). The pair is a basis, not a generator: one crease and one
height give one hyperplane; the twist needs two creases, the closure their angle. See
`the-fold-crease-height.md`.

**Folded line from afar:** a sheet fold is a quotient, not the global reflection: it fixes one side and
reflects the other, so a line crossing the crease becomes a V whose vertex is on the crease. The shadow
`π_H` of the V is the crease — one line, the "singular line." The fold's height is dropped by the
projection but survives in the length at second order (`L m²` for slope `m`; `2a²/ℓ²` for pleats of
amplitude `a`). The scale `k` does not erase the fold — the shape is scale-invariant — so "from afar" is
a projection or a coarse-graining, not `k → 0`. See `the-fold-afar.md`.

**The loop:** the corpus retold as one loop — the point and its boundary, the scale and the fold, the
complexified twist, the cosmic history from inflation to the CMB, and the observer who reads the
bookmark. The loop closes in description, not in time: the observer is the zero's last witness, not its
author. The CMB enters as a rhyme; the exact physics is standard cosmology. See `the-fold-loop.md`.

**Reading paths:**

| if you want | read |
|---|---|
| the whole argument in six pages | `the-fold.pdf` |
| the lookup by value of `k` or by question | `the-fold-key.md` |
| the order of creation and the plain-language version | `the-fold-creation.md` |
| matter as the zero at a scale | `the-fold-matter.md` |
| the signature of nothing and the fold's split | `the-fold-signature.md` |
| why the back cannot be seen | `the-fold-occlusion.md` |
| the critical line as a crease | `the-fold-zeta.md` |
| which zeros are facets | `the-fold-facets.md` |
| why the critical line is at 1/2 | `the-fold-theta.md` |
| the zeros in pipeline order | `the-fold-pipeline.md` |
| what the Fold does and does not reach | `the-fold-problems.md` |
| where the Fold starts | `the-fold-initial.md` |
| objects as disguised morphisms | `the-fold-categorical.md` |
| why one plus one is two | `the-fold-composition.md` |
| one point, both sides, all angles | `the-fold-apex.md` |
| P vs NP and why the Fold cannot separate them | `the-fold-complexity.md` |
| the crease and which height | `the-fold-crease-height.md` |
| a folded line that looks like one line from afar | `the-fold-afar.md` |
| a lattice that closes at six, and the gap it can host | `the-fold-hexagon.md` |
| every two in one place: the sign | `the-fold-sign.md` |
| the integer line bent, where two numbers meet | `the-fold-integer-line.md` |
| friction as the trade across the crease | `the-fold-friction.md` |
| the creases as a network, one charge per zero | `the-fold-crease-network.md` |
| the crease moved into the parameter: the discriminant | `the-fold-discriminant.md` |
| what "mathematics is physical" can mean | `the-fold-realization.md` |
| the gate, and what a system would have to say | `the-fold-agi.md` |
| what counts as value, and what the meters read | `the-fold-value.md` |
| which theorems already have every premise | `the-fold-theorems.md` |
| where the physical words have no object | `the-fold-void.md` |
| the observer as dimension and window | `the-fold-observer.md` |
| closure as sampling and the horizon window | `the-fold-sampling.md` |
| the horizon's area and the mode count | `the-fold-area.md` |
| the horizon's clock and the temperature law | `the-fold-clock.md` |
| the accelerated observer and the Unruh period | `the-fold-unruh.md` |
| the wedge's entropy and the area law | `the-fold-entanglement.md` |
| the holographic coefficient and the minimal surface | `the-fold-holography.md` |
| the general coefficient and the Noether charge | `the-fold-wald.md` |
| the universal logarithm and the A-type anomaly | `the-fold-logarithm.md` |
| engineering applications and the limits of transfer | `the-fold-engineering.md` |
| the whole corpus as one loop | `the-fold-loop.md` |
| the observer as a chart-maker, and why a calendar closes | `the-fold-chart.md` |
| choosing the smallest arithmetic spectral power-exponent family | `the-fold-minimal-operations.md` |
| choosing the smallest crease-reflection generator set | `the-fold-geometric-generators.md` |
| deriving the hexagonal crease catalogue and its two sublattice signs | `the-fold-hexagonal-lattice.md` |
| classifying periodic crease networks and surviving sign characters | `the-fold-periodic-networks.md` |
| classifying periodic sign characters for all frieze and wallpaper groups | `the-fold-frieze-wallpaper-characters.md` |
| proving forced zeros and topological realizability of crease networks | `the-fold-forced-zero-topology.md` |
| constructing smooth and analytic periodic heights from crease networks | `the-fold-smooth-analytic-heights.md` |
| realizing prescribed analytic crease divisors as exact zero sets | `the-fold-exact-analytic-networks.md` |
| classifying disconnected crease components and prescribed analytic multiplicities | `the-fold-divisor-parity-classification.md` |
| testing local principality, normalization, and singularity resolution | `the-fold-local-principality-resolution.md` |
| computing exceptional intersection lattices and local divisor-class obstructions | `the-fold-exceptional-lattices-class-groups.md` |
| lifting Fold symmetries to singularity resolutions and exceptional curves | `the-fold-equivariant-resolution-symmetry.md` |
| classifying every analytic D4 semi-invariant on the quartic cone | `the-fold-d4-analytic-character-classification.md` |
| decomposing the complete analytic D4 representation ring on the cone | `the-fold-d4-analytic-representation-decomposition.md` |
| deriving the complete multiplication algebra of the Fold cone | `the-fold-multiplication-algebra.md` |
| deriving the trace discriminant and spectral branch geometry | `the-fold-discriminant-spectral-geometry.md` |
| classifying local algebras and Jordan strata of Fold fibers | `the-fold-local-algebra-jordan-strata.md` |
| computing the vertex Hilbert function and socle structure | `the-fold-vertex-hilbert-function.md` |\n| modular stability of the D16 Lie algebra and its exceptional central prime | `the-fold-d16-modular-stability.md` |\n| restriction to D4 and intrinsic detection of the characteristic-three center | `the-fold-d4-modular-center.md` |
| the interactive models | the nine HTML files |

## Contents

| file | what it is |
|---|---|
| `the-fold.pdf` | the paper, 6 pages |
| `the-fold.tex` | LaTeX source (TeX Live, `pdflatex`) |
| `the-fold.md` | Markdown source |
| `the-fold-key.md` | master key: the `k`-plane, the chain, the four laws, and an index by question |
| `j-plane.html` | 2D model: `A ∝ k²`, `h ∝ k`, the rotation `J` |
| `j-cone-3d.html` | external apex: tangent cone, dimension ladder |
| `j-collapse-3d.html` | sphere/cube collapse: rank, `Ω/4π`, observers at the centre and outside |
| `fold-closure.html` | the closure law: drag `α`, watch `D_m` appear or the orbit go dense |
| `the-fold-closure.md` | follow-up note: `closure m = π/α`, the crystallographic restriction |
| `horizon-scaling.html` | log–log chart: homothetic family vs fixed-mass collapse |
| `the-fold-horizon.md` | follow-up note: why the horizon table needs two columns |
| `fold-midpoint.html` | the midpoint map: `m_k = g_((1+k)/2)`, constant at `k = −1` |
| `the-fold-midpoint.md` | follow-up note: the crease is the midpoint locus |
| `fold-division.html` | every division point's own collapse value, `k_t = (t−1)/t` |
| `the-fold-division.md` | follow-up note: division points, two evolutions, the group law |
| `fold-invariants.html` | live audit: what scaling keeps, what folding keeps, side by side |
| `the-fold-invariants.md` | follow-up note: orbit spaces, invariant rings, `k = −1` as the meeting point |
| `cone-range-3d.html` | 3D range cone: apex at the centre, rim at the range, `θ` and `k` sliders |
| `the-fold-cone.md` | follow-up note: the range cone, its three formulas, and the fold's antipode |
| `the-fold-hexagon.md` | follow-up note: the hexagon - the last lattice closure, the honeycomb's two cosets, the Dirac mass gap, and corrugation as gauge rather than mass |
| `the-fold-sign.md` | follow-up note: the sign - every two in the corpus, the gap as twice the height, `w₁` over a base, and the hexagon's two independent characters |
| `the-fold-integer-line.md` | follow-up note: the integer line bent - crease on a number or in a gap, the two bends of the clock, and the second bit read as "two numbers on the crease" |
| `the-fold-friction.md` | follow-up note: friction - the contact as the crease, the momentum ledger versus the energy ledger, and why turning lengthens the path rather than the patch |
| `the-fold-crease-network.md` | follow-up note: the crease network - the modulus `M x Z`, six sum rules, vertices as sums, and the hexagon as the `k = 6` vertex |
| `the-fold-discriminant.md` | follow-up note: the discriminant - `x² = t`, the crease moved into the parameter, `A_k`'s `k` parameters, and the strata by collision type |
| `the-fold-realization.md` | follow-up note: realization - three readings of "mathematics is physical", the three classes, four ceilings, and the measured exact fraction |
| `the-fold-agi.md` | follow-up note: the gate - premise closure as the criterion, the four-valued type, the stages, and the four adjunctions |
| `the-fold-value.md` | follow-up note: value - physics as the model supply, seven meters, and the orphan test |
| `the-fold-theorems.md` | follow-up note: the theorem ledger - twelve theorems read for premise closure, the six that close, and what the five earlier notes actually did |
| `the-fold-void.md` | follow-up note: the void map - ten physical words, the nearest exact object, the six hosts, the order of the gaps, and the probability row's first move |
| `the-fold-creation.md` | follow-up note: the order of creation — point, scale, fold, twist, closure, horizon, observer, point; plain-language version and glossary |
| `the-fold-matter.md` | follow-up note: matter as the zero at a scale; the height law, its exponents, and the mass reading |
| `the-fold-signature.md` | follow-up note: the signature of zero — inertia, the forced degeneracy, the fold's split, and the ladder by stage |
| `the-fold-occlusion.md` | follow-up note: the back is not a place — side versus axis, the crease, and why the twist is not the ratchet |
| `the-fold-zeta.md` | follow-up note: the critical line as a crease — the Dirichlet term as `k`, the functional equation as a fold, and RH as a location |
| `the-fold-facets.md` | follow-up note: zeros as facets — codimension one versus vertex versus point, and the critical line as the facet |
| `the-fold-theta.md` | follow-up note: the theta fold — the functional equation derived, and why the critical line is at `1/2` |
| `the-fold-pipeline.md` | follow-up note: the zero pipeline — one zero equation per stage, five kinds of zero, and the two gaps |
| `the-fold-problems.md` | follow-up note: the Fold and the open problems — exact, reformulation, rhyme, false friend, the four walls, and the hole field's argument principle |
| `the-fold-initial.md` | follow-up note: the initial form — the common fixed point, the zero derivative, and the zero object |
| `the-fold-categorical.md` | follow-up note: objects as disguised morphisms — arrow category, Yoneda, duality, looping, and the Fold's universal constructions |
| `the-fold-composition.md` | follow-up note: one plus one is two — folds add, parameters multiply, and the two conditional readings |
| `the-fold-apex.md` | follow-up note: one point, both sides, all angles — the pencil, the cone family, and the tangent-cone correction |
| `the-fold-complexity.md` | follow-up note: P and NP — the projection/section diagram, three rhymes, and the wall |
| `the-fold-crease-height.md` | follow-up note: the crease and its height — transverse, longitudinal, and a basis not a generator |
| `the-fold-afar.md` | follow-up note: the folded line from afar — the V, the pleats, the singular line, and projection rather than scale |
| `the-fold-observer.md` | follow-up note: the observer as dimension and window — the form degree, the resolution, and two kinds of blindness |
| `the-fold-sampling.md` | follow-up note: sampling, closure, and the horizon window — Nyquist for `m`-fold patterns, the object/probe lattices, and the causal window |
| `the-fold-area.md` | follow-up note: the horizon's measure — area not volume, the mode-count exponent, angle versus area, and Bekenstein saturation |
| `the-fold-clock.md` | follow-up note: the horizon's clock — surface gravity, imaginary time, the `T ∝ 1/k` law, and Smarr |
| `the-fold-unruh.md` | follow-up note: the observer's thermometer — Rindler acceleration, the Unruh period, detailed balance, and the homothety-versus-boost distinction |
| `the-fold-entanglement.md` | follow-up note: the wedge's entropy — the modular Hamiltonian, the area law, the mode-count exponent, and the coefficient caveat |
| `the-fold-holography.md` | follow-up note: the holographic coefficient - Ryu-Takayanagi, the minimal surface, the coefficient match, and the species relation |
| `the-fold-wald.md` | follow-up note: the general coefficient - Wald entropy, the Noether charge, the higher-curvature checks, and the first law |
| `the-fold-logarithm.md` | follow-up note: the universal logarithm - the A-type anomaly, the coefficient table, the no-log in odd dimensions, and the height rhyme |
| `the-fold-engineering.md` | follow-up note: engineering - geometric similitude, the square–cube law, crease kinematics, sampling, and the false friends |
| `the-fold-loop.md` | closing note: the corpus retold as one loop — point, boundary, scale, fold, twist, the cosmic history, the CMB, and the observer |
| `the-fold-chart.md` | follow-up note: the observer as chart-maker - the chart, the calendar as a quotient of periods, the revision loop, and the horizon detector |
| `the-fold-lean.md` | formal core: the Lean 4 project - involution, quotient, cut, scale, chi, the wheel, the doubling action, and the finite counterexamples |
| `the-fold-universal-invariant.md` | UF-001: the universal invariant under a family of allowed operations, including finite spectral prime-core dynamics |
| `the-fold-geometric-generators.md` | UF-003: primitive crease reflections, dihedral subgroup generation, gcd criterion, and minimum-axis set-cover solver |
| `the-fold-hexagonal-lattice.md` | UF-004: six zero-line crease axes of Re(z^6), D6 character kernels, and the A/B-preserving D3 catalogue |
| `the-fold-periodic-networks.md` | UF-005: wallpaper groups, finite-torus crease-network symmetries, sign-character maps, and common kernels |
| `the-fold-frieze-wallpaper-characters.md` | UF-006: translation-kernel theorem, seven frieze presentations, and periodic character counts for all 17 wallpaper groups |
| `the-fold-forced-zero-topology.md` | UF-007: fixed-point forced-zero theorem, bipartite face-dual realization criterion, and sharp minimal-degree D6 semi-invariants |
| `the-fold-smooth-analytic-heights.md` | UF-008: smooth realization under regular-branch hypotheses, branch-count vanishing-order bounds, and Fourier construction of analytic periodic semi-invariants |
| `the-fold-exact-analytic-networks.md` | UF-009: global analytic principality from locally principal bipartite crease divisors, symmetry-preserving analytic averaging, and exact torus line products |
| `the-fold-divisor-parity-classification.md` | UF-010: weighted-divisor principalness criterion, odd-support homology/separation tests, all-even positive equations, singular local orders, and disconnected torus crease examples |
| `the-fold-local-principality-resolution.md` | UF-011: local generator-count test, normal-but-non-Cartier cone example, cusp/node normalization multiplicities, and weighted blow-up principalization |
| `the-fold-exceptional-lattices-class-groups.md` | UF-012: integral exceptional-correction criterion, ADE discriminant groups, and the simple-elliptic UF-011 cone's numerical Z/2 obstruction with Pic0 caveat |
| `the-fold-equivariant-resolution-symmetry.md` | UF-013: D4 action on the UF-011 cone, elliptic exceptional-curve automorphisms, trivial lattice action with nontrivial height character, and unit-cocycle condition |
| `the-fold-d4-analytic-character-classification.md` | UF-014: complete convergent analytic character modules, invariant quotient ring K{p,z}, and all odd multiplicity patterns on forced reflection branches |
| `the-fold-minimal-operations.md` | UF-002: feasibility, set-cover equivalence, NP-hardness, minimal arithmetic spectral power-exponent families, and a reference solver |

Open the HTML files directly in a browser — no build step, no dependencies.

## Build

```
pdflatex the-fold.tex
pdflatex the-fold.tex
```

## Checks

```
python check.py        # 9 HTML models, 6 pages, index, links, tables, lints
python fold_lint.py    # docs: zone labels; approx: tolerance-as-equality
python fold_lint.py zones
python fold_lint.py selftest
python fold_lint.py reuse   # note-to-note citations; the notes nothing cites
```

`check.py` is the single gate: it runs the structural checks and then the linter. `fold_lint.py` can
also be run alone. It is the corpus's two transferable habits, mechanized. It checks that every table
with a `zone` column uses `exact`, `reformulation`, `rhyme`, or `false friend`; that a `rhyme` row or
sentence carries no proof claim; and that a prose "false friend" names the claim. On the Python side
it rejects a class with an approximate `__eq__` and an exact `__hash__`, a `cmp_to_key` comparator
that uses a tolerance, and `@total_ordering` on an approximate `__eq__`, because each assumes a
quotient that a tolerance does not have. The five fixtures in `tools/fixtures/` make the rules
non-vacuous.

`zones` is the map rather than the gate. It separates three things that look alike: a **claim** in a
zone table, an **inline label** beside a claim, and the **legend** that defines the vocabulary. A
definition is not a claim, so the legend is counted apart rather than inflating the map. It then
counts the **prose attributions**, because that is how most of the corpus actually labels.

```
zone map: 11 files with zone tables of 49
     exact           135
     reformulation     9
     rhyme            22
     false friend     10
     the absence       1
     without tables    38
     legend (definitions, not claims)    11

prose attributions: 48 files of 49
     exact           157
     reformulation     9
     rhyme            21
     false friend     39
     total           226
```

The tables are the formal layer and cover eleven files. The prose is where the corpus actually works:
forty-eight of forty-nine files label their comparisons in the predicative form — a noun phrase
then `is exact`, `remains a rhyme`, `is a false friend` — as in "the quotient statement is exact" or
"`height` is a false friend unless the register is named". The detector is deliberately narrow: it
skips the maxims ("a rhyme written as a proof"), skips negated rejections ("this is not exact"), reads
the negation only inside the clause the verb sits in, and reads a whole paragraph so a sentence
wrapped across lines is not cut in two. It reads the definite form too — "… is the false friend" —
but not "is the exact opposite", which is a noun phrase rather than a label. `--show` prints every
attribution, so the rule can be audited rather than trusted.

A third idiom marks a claim's status without naming a zone: "a reading, not a derivation", "an input,
not a result", "a statement about the lattice, not about the probe". That is the same discipline, one
step short of a label — it says what the claim is *not* without saying which of the four it is.

```
status markers (marked by contrast, zone not named): 28 files of 49
     total            54
     derivation       19
     about             7
     proof             5
     identity          6
     boost             2
     theorem           6
     other             9
```

The objects are the finding. Nineteen say "not a derivation", five "not a proof", six "not a theorem",
and one "not a reduction": thirty-one point at proof. One of those is not a claim — "the Fold is a
dictionary, not a proof engine" — and one "not the identity" is a list of what a point is not, so the
fifty-four marked sentences carry fifty-two claims, and thirty of them say that nothing was proved. That
is the corpus's own definition of **reformulation**, yet the word appears as a label eighteen times, nine
in tables and nine in prose. The middle zone is not scarce; it is unnamed, and the corpus says it with
a contrast instead of a noun.

The remaining objects do different work. "Not an identity", "not about", "not a boost" use one word
in two senses, which is false-friend work rather than a zone; "not a law", "not a model", "not a
result" separate a description from a mechanism.

With that count the map closes: every one of the forty-nine files carries zone language. The three
notes that looked silent in the first two counts — `the-fold-closure.md`, `the-fold-division.md`,
`the-fold-horizon.md` — mark exactly once each, and each mark is the one that matters:

| note | the mark |
|---|---|
| closure | the crystallographic restriction is a statement about the lattice, not about the probe's `N` |
| division | the crease stiffness `κ` is an input, not a result |
| horizon | this is a reading, not a derivation; the Fold supplies the ratio, not the metric |

An earlier version of this section said those three notes named no foreign object. That was wrong,
and measuring it showed the error: all three name one — the crystallographic restriction, the crease
stiffness, the metric — and each flags the borrow at the point it is made. The zone vocabulary is a
scale for comparisons, so the note that compares once is labelled once.

### The lint turned on code it was not written for

The tolerance half was run over installed packages, none of them written for this corpus:

```
sympy   1532 files   0 findings
numpy    407 files   0 findings
scipy    973 files   1 warning
```

The one warning was scipy's `test_filter_design.py:3610`, and it was the linter's mistake, not
scipy's: `abs_tol=5e-16 if not DEFAULT_F32 else 1e-7` is not a literal, and the check was reading an
unreadable tolerance as the default `0.0`, then reporting an exact comparison the source never makes.
That is the rule's own failure — a tolerance treated as a value when it is unknown. It now treats an
unparseable argument as unknown, and `tools/fixtures/approx_good.py` pins the case. After the fix:
2,912 files, 0 findings.

A fourth corpus, the standard library's own equality machinery — `unittest`, `statistics`, `fractions`,
`decimal`, `dataclasses`, `enum` — is 18 files and 0 findings. The rule looks for a tolerance where a
quotient is assumed, and the code that defines equality most carefully does not make that assumption.

The measured result is worth stating plainly: in three mature numerical libraries, `__eq__` with a
tolerance plus a separate `__hash__` does not occur at the top level of the source, because the
libraries that care have already made equality exact. The bug this rule looks for lives in
application classes, not in the scientific stack.

## Measured values quoted in the paper

Silhouette change of a cube twisted about a face axis: 0.0% at 0°/90°/180°/270°, 1.4% at 30°,
**12.3% at 45°**; sphere 0.0% at every angle.

Solid angle seen by an exterior point, `Ω/4π`: 5.060% at `k = 1`, 1.216% at `k = 0.5`, 0.301% at
`k = 0.25`. At the centre of the body it is exactly 100% for every `k > 0`.

Horizon formation, `k* = 2GM/(c²R)`: Earth `1.4 × 10⁻⁹`, Sun `4.3 × 10⁻⁶`, a 70 kg sphere of water
`4 × 10⁻²⁵`.

Recomputed from the formulas, the list reproduces: Earth `1.392 × 10⁻⁹`, the water sphere
`4.067 × 10⁻²⁵`; the three solid angles from `d = 2.281 r` (`1.2158%` and `0.3012%`); the cube
silhouette from the model's own `rotY`/`rotCam` (`1.41%` at 30°, `12.33%` at 45°, `0.00%` at
90°/180°/270°); the cone's `Ω = 3.1416`, `V = 1.0472`, `A = 5.8623`, `V/A = 0.17863`; and the exact
overlap `−cos 120° = 0.5`. The Sun's two values are the same law twice: the paper prints
`4.3 × 10⁻⁶` and `the-fold-horizon.md` prints `4.245 × 10⁻⁶`, and each is right for its own input.
The rounded `M_⊙ = 2.0 × 10³⁰ kg` gives `4.270 × 10⁻⁶`, which prints as `4.3`; the notes'
`1.988 × 10³⁰ kg` gives `4.245 × 10⁻⁶`, which prints as `4.2`. That is a reformulation, not a
disagreement: one law through two values of `M_⊙`, with the last digit recording which value was used.

The midpoint map: `m_k(P) = ½(P + g_k P) = g_((1+k)/2)(P)` to `4.6 × 10⁻¹⁶`, with
`det m_k = ((1+k)/2)ⁿ` exact and rank 0 only at `k = −1`. For a fold `σ_H`, `½(I + σ_H)` is the
projection onto the crease (rank `n − 1`): the midpoint set lies in `H` to `2.2 × 10⁻¹⁶`.

Division points: `q_t = (1 − t + tk)P`, collapsing at `k_t = (t − 1)/t` — ¼ ↦ −3, ⅓ ↦ −2, ½ ↦ −1,
2 ↦ ½. Every `k ≠ 1` is owned by exactly one `t = 1/(1−k)` (round trip `1.8 × 10⁻¹⁵`), and
`t ↔ 1−t` pairs `k` with `1/k` to `2.2 × 10⁻¹⁶`. Map iteration is `m^n = g_(f^n)` exactly; repeated
bisection is `f_n = 1 + (k − 1)/2ⁿ`, converging to the identity for every `k`.

Invariants: a scaling changes every distance by `|k|` (relative `0.850` at `k = 1.85`) and holds
direction at `0°`; a fold holds distances at `0`, radius at `2.2 × 10⁻¹⁶`, and moves direction by
`87°`. `k = −1` is both — an isometry that reverses direction by `180°`. The cross-ratio of four
division points is `t(1−s)/(s(1−t))`, independent of `k` to `4.4 × 10⁻¹⁶`.

Range cone (a spherical sector, not a Euclidean cone): `Ω = 2π(1 − cos θ)`, `V = (R³/3)Ω`,
`A = R²(Ω + π sin θ)`. At `θ = 60°` and `R = 1`: `Ω = 3.1416`, `V = 1.0472`, `A = 5.8623`,
`V/A = 0.1786`, and `(V/A)/k = 0.17863` constant across `k`. `Ω` agrees with Monte Carlo to
`3.5 × 10⁻³` or better. The fold fixes the sector only at `θ = 180°`; otherwise it sends it to its
antipode, the overlap with which is `max(0, −cos θ)` of the ball (`0.50113` measured at `θ = 120°`
against `0.5`).

The observer table is that formula at three apertures: `180°` at the centre, `90°` on the surface,
`arcsin(r/d)` outside. Inverting the paper's `5.060%` gives `d = 2.281 r`, and that one ratio
reproduces `1.216%` and `0.301%` at `k = 0.5, 0.25`. A cone's fold group is the planes through its
axis (residual `0.0`), not the point reflection; a turn about that axis is the *identity* on the
body, so the twist is exact `0.0%` at every angle for a cone as for a sphere — only the cube's
finite symmetry shows it (`12.3%` at `45°`). Collapsing the family leaves the aperture intact as a
limit of directions (`60.0000°` at `k = 1`, `10⁻³`, `10⁻⁶` alike while the range falls six orders),
and the cap alone yields `R = √(A_cap/Ω)`, `θ = 2 arcsin √(Ω/4π)` to `10⁻¹⁵`.

## Structure

0. Summary — the one determinant
1. The scale factor and the datum — area and height cannot share a law
2. Two regimes — sphere (interior apex) and cone (boundary apex)
3. The twist — `J² = −I`, and `U(1)/Sym(B)` as the observable quotient
4. The fold, completed — two folds at `α` give a rotation by `2α`; `(σ₂σ₁)⁴ = I`
5. The horizon — two laws: the homothetic family (`M ∝ k`) and the fixed-mass collapse
6. Zero as the point — rank drops from `n` to 0 in one step
7. What an observer can see — dimension fixes the observable
8. Devices — one bench-top instance per step
9. The one sentence

## Related repository

The executable counterpart of the descent in `Fold/Basic.lean` lives in a
separate repository. `model/fold.py` implements the Joukowski quotient
`q(x) = x + 1/x` and `fold_preimages`; `model/fold_corpus.py` makes the
homothety, fold, cap/puncture ledger, solid angle, and closure checks runnable.
The mapping, including the numerical audit of the theta and calendar notes, is
in [FOLD_CORPUS.md](https://github.com/Puronbo/Universal-Theory-Informata/blob/main/FOLD_CORPUS.md).

## What the Fold is for

The corpus says what it is not — not a proof engine, not a constitutive theory, not a computational
model — but not what it is for. It is for this:

> The Fold is a vocabulary for placing a zero, a crease, a scale, and an observer in one diagram, and
> for saying which of those statements are exact and which are only shaped alike. It is a map of where
> the walls are, not a key through them.

Everything else is an entry in that map. The determinant gives the exponents, the fold gives the
split, the twist gives the period, the closure gives the pattern, the horizon gives the edge, and the
observer gives the reading. The four zones are the map's legend.


**Universal invariant (UF-001):** the complete common invariant of a specified family of operations is its orbit quotient. The finite spectral-power specialization is arithmetic, not itself a geometric crease move. For a finite family of spectral power maps, the note derives a closed-form quotient representative, proves completeness on the abstract spectral-state graph, and records the total-collapse and all-powers no-go boundaries. See the root note `the-fold-universal-invariant.md` and its [full text](the-fold-universal-invariant.md); the standard-library experiment is [tools/fold_universal_invariant.py](tools/fold_universal_invariant.py). The theorem is a specialization of standard quotient and cyclic-group results, not a new prime-distribution theorem.


**Geometric generator catalogue (UF-003):** the primitive planar Fold operations are available crease reflections; twists and rotations are their composites. For a finite closure D_m, the selected crease axes generate a subgroup determined by the gcd of their index differences. The minimum-axis solver reduces the catalogue problem to set cover. See `the-fold-geometric-generators.md` and `tools/fold_geometric_generators.py`.

**Hexagonal lattice crease catalogue (UF-004):** the zero-lines of h(z)=Re(z^6) fix the six actual axes at 15°+30°j. The full unlabelled honeycomb uses all six; even-index creases preserve A/B, while odd-index creases exchange them. The determinant and sublattice signs are independent D6 characters. See `the-fold-hexagonal-lattice.md` and `tools/fold_hexagonal_lattice.py`.


**Hexagonal lattice catalogue (UF-004):** the repository's height h(z)=Re(z^6) fixes the six crease axes at 15°+30°j. The six reflections generate D6; even-index creases preserve the honeycomb A/B labels, while odd-index creases exchange them. The two sign characters (determinant and sublattice) are independent. See the-fold-hexagonal-lattice.md and tools/fold_hexagonal_lattice.py.


**Periodic network classification (UF-005):** a periodic crease graph has a wallpaper symmetry group with a rank-two translation subgroup and finite point quotient. Signed height and site decorations define characters when each is transformed globally by a sign; the subgroup preserving all decorations is the kernel of their combined character map. The finite-torus solver tests square, triangular, and generic oblique examples. See the-fold-periodic-networks.md and tools/fold_periodic_networks.py.


**Frieze and wallpaper characters (UF-006):** when a signed height is periodic under the full translation subgroup T, its sign homomorphism factors through the finite point group P=W/T. This remains true for nonsplit wallpaper extensions. The seven frieze groups give 17 translation-trivial character maps; the 17 wallpaper types give 46. Glide reflections may reverse height once while their squares preserve it. See `the-fold-frieze-wallpaper-characters.md` and `tools/fold_frieze_wallpaper_characters.py`.


**Forced zeros and crease topology (UF-007):** anti-symmetries force their fixed sets into the height zero set. A connected crease network supports a continuous scalar height that changes sign across every crease iff its face dual is bipartite; the network then determines its sign character. In the D6 model, the three nontrivial characters have sharp minimal polynomial degrees 6, 3, and 3. See the-fold-forced-zero-topology.md and tools/fold_forced_zero_topology.py.


**Smooth and analytic Fold heights (UF-008):** for finite networks of regular smooth branches, bipartiteness of the face dual is equivalent to existence of a global smooth sign-changing height. A vertex with q smooth branches forces vanishing order at least q, sharply attained by the local product. Fourier projection realizes every real sign character of a finite periodic point group by a nonzero real-analytic periodic function. Exact realization of a preselected zero network remains a stronger problem. See the-fold-smooth-analytic-heights.md and tools/fold_smooth_analytic_heights.py.


**Exact analytic crease networks (UF-009):** for compact nonsingular global real-analytic surfaces and locally principal analytic crease divisors, a bipartite face dual supplies the disconnection and vanishing mod-2 class hypotheses of the Acquistapace–Díaz-Cano global-principality theorem. Hence the network is the exact zero divisor of a global real-analytic function, with multiplicity one on each irreducible crease component. A finite character-weighted group average imposes the induced symmetry without changing zeros. Paired rational line families also have an explicit sine-product construction. See `the-fold-exact-analytic-networks.md` and `tools/fold_exact_analytic_networks.py`.



**Weighted analytic crease divisors (UF-010):** for D=ΣmᵢCᵢ, only components with odd multiplicity control sign changes. Under the global-principality hypotheses, D is principal iff its mod-2 divisor class vanishes and removing its odd support disconnects X, with each component ideal locally principal. All-even divisors have positive analytic equations without a separation condition. Two disjoint nonseparating loops can separate collectively, while three parallel odd loops fail the mod-2 test. See `the-fold-divisor-parity-classification.md` and `tools/fold_divisor_parity_classification.py`.


**Local principality and normalization (UF-011):** the key local test is μ(I)=dim_k(I/mI). The source-paper cone X:z²=x⁴+y⁴ is normal but the divisor Y:x=0,z=y² has local ideal (x,z-y²) with two minimal generators, so normalization is the identity and does not repair it. A cusp's intrinsic point ideal (t²,t³) becomes (t²) after normalization, recording order two. A weighted blow-up chart makes the cone divisor's strict transform locally principal. See the-fold-local-principality-resolution.md and tools/fold_local_principality_resolution.py.


**Exceptional intersection lattices (UF-012):** if D is principal downstairs, its strict transform has an integral exceptional valuation correction a satisfying Ma=-b, where M is the negative-definite exceptional intersection matrix and b_j=(D~.E_j). The cokernel gives the complete local class obstruction for rational singularities under standard hypotheses; for the UF-011 simple-elliptic E7-tilde cone it is only the finite numerical quotient Z/2, with a degree-zero Picard contribution remaining. See the-fold-exceptional-lattices-class-groups.md and tools/fold_exceptional_lattice_obstruction.py.


**Equivariant resolution and Fold characters (UF-013):** the cone X:z²=x⁴+y⁴ admits a natural D4 action by signed permutations of x,y. Its unique exceptional curve is fixed, so the rank-one lattice action is trivial, while the elliptic curve action is nontrivial. The exact principal height h=xy transforms by χ(r)=-1, χ(s)=+1, with four strict-transform intersections and exceptional correction a=2. A general invariant principal divisor admits a prescribed character generator only when its unit cocycle can be adjusted by a unit. See `the-fold-equivariant-resolution-symmetry.md` and `tools/fold_equivariant_resolution.py`.


**Complete analytic D4 character classification (UF-014):** on X:z²=x⁴+y⁴, every convergent scalar semi-invariant has the unique form h=ΔχF(p,z), where p=x²+y², F is an arbitrary invariant analytic germ, and Δχ is 1, xy, x²−y², or xy(x²−y²) for the four one-dimensional D4 characters. The theorem covers all analytic germs, not just polynomials. On forced reflection supports, multiplicities are 1+2k independently on each D4 branch orbit. See the-fold-d4-analytic-character-classification.md and tools/fold_d4_analytic_character_classification.py.


**Complete analytic D4 representation decomposition (UF-015):** the cone coordinate ring is free of rank eight over its invariant analytic ring A=K{p,z}. Its explicit A-basis consists of four scalar relative invariants and two E-covariant pairs V1=(x,y), V3=(xy²,x²y). Thus the two-dimensional irreducible occurs with multiplicity two, and every E-covariant is a unique A-linear combination of V1 and V3. See the-fold-d4-analytic-representation-decomposition.md and tools/fold_d4_analytic_representation_decomposition.py.


**Complete multiplication algebra (UF-016):** over A=K{p,z}, with q=(p²−z²)/2, the cone algebra is generated by commuting multiplication operators Mx and My on an explicit rank-eight basis. They satisfy Mx²+My²=pI and Mx²My²=qI; their matrices determine every product. The generic joint spectrum reconstructs the D4 orbit fiber. See the-fold-multiplication-algebra.md and tools/fold_multiplication_algebra.py.


**Fold trace discriminant (UF-017):** in the rank-eight basis, det(Tr(b_i b_j))=2^16 q^4(p²−4q)^4. The quotient Jacobian is J=4xy(x²−y²), so its pullback satisfies det(B)=J^8. The reduced branch components map from the four D4 reflection lines. See `the-fold-discriminant-spectral-geometry.md` and `tools/fold_discriminant_trace.py`.


**Local algebra and Jordan strata (UF-018):** generic points on either discriminant branch have four geometric points of local length two and trace rank four. Their multiplication Jordan types differ: q=0 gives [2,2,1,1,1,1], while p²−4q=0 gives [2,2,2,2]. At the vertex there is one length-eight point, trace rank one, and Jordan type [4,4] for both coordinate operators. See `the-fold-local-algebra-jordan-strata.md` and `tools/fold_local_algebra.py`.


**Vertex Hilbert function (UF-019):** the local algebra at p=q=0 has Hilbert function (1,2,2,2,1), embedding dimension two, Loewy length five, and one-dimensional socle generated by x³y. See `the-fold-vertex-hilbert-function.md` and `tools/fold_vertex_hilbert.py`.

**Simultaneous multiplication and Frobenius arithmetic (UF-020):** the commuting multiplication pair (Mx,My) together with its cyclic unit vector is a complete invariant of the based algebra. The coefficient functional extracting x³y gives a perfect Frobenius pairing with Gram determinant 1 over every characteristic. Thus the local algebra itself has no exceptional prime in these invariants; characteristic 2 is exceptional for the D4 quotient differential, whose Jacobian vanishes there. The odd-characteristic fiber classification remains open. See `the-fold-simultaneous-frobenius-arithmetic.md` and `tools/fold_simultaneous_frobenius.py`.

**Residue-characteristic classification (UF-021):** the monic presentation x⁴−px²+q=0 with y²=p−x² proves every fiber has length eight in every characteristic. In odd characteristic, the two discriminant branches and the three previously identified fiber strata persist without additional exceptional residue primes. In characteristic two, the quotient Jacobian vanishes identically and every fiber is non-étale, although the rank-eight algebra and its vertex Frobenius pairing survive. See `the-fold-residue-characteristics.md` and `tools/fold_residue_characteristics.py`.

**Modular D4 symmetry and eigenprimes (UF-022):** in every odd characteristic, the vertex algebra is the D4 coinvariant algebra and carries the regular representation 1⊕χ₁⊕χ₂⊕χ₃⊕2E. In characteristic two, sign changes become trivial, the action factors through coordinate swap, and the four sign characters collapse. Thus 2 is the unique modular eigenprime for this specified integral D4 module. See `the-fold-modular-d4-eigenprimes.md` and `tools/fold_modular_d4.py`.

**Explicit D4 character projectors (UF-023):** with r(x,y)=(-y,x), s(x,y)=(x,-y), the four one-dimensional projectors are Pε,δ=(1/8)(I+εR+R²+εR³)(I+δS), and the two-dimensional isotypic projector is PE=(1/2)(I−R²). In odd characteristic they have ranks 1,1,1,1,4 and sum to identity. In characteristic two, r becomes coordinate swap, s becomes trivial, and the fixed space has dimension six with two nontrivial 2D indecomposable blocks. The decomposition is representation-theoretic, not a product decomposition of the algebra. See `the-fold-d4-character-projectors.md` and `tools/fold_d4_character_projectors.py`.

**D4-isotypic multiplication tensor (UF-024):** an explicit basis is 1, x², xy, x³y, x, y, x³, −x²y. The four character lines are represented by 1, x², xy, x³y, and the two E copies by (x,y) and (x³,−x²y). The complete multiplication table shows how these representation summands couple; in particular E₁E₂ maps by an alternating determinant pairing to the socle character line. The isotypic decomposition is not a product decomposition. See `the-fold-d4-multiplication-tensor.md` and `tools/fold_d4_multiplication_tensor.py`.

**Graded automorphism group (UF-025):** the homogeneous presentation C=k[x,y]/(x²+y²,x⁴) yields a graded linear automorphism group whose orthogonal part is dihedral of order 16, up to scalar dilations. It strictly contains the original signed-permutation D4: the 45-degree change x↦x−y, y↦x+y preserves the ideal after rescaling the quadratic relation. This classifies graded linear automorphisms only, not all nonlinear automorphisms. See `the-fold-graded-automorphism-group.md` and `tools/fold_graded_automorphisms.py`.

**Complete nonlinear automorphism group (UF-026):** the kernel of the linear-part map consists exactly of the seven-parameter substitutions
`X=x+αx²+βxy+γx³+δx²y+ux³y`,
`Y=y−βx²+αxy−δx³+ηx²y+vx³y`.
It is a 7-dimensional unipotent group. The full automorphism group is its semidirect product with the graded linear group from UF-025, hence has algebraic-group dimension 8. See `the-fold-nonlinear-automorphism-group.md` and `tools/fold_nonlinear_automorphisms.py`.

**Unipotent automorphism group law (UF-027):** the composition of the seven-parameter identity-linear automorphisms is now given by an explicit polynomial law on k⁷. The first two parameters add; higher coordinates acquire quadratic and cubic corrections. The SymPy verifier checks all ten coefficient identities. See `the-fold-unipotent-group-law.md` and `tools/fold_unipotent_group_law.py`.

**Lie algebra and exact commutators (UF-028):** the seven-dimensional nonlinear kernel is two-step nilpotent. Its Lie-algebra center equals its derived algebra and is the two-dimensional socle-translation space. The same is true at group level: the exact group commutator has only its final two coordinates nonzero, and every socle translation is a commutator. See `the-fold-unipotent-lie-algebra.md` and `tools/fold_unipotent_commutators.py`.

**D16 representation on the nonlinear Lie algebra (UF-029):** conjugation decomposes the seven-dimensional Lie algebra multiplicity-free as E1 ⊕ E2 ⊕ χ ⊕ E3. The five-dimensional quotient by the center is E1 ⊕ E2 ⊕ χ, while the two-dimensional center is E3. The commutator pairing is D16-equivariant. See `the-fold-d16-lie-representation.md` and `tools/fold_d16_lie_representation.py`.
\n\n**Modular Lie algebra:** the D16 decomposition is geometrically stable in every odd characteristic, while the integral commutator radical acquires the cubic character line in characteristic three. The bracket remains surjective; its center grows from dimension two to three. Characteristic two requires a separately constructed integral D16 model. See `the-fold-d16-modular-stability.md`.\n\n\n**D4 modular center:** restricting the seven-dimensional Lie algebra to the original signed-permutation D4 gives two standard planes and three character lines. In characteristic three, the bracket makes the D4-trivial cubic line central, enlarging the center to `E ⊕ 1`; this is detectable without the larger D16 symmetry. See `the-fold-d4-modular-center.md`.\n

**Characteristic-two D4 reduction (UF-032):** the integral action factors through C2 modulo two, with indecomposable module 3J2 ⊕ J1. The alternating bracket remains surjective, its quotient radical remains zero, and center = derived algebra is the two-dimensional socle plane. The full automorphism group scheme in characteristic two remains an open problem. See `the-fold-d4-characteristic-two.md` and `tools/fold_d4_characteristic_two.py`.


**Characteristic-two automorphism group scheme (UF-033):** for C = k[x,z]/(x^4,z^2), the full derivation algebra has dimension 16. The automorphism scheme is cut out by three Frobenius-thickening equations, has reduced dimension 13 and tangent dimension 16, and is therefore non-smooth. This is larger than the seven-dimensional characteristic-zero unipotent subgroup. See `the-fold-char2-automorphism-scheme.md` and `tools/fold_char2_automorphism_scheme.py`.


**Full automorphism functor across characteristics (UF-034):** the integral algebra is presented functorially by substitutions x↦X, y↦Y satisfying X²+Y² = X²Y² = 0, with automorphisms cut out by invertibility of the induced rank-eight linear map. The full derivation dimension is 8 in every odd characteristic and 16 in characteristic two. The characteristic-three center jump of the restricted seven-dimensional bracket algebra is a separate phenomenon. See `the-fold-full-automorphism-characteristics.md` and `tools/fold_full_automorphism_characteristics.py`.

**Odd-characteristic full automorphisms (UF-035):** the full group is the seven-dimensional identity-linear unipotent kernel semidirect the one-dimensional scalar extension of D16. Its dimension and tangent dimension are both eight, proving smoothness in every odd characteristic. Characteristic two is the unique nonsmooth geometric fiber found so far; the characteristic-three bracket-center jump is separate. See `the-fold-odd-characteristic-automorphisms.md`.


**Integral unipotent model and flatness (UF-036):** the seven-parameter identity-linear automorphisms extend to a smooth flat group scheme U_Z ≅ A^7_Z, with an integer-coefficient group law and inverse. This is exactly the schematic closure of the characteristic-zero subgroup. The full automorphism scheme is not flat over Z: its generic dimension is eight and its characteristic-two fiber dimension is thirteen. In characteristic two the identity-linear kernel is ten-dimensional, strictly larger than the seven-dimensional flat subgroup. See `the-fold-integral-unipotent.md` and `tools/fold_integral_unipotent.py`.


**Characteristic-two identity-linear kernel and normal closure (UF-037):** the full reduced identity-linear automorphism group is H ≅ A^10, while the flat subgroup U_F2 ≅ A^7 is cut out by three explicit coefficient equations. U_F2 is not normal. Its normal closure is the eight-dimensional subgroup N defined by the two degree-two equations F=0 and H=A, and the genuine quotient is H/N ≅ G_a². The remaining cubic transverse direction is generated by conjugation rather than forming a group quotient. Exact GF(2) checks are in `tools/fold_char2_identity_kernel.py`; the proof is in `the-fold-char2-identity-kernel.md`.

**Open UF-038:** determine the homogeneous space H/U, the lower central series of N, and the extension to the nonreduced characteristic-two automorphism scheme.


**Characteristic-two homogeneous space and class-two normal closure (UF-038):** the eight-dimensional normal closure N has an explicit characteristic-two group law; N/U ≅ G_a, its center equals its derived subgroup and is G_a², and N has nilpotency class two. The non-normal homogeneous space H/U is nevertheless affine three-space, with explicit polynomial right-coset coordinates (F, H+A, B+G+I+F(A+C)+A(H+A)). The exact verifier checks the composition law, inverse, commutator, and quotient coordinates. See `the-fold-char2-homogeneous-space.md` and `tools/fold_char2-homogeneous-space.py`.

**Open UF-039:** extend the normal-closure calculation to the full nonreduced characteristic-two automorphism group scheme.


**Characteristic-two infinitesimal normal closure (UF-039):** the reduced normal closure of U remains the eight-dimensional N inside the 13-dimensional reduced automorphism group. In contrast, the Lie ideal generated by Lie(U) under the full 16-dimensional derivation algebra is the entire derivation algebra. Thus the scheme-theoretic normal closure has reduced support N but tangent dimension 16, a non-reduced thickening. The exact Hopf ideal remains open. See `the-fold-char2-infinitesimal-normal-closure.md` and `tools/fold_char2_infinitesimal_normal_closure.py`.

**Open UF-040:** compute the Hopf ideal and nilpotence structure of the scheme-theoretic normal closure.


**UF-040 — Frobenius-kernel candidate:** the reduced quotient Q = Aut(C)_red/N is a smooth five-dimensional group. The preimage of its first Frobenius kernel is a candidate for the scheme-theoretic normal closure of U. It predicts reduced support N and tangent dimension 16, but the quotient map's extension to the full non-reduced automorphism scheme and the minimality proof remain open. See `the-fold-char2-frobenius-normal-closure.md`.

**Open UF-041:** derive Q's explicit group law and test extension of the quotient morphism.


**UF-041 — Second-Frobenius normal thickening:** the ambient nilradical is killed by the second relative Frobenius since c⁴=d⁴=h⁴=0. This gives a canonical homomorphism from the full automorphism scheme to the twice-twisted reduced quotient Q^(2), Q=Aut(C)_red/N. Its kernel is a normal subgroup scheme containing U, with reduced support N and tangent dimension 16. The minimal normal closure is contained in this explicit thickening; equality is not yet proved. See `the-fold-char2-second-frobenius-closure.md`.

**Open UF-042:** compute the minimal Hopf ideal and test equality with the second-Frobenius kernel.


**UF-042 — Explicit reduced quotient law:** the five-dimensional quotient Q = Aut(C)_red/N is now identified as `(G_a^2) ⋊ B`. The graded subgroup B has multiplication `(a1a2, a2 b1 + b2 d1, d1 d2)`; its action on the quotient coordinates (F,R) is `(a²F/d, aR + abF/d)`. This yields the full semidirect-product law. See `the-fold-char2-reduced-quotient-law.md`.

**Open UF-043:** determine the exact Hopf ideal of the scheme-theoretic normal closure by scheme-valued conjugation and compare it with the second-Frobenius kernel.


**UF-043 — Explicit second-Frobenius Hopf ideal:** for Q = (G_a²) ⋊ B, the second-Frobenius kernel has global Hopf ideal `(a⁴−1, b⁴, d⁴−1, F⁴, R⁴)` and length 1024. Pulling it back through the full automorphism scheme gives the UF-041 normal thickening candidate, with predicted rank 16384 over N after including the ambient nilpotent parameters. This does not prove minimality. See `the-fold-char2-second-frobenius-hopf-ideal.md`.

**Open UF-044:** derive the Hopf ideal generated by universal scheme-valued conjugates of U and compare it with the UF-043 candidate.


**UF-044 — Universal Hopf-ideal characterization:** the minimal normal closure corresponds to the largest conjugation-stable Hopf ideal contained in the full ideal of U. The universal condition is `Ad^*(J) ⊆ A ⊗ J`. This formalizes the exact problem without claiming it is solved. See `the-fold-char2-universal-hopf-ideal.md`.

**Open UF-045:** compute the full coordinate Hopf algebra and conjugation coaction, including explicit regular extensions of the quotient functions F and R.


**UF-047 — Globality of the second-Frobenius quotient equations:** the full determinant condition Delta = ai - bh invertible, together with h^2 = 0, implies ai = Delta + bh is a unit. Thus a and i are individually units, so the quotient coordinate formulas from UF-045/046 are global on the entire automorphism scheme. The fourth-power lifts are globally regular; no chart-overlap gluing is needed. This does not establish minimality of the normal closure. See the-fold-char2-fourth-power-quotient-lifts.md.

**Open UF-048:** compute the universal conjugation coaction on the globally defined Frobenius quotient equations and determine whether the Frobenius-kernel candidate is generated scheme-theoretically by conjugates of U.


**UF-048 — Universal conjugation image and Hopf core:** writes U's defining ideal in the full automorphism coordinates and identifies the scheme-theoretic conjugacy-image ideal as the kernel of A→O(G)⊗O(U) induced by G×U→G. This is distinct from pulling back generators of I(U). The subgroup generated by all conjugates is then obtained from the largest Hopf ideal contained in that image ideal. No minimality claim for the second-Frobenius candidate is made. See the-fold-char2-universal-conjugation-coefficient-ideal.md.

**Open UF-049:** compute the universal conjugation coefficient ideal and its largest conjugation-stable Hopf subideal; compare the result with the second-Frobenius kernel modulo all powers of the nilradical through n⁶=0. Important distinction: every element of n=(c,d₀,h) has fourth power zero, but n⁴ and n⁵ as ideal powers are nonzero (c³d₀h∈n⁵), while n⁶=0.


**UF-049 — Nilradical length and associated graded:** the nilpotent coefficient algebra has relative length 16 over the reduced base and Hilbert series 1+3T+4T²+4T³+3T⁴+T⁵ for the ordinary nilradical filtration. Thus n⁵ is nonzero but n⁶=0, even though every individual element of n has fourth power zero. This is not the tangent dimension calculation; it is the length and associated-graded structure of the nilpotent coefficient thickening. See `the-fold-char2-nilradical-associated-graded.md`.

**Open UF-050:** compare the normal-closure and second-Frobenius-kernel ideals on each associated-graded piece.


**UF-050 — Associated graded of the second-Frobenius candidate:** proves that the Frobenius candidate's coordinate algebra is the reduced candidate coordinate algebra tensored with T=k[c,d₀,h]/(c⁴,d₀²,h²). It therefore retains the full nilpotent thickening, with graded ranks 1,3,4,4,3,1. This does not prove that the minimal normal closure has the same thickening. See `the-fold-char2-frobenius-candidate-associated-graded.md`.

**Open UF-051:** determine the degree-two nilradical relations imposed by the actual normal-closure Hopf ideal.


**UF-051:** derives exact composition coproducts for c,d₀,h and corrects the degree-two nilradical basis to c², cd₀, ch, d₀h. The conjugation coaction remains open. See `the-fold-char2-quadratic-nilradical-coproduct.md`.


**UF-052:** derives the universal conjugation pullback modulo the third nilradical power, explicitly exposing the quadratic classes c², cd₀, ch, d₀h. The Hopf-core calculation remains open. See `the-fold-char2-quadratic-conjugation-coaction.md`.


**UF-052 correction:** the h-coordinate formula omitted c₋h₋. The ch terms cancel at lowest order; the earlier degree-two detection claim is withdrawn pending second-order inverse calculations. See the correction in `the-fold-char2-quadratic-conjugation-coaction.md`.


**UF-052 second-order completion:** the inverse constant coefficient d₋ has a nonzero quadratic correction. The h-coordinate formula has been corrected modulo n³ in Section 8 of the conjugation-coaction paper; ch and d₀h are not independently detected by that coordinate at this order.


**UF-052 inverse audit:** the explicit Section 8 h-coordinate formula was withdrawn because inverse coefficients a₋ and h₋ have first-order feedback from the nonlinear coproduct term S=c₋h₋+d₋a₋. Section 9 records the coupled recursion modulo n³. The degree-two coefficient-span conclusion remains open.


**UF-053 partial result:** the corrected coupled inverse computation yields the rank-three coefficient module ⟨c², cd₀, d₀h⟩ from the conjugate's three nilpotent coordinate functions in gr². The remaining direction ch is not detected by those three outputs; the other target coordinates and Hopf core remain open. See Section 10 of `the-fold-char2-quadratic-conjugation-coaction.md`.


**UF-053 grading audit:** Section 11 of the quadratic conjugation paper corrects the homogeneous-degree bookkeeping in the inverse expansion and independently verifies the Section 10 formula and rank-three span.


**UF-054 — Full target-coordinate quadratic audit:** identifies why the rank-three module from the conjugate's nilpotent coordinates cannot be promoted to the full conjugacy-family coefficient module: cubic parameters in U contribute quadratic nilradical terms to nonconstant target coefficients, as shown by `(x+c)^3`. The complete sixteen-function audit (fourteen nonconstant coefficients and two constants) and subsequent Hopf-core computation remain open. See `the-fold-char2-full-conjugation-quadratic-audit.md`.

**Open UF-055:** compute the full degree-two target-coordinate coefficient module, its annihilator, and then the scheme-theoretic conjugacy-image kernel and largest Hopf ideal contained in it.

**UF-055 — Exact cubic conjugation test and coordinate-count correction:** clarifies that the full substitution has fourteen nonconstant coefficients plus two constants (sixteen coefficient functions total); the three nilpotent outputs are c, d₀, h, with h counted among the nonconstant coefficients. Gives an exact conjugation by x-translation showing a cubic U-parameter contributes Bc² to a linear target coefficient. See `the-fold-char2-fourteen-coordinate-conjugation-test.md`.

**Open UF-056:** compute the complete degree-two coaction across all sixteen coefficient functions, then determine the full conjugacy-image kernel and its largest Hopf ideal.


**UF-056 — Nilpotent affine centralizer:** proves that the two-parameter infinitesimal family g(x)=x+c, g(z)=z+hx (c⁴=h²=0) centralizes the entire seven-dimensional subgroup U, using the exact inverse z↦z+hx+hc and the U relation I=B+G. This restricted family therefore contributes no new conjugates and does not detect ch, despite ch being present in its coefficient algebra. The full ambient conjugation problem remains open. See `the-fold-char2-nilpotent-affine-centralizer.md`.


**UF-057 — Triangular affine centralizer:** extends the exact centralizer result to all triangular affine automorphisms (g(x)=c+ax, g(z)=d+hx+iz), with a,i units and c⁴=d²=h²=0. Exact substitution shows every such g centralizes U. This restricted family contains mixed nilpotent products such as ch and dh but contributes no nontrivial conjugates. Off-diagonal linear and higher ambient coefficients remain open. See `the-fold-char2-triangular-affine-centralizer.md`.


**UF-058 — Full affine centralizer:** proves that every determinant-open affine automorphism `g(x)=c+ax+bz`, `g(z)=d+hx+iz` centralizes the seven-dimensional subgroup U. The proof factors the linear matrix into lower- and upper-triangular parts; UF-057 handles the lower-triangular/translation factors and exact substitution handles the upper-triangular factor. Hence the off-diagonal coefficient `b` still produces no conjugation variation, and `ch` is absent from all sixteen target-coordinate variations on the affine family. Nonlinear ambient coefficients and the universal orbit-image Hopf core remain open. See `the-fold-char2-full-affine-centralizer.md`.

**Open UF-059:** introduce quadratic ambient terms and identify the first nonlinear stratum where conjugation becomes nontrivial.


## UF-058 — Composition-order correction: affine conjugation detects ch

**Correction and withdrawal.** The claimed centralizer results UF-056 and UF-057, and the attempted full-affine extension UF-058, used the wrong order when applying the substitution maps. Those centralizer conclusions are withdrawn. For algebra automorphisms represented by their images, the correct calculation is g(u(g^{-1}(x))) and g(u(g^{-1}(z))).

Take the triangular affine element g(x)=x+c, g(z)=z+hx, with c⁴=h²=0, and the U-element u(x)=x+Ax², u(z)=z+Axz. Since g^{-1}(x)=x+c and g^{-1}(z)=z+hx+hc, exact composition in characteristic two gives

\[
(gug^{-1})(x)=x+Ax²+Ac²,
\]
\[
(gug^{-1})(z)=z+Axz+Acz+Ach\,x+Ac²h.
\]

Therefore the target coefficient of x in the second coordinate is Ac h. This is an exact scheme-level polynomial identity and proves that ch is detected by the affine conjugation family. It directly contradicts the prior assertion that the triangular affine family centralizes U. The separate UF-055 cubic translation calculation remains valid because it used the correct composition order.

The papers UF-056, UF-057, and UF-058 now carry explicit withdrawal/correction sections. Do not use their earlier centralizer conclusions. The full affine conjugation coefficient module, scheme-theoretic image kernel, and largest Hopf ideal remain open.

**Open UF-059:** compute the correct conjugation coaction for the full determinant-open affine family, all sixteen target coefficient functions, and the resulting coefficient module/annihilator. Only then proceed to the universal orbit-image kernel and its largest Hopf ideal.


## UF-059 — Mixed ch coefficient vector on an affine slice

**Theorem UF-059.1.** On the affine slice g(x)=x+c+bz, g(z)=z+hx with c⁴=h²=0, the determinant 1+bh is a unit. Using the correct composition order, the coefficient of ch is nonzero in ten target coordinates: a', b', α', β', δ', h', i', φ', ψ', θ', with respective coefficients Ab+C, Ab²+Cb, Bb+Gb², E+Jb, Eb+Jb², A, Ab+C, B+Gb, J, E+Jb. It vanishes in c', d', γ', ε', η', κ'. In particular, b=0 gives h'=Ach for the A-only element of U. This is an exact coefficient extraction in the truncated ring, not a first-order approximation.

This establishes detection of ch by the affine conjugation family, but the calculation is restricted to a=i=1,d=0 and is not the full affine coaction or the orbit-image Hopf core. See `the-fold-char2-affine-ch-coefficient-vector.md`.

**Open UF-060:** compute the complete determinant-open affine coaction for arbitrary a,b,d,h,i,c and determine the coefficient module across all sixteen target functions, its annihilator, and its relation to the second-Frobenius candidate.


## UF-060 — Full determinant-open affine ch coefficient

**Theorem UF-060.1.** For the full affine family g(x)=c+ax+bz, g(z)=d+hx+iz, with a,i units and c⁴=d²=h²=0, put r=a⁻¹, t=i⁻¹, L=Abt+C, M=B+Ed+Gbt+Jbdt, and N=E+Jbt. With the correct composition order, the exact coefficient of ch in the conjugated coordinate polynomials is

\[
[ch]X'=bd r²tL+rLx+br²Lz+btM x²+aN x³+bN x²z,
\]
\[
[ch]Z'=drtL+Atx+rLz+atM x²+Ja²t x³+aN x²z.
\]

Thus ch appears in twelve of the sixteen target coefficient functions and vanishes in γ′, ε′, η′, κ′. This is the complete ch-component of the full affine coaction, not the complete coefficient module or the orbit-image Hopf core. See `the-fold-char2-full-affine-ch-coefficient.md`.

**Open UF-061:** compute all nilradical monomial coefficients in all sixteen target functions, determine the full affine coefficient module and annihilator, and compare the orbit-image kernel with the second-Frobenius candidate.


## UF-061 — Maximal generic rank of the affine coefficient matrix

**Theorem UF-061.1.** The fifteen nonconstant monomials of T=k[c,d,h]/(c⁴,d²,h²) give fifteen columns in the 16×15 coefficient matrix of the full affine conjugation's target coordinates. At the admissible specialization a=i=1, b=0 and (A,B,C,D,E,G,J)=(0,0,0,1,1,1,1), the 15×15 minor using all target rows except ε′ has determinant 1 over F₂. Hence the coefficient matrix has generic rank 15, its maximal possible rank. Thus every nilpotent monomial direction is generically linearly independent across the sixteen target functions. This is not a computation of the orbit-image kernel or its Hopf core. See `the-fold-char2-affine-coefficient-matrix-rank.md`.

**Open UF-062:** determine the maximal-minor rank-drop locus and then compute the orbit-image kernel and its largest Hopf ideal.


## New research direction — automorphic methods and Hopf–Galois theory

Added `the-fold-automorphic-and-hopf-galois-applicability.md`, an applicability audit of the four-page RH/GRH research announcement at alpo.ge/remark.pdf. It distinguishes automorphic forms/representations from algebra automorphisms, concludes that theta lifts and adelic machinery do not directly apply to the finite Fold algebra without additional global arithmetic structure, and identifies determinant, representation, and integral-lattice methods as methodological parallels.

The note also establishes a concrete characteristic-two direction: C_k ≅ k[x,z]/(x⁴,z²) admits the primitive Hopf structure of O(α₄×α₂), giving a rank-eight finite connected group scheme and a Hopf–Galois torsor structure via the regular coaction. This is characteristic-two-specific and does not identify the full automorphism group scheme with the translation subgroup. Suggested follow-ups cover exact verification, normalizers/centralizers, Hopf-structure classification, and descent/twists.


### G-1/G-2 — Hopf–Galois structure and translation normalizer
- Verifies the primitive Hopf algebra structure on (k[x,z]/(x^4,z^2)), identifying (G=alpha_4\times\alpha_2).
- Gives the Hopf–Galois canonical map and its antipode inverse; an exact 64-by-64 matrix verifier over (mathbb F_2) confirms full rank.
- Proves functorially that the translation subgroup's centralizer in the full automorphism scheme of (operatorname{Spec}(A)) is exactly (G), and its normalizer is (G\rtimes\operatorname{Aut}_{\mathrm{grp}}(G)).
- Computes (operatorname{Aut}_{\mathrm{grp}}(G)=operatorname{Spec} k[a^{\pm1},f^{\pm1},b,c,d,e]/(d^2)), with reduced dimension 5 and tangent dimension 6.
- Adds `the-fold-char2-hopf-galois-normalizer.md` and `tools/fold_char2_hopf_galois.py`.
- Computes fixed-group-scheme torsor classes over a characteristic-two field: (H^1_{\mathrm{fppf}}(k,G)\cong(k/k^4)\times(k/k^2)). This does not classify all algebra forms or all Hopf structures.


### G-3 — Four pairwise non-isomorphic Hopf structures on the same algebra
- Exhibits the four product group schemes alpha_4 x alpha_2, mu_4 x alpha_2, alpha_4 x mu_2, and mu_4 x mu_2 on the same underlying algebra k[x,z]/(x^4,z^2).
- Gives additive and multiplicative coproducts, counits, and antipodes in the common truncated coordinates.
- Proves pairwise non-isomorphism using the restricted 2-power map on Lie algebras and, for the two mixed cases, the scheme-theoretic image of relative Frobenius.
- Extends the canonical-map verifier to all four structures; all four 64-by-64 matrices have rank 64 over F_2.
- Adds the-fold-char2-multiple-hopf-structures.md and tools/fold_char2_hopf_structures.py.
- Explicitly does not claim an exhaustive classification; non-product Hopf structures remain open.


### UF-061 verification addition
- Adds tools/fold_char2_affine_coefficient_matrix_rank.py, which reconstructs the admissible specialization in the exact truncated polynomial ring and verifies the stated 15-by-15 determinant is 1 over F₂ using standard-library arithmetic.


### UF-062A — Exact rank-drop scheme on a triangular affine slice
- Restricts the affine conjugator to g(x)=x+c, g(z)=z+d+hx while retaining all seven U parameters.
- Computes all sixteen maximal minors of the 16-by-15 nilpotent coefficient matrix exactly over F₂[A,B,C,D,E,G,J]: their ideal is (E^15), and the only nonzero maximal minor is the one omitting epsilon-prime.
- Therefore the rank-15 locus on this slice is D(E), with set-theoretic rank-drop support V(E).
- On E=0 the generic rank is exactly 11 over F₂(A,B,C,D,G,J); an explicit 11-by-11 minor is C^3 D^4 J^4.
- Adds the-fold-char2-affine-rank-drop-slice.md and tools/fold_char2_affine_rank_drop_slice.py (SymPy required).
- This resolves only a restricted slice; the full determinant-open rank-drop locus and the orbit-image Hopf core remain open.


### G-3b — Corrected scheme-theoretic normalizers for all four Hopf laws
- Proves the translation centralizer is the translation subgroup for each of the four group laws; the normalizer is the translation group semidirect its full group-scheme automorphism functor.
- Corrects an initial mixed-case calculation: cross-homomorphisms vanish on field-valued points but not over nonreduced coefficient rings.
- For mu_4 x alpha_2, finds the infinitesimal cross map t -> 1+r z with r²=0; its automorphism group scheme has underlying C2 x G_m x alpha_2, reduced dimension 1 and tangent dimension 2.
- For alpha_4 x mu_2, finds the cross map t -> 1+p x+q x²+pq x³ with p²=q²=0; its automorphism group scheme has reduced dimension 2 and tangent dimension 4.
- Retains the additive-additive automorphism scheme (reduced/tangent dimensions 5/6) and the multiplicative-multiplicative constant D8 automorphism group.
- Adds the-fold-char2-hopf-normalizers-all-four.md, including corrected mixed-case composition laws.


### G-4 — Explicit fppf torsors for all four Fold group laws
- Uses the Frobenius exact sequences for alpha_4, alpha_2 and the fppf Kummer sequences for mu_4, mu_2.
- Computes the four H^1 sets as products of k/k^4, k/k^2, k×/(k×)^4, and k×/(k×)^2 according to the additive/multiplicative factors.
- Gives explicit rank-eight torsor algebras and coactions for all four product group schemes.
- Shows all four torsor sets vanish over perfect fields and can be nontrivial over imperfect fields, e.g. F_2(t).
- Adds the-fold-char2-hopf-torsors-four-laws.md. This classifies torsors under the fixed four group schemes, not all group-scheme forms or Hopf structures.


### G-3c — Fifth, non-product Hopf structure
- Constructs the cocycle coproduct Delta(x)=x⊗1+1⊗x and Delta(z)=z⊗1+1⊗z+x²⊗x².
- Proves the Hopf axioms and identifies the group law as a nontrivial central extension of alpha_4 by alpha_2.
- Distinguishes it from the four product structures using primitive-space dimension 2, relative-Frobenius image alpha_2, and zero restricted Lie 2-power map.
- Adds the-fold-char2-nontrivial-cocycle-hopf-structure.md and tools/fold_char2_cocycle_hopf.py; exact F₂ verification passes.
- Together with G_D, establishes at least six pairwise non-isomorphic base Hopf structures on the same Fold algebra; exhaustive classification remains open.


### G-3d — Automorphism group and translation normalizer of the fifth Hopf law
- Computes every Hopf automorphism of the cocycle group: x maps to ax+bx² and z maps to a⁴z+cx+dx², with a invertible and c²=0.
- Gives the exact composition and inverse laws.
- Identifies Aut_grp(G_C)=Spec k[a,a⁻¹,b,c,d]/(c²), reduced dimension 3 and tangent dimension 4.
- Proves the translation centralizer is G_C and the normalizer is G_C semidirect Aut_grp(G_C).
- Adds the-fold-char2-cocycle-automorphism-normalizer.md. The cocycle group's fppf torsors and further Hopf structures remain open.


### G-3e/G-4 — Fppf torsors of the fifth, non-product Hopf group
- Uses the exact sequence 0 -> alpha_2 -> G_C -> alpha_4 -> 0.
- Proves the short exact sequence 0 -> k/k² -> H¹_fppf(k,G_C) -> k/k⁴ -> 0; it splits noncanonically as F₂-vector spaces because G_C is killed by 2.
- Constructs explicit rank-eight torsors B_(a,b)=k[u,v]/(u⁴-a,v²-b) with the cocycle coaction and gives an explicit inverse to the canonical map.
- Adds the-fold-char2-cocycle-torsors.md. The cohomology group splitting is noncanonical; no canonical direct-product law on the parameters is claimed.


### G-3g — Sixth, non-product Hopf structure with nilpotent Lie 2-map
- Constructs Delta(x)=x⊗1+1⊗x+z⊗z and Delta(z)=z⊗1+1⊗z.
- Identifies it as a nontrivial central extension of alpha_2 by alpha_4.
- Computes primitive space span{z,x²}, Frobenius image alpha_2, and restricted Lie 2-map D_z^[2]=D_x, D_x^[2]=0; these distinguish it from the previous five structures.
- Computes Aut_grp(G_D)=Spec k[a,a⁻¹,b,c,d]/(b²), with reduced/tangent dimensions 3/4 and explicit composition/inverse.
- Proves the translation centralizer is G_D and the normalizer is G_D semidirect Aut_grp(G_D).
- Adds the-fold-char2-nilpotent-pmap-hopf-structure.md and tools/fold_char2_nilpotent_pmap_hopf.py.

### G-3f — Frobenius reduction of the Hopf-structure classification
- Shows A²=k[x²]/(x⁴) has rank two and the Frobenius kernel has coordinate algebra k[x,z]/(x²,z²), rank four, independent of the coproduct.
- Shows F²=0 and the Frobenius image is either alpha_2 or mu_2 over an algebraically closed field.
- Records six base structures and the G_lambda imperfect-field family in terms of Frobenius kernel and image; G_D realizes a height-one kernel with nilpotent Jordan restricted 2-map.
- Reduces the exhaustive classification to height-one kernels and extensions compatible with the fixed rank-eight algebra.
- Adds the-fold-char2-frobenius-hopf-classification.md.


### G-3h/G-4 — Fppf torsors under the nilpotent-p-map group G_D
- Uses 0 -> alpha_4 -> G_D -> alpha_2 -> 0 to prove 0 -> k/k⁴ -> H¹_fppf(k,G_D) -> k/k² -> 0.
- The sequence splits noncanonically as F₂-vector spaces because G_D is killed by 2.
- Constructs explicit rank-eight torsors B_(a,b)=k[u,v]/(u⁴-a,v²-b) with coaction rho(u)=u⊗1+1⊗x+v⊗z and rho(v)=v⊗1+1⊗z.
- Gives an explicit inverse to the canonical map and shows the torsors realize all classes after choosing representatives.
- Adds the-fold-char2-nilpotent-pmap-torsors.md.


### G-3i — Imperfect-field mixed Hopf family
- Constructs G_lambda with t=1+z, Delta(x)=x⊗1+1⊗x and Delta(t)=(t⊗t)(1+lambda x²⊗x²).
- Verifies the multiplicative 2-cocycle and Hopf identities; gives the central extension 0 -> mu_2 -> G_lambda -> alpha_4 -> 0.
- Proves the extension splits exactly when lambda is a square in k; for lambda nonsquare it is not isomorphic to alpha_4 x mu_2.
- Over k=F₂(s), lambda=s gives an additional Hopf structure on the same algebra, beyond the six base examples.
- Classifies normalized symmetric cocycles in the fixed global-section model by k/k²; records the torsor sequence and the exact boundary-vanishing criterion c²+a d²+d=λ; identifies the full Brauer class as the quaternion algebra Q(a,λ); adds the-fold-char2-imperfect-mixed-hopf-family.md and tools/fold_char2_mixed_hopf_cocycle_class.py.


### G-3i cocycle-classification verification refinement
- Restores the complete normalized symmetric cocycle basis by including the possible `xy` term.
- The condition `F²=0` forces its coefficient `rho` to satisfy `rho²=0`; over a field this gives `rho=0`.
- Re-runs the remaining cocycle equations and coboundary calculation with an exact symbolic verifier.


### G-3j — Automorphisms of the imperfect mixed Hopf family
- Computes the full group-scheme automorphism functor: `x ↦ ax+bx²`, `t ↦ t(1+ux+βx²+uβx³)`, with `u²=0` and `β²=λ(1+a⁴)`.
- Includes the infinitesimal `u`-direction missed by field-valued-point calculations; the automorphism group has reduced dimension two and tangent dimension four.
- Derives the composition and inverse laws and adds `tools/fold_char2_mixed_hopf_automorphisms.py`.
- Adds `the-fold-char2-imperfect-mixed-hopf-automorphisms.md`.


### G-3k — Frobenius factorization of the mixed-family torsor obstruction
- Identifies `G_lambda` as the pullback of the rank-four central extension `E_lambda` of `alpha_2` by `mu_2` along `F: alpha_4 -> alpha_2`.
- Proves `δ_lambda = δ'_lambda ∘ F_*`; therefore the obstruction depends only on `a mod k²` and vanishes on `k²/k⁴`.
- Reduces the remaining arithmetic calculation to `δ'_lambda: k/k² -> Br(k)[2]`.


### G-3l — Exact vanishing criterion for the mixed-family torsor boundary
- For the rank-four extension E_lambda of alpha_2 by mu_2, proves `δ'_lambda([a])=0` iff `c²+a d²+d=λ` has a solution in k.
- By Frobenius factorization, the same criterion governs the boundary for G_lambda-torsors under alpha_4.
- Shows the boundary vanishes identically when λ is a square; the explicit Brauer-class representative remains open.

- Adds `tools/fold_char2_mixed_torsor_boundary.py` to verify the action cocycle identity and the explicit boundary-vanishing equation.


### G-3m — Explicit quaternion class of the mixed-family boundary
- Identifies `δ'_lambda([a])` with the Brauer class of `Q(a,λ)=k⟨U,D⟩/(U²=a,D²=λ,DU+UD=1)`.
- Proves this by realizing `E_lambda` as the pullback of `SL₂ -> PGL₂` and computing the descended matrix algebra.
- Therefore `δ_lambda([a] mod k⁴)=[Q(a,λ)]`; the equation `c²+a d²+d=λ` is its exact splitting criterion.

- Describes all `G_lambda`-torsor classes as an extension of `k×/(k×)²` by the kernel of `[a] ↦ [Q(a,λ)]` on `k/k⁴`; it splits noncanonically as an F₂-vector-space sequence.

- Adds `tools/fold_char2_mixed_quaternion_descent.py` to verify the matrix realization and quaternion descent identities.

- Classifies parameter isomorphisms: `G_lambda ≅ G_mu` iff some `a∈k×` satisfies `lambda+mu*a⁴∈k²`; fixed-section classes must be quotiented by the quotient automorphism scaling action.


### G-3n — Exhaustive height-one kernel classification
- Classifies all rank-four commutative height-one kernels over an algebraically closed field by the rank and Jordan type of the semilinear restricted 2-map.
- Proves there are exactly four types: `alpha₂²`, `I_{1,1}`, `alpha₂×mu₂`, and `mu₂²`.
- Matches all four types to existing Fold Hopf laws; further examples must differ through extension data or Frobenius image.
- Adds `the-fold-char2-height-one-kernel-classification.md`.

- Organizes the rank-eight classification into eight kernel/image pairs; five are realized and three remain open, not ruled out.


### G-4b — Fppf torsors of the non-product Hopf structures
- For `G_C`, proves `0 → k/k² → H¹(k,G_C) → k/k⁴ → 0`.
- For `G_D`, proves `0 → k/k⁴ → H¹(k,G_D) → k/k² → 0`.
- Both obstruction groups vanish because `H²(k,α₂)=H²(k,α₄)=0`; both sequences split noncanonically as F₂-vector spaces.
- Consequently these torsor groups are abstractly isomorphic to that of `α₄×α₂`, despite the non-isomorphic Hopf structures.
- Adds `the-fold-char2-nonproduct-torsor-classes.md`.

- Refines the full `G_lambda` automorphism proof by ruling out an additive component in the image of `t`, clarifies pullback composition order, and extends the symbolic verifier to check the full substitution law and inverse.


### G-4c — Comparative torsor table for all seven known Hopf structures
- Collects the fppf `H¹` groups of the four products, `G_C`, `G_D`, and `G_lambda`.
- Shows `G_C` and `G_D` have abstract torsor groups matching `α₄×α₂`, while `G_lambda` is controlled by the quaternion splitting kernel.
- Adds `the-fold-char2-comparative-torsor-groups.md`.


### G-4d — Explicit torsor models for G_C and G_D
- Constructs every torsor as `u⁴=a, v²=b` for G_C and `u²=a, v⁴=b` for G_D, with explicit group actions and inverses to the canonical maps.
- Derives complete parameter equivalences and twisted addition laws: `(a,b)+(a',b')=(a+a',b+b'+aa')` for G_C and `(a+a',b+b'+a²a'²)` for G_D.
- Explains why the cohomology splittings are noncanonical.
- Adds `the-fold-char2-nonproduct-torsor-models.md`.

- Adds `tools/fold_char2_nonproduct_torsor_models.py`, an exact symbolic verifier for the G_C and G_D torsor actions, equivalences, canonical-map inverses, and contracted-product formulas.


### G-4e — Explicit torsors under G_lambda
- For each fourth-power class `[a]` whose quaternion `Q(a,lambda)` splits, constructs a torsor `u⁴=a, v²=q` with action `(u,v)·(r,t)=(u+r, vt(1+(c+d u²)r²)` whenever `c²+a d²+d=lambda`.
- Gives the inverse to the canonical action map and proves the model realizes every lift; the remaining fiber parameter is `k×/(k×)²`.
- Adds `the-fold-char2-mixed-torsor-models.md` and a symbolic verifier.

- Expresses the mixed-family Brauer boundary in standard characteristic-two symbol notation: for `lambda ≠ 0`, `δ_lambda([a])=[a*lambda,lambda)_2`; for `lambda=0` it is zero.
- Adds `tools/fold_char2_mixed_torsor_models.py`; the explicit `G_lambda` action law and canonical-map inverse were checked symbolically over F₂.


### G-2c — Translation normalizer of the mixed Hopf family
- Applies the functorial regular-translation theorem to `G_lambda`: centralizer is `G_lambda`, normalizer is `G_lambda ⋊ Aut_grp(G_lambda)`.
- Computes reduced dimension two and tangent dimension six for the normalizer, retaining the infinitesimal automorphism parameters.
- Adds `the-fold-char2-mixed-hopf-normalizer.md`.

- Exhibits a nonzero boundary over `k=F₂(s,t)`: for `lambda=s`, the class `Q(t,s)` is nonsplit by a valuation-at-infinity argument, so the `alpha₄`-torsor `u⁴=t` does not lift.


### G-4f — Arithmetic of the quaternion boundary
- Describes the image for lambda nonzero as the fixed-second-slot symbol subgroup
  `{[b,lambda)_2 : b in k}`, and records the exact affine kernel criterion.
- Gives a valuation proof that `[st,s)_2` is nonzero over `F₂(s,t)`.
- Shows that adjoining `sqrt(lambda)` kills the entire boundary map, and records
  the remaining field-uniform kernel problem.
- Adds `the-fold-char2-quaternion-boundary-arithmetic.md`.


### G-4g — Full quaternion-boundary kernel over F₂(s,t)
- Proves the exact parameterization `ker(delta_s) = {[s r²+r] : r in F₂(s,t)×}`
  inside `k/k²), by solving the explicit torsor-lifting equation.
- Records that this is the image of an additive polynomial modulo squares;
  finding a simpler intrinsic description remains open.

 
### G-4h — One-variable Artin–Schreier criterion for the quaternion kernel
- Expands the full kernel parameterization over \(\mathbb F_2(s,t)\) in the square-subfield basis \(1,s,t,st\).
- Eliminates one coefficient to obtain an exact one-variable condition over \(K=\mathbb F_2(s^2,t^2)\): \(q^2+q+S(\alpha+T\beta^2+ST\gamma^2)\in S K^2\).
- Clarifies that this is a coset-membership criterion, not a claim of \(K\)-linearity or a closed-form classification.


### UF-063 — Exact invisible locus of the mixed (ch) direction
- Extracts the precise closed locus where the full-affine (ch)-coefficient vector vanishes in all sixteen target coordinates: (A=C=J=E=0), (B+Gbt=0).
- Separates invisibility of this one nilpotent direction from the still-open full coefficient module and Hopf-core calculations.


### UF-064 — First-order nilpotent coefficient map
- Computes the complete linear c,d,h layer of the full-affine conjugation target coefficients.
- Shows generic rank three via the explicit minor A²atC, while keeping higher nilpotent layers open.


### UF-064 correction
The complete first-order c,d,h coefficient map in both conjugated coordinates is recorded in the affine coefficient paper. The initial table was corrected: X' also has linear nilpotent terms. The generic rank-three minor A²atC remains valid.


### UF-065 — Quadratic nilpotent layer
- Computes all four degree-two coefficient vectors c², cd, ch, dh in all sixteen target coordinates.
- Cross-checks the ch column against UF-060.
- Proves generic rank four for the quadratic associated-graded coefficient map by an explicit minor.


### UF-066 — Higher nilpotent coefficient layers
- Computes all degree-three, degree-four, and degree-five coefficient vectors in both conjugated coordinates.
- Gives explicit nonzero minors proving generic associated-graded ranks 4, 3, and 1.
- Completes the positive-layer rank profile as (3,4,4,3,1), matching the graded dimensions of the nilpotent parameter algebra.
- Keeps the full coefficient module, scheme-theoretic orbit-image ideal, and largest Hopf ideal as distinct unresolved targets.


### UF-067 — Generic full rank of the nilpotent coefficient matrix
- Forms the complete 16-by-15 matrix for all nonconstant monomials in (c,d,h).
- Proves generic rank 15 by an explicit maximal-minor specialization over F_256; the determinant is 4a after deleting the X' x^3 z row.
- Establishes generic linear independence across nilpotent degrees, while keeping the orbit-image ideal and Hopf-core problem open.


### UF-068 — Local module structure of the full coefficient map
- Localizes at the nonzero UF-067 maximal minor and proves the 16-by-15 coefficient map splits as an injection on a dense principal open.
- Its cokernel is free of rank one there; the fifteen coefficient directions are a direct summand of the target module.
- Explicitly does not identify the orbit-image ideal or its Hopf core; multiplication relations and coproduct stability remain open (UF-069).


### UF-069 — Unique residual linear relation
- On the dense chart defined by the UF-067 maximal minor, constructs the unique normalized left-kernel covector \(\ell=(vM_0^{-1},1)\) of the 16-by-15 coefficient matrix.
- Shows that the corresponding parameter-ring-linear combination of the sixteen target functions has no nilpotent dependence.
- Explicitly distinguishes this module relation from a polynomial relation in the k-algebra generated by the target functions; the orbit-image ideal and Hopf core remain open (UF-070).


### UF-070 — Affine-conjugator coefficient image algebra
- Presents the auxiliary image algebra of the three-parameter affine-conjugator family as \(k[f_1,\ldots,f_{16}]\cong k[Y_1,\ldots,Y_{16}]/\ker\theta\).
- Identifies \(\ker\theta\) with the contraction of the graph ideal \((Y_j-f_j)\) to the target polynomial ring, giving an exact elimination setup that retains \(c^4=d^2=h^2=0\).
- Proves localization at the UF-067 maximal minor does not change this affine-slice image-algebra kernel, because the source parameter algebra is free over an integral reduced base and the minor is a nonzero divisor.
- Explicitly distinguishes this affine slice from the full universal conjugation image \(G\times U\to G\); the full orbit-image ideal and its Hopf core remain open.


### UF-071 — Two-copy coproduct criterion for the affine-slice image
- Identifies the affine-linear conjugators as a subgroup scheme \(G_{\rm aff}\subset G\).
- Defines the affine-slice image ideal \(I_{\rm aff}=\ker(O(G)\to O(G_{\rm aff})\otimes O(U))\), distinguishing it from the full universal orbit-image ideal.
- Gives the exact Hopf test using two independent conjugates and explains why a shared conjugator does not test closure.
- Does not assert the affine-slice image is a subgroup or compute its Hopf core.

**Open UF-072:** compute the one-copy affine-slice elimination ideal and the two-copy coproduct test; compare its Hopf core with the full universal normal-closure Hopf core.


### UF-072A — Structure of the affine-slice image algebra
- Proves that the nilradical of the auxiliary affine-conjugator image algebra is exactly its intersection with the source nilradical \((c,d,h)\).
- Gives the sharp general exponent bound \(\operatorname{Nil}(\mathcal A_{\rm aff})^6=0\) and the Krull-dimension upper bound \(\dim\mathcal A_{\rm aff}\leq10\), from its ten-dimensional reduced parameter base.
- Does not claim the image dimension is ten, compute elimination generators, or establish Hopf stability. UF-072B identifies the reduced image exactly and proves its dimension is seven; UF-072C lifts through the nilpotent filtration.


### UF-072B — Exact reduced affine-slice image
- Proves that every reduced affine-linear conjugator \(g(x)=ax+bz,\ g(z)=iz\) centralizes every element of \(U\) in characteristic two.
- Identifies the reduced affine-slice image algebra exactly as \(k[A,B,C,D,E,G,J]\), with dimension seven (not merely at most ten).
- Distinguishes this reduced centralization result from the still-open nilpotent translation thickening and two-independent-copy coproduct test (UF-072C).


**UF-072D:** the nine-generator first-order source-expansion map has exactly two invisible generators, the constant coefficients (X_1) and (Z_1). The true relation module in the nilradical conormal layer is contained in their span; deciding whether they lie in the square of the nilradical remains UF-072E.


**UF-072F:** exact quadratic initial multiplication matrix has rank 24 over \(\operatorname{Frac}(S)\), with four initial relations. The degree-two source layer is four-dimensional; higher-order contributions to \(\mathcal N^2/\mathcal N^3\) remain unresolved.


**UF-072G:** proves (n_2^2=n_5^2=0) exactly. Its corrected cubic calculation gives a finite-field triple-product rank of 60; adjoining the corrected initial term of n_2n_5 leaves rank 60, while adjoining that of n_2n_6+n_3n_5 raises it to 61. The exact generic cubic relation module remains open.


**UF-072G correction:** the cubic term of \(n_2n_5\) has zero \(cdh\)-coordinate. A reproducible finite-field calculation gives ranks 60 (triple products), 60 (plus \(n_2n_5\)), and 61 (plus \(n_2n_6+n_3n_5\)); the former two-independent-generic-classes claim is withdrawn. See [the certificate](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072g_cubic_specialization.py).


**UF-072H:** exact elimination over F_2(A,B,C,D,E,G,J) gives generic cubic triple-product rank 60. The corrected n_2n_5 vector leaves this rank unchanged; n_2n_6+n_3n_5 raises it to 61. Exact certificate: [uf072h_generic_cubic_rank.py](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072h_generic_cubic_rank.py). The full N^2/N^3 remains open.


**UF-072I:** exact generic elimination shows the cubic triple-product rank rises from 60 to 70 after adding cubic initial terms of n_1n_j and n_4n_j, and to 71 after adding n_2n_6+n_3n_5. The first two graded pieces of N^2/N^3 contribute 24+11=35 generic dimensions; higher layers remain open. Certificate: [uf072i_degree3_pair_product_rank.py](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072i_degree3_pair_product_rank.py).


**UF-072J:** proves n_1^2=n_4^2=0 exactly and computes in_4(n_1n_4)=A^2 c^3d/(ai). Whether this product survives modulo N^3 remains open; the degree-four initial image of N^3 is the next target.



undefined



## UF-072L — Corrected degree-four checkpoint

A term-by-term comparison with UF-065 now confirms the patched quadratic inputs, including Q7. This is an input-table audit only; no degree-four ranks are currently claimed.

The subsequent audit also found a missing factor of `a` in the `dh`-coefficient of `Q_7`. The 175/176 ranks are withdrawn. The certificate has been patched, but no new ranks are claimed until the full calculation is rerun. See [the certificate](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072k_degree4_specialization.py).

### UF-072O — Degree-four test-space completeness
The 350-column construction accounts for every source-degree-four initial contribution from N^3: 84 corrected triple products, 56 n1/n4-pair products, and 210 fourfold products arising from multiplication by an algebra generator. This is a completeness result only; no degree-four rank is certified. A target outside the generic K-span proves nonmembership in N^3, while membership in that K-span still requires an integral S-module argument.


### UF-072P — Fresh degree-four specialization lower bounds
The rebuilt 350-column, 470-row degree-four matrix gives ranks 172 and 173 after adjoining in4(n1*n4), respectively, at three listed F_256 specializations. These imply generic lower bounds only; the matching symbolic upper bound 172 is still needed to prove a generic strict rank gap. The certificate records the specialization test: [uf072k_degree4_specialization.py](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072k_degree4_specialization.py).

Execution audit: all three tuples in the certificate were run and each returned ranks (172,173). The earlier count of five was erroneous; only three specializations are claimed.

### G-7 — Quadratic Galois cohomology in characteristic two
For a separable quadratic extension (L/K) in characteristic two, let (C_2=\operatorname{Gal}(L/K)) act on a finite-dimensional module (V), and put (N=\sigma-1). The norm equals (N), so the standard two-periodic resolution gives
\[
H^q(C_2,V)=\ker N/\operatorname{im}N\quad(q\ge1).
\]
If (m=\dim V) and (r=\operatorname{rank}N), this dimension is (m-2r). In fact (V≅k[C_2]^r⊕k^{m-2r}), so positive cohomology counts the trivial Jordan blocks. The inflation–restriction transgression from (H^1(G_L,V)^{C_2}) lands in this explicit (H^2(C_2,V^{G_L})), giving a concrete order-two descent obstruction. This does not construct a global Fold Galois representation; that remains the next arithmetic task. See [the applicability and Galois note](the-fold-automorphic-and-hopf-galois-applicability.md).



### G-8 — Cyclic 2-power Galois cohomology
For a cyclic quotient (C_q), (q=2^n), in characteristic two, set (D=\sigma-1). Then (k[C_q]=k[D]/(D^q)), and the norm is (D^{q-1}). The two-periodic cyclic resolution gives odd cohomology (\ker D^{q-1}/\operatorname{im}D) and even positive cohomology (\ker D/\operatorname{im}D^{q-1}). Each nilpotent Jordan block of length less than (q) contributes one dimension in every positive degree; a length-(q) block is free and contributes zero. Thus positive cohomology counts the non-projective indecomposable blocks. Inflation–restriction places the descent obstruction in (H^2(C_q,V^{G_L})). See [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-9 — Explicit cyclic-cohomology representatives
For a Jordan chain \(De_j=e_{j-1}\) of length \(d<q=2^n\), the top vector \(e_{d-1}\) represents its basis class in \(H^1(C_q,V)\), and the bottom vector \(e_0\) represents its basis class in \(H^2(C_q,V)\). A length-\(q\) block contributes zero because its top is a D-boundary and its bottom is a norm. Thus G-8 has explicit representative-level bases, not only a dimension formula. Evaluating a Galois transgression still requires a specified extension and module.

### G-10 — Cochain-level Galois transgression
The Hochschild–Serre transgression can be computed from an invariant class \([\alpha]\in H^1(N,V)^Q\): extend a representing 1-cocycle on N to a 1-cochain on G, choose the extension so its coboundary descends to a 2-cocycle on Q with values in \(V^N\), and take that cohomology class. For a cyclic 2-power quotient in characteristic two, G-8 identifies the quotient \(H^2=\ker D/\operatorname{im}D^{q-1}\), and G-9 gives explicit Jordan-chain representatives. A Fold-specific arithmetic computation still requires a concrete extension, module, and invariant cocycle.

### G-11 — Cyclic cocycle-sum obstruction vector
For a normalized inhomogeneous 2-cocycle \(\tau\) on \(C_q=\langle\sigma\rangle\), using multiplication \((w,g)(w',g')=(w+gw'+\tau(g,g'),gg')\), its extension class in \(H^2(C_q,W)=W^{C_q}/N W\) is represented by \(w_\tau=\sum_{j=0}^{q-1}\tau(\sigma^j,\sigma)\). In characteristic two the norm is \(D^{q-1}\). Thus the G-10 transgression can be reduced to one invariant vector, then tested against the short Jordan-block bottom-vector coordinates from G-9. This is a general computational criterion; a Fold-specific arithmetic input is still open. See [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-12 — Explicit cyclic quartic test case
Over \(K=\mathbb F_2(s)\), set \(u^2+u=s\) and \(w^2+w=u^3+u\). The odd pole order three proves the second Artin–Schreier equation is nontrivial. The automorphism \(\sigma(u)=u+1,\ \sigma(w)=w+u+1\) has square \(\sigma^2(w)=w+1\), so this is an explicit cyclic quartic extension. Its additive regular module \(L\) is projective by the normal basis theorem, while trivial coefficients \(\mathbb F_2\) have \(H^1=H^2=\mathbb F_2\). This isolates the coefficient-module dependence of the G-8 obstruction; an actual nonzero transgression remains open. See [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-13 — cyclic octic lift and nonzero transgression
The explicit G-12 cyclic quartic extension (L/K) lifts to a cyclic octic extension (M/K): the Artin–Schreier–Witt truncation (W_3(K)/(F-1)\to W_2(K)/(F-1)) is surjective, and any lift of the order-four character has order eight. For (1\to C_2\to C_8\to C_4\to1) with trivial (mathbb F_2)-coefficients, restriction (H^1(C_8,\mathbb F_2)\to H^1(C_2,\mathbb F_2)) is zero. The five-term sequence therefore makes the transgression (H^1(C_2,\mathbb F_2)^{C_4}\to H^2(C_4,\mathbb F_2)) an isomorphism. This supplies a concrete nonzero finite-group transgression; an explicit third Witt coordinate and a Fold-specific arithmetic realization remain open. Details: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-14 — explicit cyclic octic equations
The G-12 quartic extension is represented by the length-two Witt vector \((s,s)\). Its length-three lift \((s,s,0)\) gives the explicit cyclic-octic tower
\[
u^2+u=s,\quad w^2+w=u^3+u,\quad
v^2+v=u^7+u^4+u^3w^2+u^3w+u^2w^2+u^2w+w^3+w^2.
\]
A generator is \(\sigma(u)=u+1,\ \sigma(w)=w+u,\ \sigma(v)=v+u^3+uw+u\); its square sends \((w,v)\) to \((w+1,v+w)\), and its fourth power sends \(v\) to \(v+1\). Thus the G-13 nonzero transgression example now has explicit field equations. The remaining arithmetic task is a Fold-specific realization. See [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-15 — explicit cyclic factor set
For (C_8\twoheadrightarrow C_4), the section (s(i)=g^i) gives (\tau(i,j)=\lfloor(i+j)/4\rfloor\bmod2). Its G-11 cyclic sum is (w_\tau=\sum_{j=0}^3\tau(j,1)=1), the nonzero generator of (H^2(C_4,\mathbb F_2)) with trivial coefficients. This explicitly identifies the G-13 transgression with the cyclic cocycle-sum obstruction. The Fold-specific realization remains open; see [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-16 — uniform cyclic (2)-power transgression family
For every (r\ge1), (1\to C_{2^r}\to C_{2^{r+2}}\to C_4\to1) has an isomorphism transgression (H^1(C_{2^r},\mathbb F_2)^{C_4}\to H^2(C_4,\mathbb F_2)). The restriction map from the larger cyclic group is zero, so five-term exactness proves injectivity; both spaces are one-dimensional. The pushed-out factor set is (\tau(i,j)=\lfloor(i+j)/4\rfloor\bmod2), whose cyclic sum is 1. Arithmetic realization in all lengths and a Fold-specific interpretation remain open. Details: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-17 — arithmetic realization in every Witt length
Every G-16 cyclic extension is realized over (K=\mathbb F_2(s)): for each (n\ge2), the length-(n) Witt vector ((s,s,0,\ldots,0)) defines a cyclic extension of degree (2^n), because its first coordinate (s) is not Artin–Schreier (odd pole order at infinity). Its length-two truncation is the explicit G-12 quartic class. The Witt equation specifies all levels; expanded coordinate polynomials beyond length three and a Fold-specific interpretation remain open. See [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-18 — arbitrary cyclic quotient transgression
The G-16/G-17 result extends from quotient C4 to every C_(2^m): for all r,m≥1, the extension \(1\to C_{2^r}\to C_{2^{r+m}}\to C_{2^m}\to1\) has an isomorphism transgression with trivial \(\mathbb F_2\)-coefficients. Its explicit pushed-out factor set \(\tau(i,j)=\lfloor(i+j)/2^m\rfloor\bmod2\) has cyclic sum 1. Every pair (r,m) is realized over the single field \(\mathbb F_2(s)\) by the Artin–Schreier–Witt vector \((s,s,0,\ldots,0)\) of length r+m. The theorem is not yet Fold-specific; see [the Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-19 — transgression as a pushout extension class
For an abelian-kernel extension and a quotient-invariant character of the kernel into a coefficient module on which the kernel acts trivially, the Hochschild–Serre transgression is the pushout extension class (up to the standard factor-set sign). In G-18, the nonzero character sends the cyclic carry factor set to the explicit cocycle with cyclic sum 1. This explains the obstruction as nonsplitting of the pushed-out extension. It remains a group-cohomological result, not yet a Fold-derived construction; details and reference are in the Galois applicability note.


### G-20 — arbitrary quotient-module transgression
For the cyclic extension in G-18 and any (possibly nontrivial) \(\mathbb F_2[C_{2^m}]\)-module A, the transgression from invariant kernel characters is the quotient map \(A^{C_{2^m}}\to A^{C_{2^m}}/N_QA=H^2(C_{2^m},A)\). It is surjective, and its kernel is exactly the norm image. In Jordan form it detects precisely the short blocks; full-length free blocks contribute zero. Details and proof are in the Galois applicability note. This is not yet Fold-specific.


**Galois cohomology — explicit degree-16 tower (G-21):** the cyclic Artin–Schreier–Witt family over \(\mathbb F_2(s)\) is now expanded through length four. The quartic and octic truncations are joined by a fully written fourth Witt coordinate and the exact order-16 generator translation. The degree follows from the odd pole order of the first coordinate \(s\). This remains an arithmetic model, not yet a Fold-derived Galois representation or Selmer class; see the-fold-automorphic-and-hopf-galois-applicability.md.


**Galois cohomology — degree-16 ramification (G-22):** the explicit cyclic degree-16 Artin–Schreier–Witt cover has upper breaks \((1,2,4,8)\), lower breaks \((1,3,11,43)\), different exponent \(100\), and genus \(35\). The conductor-discriminant sum independently gives the same different exponent. See the-fold-automorphic-and-hopf-galois-applicability.md for the calculation and scope.


**Galois cohomology — tower \(2\)-rank (G-23):** all four curves in the one-point cyclic \(2\)-power tower have geometric \(2\)-rank zero by Deuring–Shafarevich. Their genera are \(0,1,7,35\); the genus-one intermediate curve is supersingular. The higher-genus Newton polygons and \(a\)-numbers remain undetermined.


**Galois cohomology — quartic elliptic quotient Frobenius (G-24):** identifies the genus-one intermediate curve as \(y^2+y=x^3+x\), counts five \(\mathbb F_2\)-points, and obtains Frobenius polynomial \(T^2+2T+2\). Its trace \(-2\) confirms supersingularity independently of the Deuring–Shafarevich argument. Higher-genus Jacobian Newton polygons remain open; see the Galois applicability note.


**Galois cohomology — genus-seven Jacobian Frobenius (G-25):** exact finite-field counts over \(\mathbb F_{2^m}\), \(1\le m\le10\), determine the genus-seven octic curve's Weil polynomial
\[
1+6T+20T^2+48T^3+90T^4+140T^5+196T^6+272T^7+392T^8+560T^9+720T^{10}+768T^{11}+640T^{12}+384T^{13}+128T^{14}.
\]
Degrees 8–10 provide independent checks. Reproducible exact enumeration: `certificates/g24_genus7_weil_polynomial.py`. The genus-35 Jacobian remains open; see the Galois applicability note.


**Galois cohomology — genus-seven Jacobian decomposition (G-26):** the G-25 Weil polynomial factors as \((1+2T^2)^2(1+2T+2T^2)Q(T)\), where Q has degree eight. The Jacobian is isogenous to the corresponding two elliptic factors (the first repeated twice) and a four-dimensional factor with polynomial Q. Its exact Newton slopes are \(1/4\) four times, \(1/2\) six times, and \(3/4\) four times. Thus its 2-rank is zero but it is not supersingular. Exact factorization/Newton-hull certificate: "certificates/g26_genus7_newton_polygon.py". The residual factor's further decomposition and the genus-35 Jacobian remain open.


**Galois cohomology — simple four-dimensional factor (G-27):** the degree-eight Frobenius factor of the genus-seven Jacobian is irreducible over Q. Its Newton polygon forces any proper rational factor to be quartic; Weil bounds reduce quartic candidates to 12,650, all excluded by exact integer division. The corresponding four-dimensional isogeny factor is simple, with slopes 1/4 four times and 3/4 four times. Certificate: "certificates/g27_degree8_irreducibility.py".


**Genus-seven CM field (G-28):** the simple fourfold's Frobenius field is an explicit degree-eight CM field. Its maximal real subfield is generated by \\(\\beta=\\pi+2/\\pi\\), with minimal polynomial \\(Y^4+4Y^3-2Y^2-20Y-14\\). The resultant identity and irreducibility certificate are in `certificates/g28_cm_real_subfield.py`; the polynomial discriminant is \\(2^8\\cdot17\\) (not yet asserted to be the field discriminant). See `the-fold-genus7-cm-field.md`.


**CM extension arithmetic (G-29):** the real quartic has full ring of integers `Z[beta]` and field discriminant `2^8 * 17`. The quadratic CM extension `Q(pi)/Q(beta)` is unramified at every finite prime; its unique prime above 2 splits. Exact checks are in `certificates/g29_cm_extension_arithmetic.py`, with the argument and scope in `the-fold-genus7-cm-field.md`.


**Real quartic class number (G-30):** the ordinary class number of Q(beta) is one. Minkowski's bound is (3/2)*sqrt(17) < 7; 3 and 5 are inert, and the unique prime above 2 is generated by beta+2. See `certificates/g30_real_quartic_class_number.py` and the CM-field note. The narrow class number is not yet claimed.


**Narrow class field (G-31):** three explicit norm-one units generate all eight even-parity signatures. Together with h_K=1 and the finite-unramified CM quadratic extension, this proves h_K^+=2 and identifies Q(pi)/Q(beta) as the narrow Hilbert class field. Exact unit norm and rational interval-sign checks are included in `certificates/g30_real_quartic_class_number.py`.


**CM splitting and Newton slopes (G-32):** the two local factors of the CM quadratic at the prime above 2 have normalized valuations 1/4 and 3/4. Each local degree-four factor contributes four conjugates, recovering the simple fourfold slopes (1/4)^4 and (3/4)^4 from the CM prime decomposition.


**CM Artin splitting (G-33):** the narrow Hilbert class field description yields an explicit Frobenius character: for a principal ideal \((\alpha)\) of the real quartic, its Artin symbol is determined by the sign of \(N(\alpha)\). This predicts and verifies the factorization of the degree-eight Frobenius polynomial modulo 3, 5, and 7: two irreducible quartics at 3 and 5, and four irreducible quadratics at 7. Exact modular products and irreducibility checks: `certificates/g33_cm_artin_splitting.py`; derivation: `the-fold-genus7-cm-field.md`.


**Odd CM class number (G-34):** the ambiguous class number formula, four ramified infinite places, and the previously computed order-eight unit-signature image show that the degree-eight CM field has trivial ambiguous class group. Since the real quartic class number is one, complex conjugation acts by inversion on the CM class group; hence its 2-torsion is trivial and its class number is odd. The odd part and exact class group remain open. Details: `the-fold-genus7-cm-field.md`.
