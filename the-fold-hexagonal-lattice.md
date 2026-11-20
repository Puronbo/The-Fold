# UF-004 — The Hexagonal Lattice and Its Two Crease Characters

**Research question.** Derive the allowed crease catalogue from the hexagonal honeycomb itself, rather than choosing an abstract subset of dihedral reflection axes.

**Main result.** The height field \(h(z)=\operatorname{Re}(z^6)\) determines six zero-lines at \(15^\circ+30^\circ j\). These are exactly the six reflection axes of an appropriately oriented hexagon. Their reflections generate the full unlabelled honeycomb point group \(D_6\). Alternating the two honeycomb sublattices splits these six creases into two parity classes: three preserve the \(A/B\) label and three exchange it. The two parity classes each generate a different index-two \(D_3\) subgroup.

## 1. Start with the crease height, not an arbitrary axis origin

The repository's crease-network model chooses

\[
h(z)=\operatorname{Re}(z^6)=r^6\cos(6\theta),\qquad z=re^{i\theta}.
\]

Its zero set is

\[
\cos(6\theta)=0
\quad\Longleftrightarrow\quad
\boxed{\theta_j=\frac{\pi}{12}+j\frac{\pi}{6},\quad j=0,\ldots,5.}
\]

Thus the six unoriented crease lines lie at

\[
15^\circ,\;45^\circ,\;75^\circ,\;105^\circ,\;135^\circ,\;165^\circ.
\]

The half-step offset \(\pi/12\) matters. A generic dihedral group may be written with any base reflection axis, but the physical zero-lines of this particular height are not at \(0^\circ,30^\circ,\ldots\). This corrects the axis-origin convention in the earlier generic generator note; its gcd subgroup formula is unchanged.

Reflection in crease \(j\) is

\[
\boxed{\sigma_j(z)=e^{2i\theta_j}\overline z
=e^{i(2j+1)\pi/6}\overline z.}
\]

It is an involution and it reverses the signed height:

\[
\boxed{\sigma_j^2=I,\qquad h(\sigma_j z)=-h(z).}
\]

This is precisely a Fold: the fixed line is the crease and the two signs of \(h\) are the two sides.

## 2. The crease reflections generate \(D_6\)

Let

\[
r(z)=e^{i\pi/3}z,\qquad s(z)=e^{i\pi/6}\overline z.
\]

Here \(r\) is a \(60^\circ\) rotation and \(s=\sigma_0\) is reflection in the \(15^\circ\) crease. Then

\[
\sigma_j=r^j s,
\qquad r^6=s^2=1,
\qquad srs=r^{-1}.
\]

Composing any two creases gives

\[
\boxed{\sigma_b\sigma_a=r^{b-a}.}
\]

Adjacent crease axes differ by \(30^\circ\); their product is a \(60^\circ\) rotation. All six crease reflections generate the dihedral point group \(D_6\) of order 12.

The signed height distinguishes the two kinds of group elements:

\[
h(r^k z)=h(z),\qquad h(r^k s z)=-h(z).
\]

That is the determinant character of \(D_6\): rotations preserve the signed height, reflections reverse it.

### A subtle extra symmetry that is not a lattice symmetry

A \(30^\circ\) rotation sends \(h\) to \(-h\) and permutes the six zero-lines. It is therefore a symmetry of the **unlabelled crease arrangement**. But it is a rotation of order 12, so it cannot preserve a two-dimensional periodic lattice. The honeycomb point group contains \(60^\circ\) rotations, not \(30^\circ\) rotations. This is a useful warning: the zero-set arrangement can have more symmetry than the lattice that hosts it.

