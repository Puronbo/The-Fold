# The Fold in Lean 4

## What this is

A dependency-free Lean 4 library at the repository root. It imports only `Init`, so it builds
with the bare toolchain: no Mathlib, no network, no cache. The compiled statements are the exact
skeleton of the corpus — an involution, its fixed set, its quotient, the observer as a cut, the
scale action, the cap/puncture ledger, the calendar arithmetic, the wheel's closure, four finite
counterexamples from the second problem map, a non-vacuous quotient instance, the Euler
characteristic of the `m = 2` dessin, that dessin's monodromy, the `A1` node as a quotient, and the
scale action at `k = 2` on `ℤ/n`.

It proves the skeleton. It does not prove the rhymes. The distinction is the same four-zone rule
as the prose: a theorem is either exact, a model, or absent, and the file says which.

## Build

```
lake build
```

Expected last line: `Build completed successfully`.

The toolchain is pinned in `lean-toolchain` to `leanprover/lean4:v4.35.0`. The Lake package is
`fold`; the default target is the library `Fold`.

| file | contents |
|---|---|
| `Fold/Basic.lean` | the fold as an involution; fixed set, orbit, chart, cut |
| `Fold/Scale.lean` | the scale action on `ℤ`; the datum, the collapse, the ray |
| `Fold/Chi.lean` | capping, uncapping, puncturing, filling; the ledger and the space |
| `Fold/Arithmetic.lean` | the four formats mod `99`, the Gregorian cycle, the Unix weeks |
| `Fold/Wheel.lean` | the combinatorial wheel and its closure after `m` turns |
| `Fold/Problems.lean` | Simpson, tolerance, contraposition, Monty Hall |
| `Fold/Pressure.lean` | the linear hydrostatic law; monotone, unbounded, gauge |
| `Fold/Doubling.lean` | the scale action at `k = 2`: doubling on `ℤ/n`, its inverse, cycles, and the `n = 3` coincidence |
| `Fold/Examples.lean` | a non-vacuous descent on `Option Bool`; the `m = 2` dessin's Euler characteristic and monodromy; the `A1` node quotient |
| `Fold/Audit.lean` | the `#print axioms` audit |
| `Fold.lean` | the root module and the `#check` inventory |

## The exact core

### The fold and its quotient

A fold is an involution:

    structure Fold (X : Type) where
      f : X → X
      invol : ∀ x : X, f (f x) = x

The exact statements:

| Lean name | statement | zone |
|---|---|---|
| `Fold.Fix` | the fixed set of a fold: the crease, scar, horizon, or critical line | exact |
| `Fold.fix_iff` | `Fix F (F.f x) ↔ Fix F x` | exact |
| `Fold.Orbit` | the two sides: `y = x ∨ y = F.f x` | exact |
| `Fold.orbit_equivalence` | the orbit relation is an equivalence | exact |
| `Fold.chart_eq_iff` | `chart x = chart y ↔ Orbit x y` | exact |
| `Fold.chart_fold` | `chart (F.f x) = chart x`: the fold is invisible in the chart | exact |
| `Fold.desc` | an invariant function factors through the chart | exact |
| `Fold.desc_chart` | `desc g h (chart x) = g x` | exact |
| `Fold.desc_injective` | a separating invariant has injective descent | exact |
| `Fold.desc_bijective` | invariant, separating, surjective: the descent is a bijection | exact |

The last line is the formal content of "a fold is a change of chart, not a change of the quotient".
The quotient is the chart; the involution moves the representative and fixes the class.
`desc_bijective` is the quotient universal property in the form an instance needs: if `g` is
constant on orbits, separates them, and is surjective, then `g` *is* the quotient map. The
Joukowski map `J(z) = z + 1/z` is the instance with `g = J`: `J(1/z) = J(z)`, `J(z) = J(w)`
forces `w = z` or `w = 1/z`, and every value is attained.

### The observer as a cut

A cut is an idempotent retraction onto the fixed set that is constant on orbits:

    structure Cut (F : Fold X) where
      p : X → X
      image_fix : ∀ x, Fix F (p x)
      fix_eq : ∀ x, Fix F x → p x = x
      orbit_eq : ∀ x, p (F.f x) = p x

| Lean name | statement | zone |
|---|---|---|
| `Fold.Cut.idem` | `p (p x) = p x` | exact |
| `Fold.Cut.invisible` | `p (F.f x) = p x` | exact |
| `Fold.Cut.fix_iff` | `Fix F x ↔ p x = x`: the cut detects exactly the fixed set | exact |
| `Fold.Cut.lift` | the cut factors through the chart | exact |
| `Fold.Cut.lift_chart` | `lift (chart x) = p x` | exact |
| `Fold.Cut.lift_fix` | the image of the lifted cut is fixed | exact |

