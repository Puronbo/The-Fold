# G-EP172 — Outward workload scaling and inward irreducible density

## Question

How does the weight

\[
w(n)=\frac{n}{n^n}=n^{1-n}
\]

behave when we move outward across field size and degree, and inward from the
entire polynomial space to the irreducible members?

The two directions answer different questions and must not be conflated.

## Outward: the full search space

There are exactly

\[
N(p,n)=p^n
\]

monic degree-\(n\) polynomials over \(\mathbb F_p\). Applying the proposed
weight gives

\[
W(p,n)=N(p,n)w(n)=n\left(\frac pn\right)^n.
\]

For fixed degree, \(W(p,n)\) grows as \(p^n\) when the field grows. Thus
\(w(n)\) does not normalize across field sizes: it is independent of \(p\).

For fixed prime \(p\), adjacent degrees obey the exact ratio

\[
\frac{W(p,n+1)}{W(p,n)}
=\frac pn\left(\frac{n}{n+1}\right)^n.
\]

Consequently the weighted sequence increases from degree \(n\) to \(n+1\)
exactly when

\[
p>n\left(1+\frac1n\right)^n.
\]

The threshold on the right tends to \(en\). This locates the turning region
near \(n\approx p/e\), but the exact integer comparison above, not the
approximation, decides each step. For fixed \(p\), the weighted quantity
eventually decreases and tends to zero. This is a property of the chosen
weight, not of the actual enumeration workload, which continues to grow as
\(p^n\).

## Inward: the irreducible part of the space

Let \(I_p(n)\) be the number of monic irreducible degree-\(n\) polynomials
over \(\mathbb F_p\). The exact finite-field counting formula is

\[
I_p(n)=\frac1n\sum_{d\mid n}\mu(d)p^{n/d},
\]

where \(\mu\) is the Möbius function. Dividing by the full monic domain gives
the exact irreducible density

\[
\rho_p(n)=\frac{I_p(n)}{p^n}
=\frac1n\sum_{d\mid n}\mu(d)p^{-n(1-1/d)}.
\]

The natural first-order normalization is therefore

\[
R_p(n)=n\rho_p(n)
=\frac{nI_p(n)}{p^n}
=\sum_{d\mid n}\mu(d)p^{-n(1-1/d)}.
\]

The divisor \(d=1\) contributes exactly one. Every other term tends to zero
as the degree grows, so for fixed prime \(p\),

\[
R_p(n)\longrightarrow 1,
\qquad
\rho_p(n)\sim\frac1n.
\]

This explains why multiplying the observed irreducible fraction by \(n\)
is a meaningful cross-degree normalization. It is fundamentally different
from multiplying the total workload by \(n/n^n\).

### First exact cases

- If \(n=1\), then \(I_p(1)=p\) and \(R_p(1)=1\).
- If \(n\) is prime, then
  \[
  I_p(n)=\frac{p^n-p}{n},\qquad R_p(n)=1-p^{1-n}.
  \]
- For \(n=4\), the divisors with nonzero Möbius value are 1 and 2, so
  \[
  I_p(4)=\frac{p^4-p^2}{4},\qquad R_p(4)=1-p^{-2}.
  \]
- For \(n=6\),
  \[
  I_p(6)=\frac{p^6-p^3-p^2+p}{6},\qquad
  R_p(6)=1-p^{-3}-p^{-4}+p^{-5}.
  \]

The correction terms depend on the divisor structure of \(n\), not merely
on its size. Prime degrees and composite degrees therefore approach the
limit through different exact correction patterns.

## Connecting the two directions

The two normalized quantities can be placed side by side:

\[
\underbrace{W(p,n)}_{\text{weighted total domain}}
=n\left(\frac pn\right)^n,
\qquad
\underbrace{R_p(n)}_{\text{normalized irreducible density}}
=\frac{nI_p(n)}{p^n}.
\]

The first is an imposed degree weight on computational workload. The second
is an exact arithmetic statistic whose limit is one for fixed \(p\).
They answer different questions:

1. How large does a weighted enumeration scale?
2. What fraction of all monic polynomials are irreducible, after correcting
   for the leading \(1/n\) density?

A useful audit extension is to report the observed irreducible count
\(\widehat I\), observed density \(\widehat I/p^n\), and normalized
density \(n\widehat I/p^n\) alongside predicate/factorizer agreement.
For a sample, these are sample statistics and must not be labeled exact
whole-domain counts. The exact formula above supplies an independent
mathematical benchmark; a production implementation should compare against
it without treating agreement between two software routines as a proof.

## Boundary

The formula for \(I_p(n)\) is an exact theorem. The asymptotic statement is
for fixed prime \(p\) as \(n\) grows. If \(p\) and \(n\) both vary, the
joint regime must be specified; no single-variable limit should be silently
reused. Likewise, \(W(p,n)\) is not runtime, and a sampled audit is not an
exhaustive count.


## G-EP173 implementation: theory alongside computation

The parameterized audit now computes the exact theoretical irreducible count
with an independent Möbius-function implementation:

\[
I_p(n)=\frac1n\sum_{d\mid n}\mu(d)p^{n/d}.
\]

It reports both observed and theoretical densities, and their degree-normalized
forms. It also reports the expected number of irreducibles in the checked
subset under uniform sampling:

\[
\mathbb E[X]=m\frac{I_p(n)}{p^n},
\]

where \(m\) is the number of distinct polynomials checked. This is an
expectation, not a prediction that the observed sample count must equal it.

