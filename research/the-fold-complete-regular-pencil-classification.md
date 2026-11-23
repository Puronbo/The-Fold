# G-EP37 — complete regular-pencil classification over the base field

## The invariant

Let (Q,K\in M_n(\mathbb F_p)) and assume the pencil (Q+tK) is regular, meaning its determinant is not the zero polynomial.

The Smith invariant factors of (Q+tK) over (\mathbb F_p[t]) encode all finite elementary divisors. They retain irreducible polynomial labels and block exponents, not merely eigenvalue counts or determinant data.

For infinity, reverse the pencil to (K+tQ). The elementary divisors at infinity are **only the powers of (t)** dividing the reversed Smith invariant factors. Other nonzero roots of the reversed polynomials are not infinity divisors; they encode the corresponding finite projective points in the reversed coordinate chart.

Consequently a complete regular-pencil invariant is:
1. the ordered list of monic Smith invariant factors of (Q+tK);
2. the sorted list of positive (t)-adic valuations of the Smith invariant factors of (K+tQ).

The finite Smith factors determine every finite primary elementary divisor. The (t)-adic valuations in the reversed chart determine the infinity elementary divisors. Together these are the regular Kronecker data, which classify regular square pencils over (\mathbb F_p) up to constant strict equivalence of the ordered coefficient pair.

The degree check is
[
\sum_i \deg d_i(t)+\sum_j \nu_t(e_j(t))=n,
]
where (d_i) are the finite Smith invariant factors and (e_j) the reversed Smith invariant factors. This is the determinant degree plus its order of vanishing at infinity.

## Important correction in interpreting the reversed chart

The *full degrees* of the reversed Smith factors must not be added as the infinity contribution. Only their (t)-adic valuations count. For example, over (\mathbb F_2),
[
Q=\operatorname{diag}(1,0,1),\quad K=\operatorname{diag}(0,1,1)
]
has (det(Q+tK)=t(1+t)) and (det(K+tQ)=t(1+t)). The finite contribution is degree 2, while the infinity contribution is the (t)-valuation 1; their sum is the dimension 3.

## Implementation

- `tools/regular_pencil_classification.py`: `regular_pencil_complete_profile(q,k,p)` computes both Smith charts, extracts the finite invariant factors and reversed (t)-adic exponents, and verifies regularity and the degree identity.
- `compare_regular_pencils_complete(...)` decides strict equivalence by comparing both collections.
- `tests/test_regular_pencil_classification.py` includes a regular (\mathbb F_2) pencil with no invertible rational projective member, plus a test distinguishing infinity partitions ([2]) and ([1,1]) even when finite divisors agree.

The implementation uses the existing exact polynomial-minor Smith routine and inherits its small-matrix minor budget. It does not construct explicit strict-equivalence witnesses or a canonical decomposition matrix. It applies to regular square pencils only; singular pencils additionally require left and right minimal indices.
