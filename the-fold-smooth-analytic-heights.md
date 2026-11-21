# UF-008 — Smooth and Analytic Realizability of Fold Heights

**Research question.** When does a periodic crease network admit a smooth or real-analytic signed height, and what does the local geometry of a crease vertex force about the height's vanishing order?

**Main result.** Under a finite regular-branch hypothesis, the dual-graph bipartite criterion from UF-007 is sufficient not only for a continuous height but also for a global smooth height. Locally, a vertex where exactly q distinct smooth crease branches meet forces every smooth sign-changing height to vanish to order at least q; the bound is sharp, attained by the product of local branch-defining functions. For analytic branches this construction is real analytic locally. Exact global analytic realization is now resolved under compact locally principal analytic-divisor hypotheses in UF-009: bipartite face duals yield global analytic defining functions, and finite-group averaging imposes the induced character without changing the exact zero set.

## 1. The local model and its assumptions

Let M be a smooth surface and C a finite embedded crease graph. Assume:

1. every open edge is a smooth embedded curve;
2. every vertex p has a neighborhood in which C is the union of q_p distinct smooth embedded curve germs through p (no terminal half-edges, cusps, or isolated singular components);
3. each such germ has a local smooth defining function \(\phi_i\) with nonzero differential on its zero curve.

The branches need not have distinct tangent lines; the clean transverse case is the usual normal-crossing model. If \(q_p\) branches meet at p, each branch contributes two half-edges, so the graph valence is \(2q_p\). A graph vertex of odd valence is excluded by these assumptions and cannot be a regular-branch zero of a scalar sign-changing height.

In a sufficiently small neighborhood U of p, the local product

\[
\boxed{H_p=\prod_{i=1}^{q_p}\phi_i}
\]

is smooth, has zero set exactly C in U, and changes sign when crossing any one branch. It vanishes to order exactly q_p if the defining functions are chosen with nonzero differentials. Its leading homogeneous Taylor term is the product of the q_p tangent linear forms; repeated tangent directions appear as repeated factors.

For analytic branches and analytic defining functions, the same product is real analytic.

## 2. The smooth realization theorem

Let D(C) be the face-adjacency dual graph of C, retaining a loop when both sides of an edge belong to the same face.

### Theorem 1 — Smooth realization under the regular-branch hypothesis

Under the assumptions in Section 1, the following are equivalent:

- D(C) is bipartite;
- there exists a global smooth function \(h\in C^\infty(M,\mathbb R)\) such that \(h^{-1}(0)=C\) and h has opposite signs on the two sides of every crease edge.

**Necessity.** Since h is nonzero on each face, its sign is constant on each connected face. Crossing any crease changes the sign. The signs therefore form a proper two-colouring of D(C), so D(C) is bipartite.

**Sufficiency.** Choose a bipartite face sign \(\epsilon(F)\in\{+1,-1\}\). Near each point of C, the local product \(H_p\) changes sign across every local branch. Choose its overall sign so it agrees with \(\epsilon\) on one local face; bipartiteness makes it agree on all local faces in that chart. On charts disjoint from C, use the constant sign of the face. Take a smooth partition of unity subordinate to this cover and form the weighted sum of the local functions. Every summand active at a point outside C has the same nonzero sign, so the sum cannot cancel; at a point of C every active local defining function vanishes. The resulting global smooth function has exact zero set C and the required sign change. \(\square\)

This strengthens UF-007: for finite networks of regular smooth branches, bipartiteness is exactly the criterion for a global C-infinity scalar height, not merely a continuous one. The regular-branch hypothesis matters; arbitrary singular graphs, endpoints, cusps, and higher-dimensional order parameters need separate treatment.

## 3. The local vanishing-order theorem

### Theorem 2 — Branch-count lower bound

Suppose q distinct regular smooth crease branches meet at p and a smooth scalar height h vanishes on all of them. Then

\[
\boxed{\operatorname{ord}_p(h)\ge q}
\]

where infinite order (flatness) is allowed. The lower bound is attained by \(H_p=\prod_i\phi_i\).

**Proof.** By the smooth Hadamard lemma, vanishing on the regular curve \(\phi_1=0\) gives \(h=\phi_1h_1\) for a smooth \(h_1\). On every other branch away from p, \(\phi_1\ne0\), so \(h_1\) vanishes there; continuity extends this to p. Divide successively by \(\phi_2,\ldots,\phi_q\), obtaining

\[
h=(\phi_1\cdots\phi_q)u
\]

