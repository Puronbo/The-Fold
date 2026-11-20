# UF-002 — Minimal Fold Operation Families

**Research question.** Given a target spectral invariant, what is the smallest admissible family of Fold power operations that removes unwanted prime-order components while preserving requested components?

**Main result.** For a finite candidate catalogue, UF-002 is exactly a set-cover problem on prime supports. With unrestricted composite exponents, the minimum number of operations is trivial (one nontrivial product operation); a nontrivial optimization requires a specified primitive-operation catalogue or cost model.

## 1. State space and operation semantics

For each spectral coordinate \(j\), let its current multiplicative order be \(d_j\). An allowed power operation with exponent \(r\ge2\) acts by

\[
\Pi_r(d,\tau)=\left(\frac{d}{\gcd(d,r)},\ \tau\,\mathbf1_{d/\gcd(d,r)\ \mathrm{even}}\right).
\]

For a finite operation family \(R\), put \(L=\operatorname{lcm}(R)\). After all allowed operations may be repeated, the terminal order is

\[
\operatorname{core}_L(d)=\prod_{q\nmid L}q^{v_q(d)},
\]

the largest divisor of \(d\) coprime to \(L\). Thus the family erases a prime-primary component exactly when that prime divides at least one selected exponent.

The operation family acts globally on every spectral coordinate. This global coupling is essential to the feasibility theorem below.

## 2. Define the target correctly

Suppose the current orders are \(d_1,\ldots,d_t\), and the desired terminal orders are \(c_1,\ldots,c_t\).

A target is **whole-primary-component compatible** when:

1. \(c_j\) divides \(d_j\); and
2. for every prime \(q\mid d_j\), the exponent \(v_q(c_j)\) is either \(0\) or exactly \(v_q(d_j)\).

This condition is necessary because the spectral core either retains the entire \(q\)-primary component or removes it; it cannot partially lower its exponent.

Define the global keep and erase sets:

\[
K=\bigcup_j\operatorname{supp}(c_j),\qquad
D=\bigcup_j\left(\operatorname{supp}(d_j)\setminus\operatorname{supp}(c_j)\right),
\]

where \(\operatorname{supp}(n)\) is the set of prime divisors of \(n\).

## 3. The exact feasibility theorem

Let \(A\) be the catalogue of allowed primitive exponents. For a candidate exponent \(r\), its coverage is

\[
S_r=\operatorname{supp}(r)\cap D.
\]

It is **safe** when

\[
\operatorname{supp}(r)\cap K=\varnothing.
\]

### Theorem 1 — Target feasibility

A compatible target \((c_1,\ldots,c_t)\) is reachable by one global finite family \(R\subseteq A\) if and only if:

1. \(K\cap D=\varnothing\); and
2. the safe candidates cover \(D\):

\[
D\subseteq\bigcup_{r\in R}S_r.
\]

Equivalently, no prime is simultaneously required to be retained in one coordinate and erased in another, and every prime that must be erased occurs in at least one selected safe exponent.

**Proof.** Let \(Q=\operatorname{supp}(\operatorname{lcm}(R))=\bigcup_{r\in R}\operatorname{supp}(r)\). The terminal order is \(\operatorname{core}_L(d_j)\). To produce \(c_j\), every prime in \(\operatorname{supp}(c_j)\) must be absent from \(Q\), while every prime in \(\operatorname{supp}(d_j)\setminus\operatorname{supp}(c_j)\) must belong to \(Q\). Taking unions over coordinates gives \(Q\cap K=\varnothing\) and \(D\subseteq Q\). The first condition is equivalent to every selected candidate being safe; the second is exactly coverage of \(D\). Conversely, if safe candidates cover \(D\), their union of prime supports misses \(K\) and contains \(D\); since every prime divisor of every \(d_j\) is in \(K\) or \(D\), the resulting prime-to-\(L\) core of each \(d_j\) is precisely \(c_j\). \(\square\)

### Corollary 1 — Global-coordinate conflict