When the checked set covers all \(p^n\) monic polynomials, the audit exposes
an exact theoretical_count_match boolean. For an incomplete sample that
field is null: the exact whole-domain count is still known from the formula,
but the sample's observed count cannot be compared to it as if it were a
complete enumeration. The schema is now
the-fold-irreducibility-audit-v2.

The tests include exact count fixtures (for example, six monic irreducible
quintics over F₂ and eighteen monic irreducible quartics over F₃), a
cross-field/degree formula grid, exhaustive agreement with the exact count,
and deterministic sampled-mode reporting.


## G-EP174 — Error structure and uniform convergence

Define the signed normalized-density error

\[
E_p(n)=1-R_p(n)=-\sum_{\substack{d\mid n\\d>1}}\mu(d)p^{-n(1-1/d)}.
\]

The divisor structure of the degree controls the correction terms. Only squarefree divisors contribute. If \(\omega(n)\) is the number of distinct prime factors of \(n\), there are exactly \(2^{\omega(n)}-1\) nontrivial squarefree divisors. For each such divisor, \(1-1/d\ge1/2\), hence

\[
|E_p(n)|\le(2^{\omega(n)}-1)p^{-n/2}\le(n-1)p^{-n/2}.
\]

Since every prime field has \(p\ge2\), this gives the uniform estimate

\[
\boxed{\sup_{p\text{ prime}}|R_p(n)-1|\le(n-1)2^{-n/2}\longrightarrow0.}
\]

This is stronger than pointwise convergence for each fixed field: the normalized irreducible density converges to one even if the prime field size is allowed to vary with the degree. The bound is intentionally conservative; the squarefree-divisor bound is often much sharper.

For odd degrees, every nontrivial divisor is at least three, so the same argument sharpens to

\[
|E_p(n)|\le(2^{\omega(n)}-1)p^{-2n/3}\qquad(n\text{ odd}, n>1).
\]

For prime degree, there is only one nontrivial Möbius divisor and the exact error is

\[
E_p(n)=p^{1-n}.
\]

Composite degrees have signed inclusion-exclusion corrections. For example,

\[
E_p(6)=p^{-3}+p^{-4}-p^{-5},
\]

whereas prime powers such as \(n=4\) have \(E_p(4)=p^{-2}\). The signs are inherited from the Möbius function; one should not assume a universal sign pattern from degree size alone.

### Executable audit

G-EP174 adds `irreducible_density_convergence(p, degree)`. It returns the exact rational normalized density and signed error as numerator/denominator pairs, the number of distinct prime factors, a squarefree-divisor bound, and the uniform prime-field bound. Its boolean bound check uses exact rational arithmetic (with a slightly relaxed rational envelope for odd degrees), not floating-point comparison.

Regression coverage includes prime and composite degree identities, invalid inputs, and a cross-grid over prime fields 2, 3, 5, 7, 11 and degrees 1 through 40. This validates the implementation against the theorem on a finite grid; the uniform convergence statement itself follows from the analytic bound above.


## G-EP175 — Prime factorization determines the leading correction

The normalized density has the finite expansion

\[
R_p(n)-1=\sum_{\substack{d\mid n\\d>1}}\mu(d)p^{-n(1-1/d)}.
\]

Write the distinct prime factors of \(n\) as
\(q_1<q_2<\cdots<q_k\). Only squarefree divisors contribute. The smallest
nontrivial squarefree divisor is \(q_1\), and its Möbius coefficient is
\(-1\). Therefore the leading correction, as the field size grows with the
degree fixed, is

\[
R_p(n)-1=-p^{-n(1-1/q_1)}+\text{remainder}.
\]

If \(k=1\), so \(n\) is a prime power, there is no remainder at all:

\[
\boxed{R_p(n)=1-p^{-n(1-1/q_1)}\quad(n=q_1^a).}
\]

This is a stronger structural observation than merely saying that prime
degrees have a simple formula: every prime-power degree has exactly one
nonzero Möbius correction, independent of the exponent \(a\) except through
the outer factor \(n\) in the exponent.

If \(k\ge2\), the smallest squarefree divisor after \(q_1\) is \(q_2\).
There are \(2^k-2\) remaining nontrivial squarefree divisors, each at least
\(q_2\). Since \(d\mapsto n(1-1/d)\) is increasing,

\[
\left|R_p(n)-1+p^{-n(1-1/q_1)}\right|
\le(2^k-2)p^{-n(1-1/q_2)}.
\]

Thus the smallest prime factor fixes the leading exponent, while the second
smallest prime factor controls a bound on the next-order remainder. The
number of distinct prime factors controls the number of terms in that
remainder. Prime-power exponents do not create new Möbius terms.

Examples:

- \(n=6=2\cdot3\): leading correction \(-p^{-3}\), remainder
  \(-p^{-4}+p^{-5}\).
- \(n=30=2\cdot3\cdot5\): leading correction \(-p^{-15}\); the next
  correction is \(-p^{-20}\), followed by the terms from divisors 6, 10,
  15, and 30.
- \(n=12=2^2\cdot3\): the same two distinct prime factors as 6, but the
  exponents scale with 12: leading correction \(-p^{-6}\), followed by
  \(-p^{-8}+p^{-10}\). The prime-power exponent on 2 adds no extra divisor.

### Executable audit

