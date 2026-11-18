# The folded line from afar

## The phrase

A line is folded. From a distance the fold is too small to resolve, and the folded line looks like a
**singular line** — one line, not two. The image is exact, but two words need names: "from afar" and
"singular."

"From afar" can mean three operations. The first and third are exact; the second is their limit.

| model | the folded line | "from afar" | what is left |
|---|---|---|---|
| orthographic | a V with vertex on the crease | the projection `π_H` along the normal | the crease |
| coarse-grained | a pleated line | a blur wider than the pleat | the mean line |
| quotient | the image of a line under the sheet fold | the fold's orbit space | the crease, the boundary |

"Singular" also has three exact readings, and they meet at the same crease: **one line** (the quotient),
**non-smooth** (the derivative jump), and **rank-deficient** (the projection). The note states each, then
the correction: **from afar is a projection, not a scale.**

## One fold: the V and its crease

The Fold's global fold is the involution

```
σ_H(x) = x − 2(n·x)n
```

It fixes the crease `H` and flips the normal. It maps a line to a line: a reflection has no corner. The
physical fold of a sheet is not `σ_H` on both sides; in the idealization it is the quotient map that
fixes one side and applies `σ_H` to the other. With `H = {y = 0}`:

```
F(x, y) = (x, |y|)
```

`F` is continuous, fixes `y ≥ 0`, reflects `y ≤ 0`, and its image is the half-plane `y ≥ 0`. The crease
is the boundary `y = 0`.

A line `ℓ: y = m x + b` with `m ≠ 0` crosses the crease at `x₀ = −b/m`. Its image is the V

```
F(ℓ):  y = |m x + b|
```

with vertex `(x₀, 0)` on the crease. The two rays have slopes `±m`, so the opening angle is

```
θ = 2 arctan |m|
```

The shadow is the projection `π_H(x, y) = (x, 0)`: the V maps to the crease line, both rays coincide,
and the image is one line. Over the window `[x₀ − L, x₀ + L]`:

| quantity | value |
|---|---|
| height at the window edge | `\|m\| L` |
| shadow length | `2L` |
| path length | `2L √(1 + m²)` |
| chord | `2L` |
| path / shadow | `√(1 + m²) = 1 + m²/2 + O(m⁴)` |
| length excess | `L m² + O(m⁴)` |

The fold's height is `|m| L`; the length excess is `L m²` — quadratic in the height. The shadow sees the
first power (the height is dropped); the length sees the second power (the height is squared). For
`m = 0.1` and `L = 1`, the ratio excess is `0.00498756` against `m²/2 = 0.005`, a relative error of
`−2.5e−3`; the length excess is `0.00997512` against `L m² = 0.01`.

The global fold `σ_H` maps the same line to `y = −m x − b`, another line, with no corner. The sheet fold
`F` maps it to the V. The difference is the quotient: `F` is the quotient map by `σ_H`, and the crease is
its boundary. This is the first correction: **the folded line is the image of the sheet fold (the
quotient), not of the global reflection.**

## Many folds: the pleats and the mean

A line folded repeatedly becomes a pleated line. In cross-section, a triangle wave of amplitude `a` and
half-period `ℓ`:

```
y(x) = a · tri(x/ℓ)
```

The creases are the peak and valley lines; the midplane `y = 0` is the mean. The projection onto the
midplane is the straight line. The path length per half-period is `√(ℓ² + 4a²)`, so

```
length / shadow = √(1 + (2a/ℓ)²) = 1 + 2a²/ℓ² + O(a⁴)
```

The excess is quadratic in the amplitude. For `a/ℓ = 0.1`, the ratio is `1.0198039`, the excess
`0.0198039`, and `2a²/ℓ² = 0.02` (relative error `−9.8e−3`). The mean is `0`; the variance is `a²/3`
(measured `0.333337 a²`). The first moment is the crease; the second moment is the fold.

The coarse-graining model: convolve the pleated line with a Gaussian of width `w`. The first Fourier mode
of the triangle wave has amplitude `8a/π²` and is multiplied by `exp(−π² w²/(2ℓ²))`, so the residual
amplitude is

```
8a/π² · exp(−π² w²/(2ℓ²))
```

