# The master key

## What this is

**The master key is the number `k` itself.** Everything in the Fold follows from it. The key is a
lookup: give it a value of `k`, and it returns the stage, the operation, what appears, what survives,
and the note that proves it. It organizes the Fold's own results; it does not add a physical theory.

Use it in four steps:

1. **Locate `k`** on the plane or in the chain.
2. **Read the stage** — what operation is active.
3. **Read the invariant** — what the operation cannot change.
4. **Follow the source** — the note that measures it.

## The key in one equation

```
g_k(P) = P₀ + k(P − P₀)          det g_k = kⁿ
k = ρ e^{iθ}                     ρ = |k| (size)      θ = arg k (turn)
```

The single complex number carries four readings:

| part of `k` | what it does | stage |
|---|---|---|
| `ρ = \|k\|` | changes size | the scale |
| `θ = arg k` | turns | the twist |
| sign of a real `k` | mirrors | the fold |
| `k = 0` | collapses | the point |

A positive real `k` uses size alone. A negative real `k` adds the mirror. A non-real unit `k` uses
turn alone. Zero uses none of them — it is the collapse of all three.

## The plane

```
                          Im k
                           ↑
                    i      │      e^{2iα}
                     ·     │     ·        |k| = 1: isometry
                           │
      ────·────────────────┼──·────·─────────→ Re k
         −1                0  k*   1
        fold             point horizon identity
```

- `k = 1`: identity — the object unchanged.
- `k = −1`: the fold / antipode — the point reflection.
- `k = i`: the quarter turn — `J`, and `J² = −1`.
- `k = e^{2iα}`: a general twist — two folds at angle `α`.
- `k* = 2GM/(c²R)`: the horizon — a real value between `0` and `1` for ordinary bodies.
- `k = 0`: the point — the origin, outside the group.

The unit circle `|k| = 1` is the isometry circle: nothing changes size, only direction or sign.

## The key table

| `k` | stage | operation | what appears | what survives | source |
|---|---|---|---|---|---|
| `0` | the point | constant map, rank 0 | the datum and its directions | `Sⁿ⁻¹`, dimension `n` | §6, cone |
| `0 < k < k*` | inside the horizon | collapse below the null surface | mathematics without physics | the mathematics | horizon |
| `k = k*` | the horizon | null boundary | entropy, temperature, causal edge | aperture `θ`, area | §5, horizon |
| `k* < k < 1` | contraction | homothety | a smaller copy | angle, cross-ratio | §1–2 |
| `k = 1` | identity | do nothing | the object itself | everything | division |
| `k > 1` | expansion | homothety | a larger copy | angle, cross-ratio | §1–2 |
| `k = −1` | the fold | point reflection | the antipode; a general `σ_H` fixes a crease of rank `n−1` | lengths, angles; orientation reverses | §4, midpoint |
| `k = i` | the quarter turn | `J` | `J² = −I` | radius, energy | §3 |
| `k = e^{2iα}` | the twist | two folds at `α` | rotation by `2α`, periodicity | radius, energy | §3–4 |
| `k^m = 1` | the closure | `D_m` | lattice, repeating pattern | `m`, root of unity | closure |
| `k` irrational phase | the quasicrystal | dense orbit | no finite closure | approximate symmetry | closure |
| real `k < 0`, `k ≠ −1` | scale + mirror | homothety ∘ point reflection | a resized, inverted copy | angle; orientation reverses | §1, §4 |

Three composite values deserve their own entry because they are the ones the paper uses:

- **The midpoint** `m_k = g_((1+k)/2)`: halving the segment; it collapses only at `k = −1`, where every
  midpoint is the datum.
- **The division point** `q_t`: collapsing at `k_t = (t−1)/t`; every `k ≠ 1` is owned by exactly
  one `t = 1/(1−k)`.
- **The horizon** `k*`: the scale at which the surface becomes null; below it the point remains in
  the mathematics and leaves the physics.

## The chain

Read left to right, the key is the order of creation; right to left, it is the paper's dissolution:

```
0 ──→ k>0 ──→ k=−1 ──→ k=e^{2iα} ──→ k^m=1 ──→ k=k* ──→ d ──→ 0
point  scale    fold       twist          closure    horizon  observer  point
```

Left to right: a direction, a size, a mirror, a turn, a pattern, an edge, a viewer, the point again.
Right to left: the same chain dissolved back to the centre. The paper teaches the twist before the
fold; creation must run fold before twist, because the twist is two folds. This is an order of
dependency, not a clock — only the horizon is a process.

## The four laws

1. **Size** — `det g_k = kⁿ`, so height `∝ k`, area `∝ k²`, volume `∝ k³`.
2. **Fold → twist** — `σ_{H₂} ∘ σ_{H₁} = R(2α)`; the quarter turn is two folds at `45°`. In the
   mixed law this is `1_a + 1_b = 2_{ab}`: the count adds, the angle doubles. See
   `the-fold-composition.md`.
3. **Closure** — `(σ₂σ₁)^m = I ⇔ m = π/α`; a lattice admits only `2 cos(2π/n) ∈ ℤ`, so
   `n ∈ {1, 2, 3, 4, 6}`.
