# The sign: every two in the corpus

## One operation

The notes call the involution by many names — `σ`, `F`, `J`, `z ↦ 1 − z`, `A ↔ B`, `K ↔ K′`,
`E ↦ −E`, `n ↦ −n`, `c ↦ −c`. In every case it is the sign of one real coordinate, and in every case
the same three objects come with it:

```
x ↦ −x        the fold
|x|           the quotient
x = 0         the crease
```

Nothing else is needed. A fold is a real line with a marked zero, and the involution that reflects it.

## Every two, sorted by its fixed set

| register | involution | fixed set | quotient | zone |
|---|---|---|---|---|
| the normal at a crease | `s ↦ −s` | `s = 0`, the plane `H_{n,c}` | `\|s\|`, the distance | exact |
| the crease moduli | `(n, c) ↦ (−n, −c)` | empty | `M`, the open Möbius band | exact |
| the direction | `n ↦ −n` | empty | `ℝP¹` | exact |
| the cone's aperture | `z ↦ 1 − z`, `z = sin²(θ/2)` | `z = 1/2`, `θ = 90°` | `z(1 − z)` | exact as a chart change |
| the honeycomb | `A ↔ B`, `K ↔ K′` | empty | the two cosets | exact in the toy |
| the Dirac bands | `E ↦ −E` | `E = 0` | `E²` | exact in the toy |
| the director | `n ↦ −n` | empty | `ℝP¹` | exact |
| the logistic map | `z ↦ 1 − z` | `z = 1/2` | `z(1 − z)` | exact at `r = 4`; a rhyme elsewhere |

The middle two columns do the work, and they give the sorting rule:

> **a fold with a fixed point is a crease; a fold without one is a holonomy.**

Both are `ℤ/2`. The first is a quotient of a space and has a boundary; the second is a class in
`H¹(base; ℤ/2)` and has a monodromy. Calling them "the same fold" is the false friend; calling them
"the same group over different bases" is exact. Every disagreement in the corpus about the number two
is a disagreement about which of these two columns is being read.

## The gap is twice the height

The honeycomb toy of `the-fold-hexagon.md` is the clearest instance, and it is a Fold written
spectrally. With `h = v(q_x σ_x + q_y σ_y) + m σ_z`,

```
h² = (v²q² + m²) I ,      E = ±√(v²q² + m²) ,      tr h = 0 .
```

So `m` is an **offset**, `|m|` is a **height**, and the two bands are the two signs. Everything lines
up with the three objects:

| Fold object | spectral name |
|---|---|
| the height | `m`, the Semenoff offset |
| the two layers | the two bands `E = ±…` |
| the crease `m = 0` | the Dirac point, where the bands touch |
| the gap | `2\|m\|`, twice the height |

The `2` in `2|m|` is the same `2` as the two layers: the gap is the distance between the two signs of
the same height, so it must be `2|h|`. And `E ↦ −E` is the particle–hole involution, whose fixed set
`E = 0` is the crease again.

The zones, kept apart: "the gap is `2|m|`" is exact inside the toy; "the mass is the height of the
crease above zero" is a reformulation within the host; "the mass is the corrugation, or the
curvature" is a false friend — the strain enters as `q → q − A`, which shifts the cone and leaves the
gap closed, while `m` opens it. The Fold supplies the double-valuedness and nothing else: no `H`, no
`t`, no Hilbert space.

## The sign over a base

Pointwise, the fold needs no base. A *global* sign does, and the obstruction is the first
Stiefel–Whitney class of the height line:

| total space | `w₁` | global sign | going once around |
|---|---|---|---|
| `S¹ × ℝ` (oriented creases, the annulus) | `0` | exists | `c ↦ c` |
| the Möbius band (unoriented creases) | `1` | does not exist | `c ↦ −c` |

`2w₁ = 0` on any base, which is why two turns return the height; that is the fold's `2` as a
cohomology relation rather than a count. Exact.

The false friend is "the fold is `w₁`". The fold is a fiber involution and is defined on a point;
`w₁` is the obstruction to patching those involutions over a base. Naming the base is the premise,
and without it the sentence has no truth value — which is the same failure as `the-fold-problems.md`'s
mass gap, where the operator was missing and the conclusion was borrowed.

This is also why the sign is the smallest member of the only family of theorems the corpus transfers
exactly. `w₁` is a mod-2 degree, and a mod-2 degree counts crease crossings mod 2 — the same
boundary/index shape as `∫K dA = δ` on the cone, `∮ d log f = 2πi Σ orders`, and `∮ω = 2πi` on the
punctured plane. Boundary statements close; bulk statements need a host.

