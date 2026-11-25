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


## 17. A period-uniform numerator bound and its limitation

The periodic-point identity has a closed-form bound for every period. Let
\[
A=\sum_{i=0}^{p-1}a_i,\qquad
A_j=\sum_{i=0}^{j-1}a_i,\qquad
D=\sum_{j=0}^{p-1}3^{p-1-j}2^{A_j}.
\]
Since every \(a_i\ge1\), one has \(A_j\le A-p+j\). Thus
\[
\begin{aligned}
D
&\le 2^{A-p}\sum_{j=0}^{p-1}2^j3^{p-1-j}\\
&=2^{A-p}(3^p-2^p).
\end{aligned}
\]
The denominator is \(q=2^A-3^p\), and a positive integer cycle requires \(q>0\). Writing the excess valuation as \(E=A-p\), this yields
\[
\boxed{
n\le
\frac{(3/2)^p-1}{1-(3/2)^p/2^E}
},\qquad
E>p\log_2(3/2).
\]
For fixed \(p\), the right-hand side decreases as \(E\) increases. But it does not provide a period-independent bound on \(n\): even when \(E\) is much larger than its required threshold, the numerator scale is \((3/2)^p\). Near the threshold, the denominator can also be small.

This pinpoints the limitation of the finite-period strategy. It supplies a finite starting-value search for each fixed period after choosing a sufficiently large total valuation, but the search range is not uniformly bounded as \(p\to\infty\). Consequently, the period-by-period argument cannot by itself exclude all periods.

**Next structural target.** Improve the numerator estimate by exploiting the divisibility condition \(2^A-3^p\mid D\), the exact valuation constraints along the orbit, or correlations between consecutive valuations. Any successful uniform argument must use information beyond positivity of the individual \(a_i\). This section is a bound and a diagnosis of its limitation, not a new Collatz theorem.


## 18. Exact multiplicative balance along a hypothetical cycle

Let \(n_0,\ldots,n_{p-1}\) be a positive accelerated cycle, with indices read cyclically and
\[
2^{a_i}n_{i+1}=3n_i+1.
\]
Multiplying all p equations cancels the cyclic product of the \(n_i\):
\[
2^A=\prod_{i=0}^{p-1}\left(3+\frac1{n_i}\right).
\]
Equivalently,
\[
\boxed{
A\log2-p\log3
=\sum_{i=0}^{p-1}\log\left(1+\frac1{3n_i}\right).
}
\]
This is an exact identity, not an asymptotic estimate.

It immediately gives
\[
p\log_2 3<A<2p
\]
for every nontrivial positive cycle. The lower inequality follows because every summand on the right is positive. For the upper inequality, each summand is at most \(\log(4/3)\), with strict inequality at any cycle element greater than 1; a nontrivial cycle has such an element. Since \(\log3+\log(4/3)=\log4=2\log2\), the upper bound follows. The all-one cycle is the exceptional fixed point, with \(A=2p\).

There is also a minimum-element constraint. If \(m=\min_i n_i\), then
\[
0<A\log2-p\log3
\le p\log\left(1+\frac1{3m}\right),
\]
and hence
\[
m\le
\frac{1}{3\left(\exp((A\log2-p\log3)/p)-1\right)}.
\]
Thus a hypothetical cycle whose average valuation lies noticeably above \(\log_2 3\) must contain a relatively small element. This is a necessary condition only; by itself it does not exclude cycles, because the excess can be arbitrarily close to zero as p varies.

**Research use.** Combine this multiplicative balance with the affine divisibility condition and the cyclic rotation constraints on the valuation word. The former records the exact product of local expansion factors; the latter records the exact additive contributions of the (+1) terms. A cycle-exclusion argument may need both simultaneously.


## 19. Exact exclusion of accelerated period ten

A useful refinement of the period-by-period argument is that a nontrivial cycle has a distinguished cyclic starting point. Let (m>1) be the smallest odd member of a hypothetical cycle. Since its successor is at least (m),
[
2^{a(m)}m\le 3m+1,
]
and (m\ge3) forces (2^{a(m)}<4). Thus (a(m)=1). Every nontrivial period-ten valuation word can therefore be cyclically rotated so that its first entry is 1 and its initial integer is the cycle minimum.

For a ten-step word, put
[
A=\sum_{i=0}^{9}a_i,\qquad
D=\sum_{j=0}^{9}3^{9-j}2^{A_j},\qquad
q=2^A-3^{10}=2^A-59049.
]
A positive integer cycle requires (q>0), (q\mid D), and
[
n=\frac Dq.
]
Since (D\le(3^{10}-2^{10})2^{A-10}=58025\,2^{A-10}), for every (A\ge24),
[
n\le\frac{58025\,2^{A-10}}{2^A-59049}
\le\frac{58025\,2^{14}}{2^{24}-59049}
<57.
]
The middle expression decreases with (A). Since the initial member is the cycle minimum and is odd, it must be one of
[
3,5,7,\ldots,55.
]
Direct accelerated trajectories from each of these 27 candidates reach 1 (the longest listed here is 27, which reaches 1 in 41 accelerated steps). Hence no nontrivial period-ten cycle can have (A\ge24).

It remains to check (16\le A\le23), because (2^{15}<3^{10}<2^{16}). The minimum-element rotation lets us enumerate only positive compositions with (a_0=1). Their counts are
[
\binom{14}{8},\binom{15}{8},\ldots,\binom{21}{8}
=
3003,6435,12870,24310,43758,75582,125970,203490,
]
for a total of 495,418 words. The exact-integer certificate `certificates/collatz_period10_exact.py` checks (q\mid D) for every such word; there are no divisibility hits.

**Theorem.** The only positive integer satisfying (S^{10}(n)=n) is (n=1). Thus there is no nontrivial accelerated Collatz cycle of period ten. Together with the preceding period results, nontrivial periods through ten are excluded. This remains a finite-period theorem, not a proof of global Collatz termination.


## 20. Minimum-residue constraint and a sharper average-valuation window

Let (m>1) be the smallest odd member of a hypothetical nontrivial accelerated cycle. The minimum-element argument in Section 19 gives (a(m)=1). Exact valuation one means
[
3m+1\equiv2\pmod4,
]
so
[
\boxed{m\equiv3\pmod4.}
]
In particular, (m\ge3).

For every cycle member (n_i\ge m), and the exact multiplicative balance from Section 18 yields
[
2^A
=\prod_{i=0}^{p-1}\left(3+\frac1{n_i}\right)
\le\left(3+\frac1m\right)^p
\le\left(\frac{10}{3}\right)^p.
]
Together with (2^A>3^p), this proves the sharper necessary window
[
\boxed{
p\log_2 3<A\le p\log_2\left(3+\frac1m\right)
\le p\log_2\frac{10}{3}.
}
]
Thus every nontrivial cycle has average valuation in
[
1.5849625\ldots<\frac Ap\le1.7369656\ldots.
]
The upper endpoint is strict for a nontrivial cycle if at least one cycle member exceeds (m=3); the weak inequality above is sufficient and avoids needing a separate case split.

This is a period-uniform restriction on the total valuation, and it sharpens the crude upper bound (A<2p). It does not bound (p), nor does it exclude cycles: the interval still contains admissible integer totals for arbitrarily large periods. Its value is as a pruning condition for exact searches and as a constraint to combine with the affine divisibility condition.


## 21. Exact exclusion of accelerated period eleven

The strict average-valuation window from Section 20 is particularly effective at period eleven:
\[
11\log_2 3<A<11\log_2\left(\frac{10}{3}\right).
\]
Numerically, the endpoints lie strictly between 17 and 18, and between 19 and 20, respectively. Since \(A\) is an integer,
\[
\boxed{A\in\{18,19\}.}
\]
This eliminates every other total valuation before any word enumeration.

Rotate a hypothetical nontrivial cycle to its smallest odd member. Its first valuation is 1, and the periodic-point identity becomes
\[
q=2^A-3^{11},\qquad
D=\sum_{j=0}^{10}3^{10-j}2^{A_j},\qquad
q\mid D.
\]
For \(A=18\), there are
\[
\binom{16}{9}=11,440
\]
positive ten-part tails after fixing \(a_0=1\). For \(A=19\), there are
\[
\binom{17}{9}=24,310.
\]
The exact-integer certificate certificates/collatz_period11_exact.py checks all 35,750 words. No word satisfies \(q\mid D\).

**Theorem.** The only positive integer satisfying \(S^{11}(n)=n\) is \(n=1\). Hence there is no nontrivial accelerated cycle of period eleven. The proof uses the minimum-element valuation constraint, the strict average-valuation window, and a finite exact divisibility check. It does not establish global termination.


## 22. Exact exclusion of accelerated period twelve

For a nontrivial period-twelve cycle, Section 20 gives
\[
12\log_2 3<A<12\log_2(10/3).
\]
The exact integer comparisons
\[
2^{19}<3^{12}<2^{20},
\\qquad
2^{20}3^{12}<10^{12}<2^{21}3^{12}
\]
show that the lower endpoint is greater than 19 and the upper endpoint is less than 21. Hence
\[
\boxed{A=20.}
\]

Rotate the cycle to its smallest odd member, so that \(a_0=1\). Then the periodic-point denominator is
\[
q=2^{20}-3^{12}=517135,
\]
and the numerator is
\[
D=\sum_{j=0}^{11}3^{11-j}2^{A_j}.
\]
There are
\[
\binom{18}{10}=43,758
\]
positive eleven-part tails with total 19. The exact-integer certificate certificates/collatz_period12_exact.py checks all 43,758 resulting valuation words and finds no divisibility hit \(q\mid D\).