G-EP175 adds `irreducible_density_factorization(p, degree)`. It reports the
prime factorization, exact leading correction, exact residual correction,
and the second-prime-factor remainder bound using integer/rational
arithmetic. For prime-power degrees it marks the leading term as exact.
Tests include prime powers, representative products of distinct primes, and
a grid of prime fields 2, 3, 5, 7 against degrees 1 through 80. These finite
checks exercise the formula and bound; the result for all degrees follows
from the squarefree-divisor expansion.


## G-EP176 — Coprime degrees do not give multiplicative density

A natural composition conjecture is
\[
R_p(ab)\stackrel{?}{=}R_p(a)R_p(b),\qquad \gcd(a,b)=1.
\]
It fails, even for the smallest nontrivial coprime pair. Over \(\mathbb F_2\),
\[
R_2(2)=\frac12,\qquad R_2(3)=\frac34,
\]
so their product is \(3/8\). But
\[
R_2(6)=1-2^{-3}-2^{-4}+2^{-5}=\frac{27}{32},
\]
and therefore
\[
\boxed{R_2(6)-R_2(2)R_2(3)=\frac{15}{32}.}
\]
The failure is not a small asymptotic correction in this example.

The source is visible in the Möbius expansion:
\[
R_p(n)=p^{-n}\sum_{d\mid n}\mu(d)p^{n/d}.
\]
For coprime \(a,b\), every squarefree divisor of \(ab\) is a product of a squarefree divisor of \(a\) and one of \(b\). The Möbius signs therefore factor over the two prime-factor sets, but the exponent in the combined term is
\[
\frac{ab}{d_a d_b}=\frac{a}{d_a}\frac{b}{d_b},
\]
not the sum of the separate exponents \(a/d_a\) and \(b/d_b\). The outer normalization is also \(p^{-ab}\), not \(p^{-a-b}\). Thus the divisor indexing has a product structure, while the numerical weight does not separate into a product of one-variable weights.

### Exact composition audit

G-EP176 adds `irreducible_density_composition(p, left_degree, right_degree)`. It requires positive coprime degrees and returns exact rational values for both inputs, their product, the combined degree, and the composition defect
\[
\Delta_p(a,b)=R_p(ab)-R_p(a)R_p(b).
\]
It does not assume that the defect has a fixed sign or is nonzero in every case: degree one is an identity case because \(R_p(1)=1\). Tests cover the explicit \((2,3)\) counterexample, the degree-one identity, invalid/non-coprime inputs, and all coprime pairs through 12 over prime fields 2, 3, 5, and 7.

The current conclusion is precise: the normalized irreducible density is not multiplicative over coprime degree products. The factorization of the Möbius divisor set survives, but the exponent/normalization kernel obstructs a direct scalar product law. A useful next step is to characterize the defect's sign and asymptotic size, rather than trying to force multiplicativity.


## G-EP177 — Sign survey of the coprime-degree defect

For coprime degrees a,b>1, define Delta_p(a,b)=R_p(ab)-R_p(a)R_p(b). A bounded exact-rational survey over prime fields p in {2,3,5,7,11} and unordered coprime degrees 2 <= a < b <= 100 found no nonpositive defects (2,944 pairs per field). The smallest observed positive defects occurred at (a,b)=(89,97), illustrating how quickly the sign margin can become tiny. This is computational evidence only, not a proof of universal positivity.

The identity Delta_p(a,b)=E_p(a)+E_p(b)-E_p(a)E_p(b)-E_p(ab), where E_p(n)=1-R_p(n), recasts positivity as a comparison between the combined-degree bad-element proportion and the corresponding expression from the two factor degrees. The uniform upper bound from G-EP174 is too coarse by itself to settle every pair and factorization pattern. No monotonicity under divisibility is assumed.

### Executable finite audit

G-EP177 adds audit_coprime_density_defect_sign(primes, max_degree), which checks every unordered coprime pair in the requested range using exact fractions. It reports positive, negative, and zero counts, the first nonpositive witness if one exists, and the minimum exact defect. Its interpretation explicitly labels the result as finite-grid evidence and makes no universal theorem claim. Regression coverage includes prime fields 2, 3, and 5 through degree 12 and input validation.

**Current status:** the sign conjecture remains open in this project. A finite sweep cannot establish positivity for all primes and all coprime degrees.


## G-EP178 — Reduce defect positivity to bad-proportion ordering

Set E_p(n)=1-R_p(n), the proportion of elements of F_(p^n) whose degree over F_p is smaller than n. Then

Delta_p(a,b)=E_p(a)+E_p(b)-E_p(a)E_p(b)-E_p(ab).

For x,y in [0,1], x+y-xy >= max(x,y). Consequently the strict ordering E_p(ab)<min(E_p(a),E_p(b)) is sufficient for Delta_p(a,b)>0. This is a stronger and more focused target than the original defect inequality, not an equivalent reformulation.

An exact-rational sweep over p in {2,3,5,7,11} and all unordered coprime pairs 2 <= a < b <= 100 found E_p(ab)<min(E_p(a),E_p(b)) in every checked case. G-EP178 adds audit_coprime_bad_proportion_order(primes, max_degree), which reports exact strict-order counts, the first failure witness, and the largest ratio E_p(ab)/min(E_p(a),E_p(b)). Regression tests cover the smaller grid and validation.

**Proof status:** the ordering is a finite-grid observation and remains unproved in general. The field interpretation identifies E_p(n) as the relative size of the union of proper subfields of F_(p^n). A union bound over maximal proper subfields gives E_p(n) <= sum over prime q dividing n of p^(-n(1-1/q)); a lower bound is supplied by any one maximal proper subfield. Comparing these bounds sharply enough for all coprime a,b is the next proof task.


