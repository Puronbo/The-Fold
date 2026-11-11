# The order of creation

## The claim in one line

The Fold's stages are forced in one order —

```
point → scale → fold → twist → closure → horizon → observer → point
```

— and that order is not the paper's section order. It is the order in which the structures can
exist, not a date on a clock.

## The same order in plain terms

1. **A point with a direction.** There is a centre and a set of rays, but no distance yet.
2. **Size.** The centre becomes a scale; things get bigger or smaller around it. Height, area and
   volume grow at different rates.
3. **A mirror.** A reflection appears; it fixes a line (or plane) — the crease — and swaps the two
   sides.
4. **A turn.** Two mirrors at an angle make a rotation. This is the first repeating motion.
5. **A repeating pattern.** The turn closes only at special angles; those angles give the finite
   symmetry groups and the crystal lattices.
6. **An edge.** The boundary of the pattern becomes a horizon: a surface you cannot see past, with
   a temperature and an entropy.
7. **A viewer.** The viewer's dimension decides what can be measured: a number, a rate, a flow, or
   a density.
8. **Back to the point.** If you allow every symmetry, all points are equivalent and only the
   centre — the point — remains.

In one sentence: start with a centre and a direction, give it a size, add a mirror, turn the
mirror into a rotation, let the rotation repeat, let the pattern end at an edge, put a viewer
inside, and everything collapses back to the centre.

## Why the paper's order is not the creation order

The paper teaches the twist (§3) before the fold (§4) because `J` is familiar. But §4 then says
that the twist is **two folds**:

```
σ_{H₂} ∘ σ_{H₁} = R(2α)
```

so the twist cannot be earlier than the fold. Creation must run fold → twist. What the paper
presents as §3 is the completed object; what creation needs first is its generator.

The paper's §9 is the **dissolution** — "degenerates at `k = 0` onto the centre that was there all
along." Creation is that sentence read backwards. The two orders are the same chain, one ascending
and one descending.

## The chain

| # | stage | parameter | operation | what appears | what survives | where |
|---|---|---|---|---|---|---|
| 0 | the point | `k = 0` | constant map | the datum, rank 0, no geometry — only a direction | `Sⁿ⁻¹`, `n` | §6, cone §6 |
| 1 | the scale | `k > 0` | homothety | the ray, the sphere/cone; `h ∝ k`, `A ∝ k²`, `V ∝ k³` | angle, direction, cross-ratio | §1–2 |
| 2 | the fold | `σ_H` (`k = −1` at the antipode) | reflection | the crease (`n−1`), orientation, `Z₂`; midpoint and division points | crease, lengths, angles | §4, midpoint, division |
| 3 | the twist | `k = e^{2iα}` | two folds at `α` | `J² = −I`; the cycle `1 → i → −1 → −i → 1`; periodicity | radius, energy | §3–4 |
| 4 | the closure | `m = π/α` | discrete group `D_m` | the lattice, the crystallographic restriction, rational/irrational order | `m`, the root of unity | closure |
| 5 | the horizon | `k* = 2GM/(c²R)` | null boundary | the cone's apex on the surface; entropy, temperature; the causal limit | aperture `θ`, area | §5, horizon, cone |
| 6 | the observer | dimension `d` | measurement | 0D scalar, 1D rate, 2D flux, 3D density | the measurable | §7 |
| 7 | the return | `k = 0` | compactification | orbit space = a point; invariant ring = constants | the point | §6, invariants, §9 |

## 0. The point

The first stage is not "nothing." It is the one map with no scale:

```
g₀(P) = P₀          rank 0          det = 0          image = {P₀}
```

`k = 0` is outside the group: not invertible, not a small scaling, the compactification of every
orbit `(P₀, P]` at once. But the point is not empty. What survives is precisely what was never a
measure:

- the direction — the sphere `Sⁿ⁻¹` of rays, or the projective `ℝPⁿ⁻¹` if sign is quotiented;
- the dimension `n`;
- the tangent cone of the family, which is the only structure a 0-dimensional observer can carry.