**Theorem.** The only positive integer satisfying \(S^{12}(n)=n\) is \(n=1\). Thus no nontrivial accelerated cycle has period twelve. This is a finite-period exclusion, not a proof of global termination.


## 23. Exact exclusion of accelerated period thirteen

The strict average-valuation window gives
\[
13\log_2 3<A<13\log_2(10/3).
\]
Exact integer comparisons
\[
2^{20}<3^{13}<2^{21},
\\qquad
2^{22}3^{13}<10^{13}<2^{23}3^{13}
\]
force
\[
\boxed{A\in\{21,22\}.}
\]

Rotate a hypothetical nontrivial cycle to its smallest odd member, so \(a_0=1\). For each admissible total, define
\[
q_A=2^A-3^{13},\qquad
D=\sum_{j=0}^{12}3^{12-j}2^{A_j}.
\]
The cycle condition requires \(q_A\mid D\). The two exact searches are:

| \(A\) | \(q_A\) | Words checked | Divisibility hits |
|---:|---:|---:|---:|
| 21 | 502,829 | 75,582 | 0 |
| 22 | 2,599,981 | 167,960 | 0 |
| **Total** | — | **243,542** | **0** |

The certificate certificates/collatz_period13_exact.py enumerates every positive twelve-part tail after fixing \(a_0=1\), and performs the divisibility tests with integer arithmetic only.

**Theorem.** The only positive integer satisfying \(S^{13}(n)=n\) is \(n=1\). Thus there is no nontrivial accelerated cycle of period thirteen. This finite-period result is not a proof of global termination.


## 24. Exact exclusion of accelerated period fourteen

The strict average-valuation window gives
\[
14\log_2 3<A<14\log_2(10/3).
\]
Exact integer comparisons
\[
2^{22}<3^{14}<2^{23},
\\qquad
2^{24}3^{14}<10^{14}<2^{25}3^{14}
\]
force
\[
\boxed{A\in\{23,24\}.}
\]

Rotate a hypothetical nontrivial cycle to its smallest odd member, so \(a_0=1\). Put
\[
q_A=2^A-3^{14},\qquad
D=\sum_{j=0}^{13}3^{13-j}2^{A_j}.
\]
A cycle requires \(q_A\mid D\). Exact enumeration of all positive thirteen-part tails gives:

| \(A\) | \(q_A\) | Words checked | Divisibility hits |
|---:|---:|---:|---:|
| 23 | 3,605,639 | 293,930 | 0 |
| 24 | 11,994,247 | 646,646 | 0 |
| **Total** | — | **940,576** | **0** |

The companion certificate certificates/collatz_period14_exact.py generates all these words and tests divisibility using integer arithmetic.

**Theorem.** The only positive integer satisfying \(S^{14}(n)=n\) is \(n=1\). Hence no nontrivial accelerated cycle has period fourteen. This remains a finite-period exclusion, not a proof of global termination.


## 25. Exact exclusion of accelerated period fifteen

The strict average-valuation window gives
\[
15\log_2 3<A<15\log_2(10/3).
\]
Exact comparisons
\[
2^{23}<3^{15}<2^{24},
\\qquad
2^{26}3^{15}<10^{15}<2^{27}3^{15}
\]
force
\[
\boxed{A\in\{24,25,26\}.}
\]

Rotate a hypothetical nontrivial cycle to its smallest odd member, giving \(a_0=1\). Set
\[
q_A=2^A-3^{15},\qquad
D=\sum_{j=0}^{14}3^{14-j}2^{A_j}.
\]
The cycle condition requires \(q_A\mid D\). The exact enumeration gives:

| \(A\) | \(q_A\) | Words checked | Divisibility hits |
|---:|---:|---:|---:|
| 24 | 2,428,309 | 497,420 | 0 |
| 25 | 19,205,525 | 1,144,066 | 0 |
| 26 | 52,759,957 | 2,496,144 | 0 |
| **Total** | — | **4,137,630** | **0** |

The certificate certificates/collatz_period15_exact.py uses the recurrence \(D_{j+1}=3D_j+2^{A_j}\), so every divisibility test is performed with exact integers.

**Theorem.** The only positive integer satisfying \(S^{15}(n)=n\) is \(n=1\). Thus there is no nontrivial accelerated cycle of period fifteen. This does not establish global termination.


## 26. Suffix congruences modulo powers of three

Use the exclusive prefix sums
\[
B_0=0,\qquad B_j=\sum_{i=0}^{j-1}a_i\ (1\le j\le p),
\qquad B_p=A.
\]
The exact periodic identity from Section 4 is
\[
(2^A-3^p)n
=\sum_{j=0}^{p-1}3^{p-1-j}2^{B_j}.
\]
For \(1\le r\le p\), reduction modulo \(3^r\) removes precisely the terms with \(j<p-r\):
\[
\boxed{
2^A n\equiv
\sum_{j=p-r}^{p-1}3^{p-1-j}2^{B_j}
\pmod{3^r}.}
\tag{26.1}
\]
The family is nested under reduction from \(3^{r+1}\) to \(3^r\).

At \(r=1\), only the final summand remains:
\[
2^A n\equiv2^{B_{p-1}}\pmod3,
\]
so, writing \(b=a_{p-1}=A-B_{p-1}\),
\[
\boxed{2^b n\equiv1\pmod3.}
\tag{26.2}
\]
This is a congruence modulo \(3\), not modulo \(3^p\).

At the other endpoint \(r=p\), all \(p\) summands remain; there is no single-term simplification. The full congruence is simply the original cycle identity reduced modulo \(3^p\).

**Interpretation.** The terminal valuation determines the starting member modulo \(3\), while longer suffixes provide progressively more detailed constraints involving several terminal valuations. They do not yield \(2^b n\equiv1\pmod{3^p}\).

## 27. CRT restriction on the minimum cycle member

Let \(m>1\) be the smallest odd member of a hypothetical accelerated cycle of length \(p\), and let \(b=a_{p-1}\) be the final valuation in the chosen cyclic ordering. The minimum-member argument gives
\[
m\equiv3\pmod4,
\]
while the full suffix congruence gives
\[
2^b m\equiv1\pmod{3^p}.
\]
Thus
\[
m\equiv 2^{-b}\pmod{3^p}.
\]

Because \(4\) and \(3^p\) are coprime, the Chinese remainder theorem gives a unique residue class
\[
\boxed{m\equiv M_{p,b}\pmod{4\cdot3^p},}
\]
where \(M_{p,b}\) is the unique class satisfying
\[
M_{p,b}\equiv3\pmod4,
\qquad
2^bM_{p,b}\equiv1\pmod{3^p}.
\]
The representative can be computed exactly: first take the least positive residue \(u\equiv(2^b)^{-1}\pmod{3^p}\), then choose the unique one of \(u,u+3^p,u+2\cdot3^p,u+3\cdot3^p\) congruent to 3 modulo 4.

Consequently, any independent upper bound \(m<4\cdot3^p\) would force \(m=M_{p,b}\) (with the representative chosen in \([1,4\cdot3^p]\)); a stronger bound can eliminate the candidate outright if \(M_{p,b}\) is too large. This is a finite exact test once \(b\) is bounded by the total valuation \(A\).

**Status.** This is a necessary CRT filter, not a new cycle exclusion theorem. The outstanding step is to prove a sufficiently strong upper bound for the minimum member, or to combine this residue with the earlier itinerary divisibility equation in a way that rules out all possible \(b\) uniformly.


The CRT representative has the explicit formula
\[
u=\operatorname{leastpos}(2^{-b}\bmod 3^p),\qquad
k\equiv(-1)^p(3-u)\pmod4,\quad 0\le k\le3,
\]
\[
\boxed{M_{p,b}=u+k3^p.}
\]
Here \((-1)^p\) is interpreted modulo 4. Also, because every valuation is at least one,
\[
1\le b\le A-p+1
< p\log_2(10/3)-p+1.
\]
Thus for each fixed period there are only linearly many terminal-valuation CRT candidates to test, before any of the interior itinerary constraints are applied.


## 28. A second-modulus obstruction for the minimum member

The terminal suffix congruence says
\[
2^b m\equiv1\pmod{3^p},\qquad b=a_{p-1}.
\]
Thus there is a positive integer \(k\) with
\[
2^b m=1+k3^p.
\tag{28.1}
\]
For a nontrivial cycle, the minimum member satisfies \(m\equiv3\pmod4\). Substituting this into (28.1) modulo \(2^{b+2}\) yields
\[
\boxed{k3^p\equiv3\cdot2^b-1\pmod{2^{b+2}}.}
\tag{28.2}
\]
Since \(3^p\) is invertible modulo \(2^{b+2}\), this fixes \(k\) to one residue class. Let \(\kappa_{p,b}\) be its least positive representative:
\[
\kappa_{p,b}
=\operatorname{leastpos}\left((3\cdot2^b-1)(3^p)^{-1}
\bmod 2^{b+2}\right).
\]
Every possible cycle therefore has \(k\ge\kappa_{p,b}\).

