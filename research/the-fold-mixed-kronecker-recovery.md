# G-EP49 — Bounded automatic mixed Kronecker recovery

## Goal

G-EP48 recovered pure right-only and pure left-only pencils. G-EP49
extends recovery to an unsplit pencil with right singular blocks, a regular
part, and left singular blocks.

## Construction

1. Compute the complete finite-field Kronecker profile: both lists of
   polynomial minimal indices, the normal rank, finite Smith invariant
   factors, and infinity t-adic elementary-divisor sizes.
2. Assemble the corresponding canonical mixed target from right and
   transposed-left Kronecker blocks plus finite companion and infinity
   nilpotent regular blocks.
3. Search a structured, bounded family of invertible left transformations.
   For each candidate S, solve the equations
   `S Q T = Q_can` and `S K T = K_can` simultaneously as one affine
   linear system in the entries of T.
4. Test invertibility of T and independently audit both strict-equivalence
   identities and both determinants over F_p.

This avoids pretending that the polynomial minimal-vector chains alone
supply compatible complementary bases in the mixed case. The profile
determines the target; the explicit constant witness is constructed by the
bounded linear-algebra search.

## API

`tools/mixed_kronecker_recovery.py` exposes
`recover_mixed_kronecker_pencil(q,k,p,...)`.

A successful result includes the discovered right and left minimal indices,
regular dimension, canonical target, explicit S and T, profile, and exact
audit. If the profile is incomplete or the structured search budget is
exhausted, the routine returns `recovered=false` and
`decision_complete=false`. Search failure is not treated as inequivalence.

## Limitations

This is a bounded constructive recovery algorithm, not a polynomial-time
general Kronecker canonical-form algorithm. The left-transform candidate
family is structured (permutations, diagonal scalings, and one elementary
shear); arbitrary mixed pencils may require transformations outside the
searched family. The profile calculation is itself bounded by the configured
minimal-index degree and minor budgets. Every positive result is exact and
independently verified; negative/incomplete search results are inconclusive.

## Tests

Tests cover an unsplit direct sum containing a right block, a left block,
and a regular block; recovery after a nontrivial left-basis shear; and
explicit rejection of an incomplete bounded profile.


## G-EP73 — Recovery boundary analysis

Added a reproducible boundary grid for automatic mixed-pencil recovery. Canonical mixed pencils with right/left minimal-index pairs (1,1), (2,1), and (2,2), plus a one-dimensional regular block, are checked over F₂, F₃, and F₅. Each positive control must have a complete profile, an explicit recovered witness, matching minimal-index lists, and a passing strict-equivalence audit.

A separate regression distinguishes two non-success outcomes: an incomplete Kronecker profile caused by a too-small degree bound, and a complete profile whose witness search is stopped by a one-candidate budget. Both remain inconclusive, but their profile state and diagnostic reasons are distinct. This prevents a bounded-search failure from being presented as a mathematical obstruction.

**Scope:** the grid covers selected small canonical families and is not a universal complexity or completeness result. A positive result is an exact verified witness; incomplete profiles and budget-limited searches remain undecided.


## G-EP74 — Structured versus exhaustive finite-field validation

Added direct comparisons between bounded structured recovery and exhaustive finite-field witness search on small mixed pencils. A deliberately one-candidate structured run is required to remain inconclusive, while exhaustive search with a larger explicit budget finds and exactly verifies a witness for the same F₂ pencil. Additional F₂/F₃ positive controls require both search modes to recover certificates with matching right/left minimal-index profiles and independently passing strict-equivalence audits.

The tests compare mathematical outputs, not necessarily the chosen transforms: multiple valid (S,T) witnesses may exist. Exhaustive mode remains exponential. A positive result is an exact witness; a negative result may be called complete only when the implementation actually exhausts all invertible S and all compatible affine T solutions. A budget cutoff, even with a complete Kronecker profile, remains inconclusive. This milestone does not claim to exhibit a genuine mathematical non-equivalence case because the tested profile-derived canonical targets are expected to represent the same pencil class when the profile is correct.


## G-EP75 — Exhaustive enumeration integrity

Refactored exhaustive search to use two small, independently testable iterators. The left-matrix iterator emits the identity first and then every remaining flattened matrix in lexicographic finite-field product order, excluding the identity tuple exactly once. The affine-solution iterator enumerates every coefficient tuple for a nullspace basis, including the zero-dimensional singleton case.

New regressions compare the left-matrix stream against the full Cartesian product for F₂ and F₃ at dimensions one and two, checking exact cardinality, set equality, uniqueness, and identity-first ordering. The affine iterator is compared against brute-force solutions of a small linear system over F₃, with separate unique-solution and unconstrained-space checks. These tests establish the iterator combinatorics on the tested finite cases; they do not turn a budget-limited run into an exhaustive decision or prove the separate affine solver correct for all inputs.

