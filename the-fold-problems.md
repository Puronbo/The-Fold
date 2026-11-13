# The Fold and the open problems

## What this note is for

The Fold is a dictionary, not a proof engine. It names a crease, a scale, a twist, a signature, a zero
pipeline. The question here is how far that dictionary reaches: which problems it reformulates
exactly, which it only rhymes with, and which it cannot touch. The answer is a map with four zones,
and the value of the map is the honesty of the labelling.

The rule for every entry:

- **exact** — the Fold's object is the problem's object, re-described;
- **reformulation** — the problem becomes a statement about the Fold, with nothing proved;
- **rhyme** — the same shape appears, but the objects are different;
- **false friend** — the same symbol appears, and it means something else.

A rhyme is not worthless: it tells you where to look. But a rhyme written as a proof is the one error
that matters, and this note is written to avoid it.

## The map

### Exact, or an exact reformulation

| problem | the Fold's object | what is exact | status |
|---|---|---|---|
| Riemann Hypothesis | the crease of `R(s) = 1 − s̄` | `ξ(R(s)) = conj ξ(s)`; RH ⇔ zeros fixed by `R` | open; reformulated, not proved |
| function-field RH | Hodge index signature `(1, ρ−1)` | its negative has the fold's shape `(ρ−1, 1, 0)` | proved (Weil, Deligne) by positivity |
| de Bruijn–Newman | theta is the heat kernel; crease `1/2` | the flow preserves the crease; `Λ ≤ 0` ⇔ RH | open; `Λ ≥ 0` is Rodgers–Tao |
| Hilbert–Pólya | a self-adjoint `H` commuting with `R` | `[H,R]=0` and `H=H*` force real eigenvalues split by `R` | open; the operator is missing |
| Atiyah–Singer / Poincaré–Hopf | the zero pipeline's conservation | `ind(0) + ind(∞) = χ(Sⁿ)` | exact in the simple case |
| argument principle | the hole field `ω = dk/k` and its residues | `(1/2πi)∮ f'/f = Z − P`; multiplicity is a residue | exact; counts, does not locate |
| Montgomery–Odlyzko | one `J` is a complex structure | a single `J` gives `β = 2`, the GUE class | statistics exact; no operator |

### Rhyme, or no contact

| problem | contact | why it stops |
|---|---|---|
| Birch–Swinnerton-Dyer | order of vanishing at `s = 1` | the pipeline counts codimension, not multiplicity |
| Hodge conjecture | the Hodge star `⋆` | the star is linear algebra; cycles are not |
| Keating–Snaith moments | a `k²` exponent | area's `k²` is geometric, not `(log T)^{k²}` |
| Goldbach, twin primes | the explicit formula | a parity barrier; the Fold has no parity breaker |
| Collatz | expansion and contraction ledgers | a rhyme of scale, not a dynamical theorem |
| Langlands | additive/multiplicative exchange | the same duality, different categories |
| Yang–Mills mass gap | the horizon (null crease) | no operator, no quantum field |
| Navier–Stokes | the collapse `g₀` | a fluid singularity is not the zero map |
| P vs NP | an existential projection; a solver is a section | no computational model; the linear projection is always split, so the hardness is cost, not existence |
| Poincaré (solved) | the return to the point | the theorem is about `π₁`, not the orbit space |

The rest of the note is the four zones, in order of how much they actually carry, followed by one pass
with the hole field — the smallest exact object — which adds a classifier and five limits but no route.

## Zone 1: the crease, and the three routes to RH

RH is the statement that every zero of `ξ` lies on the crease `Re s = 1/2`. That is exact. What the
Fold does not supply is the **forcing argument**, and there are exactly three known shapes for such an
argument. The Fold's value is that it says what each one would have to be.

### Route A — positivity (the function-field proof)

Over a function field, RH is a theorem: the eigenvalues `α` of Frobenius satisfy `|α| = q^{1/2}`. The
proof does not use an operator; it uses a **definite form**. On a smooth projective surface the
intersection form on the Néron–Severi lattice has signature

```
Hodge index:   (1, ρ−1, 0)          one positive, the rest negative
```

and its negative therefore has signature `(ρ−1, 1, 0)` — exactly the Fold's fold signature
`(n−1, 1, 0)`. This is the sharpest link in the note, and it is a link of **shape**:

