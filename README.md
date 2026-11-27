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

**What the corpus found.** Six results survived the zones, and each moved the argument rather than
adding a note:

- **A theorem ledger.** Of twelve theorems read for premise closure, six have every premise in the
  Fold, three are exact reformulations, and three remain rhymes; the missing premise, not the
  resemblance, is the finding (`the-fold-theorems.md`).
- **Ten words, six hosts.** The physical words the Fold cannot reach reduce to six structures —
  measure, flow, bath, cut, bundle, inertia — and the first four are the AGI's adjunctions
  (`the-fold-void.md`).
- **Probability moved first.** It was the row expected to resist, and it is the one that moved: on a
  finite `ℤ/n` the counting measure, the quotient `z(1−z)`, and the doubling action are exact; what
  remains missing is independent trials and the Born rule.
- **Doubling has two period sets.** `n ∣ 2^k − 1` returns the identity, `n ∣ 2^k + 1` reaches the fold,
  and for `n > 2` no `k` does both (`the-fold-lean.md`).
- **The minimal operation family is a cyclicity test.** Every information costs at most one scale if and
  only if `U(n)` is cyclic; the maximum cost is `rank U(n)`, which is unbounded; the fold fixes the even
  half of the character lattice and never costs zero (`the-fold-minimal-operations.md`).
- **Reuse, not citation count.** The corpus draws 377 note-to-note edges over 63 notes, 5.98 per note;
  fifteen notes are cited by nothing, thirteen of them research notes outside the zone map, and the two
  fold-note orphans are the ones that ask what the exercise is for (`the-fold-value.md`).

**Formal core:** `lake build` compiles a dependency-free Lean 4 library in `Fold/` — the fold as an
involution, its fixed set and quotient, the observer as a cut, the scale action, doubling's two period
sets, the cap/puncture ledger, the calendar arithmetic, the wheel's closure, and four finite
counterexamples. The build proves the skeleton, not the rhymes; the map is `the-fold-lean.md`.

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

**Minimal operations:** a family of scales preserving a character is its kernel, so "how few
operations" is a question about `U(n)`. Every level of information, the constant included, costs at
most one scale exactly when `U(n)` is cyclic (`n = 1, 2, 4, p^k, 2p^k`), and the maximum cost is
`rank U(n)`, which is unbounded.
The fold is not one of the counted operations: `χ(−1) = ±1`, so it preserves exactly the even half of
the character lattice, and a faithful character is odd, so the information the fold preserves never
costs zero. Doubling's two period sets, `n ∣ 2^k − 1` and `n ∣ 2^k + 1`, are disjoint for `n > 2`. See
`the-fold-minimal-operations.md`.

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
| abstraction, concepts, and executable proposal generation | [agi/abstraction-and-concepts.md](agi/abstraction-and-concepts.md); [Stage 9 proposal generation](agi/stage-9-proposal-generation.md); [Stage 10 compound units](agi/stage-10-compound-units.md); [Stage 11 typed affine quantities](agi/stage-11-typed-affine-quantities.md); `agi/concept_learner.py`; `agi/concept_proposer.py`; tests in `agi/test_concept_*.py` |
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
| the arithmetic of the four date labels, and why `τ` and `mod 99` disagree | `the-fold-date-numbers.md` |
| how few operations preserve a chosen amount of information | `the-fold-minimal-operations.md` |
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
| [agi/abstraction-and-concepts.md](agi/abstraction-and-concepts.md) | AGI research note: task-relative concepts, quotient abstraction, typed relations, invariants, and counterexample-driven revision |
| [agi/stage-9-proposal-generation.md](agi/stage-9-proposal-generation.md) | Stage 9: exact unit-aware concept proposals, hard negatives, and scope limits |
| [agi/stage-10-compound-units.md](agi/stage-10-compound-units.md) | Stage 10: compound-unit parsing, dimensional exponent vectors, and exact normalization |
| [agi/stage-11-typed-affine-quantities.md](agi/stage-11-typed-affine-quantities.md) | Stage 11: semantic quantity kinds, affine temperature conversion, and interval distinctions |
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
| `the-fold-date-numbers.md` | follow-up note: the date numbers - the four labels, the block lemma for `mod 99`, the divisor counts `80` and `8`, and what the date does not determine |
| `the-fold-lean.md` | formal core: the Lean 4 project - involution, quotient, cut, scale, chi, the wheel, the doubling action, and the finite counterexamples |
| `the-fold-minimal-operations.md` | follow-up note: the minimal operation family - the character lattice, cost as the rank of a kernel, cyclicity as the dividing line, and the fold as the parity |

### Research notes

The characteristic-two and Hopf notes are indexed here but sit outside the zone map: they are research
papers with their own theorem numbering, not fold notes with zone tables.

- `the-fold-d4-characteristic-two.md` — UF-032: the characteristic-two D4 module and bracket
- `the-fold-char2-identity-kernel.md` — UF-037: the identity-linear kernel and its normal closure
- `the-fold-char2-homogeneous-space.md` — UF-038: the homogeneous space `H/U` and the class-two normal closure
- `the-fold-char2-frobenius-normal-closure.md` — UF-040: the Frobenius-kernel candidate for the infinitesimal normal closure
- `the-fold-char2-second-frobenius-closure.md` — UF-041: the second-Frobenius quotient and a canonical thickening
- `the-fold-char2-reduced-quotient-law.md` — UF-042: the explicit five-dimensional reduced quotient
- `the-fold-char2-second-frobenius-hopf-ideal.md` — UF-043: the explicit Hopf ideal and the size of the second-Frobenius candidate
- `the-fold-char2-universal-hopf-ideal.md` — UF-044: the universal Hopf-ideal characterization of the normal closure
- `the-fold-char2-fourteen-coordinate-conjugation-test.md` — UF-055: the fourteen-coordinate conjugation audit and an exact cubic test
- `the-fold-char2-full-affine-ch-coefficient.md` — UF-060: the full determinant-open affine `ch` coefficient
- `the-fold-char2-nontrivial-cocycle-hopf-structure.md` — a fifth, non-product Hopf structure on the characteristic-two Fold algebra
- `the-fold-char2-quaternion-boundary-arithmetic.md` — G-4f: arithmetic of the quaternion boundary over imperfect fields
- `the-fold-automorphic-and-hopf-galois-applicability.md` — applicability audit: automorphic methods and Galois theory for the Fold algebra

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
zone map: 13 files with zone tables of 64
     exact           143
     reformulation    10
     rhyme            24
     false friend     15
     the absence       1
     without tables    51
     legend (definitions, not claims)    11

prose attributions: 53 files of 64
     exact           173
     reformulation    10
     rhyme            22
     false friend     39
     total           244
```

The tables are the formal layer and cover thirteen files. The prose is where the corpus actually works:
fifty-three of sixty-four files label their comparisons in the predicative form — a noun phrase
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
status markers (marked by contrast, zone not named): 30 files of 64
     total            57
     derivation       20
     about             8
     proof             6
     identity          6
     boost             2
     theorem           6
     other             9
     no zone language     9
```

The objects are the finding. Twenty say "not a derivation", six "not a proof", six "not a theorem",
and one "not a reduction": thirty-three point at proof. One of those is not a claim — "the Fold is a
dictionary, not a proof engine" — and one "not the identity" is a list of what a point is not, so the
fifty-seven marked sentences carry fifty-five claims, and thirty-two of them say that nothing was proved.
That is the corpus's own definition of **reformulation**, yet the word appears as a label twenty times,
ten in tables and ten in prose. The middle zone is not scarce; it is unnamed, and the corpus says it
with a contrast instead of a noun.

The remaining objects do different work. "Not an identity", "not about", "not a boost" use one word
in two senses, which is false-friend work rather than a zone; "not a law", "not a model", "not a
result" separate a description from a mechanism.

With that count the map closes on fifty-five of the sixty-four files: the nine research notes listed
above carry no zone language at all. The three notes that looked silent in the first two counts —
`the-fold-closure.md`, `the-fold-division.md`, `the-fold-horizon.md` — mark exactly once each, and each
mark is the one that matters:

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

---

# Engineering and research milestone ledger

**Rational-canonical regular-pencil witness integration (G-EP46):** the shared-chart path in `tools/regular_pencil_witness.py` now keeps its cyclic Krylov fast path and, for noncyclic normalized operators, falls back to full rational-canonical bases from G-EP45. It constructs (P=K_BK_A^{-1}), then (S=H_bPH_a^{-1}), (T=P^{-1}), and exactly verifies both original pencil equations and invertibility. If bounded basis construction is incomplete, the prior intertwiner-space fallback remains available. The no-chart path is unchanged and still uses bounded direct search. See the G-EP45/46 research note and the noncyclic regression test.


**Composable Kronecker component assembly (G-EP47):** `tools/kronecker_component_assembly.py` composes structural recovery of individual right/left singular blocks with regular-pencil canonical witnesses. Given a proposed component partition, it assembles the block-diagonal target and block-diagonal (S,T), then independently verifies (SQT=Q_{\\rm can}) and (SKT=K_{\\rm can}). This is certified assembly, not automatic discovery of the component partition from an arbitrary unsplit pencil. See `tests/test_kronecker_component_assembly.py` and `research/the-fold-kronecker-component-assembly.md`.


**Multiple-chain pure singular recovery (G-EP48):** `tools/pure_singular_pencil_recovery.py` recovers any number of right-only or left-only singular Kronecker blocks from the full pencil, including after arbitrary constant basis scrambling. It uses certified polynomial minimal-vector chains, constructs domain/codomain bases, and verifies explicit global strict-equivalence transformations. It does not yet recover a regular summand or mixed left/right pencils. See `tests/test_pure_singular_pencil_recovery.py` and `research/the-fold-pure-singular-pencil-recovery.md`.

**Bounded automatic mixed Kronecker recovery (G-EP49):** `tools/mixed_kronecker_recovery.py` discovers the right and left minimal-index lists and regular elementary divisors from one unsplit pencil, assembles the mixed canonical target, and searches structured invertible left transforms while solving exactly for the right transform. Every positive result passes the strict-equivalence audit. The witness search is deliberately bounded and its candidate family is not universal; failure is inconclusive, not a proof of inequivalence. See `tests/test_mixed_kronecker_recovery.py` and `research/the-fold-mixed-kronecker-recovery.md`.

**Exhaustive mixed-pencil witness mode (G-EP50):** `recover_mixed_kronecker_pencil(..., search_mode="exhaustive")` streams all left matrices over the finite field and all compatible affine right-transform solutions, under an explicit candidate budget. A found witness is exactly audited; a fully exhausted negative search is a finite-field non-equivalence certificate; budget exhaustion is inconclusive. Exponential by design, intended for small cases. See `research/the-fold-mixed-kronecker-recovery.md`.

