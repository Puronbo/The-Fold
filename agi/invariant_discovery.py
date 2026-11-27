"""Exact invariant profiles for scalar affine self-transformations.

Profiles are derived from coefficients, not guessed from finite samples.
The conjugacy checker verifies whether two maps are related by a declared
invertible affine coordinate change.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from agi.representation_transfer import AffineCoordinateMap, AffineRelationConcept, _exact


@dataclass(frozen=True)
class AffineInvariantProfile:
    multiplier: Fraction
    is_identity: bool
    has_unique_fixed_point: bool
    fixed_point: Fraction | None
    is_nonzero_translation: bool


@dataclass(frozen=True)
class ConjugacyReport:
    source_profile: AffineInvariantProfile
    target_profile: AffineInvariantProfile
    expected_target_fixed_point: Fraction | None
    fixed_point_covariant: bool
    conjugate: bool
    status: str


def discover_affine_invariants(
    transformation: AffineRelationConcept,
) -> AffineInvariantProfile:
    """Extract exact conjugacy invariants for f(x)=a*x+b."""
    a, b = transformation.slope, transformation.intercept
    identity = a == 1 and b == 0
    nonzero_translation = a == 1 and b != 0
    has_fixed_point = a != 1
    fixed_point = b / (1 - a) if has_fixed_point else None
    return AffineInvariantProfile(
        multiplier=a,
        is_identity=identity,
        has_unique_fixed_point=has_fixed_point,
        fixed_point=fixed_point,
        is_nonzero_translation=nonzero_translation,
    )


def conjugate_affine_transformation(
    transformation: AffineRelationConcept,
    coordinates: AffineCoordinateMap,
) -> AffineRelationConcept:
    """Return phi o f o phi^-1 for phi(x)=s*x+t."""
    s, t = coordinates.scale, coordinates.offset
    a, b = transformation.slope, transformation.intercept
    return AffineRelationConcept(a, s * b + t * (1 - a))


def verify_affine_conjugacy(
    source: AffineRelationConcept,
    target: AffineRelationConcept,
    coordinates: AffineCoordinateMap,
) -> ConjugacyReport:
    """Verify target = phi o source o phi^-1 and its invariant consequences."""
    expected = conjugate_affine_transformation(source, coordinates)
    source_profile = discover_affine_invariants(source)
    target_profile = discover_affine_invariants(target)
    expected_fixed = (
        coordinates.forward(source_profile.fixed_point)
        if source_profile.fixed_point is not None else None
    )
    fixed_covariant = target_profile.fixed_point == expected_fixed
    conjugate = (
        target == expected
        and source_profile.multiplier == target_profile.multiplier
        and source_profile.is_identity == target_profile.is_identity
        and source_profile.is_nonzero_translation == target_profile.is_nonzero_translation
        and source_profile.has_unique_fixed_point == target_profile.has_unique_fixed_point
        and fixed_covariant
    )
    return ConjugacyReport(
        source_profile, target_profile, expected_fixed, fixed_covariant,
        conjugate, "verified_conjugacy" if conjugate else "not_conjugate",
    )