For `a = 1`, `ℓ = 1`, the measured residual at `w = 1` is `5.8295e−3`, and the formula gives
`8/π² · e^{−π²/2} = 5.8295e−3`. The log residual against `w²` has slope `−π²/2 = −4.9348` (measured
`−4.9348` from `w = 0.5` to `1`; `−5.06` over `[0.2, 2]`). The length density (blurred length over
shadow length) tends to `1`: `2.112` at `w = 0.05`, `1.126` at `w = 0.5`, `1.00008` at `w = 1`,
`1.000000` at `w = 2`. The pleats disappear from the image exponentially in `w²`; the length excess
disappears only when the blur resolves the pleats. The shadow is the mean; the fold is the variance.

**The corrugated fabric.** A sheet pleated in one direction is corrugated, and the coarse-grained
object is a flat plane with an anisotropic line element. Along the corrugation the same factor appears,

```
ds² = (1 + (2a/ℓ)²) dx² + dy² ,
```

so the metric changes by a constant and the Riemann tensor of the coarse-grained plane is zero. The
curvature is not spread through the fabric: it sits on the creases as a distribution, which is the
singular line. The amplitude `a` is the distance the shadow cannot see — the mean is zero, the fold is
the variance — and it is geometric, not spectral, because there is no operator here for a gap to belong
to. Calling the corrugation a curvature of space is the false friend; calling it an anisotropic flat
metric is exact.

Read as a graph, the sheet's curvature is `K = det(Hess h)/(1 + |∇h|²)²`. A uniform slope gives
`K = 0` — a tilted plane — and a radial slope gives the cone of `the-fold-cone.md`, zero away from the
apex. Only a height with a nonzero Hessian is curved. So the slope sets the anisotropy; the *bending*
of the height sets the curvature.

**The director is a line, not an arrow.** A corrugation has no preferred direction along itself: `n`
and `−n` name the same pleat. Its order parameter is therefore `ℝP¹`, and the arrow that double-covers
it has period `2π` where the pleat has period `π`. That `ℤ/2` is the same abstract group as the fold's
two layers, but it is not the same bundle: the layers are the two sides of the sheet, along the normal
line, while the director's double cover lives in the tangent plane. Same group, different bundle: that
is the false friend.

## The singular line

"Singular" has three exact readings, and they meet at the crease:

| sense | object | exact statement |
|---|---|---|
| one line | the quotient | the sheet fold identifies the two sides; the orbit space is a half-plane; the crease is its boundary |
| non-smooth | the sheet fold `F` | `F` is continuous but not differentiable across `H`; the normal derivative jumps from `+1` to `−1` (jump `2`); the V has a corner on `H` |
| rank-deficient | the projection `π_H` | rank `n−1`, kernel the normal line; the image of the V is the crease |

The line itself is smooth; the singularity is created by the fold. The crease is the fixed set of `σ_H`,
the boundary of the quotient, and the image of the V. The rank deficiency is global, but its image is the
same crease.

The smooth model behind `F` is the fold catastrophe

```
(x, y) ↦ (x, y²)
```

Its Jacobian is `diag(1, 2y)`, so its rank drops from `2` to `1` exactly on `y = 0`; the critical line is
the crease, and its image is the boundary of the half-plane. `F` is the piecewise square root of this map.
In singularity theory the critical set is the singular line; in the Fold it is the crease. The three
readings meet at one object: the crease.

The derivative jump: for `F(x, y) = (x, |y|)`, the normal derivative is `+1` above and `−1` below, so the
jump is `2`. Numerically, `(|h| − 0)/h = +1` for `h > 0` and `−1` for `h < 0`, at
`h = 10⁻¹, 10⁻³, 10⁻⁶, 10⁻⁹`. The folded line's singular point is the vertex; the crease it lies on is
the singular line. In the line's own dimension the crease is a point (codim 1); in the ambient plane the
crease is a line; in `n` dimensions it is a hyperplane. The phrase names the ambient codimension-one
crease, not the point.

## From afar is a projection, not a scale

The tempting reading is "from afar = scaled to zero": `k → 0`, the fold shrinks, and the line becomes
straight. That is false. The scale `k` multiplies both the height and the shadow:

```
height → k h,   shadow → k L,   height/shadow = h/L,   opening angle invariant
```

