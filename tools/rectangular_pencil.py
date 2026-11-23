"""Exact rank fingerprints for rectangular matrix pencils over prime fields.

A pair (Q, K) of equal-shaped maps is treated as a pencil aQ+bK.
The rank profile on P^1(F_p), together with joint ranks, is invariant
under shared strict equivalence (Q, K) -> (S Q T^{-1}, S K T^{-1}).
This is not a complete classification of matrix pencils.
"""
from __future__ import annotations

from typing import Sequence

from tools.spectral_fingerprint import _is_prime, rank_mod


def _validate_pair(q: Sequence[Sequence[int]],
                   k: Sequence[Sequence[int]], p: int) -> tuple[int, int]:
    if not _is_prime(p):
        raise ValueError("p must be prime")
    if not q or not k:
        raise ValueError("Q and K must be non-empty rectangular matrices")
    rows, cols = len(q), len(q[0])
    if cols == 0 or any(len(row) != cols for row in q):
        raise ValueError("Q must have a non-zero, consistent column count")
    if len(k) != rows or any(len(row) != cols for row in k):
        raise ValueError("Q and K must have the same rectangular shape")
    return rows, cols


def _linear_combination(q, k, a: int, b: int, p: int) -> list[list[int]]:
    return [
        [(a * int(q[i][j]) + b * int(k[i][j])) % p
         for j in range(len(q[0]))]
        for i in range(len(q))
    ]


def _horizontal_concat(q, k) -> list[list[int]]:
    return [list(map(int, q[i])) + list(map(int, k[i]))
            for i in range(len(q))]


def _rank_distribution(profile: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in profile:
        key = str(item["rank"])
        counts[key] = counts.get(key, 0) + 1
    return {key: counts[key] for key in sorted(counts, key=int)}


def rectangular_pencil_fingerprint(q, k, p: int) -> dict:
    """Fingerprint an equal-shaped rectangular pair without square padding.

    Projective points are represented canonically by (1,t), t in F_p,
    followed by (0,1). All ranks are exact over F_p.
    """
    rows, cols = _validate_pair(q, k, p)
    q_mod = [[int(x) % p for x in row] for row in q]
    k_mod = [[int(x) % p for x in row] for row in k]

    pencil = []
    for a, b in [(1, t) for t in range(p)] + [(0, 1)]:
        combined = _linear_combination(q_mod, k_mod, a, b, p)
        pencil.append({"a": a, "b": b, "rank": rank_mod(combined, p)})

    horizontal_rank = rank_mod(_horizontal_concat(q_mod, k_mod), p)
    vertical_rank = rank_mod(q_mod + k_mod, p)
    return {
        "schema": "the-fold-rectangular-pencil-v1",
        "field": f"F_{p}",
        "shape": [rows, cols],
        "equivalence": (
            "shared strict equivalence: Q -> S Q T^{-1}, "
            "K -> S K T^{-1}, with invertible S and T"
        ),
        "rank_q": rank_mod(q_mod, p),
        "rank_k": rank_mod(k_mod, p),
        "horizontal_concatenation_rank": horizontal_rank,
        "vertical_stack_rank": vertical_rank,
        "projective_rank_profile": pencil,
        "projective_rank_distribution": _rank_distribution(pencil),
        "projective_point_count": p + 1,
        "complete_classification": False,
        "interpretation": (
            "Exact rectangular-map and matrix-pencil rank invariants. "
            "They are preserved by shared input/output coordinate changes, "
            "but do not form a complete matrix-pencil classification and "
            "do not establish neural-network functional or semantic similarity."
        ),
    }
