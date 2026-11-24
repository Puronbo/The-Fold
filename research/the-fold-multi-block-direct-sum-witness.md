# G-EP58: Exact multi-block direct-sum witness verification

G-EP57 verified a supplied two-block rectangular direct-sum witness. G-EP58
extends the same certificate boundary to an ordered list of two or more
rectangular diagonal blocks.

For Q,K in F_p^(m x n), supplied S in GL_m(F_p), T in GL_n(F_p), and block
shapes (r_i,c_i), the verifier requires sum(r_i)=m and sum(c_i)=n. It computes
SQT and SKT, partitions both using cumulative row and column cuts, and checks
that every off-diagonal block vanishes in both coefficients. The diagonal
blocks may be rectangular.

## Scope and limitations

- This verifies supplied transforms and block shapes; it does not discover them.
- It does not prove uniqueness, indecomposability, or regularity of any block.
- It does not replace G-EP49/50's structured or exhaustive witness discovery.
- A failed check invalidates the supplied witness, not every possible split.

Tests cover a scrambled three-block rectangular witness, coupling in both
coefficients, singular transforms, composite moduli, and invalid partitions.


## G-EP59 integration

Successful results from `recover_mixed_kronecker_pencil` now include an ordered `canonical_block_shapes` list and `multi_block_direct_sum_audit`. The order matches canonical target assembly: right singular blocks, left singular blocks, then the regular canonical blocks. The multi-block verifier independently checks the recovered constant transforms against every cross-block cut in both coefficient matrices. The existing whole-target strict-equivalence audit remains in place, so callers receive both an overall equality certificate and a block-structure certificate. This adds no new search capability and leaves incomplete-profile, structured-budget, and exhaustive-search semantics unchanged.


## G-EP90: Rectangular multi-block basis-invariance controls

The multi-block verifier is now exercised on a generated-style partition that
contains both a zero-row block and a zero-column block while keeping positive
total row and column dimensions. Over each of F₂, F₃, F₅, and F₇, independent
invertible unitriangular left and right basis changes scramble both pencil
coefficients. The supplied inverse basis changes recover the exact block
diagonal pair, including its empty-width/empty-height diagonal pieces, and the
verifier must accept the witness with the original ordered block shapes.

This is finite regression coverage for the stated rectangular edge case and
constant strict-equivalence convention. It does not imply decomposition
discovery, uniqueness, or a universal invariance theorem beyond the algebraic
identities checked by the verifier.


## G-EP91: Adversarial basis-invariance witness checks

The generated rectangular basis-scrambled fixture from G-EP90 is now tested
against individual off-diagonal mutations. Each representable directed
off-diagonal block is injected separately into Q and K over F₂, F₃, F₅, and
F₇; additional cases mutate both coefficients at once. The audit must identify
which coefficient contains coupling and reject the combined witness.

The tests also perturb the supplied left and right transforms while keeping
them invertible, and separately supply singular square transforms. These are
well-formed but mathematically false witnesses and must produce a negative
audit rather than a caller-input exception. By contrast, ragged or
dimension-incompatible transforms and boolean/floating-point entries are
malformed inputs and must raise ValueError. A failed witness invalidates only
that supplied witness; it does not prove that no alternative decomposition
exists. The cases are finite regression coverage, not a universal theorem.


## G-EP92: Stability under equivalent representations

Regression controls now check equivalent presentations of the same
multi-block direct sum over F₂, F₃, F₅, and F₇. Adding integer multiples of
the modulus to source entries leaves the normalized transformed matrices
unchanged. Independently selected invertible left/right basis scramblings
remain accepted, as do reciprocal nonzero scalar rescalings
(S -> cS, T -> c⁻¹T), which preserve both transformed coefficients exactly.
A simultaneous permutation of the row and column coordinate intervals and
their ordered rectangular block shapes also remains a valid direct-sum
witness.

These tests establish representation stability for the finite fixtures only.
They do not establish uniqueness of a block partition or witness, nor do they
turn failure of one supplied witness into a no-decomposition result.


## G-EP93: Adversarial near-equivalence rejection

