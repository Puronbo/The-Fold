#!/usr/bin/env python3
"""Exact F_2 verifier for A = F_2[x,z]/(x^4,z^2), x,z primitive.

Builds beta(a tensor b) = (a tensor 1) Delta(b) in the 64-element
monomial tensor basis and checks full rank. No third-party packages.
"""
from math import comb

BASIS = [(i, j) for i in range(4) for j in range(2)]
INDEX = {m: n for n, m in enumerate(BASIS)}
DIM = len(BASIS)
assert DIM == 8


def multiply_monomials(left, right):
    i, j = left
    r, s = right
    out = (i + r, j + s)
    return None if out[0] >= 4 or out[1] >= 2 else out


def delta_monomial(monomial):
    i, j = monomial
    out = {}
    for p in range(i + 1):
        for q in range(j + 1):
            coeff = (comb(i, p) * comb(j, q)) & 1
            if coeff:
                out[((p, q), (i - p, j - q))] = coeff
    return out


def canonical_matrix():
    n = DIM * DIM
    matrix = [[0] * n for _ in range(n)]
    for a in BASIS:
        for b in BASIS:
            col = INDEX[a] * DIM + INDEX[b]
            for (left, right), coeff in delta_monomial(b).items():
                product = multiply_monomials(a, left)
                if product is not None:
                    row = INDEX[product] * DIM + INDEX[right]
                    matrix[row][col] ^= coeff
    return matrix


def rank_f2(matrix):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(rows):
            if r != rank and a[r][col]:
                a[r] = [u ^ v for u, v in zip(a[r], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def main():
    beta = canonical_matrix()
    rank = rank_f2(beta)
    assert len(beta) == 64 and all(len(row) == 64 for row in beta)
    assert rank == 64, f"canonical map has rank {rank}, expected 64"
    print("basis dimension:", DIM)
    print("canonical-map matrix: 64 x 64 over F_2")
    print("rank:", rank)
    print("determinant:", 1)
    print("PASS: the canonical map is an isomorphism")


if __name__ == "__main__":
    main()
