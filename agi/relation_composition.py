"""Exact composition of proportional, inverse, and affine relations.

Maps use x -> (a*x+b)/(c*x+d), represented by exact rational matrices.
Intermediate domain exclusions are retained even if matrix multiplication
algebraically cancels a denominator factor.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable
from agi.relation_discovery import RelationHypothesis


def _canonical(values: Iterable[Fraction]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    result = tuple(Fraction(value) for value in values)
    if len(result) != 4 or all(value == 0 for value in result):
        raise ValueError("a relation needs four coefficients, not all zero")
    pivot = next(value for value in result if value != 0)
    return tuple(value / pivot for value in result)  # type: ignore[return-value]


@dataclass(frozen=True)
class ComposedRelation:
    coefficients: tuple[Fraction, Fraction, Fraction, Fraction]
    domain_exclusions: tuple[Fraction, ...] = ()
    provenance: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "coefficients", _canonical(self.coefficients))
        object.__setattr__(self, "domain_exclusions",
                           tuple(sorted(set(Fraction(x) for x in self.domain_exclusions))))

    @classmethod
    def from_hypothesis(cls, hypothesis: RelationHypothesis) -> "ComposedRelation":
        if hypothesis.status != "supported_on_supplied_observations":
            raise ValueError("only hypotheses supported on all supplied rows can be composed")
        if hypothesis.relation == "proportional" and len(hypothesis.parameters) == 1:
            a, = hypothesis.parameters
            coeffs = (a, Fraction(0), Fraction(0), Fraction(1))
        elif hypothesis.relation == "inverse" and len(hypothesis.parameters) == 1:
            k, = hypothesis.parameters
            coeffs = (Fraction(0), k, Fraction(1), Fraction(0))
        elif hypothesis.relation == "affine" and len(hypothesis.parameters) == 2:
            a, b = hypothesis.parameters
            coeffs = (a, b, Fraction(0), Fraction(1))
        else:
            raise ValueError("unsupported relation family or parameter shape")
        a, b, c, d = _canonical(coeffs)
        exclusions = () if c == 0 else (-d / c,)
        return cls(coeffs, exclusions, (hypothesis.relation,))

    def evaluate(self, x: Fraction | int) -> Fraction:
        value = Fraction(x)
        if value in self.domain_exclusions:
            raise ZeroDivisionError(f"input {value} is excluded by an intermediate relation")
        a, b, c, d = self.coefficients
        denominator = c * value + d
        if denominator == 0:
            raise ZeroDivisionError(f"relation is undefined at {value}")
        return (a * value + b) / denominator

    def then(self, outer: "ComposedRelation") -> "ComposedRelation":
        """Return outer(self(x)), preserving every intermediate restriction."""
        a, b, c, d = self.coefficients
        e, f, g, h = outer.coefficients
        product = (e*a + f*c, e*b + f*d, g*a + h*c, g*b + h*d)
        exclusions = set(self.domain_exclusions)
        ia, ib, ic, id_ = self.coefficients
        for pole in outer.domain_exclusions:
            slope = ia - pole * ic
            intercept = ib - pole * id_
            if slope == 0:
                if intercept == 0:
                    raise ValueError("outer relation is undefined for every inner output")
            else:
                exclusions.add(-intercept / slope)
        return ComposedRelation(product, tuple(exclusions),
                                 self.provenance + outer.provenance)