with u smooth. Each \(\phi_i\) vanishes to first order at p, so all derivatives of h of total order less than q vanish at p. The product itself attains order q. \(\square\)

Consequences:

- At a regular crease edge (q=1), a reduced defining function can have a simple zero and nonzero normal derivative.
- At a transverse four-valent crossing (q=2), the gradient must vanish. The local model \(xy\) has a nondegenerate saddle Hessian.
- At a six-valent three-branch junction (q=3), all first- and second-order derivatives vanish; the leading term is cubic.
- More generally, the number of half-edges is \(2q\), and the minimum finite vanishing order is q, not the valence \(2q\).

If the q branches have distinct tangent directions, the leading homogeneous Taylor polynomial must contain their q distinct tangent-line factors. If some branches are tangent, the product still gives order q, with repeated tangent factors in its leading term.

## 4. Analytic realizability: local and global are different

For regular real-analytic branches, each branch has a local analytic defining function, and their product gives a real-analytic local height with exact zero set. Therefore the branch-count lower bound and its sharpness also hold in the analytic category locally.

A global analytic function cannot in general be assembled with a smooth partition of unity: nontrivial smooth partitions of unity are not real analytic. The exact-zero problem therefore requires a different tool: the global principality theorem for real-analytic divisors. UF-009 applies that theorem to compact locally principal bipartite crease divisors and resolves exact analytic realization under those hypotheses.

### Theorem 3 — Fourier projection realizes every periodic sign character

Let a finite point group P act on a rank-two torus by affine maps \(g(x)=A_gx+b_g\), with distinct linear parts \(A_g\in GL(2,\mathbb Z)\). Let \(\chi:P\to\{\pm1\}\) be any real character. Choose an integer frequency \(k\in\mathbb Z^2\) with trivial stabilizer under the dual action \(k\mapsto A_g^{-T}k\). Such a k exists: each nonidentity finite-order linear map fixes a proper subspace, and a finite union of proper subspaces cannot cover the integer lattice.

Define the complex Fourier projection

\[
F_{\chi,k}(x)=\sum_{g\in P}\chi(g)\exp\!\bigl(2\pi i\langle k,g^{-1}x\rangle\bigr).
\]

Then \(F_{\chi,k}\) is periodic and real analytic, and

\[
\boxed{F_{\chi,k}(gx)=\chi(g)F_{\chi,k}(x).}
\]

**Proof.** For a fixed \(a\in P\), substitute \(g=ab\) in the sum for \(F_{\chi,k}(ax)\). Since \((ab)^{-1}a=b^{-1}\) and \(\chi(ab)=\chi(a)\chi(b)\), the result is \(\chi(a)F_{\chi,k}(x)\). Distinct dual-orbit frequencies make the Fourier terms linearly independent, so the sum is not identically zero. Because \(\chi\) is real, the real and imaginary parts are both semi-invariants; at least one is nonzero. \(\square\)

Therefore **every algebraically allowed periodic sign character of a wallpaper point group has some nonzero global real-analytic periodic representative**. This does not imply that its zero set equals an arbitrarily prescribed crease graph; exact-divisor realization is a stronger problem. The explicit examples below give particularly simple exact networks.

## 5. A square-periodic analytic example

On the square torus \(T_s=\mathbb R^2/\mathbb Z^2\), set

\[
\boxed{h_s(x,y)=\sin(2\pi x)\sin(2\pi y).}
\]

This is globally periodic and real analytic. Its exact zero set is the union of four closed crease circles

\[
x=0,\;x=\tfrac12,\qquad y=0,\;y=\tfrac12\pmod 1.
\]

There are four crossing vertices per fundamental torus, each with two regular branches. Near a vertex \((x_0,y_0)\), writing \(u=x-x_0,\ v=y-y_0\),

\[
h_s(x_0+u,y_0+v)=\pm(2\pi)^2uv+O(\|(u,v)\|^4),
\]

so the vanishing order is exactly 2, the sharp branch-count bound. The square point group has order 8 (D4); every point-group element sends \(h_s\) to either \(+h_s\) or \(-h_s\), giving a sign character.

## 6. A triangular-periodic analytic example realizing D6

Let the triangular torus be expressed in a lattice basis whose Gram matrix is

