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
