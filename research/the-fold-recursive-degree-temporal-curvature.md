# Temporal curvature of the recursive composition-excess family

## G-EP209 — Uniform strict negativity of the temporal second difference

For k >= 1 and real Q >= 2, define
\[
H_k(Q)=H_Q(2,3^k)
=Q^{-3^k}+Q^{-4\cdot3^{k-1}}
-Q^{-5\cdot3^{k-1}}
-Q^{-(1+2\cdot3^{k-1})}.
\]

G-EP208 proves H_1(Q)>0 and H_k(Q)<0 for every k>=2. We now prove the stronger curvature statement
\[
\boxed{H_{k+1}(Q)-2H_k(Q)+H_{k-1}(Q)<0
\quad(k\ge3,\ Q\ge2).}
\]

### Exact reduction

Fix k>=3 and set
\[
u=Q^{-3^{k-2}},\qquad c=Q^{-1}.
\]
Then 0<u<=1/8, and
\[
H_{k-1}=u^3+u^4-u^5-cu^2,
\]
\[
H_k=u^9+u^{12}-u^{15}-cu^6,
\]
\[
H_{k+1}=u^{27}+u^{36}-u^{45}-cu^{18}.
\]

Thus the second difference is
\[
K_k
=u^{27}+u^{36}-u^{45}
-2u^9-2u^{12}+2u^{15}
+u^3+u^4-u^5
-c(u^{18}-2u^6+u^2).
\]

Equivalently, collecting the terms by direct substitution gives
\[
K_k=
\underbrace{-u^3-u^4+u^5+u^9+u^{12}-u^{15}}_{A(u)}
-
c\underbrace{(u^2-2u^6+u^{18})}_{B(u)}.
\]

### Sign proof

Since 0<u<=1/8,
\[
A(u)
\le -u^3+u^5+u^9+u^{12}
=u^3(-1+u^2+u^6+u^9)<0,
\]
because
\[
u^2+u^6+u^9
\le 8^{-2}+8^{-6}+8^{-9}<1.
\]

Also
\[
B(u)=u^2(1-2u^4+u^{16})>0,
\]
since 2u^4<=2/8^4<1. As c=Q^-1>0, it follows that
\[
K_k=A(u)-cB(u)<0.
\]

This proves strict negativity for every real Q>=2 and every integer k>=3. In particular, it holds uniformly over all prime-power field sizes.

### Interpretation and scope

- G-EP208: the sequence H_k is negative for every k>=2.
- G-EP209: from k>=3 onward, its discrete second difference is also negative.
- Therefore the sequence is strictly discretely concave on the tail k>=2: its first differences H_(k+1)-H_k strictly decrease for k>=2.
- This does not assert that the first differences are always negative; that is a separate statement. Concavity alone does not imply monotonicity.
- The proof uses the exact Laurent spectrum and an interval bound u<=1/8; it is not based on finite sampling.