The cone note makes this quantitative. At the vertex of a range cone with aperture `θ = 60°`, the
solid angle stays `Ω/4π = 0.25` however far in you zoom (`5 × 10⁻²`, `10⁻²`, `2 × 10⁻³`), while a
smooth surface point goes to `0.5` and an interior point stays at `1`. The vertex is zero of every
measure and all of the direction. That is the seed: a direction without distance. The state is exactly
characterized as the unique point fixed by every non-identity `g_k`, and its form is the derivative `Dg₀ = 0`; see
`the-fold-initial.md`.

The signature of this stage is the **null signature**. The collapsed image is a point and has no
tangent space; the ambient tangent space at the datum is `ℝⁿ`, and the linear part of `g₀` is `0`
there, with inertia `(0,0,n)`: `n` directions, none signed. The scalar signature is `0`, but the planar fold also
has scalar signature `0` with inertia `(1,1,0)`, so only the full inertia separates nothing from a
split. The zero's algebraic fingerprint is `(λⁿ, λ)` — characteristic polynomial `λⁿ`, minimal
polynomial `λ`, the unique operator annihilated by `x`. The first scale signs all `n` at once,
`(n,0,0)` for `k > 0`; the first fold splits off one, `(n−1,1,0)`. A continuous path from `I` to
`−I` must cross a zero eigenvalue, and in the Fold that crossing is `k = 0`: that is why nothing is
first in the scale ledger. In the fold ledger the crease and the normal arrive together, so there is
no "before." See `the-fold-signature.md`.

## 1. The scale

The first distinction is size. For `k > 0`,

```
g_k(P) = P₀ + k(P − P₀)          det g_k = kⁿ
```

and the measures separate by degree:

```
height  h ∝ k          area  A ∝ k²          volume  V ∝ k³
```

The orbits are rays `(P₀, P]`; the level sets of the radial coordinate are spheres when the datum
is inside, proper cones when the datum is on the boundary, and shadows when it is outside. This is
where the two regimes of §2 appear: an interior apex has tangent cone `ℝ³` and no proper cone; a
boundary apex locks the cone at `P₀`; an exterior apex is the same cone seen from farther away.

The range cone carries the shape/size split exactly:

```
Ω = 2π(1 − cos θ)          V = (R³/3)Ω          A = R²(Ω + π sin θ)
```

`g_k` sends `R ↦ kR` and leaves `θ` alone. The aperture is the invariant; the range is the
coordinate. This is the first "space": a ray, a sphere, a cone — a size attached to a datum.

What survives the scale is direction, angle and cross-ratio. What does not survive is length.
The first measure is born, and with it the first distinction between shape and size.

Read as matter, this is the seed: a body is the datum — the zero — at a scale. Height fixes every
dimensional magnitude by a power of `h`; the aperture fixes the shape. That is stages 0–1; the rest
of the chain is what the zero does at that scale. See `the-fold-matter.md`.

## 2. The fold

The second stage is the first law. A fold is a reflection in a hyperplane `H`:

```
σ_H² = I          σ_H fixes H          det σ_H = −1
```

Its fixed set has dimension `n − 1`: a line in the plane, a plane in space. The fold does not fix
the datum — it fixes a **crease**. This is the correction §4 makes to the earlier account, and it is
why the fold is more primitive than the twist.

The fold has an internal measure. Halve the segment from a point to its image:

```
m_k(P) = ½(P + g_kP) = g_((1+k)/2)(P)          det m_k = ((1+k)/2)ⁿ
```

The midpoint map is itself a homothety about the same datum, and its determinant vanishes at
exactly one value, `k = −1`:

```
m_{−1} = g₀          every midpoint is the datum
```

For an honest fold `σ_H`, the midpoint map is the orthogonal projection onto the crease,
`½(I + σ_H) = π_H`, of rank `n − 1` — not rank 0. The crease is the fixed set of the midpoint map;
the point reflection is the endpoint of the family where the fixed set has shrunk to the datum.
The midpoint identity is exact to `4.58e−16`; the crease residual is `2.22e−16`.

The same law at any fraction `t` gives the division points:

```
q_t(P) = (1 − t + tk)P          collapses at  k_t = (t − 1)/t = 1 − 1/t
```

Every `k ≠ 1` is owned by exactly one division point, `t = 1/(1−k)`; the pairing `t ↔ 1−t` sends
`k ↔ 1/k`; the quarter point `t = ¼` owns `k = −3`, whose midpoint map is the fold itself. The
round trip `t → k → t` closes to `1.78e−15`.

