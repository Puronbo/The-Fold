"""Exact coordinate decoupling certificates for residual pencil blocks.

A certificate is positive precisely when both off-diagonal blocks vanish in
both coefficient matrices. It verifies the resulting block-diagonal identity
against the adapted pencil and carries the strict-equivalence witnesses.
"""
from __future__ import annotations

from typing import Sequence

from tools.residual_pencil_diagnostic import residual_pencil_diagnostic


def _rank_mod(matrix, p):
    if not matrix:
        return 0
    a = [[int(x) % p for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(x * inv) % p for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col]:
                factor = a[i][col]
                a[i] = [(x - factor*y) % p for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def _assemble(blocks, p):
    top_left, bottom_right = blocks["chain_to_chain"], blocks["residual"]
    top_rows = len(top_left)
    top_cols = len(top_left[0]) if top_left else 0
    bottom_rows = len(bottom_right)
    bottom_cols = len(bottom_right[0]) if bottom_right else 0
    return [
        [int(x) % p for x in row] + [0] * bottom_cols
        for row in top_left
    ] + [
        [0] * top_cols + [int(x) % p for x in row]
        for row in bottom_right
    ]


def _nonzero_entries(matrix, p):
    return [
        {"row": i, "column": j, "value": int(value) % p}
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
        if int(value) % p
    ]


def _certificate_from_diagnostic(diagnostic, p):
    q_blocks, k_blocks = diagnostic["Q_blocks"], diagnostic["K_blocks"]
    offdiag_names = ("chain_to_domain_complement", "codomain_complement_from_chain")
    obstructions = {}
    for name in offdiag_names:
        obstructions[name] = {
            "Q_nonzero_entries": _nonzero_entries(q_blocks[name], p),
            "K_nonzero_entries": _nonzero_entries(k_blocks[name], p),
            "Q_rank": _rank_mod(q_blocks[name], p),
            "K_rank": _rank_mod(k_blocks[name], p),
        }
    decoupled = all(
        not obstructions[name]["Q_nonzero_entries"]
        and not obstructions[name]["K_nonzero_entries"]
        for name in offdiag_names
    )
    adapted = diagnostic["adapted_coordinates"]
    reconstructed_q = _assemble(q_blocks, p)
    reconstructed_k = _assemble(k_blocks, p)
    adapted_q, adapted_k = adapted["adapted_Q"], adapted["adapted_K"]
    q_equal = reconstructed_q == adapted_q
    k_equal = reconstructed_k == adapted_k
    verified = q_equal and k_equal and adapted["verification"]["transformed_pair_exact"]
    return {
        "schema": "the-fold-residual-pencil-decoupling-certificate-v1",
        "field": diagnostic["field"],
        "decoupled": decoupled,
        "chain_shape": [
            diagnostic["left_chain_cobasis_dimension"],
            diagnostic["right_chain_basis_dimension"],
        ],
        "residual_shape": diagnostic["residual_shape"],
        "cross_coupling_obstructions": obstructions,
        "reconstructed_block_diagonal_Q": reconstructed_q,
        "reconstructed_block_diagonal_K": reconstructed_k,
        "exact_checks": {
            "reconstructed_Q_equals_adapted_Q": q_equal,
            "reconstructed_K_equals_adapted_K": k_equal,
            "adapted_strict_equivalence_verified": bool(
                adapted["verification"]["transformed_pair_exact"]
            ),
            "certificate_verified": verified,
        },
        "strict_equivalence_witness": {
            "S": adapted["codomain_cobasis_S"],
            "T": adapted["domain_basis_T"],
            "identity": "adapted_Q = S Q T; adapted_K = S K T",
            "invertibility_checks": adapted["verification"],
        },
        "scope": (
            "A positive result proves a direct-sum block decomposition in these "
            "adapted coordinates. It does not by itself prove that the residual "
            "block is regular. A negative result reports coupling obstructions "
            "and makes no direct-sum claim."
        ),
    }


def residual_pencil_decoupling_certificate(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Certify or obstruct chain/residual decoupling in adapted coordinates."""
    diagnostic = residual_pencil_diagnostic(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    diagnostic["left_chain_cobasis_dimension"] = diagnostic[
        "adapted_coordinates"
    ]["left_chain_cobasis_dimension"]
    diagnostic["right_chain_basis_dimension"] = diagnostic[
        "adapted_coordinates"
    ]["right_chain_basis_dimension"]
    return _certificate_from_diagnostic(diagnostic, p)