## The hexagon has two signs, not one

The earlier notes say "`D₆/D₃ ≅ ℤ/2`" and stop, as if the hexagon had one sign label. It has two,
and they are independent. The characters of the dihedral group are the homomorphisms

```
χ : D_m → ℤ/2 ,      χ(r^k s^j) = (−1)^{ak + bj} ,      a, b ∈ {0, 1} ,
```

and the relation `s r s = r⁻¹` forces `(−1)^a = (−1)^{−a}`, which is automatic, while `r^m = 1`
forces `(−1)^{am} = 1`, i.e. **`a` may be `1` only when `m` is even**. Counting:

| `m` | order | characters | nontrivial index-2 subgroups |
|---|---|---|---|
| 3 | 6 | 2 | 1 |
| 4 | 8 | 4 | 3 |
| 5 | 10 | 2 | 1 |
| 6 | 12 | 4 | 3 |
| 7 | 14 | 2 | 1 |
| 8 | 16 | 4 | 3 |

For even `m`, `Hom(D_m, ℤ/2) ≅ (ℤ/2)²` and the three nontrivial subgroups are always the same three:

| `(a, b)` | kernel | reading |
|---|---|---|
| `(0, 1)` | `⟨r⟩` | rotation versus reflection — the determinant, the fold's bit |
| `(1, 0)` | `⟨r², s⟩` | 60° rotation flips it, reflection does not — the sublattice/valley bit |
| `(1, 1)` | `⟨r², rs⟩` | the product of the two bits |

So "one `ℤ/2`, two readings" was one bit short. The two readings are **not alternatives**, they are
independent coordinates on the same group: the fold's reflection sign and the sublattice sign can be
chosen separately, and that is exactly why a host can carry both without identifying them. The
`D₆/D₃` coset is the second character, `(1, 0)`; the fold is the first, `(0, 1)`; and identifying
them is the false friend, now with a reason rather than a warning.

The lattice consequence is exact and short: **a sublattice sign exists if and only if `m` is even.**
The crystallographic restriction ends at `m = 6`, so the hexagon is the **last lattice on which two
independent sign labels exist**. A triangular (`D₃`) lattice has only the determinant; the first
second sign is at `m = 4`; the last is at `m = 6`. Whether graphene is the physical realisation of
that is a host statement and a rhyme — the group theory is the part that closes.

## The whole corpus in one diagram

```
                    height h
                       │
              h ↦ −h   │   the fold  (one involution)
                       │
                     |h|          the quotient  (layer-blind)
                       │
        sign of h over a base  →  w₁ ∈ H¹(base; ℤ/2)
                       │
        sign of a group       →  χ ∈ Hom(D_m; ℤ/2)
```

Every note supplies a base or a group for one of these arrows. Which is which:

| note | what it supplies |
|---|---|
| `the-fold-crease-height.md` | the height line and its zero section |
| `the-fold-composition.md` | `σ` versus `F`, and stacking versus splitting |
| `the-fold-cone.md` | the aperture chart `z = sin²(θ/2)`, where `θ ↦ π − θ` is `z ↦ 1 − z` |
| `the-fold-hexagon.md` | the lattice: `D₆`, the `(ℤ/2)²` of characters, the hosted gap |
| `the-fold-afar.md` | `ℝP¹` as a base, and the director's double cover |
| `the-fold-midpoint.md` | `k = 0` as a place, not a medium |
| `the-fold-problems.md` | the missing premise, named theorem by theorem |
| `the-fold-invariants.md` | what survives the sign and the scale |

The bases are different — a point, a circle, a group, a Brillouin zone — and the coefficient group is
always `ℤ/2`. That is the cleanest form of the corpus's oldest sentence: same group, different bundle.

## What does not fold in

The sign is exact because it is a coordinate and an involution. Words that need more than that do not
enter by rhyming:

| word | nearest object | missing |
|---|---|---|
| time | the height | a flow |
| energy | the band sign `E ↦ −E` | a Hamiltonian |
| temperature | a ratio of rates in a host | a bath |
| entropy | `\|h\|` | a measure |
| charge | the `U(1)` class `∮ dk/k = 2πi` | a coupling |
| probability | the quotient `z(1 − z)` | a measure and a dynamics |
| vacuum | the zero section | a state space |

Each of these is a place where a conclusion can be made to rhyme and no premise can be found. They
are not refutations; they are the price list.

## The one sentence

Every `2` in the corpus is the involution `x ↦ −x`; what differs is whether its fixed set is a crease,
empty, or a subgroup — and the hexagon is the last lattice where the third kind can be independent of
the first.
