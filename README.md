# The Fold

**Scale, twist, collapse — and what is left at the centre.**

Scaling about a datum is the one-parameter family `g_k(P) = P₀ + k(P − P₀)`. Everything in this
paper follows from one determinant, `det(g_k) = kⁿ`: heights scale like `k`, areas like `k²`,
volumes like `k³`. A real `k` changes size, an imaginary one twists, and a twist is the product of
two folds.

**Start here:** `the-fold-key.md` — the master key. Give it a value of `k`; it returns the stage,
the operation, what appears, what survives, and the note that proves it.

**Matter reading:** matter is the zero at a scale — stages 0–1 of the chain. In the homothetic
family `h ∝ k`, `M ∝ h`, `A ∝ h²`, `V ∝ h³`, `S ∝ h²`, `T ∝ 1/h`, while the horizon ratio `k*`
stays constant. Shape is the aperture `θ`; turn is `arg k`. A `d`-dimensional observer measures
`h^{p−d}` — scalar, derivative, flux, density for `d = 0, 1, 2, 3`. See `the-fold-matter.md`.

**Two nothings:** `k = 1` is the identity — nothing changed; `k = 0` is the collapse — nothing has
size. The creation loop returns the second, not the first.

**Two ledgers:** the fold ledger is additive — zero is a crease `H`, one is its unit normal `n`, and
each fold has its own pair, so `0 → 1 → 0 → 1` can be a chain of distinct terms. The scale ledger is
multiplicative — its zeros `k_t` are distinct but its one `k = 1` is unique. See `the-fold-key.md`.

**Signature of nothing:** the zero is totally null, inertia `(0,0,n)` — `n` directions, none signed.
Its scalar signature is `0`, but so is the planar fold's; the nullity is the fingerprint. A
continuous sign change must cross a degenerate form, and `k = 0` is that crossing. By stage: point
`(0,0,n)`, scale `(n,0,0)`, fold `(n−1,1,0)`, twist symplectic (`Pf=1`), horizon null. See
`the-fold-signature.md`.

**Occlusion:** the back of a surface is not a place; it is the sign of the normal that a quadratic
measurement forgets. The fold flips it, the projection drops it, and the crease is the only place the
two sides meet. Mathematics can see the axis, not both faces; the one-way surface is the horizon, not
the twist. See `the-fold-occlusion.md`.

**Reading paths:**

| if you want | read |
|---|---|
| the whole argument in six pages | `the-fold.pdf` |
| the lookup by value of `k` or by question | `the-fold-key.md` |
| the order of creation and the plain-language version | `the-fold-creation.md` |
| matter as the zero at a scale | `the-fold-matter.md` |
| the signature of nothing and the fold's split | `the-fold-signature.md` |
| why the back cannot be seen | `the-fold-occlusion.md` |
| the interactive models | the nine HTML files |

## Contents

| file | what it is |
|---|---|
| `the-fold.pdf` | the paper, 6 pages |
| `the-fold.tex` | LaTeX source (TeX Live, `pdflatex`) |
| `the-fold.md` | Markdown source |
| `the-fold-key.md` | master key: the `k`-plane, the chain, the four laws, and an index by question |
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
| `the-fold-creation.md` | follow-up note: the order of creation — point, scale, fold, twist, closure, horizon, observer, point; plain-language version and glossary |
| `the-fold-matter.md` | follow-up note: matter as the zero at a scale; the height law, its exponents, and the mass reading |
| `the-fold-signature.md` | follow-up note: the signature of zero — inertia, the forced degeneracy, the fold's split, and the ladder by stage |
| `the-fold-occlusion.md` | follow-up note: the back is not a place — side versus axis, the crease, and why the twist is not the ratchet |

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

The observer table is that formula at three apertures: `180°` at the centre, `90°` on the surface,
`arcsin(r/d)` outside. Inverting the paper's `5.060%` gives `d = 2.281 r`, and that one ratio
reproduces `1.216%` and `0.301%` at `k = 0.5, 0.25`. A cone's fold group is the planes through its
axis (residual `0.0`), not the point reflection; a turn about that axis is the *identity* on the
body, so the twist is exact `0.0%` at every angle for a cone as for a sphere — only the cube's
finite symmetry shows it (`12.3%` at `45°`). Collapsing the family leaves the aperture intact as a
limit of directions (`60.0000°` at `k = 1`, `10⁻³`, `10⁻⁶` alike while the range falls six orders),
and the cap alone yields `R = √(A_cap/Ω)`, `θ = 2 arcsin √(Ω/4π)` to `10⁻¹⁵`.

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
