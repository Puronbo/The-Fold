# Friction: the contact is the crease

## The object

Two bodies meet on a set `C`, and `C` is where the fold's two layers are the same surface. Friction is
what the interface transacts, and the transaction has a price per unit area:

```
F = τ A ,        A = A_real ,        μ = τ / p* .
```

`τ` is the shear strength of the junction, `p*` the yield pressure, `A` the **real** contact area — the
sum of the asperity patches, not the apparent face. `μ` is dimensionless and is the ratio of two
stresses, which is the whole reason it looks like a property of materials rather than of shapes.

That trichotomy is the note. It has three levels, and only the middle one is what the textbook slogan
says:

| contact | `A(N)` | `F(N)` | zone |
|---|---|---|---|
| plastic, `A = N/p*` | `∝ N` | `∝ N`, with `μ = τ/p*` | exact |
| one elastic sphere (Hertz) | `∝ N^{2/3}` | `∝ N^{2/3}` | exact |
| rough elastic, many asperities | `∝ N` (exactly, for an exponential height distribution) | `∝ N` | exact in the model |
| apparent area | — | independent of it | false friend |

So "friction is proportional to the contact area" is exact — with `A` the real area. "Friction is
proportional to the load" is exact only for plastic junctions, or for a rough elastic surface whose
asperity heights are distributed exponentially; that is Amontons' law, and it is a statement about a
**distribution**, not about a contact. "Friction is proportional to the apparent area" is the false
friend, and it is the one everybody believes: a brick slides the same on its face and on its edge.

The premise is the missing word. A single elastic sphere gives `F ∝ N^{2/3}`, not `F ∝ N`, and it is a
real contact with a real area. The law `F = μN` needs many asperities, and their statistics.

## Friction is not heat

The decisive case is the one with no motion at all. Static friction holds a body still:

```
v_slip = 0   ⇒   P = F · v_slip = 0 ,        F ≤ μ_s N .
```

The force is not zero and the heat is exactly zero. So friction is not the generation of heat; heat is
the **rate** that appears when the interface slips, and static friction is the same force with the rate
switched off. Two ledgers:

| ledger | what friction does | when |
|---|---|---|
| momentum | supplies the external force — traction, walking, braking, a tyre | always, static or kinetic |
| energy | dissipates `F · v_slip` (or `M ω`) into heat | only when there is slip |

"The friction of the ground moves you" is exact in the momentum ledger — the ground pushes you forward
because you push it backward — and false in the energy ledger: at a no-slip contact the friction force
does **no work**, and the energy comes from your muscles, not from the ground. That split is the exact
content of "not just the generation of heat but the source of movement". The source of *momentum* is
the interface; the source of *energy* is never the interface when it does not slip.

## The contact is shared, so it is codimension one

`A_real` is not owned by either body. It is the measure of the set where both are present, and that set
is the crease: codimension one, the boundary of each body and the interior of neither.

```
C = ∂B₁ ∩ ∂B₂ ,        area(C) = A_real .
```

Two consequences, both exact and both already in the corpus:

- the interface carries a **flux**, not a body: `F = τ A` is a stress times an area, i.e. momentum per
  unit time crossing `C`. Friction is the momentum flux through the crease, and "the change of area is
  what is being dealt" is the statement that the flux is priced per unit area;
- `μ = τ/p*` is invariant under `g_k`. Scale the contact by `k` and `N ∝ k²`, `A ∝ k²`, `F ∝ k²`, so
  `F/A` and `F/N` are unchanged. The coefficient survives the scaling because it is a ratio — the
  corpus's "shape survives, size does not", with friction as the instance.

The `0` in the denominator is the point: `p*` is a stress, and a stress is what the Fold does not have.
The Fold supplies the interface and the scaling; the host supplies `τ`, `p*`, and `N`.

## Turning is a different mode, not a different direction

Three relative motions at a contact, and only one of them is "left to right":

| mode | slip velocity | force or moment | work | what it consumes |
|---|---|---|---|---|
| slide | `v` everywhere | `F = μN` | `μN` per unit distance | the patch, in one width `w` |
| spin (twist) | `ω × r`, zero at the centre | `M = c μ N a` | `M` per radian | nothing: the path is a spiral |
| roll | zero at the contact | none (Coulomb) | `0` | nothing: the material flows through |

For a circular patch of radius `a` under uniform pressure, integrating `τ r` over the disc gives

```
M = (2/3) μ N a  = 0.6667 μ N a ,
```

and for the Hertzian pressure `p ∝ √(1 − r²/a²)` the same integral gives

```
M = (3π/16) μ N a  = 0.5890 μ N a .
```

The **constant** carries the pressure profile; the **scaling** `μ N a` does not. And since a Hertzian
contact has `a ∝ N^{1/3}`,

```
M ∝ N^{4/3} ,
```

so spin friction at a single elastic contact is **superlinear** in the load, while sliding is linear.
That exponent is exact in the model and it is the cleanest fingerprint of the mode: a moment, not a
force, with the contact radius as its lever arm.

This is the exact reading of "turning is not moving from left to right". Sliding spends the patch: you
can slide at most `w` before you have left the contact. Spinning does not: a point at radius `r`
travels `2πr` per turn and returns to where it started, so the work per patch is **unbounded** while
the contact area is fixed. Turning does not enlarge the contact; it lengthens the path through it. The
area is set by the load, not by the rotation.

So "turning increases the contact area to increase the change" is a false friend in its first half and
exact in its second: the area is fixed, the path grows without bound, and the change per turn is `2πM`.
If the area is enlarged at fixed load, `M ∝ √A` — the total grows, the density `M/A` falls. If the
pressure is held fixed instead, `N ∝ A` and `M ∝ A^{3/2}` — then both grow. Which quantity is held
fixed is the whole content of "increase".

## The Fold's part in it

The twist `J` is a `U(1)` action about the axis, and on a rotationally symmetric body it is an exact
symmetry: `the-fold-cone.md` records that the cone is carried to itself by it, so the twist is the
identity and costs nothing. The same rotation on a contact costs `M` per radian. Both are correct,
because the two statements are about different objects:

- geometry: the twist is a symmetry of the shape, so it moves nothing and is free;
- material: the twist is a slip field at the interface, so it does work and is priced.

The Fold is the first ledger. Calling the twist "work" because a material would heat is the false
friend; calling the twist "free" because the shape is symmetric is the same false friend mirrored. The
`U(1)` is one group with two ledgers, and the interface is what decides which one applies.

## What is left after the transaction

`μ = τ/p*`. Area cancels, load cancels, speed cancels. What remains is a ratio of two stresses and a
dimensionless number — which is why friction looks like a constant of the world rather than a fact
about the particular contact, and why every attempt to explain it by "more surface" fails on the
apparent area while succeeding on the real one.

The crease does not move. The two sides trade momentum across it, and the price of the trade is the
only thing the interface keeps.
