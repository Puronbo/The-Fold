**Rational-canonical regular-pencil witness integration (G-EP46):** the shared-chart path in `tools/regular_pencil_witness.py` now keeps its cyclic Krylov fast path and, for noncyclic normalized operators, falls back to full rational-canonical bases from G-EP45. It constructs (P=K_BK_A^{-1}), then (S=H_bPH_a^{-1}), (T=P^{-1}), and exactly verifies both original pencil equations and invertibility. If bounded basis construction is incomplete, the prior intertwiner-space fallback remains available. The no-chart path is unchanged and still uses bounded direct search. See the G-EP45/46 research note and the noncyclic regression test.


**Composable Kronecker component assembly (G-EP47):** `tools/kronecker_component_assembly.py` composes structural recovery of individual right/left singular blocks with regular-pencil canonical witnesses. Given a proposed component partition, it assembles the block-diagonal target and block-diagonal (S,T), then independently verifies (SQT=Q_{\\rm can}) and (SKT=K_{\\rm can}). This is certified assembly, not automatic discovery of the component partition from an arbitrary unsplit pencil. See `tests/test_kronecker_component_assembly.py` and `research/the-fold-kronecker-component-assembly.md`.


**Multiple-chain pure singular recovery (G-EP48):** `tools/pure_singular_pencil_recovery.py` recovers any number of right-only or left-only singular Kronecker blocks from the full pencil, including after arbitrary constant basis scrambling. It uses certified polynomial minimal-vector chains, constructs domain/codomain bases, and verifies explicit global strict-equivalence transformations. It does not yet recover a regular summand or mixed left/right pencils. See `tests/test_pure_singular_pencil_recovery.py` and `research/the-fold-pure-singular-pencil-recovery.md`.

**Bounded automatic mixed Kronecker recovery (G-EP49):** `tools/mixed_kronecker_recovery.py` discovers the right and left minimal-index lists and regular elementary divisors from one unsplit pencil, assembles the mixed canonical target, and searches structured invertible left transforms while solving exactly for the right transform. Every positive result passes the strict-equivalence audit. The witness search is deliberately bounded and its candidate family is not universal; failure is inconclusive, not a proof of inequivalence. See `tests/test_mixed_kronecker_recovery.py` and `research/the-fold-mixed-kronecker-recovery.md`.

**Exhaustive mixed-pencil witness mode (G-EP50):** `recover_mixed_kronecker_pencil(..., search_mode="exhaustive")` streams all left matrices over the finite field and all compatible affine right-transform solutions, under an explicit candidate budget. A found witness is exactly audited; a fully exhausted negative search is a finite-field non-equivalence certificate; budget exhaustion is inconclusive. Exponential by design, intended for small cases. See `research/the-fold-mixed-kronecker-recovery.md`.

**Minimal-chain geometry certificates (G-EP51):** `tools/minimal_chain_geometry.py` computes exact ranks of the right minimal-vector coefficient family in the domain and the left minimal-covector family in the codomain. It returns the underlying bounded nullspace certificate and explicitly distinguishes independence from a full mixed decomposition: complementary regular bases and cross-chain compatibility are not inferred. See `research/the-fold-minimal-chain-geometry.md` and its tests.

**Minimal-chain adapted coordinates (G-EP52):** `tools/minimal_chain_adapted_coordinates.py` builds full domain and codomain bases beginning with independent right-chain coefficient vectors and left-chain coefficient covectors. It returns (Q'=SQT), (K'=SKT), and exact invertibility/identity checks. Complementary coordinates are exposed without asserting that the residual block is regular or decoupled. See `research/the-fold-minimal-chain-adapted-coordinates.md`.


**Residual-pencil diagnostics (G-EP53):** `tools/residual_pencil_diagnostic.py` partitions the G-EP52 adapted pencil into chain and complementary coordinate blocks, reports cross-coupling, and profiles the bottom-right block when it is nonempty and square. The residual profile is explicitly coordinate-local; it is not claimed to be the original pencil's regular part unless decoupling is separately established. See `research/the-fold-residual-pencil-diagnostic.md`.

**Exact residual-pencil decoupling certificates (G-EP54):** `tools/residual_pencil_decoupling_certificate.py` checks both off-diagonal blocks in both adapted coefficient matrices, reports exact ranks and nonzero entries, and reconstructs the block-diagonal pair for equality checks against the adapted pencil. A positive result certifies a direct-sum split in the computed coordinates and carries the G-EP52 strict-equivalence witnesses; a negative result exposes coupling without claiming decomposition or residual regularity. See `tests/test_residual_pencil_decoupling_certificate.py` and `research/the-fold-residual-pencil-decoupling-certificate.md`.

**Minimal-chain annihilator complements (G-EP55):** `tools/minimal_chain_decoupling_completion.py` searches for complementary domain vectors in the common kernel of the left-chain constraints and complementary codomain covectors annihilating both coefficient images of the right-chain space. When both spaces extend the fixed chain bases, it constructs exact S,T witnesses and verifies both cross-coupling blocks vanish. Failure is explicitly inconclusive and does not rule out other splittings. See `tests/test_minimal_chain_decoupling_completion.py` and `research/the-fold-minimal-chain-decoupling-completion.md`.

**Minimal-chain annihilator feasibility certificates (G-EP56):** extends G-EP55 with exact rank criteria for whether the fixed right/left chain spans can be completed inside their computed annihilator spaces. It reports combined-span ranks, ambient dimensions, deficiencies, and feasibility flags. These criteria are necessary and sufficient within those fixed spaces; because each nullspace basis spans the full candidate space, exhaustive enumeration of linear combinations would be redundant. A deficient rank rules out only this particular annihilator-based completion, not other possible pencil splittings. See `research/the-fold-minimal-chain-annihilator-feasibility.md` and the updated tests.

**General direct-sum witness verifier (G-EP57):** `tools/pencil_direct_sum_witness.py` independently verifies a supplied constant strict-equivalence witness for a two-block direct sum of a rectangular pencil. It accepts arbitrary invertible left/right transforms and a compatible rectangular block cut, recomputes both transformed coefficients, and checks both off-diagonal blocks exactly over the prime field. This separates general witness verification from G-EP55/56's restricted annihilator-based construction. It does not discover a decomposition or assert regularity of either summand. See `tests/test_pencil_direct_sum_witness.py`.


**Multi-block direct-sum witness verifier (G-EP58):** `tools/pencil_multi_direct_sum_witness.py` independently verifies a supplied constant strict-equivalence witness for two or more rectangular diagonal pencil blocks. It checks the ordered block-shape partition, invertibility of both transforms, and every off-diagonal block in both transformed coefficient matrices over the prime field. It audits supplied decompositions without assuming regularity or discovering the split. See `research/the-fold-multi-block-direct-sum-witness.md` and `tests/test_pencil_multi_direct_sum_witness.py`.


**Integrated multi-block audit of mixed recovery (G-EP59):** successful `recover_mixed_kronecker_pencil` results now include `canonical_block_shapes` in canonical construction order and a `multi_block_direct_sum_audit` from G-EP58. The audit independently checks the recovered S,T against each right-minimal, left-minimal, and regular diagonal block, in addition to the existing whole-target strict-equivalence audit. This is a second exact certificate view, not a new discovery method; negative or budget-limited searches retain their previous semantics. See the updated mixed-recovery tests.


**Integrated multi-block audit of supplied component assembly (G-EP60):** successful `assemble_kronecker_components` results now include `canonical_block_shapes` in the supplied component order and an independent `multi_block_direct_sum_audit` from G-EP58. The audit verifies that the assembled block-diagonal transforms annihilate every cross-component block in both pencil coefficients, alongside the existing whole-pencil strict-equivalence audit. Failed component recovery still returns an incomplete result without a success certificate; this remains supplied-partition assembly, not decomposition discovery. See `research/the-fold-kronecker-component-assembly.md` and its tests.


