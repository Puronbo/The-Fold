#!/usr/bin/env python3
"""Exact rational and F_2 checks for UF-023 D4 character projectors."""
from fractions import Fraction

B = ((0, 0), (1, 0), (0, 1), (1, 1),
     (2, 0), (2, 1), (3, 0), (3, 1))
INDEX = {m: i for i, m in enumerate(B)}
N = len(B)


def reduce_monomial(a, b):
    q, rem = divmod(b, 2)
    a += 2 * q  # y^2 = -x^2
    if a >= 4:
        return {}
    return {INDEX[(a, rem)]: (-1) ** q}


def action_matrix(kind):
    # Columns are images of basis monomials.
    out = [[0] * N for _ in range(N)]
    for j, (a, b) in enumerate(B):
        if kind == "r":       # x -> -y, y -> x
            terms, sign = reduce_monomial(b, a), (-1) ** a
        elif kind == "s":     # x -> x, y -> -y
            terms, sign = reduce_monomial(a, b), (-1) ** b
        else:
            raise ValueError(kind)
        for i, c in terms.items():
            out[i][j] = sign * c
    return out


def eye(n=N):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def add(*matrices):
    return [[sum(M[i][j] for M in matrices)
             for j in range(N)] for i in range(N)]


def scale(M, c):
    return [[c * x for x in row] for row in M]


def mul(A, Bm):
    return [[sum(A[i][k] * Bm[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def power(A, n):
    out = eye()
    for _ in range(n):
        out = mul(out, A)
    return out


def trace(A):
    return sum(A[i][i] for i in range(N))


def rank_rational(M):
    A = [[Fraction(v) for v in row] for row in M]
    rows, cols, rank = len(A), len(A[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if A[r][col]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        v = A[rank][col]
        A[rank] = [z / v for z in A[rank]]
        for r in range(rows):
            if r != rank and A[r][col]:
                f = A[r][col]
                A[r] = [A[r][c] - f * A[rank][c]
                        for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def rank_mod2(M):
    A = [[int(v) & 1 for v in row] for row in M]
    rows, cols, rank = len(A), len(A[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if A[r][col]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        for r in range(rows):
            if r != rank and A[r][col]:
                A[r] = [a ^ b for a, b in zip(A[r], A[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def main():
    I = eye()
    R, S = action_matrix("r"), action_matrix("s")
    R2, R3, R4 = power(R, 2), power(R, 3), power(R, 4)
    assert R4 == I
    assert mul(S, S) == I
    assert mul(mul(S, R), S) == R3

    projectors = {}
    for eps in (1, -1):
        for delta in (1, -1):
            cyclic = add(I, scale(R, eps), R2, scale(R3, eps))
            projector = scale(mul(cyclic, add(I, scale(S, delta))),
                              Fraction(1, 8))
            projectors[(eps, delta)] = projector
            assert mul(projector, projector) == projector
            assert rank_rational(projector) == 1

    PE = scale(add(I, scale(R2, -1)), Fraction(1, 2))
    assert mul(PE, PE) == PE
    assert rank_rational(PE) == 4

    all_projectors = list(projectors.values()) + [PE]
    total = add(*all_projectors)
    assert total == I
    for i in range(len(all_projectors)):
        for j in range(i):
            assert mul(all_projectors[i], all_projectors[j]) == [
                [0] * N for _ in range(N)]

    # Modulo two, r is coordinate swap and s becomes identity.
    R2mod = [[v & 1 for v in row] for row in R]
    I2 = I
    difference = [[(R2mod[i][j] - I2[i][j]) & 1
                   for j in range(N)] for i in range(N)]
    assert rank_mod2(difference) == 2
    assert 8 == 0 and 2 == 0  # projector denominators are not invertible

    print("UF-023 exact checks: PASS")
    print("odd-characteristic projector ranks:",
          [rank_rational(P) for P in all_projectors])
    print("sum of projectors: identity")
    print("characteristic-two rank(R-I):", rank_mod2(difference))
    print("characteristic-two fixed-space dimension:", N - rank_mod2(difference))


if __name__ == "__main__":
    main()
