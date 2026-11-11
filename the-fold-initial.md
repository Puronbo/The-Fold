# The initial form

## The question

"Find its initial state or form." The two words are not synonyms, and the Fold answers both at once:

- an **initial state** is a point in a space — where the process starts;
- an **initial form** is a quadratic or bilinear object — the algebraic thing carried at that point;
- an **initial object** is categorical — the thing with a unique arrow to every other thing.

In the Fold the three coincide, and the coincidence is the content. The initial state is the datum
`P₀`; the initial form is the zero operator, `Dg₀ = 0`, whose null form has inertia `(0,0,n)`; and the
collapsed image is the zero object, initial and terminal at once. The form is the derivative of the
state — that is the precise link between the two words.

## The initial state: the common fixed point

The family is

```
g_k(P) = P₀ + k(P − P₀)          det g_k = kⁿ
```

Every member fixes the datum:

```
g_k(P₀) = P₀ + k(P₀ − P₀) = P₀          for every k
```

The identity `g₁` fixes every point, so it is no constraint. For every other member, the datum is the
only fixed point. If `g_k(P) = P` with `k ≠ 1`, then

```
(k − 1)(P − P₀) = 0      ⟹      P = P₀
```

So the initial state has a clean characterization with no reference to `k = 0`:

> **the initial state is the unique point fixed by every non-identity member of the family.**

At `k = 0` it is also the total image: `g₀(P) = P₀` for every `P`. The point is therefore both the
common fixed point and the collapse of everything onto it. Those are the two faces of "initial."

## The initial form: the derivative of the state

Differentiate the family at the datum:

```
Dg_k = k I          Dg₀ = 0
```

The initial form is the linear part at the initial parameter. It is the **zero operator**, and the
symmetric form it defines is the null form,

```
q₀(x) = ⟨x, 0 x⟩ = 0          inertia (0,0,n)          rank 0
```

with characteristic polynomial `λⁿ` and minimal polynomial `λ`. It is the unique operator with minimal
polynomial `λ`: the identity has `λ − 1`, the fold `λ² − 1`, the point reflection `λ + 1`. Only the
initial form has spectrum `{0}`.

So "state or form" is a false disjunction: **the form is the derivative of the state, and at the
initial state the derivative vanishes.** The point carries no signed direction because its
linearization is zero; the `n` directions survive as the ambient tangent space, not as a metric.

## The initial object: initial and terminal

The collapsed image is a single point, and a point is the **zero object** of pointed spaces: it is
both initial and terminal.

- initial: from the point there is exactly one map to any pointed space — the constant map sending it
  to the basepoint;
- terminal: from any pointed space there is exactly one map to the point — the collapse.

This makes "initial" exact rather than poetic. The Fold's first object is the zero object, and the
last object is the same zero object. The chain is a loop between them.

## What is not initial

Five near-misses, each of which the corpus has had to separate:

- **Not the empty set.** The empty set has no tangent space, so its inertia is empty, not `(0,0,n)`.
  The point has `n` ambient directions; the empty set has none. See `the-fold-signature.md`.
- **Not the identity `k = 1`.** The identity is the neutral element of the group; the group is defined
  for `k ≠ 0`, and `k = 0` is outside it. The initial state is the boundary of the group, not a member.
  `k = 1` is "nothing changed"; `k = 0` is "nothing has size." These are the two nothings, and only
  the second is initial.
- **Not "nothing."** The point has a dimension and a direction sphere. It is the least structure, not
  no structure.
- **Not one direction.** The point carries all `n` unsigned directions, the sphere `Sⁿ⁻¹` (or
  `ℝPⁿ⁻¹` if sign is quotiented). The single direction is the *normal of the first fold*, and it
  arrives with the crease, not before it.
- **Not an aperture.** The aperture `θ` is a property of a cone, which is a stage-1 object. The point
  has the whole direction sphere; a cone is a later choice inside it.

## The minimal data

A homothety family is determined by the ambient space, the datum, and the parameter. Up to isometry
that is

```
(V, P₀)  ≅  (ℝⁿ, 0)          and then the parameter k
```

