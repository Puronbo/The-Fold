"""Typed exact quantity proposals with compound and affine unit support.

Compound syntax: unit (('*' | '/') unit)*, with bounded integer powers.
Absolute affine temperature units are parsed only as standalone units.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from decimal import Decimal
from fractions import Fraction
from typing import Any

from agi.concept_learner import Candidate, ConceptLearner, Counterexample

# Dimension-vector order: (length, mass, time, thermodynamic temperature).
Dimension = tuple[int, int, int, int]
_ZERO: Dimension = (0, 0, 0, 0)


@dataclass(frozen=True)
class Quantity:
    dimension: Dimension
    base_value: Fraction
    kind: str | None
    unit: str = field(compare=False)


@dataclass(frozen=True)
class ProposalBatch:
    equivalences: tuple[Candidate, ...]
    counterexamples: tuple[Counterexample, ...]


# Multiplicative conversions to SI base units.
_UNITS: dict[str, tuple[Dimension, Fraction]] = {
    "m": ((1, 0, 0, 0), Fraction(1)),
    "cm": ((1, 0, 0, 0), Fraction(1, 100)),
    "mm": ((1, 0, 0, 0), Fraction(1, 1000)),
    "km": ((1, 0, 0, 0), Fraction(1000)),
    "s": ((0, 0, 1, 0), Fraction(1)),
    "ms": ((0, 0, 1, 0), Fraction(1, 1000)),
    "min": ((0, 0, 1, 0), Fraction(60)),
    "h": ((0, 0, 1, 0), Fraction(3600)),
    "kg": ((0, 1, 0, 0), Fraction(1)),
    "g": ((0, 1, 0, 0), Fraction(1, 1000)),
    "N": ((1, 1, -2, 0), Fraction(1)),
    "J": ((2, 1, -2, 0), Fraction(1)),
    "W": ((2, 1, -3, 0), Fraction(1)),
    "Pa": ((-1, 1, -2, 0), Fraction(1)),
    "Hz": ((0, 0, -1, 0), Fraction(1)),
    # Temperature intervals are multiplicative, unlike absolute temperatures.
    "deltaK": ((0, 0, 0, 1), Fraction(1)),
    "deltaC": ((0, 0, 0, 1), Fraction(1)),
    "deltaF": ((0, 0, 0, 1), Fraction(5, 9)),
}

# (dimension, multiplicative factor, additive offset, semantic kind)
_AFFINE_UNITS: dict[str, tuple[Dimension, Fraction, Fraction, str]] = {
    "K": ((0, 0, 0, 1), Fraction(1), Fraction(0), "absolute_temperature"),
    "degC": ((0, 0, 0, 1), Fraction(1), Fraction(5463, 20), "absolute_temperature"),
    "degF": ((0, 0, 0, 1), Fraction(5, 9), Fraction(45967, 180), "absolute_temperature"),
}

_TOKEN = re.compile(r"1|[A-Za-z]+(?:\^-?\d+)?|[*/]")


def _exact_fraction(value: Any) -> Fraction | None:
    """Accept exact numeric inputs only; reject floats, booleans and infinities."""
    if isinstance(value, bool) or isinstance(value, float):
        return None
    if isinstance(value, Decimal) and not value.is_finite():
        return None
    if isinstance(value, (int, Fraction, Decimal)):
        try:
            return Fraction(value)
        except (ValueError, OverflowError, ZeroDivisionError):
            return None
    return None


def parse_unit_expression(expression: Any) -> tuple[Dimension, Fraction] | None:
    """Parse products, quotients and bounded integer powers of linear units."""
    if not isinstance(expression, str) or not expression or len(expression) > 64:
        return None
    tokens = _TOKEN.findall(expression)
    if not tokens or "".join(tokens) != expression:
        return None

    dimensions = [0, 0, 0, 0]
    factor = Fraction(1)
    expect_unit = True
    sign = 1

    for token in tokens:
        if expect_unit:
            if token in ("*", "/"):
                return None
            if token == "1":
                power = 1
                dimension, unit_factor = _ZERO, Fraction(1)
            else:
                if "^" in token:
                    symbol, power_text = token.split("^", 1)
                    power = int(power_text)
                else:
                    symbol, power = token, 1
                # Affine absolute units must never enter a multiplicative expression.
                if abs(power) > 12 or symbol not in _UNITS:
                    return None
                dimension, unit_factor = _UNITS[symbol]
            effective_power = sign * power
            for index in range(4):
                dimensions[index] += dimension[index] * effective_power
            factor *= unit_factor ** effective_power
            expect_unit = False
        else:
            if token not in ("*", "/"):
                return None
            sign = 1 if token == "*" else -1
            expect_unit = True

    if expect_unit:
        return None
    return (dimensions[0], dimensions[1], dimensions[2], dimensions[3]), factor


def parse_quantity(payload: Any) -> Quantity | None:
    """Parse exact values with either a linear compound unit or affine unit."""
    if not isinstance(payload, dict):
        return None
    value = _exact_fraction(payload.get("value"))
    unit = payload.get("unit")
    supplied_kind = payload.get("kind")
    if value is None or not isinstance(unit, str):
        return None
    if supplied_kind is not None and (
        not isinstance(supplied_kind, str) or not supplied_kind.strip()
    ):
        return None

    if unit in _AFFINE_UNITS:
        dimension, factor, offset, inferred_kind = _AFFINE_UNITS[unit]
        if supplied_kind is not None and supplied_kind != inferred_kind:
            return None
        return Quantity(dimension, value * factor + offset, inferred_kind, unit)

    parsed_unit = parse_unit_expression(unit)
    if parsed_unit is None:
        return None
    dimension, factor = parsed_unit
    inferred_kind = "temperature_interval" if unit in ("deltaK", "deltaC", "deltaF") else supplied_kind
    if supplied_kind is not None and inferred_kind is not None and supplied_kind != inferred_kind:
        return None
    return Quantity(dimension, value * factor, inferred_kind, unit)


class UnitQuantityProposer:
    """Propose relations for exact, typed physical-quantity equality."""

    CONTEXT = "physical quantity equality"

    def propose(self, learner: ConceptLearner) -> ProposalBatch:
        if learner.context != self.CONTEXT:
            raise ValueError(f"proposer requires context: {self.CONTEXT}")

        parsed = {
            key: quantity
            for key, instance in learner.instances.items()
            if (quantity := parse_quantity(instance.payload)) is not None
        }
        equivalences: list[Candidate] = []
        counterexamples: list[Counterexample] = []
        keys = sorted(parsed)

        for index, left in enumerate(keys):
            q_left = parsed[left]
            for right in keys[index + 1:]:
                q_right = parsed[right]
                same_dimension = q_left.dimension == q_right.dimension
                same_kind = q_left.kind == q_right.kind
                same_value = q_left.base_value == q_right.base_value
                if same_dimension and same_kind and same_value:
                    equivalences.append(Candidate(
                        left, right, 1.0,
                        "exact normalization, dimension-vector and quantity-kind match",
                    ))
                elif same_value and (not same_dimension or not same_kind):
                    counterexamples.append(Counterexample(
                        left, right,
                        "equal canonical numeral but incompatible dimension or quantity kind",
                    ))

        return ProposalBatch(tuple(equivalences), tuple(counterexamples))

    def apply(self, learner: ConceptLearner) -> ProposalBatch:
        """Generate proposals and submit them to the learner's evidence gate."""
        batch = self.propose(learner)
        for item in batch.equivalences:
            learner.propose_equivalence(
                item.left, item.right, item.confidence, item.source
            )
        for item in batch.counterexamples:
            learner.add_counterexample(item.left, item.right, item.source)
        return batch