4. **Horizon** — `k* = 2GM/(c²R)`; `S = A_H/4ℓ_P²`; `T ∝ 1/k` in the homothetic family and constant
   in the fixed-mass collapse.

## Matter: the zero at a scale

Matter is not a new object in the construction. The only zero is the map at `k = 0`, and its image
is the datum `P₀`; a body is that zero with a scale attached. In the paper's homothetic family
`M ∝ k`, and every length scales with `k`, so every dimensional quantity is a power of the height:

| quantity | in the homothetic family | in terms of `h` |
|---|---|---|
| height | `h ∝ k` | `h` |
| area | `A ∝ k²` | `h²` |
| volume | `V ∝ k³` | `h³` |
| mass | `M ∝ k` | `h` |
| entropy | `S ∝ k²` | `h²` |
| temperature | `T ∝ 1/k` | `1/h` |
| density | `ρ ∝ 1/k²` | `1/h²` |
| horizon ratio | `k*` | constant |

In one formula, every dimensional quantity is `h^{p}` times a dimensionless factor
`f(θ, arg k)`. At `h = 0`, `p > 0` vanishes, `p < 0` diverges, and `p = 0` survives. The observer
dimension shifts the exponent: a `d`-dimensional observer measures `h^{p−d}` — scalar, derivative,
flux, density for `d = 0, 1, 2, 3`.

Different masses are the same zero sampled at different `k`. In the homothetic family the horizon
ratio `k*` is constant; at fixed `R`, the horizon scale is `k* ∝ M`. Scaling changes size, not
compactness: a horizon needs the collapse or a different mass-to-radius ratio. That is the exact
content of "matter is a zero at different scales."

Matter is **stages 0–1** of the chain: the zero plus the height and aperture. The rest of the chain
is what the zero does at that scale — the fold gives orientation, the twist gives turn, the closure
gives pattern, the horizon gives thermodynamics, the observer gives measurement.

What the height does **not** fix is shape, turn and closure:

- **Shape** is the aperture `θ`; `g_k` sends `R ↦ kR` and leaves `θ` alone.
- **Turn** is `arg k`; the height is real and does not see the phase.
- **Closure** is `m = π/α`; it selects the discrete pattern, not the scale.

So the sharp statement is:

> Matter is the zero at a scale. Height fixes every dimensional quantity by a power of `h`; the
> aperture fixes the shape, and the phase fixes the turn.

The full note is `the-fold-matter.md`.

Two limits keep it honest. In the fixed-mass collapse, `M` is held while `R` falls, so `M ∝ h`
fails; the homothetic family is the spectrum of masses, the collapse is the process. And under the
full similarity group the orbit space of `ℝⁿ ∖ {P₀}` is a point and the invariant ring is constants
— matter is the symmetry-breaking label `(k, θ, arg k)` before closure and the observer enter, not an
invariant of the group.

## Two nothings

The Fold has two values that can be called "nothing," and they are not the same:

| value | name | meaning |
|---|---|---|
| `k = 1` | the identity | nothing has changed; the object is exactly as it was |
| `k = 0` | the collapse | nothing has size; the object is the point |

The group law is multiplicative, `g_a ∘ g_b = g_{ab}`. The inverse of `g_k` is `g_{1/k}`, so an
action undone by its exact reaction returns `k = 1`:

```
g_k ∘ g_{1/k} = g_1          nothing happened, but the object exists
```

The collapse is not in the group; it is absorbing:

```
g_0 ∘ g_k = g_0              once at zero, no action restores it
```

The reaction mass model is a monoid `(0, 1]`, not a group: it can expel mass but cannot add it back.
So the reaction cannot cancel the action to return to `1`; it drives `k` toward `0`. That is why the
collapse is a process and the homothetic family is not.

"Nothing has happened because an action was reduced by reaction" is therefore true in two different
senses:

- **Identity sense:** the reaction is the exact inverse `1/k`; the net is `k = 1`; nothing changed,
  but the object exists.
- **Collapse sense:** the reaction is the monoid's one-way loss; the net is `k = 0`; nothing has
  size, but the direction survives.

Dimensionless bookkeeping cancels even when dimensional bookkeeping does not: the homothetic family
changes every size, but leaves `k*`, `θ`, and the cross-ratio fixed. Nothing happens to the ratios;
everything happens to the magnitudes. Read only the dimensionless side, and the family is static:
every size changes and no ratio does. That is the strongest "nothing has happened" the Fold allows —
a statement about ratios, not about existence.

The creation loop is not a group inverse. The inverse of an action returns `k = 1`; the loop returns
`k = 0`. Undoing an action leaves the object; completing it leaves the point. That is the difference
between the two nothings.

## The alternating ledger

A sequence `0 → 1 → 0 → 1 → …` with each term distinct does not live in the scale ledger. It lives
in the **fold ledger**, where zero and one are different kinds of object:

