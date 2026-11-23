"""Verify arbitrary supplied direct-sum witnesses for matrix pencils.

Unlike the minimal-chain complement routines, this verifier accepts any
invertible constant left/right transformations and any compatible rectangular
block partition. It verifies a claimed decomposition; it does not discover
one.
"""
from __future__ import annotations

from typing import Sequence


def _shape(matrix, name):
    if not isinstance(matrix, (list, tuple)):
        raise ValueError(f"{name} must be a matrix")
    if not matrix:
        return 0, 0
    if not all(isinstance(row, (list, tuple)) for row in matrix):
        raise ValueError(f"{name} must contain rows")
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError(f"{name} must be rectangular")
    return len(matrix), width


def _rank(matrix, p):
    if not matrix:
        return 0
    a = [[int(x) % p for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [x * inv % p for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [(x - factor*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def _transpose(matrix):
    return [list(col) for col in zip(*matrix)]


def _matmul(a, b, p):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    return [[sum(int(a[i][k]) * int(b[k][j]) for k in range(len(b))) % p
                 for j in range(len(b[0]))] for i in range(len(a))]


def _identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def _is_zero(matrix, p):
    return all(int(x) % p == 0 for row in matrix for x in row)


def verify_pencil_direct_sum_witness(
    q: Sequence[Sequence[int]],
    k: Sequence[Sequence[int]],
    p: int,
    left_transform: Sequence[Sequence[int]],
    right_transform: Sequence[Sequence[int]],
    first_block_shape: tuple[int, int],
) -> dict:
    """Verify S,T with S Q T and S K T block diagonal at a supplied cut.

    The first diagonal block has shape (r,c); the second has shape
    (m-r,n-c). Both blocks may be rectangular. The verifier checks the
    transformations are square/invertible, recomputes both products, and
    checks both off-diagonal blocks vanish over F_p.
    """
    if not isinstance(p, int) or p < 2:
        raise ValueError("p must be an integer prime")
    # Reject composite moduli: Fermat inversion in the exact routines assumes
    # a field, not merely a residue ring.
    if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
        raise ValueError("p must be prime")
    m, n = _shape(q, "q")
    if _shape(k, "k") != (m, n):
        raise ValueError("q and k must have the same shape")
    if m == 0 or n == 0:
        raise ValueError("pencil coefficients must be nonempty")
    if _shape(left_transform, "left_transform") != (m, m):
        raise ValueError("left_transform must be square with row dimension of q")
    if _shape(right_transform, "right_transform") != (n, n):
        raise ValueError("right_transform must be square with column dimension of q")
    if (not isinstance(first_block_shape, (tuple, list))
            or len(first_block_shape) != 2
            or any(not isinstance(x, int) for x in first_block_shape)):
        raise ValueError("first_block_shape must be an integer pair (r, c)")
    r, c = first_block_shape
    if not (0 <= r <= m and 0 <= c <= n):
        raise ValueError("first block dimensions must lie within the pencil shape")

    s = [[int(x) % p for x in row] for row in left_transform]
    t = [[int(x) % p for x in row] for row in right_transform]
    q0 = [[int(x) % p for x in row] for row in q]
    k0 = [[int(x) % p for x in row] for row in k]
    sqt = _matmul(_matmul(s, q0, p), t, p)
    skt = _matmul(_matmul(s, k0, p), t, p)

    def partition(matrix):
        return {
            "first_diagonal": [row[:c] for row in matrix[:r]],
            "top_right": [row[c:] for row in matrix[:r]],
            "bottom_left": [row[:c] for row in matrix[r:]],
            "second_diagonal": [row[c:] for row in matrix[r:]],
        }

    qb, kb = partition(sqt), partition(skt)
    s_rank, t_rank = _rank(s, p), _rank(t, p)
    cross_zero = all(_is_zero(block, p) for blocks in (qb, kb)
                     for key, block in blocks.items()
                     if key in ("top_right", "bottom_left"))
    return {
        "schema": "the-fold-pencil-direct-sum-witness-v1",
        "field": f"F_{p}",
        "source_shape": [m, n],
        "first_block_shape": [r, c],
        "second_block_shape": [m-r, n-c],
        "left_transform": s,
        "right_transform": t,
        "transformed_Q": sqt,
        "transformed_K": skt,
        "Q_blocks": qb,
        "K_blocks": kb,
        "verification": {
            "left_transform_rank": s_rank,
            "right_transform_rank": t_rank,
            "left_transform_invertible": s_rank == m,
            "right_transform_invertible": t_rank == n,
            "Q_cross_blocks_zero": all(_is_zero(qb[key], p)
                                       for key in ("top_right", "bottom_left")),
            "K_cross_blocks_zero": all(_is_zero(kb[key], p)
                                       for key in ("top_right", "bottom_left")),
            "direct_sum_verified": s_rank == m and t_rank == n and cross_zero,
        },
        "scope": (
            "This is an exact verifier for a supplied constant strict-equivalence "
            "direct-sum witness, including rectangular diagonal summands. It does "
            "not discover transformations, prove uniqueness, or assert that either "
            "summand is regular."
        ),
    }
