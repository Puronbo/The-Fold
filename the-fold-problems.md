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


## G-1/G-2/G-4 — Hopf–Galois structure, normalizer, and torsors

**Theorem G-1.1.** In characteristic two, (A=k[x,z]/(x^4,z^2)) is the coordinate Hopf algebra of (G=\alpha_4\times\alpha_2) with x,z primitive. Its regular coaction has coinvariants k and canonical map
[
\beta:A\otimes_k A\to A\otimes_k A,quad
a\otimes b\mapsto(a\otimes1)\Delta(b),
]
with inverse (a\otimes h\mapsto\sum aS(h_{(1)})\otimes h_{(2)}). Hence Spec(A) is the trivial G-torsor over k and A is a Hopf–Galois object. The verifier `tools/fold_char2_hopf_galois.py` constructs the 64-by-64 canonical-map matrix over F₂ and checks rank 64.

**Theorem G-2.1.** The centralizer of the translation subgroup G in the automorphism scheme of the underlying finite affine scheme Spec(A) is G itself. The normalizer is (G\rtimes\operatorname{Aut}_{\mathrm{grp}}(G)). Both assertions are functorial over all characteristic-two coefficient algebras.

The group-scheme automorphism functor is represented by
[
\operatorname{Aut}_{\mathrm{grp}}(G)
=\operatorname{Spec} k[a,a^{-1},f,f^{-1},b,c,d,e]/(d^2),
]
using (x\mapsto ax+bx^2+cz), (z\mapsto dx+ex^2+fz). It has reduced dimension five and tangent dimension six, so is non-smooth.

**Theorem G-4.1.** For a characteristic-two field k,
[
H^1_{\mathrm{fppf}}(k,G)\cong(k/k^4)\times(k/k^2).
]
This classifies torsors under the fixed group scheme G. It does not classify all Hopf structures or all algebra forms.

Added `the-fold-char2-hopf-galois-normalizer.md` and `tools/fold_char2_hopf_galois.py`.

**Still open G-3:** classify all Hopf structures on the underlying algebra, beyond the primitive/filtered structures considered here.

**Still open G-4b:** classify algebra forms and group-scheme twists, and study extension/degeneration over mixed-characteristic arithmetic bases.

**Still open G-5:** construct a global arithmetic family before attempting automorphic representations, Hecke operators, or theta correspondences.

UF-062 remains independent and open.


## G-3 — Multiple group laws on the same Fold algebra

**Theorem G-3.1.** Over a field of characteristic two, the algebra (A=k[x,z]/(x^4,z^2)) is the coordinate algebra of each of the four group schemes
[
\alpha_4\times\alpha_2,\quad
\mu_4\times\alpha_2,\quad
\alpha_4\times\mu_2,\quad
\mu_4\times\mu_2.
]
For multiplicative coordinates the coproduct is (\Delta(u)=u\otimes1+1\otimes u+u\otimes u); for additive coordinates it is primitive. The antipode for a multiplicative coordinate with (u^{2^r}=0) is (S(u)=u+u^2+\cdots+u^{2^r-1}).

These four group schemes are pairwise non-isomorphic. The rank of the image of the restricted 2-power map on the Lie algebra distinguishes zero, one, and two multiplicative factors. The two mixed products are separated by their relative-Frobenius images, respectively (mu_2) and (alpha_2), which are non-isomorphic.

The verifier tools/fold_char2_hopf_structures.py confirms that each of the four regular Hopf–Galois canonical maps has rank 64 over F₂.

**Open G-3a:** determine whether non-product Hopf structures exist on A and classify all structures up to Hopf isomorphism. The four product structures are examples, not an exhaustive classification.

**Open G-3b:** compute the automorphism group schemes and translation normalizers for the three non-additive product laws. The G-2 explicit automorphism-group presentation currently applies only to alpha_4 x alpha_2.


### UF-061 — Reproducible specialization certificate
Adds tools/fold_char2_affine_coefficient_matrix_rank.py. The standard-library verifier constructs the correctly ordered conjugation in F₂[x,z,c,d,h]/(x⁴,z²,c⁴,d²,h²), extracts the sixteen target coefficient rows and fifteen nilpotent monomial columns, omits epsilon-prime, and checks the exact 15-by-15 determinant equals 1. UF-062 remains the determinantal rank-drop locus and Hopf-core problem.


## UF-062A — Rank-drop scheme on a triangular affine slice

**Theorem UF-062A.1.** For g(x)=x+c, g(z)=z+d+hx and arbitrary U parameters A,B,C,D,E,G,J, the ideal of maximal minors of the 16-by-15 nilpotent coefficient matrix is exactly (E^15). The unique nonzero maximal minor is the one omitting epsilon-prime, equal to E^15. Thus the rank-15 locus is D(E), and the rank-drop support is V(E).

**Theorem UF-062A.2.** On E=0, the generic matrix rank is 11 over F₂(A,B,C,D,G,J). A displayed 11-by-11 minor, using target rows (c′,a′,b′,alpha′,beta′,d′,h′,i′,phi′,psi′,eta′) and columns (h,d,dh,c,ch,cd,cdh,c²,c²h,c³,c³h), is C³D⁴J⁴.

The exact symbolic calculation is documented in the-fold-char2-affine-rank-drop-slice.md and verified by tools/fold_char2_affine_rank_drop_slice.py (requires SymPy).

**Still open UF-062B:** determine the rank-drop ideal for the full determinant-open affine family with arbitrary reduced coefficients a,b,i.

**Still open UF-062C:** stratify all lower-rank loci inside E=0 and compute the universal orbit-image kernel and its largest Hopf ideal. The coefficient-matrix determinantal ideal is not itself the orbit-image kernel.


## G-3b — Scheme-theoretic normalizers for all four product Hopf laws

**Correction.** A first mixed-case argument incorrectly inferred that cross-homomorphisms vanish from their geometric points. Over nonreduced coefficient algebras, infinitesimal cross-homomorphisms exist. The corrected calculation is in the-fold-char2-hopf-normalizers-all-four.md.

For each group law G, the translation centralizer is exactly G and the normalizer is (G\rtimes\operatorname{Aut}_{\mathrm{grp}}(G)).

- For alpha_4 x alpha_2, Aut_grp(G) has reduced/tangent dimensions (5,6).
- For mu_4 x alpha_2, the infinitesimal cross-map t↦1+r z with r²=0 gives Aut_grp(G) with underlying scheme C2 x G_m x alpha_2, dimensions (1,2).
- For alpha_4 x mu_2, the cross-map t↦1+p x+q x²+pq x³ with p²=q²=0 gives Aut_grp(G) with underlying scheme Aut(alpha_4) x Spec(k[p,q]/(p²,q²)), dimensions (2,4), with its semidirect composition law.
- For mu_4 x mu_2, Aut_grp(G)=D8 as a constant finite étale group scheme, dimensions (0,0).

The mixed automorphism group schemes are non-smooth; their infinitesimal cross terms are invisible on field-valued points. The initial no-cross-homomorphism claim is withdrawn.



## G-4 — Fppf torsors for all four product Hopf structures

For n=1,2 the fppf cohomology groups are:
```
H^1(k, alpha_(2^n)) = k / k^(2^n)
H^1(k, mu_(2^n))    = k^× / (k^×)^(2^n)
```
Thus:
- alpha_4 x alpha_2: (k/k^4) x (k/k^2);
- mu_4 x alpha_2: (k×/(k×)^4) x (k/k^2);
- alpha_4 x mu_2: (k/k^4) x (k×/(k×)^2);
- mu_4 x mu_2: (k×/(k×)^4) x (k×/(k×)^2).

Explicit rank-eight torsor algebras and coactions are given in the-fold-char2-hopf-torsors-four-laws.md. All classes vanish over perfect fields; they can be nontrivial over imperfect fields such as F₂(t). This classifies torsors under the four fixed product group schemes, not all forms/twists or all Hopf structures.

## G-3c — Fifth, non-product Hopf structure

**Theorem G-3c.1.** On A=k[x,z]/(x^4,z^2) in characteristic two, the formulas
```
Delta(x) = x tensor 1 + 1 tensor x
Delta(z) = z tensor 1 + 1 tensor z + x^2 tensor x^2
epsilon(x) = epsilon(z) = 0
S(x) = x, S(z) = z
```
define a commutative Hopf algebra.

The corresponding group law is
```
(x,z) + (x',z') = (x+x', z+z'+x^2 x'^2).
```
It is a nontrivial central extension of alpha_4 by alpha_2 and is not isomorphic to any of the four product structures: its primitive space has dimension two with basis x,x²; its relative-Frobenius image is alpha_2; and its restricted Lie 2-power map is zero.

The standard-library verifier tools/fold_char2_cocycle_hopf.py checks the Hopf identities and primitive-space dimension exactly over F₂. Together with G_D, this gives at least six pairwise non-isomorphic base Hopf structures on the same algebra. The four product structures' torsor classes remain as in G-4; the fifth cocycle group's torsors are not yet classified.

**Open G-3c:** determine the full automorphism group scheme and translation normalizer of the cocycle group; classify its fppf torsors; and search for further non-product Hopf structures.


## G-3d — Automorphism group and normalizer of the cocycle Hopf law

**Theorem G-3d.1.** For the non-product Hopf law with Delta(x)=x tensor 1+1 tensor x and Delta(z)=z tensor 1+1 tensor z+x² tensor x², every group-scheme automorphism over a characteristic-two k-algebra R is
```
x -> a x + b x^2
z -> a^4 z + c x + d x^2
a in R^×, c^2=0
```
The automorphism group scheme is Spec k[a,a^{-1},b,c,d]/(c²), with reduced dimension 3 and tangent dimension 4. Its composition law is
```
(a,b,c,d)(a',b',c',d')
= (aa', a'b+a^2 b', (a')^4 c+a c', (a')^4 d+b c'+a^2 d')
```
and its inverse is
```
(a,b,c,d)^(-1) = (a^(-1), b a^(-3), c a^(-5), d a^(-6)+bc a^(-7)).
```

**Theorem G-3d.2.** The translation centralizer is G_C and its normalizer in the automorphism scheme of the underlying affine scheme is G_C semidirect Aut_grp(G_C).

The full calculation is in the-fold-char2-cocycle-automorphism-normalizer.md.

**Open G-3d:** classify fppf torsors under G_C and determine whether additional non-product Hopf structures exist.


## G-3e/G-4 — Fppf torsors of the fifth cocycle group

There is an exact sequence of commutative fppf sheaves
```
0 -> alpha_2 -> G_C -> alpha_4 -> 0
```
and the cohomology sequence is short exact:
```
0 -> k/k^2 -> H^1_fppf(k,G_C) -> k/k^4 -> 0.
```
Here H²_fppf(k,alpha_2)=0 by the Frobenius sequence and affine vanishing for G_a. Since G_C is killed by 2, the sequence splits noncanonically as F₂-vector spaces.