The minimum-member product bound gives
\[
m<\frac1{2^{A/p}-3},
\]
so (28.1) also gives
\[
k<\frac{2^b}{3^p(2^{A/p}-3)}.
\]
Consequently, the exact inequality
\[
\boxed{
2^A(\kappa_{p,b}3^p)^p
\ge (3\kappa_{p,b}3^p+2^b)^p
}
\tag{28.3}
\]
is sufficient to rule out that pair \((A,b)\). This is an integer-only test: it is equivalent to saying that the least permitted positive \(k\) is already at least the upper bound forced by the minimum-member estimate.

For \(3\le p\le100\), an exact integer sweep over every admissible total \(A\) and every \(1\le b\le A-p+1\) verified (28.3) in every case. The reproducible finite-range check is in certificates/collatz_crt_minimum_filter.py. This is computational evidence for a useful obstruction, not a proof that (28.3) holds for every period. Establishing that uniform inequality—or finding a different uniform argument—remains open.


## 29. Exact reduction and audit of the finite CRT sweep

The sufficient obstruction in (28.3) has a simpler equivalent form. All quantities are positive, so taking the positive real \(p\)-th root shows that (28.3) is equivalent to
\[
\boxed{
\kappa_{p,b}3^p\bigl(2^{A/p}-3\bigr)\ge 2^b.
}
\tag{29.1}
\]
This equivalence is algebraic; it does not approximate the fractional power. The integer-power form (28.3) remains preferable for a fully exact computational check.

Since \(b\le A-p+1\) and \(\kappa_{p,b}\ge1\), a simpler sufficient condition for a pair \((p,A,b)\) is
\[
3^p\bigl(2^{A/p}-3\bigr)\ge2^{A-p+1}.
\tag{29.2}
\]
However, (29.2) is not established here uniformly over all admissible periods. In particular, the fact that (28.3) holds in the finite sweep does not justify replacing the sweep by an unproved asymptotic claim.

The certificate certificates/collatz_crt_minimum_filter.py was independently rerun with Python. It completed all loops for \(3\le p\le100\), verified (28.3) for every admissible \((p,A,b)\), and reproduced the count 34,838. All calculations use integer modular inverses and integer powers; no floating-point comparison is used in the certificate.

**Scope.** The verified statement is precisely the finite-range assertion \(3\le p\le100\). The CRT congruence, the reduction (29.1), and the sufficient condition (29.2) are general. No period-uniform inequality has been proved, and no global Collatz conclusion follows from this finite sweep.


## 30. Audit of the simplified CRT bound: two exceptional pairs

The sufficient condition (29.2), obtained by replacing the exact CRT representative by the coarse bound \(\kappa_{p,b}\ge1\), is not valid for every admissible pair. In the range \(3\le p\le100\), its only failures are
\[
\boxed{(p,A)=(3,5)\quad\text{and}\quad(p,A)=(5,8).}
\]
This was checked over every admissible total using the exact strict-window inequalities. The two failures are not counterexamples to the stronger obstruction (28.3); they show that the coarse replacement loses useful information.

For \((p,A)=(3,5)\), the admissible terminal valuations and exact least CRT representatives are
\[
\begin{array}{c|ccc}
b&1&2&3\\ \hline
\kappa_{3,b}&7&1&21
\end{array}
\]
and the integer inequality (28.3) holds for all three.

For \((p,A)=(5,8)\), they are
\[
\begin{array}{c|cccc}
b&1&2&3&4\\ \hline
\kappa_{5,b}&7&9&13&21
\end{array}
\]
and (28.3) holds for all four.

The full exact sweep was rerun: all 34,838 admissible triples \((p,A,b)\) for \(3\le p\le100\) satisfy (28.3). Thus the exact CRT representative repairs both exceptions. The result remains finite-range computational evidence; it is not a proof of the all-period inequality.

**Methodological correction.** Any future attempt to prove (29.2) uniformly must first account for these two exceptions, and any claim that the coarse bound follows merely from the average-valuation window is false. The exact residue \(\kappa_{p,b}\), not just its positivity, is essential in the presently verified finite sweep.

## 31. Low-modulus structure of the exact CRT representative

The defining congruence for the least positive CRT representative is
\[
\kappa_{p,b}3^p\equiv3\cdot2^b-1\pmod{2^{b+2}}.
\tag{31.1}
\]
Because the right side and \(3^p\) are odd, \(\kappa_{p,b}\) is always odd.

Reducing (31.1) modulo four gives a further exact restriction. If \(b=1\), then \(3\cdot2^b-1=5\equiv1\pmod4\), and therefore
\[
\boxed{\kappa_{p,1}\equiv
\begin{cases}
3\pmod4,&p\text{ odd},\\
1\pmod4,&p\text{ even}.
\end{cases}}
\tag{31.2}
\]
If \(b\ge2\), then \(3\cdot2^b-1\equiv3\pmod4\), so
\[
\boxed{\kappa_{p,b}\equiv
\begin{cases}
1\pmod4,&p\text{ odd},\\
3\pmod4,&p\text{ even}.
\end{cases}}
\qquad (b\ge2).
\tag{31.3}
\]
In particular, the least representative cannot equal one when \(b=1\) and \(p\) is odd, or when \(b\ge2\) and \(p\) is even. This is a genuine improvement over the coarse estimate \(\kappa_{p,b}\ge1\), but it is not by itself strong enough to establish (28.3) uniformly.

For clarity, the two failures of the coarsened sufficient condition (29.2) in the finite range \(3\le p\le100\) were found by an exact comparison. Raising its positive sides to the \(p\)-th power gives the integer test
\[
3^{p^2}2^A
\mathrel{\ge}
\left(3^{p+1}+2^{A-p+1}\right)^p.
\tag{31.4}
\]
The only admissible pairs failing this test in that range are \((3,5)\) and \((5,8)\). The exact CRT test (28.3), which retains \(\kappa_{p,b}\), passes every admissible triple in the same range.

**Status.** Equations (31.1)–(31.4) are exact. The finite exception list is range-limited to \(p\le100\). A general lower bound for \(\kappa_{p,b}\) strong enough to prove the obstruction for all periods remains open.




## 32. Modulo-eight lower bounds for the CRT representative

The congruence (31.1) can be reduced modulo eight for every \(b\ge1\). Since
\[
3^p\equiv\begin{cases}3\pmod8,&p\text{ odd},\\1\pmod8,&p\text{ even},\end{cases}
\]
and its inverse is itself modulo eight, the residue of \(\kappa_{p,b}\) is explicit.

For \(b=1\), the right side \(3\cdot2^b-1\) is \(5\pmod8\), hence
\[
\boxed{\kappa_{p,1}\equiv
\begin{cases}
7\pmod8,&p\text{ odd},\\
5\pmod8,&p\text{ even}.
\end{cases}}
\tag{32.1}
\]
For \(b=2\), the right side is \(3\pmod8\), so
\[
\boxed{\kappa_{p,2}\equiv
\begin{cases}
1\pmod8,&p\text{ odd},\\
3\pmod8,&p\text{ even}.
\end{cases}}
\tag{32.2}
\]
For \(b\ge3\), the right side is \(-1\equiv7\pmod8\), giving
\[
\boxed{\kappa_{p,b}\equiv
\begin{cases}
5\pmod8,&p\text{ odd},\\
7\pmod8,&p\text{ even}.
\end{cases}}
\qquad(b\ge3).
\tag{32.3}
\]
Because \(\kappa_{p,b}\) is the least positive representative of its residue modulo \(2^{b+2}\), these congruences imply the lower bounds
\[
\kappa_{p,1}\ge
\begin{cases}7,&p\text{ odd},\\5,&p\text{ even},\end{cases}
\quad
\kappa_{p,2}\ge
\begin{cases}1,&p\text{ odd},\\3,&p\text{ even},\end{cases}
\quad
\kappa_{p,b}\ge
\begin{cases}5,&p\text{ odd},\\7,&p\text{ even}\end{cases}
\ (b\ge3).
\tag{32.4}
\]
These bounds are valid for every period and terminal valuation. They improve the universal estimate \(\kappa_{p,b}\ge1\) except in the class \(b=2\), \(p\) odd.

The bounds are only lower bounds: the least representative modulo \(2^{b+2}\) can be larger than its residue modulo eight. Thus (32.4) is a safe input to (28.3), but it does not by itself establish (28.3) for every \((p,A,b)\). The remaining challenge is to combine the forced low bits with the higher-bit constraints without assuming that the least representative equals its residue modulo eight.

**Status.** The congruences (32.1)–(32.3) are direct consequences of the exact CRT equation and hold uniformly. They provide a period-uniform lower bound on \(\kappa_{p,b}\), not a period-uniform cycle exclusion.


## 33. Testing the uniform modulo-eight lower bound

Let \(K_{p,b}\) denote the lower bound in (32.4). For \(b\ge3\), it depends on \(p\) but not on \(b\). The left side of (29.1) is therefore fixed as \(b\) varies over \(3\le b\le A-p+1\), while its right side \(2^b\) increases. It follows that, for each fixed \((p,A)\), it is enough to test \(b=A-p+1\) in this range. The cases \(b=1\) and \(b=2\), when admissible, must be tested separately.

Using this monotonicity, an exact integer check was reduced to at most three tests for each admissible \((p,A)\). For every \(3\le p\le200\), every admissible total \(A\), and the relevant terminal valuations \(b\in\{1,2,A-p+1\}\), the integer form
\[
2^A(K_{p,b}3^p)^p
\ge (3K_{p,b}3^p+2^b)^p
\tag{33.1}
\]
holds. The reduced check comprised 9,171 exact comparisons, with no failures.

