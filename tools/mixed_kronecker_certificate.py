"""Verify a supplied mixed Kronecker block decomposition by strict equivalence."""
from __future__ import annotations
from typing import Sequence

from tools.pencil_smith import rectangular_pencil_smith_profile
from tools.rectangular_pencil import _validate_pair
from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit


def _block_diagonal(components):
    row_sizes = [len(q) for q, _ in components]
    col_sizes = [len(q[0]) for q, _ in components]
    rows, cols = sum(row_sizes), sum(col_sizes)
    q_out = [[0] * cols for _ in range(rows)]
    k_out = [[0] * cols for _ in range(rows)]
    ro = co = 0
    for (q, k), height, width in zip(components, row_sizes, col_sizes):
        for i in range(height):
            for j in range(width):
                q_out[ro+i][co+j] = int(q[i][j])
                k_out[ro+i][co+j] = int(k[i][j])
        ro += height
        co += width
    return q_out, k_out


def _singular_blocks(indices, side):
    components = []
    for e in indices:
        if isinstance(e, bool) or not isinstance(e, int) or e < 1:
            raise ValueError("minimal indices must be positive integers (zero-index blocks are not supported)")
        if side == "right":
            q = [[int(i == j) for j in range(e+1)] for i in range(e)]
            k = [[int(j == i+1) for j in range(e+1)] for i in range(e)]
        else:
            q = [[int(i == j) for j in range(e)] for i in range(e+1)]
            k = [[int(i == j+1) for j in range(e)] for i in range(e+1)]
        components.append((q, k))
    return components


def verify_mixed_kronecker_decomposition(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    right_minimal_indices: Sequence[int] = (),
    left_minimal_indices: Sequence[int] = (),
    regular_q: Sequence[Sequence[int]] | None = None,
    regular_k: Sequence[Sequence[int]] | None = None,
    left_transform: Sequence[Sequence[int]],
    right_transform: Sequence[Sequence[int]],
    max_minors: int = 2000,
) -> dict:
    """Verify S Q T and S K T equal supplied singular blocks plus a regular pencil.

    The regular block is retained as supplied; it is certified regular over
    F_p(t), not reduced to elementary-divisor canonical form.
    """
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(max_minors, int) or max_minors < 1:
        raise ValueError("max_minors must be a positive integer")
    if (regular_q is None) != (regular_k is None):
        raise ValueError("regular_Q and regular_K must either both be supplied or both omitted")

    right_indices = list(right_minimal_indices)
    left_indices = list(left_minimal_indices)
    components = _singular_blocks(right_indices, "right")
    components += _singular_blocks(left_indices, "left")

    regular_dimension = 0
    regular_profile = None
    if regular_q is not None:
        rr, rc = _validate_pair(regular_q, regular_k, p)
        if rr != rc:
            raise ValueError("the supplied regular component must be square")
        regular_dimension = rr
        regular_profile = rectangular_pencil_smith_profile(
            regular_q, regular_k, p, max_minors=max_minors
        )["finite_chart"]
        if regular_profile["normal_rank_over_rational_function_field"] != regular_dimension:
            raise ValueError("the supplied regular component is singular over F_p(t)")
        components.append((regular_q, regular_k))

    target_q, target_k = _block_diagonal(components)
    if not components:
        raise ValueError("at least one singular block or a regular component is required")
    if len(target_q) != rows or len(target_q[0]) != cols:
        raise ValueError("declared block dimensions do not match the source pencil shape")

    audit = strict_pencil_equivalence_audit(
        q, k, p, target_q, target_k, left_transform, right_transform
    )
    return {
        "schema": "the-fold-mixed-kronecker-certificate-v1",
        "field": f"F_{p}", "source_shape": [rows, cols],
        "decomposition": {
            "right_minimal_indices": right_indices,
            "left_minimal_indices": left_indices,
            "regular_dimension": regular_dimension,
            "regular_component_is_regular_over_Fp_t": (
                regular_profile is not None and
                regular_profile["normal_rank_over_rational_function_field"] == regular_dimension
                if regular_profile is not None else None
            ),
            "regular_component_finite_smith_factors": (
                regular_profile["smith_invariant_factors_low_degree_first"]
                if regular_profile is not None else []
            ),
        },
        "canonical_target_Q": target_q,
        "canonical_target_K": target_k,
        "strict_equivalence_audit": audit,
        "decomposition_certified": audit["strict_equivalence_certified"],
        "scope": (
            "Verifies supplied constant strict-equivalence witnesses for the declared "
            "right/left singular blocks and supplied regular block. It does not discover "
            "the decomposition, canonicalize the regular block, or prove uniqueness."
        ),
    }
