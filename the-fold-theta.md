# The theta fold: why the critical line is at one-half

## The gap

The zeta note says the functional equation is a fold. It does not say where the fold comes from. The
mechanism is Riemann's theta identity, and it answers the sharpest structural question: why is the
critical line at `1/2`?

The answer is exact: the theta modular factor is `t^{1/2}`, and that exponent is the real part of the
critical line. Change the exponent and the line moves. The theta fold gives the axis; it does not give
the zeros.

The analytic pipeline's initial state is the theta function itself, with the modular factor `t^{1/2}`
as its initial form; the geometric register's initial state is the point. They are different initial
objects, and they meet at the crease. See `the-fold-initial.md`.

## The theta fold

Write `ϑ` for the theta function, to keep `θ` for the aperture:

```
ϑ(t) = Σ_{n∈ℤ} e^{−πn²t} = 1 + 2Σ_{n≥1} e^{−πn²t},     t > 0
```

The modular identity is

```
ϑ(1/t) = √t ϑ(t)
```

In the height coordinate `h = ln t`, this is

```
ϑ(e^{−h}) = e^{h/2} ϑ(e^{h})
```

So the height reflection `h ↦ −h` is a fold: it exchanges `t < 1` and `t > 1`, and its crease is
`h = 0`, i.e. `t = 1`. The factor `e^{h/2}` is the **half-density**: the square root of the Jacobian of
the inversion. The identity is Poisson summation — the sum over the lattice and the sum over the dual
lattice are the same sum, and the Jacobian is the factor.

This height is longitudinal: `h` runs along the line the fold fixes. It is not the zeta zero's height
`t = Im s` (linear) and not the term's `ln n` (a scale). See `the-fold-crease-height.md`.

## The Mellin transform

For `Re s > 1`,

```
I(s) = ∫_0^∞ (ϑ(t) − 1)/2 · t^{s/2} dt/t = π^{−s/2} Γ(s/2) ζ(s)
```

The kernel is a scale and a twist in the height:

```
t^{s/2} dt/t = e^{(s/2)h} dh
```

So the Mellin transform is the continuous version of the Dirichlet sum: a sum over heights, with
`e^{(s/2)h}` as the scale-and-twist weight. The exponent `s/2` is the observer's dimension in this
reading.

## The derivation

Split the integral at `t = 1`:

```
I(s) = ∫_0^1 + ∫_1^∞
```

In the first half put `t = 1/u`, use `ϑ(1/u) = √u ϑ(u)`, and combine:

```
I(s) = ∫_1^∞ (ϑ(t) − 1)/2 [t^{s/2−1} + t^{(1−s)/2−1}] dt + 1/[s(s−1)]
```

The integral is symmetric under `s ↦ 1−s`; the constant is symmetric because
`s(s−1) = (1−s)(−s)`. Therefore

```
I(s) = I(1−s)
```

and, since `ξ(s) = ½ s(s−1) I(s)`,

```
ξ(s) = ξ(1−s)
```

That is the functional equation, derived rather than assumed. The fold in height is the cause; the
functional equation is its Mellin shadow.

## Why one-half

The derivation did not use the value `1/2`; it used the exponent of the modular factor. Generalize:
if a function satisfies

```
Φ(1/t) = t^α Φ(t)
```

the same split gives

```
I(s) = I(2α − s)
```

so the symmetry axis is

```
Re s = α
```

For the theta function, `α = 1/2`, so the critical line is `Re s = 1/2`. The `1/2` is the half-density
exponent of the theta fold. It is not an arbitrary convention and not a dynamical equilibrium: it is
the square root of the Jacobian of `t ↦ 1/t`, read through the Mellin transform.

This is the exact content of "the critical line is the crease." The crease in height is `h = 0`; the
Mellin transform turns the height reflection into `s ↦ 1−s`; the crease in `s` is `Re s = 1/2`. The
critical line is the image of the theta crease.

What this does **not** say is where the zeros are. The theta fold fixes the axis; it does not fix the
points on the axis. RH is still the statement that the zeros lie on the crease, and that remains open.

The theta function is also the heat kernel, and the completed zeta function is a heat-flow family. That
flow is the de Bruijn–Newman deformation: RH is equivalent to its constant `Λ ≤ 0`, and Rodgers–Tao
prove `Λ ≥ 0`. The theta fold is the `t = 0` slice. See `the-fold-problems.md`.

## The crease and the facet

The theta fold is the analytic origin of the critical-line facet. In the language of the facets note:

- the crease in height is `h = 0`, a point that divides the line;
- the crease in `s` is `Re s = 1/2`, a line that divides the plane;
- the zeros of `ξ` are points on that line; relative to the line, each is a facet of the line.

So the chain is: theta fold in height → Mellin transform → critical-line facet → zeros as points on the
facet. The first arrow is exact; the last is the hypothesis. This chain is the analytic pipeline; the
Fold's stage-by-stage zeros are the zero pipeline. See `the-fold-pipeline.md`.

## Checks

All numbers use `mpmath` 1.3.0 at 30 digits.

The theta modular identity:

| `t` | `ϑ(1/t) − √t ϑ(t)` |
|---|---|
| `0.3` | `2.9e−32` |
| `0.7` | `7.0e−32` |
| `1.7` | `0` |
| `3.0` | `0` |

The Mellin representation:

| `s` | `I(s) − π^{−s/2} Γ(s/2) ζ(s)` |
|---|---|
| `2 + 3i` | `2.3e−18` |
| `1.7 + 2.3i` | `4.2e−13` |

The functional equation itself was checked in `the-fold-zeta.md`: `ξ(s) − ξ(1−s) ≈ 6.8e−32` at
`s = 0.3 + 3i`. Here the numbers confirm the theta identity and the integral representation; the
derivation is algebraic.

## What this does and does not say

- It **does** derive the functional equation from the theta fold, rather than assuming it.
- It **does** explain the `1/2`: the theta modular exponent is `1/2`, and a general exponent `α` puts
  the axis at `Re s = α`.
- It **does** identify the crease: `h = 0` in height, `Re s = 1/2` in the Mellin plane.
- It **does not** prove RH. The fold fixes the axis, not the zeros' location.
- It **does not** make theta a physical field. `ϑ` is a modular theta function, the heat kernel on the
  circle; the geometry is exact, the physics words are not.
- It **does not** replace the explicit formula. Theta gives the functional equation; the explicit
  formula gives the exchange between the primes and the zeros.

## The one sentence

**The theta identity is a fold in height; its half-density exponent is the `1/2` of the critical line,
and the functional equation is the Mellin shadow of that fold — but the zeros' location is still the
open problem.**

## Files

`the-fold-theta.md` (this note). The functional equation and the zeta dictionary are in
`the-fold-zeta.md`; the critical line as a facet is in `the-fold-facets.md`; the crease and the two
sides are in `the-fold-occlusion.md`; the master key is `the-fold-key.md`.