**Component-report consistency certificate (G-EP61):** successful `assemble_kronecker_components` results now include `component_consistency_audit`. It cross-checks each reported source shape against both source coefficients, checks both canonical coefficient block shapes, validates right/left singular block dimensions against their recovered minimal indices and regular block squareness, and reconciles ordered component dimensions with the assembled source and canonical shapes. This is a metadata/matrix consistency audit, not independent component classification or decomposition discovery.


**Per-component strict-equivalence certificates (G-EP62):** supplied-partition assembly now independently audits each component's own (S_i,T_i) against its source and canonical pair before composing the global block-diagonal witness. Successful results expose ordered `component_witness_audits` and an aggregate `all_component_witnesses_verified` check, alongside the existing global, multi-block, and metadata-consistency audits. This localizes a component witness failure rather than relying only on the assembled identity; it does not discover a partition. See `research/the-fold-kronecker-component-assembly.md` and its tests.
\n\n**Component witness composition audit (G-EP63):** supplied-partition assembly now rebuilds the global block-diagonal S and T solely from the ordered local component certificates, compares them with the returned assembled transforms, and replays both global pencil identities using the reconstructed matrices. Successful results expose `component_witness_composition_audit` and `component_witness_composition_verified`. This independently checks composition consistency; it does not discover a partition or establish uniqueness. See the component-assembly research note and tests.\n

**Adversarial component-witness composition checks (G-EP64):** the G-EP63 composition audit now validates every local left/right transform as a nonempty square matrix before block-diagonal assembly, and rejects empty or malformed certificate sequences with explicit `ValueError` diagnostics. Regression tests tamper with a local transform and verify both transform-comparison and global replay checks fail; dimension-incompatible and malformed certificates are rejected. Reordering is not treated as inherently invalid: when local transforms are interchangeable (for example, identity witnesses of compatible dimensions), order alone need not change the mathematics. See `tests/test_kronecker_component_assembly.py` and the component-assembly research note.


**Component certificate provenance and binding (G-EP65):** the composition audit now independently re-runs strict-equivalence verification for every local (S_i,T_i) against that component's own source and canonical coefficient pair. It checks certificate/block-list cardinalities, exposes the per-component replay audits, and includes an aggregate source/target-binding check. The stored boolean from an earlier local audit is not trusted as a substitute for recomputation. The global composition and transform-equality checks remain separate. See the component-assembly research note and adversarial tests.


**Component certificate mutation and replay integrity (G-EP66):** the composition audit now validates all four ordered block lists and their cardinalities before indexing or replaying any component. Adversarial tests change a bound source block and a bound canonical block while retaining the old transforms, and verify that fresh local replay fails even when stored success metadata is forged. A complementary regression proves that forged stored failure metadata cannot suppress a mathematically valid recomputed certificate. This tests mutation sensitivity for the supplied ordered component pairs; it does not establish component discovery, identity outside that ordering, or uniqueness.


**Component input and dimension integrity (G-EP67):** supplied component matrices are now validated at the assembly boundary before modular arithmetic. Matrix and row containers must be nonempty ordered sequences, rows must be rectangular with nonzero width, entries must be integers (booleans and floating-point values are rejected), and each Q/K pair must have identical dimensions. Field parameters are checked as genuine integers (not booleans) before primality validation. Regression coverage includes malformed containers, ragged/empty matrices, non-integral entries, invalid/composite fields, and Q/K dimension mismatches. This hardens input diagnostics without changing the allowed rectangular component shapes or the supplied-partition scope.


**Independent reconstruction of assembly certificates (G-EP68):** adds `verify_kronecker_component_assembly_certificate`. Given the original ordered component inputs and a returned assembly result, it deterministically reruns the component constructors and compares source/canonical matrices, dimensions, block shapes, local and global transforms, component reports, and all stored audits/checks. Adversarial regressions mutate each certificate-bearing field and require detection. This is independent of the supplied output object, but intentionally reuses the existing constructors: it is an implementation-level reconstruction/replay check, not a second classification algorithm, partition-discovery method, or uniqueness proof. See the component-assembly research note.


**Direct algebraic certificate audit (G-EP69):** adds `verify_kronecker_component_assembly_algebraically`, which does not rerun canonical constructors. It rebuilds source block-diagonal matrices from the caller's original inputs, checks the claimed canonical block structure, replays every local and global strict-equivalence identity over the finite field, and verifies that global transforms are exactly the block-diagonal composition of the supplied local witnesses. Adversarial tests cover matrix/transform tampering and show that forged stored audit flags do not control the result. This remains conditional on the supplied component partition and local witnesses; it is not a partition-discovery or uniqueness algorithm.


**Adversarial algebraic assembly-certificate verification (G-EP70):** hardens `verify_kronecker_component_assembly_algebraically` to fail closed on malformed nested certificate structures and malformed canonical/local/global matrices. Certificate matrices and transforms now require rectangular integer entries (booleans and floats are rejected), malformed local witness records cannot leak indexing/type exceptions, and singular or dimension-incompatible transforms fail the algebraic replay. The new adversarial tests cover missing fields, malformed containers and entries, noninvertible local witnesses, invalid field arguments, and malformed component inputs. The verifier still distinguishes malformed caller inputs (explicit `ValueError`) from malformed certificate data (a negative verification result). This remains a verifier for supplied ordered components, not partition discovery or a uniqueness proof.


**Seeded randomized certificate verification (G-EP71):** adds reproducible randomized tests over prime fields F₂, F₃, F₅, and F₇. Generated cases vary right/left singular minimal indices, regular one-dimensional pencil coefficients, and component ordering; every successfully assembled certificate is independently checked by the direct algebraic verifier. A second seeded suite mutates a randomly selected canonical coefficient entry and requires verification to fail. Fixed seeds keep failures reproducible. These tests broaden finite-field and block-layout coverage but are not a probabilistic proof of correctness.


**Seeded basis-scrambled component recovery (G-EP72):** extends randomized coverage by independently applying reproducible invertible constant left/right basis changes to each right-singular, left-singular, and regular component before assembly. The transformed mixed components are shuffled and passed through the existing recovery/canonicalization pipeline; every completed result must pass the direct algebraic certificate verifier. Cases span F₂, F₃, F₅, and F₇ with fixed seeds. This is finite regression evidence for basis-scrambled examples, not a universal recovery theorem or a polynomial-time guarantee.


**Mixed-recovery boundary grid (G-EP73):** adds deterministic positive controls across right/left minimal-index pairs (1,1), (2,1), and (2,2) over F₂, F₃, and F₅, each with a regular block and exact strict-equivalence verification. Additional regressions explicitly distinguish an incomplete profile (degree bound too small) from a complete profile with an exhausted witness-search budget. Both negative outcomes remain inconclusive; neither is reported as a proof of non-equivalence.


**Structured/exhaustive recovery cross-checks (G-EP74):** adds small-field comparisons between bounded structured recovery and exhaustive finite-field witness enumeration. A one-candidate structured search must remain inconclusive, while a larger exhaustive F₂ search resolves the same input with an exact witness. F₂/F₃ positive controls require matching minimal-index profiles and independently verified strict-equivalence witnesses in both modes. Different valid transforms are allowed. Exhaustive negative decisions remain valid only after complete enumeration; budget exhaustion is never a proof of inequivalence. See the G-EP74 section in research/the-fold-mixed-kronecker-recovery.md.


**Exhaustive-search enumeration integrity (G-EP75):** factors exhaustive left-matrix and affine right-transform enumeration into testable iterators. Finite regression tests check exact coverage and duplicate freedom of all left matrices over F₂/F₃ at dimensions one and two, and compare affine-space enumeration with brute-force solutions over F₃. The candidate budget counts both left and right candidates; budget cutoffs remain inconclusive. These finite tests audit enumeration mechanics without claiming a universal proof of the affine solver. See G-EP75 in research/the-fold-mixed-kronecker-recovery.md.


**Independent affine-solver verification (G-EP76):** exhaustively compares `_solve_affine` with independently enumerated solution sets for every coefficient matrix and right-hand side with zero through two equations and variables over F₂ and F₃. It checks inconsistency detection, exact affine coverage, and duplicate freedom, including empty equation systems and zero-variable systems. This is exhaustive finite regression coverage for the stated small grid, not a proof for arbitrary dimensions or fields. See G-EP76 in the mixed Kronecker recovery research note.