This is a finite-range verification of the modulo-eight lower bounds as inputs to the sufficient obstruction. It does not prove (33.1) for all periods. In particular, the small residue classes modulo eight do not control how close \(2^A\) can be to \(3^p\) as \(p\) grows; a uniform proof must address that approximation issue rather than extrapolate from the finite sweep.

**Next precise target.** Obtain an effective lower bound for \(2^A-3^p\) over the admissible integer pairs \(p\log_2 3<A<p\log_2(10/3)\), strong enough to control \(2^{A/p}-3\). Without such a bound, the low-bit CRT estimates alone do not close the argument.


## 34. A uniform congruence lower bound for the denominator gap

Write
\[
q=2^A-3^p.
\]
For every admissible nontrivial-cycle pair, \(A>p\log_2 3\), hence \(A\ge p+1\ge4\). Therefore \(16\mid2^A\), and
\[
q\equiv-3^p\pmod{16}.
\]
The powers of \(3\) modulo \(16\) have period four. Since \(q>0\), this gives the exact residue-class lower bound
\[
\boxed{
q\ge
\begin{cases}
13,&p\equiv1\pmod4,\\
7,&p\equiv2\pmod4,\\
5,&p\equiv3\pmod4,\\
15,&p\equiv0\pmod4.
\end{cases}}
\tag{34.1}
\]
In particular, \(q\ge5\) for every \(p\ge3\). This rules out not only \(q=1\), but every positive gap below five, without invoking a theorem on linear forms in logarithms.

For \(p\ge4\), we have \(A\ge5\), so the same argument modulo \(32\) yields the sharper eight-class table
\[
\boxed{
\begin{array}{c|rrrrrrrr}
p\bmod8&0&1&2&3&4&5&6&7\\ \hline
q\text{ lower bound}&31&29&23&5&15&13&7&21
\end{array}}
\tag{34.2}
\]
These are lower bounds, not equalities: the actual \(q\) is the positive integer in the indicated residue class modulo \(32\).

The gap also gives an exact factorization useful for quantitative estimates. Put \(x=2^{A/p}>3\). Then
\[
q=x^p-3^p=(x-3)\sum_{j=0}^{p-1}x^{p-1-j}3^j.
\]
Since the average-valuation window gives \(x<10/3\), every term in the sum is less than \((10/3)^{p-1}\). Consequently
\[
\boxed{
2^{A/p}-3>
\frac{q}{p(10/3)^{p-1}}
\ge
\frac{q_{\min}(p)}{p(10/3)^{p-1}},
}
\tag{34.3}
\]
where \(q_{\min}(p)\) may be taken from (34.1), or from (34.2) when \(p\ge4\).

This is a rigorous period-dependent lower bound on the denominator gap. It is not yet strong enough, by itself, to prove the CRT obstruction (29.1) uniformly: the geometric-sum estimate is deliberately coarse. The next step is to exploit the actual powers \(x^{p-1-j}3^j\), rather than replacing every term by the same worst-case bound.


## 35. Exact geometric-sum sharpening

The denominator in (34.3) was bounded termwise. The sum has an exact closed form:
\[
G_p(x)=\sum_{j=0}^{p-1}x^{p-1-j}3^j
=\frac{x^p-3^p}{x-3}.
\]
For fixed \(p\), \(G_p(x)\) is strictly increasing for \(x>0\), since it is a polynomial with positive coefficients. The average-valuation window gives \(3<x<10/3\), and hence
\[
G_p(x)<G_p(10/3)
=3\left((10/3)^p-3^p\right).
\]
Combining \(q=(x-3)G_p(x)\) with this strict upper bound gives
\[
\boxed{
2^{A/p}-3>
\frac{2^A-3^p}
{3\left((10/3)^p-3^p\right)}.
}
\tag{35.1}
\]
This improves (34.3) for every \(p>1\): indeed
\[
G_p(10/3)
=(10/3)^{p-1}\sum_{j=0}^{p-1}(9/10)^j
<p(10/3)^{p-1}.
\]

Substitution into the sufficient CRT obstruction (29.1) yields the explicit rational sufficient condition
\[
\boxed{
\kappa_{p,b}3^p(2^A-3^p)
\ge
3\cdot2^b\left((10/3)^p-3^p\right).
}
\tag{35.2}
\]
Equivalently, after multiplying by \(3^p\), this is the integer comparison
\[
\boxed{
\kappa_{p,b}3^{2p}(2^A-3^p)
\ge
3\cdot2^b\left(10^p-3^{2p}\right).
}
\tag{35.3}
\]
Whenever (35.3) holds, (29.1) follows, and the corresponding cycle itinerary is excluded.

The implication is one-way: failure of (35.3) does not imply a cycle exists. This reformulation converts the remaining analytic gap into a direct integer inequality involving the exact CRT representative and the exact difference of powers. It remains to prove (35.3) uniformly or identify and handle its exceptional triples.


## 36. Exact sweep of the sharpened integer obstruction

The integer sufficient condition (35.3) was checked over every admissible triple
\[
3\le p\le200,\qquad
3^p<2^A,\qquad
2^A3^p<10^p,\qquad
1\le b\le A-p+1.
\]
For each triple, the least positive representative was computed directly as
\[
\kappa_{p,b}
=\operatorname{leastpos}\left((3\cdot2^b-1)(3^p)^{-1}
\pmod{2^{b+2}}\right),
\]
and both sides of (35.3) were compared as integers. All
\[
\boxed{273\,119}
\]
triples passed; there were no failures.

The reproducible arbitrary-precision Python certificate is
certificates/collatz_geometric_sum_obstruction_3_200.py. It asserts the exact count and stops at the first failing triple. The finite computation is evidence only for the stated range. In particular, it does not establish (35.3) for all periods, and it does not by itself prove the Collatz conjecture.

**Current frontier.** The remaining task is now sharply isolated: prove (35.3) for every admissible \((p,A,b)\), or find a general argument that handles the cases where this sufficient inequality fails. A proof of this inequality for all admissible triples would combine with Sections 20, 27, and 35 to exclude every nontrivial odd cycle.


## 37. The only possible unit CRT representative

A useful structural question is when the least positive CRT representative can be the smallest odd integer, \(\kappa_{p,b}=1\). By its defining congruence, this happens exactly when
\[
3^p+1\equiv3\cdot2^b\pmod{2^{b+2}}.
\tag{37.1}
\]

This congruence can be classified completely.

- If \(b=1\), (37.1) would require \(3^p+1\equiv6\pmod8\). But \(3^p+1\equiv4\pmod8\) for odd \(p\), and \(2\pmod8\) for even \(p\). Impossible.
- If \(b=2\), (37.1) requires \(3^p+1\equiv12\pmod{16}\). The powers of \(3\) modulo \(16\) show this occurs exactly when \(p\equiv3\pmod4\).
- If \(b\ge3\), the right side of (37.1) has exact 2-adic valuation \(b\), so (37.1) would force \(v_2(3^p+1)=b\). The elementary LTE identity gives
  \[
  v_2(3^p+1)=
  \begin{cases}
  2,&p\text{ odd},\\
  1,&p\text{ even},
  \end{cases}
  \]
  contradicting \(b\ge3\).

Therefore
\[
\boxed{\kappa_{p,b}=1
\quad\Longleftrightarrow\quad
b=2\ \text{and}\ p\equiv3\pmod4.}
\tag{37.2}
\]
Since every \(\kappa_{p,b}\) is a positive odd integer, this proves the uniform dichotomy
\[
\boxed{
\kappa_{p,b}\ge3
\quad\text{unless }b=2,\ p\equiv3\pmod4.
}
\tag{37.3}
\]

This sharpens the interpretation of the low-bit table: the \(b=2,\ p\) odd class is not merely a weak lower-bound class. It contains the only possible cases where the exact CRT representative equals one. For all other terminal valuations and periods, the exact representative is at least three.

The classification does not by itself prove (35.3). It reduces any attempt to use the crude universal replacement \(\kappa\ge3\) to the exceptional class \(b=2,\ p\equiv3\pmod4\), where the exact representative may be one and must be retained. This is an exact all-period statement, independent of finite computation.


## 38. Reduction using the unit-representative classification

Section 37 shows that \(\kappa_{p,b}\ge3\) except possibly when \(b=2\) and \(p\equiv3\pmod4\). For the ordinary classes \(b\ne2\) or \(p\not\equiv3\pmod4\), a sufficient replacement in (35.3) is therefore \(K=3\).

For fixed \((p,A)\), the right side of (35.3) increases with \(b\). Hence, among \(3\le b\le A-p+1\), it is enough to test the endpoint \(b=A-p+1\). The resulting sufficient inequality is
\[
3^{2p}(2^A-3^p)\ge
3\cdot2^{A-p+1}(10^p-3^{2p}).
\tag{38.1}
\]
Equivalently,
\[
2^A\left(3^{2p}-\frac{3(10^p-3^{2p})}{2^{p-1}}\right)
\ge3^{3p}.
\tag{38.2}
\]
This is a useful structural reduction: for fixed \(p\), the coarse ordinary-class test is linear in \(2^A\). If the coefficient in parentheses is positive, it is enough to test the smallest admissible \(A\). If it is nonpositive, this particular coarse replacement cannot prove the claim for any \(A\).

