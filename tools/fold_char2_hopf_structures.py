#!/usr/bin/env python3
"""Verify four Hopf-Galois canonical maps on F_2[x,z]/(x^4,z^2)."""
from math import comb

BASIS = [(i, j) for i in range(4) for j in range(2)]
INDEX = {m: n for n, m in enumerate(BASIS)}
DIM = len(BASIS)


def mul_monomials(a, b):
    i, j = a
    r, s = b
    out = (i + r, j + s)
    return None if out[0] >= 4 or out[1] >= 2 else out


def tensor_mul(a, b):
    left = mul_monomials(a[0], b[0])
    right = mul_monomials(a[1], b[1])
    return None if left is None or right is None else (left, right)


def add_term(poly, term, coefficient=1):
    if term is None:
        return
    poly[term] = (poly.get(term, 0) + coefficient) & 1
    if poly[term] == 0:
        del poly[term]


def tensor_product(p, q):
    out = {}
    for a, ca in p.items():
        for b, cb in q.items():
            add_term(out, tensor_mul(a, b), ca * cb)
    return out


def delta_generator(which, multiplicative):
    one = (0, 0)
    x = (1, 0) if which == "x" else (0, 1)
    out = {(x, one): 1, (one, x): 1}
    if multiplicative:
        out[(x, x)] = 1
    return out


def delta_monomial(monomial, mult_x, mult_z):
    i, j = monomial
    one = (0, 0)
    dx = delta_generator("x", mult_x)
    dz = delta_generator("z", mult_z)
    out = {(one, one): 1}
    for _ in range(i):
        out = tensor_product(out, dx)
    for _ in range(j):
        out = tensor_product(out, dz)
    return out


def canonical_matrix(mult_x, mult_z):
    n = DIM * DIM
    matrix = [[0] * n for _ in range(n)]
    for a in BASIS:
        for b in BASIS:
            col = INDEX[a] * DIM + INDEX[b]
            for (left, right), coeff in delta_monomial(b, mult_x, mult_z).items():
                product = mul_monomials(a, left)
                if product is not None:
                    row = INDEX[product] * DIM + INDEX[right]
                    matrix[row][col] ^= coeff
    return matrix


def rank_f2(matrix):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0])
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
    names = {
        (False, False): "alpha_4 x alpha_2",
        (True, False): "mu_4 x alpha_2",
        (False, True): "alpha_4 x mu_2",
        (True, True): "mu_4 x mu_2",
    }
    for flags, name in names.items():
        matrix = canonical_matrix(*flags)
        rank = rank_f2(matrix)
        assert rank == 64, (name, rank)
        print(f"PASS {name}: canonical-map rank {rank}/64 over F_2")


if __name__ == "__main__":
    main()
