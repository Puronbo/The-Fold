# G-EP45 — Full rational-canonical bases and operator similarity witnesses

## Result

G-EP43 supplies primary invariant-subspace bases and G-EP44 supplies bounded
cyclic generators within each primary component. This milestone composes them
into a full basis and verifies a complete rational-canonical representation.

For a primary component associated with an irreducible polynomial (f), a
generator with annihilator (f^e) yields the Krylov columns
[
K_v=[v,Av,ldots,A^{edeg f-1}v].
]
In this ordered basis the restriction of (A) is the companion matrix of
(f^e), with coefficients in low-degree-first order. Concatenating these
bases over all elementary divisors and transporting them through the primary
decomposition basis gives a global invertible matrix (K). The constructed
block diagonal matrix (C) is checked by the exact identity
[
AK=KC,qquad K^{-1}AK=C.
]

The implementation is in `tools/rational_canonical_basis.py`:
- `construct_rational_canonical_basis(A,p)` returns (K,C,K^{-1}) and
  exact verification flags when all bounded primary searches succeed.
- `construct_operator_similarity_witness(A,B,p)` first compares complete
  rational-canonical invariant factors. If they differ, it decides
  non-similarity. If they agree, it constructs canonical bases (K_A,K_B)
  and returns
  [
  P=K_BK_A^{-1},qquad PA=BP.
  ]
  Every returned intertwining identity is verified exactly.

## What is now established

- A complete result is a directly auditable certificate, not just a matching
  fingerprint: the basis is invertible and (AK=KC) is checked.
- Matching rational-canonical profiles decide similarity over the same
  prime field, even if bounded generator search cannot find bases.
- When both basis searches succeed, the method returns an explicit invertible
  intertwiner (P).
- A profile mismatch is a complete negative decision.

## Boundaries

Cyclic-generator discovery remains bounded exhaustive enumeration over
(mathbb F_p^d) within each primary component. It is not a polynomial-time
algorithm and may fail to produce a basis within budget. Such a failure does
not contradict similarity: the complete invariant-factor comparison still
decides the mathematical question. In that case the API reports
`similar=true`, `witness_found=false`, and preserves the partial search
reports.

This is a matrix-similarity certificate over the base prime field. It does
not by itself solve a general singular matrix-pencil or Kronecker
decomposition problem. For regular pencils with a shared invertible chart,
the intertwiner can be used in the existing strict-equivalence construction;
the no-chart and general-pencil paths retain their previous bounded-search
limitations.

## Tests

`tests/test_rational_canonical_basis.py` checks:
1. a noncyclic nilpotent operator with elementary divisors (x^3) and (x);
2. assembly across distinct primary factors;
3. an explicit intertwiner between two differently based but similar
   noncyclic operators; and
4. complete rejection from a rational-canonical profile mismatch.

The test suite and CI results are the executable verification record. No
claim of a polynomial-time generator search or neural-network predictive
benefit is made.


## G-EP46 — Integration into regular-pencil witnesses

The shared-chart branch of `construct_regular_pencil_witness` now uses a
three-stage construction strategy:

1. For cyclic normalized operators, retain the inexpensive cyclic Krylov
   fast path.
2. If that path does not produce a witness, call
   `construct_operator_similarity_witness`. This handles noncyclic
   operators by independently assembling full rational-canonical bases and
   setting (P=K_BK_A^{-1}).
3. If bounded canonical-basis construction is incomplete, retain the existing
   nullspace/intertwiner-space search as a fallback.

For the normalized chart operators (A_a,A_b), the resulting (P) satisfies
(PA_a=A_bP). With chart pivots (H_a,H_b), the strict-equivalence
transformations are
[
S=H_bPH_a^{-1},qquad T=P^{-1}.
]
The implementation still verifies both original pencil equations
[
SQ_aT=Q_b,qquad SK_aT=K_b
]
and invertibility of (S,T). Thus the new basis strategy does not weaken the
certificate's final checks.

The new regression test uses a noncyclic operator with elementary divisors
(x^2,x^2) and a nontrivial change of basis. It asserts that the
rational-canonical-basis path is selected and that all pencil identities
verify. The no-chart path is unchanged: it still uses the direct bounded
finite-field search.
