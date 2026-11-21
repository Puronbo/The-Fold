# UF-012 — Exceptional Intersection Lattices and Local Divisor Classes

**Research question.** How does a non-Cartier crease divisor on a normal surface singularity appear on a resolution, and when can exceptional intersection data decide whether it descends as a principal analytic height?

**Main result.** On a resolution \(\pi:\widetilde X\to X\) of a normal surface singularity, let \(E_1,\ldots,E_r\) be the exceptional curves and let \(M=(E_i\cdot E_j)\) be their negative-definite intersection matrix. If a Weil divisor \(D\) downstairs is Cartier (hence principal in the local ring), its strict transform \(\widetilde D\) must admit an **integral exceptional correction** \(a\in\mathbb Z^r\) satisfying

\[
\boxed{M a=-b(D),\qquad b(D)_j=(\widetilde D\cdot E_j).}
\]

Thus the class of \(b(D)\) in the lattice cokernel \(\operatorname{coker}(M)\) is a computable obstruction. For rational surface singularities in the usual henselian/complete setting, the local divisor class group is the discriminant group of the exceptional lattice, so this obstruction is complete. For non-rational singularities it is generally only the **finite numerical quotient**: degree-zero \(\operatorname{Pic}^0\) data can remain. This distinction is essential for the cone example in UF-011.

## 1. From a principal equation to an exceptional correction vector

Let \(R=\mathcal O_{X,p}\) be a two-dimensional normal local domain, and let \(\pi:\widetilde X\to\operatorname{Spec}(R)\) be a resolution. Let \(D\) be an effective Weil divisor whose strict transform is \(\widetilde D\). The exceptional curves form the reduced exceptional fibre \(E=\bigcup_i E_i\). Their intersection matrix

\[
M=(E_i\cdot E_j)_{i,j=1}^r
\]

is negative definite, hence invertible over \(\mathbb Q\). This is the standard negativity theorem for resolutions of normal surface singularities.

If \(D\) is principal, say \(D=\operatorname{div}_R(f)\), then on the smooth surface \(\widetilde X\),

\[
\operatorname{div}_{\widetilde X}(f)
=\widetilde D+\sum_{i=1}^r a_iE_i,
\qquad a_i=v_{E_i}(f)\in\mathbb Z_{\ge0}.
\]

A principal divisor has zero intersection with every compact exceptional curve. Intersecting with \(E_j\) gives

\[
0=(\widetilde D\cdot E_j)+\sum_i a_i(E_i\cdot E_j),
\]

or, in vector form, \(Ma=-b(D)\). Therefore:

### Theorem 1 — Integral exceptional-correction obstruction

If \(D\) is Cartier/principal downstairs, then

\[
\boxed{b(D)\in M\mathbb Z^r.}
\]

Equivalently, \([b(D)]=0\) in \(\operatorname{coker}(M)\). If the unique rational solution \(a=-M^{-1}b(D)\) is not integral, then \(D\) cannot be principal downstairs.

This is always a valid **necessary** obstruction. It becomes sufficient when the local divisor class group is identified with the exceptional-lattice discriminant group (for example, for rational surface singularities under the standard henselian/complete hypotheses). Outside that setting, a numerically trivial class can still survive in a degree-zero Picard term.

## 2. Why the lattice cokernel is not always the whole class group

Lipman's resolution-theoretic sequence separates the divisor class group into a numerically trivial part and a finite group controlled by the exceptional intersection matrix. In his notation, the sequence has the form

\[
0\longrightarrow \rho(\operatorname{Pic}^0(\widetilde X))
\longrightarrow \operatorname{Cl}(R)
\longrightarrow H
\longrightarrow G\longrightarrow0,
\]

where \(H\) is the finite cokernel of the exceptional intersection map, with the appropriate degree divisors \(d_i\) included for general exceptional curves. The group \(G\) vanishes under the unibranch hypothesis on all height-one quotients; Lipman notes that this holds for henselian local rings. The lattice matrix is negative definite, and when all exceptional components are rational, \(d_i=1\), so \(H\cong\operatorname{coker}(M)\).

For rational surface singularities the degree-zero part vanishes, giving the familiar finite discriminant-group description. For a simple-elliptic singularity, the exceptional curve has genus one and contributes nontrivial degree-zero line bundles. Then the intersection lattice gives only the finite numerical quotient, not the entire local class group.