```
fold σ_H:      (n−1, 1, 0)          one direction singled out, n−1 along the crease
−intersection: (ρ−1, 1, 0)          one ample class positive, the rest negative
```

The function-field proof works because positivity plus the functional equation squeezes the
eigenvalues onto the circle of radius `q^{1/2}`. **What the Fold lacks is the surface.** It has the
signature shape and the crease, but no arithmetic surface and no intersection form, so the squeeze has
nothing to act on. That is the precise gap, and it is not a gap of language.

### Route B — an operator (Hilbert–Pólya)

If the `γ_n` are the eigenvalues of a self-adjoint `H`, then they are real, and the functional
equation forces the symmetry about `1/2`. The Fold's contribution is structural and exact:

```
H = H* ,   [H, R] = 0 ,   R² = I      ⟹      spectrum real, split by R
```

The crease is the `+1` eigenspace of `R`; an eigenvector with eigenvalue in the `+1` block is on the
crease. So the missing operator must **commute with the fold**, and its spectrum must land in the
crease block. This is a condition, not a construction. The Fold does not produce `H`; it says which
symmetry `H` must respect. Berry–Keating's `xp` Hamiltonian and the Connes trace formula are attempts
to build such an `H`; neither is a proof.

### Route C — a deformation (de Bruijn–Newman)

This is the route where the Fold's own object — theta — is literally the tool. The completed zeta
function, written on the critical line, is a heat-flow family `H_t`; the zeros are real for `t ≥ Λ`,
where `Λ` is the de Bruijn–Newman constant. The known implications are

```
RH  ⇔  Λ ≤ 0                Rodgers–Tao:  Λ ≥ 0        hence  RH ⇔ Λ = 0
```

The theta function is the heat kernel on the circle, and the Mellin transform of theta is the completed
zeta function. So the theta fold of `the-fold-theta.md` is the `t = 0` slice of this flow, and the
crease `1/2` is the centre that the flow preserves. **What the Fold lacks is the bound.** It supplies
the kernel and the crease; it does not bound `Λ` from above. Rodgers–Tao bound it from below; the
Polymath upper bound is `Λ ≤ 0.22`, not `0`.

### Route D — density (the explicit formula)

The explicit formula converts a zero-free region into a prime-counting error term. RH is equivalent to
the error `O(x^{1/2+ε})`. This route needs an estimate, and estimates come from sieve or zero-density
methods. The Fold supplies the exchange (primes ↔ zeros) but no estimate, and the parity barrier in
sieve theory is exactly the wall it cannot cross. Goldbach and the twin-prime conjecture live behind
that wall.

These four are the standard shapes of a forcing argument. The Fold sits at the entrance of each and
supplies the same thing: the crease, and the dictionary of what a zero is. It supplies the forcing in
none.

## Zone 2: the shape links

### Codimension versus multiplicity

The zero pipeline classifies a zero by **codimension**: a facet is `1`, a point is `2`, a vertex is
`n`. That is the right classifier for geometry. It is the wrong classifier for two of the problems:

- **BSD** asks for the *order of vanishing* of `L(E,s)` at `s = 1`, and that order equals the rank of
  `E(ℚ)`. Order is multiplicity, not codimension.
- **Hilbert–Pólya** asks for the *multiplicity* of an eigenvalue, i.e. the dimension of an eigenspace.

So the pipeline is blind to the axis these problems live on. That is not a defect of the pipeline; it
is a statement of its resolution. A zero can have codimension `2` and multiplicity `5`; the pipeline
sees the first number and not the second.

### The GUE class

A single complex structure `J` (`J² = −I`) makes a real vector space complex, and complex symmetry is
the `β = 2` class — the Gaussian Unitary Ensemble. The pair correlation of zeta zeros matches GUE
(Montgomery, Odlyzko). So the Fold's twist, which *is* one `J`, has the right symmetry class for the
zeta statistics.

The correction matters: the twist's invariant is a **symplectic form** `ω(x,y) = ⟨x,Jy⟩` and a
Pfaffian, but a symplectic form is not the quaternionic `β = 4` ensemble. The `β = 4` case needs three
complex structures `I, J, K` with `IJ = K`; the Fold has one. One `J` gives `β = 2`, and `β = 2` is
what the zeros show. The Pfaffian and the unitary class are consistent; "symplectic" here names the
form, not the ensemble.

### The index

The zero pipeline's conservation law,

```
ind(0) + ind(∞) = χ(Sⁿ)
```

