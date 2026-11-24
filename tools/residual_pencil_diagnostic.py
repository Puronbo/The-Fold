"""Residual-pencil diagnostics in minimal-chain adapted coordinates.

The bottom-right coordinate block is inspected without assuming it is a
Kronecker regular summand: cross-coupling blocks are returned and reported.
"""
from __future__ import annotations

from typing import Sequence

from tools.minimal_chain_adapted_coordinates import minimal_chain_adapted_coordinates
from tools.pencil_kronecker import rectangular_pencil_kronecker_profile
from tools.rectangular_pencil import _validate_pair


def _slice(matrix, row_start, row_end, col_start, col_end):
    return [list(map(int, row[col_start:col_end]))
            for row in matrix[row_start:row_end]]


def residual_pencil_diagnostic(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Inspect the complementary coordinate block after minimal-chain adaptation.

    If the residual is nonempty and square, compute its own exact Kronecker
    profile. This is a profile of the coordinate block only, not proof that
    it is a direct summand or invariantly the regular part of the source.
    """
    rows, cols = _validate_pair(q, k, p)
    adapted = minimal_chain_adapted_coordinates(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    rdim = adapted["right_chain_basis_dimension"]
    ldim = adapted["left_chain_cobasis_dimension"]
    q_adapted, k_adapted = adapted["adapted_Q"], adapted["adapted_K"]
    q_blocks = {
        "chain_to_chain": _slice(q_adapted, 0, ldim, 0, rdim),
        "chain_to_domain_complement": _slice(q_adapted, 0, ldim, rdim, cols),
        "codomain_complement_from_chain": _slice(q_adapted, ldim, rows, 0, rdim),
        "residual": _slice(q_adapted, ldim, rows, rdim, cols),
    }
    k_blocks = {
        "chain_to_chain": _slice(k_adapted, 0, ldim, 0, rdim),
        "chain_to_domain_complement": _slice(k_adapted, 0, ldim, rdim, cols),
        "codomain_complement_from_chain": _slice(k_adapted, ldim, rows, 0, rdim),
        "residual": _slice(k_adapted, ldim, rows, rdim, cols),
    }
    residual_rows, residual_cols = rows - ldim, cols - rdim
    square = residual_rows == residual_cols
    nonempty = residual_rows > 0 and residual_cols > 0
    profile = None
    if square and nonempty:
        profile = rectangular_pencil_kronecker_profile(
            q_blocks["residual"], k_blocks["residual"], p,
            max_degree=max_degree, max_minors=max_minors,
        )
    cross_coupling_zero = all(
        not any(value % p for row in q_blocks[name] + k_blocks[name] for value in row)
        for name in ("chain_to_domain_complement", "codomain_complement_from_chain")
    )
    return {
        "schema": "the-fold-residual-pencil-diagnostic-v1",
        "field": f"F_{p}",
        "source_shape": [rows, cols],
        "residual_shape": [residual_rows, residual_cols],
        "residual_is_square": square,
        "residual_is_nonempty": nonempty,
        "Q_blocks": q_blocks,
        "K_blocks": k_blocks,
        "cross_coupling_blocks_zero": cross_coupling_zero,
        "residual_kronecker_profile": profile,
        "residual_profile_scope": (
            "Profile applies to the displayed bottom-right coordinate block only. "
            "It is not a source-pencil invariant unless a compatible decoupling "
            "is separately established."
        ),
        "adapted_coordinates": adapted,
    }
