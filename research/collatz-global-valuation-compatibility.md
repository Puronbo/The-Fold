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

## 3. The exact integer-realization criterion

The same nested-cylinder argument gives a sharp criterion for when an infinite word is the itinerary of an ordinary positive integer.

**Theorem.** Let \(x\in\mathbb Z_2\) be the unique 2-adic realization of an infinite word \(\mathbf a\). Then
\[
\bigcap_{t\ge0} C_{w_t}
=
\begin{cases}
\{n\},&x=n\text{ for a positive odd integer }n,\\
\varnothing,&x\notin\mathbb Z_{>0}.
\end{cases}
\]
In particular, an infinite word is the itinerary of a positive integer if and only if its 2-adic realization is a positive odd integer.

**Proof.** If a positive odd integer \(n\) belongs to every prefix cylinder, then its image in \(\mathbb Z_2\) belongs to every corresponding residue class. By uniqueness of the 2-adic limit, \(n=x\). There can therefore be at most one such integer. Conversely, if \(x=n\) is a positive odd integer, the defining congruences at every finite stage say exactly that \(n\) has all the prescribed valuations, so it belongs to every cylinder. \(\square\)

Equivalently, writing \(r_t\) for the least nonnegative residue representative modulo \(2^{A_t+1}\), the word is an ordinary positive-integer itinerary exactly when these representatives eventually stabilize to one fixed positive odd integer. Since the moduli tend to infinity, stabilization is equivalent to the 2-adic limit having an ordinary finite binary expansion.

This pinpoints the gap between finite and infinite integer realizability: every finite prefix has infinitely many positive integer realizations, but the nested intersection over all prefixes is either empty or a singleton.

## 4. An explicit 2-adic series and the periodic-word test

The unique 2-adic point can be written directly from the itinerary. From the affine iterate identity,
\[
2^{A_t}n_t
=3^t n_0+\sum_{j=0}^{t-1}3^{t-1-j}2^{A_j},
\]
divide by \(3^t\) and rearrange:
\[
n_0
=-\sum_{j=0}^{t-1}\frac{2^{A_j}}{3^{j+1}}
+\frac{2^{A_t}}{3^t}n_t.
\]
Because \(A_t\to\infty\), the final term tends to zero 2-adically whenever \(n_t\in\mathbb Z_2\). Thus the coding map is
\[
\boxed{x(\mathbf a)=-\sum_{j=0}^{\infty}\frac{2^{A_j}}{3^{j+1}}\in\mathbb Z_2.}
\tag{5}
\]
The series converges 2-adically since the valuation of its \(j\)-th term is \(A_j\to\infty\). This is an explicit formula for the same unique point, not an additional assumption.

Now suppose the itinerary is periodic with period \(p\):
\[
(a_0,\ldots,a_{p-1},a_0,\ldots,a_{p-1},\ldots).
\]
Put \(A=\sum_{i=0}^{p-1}a_i\), \(A_j=\sum_{i<j}a_i\), and
\[
D=\sum_{j=0}^{p-1}2^{A_j}3^{p-1-j}.
\]
Grouping the series (5) into blocks of length \(p\) gives the rational value
\[
\boxed{x(\mathbf a)=\frac{D}{2^A-3^p}.}
\tag{6}
\]
Indeed, each successive block is the preceding block multiplied by \(2^A/3^p\), and the geometric series converges 2-adically because \(A\ge p\).

**Periodic-itinerary criterion.** A periodic positive-valuation word is realized by a positive odd integer if and only if
\[
2^A>3^p
\quad\text{and}\quad
2^A-3^p\mid D.
\]
When these conditions hold, its unique positive integer realization is \(n=D/(2^A-3^p)\), and the accelerated orbit of \(n\) is periodic with that valuation word. Conversely, every positive integer accelerated cycle yields a periodic valuation word satisfying this divisibility criterion.

The forward implication follows from (6): positivity requires a positive denominator, and integrality requires divisibility. The itinerary coding theorem then guarantees that the integer has exactly the prescribed valuations at every step. Periodicity of the word makes the state after \(p\) steps have the same itinerary as the initial state; more directly, the unique 2-adic point for the shifted periodic word is the same point, so \(S^p(n)=n\). Conversely, a positive integer cycle repeats its valuations, and (6) applies.