For `m = 0.2`, the ratio `height/shadow` is `0.1`, the opening angle is `22.619865°`, and `path/chord` is
`1.019804` for `k = 0.01, 0.1, 1, 10, 1000`. The shape is scale-invariant; the fold does not disappear
under `k`. What disappears is the **transverse height in the observer's projection**; "from afar" is the
observer's resolution coarser than the height, i.e. the ratio `h/D`, not `k`. If the observer and the
object scale together, the fold is invariant; if the observer's resolution is fixed and the object is
far, the height falls below the resolution. The exact operation is the projection `π_H` (or the
coarse-graining), not the scale. The observer's two parameters — form degree `d` and window `w` — are
in `the-fold-observer.md`; the discrete dual — sampling `N` and the Nyquist condition `N > 2m` — is in
`the-fold-sampling.md`.

This is the same split as the matter note: the height fixes the magnitudes, the shape is invariant. And
the same split as the occlusion note: the projection drops the side, the metric squares it. The folded
line from afar is the shadow; the length is the quadratic measurement that remembers the fold. See
`the-fold-matter.md`, `the-fold-occlusion.md`, and `the-fold-crease-height.md`.

## Rhyme: the unresolved doublet

A spectral line split by a fold into two components is a doublet. A spectrometer whose resolution is
coarser than the splitting sees one line at the mean. The splitting is the transverse height; the mean is
the crease; the unresolved singlet is the shadow. The same first/second moment structure: the mean is the
first moment, the splitting is the second. This is a rhyme, not the Fold's object: a spectral line is a
frequency, not a geometric line, and the Fold models the splitting, not the spectrum.

## Adjacent research

Every object in this note has a standard name in a neighboring field, and the standard statement is
sharper than the analogy. The table is the map; the subsections give the exact borrowing and the
boundary.

| field | here | there | what transfers |
|---|---|---|---|
| singularity theory | the V, the crease | Whitney fold; critical set and image | normal form, rank drop, critical set |
| vision and geometry | the shadow | apparent contour of a surface | the silhouette is the image of a fold |
| reflection groups | many creases | mirrors, chambers, quotient | the pleats are an affine reflection quotient |
| geometric measure theory | the shadow is shorter | 1-Lipschitz projection; Besicovitch–Federer | `H¹(π_H E) ≤ H¹(E)`; rectifiability |
| probability | mean and variance | law of total variance | the exact identity for a random phase |
| catastrophe optics | height versus resolution | Airy diffraction catastrophe | the `2/3` fringe law |
| spectroscopy | the unresolved doublet | Rayleigh and Sparrow criteria | the mean is exact, the singlet is an artifact |
| origami | crease pattern, folded state | rigid foldability; NP-hardness | input/witness/verifier rhyme |
| calculus of variations | the coarse-grained shadow | Γ-convergence, homogenization | limit density `√(1+s²)` and the excess |

### Whitney's fold and the critical set

A smooth map `f: ℝ² → ℝ²` whose differential has rank `1` at a point is, near that point, equivalent by
diffeomorphisms of source and target to

```
f(x, y) = (x, y²)
```

provided the second derivative across the kernel is nonzero. This is Whitney's **fold** normal form. Its
critical set is `{y = 0}`, a smooth curve; `f` restricted to the critical set is a diffeomorphism onto its
image, the boundary of the half-plane `y ≥ 0`. If the second derivative also vanishes and the third does
not, the normal form is the **cusp** `(x, y) ↦ (x, y³ + xy)`, whose image has a cusp point.

The note's V is not the image of a line under `f`: that image is the parabola `(x, (mx+b)²)`. The V is the
image under the quotient `F(x,y) = (x, |y|)`, and `f ∘ F = f`, `F ∘ F = F`. So `F` is the retraction onto
the image of `f` along the fibers `{y, −y}`. The crease is the critical set of `f`; the V's vertex is
where the line crosses it; the V is the square root of the parabola. The normal form supplies the rank
drop and the critical set, not the straight rays: those are the quotient's.

The cusp is the next singularity, and the boundary of the analogy: the V is a fold, not a cusp. A cusp
needs the second derivative to vanish as well, which a line crossing a crease does not do.

### Apparent contours

