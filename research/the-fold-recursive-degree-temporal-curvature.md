# Temporal curvature of the recursive composition-excess family

## G-EP209 — Uniform strict negativity of the temporal second difference

For k >= 1 and real Q >= 2, define
\[
H_k(Q)=H_Q(2,3^k)
=Q^{-3^k}+Q^{-4\cdot3^{k-1}}
-Q^{-5\cdot3^{k-1}}
-Q^{-(1+2\cdot3^{k-1})}.
\]

G-EP208 proves H_1(Q)>0 and H_k(Q)<0 for every k>=2. We prove
\[
\boxed{H_{k+1}(Q)-2H_k(Q)+H_{k-1}(Q)<0
\quad(k\ge3,\ Q\ge2).}
\]

### Exact reduction

Fix k>=3 and put
\[
u=Q^{-3^{k-2}},\qquad c=Q^{-1}.
\]
Then 0<u<=1/8 and c/u=Q^{3^{k-2}-1}>=4. We have
\[
H_{k-1}=u^3+u^4-u^5-cu^2,
\]
\[
H_k=u^9+u^{12}-u^{15}-cu^6,
\]
\[
H_{k+1}=u^{27}+u^{36}-u^{45}-cu^{18}.
\]

Thus
\[
K_k=A(u)-c u^2(1-2u^4+u^{16}),
\]
where
\[
A(u)=u^3+u^4-u^5-2u^9-2u^{12}+2u^{15}
+u^{27}+u^{36}-u^{45}.
\]

### Sign proof

For 0<u<=1/8, discard negative terms:
\[
A(u)\le u^3+u^4+2u^{15}+u^{27}+u^{36}
\le u^3(1+u+2u^{12}+u^{24}+u^{33})<2u^3.
\]
Also
\[
1-2u^4+u^{16}>1-2/8^4>99/100.
\]
Since c/u>=4,
\[
c u^2(1-2u^4+u^{16})
\ge 4u^3\cdot99/100>2u^3.
\]
Therefore K_k<0 for every real Q>=2 and k>=3.

### Interpretation and scope

- G-EP208: H_k is negative for every k>=2.
- G-EP209: its discrete second difference is negative for every k>=3.
- Hence H_k is strictly discretely concave on the tail k>=2: its first differences strictly decrease for k>=2.
- Concavity alone does not establish that H_k itself is monotone.
- The proof is uniform over real Q>=2, hence over all prime-power field sizes. It uses exact spectra and inequalities, not finite sampling.


## G-EP210 — Strict monotone convergence to zero

The same substitution proves a stronger shape theorem:
\[
\boxed{H_k(Q)<H_{k+1}(Q)<0\quad(k\ge2,\ Q\ge2),}
\]
and
\[
\boxed{\lim_{k\to\infty}H_k(Q)=0^- .}
\]

### Proof of strict increase

Fix k>=3 and again put u=Q^(-3^(k-2))<=1/8 and c=Q^-1, so c/u>=4. Then
\[
H_k-H_{k-1}
=c u^2(1-u^4)-u^3-u^4+u^5+u^9+u^{12}-u^{15}.
\]
Discarding positive terms gives
\[
H_k-H_{k-1}
\ge c u^2(1-u^4)-u^3-u^4-u^{15}.
\]
Since u<=1/8,
\[
c u^2(1-u^4)
\ge4u^3(1-8^{-4}),
\]
while
\[
u^3+u^4+u^{15}
\le u^3(1+1/8+8^{-12}).
\]
The first coefficient is greater than 3.99, and the second is less than 1.126. Hence H_k-H_(k-1)>0.

G-EP208 already gives H_k<0 for every k>=2. Each term in the exact formula for H_k tends to zero as k tends to infinity, so H_k tends to zero. Since every H_k is negative, the convergence is from below.

### Combined shape theorem

For every fixed real Q>=2:
- H_1(Q)>0;
- H_k(Q)<0 for k>=2;
- H_(k+1)(Q)>H_k(Q) for k>=2;
- H_(k+1)-2H_k+H_(k-1)<0 for k>=3;
- H_k(Q) increases to 0 from below.

Thus after the one-time sign transition, the sequence is increasing and strictly discretely concave, with positive first differences that strictly decrease to zero.


## G-EP211 — Exact asymptotic equivalent and super-geometric ratio

For k>=2 write m=3^k and
\[
B_k(Q)=1-Q^{-(m/3-1)}-Q^{-(2m/3-1)}+Q^{-(m-1)}.
\]
Factoring the exact spectrum gives
\[
H_k(Q)=-Q^{-(1+2m/3)}B_k(Q).
\]
All three correction exponents tend to infinity, so B_k(Q)->1. In fact this convergence is uniform over real Q>=2, since each correction is bounded by its value at Q=2. Therefore
\[
\boxed{H_k(Q)\sim -Q^{-(1+2\cdot3^{k-1})}}
\]
for each fixed Q>=2, with a uniform relative asymptotic over Q>=2.

For successive terms, the leading exponents differ by
\[
(1+2\cdot3^k)-(1+2\cdot3^{k-1})=4\cdot3^{k-1}.
\]
Hence the exact ratio is
\[
\frac{H_{k+1}(Q)}{H_k(Q)}
=Q^{-4\cdot3^{k-1}}\frac{B_{k+1}(Q)}{B_k(Q)}.
\]
Because B_k and B_(k+1) both tend uniformly to 1, their quotient tends uniformly to 1. Consequently
\[
\boxed{
\frac{H_{k+1}(Q)}{H_k(Q)}
\sim Q^{-4\cdot3^{k-1}}
}
\]
and in particular the ratio tends to zero, uniformly for Q>=2.

### Interpretation

The tail is not merely monotone and discretely concave (G-EP209–210): it decays toward zero at a scale whose successive leading terms are separated by an exponent growing like 3^k. The ratio theorem quantifies this super-geometric separation. Here “super-geometric” refers to the ratio tending to zero, not to a claim about a single fixed exponential rate.
