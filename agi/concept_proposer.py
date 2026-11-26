"""Deterministic, unit-aware candidate generation for concept learning.

This narrow proposer discovers exact equivalences and hard negatives from
structured physical-quantity observations. It is not a general semantic model.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Any

from agi.concept_learner import Candidate, ConceptLearner, Counterexample


@dataclass(frozen=True)
class Quantity:
    dimension: str
    base_value: Fraction
    unit: str


@dataclass(frozen=True)
class ProposalBatch:
    equivalences: tuple[Candidate, ...]
    counterexamples: tuple[Counterexample, ...]


# Each factor converts the unit value to the chosen base unit for its dimension.
_UNITS: dict[str, tuple[str, Fraction]] = {
    "m": ("length", Fraction(1)),
    "cm": ("length", Fraction(1, 100)),
    "mm": ("length", Fraction(1, 1000)),
    "km": ("length", Fraction(1000)),
    "s": ("time", Fraction(1)),
    "ms": ("time", Fraction(1, 1000)),
    "min": ("time", Fraction(60)),
    "h": ("time", Fraction(3600)),
    "kg": ("mass", Fraction(1)),
    "g": ("mass", Fraction(1, 1000)),
}


def _exact_fraction(value: Any) -> Fraction | None:
    """Accept exact numeric inputs only; reject floats and booleans."""
    if isinstance(value, bool) or isinstance(value, float):
        return None
    if isinstance(value, (int, Fraction, Decimal)):
        return Fraction(value)
    return None


def parse_quantity(payload: Any) -> Quantity | None:
    """Parse {'value': exact_number, 'unit': known_unit}; otherwise skip."""
    if not isinstance(payload, dict):
        return None
    unit = payload.get("unit")
    value = _exact_fraction(payload.get("value"))
    if not isinstance(unit, str) or unit not in _UNITS or value is None:
        return None
    dimension, factor = _UNITS[unit]
    return Quantity(dimension, value * factor, unit)


class UnitQuantityProposer:
    """Propose relations for the exact task 'physical quantity equality'.

    Same dimension and same exact base-unit value imply equivalence. Equal
    base-unit numerals with different dimensions are hard negatives. This
    proposer refuses other contexts so its assumptions cannot be silently
    reused for an unrelated notion of similarity.
    """

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
                            "exact unit normalization within the same dimension",
                        ))
                elif q_left.base_value == q_right.base_value:
                    counterexamples.append(Counterexample(
                        left, right,
                        "equal canonical numeral but incompatible physical dimensions",
                    ))

        return ProposalBatch(tuple(equivalences), tuple(counterexamples))

    def apply(self, learner: ConceptLearner) -> ProposalBatch:
        """Generate and submit proposals to the learner's conflict-aware gate."""
        batch = self.propose(learner)
        for item in batch.equivalences:
            learner.propose_equivalence(
                item.left, item.right, item.confidence, item.source
            )
        for item in batch.counterexamples:
            learner.add_counterexample(item.left, item.right, item.source)
        return batch
