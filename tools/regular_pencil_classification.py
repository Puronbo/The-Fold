"""Complete regular-pencil strict-equivalence profiles from finite/infinity divisors."""
from __future__ import annotations

from typing import Sequence

from tools.pencil_smith import rectangular_pencil_smith_profile
from tools.rectangular_pencil import _validate_pair


def _trim(poly):
    out = [int(x) for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def _degree(poly):
    value = _trim(poly)
    return -1 if value == [0] else len(value) - 1


def _t_valuation(poly):
    value = _trim(poly)
    if value == [0]:
        raise ValueError("zero cannot be a nonzero Smith invariant factor")
    count = 0
    while count < len(value) and value[count] == 0:
        count += 1
    return count


def _chart_signature(chart):
    return [_trim(factor) for factor in
            chart["smith_invariant_factors_low_degree_first"]]


def regular_pencil_complete_profile(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
    *,
    max_minors: int = 2000,
) -> dict:
    """Classify a regular square pencil under constant strict equivalence.

    Finite elementary divisors are encoded by the complete Smith invariant
    factors of Q+tK. Infinite elementary divisors are exactly the powers of
    t dividing the Smith invariant factors of K+tQ (not the full reversed
    polynomials). These two collections form the regular Kronecker data.
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
    reversed_factors = _chart_signature(infinity)
    infinity_blocks = sorted(
        (valuation for valuation in (_t_valuation(poly) for poly in reversed_factors)
         if valuation > 0)
    )
    finite_degree = sum(_degree(poly) for poly in finite_factors)
    infinity_degree = sum(infinity_blocks)
    degree_sum = finite_degree + infinity_degree
    if degree_sum != n:
        raise ArithmeticError(
            "regular-pencil degree check failed: finite elementary-divisor "
            "degrees plus infinity block sizes must equal the dimension"
        )
    return {
        "schema": "the-fold-regular-pencil-complete-profile-v2",
        "field": f"F_{p}",
        "dimension": n,
        "finite_smith_invariant_factors_low_degree_first": finite_factors,
        "finite_elementary_divisor_degree_sum": finite_degree,
        "infinity_elementary_divisor_sizes": infinity_blocks,
        "infinity_elementary_divisor_degree_sum": infinity_degree,
        "reversed_smith_invariant_factors_low_degree_first": reversed_factors,
        "total_elementary_divisor_degree": degree_sum,
        "checks": {
            "finite_chart_normal_rank_is_full": finite_rank == n,
            "reversed_chart_normal_rank_is_full": infinity_rank == n,
            "finite_plus_infinity_degree_equals_dimension": degree_sum == n,
        },
        "complete_regular_strict_equivalence_invariant": True,
        "classification_statement": (
            "For regular square pencils over F_p, the finite Smith invariant "
            "factors of Q+tK together with the t-primary exponents in the "
            "Smith factors of K+tQ determine the pencil up to constant "
            "strict equivalence of the ordered coefficient pair."
        ),
        "scope": (
            "Regular pencils only. The reversed polynomial's nonzero roots "
            "are not infinity divisors; only its t-adic Smith exponents are. "
            "No GL_2 mixing of pencil coefficients or explicit equivalence "
            "witnesses are constructed."
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
        left["finite_smith_invariant_factors_low_degree_first"]
        == right["finite_smith_invariant_factors_low_degree_first"]
    )
    infinity_equal = (
        left["infinity_elementary_divisor_sizes"]
        == right["infinity_elementary_divisor_sizes"]
    )
    return {
        "schema": "the-fold-regular-pencil-complete-comparison-v2",
        "field": f"F_{p}",
        "decision_complete": True,
        "strictly_equivalent": finite_equal and infinity_equal,
        "finite_elementary_divisors_equal": finite_equal,
        "infinity_elementary_divisors_equal": infinity_equal,
        "left_profile": left,
        "right_profile": right,
        "comparison_basis": (
            "equality of finite Smith invariant factors of Q+tK and "
            "equality of t-primary Smith exponents of K+tQ"
        ),
    }
