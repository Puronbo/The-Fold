"""Construct complementary bases that annihilate chain cross-couplings.

The routine keeps the recovered minimal-chain subspaces fixed. It searches
their complements inside simultaneous left/right annihilator spaces, and
returns an exact witness only when those spaces admit full basis extensions.
"""
from __future__ import annotations

from typing import Sequence

from tools.minimal_chain_adapted_coordinates import (
    _matmul, _rank, _transpose, minimal_chain_adapted_coordinates,
)
from tools.rectangular_pencil import _validate_pair


def _nullspace_rows(matrix, width, p):
    """Return a row-basis for the right nullspace of matrix over F_p."""
    a = [[int(x) % p for x in row] for row in matrix]
    if not a:
        return [[int(i == j) for j in range(width)] for i in range(width)]
    pivots = []
    r = 0
    for c in range(width):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [x * inv % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x-factor*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    free = [c for c in range(width) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * width
        v[f] = 1
        for i, pivot_col in enumerate(pivots):
            v[pivot_col] = (-a[i][f]) % p
        basis.append(v)
    return basis


def _extend(seed, candidates, width, p):
    chosen = [[int(x) % p for x in v] for v in seed]
    rank = _rank(chosen, p)
    for vector in candidates:
        candidate = chosen + [[int(x) % p for x in vector]]
        new_rank = _rank(candidate, p)
        if new_rank > rank:
            chosen.append(candidate[-1])
            rank = new_rank
        if rank == width:
            break
    return chosen if rank == width else None


def _columns(matrix):
    return _transpose(matrix) if matrix else []


def minimal_chain_decoupling_completion(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Find exact complements eliminating both chain/residual cross-blocks.

    Failure means this annihilator-based complement construction could not
    extend the fixed chain bases; it is not a proof that no other splitting
    or strict-equivalence decomposition exists.
    """
    rows, cols = _validate_pair(q, k, p)
    adapted = minimal_chain_adapted_coordinates(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    rdim = adapted["right_chain_basis_dimension"]
    ldim = adapted["left_chain_cobasis_dimension"]
    right_chain = _columns(adapted["domain_basis_T"])[:rdim]
    left_chain = adapted["codomain_cobasis_S"][:ldim]

    right_constraints = (
        _matmul(left_chain, q, p) + _matmul(left_chain, k, p)
        if left_chain else []
    )
    left_constraints = []
    if right_chain:
        q_chain = _matmul(q, _transpose(right_chain), p)
        k_chain = _matmul(k, _transpose(right_chain), p)
        left_constraints = _transpose(q_chain) + _transpose(k_chain)

    right_null = _nullspace_rows(right_constraints, cols, p)
    left_null = _nullspace_rows(left_constraints, rows, p)
    # The candidate lists are bases of the complete annihilator subspaces.
    # Their span together with the fixed chain span determines feasibility:
    # a full-rank concatenation is necessary and sufficient for a basis
    # extension. Greedy extension of a spanning set is therefore complete;
    # enumerating field combinations would add no information here.
    right_span_rank = _rank(right_chain + right_null, p)
    left_span_rank = _rank(left_chain + left_null, p)
    right_full = _extend(right_chain, right_null, cols, p)
    left_full = _extend(left_chain, left_null, rows, p)

    result = {
        "schema": "the-fold-minimal-chain-decoupling-completion-v1",
        "field": f"F_{p}",
        "source_shape": [rows, cols],
        "chain_dimensions": {"right": rdim, "left": ldim},
        "annihilator_dimensions": {
            "domain_complement_candidates": len(right_null),
            "codomain_complement_candidates": len(left_null),
        },
        "feasibility_certificate": {
            "domain_combined_span_rank": right_span_rank,
            "domain_ambient_dimension": cols,
            "domain_deficiency": cols - right_span_rank,
            "codomain_combined_span_rank": left_span_rank,
            "codomain_ambient_dimension": rows,
            "codomain_deficiency": rows - left_span_rank,
            "criterion": (
                "A complement exists in each fixed annihilator space iff "
                "the corresponding chain span plus annihilator span has "
                "full ambient rank. The reported ranks are exact over F_p."
            ),
            "domain_feasible": right_span_rank == cols,
            "codomain_feasible": left_span_rank == rows,
        },
        "completion_possible": right_full is not None and left_full is not None,
        "failure_reasons": [],
        "scope": (
            "The feasibility certificate is necessary and sufficient for "
            "basis completion inside the two computed annihilator spaces. "
            "A deficient rank proves no complement exists within that fixed "
            "space, but does not rule out a different splitting or a more "
            "general strict-equivalence decomposition. Successful witnesses "
            "are still checked by direct exact multiplication."
        ),
    }
    if right_full is None:
        result["failure_reasons"].append(
            "domain annihilator candidates do not extend the fixed right-chain basis"
        )
    if left_full is None:
        result["failure_reasons"].append(
            "codomain annihilator candidates do not extend the fixed left-chain basis"
        )
    if not result["completion_possible"]:
        return result

    t = _transpose(right_full)
    s = left_full
    qa, ka = _matmul(_matmul(s, q, p), t, p), _matmul(_matmul(s, k, p), t, p)
    offdiag = {
        "Q_top_right": [row[rdim:] for row in qa[:ldim]],
        "K_top_right": [row[rdim:] for row in ka[:ldim]],
        "Q_bottom_left": [row[:rdim] for row in qa[ldim:]],
        "K_bottom_left": [row[:rdim] for row in ka[ldim:]],
    }
    decoupled = all(
        not any(int(x) % p for row in block for x in row)
        for block in offdiag.values()
    )
    result.update({
        "decoupled": decoupled,
        "domain_basis_T": t,
        "codomain_cobasis_S": s,
        "adapted_Q": qa,
        "adapted_K": ka,
        "cross_coupling_blocks": offdiag,
        "exact_checks": {
            "T_invertible": _rank(_transpose(t), p) == cols,
            "S_invertible": _rank(s, p) == rows,
            "Q_transform_exact": qa == _matmul(_matmul(s, q, p), t, p),
            "K_transform_exact": ka == _matmul(_matmul(s, k, p), t, p),
            "cross_coupling_zero": decoupled,
        },
    })
    return result