This is the one structure the file does not derive. A fold always has a quotient; it does not
always have a cut. A cut exists when a retraction onto the fixed set exists, and that is an extra
choice — the observer's. The formal asymmetry is the prose asymmetry: the quotient is canonical,
the cut is supplied.

### The scale action

On `ℤ`, the scale action is `g_k(x) = k x`.

| Lean name | statement | zone |
|---|---|---|
| `Fold.scale_one` | `g_1 = id` | exact |
| `Fold.scale_comp` | `g_{k l} = g_k ∘ g_l` | exact |
| `Fold.datum_fixed` | `g_k(0) = 0` for every `k` | exact |
| `Fold.scale_collapse` | `g_0` is the constant map to the datum | exact |
| `Fold.scale_fix_iff` | for `k ≠ 1`, `g_k(x) = x ↔ x = 0` | exact |
| `Fold.scale_moves` | for `k ≠ 1` and `x ≠ 0`, `g_k(x) ≠ x` | exact |

The integral model is deliberate: it makes `0` the unique fixed point and the collapse exact. The
reciprocal `k ↦ 1/k` needs a field, and is the completion `0 ~ ∞`; it is not in the integral slice.

### Capping and puncturing

A surface summary is `(χ, boundary, punctures)`. A cap raises `χ` by one and consumes a boundary
component; a puncture lowers `χ` by one and creates a puncture.

| Lean name | statement | zone |
|---|---|---|
| `Fold.uncap_cap` | `uncap (cap S) = S` when `S.boundary > 0` | exact |
| `Fold.fill_puncture` | `fill (puncture S) = S` | exact |
| `Fold.chi_puncture_cap` | `χ(puncture (cap S)) = χ(S)` | exact |
| `Fold.puncture_cap_ne` | `puncture (cap S) ≠ S` | exact |
| `Fold.cap_puncture_ne` | `cap (puncture S) ≠ S` | exact |

The first three are the ledger; the last two are the space. Capping and puncturing cancel on `χ`
and do not cancel on the space. That is the exact form of "cap and puncture are not inverses": they
are inverse on the ledger, not on the object. What is inverse to capping is uncapping; what is
inverse to puncturing is filling.

### The calendar

| Lean name | statement | zone |
|---|---|---|
| `Fold.formats_mod_99` | the four formats are all `56` mod `99` | exact |
| `Fold.formats_distinct` | the four formats are distinct labels | exact |
| `Fold.gregorian_cycle` | `146097 = 3³ · 7 · 773` | exact |
| `Fold.unix_weeks` | `972518400 = 1608 · 604800` | exact |
| `Fold.unix_week_residue` | `1608 ≡ 5 (mod 7)` | exact |
| `Fold.jdn_residue` | `2451844 ≡ 3 (mod 7)` | exact |

### The wheel

| Lean name | statement | zone |
|---|---|---|
| `Fold.rot` | one turn: `n ↦ (n + 1) % m` | exact |
| `Fold.rotIter_eq` | `k` turns from residue `n % m` give `(n + k) % m` | exact |
| `Fold.rot_period` | after `m` turns the mark returns | exact |

The analytic closure law `m = π/α` is not in this file; it needs `Real.cos`. What is in the file is
the combinatorial content: the wheel's period is the spoke count.

### The scale action at `k = 2`

The fold is multiplication by `−1`. The scale action at `k = 2` is multiplication by `+2`; the two
coincide only where the modulus divides `3`.

| Lean name | statement | zone |
|---|---|---|
| `Fold.double` | `x ↦ 2x` on `ℤ/n` | exact |
| `Fold.half` | the inverse `x ↦ (n+1)/2 · x` when `n` is odd | exact |
| `Fold.half_double` | `half ∘ double = id` for odd `n` | exact |
| `Fold.double_half` | `double ∘ half = id` for odd `n` | exact |
| `Fold.double_bijective_iff_odd` | doubling is bijective iff `n = 2m + 1` | exact |
| `Fold.double_bijective_iff_mod_two` | the same criterion as `n % 2 = 1` | exact |
| `Fold.double_iter` | the `k`-th doubling is multiplication by `2^k` | exact |
| `Fold.double_iter_eq_id_of_dvd` | `n ∣ 2^k − 1` implies `k` doublings are the identity | exact |
| `Fold.double_fixed` | the only fixed point is `0` | exact |
| `Fold.double_eq_neg_iff` | doubling equals the fold iff `n ∣ 3` | exact |
| `Fold.double7_orbits` | `0`, `1 → 2 → 4 → 1`, `3 → 6 → 5 → 3` | exact |
| `Fold.double7_one_period` | the period of `1` is exactly `3` | exact |
| `Fold.double7_iter_three` | three doublings return every residue mod `7` | exact |

