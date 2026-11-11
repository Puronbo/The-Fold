# P and NP

## The question

```
P  = ⋃_c DTIME(n^c)          NP = ⋃_c NTIME(n^c)
```

Equivalently, `L ∈ NP` iff there is a polynomial-time relation `R` and a polynomial `p` with

```
x ∈ L  ⇔  ∃w ( |w| ≤ p(|x|)  and  R(x, w) )
```

The question `P =? NP` is open, and the Fold does not decide it. The Fold has no computational model:
no machine, no circuit, no resource bound. What it does have is one exact **restatement** — a projection
and a section — three rhymes, and a precise **wall**. This note states all three and keeps them apart.

The verdict up front: the Fold can say where the question sits, and it can prove that its own invariants
cannot answer it. It cannot cross the wall, and a note that pretended otherwise would be the
false-friend error the problems note is written to avoid.

## The exact restatement: NP is a projection, a solver is a section

The verifier's relation `R ⊆ X × W` projects onto the decision set:

```
π_X : R → X,     (x, w) ↦ x
```

`x` is in the language iff the fiber `π_X^{-1}(x)` is nonempty. A **solver** is a polynomial-time
section of that projection:

```
S : X → W,     π_X(S(x)) = x,     defined whenever the fiber is nonempty
```

So the question has an exact form:

> **`P = NP` iff every polynomial-time projection arising from a verifier has a polynomial-time
> section.**

This is standard, and it is the sharpest contact the Fold has. The Fold's projection is the linear
model of the same diagram:

```
π_H = ½(I + σ_H),     ker π_H = the normal line,     im π_H = the crease H
```

The witness is the normal coordinate `s`; the instance is the crease coordinate `h`; the section is a
choice of `s` for each `h`. In linear algebra a section always exists (take the orthogonal
complement), so the diagram is **always split**:

| check | value |
|---|---|
| `‖π_H² − π_H‖` | `≤ 1.1e−16` |
| `‖π_H n‖` for the normal `n` | `≤ 1.3e−16` |
| `‖π_H h − h‖` for `h ⊥ n` | `≤ 2.3e−16` |
| `rank π_H` | `n − 1` |

This is the exact contact **and** the exact limit. The shape — projection, fiber, section — is the
Fold's. The object is not: the verifier is a Boolean relation, not a linear map. And the linear
projection is always split, so the geometry predicts no obstruction. If `P ≠ NP`, the hardness is the
**cost** of the section, not its existence. That is precisely what the Fold cannot see. The linear
section is free; the combinatorial one is the search.

In the height note's language, the witness is the transverse height over the crease and a solver is a
height function `h ↦ s(h)`; the open question is the **cost** of that function. See
`the-fold-crease-height.md`.

This is why the problems note's "the Fold has no computational model" is right. The projection is a
picture of the logic, not a model of the computation.

## Rhyme 1: the two ledgers

P is closed under sequential composition: running two polynomial algorithms one after the other adds
their times. NP is closed under existential branching: a witness of length `n^c` multiplies the search
space by `2^{n^c}`. The Fold's mixed law is the same shape:

| | P | NP | Fold |
|---|---|---|---|
| closure | sequential composition | existential branching | folds add; scales multiply |
| cost | a sum of stage times | a product of branch counts | `1 + 1 = 2`; `ab` |
| object | a morphism | a projection with a witness | the crease; the normal |

So `P = NP` reads: **can the multiplicative search ledger be absorbed into the additive time ledger?**
That is a restatement of "can nondeterminism be simulated deterministically with polynomial overhead,"
not a proof of it. The Fold's `1_a + 1_b = 2_{ab}` is the template — count adds, parameter multiplies —
and the question is whether the parameter's product can be paid for by the count's sum. Nothing in the
Fold forces either answer. See `the-fold-composition.md`.

## Rhyme 2: the one-way horizon

Verification is easy in one direction: witness → bit. Search is the other direction: bit → witness. The
Fold has exactly one one-way surface, the horizon, where the normal is null and timelike curves cross one
way. The fold itself is reversible (`σ_H² = I`), the twist is periodic (`J⁴ = I`), and the scale is
invertible (`k ≠ 0`). So the horizon is the model's only arrow.

The rhyme is real and it stops immediately: the horizon's arrow is a **signature**, `n·n = 0`, not a
resource bound. A null crease is one-way for every observer and every clock; a verifier is one-way for a
polynomial-time observer, and only a guess makes the return trip. Same picture, different obstruction.
See `the-fold-occlusion.md` and `the-fold-horizon.md`.

## Rhyme 3: the alternating ledger

`NP` is the first existential level; the polynomial hierarchy is the alternation `∃∀∃…`; `P = NP` asks
whether the **first** alternation collapses. The Fold's ledger alternates `0 → 1 → 0 → 1`, and the key
note asks how the terms can all be new. There the alternation is geometric — distinct creases and
normals — while here it is logical — distinct quantifiers. The shapes rhyme; the objects do not. In the
scale ledger the one is unique (`k = 1`), so that ledger cannot supply the alternation at all; only the
fold ledger can, and its alternation is spatial, a matter of creases rather than quantifiers. See
`the-fold-key.md`.

## The wall: why the Fold's invariants cannot separate the classes

Three barriers, in increasing strength:

1. **A polynomial-time invariant collapses, it does not separate.** The Fold's invariants — `det`,
   inertia, signature, the parameter `k`, the crease — are computed in polynomial time from the input. If
   one of them separated an `NP`-complete language `L` from its complement — if its value told membership
   in `L` — then it would be a polynomial-time decision procedure for `L`, so `L ∈ P`, so `P = NP`. A
   poly-time invariant can therefore only **prove equality**, never inequality. This is the sharpest
   statement of the wall, and it is internal to the Fold: every invariant it owns is a polynomial-time
   computation, an upper bound and not a lower bound.