**Minimal-chain geometry certificates (G-EP51):** `tools/minimal_chain_geometry.py` computes exact ranks of the right minimal-vector coefficient family in the domain and the left minimal-covector family in the codomain. It returns the underlying bounded nullspace certificate and explicitly distinguishes independence from a full mixed decomposition: complementary regular bases and cross-chain compatibility are not inferred. See `research/the-fold-minimal-chain-geometry.md` and its tests.

**Minimal-chain adapted coordinates (G-EP52):** `tools/minimal_chain_adapted_coordinates.py` builds full domain and codomain bases beginning with independent right-chain coefficient vectors and left-chain coefficient covectors. It returns (Q'=SQT), (K'=SKT), and exact invertibility/identity checks. Complementary coordinates are exposed without asserting that the residual block is regular or decoupled. See `research/the-fold-minimal-chain-adapted-coordinates.md`.


**Residual-pencil diagnostics (G-EP53):** `tools/residual_pencil_diagnostic.py` partitions the G-EP52 adapted pencil into chain and complementary coordinate blocks, reports cross-coupling, and profiles the bottom-right block when it is nonempty and square. The residual profile is explicitly coordinate-local; it is not claimed to be the original pencil's regular part unless decoupling is separately established. See `research/the-fold-residual-pencil-diagnostic.md`.

**Exact residual-pencil decoupling certificates (G-EP54):** `tools/residual_pencil_decoupling_certificate.py` checks both off-diagonal blocks in both adapted coefficient matrices, reports exact ranks and nonzero entries, and reconstructs the block-diagonal pair for equality checks against the adapted pencil. A positive result certifies a direct-sum split in the computed coordinates and carries the G-EP52 strict-equivalence witnesses; a negative result exposes coupling without claiming decomposition or residual regularity. See `tests/test_residual_pencil_decoupling_certificate.py` and `research/the-fold-residual-pencil-decoupling-certificate.md`.

**Minimal-chain annihilator complements (G-EP55):** `tools/minimal_chain_decoupling_completion.py` searches for complementary domain vectors in the common kernel of the left-chain constraints and complementary codomain covectors annihilating both coefficient images of the right-chain space. When both spaces extend the fixed chain bases, it constructs exact S,T witnesses and verifies both cross-coupling blocks vanish. Failure is explicitly inconclusive and does not rule out other splittings. See `tests/test_minimal_chain_decoupling_completion.py` and `research/the-fold-minimal-chain-decoupling-completion.md`.

**Minimal-chain annihilator feasibility certificates (G-EP56):** extends G-EP55 with exact rank criteria for whether the fixed right/left chain spans can be completed inside their computed annihilator spaces. It reports combined-span ranks, ambient dimensions, deficiencies, and feasibility flags. These criteria are necessary and sufficient within those fixed spaces; because each nullspace basis spans the full candidate space, exhaustive enumeration of linear combinations would be redundant. A deficient rank rules out only this particular annihilator-based completion, not other possible pencil splittings. See `research/the-fold-minimal-chain-annihilator-feasibility.md` and the updated tests.

**General direct-sum witness verifier (G-EP57):** `tools/pencil_direct_sum_witness.py` independently verifies a supplied constant strict-equivalence witness for a two-block direct sum of a rectangular pencil. It accepts arbitrary invertible left/right transforms and a compatible rectangular block cut, recomputes both transformed coefficients, and checks both off-diagonal blocks exactly over the prime field. This separates general witness verification from G-EP55/56's restricted annihilator-based construction. It does not discover a decomposition or assert regularity of either summand. See `tests/test_pencil_direct_sum_witness.py`.


**Multi-block direct-sum witness verifier (G-EP58):** `tools/pencil_multi_direct_sum_witness.py` independently verifies a supplied constant strict-equivalence witness for two or more rectangular diagonal pencil blocks. It checks the ordered block-shape partition, invertibility of both transforms, and every off-diagonal block in both transformed coefficient matrices over the prime field. It audits supplied decompositions without assuming regularity or discovering the split. See `research/the-fold-multi-block-direct-sum-witness.md` and `tests/test_pencil_multi_direct_sum_witness.py`.


**Integrated multi-block audit of mixed recovery (G-EP59):** successful `recover_mixed_kronecker_pencil` results now include `canonical_block_shapes` in canonical construction order and a `multi_block_direct_sum_audit` from G-EP58. The audit independently checks the recovered S,T against each right-minimal, left-minimal, and regular diagonal block, in addition to the existing whole-target strict-equivalence audit. This is a second exact certificate view, not a new discovery method; negative or budget-limited searches retain their previous semantics. See the updated mixed-recovery tests.


**Integrated multi-block audit of supplied component assembly (G-EP60):** successful `assemble_kronecker_components` results now include `canonical_block_shapes` in the supplied component order and an independent `multi_block_direct_sum_audit` from G-EP58. The audit verifies that the assembled block-diagonal transforms annihilate every cross-component block in both pencil coefficients, alongside the existing whole-pencil strict-equivalence audit. Failed component recovery still returns an incomplete result without a success certificate; this remains supplied-partition assembly, not decomposition discovery. See `research/the-fold-kronecker-component-assembly.md` and its tests.


**Component-report consistency certificate (G-EP61):** successful `assemble_kronecker_components` results now include `component_consistency_audit`. It cross-checks each reported source shape against both source coefficients, checks both canonical coefficient block shapes, validates right/left singular block dimensions against their recovered minimal indices and regular block squareness, and reconciles ordered component dimensions with the assembled source and canonical shapes. This is a metadata/matrix consistency audit, not independent component classification or decomposition discovery.


**Per-component strict-equivalence certificates (G-EP62):** supplied-partition assembly now independently audits each component's own (S_i,T_i) against its source and canonical pair before composing the global block-diagonal witness. Successful results expose ordered `component_witness_audits` and an aggregate `all_component_witnesses_verified` check, alongside the existing global, multi-block, and metadata-consistency audits. This localizes a component witness failure rather than relying only on the assembled identity; it does not discover a partition. See `research/the-fold-kronecker-component-assembly.md` and its tests.
\n\n**Component witness composition audit (G-EP63):** supplied-partition assembly now rebuilds the global block-diagonal S and T solely from the ordered local component certificates, compares them with the returned assembled transforms, and replays both global pencil identities using the reconstructed matrices. Successful results expose `component_witness_composition_audit` and `component_witness_composition_verified`. This independently checks composition consistency; it does not discover a partition or establish uniqueness. See the component-assembly research note and tests.\n

**Adversarial component-witness composition checks (G-EP64):** the G-EP63 composition audit now validates every local left/right transform as a nonempty square matrix before block-diagonal assembly, and rejects empty or malformed certificate sequences with explicit `ValueError` diagnostics. Regression tests tamper with a local transform and verify both transform-comparison and global replay checks fail; dimension-incompatible and malformed certificates are rejected. Reordering is not treated as inherently invalid: when local transforms are interchangeable (for example, identity witnesses of compatible dimensions), order alone need not change the mathematics. See `tests/test_kronecker_component_assembly.py` and the component-assembly research note.


**Component certificate provenance and binding (G-EP65):** the composition audit now independently re-runs strict-equivalence verification for every local (S_i,T_i) against that component's own source and canonical coefficient pair. It checks certificate/block-list cardinalities, exposes the per-component replay audits, and includes an aggregate source/target-binding check. The stored boolean from an earlier local audit is not trusted as a substitute for recomputation. The global composition and transform-equality checks remain separate. See the component-assembly research note and adversarial tests.


**Component certificate mutation and replay integrity (G-EP66):** the composition audit now validates all four ordered block lists and their cardinalities before indexing or replaying any component. Adversarial tests change a bound source block and a bound canonical block while retaining the old transforms, and verify that fresh local replay fails even when stored success metadata is forged. A complementary regression proves that forged stored failure metadata cannot suppress a mathematically valid recomputed certificate. This tests mutation sensitivity for the supplied ordered component pairs; it does not establish component discovery, identity outside that ordering, or uniqueness.


**Component input and dimension integrity (G-EP67):** supplied component matrices are now validated at the assembly boundary before modular arithmetic. Matrix and row containers must be nonempty ordered sequences, rows must be rectangular with nonzero width, entries must be integers (booleans and floating-point values are rejected), and each Q/K pair must have identical dimensions. Field parameters are checked as genuine integers (not booleans) before primality validation. Regression coverage includes malformed containers, ragged/empty matrices, non-integral entries, invalid/composite fields, and Q/K dimension mismatches. This hardens input diagnostics without changing the allowed rectangular component shapes or the supplied-partition scope.


**Independent reconstruction of assembly certificates (G-EP68):** adds `verify_kronecker_component_assembly_certificate`. Given the original ordered component inputs and a returned assembly result, it deterministically reruns the component constructors and compares source/canonical matrices, dimensions, block shapes, local and global transforms, component reports, and all stored audits/checks. Adversarial regressions mutate each certificate-bearing field and require detection. This is independent of the supplied output object, but intentionally reuses the existing constructors: it is an implementation-level reconstruction/replay check, not a second classification algorithm, partition-discovery method, or uniqueness proof. See the component-assembly research note.


**Direct algebraic certificate audit (G-EP69):** adds `verify_kronecker_component_assembly_algebraically`, which does not rerun canonical constructors. It rebuilds source block-diagonal matrices from the caller's original inputs, checks the claimed canonical block structure, replays every local and global strict-equivalence identity over the finite field, and verifies that global transforms are exactly the block-diagonal composition of the supplied local witnesses. Adversarial tests cover matrix/transform tampering and show that forged stored audit flags do not control the result. This remains conditional on the supplied component partition and local witnesses; it is not a partition-discovery or uniqueness algorithm.


**Adversarial algebraic assembly-certificate verification (G-EP70):** hardens `verify_kronecker_component_assembly_algebraically` to fail closed on malformed nested certificate structures and malformed canonical/local/global matrices. Certificate matrices and transforms now require rectangular integer entries (booleans and floats are rejected), malformed local witness records cannot leak indexing/type exceptions, and singular or dimension-incompatible transforms fail the algebraic replay. The new adversarial tests cover missing fields, malformed containers and entries, noninvertible local witnesses, invalid field arguments, and malformed component inputs. The verifier still distinguishes malformed caller inputs (explicit `ValueError`) from malformed certificate data (a negative verification result). This remains a verifier for supplied ordered components, not partition discovery or a uniqueness proof.