For the trivial cycle \(n=1\), the word is constantly \(2\), so \(p=1,A=2,D=1\) and (6) gives \(x=1\). The criterion is exact but does not by itself rule out other periods: doing so requires proving that no other periodic word satisfies the divisibility condition.

## 5. Exact Haar independence—and its limitation

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

## 6. What this rules out, and what remains

This result sharpens the previous finite-itinerary theorem in two opposite directions:

- It proves a genuine global compatibility theorem: every infinite valuation itinerary has a unique 2-adic starting point.
- It also shows why compatibility alone cannot settle Collatz: there are no forbidden infinite words at the 2-adic level.

The exact geometric law is useful as a baseline for finite cylinders and for identifying which arguments silently substitute Haar-generic behavior for a specific integer orbit. It is not legitimate to infer that a positive integer orbit has typical valuations, nor that its cumulative valuation obeys a probabilistic concentration estimate.

A viable next step must exploit an integer-specific constraint: for example, combine the affine iterate identity
\[
2^{A_t}n_t=3^t n_0+\sum_{j<t}3^{t-1-j}2^{A_j}
\]
with the requirement that every \(n_t\) is a positive ordinary integer. The 2-adic coding theorem supplies the exact symbolic side; it does not supply this missing Archimedean control.

## 7. Status

- Nested-cylinder compatibility: **proved**.
- Exact partition of each cylinder by its next valuation: **proved**.
- Unique 2-adic realization of every infinite valuation word: **proved**.
- Explicit 2-adic series for the coding map: **proved**.
- Rational formula and divisibility criterion for periodic-word integer realizations: **proved**.
- Haar geometric product law for valuation coordinates: **proved**.
- Transfer of Haar-generic behavior to a specified positive integer orbit: **not proved and not implied**.
- Collatz termination: **open**.

## 8. Exact exclusion of accelerated periods one and two

The periodic-word criterion immediately gives a small, fully arithmetic cycle exclusion.

For a period-(p) valuation word, retain
\[
A=\sum_{i=0}^{p-1}a_i,\qquad
D=\sum_{j=0}^{p-1}2^{A_j}3^{p-1-j}.
\]
A positive integer cycle requires
\[
2^A>3^p,\qquad 2^A-3^p\mid D,
\]
and its starting integer is (n=D/(2^A-3^p)).

**Theorem.** The only positive-integer accelerated Collatz cycles whose valuation word has period one or two are the fixed point (n=1), with valuation word ((2)) or its repetition ((2,2)).

**Proof for period one.** Here (D=1). The denominator (2^a-3) must be a positive divisor of 1, hence it equals 1. Thus (2^a=4), so (a=2), and (n=1).

**Proof for period two.** Let the word be ((a,b)), with (a,b\ge1). Then
\[
D=3+2^a,\qquad d=2^{a+b}-9.
\]
A positive cycle requires (d>0) and (d\mid D). In particular (d\le D), so
\[
2^{a+b}-9\le 2^a+3,
\quad\text{hence}\quad
2^a(2^b-1)\le12.
\]
Since (b\ge1), this forces (2^a\le12), hence (a\in\{1,2,3\}). The positivity condition (2^{a+b}>9), together with the displayed bound, leaves only:
- (a=1): (b\ge3), but then (d\ge7>D=5), impossible;
- (a=2): (b\ge2), and the bound forces (b=2). Then (d=7=D), giving (n=1);
- (a=3): (b\ge1). For (b=1), (d=7) does not divide (D=11); for (b\ge2), (d\ge23>D=11).

Thus only ((a,b)=(2,2)) occurs, and it gives (n=1). \(\square\)

This is an exact exclusion of nontrivial accelerated cycles with valuation period at most two. It does **not** exclude cycles with longer periods, nor does it establish that all trajectories reach the fixed point. The divisibility criterion remains a possible route for each fixed period, but a proof for arbitrary periods would need a uniform argument rather than a finite enumeration.

## 9. Exact exclusion of accelerated period three

The same divisibility criterion can be pushed one period further without an unbounded search.

Let the period-three valuation word be \((a,b,c)\), with all entries positive. Then
\[
A=a+b+c,\qquad D=9+3\cdot2^a+2^{a+b},\qquad d=2^{a+b+c}-27.
\]
A positive integer cycle requires \(d>0\) and \(d\mid D\), hence \(d\le D\). Rearranging the latter gives
\[
2^a\big(2^b(2^c-1)-3\big)\le36.
\tag{7}
\]
Write \(K=2^b(2^c-1)-3\).