## G-EP179 — A sharp candidate bound for the coprime bad-proportion ratio

For coprime degrees (a,b>1), define
[
Q_p(a,b)=\frac{E_p(ab)}{\min(E_p(a),E_p(b))},
\qquad E_p(n)=1-R_p(n).
]
The exploratory finite sweep suggested that the largest ratio occurs at
((a,b)=(2,3)). In that case,
[
E_p(2)=p^{-1},\qquad E_p(3)=p^{-2},
]
and
[
E_p(6)=p^{-3}+p^{-4}-p^{-5}.
]
Since (p^{-2}<p^{-1}), this gives the exact candidate envelope
[
\boxed{Q_p(2,3)=\frac{p^2+p-1}{p^3}.}
]

This motivates the stronger conjecture
[
\boxed{
Q_p(a,b)\le\frac{p^2+p-1}{p^3}
\quad\text{for every prime }p
\text{ and coprime }a,b>1.
}
]
If true, it implies the strict ordering from G-EP178 because the right-hand
side is strictly less than one for every prime (p\ge2). It would also
quantify a uniform margin in the bad-proportion comparison.

G-EP179 adds
`audit_coprime_bad_proportion_ratio_bound(primes, max_degree)`. The audit
checks all unordered coprime pairs in the requested finite range using exact
fractions, reports the first counterexample if present, counts successful
comparisons, and identifies the largest observed ratio. Its test fixture
covers 102 pairs across (p=2,3,5) through degree 12 and checks that the
maximum is attained at ((2,3)), with ratio (5/8) over (mathbb F_2).

**Proof status:** this remains a conjectured universal bound. The regression
grid is finite evidence only; no proof for arbitrary prime fields and
coprime degrees is claimed.



## G-EP180 — Prove the sharp ratio bound when one degree is two

The G-EP179 conjecture can be proved for every coprime pair whose smaller
degree is 2. Write the pair as (2,b), where b is odd and b>1. The case b=3
is the equality case:
[
Q_p(2,3)=\frac{p^2+p-1}{p^3}.
]

For the remaining cases, use the maximal-proper-subfield union bound
[
E_p(n)\le\sum_{q\mid n,\ q\text{ prime}}
p^{-n(1-1/q)}
]
and the one-subfield lower bound
[
E_p(n)\ge p^{-n(1-1/q)}
\quad(q\mid n,\ q\text{ prime}).
]
Let r be the smallest prime divisor of odd b and put
(A=b(1-1/r)). Then (E_p(b)\ge p^{-A}). Also
(E_p(b)\le\omega(b)p^{-b/2}<p^{-1}=E_p(2)) for odd b≥5, so
(min(E_p(2),E_p(b))=E_p(b)).

Applying the union bound to 2b, and using q≥r for every prime q|b,
[
Q_p(2,b)
\le p^{-(b-A)}+\omega(b)p^{-A}
=p^{-b/r}+\omega(b)p^{-A}.
]

If b is prime and b≥5, this sharpens to
[
Q_p(2,b)\le p^{-1}+p^{-(b-1)}
\le p^{-1}+p^{-2}-p^{-3}
=\frac{p^2+p-1}{p^3},
]
where the middle inequality follows from (p^{-4}\le p^{-2}-p^{-3}).

If b is composite, then b≥9, r≥3, and
[
p^{-b/r}\le p^{-3}\le p^{-1}.
]
Moreover, distinct prime divisors of b are all at least 3, so
(omega(b)\le\log_3 b). For b≥9,
[
\omega(b)2^{2-b/2}\le
(\log_3 b)2^{2-b/2}<\frac12.
]
The left side decreases for b≥9; its value at b=9 is
(2^{-1/2}<1/2) is false, so use the sharper integer bound
(omega(9)=1) at b=9 and for b≥15 use
((\log_3 b)2^{2-b/2}<1/2).
Consequently, for every p≥2,
[
\omega(b)p^{-A}\le\omega(b)p^{-b/2}
\le p^{-2}-p^{-3}.
]
Combining the two terms proves
[
Q_p(2,b)\le p^{-1}+p^{-2}-p^{-3}
=\frac{p^2+p-1}{p^3}.
]

**Scope:** this proves the G-EP179 bound for the entire smaller-degree-2
family, with equality at (2,3) and strict inequality for odd b≥5. It does
not settle pairs whose smaller degree is at least 3. The displayed
logarithmic estimate is handled separately at b=9 and uniformly for b≥15;
the union-bound argument is analytic, not a finite-grid inference.


## G-EP181 — Complete the sharp ratio bound for all coprime degrees

G-EP180 handles the case where the smaller degree is 2. We now prove the
G-EP179 bound for every remaining pair as well. Let \(3\le a<b\),
\(\gcd(a,b)=1\), and let \(\omega(m)\) denote the number of distinct prime
factors of \(m\).

For any \(n>1\), if \(q_n\) is its smallest prime factor, the maximal
proper-subfield lower bound and union upper bound give
\[
E_p(n)\ge p^{-A_n},\quad A_n=n(1-1/q_n),
\qquad
E_p(n)\le\sum_{q\mid n,\ q\ {\rm prime}}p^{-n(1-1/q)}.
\]
Since \(A_a<a<b\) and \(A_b<b\), we have
\(\max(A_a,A_b)<b\). Therefore
\[
\begin{aligned}
Q_p(a,b)
&=\frac{E_p(ab)}{\min(E_p(a),E_p(b))}\\
&\le \sum_{q\mid ab,\ q\ {\rm prime}}
p^{\max(A_a,A_b)-ab(1-1/q)}\\
&\le \omega(ab)p^{b-ab/2}\\
&\le \omega(ab)p^{-b/2},
\end{aligned}
\]
where the last step uses \(a\ge3\). It remains to control the elementary
factor \(\omega(ab)\).