| | fold ledger | scale ledger |
|---|---|---|
| zero | a crease `H` | the collapse `k = 0` |
| one | the unit normal `n ∈ Sⁿ⁻¹` | the identity `k = 1` |
| split | the two sides `±` of `H` | the reciprocal pair `k, 1/k` |
| annihilation | midpoint back onto `H` | product returns `1` |

The fold ledger is **additive**: a fold is a sign, `+` or `−`, and reflection swaps the signs. The
scale ledger is **multiplicative**: a scale is a ratio, and the identity is `1`.

The reason the fold ledger can alternate is that each fold carries its own crease. Give a fold by a
point `P_H` on `H` and a unit normal `n`; the signed distance is

```
f(P) = (P − P_H) · n          f⁻¹(0) = H          ∇f = n
```

The zero set is the crease; the gradient is the normal. The normal is literally the split of the
zero: it is what the zero is differentiated into. Reflection sends `f → −f`, so the two sides of the
crease are the `+` and `−` of one sign — **one is a split of zero**. Halving a point and its image
lands on the crease again, `½(P + σ_H P) = π_H P ∈ H` — **zero is the annihilation**.

A fold is fixed by its hyperplane, so distinct folds have distinct creases. The normal is defined
only up to sign, so the fold ledger's one is the pair `{n, −n}`: the two choices of arrow name the
same two sides. The crease, not the arrow, is what distinguishes folds. That is enough to make
`0 → 1 → 0 → 1` a chain of distinct zeros and ones rather than a repetition:

```
H₁ → n₁ → H₂ → n₂ → …          each crease new, each normal a new pair
```

The scale ledger cannot do this. It has a unique one, `k = 1`: multiplying by `1` changes nothing,
so there is no second identity. Its zeros are distinct — `k_t = 1 − 1/t` for each division point
`t` — but they are distinct *collapses*, and to each collapse `k_t` there is an owning `t`. So:

- **Distinct zeros:** yes, in both ledgers. Fold creases `H`, division points `k_t`.
- **Distinct ones:** only in the fold ledger. In the scale ledger the one is unique; different
  "ones" are different choices of unit or frame, not different identities.

The two ledgers meet at `k = −1`, the point reflection `g_{−1}(P) = P₀ − (P − P₀)`. It is the
degenerate fold: its fixed set is the datum alone, not a hyperplane, and its midpoint map is
`m_{−1} = g₀`. It is the fold ledger's zero wearing the scale ledger's zero — a crease with no
extent.

Read that way, existence alternates because the fold alternates: crease, normal, crease, normal.
The scale ledger supplies the amplitudes `k`; the fold ledger supplies the signs. Neither ledger
alone produces the sequence, and the distinction is what keeps "each zero and one is distinct" from
collapsing into "the same zero repeats."

## The signature of zero

The strict signature of a symmetric form is its inertia `(n₊, n₋, n₀)`. The zero map's linear part
is `0`, so it is totally null rather than balanced:

| operator | inertia | scalar signature |
|---|---|---|
| zero `g₀` | `(0,0,n)` | `0` |
| fold `σ_H` | `(n−1,1,0)` | `n−2` |
| identity `g₁` | `(n,0,0)` | `n` |
| point reflection `g_{−1}` | `(0,n,0)` | `−n` |

The scalar signature of the zero is `0`, but so is the planar fold's (`(1,1,0)`); only the full
inertia separates **all null** from **one plus, one minus**. So the signature of nothing is the
nullity `n`, not the number `0`. The zero's algebraic fingerprint is `(λⁿ, λ)`: characteristic
polynomial `λⁿ`, minimal polynomial `λ`, the unique operator annihilated by `x`.

Why the zero is forced: `k|·|²` has inertia `(n,0,0)` for `k > 0` and `(0,n,0)` for `k < 0`; inertia
is constant on nondegenerate forms, and any path from `I` to `−I` must cross an eigenvalue `0`. In
the Fold that crossing is `k = 0`. The fold is the discrete exception: a reflection jumps from `+`
to `−` without a path, which is why the fold ledger needs no zero before the one.

What survives at the zero is `n`, the sphere `Sⁿ⁻¹`, the tangent cone and the aperture `θ`; under the
full similarity group only `n` is invariant. The fold's signature is `(n−1,1,0)`: the crease is the
`+` eigenspace of dimension `n−1`, the normal the `−` eigenspace of dimension `1`. That is the
signature reading of "one is a split of zero": the fold signs all `n` directions at once, `n−1` plus
and one minus, and the singled-out minus direction is the "one"; the projection
`½(I + σ_H) = π_H` annihilates it back onto the crease.

On the compactified space the radial field has a second zero at infinity, with index `(−1)ⁿ`; the two
indices sum to `χ(Sⁿ)`. So the return is forced too: the loop has two ends, origin and infinity, and
their signs differ by the parity of `n`.

By stage: point `(0,0,n)`, scale `(n,0,0)`, fold `(n−1,1,0)`, twist symplectic (`Pf=1`), horizon null
(`(n−2,0,1)` induced), return `(0,0,n)`. The twist is invisible to inertia because its symmetric part
is zero on the rotation plane; the Pfaffian is its invariant.