The exceptional class \(b=2,\ p\equiv3\pmod4\) must still use the exact \(\kappa_{p,2}\), rather than \(K=3\). The case \(b=1\) is also checked separately, with its exact universal lower bound \(\kappa_{p,1}\ge5\) (indeed \(\ge7\) for odd \(p\)).

As a finite diagnostic, the reduced endpoint tests (ordinary \(b\ge3\)), the \(b=1\) test, and the exact exceptional \(b=2\) test were checked for every admissible \((p,A)\) with \(3\le p\le300\). All 20,595 comparisons passed. This is a finite check, not a proof that (38.1) holds for every period. In particular, positivity of the coefficient in (38.2) and the smallest-admissible-\(A\) test still require an all-period argument.


## 39. Positivity of the reduced coefficient

The coefficient in (38.2) is
\[
C_p=3^{2p}-\frac{3(10^p-3^{2p})}{2^{p-1}}.
\]
It is positive for every integer \(p\ge3\). Indeed,
\[
C_p>0
\quad\Longleftrightarrow\quad
R_p:=\frac{(2^{p-1}+3)9^p}{3\cdot10^p}>1.
\]
At \(p=3\), \(R_3=8019/3000>1\). Moreover,
\[
\frac{R_{p+1}}{R_p}
=\frac9{10}\frac{2^p+3}{2^{p-1}+3}>1
\qquad(p\ge3),
\]
because the last inequality is equivalent to
\(2^{p-1}>3/4\). Thus \(R_p\) is increasing from a value greater than one, proving \(C_p>0\) for all \(p\ge3\).

Consequently, for each fixed period \(p\), the left side of (38.2) is strictly increasing in \(2^A\). Therefore the coarse ordinary-class inequality (38.1), if true at the smallest admissible integer
\[
A_0(p)=\lfloor p\log_2 3\rfloor+1,
\]
is true for every admissible \(A\) at that period.

This removes coefficient positivity as an obstacle. It does **not** settle the remaining endpoint inequality: positivity of \(C_p\) alone does not imply \(2^{A_0(p)}C_p\ge3^{3p}\). That last comparison still involves the fine approximation of \(p\log_2 3\) by integers and must be proved separately (or bypassed with a stronger bound).

The same monotonicity principle applies to any fixed lower bound \(K\) for the CRT representative: after rearrangement, a positive coefficient of \(2^A\) reduces the test to \(A_0(p)\). The exceptional class \(b=2,\ p\equiv3\pmod4\) remains separate and must retain its exact representative.

**Status.** This section proves an all-period algebraic lemma and clarifies the exact remaining gap. It does not claim an all-period Collatz result.


## 40. Audit of the coarse endpoint reduction

There is an important exception to the coarse replacement in Section 38. Replacing the exact CRT representative by the universal lower bound \(\kappa_{p,b}\ge3\) and then taking the largest \(b\) is not sufficient in every admissible case. The endpoint inequality (38.1) fails at
\[
(p,A)=(3,5)\quad\text{and}\quad(p,A)=(5,8).
\]
These are admissible pairs: \(3^p<2^A\) and \(2^A3^p<10^p\) hold in both cases.

The failures are exact:
\[
\begin{array}{c|r|r}
(p,A)&9^p(2^A-3^p)&3\cdot2^{A-p+1}(10^p-9^p)\\ \hline
(3,5)&3645&6504\\
(5,8)&767637&1965648
\end{array}
\]
The second row has difference \(-1198011\).

This does **not** produce a cycle or a counterexample to Collatz. It only shows that the uniform substitution \(\kappa\ge3\) loses too much information in these two cases. The exact representatives are larger: \(\kappa_{3,3}=21\) and \(\kappa_{5,4}=21\), so the original exact condition (35.3) can still succeed.

For clarity, the endpoint test with the coarse value \(K=3\) has been checked with exact integer arithmetic for \(3\le p\le1000\). Its only failures in that range are precisely \((3,5)\) and \((5,8)\). This remains a finite observation, not an all-period theorem. The earlier finite diagnostic in Section 38 should be read with this correction: the exact-\(\kappa\) checks and the coarse \(K=3\) endpoint check are distinct tests and must not be conflated.

A useful normalization exposes the remaining approximation problem. Put \(u=2^A/3^p>1\). Then (38.1) is equivalent to
\[
u-1\ge 6u\left((5/9)^p-2^{-p}\right).
\tag{40.1}
\]
Thus the coarse endpoint test asks for a quantitative lower bound on the relative gap \(u-1=(2^A-3^p)/3^p\). The elementary congruence bounds on \(2^A-3^p\) from Section 34 do not by themselves provide a strong enough uniform estimate. The exact CRT representative, especially its growth with \(b\), remains essential.

**Status correction.** The coefficient positivity proved in Section 39 is valid, but it does not settle the endpoint inequality. The two small-period failures above must be handled with their exact CRT representatives, and an all-period proof for the remaining endpoint cases is still open.


## 41. A lift recurrence for the CRT representative

For fixed \(p\), write
\[
\kappa_{p,b}3^p\equiv3\cdot2^b-1\pmod{2^{b+2}},
\qquad 1\le\kappa_{p,b}<2^{b+2}.
\]
The target numerator at level \(b+1\) differs from that at level \(b\) by \(3\cdot2^b\). Reducing the level-\((b+1)\) congruence modulo \(2^{b+2}\) therefore gives
\[
\kappa_{p,b+1}
\equiv \kappa_{p,b}+3\cdot2^b(3^p)^{-1}
\pmod{2^{b+2}}.
\]
Since \((3^p)^{-1}\equiv3\pmod4\) for odd \(p\), and is congruent to \(1\pmod4\) for even \(p\), this simplifies to
\[
\boxed{
\kappa_{p,b+1}\equiv
\begin{cases}
\kappa_{p,b}+2^b\pmod{2^{b+2}},&p\text{ odd},\\
\kappa_{p,b}+3\cdot2^b\pmod{2^{b+2}},&p\text{ even}.
\end{cases}}
\tag{41.1}
\]
The least positive representative at level \(b+1\) is the unique representative of this residue in \(\{1,\ldots,2^{b+2}\}\).

This recurrence is exact, but it does not imply that \(\kappa_{p,b}\) is monotone in \(b\): the residue must be reduced modulo the old modulus, and can wrap around. It does, however, reduce the transition to a simple addition followed by a modular reduction. In particular, for fixed parity of \(p\), each step is controlled by one of two explicit shifts.

**Use in the cycle inequality.** The exact obstruction (35.3) contains both \(\kappa_{p,b}\) and \(2^b\). Recurrence (41.1) makes it possible to compare successive values of the ratio
\[
T_{p,A}(b)=
\frac{\kappa_{p,b}}{2^b}
\]
without recomputing a modular inverse from scratch. A uniform lower bound for this ratio is not asserted here: modular wraparound prevents such a conclusion from the recurrence alone. The next step is to derive a sharp two-step or block estimate that accounts for the wraparound and can be inserted into (35.3).

This is an all-period identity, not an all-period cycle exclusion.


## 42. Correct two-branch lift and the missing high bit

The modulus in the definition of \(\kappa_{p,b}\) is \(M_b=2^{b+2}\), so \(M_{b+1}=2M_b\). The reduction in (41.1) determines \(\kappa_{p,b+1}\) only modulo \(M_b\), not modulo \(M_{b+1}\).

Define the odd residue
\[
r_{p,b}=\operatorname{leastpos}\left(
\kappa_{p,b}+c_p2^b\pmod{M_b}
\right),\qquad
c_p=\begin{cases}1,&p\text{ odd},\\3,&p\text{ even}.\end{cases}
\]
Then the exact level-\((b+1)\) representative has the form
\[
\boxed{\kappa_{p,b+1}=r_{p,b}+\varepsilon_{p,b}M_b,\qquad
\varepsilon_{p,b}\in\{0,1\}.}
\tag{42.1}
\]
The bit \(\varepsilon_{p,b}\) is fixed by the original congruence modulo \(2M_b\):
\[
\boxed{
\varepsilon_{p,b}\equiv
\frac{(3\cdot2^{b+1}-1)-3^p r_{p,b}}{M_b}
\pmod2.
}
\tag{42.2}
\]
The quotient is an integer because \(r_{p,b}\) satisfies the reduced congruence modulo \(M_b\). Taking its parity selects the unique one of the two lifts that satisfies the full congruence modulo \(2M_b\).

This repairs the interpretation of Section 41. The modular addition there is correct, but it does not alone determine the next least positive representative. In particular, neither monotonicity nor a growth bound follows without controlling the lift bit.

**Consequence for the proposed block estimate.** Any two-step or longer recurrence must track these high bits, or equivalently work directly with the inverse modulo the full power of two. A block estimate that ignores them would be incomplete. The exact formula (42.2) provides a finite arithmetic rule for each lift, but a useful uniform lower bound for \(\kappa_{p,b}/2^b\) remains unproved.


## 43. A valuation-dependent hierarchy of low-bit lower bounds

The defining congruence can be reduced modulo any \(2^s\) with \(1\le s\le b\). In that range, \(3\cdot2^b\equiv0\pmod{2^s}\), so
\[
3^p\kappa_{p,b}\equiv-1\pmod{2^s}.
\]
Define
\[
\rho_s(p)=\operatorname{leastpos}\bigl(- (3^p)^{-1}\pmod{2^s}\bigr),
\qquad 1\le s\le b.
\]
Then
\[
\boxed{\kappa_{p,b}\ge \rho_s(p)\quad\text{for every }s\le b.}
\tag{43.1}
\]
The strongest bound available from this nested family is
\[
\boxed{\kappa_{p,b}\ge\max_{1\le s\le b}\rho_s(p).}
\tag{43.2}
\]
This is an all-period statement. It is stronger in scope than fixing a single modulus such as eight, although the maximum need not increase with \(b\).