For a surface `S ⊂ ℝ³` and a projection `π` along a view direction, the **contour generator** is the set
of points of `S` where the view direction lies in the tangent plane; the **apparent contour** is its image
under `π`. At a generic contour point the restriction `π|_S` is a fold, so the apparent contour is the
image of the fold's critical set. This is the theorem behind "the silhouette is the image of a crease."

The sphere is the exact check. View along `z`, so `π(x,y,z) = (x,y)`. Near the equator `z = 0`, write the
sphere as `y = ±√(1 − u² − z²)` with `u = x`. Then

```
∂y/∂z = −z/y,   ∂²y/∂z²|₀ = −1/y₀
```

so the derivative vanishes on the equator and the second derivative does not: `π|_S` is a fold, the
contour generator is the equator, and the apparent contour is the unit circle. The two signs are the two
sides; the fold identifies them. Koenderink and van Doorn made this the basis of shape-from-contour;
Bruce and Giblin's *Curves and Singularities* is the standard reference.

The folded line from afar is the one-dimensional analogue: the "singular line" is the apparent contour of
the pleated line under `π_H`, and the crease is its contour generator.

### Reflection groups: the pleats as a quotient

The creases of the pleated line are mirrors. The reflections

```
r_k(x) = 2kℓ − x
```

generate the infinite dihedral group; the creases `x = kℓ` are their fixed sets; the orbit of `x` is
`{2kℓ ± x}`; a fundamental domain is `[0, ℓ]`. The triangle wave is exactly the quotient coordinate

```
tri(x) = a(2d/ℓ − 1),   d = dist(x, 2ℓℤ)
```

so the pleated line factors through the quotient, and the crease pattern is the mirror arrangement. In `n`
dimensions a set of creases through a point generates a reflection group; the creases are the mirrors, the
connected components of the complement are the chambers, and the quotient is a chamber. A finite
reflection group's quotient is a cone; an affine reflection group's quotient is an alcove, and the pleated
line is the affine `A₁` alcove, an interval. Humphreys is the standard reference.

The boundary: the apex note's pencil is *all* creases through `P₀`, i.e. all of `ℝPⁿ⁻¹`; a reflection
arrangement is a chosen finite or affine subset of them. The quotient statement is exact for the chosen
arrangement, not for the full pencil. The one-mirror case is the Fold's `σ_H`: `ℝⁿ/ℤ₂ ≅ ℝⁿ₊`, the
quotient map is `F`, and the crease is the branch locus.

### Geometric measure theory: the shadow is 1-Lipschitz

The projection `π_H` is orthogonal, hence 1-Lipschitz:

```
|π_H(x) − π_H(y)| ≤ |x − y|
```

so for every `H¹`-measurable set `E`, `H¹(π_H E) ≤ H¹(E)`. For the V, `H¹(V) = 2L√(1+m²)` and
`H¹(π_H V) = 2L`, with equality only at `m = 0` (the line is the crease). The shadow is shorter, never
longer; the difference is the quadratic excess.

The Besicovitch–Federer projection theorem is the global statement: a purely unrectifiable set has
zero-length projections in almost every direction, while a rectifiable set has positive-length
projections in almost every direction. The folded line is rectifiable, so its shadow cannot be erased in
almost every direction. "From afar" chooses the direction; the shadow's length is the projection of the
fold's length. Mattila is the standard reference. This is measure theory, not a fold theorem: a fractal
fold would have vanishing shadows in almost every direction.

### The law of total variance

If the pleat's phase is unresolved, model it as random: `X` is the shadow coordinate and `Φ` is uniform
on `[0, 2ℓ)`, so `Y = a·tri((X+Φ)/ℓ)`. Then `E[Y|X] = 0` and `Var(Y|X) = a²/3`, and the law of total
variance

```
Var(Y) = E[Var(Y|X)] + Var(E[Y|X])
```

gives `Var(Y) = a²/3`. The shadow is the conditional mean; the fold is the conditional variance; the
first moment is the crease, the second is the fold. For a deterministic pleat the conditional variance is
zero — the height is a function of the shadow — so the probabilistic reading requires the unresolved
phase. The identity is exact; the randomness is the model of the observer's ignorance.

### Catastrophe optics: the `2/3` law

The fold diffraction integral is

```
I(k,u) = ∫ exp(ik(t³/3 + ut)) dt = 2π k^{−1/3} Ai(k^{2/3}u)
```

