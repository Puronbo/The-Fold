# Stage 15 — independent validation of composed relations

## Purpose

Stages 13–14 propose exact relations and compose them. Stage 15 tests a fixed composed path against a separate validation set. Validation rows are not used to fit or revise the component relations.

## Validation protocol

Each row supplies an input and independently observed endpoint. It may also supply one expected value after each intermediate step. The validator executes the path exactly, compares intermediate values where available, then compares the final output.

The report distinguishes:
- `validated_on_independent_observations`: every endpoint and every supplied intermediate check agrees;
- `refuted_on_independent_observations`: at least one endpoint or intermediate check fails, or a path cannot be evaluated because of a domain restriction;
- `insufficient_validation_data`: no held-out rows were supplied.

If intermediate observations are omitted, the validator can test only the endpoint. A matching endpoint does not prove that the internal path is correct; the tests include an example where a wrong intermediate value is hidden by a later map.

## Design constraints

- Exact integers, Fractions, and Decimals only; floating-point inputs are rejected.
- The validation function never changes coefficients, searches for a better fit, or feeds observations back into discovery.
- Duplicate keys and malformed intermediate paths are rejected.
- A division-by-zero or other domain failure is recorded as a failed row, not silently skipped.
- Endpoint agreement and intermediate agreement are counted separately.

## Verification

Run:

    python -m unittest agi.test_concept_learner agi.test_concept_proposer agi.test_relation_discovery agi.test_relation_composition agi.test_relation_validation -v

Tests cover held-out affine composition, independent intermediate checks, endpoint counterexamples, domain failures, empty validation data, malformed rows, and float rejection.

## Limits

This validates a supplied path on a finite held-out set. It does not prove a relation universally, guarantee distributional generalization, estimate uncertainty, select among competing paths, infer causality, or discover arbitrary programs. Independence here is a data-protocol requirement: callers must keep validation observations separate from the observations used to propose the relations.

## Next step

Stage 16 can compare competing composed paths on the same held-out observations, with explicit complexity and coverage accounting, while avoiding the mistake of selecting a path solely because it overfits a small validation set.