is the Poincaré–Hopf theorem, the first case of the Atiyah–Singer index theorem. This is exact: a zero
cannot appear alone, and its partner at infinity is the other end of the compactified field. The Fold
does not produce a new index; it uses the oldest one. The Atiyah–Singer generalization — analytic index
equals topological index — is the exact ancestor of "a zero is a conserved charge."

## Zone 3: the rhymes

- **Langlands.** Automorphic forms and Galois representations are dual, like the Euler product and the
  zeros. The explicit formula is a trace formula, and the Langlands program is the general trace
  formula. The rhyme is real — the Fold's "exchange" is the shape of functoriality — but the
  categories are different, and nothing transfers. In categorical terms the exchange is not an
  adjunction; see `the-fold-categorical.md`.
- **Goldbach and twin primes.** The explicit formula is additive in the zeros; Goldbach is additive in
  the primes. The Fold sees both ledgers, but it has no device that breaks parity, which is what the
  sieve obstacle is. A dictionary is not a sieve.
- **Collatz.** `3n+1` and `n/2` are an expansion and a contraction — the scale ledger's two signs. The
  rhyme is the two-ledger structure; the theorem is about a specific map on `ℤ`, which the Fold does
  not model.
- **Yang–Mills mass gap and Navier–Stokes.** The horizon is a null crease where the induced metric
  degenerates; a mass gap is a spectral gap of a Hamiltonian, and a Navier–Stokes singularity is a
  blow-up of a velocity field. The Fold has neither an operator nor a field equation. The horizon's
  entropy and temperature are a scaling reading in the homothetic family, not a derivation of
  thermodynamics. These are rhymes, and stating them as more would be the false-friend error.
- **Unruh and the thermal observer.** The horizon clock and the Unruh effect share a null crease and a
  `2π` period, but the Fold's `k` is a homothety, not a boost: it is dimensionless, conformal, and has no
  Killing vector. The Fold gives `T ∝ 1/k` through the surface gravity, not `T ∝ a`; the local Unruh
  temperature is a rhyme, not a derivation. See `the-fold-unruh.md`. The wedge's entanglement entropy and
  the species problem are in `the-fold-entanglement.md`; the holographic coefficient is in
  `the-fold-holography.md`; the general coefficient (Wald entropy) and its boundaries are in
  `the-fold-wald.md`.
- **P vs NP.** No contact for a proof, but one exact diagram: `NP` is an existential projection and a
  solver is a section; the Fold's linear projection is the simplest instance, and it is always split, so
  the hardness is the cost of the section, not its existence. The two ledgers and the one-way horizon
  are rhymes. Every Fold invariant is polynomial-time, so it can only collapse the classes, not separate
  them. See `the-fold-complexity.md`.

## Zone 4: the false friends

- **`k²` in the area law is not `(log T)^{k²}` in the moment conjecture.** Area scales as the square of
  the height because the form is degree two. The Keating–Snaith exponent is a different `k²`, from the
  combinatorics of the moment. Same symbol, different origin.
- **The 4-fold closure's signature zero is not Rochlin's theorem.** `cos(2π/4) = 0` is the symmetric
  part of a plane rotation; Rochlin's `σ ≡ 0 mod 16` is a theorem about closed spin 4-manifolds. Both
  are "zero" and "four"; that is all they share.
- **A zeta zero is not the Fold's zero.** The Fold's zero is the zero map, inertia `(0,0,n)`; a zeta
  zero is an isolated cancellation, codimension two. The note `the-fold-zeta.md` states this; the
  pipeline note states it again, and it bears repeating here because the two are most often conflated.
- **"The critical line is the fixed set of the functional equation" is false.** The fixed set of
  `s ↦ 1−s` is the point `1/2`; the line is the fixed set of the composition with reality,
  `R(s) = 1 − s̄`.
- **The critical line's `1/2` is not the entanglement log coefficient.** The theta half-density
  exponent gives `Re s = 1/2`; the log coefficient is the A-type anomaly (`c/3` in 2D, `−4a` in 4D). A
  theory with `c = 3/2` makes the numbers coincide, but the objects differ. See
  `the-fold-logarithm.md`.

## The hole field: what the smallest exact object adds

The engineering note ended at the edge of transfer. This note's map has the same edge, and the hole
field is the smallest object that shows where it is. On `ℂ*`,