This prevents a common error: **do not identify the determinant of the exceptional matrix with the order of the full local class group unless the rationality/Picard hypotheses justify it.**

## 3. Calibration example: the rational double point \(A_n\)

Consider

\[
R_n=\mathbb C\{x,y,z\}/(xy-z^{n+1}),\qquad n\ge1.
\]

Its minimal resolution has a chain of \(n\) exceptional curves \(E_1-\cdots-E_n\), each a smooth rational curve with self-intersection \(-2\), neighboring curves meeting once, and all other pairs disjoint. The intersection matrix is

\[
M_{A_n}=\begin{pmatrix}
-2&1&0&\cdots&0\\
1&-2&1&\ddots&\vdots\\
0&1&-2&\ddots&0\\
\vdots&\ddots&\ddots&\ddots&1\\
0&\cdots&0&1&-2
\end{pmatrix}_{n\times n}.
\]

A determinant recurrence gives

\[
\det(M_{A_n})=(-1)^n(n+1),
\]

and the cokernel is cyclic:

\[
\boxed{\operatorname{coker}(M_{A_n})\cong\mathbb Z/(n+1).}
\]

The height-one prime \(P=(x,z)\) is a standard generator of \(\operatorname{Cl}(R_n)\). The divisor of \(x\) is \((n+1)P\), and the strict transform of P meets one end exceptional curve once. Its intersection vector is therefore the end basis vector \(e_1\), which has order \(n+1\) in the cokernel. Thus \(P\) is non-Cartier, but \((n+1)P\) is principal.

For \(n=1\), this is the \(A_1\) example: \(M=[-2]\), \(b=[1]\), and the correction equation is

\[
-2a=-1\quad\Longrightarrow\quad a=\tfrac12.
\]

The fractional correction exposes the nontrivial class in \(\mathbb Z/2\).

## 4. Return to the UF-011 cone: a simple-elliptic \(\widetilde E_7\) singularity

The UF-011 surface is

\[
X=\{z^2=x^4+y^4\}\subset\mathbb C^3.
\]

It is the simple-elliptic singularity of type \(\widetilde E_7\) (also called \(\widetilde T_{2,4,4}\)). Its minimal resolution has one exceptional curve \(E\), a smooth genus-one curve, with

\[
\boxed{E\cdot E=-2.}
\]

The genus can also be read from the exceptional curve in weighted projective coordinates: it is a double cover of \(\mathbb P^1\), branched at the four distinct roots of \(x^4+y^4\); Riemann–Hurwitz gives genus one. The self-intersection \(-2\) is the degree of this simple-elliptic type.

Recall the UF-011 crease

\[
Y=\{x=0,\ z=y^2\}.
\]

In the weighted chart \(x=uv,\ y=u,\ z=u^2w\), the strict transform of X is \(w^2=1+v^4\); the strict transform of Y is \(v=0,w=1\), and the exceptional curve is \(u=0\). Near \(w=1\), \(w\) is an analytic function of \(v\), so \((u,v)\) are local coordinates. Hence the strict transform meets E transversely at one point P:

\[
\widetilde Y\cdot E=1.
\]

The exceptional matrix and intersection vector are

\[
M=[-2],\qquad b(Y)=[1].
\]

The correction equation again has solution \(a=1/2\), not an integer. Therefore its class is nonzero in the numerical quotient

\[
\boxed{H\cong\mathbb Z/2.}
\]

This recovers the non-Cartier obstruction from UF-011 by intersection theory, independently of the two-generator calculation \((x,z-y^2)\).

**Important nuance.** The exceptional curve is elliptic, not rational. Its degree-zero Picard group is nontrivial, so \(\mathbb Z/2\) is the finite numerical quotient, not automatically the full local class group. The nonzero residue \(1\bmod2\) is already enough to prove that Y is not Cartier; no claim about the complete group structure is needed.

## 5. The exact descent criterion: rational versus non-rational cases

The exceptional correction test has two levels.

**Numerical necessity, any normal surface singularity:**

\[
D\text{ Cartier}\ \Longrightarrow\ b(D)\in M\mathbb Z^r.
\]

If this fails, stop: the divisor cannot descend as a Cartier crease divisor, regardless of its global sign character.