For \(s=4\), the residues are especially simple:
\[
\begin{array}{c|rrrr}
p\bmod4&0&1&2&3\\ \hline
\rho_4(p)&15&5&7&13
\end{array}
\]
and therefore, whenever \(b\ge4\),
\[
\boxed{
\kappa_{p,b}\ge
\begin{cases}
15,&p\equiv0\pmod4,\\
5,&p\equiv1\pmod4,\\
7,&p\equiv2\pmod4,\\
13,&p\equiv3\pmod4.
\end{cases}}
\tag{43.3}
\]
For larger \(b\), one may choose \(s=5,6,\ldots,b\) and calculate the corresponding inverse residue. This supplies a period-sensitive and valuation-sensitive lower bound without assuming monotonicity of the full representatives.

**Limitation.** The bound (43.2) is a lower bound on each individual representative. It does not establish a block-average estimate, because the residues \(\rho_s(p)\) can vary with \(s\), and the maximum may be far below \(2^b\). The next step is to understand the sequence of binary prefixes of \(-3^{-p}\) and determine whether its largest positive residue among the first \(b\) moduli is quantitatively large often enough to force (35.3).


## 44. Exact four-lift decomposition over the terminal modulus

The hierarchy in Section 43 can be made exact at its largest level \(s=b\). Let
\[
\rho_b(p)=\operatorname{leastpos}(-3^{-p}\bmod 2^b),
\qquad 1\le\rho_b(p)<2^b.
\]
Because \(\kappa_{p,b}\equiv\rho_b(p)\pmod{2^b}\) and \(1\le\kappa_{p,b}<2^{b+2}\), there is a unique \(t_{p,b}\in\{0,1,2,3\}\) such that
\[
\boxed{\kappa_{p,b}=\rho_b(p)+t_{p,b}2^b.}
\tag{44.1}
\]
Set
\[
h_{p,b}=\frac{3^p\rho_b(p)+1}{2^b}\in\mathbb Z.
\]
Substituting (44.1) into the defining congruence and dividing by \(2^b\) gives
\[
h_{p,b}+3^p t_{p,b}\equiv3\pmod4.
\]
Since \(3^p\) is invertible modulo four,
\[
\boxed{
t_{p,b}\equiv(3-h_{p,b})(3^p)^{-1}\pmod4,
\qquad t_{p,b}\in\{0,1,2,3\}.
}
\tag{44.2}
\]
Thus the full CRT representative is exactly determined by the \(b\)-bit residue \(\rho_b(p)\) and one additional two-bit correction.

This decomposition is equivalent to the original CRT definition, but it separates two sources of size:
\[
\frac{\kappa_{p,b}}{2^b}
=\frac{\rho_b(p)}{2^b}+t_{p,b}.
\]
In particular, if \(t_{p,b}\ge1\), then \(\kappa_{p,b}\ge2^b\), a strong bound relative to the terminal factor \(2^b\) in (35.3). The difficult cases are exactly those with \(t_{p,b}=0\), where the full representative is the least positive residue \(\rho_b(p)\) itself.

**Limitation and next target.** Formula (44.2) does not prove that \(t_{p,b}\ge1\) uniformly. The case \(t=0\) is equivalent to the additional congruence \(h_{p,b}\equiv3\pmod4\), or
\[
3^p\rho_b(p)\equiv3\cdot2^b-1\pmod{2^{b+2}},
\]
which is precisely the original CRT condition with \(\kappa=\rho_b(p)\). The next problem is to bound the size of this least residue in the \(t=0\) cases, rather than assuming that the correction digit is nonzero.


## 45. The zero-correction branch can have a very small representative

The decomposition (44.1) shows that a tempting strengthening, \(\kappa_{p,b}\ge c\,2^b\) for a fixed positive constant \(c\) and all \(p,b\), cannot be inferred merely from the fact that the correction digit is zero or from the low-bit hierarchy.

For example, direct exact modular evaluation gives
\[
\begin{array}{c|rrrrrrrr}
b&3&4&5&6&7&8&9&10\\ \hline
p&7&9&29&5&21&53&373&1013\\
\kappa_{p,b}&5&5&5&5&5&5&5&5
\end{array}
\]
and each row satisfies
\[
5\cdot3^p\equiv3\cdot2^b-1\pmod{2^{b+2}}.
\]
Thus the exact representative can remain equal to five while the modulus grows substantially. These examples disprove any proposed pointwise lower bound that grows with \(2^b\) uniformly over unrestricted \(p\).

They do **not** disprove the cycle obstruction: the period \(p\), total valuation \(A\), and terminal valuation \(b\) in a genuine cycle are coupled by the admissible-window and itinerary constraints. The examples above are modular examples, not asserted cycle triples.

The right target is therefore not a bound on \(\kappa_{p,b}\) uniform in all \(p\) at fixed \(b\). It is a bound on \(\kappa_{p,b}\) under the simultaneous constraints
\[
3^p<2^A<\frac{10^p}{3^p},
\qquad 1\le b\le A-p+1,
\]
possibly combined with the other suffix congruences from Section 26. Those additional constraints retain information discarded by the isolated CRT representative.

**Research correction.** A block-average estimate cannot be assumed to follow from the lift recurrence. The explicit small-representative examples show why a proof must use the coupling to \(A\) or the higher suffix congruences, not just the modulus-doubling process.


## 46. Correction: the even-valuation claim is withdrawn

The claimed theorem that every valuation in a periodic odd cycle is even was based on an indexing error in the cycle numerator. The correct numerator uses exclusive prefix sums \(B_j=\sum_{i<j}a_i\), so its final term modulo three is \(2^{A-a_{p-1}}\), not \(2^A\).

The correct reduction is
\[
(2^A-3^p)n
=\sum_{j=0}^{p-1}3^{p-1-j}2^{B_j}
\quad\Longrightarrow\quad
2^A n\equiv2^{A-b}\pmod3.
\]
Equivalently,
\[
\boxed{2^b n\equiv1\pmod3.}
\]
This is consistent with either parity of \(b\): it says \(n\equiv1\pmod3\) when \(b\) is even and \(n\equiv2\pmod3\) when \(b\) is odd. It does not imply that \(b\) is even.

The transition relation gives no additional parity restriction: the residue of the next member modulo three is exactly what makes \(2^{a_i}n_{i+1}\equiv1\pmod3\) hold.

**Status:** the assertions in the former version of Section 46 that all cycle members are \(1\pmod3\), all valuations are even, \(A\ge2p\), and \(b\) is even are withdrawn. They must not be used in subsequent arguments.

## 47. Audit notice: Sections 27–45 are not established

The correction to Section 26 also invalidates the main CRT chain in Sections 27–45. Those sections used the false congruence
\[
2^b m\equiv1\pmod{3^p}
\]
and consequently the equation \(2^b m=1+k3^p\). The valid consequence from the \(r=1\) suffix congruence is only
\[
2^b m\equiv1\pmod3.
\]
Therefore the CRT representatives \(\kappa_{p,b}\), their lower bounds, the finite obstruction sweeps, and the later lift decompositions in Sections 27–45 do not currently establish necessary conditions for Collatz cycles. Their calculations may be arithmetically correct for the stated modular congruence, but that congruence was not derived from the cycle equation.

This is a mathematical correction, not a cosmetic change. Treat Sections 27–45 as withdrawn pending a fresh derivation from the correctly indexed identity. The valid general foundation remains the periodic criterion in Section 4 and the corrected suffix family in Section 26.

**Next research direction:** retain the full nested congruences (26.1), where \(r>1\) couples several terminal valuations, and derive any CRT restrictions directly from those identities. No parity theorem or nontrivial-cycle exclusion is claimed here.


## 48. A valid suffix-CRT filter from the full hierarchy

The corrected suffix identity does yield a CRT restriction, but it depends on the entire chosen terminal block rather than on the final valuation alone.

Rotate a hypothetical nontrivial cycle so that \(n_0=m\) is its smallest odd member. Write the last \(r\) valuations as
\[
c_0=a_{p-r},\ c_1=a_{p-r+1},\ldots,c_{r-1}=a_{p-1},
\]
and let
\[
T_r=\sum_{i=0}^{r-1}c_i,\qquad
C_0=0,\quad C_\ell=\sum_{i=0}^{\ell-1}c_i.
\]
Factor \(2^{B_{p-r}}\) out of the corrected suffix congruence (26.1). Since \(A-B_{p-r}=T_r\), this gives
\[
2^{T_r}m\equiv
H_r:=\sum_{\ell=0}^{r-1}3^{r-1-\ell}2^{C_\ell}
\pmod{3^r}.
\]
As \(2\) is invertible modulo \(3^r\),
\[
\boxed{m\equiv R_r:=2^{-T_r}H_r\pmod{3^r}.}
\tag{48.1}
\]
This is the valid \(3^r\)-adic residue of the minimum member determined by the final \(r\) valuations.