So the minimal initial data is two things: **a dimension and a centre.** No metric, no scale, no sign,
no aperture, no clock. Everything else is the parameter `k`; the stages are the values of `k`. The
master key's "the key is the number `k`" is the statement that the generator is the parameter, while
the initial state is the parameter's degenerate value `k = 0`.

This is why the point is not derived: it is the base case. There is nothing simpler in the Fold to
derive it from. The only honest answer to "what came before the point" is "nothing in this
construction" — and that is a statement about the model, not about the world.

## The return: initial equals terminal

The chain returns to the same object:

```
point → scale → fold → twist → closure → horizon → observer → point
```

The orbit space of `ℝ₊ × O(n)` on `ℝⁿ ∖ {P₀}` is a point, and the invariant ring is the constants.
The return is not the inverse: the inverse of an action returns `k = 1`, the identity; the loop returns
`k = 0`, the collapse. Undoing an action leaves the object; completing it leaves the point. So the
initial object is also the terminal object, but the **route** from one to the other is not a round
trip through the group — it is a passage through every stage and out the far side.

## The analytic register's initial state

The analytic pipeline has a different initial state. Its input is the theta function

```
ϑ(t) = Σ_{n∈ℤ} e^{−πn²t}
```

and its "initial form" is the modular factor `t^{1/2}`. This is an analytic object — a function on
`(0, ∞)` with an inversion symmetry — not a geometric point. The two registers do not share an initial
object; they meet at the crease, where the theta fold becomes the critical line. See
`the-fold-theta.md`.

There is one honest rhyme between the two initial states. In two dimensions the direction sphere is
`S¹`, and theta is the heat kernel on a circle. So the analytic initial state is, in that one
dimension, the heat kernel on the geometric initial state's direction sphere. It is a rhyme, not an
identification: theta needs a circle of a specific circumference, while the Fold's `S¹` carries no
metric. Do not read it as a derivation.

## Checks

The statements are algebraic; the numbers confirm them for random data with NumPy.

| check | value |
|---|---|
| `g_k(P₀) − P₀` for `k = 0.5, −1, 2, 0` | `0` |
| `g_k(P) − P` for random `P ≠ P₀`, `k = 0.7` | `0.283` (nonzero: only `P₀` is fixed) |
| `g_1(P) − P` | `0` (the identity fixes every point) |
| `‖Dg_k − kI‖` | `0` |
| `rank Dg_k` for `k = 0.5, −1, 2` | `n` |
| `rank Dg₀` | `0` |
| null-form inertia, `n = 2, 3, 4` | `(0,0,2)`, `(0,0,3)`, `(0,0,4)` |
| `g₀(P) − P₀` | `0` |

The zero-object statement is categorical, not numerical: a point has a unique map to and from every
pointed space. The minimal-data statement is an argument, not a computation: a homothety is fixed by
its centre and its parameter.

## What this does and does not say

- It **does** identify the initial state exactly: the unique point fixed by every non-identity `g_k`.
- It **does** identify the initial form exactly: `Dg₀ = 0`, the null form `(0,0,n)`.
- It **does** identify the initial object: the zero object, initial and terminal.
- It **does** reduce the initial data to a dimension and a centre.
- It **does not** say the point is the empty set, the identity, one direction, or an aperture.
- It **does not** derive the point from anything simpler; it is the base case.
- It **does not** give a single initial object for the whole corpus. The geometric register starts at
  the point; the analytic register starts at theta; they meet at the crease.

## The one sentence

**The Fold's initial state is the datum — the unique point fixed by every non-identity scale — its
initial form is the derivative there, `Dg₀ = 0`, the null form `(0,0,n)`, and its initial object is the
zero object: one point, `n` unsigned directions, no size, no sign, no clock.**

## Files

`the-fold-initial.md` (this note). The order and stage 0 are in `the-fold-creation.md`; the null form
and the zero object are in `the-fold-signature.md`; the two nothings are in `the-fold-creation.md` and
`the-fold-key.md`; the analytic initial state is in `the-fold-theta.md`; the pipeline starts at stage 0
in `the-fold-pipeline.md`; the lookup is `the-fold-key.md`.
