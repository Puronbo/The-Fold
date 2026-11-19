# The theorem ledger

## The rule

A theorem has meaning in the Fold when **every premise** has an exact Fold object. The conclusion
rhyming is not enough, and the missing premise is the finding. Twelve theorems, each read against that
rule:

| # | theorem | the premise that decides it | Fold object | zone |
|---|---|---|---|---|
| 1 | Gauss–Bonnet | a metric with a cone point | the range cone, deficit `δ = 2π(1 − sin θ)` | exact |
| 2 | holonomy / period | an invariant `1`-form on a circle | the twist chart `k = e^{iθ}`, `ω = dk/k` | exact |
| 3 | Poincaré–Hopf | a vector field with isolated zeros | the height's gradient `∇h` | exact |
| 4 | Lefschetz | a `ℤ/2` acting on a surface | the fold `σ`, fixed set the crease | exact |
| 5 | Borsuk–Ulam | an involution with a quotient | `x ↦ −x`, orbit space `ℝPⁿ` | exact |
| 6 | Noether | an action invariant under the flow | `g_k` and `dk/k`; no action | reformulation |
| 7 | Euler homogeneity | a function homogeneous under scaling | `g_k` | exact |
| 8 | argument principle | a meromorphic `f` | the zero set and the winding | reformulation |
| 9 | Ward / anomaly | a fermion determinant | the index shape | reformulation |
| 10 | KMS | a state, a flow, a temperature | — | rhyme |
| 11 | Carnot | a cycle and two reservoirs | — | rhyme |
| 12 | optical theorem | an `S`-matrix with unitarity | — | rhyme |

Six close, three reformulate, three rhyme. The six are all boundary, index, orbit, or homogeneity
statements, which is the corpus's thesis arriving as a measurement rather than a claim.

## The six that close, with the number

**1. Gauss–Bonnet.** On the cone's lateral surface `ds² = dℓ² + ℓ² sin²θ dφ²`, the boundary circle at
slant `ℓ` has circumference `2πℓ sin θ` and geodesic curvature `1/ℓ`, so

```
∮ k_g ds = 2π sin θ ,      δ = 2π(1 − sin θ) ,      sum = 2π = 2πχ(disc) .
```

At `θ = 45°`: `4.4429 + 1.8403 = 6.2832`. No host: the metric is the Fold's.

**2. The period.** `ω = dk/k = dr/r + i dθ` on the twist chart, so on a circle `|k| = r` it is `i dθ`
and `∮_{|k|=r} ω = 2πi` for every `r`. This is a class in `H¹(S¹; ℤ)`, a **holonomy**, not a Chern
class: `c₁` would live in `H²`, and `H²` of a circle is zero. "First Chern class" is the false friend
here, and the exact word is period.

**3. Morse = Poincaré–Hopf.** Take `X = ∇h` for the Fold's own height. Then `ind(∇h, p) = (−1)^k` at a
critical point of index `k`, and

```
Σ (−1)^k = χ .      sphere: 1 + 1 = 2 ,      torus: 1 − 2 + 1 = 0 .
```

The missing premise of Poincaré–Hopf — a vector field — is supplied by the height, and the critical
points are the vertices of the crease network, where a degenerate one has `A_k` as its local model.
This is `the-fold-discriminant.md`'s `A_k` appearing as the index.

**4. Lefschetz, mod 2.** For an involution `σ` on a finite complex, `L(σ) ≡ χ(X) (mod 2)`, because
each eigenvalue is `±1` and `−1 ≡ +1` in `ℤ/2`, so every trace is the dimension. If `Fix` is a
subcomplex, `L(σ) = χ(Fix)`, hence

```
χ(Fix) ≡ χ(X) (mod 2) .
```

On a closed surface the quotient is a branched cover along the fixed set, and Riemann–Hurwitz gives

```
χ(M) = 2χ(M/σ) − χ(Fix)      ⇒      χ(Fix) ≡ χ(M) (mod 2) ,
```

with `χ(Fix)` the number of fixed points when they are isolated. Sphere: `0 ≡ 2`; torus: `0 ≡ 0`;
genus two: `6 ≡ −2`. The Fold's fixed set is a crease, so on the sphere it is a circle and the Euler
characteristic, not a count of points, is what enters.

