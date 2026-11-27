"""FoldRetention: find the smallest safe residual feature set for an abstraction.

Given a task's must-link and cannot-link pairs, search candidate residual
features for a minimum-cardinality set that separates every required
cannot-link pair without splitting any must-link pair. Branch-and-bound search is exact for the finite candidate set, but can be
exponential in its size.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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
    lower_bound_pairs: tuple[tuple[str, str], ...] = ()
    dual_denominator: int = 0
    dual_weights: tuple[tuple[int, int], ...] = ()



def _maximum_fractional_dual(
    coverage: Sequence[int],
    useful: Sequence[int],
    collision_count: int,
) -> tuple[Fraction, ...]:
    """Solve the set-cover dual exactly with a Bland-rule rational simplex."""
    variable_count = collision_count
    constraint_count = len(useful)
    if variable_count == 0:
        return ()
    if constraint_count == 0:
        return tuple(Fraction(0) for _ in range(variable_count))

    tableau: list[list[Fraction]] = []
    for row_index, feature_index in enumerate(useful):
        row = [
            Fraction(1 if coverage[feature_index] & (1 << j) else 0)
            for j in range(variable_count)
        ]
        row.extend(
            Fraction(1 if slack_index == row_index else 0)
            for slack_index in range(constraint_count)
        )
        row.append(Fraction(1))
        tableau.append(row)

    tableau.append(
        [Fraction(-1) for _ in range(variable_count)]
        + [Fraction(0) for _ in range(constraint_count + 1)]
    )
    basis = [variable_count + i for i in range(constraint_count)]
    column_count = variable_count + constraint_count

    while True:
        entering = next(
            (j for j in range(column_count) if tableau[-1][j] < 0),
            None,
        )
        if entering is None:
            break
        eligible = [
            (tableau[i][-1] / tableau[i][entering], basis[i], i)
            for i in range(constraint_count)
            if tableau[i][entering] > 0
        ]
        if not eligible:
            raise ValueError("fractional dual is unbounded; a collision is uncovered")
        _, _, leaving = min(eligible)
        pivot = tableau[leaving][entering]
        tableau[leaving] = [value / pivot for value in tableau[leaving]]
        for i in range(constraint_count + 1):
            if i == leaving:
                continue
            factor = tableau[i][entering]
            if factor:
                tableau[i] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(tableau[i], tableau[leaving])
                ]
        basis[leaving] = entering

    solution = [Fraction(0) for _ in range(variable_count)]
    for i, basic_variable in enumerate(basis):
        if basic_variable < variable_count:
            solution[basic_variable] = tableau[i][-1]
    return tuple(solution)


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
    dual_denominator = max((mask.bit_count() for mask in coverage), default=0)

    # Checkable packing lower bound: no safe feature covers two packed pairs.
    coverers = tuple(
        frozenset(i for i in useful if coverage[i] & (1 << j))
        for j in range(len(required))
    )
    packing: list[int] = []
    used_coverers: set[int] = set()
    for j in sorted(range(len(required)), key=lambda k: (len(coverers[k]), k)):
        if coverers[j] and not (used_coverers & coverers[j]):
            packing.append(j)
            used_coverers.update(coverers[j])

    # Solve the fractional set-cover dual exactly over safe features.
    best_dual = _maximum_fractional_dual(coverage, useful, len(required))
    dual_weights = tuple((weight.numerator, weight.denominator) for weight in best_dual)

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
            separated, (), tuple(required[j] for j in packing), dual_denominator, dual_weights,
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



def verify_optimality_certificate(
    instances: Sequence[Instance],
    context: Context,
    candidate_features: Sequence[str],
    must_link_pairs: Sequence[tuple[str, str]],
    cannot_link_pairs: Sequence[tuple[str, str]],
    plan: RetentionPlan,
) -> bool:
    """Verify a packing lower bound; equality with plan size proves optimality."""
    by_id = {item.identifier: item for item in instances}
    if len(by_id) != len(instances):
        return False
    try:
        safe = tuple(
            feature for feature in candidate_features
            if all(by_id[a].get(feature) == by_id[b].get(feature)
                   for a, b in must_link_pairs)
        )
        required = tuple(
            (a, b) for a, b in cannot_link_pairs
            if equivalent(by_id[a], by_id[b], context)
        )
        certificate = plan.lower_bound_pairs
        if plan.separated_pairs != required or len(set(certificate)) != len(certificate):
            return False
        if any(pair not in required for pair in certificate):
            return False
        coverers = [
            {feature for feature in safe
             if by_id[a].get(feature) != by_id[b].get(feature)}
            for a, b in certificate
        ]
        if any(not group for group in coverers):
            return False
        packing_valid = all(
            not (left & right)
            for i, left in enumerate(coverers)
            for right in coverers[i + 1:]
        )
        # Uniform rational dual: weight 1/D per required collision, where
        # D is the maximum number any safe feature can cover.
        all_coverage = [
            sum(by_id[a].get(feature) != by_id[b].get(feature)
                for a, b in required)
            for feature in safe
        ]
        denominator = max(all_coverage, default=0)
        if not required:
            return (
                not certificate and plan.dual_denominator == 0
                and not plan.dual_weights
            )
        if denominator == 0 or plan.dual_denominator != denominator:
            return False
        if len(plan.dual_weights) != len(required):
            return False
        weights = tuple(Fraction(n, d) for n, d in plan.dual_weights)
        if any(weight < 0 for weight in weights):
            return False
        # Dual feasibility: for each safe feature, the weights of all
        # collisions it separates sum to at most one.
        dual_feasible = all(
            sum(
                (weights[j] for j, (a, b) in enumerate(required)
                 if by_id[a].get(feature) != by_id[b].get(feature)),
                Fraction(0),
            ) <= 1
            for feature in safe
        )
        return packing_valid and dual_feasible
    except (KeyError, ValueError, ZeroDivisionError):
        return False


def retention_plan_proves_optimality(
    instances: Sequence[Instance],
    context: Context,
    candidate_features: Sequence[str],
    must_link_pairs: Sequence[tuple[str, str]],
    cannot_link_pairs: Sequence[tuple[str, str]],
    plan: RetentionPlan,
) -> bool:
    """A feasible plan plus matching packing/dual bounds certifies minimum."""
    if any(denominator <= 0 for _, denominator in plan.dual_weights):
        return False
    by_id = {item.identifier: item for item in instances}
    required_count = sum(
        1 for a, b in cannot_link_pairs
        if a in by_id and b in by_id and equivalent(by_id[a], by_id[b], context)
    )
    uniform_bound = (
        (required_count + plan.dual_denominator - 1) // plan.dual_denominator
        if plan.dual_denominator else 0
    )
    dual_sum = sum(
        (Fraction(n, d) for n, d in plan.dual_weights), Fraction(0)
    )
    weighted_bound = (
        (dual_sum.numerator + dual_sum.denominator - 1) // dual_sum.denominator
        if dual_sum else 0
    )
    return (
        verify_retention_plan(instances, plan, must_link_pairs, cannot_link_pairs)
        and verify_optimality_certificate(
            instances, context, candidate_features,
            must_link_pairs, cannot_link_pairs, plan,
        )
        and max(len(plan.lower_bound_pairs), uniform_bound, weighted_bound) == len(plan.retained_features)
    )


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
    assert retention_plan_proves_optimality(
        items, base, ("colour", "material", "weight"), must, cannot, plan
    )
    assert len(plan.lower_bound_pairs) == 2
    assert plan.dual_denominator == 1
    assert len(plan.dual_weights) == len(plan.separated_pairs)
    assert sum((Fraction(n, d) for n, d in plan.dual_weights), Fraction(0)) == 2

    # One feature is insufficient: colour splits a/b but not a/d; material
    # splits a/d but not a/b. The minimum safe set therefore has size two.
    assert len(plan.retained_features) == 2

    # Nonuniform rational weights improve the dual objective when one
    # collision has fewer available separating features.
    weighted_items = (
        Instance.make("w0", {"shape": "round", "f1": 0, "f2": 0, "f3": 0, "f4": 0}),
        Instance.make("w1", {"shape": "round", "f1": 1, "f2": 1, "f3": 0, "f4": 0}),
        Instance.make("w2", {"shape": "round", "f1": 1, "f2": 0, "f3": 1, "f4": 0}),
        Instance.make("w3", {"shape": "round", "f1": 0, "f2": 0, "f3": 0, "f4": 1}),
    )
    weighted_plan = minimum_retention_features(
        weighted_items, base, ("f1", "f2", "f3", "f4"), (),
        (("w0", "w1"), ("w0", "w2"), ("w0", "w3")),
    )
    assert weighted_plan is not None
    weighted_objective = sum(
        (Fraction(n, d) for n, d in weighted_plan.dual_weights), Fraction(0)
    )
    assert weighted_objective == 2
    assert retention_plan_proves_optimality(
        weighted_items, base, ("f1", "f2", "f3", "f4"), (),
        (("w0", "w1"), ("w0", "w2"), ("w0", "w3")), weighted_plan
    )

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
    print("PASS  packing certificate proves the two-feature optimum")
    print("PASS  rational dual bound independently matches the optimum")
    print("PASS  nonuniform rational weights certify a weighted optimum")
    print("8/8 checks passed")


if __name__ == "__main__":
    _self_test()
