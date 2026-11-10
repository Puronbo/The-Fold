# The signature of zero

## The question

"Signature" in the strict sense is the inertia of a symmetric bilinear form: the triple
`(n₊, n₋, n₀)` of positive, negative and null directions (Sylvester's law). The scalar signature is
`n₊ − n₋`. The zero map has a linear part, and the form it defines is symmetric, so it has a
signature. The question is what it is, and whether it is the signature of nothing.

## The answer

The zero is not "signature 0" in the sense of a balanced form. It is totally null:

```
g₀ = 0          inertia (0, 0, n)          scalar signature 0          rank 0          nullity n
```

The scalar signature is `0`, but the scalar signature of a planar fold is also `0`. The scalar cannot
tell them apart. The full inertia can: the zero has **no signed directions at all**, while the planar
fold has one of each. The signature of nothing is the **nullity `n`**, not the number `0`.

One distinction matters here. The Fold's zero is not the empty set: it is the point at the centre,
and the linear part of the scale map at `k = 0` is the zero map. The collapsed **image** is a point and
has no tangent space. The **ambient** tangent space at the datum is `ℝⁿ`, and the linear part of
`g₀` is the zero map on it; the null form lives there. This is the
difference between the image's dimension (0) and the ambient dimension (n): the zero has no geometry
of its own, but it sits in an `n`-dimensional space whose directions survive. The empty set has no
tangent space and no `n`, so its signature is empty, not `(0,0,n)`. The Fold starts at the **point**,
not at the absence of a point. "Nothing" in the question is the Fold's zero, not the empty set.

## The signature ladder

| operator | matrix (linear part) | inertia | scalar signature | rank |
|---|---|---|---|---|
| zero `g₀` | `0` | `(0,0,n)` | `0` | `0` |
| fold `σ_H` | `I − 2nnᵀ` | `(n−1,1,0)` | `n−2` | `n` |
| identity `g₁` | `I` | `(n,0,0)` | `n` | `n` |
| point reflection `g_{−1}` | `−I` | `(0,n,0)` | `−n` | `n` |

The zero is the bottom in rank; the identity and the point reflection are the two full-rank ends;
the fold is the split in between.

In the plane the ambiguity is explicit:

| operator | inertia | scalar signature |
|---|---|---|
| zero | `(0,0,2)` | `0` |
| fold | `(1,1,0)` | `0` |
| identity | `(2,0,0)` | `2` |
| point reflection | `(0,2,0)` | `−2` |

The first two have the same scalar signature and different inertia. That is the cleanest proof that
"signature 0" is not enough: the zero is **all null**, the fold is **one plus, one minus**.

## Why the zero is forced

The scale family is `Q_k = k|·|²`, with matrix `kI`. For `k > 0` the inertia is `(n,0,0)`; for
`k < 0` it is `(0,n,0)`. Inertia is constant on the nondegenerate forms. Along any continuous path of
symmetric operators from `I` to `−I`, the ordered eigenvalues are continuous and the largest goes
from `1` to `−1`, so one must be `0` somewhere. In the Fold's family that point is exactly `k = 0`.

So the zero is not an optional stage: it is the **unique degeneracy** through which the signature can
change. If nothing had to be created first, this is why: a sign cannot be born from a nonzero form
without passing through a zero.

The fold is the exception that proves the rule. A reflection is not a path; it is a single discrete
jump. `σ_H` has inertia `(n−1,1,0)` and does not pass through the zero form. The fold ledger can
change sign without a temporal zero; the scale ledger cannot. That is the signature-level version of
the two ledgers.

## What survives inside the zero

The null form has no metric, but it is not featureless. The data that survive are:

- **the dimension `n`** — the number of null directions, the only invariant under the full
  similarity group;
- **the direction sphere `Sⁿ⁻¹`** — the rays that the zero can unfold into;
- **the tangent cone** — the local shape of the family at the datum;
- **the aperture `θ`** — at a cone vertex, `Ω/4π = 0.25` at `θ = 60°` at every zoom, while every
  dimensional measure vanishes.

So the zero has a shape but no size, a dimension but no metric, directions but no signs. That is the
precise content of "nothing is not empty."

Algebraically:

```
characteristic polynomial  λⁿ
minimal polynomial         λ
Jordan form                0 (semisimple)
trace                      0
determinant                0
```

The zero is the unique operator annihilated by `x`; its minimal polynomial is `λ`. Every other member
of the family has a minimal polynomial with a nonzero root: `x−1` for the identity, `x+1` for the
point reflection, `x²−1` for the fold. The zero is the only one whose spectrum is `{0}`.

Under the full similarity group with the datum fixed, the orbit space of `ℝⁿ ∖ {P₀}` is a point and
the invariant ring is constants. The zero is the unique fixed point, the 0-dimensional orbit, the
point with maximal stabilizer. So the only invariant signature of nothing is `n`.

## The signature of the fold

The fold is where a sign first appears. `σ_H` is symmetric with eigenvalues `+1` on the crease
(multiplicity `n−1`) and `−1` on the normal line (multiplicity `1`):

```
inertia  (n−1, 1, 0)          scalar signature  n − 2
crease    + eigenspace, dimension n − 1
normal    − eigenspace, dimension 1
```

Read as a quadratic form, the signed distance `f(P) = (P − P_H)·n` gives `f²`, whose inertia is
`(1,0,n−1)`: the normal is the one positive direction, the crease is the `n−1`-dimensional null
space. The two readings are dual:

```
reflection σ_H:   crease + , normal −      (n−1, 1, 0)
distance f²:      crease 0 , normal +      (1, 0, n−1)
```

In both, the one is one-dimensional and the zero is `n−1`-dimensional. "One is a split of zero" is
literal: the fold signs all `n` directions at once, `n−1` plus and one minus; the singled-out minus
direction is the "one," and the plus eigenspace is the crease. "Zero is the annihilation" is the
projection back: `½(I + σ_H) = π_H` kills the normal component and returns to the crease.

At `k = −1` the point reflection has inertia `(0,n,0)`, scalar `−n`: the fold ledger's zero and the
scale ledger's zero meet at the fully negative end.

## The ladder by stage

The signature is not only a property of the zero; it is a label on each stage. The exact rows are
0–4; the later rows are readings.

| stage | operator | signature / invariant | what it means |
|---|---|---|---|
| 0 point | `0` | `(0,0,n)` | totally null |
| 1 scale | `kI` | `(n,0,0)` for `k>0`; `(0,n,0)` for `k<0`; `(0,0,n)` at `k=0` | a signed magnitude |
| 2 fold | `σ_H` | `(n−1,1,0)` | the first split |
| 3 twist | `J` on a 2-plane, `J²=−I` | no symmetric inertia there; `Pf(ω)=1` | leaves the symmetric ladder |
| 4 closure | `D_m` | `m` discrete; the rotation's symmetric part is `cos(2π/m)` | quantizes the angle; the cosine sets the sign |
| 5 horizon | null normal | `(n−2,0,1)` induced in Lorentzian `(n−1,1,0)` | a null crease |
| 6 observer | `d`-form | `(d−1,1,0)` timelike; `(d,0,0)` spacelike; `(0,0,0)` for `d=0` | selects the form |
| 7 return | `0` | `(0,0,n)` | null again |

The exact content is the first five rows: the zero is null, the scale is definite, the fold is split,
the twist is symplectic, and the closure is a cosine. Read in order, the ladder's zeros are the zero
pipeline: a value, a vertex, a facet, a null, a point. See `the-fold-pipeline.md`. The twist is the
first stage that inertia cannot see: `J` is skew on its 2-plane, so its symmetric part is `0` there,
and the inertia on that plane is `(0,0,2)` — the same as the zero on a plane. But `J` is not zero; its
invariant is the Pfaffian `Pf(ω)=1`, where `ω(x,y)=⟨x,Jy⟩`. That is why the twist needs its own
invariant: it is the one stage whose operator has no inertia at all. The closure restores a cosine, so
the ladder has a single gap, and the twist occupies it. In higher dimensions the orthogonal complement
of the plane contributes `(n−2,0,0)` and is fixed.

The closure row has an exact cosine. A rotation by `2π/m` has symmetric part `cos(2π/m)` on its
plane. The crystallographic cases give `m = 2: −1`, `m = 3: −½`, `m = 4: 0`, `m = 6: ½`. The 4-fold
closure is the unique signature-zero closure; the 2-fold is the point reflection; the 3- and 6-fold
are definite. The lattice is positive definite in the plane; the closure's signature is the cosine of
its angle.

The later rows are readings, not derivations. In a Lorentzian extension the ambient signature is
`(n−1,1,0)` — here `n` is the spacetime dimension; the Fold's spatial `n` would give `(n,1,0)`. A
horizon is a null hypersurface, `n·n=0`, so the induced form is degenerate, `(n−2,0,1)`. The
orthogonal fold requires `n·n=±1`; at the horizon the fold degenerates. The Fold's `k*` is the scalar
ratio at which the radial normal becomes null. That is the signature reading of the paper's "the
surface becomes null."

## The observer's star

A `d`-dimensional observer measures a `d`-form. The Hodge star on an `n`-dimensional space with `s`
negative directions obeys

```
⋆² = (−1)^{d(n−d)+s}
```

In the Lorentzian reading `s = 1`. In four dimensions the exponent `d(4−d)+1` has the parity of
`d+1`, so `⋆² = (−1)^{d+1}` on `d`-forms: a 1-form (gradient) and a 3-form (density) square to `+1`,
while a 0-form (scalar), a 2-form (flux) and a 4-form (volume) square to `−1`. The observer's
dimension `d` selects the form; the signature selects the star's square. This is the footprint of the
signature on measurement, and it is exact.

## The division thresholds

Every division point gives its own collapse value `k_t = 1 − 1/t`. Write the factor as

```
q_t = (1 − t + tk)P = t(k − k_t)P
```

For `0 < t < 1`, the sign of the factor is the sign of `k − k_t`. So the inertia of `q_t` is

| range | factor | inertia |
|---|---|---|
| `k > k_t` | `+` | `(n,0,0)` |
| `k = k_t` | `0` | `(0,0,n)` |
| `k < k_t` | `−` | `(0,n,0)` |

Each division point is a **sign-change threshold** of the scale ledger. The zeros `k_t` are distinct
values — `−3, −2, −1, −½, −⅓, ½, 2` — but every one of them has the same null inertia `(0,0,n)`. The
distinctness is in the threshold, not in the signature. The one `k = 1` is not a threshold: it is the
unique identity, and no division point owns it.

This is the exact signature version of "distinct zeros, unique one": the scale ledger has as many
zeros as division points, all with the same null signature, and exactly one one. The fold ledger is
different: its zeros are distinct creases, so they are distinct as objects, not only as values.

## Topological signature

The distance field `h(P) = |P − P₀|` has an isolated zero at `P₀`; the normalized field
`(P−P₀)/|P−P₀|` restricts to the identity on `Sⁿ⁻¹`, so the degree is `+1`. Under `g_k` with `k < 0`
the normalized field is multiplied by `−1`, i.e. it becomes the antipodal map, of degree `(−1)ⁿ`;
so the sign of `k` flips the index only when `n` is odd.

A fold does not change the index of a radial field. The field is equivariant, `V(σ_H P) = σ_H V(P)`,
so conjugating it by a reflection moves the zero but keeps the charge `+1`. The fold flips
orientation, not the index. The two are different signatures: `det σ_H = −1` is the orientation
sign, while the index of the radial zero is always `+1`.

The collapsed map `g₀` itself has no isolated zero: it is constant, so every point maps to `P₀` and
there is no index to compute. The index is a signature of the **uncollapsed** radial field, not of
the collapse. That is the difference between the point (stage 0) and the zero map (stage 1 at
`k = 0`).

On the one-point compactification `Sⁿ` the same radial field has a second zero at infinity. In the
chart `y = x/|x|²` it becomes `−y`, so its index there is `(−1)ⁿ`. The two indices sum to
`1 + (−1)ⁿ`, which is `2` for even `n` and `0` for odd `n` — exactly `χ(Sⁿ)`, as Poincaré–Hopf
requires. The creation loop's return is that second zero: origin and infinity are the two ends of one
compactified field, and their signs differ by the parity of `n`.

The conservation is the point: `ind(0) + ind(∞) = χ(Sⁿ)`. A zero cannot appear alone; the second zero
at infinity is its partner. The creation loop's two ends are that pair. In the scale ledger the zero
is forced by the signature change; in the compactified ledger it is forced by the index sum. Both say
the same thing: nothing is not an isolated event.

## Checks

The algebraic claims are exact; the numbers below are floating-point confirmations for `n = 2, 3, 4`
with a random unit normal.

| check | `n=2` | `n=3` | `n=4` |
|---|---|---|---|
| `σ_H² = I` max error | `3.3e−16` | `5.6e−17` | `5.6e−16` |
| trace `σ_H` | `0` | `1` | `2` |
| det `σ_H` | `−1` | `−1` | `−1` |
| rank `σ_H − I` | `1` | `1` | `1` |
| rank `σ_H + I` | `1` | `2` | `3` |
| midpoint error | `1.1e−16` | `5.6e−17` | `1.1e−16` |

The trace is the scalar signature `n−2`. The rank columns are the inertia count: `rank(σ_H−I)=1` is
the single `−1` direction, and `rank(σ_H+I)=n−1` is the `n−1` `+1` directions. The midpoint error is
`½(P+σ_H P)` against `π_H P`.

Two exact checks:

- the symmetric part of `J` is `0`, and `Pf(J)=1` in the plane;
- `1 + (−1)ⁿ = χ(Sⁿ)` for `n = 1, 2, 3, 4, 5`: `0, 2, 0, 2, 0`.

## What this does and does not say

- It does **not** predict `n`. The dimension is an input.
- It does **not** make the signature a measurement. The signature is the invariant of a chosen form;
  under the full similarity group only `n` survives.
- The **manifold signature** is defined for `4k`-manifolds; a point is `0`-dimensional, so that
  invariant does not apply. The inertia is the one with content here.
- It **does** explain why the zero is forced in the scale ledger: a continuous sign change needs a
  degeneracy.
- It **does** explain why the fold ledger needs no zero before the one: a reflection is discrete.
- It **does** give the zero a positive fingerprint: `(0,0,n)`, not "nothing at all."
- It **does not** confuse the signature with the side of a surface. The signature counts signed
  directions of a form; a side is the sign of one normal coordinate. The metric is even in that
  coordinate, so it is side-blind; the fold is linear and flips it. See `the-fold-occlusion.md`.
- It **does not** apply to a zero of a function. The zeros of `ζ` are cancellation points, not the
  zero map; `(0,0,n)` is the inertia of the collapsed scale, not of a zeta zero. See
  `the-fold-zeta.md`.

## Files

`the-fold-signature.md` (this note). The lookup is `the-fold-key.md`; the order is
`the-fold-creation.md`; the two ledgers are in the key's "The alternating ledger" section. A
one-sentence insertion in the paper's §6 was tested and reverted because it pushed the PDF to seven
pages; the paper stays at six and the signature result stays here.

## The one sentence

**The signature of nothing is `(0,0,n)`: `n` unsigned directions. The zero is not empty — it is
totally null, and its nullity is the only thing that survives; the first fold splits off one signed
direction, and the first scale signs all `n`.**
