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
  thermodynamics. These are rhymes, and stating them as more would be the false-friend error. One
  phrasing to name: "the mass gap is the imaginary fabric connecting the real fabric." The exact kernel
  is `i² = −1` — the twist squared is the fold, and one complex `k` carries scale in its modulus and
  twist in its phase. That is one parameter with two coordinates, not two fabrics with a connector. And
  a gap is `inf spec H > 0`, a statement about the real spectrum of an operator; the Fold's `k` is a
  group parameter, and its only punctured point is `k = 0`, an absence rather than a gap. The complex
  plane where a gap appears as a pole off the real axis is the momentum plane, not the `k` plane: same
  picture, different object. Calling them the same is the false friend.
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
- **"Twister" is not "twistor".** The Fold's twist is a quarter turn, `J² = −I`, one orthogonal
  complex structure on a real plane. In Euclidean four-space the orthogonal complex structures at a
  point form `S² ≅ ℂP¹` — precisely the twistor line over that point — so the Fold's `J` is one
  *point* of a twistor line, not the line, and not `ℂP³`. Twistor theory then adds what the Fold does
  not have: the incidence relation `ω = i x π`, the conformal group `SU(2,2)`, spinors, and the
  Penrose transform `H¹(PT, O(−2h−2))` ↔ massless fields of helicity `h`. The hole field's
  `H¹_dR(ℂ*) = ℝ[η]` shares the *shape* — a cohomology class carries the content — but not the
  manifold, the coefficients, or the dimension. Same square root of `−1`; different space. The
  shared `2π` (the fan's closure, the twistor phase) is a rhyme, not an identity. Calling the two the
  same theory is the false friend.

## The ladder of `J`s

The Fold has one complex structure, `J² = −I`, on a real plane. The orthogonal complex structures on
`ℝ^{2m}` form a symmetric space, and its dimension is the first place the dimension `2` of the Fold
stops being enough:

```
SO(2m) / U(m) ,        dim = m(m − 1)
```

| `m` | `SO(2m)/U(m)` | dim | what it is |
|---|---|---|---|
| 1 | point | 0 | the Fold's `J`; nothing to vary |
| 2 | `S² = ℂP¹` | 2 | the twistor line over a point of `ℝ⁴`; the unit imaginary quaternions |
| 3 | `ℂP³` | 6 | the twistor space over `S⁴`; also the complex structures on `ℝ⁶` |
| 4 | `SO(8)/U(4)` | 12 | no familiar name |

In complex dimension the ladder is `m(m−1)/2` = `0, 1, 3, 6`: the triangular numbers. Only the first
three rows are projective spaces; `SO(8)/U(4)` has rank two and cannot be `ℂP⁶`.

The `m = 3` row is an exact homogeneous-space identity: `SO(6)/U(3) ≅ SU(4)/S(U(3) × U(1)) = ℂP³`,
and the same `ℂP³` is the twistor fibration `S² → ℂP³ → S⁴`, i.e. `ℂP³ = SO(5)/U(2)`. So the twistor
space is itself a moduli space of complex structures one dimension up. That is a statement about
homogeneous spaces, not a derivation of twistor theory.

At `m = 2` the sphere is the unit imaginary quaternions and the Fold's `J` is the point `i`. The GUE
paragraph above says the rest: one `J` gives `β = 2`; the quaternionic `β = 4` needs the triple
`I, J, K` with `IJ = K`, three orthogonal axes — three points of that same `S²`. The Fold has one
point of the sphere, so it can see the unitary class and not the symplectic one. Twistor theory is the
theory of the whole sphere; the Fold is the theory of one point on it.

The letter `m` is a false friend across the two uses: in `D_m` it is the closure order `m = π/α` and
the group has order `2m`; in `SO(2m)/U(m)` it is half the dimension. Same letter, different index.

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

## The second map: problems of description

The first map is about problems with an arithmetic or geometric object: RH, BSD, Hodge, Yang–Mills,
Navier–Stokes, P vs NP. The second map is about problems whose object is a **description**: a measure,
a section, a coarse-graining, or a self-reference. The Fold's machinery — an involution, a quotient, a
cut, a completion — is the right size for these, and the zones are sharper because the obstruction is
often a single missing object rather than a missing theory.

The rule is unchanged: exact means the Fold's object is the problem's object; reformulation means the
problem is renamed; rhyme means the shape matches and the objects do not; false friend means the symbol
matches and the object does not.

| problem | the Fold's object | zone | what stops it |
|---|---|---|---|
| Banach–Tarski | an invariant mean fixed by the group | exact | `F₂` is not amenable; the equivalence is exact, the theorem is not proved here |
| Simpson's paradox | aggregation is a quotient | exact | a quotient need not preserve order |
| Sorites / vagueness | tolerance is not an equivalence | exact | no quotient exists |
| improper priors, two envelopes, St. Petersburg | `dk/k` is an infinite invariant measure | exact | no scale-invariant probability on the line |
| raven paradox | contraposition is an involution | exact | the involution is logical, not evidential |
| Hilbert hotel | a bijection is not an isomorphism | exact as a model | cardinality is invariant, structure is not |
| Monty Hall | the host's action revises the section | exact as a model | the probability is a count, not a property of the doors |
| axiom of choice / sections | a cut is a section of the chart | exact as a model | the quotient is canonical; the section is a choice |
| natural kinds / universals | a kind is an orbit of a group action | exact as a model | the group is chosen; the orbit is not an essence |
| problem of time (Wheeler–DeWitt) | the clock is a section of the constraint surface | reformulation | no dynamics, no quantization |
| arrow of time | the involution is time-symmetric | reformulation | the arrow needs a coarse-graining and a measure |
| anthropic / measure problem | the observer's cut is a conditioning event | reformulation | no canonical measure on the space of charts |
| Ship of Theseus | identity is a quotient by a coarse-graining | reformulation | the quotient is chosen, not given |
| measurement problem | collapse is not an equivariant section | rhyme | the cut is equivariant; collapse is not |
| black-hole information | the horizon is a scar; information is a quotient invariant | rhyme | no quantum state, no unitarity, no Page curve |
| hierarchy problem, cosmological constant | the Fold's scale invariance is exact | rhyme | the Fold has no mechanism to break it; calling it a solution is the false friend |
| Gödel, Russell | the chart excludes the observer | rhyme | `S¹ ∖ {p} ≅ ℝ` is topology, not semantics |
| hard problem of consciousness | the observer is `(d,w)` | the absence | the map names the edge; it does not cross it |

The four rows marked *exact as a model* are the Fold's own structures applied to philosophy: a cut is
a section of the chart, a kind is an orbit of a group action, cardinality is what a bijection
preserves, and a probability is a count over the observer's section. They are exact as models and not
as metaphysics: the model says which object is which, and the group or the cut remains a choice.

Not every problem belongs on the map. Proton decay, dark matter, baryogenesis, the origin of life,
and the Fermi paradox supply no Fold object: no involution, quotient, cut, or measure is given by the
problem, and naming one would be decoration. They are not rows; they are the blank space around the
table. The same rule excludes a "theory of everything": the Fold has a diagram, not a dynamics, and
the diagram does not predict a particle.

### The exact additions

Five rows of the table are exact in the strict sense, and four more are exact as models. Every strict
one is a statement about measure, quotient, or logic, not about arithmetic geometry. That is why they
can be checked in the Lean file.

**Amenability.** Let a group `G` act on a set `X`. A `G`-invariant mean is a fixed point of the action
on the dual of `ℓ^∞(X)`. For a discrete `G`, such a mean on all subsets exists if and only if `G` is
amenable (von Neumann). The free group `F₂` is not amenable; its paradoxical decomposition is the
algebraic heart of Hausdorff's paradox and, with choice, of Banach–Tarski. The Fold's `Fix(G)` language
is exact here: the invariant is a fixed point, and the theorem is that the fixed point does not exist.
What the Fold adds is the question "fixed by which group?"; what it does not add is the proof.

**Quotients and order.** Simpson's reversal is the statement that the quotient map from strata to the
pool does not preserve an order:

```
stratum 1:  81/87  vs  234/270       treatment better
stratum 2:  192/263 vs  55/80        treatment better
pool:       273/350 vs  289/350      control better
```

The finite table is exact. The Fold's `X → X/F` is the same kind of map: it forgets the side, and
forgetting can reverse a comparison. This is the exact content of "the quotient is not the object." The
Lean lemma `simpson_reversal` checks the three cross-multiplied inequalities.

**Tolerance.** A tolerance relation is reflexive and symmetric but not transitive. The equivalence
closure of `0 ~ 1 ~ 2` identifies `0` and `2`, so the quotient by tolerance is not a set of heaps and
non-heaps; it is one class. This is the exact obstruction behind the sorites. The Fold's quotient
requires an equivalence relation; a tolerance supplies none. The Lean lemma `tolerance_not_trans` is the
finite counterexample.

**Improper measure.** On `ℝ_{>0}`, the invariant measure is `dk/k`, and

```
∫_0^∞ dk/k = ∞ .
```

The completion `0 ~ ∞` turns the line into a circle, where `dθ/2π` is a finite invariant probability.
The observer's cut `S¹ ∖ {p} ≅ ℝ` turns the finite measure back into the infinite one. This is the exact
measure-theoretic version of the cut: the circle has a canonical probability; the line does not. Two
envelopes and St. Petersburg are the same obstruction in a discrete dress — a uniform prior on `ℕ` does
not exist.

**Contraposition.** `(P → Q) ↔ (¬Q → ¬P)` is an involution on the pair of truth values. The raven
paradox's inference — a white shoe confirms all ravens — is not a consequence: the involution preserves
truth, not confirmation. The Lean lemma `contraposition` checks the Boolean identity; the evidential
step is the false friend.

### The reformulations

**Time.** The Wheeler–DeWitt equation is `HΨ = 0`: there is no external time. A clock is a field `T`
with `dT ≠ 0` along the flow, i.e. a section of the constraint surface; different clocks are different
sections. The Fold's observer's cut is a section. This is a reformulation: it names the object (a
section) and the invariance (the quotient), and it supplies neither the quantization nor the dynamics.

**Arrow.** The fold is an involution; it is time-symmetric. An arrow requires a dynamics `φ_t`, a
coarse-graining `q`, and a measure `μ` such that `S = −log μ` increases under `φ_t`. The Fold has `q`
but no `φ_t` and no `μ`. The second law is therefore a rhyme, not a theorem of the Fold; and the
involution is the opposite of an arrow.

**Anthropic.** The observer's cut is a conditioning event. A probability requires a measure on the
space of charts; the Fold has no canonical measure there. The `0 ~ ∞` completion gives a measure on the
parameter circle, not on the space of charts. This is the precise gap, and it is why the measure problem
is not solved by naming the observer.

### The false friends

- **Collapse is the cut.** The cut is equivariant (`p(F x) = p x`); collapse is not
  (`collapse(U_t ψ) ≠ U_t collapse(ψ)` in general). Same shape, different object.
- **The second law is the fold.** The fold is reversible. The second law is a statement about a
  coarse-grained quotient with a measure; the fold supplies the quotient and not the measure.
- **The hierarchy is the Fold's scale invariance.** The Fold's scale invariance is exact and
  unbroken; the hierarchy problem is its breaking. The Fold has no mechanism for the breaking.
- **The cosmological constant is the Fold's zero.** The Fold's zero is the zero map, not a
  cancellation of vacuum energy. Same symbol, different object.
- **Fine-tuning is a chart choice.** A chart choice is a section; a probability over charts needs a
  measure. Without the measure, "the chart is fine-tuned" has no content.
- **The simulation argument is a chart inside a chart.** The regress is a regress of charts, not a
  probability; the Fold can draw the nesting and cannot weight it.
- **Free will is the two sides of the fold.** The two sides are the orbit of a deterministic
  involution. A choice is not an involution.
- **The Fold solves the hard problem.** The observer is `(d,w)`. The pattern places the cut and names
  the absence; it does not fill it.

### Two boundary cases: astigmatism and `0/0`

Neither is an open problem, and neither is a row of the table. They are the two ways a symbol can
look like the Fold and fail to be it: a tensor that looks like a crease, and a quotient that looks
like freedom.

**Astigmatism: exact optics, false friend as a fold.** A spherical wavefront has one principal
curvature, `κ₁ = κ₂ = κ`; its caustic is a point at `1/κ`. A regular astigmatic wavefront has two,
`κ₁ ≠ κ₂`; its caustic is the pair of focal lines at `1/κ₁` and `1/κ₂`, separated by the Sturm
interval. The exact object is the shape operator, a symmetric `2×2` matrix: the spherical equivalent
is its trace, the astigmatism its traceless part. This is exact optics, and it is not a fold. A fold
is a reflection or a rank drop; the power matrix is invertible and symmetric. The Fold's scale-twist
`k e^{iθ}` is conformal — two equal singular values — so it carries the scalar part and the rotation,
not the traceless shear. The crease and the cylinder axis are both eigenvectors of an orthogonal pair,
but the fold's eigenvalues are `(+1,−1)` and the lens's are `(κ₁,κ₂)`: a sign split, not a magnitude
split. The axis is a spin-2 angle; a traceless symmetric matrix rotates by `2α`, while the Fold's
twist rotates vectors by `α`. "Astigmatism is the Fold's twist" is therefore exact only after the
double cover `θ = 2α`, and "astigmatism is the crease" is a false friend. The circle of least
confusion is a second false friend: a circular blur at the dioptric midpoint is not a spherical
wavefront. Regular (toric) astigmatism is the quadratic model; irregular astigmatism needs
higher-order aberrations and has no single axis, so it lies outside the model. The word is a rhyme —
*a-stigma* is the loss of the point image, and the Fold's `P₀` is a point — but the Fold's point is
a fixed point, not an image point.

**`0/0`: exact arithmetic, false friend as freedom.** In a field, `0/0` is not an element: division
requires a nonzero denominator, and `0x = 0` is solved by every `x`. The exact statement is a
solution set, not a value: the preimage of `0` under the zero map is the whole space, and the zero
map has inertia `(0,0,n)`. As a limit the form is indeterminate: `x/x → 1`, `x²/x → 0`, `x/x²`
diverges, and `x sin(1/x)/x` has no limit. A rate is needed, and the Fold's scale supplies one:
`k^p/k^q = k^{p−q}` tends to `0`, `1`, or `∞` as `k → 0⁺`, according to the sign of `p−q`. The
indeterminacy is a weight difference, not a freedom. Totalized systems choose a convention — Lean's
`Rat` evaluates `0/0` to `0`, IEEE gives `NaN`, and `NaN ≠ NaN` — which is the false friend in its
purest form: the symbol survives and the object does not. The philosophical step fails twice.
"Undefined" is not "free": a partial function has no value at the point, and the zero map collapses
every input to one value without distinguishing among them. And freedom requires a selection among
alternatives; `0/0` is the absence of a selection. The Fold can name the place — the cut, the zero
map, the missing section — but it cannot fill it. The claim that free will is equal to `0/0` is
therefore, at best, a rhyme with the observer's cut, not an identity; as an equation it is the false
friend. The existing entry "free will is the two sides of the fold" fails for the same reason: an
orbit of a deterministic involution is not a choice.

**Flatness.** The hole is flat in the exact sense: `ω = dk/k` is closed, `dω = 0`, but
`∮_{|k|=1} ω = 2πi`, so it has no single-valued primitive. A flat hole is not a cavity; it is a
period. Flatness removes the local obstruction — curvature — and leaves the global one, a loop. The
developing map makes the local statement exact: on the universal cover of `ℂ*` any branch of `log`
is a chart, and the deck transformation `z ↦ z + 2πi` is the period. "Any application" is therefore
true on the cover and false on the quotient; the applications differ by the holonomy. One can add
the point topologically, but the class dies in the cohomology of the filled space and the form
acquires a pole; the completion `0 ~ ∞` is a compactification, not a filling. The zero map has
`Dg_0 = 0` and inertia `(0,0,n)`, so there is no tangent direction in which to fill the puncture.
This is why the Fold's hole is harmless as a coordinate hole. If "flat" is offered as the reason the
hole is free, that is the false friend: a flat hole is a period and a constraint, not a freedom.

**The integer exponent.** `z^{e^{iπ}}` is `z^{-1}` because `e^{iπ} = -1`. A complex power is
multi-valued for a non-integer exponent, but at an integer every branch of `log` gives the same
value: `e^{-2πin} = 1`. This is the cleanest exact case of "many developments, one answer." The map
`ι(z) = 1/z` is an involution on `ℂ*`: its fixed points are `±1`, it swaps `0` and `∞`, and its
quotient is the Joukowski map `J(z) = z + 1/z`, branched at `±1` with critical values `±2`. The
fiber is exactly the orbit: `J(z) = J(w)` gives `(z−w)(zw−1) = 0`, so `w = z` or `w = 1/z`. On the
log cover it is the half-turn `w ↦ -w`; the deck translation makes the fixed points `w = πi n`.
This is not the real reflection `σ_H`: both are `ℤ/2`, but `σ_H` has a codimension-one fixed
hyperplane and reverses orientation, while `ι` has two fixed points and preserves orientation; the
quotient of `σ_H` is a half-space with boundary, the quotient of `ι` is a branched cover. The shared
group is exact; the shared geometry is a rhyme. This is a canonical Fold — involution, orbit, crease,
quotient, branch locus — and it is exactly what `0/0` is not: an integer exponent collapses the
branches; a zero denominator has no value to collapse to. The Weyl reading names the quotient: on
`T = {diag(z, z⁻¹)}` the group `W ≅ ℤ/2` swaps the eigenvalues, and `J` is the trace, so the orbit
space is `T/W ≅ ℂ` and the branch points `±2` are the traces of the central elements `±I`. Normalizing
the critical values gives the Belyi coordinate `B(z) = (J(z)+2)/4 = (z+1)²/(4z) = det(A+I)/4`, with
`1−B = det(I−A)/4`; its dessin is the unit circle with the two marks `±1`, i.e. the `m = 2` wheel.
With `z = λ`, `B = (λ + 1/λ + 2)/4` is an affine function of the Hauptmodul `λ + 1/λ` of the
index-three group `Γ⁰(2)` (a conjugate of `Γ₀(2)`), and `j = 64(4B−3)³/(B−1)` is the degree-three
map to the `j`-line, so the `m = 2` dessin is the quotient of the λ-dessin by `λ ↦ 1/λ`, not a
degeneration of `X(2)`. That is a rhyme with the closure, not a new route.

**Three folds, three creases.** The comparison sharpens when the navel inversion is put beside the
real reflection and the holomorphic inversion:

| fold | map | fixed set | codim | orientation | quotient |
|---|---|---|---|---|---|
| `σ_H` | `x ↦ x − 2(x·n)n` | hyperplane `H` | 1 | reversing | half-space, boundary `H` |
| `I_ρ` | `z ↦ ρ²/z̄` | circle `\|z\| = ρ` | 1 | reversing (anti-holomorphic) | `\|w\| ≥ 2`, boundary circle |
| `ι` | `z ↦ 1/z` | `±1` | 2 | preserving (holomorphic) | `ℂ`, branched at `±2` |

The navel inversion is the Fold's original geometric fold: in polar form `I_ρ(r e^{iθ}) = (ρ²/r)
e^{iθ}`, so it preserves the argument and inverts the radius. Its orbits are the reciprocal pairs on
each ray, and its fixed set is the circle `|z| = ρ`. The quotient coordinate `w = z/ρ + ρ/z̄` is
invariant, and `|w| = r/ρ + ρ/r ≥ 2`, with equality exactly on the fixed circle; the quotient is the
closed exterior disk `|w| ≥ 2`, whose boundary is the crease. Because `I_ρ` is anti-holomorphic, the
crease is a real curve, codimension 1. The holomorphic inversion drops the conjugation: its fixed set
is two points, codimension 2, and its quotient is `ℂ`, branched at `±2`. The structural reason is
exact: the fixed set of a holomorphic involution is a complex submanifold (real codimension 2), while
the fixed set of an anti-holomorphic involution is a real submanifold (real codimension 1). Removing
the bar collapses the circle to `±1` and turns the boundary into a branch locus. `σ_H` is the linear
isometric model, `I_ρ` the conformal anti-holomorphic model, `ι` the conformal holomorphic model. On
the unit circle `ρ = 1`, `I_1` fixes the circle pointwise while `ι` acts by `z ↦ z̄`; their agreement
is only at `±1`. The shared `ℤ/2` is exact; "they are the same fold" is the false friend.

**The Fricke involution.** The index-three curve `Γ⁰(2)\ℍ` carries a second `ℤ/2`, the Atkin–Lehner
involution `τ ↦ -2/τ`. On the `B`-line it is the Möbius involution

```
f(B) = B/(B − 1),    f(f(B)) = B,
```

with fixed points `B = 0` and `B = 2`, swapping `B = 1` and `B = ∞`. This is not the deck involution
`λ ↦ 1/λ` (which is trivial on `B`), and it is not the holomorphic inversion `z ↦ 1/z`. Applied to
the Belyi map, it sends

```
B(z) ↦ B(z)/(B(z) − 1) = ((z + 1)/(z − 1))²,
```

which is the **dual** Belyi map: the double zero at `−1` stays, the double value `1` at `1` becomes a
double pole, and the simple poles at `0, ∞` become simple value-`1` points. So the Fricke involution
exchanges the `m = 2` dessin with its dual: the vertex `B = 1` becomes a face center, and the face
centers `B = 0, ∞` become vertices. It is an exact `ℤ/2` on the modular curve, not on the dessin; the
dessin is not invariant, it is dualized.

**The character variety and the Markoff surface.** The trace coordinate of the Weyl section is the
first case of a general statement. For a once-punctured torus the character variety is cut out by the
Markoff equation

```
x² + y² + z² − xyz = 0,    x = tr A, y = tr B, z = tr AB,
```

with `A`, `B` in `SL₂` and the commutator parabolic. This is the Fricke identity at `tr(ABA⁻¹B⁻¹) = −2`
in the classical normalization: for diagonal `A = diag(a, a⁻¹)`, `B = diag(b, b⁻¹)`, both sides are
identically `4`. The surface is singular exactly where the two trace coordinates stop being independent:

| fact | computation |
|---|---|
| gradient at the origin | `(0, 0, 0)` |
| Hessian at the origin | `2I` |
| tangent cone | the quadratic cone `x² + y² + z² = 0` |
| Vieta involution `s_z` | `(x, y, z) ↦ (x, y, xy − z)` |
| invariance | `F(x, y, xy − z) = F(x, y, z)` identically |
| fixed curve of `s_z` | `z = xy/2`, i.e. `4x² + 4y² − x²y² = 0` |

Each Vieta involution is a fold: an exact `ℤ/2` with a fixed curve, and the three of them generate
the action of the mapping class group on the character variety. The origin is not a point of the
surface to be resolved away — it is where `0/0` lives, the same zero-map kernel the Fold already
records, now with coordinates. The classical Markoff surface `x² + y² + z² = 3xyz` is this one
rescaled by `3`: `F(3X, 3Y, 3Z) = 9(X² + Y² + Z² − 3XYZ)`, so the same singular point and the same
Vieta folds appear in both normalizations. The orbit of `(3, 3, 3)` under the three involutions is
the classical Markoff tree — `(3,3,6)`, `(3,6,15)`, `(6,15,39)`, … — which is the orbit of a fold
group, not a new route. The trace is exact as a coordinate; “the trace proves the Markoff conjecture”
is the false friend.

A concrete realization of that tree, with every commutator parabolic: hold
`A = [[−1, −5], [1, 4]]` and take `B = [[1, 1], [1, 2]]`, `[[0, −1], [1, 3]]`, `[[3, −4], [−2, 3]]`.
The traces are `(3, 3, 3)`, `(3, 3, 6)`, `(3, 6, 15)`, each on `x² + y² + z² − xyz = 0`, and each
commutator has trace `−2` — for the first two, `[[−7, −6], [6, 5]]`. The Fricke identity was checked
with exact rational arithmetic over 200 random `SL₂` pairs: residual `0`, not `10⁻¹⁶`. The tree is the
trace of a family of parabolic pairs, not a numerical coincidence.

**The node is a fold.** At `(0,0,0)` the gradient vanishes and the Hessian is `2I`, so the tangent
cone is the isotropic cone `x² + y² + z² = 0`. After `z ↦ iz` it is the `A1` cone `X Y = Z²`, and

```
(X, Y, Z) = (u², v², uv),    X Y − Z² = 0,    (u, v) ∼ (−u, −v)
```

exhibits the cone as `ℂ²/(ℤ/2)`, with the origin the unique fixed point. So the singular point of the
Markoff surface is the Fold in algebraic form: the same `ℤ/2`, now acting on the tangent plane. The
three trace coordinates vanish there at the quaternion point `A = iσ₁`, `B = iσ₂`, `AB = −iσ₃` (up to
sign), where `A² = B² = (AB)² = −I` and the commutator is `−I` with trace `−2`; the Fricke identity
reads `0 = 2 + (−2)`. The integer skeleton of this quotient is compiled in `Fold/Examples.lean`:
`nodeInv`, `nodeFold`, `a1`, `a1_cone`, `a1_fixed`. That the whole surface is locally biholomorphic
to the cone is the holomorphic Morse lemma, and that the link is `SO(3) ≅ ℝP³` is a standard
computation; both are cited, not proved here. The Fold supplies the exact local quotient; the
topology is the rhyme.

**The Cohn matrices.** The triple `(3, 3, 6)` is realized by

```
A = [[1, 1], [1, 2]],   B = [[2, 1], [1, 1]],
tr A = tr B = 3,   tr AB = 6,   det A = det B = 1,   tr(ABA⁻¹B⁻¹) = −2.
```

The Vieta move `(x, y, z) ↦ (x, xz − y, z)` is right multiplication: replacing `v` by `uv` sends the
triple `(tr u, tr v, tr uv)` to `(tr u, tr(uv), tr(u²v))`, and the trace identity
`tr(u) tr(uv) = tr(u²v) + tr(v)` gives `tr(u²v) = xz − y`. The other move `(u, v) ↦ (uv, v)` gives
`(z, y, zy − x)`. So the Markoff tree is the orbit of the pair `(A, B)` under right multiplication —
the same fold group, now inside `SL₂(ℤ)`. The Markoff numbers `1, 2, 5, 13, 29, …` are the entries
divided by `3`, and the values `√(9 − 4/m²)`, one for each Markoff number `m`, lie in the Lagrange
spectrum below `3`. That each Markoff number appears in exactly one triple up to symmetry is the
Markoff uniqueness conjecture, still open. The tree is exact; “the trace proves uniqueness” is the
false friend.

### What the second map changes

- It adds five exact statements, all about measure, quotient, or logic: amenability, order under a
  quotient, tolerance versus equivalence, the finite/infinite measure of the completed parameter, and
  contraposition.
- It adds no route to the open problems of the first map. The exact additions are about descriptions,
  not about arithmetic surfaces, operators, bounds, or parity.
- It sharpens the Fold's edge: the missing object is a **canonical measure** or a **canonical
  section**. The Fold can name both; it can supply neither.
- It records two boundary cases without adding rows: astigmatism is the shear sector the conformal
  scale does not carry, and `0/0` is the zero map's total kernel, not a value.
- It gives the honest form of the hard problem: not a problem the Fold can solve, but the one absence
  the map is built around.

The formal core of the five exact rows is in the Lean library; `the-fold-lean.md` lists which theorem
checks which row and which rows are left to the prose.

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

**The second map has the same shape: amenability needs a group, Simpson needs a non-order-preserving
quotient, the sorites needs an equivalence, the improper prior needs a finite measure, and
contraposition needs a logic that is not an epistemology — five exact statements about descriptions,
and one absence the Fold names but does not fill.**

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


## UF-001 — Universal invariant under allowed operations

**Question.** Given a specified family of Fold transformations, what information is unchanged by every allowed operation?

**General answer.** The complete common invariant is the orbit-equivalence class generated by operation edges. Every common invariant factors uniquely through this quotient. If the operation family contains a constant observable-collapse map, every observable-only invariant is constant.

**Finite spectral answer.** For a finite family of spectral power transitions, the quotient on the abstract spectral-signature state graph has a closed-form representative: the prime-to-L core of each multiplicative order, with the turning flag retained exactly when L is odd.

**Status.** The quotient statement is the standard universal-property theorem. The finite spectral result is a proved specialization of cyclic-group arithmetic. Neither is a new prime-generation method or a proof of RH. Full proofs and the executable reference experiment are in [the-fold-universal-invariant.md](the-fold-universal-invariant.md).


## UF-002 — Minimal arithmetic spectral power-operation families

**Question.** Given a desired terminal spectral profile, what is the smallest family of allowed arithmetic power maps on modular units that removes unwanted prime-primary components while preserving requested ones?

**Exact feasibility result.** For initial spectral orders (d_1,\ldots,d_t) and target orders (c_1,\ldots,c_t), each target must retain or remove each whole prime-primary component. Let

`K = union_j supp(c_j)` and `D = union_j (supp(d_j) \\ supp(c_j))`.

A single global operation family can realize the target if and only if (K\cap D=\varnothing) and the safe allowed exponents cover every prime in (D). A prime that must be retained in one coordinate and erased in another is a genuine global-operation obstruction.

**Optimization result.** A finite catalogue of arithmetic power exponents gives exactly weighted or unweighted Set Cover on the erased-prime universe (D); consequently the general catalogue problem is NP-hard (and the factored/support-encoded decision version is NP-complete). If arbitrary composite exponents are allowed, the problem becomes trivial: one reusable exponent type suffices; the product of the erased primes determines its smallest support-minimal representative, while the D-supported part of the joint lcm reaches the target in one application. If only prime exponents are allowed, one exponent type is needed per erased prime.

**Example.** Starting from orders (720=2^4 3^2 5) and (98=2\cdot7^2), retain targets (5) and (49). Then (K=\{5,7\}), (D=\{2,3\}); the allowed arithmetic power-exponent type (6) is safe and achieves both terminal targets under repeated global application, whereas prime-only exponent types require (2) and (3). The one-generator minimum (6) takes four rounds; the one-step exponent (144) removes the complete primary components immediately.

The exact theorem, reduction, turning-bit analysis, bounded verification, and standard-library reference solver are in [the-fold-minimal-operations.md](the-fold-minimal-operations.md) and [tools/fold_minimal_operations.py](tools/fold_minimal_operations.py).


## UF-003 — Geometric Fold generator catalogue

**Question.** What is the natural primitive operation catalogue when it is derived from the Fold geometry itself?

**Repository-grounded answer.** The primitive geometric operation is a crease reflection \(\sigma_H\), an involution. A twist or rotation is the composition of two reflections, not an independent primitive when the creation order is respected. The sheet fold \(F(x,y)=(x,|y|)\) is idempotent and is not the reflection used to generate twists. The zero scale is an absorbing collapse, not an invertible group generator.

**Finite geometric theorem.** For a closure order \(m\), index the available reflection axes by \(A\subseteq\mathbb Z/m\mathbb Z\). A nonempty selected set \(J\subseteq A\), anchored at \(a_0\), generates a dihedral subgroup whose rotation order is
\[
q_J=\frac{m}{\gcd(m,\{j-a_0:j\in J\})}.
\]
Thus the target subgroup \(D_q\), \(q\mid m\), is generated exactly when that gcd is \(m/q\).

**Optimization.** For a fixed anchor and target \(q\), every other chosen axis must be congruent to the anchor modulo \(m/q\). Its normalized difference covers the prime divisor \(\ell\mid q\) exactly when it is nonzero modulo \(\ell\). The minimum crease set is therefore a finite Set Cover problem over the prime divisors of \(q\), minimized over anchors.

**Example.** For \(m=30\) and available axes \(A=\{0,6,10,15\}\), no pair generates the full \(D_{30}\), but \(\{6,10,15\}\) does. It generates a group of order \(60\).

**Important distinction.** The arithmetic UFSF transition \(a\mapsto a^r\) acts on a modular unit/Frobenius element. A geometric rotation \(z\mapsto\zeta_m^\delta z\) shifts root indices additively; Frobenius acts by multiplying them. They share an order-of-a-power formula but are not the same transformation.

Full proofs, the minimum-axis set-cover reduction, and the standard-library solver are in [the-fold-geometric-generators.md](the-fold-geometric-generators.md) and [tools/fold_geometric_generators.py](tools/fold_geometric_generators.py).


## UF-004 — Hexagonal lattice crease catalogue and two sign characters

**Question.** Derive the allowed crease axes from the hexagonal lattice and the repository's actual crease-height function, rather than choosing an abstract dihedral axis catalogue.

**Height-derived crease set.** For \(h(z)=\operatorname{Re}(z^6)\), the zero-lines are
\[
\theta_j=\frac{\pi}{12}+j\frac{\pi}{6},\qquad j=0,\ldots,5,
\]
i.e. 15°, 45°, 75°, 105°, 135°, and 165°. Reflection across each line is an involution and sends \(h\) to \(-h\). Two crease reflections compose to a 60° rotation, and all six generate the unlabelled honeycomb point group \(D_6\) of order 12.

**Sublattice split.** With alternating A/B labels on the six vertices of a hexagon, even crease indices preserve the sublattice label and odd indices exchange it. Thus the six physical creases split into \(A_{\mathrm{pres}}=\{0,2,4\}\) and \(A_{\mathrm{swap}}=\{1,3,5\}\).

**Two independent characters.** For \(r\) the 60° rotation and \(s\) the 15° base reflection, write \(g=r^k s^\epsilon\). The determinant character is \(\chi_{\mathrm{det}}(g)=(-1)^\epsilon\); the sublattice character is \(\chi_{AB}(g)=(-1)^k\). Their product is a third character. The A/B-preserving subgroup is \(\ker\chi_{AB}=\langle r^2,s\rangle\cong D_3\); the odd-axis subgroup is the other D3 kernel \(\ker(\chi_{\mathrm{det}}\chi_{AB})=\langle r^2,rs\rangle\).

**Minimum crease sets.** All six axes generate D6 with two adjacent crease generators. The three even axes generate the A/B-preserving D3 with two generators; the three odd axes generate the alternate D3 with two generators.

**Boundary.** The 30° rotation permutes the zero-line arrangement and negates \(h\), but it has order 12 and is not a honeycomb lattice point symmetry. The lattice's rotational symmetry is 60°, consistent with the planar crystallographic restriction. The honeycomb is a triangular Bravais lattice with a two-site basis; making the two basis sites inequivalent reduces the point symmetry to D3.

Full proofs, exact character kernels, examples, and the standard-library verification program are in [the-fold-hexagonal-lattice.md](the-fold-hexagonal-lattice.md) and tools/fold_hexagonal_lattice.py.


## UF-005 — Periodic crease networks and surviving sign characters

**Question.** Can the symmetry group of a periodic Fold network be derived from the translation lattice, crease graph, signed height, and site decorations, with the surviving invariants identified exactly?

**Geometric group.** A periodic crease graph on a flat torus lifts to a periodic graph in the plane. Its full isometry group \(W_C\) has a rank-two translation subgroup \(T_C\) and a finite quotient \(P_C=W_C/T_C\), giving the wallpaper-group exact sequence
\[
1\longrightarrow T_C\longrightarrow W_C\longrightarrow P_C\longrightarrow1.
\]
The extension need not split; glide reflections are affine lifts that prevent assuming a universal semidirect-product decomposition. There are 17 wallpaper-group types.

**Height character.** For a nonzero signed periodic height, restrict to symmetries satisfying \(h(gx)=\chi_h(g)h(x)\) with \(\chi_h(g)\in\{\pm1\}\). These symmetries form a subgroup and \(\chi_h\) is a homomorphism. The exact height-preserving subgroup is \(\ker\chi_h\). Network symmetries that preserve the zero set but not the defining height up to sign need not belong to this subgroup.

**Multiple decorations.** A binary site decoration \(c:S\to\{\pm1\}\), such as A/B, gives a second character when each allowed symmetry globally preserves or globally exchanges the two labels. With \(k\) binary decorations, the character map is \(\chi:G\to(\mathbb Z/2)^k\). The common sign-preserving subgroup is \(\ker\chi\). If the image has rank \(r\), its index is exactly \(2^r\); dependent signs do not add a new independent reduction.

**Finite model and tests.** The reference implementation enumerates affine maps \(x\mapsto Ax+b\) on a finite torus, where \(A^TGA=G\), and checks preservation of vertices, crease-crossing bonds, height signs, and colour signs. It verifies point-group orders 8 (square), 12 (triangular), and 2 (generic oblique). In the 4-by-4 square example, the joint sign map has all four values in \(\mathbb Z_2^2\): 64 joint sign-covariant symmetries and a common sign-preserving kernel of order 16. The triangular Bravais-net example has 192 affine symmetries on the same finite torus.

**Scope correction for UF-004.** \(h(z)=\operatorname{Re}(z^6)\) is a homogeneous local six-line crease star; it is not itself a periodic honeycomb height function. The global honeycomb requires a triangular translation lattice and a two-site basis as separate data. The UF-004 local \(D_6\) and A/B parity calculations are retained, but the periodic extension is handled here.

Full definitions, the two proved character theorems, wallpaper-group boundary, limits, and executable solver are in the-fold-periodic-networks.md and tools/fold_periodic_networks.py.


## UF-006 — Sign characters of frieze and wallpaper groups

**Question.** Which global sign characters can a periodic Fold height carry under the seven frieze groups and the seventeen wallpaper groups, and how do glide reflections affect the answer?

**Translation-kernel theorem.** For a frieze or wallpaper group \(W\), let \(T\triangleleft W\) be its full translation subgroup and \(P=W/T\) its finite point group. Every periodic height-sign character is trivial on \(T\), and there is a canonical isomorphism
\[
\{\chi\in\operatorname{Hom}(W,C_2):\chi|_T=1\}\cong\operatorname{Hom}(P,C_2).
\]
The proof is direct: characters trivial on \(T\) descend uniquely to the quotient. No splitting of the crystallographic extension is needed.

**Glide corollary.** If \(g\) is a glide reflection with \(g^2=t\in T\), then \(\chi(g)^2=\chi(t)=+1\). Both \(\chi(g)=+1\) and \(-1\) are possible. A glide may reverse height once while its square, a pure translation, preserves it.

**Seven frieze groups.** Explicit presentations yield the following counts of all abstract characters and of those trivial on translations, respectively:
\[
F_1:(8,4),\ F_2:(4,4),\ F_3:(4,2),\ F_4:(4,2),\
F_5:(4,2),\ F_6:(2,2),\ F_7:(2,1).
\]
There are 28 abstract character maps and 17 translation-trivial maps across the seven types. The abstract types are \(\mathbb Z\), \(\mathbb Z\times C_2\), \(D_\infty\), and \(D_\infty\times C_2\).

**All 17 wallpaper groups.** The periodic character count is \(|\operatorname{Hom}(P,C_2)|\), determined by the finite point group:
- \(C_n\): one character when \(n\) is odd; two when \(n\) is even.
- \(D_n\) (order \(2n\)): two characters when \(n\) is odd; four when \(n\) is even.

The resulting counts are: p1=1; p2, pm, pg, cm=2 each; pmm, pmg, pgg, cmm=4 each; p4=2; p4m and p4g=4 each; p3=1; p3m1 and p31m=2 each; p6=2; p6m=4. Their total is 46. Only p1 and p3 have only the trivial periodic sign character.

**Scope.** These are algebraically possible characters, not guaranteed realizations by a particular fixed crease motif. A given height must still satisfy the pointwise sign-covariance equation; its zero set, stabilizers, and decorations can exclude some algebraic candidates.

Full presentations, proofs, tables, references, and the standard-library enumerator are in the-fold-frieze-wallpaper-characters.md and tools/fold_frieze_wallpaper_characters.py.


## UF-007 — Forced zeros, crease topology, and minimal D6 semi-invariants

**Question.** Given a group character and a prescribed crease network, what zeros are forced by symmetry, when can a continuous signed height realize that network, and what are the simplest D6 realizations?

**Fixed-point theorem.** If \(h(gx)=\chi(g)h(x)\) and \(\chi(g)=-1\), then every fixed point of \(g\) is a zero of \(h\):
\[
\operatorname{Fix}(g)\subseteq h^{-1}(0).
\]
The union of fixed sets of all sign-reversing elements is therefore a forced-zero locus.

**D6 sharp examples.** With \(r(z)=e^{i\pi/3}z\) and \(s(z)=e^{i\pi/6}\bar z\), the three nontrivial real characters have harmonic polynomial representatives:
\[
f_{\det}=\operatorname{Re}(z^6),\quad
f_{\mathrm{sub}}=\operatorname{Re}(e^{-i\pi/4}z^3),\quad
f_{\mathrm{mix}}=\operatorname{Re}(e^{i\pi/4}z^3).
\]
They have exactly six, three, and three forced reflection axes as zero sets. Any polynomial in the corresponding character space must be divisible by the distinct linear forms defining the anti-reflection axes; hence the minimum total degrees 6, 3, and 3 are sharp.

**Dual-graph theorem.** Let C be a closed embedded crease graph on a connected surface, and let D(C) be its face-adjacency dual, retaining loops when both sides of an edge border the same face. A face-sign assignment that reverses across each crease exists iff D(C) is bipartite. For a connected bipartite dual it is unique up to global sign reversal. A signed-distance construction then gives a continuous height with exact zero set C.

**Network-induced character.** If a symmetry group preserves C and D(C) is connected and bipartite, each symmetry either preserves or exchanges the two dual colour classes. This gives a unique character \(\chi_C:G\to\{\pm1\}\); any continuous scalar height with zero set C and sign reversal across every crease has this character. Thus a fixed crease network may realize only one of the characters that are abstractly allowed by the group.

**Obstructions.** A three-ray Y-junction has dual C3 and cannot be the exact sign-changing zero set of a continuous scalar height. A nonseparating crease loop on a torus gives a dual self-loop and is likewise obstructed. These scalar obstructions do not exclude vector-valued order parameters or sections of nontrivial line bundles.

Full proofs, D6 formulas, polynomial sharpness, topological construction, examples, references, and tests are in the-fold-forced-zero-topology.md and tools/fold_forced_zero_topology.py.


## UF-008 — Smooth and analytic realizability of Fold heights

**Question.** When does a periodic crease network admit a smooth or real-analytic signed height, and what does its local vertex geometry force about vanishing order?

**Smooth realization theorem.** Assume a finite crease graph on a smooth surface has only regular smooth branches through its vertices (no terminal half-edges, cusps, or isolated singular components). Then a global \(C^\infty\) scalar height with exact zero set equal to the network and opposite signs across each crease exists if and only if its face-adjacency dual is bipartite. Necessity is the face-sign colouring argument; sufficiency follows by taking local products of branch-defining functions with signs matched to the dual colouring and gluing them by a nonnegative smooth partition of unity.

**Local branch-count theorem.** If q distinct regular branches meet at p and a smooth height vanishes on all of them, repeated Hadamard division gives \(h=(\prod_{i=1}^q\phi_i)u\). Hence \(\operatorname{ord}_p(h)\ge q\), with equality attained by the product. A transverse four-valent crossing has minimum order 2; a six-valent three-branch junction has minimum order 3. The branch count is half the valence under the regular-branch hypothesis.

**Analytic Fourier-projection theorem.** For a finite wallpaper point group P acting affinely on a rank-two torus, every real character \(\chi:P\to\{\pm1\}\) has a nonzero real-analytic periodic semi-invariant. Choose a lattice frequency with trivial dual stabilizer and project its Fourier mode over P with character weights. The resulting Fourier orbit sum transforms by \(\chi\). At least one of its real and imaginary parts is nonzero and has the same character.

**Explicit periodic models.** The square-torus function \(\sin(2\pi x)\sin(2\pi y)\) has two crossing crease families and order-2 vertices. The triangular-torus function \(\sin(2\pi x)\sin(2\pi y)\sin(2\pi(x+y))\) has three crease directions, four triple-intersection vertices of order 3, and realizes the D6 character \(\chi(r)=-1,\chi(s)=+1\) for \(r(x,y)=(-y,x+y)\), \(s(x,y)=(-x-y,y)\).

**Important boundary.** Fourier projection guarantees an analytic periodic representative for each algebraically allowed character, but it does not guarantee that the zero set equals an arbitrarily prescribed crease network. Exact global analytic zero-divisor realization remains open in this project. Smooth sufficiency also depends on the regular-branch hypotheses; arbitrary singular graphs need separate treatment.

Proofs, local models, Fourier construction, references, and bounded tests are in the-fold-smooth-analytic-heights.md and tools/fold_smooth_analytic_heights.py.


## UF-009 — Exact analytic zero-set realization of periodic crease networks

**Question.** When is a periodic crease network the exact zero set of one global real-analytic scalar height, rather than merely contained in the zero set of a symmetry-compatible function?

**Analytic-principality theorem.** Let X be a compact nonsingular pure two-dimensional global real-analytic set and C a compact locally principal real-analytic divisor. If the face-adjacency dual D(C) is bipartite, its face colouring shows that X\C is disconnected and that the mod-2 divisor class [C] vanishes in H_1(X;Z_2). By the global-principality theorem of Acquistapace–Díaz-Cano, C is the exact zero divisor of a global real-analytic function. Their generic-equation result allows multiplicity one along each irreducible crease component, so the function changes sign across every regular crease arc.

**Converse.** Any scalar function with exact zero set C and sign reversal across every crease induces a two-colouring of adjacent faces. Thus the dual must be bipartite. Under the stated locally principal analytic hypotheses, bipartiteness is therefore necessary and sufficient.

**Equivariant exact realization.** If a finite analytic symmetry group preserves C and D(C) is connected and bipartite, the unique face bipartition induces a character chi_C. From an exact analytic height h_0 construct
\[
H(x)=\sum_{g\in G}\chi_C(g)h_0(gx).
\]
Every summand has the same sign on each face, so the sum has no extra zeros and still vanishes exactly on C. Reindexing the sum proves H(ax)=chi_C(a)H(x). This produces an exact analytic height with the network-induced character.

**Explicit torus products.** For primitive integer covectors n_j and an even number of distinct levels c_{j,l} modulo one in each direction family, the function
\[
h(x,y)=\prod_j\prod_{l=1}^{2r_j}
\sin(\pi(n_j\cdot(x,y)-c_{j,l}))
\]
is globally periodic, real analytic, and has exactly the prescribed paired affine circles as its zero set. At a transverse intersection of q distinct families its vanishing order is q. The UF-008 square and triangular examples are special cases.

**Scope.** The theorem applies to compact nonsingular global real-analytic surfaces and compact locally principal real-analytic crease divisors. It does not yet classify non-locally-principal singularities, noncompact covers, prescribed higher odd multiplicities, or networks with disconnected duals and nontrivial component permutations.

Full proof, cited analytic-principality input, exact products, equivariant averaging, and tests are in the-fold-exact-analytic-networks.md and tools/fold_exact_analytic_networks.py.


## UF-010 — Divisor parity, disconnected creases, singularities, and multiplicity

**Question.** How do disconnected crease components, singular analytic branches, and prescribed zero multiplicities affect exact global analytic height realization?

**Weighted-divisor criterion.** Let \(X\) be a pure-dimensional irreducible global real-analytic set and let \(D=\sum_i m_i C_i\) be a locally finite effective divisor, with each component ideal sheaf locally principal. Define the odd support \(C_{\mathrm{odd}}=\bigcup_{m_i\text{ odd}}C_i\). Acquistapace–Díaz-Cano, Corollary 3.7, gives:
\[
\prod_i\mathfrak p_i^{m_i}\text{ is principal}
\iff
\sum_i m_i[C_i]=0\text{ in }H^\infty_{q-1}(X;\mathbb Z_2)
\quad\text{and}\quad
X\setminus C_{\mathrm{odd}}\text{ is disconnected}.
\]
The componentwise local-principality hypotheses are required.

**Parity decomposition.** Write \(D=D_{\mathrm{odd}}+2E\), where \(D_{\mathrm{odd}}\) is the reduced odd support and \(E=\sum_i\lfloor m_i/2\rfloor C_i\). The source paper proves every positive even divisor \(2E\) has a positive analytic equation. Thus the global topological obstructions are entirely controlled by the odd support; prescribed higher odd multiplicities are obtained by multiplying its reduced generator by a positive equation for the residual even divisor.

**Disconnected support examples.** On the torus, one essential odd loop fails; two parallel essential odd loops succeed even though each separately is nonseparating; three parallel odd loops fail the mod-2 class condition despite having disconnected complement; four succeed. The face-dual cycles are \(C_1,C_2,C_3,C_4\), respectively.

**Mixed multiplicities.** Two parallel odd loops plus an additional even loop have an exact periodic height proportional to
\[
\sin(2\pi x)\bigl(1-\cos(2\pi(x-\tfrac14))\bigr).
\]
The even loop is a zero of multiplicity two but is not a sign-changing wall. Accordingly, use the dual/homology test on the odd support, not on the entire weighted support.

**Singular local orders.** If a locally principal local equation is \(h=u\prod_i f_i^{m_i}\), then its analytic order at a point is \(\sum_i m_i\,\operatorname{ord}_p(f_i)\). A node \(xy=0\) has order two; the cusp \(y^2-x^3=0\) has order two despite having one irreducible real branch; weighting the cusp divisor by three gives order six. Local principality on a singular ambient space is a separate obstruction and cannot be inferred from mod-2 topology alone.

**Disconnected-component symmetries.** A symmetry preserving a weighted divisor must preserve multiplicities on component orbits. A half-period translation can swap two disconnected parallel odd crease circles and reverse the height. For a connected odd-support face dual, the network-induced sign is a character; multiple independent dual components may instead require a signed permutation representation.

**Periodic covers.** A global analytic generator on the universal cover need not be periodic. For a periodic scalar Fold, descend the divisor to the compact torus and test principality there; a torus generator lifts to a periodic height.

Full statements, torus products, singular examples, and the bounded verifier are in the-fold-divisor-parity-classification.md and tools/fold_divisor_parity_classification.py.


## UF-011 — Local principality, normalization, and singularity resolution

**Question.** When does a singular crease component define a locally principal divisor, and what exactly can normalization or resolution repair?

**Local generator-count test.** For a local analytic ring \((A,\mathfrak m,k)\) and a finitely generated divisor ideal \(I\),
\[
\mu_A(I)=\dim_k(I/\mathfrak m I).
\]
By Nakayama's lemma, \(\mu=1\) is equivalent to local principality; \(\mu\ge2\) proves failure. In a smooth ambient surface, regular local rings are factorial, so codimension-one divisors are locally principal. Singular support alone is not an obstruction.

**Normal but non-Cartier counterexample.** The source-paper surface \(X:z^2=x^4+y^4\) is a two-dimensional hypersurface with isolated singularity at the origin. Its complexification is a domain, satisfies S2 because it is a hypersurface, and satisfies R1 because the singular locus has codimension two; Serre's criterion makes it normal. The divisor \(Y:x=0,z=y^2\) has local ideal \(I=(x,z-y^2)\). The independent linear classes x and z in \(\mathfrak m/\mathfrak m^2\) show \(\dim I/\mathfrak m I=2\). Thus the normalization is the identity and cannot repair the non-Cartier divisor.

**Cusp normalization.** The cusp as a curve in the smooth plane is principal, defined by \(y^2-x^3\). Intrinsically, its point ideal in \(A=\mathbb R\{t^2,t^3\}\) is \((t^2,t^3)\), which needs two generators. The normalization \(B=\mathbb R\{t\}\) extends it to \((t^2)\), principal of order two. Normalization repairs the nonnormal curve ideal but changes the divisor multiplicity.

**Node distinction.** The plane node \(xy=0\) is a principal curve divisor in the plane. Its intrinsic node ideal \((x,y)\) needs two generators in \(\mathbb R\{x,y\}/(xy)\). Normalization separates the two branches and makes the extended point ideal principal componentwise, with order one on each branch.

**Weighted blow-up calculation.** In the chart \(x=uv,\ y=u,\ z=u^2w\), the strict transform of the cone is \(w^2=1+v^4\). The strict transform of Y is \(v=0,w=1\). Since \((w-1)(w+1)=v^4\) and \(w+1\) is a unit near w=1, its ideal \((v,w-1)\) equals \((v)\). This repairs the local strict-transform ideal in this chart; it is not a claim that the single chart is a complete global resolution.

**Resolution boundary.** On a smooth resolution surface, strict transforms of codimension-one divisors are Cartier. But strict transform, total transform, and push-forward are different; exceptional components and their multiplicities carry the original obstruction. A principal divisor upstairs does not imply the original Weil divisor was Cartier downstairs.

**Local-to-global pipeline.** Compute the local ring and ideal, test \(\mu(I)\), examine normality and the local divisor class group, track branch valuations under normalization or exceptional valuations under resolution, then reapply UF-010's odd-support mod-2 and complement-disconnection criterion.

Full proofs, calculations, examples, and the standard-library verifier are in the-fold-local-principality-resolution.md and tools/fold_local_principality_resolution.py.


## UF-012 — Exceptional intersection lattices and local divisor classes

**Question.** How does a non-Cartier crease divisor appear on a resolution, and when can exceptional intersection data decide whether it descends as a principal analytic height?

**Exceptional-correction theorem.** Let M be the negative-definite intersection matrix of the exceptional curves E_i on a resolution, and let b(D)_j=(D~.E_j). If D is Cartier/principal downstairs, then its principal equation upstairs has divisor D~+Σa_iE_i with integral exceptional valuations a_i, so
\[
Ma=-b(D),\qquad a\in\mathbb Z^r.
\]
Therefore [b(D)] must vanish in coker(M). A nonintegral solution is a definitive non-Cartier obstruction. For rational surface singularities under the standard henselian/complete hypotheses, the local class group is the exceptional-lattice discriminant group, making this criterion complete. For non-rational singularities, it is only the finite numerical quotient and degree-zero Picard data can remain.

**Lipman sequence.** The resolution class group separates a numerically trivial Picard term from a finite quotient controlled by the exceptional intersection matrix, with a final obstruction group G. Lipman's unibranch condition (in particular, for henselian local rings) makes G vanish. Rational singularities also eliminate the degree-zero part, recovering the finite discriminant-group description. For general exceptional components, the degrees d_i enter the intersection map; when the exceptional curves are rational, d_i=1 and the finite group is coker(M).

**ADE calibration.** For the A_n rational double point \(xy=z^{n+1}\), the exceptional graph is a chain of n rational (-2)-curves. Its matrix has determinant \((-1)^n(n+1)\) and cokernel \(\mathbb Z/(n+1)\). The prime divisor \((x,z)\) meets one end exceptional curve once and generates this cyclic group; \((n+1)\) times that divisor is principal.

**UF-011 cone reanalysis.** The normal cone \(z^2=x^4+y^4\) is the simple-elliptic singularity \(\widetilde E_7=\widetilde T_{2,4,4}\). Its minimal resolution has one elliptic exceptional curve E with \(E^2=-2\). In the weighted chart \(x=uv,y=u,z=u^2w\), the crease strict transform \(v=0,w=1\) meets E:u=0 transversely once, so b(Y)=1. The numerical lattice quotient is \(\mathbb Z/2\), and the correction equation \(-2a=-1\) gives \(a=1/2\). Thus the local non-Cartier obstruction is visible in the exceptional lattice, independently of the two-generator ideal proof.

**Important limitation.** Since E is elliptic, its degree-zero Picard group is nontrivial. The \(\mathbb Z/2\) lattice quotient is not automatically the full local divisor class group. The nonzero residue already proves this crease is non-Cartier; no claim about the complete class-group structure is needed.

**Local-to-global pipeline.** Compute b(D), solve Ma=-b(D) over Q, and reject if the correction is not integral. If it is integral, use the rationality/Picard hypotheses to decide whether the lattice test is sufficient; otherwise compute the remaining Picard/class obstruction. Once locally Cartier everywhere, reapply UF-010's odd-support homology and complement-disconnection criterion.

Full proofs, ADE calculations, simple-elliptic interpretation, references, and exact-arithmetic tests are in the-fold-exceptional-lattices-class-groups.md and tools/fold_exceptional_lattice_obstruction.py.


## UF-013 — Equivariant resolution, exceptional curves, and Fold characters

**Question.** When a finite symmetry group acts on a singular Fold surface, how does it lift to the resolution, what representation does it induce on the exceptional lattice, and which exact analytic height characters can descend?

**Equivariant exceptional-lattice action.** A finite group acting on a normal surface germ lifts to its unique minimal resolution (or to a suitable equivariant good resolution). If \(E_i\) are exceptional components, the induced permutation matrices \(P_g\) preserve the intersection matrix:
\[
P_g^T M P_g=M.
\]
Hence the action descends to the numerical discriminant group. It need not determine the action on the exceptional curves as Riemann surfaces, their marked points, or their degree-zero Picard varieties.

**Concrete D4 action on the UF-011 cone.** On \(X:z^2=x^4+y^4\), define \(r(x,y,z)=(-y,x,z)\) and \(s(x,y,z)=(y,x,z)\). These generate the order-eight dihedral group \(D_4\). The simple-elliptic \(\widetilde E_7\) exceptional curve is \(E:w^2=t^4+1\), with \(t=x/y,w=z/y^2\). The lifted maps are \(r_E(t,w)=(-1/t,w/t^2)\), \(s_E(t,w)=(1/t,w/t^2)\). They act nontrivially on E (their image is \(V_4\)), but the unique exceptional component is fixed, so the rank-one lattice \(M=[-2]\) has trivial D4 action.

**Exact character height.** \(h=xy\) has exact zero divisor consisting of four branches \(x=0,z=\pm y^2\) and \(y=0,z=\pm x^2\). It transforms by \(\chi(r)=-1,\chi(s)=+1\). The four strict-transform branches meet E transversely, so \(b(D)=4\); the exceptional correction equation \(-2a=-4\) gives the integral value \(a=2\). This example proves that the exceptional lattice representation can be trivial while the exact analytic generator has a nontrivial character.

**Elliptic-curve differential.** For \(\omega=dt/w\), \(r_E^*\omega=+\omega\) and \(s_E^*\omega=-\omega\). The curve automorphism/Picard data therefore contain information absent from the lattice \(L=\mathbb Z[E]\). This agrees with the known description of simple-elliptic automorphisms in terms of torsion translations and automorphisms of the exceptional elliptic curve.

**Unit-cocycle criterion.** If an invariant principal divisor has a generator \(h_0\), write \(g^*h_0=u_g h_0\) with \(u_g\) a unit. A new generator \(h=v h_0\) has character \(\chi\) exactly when
\[
(g^*v/v)u_g=\chi(g)
\]
for all \(g\in G\). Thus divisor invariance and numerical Cartierness do not by themselves guarantee a prescribed equivariant generator; the unit cocycle must be adjusted by a unit. For real separating divisors with a connected bipartite face dual, UF-009's sign-colouring average is a useful sufficient construction.

**Four D4 real characters.** For the chosen generators \((r,s)\), polynomial semi-invariants are \(z\) for \((+,+)\), \(xy\) for \((-,+)\), \(x^2-y^2\) for \((-,-)\), and \(xy(x^2-y^2)\) for \((+,-)\). The \(z\) representative has only the vertex as its real zero set on X; the other three produce real curve networks.

Full proofs, induced elliptic-curve maps, marked points, the cocycle condition, and exact finite checks are in [the-fold-equivariant-resolution-symmetry.md](the-fold-equivariant-resolution-symmetry.md) and tools/fold_equivariant_resolution.py.


## UF-014 — Complete analytic D4 character classification on the cone

**Question.** Classify every convergent analytic scalar height germ on \(X:z^2=x^4+y^4\) that transforms by a one-dimensional character of the natural D4 symmetry, and determine the exact forced crease supports and allowed multiplicities.

**Invariant analytic ring.** With \(p=x^2+y^2\), \(q=x^2y^2\), the signed-permutation reflection group has \(\mathbb K\{x,y\}^{D_4}=\mathbb K\{p,q\}\). On X, \(z^2=p^2-2q\), so
\[
\mathcal O_{X,0}^{D_4}\cong\mathbb K\{p,z\}.
\]

**Complete semi-invariant theorem.** The D4 generators are \(r(x,y,z)=(-y,x,z)\) and \(s(x,y,z)=(y,x,z)\). For the four characters \((\chi(r),\chi(s))=(+,+),(-,+),(-,-),(+,-)\), define
\[
\Delta_\chi=1,\quad xy,\quad x^2-y^2,\quad xy(x^2-y^2),
\]
respectively. Every convergent analytic germ satisfying \(g^*h=\chi(g)h\) has a unique representation
\[
h=\Delta_\chi F(p,z),\qquad F\in\mathbb K\{p,z\}.
\]
The proof uses unique Weierstrass division \(h=a(x,y)+zb(x,y)\), divisibility by the reflection hyperplanes on which \(\chi=-1\), and the invariant-ring description. Thus each scalar character space is free rank one over the invariant analytic ring. This is a classification of one-dimensional scalar semi-invariants; the two-dimensional irreducible representation is a separate covariant problem.

**Exact forced multiplicities.** The quotient coordinates \((p,z)\) have four relevant branch curves \(z-p=0,\ z+p=0,\ z-p/\sqrt2=0,\ z+p/\sqrt2=0\). Their pullbacks are the positive/negative coordinate and diagonal branch orbits, each with ramification multiplicity two. Consequently a semi-invariant with no extra divisor components has multiplicities \(1+2k_i\) independently on each forced D4-orbit. The \((- ,+)\) character uses the two coordinate orbits; \((-,-)\) uses the two diagonal orbits; \((+,-)\) uses all four. The trivial character forces no reflection crease.

**Degree statement.** With weights \(\deg x=\deg y=1,\deg z=2\), the minimal semi-invariant degrees are 0,2,2,4. The trivial relative-invariant generator is 1; z is one example of a trivial-character function, not the generator of that module.

Complete proofs, quotient branch equations, multiplicity classification, and finite checks are in the-fold-d4-analytic-character-classification.md and tools/fold_d4_analytic_character_classification.py.


## UF-015 — Complete analytic D4 representation decomposition

**Question.** Complete UF-014 by classifying the two-dimensional irreducible covariants and decomposing the entire convergent analytic coordinate ring of X:z²=x⁴+y⁴ over its invariant analytic ring A=K{p,z}.

**Theorem.** The coordinate ring is free of rank eight over A, with basis
\[
1,\ xy,\ x^2-y^2,\ xy(x^2-y^2),\ x,\ y,\ xy^2,\ x^2y.
\]
The first four basis elements generate the four rank-one character modules from UF-014. The remaining four form two copies of the two-dimensional irreducible representation E, generated as vector-valued covariants by
\[
V_1=(x,y),\qquad V_3=(xy^2,x^2y).
\]
Both transform by the same matrices rho(r) and rho(s) given in the UF-015 paper. Every analytic E-covariant is uniquely A_1(p,z)V_1+A_3(p,z)V_3.

**Proof strategy.** The signed-permutation reflection-group theorem gives a free rank-eight analytic module over K{p,q}. Its coinvariant basis is verified by reducing modulo (p,q), where y²=-x² and x⁴=0. The cone relation identifies q=(p²-z²)/2, and analytic base change gives the displayed A-basis. This proves completeness and uniqueness, not merely generation by examples.

**Representation decomposition.**
\[
\mathcal O_{X,0}\cong A\otimes(\mathbf1\oplus\chi_{-+}\oplus\chi_{--}\oplus\chi_{+-}\oplus E\oplus E).
\]
This is a module/representation decomposition, not a product decomposition of rings; multiplication still couples the summands.

The Hilbert numerator is 1+2t+2t²+2t³+t⁴, agreeing with the weighted hypersurface Hilbert series. The E-isotypic part has A-basis degrees 1,1,3,3, so E occurs with multiplicity two.

Proof, degree check, scope, and finite verifier are in the UF-015 paper and tools/fold_d4_analytic_representation_decomposition.py.


## UF-016 — Complete multiplication algebra of the Fold

**Question.** Determine all products in the rank-eight analytic coordinate algebra over A=K{p,z}.

Put p=x²+y² and q=x²y²=(p²−z²)/2. Then
\[
R\cong A\{x,y\}/(x^2+y^2-p,\ x^2y^2-q).
\]
In the ordered A-basis (1,x,y,xy,x²,x²y,x³,x³y), multiplication by x and y is represented by the two explicit 8×8 matrices in the UF-016 paper.

**Theorem UF-016.1.** These commuting operators satisfy
\[
M_xM_y=M_yM_x,\quad M_x^2+M_y^2=pI_8,\quad M_x^2M_y^2=qI_8.
\]
Every product is obtained by applying a word in the two operators to the unit vector, so these matrices determine the entire multiplication algebra and all structure constants. The representation is faithful.

**Spectral consequence.** The generic characteristic polynomial of either multiplication operator is
\[
(T^4-pT^2+q)^2.
\]
The joint eigenvalue pairs satisfy X²+Y²=p and X²Y²=q and reconstruct the generic D4 orbit fiber. At the singular fiber, scheme-theoretic nilpotents and non-semisimple operator structure must be retained; eigenvalues alone do not encode the nonreduced fiber.

The exact matrices, reduction rules, proof, character tensor-product rules, spectral caveats, and subsequent discriminant questions are in the UF-016 paper. The standard-library exact verifier is tools/fold_multiplication_algebra.py.


## UF-017 — Fold trace discriminant and spectral geometry

**Theorem.** For the rank-eight basis (1,x,y,xy,x²,x²y,x³,x³y), the trace-pairing Gram determinant is
\[
\det(\operatorname{Tr}(b_i b_j))=2^{16}q^4(p^2-4q)^4,\quad q=(p^2-z^2)/2.
\]
The quotient Jacobian for p=x²+y² and q=x²y² is J=4xy(x²−y²), and its square is 16q(p²−4q). Thus the pullback of the trace determinant is exactly J⁸. The reduced branch components are the images of x=0, y=0, x−y=0, x+y=0.

The trace form is nondegenerate off the discriminant and degenerates on it. It does not by itself determine the full nonreduced local algebra or Jordan structure; those remain follow-up questions. Exact matrix construction and symbolic determinant verification are in the UF-017 paper and verifier.


## UF-018 — Local algebras and Jordan strata

**Theorem UF-018.1.** The length-eight fibers stratify as follows:
- q=0, p≠0: four geometric points, each of local length two; trace rank four; Mx and My have Jordan block sizes [2,2,1,1,1,1].
- p²−4q=0, p≠0: four geometric points, each of local length two; trace rank four; both coordinate operators have Jordan sizes [2,2,2,2].
- p=q=0: one geometric point of local length eight; trace rank one; both coordinate operators have Jordan sizes [4,4].

The two generic branches have equal point counts, local lengths, and trace rank, but their operator Jordan patterns distinguish them in the chosen coordinates. The vertex has a single highly nonreduced fiber. A single operator's Jordan form is not a complete invariant; the faithful simultaneous pair and unit are required.

Proof, local presentations, exact specialized matrices, and a SymPy verifier are in the UF-018 paper and script.


## UF-019 — Vertex Hilbert function and socle

**Theorem UF-019.1.** For R0=k[x,y]/(x²+y²,x²y²), with maximal ideal m=(x,y), the m-adic Hilbert function is
\[
H(t)=1+2t+2t^2+2t^3+t^4.
\]
Thus the successive dimensions are (1,2,2,2,1), embedding dimension is two, m⁵=0 but m⁴≠0, and the socle is one-dimensional, generated by x³y. The length is eight. The local algebra is an Artin Gorenstein complete intersection.

The Hilbert function alone is not asserted to classify the algebra. The proof and exact multiplication-based verifier are in the UF-019 paper and script.


## UF-020 — Simultaneous multiplication, Frobenius duality, and arithmetic reduction

**Theorem UF-020.1.** A commuting pair of endomorphisms (X,Y) on an eight-dimensional vector space, together with a cyclic distinguished vector e, determines its generated unital algebra. Intertwiners preserving X, Y, and e are exactly unital algebra isomorphisms. For the vertex algebra, (Mx,My,1) is therefore a complete based representation; separate Jordan forms are not.

**Theorem UF-020.2.** The functional λ extracting the coefficient of x³y defines a perfect associative symmetric pairing λ(ab). In the basis (1,x,y,xy,x²,x²y,x³,x³y), its Gram matrix is anti-diagonal with determinant 1. This remains true after reduction to every characteristic.

**Arithmetic consequence.** The integral local algebra is free of rank eight and its Hilbert function, socle dimension, and Frobenius determinant do not distinguish any prime. Characteristic 2 is nevertheless exceptional for the quotient map (p,q)=(x²+y²,x²y²), because its Jacobian 4xy(x²−y²) vanishes identically in characteristic 2. This is a distinction between the abstract local algebra and its D4 quotient geometry.

**Open problem UF-020-A.** Classify all parameterized fibers R_{p,q} over residue characteristics, and determine whether odd characteristics introduce additional exceptional strata after specialization. The paper and exact verifier are `the-fold-simultaneous-frobenius-arithmetic.md` and `tools/fold_simultaneous_frobenius.py`.


## UF-021 — Complete residue-characteristic classification

**Theorem UF-021.1.** Every fiber R_{p,q} has rank/length eight in every characteristic, by the monic tower presentation
\[
k[x]/(x^4-px^2+q)\quad\text{with }y^2=p-x^2.
\]
In odd characteristic, the fiber is étale exactly when q(p²−4q)≠0. The two generic discriminant branches have the same four length-two local points and Jordan types as in UF-018, and the vertex retains Hilbert function (1,2,2,2,1).

**Theorem UF-021.2.** In characteristic two, the quotient Jacobian vanishes identically, so every finite fiber is non-étale; the trace discriminant also vanishes identically. This does not contradict UF-020: the abstract vertex algebra still has a perfect Frobenius pairing, and all fibers retain vector-space length eight.

**Arithmetic conclusion.** Characteristic two is the unique exceptional residue characteristic for generic étaleness and the trace discriminant. Rational point splitting can still vary with the parameter field and is not classified by this statement. See `the-fold-residue-characteristics.md` and `tools/fold_residue_characteristics.py`.


## UF-022 — Modular D4 symmetry and a precise eigenprime

**Theorem UF-022.1.** For odd characteristic, the invariant ring of the signed-permutation D4 action is k[x²+y²,x²y²], and the vertex quotient is its coinvariant algebra. Since the characteristic does not divide |D4|=8, the coinvariant algebra is the regular representation
\[
\mathbf1\oplus\chi_1\oplus\chi_2\oplus\chi_3\oplus 2E.
\]

**Theorem UF-022.2.** In characteristic two, sign changes act trivially and the action factors through coordinate swap. The invariant ring becomes k[x+y,xy], while p=(x+y)² and q=(xy)²; the characteristic-zero sign characters collapse and the semisimple decomposition fails.

**Definition (project-local modular eigenprime).** For a specified integral G-module M, a prime ℓ is a modular eigenprime if reduction modulo ℓ changes its semisimple irreducible-character multiplicities from characteristic zero. For this D4 coinvariant module the only such prime is 2. This term is relative to the named action/module, not a claim that primes are eigenvalues.

The paper and finite identity verifier are `the-fold-modular-d4-eigenprimes.md` and `tools/fold_modular_d4.py`.


## UF-023 — Explicit D4 character projectors

**Theorem UF-023.1.** For the signed-permutation generators r(x,y)=(-y,x), s(x,y)=(x,-y), the four one-dimensional projectors on the vertex algebra are
\[
P_{ε,δ}=\frac18(I+εR+R²+εR³)(I+δS),\qquad ε,δ=±1.
\]
Their images are four one-dimensional character lines.

**Theorem UF-023.2.** The two-dimensional isotypic projector is
\[
P_E=\frac12(I-R²),
\]
of rank four. The five projectors are pairwise orthogonal and sum to identity in odd characteristic. Thus the vector-space decomposition has dimensions 1+1+1+1+4, with the final summand two copies of E.

**Modular statement.** In characteristic two, r acts as coordinate swap and s acts trivially. The fixed space has dimension six; the effective C2-module consists of four trivial lines and two indecomposable 2D regular modules. The projectors cannot be reduced because their denominators are not units. These are representation summands, not necessarily algebra ideals.

The paper and exact rational/F2 verifier are `the-fold-d4-character-projectors.md` and `tools/fold_d4_character_projectors.py`.


## UF-024 — Multiplication tensor in the D4-isotypic basis

**Theorem UF-024.1.** In the basis (1,c=x²,b=xy,d=x³y,x,y,u=x³,v=−x²y), the four character lines have characters ++, −+, −−, +−, and the two E copies are (x,y) and (u,v). The complete nonzero non-unit products are
\[
bc=d,\quad x²=c,\quad xy=b,\quad y²=-c,
\]
\[
xv=-d,\quad yu=d,\quad bx=-v,\quad by=-u,\quad cx=u,\quad cy=-v.
\]
All other products between non-unit basis vectors vanish.

**Equivariant consequence.** Multiplication couples the character lines and E copies, so the isotypic decomposition is not a direct-product or ideal decomposition. In particular E₁·E₂ maps through the alternating determinant pairing to the socle character. The algebra multiplication tensor contains more information than the representation decomposition alone.

The exact multiplication table and verifier are in `the-fold-d4-multiplication-tensor.md` and `tools/fold_d4_multiplication_tensor.py`. The next open problem is to compute the full automorphism stabilizer of this tensor and test whether D4 is intrinsically recoverable.


## UF-025 — Graded automorphism group and enlargement beyond D4

**Theorem UF-025.1.** In characteristic zero, every graded linear automorphism is A=tQ, where t∈k* and Q∈O(2,k) has first row (a,b) satisfying
\[
ab(a²-b²)=0.
\]
The orthogonal subgroup has 16 elements and is dihedral of order 16. The original signed-permutation D4 is an index-two subgroup.

**Explicit extra symmetry.** The map x↦x−y, y↦x+y sends q=x²+y² to 2q and sends both fourth powers to zero in C. After normalization by √2 it is a 45-degree rotation of order eight, not contained in signed-permutation D4.

**Scope.** This determines the graded linear automorphism group, not the full possibly nonlinear algebra automorphism group. It shows D4 is not the full graded symmetry group; further intrinsic recovery requires additional data such as chosen axes or quotient-map structure.

See `the-fold-graded-automorphism-group.md` and `tools/fold_graded_automorphisms.py`.


## UF-026 — Complete nonlinear automorphism group

**Theorem UF-026.1.** Over characteristic zero, every automorphism inducing the identity on m/m² is uniquely of the form
\[
X=x+αx²+βxy+γx³+δx²y+ux³y,
\]
\[
Y=y−βx²+αxy−δx³+ηx²y+vx³y,
\]
with seven arbitrary parameters. This kernel is a 7-dimensional unipotent algebraic group.

**Theorem UF-026.2.** The linear-part map gives a split exact sequence
\[
1\to Aut_1(C)\to Aut(C)\to G_{gr}\to1,
\]
so Aut(C)≅Aut₁(C)⋊G_gr. Since G_gr has one-dimensional scalar factor and finite orthogonal part D16, the full automorphism group has dimension 8.

The coefficient constraints follow from expanding X²+Y² in the basis x³,x²y,x³y; X⁴ vanishes automatically once the linear part is x. Nakayama's lemma proves each such endomorphism is an automorphism. The symbolic verifier is `tools/fold_nonlinear_automorphisms.py`; the complete proof and characteristic-zero scope are in `the-fold-nonlinear-automorphism-group.md`.

**Open problem UF-026-A:** compute the seven-parameter group law and lower central series, then study the modular characteristic-two automorphism group.


## UF-027 — Explicit group law for the nonlinear kernel

For θ=(a,b,c,d,e,f,g) and Θ=(A,B,C,D,E,F,G), composition Φθ∘ΦΘ has coordinates
\[
\begin{aligned}
a'&=a+A,&b'&=b+B,\\
c'&=c+C+2Aa-2Bb,&d'&=d+D+2Ab+2Ba,\\
e'&=e+E+2Aa-2Bb,\\
f'&=f+F+2Aab+2Ad+Ba²-Bb²+Bc+Be+3Cb+3Da,\\
g'&=g+G+Aa²-Ab²+Ac+Ae-2Bab-2Bd-3Db+3Ea.
\end{aligned}
\]
This is the exact polynomial group law on the seven-dimensional unipotent kernel from UF-026. The identity is the zero vector; inverse coordinates are obtained from the triangular equations. A symbolic verifier checks all coefficient identities.

See `the-fold-unipotent-group-law.md` and `tools/fold_unipotent_group_law.py`.

**Open problem UF-027-A:** compute inverse and commutator formulas, center, derived subgroup, and lower central series; compare with the m-adic filtration and the D16 action.


## UF-028 — Lie algebra and commutator structure

The Lie algebra of the seven-dimensional kernel has bracket
\[
[D_1,D_2](x)=\omega_u x³y,\qquad [D_1,D_2](y)=\omega_v x³y,
\]
with
\[
\begin{aligned}
\omega_u={}&a₁d₂-a₂d₁+2b₁c₂-b₁e₂-2b₂c₁+b₂e₁,\\
\omega_v={}&-a₁c₂+2a₁e₂+a₂c₁-2a₂e₁-b₁d₂+b₂d₁.
\end{aligned}
\]
Its center and derived algebra coincide and are two-dimensional. At group level the exact commutator is a socle translation; the center and derived subgroup are both precisely the socle-translation subgroup. Thus the nonlinear kernel has nilpotency class two.

See `the-fold-unipotent-lie-algebra.md` and `tools/fold_unipotent_commutators.py`.

**Open problem UF-028-A:** determine the D16 representation on the Lie algebra, its quotient by the center, and the center itself; establish equivariance of the commutator pairing.


## UF-029 — D16 representation on the nonlinear Lie algebra

Under conjugation by a 45-degree rotation r and reflection s, the Lie algebra decomposes multiplicity-free:
\[
\mathfrak u\cong E_1\oplus E_2\oplus\chi\oplus E_3.
\]
Here E1 is the quadratic parameter plane (a,b), E2 is the invariant cubic plane e=c, χ is the cubic line (-1,0,1) with r acting by −1 and s by +1, and E3 is the socle center (u,v). Thus
\[
\mathfrak u/Z(\mathfrak u)\cong E_1\oplus E_2\oplus\chi,
\qquad Z(\mathfrak u)\cong E_3.
\]
The bracket is D16-equivariant because the action is by conjugation; the symbolic verifier checks the explicit identities for both generators.

See `the-fold-d16-lie-representation.md` and `tools/fold_d16_lie_representation.py`.

**Open problem UF-029-A:** restrict the four summands to the original D4 subgroup and compute modular decomposition changes prime by prime.


## UF-030 — Modular stability and the exceptional central prime

**Theorem UF-030.1.** Over an algebraically closed field of any odd characteristic, the D16 representation of UF-029 remains semisimple and multiplicity-free:
\[
\mathfrak u\cong E_1\oplus E_2\oplus\chi\oplus E_3.
\]
This follows from Maschke's theorem and the distinct eighth-root eigenvalue pairs. Over nonclosed fields, square-root availability can change the ground-field realization without changing geometric semisimplicity.

**Theorem UF-030.2.** The integral commutator map \(\Lambda^2\mathbb Z^5\to\mathbb Z^2\) has Smith normal form \((1,1)\), hence remains surjective in every characteristic.

**Theorem UF-030.3.** The radical map \(W\to\operatorname{Hom}(W,Z)\) has Smith normal form
\[
(1,1,1,1,3).
\]
Therefore the center is two-dimensional in every characteristic other than three, but grows to dimension three in characteristic three. The extra central line is precisely the cubic character line \(\chi=\langle(-1,0,1)\rangle\). The derived algebra remains the two-dimensional socle center in every characteristic.

**Important scope.** The normalized orthogonal D16 matrices contain denominators involving 2 and \(\sqrt2\). This note does not claim they reduce directly to characteristic two. Constructing a compatible integral D16 lattice is still required before a characteristic-two modular representation theorem can be stated.

Exact determinantal-divisor and modular-rank checks are in `tools/fold_d16_modular_stability.py`; the proof and coefficient-field distinctions are in `the-fold-d16-modular-stability.md`.

**Open problem UF-030-A:** construct or obstruct an integral D16-stable lattice compatible with the normalized action, then determine the characteristic-two module and the corresponding automorphism-group scheme.


## UF-031 — D4 restriction and the intrinsic characteristic-three center

**Theorem UF-031.1.** Restricting the UF-029 Lie algebra representation to the original signed-permutation subgroup \(D_4=\langle r^2,s\rangle\) gives, over every algebraically closed field of odd characteristic,
\[
\mathfrak u\!\downarrow_{D_4}\cong 2E\oplus\mathbf1\oplus\chi_{-+}\oplus\chi_{--}.
\]
The D16 character line \(\chi=\langle(-1,0,1)\rangle\) becomes trivial; the cubic plane splits into the two indicated one-dimensional characters; the quadratic and socle planes each restrict to the unique two-dimensional irreducible \(E\). This is not the regular D4 representation because \(\chi_{+-}\) is absent.

**Theorem UF-031.2.** The center is intrinsically detectable from the D4 action and bracket. Away from characteristic three it is the socle plane \(E\). In characteristic three it enlarges to \(E\oplus\mathbf1\), with the additional trivial line exactly the cubic vector \((-1,0,1)\). The derived algebra remains \(E\), two-dimensional.

The D4 generators \(r^2\) and \(s\) have integral matrices, even though the full normalized D16 generator \(r\) contains \(1/\sqrt2\). Thus this restriction genuinely has a characteristic-three reduction. The change is in the bracket radical, not in the underlying D4-module decomposition.

The proof and symbolic verifier are in `the-fold-d4-modular-center.md` and `tools/fold_d4_modular_center.py`.

**Resolved by UF-032:** in characteristic two the D4 action factors through C2 and the module is 3J2 ⊕ J1. The reduced bracket remains surjective with zero radical on the five-dimensional quotient, so center = derived algebra = the two-dimensional socle plane.


## UF-032 — Characteristic-two D4 module and bracket

**Theorem UF-032.1.** The integral D4 action reduces modulo two with the reflection generator acting trivially and the quarter-turn generator swapping the coordinate pairs \((a,b)\), \((c,e)\), and \((u,v)\), while fixing \(d\). Hence the action factors through \(C_2\) and
\[
\mathfrak u_{\mathbb F_2}\cong 3J_2\oplus J_1,
\]
where \(J_2\) is the indecomposable two-dimensional regular \(\mathbb F_2[C_2]\)-module and \(J_1\) is trivial.

**Theorem UF-032.2.** The characteristic-two bracket has precisely four nonzero basic products:
\[
[a,d]=u,\quad[b,e]=u,\quad[a,c]=v,\quad[b,d]=v.
\]
It remains surjective onto \(\langle u,v\rangle\), and its radical on the five-dimensional quotient is zero. Thus center = derived algebra = \(\langle u,v\rangle\), dimension two. The bracket remains D4-equivariant.

This is a modular nonsemisimplicity phenomenon without a bracket-center jump. It differs from characteristic three, where the center acquires the additional cubic trivial-character line. The theorem concerns the specified integral bracket lattice. UF-033 separately computes the full characteristic-two derivation algebra, which has dimension 16; the seven-dimensional bracket Lie algebra is not the full tangent algebra.

Proof and exact verifier: `the-fold-d4-characteristic-two.md`, `tools/fold_d4_characteristic_two.py`.

**Open problem UF-032-A:** determine the full automorphism group scheme of the vertex algebra over \(\mathbb Z\), including its characteristic-two tangent dimension and smoothness.


## UF-033 — The characteristic-two automorphism group scheme

**Theorem UF-033.1.** For C = k[x,z]/(x^4,z^2) in characteristic two, every derivation is determined freely by D(x), D(z) in C. Hence dim_k Der_k(C) = 16.

**Theorem UF-033.2.** For general images X,Z, the endomorphism-scheme equations are exactly c^4 = d^2 = h^2 = 0, where c,d are their constant coefficients and h is the x-linear coefficient of Z. The automorphism locus is the open subset where ai − bh is invertible.

**Theorem UF-033.3.** The reduced automorphism scheme has dimension 13, while its identity tangent space has dimension 16. It is therefore non-smooth. The 16-dimensional tangent algebra is the full derivation algebra, not the reduction of the seven-dimensional characteristic-zero unipotent Lie algebra.

Proof and structural verifier: `the-fold-char2-automorphism-scheme.md`, `tools/fold_char2_automorphism_scheme.py`.

**Open problem UF-034:** determine the full automorphism group scheme over arbitrary characteristic and identify the integral closure of the characteristic-zero seven-dimensional unipotent subgroup inside it.


## UF-034 — Full automorphism functor across characteristics

**Theorem UF-034.1.** For (C_{\mathbb Z}=\mathbb Z[x,y]/(x^2+y^2,x^2y^2)), the endomorphism functor is represented by pairs (X,Y\in C_A) satisfying (X^2+Y^2=0) and (X^2Y^2=0). The automorphism locus is the open subset where the induced rank-eight linear map has unit determinant.

**Theorem UF-034.2 (corrected).** The full derivation algebra has dimension 8 in every odd characteristic and dimension 16 in characteristic two. The relation map after removing its common factor 2 has rank eight and Smith invariants (1,1,1,1,1,1,1,2). The actual differentiated-relation map therefore has eight nonzero Smith invariants (2,2,2,2,2,2,2,4). The kernel dimensions are 8 and 16, respectively. The sign in the second relation is \(-x^3P+x^2yQ\).

The characteristic-three center enlargement of the seven-dimensional bracket algebra is distinct from this full tangent calculation.

Proof and verifier: `the-fold-full-automorphism-characteristics.md`, `tools/fold_full_automorphism_characteristics.py`.

**Resolved by UF-035:** the full automorphism group over every algebraically closed field of odd characteristic is U ⋊ G_gr, with dim(U)=7 and G_gr=(G_m × D16)/⟨(-1,-I)⟩ of dimension 1. The full group is smooth of dimension and tangent dimension 8. See `the-fold-odd-characteristic-automorphisms.md`.\n\n**Resolved by UF-036:** the schematic closure is the flat seven-dimensional group scheme U_Z ≅ A^7_Z; the full automorphism scheme is not flat over Z because its generic fiber has dimension 8 while its characteristic-two fiber has dimension 13. See `the-fold-integral-unipotent.md`.


## UF-035 — Odd-characteristic automorphism classification

**Theorem UF-035.1.** Over every algebraically closed field of odd characteristic, the full automorphism group is the semidirect product of the seven-dimensional identity-linear unipotent group U and the one-dimensional graded quotient G_gr=(G_m × D16)/⟨(-1,-I)⟩. Its dimension is eight.

**Theorem UF-035.2.** The full automorphism group scheme is smooth of dimension eight in every odd characteristic: the geometric reduced group has dimension eight and UF-034 gives tangent dimension eight. Characteristic two remains the unique nonsmooth fiber established here; characteristic three's center jump is a property of the marked seven-dimensional bracket algebra, not the full automorphism group.

Proof: `the-fold-odd-characteristic-automorphisms.md`.

**Resolved by UF-036:** the closure of U_Q is U_Z ≅ A^7_Z, a smooth flat integral group scheme; the full automorphism scheme is non-flat at 2. See `the-fold-integral-unipotent.md`.


## UF-036 — Integral unipotent subgroup and full-scheme flatness

**Theorem UF-036.1.** The seven-parameter identity-linear substitutions define a group scheme U_Z ≅ A^7_Z. The UF-027 composition law and its inverse have integer coefficients, and every substitution preserves the defining relations integrally and has determinant one on the rank-eight algebra. Thus U_Z is smooth and flat over Z, with seven-dimensional fibers in every characteristic.

**Theorem UF-036.2.** The schematic closure of the characteristic-zero subgroup U_Q inside Aut(C_Z) is exactly U_Z. Its coordinate ring is torsion-free over Z, so the closure has no vertical components or extra special-fiber thickening.

**Theorem UF-036.3.** The full automorphism scheme is not flat over Z: the generic fiber has dimension eight, whereas the characteristic-two fiber has dimension thirteen. For group schemes locally of finite presentation, flatness forces fiber dimension to be locally constant. The characteristic-two identity-linear kernel has dimension ten, so U_F2 is a proper seven-dimensional subgroup of it.

Proof and symbolic verifier: `the-fold-integral-unipotent.md`, `tools/fold_integral_unipotent.py`.

**Resolved by UF-037:** in characteristic two, the ten-dimensional identity-linear kernel H has coordinates (A,B,C,D,E,F,G,H,I,J), and the flat seven-dimensional subgroup U is cut out by F=0, H=A, B+G+I=0. U is not normal. Its normal closure N is the eight-dimensional subgroup F=0, H=A, and H/N ≅ G_a². The third transverse direction B+G+I is supplied by conjugation; the two remaining directions form the genuine additive quotient. See `the-fold-char2-identity-kernel.md` and `tools/fold_char2_identity_kernel.py`.

**Resolved by UF-038:** N/U ≅ G_a, N is two-step nilpotent with Z(N)=[N,N] ≅ G_a², and the homogeneous space H/U is explicitly A³. The right-coset coordinates are (F, H+A, B+G+I+F(A+C)+A(H+A)). See `the-fold-char2-homogeneous-space.md` and `tools/fold_char2-homogeneous-space.py`.

**Resolved by UF-039:** the reduced normal closure of U in the full reduced automorphism group remains N (dimension 8). But the Lie ideal generated by Lie(U) inside the full 16-dimensional derivation algebra is all of Der(C). Therefore the scheme-theoretic normal closure has reduced support N but full 16-dimensional tangent space: it is a non-reduced thickening supported on N. The exact Hopf ideal and nilpotence structure remain open; see `the-fold-char2-infinitesimal-normal-closure.md` and `tools/fold_char2_infinitesimal_normal_closure.py`.

**UF-040 candidate:** let Q=A_red/N, a smooth five-dimensional quotient. The scheme-theoretic normal closure may be the kernel of A → Q → Q^(1), i.e. the preimage of the first Frobenius kernel. This predicts reduced support N and tangent dimension 16. The extension of the quotient map to the full non-reduced automorphism scheme and the minimality proof remain open. See `the-fold-char2-frobenius-normal-closure.md`.

**Open UF-041:** compute the semidirect-product law of Q and determine whether its quotient morphism extends to the full automorphism group scheme.


## UF-047 — Globality of the second-Frobenius quotient equations

**Theorem UF-047.1.** In the full characteristic-two automorphism coordinate ring, let Delta = ai - bh be the invertible linear determinant. Since h^2 = 0, bh is nilpotent. In characteristic two, ai = Delta + bh, hence ai is a unit. Therefore both a and i are units. The localization used to define the quotient coordinates F = phi/i and R = alpha/a + b phi/(ai) + eta/i is the entire determinant-open automorphism scheme, not a proper chart.

The fourth-power pullbacks F-tilde = phi^4/i^4 and R-tilde = alpha^4/a^4 + b^4 phi^4/(a^4 i^4) + eta^4/i^4 are therefore globally regular on the full automorphism scheme. This removes the chart-overlap issue for these formulas.

**Scope:** this globalizes the second-Frobenius quotient-kernel equations. It does not compute the largest conjugation-stable Hopf ideal contained in the ideal of U, so equality with the minimal normal closure remains open.

**Open UF-048:** compute the universal conjugation coaction on the globally defined Frobenius quotient equations and determine whether the resulting kernel is generated scheme-theoretically by conjugates of U.


## UF-048 — Universal conjugation coefficient ideal

**Theorem/definition UF-048.1.** In full substitution coordinates, U is defined by c=d₀=h=0, a=i=1, b=0, φ=0, η−α=0, β+ψ+θ=0. The universal conjugation map G×U→G induces Conj*:A→O(G)⊗O(U). The ideal of its scheme-theoretic image is ker(Conj*); it is computed by requiring the pullback of a general coordinate function to vanish identically in both variables. It is not obtained by merely pulling back generators of I(U), which tests whether a conjugate lies in U.

The normal closure is obtained by taking the largest Hopf ideal contained in this universal conjugacy-image ideal. This separates the scheme-theoretic union of conjugates from the subgroup generated by them.

**Open UF-049:** compute the coefficient ideal in the full ring A=k[c,d₀,h,a,b,…,Δ⁻¹]/(c⁴,d₀²,h²), then compute its Hopf core and compare with the second-Frobenius kernel through the full intrinsic nilradical filtration n ⊃ n² ⊃ n³ ⊃ n⁴ ⊃ n⁵ ⊃ n⁶=0. Although every element of n has fourth power zero, n⁴ and n⁵ as ideal powers are nonzero.


## UF-049 — Nilradical length and associated graded

**Theorem UF-049.1.** For the nilradical ideal n=(c,d₀,h), with c⁴=d₀²=h²=0, the monomial basis cʳd₀ˢhᵗ (0≤r≤3, 0≤s,t≤1) gives the Hilbert series (1+T+T²+T³)(1+T)² = 1+3T+4T²+4T³+3T⁴+T⁵. Thus the associated-graded ranks in positive degrees are 3,4,4,3,1; n⁵≠0 and n⁶=0. Every individual element of n nevertheless has fourth power zero. This distinction is essential for the Hopf-ideal comparison.

**Open UF-050:** compute the normal-closure and second-Frobenius-kernel ideals on each associated-graded piece and identify the first degree at which they differ, if any. See `the-fold-char2-nilradical-associated-graded.md`.


## UF-050 — Associated graded of the second-Frobenius candidate

**Theorem UF-050.1.** The full automorphism coordinate algebra decomposes as A ≅ A_red ⊗ T, where T=k[c,d₀,h]/(c⁴,d₀²,h²), because determinant localization is equivalent to inverting ai and the Frobenius-candidate equations are pulled back from the reduced quotient. The candidate quotient therefore retains the full nilpotent coefficient algebra. Its associated-graded ranks over its reduced support are 1,3,4,4,3,1 in degrees zero through five; the positive-degree ranks are 3,4,4,3,1. This determines the candidate's thickening but not the minimal normal closure.

**Open UF-051:** compute the actual normal-closure Hopf ideal in degree two n²/n³ and test whether it imposes any additional relation beyond the second-Frobenius candidate. See `the-fold-char2-frobenius-candidate-associated-graded.md`.


## UF-051 — Constant-term coproduct and quadratic nilradical layer

**Exact calculation.** The full degree-two nilradical basis is c², cd₀, ch, d₀h. Under right-to-left composition, the constant-term coproducts are c∘c′ = c+ac′+bd₀′+α(c′)²+β(c′)³+γc′d₀′+δ(c′)²d₀′+ε(c′)³d₀′; d₀∘d₀′ = d₀+hc′+id₀′+φ(c′)²+ψ(c′)³+ηc′d₀′+θ(c′)²d₀′+κ(c′)³d₀′; and h∘h′ = ha′+ih′+η(c′h′+d₀′a′). These are exact coproduct formulas for c,d₀,h. The full conjugation coaction is not yet computed.

**Open UF-052:** derive the conjugation coaction on all four degree-two classes and compare with the candidate.
See `the-fold-char2-quadratic-nilradical-coproduct.md`.


## UF-052 — Quadratic conjugation coaction

**Theorem UF-052.1.** For U-parameters A,C and a full automorphism g, the universal conjugate coordinates modulo n³ are explicitly computed in terms of c² and cd₀ for the c,d₀ outputs, and ch,d₀h for the h output. The formulas are recorded in `the-fold-char2-quadratic-conjugation-coaction.md`. This is the degree-two conjugacy pullback, not yet the orbit ideal's Hopf core.

**Open UF-053:** compute the coefficient span/annihilator in the four-dimensional degree-two layer and compare it with the candidate.


### UF-052 correction / UF-053 reopened

The h-coordinate of the conjugate includes (hC+iA)(c₋h₋+d₋a₋). Its lowest-order approximation has cancellation of the ch terms and equals (hC+iA)d₀/Δ modulo n². The earlier boxed formula modulo n³ and the claim of independent detection of ch and d₀h are withdrawn; second-order inverse coefficients are required. See the correction section in `the-fold-char2-quadratic-conjugation-coaction.md`.


### UF-052 second-order completion

The inverse constant expansion gives d₂ ≡ a(φc₁²+ηc₁d₁)/Δ mod n³. Including this term yields the corrected expression for c₋h₋+d₋a₋ and hence for the h-coordinate of gug⁻¹ modulo n³; see Section 8 of `the-fold-char2-quadratic-conjugation-coaction.md`. This correction still does not determine the full orbit ideal or Hopf core, and it gives no independent detection of ch or d₀h through the h-coordinate.


### UF-052 inverse audit — coupled recursion

The Section 8 explicit formula for S=c₋h₋+d₋a₋ is withdrawn: it omitted first-order feedback in a₋ and h₋ from the exact coproduct terms γS and ηS. Section 9 of `the-fold-char2-quadratic-conjugation-coaction.md` records the corrected coupled filtered system, including c₂,d₂,h₁,a₁ and S modulo n³. The quadratic coefficient span remains open; no conclusion about ch or d₀h is currently justified.


### UF-053 — partial resolution: nilpotent-coordinate coefficient span

The coupled inverse recursion in Section 9 of `the-fold-char2-quadratic-conjugation-coaction.md` simplifies to S=c₋h₋+d₋a₋ ≡ d₀/Δ + φi²c²/Δ³ mod n³. Taking homogeneous degree two in the universal conjugate coordinates c,d₀,h gives the coefficient module M₂=⟨c², cd₀, d₀h⟩ in gr²_n A, rank three. The class ch is not detected by these three output coordinates. This is not yet the full orbit-image ideal: the remaining target coordinates and then the Hopf-core operation must still be computed. See Section 10 of the UF-052 paper.


### UF-053 homogeneous-grading audit

The exact fractions (ic+bd₀)/Δ and (hc+ad₀)/Δ are not homogeneous in the nilradical filtration because Δ=ai+bh. Section 11 of `the-fold-char2-quadratic-conjugation-coaction.md` replaces the earlier degree labels with genuinely homogeneous pieces C₁,D₁,C₂,D₂ and independently rederives S ≡ d₀/Δ + φi²c²/Δ³ mod n³. The rank-three coefficient span in Section 10 is retained.


## UF-054 — Full target-coordinate quadratic audit

**Exact filtration warning.** Cubic terms in the seven-dimensional subgroup U cannot be discarded when computing nonconstant target coefficients modulo the third nilradical power. In characteristic two, `(x+c)^3=x^3+cx^2+c^2x+c^3`, so the coefficient of x has nilradical degree two even though the constant contribution has degree three. The translation test `g(x)=x+c`, `g(z)=z` exhibits a cubic perturbation contributing `Bc²` to a linear target coefficient.

The UF-053 module `⟨c²,cd₀,d₀h⟩` remains restricted to the three nilpotent target coordinates c,d₀,h. It is not the full conjugacy-family coefficient module, and no conclusion about detection of ch by the remaining target coordinates is drawn. See `the-fold-char2-full-conjugation-quadratic-audit.md`.

**Open UF-055:** compute the full degree-two coefficient module across all thirteen nonconstant target coordinates, its annihilator, the conjugacy-image kernel, and its largest Hopf subideal. Do not identify any of these objects with one another without proof.


## UF-055 — Exact cubic conjugation test and coordinate-count correction

The full substitution has fourteen nonconstant coefficient functions plus two constants. The three nilpotent outputs are c,d₀,h, where h is one of the nonconstant coefficients; the remaining thirteen coefficient functions are a,b,α,β,γ,δ,ε,i,φ,ψ,η,θ,κ. This corrects the prior shorthand that described the remaining list as thirteen target coefficients without separately counting h.

For g(x)=x+c, g(z)=z with c⁴=0, and u(x)=x+Bx³, u(z)=z+Bx³ in U, direct composition gives X'=x+B(x+c)³ and Z'=z+B(x+c)³. In characteristic two, the linear coefficient changes by Bc². Hence cubic parameters contribute to the quadratic nilradical layer of nonconstant target coefficients.

**Open UF-056:** compute homogeneous degree-two components of all sixteen coefficient functions c,d₀,a,b,α,β,γ,δ,ε,h,i,φ,ψ,η,θ,κ; determine their coefficient module and annihilator; then compute the conjugacy-image kernel and its largest Hopf ideal. These are distinct objects and must remain distinguished. See `the-fold-char2-fourteen-coordinate-conjugation-test.md`.


### UF-056 — Nilpotent affine centralizer

Let (T) be the family (g(x)=x+c, g(z)=z+hx), with (c^4=h^2=0). Its inverse is (g^{-1}(x)=x+c, g^{-1}(z)=z+hx+hc). Exact substitution in the seven-parameter subgroup
[
u(x)=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,quad
u(z)=z+Axz+Gx^3+(B+G)x^2z+Jx^3z
]
gives (gug^{-1}=u). Thus (T) is contained in the scheme-theoretic centralizer of (U). In particular, this restriction of the conjugation family does not detect (ch); it does not prove that (ch) is absent from the full universal image. The full ambient coaction and Hopf core remain open. See `the-fold-char2-nilpotent-affine-centralizer.md`.

**Open UF-057:** enlarge the tested affine family by general reduced linear coefficients and higher ambient coefficients, and determine whether the mixed class (ch) appears in any of the fourteen nonconstant target-coordinate expansions.


### UF-057 — Triangular affine centralizer

For the seven-dimensional subgroup U, consider (g(x)=c+ax, g(z)=d+hx+iz), with a,i units and c⁴=d²=h²=0. The inverse is (g^{-1}(x)=a^{-1}(x+c)), (g^{-1}(z)=i^{-1}(z+d+ha^{-1}(x+c))). Exact substitution gives (gug^{-1}=u) for every U-element. Thus this entire triangular affine family lies in the scheme-theoretic centralizer, including its mixed nilpotent coefficient products. This does not cover the off-diagonal linear coefficient in g(x), nor higher ambient terms. See `the-fold-char2-triangular-affine-centralizer.md`.

**Resolved by UF-058:** the full determinant-open affine subgroup centralizes the seven-dimensional subgroup U. The proof factors an arbitrary affine linear part into lower- and upper-triangular factors, uses UF-057 for the lower-triangular and translation factors, and verifies the upper-triangular factor by exact substitution. Thus the off-diagonal term bz in g(x) still produces no conjugation variation, and ch is absent from all sixteen target coefficient variations on the affine family. This does not settle nonlinear ambient automorphisms or the universal orbit-image Hopf core. See `the-fold-char2-full-affine-centralizer.md`.

**Open UF-059:** introduce quadratic ambient terms in g(x) and g(z), locate the first nonlinear stratum where conjugation is nontrivial, and compute its effect on all sixteen target coefficient functions before attempting the orbit-image kernel and Hopf core.


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
