# Global compatibility of accelerated Collatz valuation itineraries

## 1. The finite cylinders form a coherent tree

For an odd positive integer, let
\[
S(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1)\ge1.
\]
For a finite word \(w=(a_0,\ldots,a_{t-1})\) of positive integers, write
\[
A(w)=\sum_{i<t}a_i
\]
and let \(C_w\) be the set of odd starting integers whose first \(t\) accelerated valuations equal \(w\).

The finite-itinerary theorem in [the companion note](collatz-accelerated-valuation-itineraries.md) says that \(C_w\) is exactly one odd residue class modulo \(2^{A(w)+1}\).

**Compatibility theorem.** If \(w'=(a_0,\ldots,a_{t-1},b)\) extends \(w\), then
\[
C_{w'}\subseteq C_w,
\]
and the defining residue of \(C_{w'}\), reduced modulo \(2^{A(w)+1}\), is the defining residue of \(C_w\).

**Proof.** Every integer realizing the extended word realizes its prefix. The prefix cylinder is one residue class at its stated modulus, and the extended cylinder is one residue class at a higher power of two. Since the latter is nonempty and contained in the former, its residue reduces to the prefix residue. \(\square\)

At each node, the children indexed by \(b=1,2,\ldots\) partition the parent:
\[
C_w=\bigsqcup_{b\ge1} C_{(w,b)}.
\]
This is an exact partition, not an independence assumption. In the normalized counting measure on odd residues at the relevant powers of two,
\[
\frac{\mu(C_{(w,b)})}{\mu(C_w)}=2^{-b},
\qquad \sum_{b\ge1}2^{-b}=1.
\]
The identity follows by comparing the unique residue classes at moduli \(2^{A(w)+1}\) and \(2^{A(w)+b+1}\).

## 2. Infinite words have unique 2-adic realizations

Let \(\mathbb Z_2\) denote the 2-adic integers. For an infinite word
\[
\mathbf a=(a_0,a_1,a_2,\ldots),\qquad a_i\ge1,
\]
let \(w_t=(a_0,\ldots,a_{t-1})\) and \(A_t=\sum_{i<t}a_i\).

**Theorem (2-adic itinerary coding).** Every infinite positive-integer word \(\mathbf a\) determines exactly one odd 2-adic integer \(x\) lying in every finite cylinder \(C_{w_t}\). Conversely, every odd 2-adic integer whose successive accelerated iterates never encounter the singular value \(-1/3\) has one such infinite valuation word. Thus the itinerary map is a bijection between infinite valuation words and the nonsingular odd 2-adic starting points.

**Proof.** The compatibility theorem gives nested residue classes
\[
r_t\pmod{2^{A_t+1}},
\qquad
r_{t+1}\equiv r_t\pmod{2^{A_t+1}}.
\]
Since each \(a_i\ge1\), we have \(A_t\to\infty\). A compatible system of residues modulo powers of two determines exactly one element of \(\mathbb Z_2\). Every class is odd, so its limit is odd.

At stage \(i\), membership in the cylinder for the prefix through \(a_i\) imposes
\[
3x_i+1\equiv 2^{a_i}\pmod{2^{a_i+1}},
\]
where \(x_i\) is the corresponding 2-adic iterate. This is precisely the assertion that the valuation is exactly \(a_i\), and division by \(2^{a_i}\) defines the next odd iterate. Hence the limit realizes the whole word. Uniqueness follows because two 2-adic integers in every cylinder are congruent modulo \(2^{A_t+1}\) for every \(t\), and these moduli tend to zero 2-adically.

Conversely, a nonsingular odd 2-adic orbit has a finite valuation at every stage, and those valuations define its unique itinerary. The only excluded case at a stage is \(3x_i+1=0\), namely \(x_i=-1/3\). \(\square\)

## 3. Exact Haar independence—and its limitation

Normalize Haar measure on the compact group of odd 2-adic integers to have total mass one. The cylinder theorem gives
\[
\mu(C_{(a_0,\ldots,a_{t-1})})
=2^{-(a_0+\cdots+a_{t-1})}
=\prod_{i<t}2^{-a_i}.
\]
Consequently, under this 2-adic Haar measure, the coordinate valuations have the geometric product law
\[
\Pr(a_i=b)=2^{-b},\qquad b=1,2,\ldots.
\]
In particular, the valuation coordinates are independent **for Haar-almost every 2-adic starting point**. This is a theorem about Haar measure on \(\mathbb Z_2\), not a stochastic model imposed on integer Collatz orbits.

The distinction is decisive. Positive odd integers embed into \(\mathbb Z_2\), but they form a countable, Haar-null subset. Haar-almost-everywhere statements do not decide the itinerary of any specified positive integer, and they do not prove that every positive integer orbit reaches 1. Every finite cylinder contains infinitely many positive odd integers, while an infinite word's unique 2-adic realization need not be an ordinary positive integer.

Therefore the cylinder tree has no further finite-prefix obstruction: **every finite or infinite valuation word is 2-adically compatible**. Any successful integer-orbit argument must use the extra condition that the starting point is a positive ordinary integer, together with the arithmetic growth identity—not merely compatibility of residues or Haar statistics.

## 4. What this rules out, and what remains

This result sharpens the previous finite-itinerary theorem in two opposite directions:

- It proves a genuine global compatibility theorem: every infinite valuation itinerary has a unique 2-adic starting point.
- It also shows why compatibility alone cannot settle Collatz: there are no forbidden infinite words at the 2-adic level.

The exact geometric law is useful as a baseline for finite cylinders and for identifying which arguments silently substitute Haar-generic behavior for a specific integer orbit. It is not legitimate to infer that a positive integer orbit has typical valuations, nor that its cumulative valuation obeys a probabilistic concentration estimate.

A viable next step must exploit an integer-specific constraint: for example, combine the affine iterate identity
\[
2^{A_t}n_t=3^t n_0+\sum_{j<t}3^{t-1-j}2^{A_j}
\]
with the requirement that every \(n_t\) is a positive ordinary integer. The 2-adic coding theorem supplies the exact symbolic side; it does not supply this missing Archimedean control.

## 5. Status

- Nested-cylinder compatibility: **proved**.
- Exact partition of each cylinder by its next valuation: **proved**.
- Unique 2-adic realization of every infinite valuation word: **proved**.
- Haar geometric product law for valuation coordinates: **proved**.
- Transfer of Haar-generic behavior to a specified positive integer orbit: **not proved and not implied**.
- Collatz termination: **open**.
