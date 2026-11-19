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
| `the-fold-lean.md` | formal core: the Lean 4 project - involution, quotient, cut, scale, chi, the wheel, and the finite counterexamples |

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
zone map: 9 files with zone tables of 46
     exact           112
     reformulation     5
     rhyme            18
     false friend      9
     the absence       1
     without tables    37
     legend (definitions, not claims)    11

prose attributions: 44 files of 46
     exact           134
     reformulation     5
     rhyme            21
     false friend     37
     total           197
```

The tables are the formal layer and cover nine files. The prose is where the corpus actually works:
forty-four of forty-six files label their comparisons in the predicative form — a noun phrase
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
status markers (marked by contrast, zone not named): 25 files of 46
     total            47
     derivation       18
     about             7
     proof             5
     identity          6
     boost             2
     theorem           2
     other             7
```

The objects are the finding. Sixteen say "not a derivation" and five "not a proof"; with the two "not
a theorem" and the one "not a reduction", twenty-four point at proof. One of those is not a claim —
"the Fold is a dictionary, not a proof engine" — and one "not the identity" is a list of what a point
is not, so thirty-nine claims are marked and twenty-three of them say that nothing was proved. That
is the corpus's own definition of **reformulation**, yet the word appears as a label eight times, five
in tables and three in prose (the third is the Sun comparison below). The middle zone is not scarce;
it is unnamed, and the corpus says it with a contrast instead of a noun.

The remaining objects do different work. "Not an identity", "not about", "not a boost" use one word
in two senses, which is false-friend work rather than a zone; "not a law", "not a model", "not a
result" separate a description from a mechanism.

With that count the map closes: every one of the thirty-eight files carries zone language. The three
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

## What the Fold is for

The corpus says what it is not — not a proof engine, not a constitutive theory, not a computational
model — but not what it is for. It is for this:

> The Fold is a vocabulary for placing a zero, a crease, a scale, and an observer in one diagram, and
> for saying which of those statements are exact and which are only shaped alike. It is a map of where
> the walls are, not a key through them.

Everything else is an entry in that map. The determinant gives the exponents, the fold gives the
split, the twist gives the period, the closure gives the pattern, the horizon gives the edge, and the
observer gives the reading. The four zones are the map's legend.
