# UF-010 — Divisor Parity, Disconnected Creases, Singularities, and Multiplicity

**Research question.** How do disconnected crease components, higher-order analytic singularities, and prescribed zero multiplicities affect the existence of one global analytic Fold height with exactly the requested zero set?

**Main result.** The right object is not the full support of a weighted crease divisor, but its **odd-multiplicity support**. If

\[
D=\sum_{i\in I}m_iC_i,\qquad m_i>0,
\]

then only components with odd \(m_i\) reverse the sign of a scalar height. The exact global-principality criterion of Acquistapace–Díaz-Cano says that, under their global analytic and local-principality hypotheses, \(D\) is principal exactly when its mod-2 divisor class vanishes and removing its odd support disconnects the ambient analytic set. The all-even case is different: every positive even divisor has a positive analytic equation, without a separating-complement requirement.

This gives a complete parity classification for the divisor class of networks covered by the theorem, and it corrects a common overrestriction: even-multiplicity crease components need not separate faces or be part of the sign-changing graph.

## 1. Weighted analytic crease divisors

Let \(X\subset\mathbb R^n\) be a pure-dimensional, irreducible global real-analytic set of dimension \(q\). Let \(\{C_i\}_{i\in I}\) be a locally finite family of irreducible codimension-one analytic divisors, with each \(C_i\) meeting the regular locus of \(X\). Write

\[
D=\sum_{i\in I}m_iC_i,\qquad m_i\in\mathbb Z_{>0}.
\]

Assume each component ideal sheaf \(\mathfrak p_i\mathcal O_X\) is locally principal. This hypothesis is automatic in many smooth ambient settings, but must not be silently assumed on singular analytic spaces.

Define the reduced odd support

\[
C_{\mathrm{odd}}=\bigcup_{m_i\text{ odd}} C_i,
\]

and the mod-2 divisor class

\[
[D]_2=\sum_i(m_i\bmod2)[C_i]
=\sum_{m_i\text{ odd}}[C_i]
\in H_{q-1}^{\infty}(X;\mathbb Z_2).
\]

The homology here is the locally finite (Borel–Moore type) homology used in the cited theorem. On compact \(X\), it agrees with ordinary homology in the relevant dimension.

## 2. Exact parity criterion for prescribed multiplicities

### Theorem 1 — Weighted divisor principalness criterion

Under the hypotheses above, the ideal

\[
\prod_i\mathfrak p_i^{m_i}
\]

is principal if and only if

\[
\boxed{[D]_2=0\quad\text{and}\quad X\setminus C_{\mathrm{odd}}\text{ is disconnected}.}
\]

The local-principality assumptions on the component ideals are part of the theorem's hypotheses.

This is Corollary 3.7 of Acquistapace and Díaz-Cano, *Divisors in global analytic sets* (JEMS 13 (2011), 297–307). It is stronger than simply applying the reduced-divisor theorem to the full support: **only odd-multiplicity components enter the homology and separation tests.**

### Proof structure and parity decomposition

Write

\[
D=D_{\mathrm{odd}}+2E,
\]

where

\[
D_{\mathrm{odd}}=\sum_{m_i\text{ odd}}C_i,
\qquad
E=\sum_i\left\lfloor\frac{m_i}{2}\right\rfloor C_i.
\]

The source paper proves two ingredients:

1. A positive even divisor \(2E\) always has a positive analytic equation with exactly the prescribed even multiplicities (Theorem 2.3).
2. A reduced locally principal divisor is principal when its mod-2 class is zero and its complement disconnects (Theorem 3.4).

Thus, if the odd support satisfies the two global conditions, choose an analytic generator \(g\) for \(D_{\mathrm{odd}}\) with multiplicity one on each odd component, and a positive analytic equation \(p\) for \(2E\). Then

\[
\boxed{h=g\,p,\qquad \operatorname{div}(h)=D.}
\]

Conversely, if \(D\) is principal, its odd-multiplicity components are exactly the places where a real generator changes sign. The theorem's mod-2 class and odd-support disconnection conditions are necessary.

### Corollary 1 — All-even divisors

If every \(m_i\) is even, then \(D\) has a positive analytic equation even when its support is nonseparating:

\[
\boxed{D=2E\implies \exists p\ge0\text{ analytic with }\operatorname{div}(p)=D.}
\]

An even-multiplicity crease is a zero, but it is not a sign-changing wall.

## 3. Disconnected crease components can separate collectively

A disconnected crease support does not imply failure. The relevant question is whether the **union of odd-multiplicity components** satisfies the global conditions.

Consider a flat torus \(T^2=\mathbb R^2/\mathbb Z^2\), with coordinates \((x,y)\). The circles \(x=c\pmod1\) are individually nonseparating. Nevertheless:

| Odd parallel circles | Face-dual graph | Mod-2 class | Exact odd height? |
|---:|---|---|---|
| 1 | one vertex with a loop \(C_1\) | nonzero | No |
| 2 | two vertices with parallel edges \(C_2\) | zero | Yes |
| 3 | triangle \(C_3\) | nonzero | No |
| 4 | square \(C_4\) | zero | Yes |

For two parallel crease circles,

\[
\boxed{h(x,y)=\sin(2\pi x)}
\]

has exactly the two circles \(x=0\) and \(x=\tfrac12\) as simple zero components. Each circle alone is nonseparating, but together they divide the torus into two cylinders. Translation by half a period exchanges the two disconnected crease components and reverses the height:

\[
h(x+\tfrac12,y)=-h(x,y).
\]

For three parallel odd circles, the complement has three components, but the mod-2 class is nonzero. This shows why **both** global conditions matter: disconnection alone is not enough.

## 4. Mixed odd and even support

The face-dual test must be applied to \(C_{\mathrm{odd}}\), not to the entire support \(\bigcup_i C_i\).

For example, take three distinct parallel circles with multiplicities

\[
D=C_0+C_{1/2}+2C_{1/4}.
\]

The odd support consists of only \(C_0\cup C_{1/2}\), which is separating and mod-2 null-homologous. The third circle has even multiplicity and does not reverse signs. An exact analytic height is

\[
\boxed{h(x,y)=\sin(2\pi x)\bigl(1-\cos(2\pi(x-\tfrac14))\bigr).}
\]

Its zero set contains exactly the three specified circles: simple zeros at \(x=0,\tfrac12\) and a double zero at \(x=\tfrac14\). The full support has three parallel circles, whose unweighted dual is the odd cycle \(C_3\); that graph is not the right sign-changing dual. Only the two odd-multiplicity circles are sign-changing walls.

## 5. Arbitrary prescribed odd multiplicities

Suppose the separating odd components have multiplicities \(3,5,1,\ldots\). Their parity class is the same as if each had multiplicity one. Once the reduced odd support has an analytic generator \(g\), the residual even divisor is supplied by a positive equation \(p\). Their product has exactly the requested multiplicities.

On the torus, for two parallel circles one explicit example is

\[
h(x,y)=\sin^3(\pi x)\sin^5\!\bigl(\pi(x-\tfrac12)\bigr).
\]

The total exponent is even, so the product is 1-periodic in \(x\); its zero multiplicities are exactly 3 and 5. It changes sign at both circles because both multiplicities are odd.

## 6. Exact torus product and its mod-2 periodicity condition

For primitive integer normals \(n_j=(a_j,b_j)\), affine levels \(c_j\pmod1\), and positive multiplicities \(m_j\), consider

\[
H(x)=\prod_j\sin\!\left(\pi(n_j\cdot x-c_j)\right)^{m_j}.
\]

Under an integer translation \(v\in\mathbb Z^2\),

\[
H(x+v)=(-1)^{\left(\sum_jm_jn_j\right)\cdot v}H(x).
\]

Therefore the product descends to the torus exactly when

\[
\boxed{\sum_jm_jn_j\equiv(0,0)\pmod2.}
\]

The mod-2 homology class of the line divisor is obtained from the normals by an invertible quarter-turn, so this is precisely its vanishing condition in \(H_1(T^2;\mathbb Z_2)\). The formula gives the exact prescribed affine circles as zero set; a factor with exponent \(m_j\) gives divisor multiplicity \(m_j\).

This is a constructive subclass of the global theorem. It is not a classification of all analytic divisors on the torus.

## 7. Singularities and local vanishing order

Let a local analytic equation for the divisor at a point p be

\[
h=u\prod_{i=1}^r f_i^{m_i},
\]

where u is an analytic unit and the \(f_i\) are reduced local equations for distinct irreducible components. Let \(\nu_p(f_i)\) denote the order of the first nonzero homogeneous term of \(f_i\) at p. Then

\[
\boxed{\nu_p(h)=\sum_{i=1}^r m_i\nu_p(f_i).}
\]

This extends the regular-branch rule from UF-008, but distinguishes analytic multiplicity from the number of real half-branches.

| Local singularity | Reduced local equation | Analytic order | Divisor multiplicity m | Height order |
|---|---|---:|---:|---:|
| Transverse node | \(xy\) | 2 (two order-1 components) | 1 each | 2 |
| Tangential branches | \(y(y-x^2)\) | 2 | 1 each | 2 |
| Cusp | \(y^2-x^3\) | 2 (one irreducible branch) | 1 | 2 |
| Cusp with divisor weight 3 | \((y^2-x^3)^3\) | 2 | 3 | 6 |

Thus a cusp has one irreducible real analytic branch but its defining function has order two. The number of branches alone is not a general formula for the height's vanishing order.