If \(b=4\), coprimality and \(3\le a<b\) force \(a=3\), so
\(\omega(ab)=\omega(12)=2\). Thus
\[
Q_p(3,4)\le2p^{-2}
\le p^{-1}+p^{-2}-p^{-3}
=\frac{p^2+p-1}{p^3},
\]
because \(p^2-p-1>0\) for every prime \(p\ge2\).

For \(b=5,6,7\), the admissible smaller degrees and products are finite:
\[
\begin{array}{c|c|c}
b & a & ab\\ \hline
5&3,4&15,20\\
6&5&30\\
7&3,4,5,6&21,28,35,42
\end{array}
\]
Every listed product has at most three distinct prime factors. Hence
\(\omega(ab)\le3\le2^{b/2-1}\) in these cases.

For \(b\ge8\), since \(a<b\),
\[
\omega(ab)\le\log_2(ab)<2\log_2 b
\le2^{b/2-1}.
\]
The last inequality holds at \(b=8\), where \(6\le8\), and its
right-minus-left difference is increasing for real \(b\ge8\): the
exponential term has increasing derivative while the logarithmic
derivative decreases. Consequently, for every \(b\ge5\),
\[
\omega(ab)\le2^{b/2-1}\le p^{b/2-1},
\]
and so
\[
Q_p(a,b)\le p^{-1}
< p^{-1}+p^{-2}-p^{-3}.
\]

Together with the \(b=4\) case, this proves
\[
\boxed{
Q_p(a,b)\le\frac{p^2+p-1}{p^3}
}
\]
for all prime \(p\) and all coprime \(a,b\ge3\), with strict inequality
throughout this range. G-EP180 supplies the remaining pairs with smaller
degree 2; equality in the complete theorem occurs exactly at
\(\{a,b\}=\{2,3\}\).

**Conclusion:** the G-EP179 sharp ratio conjecture is now a theorem for all
coprime degrees \(a,b>1\). In particular,
\(E_p(ab)<\min(E_p(a),E_p(b))\), so the coprime-degree defect
\(\Delta_p(a,b)\) is strictly positive. The proof uses exact
finite-field subfield bounds and an elementary factor-count estimate;
the finite computational sweeps remain corroboration, not the proof.


## G-EP182 — The coprime-degree defect is asymptotically additive

The exact identity from G-EP178 is
\[
\Delta_p(a,b)=E_p(a)+E_p(b)-E_p(a)E_p(b)-E_p(ab).
\]
G-EP181 proves that \(E_p(ab)<\min(E_p(a),E_p(b))\). We now sharpen this:
the combined-degree term is negligible relative to the smaller input
bad-proportion as the larger degree grows.

Assume \(2\le a<b\), \(\gcd(a,b)=1\), and write
\[
Q_p(a,b)=\frac{E_p(ab)}{\min(E_p(a),E_p(b))}.
\]
For \(a\ge3\), the union-bound/lower-bound argument in G-EP181 gives
\[
Q_p(a,b)\le\omega(ab)p^{-b/2}
<2\log_2(b)\,p^{-b/2}
\le2\log_2(b)\,2^{-b/2}.
\]
For \(a=2\), \(b\) is odd. If \(b\ge5\), let \(r\ge3\) be its smallest
prime factor and \(A=b(1-1/r)\). The G-EP180 estimate gives
\[
Q_p(2,b)\le p^{-b/r}+\omega(b)p^{-A}
\le2^{-b/3}+(\log_3 b)2^{-b/2}.
\]
The exceptional pair \((2,3)\) is isolated and has the exact ratio
\((p^2+p-1)/p^3\).

Thus, uniformly over every prime field,
\[
\boxed{
\sup_{\substack{a,b>1,\ \gcd(a,b)=1\\\max(a,b)=B}}
Q_p(a,b)\longrightarrow0
\quad(B\to\infty).
}
\]
More explicitly, for \(B\ge5\) the ratio is bounded by the larger of
\[
2\log_2(B)\,2^{-B/2}
\quad\hbox{and}\quad
2^{-B/3}+(\log_3 B)2^{-B/2},
\]
both of which tend to zero. (For the first expression the \(a\ge3\)
case applies; for the second, the \(a=2\) case.)

Now put \(S=E_p(a)+E_p(b)\), \(m=\min(E_p(a),E_p(b))\), and
\(M=\max(E_p(a),E_p(b))\). Since
\[
\frac{E_p(a)E_p(b)}S\le m,\qquad
\frac{E_p(ab)}S
=Q_p(a,b)\frac mS\le\frac{Q_p(a,b)}2,
\]
we obtain the explicit relative-error estimate
\[
0\le1-\frac{\Delta_p(a,b)}S
\le m+\frac{Q_p(a,b)}2.
\]
Also, the uniform convergence estimate from G-EP174 gives
\[
m\le E_p(b)\le(b-1)2^{-b/2}\longrightarrow0.
\]
Combining these estimates proves
\[
\boxed{
\frac{\Delta_p(a,b)}{E_p(a)+E_p(b)}\to1
}
\]
as \(\max(a,b)\to\infty\) through coprime pairs, uniformly in prime \(p\).

