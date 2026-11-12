# The universal logarithm: the one coefficient the cutoff does not set

## The claim

The area note separated the horizon's exponent from its coefficient. The entanglement note gave the
wedge's area law and showed that its leading coefficient is the cutoff's. The holography note gave the
one case where the coefficient is a bulk coupling, and the Wald note gave the general gravitational
coefficient. This note asks about the one term in the ultraviolet expansion that is not a power of the
cutoff: the logarithm.

For a smooth spherical entangling surface in `n` spacetime dimensions,

```
S_EE = (power terms) + g_0 ln(ε/R) + S_0
```

In even `n`,

```
g_0 = (−1)^{n/2} 4 a_n
```

where `a_n` is the A-type conformal anomaly. In two dimensions `a_2 = c/12`, so `g_0 = −c/3` and
`S = (c/3) ln(R/ε)`. In four dimensions `a_4 = a`, so `g_0 = 4a` and `S = −4a ln(R/ε)`. In odd
spacetime dimensions the anomaly vanishes: there is no log term, and the universal term is a constant.

The coefficient is universal in the precise sense: the cutoff does not set it, and the regularization
does not shift it; the CFT's A-type anomaly does. It is not theory-independent. The Fold's `ln` is the
additive height; the coefficient is external. The `1/2` of the theta critical line is a different
object.

## The expansion

For a region `V` with smooth edge `∂V`, the entanglement entropy in a local quantum field theory has
the short-distance expansion

```
S_V = Σ_{k>0} g_k ε^{−k} + g_0 ln ε + S_0
```

where `ε` is the UV cutoff and the `g_i` are local functionals of the edge geometry. With `d = n − 1`
spatial dimensions, this is Casini and Huerta's

```
S_V = Σ_{k=1}^{d−1} g_k ε^{−k} + g_0 ln ε + S_0
```

For a smooth surface the leading power is `k = n − 2` when `n > 2`; at `n = 2` the power sum is empty
and the log is leading. The power terms are non-universal: their coefficients depend on the
regularization. The log coefficient `g_0` is universal: it is independent of the cutoff and the scheme,
though it depends on the CFT's field content. The finite part `S_0` can also shift under a change of
scheme.

| term | dependence | status |
|---|---|---|
| leading power (`n > 2`) | `ε^{−(n−2)}` | non-universal |
| subleading powers | `ε^{−k}`, `k > 0` | non-universal |
| logarithm | `ln ε` | universal |
| finite part | `ε^0` | scheme-dependent |

At `n = 2` the power sum is empty and the log is the leading term.

"Universal" means independent of the cutoff and the regularization, not independent of the theory. The
log coefficient is a property of the CFT and of the entangling surface. For a sphere it is the A-type
anomaly; for a general surface, type-B and extrinsic terms can enter.

## Two dimensions: the exact logarithm

In `n = 2`, the entangling surface is a point, the area exponent `n − 2` is zero, and the log is the
leading term. For a single interval of length `L` in an infinite line,

```
S_EE = (c/3) ln(L/ε)
```

where `c` is the Virasoro central charge. This is the Holzhey–Larsen–Wilczek result. For a finite
system the same formula holds with `L` replaced by the chord length; the periodic case carries `c/3`,
the open case `c/6`. For a real scalar `c = 1`, so `S = (1/3) ln(L/ε)`, and `g_0 = −1/3` in the
`g_0 ln(ε/R)` convention.

The vanishing of the area exponent is the exact reason the log is leading: there is no `ε^{−(n−2)}`
term to dominate it. The Fold's `n − 2` exponent is zero in the same counting. The coefficient `c/3` is
the Virasoro central charge, not the Fold's.

## Four dimensions: the type-A anomaly

In `n = 4` the trace anomaly has two coefficients,

```
⟨T⟩ = −a E_4 + c W² + …
```

with `E_4` the Euler density and `W` the Weyl tensor. The sphere's log term is fixed by `a` alone:

```
S_EE = (power terms) + 4a ln(ε/R) + S_0 = (power terms) − 4a ln(R/ε) + S_0
```

The type-B coefficient `c` does not contribute to the sphere's log. For a real scalar `a = 1/360`, so
`4a = 1/90` and `S = −(1/90) ln(R/ε) + …`; this is Casini and Huerta's `g_0 = 1/90` in the
`g_0 ln(ε/R)` convention. In units `R = 1`, Solodukhin's normalization gives the same term,
`4a ln ε` (his anomaly coefficient is `4a/π²`); for the scalar this is `(1/90) ln ε`.