The inverse is the reason parity matters: `(n+1)/2` is an integer exactly when `n` is odd, and then it
multiplies by `2` to `n+1 ≡ 1`. The fixed-point statement is the finite crease: doubling has a
one-point fixed set for every modulus, so unlike the fold it has no line to quotient by. Doubling and
the fold coincide exactly when `n ∣ 3`: trivially at `n = 1`, and at `n = 3` where `2 = −1`. The
reading of `+2` as `−1` away from `n ∈ {1, 3}` is a false friend. On `ℤ/7` the orbits are the
three cycles above, and `7 = 2³ − 1` is the arithmetic reason the third iterate is the identity.

### The finite counterexamples

| Lean name | statement | zone |
|---|---|---|
| `Fold.simpson_reversal` | treatment wins both strata and loses the pool | exact |
| `Fold.simpson_totals` | the pool is the sum of the strata | exact |
| `Fold.tolerance_not_trans` | tolerance is reflexive and symmetric, not transitive | exact |
| `Fold.tolerance_structure` | the three properties in one statement | exact |
| `Fold.contraposition` | `(P → Q) = (¬Q → ¬P)` on `Bool` | exact |
| `Fold.contraposition_invol` | the pair map `(a,b) ↦ (¬b,¬a)` is an involution | exact |
| `Fold.monty_two_of_three` | switching wins two of the three configurations | exact |

Simpson is the quotient that does not preserve order; tolerance is the relation that has no
quotient; contraposition is the involution that is logical and not evidential; Monty Hall is the
section that the host's action revises. Each is a finite computation, and each is a place where the
prose note says what the computation is allowed to touch.

### A non-vacuous descent

| Lean name | statement | zone |
|---|---|---|
| `Fold.swapFold` | the involution on `Option Bool` fixing `none` and swapping `some true`/`some false` | exact |
| `Fold.swapInv` | `false` on `none`, `true` on the two `some` values | exact |
| `Fold.swapInv_sep` | equal invariants force the same orbit | exact |
| `Fold.swapFold_desc_bijective` | `desc_bijective` at `swapFold`: the quotient is `Bool` | exact |

`swapFold` is the smallest non-free involution: one fixed point and one two-point orbit. The
quotient is therefore a two-point type, and `swapFold_desc_bijective` is an inhabited application of
`desc_bijective` — not a vacuous instance with one orbit. The descent is a bijection
`Chart swapFold → Bool`, and the witness `some true` shows the invariant is surjective.

### The `m = 2` dessin

| Lean name | statement | zone |
|---|---|---|
| `Fold.Dessin` | a spherical dessin: `V + F = E + 2` | exact |
| `Fold.Dessin.euler_eq_two` | `V + F - E = 2` | exact |
| `Fold.dessin2` | two vertices, two edges, two faces | exact |
| `Fold.dessin2_euler` | the `m = 2` dessin has Euler characteristic `2` | exact |

The `m = 2` dessin is the unit circle with the two marks `±1`: two vertices, two semicircle edges,
and two faces (inside and outside). The identity is `2 + 2 - 2 = 2`. It is the finite shadow of the
Belyi map `B(z) = (z+1)²/(4z)`, whose critical values `0` and `1` are the two vertices.

### The monodromy of the `m = 2` dessin

| Lean name | statement | zone |
|---|---|---|
| `Fold.dessinSheet` | the two sheets, labelled by `Bool` | exact |
| `Fold.dessinSigma0` | monodromy around `0`: the transposition `Bool.not` | exact |
| `Fold.dessinSigma1` | monodromy around `1`: the same transposition | exact |
| `Fold.dessinSigma0_invol` | `sigma0 ∘ sigma0 = id` | exact |
| `Fold.dessinSigma0_ne_id` | `sigma0 ≠ id` | exact |
| `Fold.dessinSigma_product` | `sigma0 ∘ sigma1 = id`: the loop around `∞` is unramified | exact |
| `Fold.dessinMonodromy_transitive` | one transposition already moves between the two sheets | exact |
| `Fold.dessin_passport` | the full passport in one conjunction | exact |
| `Fold.dessinMonodromy_group` | the generated group is `ℤ/2`, of order two | exact |

The degree-two cover `B : ℂ* → ℂ` has two ramification points: `z = −1` over `0` and `z = 1` over
`1`. With only two sheets, every ramification is a transposition, so the two monodromies coincide.
The third loop, around `∞`, is trivial because `B` is unramified there: `0` and `∞` are simple
poles. Riemann–Hurwitz checks the count,