Over F₂, F₃, F₅, and F₇, the generated rectangular basis-scrambled witness is now subjected to three inconsistent changes: a single source coefficient is altered after scrambling; one entry of the supplied left or right transform is perturbed while preserving invertibility; and only the ordered block-shape list is permuted, without the corresponding row/column coordinate permutation. These correctly shaped but inconsistent witnesses must fail the direct-sum audit.

A dimension-incompatible transform remains a malformed caller input and raises ValueError, distinct from a validly shaped but false witness. This complements G-EP92's acceptance of simultaneous, equivalent block-coordinate permutations. The finite tests do not imply that failure of one witness excludes another decomposition.


## G-EP94: Independent audit-record cross-checks

A test-only reference calculation independently computes SQT and SKT, slices every ordered rectangular block, and uses a separately implemented Gaussian elimination routine for transform ranks. For valid witnesses and two false-witness controls (a source coefficient mutation and an invertible transform perturbation), it compares the verifier's transformed matrices, complete Q/K block grids, both ranks, both invertibility flags, both off-diagonal-zero flags, and aggregate decision against the reference calculation over F₂, F₃, F₅, and F₇.

The independent routines are test-local and do not call the verifier's private multiplication, split, or rank helpers. This provides finite regression evidence that diagnostics match the algebraic data; it is not a formal proof of the implementation or a decomposition discovery result.


## G-EP95: Serialized audit round-trip and replay

Tests JSON serialization/deserialization of both valid and false audit records over F₂, F₃, F₅, and F₇. The restored structure is compared recursively with exact Python types, then compared against a fresh verifier result recomputed from the original source matrices, field, transforms, and partition. Mutations to the aggregate success flag, off-diagonal-zero flag, transform-rank type (including bool-for-int), or required block grid are rejected by this exact replay comparison.

The verifier API accepts source inputs and transforms, not a serialized audit record. Therefore this milestone establishes regression coverage for JSON round-trip stability and an explicit test-side replay discipline; it does not claim to introduce a serialized-certificate ingestion or verification API.


## G-EP96: Strict JSON snapshot boundary regressions

A test-side strict JSON decoder rejects duplicate object keys (which ordinary decoding can silently collapse) and non-finite constants such as NaN and infinities. Adversarial snapshots then exercise unexpected schema versions, malformed nested block arrays, missing required fields, and boolean/floating-point substitutions in integer diagnostic positions. Each decoded mutation fails recursive type-exact comparison with a fresh audit computed from original caller inputs.

The tests separately retain the caller-input boundary: malformed source matrices raise `ValueError` in the verifier. This milestone does not add a production deserializer or serialized-certificate API; malformed snapshot handling is asserted by test-side decoding and replay comparison.


## G-EP97: Deterministic serialized-record mutation sweep

A deterministic recursive traversal enumerates every dictionary field and list slot in a valid multi-block audit snapshot. Each location is replaced independently, serialized and deserialized, and checked against the baseline using recursive type-exact equality. The test asserts that every single-location mutation is detected, and explicitly checks coverage of top-level verification metadata, both coefficient block grids, and nested aggregate verification fields.

This is finite regression coverage for the tested record shape. It does not establish cryptographic authenticity, tamper resistance against a party able to replace both record and expected baseline, or provenance of the original inputs.


## G-EP98: Explicit v1 audit schema contract

The test suite now defines a test-side structural validator for the v1 audit record. It checks the exact top-level and verification-field sets; primitive types (including exclusion of booleans from integer slots); positive source dimensions; valid ordered rectangular block shapes and total partition dimensions; left/right transform and transformed-coefficient dimensions; both square block-grid layouts and each rectangular block's expected dimensions; rank ranges; and the scope field.

Crucially, structural validity is separate from algebraic truth. A well-formed record produced from a mathematically false supplied witness must satisfy the schema validator while its direct_sum_verified diagnostic remains false. Adversarial tests cover wrong schema versions, malformed dimensions and grids, invalid primitive types, and unexpected fields.

This is a test-side v1 contract, not a production deserializer, schema migration mechanism, or cryptographic authenticity layer.


## G-EP99: Rectangular schema edge-case grid

