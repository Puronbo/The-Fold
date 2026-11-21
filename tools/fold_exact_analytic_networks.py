#!/usr/bin/env python3
"""UF-009: exact analytic zero sets for paired rational crease families.

On T^2=R^2/Z^2, for each primitive integer covector n_j and an even set
of distinct levels c_{j,l} modulo one, the product
    H(x)=prod_j prod_l sin(pi*(n_j dot x-c_{j,l}))
is periodic, real analytic, and has exactly the prescribed affine circles
as its zero set. It changes sign across each regular crease.

The program also verifies character-weighted symmetrization of the exact
triangular D6 height. Standard library only.
"""
from __future__ import annotations

from itertools import product
from math import pi, sin, cos

Point = tuple[float, float]
Covector = tuple[int, int]
Matrix = tuple[int, int, int, int]
IDENTITY: Matrix = (1, 0, 0, 1)


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def line_family_factor(x: Point, normal: Covector, levels: tuple[float, ...]) -> float:
    if normal == (0, 0) or gcd(abs(normal[0]), abs(normal[1])) != 1:
        raise ValueError("normal must be a nonzero primitive integer covector")
    if not levels or len(levels) % 2:
        raise ValueError("a periodic scalar factor needs a positive even number of levels")
    normalized = tuple(c % 1.0 for c in levels)
    if len({round(c, 12) for c in normalized}) != len(normalized):
        raise ValueError("levels must be distinct modulo one")
    q = normal[0] * x[0] + normal[1] * x[1]
    value = 1.0
    for c in levels:
        value *= sin(pi * (q - c))
    return value


def exact_line_arrangement(
    x: Point, families: tuple[tuple[Covector, tuple[float, ...]], ...]
) -> float:
    if not families:
        raise ValueError("at least one crease family is required")
    value = 1.0
    seen: list[Covector] = []
    for normal, levels in families:
        if any(normal[0] * old[1] == normal[1] * old[0] for old in seen):
            raise ValueError("family directions must be pairwise nonparallel")
        seen.append(normal)
        value *= line_family_factor(x, normal, levels)
    return value


def triangular_height(x: float, y: float) -> float:
    return sin(2*pi*x) * sin(2*pi*y) * sin(2*pi*(x+y))


def matrix_mul(A: Matrix, B: Matrix) -> Matrix:
    a,b,c,d=A; e,f,g,h=B
    return (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)


def matrix_apply(A: Matrix, x: Point) -> Point:
    a,b,c,d=A; u,v=x
    return (a*u+b*v, c*u+d*v)


def d6_elements() -> tuple[tuple[int, int, Matrix], ...]:
    """Return (k,epsilon,r^k s^epsilon) in triangular lattice coordinates."""
    r: Matrix = (0,-1,1,1)
    s: Matrix = (-1,-1,0,1)
    power = IDENTITY
    result = []
    for k in range(6):
        result.append((k,0,power))
        a,b,c,d=power; e,f,g,h=s
        reflected=(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
        result.append((k,1,reflected))
        power=matrix_mul(power,r)
    return tuple(result)


def symmetrized_triangular_height(x: float, y: float) -> float:
    """Exact-zero D6-equivariant sum using a strictly positive analytic weight."""
    total = 0.0
    for k, epsilon, A in d6_elements():
        u,v = matrix_apply(A,(x,y))
        weight = 2.0 + cos(2*pi*u) + 0.3*sin(2*pi*v)  # >= 0.7
        chi = (-1)**k  # chi(r)=-1, chi(s)=+1
        total += chi * weight * triangular_height(u,v)
    return total


def verify() -> dict[str,int]:
    square = (((1,0),(0.0,0.5)),((0,1),(0.0,0.5)))
    triangle = (((1,0),(0.0,0.5)),((0,1),(0.0,0.5)),((1,1),(0.0,0.5)))
    samples=((.137,.271),(.193,.347),(.311,.127),(.227,.419))
    periodicity=nonzero=zero_square=zero_triangle=0

    for families in (square,triangle):
        for x,y in samples:
            h=exact_line_arrangement((x,y),families)
            assert abs(h)>1e-10
            nonzero+=1
            for m in range(-2,3):
                assert abs(exact_line_arrangement((x+m,y),families)-h)<1e-9
                assert abs(exact_line_arrangement((x,y+m),families)-h)<1e-9
                periodicity+=2

    for t in (.13,.27,.41,.73):
        for x,y in ((0,t),(.5,t),(t,0),(t,.5)):
            assert abs(exact_line_arrangement((x,y),square))<1e-10
            zero_square+=1
        for x,y in ((0,t),(.5,t),(t,0),(t,.5),(t,-t),(t,.5-t)):
            assert abs(exact_line_arrangement((x,y),triangle))<1e-10
            zero_triangle+=1

    for x,y in samples:
        hs=exact_line_arrangement((x,y),square)
        ht=exact_line_arrangement((x,y),triangle)
        assert abs(hs-.25*sin(2*pi*x)*sin(2*pi*y))<1e-9
        assert abs(ht+.125*triangular_height(x,y))<1e-9

    r: Matrix=(0,-1,1,1)
    s: Matrix=(-1,-1,0,1)
    power=IDENTITY
    for _ in range(6):
        power=matrix_mul(power,r)
    assert power==IDENTITY
    assert matrix_mul(s,s)==IDENTITY
    assert matrix_mul(matrix_mul(matrix_mul(s,r),s),r)==IDENTITY
    relation_checks=4

    seed_checks=average_checks=equivariance_checks=0
    for k,eps,A in d6_elements():
        chi=(-1)**k
        for x,y in samples:
            u,v=matrix_apply(A,(x,y))
            assert abs(triangular_height(u,v)-chi*triangular_height(x,y))<1e-9
            seed_checks+=1
            seed=triangular_height(x,y)
            averaged=symmetrized_triangular_height(x,y)
            assert averaged*seed>0
            average_checks+=1
            transformed=symmetrized_triangular_height(u,v)
            assert abs(transformed-chi*averaged)<1e-8
            equivariance_checks+=1

    return {
        "square_exact_zero_samples":zero_square,
        "triangular_exact_zero_samples":zero_triangle,
        "integer_translation_periodicity_checks":periodicity,
        "generic_nonzero_samples":nonzero,
        "D6_relation_checks":relation_checks,
        "triangular_seed_equivariance_checks":seed_checks,
        "symmetrized_exact_zero_checks":average_checks,
        "symmetrized_D6_equivariance_checks":equivariance_checks,
    }


def main() -> None:
    print("square exact product = (1/4) sin(2pi x) sin(2pi y)")
    print("triangular exact product = (-1/8) sin(2pi x) sin(2pi y) sin(2pi(x+y))")
    print("character-weighted D6 average preserves the exact triangular zero set")
    print("verification:",verify())


if __name__ == "__main__":
    main()
