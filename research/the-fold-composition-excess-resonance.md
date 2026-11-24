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


## G-EP199 — Exact finite-field signs with an explicit threshold

The asymptotic phase rule gives the eventual sign, but a finite field may lie below a convenient analytic threshold. The full exponent spectrum resolves the exact value:
[
H_Q=sum_{j=0}^{s}c_jQ^{-e_j},qquad
e_0<e_1<cdots<e_s,quad c_0
e0.
]
Let (L=sum_{j=1}^{s}|c_j|). For (Qge2),
[
left|sum_{j=1}^{s}c_jQ^{-(e_j-e_0)}ight|
le rac{L}{Q}.
]
Therefore, whenever (Q>L/|c_0|), the tail is strictly smaller than the leading coefficient and the exact sign is the sign of (c_0). An integer threshold is
[
oxed{Q_0=maxleft(2,leftlfloorrac{L}{|c_0|}ightfloor+1ight).}
]
This is a sufficient threshold, not necessarily the smallest threshold.

The new `coprime_composition_excess_sign_certificate(degrees, field_size)` API returns the exact rational value and sign at the requested prime-power field size, the full spectrum, and this guaranteed eventual threshold. It separates two questions that must not be conflated: the exact sign at one finite field, and the sign valid uniformly for every prime-power field size above a proven bound.

Examples:
- (H_Q(2,3)=Q^{-4}-Q^{-5}>0), with (Q_0=2).
- (H_Q(3,4)=-Q^{-4}+Q^{-6}+Q^{-8}-Q^{-10}<0); the simple coefficient-tail certificate gives (Q_0=4), although the exact spectrum can show negativity at smaller field sizes too.

The threshold follows from a triangle-inequality bound and is intentionally conservative. Finding the optimal threshold for each degree tuple is a separate exact inequality problem.


## G-EP200 — Optimal integer sign threshold below the analytic tail bound

G-EP199 supplied a simple coefficient-norm threshold. We can sharpen it without weakening the proof. Let (Q_0^{\mathrm{tail}}) be that certified bound. Every integer (Q\ge Q_0^{\mathrm{tail}}) has the leading-coefficient sign. Therefore only the finite interval (2\le Q<Q_0^{\mathrm{tail}}) remains to inspect.

The implementation evaluates the exact rational spectrum at every integer in that interval, records the last integer whose sign is zero or differs from the eventual sign, and returns
[
\boxed{Q_0^{\mathrm{int}}=\max(2,1+\max\{Q<Q_0^{\mathrm{tail}}:
\operatorname{sgn}H_Q\ne\operatorname{sgn}(c_0)\})}.
]
If the exceptional set is empty, the maximum convention gives threshold 2. This is the **smallest integer threshold** such that every integer (Q\ge Q_0^{\mathrm{int}}) has the eventual sign. It is consequently also optimal when restricted to prime-power field sizes, though the smallest prime-power-only threshold could be lower.

The API now returns both `sufficient_field_size_threshold` (the short analytic bound) and `smallest_integer_threshold` (the exact sharpened bound). For the examples ((2,3)) and ((3,4)), both thresholds are 2. The scan is finite and exact; the infinite tail remains certified by G-EP199. No unbounded numerical search is involved.

---

## G-EP201 — Exact global sign certificates by Sturm theory

For the Laurent spectrum

\\[ H_Q=\\sum_j c_jQ^{-e_j}, \\]

put \\(x=1/Q\\), let \\(e_0\\) be the smallest exponent, and form

\\[ H_Q=x^{e_0}P(x),\\qquad P(x)=\\sum_jc_jx^{e_j-e_0}. \\]

Since \\(x^{e_0}>0\\), the sign for every real \\(Q\\ge2\\) is the sign of
\\(P\\) on \\(0<x\\le1/2\\).

The new API `coprime_composition_excess_global_sign_certificate(degrees)`
constructs the integer polynomial exactly, builds its Sturm sequence over
\\(\\mathbb Q\\), and counts roots in the open interval \\((0,1/2)\\).
One-sided endpoint signs are evaluated exactly, and \\(P(1/2)=0\\) is
checked separately. A zero root count together with a nonzero endpoint
value certifies that the polynomial has no zero anywhere on
\\((0,1/2]\\); continuity then makes its sign equal to its nonzero
constant coefficient.