If \(K>0\), then (7) and \(a\ge1\) imply \(K\le18\). The only positive pairs \((b,c)\) satisfying this are
\[
(1,2),(1,3),(2,1),(2,2),(3,1),(4,1).
\]
For each pair, (7) bounds \(a\), leaving the following finite list of positive-denominator cases. The entries show \((a,b,c;d,D)\):
\[
\begin{array}{c|c|c}
(b,c)&\text{allowed }a& (a;d,D)\\\hline
(1,2)&2,3&(2;5,29),\ (3;37,49)\\
(1,3)&1&(1;5,19)\\
(2,1)&2,3,4,5&(2;5,37),\ (3;37,65),\ (4;101,121),\ (5;229,233)\\
(2,2)&1,2&(1;5,23),\ (2;37,37)\\
(3,1)&1,2&(1;5,31),\ (2;37,53)\\
(4,1)&1&(1;37,47)
\end{array}
\]
Among these, the only divisibility \(d\mid D\) is \((a,b,c)=(2,2,2)\), where \(d=D=37\).

If \(K\le0\), positivity of \(b,c\) forces \((b,c)=(1,1)\), for which \(K=-1\). In this case
\[
d=2^{a+2}-27,\qquad D=9+5\cdot2^a.
\]
The conditions \(d>0\) and \(d\mid D\) imply \(d\mid(D-d)=2^a+36\), so
\[
4\cdot2^a-27\le2^a+36,
\]
hence \(2^a\le21\), and therefore \(a\le4\). Positivity gives \(a\ge3\). The two cases are \(a=3\), with \((d,D)=(5,49)\), and \(a=4\), with \((d,D)=(37,89)\); neither has \(d\mid D\).

**Theorem.** The only positive-integer accelerated Collatz cycle whose valuation word has period three is again the fixed point \(n=1\), with word \((2,2,2)\). \(\square\)

Together with the period-one and period-two results, this excludes every nontrivial accelerated cycle whose valuation word has period at most three. The argument is exact and finite, but its bounds do not yet provide a uniform exclusion for arbitrary periods.

## 10. A period-uniform valuation-pressure bound

The periodic-cycle formula yields a necessary condition independent of the order of the valuations.

For a positive accelerated cycle with valuation word of length \(p\), let
\[
A=\sum_{i=0}^{p-1}a_i.
\]
Its cycle denominator is \(2^A-3^p\). Since the cycle value is a positive integer, this denominator must be positive. Therefore
\[
2^A>3^p
\quad\Longleftrightarrow\quad
A>p\log_2 3.
\]
Writing the *excess valuation* as
\[
E=\sum_{i=0}^{p-1}(a_i-1)=A-p,
\]
we obtain the exact integer bound
\[
\boxed{E\ge\lfloor p(\log_2 3-1)\rfloor+1.}
\tag{8}
\]

Thus every periodic accelerated orbit must accumulate strictly more than \(0.58496\ldots\) units of valuation excess per step on average. In particular, the all-ones word is impossible at every period, and the required total excess grows linearly with the period.

This is a genuine period-uniform restriction, but it is only a necessary condition. It does not force the excess to occur at any particular positions, does not bound individual valuations, and does not prove that the divisibility condition
\[
2^A-3^p\mid D
\]
fails for all nontrivial words. The known fixed point has \(a_i=2\), so its excess per step is exactly one and comfortably satisfies (8).

### Period-four frontier (computation, not theorem)

For \((a,b,c,d)\), the exact numerator and denominator are
\[
D=27+9\cdot2^a+3\cdot2^{a+b}+2^{a+b+c},
\qquad
q=2^{a+b+c+d}-81.
\]
A positive cycle requires \(q>0\) and \(q\mid D\). An exhaustive finite search over \(1\le a,b,c,d\le20\) finds only \((2,2,2,2)\), yielding \(n=1\). This is a bounded computational check only: it is not an exclusion theorem for all positive quadruples, because the valuation variables have not been bounded by a proof. The period-four theorem therefore remains open.

## 11. Exact exclusion of accelerated period four

Let the four positive valuations be \((a,b,c,d)\), with total
\[
A=a+b+c+d.
\]
The periodic formula specializes to
\[
q=2^A-81,
\qquad
D=27+9\cdot2^a+3\cdot2^{a+b}+2^{a+b+c}.
\]
A positive integer cycle requires \(q>0\), \(q\mid D\), and its starting odd integer is \(n=D/q\).

