# G-EP35 — complete strict-equivalence profiles in the invertible-Q chart

Let (Q,Kin M_n(mathbb F_p)) and assume (Q) is invertible. Left multiplication by (Q^{-1}) sends the ordered pencil pair to
[
(Q,K)longmapsto (I,A),qquad A=Q^{-1}K.
]
For two normalized pairs ((I,A)) and ((I,B)), a strict-equivalence witness (S,T) must satisfy (ST=I), hence (T=S^{-1}), and the second identity becomes (B=SAS^{-1}). Therefore
[
(Q_1,K_1)	ext{ and }(Q_2,K_2)	ext{ are strictly equivalent}
iff Q_1^{-1}K_1	ext{ and }Q_2^{-1}K_2	ext{ are similar}.
]
The rational canonical invariant factors of (Q^{-1}K) are consequently a complete strict-equivalence fingerprint for ordered pairs in this chart.

## Implementation

- `tools/regular_pencil_profile.py`: `regular_pencil_similarity_profile(q,k,p)` normalizes the pair and calls G-EP21's exact rational-canonical classifier.
- `compare_regular_pencils(q_a,k_a,q_b,k_b,p)` decides strict equivalence by equality of the complete invariant-factor chains.
- `tests/test_regular_pencil_profile.py` checks normalization, a nonidentity first coefficient, invariance under explicit strict-equivalence basis changes, separation of distinct similarity classes, and invalid inputs.

No floating-point arithmetic is used. Matrix inversion and multiplication are exact over (mathbb F_p).

## What this does and does not establish

This is a complete decision procedure for constant strict equivalence of two **ordered** square pencils when each first coefficient (Q) is invertible over the selected field. It does not handle a regular pencil whose (Q) is singular, does not permit a change of basis in the two-dimensional coefficient space (mixing (Q) and (K)), and does not produce explicit strict-equivalence witness matrices. It is a classification result in one chart, not a general Kronecker algorithm.

The condition (Q) invertible itself certifies regularity: (det(Q+tK)) has nonzero constant term (det Q). The resulting operator profile is prime-dependent, as all finite-field reductions are.
