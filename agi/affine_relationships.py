"""Exact pairwise relationships among scalar affine transformations."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from agi.representation_transfer import AffineRelationConcept, _exact


@dataclass(frozen=True)
class AffinePairRelationship:
    left_key: str
    right_key: str
    commute: bool
    commutator_offset: Fraction
    same_fixed_point_set: bool
    shared_unique_fixed_point: Fraction | None
    left_after_right: AffineRelationConcept
    right_after_left: AffineRelationConcept
    composition_order_matters: bool


@dataclass(frozen=True)
class RelationshipDiscovery:
    relationships: tuple[AffinePairRelationship, ...]
    commuting_pairs: tuple[tuple[str, str], ...]
    noncommuting_pairs: tuple[tuple[str, str], ...]
    status: str


def compose_affine(
    outer: AffineRelationConcept, inner: AffineRelationConcept
) -> AffineRelationConcept:
    """Return outer o inner exactly."""
    return AffineRelationConcept(
        outer.slope * inner.slope,
        outer.slope * inner.intercept + outer.intercept,
    )


def _fixed_set_signature(
    transformation: AffineRelationConcept,
) -> tuple[str, Fraction | None]:
    a, b = transformation.slope, transformation.intercept
    if a == 1:
        return ("all", None) if b == 0 else ("empty", None)
    return ("singleton", b / (1 - a))


def analyze_affine_pair(
    left_key: str,
    left: AffineRelationConcept,
    right_key: str,
    right: AffineRelationConcept,
) -> AffinePairRelationship:
    """Discover exact commutation and fixed-set relationships."""
    for key in (left_key, right_key):
        if not isinstance(key, str) or not key.strip():
            raise ValueError("transformation keys must be non-empty strings")
    if left_key == right_key:
        raise ValueError("pair keys must be distinct")

    left_after_right = compose_affine(left, right)
    right_after_left = compose_affine(right, left)
    commutator = left_after_right.intercept - right_after_left.intercept
    left_fixed = _fixed_set_signature(left)
    right_fixed = _fixed_set_signature(right)
    same_fixed = left_fixed == right_fixed
    shared_unique = (
        left_fixed[1]
        if left_fixed[0] == "singleton" and same_fixed else None
    )
    return AffinePairRelationship(
        left_key, right_key, commutator == 0, commutator,
        same_fixed, shared_unique, left_after_right, right_after_left,
        left_after_right != right_after_left,
    )


def discover_affine_relationships(
    transformations: Sequence[tuple[str, AffineRelationConcept]],
) -> RelationshipDiscovery:
    """Analyze every unordered pair in a finite declared transformation set."""
    keys = [key for key, _ in transformations]
    if any(not isinstance(key, str) or not key.strip() for key in keys):
        raise ValueError("transformation keys must be non-empty strings")
    if len(keys) != len(set(keys)):
        raise ValueError("transformation keys must be unique")
    relationships = tuple(
        analyze_affine_pair(key_a, law_a, key_b, law_b)
        for i, (key_a, law_a) in enumerate(transformations)
        for key_b, law_b in transformations[i + 1:]
    )
    commuting = tuple(
        (item.left_key, item.right_key)
        for item in relationships if item.commute
    )
    noncommuting = tuple(
        (item.left_key, item.right_key)
        for item in relationships if not item.commute
    )
    return RelationshipDiscovery(
        relationships, commuting, noncommuting,
        "insufficient_transformations" if len(transformations) < 2
        else "analyzed_supplied_transformations",
    )
