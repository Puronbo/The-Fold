# Accelerated Collatz dynamics: exact valuation itineraries

## 1. Why accelerate

For odd \(n\), define
\[
S(n)=\frac{3n+1}{2^{a(n)}},
\qquad a(n)=v_2(3n+1)\ge1.
\]
Then \(S(n)\) is again a positive odd integer. The ordinary Collatz orbit reaches \(1\) if and only if the accelerated odd orbit reaches \(1\): the omitted steps are precisely the finite strings of divisions by \(2\) between successive odd terms.

Write
\[
n_{i+1}=S(n_i),\qquad a_i=v_2(3n_i+1),\qquad
A_t=\sum_{i=0}^{t-1}a_i.
\]

The sequence \((a_0,a_1,\ldots)\) is the valuation itinerary. Unlike a fixed residue, it records the exact number of divisions at each odd step.

## 2. Affine iterate identity

For every \(t\ge0\),
\[
\boxed{
2^{A_t}n_t
=3^t n_0+\sum_{j=0}^{t-1}3^{t-1-j}2^{A_j}.
}
\tag{1}
\]
Here \(A_0=0\), and the empty sum for \(t=0\) is zero.

**Proof.** For \(t=0\) the identity is \(n_0=n_0\). If it holds at \(t\), then
\[
2^{a_t}n_{t+1}=3n_t+1.
\]
Multiplying by \(2^{A_t}\) and substituting (1) gives
\[
2^{A_{t+1}}n_{t+1}
=3^{t+1}n_0+
\sum_{j=0}^{t-1}3^{t-j}2^{A_j}+2^{A_t},
\]
which is exactly (1) with \(t+1\). \(\square\)

In particular,
\[
\frac{n_t}{n_0}
=\frac{3^t}{2^{A_t}}
\left(
1+\frac{1}{3n_0}
+\frac{2^{A_1}}{3^2n_0}
+\cdots+
\frac{2^{A_{t-1}}}{3^t n_0}
\right).
\]
A more useful multiplicative form follows directly from the one-step recurrence:
\[
\boxed{
n_t=n_0\,\frac{3^t}{2^{A_t}}
\prod_{i=0}^{t-1}\left(1+\frac{1}{3n_i}\right).
}
\tag{2}
\]
Thus the exact growth is controlled by the cumulative valuation \(A_t\), with a positive correction product.

## 3. Exact finite-itinerary residue theorem

Fix a finite list of positive integers
\[
\mathbf a=(a_0,\ldots,a_{t-1}),\qquad
A=a_0+\cdots+a_{t-1}.
\]

**Theorem.** There is exactly one odd residue class
\[
r_{\mathbf a}\pmod{2^{A+1}}
\]
such that a positive odd integer \(n_0\) has first \(t\) accelerated valuations
\[
(a_0,\ldots,a_{t-1})
\]
if and only if
\[
n_0\equiv r_{\mathbf a}\pmod{2^{A+1}}.
\]

In particular, the itinerary is constant on this entire residue class, and every positive integer in the class realizes it.

### Proof by successive lifting

For an odd integer \(x\), the condition \(v_2(3x+1)=a\) is equivalent to
\[
3x+1\equiv 2^a\pmod{2^{a+1}}.
\tag{3}
\]
Since \(3\) is invertible modulo every power of \(2\), (3) specifies exactly one odd residue class modulo \(2^{a+1}\).

Suppose the first \(i\) valuations have been prescribed. Put \(A_i=a_0+\cdots+a_{i-1}\). The recurrence gives
\[
n_i=\frac{3^i n_0+c_i}{2^{A_i}}
\]
for an integer \(c_i\) determined by the preceding exponents. To prescribe \(a_i\), impose (3) on \(n_i\):
\[
3(3^i n_0+c_i)+2^{A_i}
\equiv 2^{A_i+a_i}
\pmod{2^{A_i+a_i+1}}.
\]
The coefficient \(3^{i+1}\) of \(n_0\) is odd and hence invertible modulo \(2^{A_i+a_i+1}\). This gives exactly one residue class for \(n_0\) modulo \(2^{A_i+a_i+1}\). The congruence also enforces the divisibility needed to define \(n_i\), while retaining all earlier valuation conditions because it refines the previously obtained class.

Starting at \(i=0\) and repeating this lift gives exactly one class modulo \(2^{A+1}\). Conversely, each lift imposed the exact congruence (3), so every positive odd representative has precisely the stated valuations. \(\square\)

### Consequence: cylinder sets have exact 2-adic size

Among odd residues modulo \(2^{A+1}\), the itinerary cylinder \(\mathbf a\) is one residue class. Its relative density within the odd integers is therefore
\[
2^{-A}.
\]
This is an exact finite statement about initial valuations, not a probability assertion about infinite orbits.

## 4. A necessary average-valuation condition for divergence

Taking logarithms in (2) gives
\[
\frac{1}{t}\log_2\frac{n_t}{n_0}
=
\log_2 3-\frac{A_t}{t}
+\frac1t\sum_{i=0}^{t-1}
\log_2\left(1+\frac1{3n_i}\right).
\tag{4}
\]
Since \(n_i\ge1\),
\[
0<
\log_2\left(1+\frac1{3n_i}\right)
\le\log_2(4/3).
\]
The correction is positive but bounded per step.

If an accelerated orbit tends to infinity, then the left side of (4) need not have a limit, but along any subsequence on which \(n_t\to\infty\) and the logarithmic growth rate has a limit, that limit is constrained by the average valuation. In particular, if
\[
\lim_{t\to\infty}\frac{A_t}{t}
\]
exists and is strictly greater than \(\log_2 3+\log_2(4/3)=2\), then (4) forces \(n_t\to0\), impossible for positive integers. Hence every infinite orbit with a limiting average valuation must satisfy
\[
\lim_{t\to\infty}\frac{A_t}{t}\le2.
\]
A sharper conclusion requires control of the correction term and/or the actual growth rate; the crude bound above is not a Collatz proof.

More directly, if \(n_t\) is unbounded along a subsequence, (4) gives the necessary subsequential inequality
\[
\liminf \frac{A_t}{t}
\le \log_2 3+\log_2(4/3)=2
\]
along any subsequence where \(n_t\to\infty\) and the corresponding averages converge. The constant \(2\) here is only a coarse universal bound.

## 5. What this adds to the Fold programme

The accelerated system supplies a scale-sensitive state:
\[
(n_i,\ a_i,\ A_i).
\]
The finite-itinerary theorem says that a prefix with total valuation \(A\) is exactly encoded by one odd residue class modulo \(2^{A+1}\). The required precision grows with cumulative valuation, rather than remaining fixed.

This avoids the false claim that one finite quotient captures all future divisions. It also gives a precise refinement rule: appending valuation \(a_i\) increases the required input precision from \(2^{A_i+1}\) to \(2^{A_i+a_i+1}\), and the lift is unique.

The theorem is a coding result, not a termination result. It does not show that valuation sums are large enough, nor that every itinerary eventually reaches the one associated with \(1\).

## 6. Status

- Accelerated odd map and equivalence with ordinary Collatz: **proved**.
- Affine iterate identity (1): **proved**.
- Exact unique residue class for every finite valuation itinerary: **proved**.
- Exact relative density \(2^{-A}\) of a fixed itinerary cylinder among odd integers at its natural precision: **proved**.
- A global estimate forcing every orbit to reach \(1\): **open**.
- Collatz conjecture: **not solved**.

The next target is to exploit the unique-lift structure quantitatively: determine whether long valuation itineraries that would permit sustained growth can be excluded by a global compatibility or counting argument, rather than by assuming valuations behave independently.