The power terms are scheme-dependent. The log is not: it is the type-A anomaly. For a general
entangling surface, type-B and extrinsic-curvature terms can contribute; the sphere is the case where
only `a` survives. Solodukhin's 2008 paper separates the type-A (topological) and type-B (extrinsic)
parts; Schwimmer and Theisen argued that the Ryu–Takayanagi prescription can miss the type-A piece for
surfaces with extrinsic curvature. The sphere is the case where the direct CFT calculations of Casini
and Huerta, and of Solodukhin, agree with the holographic value.

## The coefficient table

For one real scalar, the exact coefficients are:

| `n` | `g_0` in `g_0 ln(ε/R)` | coefficient of `ln(R/ε)` | `a_n` |
|---|---|---|---|
| 2 | `−1/3` | `+1/3` | `1/12` |
| 4 | `+1/90` | `−1/90` | `1/360` |
| 6 | `−1/756` | `+1/756` | `1/3024` |
| 8 | `+23/113400` | `−23/113400` | `23/453600` |

The sign alternates: `g_0 = (−1)^{n/2} 4a_n`. The table is the scalar's contribution; a general CFT
replaces `a_n` by the total A-type anomaly, which is the sum over its fields. The scalar values are
Casini and Huerta's table; the `a_n` column is `g_0` divided by `(−1)^{n/2}4`.

## No log in odd dimensions

In odd spacetime dimensions the trace anomaly of a CFT vanishes: the would-be A-type coefficient is
absent. The sphere's universal term is a constant, the finite part `S_0`, not a logarithm. The divergent
expansion still has power terms, but the `ε^0` term is not accompanied by `ln ε`.

This is why the table has only even `n`. The Fold's area exponent `n − 2` is odd in odd `n`; the absence
of the log is the anomaly's vanishing, not a failure of the area counting. For a smooth surface the
statement is exact; corners can produce additional logs, which are not the sphere's universal term.

## The holographic check

The cleanest exact case is AdS₃/CFT₂. Brown and Henneaux give

```
c = 3ℓ/(2G_N)
```

and the two-dimensional formula becomes

```
S_EE = (c/3) ln(L/ε) = (ℓ/(2G_N)) ln(L/ε)
```

The bulk's `1/G_N` sets the log coefficient. This is the log analog of the Ryu–Takayanagi coefficient
match: the same `1/G_N`, now multiplying a logarithm.

In higher dimensions, Myers and Sinha show that the universal coefficient in the entanglement entropy is
the A-type central charge:

```
S_univ = (−1)^{n/2−1} 4 a_n ln(2ℓ/δ)
```

for even `n`, with `δ` the cutoff and `ℓ` the AdS scale. In four-dimensional Einstein gravity `a = c`;
higher-curvature terms can separate them. The sphere is the case where the identification is clean; for general surfaces
with extrinsic curvature, the Ryu–Takayanagi prescription can miss the type-A piece, as Schwimmer and
Theisen argued.

## The Fold's reading: the logarithm is a height

The Fold's scale is multiplicative: `g_a ∘ g_b = g_{ab}`, and `det g_k = k^n`. The logarithm is the map
that turns that multiplicative ledger into an additive one:

```
ln(ab) = ln a + ln b
```

The Fold already uses this map: the theta note's height is `h = ln t`, and the Dirichlet term uses the
scale height `h = ln n`, `n^{-s} = e^{−σh} e^{−ith}`. In the height coordinate, a change of scale
`ε → λε` is a translation `h → h + ln λ`; the log term `g_0 ln(ε/R)` is the one term in the entropy
expansion that is linear in that height. The power terms are exponentials `e^{−k h}`; the log is the
linear term.

That is the rhyme. The Fold supplies the `ln` — the height coordinate and its additivity — but not the
coefficient. `g_0` is the A-type anomaly; the Fold has no anomaly, no CFT, and no field content. In the
`n = 2` case the Fold's area exponent `n − 2` is zero, so the log is the leading term; that is the exact
exponent statement, not a derivation of `c/3`. The shared object is the logarithm as a height
coordinate, not the same argument: the theta height is `ln t`, the entropy height is `ln(ε/R)`.

| reading | exact object | Fold's version |
|---|---|---|
| power terms | `ε^{−k}` | scale ledger, multiplicative `k` |
| log term | `g_0 ln(ε/R)` | height `h = ln k`, additive |
| coefficient | A-type anomaly `a_n` | external |
| 2D leading log | `(c/3) ln(L/ε)` | `n − 2 = 0` exponent |
| odd `n` | no log | anomaly vanishes |

