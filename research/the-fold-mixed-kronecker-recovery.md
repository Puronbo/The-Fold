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