```
ω = dk/k ,   Res_0 ω = 1 ,   Res_∞ ω = −1 ,   ∮_{|k|=r} ω = 2πi
η = Im ω = dθ ,   ∮ η = 2π ,   H¹_dR(ℂ*) = ℝ[η]
```

`ω` is the unique `ℂ*`-invariant meromorphic `1`-form up to scale; `η` is the twist class. That is the
whole object. It adds one exact theorem to the problem map — the argument principle — and five limits.
It adds no route.

### The argument principle is the exact transfer

For meromorphic `f`, `d log f = f'/f` is a meromorphic `1`-form, and near a zero of order `n`,

```
f(z) = (z−a)^n g(z) ,  g(a) ≠ 0   ⟹   d log f = n dz/(z−a) + d log g
```

so the residue is the order. On a contour avoiding zeros and poles,

```
(1/2πi) ∮_γ d log f = Z − P
```

The Fold's `ω` is the unit case `f(k) = k`, `n = 1`, one zero at `0` and one pole at `∞`. Every problem
that asks **how many** or **what order** is a coefficient of this form; every problem that asks
**where** is not. That is the exact content and the exact limit in one line.

| question | hole-field answer | exact? |
|---|---|---|
| how many zeros inside `γ`? | `(1/2πi)∮ d log f` | exact, argument principle |
| what is the order at `a`? | `Res_a d log f` | exact |
| where are the zeros? | — | no: the residue is a contour sum |
| which contour? | any avoiding the divisor | exact, but arbitrary |

### RH: the count is exact; the placement is the wall

`ξ` is entire and `ξ(s) = ξ(1−s)`. `d log ξ = ξ'/ξ` has poles at the zeros of `ξ` — inside the
strip, the nontrivial zeros — with residue the multiplicity. On a rectangle bounding `0 < Re s < 1`,
`−T < Im s < T`,

```
N(T) = (1/2πi) ∮ ξ'/ξ
```

counts the zeros in the strip, with multiplicity. RH says every one of them has `Re s = 1/2`. The
argument principle supplies `N(T)`; the Riemann–von Mangoldt formula evaluates it. Neither supplies the
abscissa. The reason is structural: a residue is invariant under any change of contour that does not
cross the divisor, so it is blind to motion *along* the contour. Placement needs a positive-definite
quantity, which is Route A, or an operator, which is Route B. The hole field is neither.

Note also: `d log ξ` is **not** `cω`. On any compact set it is a finite sum
`Σ n_j dz/(z−ρ_j)` plus a regular term; the Fold's `ω` is the one-zero model. Saying "zeta is the hole
field" is the false friend; saying "the hole field is the unit-residue model of the argument
principle" is exact. The separation matters because `ω` has its pole at the *coordinate origin*, while
`ξ'`/`ξ` has its poles at the zeros, wherever they are.

### BSD and Hilbert–Pólya: the residue reads the axis the pipeline cannot

Zone 2 said the pipeline classifies by codimension and is blind to multiplicity. The hole field
repairs exactly that, and only that.

- **BSD.** `L(E,s)` is entire, and `ord_{s=1} L = Res_{s=1} d log L`. The conjecture is
  `ord_{s=1} L = rank E(ℚ)`. The hole field reads the left side exactly; it has no arithmetic input
  that identifies it with the right. The classifier is supplied; the theorem is not.
- **Hilbert–Pólya.** When the determinant is defined, `det(z−H)` is entire, and
  `Res_{z=λ} d log det(z−H) = mult(λ) = dim ker(H−λ)`. The hole field reads multiplicity exactly —
  once `H` exists. A residue of a determinant is not an operator.

| problem | hole-field statement | it supplies | it still lacks |
|---|---|---|---|
| RH | `N = (1/2πi)∮ ξ'/ξ` | the count | placement on the crease |
| BSD | `ord_{s=1} L = Res_{s=1} d log L` | the order | `ord = rank` |
| Hilbert–Pólya | `mult λ = Res_λ d log det(z−H)` | the multiplicity | `H` |
| function-field RH | residues of the explicit formula | the coefficient | positivity, the surface |

The last row is the honest one for Route A: the explicit formula is a sum of residues at the zeros and
at the pole, and the positivity that proves the function-field case is a polarization of the surface,
not a residue of the form. The hole field counts; the surface forces.

### P vs NP: point propagation has no cost metric

The point-propagation theorem has three readings; each meets the P vs NP diagram at a different place,
and none yields hardness.