```
2g − 2 = d(2h − 2) + R,   −2 = 2(−2) + 2,   R = (2−1) + (2−1) = 2,
```

so the cover is again a sphere. The Lean statements are the finite skeleton of that geometry: the
group is `ℤ/2`, the same abstract group as `rot 2`, and the passport is
`(2)(1,1)(1,1)`. Tracking the two roots of `B(z) = w`,

```
z = 2w − 1 ± 2√(w(w−1)),
```

along loops of radius `0.2` about `0` and about `1` swaps them (residual `3e−16`), and a loop of
radius `1.0` about both fixes them (residual `1e−15`); that is the passport numerically. What is not
in the file is the identification of these permutations with paths in the base; that needs the
topology of `ℂ ∖ {0,1}`.

### The `A1` node as a fold quotient

| Lean name | statement | zone |
|---|---|---|
| `Fold.nodeInv` | `(u, v) ↦ (−u, −v)` on `Int × Int` | exact |
| `Fold.nodeInv_invol` | the node map is an involution | exact |
| `Fold.nodeFold` | the node involution as a `Fold` | exact |
| `Fold.a1` | the three invariants `(u², v², uv)` | exact |
| `Fold.a1_invariant` | the invariants are constant on the node orbits | exact |
| `Fold.a1_cone` | `X Y = Z²` for `X = u²`, `Y = v²`, `Z = uv` | exact |
| `Fold.nodeFold_fixed` | the only fixed point is the origin | exact |
| `Fold.a1_fixed` | the invariants vanish exactly at the origin | exact |
| `Fold.a1Chart` | the descent of `a1` to the chart | exact |
| `Fold.a1Chart_chart` | the descent evaluates to the invariants | exact |

The Markoff surface is singular at `(0,0,0)`: the gradient vanishes and the Hessian is `2I`, so the
tangent cone is `x² + y² + z² = 0`. After `z ↦ i z` this is the `A1` cone `X Y = Z²`, and the map
`(u, v) ↦ (u², v², uv)` exhibits it as `ℂ² / (ℤ/2)`. The Lean section is the integer skeleton of
that quotient: the involution, its unique fixed point, the three invariants, and the descent. It does
not prove that the Markoff surface is locally biholomorphic to the cone — that is the holomorphic
Morse lemma — and it does not prove that the link is `SO(3) ≅ ℝP³`. Those two are recorded as
standard facts, not as compiled rows.

The point `(0,0,0)` is the quaternion point: `A = iσ₁`, `B = iσ₂`, `AB = −iσ₃`, so all three traces
vanish, `A² = B² = (AB)² = −I`, and the commutator is `−I` with trace `−2`. The Fricke identity
`x² + y² + z² − xyz = 2 + tr(ABA⁻¹B⁻¹)` holds exactly there. The node is not a defect of the
coordinate: it is the Fold's own `ℤ/2`, seen on the tangent plane.

### The hydrostatic chart

| Lean name | statement | zone |
|---|---|---|
| `Fold.pressure` | `p(h) = p0 + c h` | exact as a model |
| `Fold.pressure_strict` | pressure is strictly increasing with depth | exact |
| `Fold.pressure_unbounded` | every target pressure is exceeded at some finite depth | exact |
| `Fold.pressure_finite` | at a finite depth the value is the finite linear law | exact |
| `Fold.pressure_gauge` | shifting the datum shifts every pressure by the same constant | exact |

The pair `pressure_unbounded` and `pressure_finite` is the exact form of the pressure triad:
"increases until infinity" is true as an unboundedness statement over finite depths, and false as a
claim that a finite depth has infinite pressure. The real-valued law is `p(h) = p0 + ρ g h`; the
integer model normalizes `ρg` to a positive integer `c`.

## What the file does not prove

| missing statement | why it is missing | where it lives |
|---|---|---|
| `I_C(z) = ρ²/z̄` is an involution of `ℂ*` | needs `ℂ` and conjugation | `the-fold-loop.md` |
| `m = π/α` | needs `Real.cos` and the twist angle | `the-fold-closure.md` |
| `m ∈ {1,2,3,4,6}` (crystallographic restriction) | needs lattices and `2cos(2π/m)` | `the-fold-closure.md` |
| `S¹ ∖ {p} ≅ ℝ` | needs topology | `the-fold-chart.md` |
| amenability, `F₂`, Banach–Tarski | needs choice and measure theory | `the-fold-problems.md` |
| `p(z) = p0 e^{-z/H}` for the atmosphere | needs `Real.exp` and the ideal-gas law | the hydrostatic chart above |
| the order of doubling is the multiplicative order of `2` mod `n` | the file proves `n ∣ 2^k − 1 → double^k = id`, not that no smaller `k` works | the scale action above |
| the actual pressures at Challenger Deep and Earth's centre | unit conversions and a density model | the hydrostatic chart above |
| RH, BSD, Hodge, Yang–Mills, Navier–Stokes, P vs NP | the four walls; no formal proof exists here | `the-fold-problems.md` |
| the hard problem of consciousness | not a mathematical object | the absence named in the prose |

