"""Compare primary-module structure of different-sized operators over F_p."""
from __future__ import annotations

from typing import Sequence

from tools.rational_canonical import rational_canonical_profile
from tools.spectral_fingerprint import _is_prime


def _components(profile: dict) -> dict[tuple[int, ...], dict]:
    result = {}
    for item in profile["irreducible_primary_components"]:
        key = tuple(item["factor_coefficients_descending"])
        blocks = tuple(item["elementary_divisor_exponents_descending"])
        degree = item["factor_degree"]
        result[key] = {
            "degree": degree,
            "blocks": blocks,
            "primary_dimension": degree * sum(blocks),
        }
    return result


def compare_primary_structure(
    matrix_a: Sequence[Sequence[int]],
    matrix_b: Sequence[Sequence[int]],
    p: int,
) -> dict:
    """Compare irreducible primary components without requiring equal dimensions.

    Reports common irreducible support, primary-dimension overlap, and exact
    elementary-divisor overlap. These are descriptive overlaps, not metrics
    of functional or semantic similarity.
    """
    if not _is_prime(p):
        raise ValueError("p must be prime")
    left_profile = rational_canonical_profile(matrix_a, p)
    right_profile = rational_canonical_profile(matrix_b, p)
    left, right = _components(left_profile), _components(right_profile)
    keys = sorted(set(left) | set(right), key=lambda x: (len(x), x))

    rows = []
    shared_primary_dimension = 0
    shared_elementary_divisor_dimension = 0
    for key in keys:
        a, b = left.get(key), right.get(key)
        da = a["primary_dimension"] if a else 0
        db = b["primary_dimension"] if b else 0
        shared_dim = min(da, db)
        shared_primary_dimension += shared_dim

        blocks_a = a["blocks"] if a else ()
        blocks_b = b["blocks"] if b else ()
        counts_a, counts_b = {}, {}
        for size in blocks_a:
            counts_a[size] = counts_a.get(size, 0) + 1
        for size in blocks_b:
            counts_b[size] = counts_b.get(size, 0) + 1
        common_blocks = {
            size: min(counts_a.get(size, 0), counts_b.get(size, 0))
            for size in sorted(set(counts_a) | set(counts_b))
            if min(counts_a.get(size, 0), counts_b.get(size, 0))
        }
        exact_block_overlap = sum(
            key_degree * size * count
            for size, count in common_blocks.items()
            for key_degree in [len(key) - 1]
        )
        shared_elementary_divisor_dimension += exact_block_overlap

        rows.append({
            "irreducible_factor_coefficients_descending": list(key),
            "factor_degree": len(key) - 1,
            "present_in_a": a is not None,
            "present_in_b": b is not None,
            "primary_dimension_a": da,
            "primary_dimension_b": db,
            "shared_primary_dimension_upper_bound": shared_dim,
            "elementary_divisor_block_sizes_a": list(blocks_a),
            "elementary_divisor_block_sizes_b": list(blocks_b),
            "exact_common_block_multiplicities": {
                str(size): count for size, count in common_blocks.items()
            },
            "exact_elementary_divisor_dimension_overlap": exact_block_overlap,
        })

    dim_a, dim_b = left_profile["dimension"], right_profile["dimension"]
    denominator = min(dim_a, dim_b)
    return {
        "schema": "the-fold-primary-structure-comparison-v1",
        "field": f"F_{p}",
        "dimension_a": dim_a,
        "dimension_b": dim_b,
        "same_dimension": dim_a == dim_b,
        "same_similarity_class": (
            dim_a == dim_b
            and left_profile["invariant_factors_coefficients_descending"]
            == right_profile["invariant_factors_coefficients_descending"]
        ),
        "common_irreducible_factor_count": sum(
            1 for key in set(left) & set(right)
        ),
        "shared_primary_dimension": shared_primary_dimension,
        "shared_primary_dimension_fraction_of_smaller_operator": (
            shared_primary_dimension / denominator
        ),
        "exact_elementary_divisor_dimension_overlap": (
            shared_elementary_divisor_dimension
        ),
        "exact_elementary_divisor_overlap_fraction_of_smaller_operator": (
            shared_elementary_divisor_dimension / denominator
        ),
        "components": rows,
        "interpretation": (
            "Primary-dimension overlap measures common dimension within "
            "matching irreducible primary components. Exact elementary-divisor "
            "overlap additionally requires matching block sizes. Neither "
            "quantity establishes functional or semantic similarity."
        ),
    }
