# The Fold — Composition-excess resonance and sign classification (G-EP194–G-EP198)

Throughout, \(Q\) is a prime-power field size, \(I_Q(n)\) is the number of monic irreducibles of degree \(n\), \(R_Q(n)=nI_Q(n)/Q^n\), and \(E_Q(n)=1-R_Q(n)\). For \(n>1\), let \(q(n)\) be its smallest prime divisor and
\[
A(n)=n\left(1-\frac1{q(n)}\right).
\]
The maximal proper-subfield term gives
\[
E_Q(n)=Q^{-A(n)}+\text{terms of strictly higher exponent}.
\]
For pairwise-coprime \(n_1,\ldots,n_r>1\), write \(N=\prod_i n_i\) and
\[
H_Q(n_1,\ldots,n_r)=E_Q(N)-\prod_i E_Q(n_i).
\]

## G-EP194 — Complete two-factor resonance classification

Label the factors so \\(q(a)<q(b)\\), where \\(q(n)\\) is the smallest prime divisor; no ordering by numerical size is required. Then \\(A(ab)=bA(a)\\), while the product \\(E_Q(a)E_Q(b)\\) begins at exponent \\(A(a)+A(b)\\).

If \(A(ab)=A(a)+A(b)\), then
\[
(b-1)A(a)=A(b)<b.
\]
If \(a\ge3\), then \(A(a)\ge2\), so the left side is at least \(2(b-1)\ge b\), impossible. Hence \(a=2\), and equality becomes \(b-1=A(b)=b(1-1/q(b))\), equivalent to \(q(b)=b\), i.e. \(b\) is prime. Therefore
\[
\boxed{A(ab)=A(a)+A(b)\iff (a,b)=(2,\ell),\quad \ell\text{ an odd prime}.}
\]
This classifies every two-factor leading resonance.

## G-EP195 — Exact resolution of every resonant pair

For an odd prime \(\ell\), the squarefree-divisor formula gives
\[
E_Q(2\ell)=Q^{-\ell}+Q^{-2\ell+2}-Q^{-2\ell+1},
\]
while \(E_Q(2)E_Q(\ell)=Q^{-1}Q^{-(\ell-1)}=Q^{-\ell}\). Thus
\[
\boxed{H_Q(2,\ell)=Q^{-(2\ell-2)}-Q^{-(2\ell-1)}>0.}
\]
The first surviving exponent/coefficient pair is exactly \((2\ell-2,+1)\), followed by \((2\ell-1,-1)\). This recovers \(Q^{-4}-Q^{-5}\) for \((2,3)\) and gives an infinite family of exact positive examples.

## G-EP196 — Complete eventual-sign classification for two factors

For coprime \(a,b>1\):
- If \((a,b)=(2,\ell)\) with \(\ell\) an odd prime, the leading terms resonate and G-EP195 gives positive \(H_Q\) exactly.
- In every other case, \(A(ab)>A(a)+A(b)\). The product term is then the first surviving contribution, with coefficient \(-1\), so \(H_Q\) is negative for all sufficiently large \(Q\).

This is an eventual sign statement, not a claim that the negative sign holds for every small field size. The exact spectrum decides finite-\(Q\) behavior when needed.

## G-EP197 — No leading resonance with three or more factors

Let \(r\ge3\), choose \(n_1\) whose smallest prime divisor is the smallest among all factors, and put \(M=\prod_{i=2}^r n_i\). Then
\[
A(N)=M A(n_1),\qquad A(n_1)\ge1.
\]
For pairwise-coprime integers \(n_i>1\), one has \(M-1\ge\sum_{i=2}^r n_i\), with equality possible only for the two-number set \(\{2,3\}\). Since \(A(n_i)<n_i\),
\[
(M-1)A(n_1)\ge M-1\ge\sum_{i=2}^r n_i>
\sum_{i=2}^r A(n_i).
\]
Consequently
\[
\boxed{A(N)>\sum_{i=1}^r A(n_i)\quad(r\ge3).}
\]
There is no leading-exponent resonance for three or more pairwise-coprime factors. The product \(\prod_i E_Q(n_i)\) dominates the first term, and
\[
H_Q(n_1,\ldots,n_r)\sim- Q^{-\sum_i A(n_i)}.
\]
Thus the multi-factor excess is eventually negative whenever there are at least three factors, independently of the finite-field order.

## G-EP198 — Unified phase rule and executable certificate

The large-field sign is determined by the first-exponent comparison:
\[
\begin{array}{c|c}
A(N)<\sum_i A(n_i)&H_Q\text{ has positive leading term }+Q^{-A(N)}\\
A(N)>\sum_i A(n_i)&H_Q\text{ has negative leading term }-Q^{-\sum_i A(n_i)}\\
A(N)=\sum_i A(n_i)&\text{collect exact integer coefficients; the first survivor decides}
\end{array}
\]
For pairwise-coprime inputs, the equality row occurs exactly for two factors \((2,\ell)\) with \(\ell\) an odd prime; G-EP195 resolves it positively. All other two-factor cases and every case with at least three factors are eventually negative. The new function coprime_composition_excess_asymptotic(degrees) reports the exponent comparison, eventual regime, leading exponent/coefficient after cancellation, and (only in the resonant case) the exact spectrum.

The regression tests include odd-prime resonance fixtures, composite odd controls, pairs with both degrees at least three, and three-/four-factor cases. Tests are finite implementation checks; the proofs above establish the stated general classifications.