The fold is the first `Z₂`, the first orientation, the first crease. It is where "inside" and
"outside" acquire a mirror.

The fold also carries a ledger of its own, and it is the one that alternates. Give a fold by a point
`P_H` on its crease and a unit normal `n`:

```
f(P) = (P − P_H) · n          f⁻¹(0) = H          ∇f = n
```

The zero is the crease; the one is the normal. `f` vanishes on `H` and its gradient is `n`, so the
normal is the split of the zero into two sides. Reflection sends `f → −f`; halving a point and its
image lands back on `H`, `½(P + σ_H P) = π_H P`. So one is a split of zero, and zero is the
annihilation of the split.

Each fold has its own crease, and the normal is fixed up to sign, so its "one" is the pair
`{n, −n}`. This is how existence can read `0 → 1 → 0 → 1` with every term new:
`H₁ → {n₁, −n₁} → H₂ → {n₂, −n₂}`, each crease and each normal-pair a different object. In the scale ledger the same reading fails at the ones, because `k = 1` is the
unique identity; the zeros there are distinct — `k_t = 1 − 1/t` — but they are distinct collapses,
not distinct split points. The two ledgers meet at `k = −1`, the point reflection whose fixed set
shrinks to the datum; there the fold's zero becomes the scale's zero.

Read as a facet, the crease is the zero of the supporting functional `f(P) = (P−P_H)·n`: codimension
one, a face of the body. The scale's zero is a vertex, not a facet. See `the-fold-facets.md`.

Read as a view, the same normal is the occlusion. The two sides are `f > 0` and `f < 0`; the crease
is `f = 0`, where the surface is edge-on. A metric is quadratic and even in `f`, so it cannot tell the
sides apart; only the linear coordinate `f` knows both. The back is not a region behind the surface;
it is the sign the form forgets. `π_H` drops it, `σ_H` flips it, and `f = 0` is the only place they
meet. See `the-fold-occlusion.md`.

## 3. The twist

One reflection is not a rotation. Two folds at angle `α` are:

```
σ_{H₂} ∘ σ_{H₁} = R(2α)
```

In two dimensions this is the complex structure:

```
J = [ 0  −1 ]        J² = −I        e^{θJ} = cos θ · I + sin θ · J = R(θ)
[ 1   0 ]
```

The quarter turn `J` is two folds at `45°`; the half turn `−I` is two folds at `90°`, or `J²`. This is
the mixed law `1_a + 1_b = 2_{ab}`: the folds add in number, the angle doubles, and the parameter
composes. See `the-fold-composition.md`.

The four cardinal values form the cycle

```
1 → i → −1 → −i → 1
```

and the cycle is the twist written multiplicatively. Orientation is the parity of the fold count:
an even number preserves it, an odd number reverses it. The twist is the first **periodic motion**,
hence the first time-like structure: `arg k` is the phase, and the twist squared is the point
reflection, `J² = −I` — the fold at `k = −1`.

This is the stage where frequency is born. A rotation has a period; a period has a frequency; a
frequency is what a 1-dimensional observer will later measure as a rate.

The same complex `k` appears in the zeta function: at height `h = ln n`, the Dirichlet term is
`n^{-s} = e^{-σh} e^{-ith}`, a scale by `e^{-σh}` and a twist by `−th`. The sum over `n` is a sum over
heights. See `the-fold-zeta.md`.

The twist also leaves the signature ladder. `J` is skew on its 2-plane, so its symmetric part is zero
there and inertia sees only `(0,0,2)` on that plane; but `J` is not zero. Its invariant is the
Pfaffian `Pf(ω)=1` of `ω(x,y)=⟨x,Jy⟩`. The signature is the invariant of the symmetric stages; the
twist needs a symplectic one.

## 4. The closure

A rotation closes only at rational angles. For two creases at `α`,

```
(σ₂σ₁)^m = I      ⇔      2αm ≡ 0 (mod 2π)      ⇔      m = π/α
```

If `α = pπ/q` in lowest terms, `m = q` and the group is the dihedral group `D_q` of order `2q`.
The twist `k = e^{2iα}` is an `m`-th root of unity. Measured to a residual of `2.4e−16`:

| `n` | `α = π/n` | `θ = 2α` | `k` | `m` | `\|G\|` |
|---|---|---|---|---|---|
| 2 | 90° | 180° | −1 | 2 | 4 |
| 3 | 60° | 120° | −0.5 + 0.866 i | 3 | 6 |
| 4 | 45° | 90° | **i** | 4 | 8 |
| 5 | 36° | 72° | 0.309 + 0.951 i | 5 | 10 |
| 6 | 30° | 60° | 0.5 + 0.866 i | 6 | 12 |
| 8 | 22.5° | 45° | 0.707 + 0.707 i | 8 | 16 |
| 10 | 18° | 36° | 0.809 + 0.588 i | 10 | 20 |
| 12 | 15° | 30° | 0.866 + 0.5 i | 12 | 24 |

Three limits define the stage:

- **Rational** `α/π`: the orbit visits `m` points and stops. The group is finite.
- **Irrational** `α/π`: no `m ≤ 20000` closes; the orbit is dense. The group is the infinite
  dihedral group; the symmetry is only approximate — a quasicrystal.
- **Parallel creases** (`α = 0`): the composition is a translation, `2(d₂ − d₁)`, with no fixed
  point. The datum is pushed to infinity.

The lattice adds the crystallographic restriction. A rotation by `θ` is an integer matrix in a
lattice basis only if `2 cos θ` is an integer:

| `n` | `2 cos(2π/n)` | lattice |
|---|---|---|
| 2 | −2 | yes |
| 3 | −1 | yes |
| 4 | 0 | yes |
| 5 | 0.618 | no |
| 6 | 1 | yes |
| 8 | 1.414 | no |
| 10 | 1.618 | no |
| 12 | 1.732 | no |

So `n ∈ {1, 2, 3, 4, 6}`, and nothing else. `D₄` is the largest crystallographic group that
contains a quarter turn;
`D₅`, `D₈`, `D₁₀`, `D₁₂` require quasicrystalline order. This is the first discrete skeleton —
the "quantization" of the twist, and the first place where only some symmetries survive in a
lattice.

## 5. The horizon

The boundary case of the scale is the horizon: the apex sits on the surface, and the surface
becomes null. The condition is

```
k* = r_s/R = 2GM/(c²R)
```

The horizon is where the two columns of §5 separate. A homothetic family (`M ∝ k`) is a set of
solutions, not a process; a fixed-mass collapse holds `M` and lets `R` fall:

| quantity | homothetic `M ∝ k` | collapse `M` fixed |
|---|---|---|
| `r_H` | `∝ k` | `= r_s`, constant |
| `A_H` | `∝ k²` | constant |
| `S = A_H/4ℓ_P²` | `∝ k²` | constant |
| `T` | `∝ 1/k` | constant |
| `M` | `∝ k` | constant |
| `R` | `∝ k` | `∝ k` |
| `r_H/R` | constant | `∝ 1/k` |

Only the right-hand column is a process. The horizon arrives **before** zero: Earth `k* = 1.392e−9`,
Sun `4.245e−6`, a 70 kg sphere of water `4.067e−25`. Below `k*` the point remains in the mathematics
and leaves the physics.

This is the first event and the first clock. Temperature is a frequency through `k_B T ~ ℏω`; in
the homothetic family `T ∝ 1/k`, while in the fixed-mass collapse `T` is constant. The horizon is
the first place where the order acquires a clock. Entropy does not accumulate during the fall —
it appears with the horizon in one step — and `V/A_H` falls as `k` in the homothetic family and as
`k³` in the collapse.

Read through a signature, the horizon is a **null crease**. A null surface has `n·n = 0`, so the
induced form is degenerate, `(n−2,0,1)` inside a Lorentzian `(n−1,1,0)` (with `n` the spacetime
dimension); the orthogonal fold requires `n·n = ±1`, so the fold degenerates there. The Fold's `k*`
is the scalar ratio at which the radial normal becomes null. This is a reading, not a derivation:
the Fold supplies the ratio, not the metric.

Mass loss at fixed `R` is a third column — an extension beyond the paper's two-column table: `M`
falls, `R` stays, and `k* ∝ M` falls with it. That is how a body climbs back out of its own
horizon. The reaction is the process opposite to the collapse. For the pendulum the mass cancels
from the energy condition — the equivalence principle at work; for the horizon the geometry does
depend on `M`, but the reaction's cost is carried by the propellant, not by the geometry.