so the intensity is `|I|² ∝ k^{−2/3}|Ai(k^{2/3}u)|²`. The Airy zeros `a_n` give the fringe positions
`u_n = a_n k^{−2/3}`: the fringe spacing in the scaled transverse variable scales as `k^{−2/3}`, i.e. as
`λ^{2/3}` once the cubic coefficient is fixed. The geometric caustic is the `k → ∞` limit; the
resolution threshold scales as `λ^{2/3}`. Berry and Upstill's "Catastrophe optics" is the standard
reference.

This is the sharpest rhyme in the note, and still a rhyme: in diffraction the transverse variable is an
optical path, `k = 2π/λ` is the wave number, and `λ^{2/3}` is a physical resolution. The Fold's height is
geometric; the `2/3` says how a wave of a given scale resolves a fold, not that the Fold's height is a
wavelength. The check below is the exact scaling of the Airy zeros, not an optical measurement.

### Resolution criteria: the doublet

Two equal Gaussian profiles of width `σ` separated by `Δ` have

```
f(x) = exp(−(x−Δ/2)²/(2σ²)) + exp(−(x+Δ/2)²/(2σ²))
```

and at the midpoint `f''(0) = (2/σ²) e^{−Δ²/(8σ²)} (Δ²/(4σ²) − 1)`. The dip closes exactly at `Δ = 2σ`
(the Sparrow criterion); for `Δ > 2σ` there are two peaks, for `Δ < 2σ` one. The Rayleigh criterion is
profile-dependent: in angle, `Δθ = λ/D` for a slit and `1.22λ/D` for a circular aperture; in wavelength
the analogous scale is `Δλ = λ/R`, and Robertson argues that neither is the right scale for Gaussian or
Lorentzian lines. The unresolved doublet is the mean; the singlet is a resolution artifact, not a line.
This is the rhyme of the note's last section, and the boundary is that a spectral line is a frequency
profile, not a geometric crease.

### Origami: pattern, state, and a rhyme

A crease pattern is a planar graph with a mountain/valley label; a flat folding maps it to the plane,
isometric on the facets and folding along the creases; rigid foldability asks whether the facets move as
rigid plates. Akitaya, Demaine, Horiyama, Hull, Ku, and Tachi prove that deciding rigid foldability is
weakly NP-hard with all creases (from Partition) and strongly NP-hard with optional creases (from 1-in-3
SAT). Their abstract also notes the asymmetry: folding from a flat sheet is harder than unfolding a
folded state, because the difficulty is the combinatorial behavior at each vertex, not layer ordering.

The rhyme with the complexity note is exact at the level of shape: the crease pattern is the input, the
folded state is the witness, and the isometric map is the verifier; folding is the quotient
(many-to-one), unfolding is a section (a choice). It is a rhyme, not a reduction: rigid foldability is a
different combinatorial model, and its NP-hardness gives no lower bound for the Fold or for any open
problem.

### Γ-convergence: the coarse-grained length

Fix the slope `s` and let the half-period `ℓ → 0` with amplitude `a = sℓ/2`. The pleated graph
`y_ℓ(x) = (sℓ/2)·tri(x/ℓ)` has `|y_ℓ'| = s`, so its length density is

```
√(1 + s²)
```

for every `ℓ`, and the excess over the straight line is `√(1 + s²) − 1 ≈ s²/2`. The homogenized density
is the constant `√(1+s²)`; Γ-convergence is the theory that makes this a limit of variational problems:
the oscillating functionals converge to the functional with that constant density, whose minimizer is the
straight line. It makes "the shadow is the limit" a statement about energies rather than images.
Braides's handbook is the standard reference.

The boundary: the blur is an image-space limit; Γ-convergence is an energy-space limit. They give the
same density but they are different theorems. The note uses "coarse-graining" for the blur and
"homogenization" for the Γ-limit; they should not be identified.

### What transfers, and what does not

| element | exact in the literature | not claimed |
|---|---|---|
| the V and the crease | Whitney fold normal form; critical set and image | `σ_H` is a global involution, not a map-germ |
| the shadow | apparent contour; 1-Lipschitz projection | it is not a physical shadow or a perception theorem |
| many folds | quotient by a reflection group; chambers | not every pencil of creases is a finite arrangement |
| mean and variance | law of total variance under a random phase | a deterministic pleat is not random |
| the `2/3` law | Airy diffraction catastrophe | the Fold's height is not a wavelength |
| the doublet | Rayleigh/Sparrow resolution criteria | not a spectral theorem |
| the crease pattern | rigid foldability is NP-hard | no P vs NP or lower-bound claim |
| the coarse-grained length | Γ-convergence and homogenization | not the same limit as the blur |