The full note is `the-fold-signature.md`.

## The occlusion

The front and back of a surface are the two signs of its normal `s = (P−P_H)·n`. The fold flips `s`;
the projection `π_H` drops it; the metric `|·|²` squares it and cannot see the sign. That is why a
sensor made of a form is side-blind: a form is quadratic, the side is linear. The crease `s = 0` is
the only place the two sides meet, and there the surface is edge-on. A continuous turn must cross it;
a fold jumps. The one-way surface in the model is the horizon, not the twist: `J` is
orientation-preserving and periodic. Mathematics can see the axis `s`, not both faces. See
`the-fold-occlusion.md`.

## The critical line is a crease

The Dirichlet term is the Fold's complex `k` at height `h = ln n`:

```
n^{-s} = e^{-σh} e^{-ith}          |k| = n^{-σ}          arg k = −t ln n
```

The term is a scale by `n^{-σ}` and a twist by `−t ln n`. The Euler product is the multiplicative
ledger; the Dirichlet series is the additive one.

The functional equation `ξ(s) = ξ(1−s)` and reality `ξ(s̄) = conj ξ(s)` compose into the reflection
`R(s) = 1 − s̄`, a fold whose crease is the critical line `Re s = 1/2`. The hypothesis is that every
zero of `ξ` is fixed by `R`, i.e. lies on the crease. That is an exact reformulation, not a proof: the
equation pairs `ρ` with `1−ρ`, reality pairs it with `ρ̄`, and the composition is `R`; a symmetric
pair can still sit off the crease. The primes are the multiplicative generators; the zeros are the
additive frequencies; the explicit formula is the exchange. See `the-fold-zeta.md`.

## Zeros as facets

A facet is a zero of a supporting functional, codimension one. The fold's crease is a facet; the
scale's zero is a vertex, codimension `n`; a zeta zero is a point, codimension `2`, a facet only of the
critical line. The two ledgers say it plainly: fold zeros are facets, scale zeros are vertices. See
`the-fold-facets.md`.

## The theta fold

The functional equation is not assumed. It is derived from the theta identity

```
ϑ(1/t) = √t ϑ(t)          ϑ(t) = Σ_{n∈ℤ} e^{−πn²t}
```

In the height `h = ln t`, this is a fold: `h ↦ −h`, with crease `h = 0`. The factor `e^{h/2}` is the
half-density, the square root of the Jacobian of the inversion. The Mellin transform of `ϑ` is
`π^{−s/2} Γ(s/2) ζ(s)`; splitting the integral at `t = 1` and using the theta identity gives
`I(s) = I(1−s)`, hence `ξ(s) = ξ(1−s)`.

The `1/2` is not a convention. If a modular function satisfies `Φ(1/t) = t^α Φ(t)`, the same split
gives `I(s) = I(2α − s)`, so the axis is `Re s = α`. For theta `α = 1/2`, which is exactly the
critical line. The fold gives the axis; it does not give the zeros. See `the-fold-theta.md`.

## The zero pipeline

Every stage of the Fold solves a zero equation, and each solution is a different kind of zero:

| stage | zero equation | zero type |
|---|---|---|
| point | `P − P₀ = 0` | value |
| scale | `det g_k = kⁿ = 0` | vertex |
| fold | `(σ_H − I)P = 0` | facet |
| twist | `(J − I)v = 0` (only `v = 0`) | none |
| closure | `cos(2π/m) = 0` | discrete angle |
| horizon | `g(v,v) = 0`, `v ≠ 0` | null crease |
| observer | none | none |
| zeta | `ξ(ρ) = 0` | point |

It is a list of roles, not a conveyor: the type changes at every stage, so a vertex cannot be piped
into a facet. The twist and the observer are the two gaps, and they are exactly the stages whose
invariant is not an inertia (`Pf(ω) = 1`, `⋆²`). The only pipeline that composes is analytic: theta's
fold becomes the critical line and the zeros land on it. See `the-fold-pipeline.md`.

## The problems

The dictionary reaches RH exactly and a dozen other problems by rhyme. The useful part is the map of
what is missing, one item per known route to RH:

| route | needs | the Fold supplies |
|---|---|---|
| positivity (function fields) | an arithmetic surface whose intersection form has signature `(ρ−1,1,0)` | the signature shape `(n−1,1,0)`; no surface |
| Hilbert–Pólya | a self-adjoint `H` with `[H,R]=0`, spectrum `{γ_n}` | the crease and the commutation condition; no `H` |
| de Bruijn–Newman | a bound `Λ ≤ 0` | the heat kernel (theta) and the crease; no bound |
| explicit formula | a parity-breaking estimate at `1/2` | the prime–zero exchange; no estimate |

The fold's inertia and the negative Hodge intersection form have the same shape at every rank; that is
the closest link, and it is a link of shape, not of proof. See `the-fold-problems.md`.

## The initial form

