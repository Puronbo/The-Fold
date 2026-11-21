# UF-007 — Forced Zeros, Crease Topology, and Minimal D6 Semi-Invariants

**Research question.** Given a group character and a prescribed crease network, what zeros are forced by symmetry, when can a single continuous signed-height function realize that network, and what are the simplest realizations in the hexagonal D6 model?

**Main results.** Three complementary criteria emerge:

1. A point fixed by any sign-reversing symmetry must lie in the zero set.
2. A connected crease network admits a continuous scalar height that is nonzero off the creases and changes sign across every crease exactly when its face-adjacency dual graph is bipartite. The network then determines the height's sign character.
3. For the three nontrivial real characters of D6, the forced reflection axes are realized exactly by harmonic polynomials of minimal possible degrees 6, 3, and 3.

These are statements about a scalar real height. Multi-component order parameters can evade some scalar obstructions and require a representation-valued generalization.

## 1. The fixed-point obstruction

Let a group G act on a space X, let χ:G→{+1,−1} be a character, and let h:X→R satisfy the equivariance law

\[
h(gx)=\chi(g)h(x)\qquad(g\in G,\ x\in X).
\]

### Theorem 1 — Fixed-point forced-zero theorem

For every element g with χ(g)=−1,

\[
\boxed{\operatorname{Fix}(g)\subseteq h^{-1}(0).}
\]

**Proof.** If gx=x, equivariance gives h(x)=h(gx)=χ(g)h(x)=−h(x), hence h(x)=0. ∎

Define the forced-zero locus

\[
F_\chi=\bigcup_{g:\chi(g)=-1}\operatorname{Fix}(g).
\]

Every χ-equivariant scalar height must vanish on Fχ. This is a necessary condition; additional zeros can be forced by topology, boundary conditions, analyticity, or other geometric requirements.

## 2. The D6 character model

Let

\[
r(z)=e^{i\pi/3}z,\qquad s(z)=e^{i\pi/6}\overline z,
\]

so r is a 60° rotation and s is reflection in the 15° axis. Then

\[
D_6=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle.
\]

Every element is r^k s^ε. The four real one-dimensional characters are

| Character | χ(r) | χ(s) | χ(r^k s^ε) |
|---|---:|---:|---|
| Trivial | +1 | +1 | +1 |
| Determinant | +1 | −1 | (−1)^ε |
| Sublattice | −1 | +1 | (−1)^k |
| Mixed | −1 | −1 | (−1)^(k+ε) |

The six crease reflections are σ_j=r^j s, with fixed axes

\[
\phi_j=15^\circ+30^\circ j,\qquad j=0,\ldots,5.
\]

Applying Theorem 1 gives:

| Character | Sign-reversing reflections | Forced reflection axes |
|---|---|---|
| Determinant | all six σ_j | 15°, 45°, 75°, 105°, 135°, 165° |
| Sublattice | σ_1, σ_3, σ_5 | 45°, 105°, 165° |
| Mixed | σ_0, σ_2, σ_4 | 15°, 75°, 135° |

For the sublattice and mixed characters, r itself is sign-reversing and fixes only the origin; the origin is already contained in every listed axis. Thus the forced-zero locus is exactly the union of the listed lines.

## 3. Minimal-degree polynomial realizations

A polynomial f is a χ-semi-invariant when

\[
f(gz)=\chi(g)f(z)\qquad(g\in D_6).
\]

The three nontrivial characters have the following explicit real harmonic representatives:

\[
\boxed{f_{\det}(z)=\operatorname{Re}(z^6)}
\]

\[
\boxed{f_{\mathrm{sub}}(z)=\operatorname{Re}(e^{-i\pi/4}z^3)}
\]

\[
\boxed{f_{\mathrm{mix}}(z)=\operatorname{Re}(e^{i\pi/4}z^3)}.
\]

Direct substitution verifies their characters:

