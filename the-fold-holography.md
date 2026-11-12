# The holographic coefficient: Ryu–Takayanagi and the minimal surface

## The claim

The area note gave the horizon `S = A/4ℓ_P²` and separated the exponent from the coefficient. The
entanglement note gave the wedge `S_EE ~ A/ε^{n−2}` and showed that its coefficient is the cutoff's. This
note asks when the coefficient is fixed. There is one exact case in this thread: the holographic case.

Ryu and Takayanagi proposed

```
S_EE = A_min/(4G_N)
```

where `A_min` is the area of the minimal bulk surface homologous to the boundary entangling region and
`G_N` is the bulk Newton constant. The coefficient is exactly the Bekenstein–Hawking `1/4G_N`. This is
the one setting where the area law's coefficient is not the cutoff's.

The Fold's `S ∝ A` supplies the exponent. The bulk geometry, the minimal surface, and `1/4G_N` are the
holographic theory's. The RT formula is a precise rhyme with the Fold's area law, not a derivation.

## The RT formula

In the AdS/CFT correspondence, a `d`-dimensional boundary CFT is dual to a `(d+1)`-dimensional bulk. For
a spatial entangling region `A` on the boundary, the entanglement entropy is

```
S_EE(A) = A_min(∂A)/(4G_N)
```

where `∂A` is the entangling surface (codimension two on the boundary), and `A_min` is the minimal
surface in the bulk homologous to `A`. The surface is anchored on `∂A`.

The dimensions close exactly. In `D = d+1` bulk dimensions:

```
[G_N] = length^{D−2} = length^{d−1},        [A_min] = length^{D−2} = length^{d−1}
```

so `A_min/G_N` is dimensionless. The minimal surface has codimension two in the bulk, the same
codimension as the entangling surface on the boundary.

| boundary CFT | bulk | entangling surface | minimal surface | `G_N` |
|---|---|---|---|---|
| `d = 2` | AdS₃ | point | geodesic (1D) | length¹ |
| `d = 3` | AdS₄ | line | 2D | length² |
| `d = 4` | AdS₅ | surface | 3D | length³ |
| `d = 5` | AdS₆ | 3-surface | 4D | length⁴ |

The static case is the minimal surface; the time-dependent case uses the extremal surface
(Hubeny–Rangamani–Takayanagi). The homology condition is what selects the surface: it must be homologous
to the entangling region.

## The coefficient match

The Bekenstein–Hawking entropy of a bulk horizon is

```
S_BH = A_horizon/(4G_N)
```

and the RT formula is

```
S_EE = A_min/(4G_N)
```

The same `1/4G_N` appears in both. For the whole-boundary region in a static thermal state, the minimal
surface is the horizon of the bulk black hole, so the boundary entanglement entropy equals the bulk
horizon entropy. That is the exact sense in which the coefficient closes: the boundary's entanglement is
the bulk's geometry.

The match is not a coincidence of notation. Both entropies are gravitational entropies in the same bulk
theory, and the RT surface is the same codimension-two object as the horizon cross-section. The boundary
CFT's entanglement is the bulk's area.

## The species problem in the holographic case

The entanglement note's species problem was: `c` scales with the number of fields, while `1/4G` does not.
The holographic case does not make `c` universal. It relates the boundary's degrees of freedom to the
bulk's `1/G_N` through the duality.

For `N = 4` super-Yang–Mills with `SU(N_c)`, the boundary has `~N_c²` degrees of freedom, and the bulk
has

```
ℓ^{d−1}/G_N ~ N_c²
```

where `ℓ` is the AdS radius. The RT entropy `A_min/(4G_N)` scales as `N_c²`, matching the boundary's
species count. The coefficient is not a fixed number; it is the bulk coupling, which the duality ties to
the boundary's rank.

| quantity | boundary | bulk |
|---|---|---|
| degrees of freedom | `~N_c²` | `ℓ^{d−1}/G_N` |
| entropy | `S_EE` | `A_min/(4G_N)` |
| coefficient | `c` (cutoff-dependent) | `1/4G_N` (bulk coupling) |

So the holographic case resolves the species problem by **relating** the two coefficients, not by
identifying them. The boundary's `c` and the bulk's `1/4G_N` are dual descriptions of the same count.

## The Fold's reading

The Fold's area law is `S ∝ A`; the exponent is `n−2`. The RT formula has the same exponent and a fixed
coefficient. The Fold has no bulk, no `G_N`, and no minimal surface. The shared objects are:

- the **codimension-two surface**: the RT minimal surface and the horizon cross-section;
- the **area exponent**: `A ∝ R^{n−2}`;
- the **`2π` modular period**: the RT derivation uses the same replica/thermal circle;
- the **null crease**: the horizon's null limit.

They are rhymes, not a derivation. The Fold cannot supply `1/4G_N` because it has no gravitational
coupling; the holographic theory supplies it because it has a bulk. The Fold's contribution is the
exponent and the area measure, exactly as in `the-fold-area.md`.

| reading | exact object | Fold's version |
|---|---|---|
| entangling surface | `∂A`, codimension two | horizon cross-section |
| minimal surface | `A_min` in the bulk | no bulk |
| coefficient | `1/4G_N` | external |
| exponent | `n−2` | `S ∝ A` |
| modular period | `2π` | twist/closure's `2π` |

## The quantum corrections

The classical RT formula is the leading term. Faulkner, Lewkowycz, and Maldacena gave the quantum
correction:

```
S_EE = A_min/(4G_N) + S_bulk + counterterms
```

