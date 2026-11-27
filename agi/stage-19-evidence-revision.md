# Stage 19 — Evidence-driven hypothesis revision

## Protocol

The `EvidenceLedger` is immutable. Calling `append` creates a new ledger history and a feedback report; prior records and predictions are unchanged.

For each new exact observation ((x,y)), every supplied candidate is evaluated:
- exact match: `consistent_with_observation`;
- defined but unequal: `refuted_by_observation`;
- undefined at x: `undefined_on_observation`.

Refuted and undefined candidates are excluded from the returned retained set for this observation. The accumulated evidence is then passed to the existing exact relational proposer, which may generate proportional, inverse, or affine hypotheses supported on all accumulated rows. Generated candidates are returned separately and are never silently installed or selected.

## Data integrity

- Evidence keys are unique and append-only.
- Integers and rational `Fraction` values are accepted; floats and booleans are rejected.
- Every assessment records the prediction made at the time the observation was appended.
- A later observation cannot mutate earlier assessments.
- Candidate IDs must be unique within an update.
- Revision proposals are based only on the ledger's accumulated input/output evidence.

## Important limits

This is a small exact scalar feedback mechanism, not general learning. It does not infer noisy models, uncertainty, causal effects, or arbitrary programs. The existing proposer requires sufficient observations for each relation family; for example, affine proposals require at least three observations. A model refuted by one observation is not automatically replaced with a better one: generated proposals remain candidates requiring comparison and independent evaluation.

The ledger is immutable in the Python API, but durable storage, cryptographic tamper evidence, and multi-process synchronization are not provided. Provenance records cannot prove that external candidate generation avoided leakage. No physical experiment is executed. This is a bounded evidence-driven revision capability, not AGI.