**Exhaustive-search decision and budget integrity (G-EP77):** independently cross-checks modular determinant values against the permutation formula on all matrices through dimension three over F₂/F₃, verifies that exhaustive negative status requires complete left/right candidate enumeration, and confirms the budget counts both S and T candidates. A patched impossible-target fixture exercises search control flow only; it is not a mathematical non-equivalence example. See G-EP77 in the mixed Kronecker recovery research note.


**Replayable exhaustive negative certificates (G-EP78):** adds an independent verifier that recomputes the input's complete Kronecker profile, enumerates every left matrix and compatible affine right-transform solution, and checks the reported candidate count and negative-result metadata. It rejects forged completion flags, search modes, counts, budgets, explanations, and budget-limited runs. This is an exact replay for the stated finite field and profile bounds, not a universal polynomial-time method.


**Replay-verifier boundary hardening (G-EP79):** validates caller matrices as nonempty rectangular integer sequences and rejects booleans/floats and invalid fields as caller-input errors. Malformed result containers, missing metadata, and malformed profile structures fail closed with a negative verification result. Tests distinguish invalid caller inputs (ValueError) from untrusted certificate data (verified=false).


**Certificate-bound profile parameters (G-EP80):** exhaustive negative results now record the exact max_degree and max_minors used to compute their Kronecker profile. Replay takes these bounds from the certificate rather than requiring remembered caller arguments, validates their types/ranges, and recomputes the profile with those exact values. Omitting either field or supplying boolean/float/negative/zero-invalid values fails closed. Replay recomputes using the exact recorded values; if a changed bound changes the resulting profile, the profile comparison fails. Different bounds that happen to produce the same profile are observationally equivalent to this replay and cannot be distinguished from the output alone. Custom non-default bounds are replayed directly from the result metadata.
\n\n**Full recovery replay (G-EP81):** `verify_mixed_kronecker_recovery_certificate` recomputes the profile and canonical target for every outcome. Positive results are checked against reconstructed canonical matrices, minimal-index/regular metadata, exact strict-equivalence transforms, and the multi-block direct-sum audit. Incomplete-profile and bounded-search failures are replayed as accurately described inconclusive outcomes, not negative decisions; exhaustive negatives continue through the G-EP78 replay path. Recovery results now consistently record search mode and candidate budget, including incomplete-profile returns.\n
 
**Positive recovery-certificate adversarial replay (G-EP82):** hardens `verify_mixed_kronecker_recovery_certificate` against malformed nested transforms and forged audit records. Positive S/T transforms must be correctly sized square sequences with genuine integer entries (booleans and floats are rejected); malformed nested audit structures fail closed. Strict-equivalence and multi-block audits are recomputed and compared in full, including nested fields and matrices, rather than trusting stored success flags. Invalid caller matrices/fields still raise `ValueError`; the verifier explicitly rejects boolean/floating-point source entries before shared pair validation, while malformed certificate contents return `verified=false`. This is certificate-boundary hardening, not a new recovery algorithm or a uniqueness claim.


**G-EP83:** positive-certificate replay now uses type-exact recursive comparisons when matching the recomputed profile, canonical matrices, minimal-index metadata, regular dimension, and canonical block shapes. This prevents Python boolean/integer equality from allowing boolean-forged numerical fields to pass. The verifier reconstructs these values from the supplied pencil and recorded profile bounds; adversarial tests cover nested profile mutation, source-shape forgery, canonical matrix and block-shape boolean aliases, and container-type changes. This is deterministic replay hardening, not an independent classifier or uniqueness claim.


**G-EP84:** adds cross-field positive-certificate replay tests over F₂, F₃, F₅, and F₇ using basis-scrambled mixed pencils, plus rejection of forged field metadata and boolean transform entries. Distinct valid S/T witnesses produced by reciprocal nonzero scalar rescaling are accepted when their witness-dependent strict-equivalence and multi-block audit records are also regenerated; stale nested audits remain rejected. These are finite regression controls, not a universal recovery or uniqueness theorem.


**G-EP85:** expands positive recovery replay adversarial coverage: required metadata omission and type substitutions, boolean/integer aliases and container substitutions in nested strict-equivalence and multi-block audit records, now rejected through recursive type-exact audit comparison, and cross-field S/T transplantation across F₃/F₅/F₇, accepting a transplanted pair only when it satisfies the destination-field identities and rejecting a mutated pair after audit regeneration. Witness provenance is not required. These are deterministic certificate-integrity regressions for the selected fixture, not a universal recovery or uniqueness theorem.


**G-EP86:** tests tampering with canonical block order, block dimensions, canonical target entries, and nested multi-block audit matrices. A consistently reordered right/regular/left block decomposition remains valid under the standalone direct-sum witness verifier, while the recovery-certificate verifier rejects it because that certificate uses a fixed profile-derived canonical block order. This distinguishes algebraic direct-sum validity from canonical certificate serialization; the regression uses one 4×4 fixture over F₅.


**G-EP87:** standalone multi-block witness verification now rejects boolean and non-integral entries in source coefficients and transforms. Tests cover all six consistent permutations of a three-block mixed pencil, plus malformed, incomplete, dimension-inconsistent, and zero-by-zero block partitions. The API represents blocks as consecutive partitions, so overlapping intervals cannot be separately encoded; invalid totals and shapes are rejected.


**Multi-block witness adversarial verification (G-EP88):** adds regressions ensuring singular left or right transforms produce a failed verification audit rather than being confused with malformed caller data; modularly equivalent integer representatives yield identical normalized audit data; field validation rejects booleans, non-integers, small invalid values, and composites while F₂/F₃ positive controls pass; and malformed nested/ragged matrix inputs raise explicit `ValueError`. This hardens the supplied-witness verifier without changing its discovery scope or treating a failed witness as proof that no decomposition exists.


**Generated rectangular partition coverage (G-EP89):** deterministic generated-style fixtures exercise multi-block partitions containing zero-row and zero-column blocks (but no zero-by-zero blocks) over F₂, F₃, F₅, and F₇. Identity transforms verify valid block-diagonal pairs, while injected cross-block coefficients must fail the corresponding zero-block and overall verification checks. Invalid total partitions are also rejected. These are finite regression controls, not a universal proof.


**G-EP90 — rectangular multi-block basis invariance:** adds generated-style
regression coverage for an ordered partition containing zero-row and
zero-column blocks (never a zero-by-zero block), with positive total
dimensions. Independently invertible unitriangular left and right basis
changes scramble both coefficients over F₂, F₃, F₅, and F₇; the exact inverse
witness must recover and verify the original block-diagonal pair. This is
finite test coverage, not decomposition discovery, uniqueness, or a universal
recovery theorem.


**G-EP91 — adversarial rectangular basis-invariance witnesses:** extends the
G-EP90 generated rectangular fixture over F₂, F₃, F₅, and F₇. Tests inject
coupling into each representable directed off-diagonal block independently in
both Q and K, mutate both coefficients together, and alter left/right
transforms while keeping them invertible. These well-formed but false
witnesses must return failed audits. Singular square transforms also return
failed audits; malformed dimensions or non-integral entries instead raise
ValueError. This distinction is tested explicitly and does not imply that a
failed witness rules out another valid decomposition.


**G-EP92 — equivalent-representation stability:** verifies that modularly
equivalent integer representatives, independently chosen invertible row and
column scramblings, reciprocal nonzero scalar rescalings of the two witness
transforms, and simultaneous block-coordinate permutations preserve valid
multi-block audits. Controls run over F₂, F₃, F₅, and F₇. These are exact
finite regression tests; they do not establish uniqueness of a partition or
of its witness.


**G-EP93 — near-equivalence rejection:** tests one-entry source-coefficient mutations after a valid rectangular basis scrambling, one-entry perturbations of each supplied invertible transform, and block-shape permutation without the corresponding coordinate permutation. These well-formed near-equivalences must fail the algebraic audit, while malformed transform dimensions continue to raise ValueError. Controls run over F₂, F₃, F₅, and F₇; a failed supplied witness is not a no-decomposition theorem.


