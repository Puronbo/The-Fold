# G-EP38 — constructive strict-equivalence witnesses in a rational chart

## Goal

G-EP37 decides strict equivalence of regular square pencils from their finite and infinite elementary divisors. G-EP38 adds a constructive path for the important subclass where the two pencils share an invertible projective member over the base field.

Suppose the common chart is finite, with (H_a=Q_a+\lambda K_a) and (H_b=Q_b+\lambda K_b) invertible. Define
[
A_a=H_a^{-1}K_a,\qquad A_b=H_b^{-1}K_b.
]
For the infinity chart, use (H_a=K_a,H_b=K_b) and (A_a=K_a^{-1}Q_a,A_b=K_b^{-1}Q_b).

Find an invertible intertwiner (P) satisfying
[
P A_a=A_bP.
]
Then set
[
T=P^{-1},\qquad S=H_bPH_a^{-1}.
]
A direct substitution gives
[
S Q_aT=Q_b,\qquad S K_aT=K_b.
]
Thus ((S,T)) is an explicit constant strict-equivalence witness.

## Exact search method

The intertwining equation is linear in the (n^2) entries of (P). The implementation computes a basis for this linear solution space over (\mathbb F_p), then enumerates its linear combinations until it finds an invertible member. The search has a configurable candidate budget. If the budget is exceeded, the result is explicitly inconclusive; it does not claim inequivalence.

A matching rational-canonical profile guarantees that the operators are similar, hence that an invertible intertwiner exists. The returned witness is nevertheless independently verified by exact modular matrix multiplication and invertibility checks.

## Implementation and limitations

- `tools/regular_pencil_witness.py`: `construct_regular_pencil_witness(...)`.
- `tests/test_regular_pencil_witness.py`: tests finite and infinity charts, explicit witness identities, profile-based non-equivalence, search-budget behavior, and a regular pencil with no base-field chart.
- The routine does **not** yet construct witnesses for pencils without a base-field invertible projective member. G-EP37 still classifies those pencils, but witness construction for them remains open.
- This is a bounded search in the intertwiner space, not a polynomial-time canonical-form constructor. It is suitable for small exact instances and for producing independently checkable certificates.
