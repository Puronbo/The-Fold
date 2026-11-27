"""Orbit quotients for finite group actions, with exact relation descent checks."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Sequence

from agi.symmetry_actions import analyze_finite_group_action


@dataclass(frozen=True)
class OrbitQuotientReport:
    valid_group_action: bool
    status: str
    equivalence_classes: tuple[tuple[Hashable, ...], ...]
    representatives: tuple[Hashable, ...]
    state_to_class: tuple[tuple[Hashable, int], ...]
    class_sizes: tuple[int, ...]
    original_state_count: int
    quotient_state_count: int
    information_collapsed: int
    canonicalization: str
    diagonal_relation_invariant: bool | None
    quotient_relation_well_defined: bool | None
    quotient_relation: tuple[tuple[int, int], ...] | None


def construct_orbit_quotient(
    states: Sequence[Hashable],
    transformations: Sequence[tuple[str, Sequence[int]]],
    relation: Sequence[tuple[Hashable, Hashable]] | None = None,
) -> OrbitQuotientReport:
    """Construct X/G and, only when valid, descend a supplied binary relation.

    Class indices follow the first occurrence of each orbit in the supplied
    state order. Representatives are the first supplied state in each orbit;
    this is a deterministic convention, not an intrinsic canonical form.

    Diagonal invariance applies the same group element to both relation
    endpoints. Relation descent is checked more strongly: membership must be
    constant on every product of two orbits.
    """
    state_values = tuple(states)
    analysis = analyze_finite_group_action(state_values, transformations, relation)
    n = len(state_values)
    if not analysis.is_group_action:
        return OrbitQuotientReport(
            False, analysis.status, (), (), (), (), n, 0, 0,
            "not_constructed", analysis.relation_preserved_by_all, None, None,
        )

    position = {state: i for i, state in enumerate(state_values)}
    classes = tuple(
        tuple(sorted(orbit, key=position.__getitem__))
        for orbit in analysis.orbits
    )
    representatives = tuple(orbit[0] for orbit in classes)
    state_to_class = tuple(
        (state, class_index)
        for class_index, orbit in enumerate(classes)
        for state in orbit
    )
    class_sizes = tuple(len(orbit) for orbit in classes)

    diagonal_invariant = analysis.relation_preserved_by_all
    quotient_relation = None
    quotient_well_defined = None
    status = "orbit_quotient_constructed"

    if relation is not None:
        relation_set = set(relation)
        quotient_pairs = []
        well_defined = True
        for i, left_orbit in enumerate(classes):
            for j, right_orbit in enumerate(classes):
                memberships = {
                    (left, right) in relation_set
                    for left in left_orbit
                    for right in right_orbit
                }
                if len(memberships) != 1:
                    well_defined = False
                elif True in memberships:
                    quotient_pairs.append((i, j))
        quotient_well_defined = well_defined
        if well_defined:
            quotient_relation = tuple(quotient_pairs)
            status = "orbit_quotient_and_relation_descent_verified"
        else:
            status = "orbit_quotient_constructed_relation_not_well_defined"

    return OrbitQuotientReport(
        True, status, classes, representatives, state_to_class, class_sizes,
        n, len(classes), n - len(classes),
        "first state in each orbit under supplied state order",
        diagonal_invariant, quotient_well_defined, quotient_relation,
    )