The `negFold` in `Fold/Scale.lean` is the real slice of the reflection `σ_H`: `x ↦ −x` on `ℤ`. It
is the fold with crease `0`, not the navel inversion. The navel inversion's real slice is
`x ↦ ρ²/x` on `ℝ*`; that involution is not in the file, and saying `negFold` is `I_C` would be the
false friend.

## Why this is the right core

The corpus's five roles are exactly the five Lean structures:

| role | Lean |
|---|---|
| datum | the type `X` and the fixed point |
| operation | `Fold.f` |
| fixed set | `Fold.Fix` |
| quotient | `Fold.Chart` |
| observer / return | `Fold.Cut` |

The roles are not decoration. `Fix` is a predicate, `Chart` is a quotient type, `Cut` is a
structure with a law, and `Fold` is an involution. A claim that does not fit one of these is either
a reformulation, a rhyme, or a false friend — which is the zone rule in formal dress.

## The four zones in the build

| zone | in the build |
|---|---|
| exact | every theorem in `Fold/` compiles with no `sorry`; the only axioms are Lean's core |
| reformulation | `Cut` models the observer; it is not a theory of consciousness |
| rhyme | `rot_period` is the combinatorial closure; `m = π/α` is the analytic statement left out |
| false friend | "the Lean project proves the Fold" — it proves the skeleton, not the flesh |

The axiom audit is reproducible with `#print axioms` in `Fold/Audit.lean`:

| theorem | axioms |
|---|---|
| `Fold.Cut.fix_iff` | none |
| `Fold.formats_mod_99` | none |
| `Fold.simpson_reversal` | none |
| `Fold.chart_eq_iff` | `propext`, `Quot.sound` |
| `Fold.desc_bijective` | `Quot.sound` |
| `Fold.swapFold_desc_bijective` | `Quot.sound` |
| `Fold.Dessin.euler_eq_two` | `propext` |
| `Fold.dessin_passport` | `Quot.sound` |
| `Fold.dessinMonodromy_group` | `Quot.sound` |
| `Fold.a1_cone` | `propext`, `Quot.sound` |
| `Fold.a1_fixed` | `propext` |
| `Fold.a1Chart_chart` | `propext` |
| `Fold.scale_fix_iff` | `propext`, `Quot.sound` |
| `Fold.chi_puncture_cap` | `propext` |
| `Fold.rot_period` | `propext` |
| `Fold.tolerance_not_trans` | `propext`, `Classical.choice`, `Quot.sound` |

`propext`, `Quot.sound`, and `Classical.choice` are Lean's core axioms, not `sorryAx`. No theorem in
the library depends on a hole. `desc_bijective` is the sharpest entry: it uses only `Quot.sound` —
the descent is constructive up to the quotient's own computation rule, with no classical choice.

## How to extend

The dependency-free core is the audit. Put Mathlib results in a separate library, so the core
still builds on a bare toolchain.

1. **Complex analysis.** `ℂ*`, the inversion `z ↦ ρ²/z̄`, the fixed circle, the cap/puncture
   transition. This is the local model, and it is the first target.
2. **Topology.** `S¹`, the one-point compactification, `χ` as a homotopy invariant, the classification
   of 1-manifolds. This turns the ledger in `Fold/Chi.lean` into a theorem about spaces.
3. **Groups.** `D_m`, the crystallographic restriction, the orbit-stabilizer theorem for the
   observer's position. This turns the wheel into the exact symmetry statement.
4. **Measure.** Amenability, invariant means, Haar measure, the `dk/k` divergence. This is the
   second map's exact content.
5. **Arithmetic.** `ZMod 99`, the calendar theorem, the weekday as a group coordinate.

The order matters: complex analysis and topology first, because the navel and the chart are their
statements; measure after, because the second map's exact additions are measure statements; groups
and arithmetic alongside.

## The one sentence

**The Lean file proves the skeleton — an involution, its fixed set, its quotient, its cut, and the
exact arithmetic — and it leaves the flesh to the prose: the analytic closure, the measure, and the
consciousness.**