1. **The trivial orbit.** `g_k(P₀) = P₀` for every `k`: the basepoint is fixed by the whole scale
   action. Read a witness as a basepoint — a rhyme, not an identification — and its orbit is
   trivial; the *search* for the witness is not. The Fold's action is free on `ℂ*` and trivial only
   at `P₀`; a discrete search has no continuous action at all. "The orbit does not move" is a
   statement about the group, not about the algorithm.
2. **The tangent cone.** The orbit's tangent cone at `P₀` is `{0}` — the derivative `Dg₀` vanishes,
   and the orbit is a point. The ambient tangent space at `P₀` is `ℝⁿ`, with directions `S^{n−1}`,
   but those are not directions of the orbit. A solution set's tangent cone is a cone cut out by the
   linearized verification equations; at a smooth solution it is a linear subspace. Either way the
   local model is linear and polynomial; hardness, if it exists, is a property of the global
   arrangement of solutions, not of any tangent cone.
3. **Hole propagation.** A residue is conserved under biholomorphic change of coordinates. Every
   invariant the Fold computes is therefore deformation-invariant and cheap. P vs NP asks for a
   **cost separation**, which is not a deformation invariant. A polynomial-time complete invariant
   would decide the classes; the Fold has no complete invariant for computation, and its invariants
   can only merge the classes, not separate them.

The zero-parameter stratum is where the false friend lives. Model a unique-witness instance as a
point, `(ℂ*)^0`: empty sum `0`, empty product `1`, trivial orbit. "Zero parameters" is the identity of
the parameter action, not the identity of the search. A unique solution is a point, and a point is not
free. The algebraic emptiness is exact; the computational inference is invalid.

### The five limits

| limit | the field gives | the problem needs | where |
|---|---|---|---|
| count vs placement | `∮ d log f` | an abscissa | RH |
| coefficient vs existence | `Res d log f` | the object `f` or `H` | BSD, Hilbert–Pólya |
| period vs parity | `2π` of `dθ` | `ℤ/2` | Goldbach, twins |
| puncture vs singularity | a removed point | a blow-up | Navier–Stokes, Yang–Mills |
| flow vs map | `k ↦ e^t k` | a discrete dynamics | Collatz |

Each row is a different reason, not a different slogan:

- **Count vs placement.** A residue is a contour sum; it is invariant under moving the contour. It
  cannot localize a zero. RH is a placement problem.
- **Coefficient vs existence.** `d log` presupposes `f` or `H`. BSD's rank and Hilbert–Pólya's
  operator are existence problems; the residue reads the order once the object is given.
- **Period vs parity.** `2π` is the period of `dθ`; parity is `ℤ/2`. A period is continuous and a
  parity is discrete, and the sieve barrier is the discrete one. The `2π` in the Montgomery–Odlyzko
  sine kernel is a normalization of the pair correlation, not the hole's period: same symbol,
  different origin.
- **Puncture vs singularity.** `ℂ*` is the plane with `0` removed; `ω` has a pole at the puncture, but
  the puncture is not in the space. The Fold's hole is `k = 0`, not the horizon `k = k*`; the horizon
  is regular in the scale field. A blow-up is a singularity *in* the space, not a point removed from
  it. The Fold's hole is harmless precisely because it is a coordinate hole.
- **Flow vs map.** `ω` integrates to the flow `k ↦ e^t k`. Collatz is a discrete map, not a
  one-parameter group. The scale ledger's two signs rhyme with expansion and contraction; the theorem
  is about a specific map on `ℤ`.

### Several scales, one diagonal

The stratified field is `Ω_r = Σ_{i=1}^r dk_i/k_i` on `(ℂ*)^r`; its residues are the sum of the
coordinate residues, and `Re Ω_r` is the log-scale, `Im Ω_r` the twist. A problem with `r` independent
scales would sit on the `r`-stratum, and the Fold controls the **diagonal** part only. BSD's regulator
is a height-pairing determinant, not a sum of coordinate residues; the Fold's `Ω_r` is diagonal and
cannot produce it. The same boundary was reached in the engineering note: shear, curvature, and the
full connection are external. The hole field is the diagonal scale–twist datum, not a general
geometry.

### What the extension changes

- It adds one exact classifier to Zone 2: multiplicity as `Res d log`, which the codimension pipeline
  could not see.
