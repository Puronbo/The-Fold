"""Complete regular-pencil strict-equivalence profiles from both Smith charts."""
from __future__ import annotations

from typing import Sequence

from tools.pencil_smith import rectangular_pencil_smith_profile
from tools.rectangular_pencil import _validate_pair


def _degree(poly):
    if not poly or all(int(x) == 0 for x in poly):
        return -1
    return max(i for i, value in enumerate(poly) if int(value) != 0)


def _chart_signature(chart):
    return [
        [int(x) for x in factor]
        for factor in chart["smith_invariant_factors_low_degree_first"]
    ]


def regular_pencil_complete_profile(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
    *,
    max_minors: int = 2000,
) -> dict:
    """Return complete regular-pencil data when Q+tK is regular.

    For a regular square pencil, the Smith factors of Q+tK encode all
    finite elementary divisors. The Smith factors of K+tQ encode the
    elementary divisors at infinity. Together these determine the regular
    pencil up to constant strict equivalence over F_p.
    """
    rows, cols = _validate_pair(q, k, p)
    if rows != cols:
        raise ValueError("complete regular-pencil classification requires square matrices")
    smith = rectangular_pencil_smith_profile(q, k, p, max_minors=max_minors)
    finite = smith["finite_chart"]
    infinity = smith["infinity_chart"]
    n = rows
    finite_rank = finite["normal_rank_over_rational_function_field"]
    infinity_rank = infinity["normal_rank_over_rational_function_field"]
    if finite_rank != n or infinity_rank != n:
        raise ValueError("pencil is singular: determinant polynomial is identically zero")

    finite_factors = _chart_signature(finite)
    infinity_factors = _chart_signature(infinity)
    finite_degree = sum(_degree(poly) for poly in finite_factors)
    infinity_degree = sum(_degree(poly) for poly in infinity_factors)
    degree_sum = finite_degree + infinity_degree
    if degree_sum != n:
        raise ArithmeticError(
            "regular-pencil degree check failed: finite and infinity "
            "elementary-divisor degrees must sum to the pencil dimension"
        )
    return {
        "schema": "the-fold-regular-pencil-complete-profile-v1",
        "field": f"F_{p}",
        "dimension": n,
        "finite_elementary_divisor_invariant_factors_low_degree_first": finite_factors,
        "infinity_elementary_divisor_invariant_factors_low_degree_first": infinity_factors,
        "finite_degree_sum": finite_degree,
        "infinity_degree_sum": infinity_degree,
        "total_elementary_divisor_degree": degree_sum,
        "checks": {
            "finite_chart_normal_rank_is_full": finite_rank == n,
            "infinity_chart_normal_rank_is_full": infinity_rank == n,
            "finite_plus_infinity_degree_equals_dimension": degree_sum == n,
        },
        "complete_regular_strict_equivalence_invariant": True,
        "classification_statement": (
            "For regular square pencils over F_p, equality of both the "
            "finite and infinity Smith invariant-factor lists is equivalent "
            "to constant strict equivalence of the ordered coefficient pairs."
        ),
        "scope": (
            "Regular pencils only. The result classifies under constant "
            "strict equivalence over the base field; it does not identify "
            "pencils under GL_2 changes mixing their two coefficients and "
            "does not construct explicit equivalence witnesses."
        ),
    }


def compare_regular_pencils_complete(
    q_a: Sequence[Sequence[int]], k_a: Sequence[Sequence[int]],
    q_b: Sequence[Sequence[int]], k_b: Sequence[Sequence[int]],
    p: int, *, max_minors: int = 2000,
) -> dict:
    """Decide strict equivalence of two regular square pencils over F_p."""
    left = regular_pencil_complete_profile(q_a, k_a, p, max_minors=max_minors)
    right = regular_pencil_complete_profile(q_b, k_b, p, max_minors=max_minors)
    finite_equal = (
        left["finite_elementary_divisor_invariant_factors_low_degree_first"]
        == right["finite_elementary_divisor_invariant_factors_low_degree_first"]
    )
    infinity_equal = (
        left["infinity_elementary_divisor_invariant_factors_low_degree_first"]
        == right["infinity_elementary_divisor_invariant_factors_low_degree_first"]
    )
    return {
        "schema": "the-fold-regular-pencil-complete-comparison-v1",
        "field": f"F_{p}",
        "decision_complete": True,
        "strictly_equivalent": finite_equal and infinity_equal,
        "finite_elementary_divisors_equal": finite_equal,
        "infinity_elementary_divisors_equal": infinity_equal,
        "left_profile": left,
        "right_profile": right,
        "comparison_basis": (
            "simultaneous equality of finite Smith invariant factors of "
            "Q+tK and infinity Smith invariant factors of K+tQ"
        ),
    }