**Seeded randomized certificate verification (G-EP71):** adds reproducible randomized tests over prime fields F₂, F₃, F₅, and F₇. Generated cases vary right/left singular minimal indices, regular one-dimensional pencil coefficients, and component ordering; every successfully assembled certificate is independently checked by the direct algebraic verifier. A second seeded suite mutates a randomly selected canonical coefficient entry and requires verification to fail. Fixed seeds keep failures reproducible. These tests broaden finite-field and block-layout coverage but are not a probabilistic proof of correctness.


**Seeded basis-scrambled component recovery (G-EP72):** extends randomized coverage by independently applying reproducible invertible constant left/right basis changes to each right-singular, left-singular, and regular component before assembly. The transformed mixed components are shuffled and passed through the existing recovery/canonicalization pipeline; every completed result must pass the direct algebraic certificate verifier. Cases span F₂, F₃, F₅, and F₇ with fixed seeds. This is finite regression evidence for basis-scrambled examples, not a universal recovery theorem or a polynomial-time guarantee.


**Mixed-recovery boundary grid (G-EP73):** adds deterministic positive controls across right/left minimal-index pairs (1,1), (2,1), and (2,2) over F₂, F₃, and F₅, each with a regular block and exact strict-equivalence verification. Additional regressions explicitly distinguish an incomplete profile (degree bound too small) from a complete profile with an exhausted witness-search budget. Both negative outcomes remain inconclusive; neither is reported as a proof of non-equivalence.


**Structured/exhaustive recovery cross-checks (G-EP74):** adds small-field comparisons between bounded structured recovery and exhaustive finite-field witness enumeration. A one-candidate structured search must remain inconclusive, while a larger exhaustive F₂ search resolves the same input with an exact witness. F₂/F₃ positive controls require matching minimal-index profiles and independently verified strict-equivalence witnesses in both modes. Different valid transforms are allowed. Exhaustive negative decisions remain valid only after complete enumeration; budget exhaustion is never a proof of inequivalence. See the G-EP74 section in research/the-fold-mixed-kronecker-recovery.md.


**Exhaustive-search enumeration integrity (G-EP75):** factors exhaustive left-matrix and affine right-transform enumeration into testable iterators. Finite regression tests check exact coverage and duplicate freedom of all left matrices over F₂/F₃ at dimensions one and two, and compare affine-space enumeration with brute-force solutions over F₃. The candidate budget counts both left and right candidates; budget cutoffs remain inconclusive. These finite tests audit enumeration mechanics without claiming a universal proof of the affine solver. See G-EP75 in research/the-fold-mixed-kronecker-recovery.md.


**Independent affine-solver verification (G-EP76):** exhaustively compares `_solve_affine` with independently enumerated solution sets for every coefficient matrix and right-hand side with zero through two equations and variables over F₂ and F₃. It checks inconsistency detection, exact affine coverage, and duplicate freedom, including empty equation systems and zero-variable systems. This is exhaustive finite regression coverage for the stated small grid, not a proof for arbitrary dimensions or fields. See G-EP76 in the mixed Kronecker recovery research note.


**Exhaustive-search decision and budget integrity (G-EP77):** independently cross-checks modular determinant values against the permutation formula on all matrices through dimension three over F₂/F₃, verifies that exhaustive negative status requires complete left/right candidate enumeration, and confirms the budget counts both S and T candidates. A patched impossible-target fixture exercises search control flow only; it is not a mathematical non-equivalence example. See G-EP77 in the mixed Kronecker recovery research note.


**Replayable exhaustive negative certificates (G-EP78):** adds an independent verifier that recomputes the input's complete Kronecker profile, enumerates every left matrix and compatible affine right-transform solution, and checks the reported candidate count and negative-result metadata. It rejects forged completion flags, search modes, counts, budgets, explanations, and budget-limited runs. This is an exact replay for the stated finite field and profile bounds, not a universal polynomial-time method.


**Replay-verifier boundary hardening (G-EP79):** validates caller matrices as nonempty rectangular integer sequences and rejects booleans/floats and invalid fields as caller-input errors. Malformed result containers, missing metadata, and malformed profile structures fail closed with a negative verification result. Tests distinguish invalid caller inputs (ValueError) from untrusted certificate data (verified=false).


**Certificate-bound profile parameters (G-EP80):** exhaustive negative results now record the exact max_degree and max_minors used to compute their Kronecker profile. Replay takes these bounds from the certificate rather than requiring remembered caller arguments, validates their types/ranges, and recomputes the profile with those exact values. Omitting either field or supplying boolean/float/negative/zero-invalid values fails closed. Replay recomputes using the exact recorded values; if a changed bound changes the resulting profile, the profile comparison fails. Different bounds that happen to produce the same profile are observationally equivalent to this replay and cannot be distinguished from the output alone. Custom non-default bounds are replayed directly from the result metadata.
\n\n**Full recovery replay (G-EP81):** `verify_mixed_kronecker_recovery_certificate` recomputes the profile and canonical target for every outcome. Positive results are checked against reconstructed canonical matrices, minimal-index/regular metadata, exact strict-equivalence transforms, and the multi-block direct-sum audit. Incomplete-profile and bounded-search failures are replayed as accurately described inconclusive outcomes, not negative decisions; exhaustive negatives continue through the G-EP78 replay path. Recovery results now consistently record search mode and candidate budget, including incomplete-profile returns.\n
 
**Positive recovery-certificate adversarial replay (G-EP82):** hardens `verify_mixed_kronecker_recovery_certificate` against malformed nested transforms and forged audit records. Positive S/T transforms must be correctly sized square sequences with genuine integer entries (booleans and floats are rejected); malformed nested audit structures fail closed. Strict-equivalence and multi-block audits are recomputed and compared in full, including nested fields and matrices, rather than trusting stored success flags. Invalid caller matrices/fields still raise `ValueError`; the verifier explicitly rejects boolean/floating-point source entries before shared pair validation, while malformed certificate contents return `verified=false`. This is certificate-boundary hardening, not a new recovery algorithm or a uniqueness claim.


**G-EP83:** positive-certificate replay now uses type-exact recursive comparisons when matching the recomputed profile, canonical matrices, minimal-index metadata, regular dimension, and canonical block shapes. This prevents Python boolean/integer equality from allowing boolean-forged numerical fields to pass. The verifier reconstructs these values from the supplied pencil and recorded profile bounds; adversarial tests cover nested profile mutation, source-shape forgery, canonical matrix and block-shape boolean aliases, and container-type changes. This is deterministic replay hardening, not an independent classifier or uniqueness claim.


**G-EP84:** adds cross-field positive-certificate replay tests over F₂, F₃, F₅, and F₇ using basis-scrambled mixed pencils, plus rejection of forged field metadata and boolean transform entries. Distinct valid S/T witnesses produced by reciprocal nonzero scalar rescaling are accepted when their witness-dependent strict-equivalence and multi-block audit records are also regenerated; stale nested audits remain rejected. These are finite regression controls, not a universal recovery or uniqueness theorem.


**G-EP85:** expands positive recovery replay adversarial coverage: required metadata omission and type substitutions, boolean/integer aliases and container substitutions in nested strict-equivalence and multi-block audit records, now rejected through recursive type-exact audit comparison, and cross-field S/T transplantation across F₃/F₅/F₇, accepting a transplanted pair only when it satisfies the destination-field identities and rejecting a mutated pair after audit regeneration. Witness provenance is not required. These are deterministic certificate-integrity regressions for the selected fixture, not a universal recovery or uniqueness theorem.


**G-EP86:** tests tampering with canonical block order, block dimensions, canonical target entries, and nested multi-block audit matrices. A consistently reordered right/regular/left block decomposition remains valid under the standalone direct-sum witness verifier, while the recovery-certificate verifier rejects it because that certificate uses a fixed profile-derived canonical block order. This distinguishes algebraic direct-sum validity from canonical certificate serialization; the regression uses one 4×4 fixture over F₅.


**G-EP87:** standalone multi-block witness verification now rejects boolean and non-integral entries in source coefficients and transforms. Tests cover all six consistent permutations of a three-block mixed pencil, plus malformed, incomplete, dimension-inconsistent, and zero-by-zero block partitions. The API represents blocks as consecutive partitions, so overlapping intervals cannot be separately encoded; invalid totals and shapes are rejected.


**Multi-block witness adversarial verification (G-EP88):** adds regressions ensuring singular left or right transforms produce a failed verification audit rather than being confused with malformed caller data; modularly equivalent integer representatives yield identical normalized audit data; field validation rejects booleans, non-integers, small invalid values, and composites while F₂/F₃ positive controls pass; and malformed nested/ragged matrix inputs raise explicit `ValueError`. This hardens the supplied-witness verifier without changing its discovery scope or treating a failed witness as proof that no decomposition exists.


**Generated rectangular partition coverage (G-EP89):** deterministic generated-style fixtures exercise multi-block partitions containing zero-row and zero-column blocks (but no zero-by-zero blocks) over F₂, F₃, F₅, and F₇. Identity transforms verify valid block-diagonal pairs, while injected cross-block coefficients must fail the corresponding zero-block and overall verification checks. Invalid total partitions are also rejected. These are finite regression controls, not a universal proof.


**G-EP90 — rectangular multi-block basis invariance:** adds generated-style
regression coverage for an ordered partition containing zero-row and
zero-column blocks (never a zero-by-zero block), with positive total
dimensions. Independently invertible unitriangular left and right basis
changes scramble both coefficients over F₂, F₃, F₅, and F₇; the exact inverse
witness must recover and verify the original block-diagonal pair. This is
finite test coverage, not decomposition discovery, uniqueness, or a universal
recovery theorem.


**G-EP91 — adversarial rectangular basis-invariance witnesses:** extends the
G-EP90 generated rectangular fixture over F₂, F₃, F₅, and F₇. Tests inject
coupling into each representable directed off-diagonal block independently in
both Q and K, mutate both coefficients together, and alter left/right
transforms while keeping them invertible. These well-formed but false
witnesses must return failed audits. Singular square transforms also return
failed audits; malformed dimensions or non-integral entries instead raise
ValueError. This distinction is tested explicitly and does not imply that a
failed witness rules out another valid decomposition.


**G-EP92 — equivalent-representation stability:** verifies that modularly
equivalent integer representatives, independently chosen invertible row and
column scramblings, reciprocal nonzero scalar rescalings of the two witness
transforms, and simultaneous block-coordinate permutations preserve valid
multi-block audits. Controls run over F₂, F₃, F₅, and F₇. These are exact
finite regression tests; they do not establish uniqueness of a partition or
of its witness.


**G-EP93 — near-equivalence rejection:** tests one-entry source-coefficient mutations after a valid rectangular basis scrambling, one-entry perturbations of each supplied invertible transform, and block-shape permutation without the corresponding coordinate permutation. These well-formed near-equivalences must fail the algebraic audit, while malformed transform dimensions continue to raise ValueError. Controls run over F₂, F₃, F₅, and F₇; a failed supplied witness is not a no-decomposition theorem.