## 6. The observer

A horizon limits what can be seen. An observer is defined by its dimension, and the dimension fixes
the observable:

| observer dimension | observable |
|---|---|
| **0D** | scalar — curvature, potential, temperature |
| 1D | derivative, direction, rate |
| 2D | flux (needs an oriented area) |
| 3D | density, integral |

A point sees **values, not flows**. It has no tangent space, so it cannot host a vector; it can
measure a temperature, not a rate. This is why time is undefined at the point rather than zero.

The same table reads the sphere from three places:

| observer | `Ω/4π` | behaviour |
|---|---|---|
| outside | `5.060%` at `k = 1`, falls as `k²` | body shrinks to a point |
| at the centre | `100%` for every `k > 0` | sky fixed, distance shrinks |
| on the surface | `2π` half-space | edge-on; the horizon case |

The exterior `5.060%` is exactly `d = 2.281 r`; the same ratio reproduces `1.216%` and `0.301%` at
`k = 0.5, 0.25`. The observer stage is the first perspective: the universe becomes measurable only
when a dimension is specified.

## 7. The return

The last stage is the point again. Allow both scalings and folds and the group is
`ℝ₊ × O(n)`, which acts transitively on `ℝⁿ ∖ {P₀}`:

```
orbit space = a point          invariant ring = ℝ (constants)
```

At `φ = 0` — at `k = 0`, or at the collapse value of any division point — the rank drops to zero
and every row of the audit becomes undefined rather than false: no distance, no angle, no
cross-ratio. Four points have become one. "The point is what is left when everything is allowed."

The return is not a separate event. It is the same point as stage 0, read from the other side.
The creation order is a loop:

```
point → scale → fold → twist → closure → horizon → observer → point
```

The paper's §9 is the loop read downwards; this note is the loop read upwards.

The return also has a topological signature. On the one-point compactification `Sⁿ`, the radial field
has a zero at the origin and a zero at infinity; their indices are `+1` and `(−1)ⁿ`, summing to
`χ(Sⁿ)`. The loop's two ends are those two zeros, so the return is forced by the topology of the
compactification as well as by the group. See `the-fold-signature.md`.

The loop is not an inverse. The inverse of an action returns the identity, `k = 1`; the loop returns
the collapse, `k = 0`. Undoing an action leaves the object; completing it leaves the point. That is
the difference between the two nothings.

## Why this order and not another

Each arrow is a dependency:

- **point → scale:** a point without size cannot be a space; the first distinction is size.
- **scale → fold:** a scale is purely radial; a fold breaks the radial symmetry and introduces a
  hyperplane — the crease.
- **fold → twist:** one reflection is not a rotation; two folds at an angle are. The twist is the
  first periodic motion, hence the first time-like structure.
- **twist → closure:** a rotation is continuous; closure at rational angles selects the discrete
  groups — the first quantization.
- **closure → horizon:** a discrete body has a boundary; at the boundary the cone becomes null —
  the causal surface.
- **horizon → observer:** a horizon limits what can be seen; an observer needs a dimension to
  measure anything at all.
- **observer → return:** the full similarity group is transitive; the orbit space is a single point;
  only constants remain.

## Time and frequency enter here

| stage | time / frequency |
|---|---|
| 0–1 | `k` is the parameter, not a clock; no periodicity yet |
| 2 | the fold is an isometry: static, no rate |
| 3 | the twist gives periodicity; `arg k` is the phase |
| 4 | `m = π/α` counts the turns; rational closes, irrational goes dense |
| 5 | `T ∝ 1/k`; the horizon is the first clock |
| 6 | the 1D observer measures rates; time becomes observable |
| 7 | the 0D point has no clock; time is undefined, not zero |

Frequency is born at the twist, counted at the closure, given a temperature at the horizon, and
made observable by the 1D observer. Time is not a coordinate of `g_k`; it is what the order
acquires when the twist and the horizon are present.

## A laboratory for the middle: the pendulum and the reaction

The stages 2–5 are not only algebraic. A rigid pendulum is a physical instance of the same plane.
Define the complex amplitude

