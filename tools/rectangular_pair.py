"""Finite-field fingerprints for pairs of rectangular linear maps.

The pair (Q, K), with equal m x n shape, is treated as a matrix pencil
a Q + b K over F_p. Its projective rank profile is invariant under shared
strict equivalence Q -> S Q T^{-1}, K -> S K T^{-1}. This is a partial
invariant, not a complete classification of matrix pencils.
"""
from __future__ import annotations

from typing import Sequence

from tools.spectral_fingerprint import rank_mod


def _validate_pair(q: Sequence[Sequence[int]],
                   k: Sequence[Sequence[int]]) -> tuple[int, int]:
    if not q or not k:
        raise ValueError("Q and K must be non-empty matrices")
    q_width = len(q[0])
    k_width = len(k[0])
    if q_width < 1 or k_width < 1:
        raise ValueError("Q and K must have non-empty rows")
    if any(len(row) != q_width for row in q):
        raise ValueError("Q must be rectangular")
    if any(len(row) != k_width for row in k):
        raise ValueError("K must be rectangular")
    if (len(q), q_width) != (len(k), k_width):
        raise ValueError("Q and K must have identical shapes")
    return len(q), q_width


def _combine(q: Sequence[Sequence[int]], k: Sequence[Sequence[int]],
             a: int, b: int, p: int) -> list[list[int]]:
    return [[(a * int(x) + b * int(y)) % p for x, y in zip(qrow, krow)]
            for qrow, krow in zip(q, k)]


def _horizontal(q: Sequence[Sequence[int]],
                k: Sequence[Sequence[int]]) -> list[list[int]]:
    return [list(map(int, qr)) + list(map(int, kr))
            for qr, kr in zip(q, k)]


def _vertical(q: Sequence[Sequence[int]],
              k: Sequence[Sequence[int]]) -> list[list[int]]:
    return [list(map(int, row)) for row in q] + [
        list(map(int, row)) for row in k
    ]


def analyze_rectangular_pair(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
) -> dict:
    """Compute exact rank invariants of an equal-shaped pair over F_p.

    Projective coefficients are represented once each as (1,t), t in F_p,
    together with (0,1). The result is invariant under shared invertible
    changes of codomain and domain coordinates.
    """
    rows, columns = _validate_pair(q, k)
    rank_q = rank_mod(q, p)
    rank_k = rank_mod(k, p)
    horizontal_rank = rank_mod(_horizontal(q, k), p)
    vertical_rank = rank_mod(_vertical(q, k), p)

    pencil = []
    for a, b in [(1, t) for t in range(p)] + [(0, 1)]:
        combined = _combine(q, k, a, b, p)
        pencil.append({
            "a": a,
            "b": b,
            "rank": rank_mod(combined, p),
        })
    histogram: dict[str, int] = {}
    for entry in pencil:
        key = str(entry["rank"])
        histogram[key] = histogram.get(key, 0) + 1

    return {
        "schema": "the-fold-rectangular-pair-pencil-v1",
        "field": f"F_{p}",
        "shape": [rows, columns],
        "individual_ranks": {"q": rank_q, "k": rank_k},
        "joint_ranks": {
            "horizontal_concatenation_q_k": horizontal_rank,
            "vertical_stack_q_k": vertical_rank,
        },
        "projective_pencil_rank_profile": pencil,
        "projective_rank_histogram": dict(sorted(
            histogram.items(), key=lambda item: int(item[0])
        )),
        "invariance": (
            "Preserved by Q -> S Q T^{-1}, K -> S K T^{-1} "
            "for invertible S and T over F_p."
        ),
        "limitations": [
            "The projective rank profile and joint ranks are invariants, not a complete classification of matrix pencils.",
            "The shared-coordinate-change assumption must be justified for the application; independent Q/K basis changes are not covered.",
            "This analyzes quantized finite-field maps, not real-valued model behavior or attention outputs.",
        ],
    }