**G-EP94 — independent audit-record cross-checks:** test-only matrix multiplication, Gaussian rank, and block slicing independently reconstruct SQT/SKT and every ordered rectangular block. The tests compare all verifier diagnostic fields, including both transform ranks, invertibility flags, per-coefficient off-diagonal-zero flags, and the aggregate decision, for valid and deliberately false witnesses over F₂/F₃/F₅/F₇.


**G-EP95 — serialized audit round-trip and replay:** JSON round-trips valid and false multi-block audit records, then exactly compares the restored data with a fresh audit recomputed from source matrices and transforms. Forged aggregate flags, stale off-diagonal flags, boolean-for-integer rank substitutions, and missing block grids are rejected by type-exact replay comparison. The verifier itself consumes source matrices and transforms, not serialized audit records; this is a test of serialization integrity and replay discipline, not a new certificate-loading API.


**G-EP96 — Strict JSON snapshot boundary regressions:** test-side decoding rejects duplicate object keys and non-finite JSON constants. Restored records with unexpected schema versions, malformed nested block arrays, missing required fields, or boolean/floating-point substitutions in integer diagnostic positions fail recursive type-exact comparison with a fresh audit. Original malformed caller matrices continue to exercise the verifier's separate `ValueError` input boundary. No serialized-record ingestion API is introduced.


**G-EP97 — Deterministic serialized-record mutation sweep:** recursively enumerates every dictionary field and list slot in a valid JSON audit snapshot, mutates one location at a time, round-trips each mutation, and confirms exact type-aware comparison rejects every changed record. Coverage explicitly includes top-level metadata, both block grids, and nested verification fields. This is finite regression testing of snapshot integrity, not cryptographic authenticity or provenance.


**G-EP98 — v1 audit schema contract:** test-side structural validation checks exact required fields and types, positive source dimensions, rectangular block partition totals, transform/transformed-matrix dimensions, both nested block-grid dimensions, and verification diagnostic types/ranges. It deliberately accepts well-formed but mathematically false witness records, keeping schema validity distinct from algebraic verification. No production parser or schema migration is introduced.


**G-EP99 — Rectangular schema edge-case grid:** exercises the v1 structural contract across two-, three-, and four-block partitions, including legal zero-row and zero-column rectangular blocks. It verifies exact nested grid dimensions, accepts well-formed false witnesses as structurally valid without treating them as successful algebraic certificates, and rejects malformed nested grid dimensions. Finite deterministic regression coverage only.


**G-EP100 — Schema/algebra outcome cross-check:** pairs structural validation with four verifier outcomes: valid structure and valid witness; valid structure and false witness; malformed snapshots rejected independently of witness intent; and well-formed singular-transform records with a negative audit. This explicitly tests that schema validity is not conflated with invertibility or block-diagonal truth.

**G-EP101 — independent audit-record reconstruction:** adds test-local matrix multiplication, Gaussian rank, and rectangular block slicing to reconstruct transformed coefficients, both complete block grids, transform ranks, invertibility flags, off-diagonal-zero diagnostics, and the aggregate decision directly from source matrices and supplied transforms. It cross-checks positive, false, and singular witnesses, including zero-row/zero-column partition blocks, and detects schema-shaped mutations to transformed matrices, nested blocks, and diagnostics. This is finite regression evidence; it is not a production snapshot-ingestion API, formal proof, or provenance/authenticity mechanism.

**G-EP102 — seeded cross-field rectangular reconstruction:** extends the test-local audit checks over deterministic fixtures in F₂, F₃, F₅, and F₇. Each field uses a different rectangular partition, including zero-row/zero-column blocks, independently generated invertible left/right basis changes, and modularly equivalent source-entry representatives. Reconstructed transformed coefficients must recover the block-diagonal controls; normalized block grids and verification diagnostics must remain stable under adding multiples of the field characteristic. A shape-preserving snapshot mutation is also checked. These seeded finite tests are regression evidence, not universal proof or a production snapshot verifier.

**G-EP103 — three-layer audit pipeline:** adds a deterministic mutation matrix that checks structural schema validity, consistency with source matrices/transforms through test-local reconstruction, and the mathematical witness verdict as separate outcomes. It includes malformed nested grids, schema-valid forged transformed coefficients/blocks/diagnostics, a positive witness, and a structurally valid, reconstruction-consistent negative witness. This clarifies the trust boundary: schema validity does not imply record consistency, and record consistency does not imply mathematical success. Test-only finite regression coverage.

**G-EP104 — adversarial audit metadata:** tests schema-version, field-label, source-dimension, partition-order, and scope mutations. It distinguishes malformed metadata from well-typed but source-unbound metadata, and confirms that an alternative reciprocal scalar rescaling of the left/right transforms can remain a valid equivalent witness. These are test-side snapshot-integrity and algebraic regression checks, not cryptographic provenance.


- **G-EP105:** add cross-field rectangular coordinate-permutation regressions over F₂/F₃/F₅/F₇. Simultaneously permuting row and column coordinate intervals, the ordered block list, and the corresponding supplied transforms preserves the exact reordered block-diagonal pair, including zero-row and zero-column blocks. One-sided row or column coordinate permutations are rejected. These are deterministic finite regression tests, not a universal theorem, decomposition discovery method, or uniqueness claim.


**G-EP106 — composed equivalence transformations:** tests compositions of two successive, independent left and right source-basis changes, a consistent rectangular block-coordinate permutation, and reciprocal nonzero scalar rescaling. The composite witness must recover the exact reordered Q/K pair over F₂, F₃, F₅, and F₇, including zero-row and zero-column blocks. A mismatched final row transform is rejected. This is finite deterministic regression coverage, not a uniqueness theorem or decomposition-discovery result.


**G-EP107 — transformation factorization-order invariance:** tests two distinct ordered factorizations of identical composite left/right basis changes. Both paths are followed by the same rectangular block-coordinate permutation and reciprocal scalar rescaling, and must produce identical verified transformed matrices and block records over F₂/F₃/F₅/F₇. An omitted inverse factor is rejected. Deterministic finite regression coverage only; no uniqueness or decomposition-discovery claim.


**G-EP108 — seeded metamorphic rectangular witness families:** generates deterministic products of elementary invertible matrices for independent left/right basis scramblings, then checks exact recovery of randomly populated rectangular block-diagonal Q/K pairs over F₂/F₃/F₅/F₇. Three partition families include zero-row and zero-column blocks. A transported single-entry cross-block mutation must be rejected in every case. This is reproducible finite regression coverage, not a universal theorem or decomposition-discovery algorithm.


**G-EP109 — long composition and partition adversaries:** checks 17-step and 19-step deterministic products of elementary invertible transformations on the left and right over F₂/F₃/F₅/F₇, with reciprocal scalar witness rescaling and exact recovery of both coefficients. A second control changes the rectangular block partition while preserving total dimensions; the supplied transforms must reject that incorrect partition. Finite deterministic regression coverage only.


**G-EP110 — paired-pencil partition boundary and cancellation adversaries:** adds cross-field controls over F₂/F₃/F₅/F₇ for block-preserving transforms, Q-only and K-only cross-block mutations, and a paired mutation whose opposite off-diagonal entries cancel in Q+K while remaining nonzero in each coefficient separately. The verifier must reject the paired mutation, demonstrating that it checks both pencil coefficients independently rather than only their aggregate. Deterministic finite regression coverage; no decomposition-discovery, uniqueness, or universal-theorem claim. See G-EP110 in `research/the-fold-multi-block-direct-sum-witness.md`.


**G-EP111 — invertible pencil-parameter basis changes:** tests coefficient-space changes by invertible 2×2 matrices over F₂, F₃, F₅, and F₇, including coefficient swaps, shears, and mixed determinant-one changes. The same rectangular coordinate witness must verify the transformed pair and recover the expected mixed target coefficients; applying the inverse parameter change recovers the original ordered pair exactly. This finite regression checks direct-sum stability under an invertible change of basis in the pencil coefficient space. It does not cover singular coefficient mixing, decomposition discovery, uniqueness, or universal classification.


**G-EP112 — singular coefficient-space maps and information loss:** tests rank-deficient linear maps on the ordered pair (Q,K). Over F₂/F₃/F₅/F₇, the original pair is coupled through K, but a singular map can erase K or duplicate Q and make the collapsed pair pass the direct-sum verifier. A retained coupled combination remains rejected. This documents the crucial boundary: verifier success applies to the supplied transformed pair, not to an original pencil after information-losing singular mixing. See G-EP112 in `research/the-fold-multi-block-direct-sum-witness.md`.


**G-EP113 — exhaustive coefficient-map rank boundary:** enumerates all p⁴ 2×2 coefficient-space maps over F₂/F₃/F₅/F₇ and checks their rank census, output coefficient-span dimension, individual off-diagonal conditions, and verifier result on a fixed pencil with block-diagonal Q and coupled K. Exactly p² maps pass: the zero map and rank-one maps that erase K. No invertible map passes. Exhaustive for the tested fields and fixture, not a universal result for arbitrary pencils.


**G-EP114 — intersecting common block-diagonal constraints:** for a fixed left transform and two-block partition, exhaustively enumerates right transforms over F₂/F₃/F₅/F₇. The Q-only and K-only off-diagonal constraint spaces are checked separately and intersected; only the common intersection satisfies both coefficients. Singular members are retained by the linear equations, so invertibility is checked independently. Fixed-left 2×2 fixture only; not general decomposition discovery.


**G-EP115 — simultaneous linear constraint solving:** builds the homogeneous finite-field system for all off-diagonal entries of both coefficients in the unknown right transform. A test-local RREF/nullspace solver is cross-checked against brute force over F₂/F₃/F₅/F₇; invertibility is filtered separately, and every surviving candidate is replayed through the exact witness verifier. Fixed-left 2×2 fixture; not a general discovery API.


- **G-EP116:** generalizes test-local simultaneous right-transform equations to rectangular block partitions, including a 3×3 pencil with block shapes (1,2) and (2,1) under independent left/right scramblings. The known witness is checked against the computed nullspace; small 2×2 controls are exhaustively cross-checked against brute force, and adding coefficient constraints is verified not to increase nullspace dimension. Finite test coverage only; no production discovery API or general completeness claim.


- **G-EP117:** independently cross-checks test-local rectangular off-diagonal equations against direct matrix multiplication for arbitrary candidate right transforms. Seeded cases span rectangular matrices, independent left/right basis scramblings, zero-row/zero-column blocks, and F₂/F₃/F₅/F₇. The planted witnesses are replayed through the production verifier; this is finite test evidence, not a general solver or completeness claim.


