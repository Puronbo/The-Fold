"""FoldLoop: constraint-guided abstraction and counterexample refinement.

This is a deterministic research prototype, not an autonomous AI or AGI.
A model may propose candidate features and constraints; this module checks
whether the resulting task-relative abstraction satisfies those constraints.
It never executes model-generated code.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from FoldConcept import Context, Instance, equivalent, signature


@dataclass(frozen=True)
class PairConstraint:
    """A pair that must remain together (same=True) or be distinguished."""
    left: str
    right: str
    same: bool
    reason: str = ""


@dataclass(frozen=True)
class Refinement:
    feature: str
    newly_separated: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class LoopResult:
    context: Context
    satisfied: bool
    violations: tuple[PairConstraint, ...]
    refinements: tuple[Refinement, ...]
    unresolved_features: tuple[str, ...]


def audit(
    instances: Sequence[Instance],
    context: Context,
    constraints: Sequence[PairConstraint],
) -> tuple[PairConstraint, ...]:
    """Return constraints violated by the current projection."""
    by_id = {item.identifier: item for item in instances}
    if len(by_id) != len(instances):
        raise ValueError("instance identifiers must be unique")
    violations = []
    for rule in constraints:
        if rule.left not in by_id or rule.right not in by_id:
            raise KeyError(f"unknown instance in constraint: {rule}")
        observed_same = equivalent(by_id[rule.left], by_id[rule.right], context)
        if observed_same != rule.same:
            violations.append(rule)
    return tuple(violations)


def refine_until_consistent(
    instances: Sequence[Instance],
    initial: Context,
    candidate_features: Sequence[str],
    constraints: Sequence[PairConstraint],
) -> LoopResult:
    """Greedily add proposed features while preserving all must-link pairs.

    At each step, choose the feature that separates the largest number of
    currently violated cannot-link pairs without splitting any must-link pair.
    Ties are broken lexicographically. Stop when constraints are satisfied
    or no candidate feature can make progress.
    """
    by_id = {item.identifier: item for item in instances}
    if len(by_id) != len(instances):
        raise ValueError("instance identifiers must be unique")
    for rule in constraints:
        if rule.left not in by_id or rule.right not in by_id:
            raise KeyError(f"unknown instance in constraint: {rule}")
    features = tuple(sorted(set(candidate_features) - set(initial.relevant_features)))
    # Validate feature availability before beginning, avoiding partial results.
    for item in instances:
        for feature in features:
            item.get(feature)

    context = initial
    refinements: list[Refinement] = []
    unresolved: set[str] = set(features)

    while True:
        violations = audit(instances, context, constraints)
        if not violations:
            return LoopResult(context, True, (), tuple(refinements), ())

        cannot_links = [rule for rule in violations if not rule.same]
        best_feature: str | None = None
        best_pairs: tuple[tuple[str, str], ...] = ()

        for feature in sorted(unresolved):
            # A feature is admissible only if it preserves every must-link.
            splits_must_link = any(
                by_id[rule.left].get(feature) != by_id[rule.right].get(feature)
                for rule in constraints if rule.same
            )
            if splits_must_link:
                continue
            separated = tuple(
                (rule.left, rule.right)
                for rule in cannot_links
                if by_id[rule.left].get(feature) != by_id[rule.right].get(feature)
            )
            if len(separated) > len(best_pairs):
                best_feature, best_pairs = feature, separated

        if best_feature is None or not best_pairs:
            return LoopResult(
                context, False, violations, tuple(refinements),
                tuple(sorted(unresolved)),
            )

        context = Context(
            context.name, context.relevant_features + (best_feature,)
        )
        unresolved.remove(best_feature)
        refinements.append(Refinement(best_feature, best_pairs))


def main() -> None:
    items = (
        Instance.make("a", {"shape": "round", "colour": "red", "material": "wood"}),
        Instance.make("b", {"shape": "round", "colour": "blue", "material": "wood"}),
        Instance.make("c", {"shape": "square", "colour": "red", "material": "metal"}),
        Instance.make("d", {"shape": "round", "colour": "red", "material": "wood"}),
    )
    base = Context("object-identity-task", ())
    rules = (
        PairConstraint("a", "b", False, "different labels"),
        PairConstraint("a", "d", True, "same label"),
        PairConstraint("a", "c", False, "different labels"),
    )
    result = refine_until_consistent(
        items, base, ("shape", "colour", "material"), rules
    )
    checks = [
        ("feedback loop reaches a consistent abstraction", result.satisfied),
        ("must-link pair remains together",
         equivalent(items[0], items[3], result.context)),
        ("cannot-link pairs become distinct",
         not equivalent(items[0], items[1], result.context)
         and not equivalent(items[0], items[2], result.context)),
        ("at least one counterexample caused refinement", len(result.refinements) > 0),
        ("refinement log records selected features",
         tuple(r.feature for r in result.refinements) == result.context.relevant_features),
        ("independent audit confirms no violations",
         len(audit(items, result.context, rules)) == 0),
    ]

    # Contradictory constraints must not be silently "solved".
    impossible = rules + (PairConstraint("a", "b", True, "contradicts first rule"),)
    blocked = refine_until_consistent(items, base, ("shape", "colour"), impossible)
    checks.append(("contradictory constraints remain explicitly unresolved",
                   not blocked.satisfied and len(blocked.violations) > 0))

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name}")
    print(f"{sum(p for _, p in checks)}/{len(checks)} checks passed")
    if not all(p for _, p in checks):
        raise SystemExit("FoldLoop regression failure")


if __name__ == "__main__":
    main()