Write \(A_j=a_0+\cdots+a_{j-1}\), with \(A_0=0\). Since the four valuations are positive, the remaining \(4-j\) terms have sum at least \(4-j\), so
\[
A_j\le A-(4-j).
\]
Consequently,
\[
D=\sum_{j=0}^{3}2^{A_j}3^{3-j}
\le 2^{A-4}\sum_{j=0}^{3}2^j3^{3-j}
=65\cdot2^{A-4}.
\]
For \(A\ge9\), this gives
\[
0<n=\frac Dq
\le\frac{65\cdot2^{A-4}}{2^A-81}
=\frac{65/16}{1-81/2^A}
\le\frac{65/16}{1-81/512}
<5.
\]
Both \\(D\\) and \\(q\\) are odd, hence \\(n\\) is odd. Thus \\(n\\in\\{1,3\\}\\). The value \\(n=3\\) cannot be periodic, since its accelerated trajectory is \\(3\\mapsto5\\mapsto1\\mapsto1\\). If \\(n=1\\), every step has valuation \\(v_2(3\\cdot1+1)=2\\), so the four-step total is necessarily \\(A=8\\), contradicting \\(A\\ge9\\). Hence no cycle with \\(A\\ge9\\) exists.

It remains to handle \(A<9\). The condition \(q>0\) gives \(2^A>81\), hence \(A\ge7\); therefore only \(A=7,8\) remain. There are respectively
\[
\binom{6}{3}=20,\qquad \binom{7}{3}=35
\]
positive compositions of these totals into four ordered parts. Direct substitution into the displayed formula for \(D\) gives the following complete residue check (words are in lexicographic order):
\[
\begin{array}{c|l}
A & D\bmod q\text{ in lexicographic word order}\\\hline
7 & 18,26,42,27,38,7,39,31,16,17,9,25,10,2,34,35,38,23,24,2\\
8 & 65,73,89,121,10,85,101,133,22,125,157,46,30,94,15,103,119,151,40,143,0,64,48,112,33,4,36,100,84,148,69,156,45,141,110
\end{array}
\]
For \(A=7\), none of the residues is zero. For \(A=8\), the unique zero residue occurs at \((a,b,c,d)=(2,2,2,2)\), for which \(D=q=175\) and \(n=1\).

**Theorem.** The only positive-integer accelerated Collatz cycle whose valuation word has period four is the fixed point \(1\), with valuation word \((2,2,2,2)\).

Together with the period-one, period-two, and period-three exclusions above, this proves that no nontrivial accelerated cycle can have a valuation word of period at most four. It does not exclude cycles with longer valuation periods and does not prove global termination.

## 12. Exact exclusion of accelerated period five

For a five-step valuation word \((a,b,c,d,e)\), put
\[
A=a+b+c+d+e,\qquad q=2^A-3^5=2^A-243.
\]
The periodic numerator is
\[
D=81+27\cdot2^a+9\cdot2^{a+b}
  +3\cdot2^{a+b+c}+2^{a+b+c+d}.
\]
A positive integer five-cycle requires \(q>0\), \(q\mid D\), and \(n=D/q\).

As all five valuations are positive, the partial sums obey
\[
A_j\le A-(5-j)\qquad(0\le j\le4).
\]
Hence
\[
D=\sum_{j=0}^4 2^{A_j}3^{4-j}
\le 2^{A-5}(81+54+36+24+16)
=211\cdot2^{A-5}.
\]
Also \(D\) and \(q\) are odd, so \(n\) is odd. For \(A\ge10\),
\[
0<n\le\frac{211\cdot2^{A-5}}{2^A-243}
\le\frac{211\cdot2^5}{2^{10}-243}
=\frac{6752}{781}<9.
\]
The fraction decreases as \(A\) increases. Thus \(n\in\{1,3,5,7\}\). Under the accelerated map,
\[
3\mapsto5\mapsto1,\qquad
5\mapsto1,\qquad
7\mapsto11\mapsto17\mapsto13\mapsto5\mapsto1.
\]
None of \(3,5,7\) returns to itself after five steps. The only candidate is \(n=1\), whose valuation is 2 at every step; its five-step valuation total is exactly \(A=10\). Therefore the only five-step cycle in the range \(A\ge10\) is the fixed point.

