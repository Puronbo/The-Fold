# UF-009 — Exact Analytic Zero-Set Realization of Periodic Crease Networks

**Research question.** When does a periodic crease network occur as the *exact* zero set of a single globally defined real-analytic, periodic, scalar height, rather than merely lying inside the zero set of a function with the right symmetry?

**Main result.** For a compact real-analytic surface presented as a pure-dimensional global real-analytic set, a compact, locally principal real-analytic crease divisor with bipartite face-adjacency dual is the exact zero divisor of a global real-analytic function. The bipartite colouring supplies both the separating complement and the vanishing mod-2 divisor class required by the global principality theorem of Acquistapace and Díaz-Cano. A generic equation has multiplicity one along every irreducible crease component, so the height changes sign across every regular crease arc. If a finite symmetry group preserves the network and the dual graph is connected, a character-weighted group average makes the exact analytic height equivariant without changing its zero set.

A second, fully explicit construction realizes finite unions of paired rational affine line families on a flat torus by products of sine factors.

## 1. The precise object and hypotheses

Let M be a compact connected real-analytic surface, and let C be a compact one-dimensional real-analytic subset. Assume C is a locally principal effective analytic divisor: around every point p there is an analytic function f_p such that

\[
C\cap U_p=\{x\in U_p:f_p(x)=0\},
\]

and f_p is a local generator of the reduced divisor ideal. In particular, if finitely many regular analytic crease branches meet at p, a local defining equation is the product of their branch equations. This includes ordinary transverse crossings and finite normal-crossing stars. Cusps and more complicated singularities are included only when their reduced analytic germ is locally principal.

Let D(C) be the face-adjacency dual graph: one vertex for each connected component of M\C, one edge for each crease arc separating two incident faces, and a loop if the two sides of an arc belong to the same face.

The key distinction is between:

- a function whose zero set merely contains C;
- a function whose zero set is exactly C;
- a function whose zero set is exactly C and changes sign across each crease.

UF-009 addresses the third, strongest requirement.

## 2. Bipartite duals give the analytic divisor's mod-2 boundary condition

Assume D(C) is bipartite. Give each face the sign +1 or −1 according to its bipartition. The union of the + faces and the union of the − faces are disjoint nonempty open subsets of M\C, so M\C is disconnected.

Moreover, take the closure of the + faces as a mod-2 two-chain. Every crease arc separates a + face from a − face, so its boundary contains that arc exactly once. Around a regular-branch vertex the face colours alternate, and every incident branch is again in the boundary once. Therefore the mod-2 boundary of the + region is precisely C:

\[
\boxed{[C]=0\quad\text{in }H_1(M;\mathbb Z_2).}
\]

Thus the bipartite dual gives two global conditions:

1. M\C is disconnected;
2. the mod-2 fundamental class of the divisor vanishes.

These are precisely the topological inputs in the analytic principality theorem used next.

## 3. Exact analytic realization theorem

Acquistapace and Díaz-Cano prove that a locally principal divisor Y in a pure-dimensional global real-analytic set X is globally principal when X\Y is disconnected and the mod-2 divisor class vanishes. They also establish the existence of a generic equation with multiplicity one along each irreducible component of a divisor. See their paper, *Divisors in global analytic sets*, J. Eur. Math. Soc. 13 (2011), 297–307, DOI 10.4171/JEMS/253.

### Theorem 1 — Bipartite analytic divisor realization

Let X be a compact pure two-dimensional global real-analytic set which is nonsingular, and let C be a compact locally principal real-analytic divisor on X. If D(C) is bipartite, then there exists a global real-analytic function h on X such that

\[
\boxed{h^{-1}(0)=C,}
\]

and h has multiplicity one along every irreducible crease component. Consequently h changes sign across every regular crease arc.

**Proof.** The bipartite face colouring gives X\C disconnected and [C]=0 in mod-2 one-dimensional homology, as shown in Section 2. Since C is locally principal and X is pure dimensional, the global principality theorem of Acquistapace–Díaz-Cano applies: the divisor C is principal, so it is the zero divisor of a global analytic function. Their generic-equation result allows multiplicity one on each irreducible component. A real analytic function with a simple zero across a regular real curve changes sign across it. Since the principal divisor is exactly C, there are no additional zero components. ∎

### Converse

If a continuous real-valued function has exact zero set C and changes sign across every crease, its sign on each face gives a proper two-colouring of D(C). Therefore D(C) must be bipartite. The analytic theorem and the converse together give the desired equivalence under the stated locally principal global-analytic hypotheses:

\[
\boxed{\begin{array}{c}
D(C)\text{ bipartite}\\[2pt]
\Updownarrow\\[2pt]
\exists\text{ global analytic }h:\ h^{-1}(0)=C,\\
\text{with sign reversal across every regular crease.}
\end{array}}
\]

The forward implication is the deep analytic-principality step; it is not obtained by trying to glue local analytic functions with an analytic partition of unity (such partitions generally do not exist).

**Scope.** The theorem is stated for nonsingular compact global real-analytic surfaces and locally principal analytic divisors. It is not a theorem about arbitrary topological graphs, nonanalytic crease arcs, non-locally-principal singularities, or noncompact surfaces without further hypotheses. The flat torus is within the stated setting; for example, it is a compact analytic submanifold of R⁴ given by x₁²+x₂²=1 and x₃²+x₄²=1.

## 4. Enforcing a finite symmetry without changing the exact zero set

Suppose a finite group G acts real-analytically on X, preserves C, and D(C) is connected and bipartite. Its unique bipartition up to global reversal induces a character