This is an additive asymptotic law, not a multiplicative law for
\(R_p\): the defect is asymptotically the sum of the two input
proper-subfield proportions, while the combined-degree correction is
lower order. The displayed estimates quantify convergence and cover
the regime where the smaller degree remains fixed (including \(a=2\));
the single pair (2,3) does not affect the limit.


## G-EP183 — Prime-factorization law for the defect's exponential scale

For \(n>1\), let \(q(n)\) be its smallest prime divisor and define
\[
A(n)=n\left(1-\frac1{q(n)}\right).
\]
The Möbius expansion of \(E_p(n)=1-R_p(n)\) has leading term
\(p^{-A(n)}\). The one-maximal-subfield lower bound and the
maximal-proper-subfield union bound give the exact inequalities
\[
\boxed{
p^{-A(n)}\le E_p(n)\le\omega(n)p^{-A(n)}.
}
\]
Indeed, the smallest prime divisor gives the largest term in the union
bound, and every other prime divisor contributes no more than that term.
This estimate is valid for every prime \(p\), without taking a limit in
\(p\).

For coprime \(a,b>1\), put
\[
A_*=\min(A(a),A(b)),\qquad
S=E_p(a)+E_p(b),\qquad B=\max(a,b).
\]
The G-EP182 relative-error estimate gives
\[
0\le1-\frac{\Delta_p(a,b)}S
\le \min(E_p(a),E_p(b))+\frac{Q_p(a,b)}2.
\]
Its right-hand side tends to zero uniformly in prime \(p\) as \(B\)
grows. Hence there is an absolute threshold \(B_0\) such that
\(\Delta_p(a,b)\ge S/2\) for every prime \(p\) and every coprime pair
with \(B\ge B_0\).

The factorization bounds imply
\[
p^{-A_*}\le S
\le\bigl(\omega(a)+\omega(b)\bigr)p^{-A_*}.
\]
Consequently, for all such sufficiently large pairs,
\[
\boxed{
\frac12p^{-A_*}
\le\Delta_p(a,b)
\le\bigl(\omega(a)+\omega(b)\bigr)p^{-A_*}.
}
\]
Since \(\omega(a)+\omega(b)<2\log_2 B\), this yields the explicit
logarithmic-scale statement
\[
\boxed{
\left|-\log_p\Delta_p(a,b)-A_*\right|
\le 1+\log_2(2\log_2 B).
}
\]
The bound is uniform over prime fields. In particular,
\[
-\log_p\Delta_p(a,b)
=\min\left\{
a\left(1-\frac1{q(a)}\right),
b\left(1-\frac1{q(b)}\right)
\right\}
+O(\log\log B),
\]
with an absolute, field-uniform error bound.

Thus the degree with the smaller subfield exponent controls the defect's
leading exponential scale. It is not necessarily the smaller degree:
a larger degree with a smaller prime divisor can dominate a smaller
degree with a larger smallest prime divisor. This distinction is why
degree size alone does not determine the leading term.

**Scope:** the result is an asymptotic statement as \(B\to\infty\), with
an absolute threshold inherited from G-EP182. The two-sided
factorization bound for each individual \(E_p(n)\) is exact for every
\(n>1\) and every prime \(p\). The \(O(\log\log B)\) estimate does not
assert a fixed multiplicative leading constant; that finer constant
depends on the remaining prime divisors and on the lower-order
inclusion-exclusion terms.


## G-EP184 — Exact divisor spectrum and the second-order hierarchy

The error term has a finite, exact exponential spectrum. Let
\[
\mathcal S(n)=\{d:d\mid n,\ d>1,\ d\text{ squarefree}\},
\qquad e_n(d)=n\left(1-\frac1d\right).
\]
Then
\[
\boxed{
E_p(n)=-\sum_{d\in\mathcal S(n)}\mu(d)p^{-e_n(d)}.
}
\]
This is not an asymptotic expansion: it is an identity for every prime
\(p\). It exposes all subfield-intersection scales, not only the
largest maximal proper subfield.

Order the squarefree divisors as
\(d_1<d_2<\cdots<d_{2^{\omega(n)}-1}\). The first is the smallest prime
factor \(q_1\), and, when \(n\) has at least two distinct prime factors,
the second is the next smallest prime factor \(q_2\). Therefore
\[
E_p(n)=p^{-e_n(d_1)}+p^{-e_n(d_2)}
-\mu(d_3)p^{-e_n(d_3)}-\cdots.
\]
The displayed second term is absent when \(n\) is a prime power; in
that case \(E_p(n)=p^{-e_n(q_1)}\) exactly. The third divisor is not
always the third prime: it is the third-smallest squarefree divisor.
For example, for prime factors \(2,3,7\), it is \(6\), not \(7\).
This gives a full hierarchy of correction scales ordered by the
integer squarefree divisors, with signs fixed by the Möbius function.

### Exact spectrum of the coprime defect

For coprime \(a,b>1\), write \(u_d=e_a(d)\) and \(v_f=e_b(f)\).
Substitution into
\(\Delta_p(a,b)=E_p(a)+E_p(b)-E_p(a)E_p(b)-E_p(ab)\) gives
\[
\begin{aligned}
\Delta_p(a,b)={}&
-\sum_{d\in\mathcal S(a)}\mu(d)p^{-u_d}
-\sum_{f\in\mathcal S(b)}\mu(f)p^{-v_f}\\
&-\sum_{\substack{d\in\mathcal S(a)\\f\in\mathcal S(b)}}
\mu(d)\mu(f)p^{-(u_d+v_f)}
+\sum_{g\in\mathcal S(ab)}\mu(g)p^{-e_{ab}(g)}.
\end{aligned}
\]
Collect terms with equal integer exponents. This produces a unique finite
integer-coefficient polynomial in \(x=1/p\). It is an exact
representation, and coefficient collisions must be combined before
reading off a second-order term.