The initial state is the datum `P₀`, and it has an exact characterization: **the unique point fixed by
every `g_k`** (`g_k(P₀)=P₀`; and `g_k(P)=P` with `k≠1` forces `P=P₀`). Its initial form is the
derivative there, `Dg₀ = 0` — the null form `(0,0,n)`, rank 0, minimal polynomial `λ`. So the form is
the derivative of the state, and at the initial state the derivative vanishes.

The collapsed image is the **zero object**: a point is initial and terminal among pointed spaces. The
initial data reduces to a dimension and a centre; `k` is the generator, and `k = 0` is its degenerate
value, outside the group. The point is not the empty set, not the identity `k=1`, not one direction,
not an aperture. See `the-fold-initial.md`.

## The categorical reading

"Objects are disguised morphisms" has three exact readings: the arrow category (trivial), Yoneda
(substantive), and duality/looping (the direction reverses or drops a level). The content is always
the **functor**, not the word "disguised." The Fold names one, and its objects are universal
constructions:

| Fold object | categorical construction |
|---|---|
| the key `k` | an endomorphism: `End_ℂ(ℂ) ≅ ℂ`, `k ↦ m_k` |
| the crease | the equalizer of `σ_H` and `id`, `ker(σ_H − I)` |
| the orbit space | the coequalizer of the action, a point |
| the point | the zero object: initial and terminal |
| the scale family | a representation `Bℂ* → Vect` |

The zeta exchange rhymes with a duality but is not an adjunction. See `the-fold-categorical.md`.

## The mixed law of composition

`1_a + 1_b = 2_{ab}` is the Fold's composition law. It is **mixed**: the number of folds adds
(`1 + 1 = 2`) while the parameter multiplies (`a` and `b` compose). Two folds compose to a rotation
`R(2(ψ−φ))`, so the `2` is at once the fold count, the doubled angle, and the first nontrivial
orientation-preserving composite. The two conditional readings are the crease (`1_a + 1_b = 2` exactly
on `a ∩ b`) and the midpoint (`1/a + 1/b = 2/(ab)` iff `a + b = 2`). See `the-fold-composition.md`.

## The point's extensions

A crease through `P₀` is indexed by an unoriented normal: `H_n = H_{−n}`, so the folds through the
point are the projective sphere `ℝPⁿ⁻¹ = Sⁿ⁻¹/(±1)`. The two sides are one fold. The pencil of
creases covers the space and intersects in the point:

```
⋂_{H ∋ P₀} H = {P₀}          ⋃_{H ∋ P₀} H = ℝⁿ
```

Cones with apex `P₀` and all proper apertures do the same: their union is `ℝⁿ` and their intersection
is `{P₀}`; the double cone (both nappes) is the orbit of one ray under `O(n−1) × {±1}`. The point does
not extend: it has the tangent space `ℝⁿ` with the zero form `(0,0,n)`, the direction sphere `Sⁿ⁻¹`,
and no metric, no selected aperture, and no tangent *plane*. See `the-fold-apex.md`.

## P and NP

`NP` is an existential projection: `x ∈ L ⇔ ∃w R(x,w)`, and a solver is a section of `π_X`. The Fold's
linear projection `π_H = ½(I + σ_H)` is the simplest instance, and it is always split (`rank n−1`,
kernel the normal line), so the hardness is the **cost** of the section, not its existence. P is the
additive ledger (`1+1=2`), NP the multiplicative one (`ab`); verification is the outward crossing of
the one-way horizon. The Fold has no computational model, and every invariant it computes is
polynomial-time: a poly-time invariant that separated the classes would decide the NP language and
collapse them, so the Fold can map the wall but not cross it. See `the-fold-complexity.md`.

## The crease and its height

In every geometric register the crease is codim 1. The height is whichever coordinate it leaves free, and
that coordinate has three registers: **transverse** (the affine offset `c`, which the fold flips), **longitudinal** (the zeta
zero's imaginary part `t = Im s`, which the crease leaves free), and **scale** (matter's `h` and the
Dirichlet term's `ln n`). "What is left is the crease and its height" is exact only with the register
named. The pair is a basis, not a generator: one crease plus one height is one affine hyperplane; the
twist needs two creases, the closure their angle, the observer a dimension. See
`the-fold-crease-height.md`.

## The folded line from afar

A sheet fold is the quotient map `F(x, y) = (x, |y|)`, not the global reflection `σ_H` (which maps a line
to a line). A line crossing the crease becomes a V with vertex on the crease; its shadow `π_H` is the
crease — one line, the "singular line." The V's path exceeds its shadow by `L m²`, and a pleated line's
by `2a²/ℓ²`: the fold's transverse height is invisible in the projection but survives in the length at
second order. "Singular" has three readings — one line (quotient), non-smooth (the normal derivative
jumps by `2`), rank-deficient (the projection) — all at the crease. The scale `k` does not erase the fold
(the shape is scale-invariant); "from afar" is a projection or a coarse-graining, not `k → 0`. See
`the-fold-afar.md`.

Adjacent research: the V is the Whitney fold's normal form, the shadow is an apparent contour, the
pleats are an infinite-dihedral quotient, the moments are the law of total variance, the resolution is
the Airy `2/3` law and the Sparrow criterion, the crease pattern is rigid foldability (NP-hard), and the
coarse-graining is Γ-convergence. The note states what transfers and what does not.

## The observer: dimension and window

The observer is the pair `(d, w)`. `d` is the form degree: a `d`-dimensional observer measures a
`d`-form, so a homogeneous quantity of degree `p` becomes `h^{p−d}` — scalar, derivative, flux, density
for `d = 0, 1, 2, 3`. The star's square is `⋆² = (−1)^{d(n−d)+s}`; the signature selects the sign. `w`
is the window: the Gaussian `G_w`, with exact semigroup `G_{w1} * G_{w2} = G_{√(w1²+w2²)}`, attenuates a
feature of half-period `ℓ` by `e^{−π²w²/(2ℓ²)}`. The paper's table is the `w → 0` slice; "from afar" is
`w` larger than the fold's height. The parameters are independent: wrong `d` is degree blindness (no
flux without an oriented area), wrong `w` is scale blindness (the fold is averaged away); neither fixes
the other. The surface is `d = n−1`, edge-on; the horizon is its null limit. See
`the-fold-observer.md`.

