"""Compositional affine concepts and exact transfer through layered coordinates.

Each path edge maps one representation space to the next. A coordinate map
is supplied for every layer, so transfer is checked edge-by-edge, not only
at the final output.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from agi.representation_transfer import (
    AffineCoordinateMap, AffineRelationConcept, _exact,
)


@dataclass(frozen=True)
class CompositionalAffineConcept:
    steps: tuple[AffineRelationConcept, ...]

    def __post_init__(self) -> None:
        if not self.steps:
            raise ValueError("a compositional concept needs at least one step")
        if any(not isinstance(step, AffineRelationConcept) for step in self.steps):
            raise TypeError("every path step must be an affine relation concept")

    @property
    def composed(self) -> AffineRelationConcept:
        """Return the endpoint relation, retaining the original path separately."""
        slope, intercept = Fraction(1), Fraction(0)
        for step in self.steps:
            intercept = step.slope * intercept + step.intercept
            slope = step.slope * slope
        return AffineRelationConcept(slope, intercept)

    @property
    def structural_signature(self) -> tuple[tuple[Fraction, Fraction], ...]:
        return tuple((step.slope, step.intercept) for step in self.steps)

    @property
    def endpoint_signature(self) -> tuple[Fraction, Fraction]:
        return self.composed.slope, self.composed.intercept

    def evaluate_path(self, value: int | Fraction) -> tuple[Fraction, ...]:
        current = _exact(value)
        outputs = []
        for step in self.steps:
            current = step.predict(current)
            outputs.append(current)
        return tuple(outputs)


@dataclass(frozen=True)
class CompositionalTransferResult:
    concept: CompositionalAffineConcept
    mapped_path: CompositionalAffineConcept
    source_intermediates: tuple[tuple[str, tuple[Fraction, ...]], ...]
    target_intermediates: tuple[tuple[str, tuple[Fraction, ...]], ...]
    edge_commuting: tuple[bool, ...]
    status: str


def transfer_compositional_concept(
    concept: CompositionalAffineConcept,
    layer_coordinates: Sequence[AffineCoordinateMap],
    inputs: Sequence[tuple[str, int | Fraction]],
) -> CompositionalTransferResult:
    """Transfer every edge using one invertible coordinate map per layer.

    For edge i, the diagram commutes:
        phi_(i+1)(f_i(x)) = f'_i(phi_i(x)).
    All intermediate layers are checked exactly.
    """
    if len(layer_coordinates) != len(concept.steps) + 1:
        raise ValueError("one coordinate map is required for each path layer")
    keys = [key for key, _ in inputs]
    if any(not isinstance(key, str) or not key.strip() for key in keys):
        raise ValueError("input keys must be non-empty strings")
    if len(keys) != len(set(keys)):
        raise ValueError("input keys must be unique")

    mapped_steps = []
    for index, step in enumerate(concept.steps):
        input_map = layer_coordinates[index]
        output_map = layer_coordinates[index + 1]
        slope = output_map.scale * step.slope / input_map.scale
        intercept = (
            output_map.scale * step.intercept
            + output_map.offset
            - slope * input_map.offset
        )
        mapped_steps.append(AffineRelationConcept(slope, intercept))
    mapped_concept = CompositionalAffineConcept(tuple(mapped_steps))

    source_rows = []
    target_rows = []
    edge_ok = [True] * len(concept.steps)
    for key, raw_x in inputs:
        x = _exact(raw_x)
        source_values = concept.evaluate_path(x)
        target_x = layer_coordinates[0].forward(x)
        target_values = mapped_concept.evaluate_path(target_x)
        expected_values = tuple(
            layer_coordinates[index + 1].forward(value)
            for index, value in enumerate(source_values)
        )
        source_rows.append((key, source_values))
        target_rows.append((key, target_values))
        for index, (actual, expected) in enumerate(zip(target_values, expected_values)):
            edge_ok[index] = edge_ok[index] and actual == expected

    return CompositionalTransferResult(
        concept, mapped_concept, tuple(source_rows), tuple(target_rows),
        tuple(edge_ok),
        "transferred" if all(edge_ok) else "invariant_check_failed",
    )


def compare_compositional_structure(
    left: CompositionalAffineConcept,
    right: CompositionalAffineConcept,
) -> str:
    """Distinguish identical paths from merely identical endpoint functions."""
    if left.structural_signature == right.structural_signature:
        return "structurally_equivalent"
    if left.endpoint_signature == right.endpoint_signature:
        return "endpoint_equivalent_only"
    return "not_equivalent"