The v1 schema contract is exercised over deterministic two-, three-, and four-block fixtures, including partitions containing zero-row and zero-column blocks while forbidding 0×0 blocks. The tests check source-dimension totals, transform dimensions, and every nested block's exact row/column dimensions. They also mutate grid row counts, grid widths, and nested block dimensions to ensure malformed structures are rejected.

A well-formed but mathematically false witness remains structurally valid and retains a false algebraic diagnostic. This preserves the separation between record shape and witness truth. The fixtures are finite regression cases, not a universal schema proof.


## G-EP100: Schema and algebraic outcome cross-check

A deterministic cross-check exercises four distinct cases against the v1 structural contract and the algebraic verifier:

1. A structurally valid record with invertible transforms and both transformed coefficients block diagonal is accepted by both layers.
2. A structurally valid record with an invertible shear that introduces cross-block entries passes schema validation but fails the algebraic direct-sum decision.
3. Malformed nested block-grid dimensions and a boolean substituted for an integer rank are rejected structurally, independent of any underlying witness intent.
4. A singular left transform produces a structurally valid audit record with an explicit negative invertibility/direct-sum result, not a schema exception.

The test establishes separation of record structure from mathematical witness validity for these fixtures. It is deterministic regression coverage, not a universal proof of the verifier or a provenance/authenticity mechanism.

## G-EP101: Independent audit-record reconstruction

A new test-local reference calculation reconstructs the audit record from the original coefficient matrices, field, supplied left/right transforms, and ordered rectangular partition. It independently multiplies matrices modulo the field, computes transform ranks by Gaussian elimination, slices every rectangular block (including zero-row and zero-column blocks), and derives invertibility, off-diagonal-zero, and aggregate diagnostics.

The regression compares these independently derived values with the verifier output for identity, nontrivial invertible, and singular left transforms. It also mutates transformed coefficients, nested Q/K blocks, rank diagnostics, and the aggregate decision in otherwise shape-preserving snapshots, requiring each changed value to disagree with the independently reconstructed record. False and singular witnesses are deliberately reconstructed as consistent negative records: consistency of the audit data is not the same as a positive direct-sum result.

The routines are test-local and do not call the production verifier's multiplication, rank, or block-splitting helpers. This is finite independent regression evidence, not a production snapshot-ingestion API, a formal proof, or cryptographic provenance/authenticity.

## G-EP102: Seeded cross-field rectangular reconstruction

Deterministic, field-specific rectangular partitions are exercised over F₂, F₃, F₅, and F₇. For each fixture, test-local seeded elementary row operations produce independently invertible left and right transforms. The source pencil is formed by applying their inverses to independently generated block-diagonal coefficient matrices; the verifier must reconstruct those original matrices exactly. The partitions include zero-row and zero-column blocks without any 0×0 block.

The same source entries are then shifted by different multiples of the field characteristic. The normalized transformed matrices, rectangular block grids, and verification diagnostics must remain unchanged. A shape-preserving transformed-matrix mutation is included as a snapshot-integrity control. These tests add finite cross-field regression coverage; they do not establish a universal theorem, formal proof, or production snapshot-authenticity mechanism.

## G-EP103: Three-layer audit pipeline

The new test keeps three questions independent:

1. **Structural schema:** does the record have the required v1 fields, exact primitive types, matrix dimensions, rectangular block-grid dimensions, and bounded rank diagnostics?
2. **Source consistency:** do the transformed coefficients, both nested block grids, normalized transforms, and verification diagnostics match a test-local reconstruction from the original Q/K matrices, field, and supplied transforms?
3. **Mathematical verdict:** after reconstruction, are both transforms invertible and are all off-diagonal blocks zero in both coefficients?

A mutation matrix records which layer detects each case. A missing nested grid row fails schema validation. Shape-preserving edits to a transformed coefficient, a nested block, or a rank diagnostic pass the schema check but fail reconstruction. A valid positive witness passes all three layers. A well-formed, reconstruction-consistent false witness passes the first two layers and fails only the mathematical verdict. Thus neither schema validity nor audit-record consistency is treated as proof of decomposition success.

These are deterministic test-local regressions on a small F₅ fixture, not a production ingestion pipeline, formal proof, or cryptographic authenticity mechanism.