Since \(q>0\) forces \(A\ge8\), the remaining totals are \(A=8,9\). They have respectively 35 and 70 positive ordered compositions into five parts. The accompanying exact-integer certificate checks every composition: for \(A=8\), \(q=13\) and there are zero divisibility hits; for \(A=9\), \(q=269\) and there are zero hits. The reproducible script is certificates/collatz_period5_exact.py.

**Theorem.** The only positive-integer accelerated Collatz orbit satisfying \(S^5(n)=n\) is \(n=1\). Equivalently, no nontrivial accelerated cycle has valuation-word period five.

Together with the previous sections, no nontrivial accelerated cycle has valuation-word period at most five. This is a cycle exclusion result, not a proof that every positive integer orbit terminates.

## 13. Exact exclusion of accelerated period six

For a six-step valuation word \((a,b,c,d,e,f)\), write
\[
A=a+b+c+d+e+f,\qquad q=2^A-3^6=2^A-729.
\]
The periodic numerator is
\[
D=243+81\cdot2^a+27\cdot2^{a+b}
 +9\cdot2^{a+b+c}+3\cdot2^{a+b+c+d}
 +2^{a+b+c+d+e}.
\]
A positive integer six-cycle requires \(q>0\), \(q\mid D\), and \(n=D/q\).

Positivity of all six valuations gives
\[
D=\sum_{j=0}^{5}2^{A_j}3^{5-j}
\le 2^{A-6}(243+162+108+72+48+32)
=665\cdot2^{A-6}.
\]
The numerator and denominator are odd, so \(n\) is odd. For \(A\ge12\),
\[
0<n\le\frac{665\cdot2^{A-6}}{2^A-729}
\le\frac{665\cdot2^6}{2^{12}-729}
=\frac{42560}{3367}<13.
\]
The bound decreases with \(A\). Thus \(n\in\{1,3,5,7,9,11\}\). The accelerated trajectories of the nontrivial candidates are
\[
3\mapsto5\mapsto1,\quad
5\mapsto1,\quad
7\mapsto11\mapsto17\mapsto13\mapsto5\mapsto1,
\]
\[
9\mapsto7,\qquad
11\mapsto17\mapsto13\mapsto5\mapsto1.
\]
Every candidate above 1 reaches 1 before returning to itself. The candidate \(n=1\) has valuation 2 at every step, hence total valuation \(A=12\). Therefore no nontrivial six-cycle exists when \(A\ge12\).

The condition \(q>0\) forces \(A\ge10\), leaving totals \(A=10,11\). The numbers of positive ordered six-part compositions are respectively
\[
\binom{9}{5}=126,\qquad \binom{10}{5}=252.
\]
The exact-integer certificate certificates/collatz_period6_exact.py checks all 378 words and finds no divisibility hits (the denominators are 295 and 1319, respectively).

**Theorem.** The only positive-integer accelerated Collatz orbit satisfying \(S^6(n)=n\) is \(n=1\). Thus no nontrivial accelerated cycle has valuation-word period six.

Combined with the previous results, no nontrivial accelerated cycle has valuation-word period at most six. Longer periods and global termination remain open.

## 14. Exact exclusion of accelerated period seven

For a seven-step valuation word \((a_0,\ldots,a_6)\), put
\[
A=\sum_{i=0}^{6}a_i,\qquad q=2^A-3^7=2^A-2187.
\]
Its periodic numerator is
\[
D=729+243\cdot2^{a_0}+81\cdot2^{a_0+a_1}
 +27\cdot2^{a_0+a_1+a_2}
 +9\cdot2^{a_0+a_1+a_2+a_3}
 +3\cdot2^{a_0+\cdots+a_4}
 +2^{a_0+\cdots+a_5}.
\]
As all valuations are positive,
\[
D=\sum_{j=0}^{6}2^{A_j}3^{6-j}
\le2^{A-7}(729+486+324+216+144+96+64)
=2059\cdot2^{A-7}.
\]
A positive seven-cycle requires \(q>0\), hence \(A\ge12\). The quotient \(n=D/q\) is odd because both numerator and denominator are odd. For \(A\ge16\),
\[
0<n\le\frac{2059\cdot2^{A-7}}{2^A-2187}
\le\frac{2059\cdot2^9}{2^{16}-2187}
=\frac{1,054,208}{63,349}<17.
\]
The bound decreases with \(A\), so \(n\in\{1,3,5,7,9,11,13,15\}\). Their accelerated trajectories, other than the fixed point 1, all reach 1 before returning to their starting value:
\[
3\mapsto5\mapsto1,\quad 5\mapsto1,\quad
7\mapsto11\mapsto17\mapsto13\mapsto5\mapsto1,
\]
\[
9\mapsto7,\quad
11\mapsto17\mapsto13\mapsto5\mapsto1,\quad
13\mapsto5,
\]
\[
15\mapsto23\mapsto35\mapsto53\mapsto5\mapsto1.
\]
Thus no nontrivial seven-cycle is possible for \(A\ge16\). The fixed point 1 has valuation 2 at every step, so its seven-step total is \(A=14\), not in this large-total range.

