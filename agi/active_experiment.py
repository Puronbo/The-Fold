"""Finite, exact selection of inputs that distinguish candidate relations."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from agi.relation_selection import RelationCandidate


@dataclass(frozen=True)
class Prediction:
    candidate_id: str
    value: Fraction | None
    error: str | None


@dataclass(frozen=True)
class ExperimentOption:
    input_value: Fraction
    predictions: tuple[Prediction, ...]
    defined_candidates: int
    distinct_predictions: int
    pairwise_disagreement: Fraction


@dataclass(frozen=True)
class ExperimentDesign:
    status: str
    selected_input: Fraction | None
    selected_option: ExperimentOption | None
    ranked_options: tuple[ExperimentOption, ...]
    candidate_count: int


def _exact_input(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("experiment inputs must be exact integers or Fractions")
    return Fraction(value)


def _option(value: Fraction, candidates: Sequence[RelationCandidate]) -> ExperimentOption:
    predictions = []
    defined = []
    for candidate in candidates:
        try:
            result = candidate.composed.evaluate(value)
            predictions.append(Prediction(candidate.candidate_id, result, None))
            defined.append(result)
        except ZeroDivisionError as exc:
            predictions.append(Prediction(candidate.candidate_id, None, str(exc)))
    distinct = len(set(defined))
    separation = sum(
        (abs(left - right) for index, left in enumerate(defined)
         for right in defined[index + 1:]),
        Fraction(0),
    )
    return ExperimentOption(value, tuple(predictions), len(defined), distinct, separation)


def design_discriminating_experiment(
    candidates: Sequence[RelationCandidate],
    candidate_inputs: Sequence[int | Fraction],
) -> ExperimentDesign:
    """Rank caller-supplied inputs by exact pairwise prediction disagreement.

    No input is invented or executed. The finite candidate domain is supplied by
    the caller; undefined predictions reduce coverage and are never treated as
    matching predictions. Ties are resolved by coverage, distinct predictions,
    then the smallest numeric input for reproducibility.
    """
    if not candidates:
        raise ValueError("at least one candidate is required")
    ids = [candidate.candidate_id for candidate in candidates]
    if len(ids) != len(set(ids)):
        raise ValueError("candidate IDs must be unique")
    inputs = tuple(_exact_input(value) for value in candidate_inputs)
    if len(inputs) != len(set(inputs)):
        raise ValueError("candidate inputs must be unique")
    options = tuple(_option(value, candidates) for value in inputs)
    informative = [option for option in options
                   if option.defined_candidates >= 2 and option.distinct_predictions >= 2]
    if not informative:
        return ExperimentDesign("no_discriminating_input", None, None, options, len(candidates))
    ranked = tuple(sorted(
        options,
        key=lambda option: (
            option.pairwise_disagreement,
            option.defined_candidates,
            option.distinct_predictions,
            -option.input_value,
        ),
        reverse=True,
    ))
    best = ranked[0]
    if best not in informative:
        best = informative[0]
    return ExperimentDesign("input_selected", best.input_value, best, ranked, len(candidates))
