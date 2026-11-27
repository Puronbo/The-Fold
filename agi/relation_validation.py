"""Independent exact validation for composed relational paths."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Sequence
from agi.relation_composition import ComposedRelation


def _exact(value: Any) -> Fraction | None:
    if isinstance(value, bool) or isinstance(value, float):
        return None
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError, OverflowError):
        return None


@dataclass(frozen=True)
class ValidationObservation:
    key: str
    input_value: Fraction
    expected_output: Fraction
    expected_intermediates: tuple[Fraction | None, ...] = ()

    @classmethod
    def create(cls, key: str, input_value: Any, expected_output: Any,
               expected_intermediates: Sequence[Any | None] = ()) -> "ValidationObservation":
        if not isinstance(key, str) or not key.strip():
            raise ValueError("validation key must be a non-empty string")
        x, y = _exact(input_value), _exact(expected_output)
        if x is None or y is None:
            raise ValueError("validation values must be exact integers, Fractions, or Decimals")
        middle = tuple(None if value is None else _exact(value) for value in expected_intermediates)
        if any(value is None and raw is not None for value, raw in zip(middle, expected_intermediates)):
            raise ValueError("intermediate expectations must be exact numeric values or None")
        return cls(key, x, y, middle)


@dataclass(frozen=True)
class RowValidation:
    key: str
    predicted_output: Fraction | None
    predicted_intermediates: tuple[Fraction, ...]
    intermediate_matches: tuple[bool | None, ...]
    output_matches: bool | None
    error: str | None


@dataclass(frozen=True)
class ValidationReport:
    status: str
    rows: tuple[RowValidation, ...]
    checked_rows: int
    output_matches: int
    output_mismatches: int
    intermediate_checks: int
    intermediate_matches: int
    intermediate_mismatches: int


def validate_composed_path(steps: Sequence[ComposedRelation],
                           observations: Sequence[ValidationObservation]) -> ValidationReport:
    """Evaluate a fixed path on independent rows; never fit or alter its parameters."""
    if not steps:
        raise ValueError("at least one relation step is required")
    if not observations:
        return ValidationReport("insufficient_validation_data", (), 0, 0, 0, 0, 0, 0)
    keys = [row.key for row in observations]
    if len(set(keys)) != len(keys):
        raise ValueError("validation observation keys must be unique")
    results = []
    out_ok = out_bad = mid_ok = mid_bad = mid_count = 0
    for row in observations:
        if row.expected_intermediates and len(row.expected_intermediates) != len(steps):
            raise ValueError("expected_intermediates must be empty or match the path length")
        value = row.input_value
        intermediates = []
        comparisons = []
        error = None
        try:
            for index, step in enumerate(steps):
                value = step.evaluate(value)
                intermediates.append(value)
                expected = row.expected_intermediates[index] if row.expected_intermediates else None
                comparisons.append(None if expected is None else value == expected)
                if expected is not None:
                    mid_count += 1
                    if value == expected:
                        mid_ok += 1
                    else:
                        mid_bad += 1
            output_match = value == row.expected_output
            out_ok += int(output_match)
            out_bad += int(not output_match)
            results.append(RowValidation(row.key, value, tuple(intermediates), tuple(comparisons),
                                         output_match, None))
        except (ZeroDivisionError, ValueError) as exc:
            out_bad += 1
            results.append(RowValidation(row.key, None, tuple(intermediates), tuple(comparisons),
                                         False, str(exc)))
    status = "validated_on_independent_observations" if out_bad == 0 and mid_bad == 0 else "refuted_on_independent_observations"
    return ValidationReport(status, tuple(results), len(observations), out_ok, out_bad,
                            mid_count, mid_ok, mid_bad)
