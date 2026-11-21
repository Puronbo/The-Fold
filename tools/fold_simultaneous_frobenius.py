#!/usr/bin/env python3
"""Exact standard-library checks for UF-020."""
from fractions import Fraction

BASIS = ((0, 0), (1, 0), (0, 1), (1, 1),
         (2, 0), (2, 1), (3, 0), (3, 1))
INDEX = {m: i for i, m in enumerate(BASIS)}


def reduce_monomial(a, b):
    """Return (basis exponent, coefficient) for x^a y^b."""
    q, r = divmod(b, 2)
    a += 2 * q  # y^2 = -x^2
    if a >= 4:  # x^4 = 0
        return None, 0
    return (a, r), (-1) ** q


def multiply_basis(i, j):
    (a, b), (c, d) = BASIS[i], BASIS[j]
    monomial, coefficient = reduce_monomial(a + c, b + d)
    if monomial is None:
        return {}
    return {INDEX[monomial]: coefficient}


def determinant(matrix):
    """Exact determinant by fraction-preserving Gaussian elimination."""
    a = [[Fraction(v) for v in row] for row in matrix]
    n = len(a)
    sign, det = 1, Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        value = a[col][col]
        det *= value
        for r in range(col + 1, n):
            factor = a[r][col] / value
            for c in range(col + 1, n):
                a[r][c] -= factor * a[col][c]
    return sign * det


def main():
    assert len(BASIS) == 8 and len(INDEX) == 8
    gram = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            gram[i][j] = multiply_basis(i, j).get(INDEX[(3, 1)], 0)

    expected = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert gram == expected
    assert determinant(gram) == 1

    # Verify the m-adic dimensions from the monomial basis:
    # m^d is spanned by basis monomials of total degree >= d.
    dimensions = tuple(sum(a + b >= d for a, b in BASIS)
                       for d in range(6))
    assert dimensions == (8, 7, 5, 3, 1, 0)
    hilbert = tuple(dimensions[d] - dimensions[d + 1]
                    for d in range(5))
    assert hilbert == (1, 2, 2, 2, 1)

    print("UF-020 exact checks: PASS")
    print("basis size:", len(BASIS))
    print("Frobenius Gram determinant:", determinant(gram))
    print("m-adic dimensions:", dimensions)
    print("Hilbert function:", hilbert)


if __name__ == "__main__":
    main()
