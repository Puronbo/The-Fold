"""Recover polynomial left/right minimal indices of a linear pencil."""
from __future__ import annotations
from typing import Sequence
from tools.pencil_smith import rectangular_pencil_smith_profile
from tools.rectangular_pencil import _validate_pair
from tools.spectral_fingerprint import rank_mod

def _transpose(matrix):
    return [list(column) for column in zip(*matrix)]

def _convolution_matrix(q, k, degree: int, p: int):
    rows, cols = len(q), len(q[0])
    result = [[0] * ((degree + 1) * cols)
              for _ in range((degree + 2) * rows)]
    for block_row in range(degree + 2):
        for i in range(rows):
            target = block_row * rows + i
            if block_row <= degree:
                for j in range(cols):
                    result[target][block_row * cols + j] = int(q[i][j]) % p
            if block_row >= 1:
                for j in range(cols):
                    result[target][(block_row - 1) * cols + j] = int(k[i][j]) % p
    return result

def _bounded_nullities(q, k, p: int, max_degree: int) -> list[int]:
    values = []
    for degree in range(max_degree + 1):
        convolution = _convolution_matrix(q, k, degree, p)
        values.append(len(convolution[0]) - rank_mod(convolution, p))
    return values

def _recover_indices(nullities: list[int], expected_count: int):
    previous_slope = 0
    indices, slopes = [], []
    previous_h = 0
    for degree, h_value in enumerate(nullities):
        slope = h_value - previous_h
        slopes.append(slope)
        count_at_degree = slope - previous_slope
        if count_at_degree < 0:
            raise ArithmeticError("bounded nullity sequence is not convex")
        indices.extend([degree] * count_at_degree)
        previous_slope, previous_h = slope, h_value
    indices.sort()
    return indices, slopes, len(indices) == expected_count

def _side_profile(q, k, p: int, max_degree: int, expected_count: int):
    nullities = _bounded_nullities(q, k, p, max_degree)
    indices, slopes, complete = _recover_indices(nullities, expected_count)
    return {
        "bounded_polynomial_nullities": nullities,
        "first_differences": slopes,
        "minimal_indices": indices if complete else None,
        "recovered_indices_so_far": indices,
        "expected_number_of_indices_from_normal_rank": expected_count,
        "complete": complete,
    }

def rectangular_pencil_minimal_indices(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Recover right/left Forney indices, or explicitly report incompleteness.

    Normal rank is exact. A finite degree bound is never silently treated as
    complete: the recovered index count must equal cols-rank and rows-rank.
    """
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(max_degree, int) or max_degree < 0:
        raise ValueError("max_degree must be a non-negative integer")
    smith = rectangular_pencil_smith_profile(q, k, p, max_minors=max_minors)
    normal_rank = smith["finite_chart"]["normal_rank_over_rational_function_field"]
    right = _side_profile(q, k, p, max_degree, cols - normal_rank)
    left = _side_profile(_transpose(q), _transpose(k), p,
                         max_degree, rows - normal_rank)
    return {
        "schema": "the-fold-pencil-minimal-indices-v1",
        "field": f"F_{p}", "shape": [rows, cols], "pencil": "Q + t K",
        "normal_rank_over_rational_function_field": normal_rank,
        "right": right, "left": left,
        "complete": right["complete"] and left["complete"],
        "scope": (
            "Exact left/right polynomial minimal indices over F_p[t]. "
            "No transforming matrices or canonical block decomposition."
        ),
        "method": (
            "coefficient-convolution nullities over F_p, first differences, "
            "and exact normal rank from polynomial determinantal divisors"
        ),
    }
