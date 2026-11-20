# The hexagon: the last lattice closure, and the gap it can host

## The last closure

The crystallographic restriction ends at `m = 6`. Six folds at `α = 30°` close,

```
(σ₂σ₁)^6 = I ,     2αm = 2π ,     D₆ of order 12 ,     2 cos 60° = 1 ,
```

and no larger `m` is an integer trace. The hexagon is the polygon this closure draws: interior angle
`2π/3`, exterior `π/3`, six creases. It is also the Voronoi cell of the triangular lattice and the
Brillouin zone of the honeycomb, and the Dirac points sit at its corners `K` and `K′`.

| `m` | `α` | group | order | creases |
|---|---|---|---|---|
| 3 | 60° | `D₃` | 6 | 3 |
| 6 | 30° | `D₆` | 12 | 6 |

The two are nested, `D₃ ⊂ D₆`, and the index is `2`. That `2` is the first sign that the hexagon has a
two-valued label: the 3-fold rotations preserve it, the 6-fold rotations exchange it.

## The hexagon is not the circle

A regular `n`-gonal pyramid with aperture `θ` has an apex angle between adjacent base vertices given by

```
cos α_n = sin²θ cos(2π/n) + cos²θ ,
```

and its intrinsic defect is `δ_n = 2π − n α_n`. The circular cone is the limit `n → ∞`, where
`n α_n → 2π sin θ` and `δ → 2π(1 − sin θ)`. At `n = 6` the two differ:

| `θ` | `δ₆` hexagonal pyramid | `δ` circular cone | difference |
|---|---|---|---|
| 30° | 3.2510 | 3.1416 | 0.1094 |
| 45° | 1.9468 | 1.8403 | 0.1065 |
| 60° | 0.9092 | 0.8418 | 0.0674 |
| 90° | 0.0000 | 0.0000 | 0.0000 |

They agree only at `90°`, where both are zero. So "the hexagon's defect is the cone's deficit" is a
false friend: the hexagon is the `n = 6` polygon, and the circle is its limit. The difference is a
discrete-versus-smooth effect, not an error — but it is not zero.

## The honeycomb's two cosets

The honeycomb is the triangular lattice with a two-site basis, `A` and `B`. A `60°` rotation about a
hexagon centre maps `A` to `B`; a `120°` rotation maps `A` to `A`. So the sublattice label is the coset

```
D₆ / D₃ ≅ ℤ/2 .
```

The same `60°` rotation maps `K` to `K′`, so the two valleys are the same two cosets. One `ℤ/2`, two
readings: sublattice and valley.

The Fold's `F(x, y) = (x, |y|)` is a quotient of the *space*; the honeycomb's `ℤ/2` is a coset of the
*point group*. Same abstract group, different bundle — that is the false friend. And the swap is a
rotation (`det = +1`), not a reflection: a single fold cannot exchange the sublattices, while the
product of two folds can. So "the two sublattices are the two layers" is a rhyme of the `ℤ/2`, not an
identity of objects.

One correction, developed in `the-fold-sign.md`: the hexagon carries **two** independent sign labels,
not one. `Hom(D₆, ℤ/2) ≅ (ℤ/2)²`, with the fold's determinant `(0,1)` and the sublattice character
`(1,0)` as separate bits, and their product `(1,1)` as a third index-2 subgroup `⟨r², rs⟩`. The
sublattice sign exists precisely because `6` is even; on a `D₃` lattice the only character is the
determinant. So the sublattice coset is not a rival reading of the fold's `ℤ/2` — it is an
independent coordinate on the same group.

The six zero-lines are also the actual crease-reflection axes: for \(h(z)=\operatorname{Re}(z^6)\), they occur at \(15^\circ+30^\circ j\). Even-index axes pass through opposite vertices and preserve the A/B label; odd-index axes pass through opposite edge midpoints and exchange it. The full unlabelled point group is \(D_6\), while the A/B-preserving subgroup is \(D_3\). See `the-fold-hexagonal-lattice.md` for the explicit two-character derivation and tested crease catalogues.

## The Dirac mass gap, hosted

Take the nearest-neighbour tight-binding model,

```
H = −t Σ_{<ij>} c†_i c_j ,      h(k) = −t [ 0    f(k) ]
                                          [ f*(k) 0   ] ,
f(k) = Σ_{j=1}^{3} e^{i k·δ_j} .
```

At `K = (4π/(3√3), 0)` with `δ = {(0,1), (−√3/2,−1/2), (√3/2,−1/2)}`,

```
f(K) = 1 + 2 cos(2π/3) = 0 ,      |∇f|(K) = 3/2 ,
```

so the low-energy Hamiltonian is

```
h ≈ v_F (q_x σ_x + q_y σ_y) ,      v_F = 3t/2 .
```

Add the Semenoff mass `m σ_z`, the difference of on-site energies on `A` and `B`:

```
E(q) = ±√(v_F² q² + m²) ,      gap = 2|m| .
```

This is an exact spectral gap in the toy model. The mass is the `A`/`B` splitting; the Fold has no
Hamiltonian, so the toy supplies the whole spectral side. The Fold supplies the hexagon, the `D₆/D₃`
coset, and the `ℤ/2` — not the gap.

## Corrugation is gauge, not mass

A strain or a varying corrugation enters the Dirac equation as a pseudo-vector potential,

```
q → q − A ,      E = ±v_F |q − A| ,
```

so it shifts the Dirac point and leaves the spectrum gapless. A gap needs the mass term, which is a
sublattice splitting. The two structures are different, and the distinction is exact in the model:

- corrugation → `A`, a gauge field; the cone shifts, the gap stays closed;
- `A`/`B` asymmetry → `m`, a mass; the gap opens, the cone stays at `q = 0`.

So "the mass gap is the imaginary fabric" is the false friend; "the mass gap is the layer asymmetry in
the host" is exact. The corrugated fabric of `the-fold-afar.md` gives the geometry, not the gap.

## What the Fold supplies, and what it does not

| object | Fold | host |
|---|---|---|
| hexagon, `D₆`, `30°` closure | exact | — |
| `D₆/D₃ ≅ ℤ/2` | exact | — |
| hopping `t`, Bloch `f(k)` | — | input |
| mass `m`, gap `2\|m\|` | — | exact in the toy |

"The hexagon is the mass gap" is a false friend. "The hexagon is the lattice on which a mass gap can be
hosted" is exact — and the host's gap is the `A`/`B` splitting, not the corrugation.