## G-EP104: Adversarial metadata and equivalent witnesses

The metadata regression set mutates the schema version, finite-field label, source dimensions, ordered block partition, and descriptive scope. An unsupported schema version, dimension mismatch, or partition whose declared rectangular pieces no longer match the stored block grid fails structural validation. A well-typed but altered field label or scope string can remain structurally valid; the test separately detects that it no longer matches the expected source-bound snapshot. The mathematical verdict is recomputed from the original matrices and transforms rather than accepted from metadata.

The test also supplies a distinct valid witness over F₅ using reciprocal scalar rescaling, S → 2S and T → 3T. Since 2·3 = 1 in F₅, both transformed coefficients remain unchanged even though the transforms differ. This is an equivalent witness, not a forged certificate. These deterministic tests do not provide cryptographic provenance or authenticate who created a snapshot.


## G-EP105: Rectangular coordinate-permutation conjugacy

The rectangular multi-block witness tests now distinguish a consistent
coordinate reindexing from one-sided changes. Over F₂, F₃, F₅, and F₇, the
fixture contains both zero-row and zero-column blocks. The test simultaneously
reorders row and column coordinate intervals, reorders the corresponding
block-shape list, and conjugates the supplied left and right transforms by
their respective permutation matrices. The verifier must accept the witness
and reproduce the exactly reordered block-diagonal Q and K coefficients.

Separate controls permute only row coordinates or only column coordinates
while retaining the incompatible side's coordinates and original partition;
these witnesses must fail. Empty intervals are retained as ordered block
slots even though they contribute no coordinate indices.

This is deterministic finite regression coverage of the verifier's supplied
witness contract. It does not add decomposition discovery, prove uniqueness,
or imply that failure of one supplied witness excludes another.


## G-EP106: Composed equivalence transformations

The new regression composes two successive independent basis changes on
the source row and column spaces, then applies a common block-order
permutation and reciprocal scalar rescaling of the supplied transforms.
The rectangular fixture retains zero-row and zero-column block slots.
Across F₂, F₃, F₅, and F₇, the composite witness must reproduce the exact
reordered block-diagonal Q and K coefficients. A negative control changes
only the final left-transform permutation and must fail verification.

For source updates Q ↦ A Q B, the corresponding witness updates by
S ↦ S A⁻¹ and T ↦ B⁻¹ T. The test composes these in the stated order,
then applies the output block-coordinate permutation and reciprocal
scalars. It checks the resulting algebraic identities through the public
verifier rather than relying on a stored success flag.

This is deterministic finite regression evidence. It does not establish
uniqueness, decomposition discovery, or universal correctness beyond the
tested finite fields and fixtures.


## G-EP107: Transformation factorization-order invariance

The regression constructs two different ordered factorizations of the same
composite left and right basis changes. The second path uses conjugated
factors so that reversing the factor application order preserves the exact
composite matrices. Both paths therefore produce identical source-coordinate
pairs before a shared block-coordinate permutation and reciprocal scalar
rescaling are applied.

The resulting witness is checked over F₂, F₃, F₅, and F₇ using a rectangular
partition with zero-row and zero-column blocks. The test compares the exact
transformed coefficients and all reported diagonal block records. A
negative control omits an inverse basis factor and must fail verification.

This tests equality of two explicit transformation factorizations; it does
not imply uniqueness of the witness or discover a decomposition.


## G-EP108: Seeded metamorphic rectangular witness families

A fixed pseudo-random seed generates products of elementary invertible row
operations independently on the left and right coordinate spaces. Three
rectangular block partitions are exercised over F₂, F₃, F₅, and F₇, with
zero-row and zero-column block slots. Each block receives deterministic
pseudo-random Q and K coefficients; the source pair is formed by applying
the inverse basis changes, and the verifier must recover the exact original
block-diagonal matrices.

For each field and partition, a single-entry off-diagonal perturbation is
transported back to source coordinates. The unchanged supplied witness must
then expose that exact cross-block coefficient and reject the pair. This
provides reproducible metamorphic regression coverage, not a universal
correctness theorem or an automatic decomposition method.