- It adds no route. The four walls are unchanged, and the new section explains why: the first is a
  placement problem that needs a surface, the second and third are existence problems, and the fourth
  is parity.
- It sharpens the P vs NP entry: the Fold's invariants are local (derivatives) and
  deformation-invariant (residues), hence polynomial; hardness is global and cost-theoretic.
- It gives the correct form of the unique-solution false friend: zero parameters is not zero search.

## What would count as progress

The map says exactly what is missing, one item per route:

1. **A surface.** An arithmetic surface whose intersection form has the fold's signature and whose
   positivity forces the zeros onto the crease. Missing: the surface.
2. **An operator.** A self-adjoint `H`, commuting with `R`, whose spectrum is `{γ_n}`. Missing: `H`.
3. **A bound.** A proof that de Bruijn–Newman `Λ ≤ 0`, matching Rodgers–Tao's `Λ ≥ 0`. Missing: the
   upper bound.
4. **A parity breaker.** A sieve or density argument that reaches the `1/2` exponent. Missing: the
   argument.

Each of the four is a known open problem in its own right. The Fold's contribution is to show that
these four are the same question seen from four sides, and that the crease is where all four must meet.
It does not cross any of them.

The hole field does not add a fifth item. It classifies the four: the first is placement, the second
and third are existence, the fourth is parity. The one thing the Fold counts exactly — the number and
the order of the zeros — is not the thing any of them asks for. Counting is not placing, a coefficient
is not an object, a period is not a parity, a puncture is not a singularity, and a flow is not a map.

## Checks

The signature shape match and the Hilbert–Pólya commutation are exact; the numbers below confirm them
for small `n` with random data.

| check | `n=2` | `n=3` | `n=4` | `n=5` |
|---|---|---|---|---|
| fold inertia `σ_H` | `(1,1,0)` | `(2,1,0)` | `(3,1,0)` | `(4,1,0)` |
| negative Hodge form, `ρ=n` | `(1,1,0)` | `(2,1,0)` | `(3,1,0)` | `(4,1,0)` |

The fold and the negative intersection form have the same inertia at every rank. That is the shape
match of Route A; it is arithmetic, not analysis.

For Route B, take `H = Hᵀ`, `R = diag(1,…,1,−1,…,−1)`, and `[H,R] = 0`. Then:

| check | value |
|---|---|
| `‖H − Hᵀ‖` | `0` |
| `‖HR − RH‖` | `0` |
| max `\|Im λ\|` over the spectrum | `0` |
| each eigenvector's mass on the `+1` block | `1` or `0` |

Every eigenvector lies wholly in the crease block or wholly in the normal block. That is the exact
content of "the operator must commute with the fold": its spectrum splits along the crease. The
existence of such an `H` with spectrum `{γ_n}` is the open problem, not the check.

The de Bruijn–Newman statements are definitions and literature (`Λ ≤ 0` ⇔ RH; Rodgers–Tao `Λ ≥ 0`);
they are not recomputed here. The GUE pair correlation is likewise numerical literature, not a
computation in this note.

The hole-field statements are identities, not estimates: the period of `dk/k` on the unit circle is
`2πi`, its residues at `0` and `∞` are `1` and `−1`, and the residue of `d log det(z−H)` at an
eigenvalue is its multiplicity. The last is the argument principle applied to a polynomial; it is the
one new exact classifier, and it is a restatement, not a bound.

## The one sentence

**The Fold reformulates RH exactly and rhymes with a dozen other problems, but its real value is a
map: positivity needs a surface, Hilbert–Pólya needs an operator, de Bruijn–Newman needs a bound, and
the explicit formula needs a parity breaker — four known walls, one crease.**

## Files

`the-fold-problems.md` (this note). The crease and the functional equation are in
`the-fold-zeta.md`; the theta fold and the heat kernel are in `the-fold-theta.md`; the zero types and
the codimension/multiplicity distinction are in `the-fold-pipeline.md`; the signature and the
Poincaré–Hopf index are in `the-fold-signature.md`; the facet classification is in
`the-fold-facets.md`; the universal logarithm and the `1/2` distinction are in
`the-fold-logarithm.md`; the engineering zone — similitude, crease kinematics, sampling, and the
false friends — is in `the-fold-engineering.md`; the projection/section diagram and the P vs NP wall
are in `the-fold-complexity.md`; the closure restriction and the crystallographic `m` are in
`the-fold-closure.md`; the lookup is `the-fold-key.md`.
