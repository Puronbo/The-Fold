"""Exact transfer of affine relational concepts across declared coordinates.

This is a narrow symbolic transfer rule: invertible affine coordinate maps
preserve affine relationships, with coefficients transformed exactly.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence


def _exact(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("values must be exact integers or Fractions")
    return Fraction(value)


@dataclass(frozen=True)
class AffineCoordinateMap:
    scale: Fraction
    offset: Fraction

    def __post_init__(self) -> None:
        scale, offset = _exact(self.scale), _exact(self.offset)
        if scale == 0:
            raise ValueError("coordinate map must be invertible (nonzero scale)")
        object.__setattr__(self, "scale", scale)
        object.__setattr__(self, "offset", offset)

    def forward(self, value: int | Fraction) -> Fraction:
        return self.scale * _exact(value) + self.offset

    def inverse(self, value: int | Fraction) -> Fraction:
        return (_exact(value) - self.offset) / self.scale


@dataclass(frozen=True)
class AffineRelationConcept:
    slope: Fraction
    intercept: Fraction

    def __post_init__(self) -> None:
        object.__setattr__(self, "slope", _exact(self.slope))
        object.__setattr__(self, "intercept", _exact(self.intercept))

    def predict(self, x: int | Fraction) -> Fraction:
        return self.slope * _exact(x) + self.intercept

    def residual(self, x: int | Fraction, y: int | Fraction) -> Fraction:
        return _exact(y) - self.predict(x)


@dataclass(frozen=True)
class PairedObservation:
    key: str
    x: Fraction
    y: Fraction

    @classmethod
    def create(cls, key: str, x: int | Fraction, y: int | Fraction) -> "PairedObservation":
        if not isinstance(key, str) or not key.strip():
            raise ValueError("observation key must be non-empty")
        return cls(key, _exact(x), _exact(y))


@dataclass(frozen=True)
class TransferResult:
    concept: AffineRelationConcept
    transformed_observations: tuple[PairedObservation, ...]
    source_zero_residuals: tuple[tuple[str, Fraction], ...]
    target_zero_residuals: tuple[tuple[str, Fraction], ...]
    invariant_preserved: bool
    status: str


def transfer_affine_concept(
    concept: AffineRelationConcept,
    input_coordinates: AffineCoordinateMap,
    output_coordinates: AffineCoordinateMap,
    observations: Sequence[PairedObservation],
) -> TransferResult:
    """Transfer y=a*x+b through x'=s*x+t and y'=u*y+v.

    The transferred relation is y'=a'*x'+b', where
    a'=u*a/s and b'=u*b+v-a'*t. The zero/nonzero status of each
    residual is invariant because residual' = u*residual.
    """
    keys = [row.key for row in observations]
    if len(keys) != len(set(keys)):
        raise ValueError("observation keys must be unique")
    a_prime = output_coordinates.scale * concept.slope / input_coordinates.scale
    b_prime = (
        output_coordinates.scale * concept.intercept
        + output_coordinates.offset
        - a_prime * input_coordinates.offset
    )
    transferred = AffineRelationConcept(a_prime, b_prime)
    mapped = tuple(
        PairedObservation(
            row.key,
            input_coordinates.forward(row.x),
            output_coordinates.forward(row.y),
        )
        for row in observations
    )
    source_residuals = tuple(
        (row.key, concept.residual(row.x, row.y)) for row in observations
    )
    target_residuals = tuple(
        (row.key, transferred.residual(row.x, row.y)) for row in mapped
    )
    preserved = all(
        target == output_coordinates.scale * source
        for (_, source), (_, target) in zip(source_residuals, target_residuals)
    )
    return TransferResult(
        transferred, mapped, source_residuals, target_residuals, preserved,
        "transferred" if preserved else "invariant_check_failed",
    )
