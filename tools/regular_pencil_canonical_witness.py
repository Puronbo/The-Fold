"""Construct and verify a strict-equivalence certificate to canonical form."""
from __future__ import annotations

from typing import Sequence

from tools.regular_pencil_canonical import regular_pencil_canonical_form
from tools.regular_pencil_witness import construct_regular_pencil_witness
from tools.rectangular_pencil import _validate_pair


def regular_pencil_canonical_witness(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
    *,
    max_candidates: int = 100_000,
    max_minors: int = 2000,
) -> dict:
    """Return a canonical representative and, when found, constant S,T.

    The target is assembled from finite/infinity elementary divisors.
    Existing chart-based or bounded no-chart witness construction is then
    used to find S,T satisfying S Q T=Q_can and S K T=K_can.
    """
    rows, cols = _validate_pair(q, k, p)
    if rows != cols:
        raise ValueError("canonical witness requires a square regular pencil")
    canonical = regular_pencil_canonical_form(
        q, k, p, max_minors=max_minors
    )
    witness = construct_regular_pencil_witness(
        q, k, canonical["canonical_Q"], canonical["canonical_K"], p,
        max_candidates=max_candidates,
    )
    result = {
        "schema": "the-fold-regular-pencil-canonical-witness-v1",
        "field": f"F_{p}",
        "dimension": rows,
        "canonical_Q": canonical["canonical_Q"],
        "canonical_K": canonical["canonical_K"],
        "canonical_profile_verified": canonical["checks"][
            "canonical_profile_matches_source"
        ],
        "decision_complete": witness["decision_complete"],
        "strictly_equivalent": witness["strictly_equivalent"],
        "witness_found": witness["witness_found"],
        "left_transform_S": witness.get("left_transform_S"),
        "right_transform_T": witness.get("right_transform_T"),
        "construction_method": (
            "shared-chart operator intertwiner" if witness.get("common_chart")
            else "bounded direct finite-field search"
        ),
        "witness_details": witness,
        "scope": (
            "Canonical target is constructed and independently profile-verified. "
            "Constant transformations are returned only when the exact witness "
            "search finds and verifies them; no-chart search is exponential and "
            "budget-bounded."
        ),
    }
    return result
