# UF-013 — Equivariant Resolution, Exceptional Curves, and Fold Characters

**Research question.** When a finite symmetry group acts on a singular Fold surface, how does it lift to the resolution, what representation does it induce on the exceptional intersection lattice, and which analytic height characters can descend to the original singularity?

**Main result.** A symmetry of a normal surface germ lifts to its unique minimal resolution (or, more generally, to a suitable equivariant good resolution). It permutes exceptional components and acts by an integral isometry of the exceptional intersection lattice, hence on its discriminant group. But this lattice representation is only part of the story: the action on the exceptional curves themselves, their marked intersection points, and their Picard data can be nontrivial even when the lattice permutation is trivial. The cone from UF-011 gives an explicit example: a natural order-eight dihedral symmetry group fixes the unique exceptional component, while a principal height `h=xy` transforms by a nontrivial one-dimensional character.

## 1. Lifting finite symmetries to a resolution

Let `(X,p)` be a normal complex analytic surface germ and let a finite group `G` act by analytic automorphisms fixing p. The minimal resolution of a normal surface singularity is unique up to unique isomorphism over X. Therefore each germ automorphism induces an automorphism of the minimal resolution, and composition is respected. In situations where a chosen minimal resolution is not a good/SNC resolution for the entire action, one may pass to a common equivariant good resolution; a finite group action can be made equivariant by resolving invariant ideals/centres.

Write the exceptional divisor as

\[
E=\bigcup_{i=1}^r E_i.
\]

The group permutes its irreducible components. If `P_g` is the corresponding integral permutation matrix on the free lattice

\[
L=\bigoplus_i\mathbb Z[E_i],
\]

then the intersection form `M=(E_i\cdot E_j)` is preserved:

\[
\boxed{P_g^T M P_g=M.}
\]

Thus `G` acts on the discriminant group `A_L=L^*/L`, equivalently on the appropriate cokernel of M. This is the **exceptional-lattice representation**.

### Theorem 1 — Equivariant exceptional-lattice action

Every lifted automorphism acts on the exceptional component lattice by an integral isometry of its intersection form. It therefore induces an automorphism of the numerical discriminant group. The action on the graph must preserve all vertex weights (self-intersection and genus) and edge intersection multiplicities.

The lattice action does not in general determine the action on the exceptional curves as Riemann surfaces, on their marked points, or on their degree-zero Picard varieties.

## 2. The cone singularity has a natural D4 action

Return to

\[
X=\{(x,y,z)\in\mathbb C^3:z^2=x^4+y^4\}.
\]

Define

\[
r(x,y,z)=(-y,x,z),\qquad s(x,y,z)=(y,x,z).
\]

These preserve X and satisfy

\[
r^4=s^2=1,\qquad srs=r^{-1}.
\]

They generate the order-eight dihedral group `D4` (using the convention that `D4` has order eight). The group acts by signed permutations of x and y while fixing z.

This is the appropriate finite symmetry group for this quartic cone. It should not be confused with the hexagonal `D6` action used in the separate triangular-lattice model.

## 3. The elliptic exceptional curve and its D4 action

The simple-elliptic singularity of type `\widetilde E_7=\widetilde T_{2,4,4}` has a single genus-one exceptional curve E with

\[
E^2=-2.
\]

In the weighted projective description of the exceptional curve, set

\[
t=x/y,\qquad w=z/y^2.
\]

Then

\[
\boxed{E:\ w^2=t^4+1.}
\]

The lifted generators act by

\[
r_E(t,w)=\left(-\frac1t,\frac{w}{t^2}\right),\qquad
s_E(t,w)=\left(\frac1t,\frac{w}{t^2}\right).
\]

Direct substitution verifies that both preserve the equation. On E, `r_E^2=s_E^2=1` and the two involutions commute; the action on E factors through `D4/<r^2>\cong V_4`. In particular, the central element `r^2` acts trivially on E: in weighted projective coordinates it sends `(x,y,z)` to `(-x,-y,z)`, which is the same point under weight-one/weight-two scaling.

For the holomorphic differential

\[
\omega=dt/w,
\]

we obtain

\[
\boxed{r_E^*\omega=+\omega,\qquad s_E^*\omega=-\omega.}
\]

The first involution is nontrivial but preserves the differential, hence is translation by a nonzero 2-torsion point after choosing an origin. The second is an involution with linear part -1 (an inversion composed with a translation). This is consistent with the general description of automorphism groups of simple-elliptic singularities in terms of torsion translations and automorphisms of the central elliptic curve.

Crucially, the exceptional **component** is unique. Every element fixes `[E]`, so on the rank-one lattice

\[
L=\mathbb Z[E],\qquad M=[-2],
\]

we have

\[
\boxed{P_g=[1]\quad\text{for all }g\in D_4.}
\]

The induced action on `coker(M)\cong\mathbb Z/2` is therefore trivial, even though the action on E and its points is nontrivial. The rank-one intersection lattice forgets this elliptic-curve automorphism data.

## 4. Four marked crease points on E

The principal divisor `xy=0` on X has four irreducible branches:

\[
C_{x,+}:x=0,\ z=y^2,\quad C_{x,-}:x=0,\ z=-y^2,
\]

\[
C_{y,+}:y=0,\ z=x^2,\quad C_{y,-}:y=0,\ z=-x^2.
\]

On E these strict transforms meet at the four distinct points

- `t=0, w=+1` and `t=0, w=-1`;
- `t=\infty` with the two corresponding values of `z/x^2`, namely `+1` and `-1`.

Each intersection is transverse. Therefore the intersection vector for the full strict-transform divisor D is

\[
b(D)=\widetilde D\cdot E=4.
\]