The crystallographic restriction allows nontrivial planar lattice rotation orders 2, 3, 4 and 6; order 12 is excluded. The hexagonal lattice is the case that realizes order 6. [The crystallographic restriction is stated in the International Tables for Crystallography.](https://onlinelibrary.wiley.com/iucr/itc/Ac/ch3o2v0001/sec3o2o1/)

## 3. The honeycomb's two-site basis determines the crease parity

The honeycomb is not itself a Bravais lattice: it is a triangular Bravais lattice with a two-site basis \(A,B\). This standard description is explicit in solid-state physics treatments of graphene. [University of Pisa solid-state physics notes](https://cmp.df.unipi.it/roddaro/SSPnotes/ch01-bravais.html) [Graphene tight-binding notes](https://cmp.df.unipi.it/roddaro/SSPnotes/ch04-tight-binding.html).

Choose the hexagon orientation so its vertices are at

\[
\vartheta_n=15^\circ+60^\circ n,\qquad n=0,\ldots,5,
\]

and alternate the sublattice labels around the six vertices: even \(n\) are \(A\), odd \(n\) are \(B\). The reflection axis \(\theta_j=15^\circ+30^\circ j\) acts on vertex indices by

\[
\boxed{n\longmapsto j-n\pmod 6.}
\]

Therefore:

- if \(j\) is even, vertex parity is preserved and the reflection preserves the \(A/B\) sublattice label;
- if \(j\) is odd, vertex parity changes and the reflection exchanges \(A\) and \(B\).

The six crease axes split into two geometrically distinguished catalogues:

\[
\boxed{A_{\mathrm{pres}}=\{0,2,4\},\qquad
A_{\mathrm{swap}}=\{1,3,5\}.}
\]

The unlabelled honeycomb allows all six. If the two sublattices are distinguished by a decoration or different site energies, only the sublattice-preserving class remains a symmetry. This is consistent with the standard observation that making the two basis sites inequivalent reduces the honeycomb point symmetry from \(D_6\) to \(D_3\). [See the discussion of the honeycomb point group and its two-site basis.](https://www.fisica.unina.it/documents/12375590/13725484/2955_RennellaR.pdf/dc6a141c-c0bf-4b47-93b9-443bd93e07f7)

## 4. The two sign characters are independent

Write an element of \(D_6\) as \(r^k s^\epsilon\), with \(k\in\mathbb Z/6\mathbb Z\) and \(\epsilon\in\{0,1\}\). There are two independent homomorphisms to \(\{+1,-1\}\):

\[
\boxed{\chi_{\mathrm{det}}(r^k s^\epsilon)=(-1)^\epsilon,\qquad
\chi_{AB}(r^k s^\epsilon)=(-1)^k.}
\]

The first is the orientation/determinant sign; the second records whether the operation exchanges the two sublattices. Their product is a third character:

\[
\chi_{\mathrm{mix}}=\chi_{\mathrm{det}}\chi_{AB}=(-1)^{k+\epsilon}.
\]

Since \(6\) is even, both signs are well-defined, and

\[
\operatorname{Hom}(D_6,\mathbb Z/2)\cong(\mathbb Z/2)^2.
\]

The three nontrivial index-two kernels are:

| Character | Kernel | Geometric meaning |
|---|---|---|
| \(\chi_{\mathrm{det}}\) | \(\langle r\rangle\cong C_6\) | rotations only; preserves orientation |
| \(\chi_{AB}\) | \(\langle r^2,s\rangle\cong D_3\) | preserves the \(A/B\) labels |
| \(\chi_{\mathrm{mix}}\) | \(\langle r^2,rs\rangle\cong D_3\) | preserves the product of orientation and sublattice signs |

On the six actual crease reflections, the character values are:

| Crease parity | \(\chi_{\mathrm{det}}\) | \(\chi_{AB}\) | \(\chi_{\mathrm{mix}}\) |
|---|---:|---:|---:|
| even \(j\) | \(-1\) | \(+1\) | \(-1\) |
| odd \(j\) | \(-1\) | \(-1\) | \(+1\) |

Thus every crease reflection reverses the signed height. Even creases preserve the sublattice; odd creases exchange it. The determinant sign and sublattice sign are not the same bit.

## 5. The natural crease catalogues and their minimum generators

| Allowed crease catalogue | Generated subgroup | Order | Minimum crease generators |
|---|---|---:|---:|
| all six \(\{0,1,2,3,4,5\}\) | \(D_6\) | 12 | 2 adjacent axes, e.g. \(\{0,1\}\) |
| sublattice-preserving \(\{0,2,4\}\) | \(\ker\chi_{AB}=D_3\) | 6 | 2 axes, e.g. \(\{0,2\}\) |
| sublattice-exchanging \(\{1,3,5\}\) | \(\ker\chi_{\mathrm{mix}}=D_3\) | 6 | 2 axes, e.g. \(\{1,3\}\) |

A single reflection generates only a group of order two. Two even creases differ by \(60^\circ\), and their product is a \(120^\circ\) rotation; they generate the sublattice-preserving \(D_3\). Two adjacent creases from opposite parity classes differ by \(30^\circ\); their product is a \(60^\circ\) rotation and they generate the full \(D_6\).

This answers the lattice-derived catalogue question:

- if the Fold acts on the **unlabelled honeycomb geometry**, all six crease lines are allowed;
- if the operation must preserve each **labelled sublattice**, only the three even axes are allowed, and the generated group is \(D_3\);
- the odd axes form the other \(D_3\) index-two subgroup, but each odd reflection exchanges \(A\) and \(B\).

## 6. Keep the geometric and arithmetic actions separate

The geometric rotation acts on points by \(z\mapsto e^{i\pi/3}z\). The arithmetic UFSF map acts on a modular unit/Frobenius element by \(a\mapsto a^r\). A geometric rotation shifts the angle of a point; arithmetic powering changes an automorphism in a cyclic group. Their common order formula does not identify the actions.

UF-002 remains an arithmetic spectral-power problem. UF-003 gives the general geometric dihedral generator theorem. UF-004 supplies the actual hexagonal crease catalogue from the height and the two-site honeycomb basis.

## 7. Verification

The companion standard-library program **tools/fold_hexagonal_lattice.py** checks:

- all 144 products in \(D_6\);
- all three characters as group homomorphisms (432 checks);
- 182 checks of the six height-zero lines, reflection involutions, height signs, and 30°/60° rotation actions;
- all 64 crease subsets against the gcd subgroup-order formula;
- 41 checks: 36 vertex-colour cases plus 5 character-kernel/catalogue/minimality assertions.

The checks establish the finite algebra implemented by the script. The symbolic derivations above establish the general statements.

## 8. Conclusion and next problem

UF-004 derives the crease catalogue from the actual hexagonal height and honeycomb basis, rather than selecting axes abstractly. The six creases generate \(D_6\); their parity split records the independent sublattice sign; and the sublattice-preserving operations form \(D_3\).

The next question is to extend this construction from a single hexagonal cell to an arbitrary periodic crease network: characterize which zero-line arrangements are compatible with a lattice point group, which sign characters survive decorations, and how the local crease generators assemble into a global wallpaper-group action.