**Numerical sufficiency, rational case:** under the standard hypotheses that identify the local divisor class group with the exceptional-lattice discriminant group, vanishing of \([b(D)]\) in \(\operatorname{coker}(M)\) is also sufficient for local principality.

**Non-rational case:** vanishing in the finite lattice quotient only removes the numerical obstruction. One must additionally test the degree-zero Picard/class component and the final term \(G\) in the resolution sequence. This is the missing information in a criterion based solely on intersection numbers.

Once the local divisor is Cartier at every singular point, its global principalness for a prescribed real analytic Fold height still requires the UF-010 odd-support mod-2 and complement-disconnection conditions.

## 6. Exceptional multiplicities as a linear system

Given an effective crease divisor D, the vector

\[
b_j=(\widetilde D\cdot E_j)
\]

is computed from intersections on the resolved surface. If D has a principal local equation, the exceptional valuation vector is the unique solution

\[
\boxed{a=-M^{-1}b.}
\]

Its entries must be nonnegative integers for an effective holomorphic local equation. The vector a records the orders of the local height along the exceptional curves. It must not be confused with the multiplicities of the original crease components: those are the coefficients of D downstairs. Strict transform, total transform, and exceptional valuation data are three distinct pieces of information.

For a rational singularity, changing the divisor by a principal divisor changes b by an element of \(M\mathbb Z^r\). Therefore the class \([b]\) is invariant under local principal equivalence. The order of \([b]\) is the smallest positive integer k for which kD passes the numerical descent test; in the rational case it is exactly the order of the local divisor class.

## 7. Computational method added for The Fold

The companion program uses exact rational arithmetic to:

- build the negative Cartan intersection matrix for \(A_n\);
- compute its determinant by fraction-free Bareiss elimination;
- solve \(Ma=-b\) over \(\mathbb Q\) exactly;
- determine the smallest k such that \(k b\in M\mathbb Z^r\);
- verify the \(A_n\) end-divisor class has order \(n+1\) for several n;
- verify the UF-011 simple-elliptic numerical quotient \(\mathbb Z/2\) and its fractional correction \(1/2\).

The code computes the lattice obstruction. It deliberately does not claim to compute \(\operatorname{Pic}^0\), the group G, or arbitrary analytic class groups.

## 8. UF-012 conclusions and next question

1. Exceptional intersection matrices convert local divisor descent into an integer-lattice problem.
2. The quotient \(\operatorname{coker}(M)\) is the finite numerical obstruction, and is the full class group in the rational setting with the standard hypotheses.
3. The UF-011 cone is simple elliptic \(\widetilde E_7\): \(E\) is elliptic with \(E^2=-2\), and the crease meets E once. Its numerical class is the nonzero element of \(\mathbb Z/2\).
4. Because that exceptional curve has genus one, degree-zero Picard data remain; one must not equate \(|\det M|=2\) with the order of the full class group without further justification.
5. A successful local descent test must still be followed by the global UF-010 parity/separation test.

**Open UF-013 direction.** Extend the exact lattice method to ADE graphs, simple-elliptic and cusp configurations with nontrivial \(\operatorname{Pic}^0\), and symmetry actions on exceptional lattices. In particular, determine which Fold symmetry characters lift to the resolution and descend through contraction.

## References

- Joseph Lipman, “Rational Singularities, with Applications to Algebraic Surfaces and Unique Factorization,” *Publications Mathématiques de l'IHÉS* 36 (1969), 195–279. Sections 13–15 establish negative definiteness and the exact sequence separating the degree-zero Picard part from the finite exceptional-lattice quotient; §§17 and 24 discuss the rational-singularity class groups and ADE diagrams. [Numdam PDF](https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf).
- Eduard Looijenga, *Rational Surfaces and Singularities*, Table 2, identifies the simple-elliptic \(\widetilde E_7=\widetilde T_{2,4,4}\) equation, degree 2, and weights (2,4,4); § “Simple elliptic singularities” describes the genus-one exceptional curve with self-intersection \(-d\). [Lecture notes PDF](https://webspace.science.uu.nl/~looij101/delpezzo.pdf).
- Kyoji Saito, *Simply Elliptic Singularities*, for the relation between simple-elliptic surface equations and their exceptional elliptic curves. [RIMS PDF](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1611.pdf).