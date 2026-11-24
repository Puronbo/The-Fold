"""Assemble regular Smith data and singular minimal indices for a pencil."""
from __future__ import annotations
from typing import Sequence
from tools.pencil_minimal_indices import rectangular_pencil_minimal_indices
from tools.pencil_smith import rectangular_pencil_smith_profile
from tools.rectangular_pencil import _validate_pair

def _degree(poly):
    if not poly or all(int(x) == 0 for x in poly): return 0
    i = len(poly) - 1
    while i > 0 and int(poly[i]) == 0: i -= 1
    return i

def _chart_degree(chart):
    return sum(_degree(poly) for poly in chart["smith_invariant_factors_low_degree_first"])

def rectangular_pencil_kronecker_profile(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Assemble finite/infinity elementary divisors and both minimal-index lists."""
    rows, cols = _validate_pair(q, k, p)
    smith = rectangular_pencil_smith_profile(q, k, p, max_minors=max_minors)
    indices = rectangular_pencil_minimal_indices(q, k, p,
        max_degree=max_degree, max_minors=max_minors)
    normal_rank = smith["finite_chart"]["normal_rank_over_rational_function_field"]
    right, left = indices["right"]["minimal_indices"], indices["left"]["minimal_indices"]
    finite_degree, infinity_degree = _chart_degree(smith["finite_chart"]), _chart_degree(smith["infinity_chart"])
    recovered = indices["complete"]
    regular_dimension = normal_rank - sum(right or []) - sum(left or [])
    dimensions_match = (
        regular_dimension >= 0
        and rows == regular_dimension + sum(right or []) + sum(e + 1 for e in (left or []))
        and cols == regular_dimension + sum(e + 1 for e in (right or [])) + sum(left or [])
    )
    degree_sum = finite_degree + infinity_degree
    degree_match = regular_dimension == degree_sum
    checks = dimensions_match and degree_match if recovered else None
    return {
        "schema": "the-fold-pencil-kronecker-profile-v1",
        "field": f"F_{p}", "shape": [rows, cols], "pencil": "Q + t K",
        "normal_rank_over_rational_function_field": normal_rank,
        "regular_part": {
            "dimension": regular_dimension if recovered else None,
            "finite_smith_invariant_factors_low_degree_first": smith["finite_chart"]["smith_invariant_factors_low_degree_first"],
            "infinity_reversed_smith_invariant_factors_low_degree_first": smith["infinity_chart"]["smith_invariant_factors_low_degree_first"],
            "finite_elementary_divisor_degree_sum": finite_degree,
            "infinity_elementary_divisor_degree_sum": infinity_degree,
        },
        "singular_part": {
            "right_minimal_indices": right, "left_minimal_indices": left,
            "right_recovery_complete": indices["right"]["complete"],
            "left_recovery_complete": indices["left"]["complete"],
            "right_bounded_nullities": indices["right"]["bounded_polynomial_nullities"],
            "left_bounded_nullities": indices["left"]["bounded_polynomial_nullities"],
        },
        "consistency_checks": {
            "dimension_identities": dimensions_match if recovered else None,
            "regular_dimension_equals_finite_plus_infinity_degree_sum": degree_match if recovered else None,
            "regular_dimension_from_rank_and_minimal_indices": regular_dimension if recovered else None,
            "regular_dimension_from_smith_degrees": degree_sum,
            "all_checks_pass": checks,
        },
        "complete_kronecker_structure_data": recovered and checks is True,
        "scope": "Complete block-size data when checks pass; no unimodular transformation matrices or canonical decomposition are constructed.",
    }
