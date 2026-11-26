# Stage 9 — deterministic concept proposal from observations

## Scope

Stage 8 accepted candidate equivalences and counterexamples from an external caller. Stage 9 adds a first proposal mechanism that derives both kinds of evidence from structured observations.

The initial domain is deliberately narrow: **physical quantity equality** for a declared set of metric units. This is a controlled test of proposal generation, not a claim of general semantic understanding.

## Representation and normalization

An observation has the form

```python
{"value": 100, "unit": "cm"}
```

Each recognized unit maps to a dimension and an exact rational conversion factor to a canonical base unit:

- length: m, cm, mm, km;
- time: s, ms, min, h;
- mass: kg, g.

For a value v and unit factor f, the normalized value is the exact rational number

[
N(v,u)=v f_u.
]

Only integers, `Fraction`, and `Decimal` inputs are accepted. Binary floating-point values are skipped rather than silently treated as exact decimal measurements. Unknown units and malformed payloads are also skipped.

## Proposal rules

For two parsed observations x and y:

1. If their dimensions agree and their normalized values agree, propose equivalence.
2. If their dimensions differ but their normalized numerical values agree, propose a hard negative (counterexample) under the stated physical-quantity-equality task.
3. Otherwise, make no proposal.

The second rule is important: the numeral 1 in metres is not the same physical quantity as the numeral 1 in seconds. A feature matcher that sees only normalized numbers would create a false equivalence.

The proposer refuses any learner context other than the exact string `physical quantity equality`. This is a guard against silently transferring a task-specific rule to visual similarity, mathematical equality, or another context.

## Implementation

- `agi/concept_proposer.py` defines exact unit normalization and `UnitQuantityProposer`.
- `agi/test_concept_proposer.py` covers equivalence proposals, dimension-based hard negatives, exact decimal/rational handling, malformed observations, and context refusal.
- The proposer returns an immutable `ProposalBatch` so proposals can be inspected before application. Its `apply` method submits them to the existing counterexample-aware `ConceptLearner`.

Run from the repository root:

```sh
python -m unittest agi.test_concept_learner agi.test_concept_proposer
python agi/concept_learner.py
```

## What this does and does not establish

**Established by the code's rules:** within the supported unit table and accepted exact numeric types, equal dimension plus equal exact canonical value is a valid quantity-equality rule. Distinct dimensions are kept apart even when the canonical numerals coincide.

**Not established:** autonomous unit discovery, arbitrary dimensional analysis, uncertainty propagation, measurement calibration, affine units (such as Celsius/Fahrenheit), compound units, or general concept formation. The proposer does not learn conversion factors; they are supplied as explicit domain knowledge. Confidence 1.0 marks a deterministic rule application, not a calibrated probability that the observations are true.

## Next falsifiable extension

Add compound-unit parsing and dimensional exponent vectors (for example, m/s and km/h), then test that normalization is invariant under equivalent unit rewrites while rejecting dimensionally incompatible quantities. Keep measured uncertainty separate from exact symbolic equality.