### Local-principality obstruction

The topological parity conditions do not replace local analytic algebra. Acquistapace and Díaz-Cano give the example

\[
X=\{z^2=x^4+y^4\}\subset\mathbb R^3,
\qquad Y=\{x=0,\ z\ge0\}\cap X,
\]

where Y is a parabola with zero mod-2 class and is a boundary, but its ideal is not locally principal at the singular point. Hence it is not a principal divisor. This demonstrates why singular ambient spaces require an explicit local-principality test.

## 8. Symmetries permuting disconnected crease components

If a finite symmetry group G preserves a weighted divisor, its multiplicities must be constant on G-orbits of irreducible components. For the two parallel odd circles above, the half-period translation swaps the two components and preserves their multiplicities. It also swaps the two complementary cylinders, so the induced face sign is −1 and the analytic height is anti-invariant.

When the odd-support face dual is connected and bipartite, its two-colouring is unique up to global reversal. Every symmetry preserving the network therefore either preserves or swaps the two face classes, inducing a single sign character.

If a combinatorial model has several independent connected dual components, each has its own face-sign choice. A group may permute these choices by a signed permutation representation. A single scalar sign character exists only when the chosen face-sign vector is preserved up to one common global sign; otherwise the natural object is a higher-dimensional sign representation.

## 9. Periodic covers versus the compact quotient

A locally finite periodic crease network lifts to a locally finite analytic divisor on \(\mathbb R^2\). The global analytic-divisor theorem is formulated with locally finite divisors and Borel–Moore homology, so it is compatible with noncompact covers under its irreducibility, purity, and local-principality hypotheses. However, a global analytic generator on the universal cover need not be periodic.

For a genuinely periodic scalar height, the clean criterion is to descend the divisor to the compact torus and test principality there. A generator on the torus lifts to a lattice-periodic analytic function. A generator found only on the plane does not, by itself, prove such a periodic descent.

## 10. What “minimal generator” can mean

If \(D\) is principal and h generates its divisor ideal, every other generator is \(u h\) for an analytic unit u (a nowhere-zero analytic function). The divisor fixes the multiplicities along every component and the local order

\[
\nu_p(h)=\sum_i m_i\nu_p(f_i).
\]

Thus these local orders cannot be reduced without changing the prescribed divisor. There is no canonical notion of minimum Fourier support or polynomial degree until an additional complexity measure and coordinate system are chosen. Such optimization is a separate research problem, not a consequence of principality.

## 11. Computational verification

The companion program `tools/fold_divisor_parity_classification.py` checks:

- principalness in seven weighted-divisor examples, separating local, homological, and complement conditions;
- the dual graphs of one, two, three, four, and six parallel torus loops;
- exact torus sine products, mod-2 periodicity, and zero/nonzero samples;
- mixed odd/even support and prescribed odd multiplicities 3 and 5;
- local vanishing-order formulas for nodes and cusps;
- multiplicity invariance under a symmetry that permutes two disconnected crease components.

The code takes local principality and complement connectivity as mathematical inputs; it does not pretend to decide arbitrary analytic-germ principality or topology by finite sampling.

## 12. Conclusions and next problems

1. For weighted crease divisors, **odd multiplicity is the sign-changing parity**. The even part is a positive analytic factor and creates no sign wall.
2. Disconnected crease components can collectively form a principal, sign-changing divisor even when every component separately is nonseparating.
3. The exact general criterion has three independent pieces: local principality, vanishing odd mod-2 divisor class, and disconnection of the complement of the odd support.
4. Singular analytic multiplicity is governed by local equations, not simply by the number of real branches.
5. A symmetry may permute disconnected crease components; invariance of the weighted divisor requires multiplicities to be constant on those permutation orbits.
6. Periodicity is a descent condition: a generator on the universal cover is not automatically a periodic generator.

**Conclusion.** UF-010 gives the correct parity-level classification for prescribed analytic crease multiplicities. The full weighted divisor is principal precisely when its odd support carries the required local and global topology; all-even pieces can then be added by positive analytic equations. This resolves the disconnected-support and arbitrary-multiplicity part of the previous research agenda under the cited hypotheses.

## References

- F. Acquistapace and A. Díaz-Cano, “Divisors in global analytic sets,” *Journal of the European Mathematical Society* 13 (2011), no. 2, 297–307. Theorem 2.2 (generic equation), Theorem 2.3 (positive equation for positive even divisors), Theorem 3.4 (reduced locally principal divisors), and especially Corollary 3.7 (arbitrary component multiplicities, with the homology and complement conditions applied to the odd support). [Publisher page and DOI 10.4171/JEMS/253](https://ems.press/journals/jems/articles/1995); [full article PDF](https://ems.press/content/serial-article-files/31761).