## The false friend: `1/2` is not the log coefficient

The theta note derives the critical line `Re s = 1/2` from the half-density exponent of
`ϑ(1/t) = √t ϑ(t)`. That `1/2` is an exponent: the square root of the Jacobian of `t ↦ 1/t`. The log
coefficient here is `g_0`, and the scalar values are `−1/3`, `1/90`, `−1/756`, `23/113400`; none is
`1/2`. The two numbers have different jobs: one is the axis of the theta fold, the other is the weight
of the height in the entropy expansion.

There is a near miss in two dimensions: `g_0 = −c/3`, so a CFT with `c = 3/2` has `|g_0| = 1/2`. That
is a coincidence of that theory's central charge, not the theta half-density. The theta `1/2` is fixed
by the modular identity; the log coefficient is fixed by the anomaly. The rhyme is the logarithm and the
height, not the number.

| `1/2` | where it appears | what it is |
|---|---|---|
| theta half-density | `ϑ(1/t) = √t ϑ(t)` | exponent; gives `Re s = 1/2` |
| log coefficient | `g_0 ln(ε/R)` | the A-type anomaly; not `1/2` in the scalar cases |
| 2D `c/3` | `S = (c/3) ln(L/ε)` | Virasoro central charge; `1/2` only if `c = 3/2` |

## Adjacent research

Holzhey, Larsen, and Wilczek found the two-dimensional logarithm. Casini and Huerta computed the
sphere's log in any dimension and gave the coefficient table. Solodukhin identified the four-dimensional
log with the type-A anomaly and separated the type-A and type-B contributions. Myers and Sinha showed
that in even dimensions the universal coefficient is the A-type central charge. Schwimmer and Theisen
argued that the holographic prescription can miss the type-A piece for surfaces with extrinsic
curvature. Graham and Witten computed the conformal anomaly of submanifold observables. Komargodski and
Schwimmer proved the four-dimensional `a`-theorem; Brown and Henneaux fixed the AdS₃ central charge.
This note borrows the expansion, the coefficient table, the anomaly identification, and the holographic
check. It does not derive the anomaly, the CFT, or the coefficient from the Fold.