## Sampling, closure, and the horizon window

The window has a discrete dual. An `m`-fold closure has angular frequency `m`; a probe with `N` samples
per turn sees the alias `m_app = min(m mod N, N − m mod N)` and resolves the pattern only above Nyquist,
`N > 2m`, equivalently sample spacing `a < πR/m`. The Gaussian window attenuates the `m`-th harmonic by
`e^{−m²σ²/2}` with `σ = w/R`; at the half-sector width `σ = π/m` the attenuation is `e^{−π²/2} = 7.1919e−3`,
the same cutoff as the folded-line note. There are two lattices: the object's (closure `m`; the
crystallographic restriction gives `n ∈ {1,2,3,4,6}` for a periodic crystal) and the probe's (`N`, not so
restricted). The horizon is the `d = n−1` observer whose window is the causal cone; the null crease is the
boundary of its support. The Gaussian is the non-causal idealization; the retarded propagator is the
causal window. The probe is `(d, w, a)`. See `the-fold-sampling.md`.

## Key by question

| question | answer | source |
|---|---|---|
| Why do area and height disagree? | `det = kⁿ`; area is degree 2, height degree 1 | §1 |
| What is matter? | the zero at a scale: stages 0–1; every dimensional quantity is `h^{p}` | matter |
| What does height not fix? | shape `θ`, turn `arg k`, closure `m`, observer dimension `d` | matter |
| What can change a dimensionless ratio? | one of `θ`, `arg k`, `m`, `d` — never the height | matter |
| Why does a 3D observer see density? | the observer divides by a `d`-volume: `p → p−d`; mass `p=1` gives density `p=−2` | matter, §7 |
| Why is a mass ratio not just a height ratio? | it is `(h₁/h₂)(f₁/f₂)`; shape and phase contribute | matter |
| Did anything happen? | depends on the ledger: `k=1` identity, `k=0` collapse, and every dimensionless ratio invariant | key, matter |
| Why is the loop not an inverse? | the inverse returns `k=1`; the loop returns `k=0` | key |
| How can zeros and ones alternate? | fold ledger: distinct creases `H` and normals `n`; scale ledger: distinct zeros `k_t`, unique one `k=1` | key |
| Why is one plus one two? | two folds compose to `R(2(ψ−φ))`: the count adds, the parameter multiplies, the angle doubles | composition |
| Where do the two readings of `1_a+1_b=2_{ab}` hold? | indicators on the overlap `a ∩ b` (the crease); reciprocals iff `a+b=2` (the midpoint) | composition |
| Why are the two sides one fold? | the crease is `H_n = H_{−n}`: the normal is unoriented, so folds through the point are `ℝPⁿ⁻¹` | apex |
| Is the point on every crease? | yes, `P₀ ∈ H` for every `H` in its pencil; and only `P₀` is on all of them | apex |
| Does the point extend? | no; its tangent cone does: `⋃ D(n,α) = ℝⁿ` and `⋂ D(n,α) = {P₀}` | apex |
| Can the Fold decide P vs NP? | no: no computational model, and every invariant is polynomial-time | complexity |
| What is NP in the Fold's diagram? | an existential projection; a solver is a section | complexity |
| Why can't a Fold invariant separate P from NP? | a poly-time invariant decides the NP language, so it proves equality, not inequality | complexity |
| What is left after the wall? | a crease and a height — the instance and the witness, with the cost of the height function open | crease-height |
| Is "height" one coordinate? | no: transverse (affine offset, witness), longitudinal (zeta `t`, theta `ln t`), or scale (`ln n`, matter) | crease-height |
| Does one crease and one height generate the Fold? | no; they are a basis: the twist needs two creases, closure their angle, the observer `d` | crease-height |
| Why does a folded line look singular from afar? | the projection drops the transverse height; the shadow is the crease, one line | afar |
| Is "from afar" the same as `k → 0`? | no: the scale is shape-invariant; the projection or coarse-graining drops the height | afar |
| Where does the fold's height survive? | in the length, at second order: `L m²` for a V, `2a²/ℓ²` for pleats | afar |
| What does "singular" mean here? | one line (quotient), non-smooth (derivative jump), rank-deficient (projection) — all the crease | afar |
| Why does an observer need two parameters? | `d` selects the form, `w` the scale; neither fixes the other | observer |
| What is "from afar" in observer terms? | a window `w` larger than the fold's height; the ratio `h/D`, not `k → 0` | observer, afar |
| Why can a 2D observer miss the fold? | it has the flux but its window `w > h` averages the fold away | observer |
| What is the horizon as an observer? | `d = n−1` on the surface: `Ω = 2π`, edge-on; the null limit | observer, horizon |
| When is an `m`-fold closure resolved? | `N > 2m` samples per turn; equivalently `a < πR/m` | sampling, closure |
| Are the closure and the sampling lattice the same? | no: `m` is the object's symmetry, `N` the probe's discretization; they are dual | sampling |
| Does the crystallographic restriction limit the observer? | no: it limits the object's periodic lattice (`n ∈ {1,2,3,4,6}`), not `N` | sampling, closure |
| What is the horizon's window? | the causal cone: retarded support `\|x\| ≤ t`, null boundary `\|x\| = t`; not the Gaussian | sampling, horizon |
| What is the signature of zero? | `(0,0,n)`: `n` unsigned directions; scalar `0` but nullity `n` — not a balanced form | signature |
| Why must nothing come first? | in the scale ledger a continuous sign change must cross a degenerate form; `k=0` is that crossing | signature |
| What is the signature of a fold? | `(n−1,1,0)`: crease `+` of dimension `n−1`, normal `−` of dimension `1` | signature |
| Where is the second zero? | at infinity on the compactified space; index `(−1)ⁿ`; the two indices sum to `χ(Sⁿ)` | signature |
| Why is the twist invisible to signature? | `J` is skew; its symmetric part is `0`; its invariant is the Pfaffian `1`, not an inertia | signature, §3 |
| Why are the scale zeros distinct? | each division point is a threshold `k_t`; all have inertia `(0,0,n)`, but the one `k=1` is unique | signature, division |
| Why does a 2-form flux square to `−1`? | `⋆² = (−1)^{d(n−d)+s}`; in 4D Lorentzian, `d=2`, `s=1` gives `−1` | signature, §7 |
| What is the signature of a 4-fold closure? | `cos 90° = 0`: the unique signature-zero closure; 3-fold gives `−½`, 6-fold gives `+½` | signature, closure |
| What is the horizon's signature? | a null normal, `n·n=0`: the induced form is `(n−2,0,1)` in Lorentzian `(n−1,1,0)` | signature, horizon |
| Why can't a sensor see the back? | the back is the sign of the normal; a symmetric form is quadratic and even in it, so the sensor is side-blind | occlusion |
| Can both faces be seen at once? | not by a definite measurement; the crease `s=0` is the only meeting place, and it is edge-on | occlusion |
| Is the twist a one-way lock? | no; `J` preserves orientation and is periodic; the one-way surface is the horizon (null crease) | occlusion, horizon |
| What is the critical line? | the crease of `R(s) = 1−s̄`: the functional equation plus reality | zeta |
| Is RH a change of scale? | the term `n^{-s}` is a scale+twist at height `ln n`; RH is the zeros lying on the crease, not a scale change | zeta |
| Are the primes an illusion? | no; primes are the multiplicative generators, zeros the additive frequencies; the explicit formula is a duality | zeta |
| Does the Fold prove RH? | no; the fold gives the crease and pairs the zeros, but does not force them onto it | zeta |
| When is a zero a facet? | when it is codimension 1: a crease; a scale zero is a vertex, a zeta zero is a point | facets |
| Are the zeta zeros facets? | in the plane they are points; on the critical line they are facets of the line | facets, zeta |
| Why is the critical line at `1/2`? | the theta modular factor is `t^{1/2}`; a general exponent `α` gives the axis `Re s = α` | theta |
| Where does the functional equation come from? | the theta fold in height, read through the Mellin transform | theta |
| What is the zero pipeline? | the zero equation of each stage; the solution type changes: value, vertex, facet, null, point | pipeline |
| Why is the twist off the pipeline? | `J` is invertible; `(J−I)v = 0` has only `v = 0`; its invariant is `Pf(ω)=1`, not an inertia | pipeline |
| What is missing for RH? | one of: a surface (positivity), an operator (Hilbert–Pólya), a bound (`Λ≤0`), a parity breaker | problems |
| Is the Fold's zero a zeta zero? | no; a zeta zero is a cancellation, codim 2, not the zero map | problems, zeta |
| Do the zeros' statistics match the twist? | yes, one `J` gives `β=2` (GUE); the Pfaffian is not the quaternionic `β=4` class | problems |
| What is the initial state? | the datum `P₀`: the unique point fixed by every non-identity `g_k` | initial |
| What is the initial form? | `Dg₀ = 0`: the null form `(0,0,n)`, rank 0 | initial |
| Is the point the empty set? | no; it has `n` unsigned directions and a zero object; the empty set has no tangent space | initial, signature |
| Is the crease an object or a morphism? | both: it is the equalizer of `σ_H` and `id`, a limit defined by morphisms | categorical |
| Is `k` a number or an operator? | both: `End_ℂ(ℂ) ≅ ℂ`; the scalar is multiplication | categorical |
| Is the orbit space a limit or a colimit? | a colimit: the coequalizer of the action; the crease is the limit | categorical |
| Why is a twist two folds? | `σ_{H₂} ∘ σ_{H₁} = R(2α)` | §4 |
| Why does the twist repeat? | closure `m = π/α` | closure |
| Why only 2-, 3-, 4-, 6-fold in a lattice? | `2 cos(2π/n)` must be an integer | closure |
| Why is `k = 0` not in the group? | `det g₀ = 0`, rank 0, not invertible | §6 |
| Why is there no time at the point? | a 0D observer sees values, not rates | §7 |
| Where does entropy come from? | it appears in one step at `k*` | horizon |
| Why does the horizon arrive before zero? | `k* > 0` for every ordinary body | horizon |
| Why is `k = −1` the meeting point? | scaling and folding coincide: an isometry that reverses direction | invariants |
| Why does the horizon table need two columns? | homothetic family (`M ∝ k`) is not a process; fixed-mass collapse is | horizon |
| Why is a cone's twist exactly zero? | its fold group is the planes through the axis; a turn about the axis is the identity on the body | cone |
| What is left at the end? | the orbit space is a point; the invariant ring is constants | invariants, §9 |

