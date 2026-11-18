# One plus one is two

## The equation

`1_a + 1_b = 2_{ab}` is not an identity in ordinary algebra. It becomes exact under three different
readings, and each names a different Fold object:

| reading | what it says | when it holds |
|---|---|---|
| composition | one fold at `a` plus one fold at `b` is a twofold rotation | always; the count adds and the angle doubles |
| indicators | `1_a + 1_b = 2` on the overlap `a ∩ b` | exactly on the overlap; off it a term is missing |
| reciprocals | `1/a + 1/b = 2/(ab)` | iff `a + b = 2`, i.e. the roots are symmetric about `1` |

Only the first is an identity for all `a, b`; the other two are conditions. The first is the Fold's
second law, and it is the reading this note develops. The other two turn out to be the crease (the
fold ledger's zero) and the midpoint (the scale ledger balanced about its identity).

## Reading 1: folds add, the angle doubles

A fold is a reflection in a line at angle `φ`:

```
σ(φ) = [ cos 2φ   sin 2φ ]
       [ sin 2φ  −cos 2φ ]          σ(φ)² = I          det σ(φ) = −1
```

This `σ` is the global reflection. The physical sheet fold is a different map: the quotient
`F(x, y) = (x, |y|)`, which is `2`-to-`1` off the crease, `1`-to-`1` on it, and satisfies `F² = F`.
The two preimages are the two parallel layers, and the crease is their hinge: `σ` swaps the layers,
`F` identifies them. Parallel here means *over the same base point*: the two layers are one fiber,
not two pieces pushed apart. A split separates; a fold stacks. That is why the map is `2`-to-`1`
rather than `1`-to-`2`. That is the false friend: one word, two maps, and only the reflection composes
into a turn. The composition below uses `σ`, because `F² = F` — iterating the sheet fold never
rotates. See `the-fold-afar.md`.

Two of them compose:

```
σ(ψ) σ(φ) = R(2(ψ − φ))          det = (+1)          eigenvalues on the unit circle
```

So **two reflections make a rotation**, and the rotation angle is twice the angle between the creases.
The equation reads exactly:

- the left side is the **count**: `1 + 1 = 2` folds;
- the right side is the **composite**: a twofold object (a rotation), indexed by the two folds.

The factor `2` is three things at once: the number of folds, the doubling of the angle, and the first
positive even number. The third is the one the parity argument uses.

### Why two is the right number

A single fold reverses orientation (`det = −1`). Two folds restore it (`(−1)(−1) = +1`). So `2` is the
first **nontrivial** orientation-preserving composite — the first thing that can be a *rotation* rather
than a reflection. That is why the twist is built from two folds and not from one: a single fold has
order two and generates no rotation; two folds at an angle generate one.

The closure then counts in units of two. For creases at angle `α`,

```
(σ₂σ₁)^m = I      ⇔      m = π/α
```

so the group is the dihedral group `D_m` of order `2m`, and a lattice admits only the crystallographic
`m ∈ {1, 2, 3, 4, 6}`. The `2` in `1 + 1 = 2` propagates into the `2m` of the group order. See
`the-fold-closure.md`.

The same equation is the stacking law. `(σ₂σ₁)^m = I` says the `m` sectors between the creases land on
one another: the fan closes onto its first sector, so there are `m` layers over one base, not `m` sectors
spread out. A twister is exactly this — the paper folded on itself, each turn parallel to the last,
until the `m`-th face meets the first. `2m` counts the group order and the number of layer images at
once, because they are the same count seen from the group and from the stack.

### The index `ab`

The composite is labelled by the two folds. In the multiplicative notation of the Fold the label is
the ratio `b/a`; the equation's `ab` is the convention that labels one fold by the inverse of its
crease. The count and the angle doubling are convention-free; only the product-versus-ratio is a
choice. The honest statement is:

> **folds add in number and multiply in parameter** — the left side is additive, the right side is
> multiplicative.

That is the precise content of the equation, and it is why the equation is not ordinary algebra. It is
a **mixed law**: additive in the fold ledger, multiplicative in the scale ledger.

## Reading 2: the indicators (a condition, not an identity)

If `1_a` is the indicator of a set `a`, then

```
1_a + 1_b = 1_{a∪b} + 1_{a∩b}
```

so the equation `1_a + 1_b = 2_{ab}` is true **exactly on the overlap** `a ∩ b`, where both indicators
are `1`. Off the overlap it fails by the symmetric-difference term:

```
1_a + 1_b − 2·1_{a∩b} = 1_{a△b}
```

The missing term is the part of the two sets that does not coincide. So in the indicator reading the
equation says: **the two ones agree exactly where the two sides meet** — and that is the crease. The
crease `s = 0` is the only place both faces are `1`; everywhere else one side is `0`. See
`the-fold-occlusion.md`.

## Reading 3: the reciprocals (a condition, not an identity)

```
1/a + 1/b = (a + b)/(ab)
```

so

```
1/a + 1/b = 2/(ab)      ⇔      a + b = 2
```

The condition is that the **midpoint of `a` and `b` is `1`**, the Fold's identity. Equivalently, `a`
and `b` are the roots of `x² − 2x + p`, symmetric about `1`; Vieta's sum is the condition. The
harmonic mean also collapses: `H = 2ab/(a+b) = ab` when `a + b = 2`.

So the reciprocal reading is the **midpoint** of the scale ledger: two values balanced about the
identity. It is a condition on a pair, not a law of composition. See `the-fold-midpoint.md`.

## The mixed law

Put the three readings together and the equation is a small dictionary:

| side | ledger | operation |
|---|---|---|
| `1_a + 1_b` | fold | the count adds: `1 + 1 = 2` |
| `2_{ab}` | scale | the parameter multiplies: `a` and `b` compose |
| `2` on `a ∩ b` | crease | the two sides agree |
| `a + b = 2` | midpoint | the pair is symmetric about `1` |

The equation is exact because it is **mixed**: the fold ledger is additive (creases and normals
alternate) and the scale ledger is multiplicative (`k = 1` is the unique identity, `k = 0` the
collapse). Writing an additive count against a multiplicative parameter is not a mistake; it is the
Fold's signature. The two ledgers meet at `k = −1`, the point reflection, where one fold is also the
scale's zero.

This is also why the equation cannot be simplified to `1 + 1 = 2`: the subscripts carry the ledger. Drop
them and only the arithmetic remains; keep them and the composition law appears.

## Checks

`NumPy` at double precision; the reflection matrices are exact up to rounding.

| check | value |
|---|---|
| `‖σ(φ)² − I‖` | `≤ 1.1e−16` |
| `det σ(φ)` | `−1` |
| `‖σ(ψ)σ(φ) − R(2(ψ−φ))‖` | `≤ 1.3e−16` |
| `det(σ(ψ)σ(φ))` | `+1` |
| `abs` of the composite's eigenvalues | `1, 1` |
| `1/a + 1/b − 2/(ab)` | `(a+b−2)/(ab)`; zero at `(0.5, 1.5)` and `(1.5, 0.5)` |
| `1_A + 1_B − 2·1_{A∩B}` | `1_{A△B}` on random sets |

The determinant row is the parity statement: two folds restore orientation. The eigenvalue row is the
rotation statement: the composite is unitary. The reciprocal row is Vieta. The indicator row is the
overlap statement.

## What this does and does not say

- It **does** identify the identity reading: two folds compose to a rotation, and the angle doubles.
- It **does** explain the `2`: the fold count, the doubled angle, and the first even number.
- It **does** separate the two conditional readings: the indicators hold on the overlap (the crease);
  the reciprocals hold when the midpoint is `1` (the identity).
- It **does** show why the equation is mixed: additive in the count, multiplicative in the parameter.
- It **does not** make `1_a + 1_b = 2_{ab}` an ordinary algebraic identity; the subscripts carry the
  ledger.
- It **does not** fix the product-versus-ratio convention; that is a labelling choice.
- It **does not** prove anything about the zeta case; the three readings are geometric and algebraic.

## The one sentence

**`1_a + 1_b = 2_{ab}` is the Fold's mixed law: one fold plus one fold makes a twofold rotation — the
count adds, the parameter multiplies — and its two conditional readings are the crease (the ones agree
on the overlap) and the midpoint (the pair is symmetric about the identity).**

## Files

`the-fold-composition.md` (this note). The twist as two folds is in `the-fold-creation.md`; the dihedral
closure is in `the-fold-closure.md`; the crease and the two sides are in `the-fold-occlusion.md`; the
midpoint map is in `the-fold-midpoint.md`; the two ledgers are in `the-fold-key.md`; the categorical
reading of composition is in `the-fold-categorical.md`.
