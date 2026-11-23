# G-EP47 — Composable Kronecker component assembly

## Objective

The preceding milestones provide independent constructive methods for:
- one pure right singular block;
- one pure left singular block (by transposition); and
- a regular square pencil, including a canonical representative and bounded
  strict-equivalence witness search.

G-EP47 composes these capabilities when a proposed component partition is
already supplied.

## API

`tools/kronecker_component_assembly.py` exposes
`assemble_kronecker_components(components, p, ...)`. Each component
contains source matrices `q`, `k`, and a `kind`:
- `right`: structurally recover one right singular block;
- `left`: structurally recover one left singular block;
- `regular`: canonicalize a regular square component and construct its
  constant strict-equivalence witness.

For singular components, an optional `minimal_index` is treated as an
assertion and checked against the recovered index. A failed component stops
the assembly with its index and recovery report; it is never silently
accepted.

For component witnesses (S_i,T_i), the global transformations are
[
S=operatorname{diag}(S_1,ldots,S_r),qquad
T=operatorname{diag}(T_1,ldots,T_r).
]
The source and target pencils are assembled by direct sums, and the complete
pair is independently audited:
[
S Q T=Q_{m can},qquad S K T=K_{m can}.
]
The global certificate is returned only if the strict-equivalence audit
passes.

## What this establishes

This is an end-to-end constructive assembly path across heterogeneous
component types. It connects the previously separate regular and singular
witness tools and provides one global, exact certificate for their direct
sum. It also gives callers a reusable way to build and audit mixed canonical
examples over prime fields.

## Boundary: decomposition discovery remains open

The caller must provide the proposed component partition. This milestone
does not take an arbitrary unsplit pencil and discover all of its Kronecker
blocks, nor does it prove uniqueness of a supplied partition. In particular,
it does not yet handle multiple singular blocks coupled by an unknown
constant basis change as a single recovery problem. The regular component
witness search and its no-chart fallback retain their existing bounded-search
limitations.

The distinction is important: G-EP47 assembles and verifies a proposed
decomposition; it is not yet a complete general Kronecker canonical-form
algorithm.

## Tests

`tests/test_kronecker_component_assembly.py` covers a mixed right/left/
regular direct sum, an incorrect declared minimal index, a component that
fails singular recovery, and empty input rejection.


## G-EP60 — Integrated multi-block direct-sum audit

Successful assembly now derives `canonical_block_shapes` directly from the
canonical component matrices in the same order as the supplied component list.
It passes the assembled source pair and global block-diagonal transforms to
the independent G-EP58 `verify_pencil_multi_direct_sum_witness` verifier.
The returned `multi_block_direct_sum_audit` checks transform invertibility and
all off-diagonal component blocks in both coefficients. The existing global
strict-equivalence audit remains independent and unchanged.

The successful result exposes both certificates and a
`multi_block_direct_sum_verified` check. A failed singular or regular component
still returns the existing incomplete result before either global success
audit is emitted. No component discovery, uniqueness, indecomposability, or
regularity claim is added; the caller still supplies the partition.

Tests now assert the ordered three-block shape list and the independent audit
for a mixed right/left/regular assembly, and ensure failed recovery does not
emit a success audit.


## G-EP61 — Component-report consistency certificate

Successful assembly now emits `component_consistency_audit`. It checks that
component report count agrees with all source/target block lists; each source
coefficient pair matches its reported shape; both canonical coefficients have
matching block dimensions; right and left singular canonical shapes agree with
the recovered minimal index; and regular canonical blocks are square. It also
checks that ordered source and canonical block dimensions sum to the respective
assembled matrix shapes.

The audit is computed from the concrete component matrices and reports. It is
independent of the strict-equivalence and multi-block zero-pattern audits, and
all three are exposed in successful results. This does not reclassify a block,
discover a partition, or prove uniqueness. Failed component recovery continues
to return an incomplete result without success certificates.

Tests assert every consistency check for a mixed right/left/regular assembly
and ensure failed recovery emits no consistency certificate.


## G-EP62 — Per-component strict-equivalence certificates

Before placing each component transform into the global block-diagonal matrices, assembly now calls the exact strict-equivalence verifier on that component's original pair, canonical pair, and local transforms. A failed local identity raises an arithmetic error and cannot be hidden by later assembly. Successful results expose the ordered `component_witness_audits` list and an aggregate `all_component_witnesses_verified` check. The existing global strict-equivalence, multi-block direct-sum, and component-report consistency audits remain separate. This strengthens certificate localization; the supplied-partition requirement and bounded regular-witness behavior are unchanged.

