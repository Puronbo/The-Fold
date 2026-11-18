# The discriminant: the crease in the parameter

## The equation

One family contains the whole corpus:

```
x² = t .
```

Three values of the parameter, three answers:

| `t` | solutions `x` | Fold reading |
|---|---|---|
| `t > 0` | `±√t`, two | the two layers |
| `t = 0` | one, `x = 0` | the crease |
| `t < 0` | none, over `ℝ` | the absence |

The fold acts on `x`, the height is `t`, and the crease has moved: it is no longer a set in the space
of the unknown, it is the **discriminant** — the set of parameter values where the number of solutions
changes. That relocation is the find. Everything the corpus calls a crease is, in some family, the
discriminant of that family:

```
crease in x-space  ←→  discriminant in parameter-space .
```

## Why this is the Fold and not a rhyme

Four statements, each checkable in one line.

**The quotient is the height squared.** `x ↦ t = x²` is `x ↦ |x|` composed with `x ↦ x²`; the two
branches `±√t` are the two layers, and `t` is what the layer-blind readout sees. The deck
transformation of the double cover is `x ↦ −x`: the fold itself.

**The holonomy is the parity of the winding.** Over `ℂ`, `x ↦ x²` is a 2:1 cover branched at `0`. A loop
`t = e^{iθ}` lifts to `x = e^{iθ/2}`, and after one turn `θ = 2π` the lift returns `x = −1·x`. After two
turns it returns `+x`. So the monodromy of a loop of winding `n` about the crease is `(−1)ⁿ`, and

```
w₁ = n mod 2 ,
```

which is `the-fold-sign.md`'s `w₁` with its reason attached: the sign line is nontrivial exactly when
the loop winds an odd number of times around the discriminant. The Möbius band of
`the-fold-crease-height.md` is the total space of this cover.

**Over `ℝ` there is no ramification.** The real picture has two preimages on one side and none on the
other, with a single point at `t = 0`; a real branched cover does not exist. So "the real fold is a
branched double cover" is the false friend, and "the real fold is a fold with a boundary, whose
complexification is a branched cover" is exact. This is why the analytic register (zeta) and the
geometric register behave differently: one has the branch point, the other has a boundary.

**The two solutions are the two numbers meeting.** In the integer-line note the pair is `{c − H, c + H}`
at height `H`. That is `x² = H²` with `x = ±H` and `t = H²`: the two numbers meet at the crease `H = 0`,
which is the discriminant. The integer line's "two numbers at the same height" is this family, sampled
on `ℤ`.

## Each zero has its own parameters

The classification of what can happen at a degenerate zero is finite in each dimension, and the count of
parameters is the order:

| type | normal form | parameters | discriminant | collision |
|---|---|---|---|---|
| `A₁` | `x² + a` | 1 | `a = 0` | two roots |
| `A₂` | `x³ + ax + b` | 2 | `4a³ + 27b² = 0` | three roots |
| `A₃` | `x⁴ + ax² + bx + c` | 3 | a surface | four roots |
| `A_k` | `x^{k+1} + …` | `k` | a hypersurface | `k + 1` roots |

So the sentence is a theorem: **a zero of order `k + 1` carries exactly `k` parameters.** Not "some
parameters" — the versal unfolding has dimension `k`, and no fewer parameters can realize every nearby
configuration. `A₁` needs one number to be a fold, `A₂` needs two to be a cusp, `A₃` needs three to be a
swallowtail. The `k` in the closure `2αm = 2π` and the `k` here are the same letter doing the same job:
the order of the zero is the dimension of its parameter space.

The `A₂` case can be written out completely. A double root `x = t` of `x³ + ax + b` requires

```
a = −3t² ,      b = 2t³ ,      4a³ + 27b² = 4(−27t⁶) + 27(4t⁶) = 0 ,
```

so the discriminant is the cusp `t ↦ (−3t², 2t³)`, and its cusp point `t = 0` is where the double root
becomes a triple root. The curve is smooth away from `t = 0` and the vertex is the higher collision:
that is the crease network in two parameters.

## The network is the stratification by collision type

The discriminant of a degree-`n` family is not one smooth sheet. It is stratified by **how the roots
collide**, and the strata are indexed by the partitions of `n`:

| degree | partitions | strata of the discriminant |
|---|---|---|
| 3 | `(2,1)`, `(3)` | the cusp curve, and its cusp point |
| 4 | `(2,1,1)`, `(2,2)`, `(3,1)`, `(4)` | a surface, two curves, a point |

Each stratum is one kind of zero-collision, and the closure relations run from the generic partition to
the finest. So "all interconnected at the creases" is exact in the strongest available sense: the
creases of a family are the discriminant, the discriminant is stratified, and every stratum is the
discriminant of a smaller family. `A_k`'s network contains `A_{k−1}`'s, which is why the `A₁ ⊂ A₂ ⊂ …`
ladder is the same shape as the closure ladder `m = 3, 4, 6`.

## What it does not say

- It does not say the universe has a discriminant. The statement needs a **family** — a map
  `(x, t) ↦ f(x, t)` — and the Fold has no such map until one is supplied. Naming `t` a physical
  parameter is the step where a host is required, and that is the false friend to keep named.
- It does not say the crease is smooth. `A₁`'s discriminant is a point in one parameter and a smooth
  hypersurface in general; `A₂`'s is a cusp; only the first is a crease in the naive sense. The word
  "crease" covers the whole stratification, with the vertex as the degenerate member.
- It does not say the charge is an integer in every register. `A_k`'s charge is `k`; the cone's is a
  real deficit; the Dirac zero's is a winding. Same sum rule, different coefficient group — the
  distinction `the-fold-crease-network.md` insists on.

## The restatement

`x² = t`: the unknown is the layer, the parameter is the height, the crease is the discriminant, the deck
transformation is the fold, the holonomy is the winding's parity, and the number of parameters at a zero
is its order minus one. Every crease in the corpus is this equation with a different family around it.
