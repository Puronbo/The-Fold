"""Finite exact affine transformation-group recognition."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from agi.representation_transfer import AffineRelationConcept
from agi.affine_relationships import compose_affine


@dataclass(frozen=True)
class AffineGroupReport:
    is_group: bool
    status: str
    identity_present: bool
    all_elements_invertible: bool
    closure_holds: bool
    inverses_present: bool
    associativity_basis: str
    identity_key: str | None
    inverse_pairs: tuple[tuple[str, str], ...]
    missing_compositions: tuple[tuple[str, str, str], ...]
    missing_inverses: tuple[tuple[str, str, str], ...]
    reasons: tuple[str, ...]
    order: int


def _signature(item: AffineRelationConcept) -> tuple[object, object]:
    return item.slope, item.intercept


def _identity() -> AffineRelationConcept:
    return AffineRelationConcept(1, 0)


def _inverse(item: AffineRelationConcept) -> AffineRelationConcept:
    if item.slope == 0:
        raise ValueError("constant affine maps are not invertible")
    return AffineRelationConcept(1 / item.slope, -item.intercept / item.slope)


def recognize_finite_affine_group(
    transformations: Sequence[tuple[str, AffineRelationConcept]],
) -> AffineGroupReport:
    """Recognize whether a finite supplied set is a group under composition.

    Associativity is inherited from function composition; the finite check
    therefore verifies identity, bijectivity, closure, and inverses.
    """
    keys = [key for key, _ in transformations]
    if any(not isinstance(key, str) or not key.strip() for key in keys):
        raise ValueError("transformation keys must be non-empty strings")
    if len(keys) != len(set(keys)):
        raise ValueError("transformation keys must be unique")
    signatures = [_signature(item) for _, item in transformations]
    if len(signatures) != len(set(signatures)):
        raise ValueError("duplicate transformations must have one canonical key")
    if not transformations:
        return AffineGroupReport(
            False, "insufficient_transformations", False, False, False, False,
            "inherited_from_function_composition", None, (), (), (), 
            ("the empty collection is not a group",), 0,
        )

    by_signature = {_signature(item): key for key, item in transformations}
    identity_key = by_signature.get(_signature(_identity()))
    identity_present = identity_key is not None
    all_invertible = all(item.slope != 0 for _, item in transformations)

    missing_compositions = []
    if all_invertible:
        for left_key, left in transformations:
            for right_key, right in transformations:
                result = compose_affine(left, right)
                result_key = by_signature.get(_signature(result))
                if result_key is None:
                    missing_compositions.append((left_key, right_key, repr(_signature(result))))
    else:
        missing_compositions = []

    missing_inverses = []
    inverse_pairs = []
    if all_invertible:
        for key, item in transformations:
            inv = _inverse(item)
            inverse_key = by_signature.get(_signature(inv))
            if inverse_key is None:
                missing_inverses.append((key, "inverse", repr(_signature(inv))))
            else:
                inverse_pairs.append((key, inverse_key))

    closure = all_invertible and not missing_compositions
    inverses = all_invertible and not missing_inverses
    reasons = []
    if not identity_present:
        reasons.append("identity transformation is absent")
    if not all_invertible:
        reasons.append("at least one map is non-bijective (zero slope)")
    if all_invertible and missing_compositions:
        reasons.append("the set is not closed under composition")
    if all_invertible and missing_inverses:
        reasons.append("at least one inverse is absent")
    is_group = identity_present and all_invertible and closure and inverses
    return AffineGroupReport(
        is_group,
        "finite_group_verified" if is_group else "not_a_group",
        identity_present, all_invertible, closure, inverses,
        "inherited_from_associativity_of_function_composition",
        identity_key, tuple(inverse_pairs), tuple(missing_compositions),
        tuple(missing_inverses), tuple(reasons), len(transformations),
    )