For \(A=12,13,14,15\), the numbers of positive ordered seven-part compositions are respectively
\[
\binom{11}{6}=462,\quad
\binom{12}{6}=924,\quad
\binom{13}{6}=1716,\quad
\binom{14}{6}=3003.
\]
The exact-integer certificate certificates/collatz_period7_exact.py checks all 6,105 words. Its unique divisibility hit is \(A=14\), word \((2,2,2,2,2,2,2)\), with \(D=q=14197\) and \(n=1\).

**Theorem.** The only positive-integer accelerated Collatz orbit satisfying \(S^7(n)=n\) is \(n=1\). Hence no nontrivial accelerated cycle has valuation-word period seven. Combined with the previous sections, no nontrivial accelerated cycle has period at most seven. This does not prove global termination.


## 15. Exact exclusion of accelerated period eight

For an eight-step valuation word \((a_0,\ldots,a_7)\), put
\[
A=\sum_{i=0}^{7}a_i,\qquad q=2^A-3^8=2^A-6561.
\]
The periodic numerator is
\[
\begin{aligned}
D={}&2187+729\cdot2^{a_0}+243\cdot2^{a_0+a_1}
 +81\cdot2^{a_0+a_1+a_2}\\
&+27\cdot2^{a_0+a_1+a_2+a_3}
 +9\cdot2^{a_0+\cdots+a_4}
 +3\cdot2^{a_0+\cdots+a_5}
 +2^{a_0+\cdots+a_6}.
\end{aligned}
\]
A positive integer orbit satisfying \(S^8(n)=n\) requires \(q>0\), \(q\mid D\), and \(n=D/q\). In particular, \(A\ge13\).

As every valuation is positive, the first \(j\) valuations have sum at most \(A-(8-j)\). Therefore
\[
D=\sum_{j=0}^{7}2^{A_j}3^{7-j}
\le2^{A-8}\sum_{j=0}^{7}2^j3^{7-j}
=6305\cdot2^{A-8}.
\]
Both \(D\) and \(q\) are odd, so \(n\) is odd. For \(A\ge18\), the bound is decreasing in \(A\), and
\[
0<n\le\frac{6305\cdot2^{A-8}}{2^A-6561}
\le\frac{6305\cdot2^{10}}{2^{18}-6561}
=\frac{6,456,320}{255,583}<26.
\]
Thus \(n\in\{1,3,5,7,9,11,13,15,17,19,21,23,25\}\). Every candidate above 1 reaches 1 before returning:
\[
\begin{gathered}
3\to5\to1,\quad 5\to1,\quad
7\to11\to17\to13\to5\to1,\\
9\to7\to11\to17\to13\to5\to1,\quad
11\to17\to13\to5\to1,\\
13\to5\to1,\quad
15\to23\to35\to53\to5\to1,\quad
17\to13\to5\to1,\\
19\to29\to11\to17\to13\to5\to1,\quad
21\to1,\\
23\to35\to53\to5\to1,\quad
25\to19\to29\to11\to17\to13\to5\to1.
\end{gathered}
\]
The fixed point 1 has valuation 2 at every step and hence total valuation \(A=16\), outside this range. No nontrivial eight-cycle is possible for \(A\ge18\).

The remaining totals are \(A=13,14,15,16,17\). Their numbers of positive ordered eight-part compositions are
\[
\binom{12}{7}=792,\quad
\binom{13}{7}=1716,\quad
\binom{14}{7}=3432,\quad
\binom{15}{7}=6435,\quad
\binom{16}{7}=11440.
\]
The exact-integer certificate `certificates/collatz_period8_exact.py` checks all 23,815 words. Its unique divisibility hit is \(A=16\), word \((2,2,2,2,2,2,2,2)\), with \(D=q=58,975\) and \(n=1\).

