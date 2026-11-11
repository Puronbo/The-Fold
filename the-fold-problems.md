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
| P vs NP | none | the Fold has no computational model |
| Poincaré (solved) | the return to the point | the theorem is about `π₁`, not the orbit space |

The rest of the note is the four zones, in order of how much they actually carry.

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
- **P vs NP.** No contact. The Fold has no notion of a computation, a certificate, or a circuit. The
  additive/multiplicative duality is not a complexity separation.

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

## The one sentence

**The Fold reformulates RH exactly and rhymes with a dozen other problems, but its real value is a
map: positivity needs a surface, Hilbert–Pólya needs an operator, de Bruijn–Newman needs a bound, and
the explicit formula needs a parity breaker — four known walls, one crease.**

## Files

`the-fold-problems.md` (this note). The crease and the functional equation are in
`the-fold-zeta.md`; the theta fold and the heat kernel are in `the-fold-theta.md`; the zero types and
the codimension/multiplicity distinction are in `the-fold-pipeline.md`; the signature and the
Poincaré–Hopf index are in `the-fold-signature.md`; the facet classification is in
`the-fold-facets.md`; the lookup is `the-fold-key.md`.