| topic | reference | link |
|---|---|---|
| 2D logarithm | Holzhey, Larsen, Wilczek, *Geometric and renormalized entropy in conformal field theory*, Nucl. Phys. B424 (1994) 443–467 | [arXiv](https://arxiv.org/abs/hep-th/9403108) |
| sphere in any dimension | Casini & Huerta, *Entanglement entropy for the n-sphere*, Phys. Lett. B694 (2010) 167–171 | [arXiv](https://arxiv.org/abs/1007.1813) |
| type A and extrinsic geometry | Solodukhin, *Entanglement entropy, conformal invariance and extrinsic geometry*, Phys. Lett. B665 (2008) 305–309 | [arXiv](https://arxiv.org/abs/0802.3117) |
| round spheres | Solodukhin, *Entanglement entropy of round spheres*, Phys. Lett. B693 (2010) 605–608 | [arXiv](https://arxiv.org/abs/1008.4314) |
| universal coefficient | Myers & Sinha, *Holographic c-theorems in arbitrary dimensions*, JHEP 1101 (2011) 125 | [arXiv](https://arxiv.org/abs/1011.5819) |
| trace anomalies and holography | Schwimmer & Theisen, *Entanglement entropy, trace anomalies and holography*, Nucl. Phys. B801 (2008) 1–24 | [arXiv](https://arxiv.org/abs/0802.1017) |
| submanifold anomaly | Graham & Witten, *Conformal anomaly of submanifold observables in AdS/CFT correspondence*, Nucl. Phys. B546 (1999) 52–64 | [arXiv](https://arxiv.org/abs/hep-th/9901021) |
| 4D `a`-theorem | Komargodski & Schwimmer, *On renormalization group flows in four dimensions*, JHEP 1112 (2011) 099 | [arXiv](https://arxiv.org/abs/1107.3987) |
| RT formula | Ryu & Takayanagi, *Holographic derivation of entanglement entropy from AdS/CFT*, Phys. Rev. Lett. 96 (2006) 181602 | [arXiv](https://arxiv.org/abs/hep-th/0603001) |
| AdS₃ central charge | Brown & Henneaux, *Central charges in the canonical realization of asymptotic symmetries*, Commun. Math. Phys. 104 (1986) 207 | [DOI](https://doi.org/10.1007/BF01211590) |

## Checks

The coefficient rows are literature values, not recomputed here. The arithmetic that relates `g_0` and
`a_n` is exact.

| check | value |
|---|---|
| 2D scalar `g_0` | `−1/3` |
| 2D scalar `S` | `(1/3) ln(L/ε)` |
| 4D scalar `g_0` | `+1/90` |
| 4D scalar `S` | `−(1/90) ln(R/ε)` |
| 6D scalar `g_0` | `−1/756` |
| 8D scalar `g_0` | `+23/113400` |
| sign pattern | `g_0 = (−1)^{n/2} 4a_n` |
| 2D: `4a` | `4 × 1/12 = 1/3` |
| 4D: `4a` | `4 × 1/360 = 1/90` |
| 6D: `4a` | `4 × 1/3024 = 1/756` |
| 8D: `4a` | `4 × 23/453600 = 23/113400` |
| 4D coefficient of `ln(R/ε)` | `−4a` |
| odd `n` | no log term |
| AdS₃/CFT₂ | `c = 3ℓ/(2G_N)`, `S = (ℓ/(2G_N)) ln(L/ε)` |

The exact-arithmetic rows check the sign and the factor `4`; they do not check the dynamical values,
which are the literature's. The AdS₃/CFT₂ row is the Brown–Henneaux and Ryu–Takayanagi result. The
"odd `n`" row is the vanishing of the anomaly, not a numerical cancellation.

## What this does and does not say

- It **does** state the short-distance expansion and identify the logarithmic coefficient `g_0` as the
  universal term.
- It **does** give the exact two-dimensional result `S = (c/3) ln(L/ε)` and the exact four-dimensional
  result `S = −4a ln(R/ε)`.
- It **does** identify `g_0` with the A-type anomaly in even dimensions,
  `g_0 = (−1)^{n/2} 4a_n`, and give the scalar coefficient table for `n = 2, 4, 6, 8`.
- It **does** state that there is no log term in odd spacetime dimensions; the universal term is a
  constant.
- It **does** give the AdS₃/CFT₂ check `S = (ℓ/(2G_N)) ln(L/ε)` and the Myers–Sinha identification in
  higher dimensions.
- It **does** identify the Fold's `ln` height as the additive rhyme and the vanishing of `n − 2` as the
  reason the log is leading in two dimensions.
- It **does** name the `1/2` of the theta critical line as a false friend: it is the half-density
  exponent, not the log coefficient.
- It **does not** derive the anomaly, the CFT, the coefficient `g_0`, or holography from the Fold.
- It **does not** claim the Fold's `k` is the cutoff, the anomaly, or the log coefficient.
- It **does not** claim the log term is the area law's coefficient; it is the leading term at `n = 2`
  and the universal subleading term for `n > 2`.
- It **does not** claim the critical line's `1/2` is the log coefficient, even in a theory where the
  numbers coincide.
- It **does not** treat general entangling surfaces beyond the sphere; type-B and extrinsic-curvature
  contributions are cited, not computed.
- It **does not** treat the full interacting entropy; it treats the universal coefficient.
- It **does not** prove the `a`-theorem or the `c`-theorem; it cites them.

## The one sentence

**The logarithmic term in the entanglement entropy is the one term the cutoff does not set: in even
spacetime dimension `n` the coefficient of `ln(R/ε)` is `(−1)^{n/2−1} 4a_n`, the A-type conformal
anomaly — `c/3` in two dimensions and `−4a` in four — while in odd dimensions it vanishes; the Fold's
`ln` height is the additive rhyme, but the coefficient is the anomaly's, not the Fold's, and the `1/2`
of the critical line is a different object.**

## Files

`the-fold-logarithm.md` (this note). The wedge's entropy and the area law are in
`the-fold-entanglement.md`; the holographic coefficient and the AdS₃/CFT₂ log are in
`the-fold-holography.md`; the general coefficient and the Noether charge are in `the-fold-wald.md`; the
area exponent and the `n = 2` log case are in `the-fold-area.md`; the theta half-density and the
critical line are in `the-fold-theta.md`; the zeta dictionary is in `the-fold-zeta.md`; the open-problem
boundaries are in `the-fold-problems.md`; the order is in `the-fold-creation.md`; the lookup is
`the-fold-key.md`.