## Calibration

No new measurements. These are the existing checks the key rests on:

| check | value |
|---|---|
| midpoint identity `m_k = g_((1+k)/2)` | `4.58e−16` |
| crease residual `½(I + σ_H) = π_H` | `2.22e−16` |
| division round trip `t → k → t` | `1.78e−15` |
| closure residual | `2.4e−16` |
| aperture at `k = 1, 10⁻³, 10⁻⁶` | `60.0000°` |
| vertex `Ω/4π` at `θ = 60°` | `0.25` at every zoom |
| exterior `Ω/4π` at `k = 1, 0.5, 0.25` | `5.060%`, `1.216%`, `0.301%` |
| `k*` for Earth / Sun / 70 kg water | `1.392e−9` / `4.245e−6` / `4.067e−25` |
| rank at `k = 0` | `n → 0` in one step |
| fold signature `rank(σ_H−I)` / `rank(σ_H+I)` | `1` / `n−1` (checked `n=2,3,4`) |
| `σ_H² = I` max error | `5.6e−16` (`n=2,3,4`) |
| twist `Pf(J)` in the plane | `1` exact |

## Index

| if you want | read |
|---|---|
| the whole argument | `the-fold.pdf` (6 pages) |
| the one determinant | `the-fold.md` §0–1 |
| the plane and the rotation `J` | `j-plane.html` |
| interior vs exterior apex | `j-cone-3d.html` |
| rank and the observer | `j-collapse-3d.html` |
| `m = π/α` and `D_m` | `fold-closure.html`, `the-fold-closure.md` |
| the two horizon columns | `horizon-scaling.html`, `the-fold-horizon.md` |
| the midpoint and the crease | `fold-midpoint.html`, `the-fold-midpoint.md` |
| division points and two evolutions | `fold-division.html`, `the-fold-division.md` |
| what scaling and folding keep | `fold-invariants.html`, `the-fold-invariants.md` |
| the range cone | `cone-range-3d.html`, `the-fold-cone.md` |
| the order of creation | `the-fold-creation.md` |
| matter as the zero at a scale | `the-fold-matter.md` |
| the signature of nothing | `the-fold-signature.md` |
| the occlusion and the back | `the-fold-occlusion.md` |
| the critical line and the zeta zeros | `the-fold-zeta.md` |
| which zeros are facets | `the-fold-facets.md` |
| why the critical line is at 1/2 | `the-fold-theta.md` |
| the zeros in pipeline order | `the-fold-pipeline.md` |
| what the Fold does and does not reach | `the-fold-problems.md` |
| where the Fold starts | `the-fold-initial.md` |
| objects as disguised morphisms | `the-fold-categorical.md` |
| why one plus one is two | `the-fold-composition.md` |
| one point, both sides, all angles | `the-fold-apex.md` |
| P vs NP and the wall | `the-fold-complexity.md` |
| the crease and which height | `the-fold-crease-height.md` |
| a folded line that looks like one line from afar | `the-fold-afar.md` |
| the observer as dimension and window | `the-fold-observer.md` |
| closure as sampling and the horizon window | `the-fold-sampling.md` |

## The key in one sentence

**`k` is one complex number: its modulus is size, its angle is turn, its sign is mirror, and zero is
the point — and the whole construction is that one number, read in dependency order.**

Read as a body, the same key says: matter is the zero at a scale. Height fixes the magnitudes;
shape and phase fix the rest.