For a nontrivial cycle, minimality forces the first valuation to be \(a_0=1\): if \(a_0\ge2\), then
\[
S(m)\le\frac{3m+1}{4}<m
\]
for \(m>1\), a contradiction. Hence \(3m+1\) is divisible by \(2\) but not \(4\), so
\[
m\equiv3\pmod4.
\]
Combining this with (48.1), the Chinese remainder theorem determines one residue
\[
\boxed{m\equiv M_r\pmod{4\cdot3^r},\qquad
M_r\in\{1,\ldots,4\cdot3^r\}.}
\tag{48.2}
\]
The least positive representative \(M_r\) is an exact lower bound: \(m\ge M_r\).

The minimum-member product estimate supplies the opposing upper bound. Since every cycle member \(n_i\ge m\),
\[
2^A=\prod_{i=0}^{p-1}\left(3+\frac1{n_i}\right)
\le\left(3+\frac1m\right)^p.
\]
For a nontrivial cycle at least one member exceeds \(m\), so the inequality is strict. As \(2^{A/p}>3\),
\[
\boxed{m<\frac1{2^{A/p}-3}.}
\tag{48.3}
\]
Consequently, the exact suffix block rules out the cycle whenever
\[
\boxed{M_r\ge\frac1{2^{A/p}-3}.}
\tag{48.4}
\]

### The first nontrivial suffix test

For \(r=2\), put \(c=a_{p-2}\), \(b=a_{p-1}\). Then \(T_2=c+b\), \(H_2=3+2^c\), and
\[
\boxed{2^{c+b}m\equiv3+2^c\pmod9.}
\tag{48.5}
\]
This is already different from the invalid terminal-only congruence modulo \(3^p\): it uses both final valuations and is genuinely modulo \(9\).

**Scope.** Equations (48.1)–(48.4) are necessary conditions and a valid sufficient exclusion test for any selected suffix length \(r\). No all-period contradiction is claimed. The practical next step is to compute these suffix-CRT representatives while respecting the actual valuation word and total \(A\), then determine whether the hierarchy forces an obstruction.


## 49. Explicit two-step suffix table and an average-valuation exclusion

The two-step congruence (48.5) can be solved completely modulo \(36\). Write
\[
c=a_{p-2},\qquad b=a_{p-1}.
\]
Since \(2\) has order six modulo nine, the residue depends only on \(c\bmod 2\) and \(b\bmod6\). Combining
\[
2^{c+b}m\equiv3+2^c\pmod9
\]
with \(m\equiv3\pmod4\) gives the following least positive CRT representative \(M_2\):

\[
\begin{array}{c|rrrrrr}
 &b\equiv1&2&3&4&5&0\pmod6\\ \hline
c\text{ odd}&35&31&11&19&23&7\\
c\text{ even}&11&19&23&7&35&31
\end{array}
\]

Every entry is at least seven. Therefore every hypothetical nontrivial cycle satisfies
\[
\boxed{m\ge7.}
\]

Combining this with the strict minimum-member estimate (48.3),
\[
7\le m<\frac{1}{2^{A/p}-3}.
\]
A necessary condition is consequently
\[
\frac{1}{2^{A/p}-3}>7,
\]
or equivalently
\[
\boxed{\frac Ap<\log_2\!\left(\frac{22}{7}\right).}
\tag{49.1}
\]

Thus we obtain a genuine partial exclusion theorem:

\[
\boxed{
\frac Ap\ge\log_2(22/7)
\quad\Longrightarrow\quad
\text{no nontrivial odd cycle with that average valuation}.
}
\]

This is an all-period statement: it uses only the exact two-step suffix congruence, the minimum-member condition, and the product identity. It does not depend on a finite computational sweep.

### What remains

The admissible average window is
\[
\log_2 3<\frac Ap<\log_2(10/3).
\]
Section 49 removes its upper portion, leaving only
\[
\boxed{
\log_2 3<\frac Ap<\log_2(22/7).
}
\]
The remaining interval is narrow but nonempty. Longer suffixes \(r\ge3\) are the natural next step: compute their CRT minima and seek a sequence of stronger lower bounds on \(m\).

**Scope:** this is a necessary-condition exclusion for the stated average-valuation range, not a proof that all nontrivial cycles are impossible.


## 50. Three-step suffix: a universal nondivisibility invariant

For the final three valuations, write
\[
d=a_{p-3},\qquad c=a_{p-2},\qquad b=a_{p-1}.
\]
The suffix identity gives
\[
\boxed{
2^{d+c+b}m
\equiv9+3\cdot2^d+2^{d+c}\pmod{27}.
}
\tag{50.1}
\]
The right-hand side is nonzero modulo three: its first two terms vanish modulo three, while \(2^{d+c}\not\equiv0\pmod3\). Since the power of two on the left is invertible modulo three, this confirms
\[
3\nmid m.
\]
Together with \(m\equiv3\pmod4\), it follows again that \(m\ge7\).

This does not improve the universal lower bound from Section 49. It identifies why: the suffix hierarchy automatically preserves nondivisibility modulo three, but a stronger universal bound requires control of the actual residue modulo \(3^r\), not merely its divisibility.

More generally, in
\[
H_r=\sum_{\ell=0}^{r-1}3^{r-1-\ell}2^{C_\ell},
\]
all terms except the final one vanish modulo three, and the final term is a power of two. Thus
\[
H_r\not\equiv0\pmod3
\]
for every suffix length \(r\). Consequently every suffix congruence implies \(3\nmid m\), but this observation alone cannot raise \(m\ge7\).

**Next target:** seek valuation-dependent CRT minima \(M_r(c_0,\ldots,c_{r-1})\), rather than a uniform lower bound over all suffix words. The valuation word and total valuation must remain coupled throughout that analysis.


## 51. Three-step CRT minima when the suffix valuation sum is small

The three-step congruence (50.1) gives more information when the sum
\[
T=d+c+b
\]
of the final three valuations is small. For fixed \(T\), there are only finitely many positive triples \((d,c,b)\), so the CRT minimum can be checked exactly.

For each triple, compute
\[
R(d,c,b)\equiv
2^{-T}\left(9+3\cdot2^d+2^{d+c}\right)\pmod{27},
\]
then combine \(m\equiv R(d,c,b)\pmod{27}\) with \(m\equiv3\pmod4\). The least positive solution is the corresponding \(M_3(d,c,b)\).

Exhausting the positive compositions for \(3\le T\le7\) gives:

\[
\begin{array}{c|c|c|c}
T&\#\{(d,c,b)\}&\min M_3&\text{one minimizing triple}\\ \hline
3&1&107&(1,1,1)\\
4&3&47&(1,2,1)\\
5&6&47&(1,1,3)\\
6&10&11&(2,1,3)\\
7&15&11&(1,3,3)
\end{array}
\]

Consequently, if the final three valuations have total at most seven, then
\[
\boxed{m\ge11.}
\]
Combining this with (48.3) yields the conditional average-valuation exclusion
\[
\boxed{
T\le7
\quad\Longrightarrow\quad
\frac Ap<\log_2\!\left(\frac{34}{11}\right).
}
\tag{51.1}
\]
Equivalently, a hypothetical cycle with \(A/p\ge\log_2(34/11)\) must have its final three valuations summing to at least eight.

This is a conditional strengthening, not a universal improvement: when \(T\ge8\), the three-step CRT minimum can already be seven. For example, the triple \((d,c,b)=(2,2,4)\), with \(T=8\), gives \(M_3=7\). Thus no unconditional bound \(m\ge11\) follows from the three-step suffix alone.

**Method note:** the table is an exact enumeration of the 35 positive compositions with \(T\le7\), not a numerical approximation. The residues depend only on the displayed integer powers modulo 27, and the CRT modulus is 108.


## 52. Piecewise average-valuation bounds from the three-step CRT

The table in Section 51 contains more information than the single uniform conclusion \(m\ge11\). For each fixed suffix sum \(T\le7\), its minimum CRT representative gives a separate lower bound on \(m\). Applying (48.3) yields:

\[
\begin{array}{c|c|c}
T&\text{CRT lower bound on }m&\text{necessary upper bound on }A/p\\ \hline
3&107&A/p<\log_2(3+1/107)\\
4&47&A/p<\log_2(3+1/47)\\
5&47&A/p<\log_2(3+1/47)\\
6&11&A/p<\log_2(34/11)\\
7&11&A/p<\log_2(34/11)\\
T\ge8&7&A/p<\log_2(22/7)
\end{array}
\]

The last row uses the universal two-step bound from Section 49; the three-step CRT alone does not guarantee \(m\ge7\) for every larger \(T\).

For reference, the numerical thresholds are approximately
\[
\begin{aligned}
\log_2(3+1/107)&\approx1.5891,\\
\log_2(3+1/47)&\approx1.5999,\\
\log_2(34/11)&\approx1.6280,\\
\log_2(22/7)&\approx1.6521.
\end{aligned}
\]

There is also a simple coupling to the full valuation sum. Since the \(p-3\) valuations preceding the final triple are each at least one,
\[
A\ge T+(p-3)=p+T-3.
\]
Thus a candidate with a specified final-three sum \(T\) must satisfy both
\[
\boxed{
1+\frac{T-3}{p}\le\frac Ap
<\log_2\!\left(3+\frac1{M_T}\right),
}
\]
where \(M_T=107,47,11\) for \(T=3,\{4,5\},\{6,7\}\), respectively. For \(T\ge8\), use the universal upper bound \(\log_2(22/7)\) and the lower bound \(A/p\ge1+5/p\).