- **G-EP118:** cross-checks simultaneous off-diagonal constraint rank using row reduction and an independently enumerated row span. Zero, duplicate, scalar-multiple, overlapping, and rank-increasing coefficient constraints are covered; exhaustive right-transform-vector enumeration confirms the nullity solution count over F₂/F₃/F₅. Fixed-left 2×2 finite controls only.


- **G-EP119:** extends test-side off-diagonal equation rank/nullity checks to rectangular sources, including a 2×3 pencil, zero-row/zero-column blocks, and an empty off-diagonal region. Elimination rank is cross-checked against explicit row-span enumeration; sampled equations are checked against direct matrix products, and small kernels are exhaustively counted over F₂/F₃. Finite regression coverage only.


- **G-EP120:** tests constraint-rank invariance under independent invertible block-diagonal row/column coordinate changes on rectangular systems, including empty row/column blocks. The induced map X′ = T⁻¹XT is checked by direct multiplication, and each off-diagonal block's zero status is preserved. A separate control shows that changing the partition can change rank; arbitrary block-mixing basis changes are not covered.


- **G-EP121:** extends constraint-rank invariance to full invertible row/column basis changes that mix blocks, provided the block decomposition is transported with the bases. The test builds the transported equation map using matrix-unit inputs and checks its rank against the original system over F₂/F₃/F₅. Explicit F₂/F₃ controls show that mixing the bases but retaining the old coordinate partition can change rank, because that is a different constraint family. Test-side finite covariance evidence only; the production API still accepts consecutive coordinate block shapes, not arbitrary subspace-basis metadata.


- **G-EP122:** extends transported-basis covariance to rectangular m×n coefficient matrices and n×n right-transform unknowns. Full row/column basis changes mix blocks, while the decomposition is transported through the inverse basis maps. Matrix-unit equation construction checks rank invariance over F₂/F₃/F₅, including a 3×4 partition with simultaneous zero-row and zero-column blocks; sampled candidates verify the pullback identity. A fixed-coordinate control confirms rank can change when the partition is not transported. Finite test-side evidence only; no generic mixed-basis production verifier is added.


**G-EP123 — transported kernel bijection and singular candidates:** exhaustively enumerates the full 2×2 right-transform matrix space for a rectangular 3×2 pencil over F₂ and F₃. The conjugation map induced by a full mixed column-basis change is checked to be a bijection on all matrices and to preserve the simultaneous off-diagonal constraint predicate after transporting the decomposition. Kernel cardinalities agree, including singular solutions; determinant filtering is kept separate, with the zero matrix explicitly retained in the linear kernel but excluded from invertible witnesses. This is finite test-side evidence, not a production mixed-basis verifier or general discovery algorithm.


- **G-EP124:** increases the right-transform space to 3×3 (nine variables) for a rectangular 4×3 coefficient pair. Independently constructs the simultaneous constraint matrices from matrix-unit inputs, compares their ranks and nullities after full row/column basis transport over F₂/F₃/F₅, and verifies both directions of the induced candidate-coordinate map on all matrix units plus sampled general candidates. Finite test-side rank/nullity and covariance evidence only; no production mixed-basis API change.


- **G-EP125:** independently cross-checks G-EP124's 3×3 transported constraint rank with complete row-span enumeration over F₂/F₃ (and RREF covariance over F₅). Shape-preserving coefficient mutation changes the reconstructed constraint map while retaining dimensions, distinguishing a mathematically false transport from malformed input; a mutated inverse-map entry breaks the inverse identity, with a separate malformed-dimension control. Finite test-side evidence only.


- **G-EP126:** transports complete nullspace bases for the 3×3 right-transform constraint system. For zero and scalar-dependent rectangular coefficient pairs over F₂/F₃/F₅, independently computed nullspaces are mapped by X′ = V⁻¹XV and checked in both directions by equation substitution and span-dimension comparisons. Includes rank-zero and nonzero rank-deficient cases; invertibility remains separate from linear-kernel membership. Finite test-side evidence only.


- **G-EP127:** composes two independently invertible row/column basis changes on the rectangular 4×3 constraint system over F₂/F₃/F₅. Verifies factor order, composed source recovery, nullspace transport and inverse recovery; omission and reversal controls remain well-shaped but produce incorrect coefficient transports. Finite test-side evidence only.


- **G-EP128:** four-stage rectangular basis transport over F₂/F₃/F₅, including identity stages and adjacent inverse-factor cancellation. Checks composed matrix identities, kernel-basis transport and recovery, plus shape-valid wrong-inverse-order controls. Finite test-side evidence only.


- **G-EP129:** transports rectangular block projectors through a four-stage row/column basis composition over F₂/F₃/F₅. Sequential and directly composed transported partitions agree, including zero-row and zero-column blocks; each projected coefficient block is checked against pullback to the original partition. Finite test-side evidence only.


**G-EP130 — projector algebra under composed rectangular transport:** verifies idempotence, pairwise orthogonality, and completeness of transported row/column block projectors after four composed basis stages over F₂/F₃/F₅. Zero-row/zero-column blocks remain explicit zero projectors. Independent shape-valid mutations isolate failures of each projector axiom, and a wrong transport direction is rejected. Test-side finite regression evidence only; no production projector-certificate API is added.


**G-EP131 — projector rank/nullity invariance:** independently computes finite-field ranks of transported row/column projectors and verifies rank and kernel dimension are preserved and match the rectangular block sizes, including empty blocks. A shape-valid idempotent with one missing image direction is detected. F₂/F₃/F₅ test-side coverage only; no production rank-certificate API is added.
\n\n**G-EP132 — rectangular projected coefficient-block transport:** verifies the covariance identity Pᵢ′ A′ Qⱼ′ = U(Pᵢ A Qⱼ)V for both coefficient matrices under four-stage composed row/column basis changes over F₂, F₃, and F₅. Every ordered block pair is checked, including off-diagonal zeros and explicit empty 1×0/0×1 diagonal summands; projected-block ranks are preserved. A shape-valid wrong column-conjugation direction is rejected. Finite test-side regression evidence only; no production projector API is added.\n

**G-EP133 — diagonal projected-block reconstruction and coupling detection:** sums all transported diagonal projected blocks and verifies exact reconstruction of each coefficient matrix, with the off-diagonal sum zero, over F₂/F₃/F₅. A one-entry, shape-valid cross-block coupling is then injected in source coordinates; the diagonal sum no longer reconstructs the full transported matrix, while diagonal plus off-diagonal sums still do. Test-side finite regression evidence only; no production projector-certificate API is added.


- **G-EP134:** recovers each indexed diagonal projected coefficient block by pulling transported blocks back through the composed row/column basis maps. Empty row/column summands remain explicit zero blocks. A second equal-dimension fixture swaps two transported projector indices: the mutation remains shape-valid but assigns the wrong subspaces and is detected. Test-side finite regression evidence over F₂/F₃/F₅; no production projector-certificate API is added.


**G-EP135 — transported projector image and kernel subspaces:** independently compares the actual image and kernel spans of each transported row and column projector with the subspaces induced by the corresponding basis map. The checks use finite-field elimination, preserve zero-dimensional and full-dimensional cases, and verify expected image/kernel dimensions over F₂/F₃/F₅. A dimension-preserving projector mutation that moves a proper nonzero image to a different coordinate subspace is rejected. Finite test-side regression evidence only; no production arbitrary-subspace projector API is added.


- **G-EP136:** constructs alternative transported row/column projector families by conjugating with coordinate permutations that move the represented subspaces. Each alternative family still satisfies idempotence, pairwise orthogonality, completeness, and the same per-index ranks over F₂/F₃/F₅. Direct comparison with the intended transported projectors detects the changed ordered subspaces. This demonstrates that projector axioms and ranks alone do not uniquely identify the supplied ordered decomposition; test-side finite evidence only.


- **G-EP137:** binds transported projector families to both rectangular coefficient matrices. For the intended row/column projectors, summing all diagonal projected blocks reconstructs each transformed coefficient exactly. Alternative projector resolutions from G-EP136 retain idempotence, orthogonality, completeness, and rank data, but produce nonzero off-diagonal projected blocks and fail diagonal-only reconstruction for both coefficients. The full diagonal-plus-off-diagonal sum remains an exact reconstruction control. Finite test-side evidence over F₂/F₃/F₅; no production arbitrary-subspace certificate API is added.


- **G-EP138:** checks projector-bound diagonal reconstruction under invertible coefficient-space mixing of the pencil pair, in addition to independent row/column basis changes. The mixing matrix has determinant one over F₂/F₃/F₅; its inverse recovers the original ordered coefficient pair exactly. The intended projectors reconstruct both mixed coefficients from diagonal projected blocks, while the alternative resolution still fails diagonal-only reconstruction and the full projected-block sum remains exact. Finite test-side covariance evidence only.

- **G-EP139:** composes two successive invertible coefficient-space basis changes and compares sequential mixing with the directly composed map over F₂/F₃/F₅. The same transported projector families reconstruct both coefficients at each stage; the composed map is inverted to recover the original ordered pair, including reverse-order inverse application. Finite test-side composition and covariance evidence only.
G-EP140: distinguishes valid invertible coefficient-space shears that change only one output coefficient from unrelated matrix-space mutations applied to only one coefficient. The same transported rectangular projectors reconstruct both coefficients before and after the shear over F₂/F₃/F₅; inverse shear recovers the original pair. A shape-preserving cross-block mutation to only one coefficient breaks diagonal-only reconstruction while the untouched coefficient remains reconstructible. Finite test-side regression evidence only.
\n- **G-EP141:** exhaustively groups nonzero rank-one 2×2 coefficient maps over F₂/F₃/F₅ by their surviving projective pencil direction. The output pair spans one surviving linear combination; all maps with the same direction yield the same direct-sum verdict despite differing kernel/preimage data. Only the pure-Q direction removes the fixture's K-coupling. Finite test-side evidence only; singular maps do not certify equivalence of the original pencil.

- **G-EP142:** exhaustively contrasts rank-zero, rank-one, and invertible 2×2 coefficient maps over F₂/F₃/F₅. A rank-zero map collapses both output matrices to zero, which the direct-sum verifier correctly accepts as a direct sum of the supplied zero pair; that success is not evidence about the original pencil. Rank-one maps retain one projective pencil direction, while invertible maps retain the full two-dimensional coefficient information. The production verifier reports only the supplied-pair verdict and does not expose coefficient-map provenance, so the rank/image distinction remains an explicit test-side audit rather than inferred verifier metadata.