If a prime \(q\) must be retained in any one spectral coordinate and erased in any other, no single global exponent family can achieve the target. The remedy is to use coordinate-specific operation families, or to change the state/operation model so the operation can act independently on coordinates.

## 4. UF-002 is set cover

For each safe candidate \(r\in A\), create the set \(S_r=\operatorname{supp}(r)\cap D\). The minimum-cardinality operation problem is

\[
\boxed{\min |R|\quad\text{subject to}\quad
R\subseteq A_{\mathrm{safe}},\quad\bigcup_{r\in R}S_r=D.}
\]

For costs \(w_r\ge0\), replace the objective with \(\min\sum_{r\in R}w_r\).

### Theorem 2 — Set-cover equivalence

For a finite candidate catalogue, UF-002 is exactly the set-cover optimization problem on universe \(D\) with candidate subsets \(S_r\).

**Proof.** Theorem 1 says that a family is feasible exactly when its safe coverage sets cover \(D\). The family size (or sum of candidate costs) is the set-cover objective. \(\square\)

### Theorem 3 — NP-hardness for finite candidate catalogues

The optimization problem is NP-hard when the candidate catalogue is part of the input. Its decision version is NP-complete when prime supports (or factorizations) are supplied as part of the input.

**Reduction.** Given a Set Cover instance with universe \(U=\{u_1,\ldots,u_n\}\) and subsets \(B_1,\ldots,B_s\), choose distinct primes \(q_1,\ldots,q_n\). Set \(D=\{q_1,\ldots,q_n\}\) and \(K=\varnothing\). For each subset \(B_i\), create candidate exponent

\[
r_i=\prod_{u_j\in B_i}q_j.
\]

Then \(\operatorname{supp}(r_i)\cap D\) corresponds exactly to \(B_i\). A collection of exponents covers \(D\) if and only if the corresponding subsets cover \(U\), with exactly the same cardinality. Thus a polynomial-time solution of UF-002 would solve Set Cover. With prime supports supplied, a proposed family can be checked by finite set-union operations in polynomial time. If candidates are provided only as unfactored binary integers, input factorization is a separate computational issue; the NP-completeness statement is therefore for factored/support-encoded catalogues. \(\square\)

The weighted version is likewise weighted Set Cover. A standard greedy weighted-cover algorithm gives the usual logarithmic approximation guarantee in \(|D|\).

## 5. Important special cases

### 5.1 Unrestricted composite exponents

If every integer exponent \(r\ge2\) is allowed and \(D\) is nonempty, one operation suffices:

\[
r_*=\prod_{q\in D}q.
\]

It is safe exactly when \(K\cap D=\varnothing\), and its support covers all of \(D\). Hence the minimum family size is **one**. If \(D\) is empty, the empty family is optimal.

This is why a meaningful UF-002 optimization needs a restricted primitive-operation catalogue or an operation cost model. Otherwise the problem collapses to one composite exponent.

### 5.2 Only prime exponents are allowed

If the available exponents include precisely the primes in \(D\) as usable erasure operations (and none is protected), each operation covers exactly one required prime. Therefore the minimum family size is

\[
|D|.
\]

### 5.3 Coordinate-specific operations

If each coordinate \(j\) may have its own family \(R_j\), the global conflict disappears. Each coordinate becomes a separate set-cover instance with keep set \(K_j=\operatorname{supp}(c_j)\) and erase set \(D_j=\operatorname{supp}(d_j)\setminus K_j\). This is a different operation model and should not be confused with a single global Fold acting on the entire joint state.

## 6. Worked example

Take two current spectral orders:

\[
d_1=720=2^4\cdot3^2\cdot5,\qquad d_2=98=2\cdot7^2.
\]

We want to retain only the 5-primary component of the first order and the 7-primary component of the second:

\[
c_1=5,\qquad c_2=49.
\]

Then

\[
K=\{5,7\},\qquad D=\{2,3\}.
\]

For the catalogue

\[
A=\{2,3,6,10,15,21,35\},
\]