**Theorem.** The only positive-integer accelerated Collatz orbit satisfying \(S^8(n)=n\) is \(n=1\). Hence no nontrivial accelerated cycle has period eight. Combined with the preceding sections, no nontrivial accelerated cycle has period at most eight. This finite-period exclusion does not prove global termination.


## 16. Exact exclusion of accelerated period nine

For a nine-step valuation word \((a_0,\ldots,a_8)\), put
\[
A=\sum_{i=0}^{8}a_i,\qquad q=2^A-3^9=2^A-19683.
\]
The periodic numerator is
\[
D=\sum_{j=0}^{8}3^{8-j}2^{A_j},\qquad
A_0=0,\quad A_j=\sum_{i=0}^{j-1}a_i.
\]
Explicitly its coefficients are \(6561,2187,729,243,81,27,9,3,1\). A positive integer orbit satisfying \(S^9(n)=n\) requires \(q>0\), \(q\mid D\), and \(n=D/q\); hence \(A\ge15\).

Since each valuation is positive, \(A_j\le A-9+j\), and therefore
\[
D\le2^{A-9}\sum_{j=0}^{8}2^j3^{8-j}
=19171\cdot2^{A-9}.
\]
Both \(D\) and \(q\) are odd, so \(n\) is odd. For \(A\ge19\), the quotient bound decreases with \(A\), giving
\[
0<n\le\frac{19171\cdot2^{A-9}}{2^A-19683}
\le\frac{19171\cdot2^{10}}{2^{19}-19683}
=\frac{19,631,104}{504,605}<39.
\]
Thus \(n\in\{1,3,5,\ldots,37\}\). Every candidate above 1 reaches 1 under the accelerated map:
\[
\begin{aligned}
3&\to5\to1, &5&\to1,\\
7&\to11\to17\to13\to5\to1, &
9&\to7\to11\to17\to13\to5\to1,\\
11&\to17\to13\to5\to1, &
13&\to5\to1,\\
15&\to23\to35\to53\to5\to1, &
17&\to13\to5\to1,\\
19&\to29\to11\to17\to13\to5\to1, &
21&\to1,\\
23&\to35\to53\to5\to1, &
25&\to19\to29\to11\to17\to13\to5\to1,\\
27&\to41\to31\to47\to71\to107\to161\to121\to91\to137
\to103\to155\to233\to175\to263\to395\to593\to445\to167
\to251\to377\to283\to425\to319\to479\to719\to1079
\to1619\to2429\to911\to1367\to2051\to3077\to577\to433
\to325\to61\to23\to35\to53\to5\to1,\\
29&\to11\to17\to13\to5\to1, &
31&\to47\to71\to107\to161\to121\to91\to137\to103
\to155\to233\to175\to263\to395\to593\to445\to167
\to251\to377\to283\to425\to319\to479\to719\to1079
\to1619\to2429\to911\to1367\to2051\to3077\to577\to433
\to325\to61\to23\to35\to53\to5\to1,\\
33&\to25\to19\to29\to11\to17\to13\to5\to1, &
35&\to53\to5\to1,\\
37&\to7\to11\to17\to13\to5\to1.
\end{aligned}
\]
The fixed point 1 has valuation 2 at every step, so its nine-step total is \(A=18\), not in this large-total range. Hence no nontrivial nine-cycle exists for \(A\ge19\).

For \(A=15,16,17,18\), the numbers of positive ordered nine-part compositions are
\[
\binom{14}{8}=3003,\quad
\binom{15}{8}=6435,\quad
\binom{16}{8}=12870,\quad
\binom{17}{8}=24310.
\]
The exact-integer certificate `certificates/collatz_period9_exact.py` checks all 46,618 words. Its unique divisibility hit is \(A=18\), word \((2,2,2,2,2,2,2,2,2)\), with \(D=q=242461\) and \(n=1\).

**Theorem.** The only positive-integer accelerated Collatz orbit satisfying \(S^9(n)=n\) is \(n=1\). Thus no nontrivial accelerated cycle has period nine. Together with the preceding results, all nontrivial accelerated cycles of periods at most nine are excluded. This does not prove global termination.
