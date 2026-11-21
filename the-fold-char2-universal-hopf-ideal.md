# UF-044 — The universal Hopf-ideal characterization of the normal closure

Work over an algebraically closed field k of characteristic two. Let \(\mathscr A\) be the full automorphism group scheme of \(C=k[x,z]/(x^4,z^2)\), with coordinate Hopf algebra \(A=k[\mathscr A]\). Let \(I_U\subset A\) be the defining ideal of the flat seven-dimensional subgroup \(U\).

## Theorem UF-044.1 — Exact maximal-ideal characterization

The scheme-theoretic normal closure \(\mathscr K\) of U is defined by the largest Hopf ideal \(J\) satisfying both
\[
J\subseteq I_U
\]
and the conjugation-stability condition
\[
\boxed{\operatorname{Ad}^*(J)\subseteq A\otimes J,}
\]
where \(\operatorname{Ad}:\mathscr A\times\mathscr A\to\mathscr A\) is conjugation, \((g,h)\mapsto ghg^{-1}\), and \(\operatorname{Ad}^*:A\to A\otimes A\) is its pullback (the first tensor factor is the conjugating group coordinate).

Equivalently, \(J\) is the sum of all Hopf ideals contained in \(I_U\) that are stable under the conjugation coaction. This sum is itself a Hopf ideal, is still contained in \(I_U\), and is conjugation-stable. Thus it is the unique largest such ideal. The corresponding closed subgroup is the smallest closed normal subgroup scheme containing U.

**Proof.** A closed subgroup scheme \(H\subseteq\mathscr A\) corresponds contravariantly to a Hopf ideal \(I(H)\subseteq A\). The inclusion \(U\subseteq H\) is equivalent to \(I(H)\subseteq I_U\). Normality of H is equivalent to stability of its ideal under the conjugation coaction. Sums of Hopf ideals are Hopf ideals, and sums of conjugation-stable ideals remain conjugation-stable. Hence the sum of all normal Hopf ideals contained in \(I_U\) is the largest one, and its subgroup is the smallest normal subgroup scheme containing U. \(\square\)

## 2. Why this is stronger than imposing equations on conjugates

The universal conjugation map is
\[
\operatorname{Ad}:\mathscr A\times\mathscr A\to\mathscr A,
\qquad(g,h)\mapsto ghg^{-1}.
\]
For any candidate ideal J, the inclusion
\[
\operatorname{Ad}^*(J)\subseteq A\otimes J
\]
must hold as an identity in the full coordinate algebra, including the nilpotent coefficients \(c,d,h\) with \(c^4=d^2=h^2=0\). Checking only field-valued points discards these directions. Checking only the tangent representation verifies only the linearized condition and cannot determine the higher-order ideal.

The characterization therefore gives a finite algebraic target: find the largest Hopf ideal inside \(I_U\) satisfying the coaction inclusion. It avoids the incorrect shortcut of equating matching reduced support and tangent dimension with equality of subgroup schemes.

## 3. Bounds inherited from UF-039 and UF-043

The preceding results give
\[
\mathscr K_{\mathrm{red}}=N,
\qquad
\operatorname{Lie}(\mathscr K)=\operatorname{Lie}(\mathscr A),
\]
while UF-043 constructs a normal candidate \(\mathscr K_2\) with
\[
\mathscr K\subseteq\mathscr K_2.
\]
In ideal language, writing \(J=I(\mathscr K)\) and \(J_2=I(\mathscr K_2)\), this is
\[
\boxed{J_2\subseteq J\subseteq I_U.}
\]
The radical of J is the ideal of N. The tangent-space equality says that at the identity the linear parts of J vanish in all 16 ambient tangent directions; it does not determine the quadratic and higher terms of J.

## 4. Computational reduction

A valid symbolic computation should proceed in the following order:

1. Write the full coordinate algebra A with the relations \(c^4=d^2=h^2=0\) and the invertibility localization \((ai-bh)^{-1}\).
2. Express the embedding U→A and obtain its full ideal \(I_U\), not just its three equations inside the reduced identity-linear subgroup H.
3. Compute the Hopf structure and conjugation coaction on generators of A.
4. Start with the candidate ideal \(J_2\), then test whether it is contained in \(I_U\) and whether \(\operatorname{Ad}^*(J_2)\subseteq A\otimes J_2\). (The known normality of the Frobenius-kernel preimage predicts this inclusion.)
5. To prove minimality, show that every conjugation-stable Hopf ideal \(J\subseteq I_U\) contains \(J_2\), or produce a strictly larger such ideal to disprove equality. Tangent-space calculations alone cannot do this.

The universal coaction calculation is substantially larger than the existing GF(2) Lie-bracket verifier: it must retain polynomial coefficients and nilpotent orders up to the ambient relations. A finite-field point search is useful only for finding counterexamples, not for proving the required polynomial identity.

## 5. Status and next problem

**UF-044 establishes the exact universal algebraic characterization, but does not compute the maximal ideal J.** In particular, it does not prove \(\mathscr K=\mathscr K_2\). That equality remains open.

**UF-045:** implement the full coordinate Hopf algebra and conjugation coaction, then test the UF-043 ideal symbolically. First settle whether the quotient coordinate functions \(F,R\) extend as explicit regular functions on the full non-reduced automorphism scheme, and record their pullbacks. This is a prerequisite for a reliable generator-level coaction calculation.
