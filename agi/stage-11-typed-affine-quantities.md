# Stage 11 — typed quantities and affine temperature units

## Why dimension vectors are not enough

A dimension vector is a necessary structural invariant for physical-quantity equality, but it is not a complete semantic type. Energy and torque both have dimension

[
(L,M,T,Theta)=(2,1,-2,0),
]

yet they are different quantity kinds. Their units may even have identical scale factors and identical numerical values. A system that uses dimensions alone can therefore merge concepts that should remain distinct in a task that cares about quantity kind.

Stage 11 adds an optional explicit `kind` label to the observation. When present, it participates in equivalence: dimension, exact canonical value, and kind must all agree. If the same canonical numeral occurs with a different kind, the proposer emits a hard negative. Untyped observations remain untyped; the system does not invent a kind.

## Four-dimensional exponent vectors

The dimension basis is now

[
(L,M,T,\Theta),
]

where \(\Theta\) denotes thermodynamic temperature. Existing units receive a zero in the fourth coordinate. Absolute temperature and temperature intervals share the temperature dimension but receive different semantic kinds.

## Affine temperature conversion

Absolute temperature conversions are affine, not merely multiplicative:

[
T_K=T_{degC}+273.15,
]

[
T_K=(T_{degF}+459.67)\frac{5}{9}.
]

The implementation uses exact rational constants:

[
273.15=\frac{5463}{20},\qquad
459.67\frac{5}{9}=\frac{45967}{180}.
]

Thus 0 °C, 32 °F, and 273.15 K normalize to the same exact Kelvin value. Absolute affine units are accepted only as standalone units; they are rejected inside compound products or quotients.

Temperature intervals are different. A change of 10 °C equals a change of 18 °F, with no absolute offset:

[
10\,\Delta ^\circ C=18\,\Delta ^\circ F=10\,\Delta K.
]

The parser treats `deltaC`, `deltaF`, and `deltaK` as multiplicative interval units and assigns the distinct kind `temperature_interval`.

## Proposal rule

Two observations are proposed equivalent exactly when all three conditions hold:

1. Their dimension vectors agree.
2. Their exact SI-normalized values agree.
3. Their quantity-kind labels agree.

If the canonical values agree but dimensions or kinds differ, the proposer emits a counterexample. A missing kind is not silently inferred for general units; callers must provide semantic labels where dimension alone is insufficient.

## Implementation and verification

- `agi/concept_proposer.py` now supports a four-axis dimension vector, optional semantic kinds, absolute affine temperatures, and multiplicative temperature intervals.
- `agi/test_concept_proposer.py` includes energy/torque separation, Celsius/Fahrenheit/Kelvin equivalence, interval conversion, affine-unit grammar restrictions, and Stage 9/10 regressions.
- Run:

```sh
python -m unittest agi.test_concept_learner agi.test_concept_proposer -v
python agi/concept_learner.py
```

## Limits and next test

The quantity-kind vocabulary is caller-supplied, not learned. The implementation does not yet model uncertainty, calibration, logarithmic units (such as decibels), vector/tensor-valued quantities, or contextual semantic inference. A future learner should infer candidate kinds from use and relations, but retain provenance and counterexamples so that inferred labels remain revisable.

This remains a deterministic symbolic prototype, not an autonomous physical scientist or an AGI system.