2. **Relativization.** The Fold's constructions are oracle-independent linear algebra over the input.
   Any separation proved from them would hold relative to every oracle. Baker–Gill–Solovay give oracles
   `A, B` with `P^A = NP^A` and `P^B ≠ NP^B`, so no relativizing proof exists. The Fold's toolkit
   relativizes, so it cannot separate.

3. **Natural proofs.** The invariants are constructive — checkable in polynomial time. If they are also
   *large* (the usual case for a property defined by a generic geometric condition), then Razborov–Rudich
   applies: assuming strong one-way functions, no natural proof can prove strong circuit lower bounds.

The missing object is therefore a **lower bound that is not itself a polynomial-time invariant** — a
proof that no section exists, not an invariant that computes one. That is the same shape as the
problems note's four missing objects — a surface, an operator, a bound, a parity breaker: in each case
the Fold supplies the dictionary and not the object. The Fold maps the wall; it does not cross it.

## The correction to the problems note

The problems note's original verdict was `P vs NP | none | the Fold has no computational model`, and
Zone 3 said "No contact." The second half is right: there is no model and no resolution. But "none" was
too strong about **description**, so the row and the bullet are corrected at the source to point here:

- **exact:** the logical form of `NP` is an existential projection, and a solver is a section; that is
  the Fold's projection/section diagram with a Boolean relation in place of a linear map.
- **rhyme:** the two ledgers (additive time, multiplicative search), the one-way horizon, the alternating
  ledger.
- **wall:** every polynomial-time invariant collapses the classes rather than separating them; the toolkit
  relativizes and is natural.

So the correct label is **reformulation and rhyme, no lower bound** — not "none." The row and the Zone 3
bullet are corrected at the source in `the-fold-problems.md`.

## Checks

The SAT table counts operations, not seconds: verification of a claimed assignment is `m` clause checks;
brute force is `2ⁿ` assignments times `m`. Random 3-SAT at clause density `4.3` is above the
satisfiability threshold, so most instances are unsatisfiable and the solver must exhaust the space —
which is the point. A purported witness is still checked in linear time. The step counts are exact; the
last column is one wall-clock run.

| `n` | `m` | satisfying | verify | brute force | ratio | time |
|---|---|---|---|---|---|---|
| 8 | 34 | 5 | 34 | 8704 | 256 | 0.001 s |
| 10 | 43 | 4 | 43 | 44032 | 1024 | 0.000 s |
| 12 | 52 | 13 | 52 | 212992 | 4096 | 0.001 s |
| 14 | 60 | 0 | 60 | 983040 | 16384 | 0.007 s |
| 16 | 69 | 0 | 69 | 4521984 | 65536 | 0.032 s |
| 18 | 77 | 0 | 77 | 20185088 | 262144 | 0.284 s |

Each `+2` variables multiplies the ratio by `4`: the `2ⁿ` factor. The measured slope of
`log₂(brute force)` against `n` is `1.12`, consistent with `2ⁿ` times the linear clause count. The
verifier's step count grows only as `m`.

The additive-versus-multiplicative gap is the same table in closed form:

| `n` | `n³` | `2ⁿ` | ratio |
|---|---|---|---|
| 10 | 1000 | 1024 | 1.02 |
| 20 | 8000 | 1048576 | 131 |
| 30 | 27000 | 1.07e9 | 3.98e4 |
| 40 | 64000 | 1.10e12 | 1.72e7 |
| 50 | 125000 | 1.13e15 | 9.01e9 |

The linear projection checks are in the first table: `π² = π`, `π` kills the normal, fixes the crease,
and has rank `n−1`. It is always split — which is the geometric fact that makes the complexity question
invisible to the geometry.

## What this does and does not say

- It **does** give the exact logical form: `NP` is a projection, a solver is a section, `P = NP` is the
  existence of polynomial-time sections.
- It **does** identify the Fold's projection as the linear model of that diagram — and shows why the
  linear model is always split, so the hardness is cost, not existence.
- It **does** state the three rhymes: the two ledgers, the one-way horizon, the alternating ledger.
- It **does** prove the wall for the Fold's own invariants: a polynomial-time invariant collapses rather
  than separates; the toolkit relativizes, and the invariants are constructive, so the natural-proofs
  barrier applies if they are also large.
- It **does not** resolve `P vs NP`; it gives no lower bound and no computational model.
- It **does not** turn the linear projection into a verifier; the verifier is a Boolean relation, and the
  analogy is one of diagram, not of object.
- It **does not** claim the Fold's invariants separate the classes; they can only collapse them.
- It **does not** use the zeta or theta machinery; `P vs NP` is not a crease problem.

## The one sentence

**The Fold cannot decide P versus NP — it has no computational model — but it can say exactly where
the question sits: NP is an existential projection and a solver is a section, P is the additive ledger
and NP the multiplicative one, verification is the outward crossing of the one-way horizon, and every
invariant the Fold can compute is polynomial-time, so it can map the wall but never cross it.**

## Files

`the-fold-complexity.md` (this note). The four open-problem zones and the original "no contact" verdict
are in `the-fold-problems.md`; the mixed law and the two ledgers are in `the-fold-composition.md`; the
one-way horizon and the side-blind crease are in `the-fold-horizon.md` and `the-fold-occlusion.md`; the
alternating ledger and the unique one are in `the-fold-key.md`; the projection `π_H` is in
`the-fold-occlusion.md`, and the orbit space and universal constructions are in
`the-fold-categorical.md`.