- **G-EP143:** exhaustively tests every invertible 2×2 coefficient-space change over F₂/F₃/F₅ on two contrasting three-block fixtures: one where both coefficients are block diagonal and one where both have cross-block coupling on independent supports. The supplied identity-coordinate direct-sum verdict is invariant under every such change; inverse coefficient maps recover the original ordered pair exactly. This establishes finite fixture-specific covariance evidence, not a universal decomposition theorem or a production coefficient-map API.

- **G-EP144:** exhaustively tests every invertible 2×2 coefficient-space map over F₂/F₃/F₅ on a rectangular 3×4 block partition containing explicit zero-column and zero-row summands. Under independent nontrivial row/column basis changes, every ordered projected block of both mixed coefficients is checked against the corresponding linear combination of the original projected blocks, including exact empty-block shapes. All off-diagonal projected blocks remain zero, diagonal blocks reconstruct each full coefficient, and inverse coefficient maps recover both the ordered matrices and all indexed projected blocks. Finite test-side covariance evidence only; no production projector API or universal theorem is added.

- **G-EP145:** checks all 24 reorderings of a four-block rectangular partition containing zero-column and zero-row summands over F₂/F₃/F₅. Row and column coordinate permutations are induced independently from the same block ordering. Every reordered witness is replayed; all off-diagonal projected blocks vanish, diagonal blocks reconstruct each coefficient, and inverse coordinate/block permutations recover the original matrices and every indexed projected block. Finite test-side permutation covariance evidence only; no canonical-order or uniqueness claim is added.


**Repeated equal-sized summands and relabeling controls (G-EP146):** adds a fixture with three equal 1×1 summands carrying distinct ordered coefficient data, plus explicit zero-column and zero-row summands. All six permutations of the repeated blocks are tested over F₂/F₃/F₅. Simultaneously transporting row and column coordinate intervals is accepted and permutes every indexed projected block as expected; inverse transport recovers both coefficients. A shape-preserving one-sided row-subspace reassignment, with column coordinates and shape metadata held fixed, creates cross-block entries in both coefficients and is rejected. This distinguishes consistent relabeling from an incorrect subspace assignment without claiming that equal shapes identify a unique decomposition. Finite test-side regression evidence only.


**G-EP147 — equal dimensions versus internal pencil equivalence:** four equal 1×1 summands carry two proportional coefficient pairs, one pair sharing only its first coefficient with another, and a fourth distinct projective pair. Over F₂/F₃/F₅, all 24 equal-shape relabelings preserve the production direct-sum verdict while moving the indexed internal signatures with their blocks. A test-local determinant criterion checks the 1×1 constant strict-equivalence relation (common nonzero scalar on both coefficients). A control changes only one diagonal K entry: the decomposition remains valid, but the internal pencil signature changes. Finite fixture-specific evidence; it does not classify larger blocks or add a production equivalence API.


**G-EP148 — 2×2 internal pencil equivalence and joint-rank obstructions:** extends internal-block testing beyond 1×1 pencils. Over F₂/F₃/F₅, a nontrivial invertible left/right transformation produces a positive 2×2 strict-equivalence witness, checked by the production auditor against both exact coefficient identities. A negative control has matching individual Q- and K-ranks but different rank profiles for Q+λK; at λ=−1 this proves that no common strict-equivalence transforms can relate the two pairs. Finite fixture-specific evidence only; it is not a complete 2×2 classification or a general witness-discovery algorithm. See `research/the-fold-internal-pencil-equivalence-2x2.md`.


- **G-EP149:** adds a test-local homogeneous determinant-polynomial audit for 2×2 pencils. A positive nontrivial strict-equivalence witness confirms the expected scalar covariance of \(\det(xQ+yK)\). A negative control compares pairs with matching individual coefficient ranks but nonproportional determinant polynomials, ruling out every common constant strict-equivalence witness. Finite fixture-specific evidence; the determinant polynomial is not claimed to be a complete invariant. See `research/the-fold-determinant-polynomial-invariant.md`.


- **G-EP150:** demonstrates that the homogeneous determinant polynomial from G-EP149 is not a complete strict-equivalence invariant. Over F₂/F₃/F₅, a scalar pencil and a nontrivial Jordan pencil have exactly the same \(\det(xQ+yK)=(x+y)^2\), but with Q=I any strict equivalence would force similarity of K. The rank of K−I differs, proving non-equivalence. Finite exact counterexample family; no complete classification is claimed. See `research/the-fold-determinant-polynomial-limit.md`.


- **G-EP151:** distinguishes characteristic-polynomial agreement from 2×2 operator similarity over F₂/F₃/F₅. The identity and a size-two Jordan block share \((t-1)^2\) but have different invariant factors and cyclic-vector behavior; the existing rational-canonical routine decides they are not similar. A nontrivial conjugation of a diagonal operator supplies a positive intertwiner checked by the production witness API. Finite regression fixtures; no new similarity algorithm is introduced. See `research/the-fold-2x2-cyclic-similarity.md`.


- **G-EP152:** exhaustively audits all 2×2 matrices over F₂ and F₃. For each matrix, a test-local characteristic-polynomial calculation and complete vector enumeration cross-check the production rational-canonical profile's cyclicity signal. Every invariant-factor profile fibre is then compared exactly with the conjugacy orbit generated by all invertible 2×2 basis changes. Exhaustive only for these two fields and dimension two; no new production similarity algorithm. See `research/the-fold-exhaustive-2x2-similarity.md`.


**G-EP153 — exhaustive 3×3 similarity-orbit audit over F₂:** exhaustively checks all 512 matrices, independently computes each characteristic polynomial, verifies invariant-factor products and cyclic-vector criteria, and compares every invariant-factor fibre with the complete conjugacy orbit under all 168 invertible basis changes. The finite exhaustive claim is limited to dimension three over F₂; no production similarity algorithm is added. See `research/the-fold-exhaustive-3x3-similarity.md`.


**G-EP154 — exhaustive 3×3 similarity-orbit audit over F₃:** exhaustively checks all 19,683 matrices, independently validates characteristic polynomials and invariant-factor products, checks cyclic-vector criteria across all 27 vectors, and compares every invariant-factor fibre with conjugacy under all 11,232 invertible basis changes. The finite exhaustive claim is limited to dimension three over F₃. See `research/the-fold-exhaustive-3x3-f3-similarity.md`.


**G-EP155 — cross-field comparison of 3×3 similarity profiles:** enumerates every 3×3 matrix over both F₂ and F₃ and compares invariant-factor degree patterns separately from coefficient tuples. The observed degree-shape set is shared, while coefficient representatives remain field-valued data (with coefficient 2 appearing over F₃ but not F₂). This comparison does not identify polynomials across fields or claim that the fields have the same irreducible polynomials; the exhaustive scope remains dimension three over these two fields.


- **G-EP156:** exhausts all monic cubic polynomials over F₂ and F₃ (each is realized as the characteristic polynomial of its companion matrix), factors them with the exact finite-field factorizer, and checks exact reconstruction. F₃ has one additional degree/multiplicity pattern: three distinct linear factors, impossible over F₂ because it has only two linear monic irreducibles. The irreducible polynomial inventories also differ by field; expected counts in degrees one through three are checked independently. No polynomial coefficients are identified across fields.


- **G-EP157:** exhausts all monic quartics over F₂ and F₃, checks exact factor reconstruction, and validates irreducible counts in degrees one through four. It confirms a quartic factor pattern containing all three distinct linear factors with one repeated over F₃, which cannot occur over F₂. This is an exhaustive degree-four comparison over these two fields.


- **G-EP158:** compares all monic quartics over F₂, F₃, and F₅. Exact factor reconstruction and irreducible inventory counts through degree four are checked. The catalog grows with field size: three distinct linear factors with one repeated occur from F₃ onward; four distinct linear factors occur over F₅; and two distinct irreducible quadratics occur from F₃ onward. These are exhaustive degree-four results for the three stated fields.


- **G-EP159:** exhausts monic quartics over F₂, F₃, F₅, and F₇. It checks exact factor reconstruction and irreducible inventory counts through degree four. The degree/multiplicity pattern catalogue strictly grows from F₂ to F₃ and F₃ to F₅, then is identical over F₅ and F₇. The irreducible polynomial inventories still differ between F₅ and F₇, so stabilization applies to quartic factor shapes, not polynomial coefficients or factor identities.


- **G-EP160:** exhausts monic quintics over F₂, F₃, F₅, and F₇. It verifies exact reconstruction and irreducible inventory counts through degree five. The degree/multiplicity pattern catalogue grows from F₂ to F₃ and F₃ to F₅, then agrees over F₅ and F₇ despite different irreducible polynomial inventories. This supports a degree-five threshold at field size five for these tested fields; it is not a theorem for arbitrary polynomial degrees.


- **G-EP161:** exhausts all monic sextics over F₂, F₃, and F₇ (64, 729, and 117,649 polynomials). It checks exact factor reconstruction and irreducible inventory counts through degree six. The complete 34-pattern degree/multiplicity catalogue occurs over F₇; the smaller tested fields have strict subsets. Six distinct linear factors impose the limiting field-size requirement, so seven is the first prime-field size at which the complete sextic shape catalogue can occur.

- **G-EP162:** exhausts all 15,625 monic sextics over F₅, independently confirming exact factor reconstruction and irreducible inventory counts through degree six. The six-distinct-linear-factor shape is absent, while representative five-linear-factor and four-linear-plus-quadratic shapes occur. This fills the F₅ comparison point between G-EP161's F₃ and F₇ experiments.

- **G-EP163:** tests the general polynomial factor API's scalar-unit convention, coefficient reduction modulo the field, constant-polynomial behavior, zero-polynomial rejection, composite-modulus rejection, and characteristic-three multiplicity — (x^3+1=(x+1)^3) over F₃.

- **G-EP164:** exhaustively cross-checks `is_irreducible_polynomial` against the factorizer's exact one-factor criterion for every monic polynomial of degrees 1–4 over F₂, F₃, and F₅ (930 inputs).

- **G-EP165:** extends the exhaustive irreducibility-predicate/factorizer cross-check to all 3,400 monic quintics over F₂, F₃, and F₅.

- **G-EP166:** extends the irreducibility-predicate/factorizer comparison to all 793 monic sextics over F₂ and F₃, checking exact agreement on degree-six inputs.

- **G-EP167:** extends the exhaustive irreducibility-predicate/factorizer comparison to all 2,315 monic degree-seven polynomials over F₂ and F₃.

- **G-EP168:** extends the exhaustive irreducibility-predicate/factorizer comparison through degree eight over F₂ and F₃ (6,817 monic polynomials).

- **G-EP169:** exhaustively cross-checks the irreducibility predicate against the factorizer for all 20,195 monic degree-nine polynomials over F₂ and F₃. This is a finite-domain consistency regression, not a proof for arbitrary degrees or fields.