### References

| topic | reference | link |
|---|---|---|
| fold and cusp | Whitney, *On singularities of mappings of Euclidean spaces I*, Ann. of Math. 62 (1955), 374–410 | [overview](https://singsurf.org/parade/stable.php) |
| curves and singularities | Bruce and Giblin, *Curves and Singularities*, 2nd ed., CUP 1992 | [frontmatter](https://assets.cambridge.org/97805214/19857/frontmatter/9780521419857_frontmatter.pdf) |
| apparent contours | Koenderink and van Doorn, *The shape of smooth objects and the way contours end*, Perception 11 (1982), 129–137 | [DOI](https://doi.org/10.1068/p110129) |
| reflection groups | Humphreys, *Reflection Groups and Coxeter Groups*, CUP 1990 | [PDF](https://sites.math.washington.edu/~billey/classes/reflection.groups/references/Humphreys.ReflectionGroupsAndCoxeterGroups.pdf) |
| projections | Mattila, *Geometry of Sets and Measures in Euclidean Spaces*, CUP 1995 | [thesis](https://www.math.unipd.it/~monti/tesi/DallAlba.pdf) |
| total variance | *Law of total variance* | [Wikipedia](https://en.wikipedia.org/wiki/Law_of_total_variance) |
| catastrophe optics | Berry and Upstill, *Catastrophe optics*, Progress in Optics 18 (1980), 257–346 | [PDF](https://michaelberryphysics.wordpress.com/wp-content/uploads/2022/02/berry089-1.pdf) |
| spectral resolution | Robertson, *Quantifying resolving power in astronomical spectra*, PASA 30 (2013), e048 | [arXiv](https://arxiv.org/abs/1308.0871) |
| Rayleigh criterion | *The Rayleigh Criterion* | [HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/Raylei.html) |
| rigid foldability | Akitaya, Demaine, Horiyama, Hull, Ku, Tachi, *Rigid foldability is NP-hard*, J. Comput. Geom. 11 (2020), 93–124 | [arXiv](https://arxiv.org/abs/1812.01160) |
| geometric folding | Demaine and O'Rourke, *Geometric Folding Algorithms*, CUP 2007 | — |
| Γ-convergence | Braides, *Γ-convergence for Beginners*, OUP 2002; *A handbook of Γ-convergence* | [handbook](https://cvgmt.sns.it/media/doc/paper/57/Handbook.pdf) |

## Checks

| check | value |
|---|---|
| V opening angle, `m = 0.1` | `11.421186°` |
| V path/chord, `m = 0.1` | `1.00498756` |
| V ratio excess vs `m²/2`, `m = 0.1` | `0.00498756` vs `0.005`, rel `−2.5e−3` |
| V length excess vs `L m²`, `m = 0.1, L = 1` | `0.00997512` vs `0.01` |
| V height/shadow, `m = 0.1` | `0.05` |
| projection residual, V → crease | `0` |
| global reflection image residual | `0` (a line, no corner) |
| sheet-fold corner residual | `≤ 3.3e−13` |
| triangle-wave length ratio, `a = 0.1` | `1.0198039` vs `1 + 2a² = 1.02` |
| triangle-wave variance | `0.333337 a²` vs `a²/3` |
| blur residual, `w = 1` | `5.8295e−3` |
| first-mode formula | `8/π² e^{−π²/2} = 5.8295e−3` |
| blur log-slope, `w = 0.5 → 1` | `−4.9348` vs `−π²/2` |
| length density, `w = 0.05 / 0.5 / 1 / 2` | `2.112 / 1.126 / 1.00008 / 1.000000` |
| derivative jump across the crease | `2` |
| fold-catastrophe rank, `y = 0` / `y ≠ 0` | `1` / `2` |
| scale invariance, `k = 0.01 … 1000` | angle `22.619865°`, path/chord `1.019804` |
| first / second moment, `a = 1` | `0` / `0.333335` vs `1/3` |
| Whitney fold rank, `y = 0` / `y ≠ 0` | `1` / `2` |
| Whitney fold fibers, `y ≠ 0` | `y` and `−y` both map to `y²` |
| sphere apparent contour, `u = 0 / 0.3 / 0.6` | `∂²y/∂z² = −1 / −1.048285 / −1.25` |
| dihedral invariance residual | `≤ 1.8e−15` |
| crease fixed by `r_k` | `0` |
| quotient formula `tri(x) = a(2d/ℓ − 1)` | `0` |
| projection Lipschitz, 200k pairs | worst `−4.8e−13` (`≤ 0`) |
| random-phase `Var(Y)` vs `a²/3` | `0.333657` vs `0.333333` |
| random-phase decomposition | `0.333574 + 7.4e−5 = 0.333648` |
| Airy zero scaling, `k = 1 / 8 / 64` | `u₁ k^{2/3} = −2.3381074105` |
| Gaussian doublet, `Δ = 2σ` | `f''(0) = 0`; two peaks for `Δ > 2σ` |
| homogenized density, `s = 0.4` | `1.07703296` for `ℓ = 1 … 0.125`; excess `0.07703296` vs `s²/2 = 0.08` |

The first block is the V; the second is the pleats; the third is the singular set and the scale check;
the fourth is the adjacent research. The numbers are floating-point confirmations of the formulas, not
new measurements.

## What this does and does not say

- It **does** give the exact one-fold picture: the sheet fold is the quotient, the V's vertex is on the
  crease, the opening angle is `2 arctan |m|`, and the shadow is the crease.
- It **does** give the exact many-fold picture: the pleats' mean is the crease, the variance is the fold,
  and the length excess is quadratic in the amplitude.
- It **does** distinguish three senses of "singular" — one line (quotient), non-smooth (derivative jump),
  rank-deficient (projection) — and locate all three at the crease.
- It **does** identify the smooth model: the fold catastrophe `(x, y) ↦ (x, y²)`, whose critical line is
  the crease.
- It **does** correct "from afar = scaled to zero": the scale is shape-invariant; the projection and the
  coarse-graining drop the transverse height.
- It **does** place the fold's height in the second moment: the shadow sees the first, the length sees the
  second.
- It **does** place the V in the Whitney fold normal form, the shadow in the apparent-contour theorem, the
  pleats in the infinite dihedral quotient, and the length excess in the 1-Lipschitz and
  Besicovitch–Federer framework.
- It **does** give the exact probabilistic identity behind the moment reading and the exact variational
  limit behind the coarse-graining.
- It **does not** claim that a real physical fold, material, or perceived line behaves exactly this way;
  it is a model of the Fold's geometry.
- It **does not** prove a new theorem in singularity theory; Whitney's normal form and the
  apparent-contour theorem are used, not extended.
- It **does not** identify the crease with a zeta zero, a horizon, or a facet; those are different
  registers.
- It **does not** make the global reflection `σ_H` a fold of a sheet; `σ_H` maps a line to a line, the
  quotient `F` makes the V.
- It **does not** import the physical content of the adjacent fields: the `2/3` Airy law is a rhyme, the
  doublet is a rhyme, rigid foldability is a different combinatorial model, and Γ-convergence is a
  different limit from the blur.

## The one sentence

**A folded line looks like a singular line from afar because the fold's transverse height is dropped by
the projection, leaving the crease — the fixed set of the fold, the boundary of the quotient, and the
singular set of the sheet fold — while the fold survives only in the length, at second order in the
height.**

## Files

`the-fold-afar.md` (this note). The projection and the side-blindness are in `the-fold-occlusion.md`; the
transverse height and the crease are in `the-fold-crease-height.md`; the two sides as one fold and the
pencil are in `the-fold-apex.md`; the equalizer/coequalizer reading is in `the-fold-categorical.md`; the
length and angle invariants are in `the-fold-invariants.md`; the height law and the observer are in
`the-fold-matter.md`; the lookup is `the-fold-key.md`. The complexity rhyme is in
`the-fold-complexity.md`; the references are collected in the `## Adjacent research` section above.
The engineering transfer — the V and pleat length penalties, rigid foldability, and the limits of the
crease kinematics — is in `the-fold-engineering.md`.