| Polynomial | r action | s action | Zero-line axes | Degree |
|---|---:|---:|---|---:|
| f_det | + | − | all six axes | 6 |
| f_sub | − | + | odd axes 45°, 105°, 165° | 3 |
| f_mix | − | − | even axes 15°, 75°, 135° | 3 |

For instance, s(z)=e^{iπ/6}\bar z, so

\[
(e^{i\pi/6}\bar z)^6=-\bar z^6,
\]

which proves f_det(sz)=−f_det(z). Similarly, since (e^{iπ/6}\bar z)^3=i\bar z^3, the choices of phases e^{∓iπ/4} give the + and − reflection signs for f_sub and f_mix respectively. Multiplication by r gives the rotation signs shown in the table.

### Theorem 2 — Polynomial degree lower bound and sharpness

Among nonzero real polynomials transforming by a fixed nontrivial D6 character, the minimum possible total degree is

\[
\boxed{\deg_{\min}(\chi_{\det})=6,\qquad
\deg_{\min}(\chi_{\mathrm{sub}})=3,\qquad
\deg_{\min}(\chi_{\mathrm{mix}})=3.}
\]

**Proof.** For every sign-reversing reflection, Theorem 1 forces f to vanish on its fixed line. A polynomial that vanishes identically on a line is divisible by that line's defining linear form. Distinct lines give pairwise nonassociate irreducible linear factors, so their product divides f. The determinant character has six distinct forced axes, giving degree at least six. The other two characters each have three forced axes, giving degree at least three. The displayed polynomials have exactly those degrees and transform by the required characters, so the bounds are attained. ∎

The displayed zero sets are exactly the forced axes, not larger sets. Thus these are sharp minimal-degree realizations with no additional real zero curves.

## 4. The global topological obstruction: bipartite dual graphs

Let S be a connected compact surface and let C⊂S be a closed embedded crease graph. The faces are the connected components of S\C. Construct the face-adjacency dual graph D(C):

- one dual vertex for each face;
- one dual edge for each crease arc separating two incident faces;
- retain a loop when both sides of a crease arc border the same face.

A scalar height with zero set exactly C and opposite signs on the two sides of every crease induces a sign ε(F)∈{+1,−1} on each face, satisfying ε(F′)=−ε(F) across every dual edge.

### Theorem 3 — Dual-graph realization criterion

A face-sign assignment that flips across every crease exists if and only if D(C) is bipartite.

If D(C) is connected, the assignment is unique up to simultaneous reversal of every face sign.

**Proof.** Such a sign assignment is exactly a proper two-colouring of the dual graph, so it exists precisely when the dual is bipartite. A connected bipartite graph has exactly two proper two-colourings, obtained from one another by swapping the two colours. ∎

### Continuous realization

When D(C) is bipartite, choose a face sign ε(F). Equip S with any compatible metric and let d(x,C) be the distance to the crease set. Define

\[
h(x)=\begin{cases}
\epsilon(F)\,d(x,C),&x\in F,\\
0,&x\in C.
\end{cases}
\]

Since d(x,C) tends to zero on approach to C, h is continuous. Its zero set is exactly C, and its sign changes across every crease. Thus bipartiteness is also sufficient for existence of a continuous scalar height with the required sign-domain pattern. This construction does not generally produce a smooth or analytic height; smoothness imposes further local compatibility conditions at vertices.

### Symmetry character induced by a connected dual graph

Assume D(C) is connected and a group G acts by isometries preserving C. Each symmetry induces an automorphism of D(C). Because the bipartition is unique up to global swap, every g either preserves both face classes or exchanges them. Define χ_C(g)=+1 in the first case and −1 in the second.

The preserve/swap rule composes multiplicatively, so χ_C:G→{±1} is a character. The signed-distance construction above satisfies

\[
\boxed{h(gx)=\chi_C(g)h(x).}
\]

Conversely, any continuous h with zero set exactly C and opposite signs across every crease has the same face-sign assignment up to a global reversal, so its symmetry character must equal χ_C. Therefore, for a connected bipartite dual, the prescribed crease network determines the sign character; it is not freely selectable from the abstract group character table.