The search budget still counts both examined left matrices and tested right-transform matrices. Exhaustive negative status is only returned when both nested streams complete without hitting the budget; positive results remain backed by exact strict-equivalence verification.


## G-EP76 — Independent affine-solver verification

Added a deterministic exhaustive cross-check of `_solve_affine` against brute-force solution sets. For each prime field F₂ and F₃, the test visits every coefficient matrix with zero through two rows and zero through two columns, and every right-hand side of the matching row dimension. It independently enumerates all candidate vectors, then checks that the solver returns `None` exactly for inconsistent systems. For consistent systems, the affine iterator must produce the exact brute-force solution set with no duplicates.

The grid includes zero-equation systems, zero-variable systems, rank-deficient systems, unique solutions, redundant equations, and inconsistent systems insofar as they occur in the exhaustive matrix/RHS enumeration. The test checks more than one thousand systems in total.

**Scope:** this is a finite exhaustive regression over the stated dimensions and fields. It does not prove the elimination implementation correct for arbitrary dimensions, arbitrary prime fields, or malformed mismatched matrix/RHS inputs.


## G-EP77 — Exhaustive-search decision and budget integrity

Added three independent checks around the exhaustive mixed-recovery decision path.

1. The modular determinant implementation is compared against an independently evaluated Leibniz permutation formula for every matrix of dimensions one through three over F₂ and F₃. Both the determinant value and its invertible/singular classification must agree.
2. A controlled same-shape impossible target exercises the exhaustive negative branch. The test confirms that a complete negative is emitted only after the entire left-matrix stream and the relevant affine right-transform search finish. Reducing the candidate budget to one interrupts the stream and must leave `decision_complete=false`.
3. A one-dimensional positive control confirms that the candidate budget counts both the left-transform candidate and the right-transform candidate: the identity witness is found with exactly two examined candidates.

The impossible-target test patches only the profile-derived target to create a deterministic search-path control; it is not a claimed mathematical non-equivalence example for a genuine Kronecker canonical target.

**Scope:** these tests audit determinant filtering and search-state/budget semantics on finite controls. They do not establish that every profile-derived target is valid in arbitrary dimensions or that exhaustive search is computationally practical beyond small fields and dimensions.


## G-EP78 — Replayable exhaustive negative certificates

Added `verify_mixed_kronecker_negative_certificate(q, k, p, result, ...)`. The verifier does not accept the result's completion flag or candidate count at face value. It validates the negative/exhaustive schema, recomputes the complete Kronecker profile from the supplied pencil and configured profile bounds, reconstructs the canonical target, and independently streams the full Cartesian family of left matrices. For each invertible left matrix it solves the compatible affine right-transform system and enumerates every solution vector, rejecting the claim if any invertible right transform exists.

The replayed candidate count must exactly match the reported count and remain within the reported positive budget. The verifier also checks the field, source shape, search mode, completion/recovery flags, profile, reason, and scope metadata. Regressions cover a controlled completed negative, forged candidate count and budget, changed search mode, forged completion/recovery flags, altered explanatory scope, and a budget-limited result.

The controlled impossible-target fixture patches target construction for the recovery and replay calls; it exercises finite search replay and metadata tamper detection only. It is not evidence of a genuine non-equivalent pencil. The verifier's guarantee is limited to exhaustive finite-field replay with the same configured profile bounds; it does not establish polynomial-time behavior or generalize beyond the supplied field/input.


## G-EP79 — Replay-verifier input and certificate boundary hardening

Hardened verify_mixed_kronecker_negative_certificate at both sides of its trust boundary. Caller-supplied Q/K inputs must be nonempty matrix sequences with nonempty rows and integer entries; booleans and floating-point values are rejected. The shared pair validator checks equal rectangular shapes and the prime field. Invalid caller inputs raise ValueError, rather than being confused with a failed certificate.

Untrusted result objects must be dictionaries with every required schema, field, shape, recovery, decision, search-mode, budget, count, profile, reason, and scope field. Missing or altered metadata, non-dictionary result containers, malformed profile containers, and malformed nested replay data fail closed with verified=false. The replay's internal malformed-data guard prevents ordinary structure/type/index errors from escaping as verifier crashes.

Regressions exercise null/list/string/scalar result containers; each required field missing in turn; malformed profile values; malformed, ragged, mismatched, boolean, and floating-point caller matrices; and boolean/composite field parameters.