### G-EP185 — Leading coefficient and resonance

Let \(A_n=e_n(q(n))\), and put \(A=\min(A_a,A_b)\).
Because \(a,b\) are coprime,
\[
A_{ab}> \max(A_a,A_b),\qquad A_a+A_b>\min(A_a,A_b).
\]
For the first inequality, suppose \(q(a)\le q(b)\). Then
\(A_{ab}=bA_a\), while \(A_a=a(1-1/q(a))\ge1\), so
\(A_{ab}\ge b>A_b\), and also \(A_{ab}>A_a\).
The other ordering is symmetric.

It follows that neither the product term nor \(E_p(ab)\) can cancel
the leading input contribution. Thus, for fixed coprime \(a,b\) and
\(p\to\infty\) through primes,
\[
\boxed{
\Delta_p(a,b)\sim C(a,b)p^{-A},
\quad
C(a,b)=
\begin{cases}
1,&A_a\ne A_b,\\
2,&A_a=A_b.
\end{cases}
}
\]
We call \(A_a=A_b\) a *leading-scale resonance*: both input degrees
contribute at the same exponential order. This is an exact
classification of the leading coefficient, not a numerical
observation.

Examples:
- \((a,b)=(2,3)\): \(A_2=1,A_3=2\), so
  \(\Delta_p(2,3)\sim p^{-1}\).
- \((a,b)=(3,4)\): \(A_3=A_4=2\), so
  \(\Delta_p(3,4)\sim2p^{-2}\). In fact,
  \[
  \Delta_p(3,4)=2p^{-2}-p^{-4}-p^{-6}-p^{-8}+p^{-10}.
  \]

### G-EP186 — The second nonzero scale is computable exactly

