#!/usr/bin/env python3
"""Verify the Hopf law Delta(x)=x|1+1|x+z|z, Delta(z)=z|1+1|z."""
BASIS = [(i, j) for i in range(4) for j in range(2)]
INDEX = {m: n for n, m in enumerate(BASIS)}
ONE, X, Z = (0, 0), (1, 0), (0, 1)


def mul_m(a, b):
    q = (a[0] + b[0], a[1] + b[1])
    return None if q[0] >= 4 or q[1] >= 2 else q


def add_term(poly, term, coeff=1):
    if term is None:
        return
    poly[term] = poly.get(term, 0) ^ coeff
    if poly[term] == 0:
        del poly[term]


def tensor_mul(a, b):
    l = mul_m(a[0], b[0])
    r = mul_m(a[1], b[1])
    return None if l is None or r is None else (l, r)


def tensor_product(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            add_term(out, tensor_mul(ma, mb), ca & cb)
    return out


DX = {(X, ONE): 1, (ONE, X): 1, (Z, Z): 1}
DZ = {(Z, ONE): 1, (ONE, Z): 1}


def delta_monomial(m):
    i, j = m
    out = {(ONE, ONE): 1}
    for _ in range(i):
        out = tensor_product(out, DX)
    for _ in range(j):
        out = tensor_product(out, DZ)
    return out


def delta_left(poly):
    out = {}
    for (a, b), coeff in poly.items():
        for (a1, a2), c in delta_monomial(a).items():
            add_term(out, (a1, a2, b), coeff & c)
    return out


def delta_right(poly):
    out = {}
    for (a, b), coeff in poly.items():
        for (b1, b2), c in delta_monomial(b).items():
            add_term(out, (a, b1, b2), coeff & c)
    return out


def rank_f2(matrix):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
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
    return rank


def main():
    for generator, delta in ((X, DX), (Z, DZ)):
        assert delta_left(delta) == delta_right(delta)

    # Delta(x)^4 = Delta(z)^2 = 0.
    dx2 = tensor_product(DX, DX)
    dx4 = tensor_product(tensor_product(dx2, dx2), {(ONE, ONE): 1})
    dz2 = tensor_product(DZ, DZ)
    assert not dx4 and not dz2

    # Counit and antipode on generators; S is the identity.
    for generator, delta in ((X, DX), (Z, DZ)):
        left_counit, right_counit, antipode = {}, {}, {}
        for (left, right), coeff in delta.items():
            if left == ONE:
                add_term(left_counit, right, coeff)
            if right == ONE:
                add_term(right_counit, left, coeff)
            add_term(antipode, mul_m(left, right), coeff)
        assert left_counit == {generator: 1}
        assert right_counit == {generator: 1}
        assert not antipode

    # Primitive-space dimension.
    matrix = [[0] * 8 for _ in range(64)]
    for col, monomial in enumerate(BASIS):
        q = delta_monomial(monomial)
        add_term(q, (monomial, ONE))
        add_term(q, (ONE, monomial))
        for (left, right), coeff in q.items():
            matrix[INDEX[left] * 8 + INDEX[right]][col] = coeff
    dimension = 8 - rank_f2(matrix)
    assert dimension == 2, dimension

    print("PASS: coassociativity, relations, counit, and antipode")
    print("PASS: primitive-space dimension =", dimension)
    print("Primitive basis: z, x^2")


if __name__ == "__main__":
    main()
