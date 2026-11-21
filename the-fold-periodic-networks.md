# UF-005 — Periodic Crease Networks, Wallpaper Groups, and Surviving Characters

**Research question.** Can the symmetry group of a periodic Fold network be derived from its translation lattice, crease graph, signed height, and site decorations, and can we identify exactly which sign information survives?

**Main answer.** A periodic crease network determines a wallpaper group: its translations form a rank-two lattice and the quotient by translations is a finite crystallographic point group. A signed height or a two-colour decoration that transforms globally by a sign defines a group character. Several independent decorations combine into a character map to \((\mathbb Z/2)^k\), and the subgroup preserving every decoration is its kernel. A finite-torus model makes these constructions exactly computable for finite periodic motifs.

## 1. The geometric object: a graph on a flat torus

Let \(\Lambda\subset\mathbb R^2\) be a rank-two lattice and let

\[
T_\Lambda=\mathbb R^2/\Lambda
\]

be the corresponding flat torus. A periodic crease network is represented by an embedded graph \(C\subset T_\Lambda\): vertices are crease intersections or higher-order zeros; edges are crease arcs between vertices. If it is defined by a nonzero real periodic height field \(h:T_\Lambda\to\mathbb R\), then its zero set is

\[
C=h^{-1}(0),
\]

possibly with additional incidence data recording which zero arcs meet at each vertex.

The zero-set network and its signed height are different objects. A transformation can preserve \(C\) while sending \(h\) to a different function with the same zero set, not necessarily to \(h\) or \(-h\). Thus we define separate groups rather than assuming every crease symmetry has a height sign.

## 2. The wallpaper group of the network

Let \(W_C\) be the group of Euclidean isometries of the plane that preserve the full periodic lift of the embedded network and its incidence structure. Its pure translations form a rank-two lattice

\[
T_C=W_C\cap\operatorname{Trans}(\mathbb R^2).
\]

The quotient

\[
P_C=W_C/T_C
\]

is finite and is the crystallographic point group of the pattern. There is an exact sequence

\[
\boxed{1\longrightarrow T_C\longrightarrow W_C\longrightarrow P_C\longrightarrow1.}
\]