These inequalities give a compact exact filter on \((p,A,T)\). They do not eliminate every period: for sufficiently large \(p\), the lower and upper average bounds can overlap. The remaining work is to use the actual ordered suffix triple, and then longer suffixes, rather than only its sum.

**Scope and correction:** the \(T\ge8\) row is supported by Section 49, not by a claim that every three-step CRT minimum is at least seven. The example \((2,2,4)\) in Section 51 shows that this distinction is necessary.


## 53. Exact classification of the weakest three-step CRT case

The three-step CRT minimum is always at least seven: the suffix residue is nonzero modulo three, while minimality gives \(m\equiv3\pmod4\). The smallest positive integer satisfying both is seven.

We can characterize exactly when the three-step test attains this weakest value. Since \(2\) has order 18 modulo 27, the condition depends only on \(d\bmod2\), \(c\bmod6\), and \(b\bmod18\). Solving
\[
2^{d+c+b}\,7\equiv9+3\cdot2^d+2^{d+c}\pmod{27}
\]
gives:

\[
\begin{array}{c|rrrrrr}
&c\equiv1&2&3&4&5&0\pmod6\\ \hline
d\text{ odd}&12&10&18&4&6&16\\
d\text{ even}&18&4&6&16&12&10
\end{array}
\]
where each table entry is the required residue of \(b\pmod{18}\).

Therefore
\[
\boxed{
M_3(d,c,b)=7
\iff
b\equiv f(d\bmod2,c\bmod6)\pmod{18},
}
\]
with \(f\) given by the table. For all other residue classes, \(M_3\ge11\).

This is an exact ordered-suffix classification, stronger than the sum-only table in Sections 51–52. It shows that the weak three-step cases occupy a specific congruence pattern, rather than all triples with large sum.

### Correction to the decimal table in Section 52

The exact value is
\[
\log_2(3+1/47)\approx1.5951583,
\]
not \(1.5999\). The other displayed thresholds are
\[
\log_2(3+1/107)\approx1.5894499,\quad
\log_2(34/11)\approx1.6280312,\quad
\log_2(22/7)\approx1.6520767.
\]
The symbolic inequalities in Section 52 are unchanged; this paragraph corrects only its decimal approximation.


## 54. Eliminate the two smallest minimum candidates directly

The congruence \(m\equiv3\pmod4\) implies that a nontrivial cycle minimum \(m>1\) must be one of
\[
3,7,11,15,19,\ldots.
\]
The two smallest candidates can be eliminated by their exact forward trajectories under the accelerated odd map
\[
S(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

For \(m=3\),
\[
3\longmapsto5\longmapsto1.
\]
For \(m=7\),
\[
7\longmapsto11\longmapsto17\longmapsto13
\longmapsto5\longmapsto1.
\]
Neither trajectory returns to its starting value, and each reaches the fixed point \(1\). Since the map is deterministic, neither 3 nor 7 can belong to a nontrivial periodic orbit.

It follows that every nontrivial odd cycle would have to satisfy
\[
\boxed{m\ge11.}
\tag{54.1}
\]

Combining (54.1) with the strict product estimate
\[
m<\frac1{2^{A/p}-3}
\]
gives the unconditional all-period restriction
\[
\boxed{
\frac Ap<\log_2\!\left(\frac{34}{11}\right).
}
\tag{54.2}
\]

This improves the universal average-valuation ceiling from Section 49. It does not depend on the three-step CRT classification or on a computational search.

**Scope:** this is a rigorous exclusion of minimum values \(3\) and \(7\), and a stronger necessary average-valuation bound. It does not eliminate possible cycles whose minimum is at least 11.


## 55. Finite audit of candidate minima through 10,000

Section 54 eliminates the first two admissible minima, \(m=3\) and \(m=7\). The next candidates are \(m\equiv3\pmod4\). Their initial accelerated trajectories include
\[
11\to17\to13\to5,
\]
\[
15\to23\to35\to53\to5,
\]
\[
19\to29\to11,
\]
\[
23\to35\to53\to5.
\]
Each reaches a value below its starting minimum, so none can be a nontrivial cycle minimum.

An exact finite computation extends this observation: for every
\[
m\in\{3,7,11,\ldots,9999\},
\]
iteration of
\[
S(n)=(3n+1)/2^{v_2(3n+1)}
\]
reaches a value below \(m\) within at most 51 accelerated steps. The maximum first-drop time in this range is 51, attained at \(m=703\), whose first value below its starting point is 157.

This is a finite verification only. It does not establish that every admissible minimum eventually drops below itself, which would be a Collatz-type global assertion. Its rigorous consequence is limited to the checked range: no nontrivial odd cycle can have minimum \(m\le9999\).

**Reproducibility:** enumerate \(m=3+4j\le9999\); repeatedly compute \(x\leftarrow S(x)\), stopping as soon as \(x<m\). The valuation is obtained exactly by counting factors of two in \(3x+1\). No floating-point arithmetic is involved.

The remaining theoretical problem is now explicit: prove that every \(m\equiv3\pmod4\), \(m>1\), eventually has an accelerated iterate below \(m\), or find a different argument that excludes all sufficiently large minima. The finite audit supplies evidence, not that missing proof.


## 56. A residue-class family that drops in two accelerated steps

The finite audit suggests looking for residue classes whose first few accelerated iterates can be bounded symbolically.

Write every admissible minimum as
\[
m=4k+3.
\]
Then \(3m+1=12k+10=2(6k+5)\), and \(6k+5\) is odd. Therefore the first accelerated step is exact:
\[
S(m)=6k+5.
\]

The next numerator is
\[
3S(m)+1=18k+16=2(9k+8),
\]
so
\[
S^2(m)=\operatorname{oddpart}(9k+8),
\]
where \(\operatorname{oddpart}(x)=x/2^{v_2(x)}\).

Now suppose \(k\equiv0\pmod4\), so \(k=4q\). Then
\[
9k+8=36q+8=4(9q+2),
\]
and hence
\[
S^2(m)=\operatorname{oddpart}(9q+2)
\le 9q+2
<16q+3=m.
\]

Thus we have the exact infinite-family result
\[
\boxed{m\equiv3\pmod{16}\implies S^2(m)<m.}
\tag{56.1}
\]

Every such value is excluded as the minimum of a nontrivial odd cycle. This covers one quarter of the admissible residue classes \(m\equiv3\pmod4\), without a finite bound or numerical search.

The other three residue classes modulo 16 are not settled by this two-step argument. In particular, failure of this sufficient condition is not evidence that their trajectories fail to drop; it only means a longer argument is needed.


## 57. Two more infinite residue families with three-step descent

The two-step result in Section 56 covers \(m\equiv3\pmod{16}\). We can extend the explicit descent partition to two further classes modulo 64.

### Family A: \(m=64q+43\)

The exact accelerated itinerary has valuations \((1,2,2)\):
\[
64q+43\longmapsto96q+65
\longmapsto72q+49
\longmapsto54q+37.
\]
At each step the displayed quotient is odd, so the valuations are exact. Since
\[
54q+37<64q+43
\]
for every integer \(q\ge0\), this family descends below its starting value in three steps.

### Family B: \(m=64q+55\)

The exact valuation itinerary is \((1,1,3)\):
\[
64q+55\longmapsto96q+83
\longmapsto144q+125
\longmapsto54q+47.
\]
Again, each displayed output is odd, confirming the exact valuations. Moreover,
\[
54q+47<64q+55
\]
for every \(q\ge0\).

Consequently,
\[
\boxed{
m\equiv43\text{ or }55\pmod{64}
\implies \exists t\le3:\ S^t(m)<m.
}
\tag{57.1}
\]

These are two additional infinite families of impossible cycle minima. Together with Section 56, the explicit residue classes now include
\[
m\equiv3\pmod{16},\qquad
m\equiv43,55\pmod{64}.
\]
Among the eight admissible classes modulo 64 (those congruent to 3 modulo 4), this covers four classes: \(3,19,43,55\pmod{64}\).

This is a sufficient descent partition, not a complete classification. The remaining admissible classes modulo 64 require further analysis; no conclusion about their eventual descent follows merely from their absence here.


## 58. Two further three-step descent classes modulo 128

Refining the remaining classes modulo 64 gives two more exact infinite families.

### Family C: \(m=128q+11\)

The accelerated trajectory is
\[
128q+11\longmapsto192q+17
\longmapsto144q+13
\longmapsto54q+5.
\]
The successive valuations are exactly \(1,2,3\), since the displayed outputs are odd and the corresponding numerators have precisely those powers of two. Finally,
\[
54q+5<128q+11
\]
for every \(q\ge0\).

### Family D: \(m=128q+87\)

Here the exact trajectory is
\[
128q+87\longmapsto192q+131
\longmapsto288q+197
\longmapsto54q+37.
\]
The successive valuations are exactly \(1,1,4\), and
\[
54q+37<128q+87
\]
for every \(q\ge0\).

Therefore
\[
\boxed{
m\equiv11\text{ or }87\pmod{128}
\implies S^3(m)<m.
}
\tag{58.1}
\]

The first class refines the \(11\pmod{64}\) family; the second refines the \(23\pmod{64}\) family. Together with Sections 56–57, the explicit descent classes modulo 128 include
\[
3,19,43,55,11,87\pmod{128}.
\]
The classes \(3,19,43,55\) here are understood as their corresponding full residue families modulo 128 inherited from the earlier congruences, not as a complete list of all lifts modulo 128.

This remains a partial residue cover. No conclusion is asserted for the uncovered lifts.
