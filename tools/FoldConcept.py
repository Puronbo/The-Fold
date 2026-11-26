"""FoldConcept: a minimal, auditable task-relative concept learner.

This is a symbolic prototype, not a general learner or an AGI system.
It groups records by explicitly selected features, retains full source
records as residual information, checks the induced equivalence relation,
and can refine a context when a counterexample exposes a missing feature.

Run:
    python tools/FoldConcept.py
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product
from typing import Iterable, Mapping, Sequence


FeatureValue = str | int | float | bool | None


@dataclass(frozen=True)
class Instance:
    """An observation with a stable identifier, features, and provenance."""
    identifier: str
    features: tuple[tuple[str, FeatureValue], ...]
    provenance: str = "unspecified"

    @classmethod
    def make(
        cls, identifier: str, features: Mapping[str, FeatureValue],
        provenance: str = "unspecified",
    ) -> "Instance":
        if not identifier:
            raise ValueError("identifier must be nonempty")
        return cls(identifier, tuple(sorted(features.items())), provenance)

    def get(self, name: str) -> FeatureValue:
        values = dict(self.features)
        if name not in values:
            raise KeyError(f"{self.identifier} lacks feature {name!r}")
        return values[name]


@dataclass(frozen=True)
class Context:
    """Features that matter for one declared task."""
    name: str
    relevant_features: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("context name must be nonempty")
        if len(set(self.relevant_features)) != len(self.relevant_features):
            raise ValueError("relevant features must be unique")


@dataclass(frozen=True)
class Concept:
    context: str
    signature: tuple[tuple[str, FeatureValue], ...]
    members: tuple[str, ...]


@dataclass(frozen=True)
class ConceptView:
    """A concept label plus the untouched source record (the residual)."""
    concept: Concept
    source: Instance
    discarded_features: tuple[str, ...]


def signature(instance: Instance, context: Context) -> tuple[tuple[str, FeatureValue], ...]:
    return tuple((name, instance.get(name)) for name in context.relevant_features)


def equivalent(a: Instance, b: Instance, context: Context) -> bool:
    """Task-relative equivalence induced by equality of projected signatures."""
    return signature(a, context) == signature(b, context)


def check_equivalence_laws(
    instances: Sequence[Instance], context: Context
) -> bool:
    """Exhaustively check reflexivity, symmetry, and transitivity on a finite set."""
    for a in instances:
        if not equivalent(a, a, context):
            return False
    for a, b in product(instances, repeat=2):
        if equivalent(a, b, context) != equivalent(b, a, context):
            return False
    for a, b, c in product(instances, repeat=3):
        if equivalent(a, b, context) and equivalent(b, c, context):
            if not equivalent(a, c, context):
                return False
    return True


def build_concepts(
    instances: Sequence[Instance], context: Context
) -> tuple[Concept, ...]:
    """Build quotient classes; retain source instances separately in ConceptView."""
    buckets: dict[tuple[tuple[str, FeatureValue], ...], list[str]] = {}
    for item in instances:
        key = signature(item, context)
        buckets.setdefault(key, []).append(item.identifier)
    return tuple(
        Concept(context.name, key, tuple(sorted(ids)))
        for key, ids in sorted(buckets.items(), key=lambda pair: repr(pair[0]))
    )


def views_for(
    instances: Sequence[Instance], context: Context
) -> tuple[ConceptView, ...]:
    concepts = build_concepts(instances, context)
    by_member = {
        member: concept for concept in concepts for member in concept.members
    }
    views = []
    for item in instances:
        discarded = tuple(
            name for name, _ in item.features
            if name not in context.relevant_features
        )
        views.append(ConceptView(by_member[item.identifier], item, discarded))
    return tuple(views)


def refine_context(
    context: Context, a: Instance, b: Instance, feature: str
) -> Context:
    """Add a feature that separates a counterexample pair.

    The pair must currently be equivalent and must differ on the new feature.
    """
    if not equivalent(a, b, context):
        raise ValueError("counterexample pair is already separated")
    if feature in context.relevant_features:
        raise ValueError("feature is already relevant")
    if a.get(feature) == b.get(feature):
        raise ValueError("proposed feature does not separate the pair")
    return replace(
        context,
        relevant_features=context.relevant_features + (feature,),
    )


def main() -> None:
    samples = (
        Instance.make("m1", {"length_mm": 1000, "colour": "red"}, "sensor-A"),
        Instance.make("m2", {"length_mm": 1000, "colour": "blue"}, "sensor-B"),
        Instance.make("cm1", {"length_mm": 1000, "colour": "green"}, "sensor-C"),
        Instance.make("short", {"length_mm": 500, "colour": "red"}, "sensor-D"),
    )
    length_task = Context("compare-length", ("length_mm",))
    colour_task = Context("compare-colour", ("colour",))
    checks: list[tuple[str, bool]] = []

    length_views = views_for(samples, length_task)
    colour_concepts = build_concepts(samples, colour_task)
    checks.append(("same length, different colour share a length concept",
                   length_views[0].concept == length_views[1].concept))
    checks.append(("colour task keeps those records distinct",
                   len(colour_concepts) == 4))
    checks.append(("the original colour survives as residual information",
                   length_views[0].source.get("colour") == "red"
                   and "colour" in length_views[0].discarded_features))
    checks.append(("finite projected relation is an equivalence",
                   check_equivalence_laws(samples, length_task)))
    checks.append(("quotient has two length classes",
                   len(build_concepts(samples, length_task)) == 2))

    refined = refine_context(length_task, samples[0], samples[1], "colour")
    checks.append(("counterexample refines the task context",
                   not equivalent(samples[0], samples[1], refined)))
    checks.append(("refinement preserves the old feature",
                   refined.relevant_features[0] == "length_mm"))
    try:
        refine_context(length_task, samples[0], samples[1], "length_mm")
        ineffective_feature_rejected = False
    except ValueError:
        ineffective_feature_rejected = True
    checks.append(("non-separating feature is rejected",
                   ineffective_feature_rejected))

    # New observations are classified by the same declared rule.
    new_item = Instance.make("new", {"length_mm": 1000, "colour": "black"})
    checks.append(("held-out instance maps to an existing length concept",
                   signature(new_item, length_task) in {
                       concept.signature for concept in build_concepts(samples, length_task)
                   }))

    failed = [name for name, passed in checks if not passed]
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    if failed:
        raise SystemExit("failed checks: " + ", ".join(failed))


if __name__ == "__main__":
    main()
