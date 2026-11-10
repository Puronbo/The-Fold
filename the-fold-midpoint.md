# The datum is forced to the midpoint

## The claim in one line

Halve the segment from a point to its image under the scaling. What you get is the same scaling
again, with the factor replaced by its average with 1:

```
m_k(P) = ½(P + g_k P) = g_((1+k)/2)(P)
```

That is exact, and it has one consequence that the fold needs: the map `m_k` is a homothety whose
determinant is `((1+k)/2)ⁿ`, so it degenerates at exactly one value of `k` — and that value is the
fold.

## Check

With `g_k(P) = P₀ + k(P − P₀)` and `m_k(P) = ½(P + g_k(P))`:

```
m_k(P) = ½(P + P₀ + kP − kP₀)
       = ½((1+k)P + (1−k)P₀)
       = P₀ + ((1+k)/2)(P − P₀)
       = g_((1+k)/2)(P)
```

Measured over `k ∈ {−1.5, −1, −0.5, 0, 0.3, 0.5, 1, 2, 2.5}` and five probe points, the largest
discrepancy between the two sides is

```
max |m_k(P) − g_((1+k)/2)(P)| = 4.578e−16
```

which is roundoff. And `det m_k = ((1+k)/2)ⁿ` holds exactly in `n = 2` and `n = 3`; the measured
deviation from the formula is `0`.

## The one value that collapses

`det m_k` vanishes when `(1+k)/2 = 0`, i.e. at `k = −1`, and only there. At that value the map is
constant: every midpoint is the datum, independent of `P`. So

| map | rank | fixed set |
|---|---|---|
| `m_k`, `k ≠ −1` | `n` | the datum, alone |
| `m_k`, `k = −1` | `0` | everything (constant) |
| `m_(σ_H) = ½(I + σ_H)` | `n − 1` | the crease `H` |

The third row is the honest fold. For a reflection `σ_H` in a hyperplane through `P₀` with unit
normal `u`, `½(P + σ_H P)` is the orthogonal projection of `P` onto `H`. Checked in 3D on four
points:

```
midpoint lies in H                     err = 2.22e−16
P − σ_H(P) parallel to u               err = 5.44e−16
|P σ_H(P)| / 2 = dist(P, H)            err = 1.11e−16
```

So the crease is the **fixed set of the midpoint map**, and the point reflection is the endpoint of
that family where the fixed set has shrunk to the datum. The paper's phrase — the datum becomes the
hinge — is the `rank n − 1 → rank 0` degeneration, and `k = −1` is where it happens.

## Everything is 0

At that point the statement is stronger than "rank 0": every quantity the paper tracks vanishes
together, because they are all the same quantity read at different degrees.

```
det m = 0        rank 0        V = k³V₀ = 0
h = k·h₀ = 0     A = k²A₀ = 0  every distance = 0
coordinate offset from P₀      = 0     (image is P₀, for every P)
```

And there is a reason it is *that* point and not another. The midpoint of the two isometries of the
scaling group is

```
½ (I + (−I)) = 0,
```

and `0` is not a scaling — it is the boundary of the group. So **the midpoint of the group's two
isometries is the one element the group does not contain.** That is why everything is zero there:
`k = 0` is not a small motion, it is the compactification point, the place where the orbit closes.
The paper already says this ("outside the group", "the compactification of every orbit"); the
midpoint calculation is the third way to say it, and the one that shows it is forced by the group
structure rather than added by hand.

Two derivations, one map: the parameter midpoint of `{+1, −1}` is `0`; the zero locus of the
midpoint map is `k = −1`, where `m = g_0`. Both land on the same constant map, and its image is the
centre.

What survives is the only thing that was never a measure. At `k = 10⁻⁹` the range is `10⁻⁹` and the
aperture is still `60.0000°`, unmoved. So "everything is 0" is exact for every measure and false for
shape, and the exception is precisely the 0-dimensional vertex: zero of every measure, all of the
direction.

## The imaginary diameter

The real pair `±1` is not the only antipodal pair of isometries. Every `k` with `|k| = 1` is one — a
rotation by `arg k` with no scaling — and the midpoint of *any* antipodal pair is the zero:

```
½ (g_k + g_(−k)) = 0        for every k, real or imaginary
```

| pair | `k` | midpoint | what it is |
|---|---|---|---|
| `{I, −I}` | `±1` | `0` | identity and point reflection |
| `{J, −J}` | `±i` | `0` | the two quarter turns, opposite senses |
| `{e^{iθ}, e^{−iθ}}` | any unit `k` | `0` | any diameter of the isometry circle |

So the zero is not a fact about the real axis. It is the **centre of the circle**, and the imaginary
diameter is the test that proves it: `(±i)² = −1`, so the twist squared *is* the fold, and the two
diameters are one object seen through one equation.

Two things to keep apart, since they are one letter away:

- the midpoint **map** at `k = i` does not vanish: `½(1 + i)` is a 45° rotation at ratio `1/√2`
  (`|m| = 0.7071`, `arg = 45.0°`);
- the midpoint of the **pair** `{g_i, g_(−i)}` is exactly `0`, for the same reason the pair `{I, −I}`
  is.

And because `|k| = 1` everywhere on the circle, the distance from the zero to every isometry is the
same: the centre is the **circumcentre** of the group of isometries. That is the geometric content of
"the midpoint where everything is 0" — not the midpoint of one segment, but the one point that is
equidistant from all of them.

## Three named members

| `k` | factor `(1+k)/2` | what is at the midpoint |
|---|---|---|
| `−1` | `0` | the datum is the midpoint of every pair |
| `½` | `¾` | the image is the midpoint of datum and point |
| `2` | `3/2` | the point is the midpoint of datum and image |

The last two are reciprocals, and they are the same statement viewed from either end of the
segment: at `k = ½` the image is halfway from the datum to `P`; at `k = 2` the point `P` is halfway
from the datum to the image. Worked for `P = (1.2, 0.9)`, `P₀ = (0.35, −0.2)`:

| `k` | image | midpoint | verdict |
|---|---|---|---|
| `−1` | `(−0.50, −1.30)` | `(0.35, −0.20)` | midpoint is exactly `P₀` |
| `0.5` | `(0.775, 0.350)` | `(0.988, 0.625)` | image = `½(P₀ + P)` |
| `2` | `(2.05, 2.00)` | `(1.63, 1.45)` | `P = ½(P₀ + image)` |

## Two places this is already the rule

**Origami, axiom 2.** "Given two points, fold one onto the other." The crease that does it is the
perpendicular bisector of the segment, and the midpoint of the segment lies on it. Axiom 2 is the
statement that a fold is determined by a **midpoint**, not by a datum — which is the same shift the
paper makes when it says the fold fixes a crease rather than a point. The map that sends `P` to
`σ_H(P)` has `m = ½(P + σ_H P)` on the crease, and the crease *is* the set of all such midpoints.

**The neutral axis.** In bending, the strain is `ε = −y/ρ` about the centroid: the fibre that does
not change length is the one through the centroid, not the one at the surface or the one at the
datum. The crease plays the role of that fibre — the locus that the map leaves fixed while everything
else is scaled or reflected. This one is a structural analogy, not a theorem of the fold; it is
recorded because it is the same word "fixed set" doing the same work.

## What changed in the paper

Section 4 gains one paragraph after "The degeneration": the midpoint law, its determinant, the
statement that `k = −1` is the unique member where the midpoint map is constant, and the comparison
with the true fold, whose midpoint map is the projection onto the crease (rank `n − 1`). No other
section is touched; the `k = ½` / `k = 2` pair is named in the same paragraph.

Later, section 9's closing sentence changed from "terminates in a point" to "degenerates at `k = 0`
onto the centre that was there all along": the point is not where the family ends, it is where it is
centred. The two derivations above are why — the zero is a midpoint, and a midpoint is what the ends
share, not where they stop.

Files: `fold-midpoint.html` (interactive: `k` slider, the body, its image, and the midpoint polygon;
readouts for `det g_k`, the midpoint factor, `det m_k`, rank, spread, and the special values
`k = −1, ½, 2, 0`; `?k=` deep link), `the-fold.tex` / `.md` / rebuilt `.pdf`.