**G-EP94 — independent audit-record cross-checks:** test-only matrix multiplication, Gaussian rank, and block slicing independently reconstruct SQT/SKT and every ordered rectangular block. The tests compare all verifier diagnostic fields, including both transform ranks, invertibility flags, per-coefficient off-diagonal-zero flags, and the aggregate decision, for valid and deliberately false witnesses over F₂/F₃/F₅/F₇.


**G-EP95 — serialized audit round-trip and replay:** JSON round-trips valid and false multi-block audit records, then exactly compares the restored data with a fresh audit recomputed from source matrices and transforms. Forged aggregate flags, stale off-diagonal flags, boolean-for-integer rank substitutions, and missing block grids are rejected by type-exact replay comparison. The verifier itself consumes source matrices and transforms, not serialized audit records; this is a test of serialization integrity and replay discipline, not a new certificate-loading API.


**G-EP96 — Strict JSON snapshot boundary regressions:** test-side decoding rejects duplicate object keys and non-finite JSON constants. Restored records with unexpected schema versions, malformed nested block arrays, missing required fields, or boolean/floating-point substitutions in integer diagnostic positions fail recursive type-exact comparison with a fresh audit. Original malformed caller matrices continue to exercise the verifier's separate `ValueError` input boundary. No serialized-record ingestion API is introduced.


**G-EP97 — Deterministic serialized-record mutation sweep:** recursively enumerates every dictionary field and list slot in a valid JSON audit snapshot, mutates one location at a time, round-trips each mutation, and confirms exact type-aware comparison rejects every changed record. Coverage explicitly includes top-level metadata, both block grids, and nested verification fields. This is finite regression testing of snapshot integrity, not cryptographic authenticity or provenance.


**G-EP98 — v1 audit schema contract:** test-side structural validation checks exact required fields and types, positive source dimensions, rectangular block partition totals, transform/transformed-matrix dimensions, both nested block-grid dimensions, and verification diagnostic types/ranges. It deliberately accepts well-formed but mathematically false witness records, keeping schema validity distinct from algebraic verification. No production parser or schema migration is introduced.


**G-EP99 — Rectangular schema edge-case grid:** exercises the v1 structural contract across two-, three-, and four-block partitions, including legal zero-row and zero-column rectangular blocks. It verifies exact nested grid dimensions, accepts well-formed false witnesses as structurally valid without treating them as successful algebraic certificates, and rejects malformed nested grid dimensions. Finite deterministic regression coverage only.


**G-EP100 — Schema/algebra outcome cross-check:** pairs structural validation with four verifier outcomes: valid structure and valid witness; valid structure and false witness; malformed snapshots rejected independently of witness intent; and well-formed singular-transform records with a negative audit. This explicitly tests that schema validity is not conflated with invertibility or block-diagonal truth.

**G-EP101 — independent audit-record reconstruction:** adds test-local matrix multiplication, Gaussian rank, and rectangular block slicing to reconstruct transformed coefficients, both complete block grids, transform ranks, invertibility flags, off-diagonal-zero diagnostics, and the aggregate decision directly from source matrices and supplied transforms. It cross-checks positive, false, and singular witnesses, including zero-row/zero-column partition blocks, and detects schema-shaped mutations to transformed matrices, nested blocks, and diagnostics. This is finite regression evidence; it is not a production snapshot-ingestion API, formal proof, or provenance/authenticity mechanism.

**G-EP102 — seeded cross-field rectangular reconstruction:** extends the test-local audit checks over deterministic fixtures in F₂, F₃, F₅, and F₇. Each field uses a different rectangular partition, including zero-row/zero-column blocks, independently generated invertible left/right basis changes, and modularly equivalent source-entry representatives. Reconstructed transformed coefficients must recover the block-diagonal controls; normalized block grids and verification diagnostics must remain stable under adding multiples of the field characteristic. A shape-preserving snapshot mutation is also checked. These seeded finite tests are regression evidence, not universal proof or a production snapshot verifier.

**G-EP103 — three-layer audit pipeline:** adds a deterministic mutation matrix that checks structural schema validity, consistency with source matrices/transforms through test-local reconstruction, and the mathematical witness verdict as separate outcomes. It includes malformed nested grids, schema-valid forged transformed coefficients/blocks/diagnostics, a positive witness, and a structurally valid, reconstruction-consistent negative witness. This clarifies the trust boundary: schema validity does not imply record consistency, and record consistency does not imply mathematical success. Test-only finite regression coverage.

**G-EP104 — adversarial audit metadata:** tests schema-version, field-label, source-dimension, partition-order, and scope mutations. It distinguishes malformed metadata from well-typed but source-unbound metadata, and confirms that an alternative reciprocal scalar rescaling of the left/right transforms can remain a valid equivalent witness. These are test-side snapshot-integrity and algebraic regression checks, not cryptographic provenance.


- **G-EP105:** add cross-field rectangular coordinate-permutation regressions over F₂/F₃/F₅/F₇. Simultaneously permuting row and column coordinate intervals, the ordered block list, and the corresponding supplied transforms preserves the exact reordered block-diagonal pair, including zero-row and zero-column blocks. One-sided row or column coordinate permutations are rejected. These are deterministic finite regression tests, not a universal theorem, decomposition discovery method, or uniqueness claim.


**G-EP106 — composed equivalence transformations:** tests compositions of two successive, independent left and right source-basis changes, a consistent rectangular block-coordinate permutation, and reciprocal nonzero scalar rescaling. The composite witness must recover the exact reordered Q/K pair over F₂, F₃, F₅, and F₇, including zero-row and zero-column blocks. A mismatched final row transform is rejected. This is finite deterministic regression coverage, not a uniqueness theorem or decomposition-discovery result.


**G-EP107 — transformation factorization-order invariance:** tests two distinct ordered factorizations of identical composite left/right basis changes. Both paths are followed by the same rectangular block-coordinate permutation and reciprocal scalar rescaling, and must produce identical verified transformed matrices and block records over F₂/F₃/F₅/F₇. An omitted inverse factor is rejected. Deterministic finite regression coverage only; no uniqueness or decomposition-discovery claim.


**G-EP108 — seeded metamorphic rectangular witness families:** generates deterministic products of elementary invertible matrices for independent left/right basis scramblings, then checks exact recovery of randomly populated rectangular block-diagonal Q/K pairs over F₂/F₃/F₅/F₇. Three partition families include zero-row and zero-column blocks. A transported single-entry cross-block mutation must be rejected in every case. This is reproducible finite regression coverage, not a universal theorem or decomposition-discovery algorithm.


**G-EP109 — long composition and partition adversaries:** checks 17-step and 19-step deterministic products of elementary invertible transformations on the left and right over F₂/F₃/F₅/F₇, with reciprocal scalar witness rescaling and exact recovery of both coefficients. A second control changes the rectangular block partition while preserving total dimensions; the supplied transforms must reject that incorrect partition. Finite deterministic regression coverage only.


**G-EP110 — paired-pencil partition boundary and cancellation adversaries:** adds cross-field controls over F₂/F₃/F₅/F₇ for block-preserving transforms, Q-only and K-only cross-block mutations, and a paired mutation whose opposite off-diagonal entries cancel in Q+K while remaining nonzero in each coefficient separately. The verifier must reject the paired mutation, demonstrating that it checks both pencil coefficients independently rather than only their aggregate. Deterministic finite regression coverage; no decomposition-discovery, uniqueness, or universal-theorem claim. See G-EP110 in `research/the-fold-multi-block-direct-sum-witness.md`.


**G-EP111 — invertible pencil-parameter basis changes:** tests coefficient-space changes by invertible 2×2 matrices over F₂, F₃, F₅, and F₇, including coefficient swaps, shears, and mixed determinant-one changes. The same rectangular coordinate witness must verify the transformed pair and recover the expected mixed target coefficients; applying the inverse parameter change recovers the original ordered pair exactly. This finite regression checks direct-sum stability under an invertible change of basis in the pencil coefficient space. It does not cover singular coefficient mixing, decomposition discovery, uniqueness, or universal classification.