```
k = √( E / (2mgL) ) · e^{iθ}
```

Then the pendulum's phase portrait **is** the `k`-plane:

| Fold | Pendulum |
|---|---|
| `k = 0` | bottom, at rest — the collapse |
| `k = −1` | top, inverted — the fold |
| `\|k\| = 1` | separatrix — the isometry circle |
| `\|k\| < 1` | libration — contraction |
| `\|k\| > 1` | rotation — expansion |
| `\arg k` | angle `θ` |
| `\|k\|²` | normalized energy `E/2mgL` |

The separatrix's two isometries are `k = 1` (bottom crossing, speed `2√(gL)`) and `k = −1` (top, at
rest); their midpoint is `0`, the bottom rest — the midpoint note's `½(I + (−I)) = 0` realized. The
midpoint map at the fold, `m_{−1} = g₀`, is "top → bottom rest."

The reaction adds the third horizon column. Let the mass ratio be the Fold's real `k`:

```
k = m_f/m_i = 1 − 1/t          t = 1/f = m_i/(m_i − m_f)
```

The division line partitions into four regimes:

| `t` | `k` | `f = 1 − k` | regime |
|---|---|---|---|
| `t < 0` | `k > 1` | `f < 0` | mass gain (not a reaction) |
| `0 < t < 1` | `k < 0` | `f > 1` | negative mass (unphysical) |
| `1 < t < ∞` | `0 < k < 1` | `0 < f < 1` | **expulsion — the reaction** |
| `t = ∞` | `k = 1` | `f = 0` | identity |
| `t = 1` | `k = 0` | `f = 1` | total expulsion (limit) |

The reaction lives in the monoid `(0, 1]`, not the group `ℝ*`: you cannot add mass back, and `k = 0`
is absorbing. The rocket equation is the logarithm of the group:

```
k = e^{−Δv/u}          f = 1 − e^{−Δv/u}
```

The Fold's law is multiplicative in `k`; the rocket's cost is additive in `Δv/u`. The determinant
`kⁿ` is a power; the mass ratio is an exponential. The optimal burn is at the bottom, where the
speed is largest (the Oberth effect); the condition to reach the top is `v_bottom ≥ 2√(gL)`.

Two nothings sit at the ends of this line. `k = 1` is the identity: an action undone by its exact
inverse `1/k` leaves the object unchanged — nothing has happened. `k = 0` is the collapse: the monoid
has no inverse, so the reaction cannot undo the action; it drives `k` to the absorbing value — nothing
has size. The rocket lives between them: in the mass ledger the reaction drives `k` toward `0`, while
in the velocity ledger the same reaction produces `Δv`. So `k = 0` is not "no motion"; it is "no mass
left to move." Whether "nothing has happened" is true depends on which ledger you read.

Two cautions keep the two `k`'s apart: the state `k` is complex (energy and phase), the mass `k` is
real (a ratio); and the fold `k = −1` is the top in the state plane but negative final mass in the
mass plane, so the reaction cannot reach the mass-ratio fold. The state plane is an exact
laboratory for stages 2–3; the reaction is an exact laboratory for the third horizon column of
stage 5.

## Checks

No new measurements are introduced by the ordering; the values below are the existing checks that
the stages rest on.

| check | value | source |
|---|---|---|
| midpoint identity `m_k = g_((1+k)/2)` | `4.58e−16` | midpoint |
| crease residual `½(I+σ_H) = π_H` | `2.22e−16` | midpoint |
| division round trip `t → k → t` | `1.78e−15` | division |
| closure residual | `2.4e−16` | closure |
| aperture at `k = 1, 10⁻³, 10⁻⁶` | `60.0000°` | cone |
| vertex `Ω/4π` at `θ = 60°` | `0.25` at every `ε` | cone |
| `k*` for Earth / Sun / 70 kg | `1.392e−9` / `4.245e−6` / `4.067e−25` | horizon |
| rank at `k = 0` | `n → 0` in one step | §6 |

## The caveat: dependency, not a timeline

This is the order of **dependencies**, not a dated cosmology. The Fold supplies the hierarchy of
structures; it does not supply dynamics. Only the horizon stage is a *process* in the paper's sense —
the homothetic family is "a set of solutions, not a process," and the fixed-mass collapse is the
process. If you want a physical timeline, it has to be added, and the horizon note's two columns
plus the reaction column are the only places where a process enters.

