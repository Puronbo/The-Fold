"""Bounded exhaustive strict-equivalence recovery for one singular Kronecker block."""
from __future__ import annotations
from itertools import product
from typing import Sequence

from tools.strict_pencil_equivalence import _det_mod, strict_pencil_equivalence_audit
from tools.rectangular_pencil import _validate_pair


def _matrices_of_shape(rows, cols, p):
    for values in product(range(p), repeat=rows * cols):
        yield [list(values[i*cols:(i+1)*cols]) for i in range(rows)]


def _general_linear(n, p):
    for matrix in _matrices_of_shape(n, n, p):
        if _det_mod(matrix, p):
            yield matrix


def _gl_order(n, p):
    count = 1
    for i in range(n):
        count *= p**n - p**i
    return count


def right_singular_block(index: int, p: int) -> tuple[list[list[int]], list[list[int]]]:
    """Canonical L_index pencil: Q=[I 0], K=[0 I], shape e by e+1."""
    if not isinstance(index, int) or index < 1:
        raise ValueError("singular-block index must be a positive integer")
    if not isinstance(p, int) or p < 2:
        raise ValueError("p must be prime")
    q = [[int(i == j) for j in range(index + 1)] for i in range(index)]
    k = [[int(j == i + 1) for j in range(index + 1)] for i in range(index)]
    return q, k


def _transpose(a):
    return [list(row) for row in zip(*a)]


def recover_single_singular_block_equivalence(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    side: str = "right", max_pairs: int = 1_000_000,
) -> dict:
    """Find constant S,T mapping a pencil to one canonical L_e or L_e^T block.

    This is exhaustive finite-field search, deliberately capped by the
    product |GL_m(F_p)| |GL_n(F_p)|. It is not a general Kronecker algorithm.
    """
    rows, cols = _validate_pair(q, k, p)
    if side not in ("right", "left"):
        raise ValueError("side must be 'right' or 'left'")
    if not isinstance(max_pairs, int) or max_pairs < 1:
        raise ValueError("max_pairs must be a positive integer")
    if side == "left":
        q_work, k_work = _transpose(q), _transpose(k)
        m, n = cols, rows
    else:
        q_work, k_work = [list(map(int, row)) for row in q], [list(map(int, row)) for row in k]
        m, n = rows, cols
    if n != m + 1:
        return {
            "schema": "the-fold-single-singular-block-recovery-v1",
            "field": f"F_{p}", "side": side, "recovered": False,
            "reason": "shape is not that of a single singular block",
            "strict_equivalence_witness": None,
        }
    index = m
    q_target, k_target = right_singular_block(index, p)
    total_pairs = _gl_order(m, p) * _gl_order(n, p)
    if total_pairs > max_pairs:
        return {
            "schema": "the-fold-single-singular-block-recovery-v1",
            "field": f"F_{p}", "side": side, "shape": [rows, cols],
            "candidate_index": index, "candidate_pairs": total_pairs,
            "max_pairs": max_pairs, "recovered": False,
            "search_complete": False,
            "reason": "exhaustive GL(m) x GL(n) search exceeds pair budget",
            "strict_equivalence_witness": None,
        }
    left_group = list(_general_linear(m, p))
    right_group = list(_general_linear(n, p))
    tested = 0
    for s in left_group:
        sq = [[sum(s[i][a] * q_work[a][j] for a in range(m)) % p
                for j in range(n)] for i in range(m)]
        sk = [[sum(s[i][a] * k_work[a][j] for a in range(m)) % p
                for j in range(n)] for i in range(m)]
        for t in right_group:
            tested += 1
            q_image = [[sum(sq[i][a] * t[a][j] for a in range(n)) % p
                         for j in range(n)] for i in range(m)]
            if q_image != q_target:
                continue
            k_image = [[sum(sk[i][a] * t[a][j] for a in range(n)) % p
                         for j in range(n)] for i in range(m)]
            if k_image != k_target:
                continue
            if side == "right":
                audit = strict_pencil_equivalence_audit(q_work, k_work, p,
                    q_target, k_target, s, t)
                witness = {"left_transform_S": s, "right_transform_T": t}
            else:
                # Transpose identities S Q^T T=Q0 and S K^T T=K0
                # correspond to Q' = T^T Q S^T, K' = T^T K S^T.
                audit = strict_pencil_equivalence_audit(q_work, k_work, p,
                    q_target, k_target, s, t)
                witness = {"transpose_left_transform_S": s,
                           "transpose_right_transform_T": t,
                           "original_left_transform_S": _transpose(t),
                           "original_right_transform_T": _transpose(s)}
            return {
                "schema": "the-fold-single-singular-block-recovery-v1",
                "field": f"F_{p}", "side": side, "shape": [rows, cols],
                "candidate_index": index, "candidate_pairs": total_pairs,
                "pairs_tested": tested, "search_complete": True,
                "recovered": audit["strict_equivalence_certified"],
                "canonical_Q": q_target, "canonical_K": k_target,
                "strict_equivalence_witness": witness,
                "verification": audit,
                "scope": "Exhaustive recovery for one right or left singular block only.",
            }
    return {
        "schema": "the-fold-single-singular-block-recovery-v1",
        "field": f"F_{p}", "side": side, "shape": [rows, cols],
        "candidate_index": index, "candidate_pairs": total_pairs,
        "pairs_tested": tested, "search_complete": True,
        "recovered": False, "strict_equivalence_witness": None,
        "reason": "no strict-equivalence witness to the single-block canonical pencil exists",
        "scope": "Exhaustive recovery for one right or left singular block only.",
    }
