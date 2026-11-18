# The integer line, bent

## The object

Bend the integer line at `c` and measure heights from the crease:

```
h(n) = |n − c| ,      n ∈ ℤ .
```

Two numbers meet at the same height exactly when they are symmetric about `c`:

```
h(n) = h(m)   ⟺   n + m = 2c .
```

So the bend is the involution `n ↦ 2c − n`, and its pairs are the orbits. Everything depends on one
arithmetic question: **is `2c` even, odd, or neither?** — that is, does the crease land on a number or
in a gap.

| crease `c` | fixed numbers | pairs | quotient | zone |
|---|---|---|---|---|
| `0` | `0` | `n ~ −n` | `ℕ`, the height | exact |
| `1/2` | none | `0 ~ 1`, `−1 ~ 2`, `−2 ~ 3` | `ℕ≥1`, the height | exact |
| `k/2`, `k ∈ ℤ` | `k/2` if `k` even | symmetric about `k/2` | `ℕ + k/2` | exact |
| irrational | none | `n ~ 2c − n` | a countable set | exact |

The middle row is the one the sentence is about. Bend at `1/2` and `0` and `1` sit at the same height,
`1/2`; bend at `0` and `0` sits alone at height `0`, meeting only itself. **A crease on a number fixes
it; a crease in a gap pairs every number.** On ℤ there is no third case.

## Height means two things, and only one of them is exact

The distance to the crease is `|n − c|`, and it is always equal for a pair. The *drawn* vertical height
is not: a V with arms of unequal slope puts the two numbers at different vertical heights while keeping
their distances equal. So:

- "two numbers meet at the same distance from the crease" is exact for every bend;
- "two numbers meet at the same height" is exact for the **symmetric** bend, arms at equal slope;
- the fold is the symmetric bend taken flat, `β = π/2`.

The invariant is the distance. The word "height" is the drawing.

## The bend is not a curvature

A V is an isometric image of the line: parameterize by arc length and it is `s ↦ (|s|/√2, s/√2)`,
unit speed, no stretching. So bending the integer line does not change any distance along it and does
not curve it. What it does is concentrate **turning** at the vertex:

```
turning = π − 2β ,
```

with `2β` the interior angle of the V. A straight line has `β = π/2` and turning `0` — that is the
fold, whose crease is straight. A hairpin has `β = 0` and turning `π`.

One dimension up the same statement is the cone's deficit, with the full angle `2π` in place of `π`:

```
turning₂ = 2π − 2π sin θ = δ .
```

So the V and the cone are the same kind of object: flat everywhere except one point, where the entire
turning sits. Calling the bent line "curved" is the false friend — the intrinsic metric is flat and the
curvature is a point charge at the crease. Calling it "flat with a kink" is exact.

## The clock

Wind the line into `ℤ/n`. The bend `n ↦ 2c − n` becomes `k ↦ 2c − k (mod n)`, and the two canonical
creases are `c = 0` and `c = 1/2`:

| `n` | `k ↦ −k` fixes | `k ↦ 1 − k` fixes | total | orbits of the second bend |
|---|---|---|---|---|
| 3 | `0` | `2` | 2 | 2 |
| 4 | `0, 2` | — | 2 | 2 |
| 5 | `0` | `3` | 2 | 3 |
| 6 | `0, 3` | — | 2 | 3 |
| 7 | `0` | `4` | 2 | 4 |
| 8 | `0, 4` | — | 2 | 4 |

Two facts are exact and both are about `2`:

- the two bends fix **two numbers in total**, for every `n ≥ 3`. Each congruence `2k ≡ b (mod n)` has
  `gcd(2, n)` solutions for `b = 0` and `0` or `1` for `b = 1`, and `gcd(2, n) + [gcd(2, n) = 1] = 2`;
- `n = 2` is the one degenerate case, where `−1 = 1` makes both bends the identity and both fix
  everything. The clock with two hours has no crease.

For `n` even the two bends look completely different — one holds two numbers, the other holds none.
For `n` odd both hold exactly one, and they are conjugate: `r s r⁻¹ = r² s` steps the offset by `2`,
which generates every residue when `n` is odd. **Conjugacy is the failure of the label**: a character
cannot separate what the group conjugates.

## Where two numbers meet is the hexagon's second bit

The reflections of the `n`-gon act on the clock as `k ↦ a − k`, and the character `(1, 0)` of
`the-fold-sign.md` is

```
χ(r^a s) = (−1)^a .
```

So `χ = +1` exactly on the creases that hold **two** numbers and `−1` on the creases that hold
**none** (`n` even). The abstract second bit has a concrete reading:

> the hexagon's `(1, 0)` is the parity of the reflection's offset, i.e. whether the crease falls on a
> number or in a gap.

That is exactly the sentence "two numbers meet at the same height": the crease is in a gap, the two
neighbours are the pair, and the gap is what the bit records. For `n` odd there is no such bit —
because there is no such gap.

The Fold's own bit is the other character, `(0, 1)`: rotation versus reflection, `det`. On the clock
that is the statement that `k ↦ −k` reverses the cyclic order and `k ↦ k + 1` does not. So the bent
integer line carries both signs of `(ℤ/2)²`, and it carries them in the only way a one-dimensional
body can: one from the orientation of the line, one from whether the crease has a number on it.

## Discreteness keeps the fold and loses the doubling

The bend is an involution, so as a dynamical system it does nothing after the first step: every orbit
is a point or a pair. All the interesting dynamics in the corpus comes from composing the bend with a
**doubling** — the tent map is

```
T = fold ∘ double ,      T(x) = 1 − |2x − 1| on [0, 1] ,
```

and chaos lives in the doubling, not in the fold. On the integers the doubling does not stay in the
interval (`2(1 − n) = 2 − 2n < 0` for `n ≥ 2`), and the bend alone is idempotent. So:

- the fold is discrete-friendly: it is an involution on `ℤ`, on `ℤ/n`, on any set;
- the doubling is not: it needs a bounded continuum, which is why `the-fold-cone.md`'s logistic thread
  is a chart on the interval and not a structure of the lattice.

"The integer line is chaotic when folded" is a false friend. "The integer line folds, and the interval
doubles" is exact, and it names the premise the chaos needs.

## The restatement

Bend the integer line at `c`. Two numbers meet at the same distance from the crease, and their common
distance is the quotient — that is why only height matters. Whether the crease holds a number or a gap
is a single bit, and it is the second bit of the hexagon.
