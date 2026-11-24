# G-EP39 — witness construction without a rational invertible chart

G-EP38 constructed explicit strict-equivalence transformations when a shared invertible projective member over the base field existed. G-EP39 adds a general exact fallback for regular square pencils even when every rational projective member is singular.

## Direct equations

For a proposed left transformation (S\in GL_n(\mathbb F_p)), the witness equations
[
SQ_aT=Q_b,\qquad SK_aT=K_b
]
are linear in the entries of (T). The implementation enumerates candidate (S), rejects singular ones, solves the combined linear system for the affine space of possible (T), and searches that space for an invertible solution. A candidate is accepted only after both original matrix identities and both invertibility conditions are checked exactly.

Before searching, the no-chart path compares the complete finite/infinity regular-pencil profiles from G-EP37. Different profiles prove non-equivalence. Matching profiles establish equivalence; the direct search then attempts to produce the explicit certificate.

## Search budget and interpretation

The search is finite but exponential in the matrix dimension. `max_candidates` bounds the total number of left-transform and right-transform candidates examined. If the budget is exceeded, the function returns `strictly_equivalent=True` with `witness_found=False` and an explicit incomplete-search status, because classification and certificate construction are separate tasks. A complete search with no witness would signal an implementation or theorem inconsistency, since the matching complete regular-pencil profiles classify strict equivalence.

## Tests

The tests include a regular pencil over (\mathbb F_2) with determinant (ab(a+b)), hence no invertible point on (\mathbb P^1(\mathbb F_2)), and a nontrivial pair obtained from it by known invertible left and right transformations. The returned transformations are verified against both coefficient matrices. A no-chart profile mismatch is also checked.

## Limitations

This is a generic constructive fallback, not an efficient canonical-form algorithm. It does not yet exploit block structure to reduce the exponential search. The chart-based intertwiner method remains the preferred route when available.