\[
\chi_C:G\longrightarrow\{+1,-1\},
\]

where +1 means a symmetry preserves the two face classes and −1 means it exchanges them.

Let h₀ be the exact analytic height supplied by Theorem 1. Define

\[
\boxed{H(x)=\sum_{g\in G}\chi_C(g)\,h_0(gx).}
\]

For x in any face F, the sign of h₀(gx) is the sign of the face gF. By definition of χ_C, multiplying by χ_C(g) returns the sign of F. Thus every term in the sum has the same sign off C; no cancellation can create an extra zero. Every term vanishes on C. Therefore

\[
H^{-1}(0)=C.
\]

Changing variables in the finite sum also gives

\[
\boxed{H(ax)=\chi_C(a)H(x)\qquad(a\in G).}
\]

So the exact analytic height can be made equivariant with the network-induced character, without sacrificing its exact zero set. This is stronger than a generic Fourier projection, which provides a semi-invariant but does not control its zero divisor.

## 5. An explicit formula for paired rational line families on a torus

There is a simple closed-form construction for an important periodic class. Work on

\[
T^2=\mathbb R^2/\mathbb Z^2.
\]

For each crease family choose a primitive integer covector n_j=(a_j,b_j), with no two covectors parallel. Choose 2r_j distinct levels c_{j,1},…,c_{j,2r_j} modulo one. The family consists of the affine circles

\[
a_jx+b_jy=c_{j,\ell}\pmod1.
\]

Define

\[
\boxed{h(x,y)=\prod_j\prod_{\ell=1}^{2r_j}
\sin\!\bigl(\pi(a_jx+b_jy-c_{j,\ell})\bigr).}
\]

### Theorem 2 — Paired-line exact product

This function is globally periodic, real analytic, and its zero set is exactly the union of the selected affine circles. It changes sign across each circle away from intersections.

**Proof.** Under an integer translation m=(m₁,m₂), each sine in family j is multiplied by

\[
(-1)^{a_jm_1+b_jm_2}.
\]

There are 2r_j factors in that family, so their combined translation multiplier is +1. Thus h is periodic. A factor vanishes exactly when its affine argument is an integer, giving precisely the specified level circle modulo one. Distinct levels and nonparallel families prevent duplicated branches. At a generic point of one circle, its factor has a simple zero and all other factors are nonzero, so the sign changes there. ∎

At a point where q distinct families intersect transversely, exactly q independent factors vanish simply. Hence

\[
\boxed{\operatorname{ord}_p(h)=q.}
\]

This gives exact analytic crease arrangements with the branch-count vanishing order predicted in UF-008. The even-number-per-direction condition is a convenient sufficient construction class, not a classification of every bipartite line arrangement on the torus.

## 6. The UF-008 square and triangular examples as exact products

Choose two levels 0 and 1/2 in each family. Since

\[
\sin(\pi q)\sin(\pi(q-1/2))=-\tfrac12\sin(2\pi q),
\]

the square arrangement is, up to a positive constant,

\[
\sin(2\pi x)\sin(2\pi y).
\]

Using the three primitive normals (1,0), (0,1), and (1,1), the triangular arrangement is, up to a nonzero constant,

\[
\sin(2\pi x)\sin(2\pi y)\sin(2\pi(x+y)).
\]

Thus these familiar examples are not only analytic semi-invariants: their displayed functions have exactly the prescribed crease sets and no hidden zero curves.

## 7. Computational verification

The companion program `tools/fold_exact_analytic_networks.py` checks:

- periodicity under integer translations for the paired-line products;
- the exact square and triangular product identities;
- zero samples on every specified line family and nonzero samples off the network;
- D₆ presentation relations and the triangular seed's sign character;
- a character-weighted analytic group average which preserves the exact zero set and realizes the induced D₆ character.

These are numerical checks of explicit formulas. The global existence theorem in Section 3 relies on the cited analytic-principality result, not on numerical sampling.

## 8. Consequences and remaining problem

1. Under the locally principal real-analytic divisor hypotheses, UF-007's bipartite criterion is sufficient for an exact global analytic height, not merely a smooth one.
2. The analytic-principality theorem supplies a global defining function; generic multiplicity one makes the scalar height sign-changing along every regular branch.
3. A finite symmetry preserving a connected-bipartite crease network can be imposed by character-weighted averaging without creating or removing zeros.
4. Paired rational line families admit an explicit product formula, making a large and useful class of periodic Fold networks constructive.
5. The remaining question is to extend the result to non-locally-principal singularities, noncompact periodic covers, prescribed higher odd multiplicities, and networks whose dual graph has several components with a nontrivial symmetry action on component signs.

**Conclusion.** UF-009 closes the main gap left by UF-008 for compact analytic periodic networks: for locally principal analytic crease divisors, bipartite topology yields a global analytic defining function with exactly the prescribed zero set. Symmetry can then be imposed by a finite character-weighted sum which preserves that exact set.

## References

- Francesca Acquistapace and A. Díaz-Cano, “Divisors in global analytic sets,” *Journal of the European Mathematical Society* 13 (2011), no. 2, 297–307. The paper proves global principality for locally principal divisors under complement-disconnection and vanishing mod-2 class hypotheses, and proves existence of generic equations with multiplicity one along irreducible components. [Publisher abstract and DOI](https://ems.press/journals/jems/articles/1995), [DOI 10.4171/JEMS/253](https://doi.org/10.4171/JEMS/253).