The false friend is the integer equality `χ(Fix) = χ(M)`: the sphere's reflection has `0 ≠ 2`, and only
the congruence survives. The surface hypothesis is the premise that makes Riemann–Hurwitz available.

**5. Borsuk–Ulam.** `f(x) = f(−x)` for some `x` says an orbit of `x ↦ −x` lies in a level set of any map
to a lower-dimensional space. The Fold's `x ↦ −x` is that involution and `ℝPⁿ` is the quotient; on the
sphere model the height `h: S² → ℝ ⊂ ℝ²` therefore has an antipodal pair at equal height, and that pair
is the equator. The one-dimensional shadow is the fold at `c`: `h(n) = h(m)` with `n + m = 2c`.

**7. Euler homogeneity.** Differentiate `f(λx) = λ^a f(x)` at `λ = 1`: `x·∇f = a f`. The generator of
`g_k` has eigenvalue `a` at a homogeneous function, so the scaling action reads the degree. Exact, and it
is the arithmetic behind `the-fold-lean.md`'s `g_{ab} = g_a ∘ g_b`.

## The three that reformulate

**6. Noether, as the period.** For `X = k ∂_k` and `ω = dk/k`, `ι_X ω = k·(1/k) = 1`, `dω = 0`, and
`L_X ω = d ι_X ω = 0`. The conserved current is the constant `1`, and its integral over a cycle is the
winding number, so **the Fold's only conserved quantity is the degree.** But this is Cartan's formula
plus the period of item 2, not Noether's theorem: Noether derives the current from an action invariant
under the flow, and the Fold has no action. Missing premise: a Lagrangian. The exact residue is the
degree, and it is why every "charge" in this corpus is an integer count.

**8. Argument principle.** The Fold has the zero set, the hole, and the winding; it does not have a
meromorphic function whose zeros they are. So `ord = Res d log f` is a reformulation: it *defines* the
charge the rest of the corpus uses. Missing premise: an `f`. The exact residue is the counting, not the
theorem.

**9. Ward and the anomaly.** The anomaly is an index, so its shape transfers; the object needs a
fermion determinant and a measure. Missing premise: a determinant. Reformulation at best.

## The three that rhyme

**10. KMS.** Needs a state on an algebra, a flow, and a temperature. `μ = τ/p*` being a ratio survives
`g_k`, which is why a friction coefficient looks universal — but that is a fact about ratios, not a
theorem about ensembles.

**11. Carnot.** `1 − T_c/T_h` is a ratio of two energies and therefore `g_k`-invariant; the cycle and
the reservoirs are absent. Rhyme with an exact residue: universality from scale invariance.

**12. Optical theorem.** `Im f(0)` is a flux through a boundary, so the shape is right; unitarity needs
an `S`-matrix. Rhyme.

## What the ledger needed

The notes this ledger was asked to test, sorted by what they actually did here:

| note | role |
|---|---|
| `the-fold-sign.md` | **dependency**: the mod-2 coefficient and `w₁` are the reason items 2, 4 and 5 are exact |
| `the-fold-crease-network.md` | **dependency**: the claim that these are sums over zeros is what the ledger tests |
| `the-fold-discriminant.md` | **dependency**: `A_k` is the index at a degenerate zero (item 3) |
| `the-fold-friction.md` | **cited, not needed**: nothing in the twelve uses `τ`, `p*`, or the contact area; it was decoration for this purpose |
| `the-fold-agi.md` | not needed, and the criterion it proposes is what this note exercises |

That is the meter's answer, and it is not the flattering one: three dependencies, one decoration. The
friction note may yet earn its place — friction is a boundary statement and item 12 is the closest
neighbour — but it did not do so here, and the ledger is where that has to be said.

## The tally

`6 exact / 3 reformulation / 3 rhyme`, and the exact six are exactly the family the corpus predicted:
a boundary, a period, an index, a fixed-set congruence, an orbit quotient, and a homogeneity. Every one
is a statement that a **global number equals a local sum**. None is a statement about a bulk dynamics,
and that is why the other six fail.

The one sentence: the Fold's physics is the part of mathematics that reads a global number off a local
object, and the ledger says which theorems are already inside it.