**G-EP112 — singular coefficient-space maps and information loss:** tests rank-deficient linear maps on the ordered pair (Q,K). Over F₂/F₃/F₅/F₇, the original pair is coupled through K, but a singular map can erase K or duplicate Q and make the collapsed pair pass the direct-sum verifier. A retained coupled combination remains rejected. This documents the crucial boundary: verifier success applies to the supplied transformed pair, not to an original pencil after information-losing singular mixing. See G-EP112 in `research/the-fold-multi-block-direct-sum-witness.md`.


**G-EP113 — exhaustive coefficient-map rank boundary:** enumerates all p⁴ 2×2 coefficient-space maps over F₂/F₃/F₅/F₇ and checks their rank census, output coefficient-span dimension, individual off-diagonal conditions, and verifier result on a fixed pencil with block-diagonal Q and coupled K. Exactly p² maps pass: the zero map and rank-one maps that erase K. No invertible map passes. Exhaustive for the tested fields and fixture, not a universal result for arbitrary pencils.


**G-EP114 — intersecting common block-diagonal constraints:** for a fixed left transform and two-block partition, exhaustively enumerates right transforms over F₂/F₃/F₅/F₇. The Q-only and K-only off-diagonal constraint spaces are checked separately and intersected; only the common intersection satisfies both coefficients. Singular members are retained by the linear equations, so invertibility is checked independently. Fixed-left 2×2 fixture only; not general decomposition discovery.


**G-EP115 — simultaneous linear constraint solving:** builds the homogeneous finite-field system for all off-diagonal entries of both coefficients in the unknown right transform. A test-local RREF/nullspace solver is cross-checked against brute force over F₂/F₃/F₅/F₇; invertibility is filtered separately, and every surviving candidate is replayed through the exact witness verifier. Fixed-left 2×2 fixture; not a general discovery API.


- **G-EP116:** generalizes test-local simultaneous right-transform equations to rectangular block partitions, including a 3×3 pencil with block shapes (1,2) and (2,1) under independent left/right scramblings. The known witness is checked against the computed nullspace; small 2×2 controls are exhaustively cross-checked against brute force, and adding coefficient constraints is verified not to increase nullspace dimension. Finite test coverage only; no production discovery API or general completeness claim.


- **G-EP117:** independently cross-checks test-local rectangular off-diagonal equations against direct matrix multiplication for arbitrary candidate right transforms. Seeded cases span rectangular matrices, independent left/right basis scramblings, zero-row/zero-column blocks, and F₂/F₃/F₅/F₇. The planted witnesses are replayed through the production verifier; this is finite test evidence, not a general solver or completeness claim.


- **G-EP118:** cross-checks simultaneous off-diagonal constraint rank using row reduction and an independently enumerated row span. Zero, duplicate, scalar-multiple, overlapping, and rank-increasing coefficient constraints are covered; exhaustive right-transform-vector enumeration confirms the nullity solution count over F₂/F₃/F₅. Fixed-left 2×2 finite controls only.


- **G-EP119:** extends test-side off-diagonal equation rank/nullity checks to rectangular sources, including a 2×3 pencil, zero-row/zero-column blocks, and an empty off-diagonal region. Elimination rank is cross-checked against explicit row-span enumeration; sampled equations are checked against direct matrix products, and small kernels are exhaustively counted over F₂/F₃. Finite regression coverage only.


- **G-EP120:** tests constraint-rank invariance under independent invertible block-diagonal row/column coordinate changes on rectangular systems, including empty row/column blocks. The induced map X′ = T⁻¹XT is checked by direct multiplication, and each off-diagonal block's zero status is preserved. A separate control shows that changing the partition can change rank; arbitrary block-mixing basis changes are not covered.


- **G-EP121:** extends constraint-rank invariance to full invertible row/column basis changes that mix blocks, provided the block decomposition is transported with the bases. The test builds the transported equation map using matrix-unit inputs and checks its rank against the original system over F₂/F₃/F₅. Explicit F₂/F₃ controls show that mixing the bases but retaining the old coordinate partition can change rank, because that is a different constraint family. Test-side finite covariance evidence only; the production API still accepts consecutive coordinate block shapes, not arbitrary subspace-basis metadata.


- **G-EP122:** extends transported-basis covariance to rectangular m×n coefficient matrices and n×n right-transform unknowns. Full row/column basis changes mix blocks, while the decomposition is transported through the inverse basis maps. Matrix-unit equation construction checks rank invariance over F₂/F₃/F₅, including a 3×4 partition with simultaneous zero-row and zero-column blocks; sampled candidates verify the pullback identity. A fixed-coordinate control confirms rank can change when the partition is not transported. Finite test-side evidence only; no generic mixed-basis production verifier is added.


**G-EP123 — transported kernel bijection and singular candidates:** exhaustively enumerates the full 2×2 right-transform matrix space for a rectangular 3×2 pencil over F₂ and F₃. The conjugation map induced by a full mixed column-basis change is checked to be a bijection on all matrices and to preserve the simultaneous off-diagonal constraint predicate after transporting the decomposition. Kernel cardinalities agree, including singular solutions; determinant filtering is kept separate, with the zero matrix explicitly retained in the linear kernel but excluded from invertible witnesses. This is finite test-side evidence, not a production mixed-basis verifier or general discovery algorithm.


- **G-EP124:** increases the right-transform space to 3×3 (nine variables) for a rectangular 4×3 coefficient pair. Independently constructs the simultaneous constraint matrices from matrix-unit inputs, compares their ranks and nullities after full row/column basis transport over F₂/F₃/F₅, and verifies both directions of the induced candidate-coordinate map on all matrix units plus sampled general candidates. Finite test-side rank/nullity and covariance evidence only; no production mixed-basis API change.


- **G-EP125:** independently cross-checks G-EP124's 3×3 transported constraint rank with complete row-span enumeration over F₂/F₃ (and RREF covariance over F₅). Shape-preserving coefficient mutation changes the reconstructed constraint map while retaining dimensions, distinguishing a mathematically false transport from malformed input; a mutated inverse-map entry breaks the inverse identity, with a separate malformed-dimension control. Finite test-side evidence only.


- **G-EP126:** transports complete nullspace bases for the 3×3 right-transform constraint system. For zero and scalar-dependent rectangular coefficient pairs over F₂/F₃/F₅, independently computed nullspaces are mapped by X′ = V⁻¹XV and checked in both directions by equation substitution and span-dimension comparisons. Includes rank-zero and nonzero rank-deficient cases; invertibility remains separate from linear-kernel membership. Finite test-side evidence only.


- **G-EP127:** composes two independently invertible row/column basis changes on the rectangular 4×3 constraint system over F₂/F₃/F₅. Verifies factor order, composed source recovery, nullspace transport and inverse recovery; omission and reversal controls remain well-shaped but produce incorrect coefficient transports. Finite test-side evidence only.


- **G-EP128:** four-stage rectangular basis transport over F₂/F₃/F₅, including identity stages and adjacent inverse-factor cancellation. Checks composed matrix identities, kernel-basis transport and recovery, plus shape-valid wrong-inverse-order controls. Finite test-side evidence only.


- **G-EP129:** transports rectangular block projectors through a four-stage row/column basis composition over F₂/F₃/F₅. Sequential and directly composed transported partitions agree, including zero-row and zero-column blocks; each projected coefficient block is checked against pullback to the original partition. Finite test-side evidence only.


**G-EP130 — projector algebra under composed rectangular transport:** verifies idempotence, pairwise orthogonality, and completeness of transported row/column block projectors after four composed basis stages over F₂/F₃/F₅. Zero-row/zero-column blocks remain explicit zero projectors. Independent shape-valid mutations isolate failures of each projector axiom, and a wrong transport direction is rejected. Test-side finite regression evidence only; no production projector-certificate API is added.


