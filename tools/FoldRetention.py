"""FoldRetention: find the smallest safe residual feature set for an abstraction.

Given a task's must-link and cannot-link pairs, search candidate residual
features for a minimum-cardinality set that separates every required
cannot-link pair without splitting any must-link pair. Exhaustive search is
exact for the finite candidate set, but exponential in its size.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

try:  # Support both script execution and package imports.
    from .FoldConcept import Context, Instance, equivalent
except ImportError:  # pragma: no cover - exercised by direct script execution
    from FoldConcept import Context, Instance, equivalent


@dataclass(frozen=True)
class RetentionPlan:
    task: str
    base_features: tuple[str, ...]
    retained_features: tuple[str, ...]
    final_features: tuple[str, ...]
    separated_pairs: tuple[tuple[str, str], ...]
    impossible_pairs: tuple[tuple[str, str], ...]


def minimum_retention_features(
    instances: Sequence[Instance],
    context: Context,
    candidate_features: Sequence[str],
    must_link_pairs: Sequence[tuple[str, str]],
    cannot_link_pairs: Sequence[tuple[str, str]],
) -> RetentionPlan | None:
    """Return an exact minimum safe feature set, or None if none exists.

    A candidate feature is safe only if it agrees across every must-link
    pair. The selected candidates must collectively distinguish each
    cannot-link pair that the base context currently merges.
    """
    by_id = {item.identifier: item for item in instances}
    if len(by_id) != len(instances):
        raise ValueError("instance identifiers must be unique")
    if len(set(candidate_features)) != len(candidate_features):
        raise ValueError("candidate features must be unique")
    if set(candidate_features) & set(context.relevant_features):
        raise ValueError("candidate features must be residual to the context")

    pairs = tuple(must_link_pairs) + tuple(cannot_link_pairs)
    for left, right in pairs:
        if left not in by_id or right not in by_id:
            raise KeyError(f"unknown instance in pair: {(left, right)}")
    for item in instances:
        for feature in candidate_features:
            item.get(feature)

    required = tuple(
        (a, b) for a, b in cannot_link_pairs
        if equivalent(by_id[a], by_id[b], context)
    )
    if not required:
        return RetentionPlan(
            context.name, context.relevant_features, (), context.relevant_features,
            (), (),
        )

    safe = tuple(
        feature for feature in candidate_features
        if all(by_id[a].get(feature) == by_id[b].get(feature)
               for a, b in must_link_pairs)
    )

    # Encode each required collision as one bit. A safe feature covers the
    # collisions it separates, reducing the search to exact set cover.
    coverage = tuple(
        sum(1 << i for i, (a, b) in enumerate(required)
            if by_id[a].get(feature) != by_id[b].get(feature))
        for feature in safe
    )
    full = (1 << len(required)) - 1
    useful = tuple(i for i, mask in enumerate(coverage) if mask)
    best: tuple[int, ...] | None = None
    visited: set[tuple[int, int]] = set()

    def search(chosen_mask: int, covered: int) -> None:
        nonlocal best
        chosen_count = chosen_mask.bit_count()
        if covered == full:
            selected = tuple(i for i in useful if chosen_mask & (1 << i))
            if best is None or (len(selected), selected) < (len(best), best):
                best = selected
            return
        if best is not None and chosen_count >= len(best):
            return
        state = (chosen_mask, covered)
        if state in visited:
            return
        visited.add(state)

        uncovered = full & ~covered
        # A valid lower bound: even the feature with maximum new coverage
        # would need at least this many additional selections.
        max_gain = max(
            ((coverage[i] & uncovered).bit_count()
             for i in useful if not chosen_mask & (1 << i)),
            default=0,
        )
        if max_gain == 0:
            return
        lower_bound = (uncovered.bit_count() + max_gain - 1) // max_gain
        if best is not None and chosen_count + lower_bound > len(best):
            return

        # Branch on the hardest uncovered collision (fewest available
        # features). Every valid cover must choose one of these features.
        options_by_pair = []
        bit = 1
        while bit <= full:
            if uncovered & bit:
                options = tuple(
                    i for i in useful
                    if not chosen_mask & (1 << i) and coverage[i] & bit
                )
                if not options:
                    return
                options_by_pair.append(options)
            bit <<= 1
        options = min(options_by_pair, key=lambda group: (len(group), group))
        for i in options:
            search(chosen_mask | (1 << i), covered | coverage[i])

    search(0, 0)
    if best is not None:
        selected = tuple(safe[i] for i in best)
        separated = required
        final = context.relevant_features + selected
        return RetentionPlan(
            context.name, context.relevant_features, selected, final,
            separated, (),
        )

    return None


def verify_retention_plan(
    instances: Sequence[Instance],
    plan: RetentionPlan,
    must_link_pairs: Sequence[tuple[str, str]],
    cannot_link_pairs: Sequence[tuple[str, str]],
) -> bool:
    """Independently check that the final projection satisfies all constraints."""
    by_id = {item.identifier: item for item in instances}
    if len(by_id) != len(instances):
        return False
    context = Context(plan.task, plan.final_features)
    try:
        for a, b in must_link_pairs:
            if not equivalent(by_id[a], by_id[b], context):
                return False
        for a, b in cannot_link_pairs:
            if equivalent(by_id[a], by_id[b], context):
                return False
    except (KeyError, ValueError):
        return False
    return True


def _self_test() -> None:
    items = (
        Instance.make("a", {"shape": "round", "colour": "red",
                            "material": "rubber", "weight": 1}),
        Instance.make("b", {"shape": "round", "colour": "blue",
                            "material": "rubber", "weight": 1}),
        Instance.make("c", {"shape": "round", "colour": "red",
                            "material": "metal", "weight": 2}),
        Instance.make("d", {"shape": "round", "colour": "red",
                            "material": "cardboard", "weight": 3}),
        Instance.make("e", {"shape": "round", "colour": "red",
                            "material": "rubber", "weight": 9}),
    )
    base = Context("object-task", ("shape",))
    must = (("a", "e"),)
    cannot = (("a", "b"), ("a", "d"))
    plan = minimum_retention_features(
        items, base, ("colour", "material", "weight"), must, cannot
    )
    assert plan is not None
    assert plan.retained_features == ("colour", "material")
    assert verify_retention_plan(items, plan, must, cannot)

    # One feature is insufficient: colour splits a/b but not a/d; material
    # splits a/d but not a/b. The minimum safe set therefore has size two.
    assert len(plan.retained_features) == 2

    # A candidate that splits a must-link pair is unsafe and cannot be used.
    impossible = minimum_retention_features(
        items, base, ("colour", "weight"), must, (("a", "b"), ("a", "d"))
    )
    assert impossible is None

    already_separated = minimum_retention_features(
        items, Context("shape-colour", ("shape", "colour")),
        ("material", "weight"), must, (("a", "b"),)
    )
    assert already_separated is not None
    assert already_separated.retained_features == ()

    print("PASS  minimum safe residual feature set is exact")
    print("PASS  must-link pairs remain equivalent")
    print("PASS  cannot-link collisions are separated")
    print("PASS  unsafe residual feature is rejected")
    print("PASS  already-separated pairs need no extra memory")
    print("5/5 checks passed")


if __name__ == "__main__":
    _self_test()