For disconnected dual graphs, each dual component has an independent face-sign choice. A symmetry can permute these components, so the correct object is then an action on the vector of component signs rather than necessarily one scalar character.

## 5. Local examples and obstructions

### The D6 crease stars

A star made from six distinct lines through one point has twelve angular sectors. Its face dual is the cycle C_12, which is bipartite. The face swap character is the determinant character (+ on r, − on s); this is precisely the zero set of f_det.

The three-axis sublattice and mixed crease stars each have six sectors, with dual C_6. Their induced face characters are respectively (χ(r),χ(s))=(−,+) and (−,−), matching f_sub and f_mix. Thus all three nontrivial D6 characters are realized by different minimal crease arrangements.

### A three-way junction obstruction

A Y-shaped three-crease junction has three local sectors. The local dual is C_3, an odd cycle, so it is not bipartite. No continuous real scalar height can have exactly these creases as sign-changing zero arcs: traversing a small loop around the junction would require the sign to flip three times and return to its negative.

### A nonseparating torus crease

A single nonseparating closed crease loop on a torus has the same face on both sides. Its dual graph has one vertex and a loop, hence is not bipartite. It cannot be the exact sign-changing zero set of a globally defined continuous real-valued periodic height. A multi-valued height, a section of a nontrivial line bundle, or a vector-valued order parameter would be a different model and is not ruled out by this scalar theorem.

## 6. What UF-007 adds to the Fold program

1. **Fixed-set constraint:** an anti-symmetry forces its fixed locus into the crease set.
2. **Topology constraint:** a scalar sign-changing crease set must have a bipartite face dual.
3. **Network-determined character:** for a connected bipartite dual, the crease arrangement induces the unique possible sign character.
4. **Minimal algebraic realization:** the three nontrivial D6 characters have sharp minimal polynomial degrees 6, 3, and 3.
5. **Scope boundary:** the continuous signed-distance construction proves existence as a continuous function, not smoothness or analyticity at crease vertices.

The next research problem is to characterize the extra local conditions under which the signed-distance construction can be replaced by a smooth or analytic semi-invariant, and to extend the face-sign obstruction to periodic networks on a torus with multiple dual components and nontrivial line-bundle twists.

## References

- Dmitri Panyushev, *Lectures on representations of finite groups and invariant theory*, Section II.6, “Semi-invariants of finite reflection groups,” for the general notion of anti-/semi-invariant polynomials and reflection-hyperplane factors: [lecture notes PDF](https://eclass.uoa.gr/modules/document/file.php/MATH857/%CE%98%CE%B5%CF%89%CF%81%CE%AF%CE%B1%20%CE%91%CE%BD%CE%B1%CE%BB%CE%BB%CE%BF%CE%B9%CF%8E%CE%BD/Lectures%20on%20representations%20of%20finite%20groups%20and%20invariant%20Dmitri%20I_%20Panyushev.pdf).
- The dual graph is the standard face-adjacency graph of an embedded plane graph; see the [GCol face-colouring and dual-graph documentation](https://gcol.readthedocs.io/en/latest/modules.html#face-coloring).
- For the more general relationship between signed planar graphs and their duals, see the chapter on [signed colouring and dual graphs](https://www.labri.fr/perso/sopena/pmwiki/uploads/CurriculumVitae/phd_Narboni.pdf).

## UF-008 extension: smooth and analytic heights

Under the regular-branch hypotheses, the dual-bipartite condition from UF-007 is also sufficient for a global smooth height, using local products of branch-defining functions and a nonnegative smooth partition of unity. At a vertex with q regular branches, the height has vanishing order at least q. Fourier projection also shows that every real character of a finite periodic point group has some nonzero analytic periodic semi-invariant; exact matching of a prescribed zero network is a stronger open problem. See the-fold-smooth-analytic-heights.md.