**G-EP131 — projector rank/nullity invariance:** independently computes finite-field ranks of transported row/column projectors and verifies rank and kernel dimension are preserved and match the rectangular block sizes, including empty blocks. A shape-valid idempotent with one missing image direction is detected. F₂/F₃/F₅ test-side coverage only; no production rank-certificate API is added.
\n\n**G-EP132 — rectangular projected coefficient-block transport:** verifies the covariance identity Pᵢ′ A′ Qⱼ′ = U(Pᵢ A Qⱼ)V for both coefficient matrices under four-stage composed row/column basis changes over F₂, F₃, and F₅. Every ordered block pair is checked, including off-diagonal zeros and explicit empty 1×0/0×1 diagonal summands; projected-block ranks are preserved. A shape-valid wrong column-conjugation direction is rejected. Finite test-side regression evidence only; no production projector API is added.\n

**G-EP133 — diagonal projected-block reconstruction and coupling detection:** sums all transported diagonal projected blocks and verifies exact reconstruction of each coefficient matrix, with the off-diagonal sum zero, over F₂/F₃/F₅. A one-entry, shape-valid cross-block coupling is then injected in source coordinates; the diagonal sum no longer reconstructs the full transported matrix, while diagonal plus off-diagonal sums still do. Test-side finite regression evidence only; no production projector-certificate API is added.


- **G-EP134:** recovers each indexed diagonal projected coefficient block by pulling transported blocks back through the composed row/column basis maps. Empty row/column summands remain explicit zero blocks. A second equal-dimension fixture swaps two transported projector indices: the mutation remains shape-valid but assigns the wrong subspaces and is detected. Test-side finite regression evidence over F₂/F₃/F₅; no production projector-certificate API is added.


**G-EP135 — transported projector image and kernel subspaces:** independently compares the actual image and kernel spans of each transported row and column projector with the subspaces induced by the corresponding basis map. The checks use finite-field elimination, preserve zero-dimensional and full-dimensional cases, and verify expected image/kernel dimensions over F₂/F₃/F₅. A dimension-preserving projector mutation that moves a proper nonzero image to a different coordinate subspace is rejected. Finite test-side regression evidence only; no production arbitrary-subspace projector API is added.


- **G-EP136:** constructs alternative transported row/column projector families by conjugating with coordinate permutations that move the represented subspaces. Each alternative family still satisfies idempotence, pairwise orthogonality, completeness, and the same per-index ranks over F₂/F₃/F₅. Direct comparison with the intended transported projectors detects the changed ordered subspaces. This demonstrates that projector axioms and ranks alone do not uniquely identify the supplied ordered decomposition; test-side finite evidence only.


- **G-EP137:** binds transported projector families to both rectangular coefficient matrices. For the intended row/column projectors, summing all diagonal projected blocks reconstructs each transformed coefficient exactly. Alternative projector resolutions from G-EP136 retain idempotence, orthogonality, completeness, and rank data, but produce nonzero off-diagonal projected blocks and fail diagonal-only reconstruction for both coefficients. The full diagonal-plus-off-diagonal sum remains an exact reconstruction control. Finite test-side evidence over F₂/F₃/F₅; no production arbitrary-subspace certificate API is added.


- **G-EP138:** checks projector-bound diagonal reconstruction under invertible coefficient-space mixing of the pencil pair, in addition to independent row/column basis changes. The mixing matrix has determinant one over F₂/F₃/F₅; its inverse recovers the original ordered coefficient pair exactly. The intended projectors reconstruct both mixed coefficients from diagonal projected blocks, while the alternative resolution still fails diagonal-only reconstruction and the full projected-block sum remains exact. Finite test-side covariance evidence only.

- **G-EP139:** composes two successive invertible coefficient-space basis changes and compares sequential mixing with the directly composed map over F₂/F₃/F₅. The same transported projector families reconstruct both coefficients at each stage; the composed map is inverted to recover the original ordered pair, including reverse-order inverse application. Finite test-side composition and covariance evidence only.
G-EP140: distinguishes valid invertible coefficient-space shears that change only one output coefficient from unrelated matrix-space mutations applied to only one coefficient. The same transported rectangular projectors reconstruct both coefficients before and after the shear over F₂/F₃/F₅; inverse shear recovers the original pair. A shape-preserving cross-block mutation to only one coefficient breaks diagonal-only reconstruction while the untouched coefficient remains reconstructible. Finite test-side regression evidence only.
\n- **G-EP141:** exhaustively groups nonzero rank-one 2×2 coefficient maps over F₂/F₃/F₅ by their surviving projective pencil direction. The output pair spans one surviving linear combination; all maps with the same direction yield the same direct-sum verdict despite differing kernel/preimage data. Only the pure-Q direction removes the fixture's K-coupling. Finite test-side evidence only; singular maps do not certify equivalence of the original pencil.

- **G-EP142:** exhaustively contrasts rank-zero, rank-one, and invertible 2×2 coefficient maps over F₂/F₃/F₅. A rank-zero map collapses both output matrices to zero, which the direct-sum verifier correctly accepts as a direct sum of the supplied zero pair; that success is not evidence about the original pencil. Rank-one maps retain one projective pencil direction, while invertible maps retain the full two-dimensional coefficient information. The production verifier reports only the supplied-pair verdict and does not expose coefficient-map provenance, so the rank/image distinction remains an explicit test-side audit rather than inferred verifier metadata.


- **G-EP143:** exhaustively tests every invertible 2×2 coefficient-space change over F₂/F₃/F₅ on two contrasting three-block fixtures: one where both coefficients are block diagonal and one where both have cross-block coupling on independent supports. The supplied identity-coordinate direct-sum verdict is invariant under every such change; inverse coefficient maps recover the original ordered pair exactly. This establishes finite fixture-specific covariance evidence, not a universal decomposition theorem or a production coefficient-map API.

- **G-EP144:** exhaustively tests every invertible 2×2 coefficient-space map over F₂/F₃/F₅ on a rectangular 3×4 block partition containing explicit zero-column and zero-row summands. Under independent nontrivial row/column basis changes, every ordered projected block of both mixed coefficients is checked against the corresponding linear combination of the original projected blocks, including exact empty-block shapes. All off-diagonal projected blocks remain zero, diagonal blocks reconstruct each full coefficient, and inverse coefficient maps recover both the ordered matrices and all indexed projected blocks. Finite test-side covariance evidence only; no production projector API or universal theorem is added.

- **G-EP145:** checks all 24 reorderings of a four-block rectangular partition containing zero-column and zero-row summands over F₂/F₃/F₅. Row and column coordinate permutations are induced independently from the same block ordering. Every reordered witness is replayed; all off-diagonal projected blocks vanish, diagonal blocks reconstruct each coefficient, and inverse coordinate/block permutations recover the original matrices and every indexed projected block. Finite test-side permutation covariance evidence only; no canonical-order or uniqueness claim is added.


**Repeated equal-sized summands and relabeling controls (G-EP146):** adds a fixture with three equal 1×1 summands carrying distinct ordered coefficient data, plus explicit zero-column and zero-row summands. All six permutations of the repeated blocks are tested over F₂/F₃/F₅. Simultaneously transporting row and column coordinate intervals is accepted and permutes every indexed projected block as expected; inverse transport recovers both coefficients. A shape-preserving one-sided row-subspace reassignment, with column coordinates and shape metadata held fixed, creates cross-block entries in both coefficients and is rejected. This distinguishes consistent relabeling from an incorrect subspace assignment without claiming that equal shapes identify a unique decomposition. Finite test-side regression evidence only.


**G-EP147 — equal dimensions versus internal pencil equivalence:** four equal 1×1 summands carry two proportional coefficient pairs, one pair sharing only its first coefficient with another, and a fourth distinct projective pair. Over F₂/F₃/F₅, all 24 equal-shape relabelings preserve the production direct-sum verdict while moving the indexed internal signatures with their blocks. A test-local determinant criterion checks the 1×1 constant strict-equivalence relation (common nonzero scalar on both coefficients). A control changes only one diagonal K entry: the decomposition remains valid, but the internal pencil signature changes. Finite fixture-specific evidence; it does not classify larger blocks or add a production equivalence API.