Tests assert one passing local certificate per right, left, and regular component, and confirm that failed component recovery emits no local-witness audit list.
\n\n## G-EP63 — Component witness composition audit\n\nThe assembly path independently reconstructs the global left and right transformations using only the ordered local audit certificates. It compares these reconstructed matrices modulo p with the returned global S and T, then passes the reconstructed transforms to a fresh global strict-equivalence audit against the assembled source and canonical pencils. Successful results expose the reconstructed matrices, three explicit checks, and the replayed audit under `component_witness_composition_audit`; the aggregate check is `component_witness_composition_verified`. A failure prevents a successful assembly result. This verifies the composition layer in addition to each local witness and the existing global/multi-block audits; it does not discover components or prove uniqueness.\n\nTests assert exact reconstruction of both transforms and successful replay for a mixed right/left/regular assembly, and confirm that failed recovery emits no composition certificate.\n

## G-EP64 — Adversarial witness-composition validation

The composition-audit helper now validates its inputs before constructing
block-diagonal matrices. The local certificate list must be a nonempty ordered
sequence of dictionaries. Each certificate must contain nonempty, rectangular,
square left and right transformation matrices. Invalid shapes raise a
controlled `ValueError` rather than leaking indexing errors from block
assembly.

Adversarial regression coverage includes:

- modifying one local left transformation while retaining the original
  certificate metadata; the reconstructed-transform comparison and replayed
  global strict-equivalence check must both fail;
- adding an incompatible row to a local transform; validation rejects it
  before composition; and
- empty certificate lists and malformed nonsquare transforms; both produce
  explicit validation errors.

Certificate order remains semantically significant because it defines the
block ordering, but a permutation is not necessarily detectable or invalid:
if the relevant transformations are interchangeable (for example, identity
matrices), reordering can leave the composed transformation unchanged. The
audit therefore tests actual algebraic consistency rather than asserting that
every permutation must fail. G-EP64 adds no partition discovery, uniqueness,
or new Kronecker classification claim.


## G-EP65 — Component certificate provenance and binding

The composition audit now receives the ordered source and canonical coefficient blocks in addition to the assembled pencils. Before composing the global transforms, it independently re-runs the strict-equivalence verifier for each local pair using that certificate's own left and right transforms. It validates that all four ordered matrix-block lists have exactly one entry per local certificate and exposes the resulting per_component_replayed_audits.

The new aggregate check every_local_certificate_reverified_against_its_bound_pair is true only when each recomputed local strict-equivalence audit succeeds. The returned assembly also exposes component_witnesses_rebound_to_source_and_target_blocks. This recomputation does not trust the previously stored strict_equivalence_certified field as proof; it checks the actual matrices and transformations afresh. The global reconstructed-transform comparisons and global strict-equivalence replay remain independent checks.

Tests verify successful per-component replay, detect a tampered local transformation, and retain malformed-shape and empty-certificate regressions. This is certificate-to-component binding for the supplied ordered partition, not decomposition discovery, component identity beyond that order, or a uniqueness result.


## G-EP66 — Component certificate mutation and replay integrity

The G-EP65 binding checks now preflight all four ordered matrix-block collections
and validate their cardinalities before indexing any component. This ensures
missing, extra, or malformed block collections fail with a controlled
validation error rather than an accidental indexing exception.

Adversarial regressions mutate a component's bound source coefficient block
and, separately, its bound canonical coefficient block while retaining the
previous local transforms. Fresh strict-equivalence replay must reject each
changed pair. The tests also forge the stored local success flag in both
directions: a forged true value cannot mask a failed recomputation, and a
forged false value cannot override a valid recomputation. These checks confirm
that the audit's conclusion is derived from the concrete matrices and
transformations rather than cached metadata.

The scope remains the supplied ordered partition and its component pairs. The
audit does not discover components, identify them independently of their
ordering, or prove uniqueness of a decomposition.


## G-EP67 — Component input and dimension integrity

The supplied-component assembly boundary now validates each coefficient matrix
before calling modular pencil routines. Matrix and row containers must be
nonempty lists or tuples; rows must have a consistent, nonzero width; and each
entry must be an integer other than a boolean. The Q and K matrices of one
component must have identical dimensions. The public field parameter must be
a genuine integer (not a boolean) and is then checked for primality by the
existing pair validator.

Regression cases cover non-matrix inputs, malformed row containers, ragged
and empty matrices, floating-point and boolean entries, invalid/composite
field parameters, and mismatched Q/K shapes. Rectangular components remain
supported: the checks require matching dimensions within each coefficient
pair, not square components except where the component kind is regular.

This is input validation only. It does not alter witness construction,
component ordering, or the requirement that callers supply the partition.
