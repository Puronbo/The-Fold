#!/usr/bin/env python3
"""Exact UF-062A symbolic rank-drop calculation; requires SymPy."""
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import GF

A, B, C, D, E, G, J = sp.symbols("A B C D E G J")
PARAMS = (A, B, C, D, E, G, J)
ZERO = sp.Poly(0, *PARAMS, modulus=2)
ONE = sp.Poly(1, *PARAMS, modulus=2)
BOUNDS = (4, 2, 4, 2, 2)  # x,z,c,d,h
NAMES = ("x", "z", "c", "d", "h")


def clean(poly):
    return {m: v for m, v in poly.items()
            if not v.is_zero and all(e < b for e, b in zip(m, BOUNDS))}


def const(value=ONE):
    return {(0, 0, 0, 0, 0): value} if not value.is_zero else {}


def var(index):
    e = [0] * 5
    e[index] = 1
    return {tuple(e): ONE}


def scale(poly, scalar):
    p = sp.Poly(scalar, *PARAMS, modulus=2)
    return {m: v * p for m, v in poly.items() if not (v * p).is_zero}


def add(*polys):
    out = {}
    for poly in polys:
        for m, v in poly.items():
            out[m] = out.get(m, ZERO) + v
    return clean(out)


def mul(left, right):
    out = {}
    for m, a in left.items():
        for n, b in right.items():
            q = tuple(x + y for x, y in zip(m, n))
            if all(e < bound for e, bound in zip(q, BOUNDS)):
                out[q] = out.get(q, ZERO) + a * b
    return clean(out)


def power(poly, n):
    out = const()
    for _ in range(n):
        out = mul(out, poly)
    return out


X, Z, Cc, Dd, Hh = [var(i) for i in range(5)]


def apply_g(poly):
    gx = add(X, Cc)
    gz = add(Z, Dd, mul(Hh, X))
    out = {}
    for exponents, coefficient in poly.items():
        term = const(coefficient)
        for _ in range(exponents[0]):
            term = mul(term, gx)
        for _ in range(exponents[1]):
            term = mul(term, gz)
        for index in range(2, 5):
            for _ in range(exponents[index]):
                term = mul(term, var(index))
        out = add(out, term)
    return out


def coefficient(poly, exponents):
    return poly.get(exponents, ZERO).as_expr()


def main():
    ux = add(
        X, scale(power(X, 2), A), scale(power(X, 3), B),
        scale(mul(X, Z), C), scale(mul(power(X, 2), Z), D),
        scale(mul(power(X, 3), Z), E),
    )
    uz = add(
        Z, scale(mul(X, Z), A), scale(power(X, 3), G),
        scale(mul(power(X, 2), Z), B + G),
        scale(mul(power(X, 3), Z), J),
    )
    g_ux = apply_g(ux)
    x_prime = add(g_ux, Cc)
    z_prime = add(apply_g(uz), Dd, mul(Hh, g_ux), mul(Hh, Cc))

    target_basis = [
        (0, 0), (1, 0), (0, 1), (2, 0),
        (3, 0), (1, 1), (2, 1), (3, 1),
    ]
    nil_basis = [
        (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
        (2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1),
        (3, 0, 0), (3, 0, 1), (3, 1, 0), (3, 1, 1),
    ]
    rows = []
    for coordinate in (x_prime, z_prime):
        for xz in target_basis:
            rows.append([
                coefficient(coordinate, xz + nil) for nil in nil_basis
            ])
    matrix = sp.Matrix(rows)
    assert matrix.shape == (16, 15)

    maximal_minors = []
    for omitted in range(16):
        submatrix = matrix[[r for r in range(16) if r != omitted], :]
        determinant = sp.Poly(
            sp.expand(submatrix.det(method="domain-ge")),
            *PARAMS, modulus=2
        )
        maximal_minors.append(determinant)

    for omitted, determinant in enumerate(maximal_minors):
        expected = sp.Poly(E**15, *PARAMS, modulus=2) if omitted == 7 else ZERO
        assert determinant == expected, (omitted, determinant.as_expr())

    matrix_e0 = matrix.subs(E, 0)
    field = GF(2).frac_field(A, B, C, D, G, J)
    generic_rank = DomainMatrix.from_Matrix(matrix_e0).convert_to(field).rank()
    assert generic_rank == 11, generic_rank

    rows11 = [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 13]
    cols11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12]
    minor11 = matrix_e0.extract(rows11, cols11)
    determinant11 = sp.Poly(
        sp.expand(minor11.det(method="domain-ge")),
        A, B, C, D, G, J, modulus=2
    )
    expected11 = sp.Poly(C**3 * D**4 * J**4, A, B, C, D, G, J, modulus=2)
    assert determinant11 == expected11, determinant11.as_expr()

    print("PASS: maximal-minor ideal is (E^15)")
    print("PASS: only nonzero 15x15 minor omits epsilon'")
    print("PASS: generic rank on E=0 is", generic_rank)
    print("PASS: displayed 11x11 minor is C^3 D^4 J^4")


if __name__ == "__main__":
    main()
