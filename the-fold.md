# The Fold

**Scale, twist, collapse — and what is left at the centre**

---

## 0. Summary

Scaling about a datum is a one-parameter family `g_k(P) = P₀ + k(P − P₀)`. The family is a group for `k ≠ 0`; `k = 0` is the boundary where it degenerates into a point. A real `k` changes size, an imaginary one twists, and a fold is the reflection whose composition produces the twist. Everything that follows is the consequence of one determinant:

```
det(g_k) = kⁿ          n = dimension
```

Heights scale like `k`, areas like `k²`, volumes like `k³`. That single fact separates every quantity in the construction.

---

## 1. The scale factor and the datum

For a datum point `P₀` and a point `P` on the object:

```
P′ = P₀ + k(P − P₀)
```

| k | behaviour |
|---|---|
| `k > 1` | expansion away from the datum |
| `0 < k < 1` | contraction toward the datum |
| `k = 0` | collapse: every point maps to `P₀` |
| `k < 0` | scaling composed with reflection through `P₀` |

The map is a **homothety**. For `k ≠ 0` the family is a group isomorphic to `ℝ*`; `g_0` is the constant map with rank 0 and is not a member. This distinction matters later: zero is not a small scaling, it is the end of the family.

### Area and height

```
height  h′ = k·h
area    A′ = k²·A
volume  V′ = |k|³·V
```

so that

```
A′/A = (h′/h)²
```

Height and area cannot share a law. A sign survives in the height and dies in the area, because area is a determinant and the determinant of `kI` is `k²`. At `k = −1` the height reverses and the area is unchanged.

---

## 2. Two regimes: the sphere and the cone

Where the datum sits decides the geometry, and there are exactly two cases.

**Datum inside the body.** Every orbit of the scaling is a diameter. The level sets are spheres:

```
g_k(S_r) = S_{|k|r}          k ≠ 0
```

The tangent cone at an interior point is the whole space `ℝ³` — no proper cone exists. The flow is purely radial and the collapse is isotropic. The bulk-to-boundary ratio vanishes:

```
V/A = r/3 → 0
```

**Datum on the boundary.** The orbits are rays and their union is a proper cone with apex `P₀`. This is the case that produces the cone of rays, and the case a horizon belongs to.

**Datum outside.** Same cone, seen from further away: the body subtends a cone and casts a shadow.

The three named choices of datum are three positions of the same apex:

| datum | apex | tangent cone | behaviour |
|---|---|---|---|
| centroid | interior | `ℝ³` | uniform scaling in place |
| vertex / base | boundary | proper cone | apex locked, body grows away |
| origin | fixed frame point, interior or exterior | `ℝ³` or proper cone | scaling also translates the body when it is off-origin |

---

## 3. The twist

The operator

```
J = [ 0  −1 ]
    [ 1   0 ]          J² = −I
```

is the infinitesimal generator of rotation, and

```
e^{θJ} = cos θ · I + sin θ · J = R(θ)
```

A general scale-with-twist is therefore the spiral similarity

```
k = ρ e^{iθ}         P′ = P₀ + ρ(cos θ · I + sin θ · J)(P − P₀)
```

`J` itself is the quarter turn. The four cardinal values are the fourth roots of unity and form a cycle:

```
1 → i → −1 → −i → 1
```

Two quarter turns equal one half turn: `i² = −1`. The twist squared is the flip.

### Which twists are observable

The twists that leave a body unchanged *are* its rotation symmetry group. Written as a quotient, the body only responds to

```
U(1) / Sym(B)
```

| body | symmetry | observable twist |
|---|---|---|
| sphere | `S¹` — all θ | none: `i = 1` exactly |
| cube | `C₄` = {1, i, −1, −i} | only between the cardinal turns |
| chiral body | {1} | every angle |

Measured on the rendered model (silhouette change under θ):

| θ | 0° | 30° | 45° | 90° | 180° | 270° |
|---|---|---|---|---|---|---|
| sphere | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| cube | 0.0% | 1.4% | **12.3%** | 0.0% | 0.0% | 0.0% |

The peak at 45° is the antipode of the fundamental domain: it is the point furthest from any symmetry.

### Orientation

Because `det(kI) = kⁿ`, the sign of `k` has different meaning in different dimensions:

- **2D**: `det(−I) = +1` — `k = −1` is a rotation by 180°, orientation preserved.
- **3D**: `det(−I) = −1` — `k = −1` is a point reflection, orientation reversed: the genuine "inside out".

The same formula, two different geometries.

---

## 4. The fold, completed

A **fold** is a reflection in a hyperplane `H`:

