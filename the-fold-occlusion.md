# The occlusion: the back is not a place

## The claim

A viewer outside a closed surface sees one side. To see the other it must walk around or turn the
object; the first side vanishes as the second appears. The claim is that the hidden back is the
"Nothing" engine, that the chiral twist is a one-way lock, and that the front face may be a hard
limit.

The geometry says something more precise, and more interesting: **the back is not a region behind the
front. It is the sign of the normal, and a quadratic measurement cannot see a sign.** The fold flips
it; the metric squares it; the projection drops it; the crease is the only place the two sides meet.
That is the exact content of "you cannot see both faces at once."

## What is exact: the side is a sign the form forgets

Write the fold about a crease `H` with unit normal `n`:

```
σ_H(P) = P − 2((P − P_H)·n) n
```

Split a point into its crease part `h` and its normal coordinate `s = (P − P_H)·n`:

```
P = P_H + h + s n,     h ⊥ n
σ_H(P) = P_H + h − s n
```

The fold keeps `h` and flips `s`. The two sides of the surface are `s > 0` and `s < 0`; the crease is
`s = 0`. The fold exchanges the sides and fixes the crease pointwise. Its two eigenspaces are the
crease `+1` of dimension `n−1` and the normal `−1` of dimension `1`. Categorically the crease is the
equalizer of `σ_H` and the identity, `ker(σ_H − I)`: an object defined by the agreement of two
morphisms. See `the-fold-categorical.md`.

Globally, for an orthographic view direction `v`, the visible set of a surface is
`{p : n(p)·v > 0}`, the hidden set is `{p : n(p)·v < 0}`, and the terminator is `{n(p)·v = 0}`.
Back-face culling is the sign test `n·v`; the terminator is the crease of that view. The local model
above is the same statement at one point.

Now the measurement. A metric is a quadratic form:

```
Q(P) = |P − P_H|² = |h|² + s²
```

It is even in `s`. It cannot distinguish `s` from `−s`. **A symmetric form is side-blind.** The
signature counts signed *directions*, not the two sides of a surface: the normal is one direction, and
the form assigns it one sign; the other side is not a second direction, it is the opposite value of
the linear coordinate. The form sees the axis; it does not see which side of the axis you are on.

This is the exact version of the sensor that cannot see the back. The sensor's instrument is a form;
a form is quadratic; a quadratic is even in the normal coordinate. The side is linear. It is not in
the instrument.

| object | formula | what it does with the side |
|---|---|---|
| fold | `σ_H` | flips it: `s → −s` |
| projection | `π_H = ½(I + σ_H)` | drops it: `s → 0` |
| metric | `Q = \|·\|²` | squares it: `s → s²`, cannot see the sign |
| orientation / `d`-form | a sign | picks one side |
| linear coordinate | `s = (P−P_H)·n` | is the axis; both values, neither face |

The last row is the only object that knows both sides, and it is not a face. It is the axis. That
distinction is the answer to the question, and the rest of this note is its consequences. The pencil
of such axes through the datum is the projective sphere `ℝPⁿ⁻¹`, the Fold's fold parameter; see
`the-fold-apex.md`.

The coordinate that `π_H` drops is the transverse height `s = (P − P_H)·n`. Keeping the crease and that
height is the affine pair of `the-fold-crease-height.md`; dropping the height is exactly why the shadow
is side-blind.

## The crease is the only meeting place

`π_H` has rank `n−1` and kernel the normal line. It sends `P` and `σ_H(P)` to the same point on the
crease:

```
π_H(P) = π_H(σ_H P) = P_H + h
```

So the shadow is the quotient by the fold. For `P` off the crease, the two sides are one orbit
`{P, σ_H P}`; the quotient is a half-space, and the crease is its boundary. This is the exact form of
"the illusion of two": the pair is one orbit, and the identification is the fold. The two are not two
substances; they are two values of one coordinate.

The crease is also the only place the two faces meet, and there the surface is **edge-on**. At
`s = 0` neither face has area. So the continuous version of "the front disappears when the back
appears" is stronger than the original: there is a moment of **neither**, and it is the crease.

This is the indicator reading of `1_a + 1_b = 2_{ab}`: the two ones agree exactly on the overlap, and
the overlap is the crease. See `the-fold-composition.md`.

In the language of facets, the crease is a facet; the local front/back is the sign of its normal. See
`the-fold-facets.md`.

## The two ledgers of a view

Changing the view has the same two-ledger structure as the scale:

- **Continuous turn.** `s` passes through `0`. A face becomes edge-on, then the other face appears.
  The zero of the view is forced, exactly as the zero of the scale is forced: a continuous sign change
  must cross a degenerate form.
- **Discrete fold.** `s` jumps from `+` to `−`. There is no intermediate face. The fold is the same
  discrete exception as in the fold ledger: a reflection changes sign without a path.

So the claim's sentence "the front disappears the exact moment the back reveals itself" is exact for
the fold and slightly too strong for the turn. In the turn, the front disappears at `s = 0` and the
back appears only after; the instant between is the crease. In the fold, the exchange is one step.

## The shadow is the quotient

The shadow analogy is exact if the shadow is `π_H`. The kernel is the axis of the back: the normal
line. The projection drops the coordinate, and with it the sign; that is why the shadow is side-blind.
But the kernel is not a hidden region; it is the direction the projection forgets.

The folded line from afar is the simplest instance: a line crossing the crease becomes a V, `π_H` sends
it to the crease, and the length remembers the fold at second order. See `the-fold-afar.md`.

