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
