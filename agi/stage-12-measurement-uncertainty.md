# Stage 12 — measurement intervals and calibration corrections

## Why exact equality is not measurement compatibility

Stages 9–11 normalize exact quantities. A measured value is different: it is an observation accompanied by a statement about its uncertainty. Two observations can have different nominal values while their stated ranges overlap. Conversely, identical nominal values do not make two measurements exact or identical.

Stage 12 keeps these relations separate:

- **Exact equivalence:** both inputs are exact observations, with equal normalized values, dimensions, and quantity kinds.
- **Interval compatibility:** at least one input has an explicit interval and the normalized closed intervals intersect.
- **No compatibility proposal:** the intervals are disjoint, the quantity types differ, or the uncertainty description is unsupported.
- **Unknown:** absence of a compatibility proposal is not by itself proof that the underlying physical quantities differ.

An overlap is not an equivalence relation: it need not be transitive. For example, intervals [0, 2] and [1, 3] overlap, as do [1, 3] and [2.5, 4], while [0, 2] and [2.5, 4] do not. Therefore interval overlap must not be fed into the learner as an equivalence merge.

## Explicit data contract

The current implementation accepts an interval in the same displayed unit as the nominal value:

```python
{
    "value": 10,
    "unit": "m",
    "uncertainty": {
        "type": "interval",
        "lower": 9,
        "upper": 11
    }
}
```

The endpoints are absolute bounds on the reading, not plus/minus magnitudes. They must be exact numeric values and satisfy

[
\text{lower}\leq\text{value}\leq\text{upper}.
]

The bounds are normalized through the same exact unit conversion as the nominal value. This also works for the monotone affine temperature conversions already supported in Stage 11.

A signed `calibration_correction` may be supplied in the displayed unit's additive scale. It is applied to the nominal value and both interval endpoints before canonical normalization. For an affine temperature unit, the correction is a temperature difference, so it is scaled but not offset.

## Exact arithmetic and evidence

The parser continues to use integers, fractions, and finite decimals, converted to exact rational values. Binary floating-point inputs are rejected rather than silently treated as exact.

For two compatible quantity types, the proposer computes

[
I_1=[a_1,b_1],\
I_2=[a_2,b_2]
]

and records compatibility exactly when

[
\max(a_1,a_2)\leq\min(b_1,b_2).
]

The returned overlap is

[
[\max(a_1,a_2),\min(b_1,b_2)].
]

This record is separate from equivalence candidates and counterexamples. It is not submitted to the concept learner's equivalence partition.

## What is deliberately not inferred

The implementation does not currently interpret standard uncertainty, expanded uncertainty, coverage factors, confidence intervals, probability distributions, or covariance. A numeric standard deviation does not determine a probability statement without a statistical model and its assumptions. The parser rejects those unsupported uncertainty types instead of inventing a Gaussian model or confidence level.

Calibration correction is an explicit supplied value; this stage does not estimate instrument bias, learn calibration curves, propagate correlated errors, or infer traceability. Nor does interval overlap establish that two instruments measure the same measurand: the quantity kind and measurement context still matter.

## Verification

The regression suite covers:
- overlap versus exact equivalence;
- disjoint intervals;
- exact observations against uncertain intervals;
- exact calibration correction;
- correction of both interval endpoints;
- rejection of malformed intervals and unsupported statistical uncertainty;
- affine normalization of Celsius and Fahrenheit interval bounds;
- all Stage 9–11 exact-unit, type, and temperature cases.

Run:

```sh
python -m unittest agi.test_concept_learner agi.test_concept_proposer -v
python agi/concept_learner.py
```

## Status

This is a deterministic, exact-arithmetic measurement-data prototype. It introduces a disciplined distinction between equality and compatibility, but it does not yet model full metrology or statistical inference. It is one useful capability for a broader learning system, not evidence that AGI has been achieved.
