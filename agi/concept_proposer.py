"""Exact compound-unit proposal generation for task-scoped concept learning.

Supported grammar: unit (('*' | '/') unit)*, with optional integer powers,
for example 'km/h', 'm/s^2', and 'kg*m/s^2'. Parentheses and implicit
multiplication are deliberately unsupported.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Any

from agi.concept_learner import Candidate, ConceptLearner, Counterexample

# Dimension-vector order is (length, mass, time).
Dimension = tuple[int, int, int]
_ZERO: Dimension = (0, 0, 0)


@dataclass(frozen=True)
class Quantity:
    dimension: Dimension
    base_value: Fraction
    unit: str


@dataclass(frozen=True)
class ProposalBatch:
    equivalences: tuple[Candidate, ...]
    counterexamples: tuple[Counterexample, ...]


# Conversion factor to SI base units, with dimensions (L, M, T).
_UNITS: dict[str, tuple[Dimension, Fraction]] = {
    "m": ((1, 0, 0), Fraction(1)),
    "cm": ((1, 0, 0), Fraction(1, 100)),
    "mm": ((1, 0, 0), Fraction(1, 1000)),
    "km": ((1, 0, 0), Fraction(1000)),
    "s": ((0, 0, 1), Fraction(1)),
    "ms": ((0, 0, 1), Fraction(1, 1000)),
    "min": ((0, 0, 1), Fraction(60)),
    "h": ((0, 0, 1), Fraction(3600)),
    "kg": ((0, 1, 0), Fraction(1)),
    "g": ((0, 1, 0), Fraction(1, 1000)),
    "N": ((1, 1, -2), Fraction(1)),
    "J": ((2, 1, -2), Fraction(1)),
    "W": ((2, 1, -3), Fraction(1)),
    "Pa": ((-1, 1, -2), Fraction(1)),
    "Hz": ((0, 0, -1), Fraction(1)),
}

_TOKEN = re.compile(r"[A-Za-z]+(?:\^-?\d+)?|[*/]")


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
    """Parse a bounded product/quotient of known units and integer powers."""
    if not isinstance(expression, str) or not expression or len(expression) > 64:
        return None
    tokens = _TOKEN.findall(expression)
    if not tokens or "".join(tokens) != expression:
        return None

    dimensions = [0, 0, 0]
    factor = Fraction(1)
    expect_unit = True
    sign = 1

    for token in tokens:
        if expect_unit:
            if token in ("*", "/"):
                return None
            if "^" in token:
                symbol, power_text = token.split("^", 1)
                power = int(power_text)
            else:
                symbol, power = token, 1
            if abs(power) > 12 or symbol not in _UNITS:
                return None
            dimension, unit_factor = _UNITS[symbol]
            effective_power = sign * power
            for index in range(3):
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
    return (dimensions[0], dimensions[1], dimensions[2]), factor


def parse_quantity(payload: Any) -> Quantity | None:
    """Parse {'value': exact_number, 'unit': unit_expression}; else skip."""
    if not isinstance(payload, dict):
        return None
    value = _exact_fraction(payload.get("value"))
    parsed_unit = parse_unit_expression(payload.get("unit"))
    if value is None or parsed_unit is None:
        return None
    dimension, factor = parsed_unit
    return Quantity(dimension, value * factor, payload["unit"])


class UnitQuantityProposer:
    """Propose relations for exact physical-quantity equality."""

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
                if q_left.dimension == q_right.dimension:
                    if q_left.base_value == q_right.base_value:
                        equivalences.append(Candidate(
                            left, right, 1.0,
                            "exact compound-unit normalization and dimension match",
                        ))
                elif q_left.base_value == q_right.base_value:
                    counterexamples.append(Counterexample(
                        left, right,
                        "equal canonical numeral but incompatible dimension vectors",
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