**G-EP148 — 2×2 internal pencil equivalence and joint-rank obstructions:** extends internal-block testing beyond 1×1 pencils. Over F₂/F₃/F₅, a nontrivial invertible left/right transformation produces a positive 2×2 strict-equivalence witness, checked by the production auditor against both exact coefficient identities. A negative control has matching individual Q- and K-ranks but different rank profiles for Q+λK; at λ=−1 this proves that no common strict-equivalence transforms can relate the two pairs. Finite fixture-specific evidence only; it is not a complete 2×2 classification or a general witness-discovery algorithm. See `research/the-fold-internal-pencil-equivalence-2x2.md`.


- **G-EP149:** adds a test-local homogeneous determinant-polynomial audit for 2×2 pencils. A positive nontrivial strict-equivalence witness confirms the expected scalar covariance of \(\det(xQ+yK)\). A negative control compares pairs with matching individual coefficient ranks but nonproportional determinant polynomials, ruling out every common constant strict-equivalence witness. Finite fixture-specific evidence; the determinant polynomial is not claimed to be a complete invariant. See `research/the-fold-determinant-polynomial-invariant.md`.


- **G-EP150:** demonstrates that the homogeneous determinant polynomial from G-EP149 is not a complete strict-equivalence invariant. Over F₂/F₃/F₅, a scalar pencil and a nontrivial Jordan pencil have exactly the same \(\det(xQ+yK)=(x+y)^2\), but with Q=I any strict equivalence would force similarity of K. The rank of K−I differs, proving non-equivalence. Finite exact counterexample family; no complete classification is claimed. See `research/the-fold-determinant-polynomial-limit.md`.


- **G-EP151:** distinguishes characteristic-polynomial agreement from 2×2 operator similarity over F₂/F₃/F₅. The identity and a size-two Jordan block share \((t-1)^2\) but have different invariant factors and cyclic-vector behavior; the existing rational-canonical routine decides they are not similar. A nontrivial conjugation of a diagonal operator supplies a positive intertwiner checked by the production witness API. Finite regression fixtures; no new similarity algorithm is introduced. See `research/the-fold-2x2-cyclic-similarity.md`.


- **G-EP152:** exhaustively audits all 2×2 matrices over F₂ and F₃. For each matrix, a test-local characteristic-polynomial calculation and complete vector enumeration cross-check the production rational-canonical profile's cyclicity signal. Every invariant-factor profile fibre is then compared exactly with the conjugacy orbit generated by all invertible 2×2 basis changes. Exhaustive only for these two fields and dimension two; no new production similarity algorithm. See `research/the-fold-exhaustive-2x2-similarity.md`.


**G-EP153 — exhaustive 3×3 similarity-orbit audit over F₂:** exhaustively checks all 512 matrices, independently computes each characteristic polynomial, verifies invariant-factor products and cyclic-vector criteria, and compares every invariant-factor fibre with the complete conjugacy orbit under all 168 invertible basis changes. The finite exhaustive claim is limited to dimension three over F₂; no production similarity algorithm is added. See `research/the-fold-exhaustive-3x3-similarity.md`.


**G-EP154 — exhaustive 3×3 similarity-orbit audit over F₃:** exhaustively checks all 19,683 matrices, independently validates characteristic polynomials and invariant-factor products, checks cyclic-vector criteria across all 27 vectors, and compares every invariant-factor fibre with conjugacy under all 11,232 invertible basis changes. The finite exhaustive claim is limited to dimension three over F₃. See `research/the-fold-exhaustive-3x3-f3-similarity.md`.


**G-EP155 — cross-field comparison of 3×3 similarity profiles:** enumerates every 3×3 matrix over both F₂ and F₃ and compares invariant-factor degree patterns separately from coefficient tuples. The observed degree-shape set is shared, while coefficient representatives remain field-valued data (with coefficient 2 appearing over F₃ but not F₂). This comparison does not identify polynomials across fields or claim that the fields have the same irreducible polynomials; the exhaustive scope remains dimension three over these two fields.


- **G-EP156:** exhausts all monic cubic polynomials over F₂ and F₃ (each is realized as the characteristic polynomial of its companion matrix), factors them with the exact finite-field factorizer, and checks exact reconstruction. F₃ has one additional degree/multiplicity pattern: three distinct linear factors, impossible over F₂ because it has only two linear monic irreducibles. The irreducible polynomial inventories also differ by field; expected counts in degrees one through three are checked independently. No polynomial coefficients are identified across fields.


- **G-EP157:** exhausts all monic quartics over F₂ and F₃, checks exact factor reconstruction, and validates irreducible counts in degrees one through four. It confirms a quartic factor pattern containing all three distinct linear factors with one repeated over F₃, which cannot occur over F₂. This is an exhaustive degree-four comparison over these two fields.


- **G-EP158:** compares all monic quartics over F₂, F₃, and F₅. Exact factor reconstruction and irreducible inventory counts through degree four are checked. The catalog grows with field size: three distinct linear factors with one repeated occur from F₃ onward; four distinct linear factors occur over F₅; and two distinct irreducible quadratics occur from F₃ onward. These are exhaustive degree-four results for the three stated fields.


- **G-EP159:** exhausts monic quartics over F₂, F₃, F₅, and F₇. It checks exact factor reconstruction and irreducible inventory counts through degree four. The degree/multiplicity pattern catalogue strictly grows from F₂ to F₃ and F₃ to F₅, then is identical over F₅ and F₇. The irreducible polynomial inventories still differ between F₅ and F₇, so stabilization applies to quartic factor shapes, not polynomial coefficients or factor identities.


- **G-EP160:** exhausts monic quintics over F₂, F₃, F₅, and F₇. It verifies exact reconstruction and irreducible inventory counts through degree five. The degree/multiplicity pattern catalogue grows from F₂ to F₃ and F₃ to F₅, then agrees over F₅ and F₇ despite different irreducible polynomial inventories. This supports a degree-five threshold at field size five for these tested fields; it is not a theorem for arbitrary polynomial degrees.


- **G-EP161:** exhausts all monic sextics over F₂, F₃, and F₇ (64, 729, and 117,649 polynomials). It checks exact factor reconstruction and irreducible inventory counts through degree six. The complete 34-pattern degree/multiplicity catalogue occurs over F₇; the smaller tested fields have strict subsets. Six distinct linear factors impose the limiting field-size requirement, so seven is the first prime-field size at which the complete sextic shape catalogue can occur.

- **G-EP162:** exhausts all 15,625 monic sextics over F₅, independently confirming exact factor reconstruction and irreducible inventory counts through degree six. The six-distinct-linear-factor shape is absent, while representative five-linear-factor and four-linear-plus-quadratic shapes occur. This fills the F₅ comparison point between G-EP161's F₃ and F₇ experiments.

- **G-EP163:** tests the general polynomial factor API's scalar-unit convention, coefficient reduction modulo the field, constant-polynomial behavior, zero-polynomial rejection, composite-modulus rejection, and characteristic-three multiplicity — (x^3+1=(x+1)^3) over F₃.

- **G-EP164:** exhaustively cross-checks `is_irreducible_polynomial` against the factorizer's exact one-factor criterion for every monic polynomial of degrees 1–4 over F₂, F₃, and F₅ (930 inputs).

- **G-EP165:** extends the exhaustive irreducibility-predicate/factorizer cross-check to all 3,400 monic quintics over F₂, F₃, and F₅.

- **G-EP166:** extends the irreducibility-predicate/factorizer comparison to all 793 monic sextics over F₂ and F₃, checking exact agreement on degree-six inputs.

- **G-EP167:** extends the exhaustive irreducibility-predicate/factorizer comparison to all 2,315 monic degree-seven polynomials over F₂ and F₃.

- **G-EP168:** extends the exhaustive irreducibility-predicate/factorizer comparison through degree eight over F₂ and F₃ (6,817 monic polynomials).

- **G-EP169:** exhaustively cross-checks the irreducibility predicate against the factorizer for all 20,195 monic degree-nine polynomials over F₂ and F₃. This is a finite-domain consistency regression, not a proof for arbitrary degrees or fields.

