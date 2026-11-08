# The Fold

**Scale, twist, collapse — and what is left at the centre.**

Scaling about a datum is the one-parameter family `g_k(P) = P₀ + k(P − P₀)`. Everything in this
paper follows from one determinant, `det(g_k) = kⁿ`: heights scale like `k`, areas like `k²`,
volumes like `k³`. A real `k` changes size, an imaginary one twists, and a twist is the product of
two folds.

## Contents

| file | what it is |
|---|---|
| `the-fold.pdf` | the paper, 6 pages |
| `the-fold.tex` | LaTeX source (TeX Live, `pdflatex`) |
| `the-fold.md` | Markdown source |
| `j-plane.html` | 2D model: `A ∝ k²`, `h ∝ k`, the rotation `J` |
| `j-cone-3d.html` | external apex: tangent cone, dimension ladder |
| `j-collapse-3d.html` | sphere/cube collapse: rank, `Ω/4π`, observers at the centre and outside |
| `fold-closure.html` | the closure law: drag `α`, watch `D_m` appear or the orbit go dense |
| `the-fold-closure.md` | follow-up note: `closure m = π/α`, the crystallographic restriction |
| `horizon-scaling.html` | log–log chart: homothetic family vs fixed-mass collapse |
| `the-fold-horizon.md` | follow-up note: why the horizon table needs two columns |
| `fold-midpoint.html` | the midpoint map: `m_k = g_((1+k)/2)`, constant at `k = −1` |
| `the-fold-midpoint.md` | follow-up note: the crease is the midpoint locus |
| `fold-division.html` | every division point's own collapse value, `k_t = (t−1)/t` |
| `the-fold-division.md` | follow-up note: division points, two evolutions, the group law |
| `fold-invariants.html` | live audit: what scaling keeps, what folding keeps, side by side |
| `the-fold-invariants.md` | follow-up note: orbit spaces, invariant rings, `k = −1` as the meeting point |
| `cone-range-3d.html` | 3D range cone: apex at the centre, rim at the range, `θ` and `k` sliders |
| `the-fold-cone.md` | follow-up note: the range cone, its three formulas, and the fold's antipode |

Open the HTML files directly in a browser — no build step, no dependencies.

## Build

```
pdflatex the-fold.tex
pdflatex the-fold.tex
```

## Measured values quoted in the paper

Silhouette change of a cube twisted about a face axis: 0.0% at 0°/90°/180°/270°, 1.4% at 30°,
**12.3% at 45°**; sphere 0.0% at every angle.

Solid angle seen by an exterior point, `Ω/4π`: 5.060% at `k = 1`, 1.216% at `k = 0.5`, 0.301% at
`k = 0.25`. At the centre of the body it is exactly 100% for every `k > 0`.

Horizon formation, `k* = 2GM/(c²R)`: Earth `1.4 × 10⁻⁹`, Sun `4.3 × 10⁻⁶`, a 70 kg sphere of water
`4 × 10⁻²⁵`.

The midpoint map: `m_k(P) = ½(P + g_k P) = g_((1+k)/2)(P)` to `4.6 × 10⁻¹⁶`, with
`det m_k = ((1+k)/2)ⁿ` exact and rank 0 only at `k = −1`. For a fold `σ_H`, `½(I + σ_H)` is the
projection onto the crease (rank `n − 1`): the midpoint set lies in `H` to `2.2 × 10⁻¹⁶`.

Division points: `q_t = (1 − t + tk)P`, collapsing at `k_t = (t − 1)/t` — ¼ ↦ −3, ⅓ ↦ −2, ½ ↦ −1,
2 ↦ ½. Every `k ≠ 1` is owned by exactly one `t = 1/(1−k)` (round trip `1.8 × 10⁻¹⁵`), and
`t ↔ 1−t` pairs `k` with `1/k` to `2.2 × 10⁻¹⁶`. Map iteration is `m^n = g_(f^n)` exactly; repeated
bisection is `f_n = 1 + (k − 1)/2ⁿ`, converging to the identity for every `k`.

Invariants: a scaling changes every distance by `|k|` (relative `0.850` at `k = 1.85`) and holds
direction at `0°`; a fold holds distances at `0`, radius at `2.2 × 10⁻¹⁶`, and moves direction by
`87°`. `k = −1` is both — an isometry that reverses direction by `180°`. The cross-ratio of four
division points is `t(1−s)/(s(1−t))`, independent of `k` to `4.4 × 10⁻¹⁶`.

Range cone (a spherical sector, not a Euclidean cone): `Ω = 2π(1 − cos θ)`, `V = (R³/3)Ω`,
`A = R²(Ω + π sin θ)`. At `θ = 60°` and `R = 1`: `Ω = 3.1416`, `V = 1.0472`, `A = 5.8623`,
`V/A = 0.1786`, and `(V/A)/k = 0.17863` constant across `k`. `Ω` agrees with Monte Carlo to
`3.5 × 10⁻³` or better. The fold fixes the sector only at `θ = 180°`; otherwise it sends it to its
antipode, the overlap with which is `max(0, −cos θ)` of the ball (`0.50113` measured at `θ = 120°`
against `0.5`).

## Structure

0. Summary — the one determinant
1. The scale factor and the datum — area and height cannot share a law
2. Two regimes — sphere (interior apex) and cone (boundary apex)
3. The twist — `J² = −I`, and `U(1)/Sym(B)` as the observable quotient
4. The fold, completed — two folds at `α` give a rotation by `2α`; `(σ₂σ₁)⁴ = I`
5. The horizon — two laws: the homothetic family (`M ∝ k`) and the fixed-mass collapse
6. Zero as the point — rank drops from `n` to 0 in one step
7. What an observer can see — dimension fixes the observable
8. Devices — one bench-top instance per step
9. The one sentence
