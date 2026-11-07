# Horizon scaling: two laws, one letter

## What section 5 originally said

```
r_H ∝ k      A_H ∝ k²      S ∝ k²      T ∝ 1/k      M ∝ k
```

and then, two lines later,

```
k* = r_s/R
```

The first line is a statement about a *homothetic family*: scale every length by `k`, and since
`r_s = 2GM/c²` is itself a length, the mass scales with it. The second is a statement about a
*collapse*: the mass stays where it is and only `R` falls. They are different regimes, and the
paper was reading both off the same table.

## Why it cannot be one table

Under `r → kr` with `M → kM`, the horizon radius goes as `k` and the body radius goes as `k`, so
their ratio does not move:

```
r_H/R = 2GM/(c²R) = constant
```

Measured for the Sun at three members of the family:

| k | M (kg) | R (m) | r_H (m) | r_H/R | S/k_B | T (K) |
|---|---|---|---|---|---|---|
| 1 | 1.988e30 | 6.957e8 | 2.953e3 | 4.245134e−6 | 1.049e77 | 6.17e−8 |
| 0.5 | 9.942e29 | 3.479e8 | 1.477e3 | 4.245134e−6 | 2.622e76 | 1.234e−7 |
| 0.1 | 1.988e29 | 6.957e7 | 2.953e2 | 4.245134e−6 | 1.049e75 | 6.170e−7 |

The ratio is identical to thirteen digits. So in this family the horizon is **either present in
every member or in none** — for the Sun, none: `R/r_H = 2.36 × 10⁵` at every `k`. There is no
`k*` inside the family. That is not a paradox; it is the same statement the paper already makes in
section 6, that a purely geometric homothety descends to zero with nothing in the way.

## The two columns, measured

| quantity | homothetic family, `M ∝ k` | collapse, `M` fixed |
|---|---|---|
| `r_H` | `∝ k` | `= r_s`, constant |
| `A_H` | `∝ k²` | constant |
| `S = A_H/4ℓ_P²` | `∝ k²` | constant |
| `T` | `∝ 1/k` | constant |
| `M` | `∝ k` | constant |
| `R` | `∝ k` | `∝ k` |
| `r_H/R` | constant | `∝ 1/k` |

Fixed-mass values at formation, computed from `M` alone:

| body | `k*` | `r_s` | `S/k_B` | `T_H` |
|---|---|---|---|---|
| Earth | 1.392e−9 | 8.870e−3 m | 9.462e65 | 2.054e−2 K |
| Sun | 4.245e−6 | 2.953e3 m | 1.049e77 | 6.170e−8 K |
| 70 kg water sphere | 4.067e−25 | 1.040e−25 m | 1.300e20 | 1.753e21 K |

Note the ordering: the 70 kg sphere is the *hottest* horizon in the table by 29 orders of magnitude,
because `T_H ∝ 1/M`. Horizon thermodynamics is anti-correlated with size.

## The entropy does not accumulate

In the fixed-mass column, `S` and `T` are constants of the collapse. They do not grow as the body
falls; they are assigned when the horizon exists and not before. On this classical accounting the
entropy appears in one step at `k*`, which is exactly why "where did the entropy come from" is a
sharp question rather than a gradual one.

In the homothetic column both sides of the first law are non-zero and balance:

```
S = αM²,  T = β/M,  2αβ = 1  ⇒  T dS = dM
```

checked numerically: `T dS / (c² dM) = 1.00005` (the deviation is the finite-difference step). And
`S·T ∝ k`, halving when `k` halves — measured 6.472e69 → 3.236e69 for the Sun.

## What happens to `V/A`

| regime | `V` | `A_H` | `V/A_H` |
|---|---|---|---|
| homothetic | `∝ k³` | `∝ k²` | `∝ k` |
| fixed `M` | `∝ k³` | constant | `∝ k³` |

So the holographic conclusion survives and gets *stronger*: once the horizon exists, the bulk dies
three powers faster than its own boundary rather than one. At the moment of formation the ratio is

```
V/A_H = r_s³/(3 r_s²) = r_s/3
```

which is `984 m` for the Sun — the number the interactive shows when you slide onto `k*`.

## One caveat worth keeping

`V/A → 0` is a statement about the *collapsing body's own volume* against the horizon area. It is
not a statement that the interior of a black hole is small: on maximal spatial slices the interior
volume grows with the time elapsed since formation (Christodoulou–Rovelli), so an old black hole has
a large interior by that measure. The paper's `V` is the matter sphere, and the claim should stay
attached to it.

## What changed in the paper

Section 5's single table is now two columns, with the sentence that only the fixed-mass column is a
process. The `k*` table, the "below `k*`" paragraph and the `V/A` paragraph are retained; the last
now states the exponent for each regime instead of quoting `k²` for `A` in both.

Files: `the-fold.md`, `the-fold.tex`, rebuilt `the-fold.pdf` (6 pages, no warnings), and
`horizon-scaling.html` — the log–log chart where the two regimes draw a crossing pair or a parallel
pair, with `R`, `r_H`, `R/r_H`, `S`, `T`, `V/A_H` and the active law.
