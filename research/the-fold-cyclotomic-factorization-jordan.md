# G-EP4 — Cyclotomic factorization and Jordan structure

**Status:** proved, using the finite-field factorization theorem and the cyclicity of companion matrices.  
**Depends on:** G-EP1, G-EP2.

## 1. Unramified factorization

Let \(m\ge2\), let \(p\) be prime, and suppose \(p\nmid m\). Write
\[
d=\operatorname{ord}_m(p),
\]
the multiplicative order of \(p\) in \((\mathbb Z/m\mathbb Z)^\times\).

Then
\[
\boxed{
\overline{\Phi_m}(x)=f_1(x)\cdots f_s(x),\quad
s=\frac{\varphi(m)}d,\quad \deg f_i=d,
}
\]
where the \(f_i\) are distinct monic irreducible polynomials over \(\mathbb F_p\).

**Reason.** The roots are the primitive \(m\)-th roots \(\zeta\). Frobenius sends \(\zeta\mapsto\zeta^p\); the orbit length is the least positive \(d\) for which \(\zeta^{p^d}=\zeta\), equivalently \(p^d\equiv1\pmod m\). Every Frobenius orbit therefore has size \(\operatorname{ord}_m(p)\), and irreducible factors correspond to these orbits.

It follows that \(\overline{\Phi_m}\) is square-free. Thus the companion matrix \(C_m\) is diagonalizable over \(\overline{\mathbb F}_p\), with exactly \(\varphi(m)\) distinct eigenvalues there. Its eigenvalues all lie in \(\mathbb F_{p^d}\), and \(d\) is the smallest extension degree over which any primitive \(m\)-th root can occur.

## 2. Ramified factorization

Suppose \(p\mid m\), and write
\[
m=p^a n,\qquad a\ge1,\quad (p,n)=1.
\]
The reduction identity is
\[
\overline{\Phi_m}(x)=\overline{\Phi_n}(x)^e,
\qquad e=\varphi(p^a)=p^{a-1}(p-1).
\]

If \(n>1\), set \(d=\operatorname{ord}_n(p)\). Then
\[
\boxed{
\overline{\Phi_m}(x)=
\left(f_1(x)\cdots f_s(x)\right)^e,
\quad s=\frac{\varphi(n)}d,
\quad \deg f_i=d,
}
\]
with distinct monic irreducible \(f_i\in\mathbb F_p[x]\). If \(n=1\), then \(\overline{\Phi_m}(x)=(x-1)^e\).

Thus every geometric root has algebraic multiplicity exactly \(e\). The set of roots is the set of primitive \(n\)-th roots (or just \(1\) when \(n=1\)).

## 3. Jordan theorem for the companion operator

**Theorem (G-EP4).** Over the algebraic closure \(\overline{\mathbb F}_p\), the Jordan form of \(C_m\) is:

- If \(p\nmid m\), one \(1\times1\) Jordan block for each primitive \(m\)-th root. In particular, \(C_m\) is diagonalizable.
- If \(m=p^a n\) with \(a\ge1\) and \((p,n)=1\), one Jordan block of size \(e=\varphi(p^a)\) for each primitive \(n\)-th root. For \(n=1\), this is one block of size \(e\) at eigenvalue 1.

**Proof.** A companion matrix is cyclic: its minimal polynomial equals its characteristic polynomial. For a cyclic operator, each primary factor \((x-\lambda)^e\) contributes exactly one Jordan block of size \(e\) over the algebraic closure. Apply the square-free and repeated-factor descriptions in Sections 1 and 2. QED.

A useful consequence is
\[
\dim\ker(C_m-\lambda I)=1
\]
for every eigenvalue \(\lambda\) over the algebraic closure, even in the ramified case. The algebraic multiplicity can be \(e>1\), but the geometric multiplicity remains one.

## 4. Examples

### Quarter-turn: \(m=4\)

- \(p\equiv1\pmod4\): \(d=1\); two distinct linear factors and two size-1 Jordan blocks.
- \(p\equiv3\pmod4\): \(d=2\); one irreducible quadratic, no eigenvalue over \(\mathbb F_p\), but two eigenvalues over \(\mathbb F_{p^2}\).
- \(p=2\): \(m=2^2\), so \(e=\varphi(4)=2\); \(\overline{\Phi_4}=(x+1)^2\), one Jordan block of size 2.

### Fifth roots: \(m=5\)

- \(p=2\): \(\operatorname{ord}_5(2)=4\); one irreducible factor of degree 4.
- \(p=11\): \(\operatorname{ord}_5(11)=1\); four distinct linear factors.
- \(p=5\): \(e=\varphi(5)=4\); \(\overline{\Phi_5}=(x-1)^4\), one Jordan block of size 4.

## 5. Scope: companion matrices versus arbitrary matrices

The characteristic polynomial determines the algebraic multiplicities and the eigenvalues, but it does not determine Jordan block sizes for an arbitrary matrix. The Jordan conclusion in Section 3 uses the cyclicity of the specific companion matrix.

For a general Fold operator \(A\), the correct extension is to record, for every eigenvalue \(\lambda\), the sequence
\[
\dim\ker(A-\lambda I),\quad
\dim\ker(A-\lambda I)^2,\quad
\dim\ker(A-\lambda I)^3,\ldots
\]
The successive differences recover the number of Jordan blocks of size at least each given length. This is strictly richer than the characteristic polynomial and the ordinary eigenspace dimension.

## 6. Formalization and implementation target

The unramified factor-degree theorem is already represented in Mathlib's cyclotomic finite-field factorization API. A Lean development should first reuse that theorem rather than reproving Frobenius-orbit theory.

The new formalization work is:
1. connect coefficient reduction of integer cyclotomic polynomials to the finite-field cyclotomic polynomial;
2. formalize the ramified reduction identity;
3. prove the cyclic companion-matrix lemma that each primary factor contributes one Jordan block;
4. expose the resulting factorization and Jordan data in the spectral fingerprint.

No Lean build or executable test is claimed by this research note.