- **G-EP170:** exhaustively cross-checks the irreducibility predicate against the factorizer for all 60,073 monic degree-ten polynomials over F₂ and F₃. This is finite-domain consistency coverage, not a general theorem.


- **G-EP171:** extracts degree-specific irreducibility-predicate/factorizer comparisons into a parameterized audit over arbitrary prime fields and positive degrees. It exhausts domains within a configurable case budget and otherwise performs reproducible sampling, reporting completeness explicitly (including the edge case where the sample covers the entire domain). The research note separately analyzes the scaling weight n/n^n and its relationship to the actual p^n workload. Finite exhaustive and sampled agreement are computational evidence, not an arbitrary-degree proof.


- **G-EP172:** works outward from the full monic-polynomial workload \(p^n\) and inward to the exact irreducible count. It derives the adjacent-degree ratio and turning threshold for the imposed weight \(n(p/n)^n\), then contrasts it with the exact Möbius formula \(I_p(n)=\frac1n\sum_{d\mid n}\mu(d)p^{n/d}\) and the natural normalized irreducible density \(nI_p(n)/p^n\to1\) for fixed \(p\). It explicitly separates workload weighting from irreducible-density normalization and distinguishes exact counts from sampled statistics. See `research/the-fold-outward-inward-scaling.md`.


- **G-EP173:** upgrades the parameterized irreducibility audit with an independent exact Möbius-formula count of monic irreducibles. It reports observed/theoretical densities, degree-normalized densities, the expected irreducible count in the checked subset, and an exact count-match flag only when the full domain has been covered. The audit schema advances to v2; tests cover exact count fixtures, a prime/degree grid, exhaustive comparison, and sampled-mode semantics. See research/the-fold-outward-inward-scaling.md.


**Uniform irreducible-density convergence and factorization corrections (G-EP174–G-EP175):** `tools/polynomial_irreducibility_audit.py` now reports exact normalized-density errors, proves a uniform-in-prime-field convergence bound, and resolves the leading correction from the prime factorization of the degree. Prime-power degrees have exactly one nonzero Möbius correction; for degrees with at least two distinct prime factors, the second-smallest prime factor bounds the remainder after the leading term. See `research/the-fold-outward-inward-scaling.md` and `tests/test_polynomial_irreducibility_audit.py`.


**Coprime-degree composition defect (G-EP176):** adds an exact audit comparing \(R_p(ab)\) with \(R_p(a)R_p(b)\) for coprime degrees. A concrete counterexample over F₂ at degrees 2 and 3 gives defect 15/32; degree one remains the identity case. The research note explains why the Möbius divisor indexing factors but its exponent weights do not. See `research/the-fold-outward-inward-scaling.md` and the irreducibility-audit tests.


**Coprime-degree defect sign survey (G-EP177):** adds an exact-rational bounded survey of Delta_p(a,b)=R_p(ab)-R_p(a)R_p(b) over all unordered coprime degree pairs in a requested range. An exploratory sweep found positive defects for 2,944 pairs per field over p=2,3,5,7,11, with degrees through 100; this remains finite evidence, not a universal positivity theorem. The executable audit reports exact sign counts and any counterexample witness. See research/the-fold-outward-inward-scaling.md.


**Bad-proportion ordering reduction (G-EP178):** records the sufficient condition E_p(ab)<min(E_p(a),E_p(b)) for positive coprime-degree composition defect, and adds an exact-rational finite-grid audit with counterexample witnesses. The condition held throughout the explored p=2,3,5,7,11 grid through degree 100, but remains unproved universally. See `research/the-fold-outward-inward-scaling.md`.


**G-EP179 — Coprime bad-proportion ratio bound audit:** adds an exact-rational finite-grid audit for the conjecture that (E_p(ab)/\min(E_p(a),E_p(b))\le(p^2+p-1)/p^3) for coprime degrees greater than one. The test grid covers 102 pairs over p=2,3,5 through degree 12 and checks that the maximum is attained at (2,3), with value 5/8 over F₂. This is finite evidence only; the universal bound remains unproved. See `research/the-fold-outward-inward-scaling.md`.


**G-EP180 — Analytic subcase of the coprime ratio conjecture:** proves the proposed bound (Q_p(a,b)\le(p^2+p-1)/p^3) for all coprime pairs with smaller degree 2. Equality occurs at (2,3); the inequality is strict for (2,b) with odd b≥5. The proof uses the maximal-proper-subfield union bound and a one-subfield lower bound. Pairs with both degrees at least 3 remain open. See `research/the-fold-outward-inward-scaling.md`.


- **G-EP181:** completes the G-EP179 sharp ratio theorem for every coprime pair (a,b>1). G-EP180 handles smaller degree 2; for (3\le a<b), a lower bound for each denominator term and the maximal-subfield union bound give (Q_p(a,b)\le\omega(ab)p^{-b/2}). Small (b=4,5,6,7) are checked explicitly, and for (b\ge8), (\omega(ab)<2\log_2b\le2^{b/2-1}\le p^{b/2-1}), yielding the strict bound (Q_p(a,b)\le p^{-1}<(p^2+p-1)/p^3). Equality in the full theorem occurs only at (2,3). Therefore (E_p(ab)<\min(E_p(a),E_p(b))) and the coprime-degree defect is always positive. See `research/the-fold-outward-inward-scaling.md`.


- **G-EP182:** proves a uniform additive asymptotic law for the coprime-degree defect. As the larger degree B grows, Q_p(a,b)=E_p(ab)/min(E_p(a),E_p(b)) tends to zero uniformly in prime p. For a≥3 it is bounded by 2 log₂(B)·2^(−B/2); for a=2,b≥5, by 2^(−B/3)+(log₃ B)·2^(−B/2). Consequently Δ_p(a,b)/(E_p(a)+E_p(b)) tends to 1, including when the smaller degree is fixed. See research/the-fold-outward-inward-scaling.md.


- **G-EP183:** identifies the leading exponential scale of the coprime-degree defect from the smallest prime factors. For every n>1, p^(−A(n)) ≤ Eₚ(n) ≤ ω(n)p^(−A(n)), where A(n)=n(1−1/q(n)) and q(n) is the smallest prime divisor. Combining this with G-EP182 yields, uniformly in prime p and for sufficiently large B=max(a,b), a two-sided bound for Δₚ(a,b) and the logarithmic estimate −logₚ Δₚ(a,b)=min(A(a),A(b))+O(log log B). The controlling degree need not be the smaller degree. See research/the-fold-outward-inward-scaling.md.


- **G-EP184–187:** expands each subfield error into its exact finite squarefree-divisor spectrum; derives the complete finite spectrum for the coprime defect; proves the fixed-degree, large-field law \(\Delta_p(a,b)\sim C(a,b)p^{-A}\), with coefficient 2 precisely when the two input exponents resonate; and specifies exact coefficient collection for the next nonzero scale. It distinguishes the fixed-degree \(p\to\infty\) limit from the uniform large-degree limit of G-EP182–183. See research/the-fold-outward-inward-scaling.md.


- **G-EP188–190:** adds an exact integer-coefficient defect-spectrum auditor and rational evaluator; extends the Möbius density and defect results from prime fields to all finite fields of prime-power order; and constructs the exact multi-factor composition-excess spectrum, including its sign-resonance criterion. The exact spectra for (2,3) and resonant (3,4) are regression fixtures. See the research note.


- **Prime-power field support:** the exact irreducible-count and normalized-density APIs now accept every finite-field order \(Q\), provided \(Q\) is a prime power. The original prime-only API remains available for backwards compatibility.


- **G-EP190 correction:** the multi-factor composition excess \(E_Q(\prod n_i)-\prod E_Q(n_i)\) is not sign-definite; (2,3) is positive after leading-term cancellation, while (3,4) is negative. The exact spectrum auditor now handles arbitrary pairwise-coprime degree lists and reports the eventual sign.


- **G-EP193:** generalizes the exact normalized-density convergence audit and its field-independent envelope from prime fields to every prime-power field order. Regression coverage spans \(Q=4,8,9,16,25\) and degrees 1–24.


**G-EP194–G-EP198 — complete composition-excess resonance and eventual-sign classification:** classifies all two-factor leading resonances as exactly \((2,\ell)\) with \(\ell\) an odd prime, resolves each by the exact identity \(H_Q(2,\ell)=Q^{-(2\ell-2)}-Q^{-(2\ell-1)}>0\), proves every other two-factor case is eventually negative, and proves there is no leading resonance with three or more pairwise-coprime factors (all such excesses are eventually negative). Adds coprime_composition_excess_asymptotic(degrees) as an executable exponent/sign certificate, with exact-spectrum fallback in the resonant case. See research/the-fold-composition-excess-resonance.md.


**Exact finite-field composition-excess sign certificates (G-EP199):** `coprime_composition_excess_sign_certificate(degrees, field_size)` evaluates the full integer Laurent spectrum as an exact rational at a prime-power field size, reports its exact sign, and derives a conservative threshold above which the leading coefficient certifies the sign for every prime-power field size. The threshold is explicit and proven by bounding the entire coefficient tail; it is not claimed optimal. See `research/the-fold-composition-excess-resonance.md` and the sign-certificate regression tests.


**G-EP200 — sharpened sign thresholds:** the composition-excess sign certificate now supplements its analytic coefficient-tail bound with an exact scan of the finite integer interval below that bound. It returns `smallest_integer_threshold`, the minimal integer (Q_0\ge2) such that every integer (Q\ge Q_0) has the eventual sign. This is stronger than the sufficient tail bound and also certifies all prime-power field sizes. The proof combines finite exact rational evaluation with the G-EP199 infinite-tail estimate.

**G-EP201 — exact global sign certificates:** adds a rational-arithmetic Sturm-sequence certificate for the sign of the composition-excess Laurent spectrum on every real field-size parameter \\(Q\\ge2\\). It counts roots of the normalized polynomial on \\((0,1/2)\\), checks the endpoint \\(Q=2\\), and certifies a global sign when the count is zero and the endpoint is nonzero. Fixtures cover the positive \\((2,3)\\) case, negative \\((3,4)\\) resonance resolution, and three multi-factor tuples. Per-tuple certificates are not a universal sign theorem. See `research/the-fold-composition-excess-resonance.md`.


**G-EP202 — exact temporal spectral folding:** adds `coprime_composition_excess_temporal_fold(two_steps_ago, one_step_ago, present)`. It aligns exponents across three exact composition-excess spectra and computes the coefficient-wise second difference \\(H_t-2H_{t-1}+H_{t-2}\\), removing cancellations and representing the zero polynomial explicitly. Regression tests cover a nontrivial fold and a constant-spectrum zero fold. See `research/the-fold-composition-excess-resonance.md`.