Regression fixtures certify:
- \\((2,3)\\): \\(P(x)=1-x\\), globally positive.
- \\((3,4)\\): \\(P(x)=-(1-x^2)(1-x^4)\\), globally negative.
- Multi-factor tuples \\((2,3,5)\\), \\((2,5,9)\\), and \\((3,5,7)\\):
  exact Sturm root count zero and globally negative.

This is a proof certificate for each supplied tuple, not a universal
theorem that every admissible tuple has the eventual sign for all
\\(Q\\ge2\\). A positive Sturm root count is an obstruction to this
simple global-sign claim and should trigger exact root isolation or
integer-field-size analysis; it does not contradict the eventual-sign
theorems. Regression tests have been added but are not reported as
executed here.


---

## G-EP202 — Exact temporal composition-excess folding

Given three chronological pairwise-coprime degree tuples
\\(\\mathbf n_{t-2},\\mathbf n_{t-1},\\mathbf n_t\\), let
\\(H_{t-i}(Q)\\) denote their exact composition-excess Laurent spectra.
The temporal second difference is

\\[
K_t(Q)=H_t(Q)-2H_{t-1}(Q)+H_{t-2}(Q).
\\]

After aligning equal exponents, its coefficient is

\\[
k_e=c_{t,e}-2c_{t-1,e}+c_{t-2,e}.
\\]

The new API
`coprime_composition_excess_temporal_fold(two_steps_ago, one_step_ago, present)`
computes this operation using integer coefficients, removes exact cancellations,
and explicitly represents the zero polynomial. It does not sample field sizes
or infer a sign numerically.

The regression example uses chronological tuples \\((2,3),(3,4),(2,3)\\).
The resulting spectrum is
\\[
4Q^{-4}-2Q^{-5}-2Q^{-6}-2Q^{-8}+2Q^{-10}.
\\]
Three identical tuples produce the zero polynomial, as expected from zero
second difference. The zero result means coefficient-wise affine evolution
across these three snapshots; it does not imply the underlying tuple sequence
is globally affine or that future states will remain so.

This operation is a spectral transformation, not yet a recurrence theorem.
Its output can be passed to polynomial sign analysis after the generic
Laurent-polynomial certificate interface is separated from the current
degree-tuple API.


---

## G-EP203 — Generic exact sign certification for Laurent spectra

The G-EP201 Sturm certificate was initially exposed through the degree-tuple
composition-excess API. G-EP203 extracts the mathematical operation into the
generic API
`laurent_spectrum_global_sign_certificate(spectrum)`, so it can certify
composition spectra, temporal folds, and other finite integer Laurent
spectra without requiring their origin to be a degree tuple.

Input terms are integer pairs \\( (e,c) \\), represented as dictionaries
with `exponent` and `coefficient`. Exponents may be negative, zero, or
positive. Duplicate exponents are combined; zero coefficients are removed.
If all terms cancel, the API reports the identically zero Laurent polynomial
rather than assigning it a sign.

For a nonzero spectrum, let \\(e_0\\) be its smallest exponent and put
\\[
H(Q)=\\sum_e c_eQ^{-e}
=x^{e_0}P(x),\\qquad x=1/Q.
\\]
The factor \\(x^{e_0}\\) is positive for \\(x>0\\), even when
\\(e_0\\) is negative. The exact rational Sturm sequence for \\(P\\)
counts distinct roots on \\(0<x<1/2\\), while an exact endpoint evaluation
checks \\(x=1/2\\). No roots in \\(0<x\\le1/2\\) certify the sign
for every real \\(Q\\ge2\\).

The new tests cover:
- Direct global-sign certification of the G-EP202 temporal fold.
- A polynomial with a root inside the interval.
- A root exactly at the endpoint corresponding to Q=2.
- Duplicate-exponent combination and complete cancellation.
- Negative Laurent exponents and malformed input.

The certificate is exact and tuple-independent, but it remains a
per-polynomial result. A failed certificate does not prove sign change; it
means this root-free criterion did not establish a global sign.