Since `M=[-2]`, the exceptional correction equation is

\[
-2a=-4,\qquad \boxed{a=2\in\mathbb Z}.
\]

This agrees with the explicit function: in a weighted chart `x=uv, y=u, z=u^2w`, one has `xy=u^2v`. Thus its total transform contains exceptional multiplicity two and the strict-transform branches meet E in the four marked points described above.

## 5. A principal Fold height carrying a nontrivial D4 character

Take

\[
\boxed{h(x,y,z)=xy.}
\]

Its zero divisor is exactly the four-branch divisor D above, with multiplicity one on each branch. It is globally principal by construction. Under the two generators,

\[
\boxed{h(r(x,y,z))=-h(x,y,z),\qquad h(s(x,y,z))=+h(x,y,z).}
\]

Thus its character is

\[
\chi(r)=-1,\qquad\chi(s)=+1.
\]

The relations of D4 are respected, so this is a genuine one-dimensional representation. The divisor itself is invariant, while its generator is semi-invariant.

This is the central UF-013 example:

- the exceptional lattice action is trivial (`P_g=1`);
- the exceptional elliptic curve action is nontrivial;
- the divisor is invariant and principal;
- its analytic generator carries a nontrivial symmetry character.

Therefore the exceptional lattice representation alone cannot classify the possible Fold-height characters.

## 6. The generator-unit cocycle: divisor invariance is not enough

Let a local analytic domain R carry a finite G-action, and let an invariant effective Cartier divisor have principal ideal `(h_0)`. For each g there is a unique unit `u_g\in R^\times` such that

\[
g^*h_0=u_g h_0.
\]

The units satisfy the group cocycle identity (with the pullback convention). A different generator `h=v h_0`, where v is a unit, transforms by

\[
g^*h=\frac{g^*v}{v}u_g\,h.
\]

Consequently, an exact generator with a prescribed character `\chi:G\to\mathbb C^\times` exists precisely when there is a unit v satisfying

\[
\boxed{\frac{g^*v}{v}u_g=\chi(g)\quad\text{for every }g\in G.}
\]

In cohomological language, the unit cocycle must become the desired character after a coboundary adjustment. This is an **equivariant trivialization** condition on the principal divisor, additional to the numerical Cartier test.

For a real separating crease divisor with connected bipartite face dual, UF-009 provides a useful sufficient construction: the face colouring induces a sign character, and a character-weighted finite-group average of an exact real defining function preserves the exact zero set. For general complex divisors or arbitrary prescribed characters, no such same-sign argument is available; the unit-cocycle condition must be checked.

## 7. D4 semi-invariant test functions on the cone

For the chosen generators, the four real one-dimensional characters are specified by the pair `(\chi(r),\chi(s))`. Explicit polynomial representatives are:

| Character `(r,s)` | Semi-invariant | Real zero set on X |
|---|---|---|
| `(+,+)` | `z` | only the cone vertex |
| `(-,+)` | `xy` | four coordinate-axis branches |
| `(-,-)` | `x^2-y^2` | four diagonal branches |
| `(+,-)` | `xy(x^2-y^2)` | the union of coordinate and diagonal branches |

The first is a valid complex-analytic semi-invariant, but its real zero locus on this cone is only the vertex, not a one-dimensional real crease network. The other three provide real curve networks. This illustrates that a representation character and a geometrically useful real crease divisor are separate requirements.

## 8. UF-013 conclusions

1. Finite symmetries lift to a suitable equivariant resolution and act by weighted graph automorphisms.
2. The exceptional intersection lattice and its discriminant group capture only the numerical permutation representation.
3. For simple-elliptic singularities, one must also retain the action on the exceptional elliptic curve, its marked points, and its Picard data.
4. On the UF-011 cone, a natural D4 action fixes the unique exceptional lattice generator but acts nontrivially on E.
5. The exact height `h=xy` realizes a nontrivial D4 sign character even though the lattice action is trivial.
6. For a general invariant principal divisor, possible generator characters are controlled by a unit-valued cocycle; divisor invariance alone does not settle equivariant trivialization.

**Conclusion.** The correct symmetry object for singular Fold geometry is not merely the exceptional intersection lattice. It is the combined package of the weighted exceptional graph, the curve automorphisms and marked points, the discriminant/Picard data, and the character carried by an exact analytic generator.

## Open UF-014 direction

Construct the full equivariant divisor-class sequence for simple-elliptic and rational surface singularities, then determine which characters of the symmetry group can be realized by exact analytic heights with a prescribed odd-multiplicity crease divisor. The concrete D4 cone example should be the first benchmark.

## References

- F. C. C. Ganter and related work on symmetries of surface singularities: automorphism groups of weighted-homogeneous singularities are studied via the induced action on the minimal good resolution and its central curve; for simple elliptic singularities the finite part involves torsion translations and automorphisms of the elliptic curve. *Journal of the London Mathematical Society* 59 (1999), 491–506. [DOI 10.1112/S0024610799007188](https://doi.org/10.1112/S0024610799007188).
- A. R. R. Ruggiero et al., discussion of unique minimal good resolutions and equivariant log resolutions of normal surface singularities; see Proposition 3.1 for a resolution to which all automorphisms lift. [Annales de la Faculté des Sciences de Toulouse PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1425.pdf).
- D. van Straten et al., description of simple elliptic \\widetilde E_7 as type (2,4,4) and its exceptional elliptic curve. [Survey chapter PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/Tree%20Singularities%20229-287%20deformations-of-surface-singularities-2013.pdf).
- E. Looijenga, *Rational Surfaces and Singularities*, for resolution graphs and simple-elliptic configurations. [Lecture notes](https://webspace.science.uu.nl/~looij101/delpezzo.pdf).