**Boundary distinction:** invalid caller inputs raise ValueError; invalid or malformed certificate data returns a negative verification result. This hardening does not expand the mathematical scope of the finite-field replay.


## G-EP80 — Profile bounds bound into replay certificates

Exhaustive recovery results now carry profile_max_degree and profile_max_minors, the exact bounds passed to the profile computation. The fields are emitted consistently for incomplete-profile outcomes, positive witnesses, and bounded/exhaustive negative outcomes. The negative-certificate verifier no longer accepts profile-bound overrides from its caller: it validates the certificate's bounds (non-boolean integers, degree at least zero, minor budget positive) and recomputes the profile from those recorded values. Thus replay does not depend on a caller remembering the original configuration. Missing or malformed bounds fail closed; a changed bound is detected when it changes the recomputed profile. Bounds that happen to yield identical profile output are observationally equivalent and cannot be distinguished from the certificate alone.

Tests cover custom non-default bounds, successful replay from metadata alone, mutation of both bound fields, missing bound fields, and malformed boolean, floating-point, negative, or zero-invalid values. Existing exhaustive search-budget and finite-field enumeration semantics are unchanged. The controlled impossible-target fixture remains a replay-control test, not a genuine mathematical non-equivalence example.
\n\n## G-EP81 — Full mixed-recovery certificate replay\n\nA unified recovery-certificate verifier now recomputes the source profile using the recorded bounds and reconstructs the profile-derived canonical target whenever profile data is complete. For positive results it checks canonical coefficient matrices, minimal-index and regular-dimension metadata, canonical block shapes, the exact constant strict-equivalence witness, the multi-block direct-sum audit, and consistency between the recorded method description and search mode. For incomplete profiles and budget-limited/structured failures it validates the stated inconclusive outcome without converting it into a non-equivalence claim. Completed exhaustive negatives delegate to the exhaustive finite-field replay verifier. Recovery outputs now include search mode and candidate budget consistently, including incomplete-profile results.\n
 
## G-EP82 — Positive-certificate adversarial replay boundary

Positive mixed-recovery replay now validates both returned transform containers before invoking the strict-equivalence auditor: each must be a square list/tuple of the exact source dimension, with rectangular rows and genuine integer entries (booleans and floats are rejected). The replay guard also converts malformed nested-audit ValueError failures into verified=false, while caller pencil/field validation remains outside that guard and continues to raise ValueError.

Adversarial regressions cover absent/scalar/empty/ragged/wrong-size transforms, boolean and floating-point entries, singular transforms, forged or missing fields in the nested strict-equivalence audit, malformed audit containers, and forged/missing multi-block audit data. The verifier recomputes both audits and compares the complete stored structures, rather than trusting nested success flags. Separate tests preserve the boundary: invalid caller matrices or fields raise ValueError; malformed positive certificate contents fail closed with verified=false.

This is a replay/input-boundary hardening change. It does not change recovery search, prove uniqueness of canonical witnesses, or broaden the mathematical scope of finite-field strict-equivalence verification.


## G-EP83 — Type-exact positive profile and canonical reconstruction

Positive recovery replay reconstructs the profile from the supplied pencil and certificate-bound profile limits, then rebuilds the canonical target and block shapes from that recomputed profile. Certificate comparisons are type-exact and recursive: Python boolean/integer equality can no longer let a forged boolean stand in for an integer in source dimensions, profile entries, canonical matrices, minimal-index data, regular dimensions, or block shapes.

Adversarial tests mutate nested profile integers, source-shape entries, canonical matrix entries, regular dimensions, and block-shape entries into booleans, and alter canonical container types. Each mutation must fail replay while the unmodified positive certificate remains valid. This strengthens deterministic certificate reconstruction and representation integrity; it is not a separate Kronecker classifier, a uniqueness proof, or a claim that canonicalization is independent of the existing exact profile/canonical-target routines.


## G-EP84 — Cross-field positive replay and witness non-uniqueness

Added positive recovery replay controls over F₂, F₃, F₅, and F₇ using the same independently invertible left/right elementary basis scramblings. Each recovered certificate must replay against its exact source pencil and field. Adversarial variants forge the field label and insert a boolean into a transform entry; both must fail closed.

A separate F₃/F₅/F₇ control rescales a valid witness by a nonzero scalar, replacing S with cS and T with c⁻¹T. The replay verifier accepts these distinct witnesses when the witness-dependent strict-equivalence and multi-block audit records are regenerated for the rescaled S/T pair. Stale nested audit records remain invalid. This guards against treating a particular transform pair as canonical while preserving full audit-to-witness binding.

