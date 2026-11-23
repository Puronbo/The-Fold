# G-EP2 — Cyclotomic spectral fingerprints

**Status:** proved statements are separated from implementation targets.  
**Scope:** finite-field spectra of integral matrices assembled from cyclotomic companion blocks.

## 1. Setup

For an integer matrix (A\in M_d(\mathbb Z)), let
\[
\chi_A(x)=\det(xI-A)\in\mathbb Z[x].
\]
Write \(\bar A_p\) and \(\bar\chi_{A,p}\) for reduction modulo a prime (p). Define the spectral eigenprime set
\[
\mathcal E(A)=\{p:\bar\chi_{A,p}\text{ has a root in }\mathbb F_p\}.
\]
This means that \(\bar A_p\) has an eigenvalue over its ground field \(\mathbb F_p\), not merely over an extension field.

For each \(p\), define the **spectral fingerprint**
\[
\mathrm{SF}_p(A)=
\left(
\bar\chi_{A,p}=\prod_i f_i(x)^{e_i},
\quad
\{(\lambda,\dim_{\mathbb F_p}\ker(\bar A_p-\lambda I)):\lambda\in\mathbb F_p,\ \bar\chi_{A,p}(\lambda)=0\}
\right),
\]
where the first component is the complete factorization into distinct monic irreducibles. The second component records the geometric eigenspace dimensions of the linear roots.

The fingerprint is invariant under similarity over \(\mathbb F_p\). It intentionally records both algebraic and geometric data: root multiplicity alone does not determine eigenspace dimension.

## 2. Cyclotomic eigenprime criterion (G-EP1)

Let \(m\ge 2\), and let \(C_m\) be the companion matrix of the cyclotomic polynomial \(\Phi_m(x)\). Write
\[
m=p^a n,\qquad a\ge0,\qquad (p,n)=1.
\]
Then
\[
\boxed{p\in\mathcal E(C_m)\iff n\mid p-1.}
\]

**Proof.** If \(a=0\), the roots of \(\Phi_m\) are primitive \(m\)-th roots of unity. Since \(\mathbb F_p^\times\) is cyclic of order \(p-1\), such a root lies in \(\mathbb F_p\) exactly when \(m\mid p-1\).

If \(a>0\), reduction modulo \(p\) gives
\[
\overline{\Phi_{p^a n}}=\overline{\Phi_n}^{\,\varphi(p^a)}.
\]
The roots are therefore precisely the primitive \(n\)-th roots in an algebraic closure, with multiplicity. A primitive \(n\)-th root belongs to \(\mathbb F_p\) exactly when \(n\mid p-1\). This includes \(n=1\), where the root is 1. QED.

For \(p\nmid m\), the stronger **primitive eigenvalue** condition (an eigenvalue of exact multiplicative order \(m\)) is equivalent to \(p\equiv1\pmod m\). Its prime set has Dirichlet density \(1/\varphi(m)\), by the prime number theorem for arithmetic progressions. This density statement concerns primitive eigenprimes, not the larger spectral eigenprime set; adding the finitely many ramified primes does not change the density.

## 3. Direct sums: union of eigenprime sets

Let
\[
A=\bigoplus_{j=1}^r C_{m_j}^{\oplus a_j},
\qquad a_j\ge1.
\]
Then
\[
\chi_A(x)=\prod_{j=1}^r\Phi_{m_j}(x)^{a_j}
\]
and
\[
\boxed{\mathcal E(A)=\bigcup_{j=1}^r\mathcal E(C_{m_j}).}
\]
Equivalently, with \(m_j=p^{b_j}n_j\) and \((p,n_j)=1\),
\[
p\in\mathcal E(A)\iff \text{there exists }j\text{ with }n_j\mid p-1.
\]

This follows because a product of polynomials over a field has a root if and only if at least one factor has a root. The exponents \(a_j\) do not change the set of eigenprimes.

## 4. Multiplicity bookkeeping and the collision rule

For a linear root \(\lambda\in\mathbb F_p\), its algebraic multiplicity in \(\bar\chi_{A,p}\) is
\[
\operatorname{am}_p(\lambda)
=\sum_j a_j\,\operatorname{mult}_{\lambda}(\overline{\Phi_{m_j}}).
\]
This formula automatically handles collisions: different cyclotomic indices can reduce to polynomials sharing a linear factor modulo \(p\).

For the displayed direct sum of companion blocks, each individual companion block contributes a one-dimensional eigenspace whenever \(\lambda\) is one of its roots. Hence
\[
\dim\ker(A_p-\lambda I)
=\sum_j a_j\,\mathbf 1_{\{\overline{\Phi_{m_j}}(\lambda)=0\}}.
\]
This is a special property of a direct sum of companion blocks. For an arbitrary matrix with the same characteristic polynomial, the geometric multiplicity must be computed as a nullity; it cannot be recovered from the characteristic polynomial alone.

## 5. The quarter-turn example

Take
\[
J=C_4=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad \chi_J(x)=x^2+1.
\]

- If \(p\equiv1\pmod4\), the polynomial splits into two distinct linear factors, so there are two eigenvalues and each eigenspace has dimension one.
- If \(p\equiv3\pmod4\), it is irreducible, so there is no eigenvalue in \(\mathbb F_p\).
- If \(p=2\), it becomes \((x+1)^2\). The eigenvalue 1 has algebraic multiplicity two but eigenspace dimension one.

Thus \(\mathcal E(J)=\{2\}\cup\{p:p\equiv1\pmod4\}\), while its primitive eigenprimes are exactly \(p\equiv1\pmod4\).

## 6. Practical computation

For a concrete integer matrix and prime \(p\):

1. Reduce its entries modulo \(p\).
2. Compute and factor its characteristic polynomial over \(\mathbb F_p\).
3. Retain the linear factors \(x-\lambda\).
4. For each such \(\lambda\), compute the rank of \(A_p-\lambda I\); the eigenspace dimension is \(d-\operatorname{rank}(A_p-\lambda I)\).
5. Store the factorization, root multiplicities, and nullities as the fingerprint.

For a cyclotomic companion family, Step 2 can be partly replaced by the theorem in Sections 2–4, avoiding a full characteristic-polynomial computation when only the eigenprime set is needed.

## 7. Lean / software formalization target

A small formalization should separate:

- the integer cyclotomic polynomial and its companion matrix;
- reduction of coefficients into \(\mathrm{ZMod}\ p\);
- the criterion \(p\mid m\) decomposition \(m=p^a n\);
- the finite-field fact that \(\mathbb F_p^\times\) is cyclic;
- the root-existence theorem above;
- matrix nullity as the geometric multiplicity.

The first executable test matrix should be the quarter-turn \(J\), followed by indices \(m\in\{3,4,5,6,8,12\}\). A test suite should include ramified cases, especially \((m,p)=(4,2),(3,3),(5,5)\), as well as split and inert cases.

**Not yet claimed:** this note does not claim a Lean proof, a compiled formalization, or a completed repository test run. The theorem above is a mathematical result; the formalization and code remain implementation work.
