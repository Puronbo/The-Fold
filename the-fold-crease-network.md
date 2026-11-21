# The crease network: each zero, its parameters, and the sum that joins them

## The claim, exactly

Everything in the corpus that connects, connects at a zero set. A crease is `h⁻¹(0)`, two creases meet
only at a zero of higher order, and every global statement is the sum of what happens at those zeros.
That is not a metaphor for the index theorems; it is what they say:

```
global invariant  =  Σ  (local charge at each zero) .
```

So "interconnected at the creases" is exact, and "each zero has its own parameters" is the reason the
sum can be taken at all: the charge is local, the total is global, and nothing else is needed to pass
between them.

## What one crease is parameterized by

A crease is a point of the Möbius band `M` of `the-fold-crease-height.md` — a normal `n ∈ ℝP¹` and an
offset `c ∈ ℝ` — plus one integer that no isometry can remove:

```
( n , c ; k )  ∈  M × ℤ .
```

The pair `(n, c)` is a modulus: move the crease and nothing changes. The integer `k` is the invariant:
it is what survives every deformation that does not cross another zero. That is the precise content of
"each zero has their own parameters" — the geometric parameters are free, the charge is not.

| register | the zero | the modulus | the charge `k` |
|---|---|---|---|
| a height `h` | `h = 0` | `(n, c)` | order of vanishing |
| a holomorphic `f` | `f = 0` | position | multiplicity, residue |
| a vector field | `X = 0` | position | index `±1`, … |
| the Bloch function `f(k)` | `f(K) = 0` | `K` in the zone | winding number |
| the cone's apex | the datum | `θ` | `δ/2π = 1 − sin θ` |

The last row is the one that makes the pattern non-circular: the cone's charge is not an integer, it is
a real number in `[0, 1]`, because the apex is a *metric* singularity and not a zero of a map. Same
sum rule, different coefficient group. Naming the coefficient group is the whole discipline.

## Six charges, one shape

| theorem | local charge | global statement |
|---|---|---|
| argument principle | `ord_z f` | `(1/2πi) ∮ d log f = Σ ord` |
| residues | `res_z ω` | `(1/2πi) ∮ ω = Σ res` |
| Gauss–Bonnet | deficit `δ_i` | `∫ K dA + ∮ k_g ds = 2π χ` |
| Poincaré–Hopf | `ind_p X` | `Σ ind = χ` |
| Berry phase | winding `w` | `γ = π Σ w (mod 2π)` |
| Lefschetz | `sign det(I − dF_p)` | `L(F) = Σ` |

Every one is a sum over zeros. Every one is a boundary statement: the left side is an integral over a
boundary or a count of a boundary, the right side is the interior's zeros. That is why these are the
theorems the corpus can transfer exactly and the bulk dynamical ones it cannot — the boundary is the
only thing a crease has, and it is enough.

## They meet only at vertices, and the vertex conserves the charge

A crease does not meet another crease transversally. Two smooth zero sets `h₁ = 0` and `h₂ = 0` meet at
codimension two, which is a point, a line, or nothing — not a crease crossing. What looks like creases
meeting is a **single zero of higher order**: near it

```
h = Re(z^k) ,        zeros at  cos kθ = 0 ,        θ = π/2k + jπ/k ,
```

so `k` unoriented creases meet at equal angles `π/k`, and the point is a vertex of the network, not an
intersection of independent creases. Under a perturbation the vertex **splits**:

```
z^k  ↦  Π (z − z_i) ,        Σ k_i = k ,        Σ z_i = 0  (centred) .
```

The individual creases move and the vertex dissolves, but the total charge is fixed. That is the
conservation law of the network: *a vertex is a sum, and a sum is what a perturbation cannot change.*
The same holds for the cone's deficits, where additivity is Gauss–Bonnet, and for the Dirac points,
where it is the total winding.

## The hexagon is the `k = 6` vertex

Take `h = Re(z⁶)`. Its zeros are six lines at

```
θ = 15°, 45°, 75°, 105°, 135°, 165° ,
```

spaced `π/6 = 30°`. The symmetry is read off in one line, since `h(e^{iφ} z) = Re(e^{i6φ} z⁶)`:

| rotation `φ` | factor `e^{i6φ}` | effect on `h` |
|---|---|---|
| `30°` | `−1` | **`h ↦ −h`**: same creases, layers swapped |
| `60°` | `+1` | `h` unchanged |
| `90°` | `−1` | `h ↦ −h` |

So the two numerals of the closure note are exact operators on this height:

- `α = 30°` is the angle that **negates** the height — it fixes the crease set and exchanges the two
  sides. That is the fold, and it is why `α` is the fold angle rather than a lattice rotation;
- `2α = 60°` is the smallest rotation that **preserves** the height, and `(2α)·6 = 2π` closes.

Six anti-symmetries compose to `+1`, which is the sign statement of `2αm = 2π` with `m = 6`. And the
six creases split into two orbits of three under the `60°` rotation — because a crease is an
unoriented line, `θ` and `θ + 180°` are the same — which is the `D₆/D₃` bit of `the-fold-hexagon.md`,
now with a body: the two classes are the two parities of the six zero-rays. Rotating by `15°` maps the
crease set to the **gaps**, which is the same statement as the integer-line note's "the crease falls in
a gap".

The overall rotation of the pattern is the modulus `n`; the spacing, the split into two orbits, and the
`30°` negation are the invariants. That is the whole difference between the parameters and the charge.

The homogeneous function h=Re(z^6) gives a local six-line crease star, not a periodic honeycomb height field: its zero lines all pass through one point. A global periodic network needs separate translation-lattice data and, for the honeycomb, a two-site basis. The general wallpaper-group and sign-character treatment is now in the-fold-periodic-networks.md (UF-005).

The physical reflections are offset by half a crease step: \(\theta_j=\pi/12+j\pi/6\). Their complex form is \(\sigma_j(z)=e^{i(2j+1)\pi/6}\overline z\); each fixes its own zero-line and sends \(h\) to \(-h\). The base reflection at 15° and the 60° rotation generate \(D_6\). Alternating A/B labels on the hexagon vertices split the six axes into three preserving and three exchanging creases. The detailed point-group and character calculation is in `the-fold-hexagonal-lattice.md`.

## The Dirac zero, and what its winding buys

`f(k)` near `K` behaves as `q e^{iφ}` — a simple zero — and a zero of order `k` behaves as `q^k e^{ikφ}`.
The eigenvector of `h = Re(f)σ_x + Im(f)σ_y` is `(1, e^{i arg f})/√2`, so as `φ` runs once around the
zero, `arg f` advances `2πk` and the Berry phase is

```
γ = π k  (mod 2π) .
```

So the Dirac point's parameter is its winding, and everything the host calls topological is that
integer: `k = 1` gives `γ = π` (graphene), `k = 2` gives `0` (bilayer), `k = 6` gives `0` again. The
hexagon supplies the lattice on which the `k = 1` zero sits; the winding is the zero's own charge, not
the lattice's.

## What is not local

The charge is local; almost everything else is not. Three false friends, all of them near this note:

- "the gap is at the Dirac point" — the **closing** is at the zero; the gap is a bulk spectral
  property, and it is `2|m|` at every `q`. Zero and gap are different objects;
- "the crease is the curvature" — the curvature is `δ` at the apex, a charge; the crease is where the
  height vanishes and has zero curvature;
- "the sum rule explains the bulk" — it computes the total charge from the zeros and says nothing about
  the spectrum away from them. Index theorems are boundary statements; they are exact precisely because
  they refuse to look at the bulk.

## The restatement

A crease is a zero of a height, and the zero carries the only data that survives deformation — an
integer, or a deficit if the singularity is metric. Creases appear to meet, but what meets is a single
zero of higher order, and it conserves the charge when it splits. Everything else in the corpus
interconnects by summing those charges over a boundary. Each zero has its own parameters; the sum is
the same for all of them.

Move the crease from the space of the unknown to the space of the parameter and it has another name:
the **discriminant**, the set of parameter values where the number of zeros changes. Its local model is
`x² = t`, its parameter count is the order minus one, and its strata are the collision types. See
`the-fold-discriminant.md`.
