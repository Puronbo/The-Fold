"""Exact relational hypothesis proposals over paired scalar observations.

This module is deliberately separate from equivalence learning. It discovers
simple candidate laws, reports every supplied counterexample, and never
silently deletes observations or treats a fit as a causal explanation.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Any


def _exact(value: Any) -> Fraction | None:
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


@dataclass(frozen=True)
class Observation:
    key: str
    x: Fraction
    y: Fraction


@dataclass(frozen=True)
class RelationHypothesis:
    relation: str
    parameters: tuple[Fraction, ...]
    support: tuple[str, ...]
    counterexamples: tuple[str, ...]

    @property
    def status(self) -> str:
        return "supported_on_supplied_observations" if not self.counterexamples else "refuted"


class RelationalConceptProposer:
    """Find proportional, inverse, and affine patterns using exact arithmetic."""

    def __init__(self) -> None:
        self._observations: dict[str, Observation] = {}

    @property
    def observations(self) -> dict[str, Observation]:
        return dict(self._observations)

    def add_observation(self, key: str, x: Any, y: Any) -> None:
        if not isinstance(key, str) or not key.strip():
            raise ValueError("observation key must be a non-empty string")
        if key in self._observations:
            raise ValueError(f"duplicate observation key: {key}")
        exact_x, exact_y = _exact(x), _exact(y)
        if exact_x is None or exact_y is None:
            raise ValueError("x and y must be exact integers, Fractions, or finite Decimals")
        self._observations[key] = Observation(key, exact_x, exact_y)

    def propose(self) -> tuple[RelationHypothesis, ...]:
        rows = tuple(self._observations[key] for key in sorted(self._observations))
        if len(rows) < 2:
            return ()
        proposals: list[RelationHypothesis] = []

        # y = a*x. Seed from the first nonzero x, then test every row.
        seed = next((row for row in rows if row.x != 0), None)
        if seed is not None:
            a = seed.y / seed.x
            bad = tuple(row.key for row in rows if row.y != a * row.x)
            proposals.append(RelationHypothesis(
                "proportional", (a,), tuple(row.key for row in rows if row.key not in bad), bad
            ))

        # y = k/x, equivalently x*y = k. Zero x cannot satisfy a finite inverse law.
        seed = next((row for row in rows if row.x != 0), None)
        if seed is not None:
            k = seed.x * seed.y
            bad = tuple(row.key for row in rows if row.x == 0 or row.x * row.y != k)
            proposals.append(RelationHypothesis(
                "inverse", (k,), tuple(row.key for row in rows if row.key not in bad), bad
            ))

        # y = a*x+b needs at least three observations to avoid reporting a
        # two-point interpolation as meaningful evidence.
        if len(rows) >= 3:
            pair = next(
                ((left, right) for i, left in enumerate(rows)
                 for right in rows[i + 1:] if left.x != right.x),
                None,
            )
            if pair is not None:
                left, right = pair
                a = (right.y - left.y) / (right.x - left.x)
                b = left.y - a * left.x
                bad = tuple(row.key for row in rows if row.y != a * row.x + b)
                proposals.append(RelationHypothesis(
                    "affine", (a, b),
                    tuple(row.key for row in rows if row.key not in bad), bad
                ))

        return tuple(proposals)
