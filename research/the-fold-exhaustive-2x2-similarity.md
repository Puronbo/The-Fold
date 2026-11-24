# G-EP152: Exhaustive 2×2 similarity-orbit audit over F₂ and F₃

This milestone exhaustively checks all 2×2 matrices over the two smallest prime fields. There are 16 matrices over F₂ and 81 over F₃.

For every matrix, the test independently computes the characteristic polynomial
\[
\chi_A(t)=t^2-\operatorname{tr}(A)t+\det(A)
\]
and enumerates all vectors \(v\) to decide whether \([v,Av]\) is a basis. The cyclic-vector predicate is compared with the production rational-canonical profile's one-invariant-factor condition.

The test then enumerates every invertible 2×2 change-of-basis matrix. For each representative, it computes the full conjugacy orbit \(P^{-1}AP\) and checks that this orbit is exactly the set of all matrices with the same production invariant-factor profile. Thus each profile fibre is checked for both containment directions against explicit conjugacy enumeration, rather than merely checking that conjugation preserves the profile.

This is exhaustive finite-field evidence for dimension two over F₂ and F₃. It is not an exhaustive classification over larger fields or dimensions, and it does not introduce a new production similarity algorithm.
