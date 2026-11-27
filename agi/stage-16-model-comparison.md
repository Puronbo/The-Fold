# Stage 16 — evidence-based comparison of competing relational models

## Purpose

Stages 13–15 discover bounded relation hypotheses, compose them, and validate fixed paths on held-out observations. Stage 16 compares multiple candidate paths on the same validation rows.

## Scoring protocol

Each candidate is evaluated without fitting or changing its parameters. The comparison reports endpoint matches and mismatches, supplied intermediate matches and mismatches, domain failures, and an explicit structural-complexity proxy.

Ranking is lexicographic:
1. Fewer endpoint mismatches.
2. Fewer supplied intermediate mismatches.
3. Lower structural complexity.
4. Candidate identifier for deterministic ordering only.

The complexity proxy counts nonzero coefficients, explicit domain exclusions, and relation steps. It is deliberately transparent and should not be mistaken for a universal measure of model simplicity.

## Mathematical equivalence

Candidates are grouped when their exact composed projective coefficient tuples and excluded input sets agree. This is equality within the implemented fractional-linear representation and domain convention, not semantic equivalence in every possible interpretation. Equivalent derivations remain visible; no candidate is silently deleted.

## Evidence safeguards

- Every candidate receives the same held-out rows.
- The selector never refits or adjusts relation parameters.
- Endpoint and intermediate evidence remain separate.
- Domain failures count as endpoint failures.
- An empty validation set returns `insufficient_validation_data`; it does not produce a winner.
- Ranking is a deterministic comparison, not a probability or confidence estimate.

## Verification

    python -m unittest agi.test_concept_learner agi.test_concept_proposer agi.test_relation_discovery agi.test_relation_composition agi.test_relation_validation agi.test_relation_selection -v

Tests cover correct-versus-refuted ranking, exact-equivalence grouping, complexity tie-breaking, hidden intermediate errors, domain failures, and insufficient data.

## Limits

This stage compares only caller-supplied candidates from the existing scalar fractional-linear family. It does not generate arbitrary programs, optimize parameters, estimate uncertainty, correct for multiple comparisons, or guarantee generalization beyond the held-out sample. The ranking can be biased if candidates or validation data were selected after inspecting the same evidence; the caller must preserve a genuinely separate evaluation set.

## Next step

Stage 17 can add controlled candidate generation and a discovery/validation/test split, with safeguards against repeatedly tuning the candidate set against the test partition.