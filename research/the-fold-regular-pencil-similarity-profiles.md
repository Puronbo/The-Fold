# G-EP35–G-EP36 — regular-pencil similarity profiles in invertible projective charts

## G-EP35: the invertible-Q chart

If (Qin M_n(\mathbb F_p)) is invertible, left multiplication by (Q^{-1}) sends
[
(Q,K)\longmapsto (I,A),\qquad A=Q^{-1}K.
]
Two normalized pairs ((I,A)) and ((I,B)) are strictly equivalent exactly when (A) and (B) are similar. Thus the rational-canonical invariant factors of (A) give a complete strict-equivalence fingerprint in this chart.

## G-EP36: any invertible projective member

The first coefficient need not be invertible. Search the projective line for a member
[
H=Q+\lambda K,\quad \lambda\in\mathbb F_p,
]
and finally the point at infinity (H=K). If a finite member is invertible, set (A=H^{-1}K). Left normalization gives
[
(H^{-1}Q,H^{-1}K)=(I-\lambda A,A).
]
If (K) is invertible, set (A=K^{-1}Q), obtaining ((A,I)).

For two ordered pencils, use the **same** projective point. Under a strict-equivalence change (Q'=SQT, K'=SKT), the normalized operator changes by conjugation:
[
A'=T^{-1}AT.
]
Conversely, similarity of the normalized operators gives simultaneous equivalence of both normalized coefficient matrices, and undoing the left normalizations gives strict equivalence of the original ordered pairs. Therefore the invariant factors of (A) are a complete decision invariant whenever the two pencils share an invertible projective member over the base field.

## Implementation

- `tools/regular_pencil_profile.py`: `regular_pencil_similarity_profile(q,k,p)` searches finite projective points ([1:\lambda]) and then ([0:1]), normalizes at the first invertible member, and computes the exact rational-canonical profile.
- `compare_regular_pencils(...)` searches for a common invertible projective point. It returns a complete yes/no decision if found, and `strictly_equivalent: null` with `decision_complete: false` if no common chart exists.
- `tests/test_regular_pencil_profile.py` covers the original chart, singular (Q) with another finite invertible member, the infinity chart, strict-equivalence invariance, distinct classes, and an important failure boundary.

## A regular pencil can have no invertible rational member

Over (mathbb F_2), take
[
Q=\operatorname{diag}(1,0,1),\qquad K=\operatorname{diag}(0,1,1).
]
Then
[
\det(aQ+bK)=ab(a+b)
]
is a nonzero homogeneous polynomial, so the pencil is regular. Yet it vanishes at all three points of (\mathbb P^1(\mathbb F_2)). Thus no base-field projective chart is invertible. The implementation correctly refuses to classify this case by the chart method; this refusal is not evidence of singularity or non-equivalence.

## Scope

G-EP36 extends complete strict-equivalence classification beyond the invertible-(Q) chart, but not to all regular pencils. A regular pencil can require an extension-field point to obtain an invertible member. This implementation does not yet construct such extensions, nor does it produce explicit strict-equivalence witnesses. It does not allow coefficient mixing as an equivalence operation; the projective point is used only to normalize both ordered coefficients consistently.