```
σ_H² = I          σ_H fixes H          det σ_H = −1
```

Its fixed set has dimension `n − 1`: a line in the plane, a plane in space. This is the piece the earlier account was missing — the fold does not fix the datum, it fixes a **crease**.

**Two folds make a twist.** Composing reflections in two hyperplanes meeting at angle `α` gives a rotation by `2α` about their intersection:

```
σ_{H₂} ∘ σ_{H₁} = R(2α)
```

So:

- `J` (90°) is **two folds at 45°** — never a single fold
- `−I` in the plane (180°) is two folds at 90°, or equivalently `J²`
- `J` is orientation-preserving because it is the product of an **even** number of folds

Orientation is the parity of the fold count. This is why a twist and a fold cannot be confused: one has determinant `+1`, the other `−1`, and any odd number of folds reverses orientation.

**The hinge is the intersection.** The twist fixes the intersection of the two creases: a point in the plane, a line in space. The datum is that hinge.

**The degeneration.** Send the two creases together and their intersection collapses to a point. The fold then has no crease left, and what remains is `k = −1`: a point reflection. That is the precise content of "the datum becomes the hinge of the fold" — the crease has shrunk into the datum, and the fold has become the point reflection.

**The crease is the midpoint locus.** Halve the segment from a point to its image. If `g_k(P) = P₀ + k(P − P₀)` then

```
m_k(P) = ½(P + g_k P) = g_((1+k)/2)(P),      det m_k = ((1+k)/2)ⁿ
```

The midpoint map is itself a homothety about the same datum, and its determinant vanishes at `k = −1` and nowhere else, in every dimension. So of the whole family exactly one member puts every midpoint on the datum, and that member is the point reflection. For an honest fold `σ_H` the midpoint map is `P ↦ ½(P + σ_H P) = π_H`, the orthogonal projection onto the crease: rank `n − 1`, not rank `0`. The crease is therefore the fixed set of the midpoint map, and the datum is the crease of zero dimension. Two other members are worth naming: `k = ½` makes the image the midpoint of datum and point, and `k = 2` makes the point the midpoint of datum and image — the reciprocal pair, in which the halving is applied at either end of the same segment.

Any division point obeys the same law. At fraction `t` of the way from `P` to `g_kP`,

```
q_t(P) = (1 − t + tk)·P
```

again a homothety, now collapsing at `k = (t − 1)/t`. Every `k ≠ 1` is therefore owned by exactly one division point, `t = 1/(1−k)`, and `t ↔ 1−t` pairs `k` with `1/k`; the midpoint is the self-paired case. The quarter point owns `k = −3`, and there `m_−3 = g_−1` — the fold itself.

**Completion.** The fold group closes when the creases have swept the full angle:

```
(σ₂σ₁)⁴ = I        for α = 45°
```

Four quarter turns return the body to itself; the two creases at 45° produce the four reflection axes at multiples of 45°, and the dihedral group `D₄` of order eight is generated by exactly two folds. The cycle `1 → i → −1 → −i → 1` is that closure written multiplicatively.

The only set fixed by the entire group is the hinge: a point in the plane, a line in space.

---

## 5. The horizon

A horizon is the boundary case of section 2: the apex sits on the surface, and the surface becomes null. It is where the cone reappears.

Under `r → kr` the mass scales too, because `r_s = 2GM/c²` is a length. That family is a set of solutions, not a process: every member has the same compactness, so the horizon is present in all of them or in none. A collapse is the opposite — the mass is held fixed and only `R` falls. The two give different laws and must not be read off one table:

| quantity | homothetic family, `M ∝ k` | collapse, `M` fixed |
|---|---|---|
| horizon radius `r_H` | `∝ k` | `= r_s`, constant |
| horizon area `A_H` | `∝ k²` | constant |
| entropy `S = A_H/4ℓ_P²` | `∝ k²` | constant |
| temperature `T` | `∝ 1/k` | constant |
| mass `M` | `∝ k` | constant |
| body radius `R` | `∝ k` | `∝ k` |
| compactness `r_H/R` | constant | `∝ 1/k` |

Only the right-hand column is a process. In the left-hand column `r_H/R` is a label of the member, not a stage, and the first law is exact: with `S = αM²` and `T = β/M`, `T dS = dM` holds identically, and `S·T ∝ k` is the horizon's energy. In the right-hand column `M` is fixed, so both sides of `T dS = dM` vanish once the horizon exists: the entropy is not accumulated during the fall, it appears with the horizon in one step.

The horizon arrives **before** zero. A body of radius `R` reaches its own Schwarzschild radius at