A `d`-dimensional observer measures a `d`-form. The measurement selects `d` directions, and the
complement has `n−d`. The shadow is the case `d = n−1`: one forgotten direction. Raising `d` shrinks
the kernel, but it does not abolish it until `d = n`; at `d = n` there is no kernel and no outside.
The observer is the whole space, not a viewer of it. That is the exact sense in which "stepping off
the wall" is possible: you gain directions, but you lose the outside. There is no dimension at which
you keep both the whole object and a place to stand.

The "Planck-sized hole" is a physicalization of the kernel. The Fold has no Planck scale and no hole:
the kernel is the normal line, and its size is not a length. The "infinite zero substrate" is not in
the model either. The zero is `k = 0`, one value, not a medium. The "binary code" is the fold ledger
(`0` = crease, `1` = normal); the "infinite zero" is the scale ledger (`k = 0`). They are two
ledgers, not the front and back of one pixel.

## The twist is not the ratchet

`J` is a rotation: `det J = +1`, and `J² = −I`. It preserves orientation. The orientation-reversing
object in the Fold is the fold, `det σ_H = −1`. So the twist is not a one-way mirror; it is a period.
Its invariant is the Pfaffian `Pf(ω) = 1`, not an arrow. It makes the loop, not the gate.

The one-way surface the idea is looking for does exist in the model, and it is not the twist. It is
the **horizon**: a null crease, `n·n = 0`, where the fold degenerates and the induced form is
`(n−2,0,1)` in a Lorentzian `n`-manifold. Timelike curves cross a null surface one way; that is a
causal ratchet, and it is exact. The twist has no such direction. The one direction the surface cannot
measure is the null radical; the invariant it leaves is the cross-section area. See `the-fold-area.md`.

Chirality in the Fold is the sign of `k` (mirror) and the parity of the fold count (orientation), not
a hidden back. "Information flows from the back to the front" is also not the fold: `σ_H` is an
involution and maps both ways. The only intrinsic arrow is the horizon's.

## Can you cheat?

There are six operations, and each has a cost.

| operation | what you get | what it costs |
|---|---|---|
| walk around / rotate | the other face, continuously | the first face; a moment of edge-on at the crease |
| fold `σ_H` | the other face as the image | orientation reverses; it is a reflection, not the same view |
| raise `d` | more directions at once | a new kernel appears unless `d = n`; at `d = n` there is no outside |
| `k = 0` | the crease / the centre | no observer; the distinction collapses |
| mathematics | the axis `s`, the quotient, the inertia, the index, `Pf` | a formula is a front-face object; you get the variable, not the value |
| a mirror | a reflected front | not the back; another front |

The answer is therefore: **the front face is a hard limit for measurement, not for knowledge.**

A measurement is a definite form with a definite orientation; it sees one side. That is not a wall
erected in front of the back; it is what a measurement is. But the axis `s` is neither face. It is the
variable whose two signs are the faces, and mathematics can see it. That is the real cheat: not a
glimpse of the back as a face, but the coordinate that generates both faces. The formula gives you the
blueprint of the back, and the blueprint is a front-face object — a symbol with a definite form — but
it is knowledge of the axis, which is more than the face can have.

"Deep awareness" is not an operation in this model. If it changes `d` or `k`, it is one of the rows in
the table. If it claims to see both faces at once, it claims a measurement with two opposite
orientations; that is not a measurement, it is the fold. To see both sides at once you would have to
**be** the fold, and the fold has no view. The zero is where the two sides meet, but it is not a
glimpse; it is the end of perspective.

## Checks

The algebra is exact; the numbers below are floating-point confirmations for `n = 2, 3, 4` with a
fixed probe point and a random unit normal.

| check | `n=2` | `n=3` | `n=4` |
|---|---|---|---|
| flip residual, `s(σ_H P) + s(P)` | `5.6e−17` | `1.1e−16` | `1.1e−16` |
| projection residual, `s(π_H P)` | `5.6e−17` | `0` | `2.8e−17` |
| metric residual, `Q(σ_H P) − Q(P)` | `1.1e−16` | `0` | `0` |

The first row is the flip, the second is the dropping, the third is the side-blindness of the metric.
The crease itself is exact: `s = 0` is fixed.

## What this does and does not say

- It **does** make "front and back" exact: the two signs of the normal coordinate, exchanged by
  `σ_H`, identified by `π_H`.
- It **does** explain the occlusion: a symmetric form is quadratic and even in `s`, so it is
  side-blind; an orientation is a sign, so it sees one side.
- It **does** locate the only meeting place: the crease `s = 0`, where the surface is edge-on.
- It **does** give the same two-ledger structure as the scale: a continuous turn crosses the crease;
  a fold jumps.
- It **does not** posit a Planck hole, a substrate, a hidden channel, or a signal. The kernel is the
  normal line; the zero is one value; `k` is a global parameter, not a channel.
- It **does not** make the twist a ratchet. The ratchet is the horizon.
- It **does not** claim that awareness is a geometric operation. If it is, it is `d` or `k`.

One more distinction, because the words collide: **the signature is not the side.** The signature
counts signed directions of a form; the side is the sign of one coordinate. The metric is even in
that coordinate, so it is side-blind. The zero's signature `(0,0,n)` is not "both sides"; it is no
signed directions. The occlusion is the difference between a form and a coordinate.

## The one sentence

**The back is not behind the front; it is the sign the quadratic form forgets. You can know it as the
axis, fold to it as its image, or collapse to it at the centre, but no look sees both faces, because
a look is a definite side.**

## Files

`the-fold-occlusion.md` (this note). The algebra of the fold and the projection is in
`the-fold-signature.md` and `the-fold-creation.md`; the one-way surface is in `the-fold-horizon.md`;
the `d`-form observer is in `the-fold-matter.md`. The critical line of the zeta function is a crease
of exactly this kind: see `the-fold-zeta.md`. The lookup is `the-fold-key.md`.