the candidates 10, 15, 21, and 35 are unsafe because they contain protected primes 5 or 7. Candidate 6 covers both required primes, so the unique one-operation minimum is

\[
R=\{6\}.
\]

Indeed, \(L=6\) and

\[
\operatorname{core}_6(720)=5,\qquad
\operatorname{core}_6(98)=49.
\]

If only prime exponents are permitted, the minimum is \(R=\{2,3\}\), requiring two primitive operations.

### Global conflict example

Let

\[
d_1=12,\ c_1=4;\qquad d_2=15,\ c_2=3.
\]

The first coordinate requires erasing 3; the second requires retaining 3. Thus \(3\in K\cap D\) and no global operation family can reach this target. Separate coordinate-specific families \(\{3\}\) and \(\{5\}\) can reach it.

## 7. Spectral turning bit

The terminal turning flag is inherited from the original flag if \(L\) is odd, and is zero if \(L\) is even. The target order profile already determines the relevant global constraint:

- If 2 must be retained anywhere, every selected exponent must be odd, so the initial turning flags are preserved.
- If 2 must be erased anywhere, a selected exponent must be even, so all terminal turning flags become zero.
- If no current order has a factor 2, every initial turning flag is already zero.

If a separate orientation bit is present, it is invariant under power operations but not under the turn operation. Protecting orientation therefore means not including turning in the allowed operation family.

## 8. Exact algorithm and complexity

For a finite catalogue, encode each erased prime in \(D\) as one bit. Each safe exponent is a bitmask of the primes it covers. Dynamic programming over masks finds the exact optimum in

\[
O(|A_{\mathrm{safe}}|\,2^{|D|})
\]

time and \(O(2^{|D|})\) space, up to the cost of storing chosen candidates. This is suitable for small and medium target sets. For larger targets, use an integer-programming solver or the greedy approximation for weighted Set Cover.

The companion script tools/fold_minimal_operations.py implements exact cardinality/weighted set cover by dynamic programming, checks target compatibility, and verifies the worked examples. It uses only the Python standard library.

## 9. Bounded verification

The reference script exhaustively checked 29,733 two-coordinate target profiles over original orders below 80 and 50, whenever the target retained or removed whole prime-primary components. For every globally compatible profile, the unrestricted product exponent reproduced the requested target exactly. It also tests the constrained catalogue example and the cross-coordinate impossibility example. A separate small-catalogue brute-force oracle checks the dynamic-programming optimizer.

These are finite checks of the implementation; the general claims are proved above.

## 10. Classification and next problems

| Claim | Status |
|---|---|
| A global target is feasible iff keep/erase sets are disjoint and safe candidates cover all erased primes | Proved |
| A finite catalogue's minimum family is Set Cover | Proved |
| General finite-catalogue minimum is NP-hard | Proved by reduction |
| Unrestricted composite exponents need one operation | Proved |
| Prime-only exponents need one operation per erased prime | Proved |
| Different coordinates can request conflicting treatment of the same prime under one global family | Impossibility proved |

Follow-on problems:

- **UF-002a — Weighted primitive operations:** choose a principled cost model from the geometry or implementation of Fold operations.
- **UF-002b — Structured catalogues:** solve the minimum family efficiently for natural catalogues such as prime powers, bounded exponents, or allowed rotation orders.
- **UF-002c — Coordinate-specific folds:** compare the cost and invariant strength of global versus coordinate-specific operation families.
- **UF-002d — Joint turning constraints:** optimize spectral erasure while preserving or deliberately removing orientation.

## Conclusion

UF-002 has a precise answer. The prime supports of allowed exponents determine which primary components are erased. A target is feasible exactly when no prime is simultaneously protected and required to be erased, and the allowed safe exponents cover all required erasures. For a constrained catalogue, finding the smallest family is Set Cover; with unrestricted composite exponents it is trivial, because one product exponent covers every required prime.

The research task is therefore to justify a nontrivial primitive-operation catalogue or cost model from The Fold itself.
