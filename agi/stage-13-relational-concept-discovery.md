# Stage 13 — exact relational concept proposals

## Goal

Stages 9–12 compare and normalize individual quantities. Stage 13 asks whether paired observations follow a shared relation. The new module `agi/relation_discovery.py` proposes three deliberately narrow families:

[
y=ax quad 	ext{(proportional)}
]
[
xy=k quad 	ext{(inverse)}
]
[
y=ax+b quad 	ext{(affine)}
]

All values and fitted parameters use exact rational arithmetic. Integers, fractions, and finite decimals are accepted; binary floats and booleans are rejected.

## Evidence rules

- Proportional and inverse candidates require at least two observations and a nonzero input from which to seed a parameter.
- Affine candidates require at least three observations and at least two distinct input values. This avoids presenting a line through two points as meaningful discovery.
- Every supplied observation is checked against each candidate.
- Violating observation keys are reported explicitly as counterexamples; supporting keys are retained.
- Observations are never removed to improve a fit.
- The module is separate from the equality learner and does not merge concepts.

A candidate marked `supported_on_supplied_observations` means only that the exact formula matches the finite dataset. It does not establish causation, a physical law, uniqueness, or predictive validity outside the observed domain. A refuted candidate remains visible with its counterexamples.

## Scope and limitations

The inputs are paired scalar values with no unit or semantic metadata. Dimensional analysis, noisy regression, uncertainty propagation, multivariate relations, conservation laws, model selection, and active experiment design are not implemented. The proposer does not search an unbounded space of formulas; it checks only the three declared families.

## Verification

Run:

```sh
python -m unittest agi.test_relation_discovery -v
python -m unittest agi.test_concept_learner agi.test_concept_proposer agi.test_relation_discovery -v
```

The tests cover proportional, inverse, and affine patterns; insufficient evidence; exact decimal handling; zero inputs; and retained counterexamples.

## Status

Stage 13 is a deterministic finite-data pattern proposer. It demonstrates explicit relational hypothesis generation and falsification within a small hypothesis class. It is not autonomous scientific discovery or evidence that AGI has been achieved.