The physical reading is an **analogy**, not a derivation:

| Fold stage | physical analogy |
|---|---|
| point | initial singularity / Planck scale |
| scale | expansion / inflation |
| fold | parity / `Z₂` symmetry breaking |
| twist | CP / chirality / rotation |
| closure | quantization / discrete symmetries |
| horizon | causal horizon / black hole |
| observer | measurement / structure |
| return | the final point / invariant ring |

## Glossary: technical term → plain term

| term | plain meaning |
|---|---|
| datum `P₀` | the fixed centre |
| homothety `g_k` | scaling about that centre |
| rank | how many independent directions the map keeps |
| determinant `kⁿ` | the factor by which n-dimensional volume changes |
| fold `σ_H` | mirror reflection |
| crease `H` | the mirror line/plane the fold leaves fixed |
| twist `J` | a quarter turn; built from two mirrors |
| closure `m = π/α` | how many turns before the pattern repeats |
| `D_m` | the symmetry group of a regular m-gon |
| crystallographic restriction | only 2-, 3-, 4- and 6-fold turns fit a repeating lattice |
| horizon `k*` | the boundary where the surface becomes a one-way edge |
| observer dimension | how many directions the observer can measure |
| orbit | the set of points a symmetry moves a point through |
| orbit space | what is left after identifying all symmetry-equivalent points |
| invariant | a quantity the symmetry does not change |
| monoid | a group without an undo (you can expel mass, not un-expel it) |
| two nothings | `k = 1` (nothing changed) and `k = 0` (nothing has size) |
| fold ledger | additive signs: zero is a crease `H`, one is its normal `n` |
| scale ledger | multiplicative ratios: one is the identity `k = 1`, zero the collapse |
| signature | the inertia `(n₊, n₋, n₀)` of a symmetric form |
| nullity | the number of zero directions; the zero's signature is all nullity |
| `k = 0` | the collapse point: no size, only direction |

## Corrections made in this pass

- The division note's `det q_t = φ²` is the two-dimensional case; the general law is `φⁿ`. Corrected
  in `the-fold-division.md`.
- "Temperature is a frequency" is shorthand; the precise statement is `k_B T ~ ℏω`. The note now
  says "temperature is a clock."
- The third column of the horizon table is an extension beyond the paper's two-column table; it is
  now labelled as such.
- "The geometry is mass-independent" applies to the pendulum's energy condition; for the horizon the
  geometry depends on `M`. The sentence is now split.
- The scale stage's "level sets are spheres" is now stated as "level sets of the radial coordinate";
  the orbits are rays.

## What changed in the paper

Nothing is retracted. The paper's §3/§4 order is pedagogical; the creation order is fold → twist.
§4 already says "two folds make a twist," so the note only makes the dependency explicit. The paper's
§9 is the dissolution; this note is the same chain read upwards.

A short §0 paragraph stating the order was tested in both `the-fold.md` and `the-fold.tex`. It pushed
the PDF from six pages to seven, with page 7 containing only "§9 The one sentence" — an orphan. The
insertion was reverted in both files. The paper therefore stays at six pages and the order stays
here, as the companion note, rather than in the paper. If it is ever added back, it must be paired
with a compensating cut, not appended.

A one-sentence §6 addition — the zero's linear part has inertia `(0,0,n)` — was tested too. It also
pushed the PDF to seven pages, and it was reverted. The signature result stays in
`the-fold-signature.md`. The paper's §6 bullet "no tangent space" refers to the **collapsed image**;
the **ambient** tangent space is still `ℝⁿ`, and that is where the null form lives.

The note adds no new measurements. It rearranges the existing findings — the point, the scale, the
fold, the twist, the closure, the horizon, the observer and the return — into the order in which
they can exist.

## Files

`the-fold-creation.md` (this note). No separate interactive model: the order is a reading of the
existing nine HTML files, not a tenth object. The compact lookup companion is `the-fold-key.md`; the
matter reading of stages 0–1 is `the-fold-matter.md`.

## The one sentence

**The Fold's stages are forced in the order of its dependencies: a point with a direction, a scale,
a fold, a twist, a closure, a horizon, an observer — and the point again.**
