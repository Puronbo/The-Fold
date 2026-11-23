# G-EP40 — canonical block representatives for regular pencils

G-EP40 turns the complete regular-pencil profile into an explicit block-diagonal representative over the original prime field.

## Finite blocks

For every nonconstant finite Smith invariant factor
[
d(t)=t^m+c_{m-1}t^{m-1}+\cdots+c_0,
]
let (C(d)) be its companion matrix. The corresponding ordered coefficient block is
[
(Q_d,K_d)=(-C(d),I_m),
]
so
[
\det(Q_d+tK_d)=\det(tI_m-C(d))=d(t).
]
Unit Smith factors contribute no block.

## Infinite blocks

For every positive (t)-adic exponent (e) in the Smith factors of the reversed pencil (K+tQ), append
[
(Q_\infty,K_\infty)=(I_e,N_e),
]
where (N_e) is the nilpotent Jordan block with ones on its superdiagonal. Its reversed block (N_e+tI_e) has determinant (t^e), giving exactly the required infinity elementary divisor.

The total dimension is the sum of the degrees of the nonconstant finite invariant factors and the infinity block sizes, which G-EP37 checks equals (n).

## Independent verification

The implementation assembles the two block-diagonal coefficient matrices and reruns the complete regular-pencil profile algorithm on the resulting pair. It requires exact equality of all finite invariant factors and infinity exponents before returning the canonical representative.

Tests cover finite blocks, pure infinity blocks, mixed finite/infinity pencils, the \(\mathbb F_2\) example with no rational invertible projective member, and rejection of singular pencils.

## Important boundary

This milestone constructs a canonical representative from the complete profile. It does **not** yet construct constant invertible matrices (S,T) satisfying
[
SQS^{-1}_{?}
]
or, in the repository's witness convention,
[
S Q T=Q_{\rm can},\qquad S K T=K_{\rm can}.
]
The latter constructive reduction is the next task. Polynomial Smith transformations cannot simply be substituted for these constant matrices.