\[
G=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

Define

\[
\boxed{h_t(x,y)=\sin(2\pi x)\sin(2\pi y)\sin(2\pi(x+y)).}
\]

This is a globally periodic real-analytic function on \(\mathbb R^2/\mathbb Z^2\). Its zero set is the union of three families of parallel closed crease circles:

\[
x\in\tfrac12\mathbb Z,\qquad y\in\tfrac12\mathbb Z,\qquad x+y\in\tfrac12\mathbb Z\pmod 1.
\]

There are six crease circles and four triple-intersection vertices \((x,y)\in\{0,\tfrac12\}^2\). Each vertex has three regular branches (six half-edges), and the local vanishing order is exactly 3.

The triangular lattice point group is D6. In lattice coordinates choose

\[
r(x,y)=(-y,x+y),\qquad s(x,y)=(-x-y,y).
\]

They satisfy \(r^6=s^2=1\) and \(srs=r^{-1}\). Direct trigonometric substitution gives

\[
\boxed{h_t(r(x,y))=-h_t(x,y),\qquad h_t(s(x,y))=h_t(x,y).}
\]

Thus this periodic analytic network realizes the D6 character with \(\chi(r)=-1\) and \(\chi(s)=+1\), which is the sublattice-type character in the UF-004 convention. It is a three-direction triangular crease network, not the honeycomb graph; the distinction is intentional.

Near a triple vertex, the leading term is

\[
h_t(u,v)=(2\pi)^3uv(u+v)+O(\|(u,v)\|^5),
\]

so the cubic order is exactly the minimum predicted by Theorem 2.

## 7. Smoothness at vertices: practical classification

For regular branches, the product model gives an immediate local rule:

| Local geometry | Branches q | Minimal vanishing order | First forced zero jet |
|---|---:|---:|---|
| Regular edge | 1 | 1 | h itself |
| Transverse four-valent crossing | 2 | 2 | value and gradient |
| Six-valent triple crossing | 3 | 3 | value, gradient, Hessian |
| Eight-valent four-branch crossing | 4 | 4 | all derivatives of order below 4 |

This is a geometric count of regular branches, not a universal formula for arbitrary singular analytic curves. Cusps and singular irreducible branches require their own local algebra; real-analytic curve germs can have more intricate branch topologies. See Ghys and Simon for the local topology of real-analytic planar curve singularities.

## 8. Consequences and remaining questions

1. The UF-007 bipartite obstruction is exactly the smooth scalar obstruction for finite regular-branch networks; the partition-of-unity construction makes it constructive.
2. Local vertex valence controls the minimum finite vanishing order: a 2q-valent regular-branch vertex requires order at least q.
3. Explicit periodic analytic heights exist on square and triangular tori. The triangular example realizes a nontrivial D6 character globally, not merely as a local polynomial star.
4. Analytic global realization is more rigid than smooth realization. A general criterion for when a bipartite periodic network is the exact zero divisor of a global analytic function remains open in this project.
5. The next step is to classify analytic equivariant functions for each wallpaper character and determine which prescribed crease divisors are globally principal.

**Conclusion.** For regular crease networks, topology decides whether a smooth sign-changing height exists; local branch geometry determines its minimum vanishing order; and global analytic periodic examples show that the framework can produce actual periodic Fold heights, not just abstract sign assignments.

## References

- É. Ghys and C.-L. Simon, *On the topology of a real analytic curve in the neighborhood of a singular point* (2018). The paper treats local real-analytic curve germs as products of irreducible branches and studies their local topology: [manuscript PDF](https://christopherlloyd.github.io/works/pre-publications/2017-04_TopoSingulaReAnalytiCurve_ghysimon.pdf).
- Yuan Xu, *Harmonic Polynomials Associated With Reflection Groups*, Canadian Mathematical Bulletin (2000; online publication page updated 2018). This is background for polynomial and harmonic constructions associated with finite reflection groups: [Cambridge article](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/harmonic-polynomials-associated-with-reflection-groups/F59059792FA3486F0F9E1B4F43128D8F).
- T. Beck, S. Becker-Kahn, and B. Hanin, *Nodal sets of smooth functions with finite vanishing order and p-sweepouts*, Calculus of Variations and Partial Differential Equations 57 (2018), 140: [DOI 10.1007/s00526-018-1406-y](https://doi.org/10.1007/s00526-018-1406-y).

## UF-009 update: exact analytic zero-set realization

The earlier global-analytic compatibility question is resolved for compact nonsingular global real-analytic surfaces and compact locally principal crease divisors: bipartiteness gives a separating complement and vanishing mod-2 divisor class, so the Acquistapace–Díaz-Cano principality theorem yields a global analytic function whose exact zero divisor is the network. A generic equation has multiplicity one along every irreducible component. For connected duals, character-weighted group averaging makes this exact defining function equivariant while preserving its zero set. See the-fold-exact-analytic-networks.md.
