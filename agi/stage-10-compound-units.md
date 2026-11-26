# Stage 10 — compound units and dimensional exponent vectors

## Objective

Stage 9 compared quantities expressed in single declared units. Stage 10 generalizes the representation to products, quotients, and integer powers of units. The aim is to recognize the same physical quantity across compound expressions without confusing equal numerals that have different dimensions.

## Dimension vectors

Use the ordered basis (length, mass, time):

[
mathbf d=(ell,m,t)inmathbb Z^3.
]

Examples:

| Quantity | Dimension vector |
|---|---:|
| length | (1, 0, 0) |
| mass | (0, 1, 0) |
| time | (0, 0, 1) |
| velocity | (1, 0, -1) |
| acceleration | (1, 0, -2) |
| force | (1, 1, -2) |
| energy | (2, 1, -2) |
| power | (2, 1, -3) |
| pressure | (-1, 1, -2) |
| frequency | (0, 0, -1) |

Multiplication adds exponent vectors; division subtracts them; raising a unit to power n multiplies its vector by n.

## Exact normalization

Every base unit has a rational conversion factor to SI units. A compound expression accumulates both its dimension vector and its exact conversion factor. For example:

[
36,mathrm{km/h}
=36cdotrac{1000}{3600},mathrm{m/s}
=10,mathrm{m/s}.
]

Likewise:

[
1,mathrm N
=1,mathrm{kg,m/s^2}.
]

The parser uses exact rational arithmetic. It supports products, quotients, and signed integer powers over an explicit unit table. It deliberately rejects parentheses, implicit multiplication, unknown symbols, malformed expressions, and powers whose absolute value exceeds 12. These restrictions keep the first parser auditable.

## Proposal rule

For parsed quantities x and y:

- If dimension vectors and exact SI-normalized values both agree, propose equivalence.
- If normalized numerals agree but dimension vectors differ, propose a hard negative.
- Otherwise, do not propose a relation.

The rule is task-specific to physical-quantity equality. It does not imply that two systems with equal numerical measurements are semantically interchangeable in every context.

## Implementation and tests

- `agi/concept_proposer.py` now parses compound expressions and emits dimension vectors.
- `agi/test_concept_proposer.py` covers speed, acceleration, force, energy, power, pressure, frequency boundaries, malformed syntax, and hard negatives.
- Run from the repository root:

```sh
python -m unittest agi.test_concept_learner agi.test_concept_proposer
python agi/concept_learner.py
```

## Limits

This is still a symbolic, deterministic system with a hand-authored SI unit table. It does not infer unit systems, parse arbitrary natural language, handle affine units, propagate measurement uncertainty, or discover physical laws. Temperature intervals and absolute temperatures require different treatment; a Celsius temperature cannot be converted by a pure multiplicative scale factor alone.

The dimension vector is a useful invariant, not a complete description of a physical quantity. Different quantities can share dimensions (for example, energy and torque), so context and semantic type may be needed to distinguish them.

## Next test

Stage 11 adds explicit quantity kinds and affine temperature handling. The next test is to preserve measurement uncertainty and calibration metadata rather than rounding them away or treating every observation as exact.