- **G-EP170:** exhaustively cross-checks the irreducibility predicate against the factorizer for all 60,073 monic degree-ten polynomials over F₂ and F₃. This is finite-domain consistency coverage, not a general theorem.


- **G-EP171:** extracts degree-specific irreducibility-predicate/factorizer comparisons into a parameterized audit over arbitrary prime fields and positive degrees. It exhausts domains within a configurable case budget and otherwise performs reproducible sampling, reporting completeness explicitly (including the edge case where the sample covers the entire domain). The research note separately analyzes the scaling weight n/n^n and its relationship to the actual p^n workload. Finite exhaustive and sampled agreement are computational evidence, not an arbitrary-degree proof.


- **G-EP172:** works outward from the full monic-polynomial workload \(p^n\) and inward to the exact irreducible count. It derives the adjacent-degree ratio and turning threshold for the imposed weight \(n(p/n)^n\), then contrasts it with the exact Möbius formula \(I_p(n)=\frac1n\sum_{d\mid n}\mu(d)p^{n/d}\) and the natural normalized irreducible density \(nI_p(n)/p^n\to1\) for fixed \(p\). It explicitly separates workload weighting from irreducible-density normalization and distinguishes exact counts from sampled statistics. See `research/the-fold-outward-inward-scaling.md`.


- **G-EP173:** upgrades the parameterized irreducibility audit with an independent exact Möbius-formula count of monic irreducibles. It reports observed/theoretical densities, degree-normalized densities, the expected irreducible count in the checked subset, and an exact count-match flag only when the full domain has been covered. The audit schema advances to v2; tests cover exact count fixtures, a prime/degree grid, exhaustive comparison, and sampled-mode semantics. See research/the-fold-outward-inward-scaling.md.


**Uniform irreducible-density convergence and factorization corrections (G-EP174–G-EP175):** `tools/polynomial_irreducibility_audit.py` now reports exact normalized-density errors, proves a uniform-in-prime-field convergence bound, and resolves the leading correction from the prime factorization of the degree. Prime-power degrees have exactly one nonzero Möbius correction; for degrees with at least two distinct prime factors, the second-smallest prime factor bounds the remainder after the leading term. See `research/the-fold-outward-inward-scaling.md` and `tests/test_polynomial_irreducibility_audit.py`.


**Coprime-degree composition defect (G-EP176):** adds an exact audit comparing \(R_p(ab)\) with \(R_p(a)R_p(b)\) for coprime degrees. A concrete counterexample over F₂ at degrees 2 and 3 gives defect 15/32; degree one remains the identity case. The research note explains why the Möbius divisor indexing factors but its exponent weights do not. See `research/the-fold-outward-inward-scaling.md` and the irreducibility-audit tests.


**Coprime-degree defect sign survey (G-EP177):** adds an exact-rational bounded survey of Delta_p(a,b)=R_p(ab)-R_p(a)R_p(b) over all unordered coprime degree pairs in a requested range. An exploratory sweep found positive defects for 2,944 pairs per field over p=2,3,5,7,11, with degrees through 100; this remains finite evidence, not a universal positivity theorem. The executable audit reports exact sign counts and any counterexample witness. See research/the-fold-outward-inward-scaling.md.


**Bad-proportion ordering reduction (G-EP178):** records the sufficient condition E_p(ab)<min(E_p(a),E_p(b)) for positive coprime-degree composition defect, and adds an exact-rational finite-grid audit with counterexample witnesses. The condition held throughout the explored p=2,3,5,7,11 grid through degree 100, but remains unproved universally. See `research/the-fold-outward-inward-scaling.md`.


**G-EP179 — Coprime bad-proportion ratio bound audit:** adds an exact-rational finite-grid audit for the conjecture that (E_p(ab)/\min(E_p(a),E_p(b))\le(p^2+p-1)/p^3) for coprime degrees greater than one. The test grid covers 102 pairs over p=2,3,5 through degree 12 and checks that the maximum is attained at (2,3), with value 5/8 over F₂. This is finite evidence only; the universal bound remains unproved. See `research/the-fold-outward-inward-scaling.md`.


**G-EP180 — Analytic subcase of the coprime ratio conjecture:** proves the proposed bound (Q_p(a,b)\le(p^2+p-1)/p^3) for all coprime pairs with smaller degree 2. Equality occurs at (2,3); the inequality is strict for (2,b) with odd b≥5. The proof uses the maximal-proper-subfield union bound and a one-subfield lower bound. Pairs with both degrees at least 3 remain open. See `research/the-fold-outward-inward-scaling.md`.


- **G-EP181:** completes the G-EP179 sharp ratio theorem for every coprime pair (a,b>1). G-EP180 handles smaller degree 2; for (3\le a<b), a lower bound for each denominator term and the maximal-subfield union bound give (Q_p(a,b)\le\omega(ab)p^{-b/2}). Small (b=4,5,6,7) are checked explicitly, and for (b\ge8), (\omega(ab)<2\log_2b\le2^{b/2-1}\le p^{b/2-1}), yielding the strict bound (Q_p(a,b)\le p^{-1}<(p^2+p-1)/p^3). Equality in the full theorem occurs only at (2,3). Therefore (E_p(ab)<\min(E_p(a),E_p(b))) and the coprime-degree defect is always positive. See `research/the-fold-outward-inward-scaling.md`.


- **G-EP182:** proves a uniform additive asymptotic law for the coprime-degree defect. As the larger degree B grows, Q_p(a,b)=E_p(ab)/min(E_p(a),E_p(b)) tends to zero uniformly in prime p. For a≥3 it is bounded by 2 log₂(B)·2^(−B/2); for a=2,b≥5, by 2^(−B/3)+(log₃ B)·2^(−B/2). Consequently Δ_p(a,b)/(E_p(a)+E_p(b)) tends to 1, including when the smaller degree is fixed. See research/the-fold-outward-inward-scaling.md.


- **G-EP183:** identifies the leading exponential scale of the coprime-degree defect from the smallest prime factors. For every n>1, p^(−A(n)) ≤ Eₚ(n) ≤ ω(n)p^(−A(n)), where A(n)=n(1−1/q(n)) and q(n) is the smallest prime divisor. Combining this with G-EP182 yields, uniformly in prime p and for sufficiently large B=max(a,b), a two-sided bound for Δₚ(a,b) and the logarithmic estimate −logₚ Δₚ(a,b)=min(A(a),A(b))+O(log log B). The controlling degree need not be the smaller degree. See research/the-fold-outward-inward-scaling.md.


- **G-EP184–187:** expands each subfield error into its exact finite squarefree-divisor spectrum; derives the complete finite spectrum for the coprime defect; proves the fixed-degree, large-field law \(\Delta_p(a,b)\sim C(a,b)p^{-A}\), with coefficient 2 precisely when the two input exponents resonate; and specifies exact coefficient collection for the next nonzero scale. It distinguishes the fixed-degree \(p\to\infty\) limit from the uniform large-degree limit of G-EP182–183. See research/the-fold-outward-inward-scaling.md.


- **G-EP188–190:** adds an exact integer-coefficient defect-spectrum auditor and rational evaluator; extends the Möbius density and defect results from prime fields to all finite fields of prime-power order; and constructs the exact multi-factor composition-excess spectrum, including its sign-resonance criterion. The exact spectra for (2,3) and resonant (3,4) are regression fixtures. See the research note.


- **Prime-power field support:** the exact irreducible-count and normalized-density APIs now accept every finite-field order \(Q\), provided \(Q\) is a prime power. The original prime-only API remains available for backwards compatibility.


- **G-EP190 correction:** the multi-factor composition excess \(E_Q(\prod n_i)-\prod E_Q(n_i)\) is not sign-definite; (2,3) is positive after leading-term cancellation, while (3,4) is negative. The exact spectrum auditor now handles arbitrary pairwise-coprime degree lists and reports the eventual sign.


- **G-EP193:** generalizes the exact normalized-density convergence audit and its field-independent envelope from prime fields to every prime-power field order. Regression coverage spans \(Q=4,8,9,16,25\) and degrees 1–24.