Let \(c_k(a,b)\) be the coefficient of \(x^k\) after collecting the
finite spectrum above. Then
\[
\Delta_p(a,b)=\sum_k c_k(a,b)p^{-k}.
\]
The first nonzero coefficient is \(c_A=C(a,b)\). Define
\(K>A\) to be the smallest exponent with \(c_K\ne0\), if one exists.
Then
\[
\Delta_p(a,b)=C(a,b)p^{-A}+c_Kp^{-K}
+O_{a,b}(p^{-K'}),
\]
where \(K'\) is the next exponent with nonzero coefficient, if present.
If there is no such next exponent, the finite sum terminates. This
coefficient-collection rule handles all resonances: an apparent
candidate correction can disappear when contributions from the two
inputs, their product, and the composite degree land at the same
exponent. The next scale is therefore determined by the *combined*
divisor spectra, not by independently taking the second prime factor
of each input.

### G-EP187 — Two different asymptotic directions

There are now two complementary limits, and they answer different
questions.

1. **Field-size direction:** keep \(a,b\) fixed and let \(p\to\infty\).
   G-EP185 gives the exact leading exponent and coefficient, while
   G-EP184–186 give every subsequent scale.
2. **Degree direction:** let \(B=\max(a,b)\to\infty\) through coprime
   pairs, allowing the smaller degree to remain fixed and allowing
   \(p\) to vary. G-EP182 gives
   \(\Delta_p(a,b)/(E_p(a)+E_p(b))\to1\) uniformly in prime \(p\);
   G-EP183 then identifies the leading exponent up to an
   \(O(\log\log B)\) error.

These are not interchangeable limits. G-EP185 is a fixed-degree
large-field expansion; G-EP182–183 are uniform large-degree results.
The exact finite spectrum is the bridge between them and supplies a
direct route for symbolic or exact-arithmetic computation of
higher-order terms.


## G-EP188 — Exact spectrum as an executable invariant

The finite spectrum is now an exact computational object, not merely
a formal expansion. The audit routine
\`coprime_defect_exponent_spectrum(a,b)\` validates coprimality,
constructs the squarefree-divisor contributions to \(E_p(a)\),
\(E_p(b)\), \(E_p(ab)\), and the product \(E_p(a)E_p(b)\), then
collects equal integer exponents and removes zero coefficients. Its
output records the leading exponent and coefficient and the next
nonzero term. The companion evaluator returns an exact rational value
at any integer field size \(Q\ge2\).

The evaluator deliberately accepts prime powers as well as primes:
the algebraic identity is a polynomial identity in the field size, and
does not depend on primality of the numerical input. A caller wishing
to interpret the result as a finite-field quantity must, of course,
supply a prime-power field size.

### Cross-check identities

For \((a,b)=(2,3)\), the auditor returns
\[
x+x^2-2x^3-x^4+x^5.
\]
For the resonant pair \((3,4)\), it returns
\[
2x^2-x^4-x^6-x^8+x^{10}.
\]
These are exact rational identities after \(x=1/Q\), not floating-point
fits. The test suite includes these fixtures, validation cases, and
small-grid positivity checks.

## G-EP189 — Prime-power base fields

Nothing in the Möbius count or subfield-lattice argument requires the
base field to have prime order. For every prime power \(Q\), the number
of monic irreducibles of degree \(n\) over \(\mathbb F_Q\) is
\[
I_Q(n)=\frac1n\sum_{d\mid n}\mu(d)Q^{n/d}.
\]
Thus
\[
R_Q(n)=\frac{nI_Q(n)}{Q^n},\qquad
E_Q(n)=1-R_Q(n)
=-\sum_{\substack{d\mid n\\d>1}}\mu(d)Q^{-n(1-1/d)}.
\]
Every theorem above that uses only \(Q\ge2\), the divisor lattice, and
the displayed exact formula extends verbatim with \(p\) replaced by
\(Q\). This includes the exact spectrum, resonance coefficient,
uniform degree-direction bounds, and positive coprime defect. The
smallest admissible field size remains 2, so the same worst-case
uniform bounds apply. The computational evaluator is therefore
correctly defined for all integer \(Q\ge2\), while field interpretation
requires \(Q\) to be a prime power.

## G-EP190 — Multi-factor composition excess and sign resonance

For pairwise-coprime degrees \(n_1,\ldots,n_r>1\), define
\[
H_Q(n_1,\ldots,n_r)
=E_Q(n_1\cdots n_r)-\prod_{i=1}^rE_Q(n_i).
\]
This is a different quantity from the two-factor defect
\(\Delta_Q(a,b)=E_Q(a)+E_Q(b)-E_Q(a)E_Q(b)-E_Q(ab)\).
Its sign is not universally positive. The exact recursion, with
\(F_j=E_Q(n_1\cdots n_j)\) and
\(D_j=F_j-\prod_{i=1}^jE_Q(n_i)\), is
\[
D_1=0,\qquad
D_j=\bigl(F_j-F_{j-1}E_Q(n_j)\bigr)+E_Q(n_j)D_{j-1}.
\]
The bracket is the *composition excess*
\(E_Q((n_1\cdots n_{j-1})n_j)
-E_Q(n_1\cdots n_{j-1})E_Q(n_j)\), not the two-factor defect
\(\Delta_Q\). The recursion is exact, but neither its bracket nor
\(D_j\) has a universal sign.

For fixed pairwise-coprime degrees, let \(N=\prod_i n_i\) and
\(A(n)=n(1-1/q(n))\). The leading field-size asymptotics are
\[
E_Q(N)\sim Q^{-A(N)},\qquad
\prod_iE_Q(n_i)\sim Q^{-\sum_iA(n_i)}.
\]
Therefore:
\[
\begin{cases}
H_Q\sim Q^{-A(N)},&A(N)<\sum_iA(n_i),\\
H_Q\sim -Q^{-\sum_iA(n_i)},&A(N)>\sum_iA(n_i).
\end{cases}
\]
At equality, the leading terms cancel and the exact divisor spectrum
must be collected to determine the next nonzero term. This is a
genuine *composition resonance*.

Examples:
\[
H_Q(2,3)=Q^{-4}-Q^{-5}>0,
\]
where the leading exponents tie at 3 and cancel, while
\[
H_Q(3,4)=-Q^{-4}+Q^{-6}+Q^{-8}-Q^{-10}<0
\]
for \(Q\ge2\). Thus composition excess is tree-decomposable but not
sign-definite. The two-factor \(\Delta_Q\) positivity theorem remains
unchanged.

The exact spectrum can be constructed for any pairwise-coprime list:
take the spectrum of \(E_Q(N)\), subtract the additive convolution of
the individual \(E_Q(n_i)\) spectra, and collect equal exponents. The
result is independent of the chosen binary composition tree, although
the intermediate local terms depend on the tree.

## G-EP191 — Boolean-lattice geometry of the divisor spectrum

Let the distinct prime divisors of \(n\) be
\(q_1,\ldots,q_k\). Every squarefree divisor corresponds to a subset
\(S\subseteq\{1,\ldots,k\}\), with
\(d_S=\prod_{i\in S}q_i\). The exact error spectrum becomes
\[
E_Q(n)=
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{|S|+1}
Q^{-n(1-1/d_S)}.
\]
Thus its terms are the vertices of a Boolean lattice, with alternating
Möbius signs. The exponent map
\[
S\longmapsto n\left(1-\frac1{\prod_{i\in S}q_i}\right)
\]
is strictly increasing under strict inclusion. The spectrum is
therefore naturally graded by subset inclusion, but its numerical
ordering is by the products \(d_S\), not by subset cardinality.
This explains why pairwise products can appear before a larger
individual prime factor: for \(\{2,3,7\}\), the subset \(\{2,3\}\)
has product 6 and precedes the singleton \(\{7\}\).

The defect spectrum is a signed combination of three such Boolean
lattices and the additive convolution of the two input spectra. This
gives a concrete combinatorial model for coefficient collisions:
different lattice vertices, or a convolution vertex, can map to the
same integer exponent. The exact auditor performs precisely this
push-forward and coefficient collection.

## G-EP192 — Exact finite-field order, not just prime characteristic

The executable count now includes
\`count_monic_irreducibles_over_field(Q,n)\` and
\`irreducible_density_over_field(Q,n)\`. They validate that \(Q\) is a
prime power and evaluate
\[
I_Q(n)=\frac1n\sum_{d\mid n}\mu(d)Q^{n/d}
\]
with integer arithmetic. The earlier prime-only API remains unchanged
for backwards compatibility. The defect-spectrum evaluator accepts any
integer \(Q\ge2\) as a polynomial evaluation; finite-field
interpretation is restricted to prime powers.

Regression fixtures include \(\mathbb F_4\), \(\mathbb F_8\), and
\(\mathbb F_9\). In particular,
\(I_4(2)=6\) and \(R_4(2)=3/4\), so \(E_4(2)=1/4\).
