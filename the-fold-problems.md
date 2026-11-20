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


## UF-002 — Minimal Fold operation families

**Question.** Given a desired terminal spectral profile, what is the smallest family of allowed power operations that removes the unwanted prime-primary components while preserving the requested ones?

**Exact feasibility result.** For initial spectral orders (d_1,\ldots,d_t) and target orders (c_1,\ldots,c_t), each target must retain or remove each whole prime-primary component. Let

`K = union_j supp(c_j)` and `D = union_j (supp(d_j) \\ supp(c_j))`.

A single global operation family can realize the target if and only if (K\cap D=\varnothing) and the safe allowed exponents cover every prime in (D). A prime that must be retained in one coordinate and erased in another is a genuine global-operation obstruction.

**Optimization result.** A finite primitive-operation catalogue gives exactly weighted or unweighted Set Cover on the erased-prime universe (D); consequently the general catalogue problem is NP-hard (and the factored/support-encoded decision version is NP-complete). If arbitrary composite exponents are allowed, the problem becomes trivial: one reusable exponent type suffices; the product of the erased primes determines its smallest support-minimal representative, while the D-supported part of the joint lcm reaches the target in one application. If only prime exponents are allowed, one exponent type is needed per erased prime.

**Example.** Starting from orders (720=2^4 3^2 5) and (98=2\cdot7^2), retain targets (5) and (49). Then (K=\{5,7\}), (D=\{2,3\}); the allowed composite exponent type (6) is safe and achieves both terminal targets under repeated global application, whereas prime-only exponent types require (2) and (3). The one-generator minimum (6) takes four rounds; the one-step exponent (144) removes the complete primary components immediately.

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
