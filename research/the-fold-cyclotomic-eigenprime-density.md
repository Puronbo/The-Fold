# G-EP3 — Density of finite cyclotomic eigenprime families

**Status:** proved, conditional only on the standard prime number theorem for arithmetic progressions.  
**Depends on:** G-EP1 / G-EP2.

## 1. The finite-family problem

Fix integers \(m_1,\ldots,m_r\ge2\), and form a direct sum of cyclotomic companion blocks
\[
A=\bigoplus_{j=1}^r C_{m_j}^{\oplus a_j},\qquad a_j\ge1.
\]
The multiplicities \(a_j\) do not affect the eigenprime set. By G-EP1, outside the finite set of primes dividing \(M=\prod_jm_j\), we have
\[
p\in\mathcal E(A)
\iff p\equiv1\pmod{m_j}\text{ for at least one }j.
\]
Thus the infinite part of the eigenprime set is a finite union of prime arithmetic progressions.

Set
\[
L=\operatorname{lcm}(m_1,\ldots,m_r).
\]
Every relevant prime is in the reduced residue classes modulo \(L\). Define
\[
R=\{a\in(\mathbb Z/L\mathbb Z)^\times:
a\equiv1\pmod{m_j}\text{ for some }j\}.
\]

## 2. Density theorem

**Theorem (G-EP3).** The spectral eigenprime set of \(A\) has Dirichlet density
\[
\boxed{\delta(A)=\frac{|R|}{\varphi(L)}.}
\]
Equivalently,
\[
\boxed{
\delta(A)=
\sum_{\varnothing\ne S\subseteq\{1,\ldots,r\}}
\frac{(-1)^{|S|+1}}
{\varphi(\operatorname{lcm}_{j\in S}m_j)}.
}
\]

**Proof.** For each index \(j\), let \(P_j\) be the set of primes in the progression \(p\equiv1\pmod{m_j}\). By the prime number theorem for arithmetic progressions, \(P_j\) has Dirichlet density \(1/\varphi(m_j)\). For any nonempty subset \(S\), the intersection is exactly the primes satisfying
\[
p\equiv1\pmod{\operatorname{lcm}_{j\in S}m_j},
\]
and so has density the reciprocal of the corresponding totient. Finite inclusion–exclusion gives the displayed sum. The actual spectral eigenprime set differs from \(\bigcup_jP_j\) by at most primes dividing \(M\), by G-EP1. A finite symmetric difference does not change Dirichlet density. QED.

The residue-class formula follows because all these progressions are unions of reduced residue classes modulo \(L\), each of which has density \(1/\varphi(L)\).

## 3. Example: indices 4 and 6

For \(m_1=4,m_2=6\), the common modulus is \(L=12\). Among the four reduced residue classes \(1,5,7,11\pmod{12}\), the eigenprime classes are
\[
1\pmod4:\{1,5\},\qquad
1\pmod6:\{1,7\}.
\]
Their union is \(\{1,5,7\}\), hence
\[
\delta=\frac34.
\]
Equivalently,
\[
\delta=\frac1{\varphi(4)}+\frac1{\varphi(6)}
-\frac1{\varphi(12)}
=\frac12+\frac12-\frac14=\frac34.
\]
This illustrates why simply summing the individual densities is wrong: the intersection progression \(p\equiv1\pmod{12}\) must be subtracted once.

## 4. What the density does and does not measure

- It measures the asymptotic frequency of primes for which at least one block has an eigenvalue over its ground field.
- It is unchanged by repeating a block, since multiplicity does not change root existence.
- It is unchanged by adding or removing finitely many ramified primes.
- It does not measure the number of eigenvalues, their multiplicities, or eigenspace dimensions. Those are the prime-by-prime data in the G-EP2 spectral fingerprint.
- It does not assert that every eigenvalue has exact order \(m_j\) at a ramified prime. Exact order is the unramified, primitive-eigenvalue notion.

## 5. Computational consequence

For a fixed finite index set, compute \(L\), enumerate the units modulo \(L\), and count those satisfying at least one congruence \(a\equiv1\pmod{m_j}\). This gives an exact integer numerator and denominator \(|R|/\varphi(L)\), with no prime sampling and no floating-point approximation.

An implementation should reduce the fraction by a gcd and separately report the exceptional ramified prime set \(\{p:p\mid M\}\). The density itself is exact; finite-prime membership should still be tested with the full G-EP1 criterion, not inferred from the unramified congruence union.