For a,b in k, explicit torsors are
```
B_(a,b) = k[u,v]/(u^4-a, v^2-b)
rho(u) = u tensor 1 + 1 tensor x
rho(v) = v tensor 1 + 1 tensor z + u^2 tensor x^2.
```
The canonical map has inverse in coordinates
```
x -> u_1+u_2
z -> v_1+v_2+u_1^2(u_1+u_2)^2.
```
For fixed a, varying b runs through the kernel k/k². After choosing representatives for k/k⁴, these torsors parameterize all G_C-torsor classes; the abstract group splitting is noncanonical.

Full derivation: the-fold-char2-cocycle-torsors.md.


## G-3g — Sixth, non-product Hopf structure with nilpotent Lie 2-map

**Theorem G-3g.1.** On A=k[x,z]/(x⁴,z²), the coproduct
```
Delta(x) = x tensor 1 + 1 tensor x + z tensor z
Delta(z) = z tensor 1 + 1 tensor z
epsilon(x)=epsilon(z)=0; S(x)=x, S(z)=z
```
defines a commutative Hopf algebra. Its group law is (x,z)+(x',z')=(x+x'+zz',z+z'), a nontrivial central extension of alpha_2 by alpha_4.

Its primitive space is span{z,x²}, its Frobenius image is alpha_2, and its invariant derivations satisfy D_z^[2]=D_x and D_x^[2]=0. These invariants distinguish it from the four product structures and the earlier cocycle group G_C.

**Theorem G-3g.2.** Every group-scheme automorphism is
```
x -> a^2 x + a b x^2 z + c z + d x^2
z -> a z + b x^2
a invertible, b^2=0
```
The automorphism group scheme is Spec k[a,a^{-1},b,c,d]/(b²), reduced dimension 3 and tangent dimension 4. Its composition law is
```
(aa', a'b+a^4b', (a')^2 c+a c', (a')^2 d+b c'+a^4 d')
```
and its inverse is (a^(-1), b a^(-5), c a^(-3), d a^(-6)+bc a^(-7)).

The translation centralizer is G_D and the normalizer is G_D semidirect Aut_grp(G_D). Full proof: the-fold-char2-nilpotent-pmap-hopf-structure.md.

## G-3f — Frobenius reduction

For every Hopf structure on A, the square subalgebra is k[x²]/(x⁴), the Frobenius kernel has coordinate algebra k[x,z]/(x²,z²), and F²=0. Over an algebraically closed field the rank-two Frobenius image is alpha_2 or mu_2. The six base Hopf structures and the G_lambda imperfect-field family, with their Frobenius kernels/images, are tabulated in the-fold-char2-frobenius-hopf-classification.md.

This reduces the exhaustive classification to possible height-one kernels and extensions compatible with the fixed algebra. It does not yet prove that the six examples are exhaustive.


## G-3h/G-4 — Fppf torsors under G_D

The exact sequence 0 -> alpha_4 -> G_D -> alpha_2 -> 0 gives
```
0 -> k/k^4 -> H^1_fppf(k,G_D) -> k/k^2 -> 0.
```
Here H²_fppf(k,alpha_4)=0 and alpha_2(k)=0. Since G_D is killed by 2, the sequence splits noncanonically as F₂-vector spaces.

For a,b in k, explicit rank-eight torsors are B_(a,b)=k[u,v]/(u⁴-a,v²-b), with
```
rho(u) = u tensor 1 + 1 tensor x + v tensor z
rho(v) = v tensor 1 + 1 tensor z.
```
The inverse canonical-map coordinates are
```
z -> v_1+v_2
x -> u_1+u_2+v_1(v_1+v_2).
```
For fixed b, varying a runs through the kernel k/k⁴. Full proof: the-fold-char2-nilpotent-pmap-torsors.md.


## G-3i — Imperfect-field mixed Hopf family

For t=1+z and lambda in k, define
```
Delta(x) = x tensor 1 + 1 tensor x
Delta(t) = (t tensor t)(1 + lambda x^2 tensor x^2)
t^2 = 1, x^4 = 0.
```
The factor 1+lambda x² tensor x² is a mu_2-valued multiplicative 2-cocycle on alpha_4, so this defines a commutative Hopf law. It is an extension 0 -> mu_2 -> G_lambda -> alpha_4 -> 0.

The extension splits exactly when lambda is a square in k. If lambda=beta², T=t(1+beta x²) is group-like. If lambda is nonsquare, the unique mu_2 subgroup makes a product isomorphism impossible. Thus over an imperfect field such as F₂(s), lambda=s gives another Hopf structure on the same algebra, non-isomorphic to the six base examples.

Full derivation: the-fold-char2-imperfect-mixed-hopf-family.md. The normalized symmetric cocycle classes in the fixed global-section model are k/k², verified by tools/fold_char2_mixed_hopf_cocycle_class.py. Over perfect fields this family splits and adds no new isomorphism class.


The fppf torsor sequence is
```
0 -> k^×/(k^×)^2 -> H^1(k,G_lambda) -> k/k^4 -> Br(k)[2].
```
The boundary map is determined by lambda and remains open. See the-fold-char2-imperfect-mixed-hopf-family.md.


### G-3i verification refinement
The normalized symmetric cocycle basis includes a possible `rho xy` term. The `mu_2`-valued condition gives `rho²=0`, and the field hypothesis forces `rho=0`. The remaining equations yield the previously stated `k/k²` classification in the fixed global-section polynomial model. See the updated cocycle verifier.


## G-3j — Automorphism group of G_lambda

For every k-algebra R, the group-scheme automorphisms are
```
x -> a x + b x²
t -> t(1 + u x + β x² + uβ x³)
u²=0, β²=λ(1+a⁴), a invertible.
```
The composition law for f after g is `(aa', a'b+a²b', u+au', β+u'b+a²β'+auu')`; the inverse is `(a⁻¹,a⁻³b,a⁻¹u,a⁻²β+a⁻³ub)`. The reduced dimension is two and tangent dimension four. The nilpotent parameter u is essential: omitting it would miss infinitesimal automorphisms. Full proof and symbolic verifier: `the-fold-char2-imperfect-mixed-hopf-automorphisms.md` and `tools/fold_char2_mixed_hopf_automorphisms.py`.


## G-3k — Frobenius factorization of the mixed-family boundary

Let E_lambda be the extension of alpha_2 by mu_2 with cocycle `1+lambda*r*s`. Since `1+lambda*x²*y²` is its pullback along relative Frobenius `F:alpha_4 -> alpha_2`, the extension G_lambda is `F*E_lambda`. Naturality gives `δ_lambda=δ'_lambda∘F_*`. The map `F_*:k/k⁴ -> k/k²` sends `[a]` to `[a]`, so `δ_lambda` factors through k/k² and vanishes on k²/k⁴. The unresolved boundary is reduced to `δ'_lambda` for E_lambda.


## G-3l — Vanishing criterion for the mixed-family boundary

For `E_lambda` and an `alpha_2`-torsor `u²=a`, the boundary vanishes exactly when there are `c,d∈k` with `c²+a d²+d=λ`. The proof classifies the possible `mu_2`-torsor over `k[u]/(u²-a)` and derives the action cocycle equation. By Frobenius factorization, this also gives the vanishing criterion for `G_lambda` on `alpha_4`-torsors. In particular, if λ is square then the boundary is identically zero. The Brauer class is explicitly `Q(a,λ)=k⟨U,D⟩/(U²=a,D²=λ,DU+UD=1)`, by the `SL₂`/`PGL₂` descent calculation in `the-fold-char2-imperfect-mixed-hopf-family.md`.

The exact action-cocycle calculation is independently encoded in `tools/fold_char2_mixed_torsor_boundary.py`.


## G-3m — Quaternion description of the boundary

The central extension `E_lambda` is the pullback of `SL₂ -> PGL₂` along `alpha_2 -> PGL₂`, `r ↦ [I+rD₀]`, with `D₀²=λI`. Twisting `M₂(k)` by the alpha₂-torsor `u²=a` descends the algebra generated by `U=uI+N` and `D=D₀`, with `U²=a`, `D²=λ`, `DU+UD=1`. Thus `δ'_lambda([a])=[Q(a,λ)]∈Br(k)[2]`, and Frobenius gives the same formula for `δ_lambda` on `k/k⁴`.

The resulting torsor classes fit into `0 -> k×/(k×)² -> H¹(k,G_lambda) -> ker([a]↦[Q(a,λ)] : k/k⁴ -> Br(k)[2]) -> 0`; this splits noncanonically because G_lambda is killed by two.

The quaternion descent identities are encoded in `tools/fold_char2_mixed_quaternion_descent.py`.

For parameters λ,μ, the mixed groups are isomorphic iff some `a∈k×` satisfies `λ+μa⁴∈k²`; this quotients fixed-section cocycle classes by the induced scaling action of `Aut(alpha_4)`.


## G-3n — Exhaustive height-one kernel classification

Over an algebraically closed field, the two-dimensional abelian restricted Lie algebra of a rank-four height-one commutative group scheme has a semilinear 2-map. Its rank is 0, 1, or 2; the rank-one case splits into image=kernel (nilpotent Jordan, `I_{1,1}`) or image≠kernel (`alpha₂×mu₂`). Rank 0 and 2 give `alpha₂²` and `mu₂²`. These are exactly four types, all already realized by Fold Hopf structures. This exhausts the possible height-one Frobenius kernels but not the full rank-eight extensions. Full proof: `the-fold-char2-height-one-kernel-classification.md`.

The height-one-kernel note gives the eight possible kernel/image pairs; three are not yet realized or ruled out. This is the next finite incidence problem before classifying extension classes.


## G-4b — Torsors under G_C and G_D

The non-product central extensions have exact fppf torsor sequences:
- `0 → k/k² → H¹(k,G_C) → k/k⁴ → 0`, from `0 → α₂ → G_C → α₄ → 0`.
- `0 → k/k⁴ → H¹(k,G_D) → k/k² → 0`, from `0 → α₄ → G_D → α₂ → 0`.

Both are short exact because the quotient has no nonidentity k-points and `H²(k,α₂)=H²(k,α₄)=0`. Since both groups are killed by two, the sequences split noncanonically as F₂-vector spaces. Thus their abstract H¹ groups agree with that of the product `α₄×α₂`, although the group schemes differ. Full proof: `the-fold-char2-nonproduct-torsor-classes.md`.

The `G_lambda` automorphism proof now explicitly excludes a possible additive component in the image of `t` by comparing the mixed tensor summands. The composition convention is stated at the ring-map level, and the symbolic verifier checks the full substitutions and inverse, not only preservation of the defining equations.


## G-4c — Comparative fppf torsor groups

The torsor groups of all seven known Hopf structures are now tabulated in `the-fold-char2-comparative-torsor-groups.md`. The four product rows follow from Kummer and Frobenius sequences; the `G_C` and `G_D` rows from their central-extension sequences; and the `G_lambda` row from its quaternion Brauer boundary. In particular, abstract `H¹` does not distinguish `G_C` or `G_D` from `α₄×α₂`.


## G-4d — Explicit torsor models for G_C and G_D

Every G_C-torsor is represented by `u⁴=a, v²=b`, with action `(u,v)·(r,s)=(u+r,v+s+u²r²)` and parameter relation `(a,b)~(a+q⁴,b+q⁴a+p²)`. Its torsor addition is `(a,b)+(a',b')=(a+a',b+b'+aa')`.

Every G_D-torsor is represented by `u²=a, v⁴=b`, with action `(u,v)·(r,s)=(u+s,v+r+us)` and parameter relation `(a,b)~(a+q²,b+q⁴a²+p⁴)`. Its addition is `(a+a',b+b'+a²a'²)`. The models, canonical-map inverses, completeness, and equivalence proofs are in `the-fold-char2-nonproduct-torsor-models.md`.

The explicit G_C/G_D torsor models are checked by `tools/fold_char2_nonproduct_torsor_models.py`; the exact symbolic identities were executed over F₂.


## G-4e — Explicit mixed-family torsors

When `c²+a d²+d=lambda`, the scheme `u⁴=a, v²=q` is a `G_lambda`-torsor under `(u,v)·(r,t)=(u+r, v t(1+(c+d u²)r²))`. The action law is exactly the quaternion splitting equation; the canonical action map has inverse `r=u'+u`, `t=(v'/v)(1+(c+d u²)r²)`. Varying `q` modulo squares gives the full fiber over the quotient torsor. See `the-fold-char2-mixed-torsor-models.md`.

Verifier: `tools/fold_char2_mixed_torsor_models.py`.

The mixed-family boundary also has standard symbol form: for `lambda≠0`, `Q(a,lambda)≅[a*lambda,lambda)_2` via `I=UD`, `J=D`; for `lambda=0` the boundary is zero. The explicit torsor action and inverse are checked in `tools/fold_char2_mixed_torsor_models.py`.


## G-2c — Normalizer of G_lambda translations

Inside the full automorphism scheme of the underlying Fold affine scheme, the translation centralizer is exactly `G_lambda` and the normalizer is `G_lambda ⋊ Aut_grp(G_lambda)`. The latter has reduced dimension two and tangent dimension six (two translation directions plus four automorphism tangent directions). See `the-fold-char2-mixed-hopf-normalizer.md`.

An explicit nonzero obstruction is now proved over `k=F₂(s,t)`: for `lambda=s` and quotient class `[t]`, the splitting equation `c²+t d²+d=s` has no solution. Multiplying by t gives an Artin–Schreier equation whose right side has odd negative valuation at t=infinity, impossible for an element of the form `y²+y`. Thus `Q(t,s)` is nontrivial in the Brauer group and the corresponding alpha₄-torsor does not lift.


## G-4f — Arithmetic of the quaternion boundary

For lambda nonzero, the mixed-family boundary has image
`{[b,lambda)_2 : b in k}` and exact kernel criterion
`c²+a d²+d=lambda`. Over k=F₂(s,t), lambda=s, the class a=t is
nontrivial: multiplying the splitting equation by t and setting y=td gives
`y²+y=t(s+c²)`; the right side has odd negative valuation at t=infinity,
whereas an Artin–Schreier expression y²+y has even negative valuation.
Adjoining sqrt(lambda) kills the whole boundary map. The complete note
`the-fold-char2-quaternion-boundary-arithmetic.md` records the proof and
the remaining kernel-classification problems.

**Open arithmetic problem:** classify all a in F₂(s,t) satisfying
`c²+a d²+d=s`, and extend the description to useful imperfect-field
extensions and valuation settings.


## G-4g — Full kernel parameterization over F₂(s,t)

For k=F₂(s,t), lambda=s, the exact boundary kernel is
`{[s r²+r] in k/k² : r in k×}`. Indeed, the splitting equation
`c²+a d²+d=s` forces d nonzero and gives
`a=s/d²+1/d+(c/d)²`; put r=1/d. Conversely choose d=1/r,c=0.
This describes the entire kernel as the image of the additive polynomial
`L_s(r)=s r²+r` modulo squares. The class [t] is outside this image by
the valuation obstruction already recorded. A simpler intrinsic description
of this image subspace remains open.

 
### G-4h — Coefficient and Artin–Schreier criterion for the full kernel

For \(k=\mathbb F_2(s,t)\), \(\lambda=s\), put \(K=k^2=\mathbb F_2(S,T)\), \(S=s^2,T=t^2\). Writing a class as \(\alpha s+\beta t+\gamma st\), the exact kernel condition is
\[
\exists q\in K:\ q^2+q+S(\alpha+T\beta^2+ST\gamma^2)\in S K^2.
\]
This follows by expanding the full parameterization \([sr^2+r]\) in the \(K\)-basis \(1,s,t,st\), then eliminating one coefficient using surjectivity of \(K\to K^2\). It is an exact one-variable Artin–Schreier coset criterion; a closed valuation/differential classification of its solutions remains open. See the-fold-char2-quaternion-boundary-arithmetic.md.


### UF-063 — Degeneracy locus for the mixed (ch) coefficient

The full-affine (ch)-coefficient vector vanishes identically across the sixteen target coordinates exactly on
[
A=C=J=E=0,qquad B+Gbt=0,
]
where (t=i^{-1}). Outside this locus the mixed nilpotent monomial is detected by at least one target coordinate. This does not settle the full coefficient-module or Hopf-core computation. See the-fold-char2-full-affine-ch-coefficient.md.


### UF-064 — First-order full-affine coefficient map

The correctly ordered full determinant-open conjugation has no terms linear in c,d,h in X'. In Z', the coefficient matrix in the basis c,d,h is the table in Section 7 of the-fold-char2-full-affine-ch-coefficient.md. Its minor on rows z,x,xz is A²atC, so the first-order map has generic rank three. Higher nilpotent layers and the Hopf core remain open.


### UF-064 correction — complete first-order map

The original UF-064 first-order table omitted linear terms in X' and misplaced some c,d contributions in Z'. It is superseded by the corrected two-coordinate tables in Section 7 of the affine coefficient paper. The generic-rank-three minor A²atC is unchanged. All subsequent higher-layer calculations must use the corrected table.


### UF-065 — Quadratic nilpotent coefficient layer

The complete degree-two coefficient vectors for c², cd, ch, dh are recorded in Section 8 of the affine coefficient paper. The ch column agrees with UF-060. A four-by-four minor on X' rows c',a',b',alpha' is bQ²TR/(a³i⁵), where Q=Ab+Ci, R=Di²+Gb²+Gbi, T=Bb+Di+Gb. Hence this graded layer has generic rank four. Higher layers and the full orbit-image/Hopf-core problem remain open.


### UF-066 — Complete higher nilpotent layers
The cubic, quartic, and top-degree coefficient vectors are now computed in
both conjugated coordinates. Explicit minors prove generic associated-graded
ranks 4, 3, and 1 in degrees three, four, and five. Together with UF-064 and
UF-065, the full positive-layer rank profile is (3,4,4,3,1), matching the
Hilbert dimensions of the nilpotent parameter algebra. This does not yet
determine the unfiltered coefficient module, orbit-image ideal, or Hopf core.
See Section 9 of the-fold-char2-full-affine-ch-coefficient.md.


### UF-067 — Generic full rank of the unfiltered coefficient matrix
The 16-by-15 matrix of all nonconstant nilpotent monomial coefficient
vectors has generic rank 15. A maximal minor is certified nonzero by an
exact specialization over F_256=F_2[u]/(u^8+u^4+u^3+u^2+1): with
(a,b,i,A,B,C,D,E,G,J)=(d9,c5,c3,d7,14,84,f8,cf,9b,f4), deleting the
X' x^3 z row gives determinant 4a. This proves generic linear independence
across all nilpotent degrees, but does not yet identify the orbit-image
ideal or its largest Hopf ideal. See Section 10 of
the-fold-char2-full-affine-ch-coefficient.md.


### UF-068 — Local splitting of the full coefficient map
The UF-067 maximal minor \(\delta\) is nonzero, so on the dense principal open \(D(\delta)\) the 16-by-15 coefficient map is a split injection with free rank-one cokernel. This is a module statement only: it does not identify the orbit-image ideal or prove coproduct stability. UF-069 is to compute the coefficient-algebra multiplication and coproduct on this chart, then test the rank-one residual direction.


### UF-069 — Unique residual linear relation on the full-rank chart
On the chart \(D(\delta)\) from UF-068, partition \(M=(M_0;v)\) using the invertible 15-row minor. The normalized left-kernel vector is \(\ell=(vM_0^{-1},1)\), and it is the unique relation among the sixteen target rows that annihilates all fifteen nilpotent monomial columns. Thus one parameter-ring-linear combination of the sixteen pulled-back target functions is nilpotent-independent. Its coefficients lie in the localized parameter ring, so this is not automatically a relation in the k-algebra generated by the target functions. UF-070 must identify that image algebra before any Hopf-core inference.


### UF-070 — Elimination presentation of the affine-conjugator coefficient image algebra
The sixteen target coefficient functions of the three-parameter affine-conjugator family define \(\theta:k[Y_1,\ldots,Y_{16}]\to\mathcal R\), with \(Y_j\mapsto f_j\), where \(\mathcal R=k[a,b,i,A,B,C,D,E,G,J,a^{-1},i^{-1},c,d,h]/(c^4,d^2,h^2)\). The auxiliary affine-slice image algebra is \(k[f_1,\ldots,f_{16}]\cong k[Y]/\ker\theta\), and \(\ker\theta\) is the contraction of the graph ideal \((Y_j-f_j)\) to \(k[Y]\). Since the UF-067 minor \(\delta\) is a nonzero divisor on this source algebra, localization at \(\delta\) leaves this kernel unchanged. This is not the full universal conjugation image for \(G\times U\to G\); its full orbit-image ideal and Hopf core remain open. See Section 13 of the affine coefficient paper.


### UF-072 — Two-copy coproduct test for the affine-conjugator image
Let \(I_{\rm aff}\) be the kernel of \(O(G)\to O(G_{\rm aff})\otimes O(U)\) for the affine-linear conjugator subgroup \(G_{\rm aff}\). UF-071 proves the exact Hopf criterion: test \(\Delta(I_{\rm aff})\subseteq I_{\rm aff}\otimes O(G)+O(G)\otimes I_{\rm aff}\) by substituting the product of two independently parameterized conjugates \(g_1u_1g_1^{-1}\) and \(g_2u_2g_2^{-1}\). The one-copy elimination ideal and this two-copy test remain uncomputed. Even its Hopf core is only the affine-conjugator-generated subgroup, not necessarily the full normal closure under \(G\).


### UF-072A — Nilradical and dimension bound for the affine-slice image
The affine-slice source is \(\mathcal R=B_{\rm red}\otimes k[c,d,h]/(c^4,d^2,h^2)\), where \(B_{\rm red}=k[a^{\pm1},b,i^{\pm1},A,B,C,D,E,G,J]\) has dimension ten. For \(\mathcal A_{\rm aff}=k[f_1,\ldots,f_{16}]\subseteq\mathcal R\), the ideal \(\mathcal N=\mathcal A_{\rm aff}\cap(c,d,h)\mathcal R\) is exactly its nilradical: \(\mathcal A_{\rm aff}/\mathcal N\) embeds in the reduced ring \(B_{\rm red}\), and \(\mathcal N^6=0\). Consequently \(\dim\mathcal A_{\rm aff}\leq10\). This is a structural bound, not an elimination presentation or coproduct calculation. **UF-072B:** the reduced image is exactly k[A,B,C,D,E,G,J], so the affine-slice image has dimension seven. **UF-072C:** compute the nilpotent filtration and two-copy coproduct.


### UF-072B — Exact reduced affine-slice image
Setting \(c=d=h=0\) makes the affine conjugator \(g(x)=ax+bz,\ g(z)=iz\). A universal substitution calculation in characteristic two proves \(gug^{-1}=u\) for every \(u\in U\). The reduced sixteen-coordinate image is exactly \((0,1,0,A,B,C,D,E;0,0,1,0,G,A,B+G,J)\), so the reduced image algebra is \(k[A,B,C,D,E,G,J]\), and \(\dim\mathcal A_{\rm aff}=7\). This sharpens UF-072A's upper bound ten. The nilpotent thickening and two-copy coproduct remain open. **UF-072C:** compute the five nilpotent layers over this seven-dimensional reduced image and then perform the independent two-copy Hopf test.


### UF-072C — Nine explicit generators for the affine-slice nilradical
- Chooses seven target coefficient lifts whose reductions are (A,B,C,D,E,G,J); they generate a polynomial subalgebra (S\cong k[A,B,C,D,E,G,J]) mapping isomorphically to the reduced image.
- Constructs the other nine target coefficients after subtracting their reduced values. These generate the nilradical (mathcal N) as an ideal.
- Proves each of the nine generators has fourth power zero, so the full affine-slice image algebra is finite as an (S)-module.
- Gives the exact first-layer presentation (mathcal N/\mathcal N^2\cong S^9/K_1), with (K_1) the still-uncomputed relation module obtained by eliminating (a,b,i).
- Higher filtration layers and the independent two-copy coproduct/Hopf test remain open.


### UF-072D — First-order relation-module bound
- Subtracts the nine UF-072C generators in the corrected UF-064 table and records their exact linear (c,d,h) coefficient vectors.
- Proves the seven nonzero columns are linearly independent over (k(A,B,C,D,E,G,J)) after retaining the Laurent parameters (a,b,i).
- Shows the first-order source-expansion map has kernel exactly the two coordinate summands for (n_1=X_1) and (n_4=Z_1).
- Consequently the true relation module for (mathcal N/\mathcal N^2) is contained in (Se_1\oplus Se_4), but equality is not asserted: quadratic source terms must still be compared with products in \(\mathcal N^2\) (UF-072E).


### UF-072E — The conormal layer is free of rank nine
- Specializes (b=C=0) and compares Laurent (a)-exponents in the UF-065 quadratic expansions.
- Proves (n_1\notin\mathcal N^2) from ([c^2]n_1=A/a), while all products of first-order generators have (c^2)-coefficients with nonnegative (a)-exponents.
- Proves (n_4\notin\mathcal N^2) from ([cd]n_4=A/i), while all products have (cd)-coefficients with (a)-exponent at least one.
- Together with UF-072D, establishes (K_1=0) and \(\mathcal N/\mathcal N^2\cong S^9\).
- Higher associated-graded layers and the two-copy Hopf test remain open.


### UF-072F — Quadratic initial multiplication map
- Forms the 28 pair products of the seven nonzero first-order generators and expands them in the four-dimensional degree-two source basis ((c^2,cd,ch,dh)).
- Exact elimination over (K=\mathbb F_2(A,B,C,D,E,G,J)), after clearing (a^2i^3), gives rank 24 and a four-dimensional kernel.
- Kernel basis: (n_2^2, n_2n_5, n_5^2, n_2n_6+n_3n_5), interpreted only as quadratic initial relations.
- Does not determine the full quotient \(\mathcal N^2/\mathcal N^3\), because products involving (n_1,n_4) may start in degree three or higher; higher terms and integral (S)-module relations remain open.



### UF-072G — Corrected cubic initial calculation
- Corrects \(\operatorname{in}_3(n_2n_5)=(0,a(AB+CG)/i,0,0)\); its \(cdh\)-coordinate cancels.
- Retains the displayed cubic initial vector for \(n_2n_6+n_3n_5\).
- A reproducible \(\mathbb F_{256}\) specialization gives cubic triple-map rank 60; adjoining the corrected first vector leaves rank 60, while adjoining the second raises it to 61.
- These are specialization ranks and generic lower bounds only. The exact generic cubic relation module and \(\mathcal N^2/\mathcal N^3\) remain open. The previous claim of two independent generic classes is withdrawn.


### UF-072H — Exact generic cubic ranks
- Computes the cubic initial matrix over K=F_2(A,B,C,D,E,G,J), retaining Laurent monomials in a,b,i.
- Exact SymPy rational-function-field elimination gives rank 60 for the 84 triple products.
- Adjoining corrected in_3(n_2n_5) leaves rank 60; adjoining in_3(n_2n_6+n_3n_5) gives rank 61; adjoining both gives 61.
- Exactly one of these two vectors contributes a new generic cubic initial direction. This does not determine the full N^2/N^3 or its integral S-module structure.
- Reproducible exact certificate: certificates/uf072h_generic_cubic_rank.py.


### UF-072I — Degree-three pair-product classes
- Computes cubic initial terms of all products n_1n_j and n_4n_j for j=2,3,5,6,7,8,9.
- Exact generic rank rises from 60 for triple products to 70 after these 14 columns; corrected n_2n_5 adds none, while n_2n_6+n_3n_5 raises rank to 71.
- Ten independent classes come from n_1/n_4 products and one from the mixed quadratic-kernel relation. Together with the degree-two rank 24, the first two graded pieces contribute 35 generic dimensions.
- Degree-four and higher contributions, including n_1^2,n_1n_4,n_4^2, remain open.
- Reproducible exact certificate: certificates/uf072i_degree3_pair_product_rank.py.


### UF-072J — Remaining constant-generator product
- Proves exact identities n_1^2=n_4^2=0 because their source expansions have degree at least two and every such monomial squares to zero in k[c,d,h]/(c^4,d^2,h^2).
- Computes in_4(n_1n_4)=A^2 c^3d/(ai), a nonzero source term.
- Whether n_1n_4 lies in N^3 is open; this requires the degree-four initial image of N^3, including triple-product syzygies and fourfold first-order products.



undefined



### UF-072L — Corrected degree-four specialization bounds

Corrects the quadratic source terms for \(n_8=Z_{xz}-s_A\) and
\(n_9=Z_{x^2z}-s_B-s_G\):
\[
Q_8=Ja c^2+at(Ea+Jb)cd+bt^2(Bi+Gb)ch+bt^2(Bb+Di+Gb)dh,
\quad
Q_9=Ja^2t ch+a^2t^2(Ei+Jb)dh.
\]
A follow-up term-by-term comparison against UF-065 confirms that the corrected quadratic inputs Q2,Q3,Q5,Q6,Q7,Q8,Q9 and the n1,n4 terms now match the source table. This validates the quadratic input table only; all degree-four ranks remain withdrawn pending a fresh matrix computation.

An additional audit found a missing factor of `a` in the `dh`-coefficient of `Q_7=Q(Z_{x^2})`. The previously reported 175/176 specialization ranks are withdrawn too. The correct coefficient is `at^2(Bb+Di+Gb)`. The script has been patched, but no degree-four rank is currently certified. The generic rank and whether `n_1n_4` survives modulo `N^3` remain open.

### UF-072O — Completeness of the degree-four initial test space
- The 350-column construction is structurally complete for the source-degree-four initial image of N^3: 84 corrected triple products of the seven degree-one generators, 56 products of n1 or n4 with a pair of degree-one generators, and 210 fourfold products of the seven degree-one generators arising from an algebra multiplier.
- No other generator-degree pattern contributes in source degree four. This proves completeness of the test space, not its rank.
- If in4(n1*n4) lies outside its K-linear span over K=Frac(S), then n1*n4 is not in N^3. If it lies inside, integral S-module membership remains unresolved.
- Next: rebuild the audited matrix and certify its exact generic rank and augmented rank.


### UF-072P — Fresh degree-four specialization lower bounds
- Rebuilt the 350-column, 470-row degree-four initial matrix from the audited L_j and Q_j tables.
- Three listed nonzero F_256 specializations all give rank 172, rising to 173 after adjoining in4(n1*n4).
- Therefore the generic ranks are at least 172 and 173, respectively. No generic upper bound is known; the strict generic rank gap and n1*n4 nonmembership in N^3 remain open.
- Next: construct a symbolic rank-172 upper-bound certificate over K=Frac(S).
- Certificate: certificates/uf072k_degree4_specialization.py (specialization computation only).

- Execution audit: the three tuples in the certificate were run; each returned (172,173). Earlier references to five specializations were erroneous and are corrected here.


### UF-072Q — Dual certificate for degree-four nonmembership
- Reframes the decisive test: instead of first proving the full generic rank of the 470-by-350 matrix (M), construct one exact row functional (lambdain K^{470}) with (lambda M=0) and (lambda v
e0), where (v=operatorname{in}_4(n_1n_4)).
- Such a certificate directly proves (v
otinoperatorname{im}_K(M)), hence (n_1n_4
otinmathcal N^3) by UF-072O.
- A promising search is a 173-row restriction whose augmented specialization has a nonzero 173-by-173 minor; seek a symbolic row dependence on the 350 unaugmented columns and verify its nonzero pairing with (v).
- A specialization-only dependence is insufficient. No symbolic dual vector has yet been found; UF-072P's finite-field lower bounds remain the only certified degree-four rank information.


### G-6 — Involutive representations in characteristic two
- For a representation (J^2=1) over a field of characteristic two, set (N=J-1). Then (N^2=0), and conversely every square-zero (N) gives an involution (J=1+N).
- Equivalently, (C_2)-modules are modules over (k[\epsilon]/(\epsilon^2)). The canonical invariant is the filtration (operatorname{im}N\subseteq\ker N\subseteq V), not a plus/minus eigenspace decomposition.
- The exact sequence (0\to\ker N\to V\xrightarrow{N}\operatorname{im}N\to0) records the possible non-semisimple extension. This is the correct local model for order-two symmetries in characteristic-two Fold/Galois representations.
- Scope: this applies to restriction to an order-two subgroup; it does not classify arbitrary profinite Galois representations or imply that every such representation contains an involution.

### G-7 — Order-two Galois cohomology in characteristic two
- For a separable quadratic extension (L/K) in characteristic two and a finite-dimensional (k[C_2])-module (V), put (N=\sigma-1). Since (N^2=0) and the norm (1+\sigma=N), the two-periodic cyclic resolution gives (H^q(C_2,V)=\ker N/\operatorname{im}N) for every (q\ge1).
- If (m=\dim_kV) and (r=\operatorname{rank}N), then every positive-degree cohomology group has dimension (m-2r). Choosing lifts of a basis of (im N) gives the decomposition (V≅k[C_2]^r⊕k^{m-2r}); positive cohomology counts the trivial Jordan blocks.
- Inflation–restriction identifies the descent obstruction for invariant classes in (H^1(G_L,V)) with the transgression into (H^2(C_2,V^{G_L})), which is this same square-zero quotient.
- This is a structural calculation for a specified quadratic quotient, not a classification of arbitrary profinite Galois representations. The Fold-specific task is to construct natural global modules and evaluate the transgression on actual arithmetic classes.



### G-8 — Cyclic (2)-power Galois cohomology
- For a finite cyclic quotient (C_q), (q=2^n), in characteristic two, put (D=\sigma-1). Then (k[C_q]\cong k[D]/(D^q)) and the norm is (D^{q-1}).
- The cyclic resolution gives (H^{2j+1}=\ker D^{q-1}/\operatorname{im}D) and (H^{2j+2}=\ker D/\operatorname{im}D^{q-1}).
- Decomposing (V) into nilpotent Jordan blocks, every block of length (d<q) contributes one dimension in every positive degree; a length-(q) block is free/projective and contributes zero. Hence (dim H^j(C_q,V)) equals the number of blocks shorter than (q), for all (j\ge1).
- Inflation–restriction places the descent obstruction in (H^2(C_q,V^{G_L})). The theorem gives an exact finite quotient test, not a global Fold Galois representation or an evaluated arithmetic transgression.
\n

### G-9 — Explicit Jordan-chain representatives
- For each Jordan block \(J_d\) of \(D=\sigma-1\) with \(d<q=2^n\), a chain \(De_j=e_{j-1}\) contributes the class of its top vector \(e_{d-1}\) to \(H^1(C_q,V)\) and the class of its bottom vector \(e_0\) to \(H^2(C_q,V)\).
- A length-\(q\) block contributes zero: its top vector is in \(\operatorname{im}D\), and its bottom vector is a norm \(D^{q-1}e_{q-1}\).
- Hence these short-block representatives give explicit bases, once Jordan chains are chosen. The arithmetic transgression still requires a concrete Galois extension, module, and invariant class; no Fold-specific transgression is claimed.

### G-10 — Cochain-level transgression computation
- For \(1\to N\to G\to Q\to1\), an invariant class \([\alpha]\in H^1(N,V)^Q\) is represented by a 1-cocycle on N.
- Extend its representative to a 1-cochain on G; the Hochschild–Serre construction chooses the extension so its coboundary descends to a 2-cocycle on Q with coefficients in \(V^N\). Its class is the transgression \(d_2([\alpha])\).
- In the cyclic characteristic-two case, reduce that class in \(\ker D/\operatorname{im}D^{q-1}\) and use G-9's short-block bottom vectors as coordinates.
- This gives an explicit computational procedure, not a Fold arithmetic example: a concrete extension, module, and invariant cocycle are still needed.

### G-11 — Cyclic cocycle-sum obstruction vector
- For a normalized inhomogeneous 2-cocycle \(\tau:C_q\times C_q\to W\), with multiplication convention \((w,g)(w',g')=(w+gw'+\tau(g,g'),gg')\), the extension class is represented in \(W^{C_q}/N_{C_q}W\) by \(w_\tau=\sum_{j=0}^{q-1}\tau(\sigma^j,\sigma)\).
- In characteristic two, check \(Dw_\tau=0\) and reduce modulo \(D^{q-1}W\); G-9 identifies the surviving coordinates as the bottom vectors of short Jordan blocks.
- This gives a direct test once the G-10 quotient cocycle is known. No Fold-specific arithmetic transgression has been evaluated.

### G-12 — Explicit cyclic quartic test case
- Constructs \(K=\mathbb F_2(s)\), \(L=K(u,w)\) with \(u^2+u=s\), \(w^2+w=u^3+u\), and generator \(\sigma(u)=u+1\), \(\sigma(w)=w+u+1\). The odd pole order of \(u^3+u\) proves the second Artin–Schreier step is nontrivial; \(\sigma^2(w)=w+1\), so the Galois group is cyclic of order four.
- For the additive regular module \(L\), the normal basis theorem gives projectivity and vanishing positive cohomology.
- For trivial coefficients \(\mathbb F_2\), \(D=0\) and norm \(D^3=0\), hence \(H^1=H^2=\mathbb F_2\).
- The nonzero target is not itself a nonzero transgression; an invariant class in \(H^1(G_L,\mathbb F_2)^{C_4}\) must still be constructed and evaluated.

### G-13 — cyclic octic lift and explicit nonzero transgression
- The G-12 cyclic quartic class in (W_2(K)/(F-1)W_2(K)) lifts through the surjection (W_3(K)/(F-1)\twoheadrightarrow W_2(K)/(F-1)). The lifted character modulo eight must have order eight because its reduction modulo four has order four. Hence the given quartic field is the quartic subfield of a cyclic octic extension.
- For (1\to C_2\to C_8\to C_4\to1) with trivial coefficients (mathbb F_2), the restriction (H^1(C_8,mathbb F_2)\to H^1(C_2,mathbb F_2)) is zero. Five-term exactness forces the transgression (H^1(C_2,mathbb F_2)^{C_4}\to H^2(C_4,mathbb F_2)) to be injective, hence an isomorphism between one-dimensional spaces.
- This is a proved finite-group example of a nonzero transgression. Still open: an explicit third Witt coordinate/equation for the octic field, and a Fold-specific Galois module realizing the same obstruction.

### G-14 — explicit cyclic-octic equations
- The G-12 quartic tower is the length-two ASW class \((s,s)\), since \((F-1)(u,w)=(u^2+u,w^2+w+u^3+u^2)\).
- Its length-three lift \((s,s,0)\) gives
  \[
  u^2+u=s,\quad w^2+w=u^3+u,\quad
  v^2+v=u^7+u^4+u^3w^2+u^3w+u^2w^2+u^2w+w^3+w^2.
  \]
- Translation by \((1,0,0)\in W_3(\mathbb F_2)\) gives the order-eight generator \(\sigma(u)=u+1,\ \sigma(w)=w+u,\ \sigma(v)=v+u^3+uw+u\). Its square sends \((u,w,v)\) to \((u,w+1,v+w)\), and its fourth power sends \(v\) to \(v+1\).
- This closes the explicit-equation gap in G-13. The transgression is nonzero by the five-term argument already recorded there; connecting it to a Fold-specific Galois module remains open.

### G-15 — explicit cyclic factor set
- For (C_8\twoheadrightarrow C_4), with section (s(i)=g^i), (0\le i<4), the normalized factor set is (\tau(i,j)=\lfloor(i+j)/4\rfloor\bmod2).
- The G-11 cyclic sum is (w_\tau=\sum_{j=0}^3\tau(j,1)=1). With trivial (\mathbb F_2)-coefficients, the norm is zero, so this represents the nonzero generator of (H^2(C_4,\mathbb F_2)).
- This identifies the explicit G-13 transgression with the G-11 cocycle-sum obstruction. Still open: a Fold-specific Galois module and arithmetic class.

### G-16 — uniform cyclic (2)-power transgression family
- For every (r\ge1), the extension (1\to C_{2^r}\to C_{2^{r+2}}\to C_4\to1) has an isomorphism transgression (H^1(C_{2^r},\mathbb F_2)^{C_4}\xrightarrow{\sim}H^2(C_4,\mathbb F_2)) for trivial coefficients.
- Proof: both groups are one-dimensional; restriction from (H^1(C_{2^{r+2}})) to (H^1(C_{2^r})) is zero since the subgroup generator is the fourth power of the ambient generator; five-term exactness gives injectivity.
- Pushing the extension factor set through the nonzero character (C_{2^r}\to\mathbb F_2) gives (\tau(i,j)=\lfloor(i+j)/4\rfloor\bmod2), with cyclic sum 1. This is uniform in (r).
- The finite-group theorem is proved. Its arithmetic realization by explicit length-((r+2)) Witt vectors and its Fold-specific interpretation remain open.

### G-17 — arithmetic realization in every Witt length
- For every (n\ge2), the vector ((s,s,0,\ldots,0)\in W_n(\mathbb F_2(s))) defines a cyclic extension of degree (2^n): its first coordinate (s) is not (x^2+x), as its pole order at infinity is odd.
- Its length-two truncation is the G-12 quartic class. Therefore every G-16 extension sequence is realized over the same field (\mathbb F_2(s)).
- This uses the ASW degree criterion (Pop, *The Oort Conjecture on lifting covers of curves*, Fact 2.1(1)). The Witt equation specifies all higher levels exactly; expanded coordinate polynomials beyond length three and a Fold-specific interpretation remain open.


### G-18 — arbitrary cyclic 2-power quotient transgression
**Status: proved (abstract group cohomology) and explicitly arithmetic-realized.** For all r,m≥1, the extension \(1\to C_{2^r}\to C_{2^{r+m}}\to C_{2^m}\to1\), with trivial \(\mathbb F_2\)-coefficients, has an isomorphism transgression \(H^1(C_{2^r},\mathbb F_2)^{C_{2^m}}\to H^2(C_{2^m},\mathbb F_2)\). The restriction map from the middle group is zero because the kernel generator is \(g^{2^m}\); five-term exactness proves injectivity, and both spaces are one-dimensional. The factor-set representative \(\tau(i,j)=\lfloor(i+j)/2^m\rfloor\bmod2\) has cyclic sum 1. Every pair (r,m) is realized over \(K=\mathbb F_2(s)\) by the length-(r+m) Witt vector \((s,s,0,\ldots,0)\), with the quotient field the unique degree-\(2^m\) intermediate field. This remains a finite-group/arithmetic model, not yet a Fold-specific Galois construction. Full proof and conventions: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).

### G-19 — transgression equals the pushout extension class
**Status: proved.** For an extension with abelian kernel N, a G-module A on which N acts trivially, and a Q-equivariant homomorphism \(\chi:N\to A\), the Hochschild–Serre transgression of \([\chi]\) is represented, up to the factor-set sign convention, by \(\chi\circ\omega\), where \(\omega(q_1,q_2)=s(q_1)s(q_2)s(q_1q_2)^{-1}\). This is precisely the factor set of the pushout extension along \(\chi\). Therefore transgression vanishes exactly when that pushout splits, equivalently when \\(\\chi\\) extends to a 1-cocycle on G. Applied to G-18, \(\chi(k)=1\) sends the cyclic carry factor set to \(\lfloor(i+j)/2^m\rfloor\bmod2\), whose cyclic sum is 1. This supplies a direct extension-class interpretation of the nonzero transgression. No Fold-derived extension or character has been constructed; the Fold bridge remains open. Full proof and reference: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-20 — transgression for arbitrary quotient modules
**Status: proved.** For \(1\to C_{2^r}\to C_{2^{r+m}}\to Q=C_{2^m}\to1\) and any \(\mathbb F_2[Q]\)-module A inflated to the middle group, identify \(H^1(C_{2^r},A)^Q\) with \(A^Q=\ker D\), where D=σ−1. The transgression is the quotient map
\[
\ker D\longrightarrow\ker D/\operatorname{im}(D^{2^m-1})=H^2(Q,A),\quad a\mapsto[a].
\]
Thus it is surjective, with kernel exactly the norm image. In Jordan form it kills bottom vectors from full-length blocks and detects one class from every shorter block. This generalizes G-18 and makes the coefficient-module dependence explicit. It remains an abstract cyclic-group theorem, not a Fold-specific construction. Full proof: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-21 — explicit cyclic degree-16 Witt tower
- Expands the common Artin–Schreier–Witt class \((s,s,0,0)\in W_4(\mathbb F_2(s))\) into all four coordinate equations.
- Derives the fourth coordinate from the Witt ghost polynomials and gives the full generator translation by \((1,0,0,0)\), of exact order 16.
- The odd pole order of \(s\) proves the class has degree 16; its length-two and length-three truncations are exactly the quartic and octic fields of G-12 and G-14.
- This is an explicit arithmetic tower calculation. It does not supply a Fold-derived Galois representation or Selmer class.
- Full equations and derivation convention: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-22 — ramification filtration and genus of the degree-16 tower
- For the reduced local Witt vector \((t^{-1},t^{-1},0,0)\) at \(s=\infty\), the upper breaks are \((1,2,4,8)\).
- Herbrand conversion gives lower breaks \((1,3,11,43)\); the lower ramification group orders are \(16,8,4,2,1\) on the corresponding intervals.
- The different exponent is \(100\). The one-point global cover of \(\mathbb P^1_{\mathbb F_2}\) has genus \(35\) by Riemann–Hurwitz.
- The nontrivial character conductor exponents \(2,3,5,9\), with multiplicities \(1,2,4,8\), reproduce the different exponent \(100\).
- This completes ramification invariants of the explicit arithmetic model; no Fold-derived Galois representation or Selmer class is constructed.
- Full derivation and references: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-23 — geometric \(2\)-rank of the tower
- The Deuring–Shafarevich formula applied to each one-point totally ramified \(C_{2^n}\)-cover gives geometric \(2\)-rank zero for every \(1\le n\le4\).
- The genera are \(0,1,7,35\); in particular, the genus-one quartic intermediate curve is supersingular.
- This determines the \(2\)-rank only, not the Newton polygons or higher-genus Jacobian \(a\)-numbers.
- Proof and formula reference: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-24 — Frobenius polynomial of the quartic elliptic quotient
- Identifies the genus-one quartic intermediate curve as \(E:y^2+y=x^3+x\) over \(\mathbb F_2\).
- Directly counts \(\#E(\mathbb F_2)=5\), giving Frobenius trace \(-2\) and characteristic polynomial \(T^2+2T+2\).
- Since the trace is divisible by 2, E is supersingular; this independently checks the G-23 2-rank conclusion.
- This determines the elliptic quotient's Frobenius polynomial, not the higher-genus Jacobian Newton polygons or a Fold-derived Galois representation. Full calculation and reference: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-25 — exact Weil polynomial of the genus-seven octic curve
- Counts the points on the smooth projective genus-seven curve over \(\mathbb F_{2^m}\), for \(1\le m\le10\), by exact finite-field enumeration of the three Artin–Schreier coordinates and the unique point at infinity.
- The counts are \(9,9,9,9,49,105,121,177,513,1009\).
- Newton identities for the first seven counts and the Weil functional equation give
  \[
  P_C(T)=1+6T+20T^2+48T^3+90T^4+140T^5+196T^6+272T^7
  +392T^8+560T^9+720T^{10}+768T^{11}+640T^{12}+384T^{13}+128T^{14}.
  \]
- Counts for degrees 8–10 independently check the reconstructed polynomial. Exact reproducible script: `certificates/g24_genus7_weil_polynomial.py`.
- This determines the genus-seven Jacobian's Frobenius polynomial/isogeny class, but not its simple-factor decomposition or the genus-35 Jacobian. Derivation and Weil reference: [Galois applicability note](the-fold-automorphic-and-hopf-galois-applicability.md).


### G-26 — genus-seven Jacobian isogeny factors and Newton polygon
- Factors the G-25 Weil polynomial as \((1+2T^2)^2(1+2T+2T^2)Q(T)\), with the explicit degree-eight factor Q.
- The Jacobian is isogenous to the product of two copies of the trace-zero supersingular elliptic class, the G-24 trace-minus-two elliptic class, and a four-dimensional factor with polynomial Q. No simplicity claim is made for the latter.
- The exact 2-adic Newton polygon has vertices \((0,7),(4,4),(10,1),(14,0)\), giving slopes \(1/4\) (multiplicity 4), \(1/2\) (multiplicity 6), and \(3/4\) (multiplicity 4).
- Hence the Jacobian has p-rank zero but is not supersingular. Adds "certificates/g26_genus7_newton_polygon.py"; the genus-35 Jacobian remains open.


### G-27 — irreducible degree-eight factor
- Proves the reciprocal degree-eight Frobenius factor irreducible over Q.
- The Newton polygon forces any proper rational factor to have degree four. Weil-root absolute values bound a monic quartic divisor to 12,650 integer candidates; exact integer division excludes every candidate.
- The corresponding four-dimensional abelian isogeny factor is therefore simple over F2, with slopes 1/4 (four times) and 3/4 (four times).
- Adds the executed certificate "certificates/g27_degree8_irreducibility.py".


## G-33 — CM Artin character and prime splitting

The real quartic CM subfield has narrow class group C2, and its narrow Hilbert class field is the genus-seven simple factor's degree-eight Frobenius field. Because the unit-signature subgroup is exactly the even-parity subgroup, the Artin character of a principal prime ideal (alpha) is the parity of the real signs of alpha, equivalently the sign of its field norm. This predicts explicit relative splitting: 3 and 5 split over their inert degree-four primes; at 7 the two degree-one primes are inert and the degree-two prime splits. The corresponding degree-eight polynomial factorizations modulo 3, 5, and 7 are certified exactly. This is a concrete arithmetic consequence of the CM class-field identification; the CM field's own full class group remains open.


## G-34 — odd class number of the CM Frobenius field

For the degree-eight CM field L over its real quartic F, the ambiguous class number formula gives |Cl(L)^Gal(L/F)|=1: there are four ramified infinite places, no ramified finite places, h_F=1, and the norm-unit index is the order-eight totally-positive signature quotient. As h_F=1, conjugation acts on Cl(L) by inversion. Therefore Cl(L)[2]=0 and h_L is odd. At the G-34 stage its odd part remained undetermined; G-35A–G-35E below subsequently prove the class group is trivial.


### G-35A — relative integral basis of the degree-eight CM field
- Set \(\mathfrak p=(\beta+2)\), with \((2)=\mathfrak p^4\), \((\beta^2-8)=\mathfrak p^2\), and \(N(\beta+2)=2\).
- The rescaled element \(\theta=\pi/(\beta+2)\) satisfies the monic quadratic
  \[
  X^2-\frac{\beta}{\beta+2}X+\frac{2}{(\beta+2)^2}=0.
  \]
  Its coefficients are integral at \(\mathfrak p\) and elsewhere, so \(\theta\in\mathcal O_L\).
- Its relative polynomial discriminant is \((\beta^2-8)/(\beta+2)^2\), a unit. Since G-29 establishes that the relative field discriminant is also a unit, the relative index-discriminant identity gives
  \[
  \mathcal O_L=\mathcal O_F[\theta].
  \]
- This provides an exact relative integral basis for the Minkowski enumeration. The full absolute class group is determined in G-35E below.
- Derivation: [CM-field arithmetic note](the-fold-genus7-cm-field.md).


### G-35B — principal prime ideals above 2
- The G-35A integral-basis polynomial reduces modulo \(\mathfrak p=(\beta+2)\) to \(X(X-1)\), so the unique prime of the real quartic above 2 splits into two degree-one primes \(\mathfrak P_0,\mathfrak P_1\) in \(L\), each of absolute norm 2.
- The local valuations of \(\theta=\pi/(\beta+2)\) are 0 and 2, and \(N_{L/\mathbb Q}(\theta)=4\), hence \((\theta)=\mathfrak P_1^2\) after labeling.
- G-34 proves there is no 2-torsion in \(\operatorname{Cl}(L)\), so \(\mathfrak P_1\) is principal. The relation \((\beta+2)\mathcal O_L=\mathfrak P_0\mathfrak P_1\) then makes \(\mathfrak P_0\) principal too.
- This removes the norm-two primes from the Minkowski search; the exact class number is determined in G-35E below.


### G-35C — finite support of the remaining Minkowski classes
- The degree-eight Minkowski bound is less than 27.488.
- The inert primes 3 and 5 in the real quartic have prime-ideal norms 81 and 625. The known relative splitting at 7 gives prime-ideal norms 49 in the CM field. All primes above 2 are principal by G-35B.
- A prime ideal above any rational prime \(p\ge11\) with residue degree at least two has norm at least \(p^2>27\).
- Therefore the remaining Minkowski generators are degree-one prime ideals above exactly the candidate rational primes 11, 13, 17, 19, and 23. Their principality and relation are resolved explicitly in G-35E below.


### G-35D — cyclicity of the degree-eight CM class group
- Proves \(\theta=\pi/(\beta+2)\) is primitive over \(\mathbb Q\): equality of its rational function on two Frobenius conjugates forces either equality or a forbidden common root; the relevant resultant is \(2^{44}\).
- Its minimal polynomial is \(H=X^8-8X^7+26X^6-44X^5+53X^4-68X^3+64X^2-24X+4\), with discriminant \(2^{38}17^2\). Since \(\operatorname{disc}(L)=2^{16}17^2\), the index is \(2^{11}\).
- Exact modular factorizations at 11, 13, 17, 19, 23 show that only two prime ideals of norm 17 can occur in a Minkowski representative.
- The real-quartic prime above 17 is narrow-principal, generated by \((\beta+4)/(\beta+2)\) up to a totally positive unit, so it splits in the narrow Hilbert class field \(L/F\).
- The two norm-17 primes in \(L\) have principal product. Along with G-35B and the Minkowski bound, they generate the class group with one generator. Therefore \(\operatorname{Cl}(L)\) is cyclic of odd order.
- The G-35D stage leaves the cyclic order open; G-35E below proves it is one. Exact certificate: certificates/g35d_cm_minkowski_primes.py.


### G-35E — exact CM class number
- With \(q=\beta+2\), \(\theta=\pi/q\), define \(x=-1-\beta\), \(y=-4-3\beta+2\beta^2+\beta^3\), and \(\alpha=x+y\theta\).
- Exact reduction modulo \(g(\beta)\) verifies
  \[
  N_{L/F}(\alpha)=\frac{\beta+4}{\beta+2}(1+\beta).
  \]
- The right-hand side has absolute norm 17, so \((\alpha)\) is a prime ideal of norm 17. The other prime above 17 is principal because their product is generated by \((\beta+4)/(\beta+2)\).
- Combining with G-35D and the principal primes above 2 proves \(\operatorname{Cl}(L)=1\), hence \(h_L=1\).
- Exact certificate: certificates/g35e_cm_principal_generator.py.


### G-4i — intrinsic image quotient for the characteristic-two quaternion boundary
For \(k=\mathbb F_2(s,t)\), \(\lambda=s\), put \(K=k^2=\mathbb F_2(S,T)\), \(S=s^2,T=t^2\). If \([a]=\alpha s+\beta t+\gamma st\) in \(k/K\), set \(A=\alpha+T\beta^2+ST\gamma^2\). The G-4h kernel criterion identifies \(\ker\delta_s\) with the preimage of \(K^2+\{u+Su^2:u\in K\}\). The resulting surjective additive map induces
\[
\operatorname{im}(\delta_s)\cong K/(K^2+\{u+Su^2:u\in K\}).
\]
Every image class has a symbol representative \([AS,s)_2\). This is an exact quotient presentation; its dimension and an explicit basis remain open. The nonzero class \(\delta_s([t])\) corresponds to the coset of \(T\).


### G-4j — infinite-dimensional quaternion-boundary image
For \(K=\mathbb F_2(S,T)\), the quotient \(K/(K^2+\{u+Su^2:u\in K\})\) is infinite-dimensional over \(\mathbb F_2\). At the valuation \(T=\infty\), every denominator element with a pole has even pole order: the leading terms of \(z^2\) and \(Su^2\) cannot cancel because \(S\) is nonsquare in the residue field \(\mathbb F_2(S)\), and \(u\) has strictly smaller pole order than \(u^2\). Thus the classes of \(T^{2n+1}\), \(n\ge0\), are linearly independent. Via G-4i, the boundary image has infinite \(\mathbb F_2\)-dimension, with independent representatives \([ST^{2n+1},s)_2\). The quotient's full normal form remains open.


### G-4k — exact dimension of quaternion-boundary image
At every place \(v_{T-a}\), \(a\in\mathbb F_2(S)\), the residue field is \(\mathbb F_2(S)\) and S is nonsquare. Every denominator element \(z^2+u+Su^2\) therefore has either no pole or even pole order there. Hence the classes of \((T-a)^{-(2n+1)}\), for all \(a\in\mathbb F_2(S)\) and \(n\ge0\), are linearly independent in the G-4i quotient. Since K is countable, its quotient has at most countable dimension. Thus the quotient and \(\operatorname{im}(\delta_s)\) have exact dimension \(\aleph_0\). A canonical basis and reduction algorithm remain open.


### G-4l — separable-place refinement
For every monic separable irreducible P in F₂(S)[T], S remains nonsquare in its finite separable residue extension. Hence every element z²+u+Su² has no pole or even pole order at P. Choosing an F₂-basis of the residue field and polynomial lifts r(T), the classes r(T)/P^(2n+1) are jointly independent as P ranges over separable irreducibles and n≥0. This refines G-4k but is not a complete quotient basis.


### G-4m — exact local parity criterion
At an irreducible P with residue E=F₂(S)[T]/(P), all denominator poles are even exactly when S is nonsquare in E. If S is square, lift a root r, write r²+S=PC, and choose w with C̄w̄²+w̄≠0; then z=rw/P and u=w/P give z²+u+Su²=(Cw²+w)/P, a simple pole. Exceptional places are necessarily inseparable. Full local quotient structure remains open.


### G-4n — explicit exceptional place
At P=T²−S, the residue field is F₂(S)(√S), so S becomes square. The exact denominator identity, with u=S/P and z=TS/P, is z²+u+Su²=(S²+S)/P. Thus a genuine simple pole occurs. This is a witness to the exceptional inseparable behavior, not a proof that arbitrary simple principal parts are removable.


### G-4o — higher odd poles at the exceptional place
At P=T²+S, for every m≥1 and P-adic unit w, the denominator identity
z=Tw/P^(m+1), u=w/P^(m+1) gives
z²+u+Su²=(w²+wP^m)/P^(2m+1), with square leading coefficient w̄².
For m=0 the leading coefficient is instead w̄²+w̄ (Artin–Schreier).
Thus the simple-pole case must not be conflated with the higher odd-pole
family. Full local principal-part quotient remains open.


### G-4p — completed local coordinates at P=T²+S
In K_P=F₂(S)((P))[T], with T²=S+P, write z=x+Ty and u=r+Tq.
Then
z²+u+Su² =
(x²+(S+P)y²+r+Sr²+S(S+P)q²)+Tq.
This is an exact coordinate description of the completed local
denominator image. The T-coordinate q is free but couples quadratically
to the scalar coordinate. Computing the resulting scalar quotient
modulo the valuation ring, and relating local data globally, remain open.


### G-4q — coefficient filtration at the exceptional place
At P=T²+S, replacing X=x+Sq puts the completed scalar coordinate in the exact form A=X²+(S+P)y²+SPq²+r+Sr². Its coefficients satisfy [P^(2j)]A=X_j²+Sy_j²+r_(2j)+Sr_j² and [P^(2j+1)]A=y_j²+Sq_j²+r_(2j+1). For the square-only part, use F=F²⊕SF²: if c_(2j)=a_j+Sb_j and c_(2j+1)=e_j+Sd_j, membership is equivalent to b_j=e_j for every j. The full quotient remains open because r+Sr² couples indices j and 2j; the next task is its principal-part recurrence.


### G-4r — exact dimension of the exceptional completed local quotient
Let P=T²+S and K_P=F((P))[T], F=F₂(S), T²=S+P. For a zero-T-coordinate target, q=0. The two coefficient obstructions E_j=π_S(c_(2j))+π_0(c_(2j+1)) and D_j=π_S(c_(2j+1)) vanish on X²+(S+P)y². On r+Sr² they are E_j=π_S(r_(2j))+r_j²+π_0(r_(2j+1)) and D_j=π_S(r_(2j+1)). If j₀≤−2 is the lowest pair index of a principal part, a least-index argument forces r_n=0 for n<j₀, hence D_(j₀)=0. Therefore Sb/P^(2m+1), for b∈F² nonzero and m≥1, is not a local denominator class. Taking an F₂-basis of F² and all m≥1 gives a countably infinite independent family. Since F is countable, the completed local quotient K_P/(F[[P]][T]+{z²+u+Su²}) has exact F₂-dimension ℵ₀. This is a completed local theorem, not a global normal form.


### G-4s — explicit global family from the exceptional place
The local quotient obstruction at P=T²+S applies to rational global classes because K=F(T) embeds in K_P and every global denominator relation remains valid after completion. Taking b=S^(2n) in the G-4r family gives the explicit global independent family {S^(2n+1)/(T²+S)^(2m+1): n≥0, m≥1} in Q. For a finite relation, the largest m gives the lowest P-adic pair index, whose odd coefficient has nonzero S F² component. This complements the separable-place family; it is not a full global basis.


### G-4t — combined independent system over finite places
For every monic irreducible R with S nonsquare in E_R=F[T]/(R), odd-pole residue lifts \tilde e/R^(2m+1), with e in an F₂-basis of E_R and m≥0, are jointly independent by localization and the even-pole criterion. At each exceptional quadratic R_c=T²+Sc² (c∈F×), a modified coefficient obstruction gives the independent family S^(2n+1)/R_c^(2m+1), n≥0,m≥1. Localizing at each place proves the union of all these families is independent in Q. This covers all nonsquare-residue places and this explicit family of square-residue places, but not every possible exceptional irreducible or a full Hamel basis.


### G-4u.1 — higher-degree square-residue exceptional places
The irreducible quartic P=T⁴+T²+S over F₂(S) has residue field containing √S: if β²+β+S=0 and α²=β, then α has minimal polynomial P and (α+β)²=S. The exact P-adic coordinates of z²+u+Su² are recorded in the quaternion-boundary arithmetic note. Determine the local quotient at P, or construct an infinite independent family. The quadratic G-4r argument does not transfer verbatim because the T² coordinate introduces an additional coupled condition.


### G-4v — quartic exceptional odd-pole cancellation
At P=T⁴+T²+S, r=T²+T satisfies r²+S=P. Thus z=rw/P^(m+1), u=w/P^(m+1) gives z²+u+Su²=(w²+wP^m)/P^(2m+1). For P-unit w this has odd pole order 2m+1 and leading residue w̄²; the simple pole is obtained with m=0,w=T. Therefore odd pole order alone is not an obstruction at this exceptional place. The local quotient and the coupled T²-coordinate problem remain open.


### G-4w — quartic local two-coordinate reduction
For targets with integral T,T³ coordinates, the corresponding denominator parameters r₁,r₃ are integral. Writing A,B for scalar,T² coordinates and C=A+(p+S)B, the exact remaining equations modulo F[[p]] are C=x₀²+(p+S)x₁²+((p+S)x₃)²+r₀+Sr₀²+(p+S)r₂ and B=x₁²+x₂²+(p+1+S)x₃²+r₂+Sr₂². The first equation alone is unobstructed; the coupled pair is the remaining local problem.


### G-4x — erratum to the attempted quartic correction
The G-4w coefficient of x₃² was correct: it is (p+S)². The attempted G-4x correction to p+S was erroneous. The exact pair is C=x₀²+(p+S)x₁²+(p+S)²x₃²+r₀+Sr₀²+(p+S)r₂ and B=x₁²+x₂²+(p+1+S)x₃²+r₂+Sr₂² modulo F[[p]]. G-4y and G-4z are updated using this corrected coefficient. The quartic local quotient remains open.


### G-4y — quartic square-class criterion after elimination
Using the corrected G-4x equations, solve r₂=R=(C+x₀²+(p+S)x₁²+(p+S)²x₃²+r₀+Sr₀²)/(p+S). The target is represented iff there exist x₀,x₁,x₃,r₀ such that B+(p+1+S)x₃²+R+SR² lies in F((p))²+F[[p]]. This is exact but retains four existential parameters. The coefficient quotient has copies of F/F² at negative even exponents and F at negative odd exponents; these are coefficient slots, each countably infinite-dimensional over F₂.


### G-4z — coefficient recursion for the quartic local membership test
The square-class space H=F((p))/(F((p))²+F[[p]]) has odd negative coefficients in F and even negative coefficients in F/F². For the G-4y expression put q=S+p, U=C+x₀²+qx₁²+qx₃²+r₀+Sr₀², and R=q⁻¹U. Then R_n=S⁻¹(U_n+R_{n−1}), with U_n given by the parity-indexed coefficient formula in the arithmetic note. The residual E=B+(1+S)x₃²+px₃²+R+SR² has explicit coefficients there. Membership is equivalent to E_n=0 for negative odd n and E_n∈F² for negative even n. This is an exact infinite coefficient test, not yet a codimension computation.


### G-4aa — finite-slot dual obstruction
No nonzero F₂-linear functional supported on finitely many negative Laurent coefficient slots annihilates the local denominator image. Any separating dual certificate must have infinite slot support. This rules out finite-coordinate dual certificates but does not prove surjectivity or determine the quartic local quotient.


### G-4ab — infinite-support local dual annihilator
The exceptional completed principal-part quotient has a nonzero F₂-linear functional annihilating the full denominator image. Construct it recursively along exponents −1,−2,−4,… using the injective map (x\mapsto[Sx^2]\colon F\to F/F^2), extending functionals at each stage. This proves nontriviality independently of the principal-part family, but the functional is noncanonical and does not give a complete local quotient classification.


### G-4ac — exact local annihilator inverse system
The annihilator splits over odd-core doubling chains. On each chain, coefficient functionals satisfy \(\lambda_1\circ\phi=\lambda_0\) and \(\lambda_{j+1}\circ\phi=\lambda_j\circ q\) for j≥1, with \(q(x)=[x]\) and \(\phi(x)=[Sx^2]\). These are necessary and sufficient, and every extension exists since \(\phi\) is injective. The full annihilator has F₂-dimension continuum. The local quotient classification remains open.


### G-4ad — canonical chain-cokernel model
The local scalar quotient decomposes over odd-core exponent chains. Each chain is canonically \(\operatorname{coker}T_r\), with \(T_r((x_j))_0=x_0\) and \(T_r((x_j))_j=q(x_j)+\phi(x_{j-1})\), where \(q:F\to F/F^2\) and \(\phi(x)=[Sx^2]\). This is equivalently the colimit of the zigzag \(W_0\leftarrow F_0\to W_1\leftarrow F_1\to\cdots\). Dualizing yields G-4ac. Closed-form evaluation of the chain cokernels remains open.


### G-4ae — chain cokernel dimension
Each odd-core chain cokernel has countably infinite F₂-dimension. The target presentation is countable, while the dual surjects onto F* and therefore has continuum cardinality; this excludes finite dimension. All odd-core summands have identical presentations. This gives the dimension of each summand, not an explicit basis or normal form.


### G-4af — explicit independent chain family
For each odd r, the classes \([S^n p^{-r}]\), n≥0, are linearly independent in C_r. The zeroth-coordinate F embeds in coker(T_r): any nonzero finite-support input has nonzero output at one index beyond its last nonzero coordinate, by injectivity of phi. This gives a constructive countable lower bound for every chain. It does not yet give a spanning set or normal form.


### G-4ag — complete exceptional local normal form
The map \(\phi:F\to F/F^2\), \(x\mapsto[Sx^2]\), is bijective since \(F=F^2\oplus SF^2\). A finite backward recursion along each odd-core doubling chain reduces every principal part uniquely to the zeroth coordinate. Hence each chain cokernel is canonically F, with basis \([S^np^{-r}]\) for n≥0; the full local quotient has basis \(\{S^np^{-r}:n≥0, r\text{ odd positive}\}\). This supersedes the earlier statement that chain normal forms were open. Dual extensions in G-4ac are unique because phi is onto.


### G-4ah — correction to local chain scope
G-4ad–G-4ag classify the auxiliary quotient H₀ only. The full completed local quotient includes the additional square term \((S+p)F((p))^2\), because \((x+Ty)^2=x^2+(S+p)y^2\). Exact full quotient: \(F((p))/(F[[p]]+F((p))^2+(S+p)F((p))^2+\{r+Sr^2\})\). It is H₀ modulo the image of this extra term. The auxiliary basis is not yet a full local normal form. G-4r/G-4s remain the established full-quotient lower bounds.


### G-4ai — exact full local quotient presentation
With \(\tau=\phi^{-1}\circ q\), the full local quotient is the direct sum of odd-chain copies of F modulo relations \(e_{2m-1}(a^2)+e_{\operatorname{odd}(m)}(\tau^{v_2(m)}a)=0\), for m≥1 and a∈F. These encode the extra square term \((S+p)y^2\). This is an exact presentation, not yet a basis. G-4r/G-4s establish countably infinite dimension for the full quotient.


### G-4aj — complete full local normal form
The full local quotient is \(F/\wp(F)\oplus\bigoplus_{r\ge3,\ r\text{ odd}}SF^2\), where \(\wp(a)=a^2+a\). The chain-1 Artin–Schreier summand has basis \(1\), odd powers \(S^d\), and \(S^j/Q^d\) for monic irreducible Q, odd d≥1, 0≤j<deg Q. For each odd r≥3, use the basis \(S\mathcal E^2\) at p^{-r}, where \(\mathcal E\) is the standard partial-fraction basis of F consisting of S^d and S^j/Q^d for all Q,d≥1,0≤j<deg Q. This gives a complete explicit countable basis of the full local quotient.



### G-4ak — surface-level global comparison and characteristic-two residue bridge

The field \(K=\mathbb F_2(S,T)\) has transcendence degree two, so it is not a global field and the Albert–Brauer–Hasse–Noether exact sequence for number fields/one-variable function fields does not apply. The divisor \(P=(T^2+S)\) lies on the regular surface \(\operatorname{Spec}\mathbb F_2[S,T]\), with residue field \(\mathbb F_2(T)\) and residue relation \(S=T^2\). The full local quotient G-4aj remains proved, but it has not yet been identified with a characteristic-two Kato residue or a global localization kernel. The correct next step is to compute the Kato/logarithmic-Hodge–Witt residue of the quaternion symbol \([aS,S)_2\) at P, identify its relation (if any) to the G-4aj quotient and its filtration, then check codimension-two boundaries at closed points of P. Only then assemble the codimension-one residues over the surface. Do not use an ABHN parity argument for K. References for the distinction: Kato’s p-primary/Gersten framework and the characteristic-p logarithmic Hodge–Witt Kato complex; see the bibliography/search notes in the research conversation. Status: open bridge, not a theorem.



### G-4al — exceptional divisor has zero residue logarithmic differential

At P=(T²+S), the residue field is E=F₂(T) and \(\bar S=T²\), so \(d\log(\bar S)=0\) in \(\Omega^1_{E/\mathbb F_2}\). This does not imply the quaternion symbol is unramified or trivial; it shows that the ordinary residue-field logarithmic differential of the second symbol entry cannot by itself detect the local classes. Compute Kato filtration/refined Swan data for \([aS,S)_2\) on G-4aj normal-form representatives. Do not identify the local quotient with a Kato graded piece until this is proved. Status: concrete local calculation target.


### G-4am — differential representative of the exceptional quaternion symbol

At \(P=(T^2+S)\), put \(p=T^2+S\). Absolute differentials satisfy \(dp=dS\), hence \((aS)d\log S=a\,dp\). Under the characteristic-two differential-symbol description, \([aS,S)_2\) is represented locally by \(a\,dp\). This explains why the vanishing residue differential \(d\log\bar S\) does not settle the wild class: the pre-residue uniformizer differential survives. Exact representative identity proved; identification of the G-4aj quotient with Kato cohomology/filtration remains open. Next compute the quotient by exact differentials and Cartier/Frobenius, then compare its graded pieces with the G-4aj basis.


### G-4an — explicit characteristic-two Kato quotient at the exceptional completion

The change of coordinates \(p=T^2+S\) gives \(K_P=\mathbb F_2(T)((p))\), with 2-basis \(\{T,p\}\). Hence every coefficient has a unique four-term square decomposition. The characteristic-two differential presentation is \(H_2^2(K_P)=\operatorname{coker}(1-\gamma:\Omega^1\to\Omega^1/dK_P)\), with \(\gamma(hdT)=[h^2T dT]\) and \(\gamma(hdp)=[h^2p dp]\). Since \([aS,S)_2\) is represented by \(a dp\), its Kato class is now explicit in this quotient. Correction: Cartier C itself acts on closed forms/de Rham classes, not arbitrary 1-forms; use \(\gamma\) for the all-forms cokernel map. Remaining open bridge: determine exactly how \(\mathcal O_P+\mathcal D_P\) maps into this quotient, and whether the G-4aj additive quotient embeds, surjects, or neither.


### G-4ao — correction to the Kato differential presentation

The provisional G-4an quotient by exact forms and the raw relations \(h dT+h^2T dT\), \(h dp+h^2p dp\) omitted the higher Cartier filtration and is not the complete presentation. The correct characteristic-two formula is \(H_2^2(F)=\operatorname{coker}(\wp:\Omega_F^1/B_\infty\to\Omega_F^1/B_\infty)\), where \(\wp=C^{-1}-1\), \(B_1=dF\), and \(B_i\) is recursively the inverse image of \(C^{-1}(B_{i-1})\) modulo \(B_1\); set \(B_\infty=\bigcup_iB_i\). For \(F=K_P=\mathbb F_2(T)((p))\), \(C^{-1}(h dT)=[h^2T dT]\) and \(C^{-1}(h dp)=[h^2p dp]\) modulo exact forms. The symbol remains represented by \(a dp\). Source: Hiranouchi–Sugiyama (2025), §3.3, (3.4)–(3.5), Corollary 3.5. Open: compare the image of \(\mathcal O_P+\mathcal D_P\) with \(B_\infty\) and the Cartier-cokernel relations; no G-4aj/Kato isomorphism is claimed.


### G-4an — geometry-shaped proof architecture

Use the smooth divisor \(P=V(T^2+S)\) on \(X=\operatorname{Spec}\mathbb F_2[S,T]\) as the organizing object. Its conormal sequence has generator \(dp=dS\), since \(S=T^2\) and \(dS=0\) along P. The exceptional symbol differential is \(a\,dp\), so it is normal-direction data. Proposed route: (i) filter these forms by pole order along P; (ii) compute associated-graded Cartier/Frobenius and exact-differential relations; (iii) compare graded layers with the G-4aj Artin–Schreier chain-1 and odd-chain \(r\ge3\) normal form; (iv) check codimension-two boundaries at closed points of P. The conormal geometry is proved; the filtration/Kato identification and gluing are open. This is a proof strategy, not a theorem.