**G-EP203 — generic Laurent-spectrum sign certification:** adds `laurent_spectrum_global_sign_certificate(spectrum)`, a tuple-independent exact Sturm certificate for finite integer Laurent spectra. It combines duplicate exponents, supports negative powers, detects the zero polynomial, counts roots on the transformed interval, and separately checks the Q=2 endpoint. This allows direct certification of G-EP202 temporal folds. A positive root count means the certificate is inconclusive about global sign, not that a sign change is guaranteed. See `research/the-fold-composition-excess-resonance.md`.


**G-EP204 — finite-family uniform sign persistence:** adds `laurent_spectrum_family_uniform_sign_certificate(spectra)`. For a finite family of exact integer Laurent spectra, it computes each leading-term/tail bound and returns a single integer field-size threshold when all members are nonzero and share the same eventual sign. Mixed signs or a zero member correctly block a common-sign claim. The theorem is finite-family only; infinite-time persistence requires uniform coefficient hypotheses. See `research/the-fold-composition-excess-resonance.md`.


**G-EP205–G-EP207 — recursive power feedback:** adds the research note `research/the-fold-recursive-power-feedback.md`. For the recurrence \(x_0=n,\ x_{t+1}=n^{x_t+1}\), it proves a same-height tower sandwich between base-\(n\) and base-\(n^2\) power towers, establishes strict discrete convexity \(x_{t+1}-2x_t+x_{t-1}>0\), and computes the exact order gap between increment-before-power and power-before-increment. These are proved for the stated integer domains; they do not claim a general classification of self-modifying operators.


**G-EP208 — recursive degree family with uniform sign:** adds `research/the-fold-recursive-degree-family.md`. For the infinite pairwise-coprime family \((2,3^k)\), it derives the exact Laurent spectrum of composition excess and proves a sign transition: \(H_Q(2,3)>0\), while \(H_Q(2,3^k)<0\) for every \(k\ge2\) and every real \(Q\ge2\). This is an infinite-family theorem with a common field-size domain, not an inference from finitely many computed examples. The sign of the temporal second difference in k is explicitly left open.


**G-EP209 — temporal concavity of the recursive degree family:** adds `research/the-fold-recursive-degree-temporal-curvature.md`. For H_k(Q)=H_Q(2,3^k), it proves H_(k+1)-2H_k+H_(k-1)<0 for every integer k≥3 and every real Q≥2. The proof substitutes u=Q^(-3^(k-2)), c=Q^-1, bounds the positive part by <2u^3, and the negative c-weighted part below by >2u^3. Thus H_k is strictly discretely concave on k≥2. This does not by itself claim monotonicity of H_k.


**G-EP210 — monotone convergence of the recursive degree family:** extends `research/the-fold-recursive-degree-temporal-curvature.md`. For each fixed real Q≥2, it proves H_(k+1)(Q)>H_k(Q) for every k≥2, while G-EP208 gives H_k<0 and the exact formula gives H_k→0. Combined with G-EP209, the tail increases strictly and is strictly discretely concave, converging to zero from below with decreasing positive increments.


**G-EP211 — exact asymptotic equivalent and super-geometric ratio:** extends `research/the-fold-recursive-degree-temporal-curvature.md`. Factoring H_k=-Q^(-(1+2·3^(k−1)))B_k with B_k→1 uniformly for real Q≥2 proves H_k∼−Q^(-(1+2·3^(k−1))). It also gives H_(k+1)/H_k = Q^(-4·3^(k−1))(B_(k+1)/B_k) ∼ Q^(-4·3^(k−1)), uniformly for Q≥2; in particular the successive ratio tends uniformly to zero.


**G-EP212 — eventual sign law for every fixed-order temporal difference:** extends `research/the-fold-recursive-degree-temporal-curvature.md`. For each fixed r≥1, the forward difference Δ^r H_k has eventual sign (−1)^(r+1), uniformly for real Q≥2. An explicit threshold K_r is the least k≥2 with 4·3^(k−1) > log₂((32/23)(2^r−1)). The proof bounds every later family term relative to H_k using 23/32 < B_k(Q) < 1. This is a fixed-order theorem; it does not provide one threshold uniform in r.


**AGI concept-learning prototype (Stages 9–12):** `agi/concept_proposer.py` now handles exact compound-unit conversions, typed quantities, affine temperatures, and explicit measurement intervals with calibration corrections. Crucially, overlapping uncertainty intervals are reported as *compatible*, not merged as equivalent. Unsupported statistical models are rejected rather than guessed. See `agi/stage-12-measurement-uncertainty.md` and the [AGI roadmap](the-fold-agi.md). This remains a narrow deterministic prototype, not an AGI system.


**AGI concept-learning prototype (Stages 9–13):** In addition to exact typed quantity and measurement-uncertainty handling, the prototype now proposes proportional, inverse, and affine relationships from paired observations. It retains counterexamples and keeps relational hypotheses separate from equivalence classes. See [Stage 13](agi/stage-13-relational-concept-discovery.md) and the [AGI roadmap](the-fold-agi.md). These are narrow deterministic capabilities, not an AGI system.


**AGI concept-learning prototype (Stages 9–14):** The relational proposer now has an exact composition layer: proportional, inverse, and affine relations are represented as fractional-linear maps and composed by rational matrix multiplication. Intermediate domain exclusions and provenance are retained; refuted hypotheses are rejected. See agi/stage-14-relational-composition.md and agi/relation_composition.py. This is bounded symbolic composition, not general program synthesis or AGI.


**AGI concept-learning prototype (Stages 9–15):** Stage 15 adds held-out validation for composed relational paths, separately checking intermediate and endpoint observations without refitting the relations. Domain failures count as refutations; empty validation sets are explicitly insufficient. See agi/stage-15-independent-validation.md and agi/relation_validation.py. This is finite validation, not proof of AGI or universal generalization.


**AGI concept-learning prototype (Stages 9–16):** Stage 16 compares competing composed relation paths on common held-out observations, keeps endpoint and intermediate errors separate, counts domain failures, groups exactly equivalent composed maps, and uses a transparent complexity tie-breaker. It does not refit candidates or claim generalization beyond the evaluation sample. See agi/stage-16-model-comparison.md and agi/relation_selection.py.


**AGI concept-learning prototype (Stages 9–17):** Stage 17 adds a three-way discovery/validation/test protocol. Candidate provenance is tied to discovery keys, model selection uses validation only, and the untouched test set evaluates only the frozen winner. See `agi/three_way_evaluation.py` and `agi/stage-17-three-way-evaluation.md`. This improves evaluation discipline but does not prove generalization or AGI.


**AGI concept-learning prototype (Stages 9–18):** Stage 18 adds exact finite active experiment design: given fixed candidate relation paths and a caller-supplied input domain, it selects an input with high pairwise prediction disagreement while reporting domain coverage. This proposes mathematical queries only; it does not execute physical experiments or establish AGI. See `agi/active_experiment.py` and `agi/stage-18-active-experiment-design.md`.


**AGI concept-learning prototype (Stages 9–19):** Stage 19 adds an immutable evidence ledger that checks new observations against fixed candidates, preserves historical predictions, and proposes fresh exact proportional/inverse/affine candidates from accumulated evidence. Proposals are not automatically accepted. See `agi/evidence_revision.py` and `agi/stage-19-evidence-revision.md`. This is bounded symbolic learning, not AGI.


**AGI concept-learning prototype (Stages 9–20):** Stage 20 adds exact transfer of affine relational concepts across declared invertible coordinate changes. It transforms model coefficients algebraically and verifies preservation of residual zero/nonzero status without refitting target data. See `agi/representation_transfer.py` and `agi/stage-20-representation-transfer.md`. This is narrow symbolic transfer, not general intelligence.


**Compositional abstraction (Stage 21):** The prototype now retains ordered affine concept paths, distinguishes structurally identical paths from paths with only the same endpoint function, and transfers each edge across a layer-specific coordinate change. Intermediate commuting identities are tested exactly. See `agi/compositional_abstraction.py` and `agi/stage-21-compositional-abstraction.md`.


**Invariant discovery (Stage 22):** The prototype now extracts exact structural invariants of scalar affine self-transformations and verifies them under declared affine conjugacies. It distinguishes invariant properties from covariant coordinates such as the numerical location of a fixed point. See `agi/invariant_discovery.py` and `agi/stage-22-invariant-discovery.md`.


**Affine relationship discovery (Stage 23):** The prototype now compares supplied affine transformations pairwise, identifying commuting pairs, order-dependent compositions, and shared fixed-point sets with exact rational arithmetic. See `agi/affine_relationships.py` and `agi/stage-23-affine-relationships.md`.


**Finite transformation-group recognition (Stage 24):** The prototype now checks whether a finite supplied set of scalar affine bijections forms a group under composition, auditing identity, closure, and inverses with exact rational arithmetic. Associativity is inherited from function composition. See `agi/affine_group.py` and `agi/stage-24-affine-groups.md`.


**Finite symmetry discovery (Stage 25):** The prototype now analyzes finite permutation-group actions, deriving orbits and stabilizers and checking preservation of supplied binary relations. See `agi/symmetry_actions.py` and `agi/stage-25-symmetry-actions.md`.


### Stage 27 — quotient homomorphisms

The AGI concept-learning prototype now checks congruence of finite operations against Stage 26 orbit quotients and constructs induced quotient operation tables only when they are well-defined. It distinguishes an equivalence partition from a congruence compatible with a chosen operation signature. See agi/structure_descent.py, agi/test_structure_descent.py, and agi/stage-27-structure-descent.md.


### Restricted P vs NP track

A first restricted decision task is now specified and implemented: 3-colourability with a supplied tree decomposition whose bags have size at most four. The deterministic dynamic program and certificate verifier accept exactly the same valid instances. This establishes a restricted polynomial-time result, not unrestricted `P = NP` or `P != NP`. See `the-fold-pnp-restricted.md`, `agi/restricted_three_colouring.py`, and its tests.


**P versus NP zero-residual analysis:** The standard class NP is not a number, so `NP = 0` needs an explicit new definition. The canonical residual `NP \\ P` is empty exactly when the classes are equal and nonempty exactly when they differ. Lean modules prove the abstract residual equivalences and the standard NP-complete-target collapse criterion (under polynomial-reduction closure). They do not prove a lower bound or resolve the open problem. See `the-fold-np-zero.md` and `Fold/Complexity/ZeroResidual.lean`.


**NP-completeness bridge:** The formal core now captures the standard result that putting any NP-complete target in P collapses P and NP, assuming P is closed under the chosen polynomial-time reductions. See `Fold/Complexity/Completeness.lean` and `the-fold-np-zero.md`.