The sequence need not split: glide reflections and other fractional affine lifts mean that one must not assume every wallpaper group is a semidirect product \(T_C\rtimes P_C\). In two dimensions there are 17 wallpaper-group types. The allowed lattice rotation orders are 1, 2, 3, 4, and 6; point groups are cyclic or dihedral subgroups compatible with the lattice. See the Manchester notes on [wallpaper patterns](https://personal.maths.manchester.ac.uk/jm/wiki/uploads/SymmetryInNature/Chapter3-v2.0.pdf) and the [classification of wallpaper groups](https://ir.canterbury.ac.nz/server/api/core/bitstreams/33f24aea-7353-4c8b-9e2e-07cde926b944/content).

For a lattice basis matrix \(B\), write its Gram matrix as \(G=B^TB\). The linear parts, expressed in lattice coordinates, lie in

\[
P_\Lambda=\{A\in GL(2,\mathbb Z):A^TGA=G\}.
\]

This is the lattice point group. The crease network generally has a subgroup of it, possibly with nonzero translational offsets in the affine lifts.

## 3. Network symmetry versus signed-height symmetry

Define

\[
G_C=\{g:g(C)=C\}
\]

for the network's geometric symmetry group. For a nonzero real height field, define its sign-covariant subgroup

\[
G_h=\{g\in G_C:\exists\,\chi_h(g)\in\{\pm1\},\quad h(gx)=\chi_h(g)h(x)\;\forall x\}.
\]

The sign is unique because \(h\) is not identically zero.

### Theorem 1 — Sign-character theorem

\(G_h\) is a subgroup of \(G_C\), and

\[
\boxed{\chi_h:G_h\to\{\pm1\},\qquad \chi_h(g_1g_2)=\chi_h(g_1)\chi_h(g_2)}
\]

is a group homomorphism.

**Proof.** The identity has sign \(+1\). If \(h(g_2x)=\chi_h(g_2)h(x)\) and \(h(g_1x)=\chi_h(g_1)h(x)\), then

\[
h(g_1g_2x)=\chi_h(g_1)h(g_2x)
=\chi_h(g_1)\chi_h(g_2)h(x).
\]

Thus the product is sign-covariant. If \(h(gx)=\chi h(x)\), then substituting \(x=g^{-1}y\) gives \(h(g^{-1}y)=\chi h(y)\), since \(\chi^{-1}=\chi\). Hence inverses are also sign-covariant. Uniqueness of the sign gives the homomorphism law. \(\square\)

The subgroup preserving the signed height is

\[
\boxed{G_h^+=\ker\chi_h.}
\]

If the image contains \(-1\), all sign-reversing symmetries form the other coset of this kernel. If the image is only \(+1\), the height has no sign-reversing symmetry in the chosen group.

A key distinction follows: \(G_C\) can be strictly larger than \(G_h\). Preserving a zero set does not imply preserving a chosen defining function up to a constant sign.

## 4. Decorations and multiple characters

Let \(S\) be a periodic set of decorated sites and let \(c:S\to\{\pm1\}\) encode a two-colour label such as A/B. Define the colour sign-covariant subgroup by

\[
G_c=\{g:g(S)=S,\quad c(gx)=\chi_c(g)c(x)\;\forall x\in S\}.
\]

When \(c\) is nonzero, the sign is unique and the same proof shows that \(\chi_c\) is a character. The joint group is \(G=G_h\cap G_c\), and the two signs combine into

\[
\boxed{\chi=(\chi_h,\chi_c):G\to(\mathbb Z/2)^2.}
\]

For \(k\) independent binary decorations, the same construction gives

\[
\chi:G\to(\mathbb Z/2)^k.
\]

### Theorem 2 — Common symmetry kernel and index

The subgroup preserving every signed decoration is \(K=\ker\chi\). If the image of \(\chi\) has dimension \(r\) as a vector space over \(\mathbb F_2\), then

\[
\boxed{[G:K]=|\operatorname{im}\chi|=2^r.}
\]

**Proof.** The first isomorphism theorem gives \(G/\ker\chi\cong\operatorname{im}\chi\). Every finite subgroup of \((\mathbb Z/2)^k\) is a vector space over \(\mathbb F_2\), so an image of dimension \(r\) has \(2^r\) elements. \(\square\)

The characters need not be independent. If two decorations always flip together, their characters coincide and they contribute only one bit of symmetry reduction. A genuinely new invariant requires a new independent character, not merely another name for the same sign.

For decorations with more than two labels, the correct generalization is a permutation representation of the symmetry group on the label set; a sign character is the special two-label case.

## 5. The finite periodic-motif model

For computation, take a finite torus

\[
T_N=(\mathbb Z/N\mathbb Z)^2
\]

in lattice coordinates. A motif consists of a vertex set, an undirected set of marked crease-crossing bonds, and optional site fields such as signed height and A/B colour. The finite affine candidates are

\[
x\mapsto Ax+b\quad (A\in P_\Lambda,\ b\in T_N).
\]
Here the torus coordinates use a chosen finite grid inside the periodic cell; increasing the grid resolution permits rational offset vectors such as half-cell glide translations.

A candidate belongs to the network group exactly when it preserves the vertex set and marked bonds. It belongs to the sign-covariant height subgroup if it sends the sampled height field to itself or its negative; the colour condition is analogous. The companion program tools/fold_periodic_networks.py implements this exact finite enumeration.

This model can encode rational affine offsets and glide-like actions when the torus grid is sufficiently subdivided. It is a finite reference model, not a complete classifier of all 17 wallpaper groups. For a continuous pattern, one must still prove that a sampled candidate extends to an isometry preserving the full embedded network between sample points.

## 6. Three lattice tests

The program computes lattice point groups directly from the Gram matrix. Its finite coefficient search bound follows from the smallest eigenvalue of the positive-definite Gram matrix; candidate matrices are then checked exactly by (A^TGA=G) and (|\det A|=1).

| Lattice metric in a chosen basis | Gram matrix | Point-group order |
|---|---|---:|
| Square | \(\begin{pmatrix}1&0\\0&1\end{pmatrix}\) | 8 (\(D_4\)) |
| Triangular | \(\begin{pmatrix}2&1\\1&2\end{pmatrix}\) | 12 (\(D_6\)) |
| Generic oblique example | \(\begin{pmatrix}4&1\\1&7\end{pmatrix}\) | 2 (\(C_2\)) |

The honeycomb is not itself a Bravais lattice: it is a triangular Bravais lattice with a two-site A/B basis. This distinction is important when adding sublattice decorations; see the [graphene lattice and two-site basis notes](https://cmp.df.unipi.it/roddaro/SSPnotes/ch04-tight-binding.html).

### Worked periodic example: independent height and colour signs

On the square torus with \(N=4\), take all 16 vertices and define

\[
h(x,y)=(-1)^x,\qquad c(x,y)=(-1)^y.
\]

Mark each nearest-neighbour bond across which \(h\) changes sign; these bonds encode the periodic crease-crossing pattern. The exact affine enumeration gives:

| Quantity | Count |
|---|---:|
| Square lattice point group | 8 |
| Affine network symmetries on the 4-by-4 torus | 64 |
| Joint height-and-colour sign-covariant subgroup | 64 |
| Image of \((\chi_h,\chi_c)\) | 4 elements, all of \(\mathbb Z_2^2\) |
| Common sign-preserving kernel | 16 |

Both signs are independent: translations by one grid step in the x and y directions flip different characters. Thus preserving the full decorated motif reduces the joint symmetry group by index four.

A separate triangular-lattice nearest-neighbour graph on the same 4-by-4 torus has \(12\times16=192\) affine symmetries: all 12 hexagonal point-group elements combined with the 16 torus translations. This example is a triangular Bravais net, not yet a honeycomb with its two-site basis.

## 7. Relation to the 17 wallpaper groups

The group of a periodic crease network is a wallpaper group when its full translation subgroup has rank two and its point quotient is finite. The classical classification has 17 types. UF-005 does not re-prove the classification; it provides a way to take a specific crease motif and compute its actual symmetry subgroup and its decoration characters.

The affine extension matters. A point-group element may lift to a rotation/reflection about a shifted centre or to a glide reflection. Therefore the correct object is the full affine group and its translation subgroup, not simply a point group acting at the origin. The exact sequence in Section 2 records this without assuming a split extension.

## 8. Limits and next problems

1. The finite-torus checker is exact for the finite combinatorial motif it is given. In the current run, the lattice point groups also passed 212 closure and inverse checks. It does not prove continuous symmetry of an arbitrary curve from finitely many samples.
2. The sign-character framework assumes each decoration is transformed globally by one sign. More general decorations require higher permutation representations.
3. A height function such as \(\operatorname{Re}(z^6)\) defines a local six-line crease star; by itself it is not a periodic honeycomb height function. The periodic lattice and its basis must be supplied separately.
4. The next step is to classify which character maps are realizable for each wallpaper group and which decorations force their kernels.

**Conclusion.** A periodic Fold is best understood as an affine wallpaper-group action on a decorated crease graph. The geometric zero set determines one symmetry group; the signed height and lattice decorations determine characters on subgroups of it. The common invariant symmetry group is the kernel of the combined character map, and the number of independent signs determines its index.
