"""Finite permutation-group actions, orbits, stabilizers, and invariant relations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Sequence


@dataclass(frozen=True)
class SymmetryActionReport:
    is_group_action: bool
    status: str
    orbits: tuple[tuple[Hashable, ...], ...]
    stabilizers: tuple[tuple[Hashable, tuple[str, ...]], ...]
    relation_preserved_by_all: bool | None
    relation_violations: tuple[tuple[str, tuple[Hashable, Hashable]], ...]
    state_count: int
    transformation_count: int


def _validate_permutation(key: str, image: Sequence[int], size: int) -> tuple[int, ...]:
    if not isinstance(key, str) or not key.strip():
        raise ValueError("transformation keys must be non-empty strings")
    result = tuple(image)
    if len(result) != size or any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0 or value >= size
        for value in result
    ):
        raise ValueError("each permutation must map every state index into the finite state set")
    if len(set(result)) != size:
        raise ValueError("each transformation must be a bijection")
    return result


def analyze_finite_group_action(
    states: Sequence[Hashable],
    transformations: Sequence[tuple[str, Sequence[int]]],
    relation: Sequence[tuple[Hashable, Hashable]] | None = None,
) -> SymmetryActionReport:
    """Analyze an explicitly supplied finite permutation group acting on states.

    Permutations are tuples of destination indices: image[i] is the image of
    states[i]. The transformation collection must itself form a group.
    An optional binary relation is checked for preservation by every element.
    """
    state_values = tuple(states)
    if not state_values:
        raise ValueError("state set must be non-empty")
    try:
        unique_states = set(state_values)
    except TypeError as exc:
        raise TypeError("states must be hashable") from exc
    if len(unique_states) != len(state_values):
        raise ValueError("states must be unique")
    n = len(state_values)

    keys = [key for key, _ in transformations]
    if any(not isinstance(key, str) or not key.strip() for key in keys):
        raise ValueError("transformation keys must be non-empty strings")
    if len(keys) != len(set(keys)):
        raise ValueError("transformation keys must be unique")
    perms = [(key, _validate_permutation(key, image, n)) for key, image in transformations]
    signatures = [image for _, image in perms]
    if len(signatures) != len(set(signatures)):
        raise ValueError("duplicate permutations must have one canonical key")

    identity = tuple(range(n))
    by_image = {image: key for key, image in perms}
    if identity not in by_image or not perms:
        return SymmetryActionReport(
            False, "not_a_group_action", (), (), None, (), n, len(perms)
        )

    closure = True
    for _, left in perms:
        for _, right in perms:
            composed = tuple(left[right[i]] for i in range(n))
            if composed not in by_image:
                closure = False
                break
        if not closure:
            break
    if not closure:
        return SymmetryActionReport(
            False, "transformations_not_closed_under_composition", (), (), None, (), n, len(perms)
        )

    # A finite nonempty set of permutations containing identity and closed
    # under composition is a group; inverses follow from finiteness.
    unseen = set(range(n))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit_indices = {image[seed] for _, image in perms}
        # Since the supplied transformations form a group, this is the full orbit.
        ordered = tuple(state_values[i] for i in sorted(orbit_indices))
        orbits.append(ordered)
        unseen.difference_update(orbit_indices)

    stabilizers = tuple(
        (state_values[i], tuple(key for key, image in perms if image[i] == i))
        for i in range(n)
    )

    preserved = None
    violations = []
    if relation is not None:
        relation_set = set(relation)
        if any(a not in unique_states or b not in unique_states for a, b in relation_set):
            raise ValueError("relation endpoints must belong to the state set")
        preserved = True
        for key, image in perms:
            for a, b in relation_set:
                ia, ib = state_values.index(a), state_values.index(b)
                mapped_pair = (state_values[image[ia]], state_values[image[ib]])
                if mapped_pair not in relation_set:
                    preserved = False
                    violations.append((key, mapped_pair))

    return SymmetryActionReport(
        True, "finite_group_action_verified", tuple(orbits), stabilizers,
        preserved, tuple(violations), n, len(perms),
    )