**Scope:** these are deterministic finite-field regression cases for the selected 4×4 mixed family. They exercise replay and witness flexibility, not universal recovery completeness, witness uniqueness, or a separate classifier.


## G-EP85 — Positive replay metadata and nested-audit adversarial coverage

Positive replay now compares the complete recomputed strict-equivalence and multi-block audit records with recursive type-exact equality, closing Python boolean/integer aliases inside nested audit dictionaries as well as their matrix/list contents. Expanded adversarial tests remove every required top-level positive field in turn and substitute wrong types or boolean/integer aliases in the recovery metadata. Nested strict-equivalence and multi-block audit records are tested for boolean/integer aliases and container substitutions. Cross-field controls build valid witnesses over F₃, F₅, and F₇, transplant S/T pairs between fields, and freshly recompute the nested audits in the destination field. A transplanted pair is accepted if it independently satisfies the destination-field identities; a subsequent transform-entry mutation is rejected even when its nested audits are freshly recomputed. Witness provenance is not a certificate property—algebraic validity in the supplied field is.

**Scope:** these tests validate fail-closed certificate replay and field binding for the selected mixed-pencil fixture. They do not establish universal recovery completeness, uniqueness of witnesses, or an independent classifier.


## G-EP86 — Canonical block-order and nested-matrix replay integrity

Added positive replay mutations for reordered canonical block-shape metadata, altered block dimensions, canonical target matrix entries, and nested transformed/block matrix entries in the multi-block audit. Every mutation must fail against the recomputed canonical target and witness audit.

A separate control consistently permutes the right-singular, regular, and left-singular blocks, including the corresponding row/column transformations and ordered shape list. The standalone multi-block witness verifier accepts this reordered direct-sum presentation because it is algebraically valid. The mixed-recovery certificate verifier rejects the same reordered presentation because its certificate schema binds the profile-derived canonical target to one deterministic block order. Thus algebraic validity of a reordered decomposition is distinguished from conformance to this recovery certificate's canonical serialization.

**Scope:** selected 4×4 mixed fixture and exact constant transformations over F₅. This tests certificate representation integrity and the ordered multi-block witness contract; it is not a uniqueness theorem for decompositions.


## G-EP87 — Permutation coverage and malformed partition boundaries

The standalone multi-block direct-sum verifier now rejects boolean and non-integral entries in the source pencil coefficients and both transformation matrices at its matrix-shape validation boundary. This prevents Python's integer coercion from silently accepting booleans or truncating floating-point values during modular arithmetic.

Regression coverage enumerates all six permutations of the three-block mixed fixture (right-singular, left-singular, regular). Each consistently permuted row/column basis and ordered rectangular block-shape list must still verify as a valid direct sum. Negative controls reject missing/underspecified partitions, row or column totals inconsistent with the source dimensions, zero-by-zero blocks, malformed shape entries, and non-integral matrix entries.

**Scope:** exhaustive permutations of one three-block 4×4 fixture over F₅. Shape lists define consecutive, disjoint rectangular partitions by construction; malformed totals and shapes are rejected, but no separate interval-overlap representation exists in this API.


## G-EP88 — Multi-block witness adversarial verification

Added focused adversarial coverage for the standalone supplied multi-block direct-sum verifier:

- Singular left and right transforms with otherwise valid dimensions and integer entries return structured audits with the corresponding invertibility flag false and `direct_sum_verified=false`; they do not raise caller-input errors.
- Adding multiples of the prime to source coefficients and transforms produces identical normalized transformed matrices, block matrices, and verification records.
- Field-boundary tests reject boolean and floating-point field values, values below two, and composite values; valid identity witnesses pass over F₂ and F₃.
- Null, empty, ragged, and dimension-incompatible nested source/transform matrices are rejected with `ValueError`.

**Boundary:** malformed caller inputs remain exceptions; a structurally valid but singular witness is a negative audit. A failed supplied witness says nothing about whether a different witness or decomposition exists. This milestone adds finite regression coverage and does not expand decomposition discovery or establish uniqueness.


## G-EP89 — Generated rectangular partition coverage

Added deterministic generated-style multi-block fixtures over F₂, F₃, F₅, and F₇. The partition grid includes rectangular blocks with zero rows or zero columns, while excluding zero-by-zero blocks; every full source pencil remains nonempty and rectangular. Valid block-diagonal coefficient pairs pass with identity transforms. For partitions containing a cross-block location, an injected nonzero coefficient is rejected by the off-diagonal and aggregate checks. Additional cases reject zero-by-zero blocks and row/column total mismatches.

This covers the verifier's permitted rectangular edge cases, not arbitrary overlapping interval partitions, a decomposition-discovery algorithm, or a universal correctness proof.