```
k* = r_s/R = 2GM/(c²R)
```

| body | `k*` |
|---|---|
| Earth | 1.4 × 10⁻⁹ |
| Sun | 4.3 × 10⁻⁶ |
| 70 kg water sphere | 4 × 10⁻²⁵ |

Below `k*` the collapse has left the observable chart. The point remains in the mathematics and leaves the physics.

Because `V ∝ k³` while the horizon area is constant, `V/A_H ∝ k³` in the collapse, and at the moment of formation it is `r_s/3`; in the homothetic family both scale, so the ratio falls only as `k`. Either way `V/A → 0`. That is the quantitative content of the holographic statement: information capacity tracks the area, and the area outlives the volume.

---

## 6. Zero as the point

`k = 0` is not a scaling. It is:

- **outside the group** — rank 0, not invertible
- **the compactification of every orbit** — each ray `(P₀, P]` is open, and `k = 0` closes them all at once
- **without geometry** — no tangent space, no normal; curvature `1/r` is undefined, not infinite

The dimensional ladder is therefore not a path through intermediate objects:

```
V ∝ k³        A ∝ k²        h ∝ k        point = k⁰
```

These are four measurements of the same family, not four consecutive states. At `k = 0` the rank drops from `n` to 0 in one step; the body never passes through a sheet or a line.

Seen through invariants the same statement has a sharper form. Scaling keeps direction and the cross-ratio and destroys length; folding keeps length and angle and destroys direction; the two groups meet only in `{I, −I}`, and `k = −1` is the one scaling that is also an isometry. Allow both and the action on `ℝⁿ ∖ {P₀}` is transitive: the invariant ring is the constants. That is the precise sense in which the point is what is left when everything is allowed.

---

## 7. What an observer can see

A point has no aperture: it subtends zero solid angle and collects zero flux. What it *can* measure is fixed by its dimension:

| observer dimension | observable |
|---|---|
| **0D** | scalar — curvature, potential, temperature |
| 1D | derivative, direction |
| 2D | flux (needs an oriented area) |
| 3D | density, integral |

A point sees **values, not flows**. It has no tangent space, so it cannot host a vector.

Two complementary views of the same sphere:

| observer | `Ω/4π` | behaviour |
|---|---|---|
| outside | `5.06%` at `k=1`, falls as `k²` | body shrinks to a point |
| at the centre | `100%` for every `k > 0` | sky fixed, distance shrinks |
| on the surface | `2π` half-space | edge-on; the horizon case |

Measured exterior view:

| k | Ω/4π | ratio |
|---|---|---|
| 1.00 | 5.060% | 1.000× |
| 0.50 | 1.216% | 0.240× |
| 0.25 | 0.301% | 0.060× |
| 0 | 0.000% | — |

The interior view is constant because a homothety is **conformal**: it preserves angles, hence solid angle, exactly. Scaling preserves what you see, but not how far away it is. Let the interior sphere recede (`k → ∞`) and the curvature `1/r → 0` while `Ω = 4π` stays fixed — the boundary flattens into the celestial plane at infinity, still carrying everything the bulk can send.

At `k = 0` all three views coincide: the point, the shell, and the observer are the same place.

---

## 8. Devices that instantiate each step

| idea | device | what it demonstrates |
|---|---|---|
| scale invariance | pinhole camera | image scales as `k`, area as `k²` |
| interior collapse | inertial confinement, sonoluminescence | compression `1/k³` |
| radial flow | integrating sphere | `Ω = 4π` independent of radius |
| twist `J` | quarter-wave plate | Jones matrix `diag(1, i)` |
| two folds make a twist | two mirrors at 45° | rotation by twice the mirror angle |
| symmetry quotient | square waveguide | invisible at 0/90/180/270, maximal at 45° |
| symmetry breaking | chiral medium (sugar solution) | every angle observable |
| directional twist | Faraday rotator | non-reciprocal 90° |
| horizon | acoustic / optical analogue horizon | `r ∝ k`, `T ∝ 1/k` |
| conformal boundary | AdS/CFT, celestial sphere | physics at infinity, `Ω` fixed |
| 0D scalar probe | thermocouple, curvature scalar | value without direction |

---

## 9. The one sentence

**Scaling preserves angles and curvature-free structure, changes lengths and curvatures, is generated by folds in pairs, and terminates in a point that has no geometry and can only be seen as a direction.**

---

*Companion models: `j-plane.html` (the plane, area and height), `j-cone-3d.html` (the external cone), `j-collapse-3d.html` (sphere, cube, horizon readouts, observers).*