where `S_bulk` is the entanglement entropy of the bulk fields across the minimal surface. The coefficient
`1/4G_N` is still the classical gravitational term; the quantum correction adds the bulk's own
entanglement. This is the holographic version of the entanglement note's coefficient caveat: the leading
area term is gravitational, and the subleading terms are the matter sector's.

The RT formula itself is a proposal, derived in the holographic framework by Lewkowycz and Maldacena via
the replica trick. It is not a general theorem about arbitrary quantum field theories. The note cites it
as the exact holographic case, not as a Fold result.

## Adjacent research

Ryu and Takayanagi proposed the minimal-surface formula; Hubeny, Rangamani, and Takayanagi gave the
covariant extremal-surface version; Lewkowycz and Maldacena derived the classical formula from the
gravitational replica trick; Faulkner, Lewkowycz, and Maldacena gave the quantum corrections. Brown and
Henneaux computed the AdS₃ central charge, which makes the AdS₃/CFT₂ log term exact. Maldacena's duality
is the framework. This note borrows the RT formula, the dimension count, and the coefficient match. It
does not derive holography, the RT formula, or the `1/4G_N`.

| topic | reference | link |
|---|---|---|
| RT formula | Ryu & Takayanagi, *Holographic derivation of entanglement entropy from AdS/CFT*, Phys. Rev. Lett. 96 (2006) 181602 | [arXiv](https://arxiv.org/abs/hep-th/0603001) |
| RT aspects | Ryu & Takayanagi, *Aspects of holographic entanglement entropy*, JHEP 0608 (2006) 045 | [arXiv](https://arxiv.org/abs/hep-th/0605073) |
| covariant RT | Hubeny, Rangamani, Takayanagi, *A covariant holographic entanglement entropy proposal*, JHEP 0707 (2007) 062 | [arXiv](https://arxiv.org/abs/0705.0016) |
| replica derivation | Lewkowycz & Maldacena, *Generalized gravitational entropy*, JHEP 1308 (2013) 090 | [arXiv](https://arxiv.org/abs/1304.4926) |
| quantum corrections | Faulkner, Lewkowycz, Maldacena, *Quantum corrections to holographic entanglement entropy*, JHEP 1311 (2013) 074 | [arXiv](https://arxiv.org/abs/1307.2892) |
| AdS₃ central charge | Brown & Henneaux, *Central charges in the canonical realization of asymptotic symmetries*, Commun. Math. Phys. 104 (1986) 207 | [DOI](https://doi.org/10.1007/BF01211590) |
| AdS/CFT | Maldacena, *The large N limit of superconformal field theories and supergravity*, Adv. Theor. Math. Phys. 2 (1998) 231 | [arXiv](https://arxiv.org/abs/hep-th/9711200) |

## Checks

| check | value |
|---|---|
| `A_min/G_N` dimension | `length^{d−1}/length^{d−1}` = dimensionless |
| minimal surface codimension | 2 in the bulk |
| RT coefficient | `1/4G_N` |
| Bekenstein–Hawking coefficient | `1/4G_N` |
| AdS₃ central charge | `c = 3ℓ/(2G_N)` |
| AdS₃/CFT₂ log | `S_EE = (c/3) ln(L/ε) = (ℓ/(2G_N)) ln(L/ε)` |
| boundary species | `~N_c²` |
| bulk coupling | `ℓ^{d−1}/G_N ~ N_c²` |
| quantum correction | `S_EE = A_min/(4G_N) + S_bulk + …` |

The dimension and coefficient rows are exact. The AdS₃/CFT₂ rows are the standard Brown–Henneaux and
RT results. The species rows are the large-`N` scaling, not an exact equality for finite `N_c`.

## What this does and does not say

- It **does** state the RT formula `S_EE = A_min/(4G_N)` and the dimension count that makes it
  dimensionless.
- It **does** show that the RT coefficient is exactly the Bekenstein–Hawking `1/4G_N`, in the same bulk
  theory.
- It **does** show that the holographic case relates the boundary's species count `~N_c²` to the bulk's
  `ℓ^{d−1}/G_N`, rather than making the coefficient universal.
- It **does** give the FLM quantum correction `A_min/(4G_N) + S_bulk + …`.
- It **does** identify the shared objects — the codimension-two surface, the area exponent, the `2π`
  period, the null crease — as rhymes with the Fold.
- It **does not** derive the RT formula, holography, or the `1/4G_N` from the Fold.
- It **does not** claim the Fold has a bulk, a minimal surface, or a Newton constant.
- It **does not** claim the RT formula is a general theorem; it is a holographic proposal, derived in
  that framework.
- It **does not** solve the species problem; it states the holographic relation.
- It **does not** treat finite-`N` corrections, non-holographic theories, or the full FLM formula beyond
  the leading correction.

## The one sentence

**In the holographic case the wedge's coefficient is exactly the Bekenstein–Hawking `1/4G_N`, because the
entanglement entropy is the area of a minimal bulk surface; the Fold's `S ∝ A` supplies the exponent, but
the bulk geometry and the coefficient are the holographic theory's, not the Fold's.**

## Files

`the-fold-holography.md` (this note). The wedge's entropy and the coefficient caveat are in
`the-fold-entanglement.md`; the horizon's area and the Bekenstein–Hawking coefficient are in
`the-fold-area.md`; the Rindler wedge and the modular period are in `the-fold-unruh.md`; the null crease
is in `the-fold-horizon.md`; the open-problem boundaries are in `the-fold-problems.md`; the order is in
`the-fold-creation.md`; the lookup is `the-fold-key.md`.
