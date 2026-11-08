# Every division point has its own fold

## The general law

The midpoint is the case `t = ½`. Let `t` be any fraction of the way from `P` to its image:

```
q_t(P) = (1 − t)P + t·g_k(P) = φP,     φ = 1 − t + tk = 1 + t(k − 1)
```

Again a homothety about the same datum, with `det q_t = φ²`. Measured over
`t ∈ {−1, −½, 0, ¼, ⅓, ½, ⅔, ¾, 1, 1.5, 2, 3}`, `k ∈ {−3 … 3}` and five probe points:
max deviation from `(1−t)P + t g_kP` is `2.512e−15`.

## The collapse value is a function of `t`

`φ = 0` when

```
k_t = (t − 1)/t = 1 − 1/t
```

| `t` | `k_t` | what it is |
|---|---|---|
| `¼` | `−3` | the quarter point |
| `⅓` | `−2` | the third point |
| `½` | `−1` | the midpoint — the fold |
| `⅔` | `−½` | |
| `¾` | `−⅓` | |
| `2` | `½` | beyond the image |
| `−1` | `2` | beyond the point |

Three facts, all measured:

**Every `k ≠ 1` is owned by exactly one division point**, namely `t = 1/(1−k)`. Round trip
`t → k → t` closes to `1.78e−15`. The single unowned value is `k = 1`, the identity: it is reached
only as `t → ±∞`.

**The pairing `t ↔ 1−t` sends `k ↔ 1/k`**, to `2.22e−16`. So the two division points equidistant
from the midpoint own reciprocal scalings. `k = −1` is its own reciprocal, which is why the midpoint
is the self-paired case — the fixed point of that involution.

**Only one division point has a fold as its midpoint map.** The midpoint map of the collapse of
division `t` has factor

```
(1 + k_t)/2 = 1 − 1/(2t)
```

which equals `−1` — the point reflection — only at `t = ¼`, and equals `0` — the constant map —
at `t = ½`. So the quarter point owns `k = −3`, and the midpoint of *that* collapse is the fold:

```
m(k = −3) = g_{−1} = the fold itself
```

Measured deviation from the formula: `0.0e+0` at `t = ¼`, `2.2e−16` at `t = ⅓`.

## Two evolutions, and they are not the same

**E1 — iterating the map.** Since `m_k = g_f` with `f = (1+k)/2`, composition multiplies factors:

```
m_k^n = g_(f^n),   verified exactly (0.0e+0) for n ≤ 6
```

so the orbit of a point is driven by `f^n`:

| `f` | limit of `f^n` | meaning |
|---|---|---|
| `f = 0` (`k = −1`) | `0` | absorbing: stays collapsed |
| `0 < |f| < 1` | `0` | the whole plane is pulled into the datum |
| `f = 1` (`k = 1`) | `1` | identity, fixed |
| `|f| > 1` | `∞` | the image escapes |
| `f = −1` (`k = −3`) | `1` after two steps | `m² = I` — period two |

The last row is the quarter point again: `k = −3` has `f = −1`, so `m_{−3}` is an involution, and
it is in fact `g_{−1}`, the fold.

**E2 — repeated bisection against the original.** If instead of iterating the map you keep halving
the segment from the *same* `P` to the successively updated image, the factor obeys
`f_{n+1} = (1 + f_n)/2`, whose solution is

```
f_n = 1 + (k − 1)/2^n
```

with no exception: every `k` converges to the identity, at one bit per step. Verified exactly for
`k ∈ {−3, −1, 0, ½, 2, 3}`. Repeated midpointing erases the scaling and keeps only the datum.

E1 and E2 are different processes that agree at `n = 1`. Confusing them would make `k = −1` look
like it drifts to `½` (E2) when as a map it is already constant and stays so (E1).

## The midpoints form a group

Because `m_a ∘ m_b = g_{f(a)f(b)}`, it is again a midpoint map, of

```
c = 2 f(a) f(b) − 1
```

so `{m_k}` is closed under composition, abelian, and isomorphic to `(ℝ*, ×)` through `f`. This is
the structural difference from folds: homotheties about one datum commute, reflections do not
(`σ_{H₂}σ_{H₁} = R(2α)`). The midpoint is the case where the group acts by averaging, and that is
why the order of the halvings does not matter.

## What is preserved

A homothety preserves the cross-ratio of any four collinear points. Checked for
`k ∈ {−2, ½, 2, 3}`: `CR = 1.250000000000` before and after, error `0.0e+0`. `k = −1` is excluded
because there all four points coincide and the cross-ratio is undefined — the rank drops to zero
and there is nothing left to compare.

So under both evolutions the datum is fixed, the cross-ratio is fixed, and only the scale moves.
The rank is the thing that can fail, and it fails at exactly one point.

## `wats` — two readings

If it was **what's**: the invariants above — datum, cross-ratio, the pairing `t ↔ 1−t`, and the
single unowned value `k = 1`.

If it was **watts**: the fold in this paper is an isometry, so the ideal fold costs no energy; any
energy statement needs a stiffness `κ` that the geometry does not supply. For a linear crease
`W = ½κθ²` with `θ = 2α`, so the twist by `90°` costs `4×` a single fold at `45°` if the crease
stiffness is the same — but `κ` is an input, not a result, and the paper has none. That is a
separate thread and would need a physical model before any number is worth quoting.

## What changed in the paper

Section 4 gains two sentences after the midpoint paragraph: the division-point law, the collapse
value `k_t = (t−1)/t`, the fact that every `k ≠ 1` is owned by exactly one division point, the
reciprocal pairing, and the quarter point whose midpoint map is the fold.

Files: `fold-division.html` (t and k sliders, the body / image / division polygon, the curve
`k_t = (t−1)/t` with the marked division points and the `k = 1` asymptote, `?t=&k=&collapsed=1`
deep link), `the-fold.tex` / `.md` / rebuilt `.pdf`.
