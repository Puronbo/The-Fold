#!/usr/bin/env python3
"""UF-008: smooth/analytic realizability and vanishing-order verification.

Tests square and triangular periodic analytic crease heights, the D6 action on
the triangular torus, and Fourier-projected representatives for all four real
one-dimensional D6 characters. Standard library only.
"""
from __future__ import annotations

from cmath import exp as cexp
from itertools import product
from math import ceil, pi, sin, sqrt
from typing import Callable

Matrix = tuple[int, int, int, int]
Point = tuple[float, float]
IDENTITY: Matrix = (1, 0, 0, 1)
TRIANGULAR_GRAM = (2, 1, 2)
SQUARE_GRAM = (1, 0, 1)


def det(A: Matrix) -> int:
    a, b, c, d = A
    return a * d - b * c


def mul(A: Matrix, B: Matrix) -> Matrix:
    a, b, c, d = A
    e, f, g, h = B
    return (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)


def matvec(A: Matrix, p: Point) -> Point:
    a, b, c, d = A
    x, y = p
    return (a*x+b*y, c*x+d*y)


def quadratic(G: tuple[int, int, int], x: tuple[int, int], y: tuple[int, int]) -> int:
    g11, g12, g22 = G
    return g11*x[0]*y[0] + g12*(x[0]*y[1]+x[1]*y[0]) + g22*x[1]*y[1]


def preserves_metric(A: Matrix, G: tuple[int, int, int]) -> bool:
    e1, e2 = (A[0], A[2]), (A[1], A[3])
    return (
        abs(det(A)) == 1
        and quadratic(G, e1, e1) == G[0]
        and quadratic(G, e1, e2) == G[1]
        and quadratic(G, e2, e2) == G[2]
    )


def entry_bound(G: tuple[int, int, int]) -> int:
    g11, g12, g22 = G
    disc = (g11-g22)**2 + 4*g12**2
    lam_min = (g11+g22-sqrt(disc))/2
    if lam_min <= 0:
        raise ValueError("Gram matrix must be positive definite")
    return max(1, ceil(sqrt(max(g11, g22)/lam_min))+1)


def lattice_point_group(G: tuple[int, int, int]) -> tuple[Matrix, ...]:
    bound = entry_bound(G)
    return tuple(sorted({
        A for A in product(range(-bound, bound+1), repeat=4)
        if preserves_metric(A, G)
    }))


def inverse_matrix(A: Matrix) -> Matrix:
    a, b, c, d = A
    D = det(A)
    if abs(D) != 1:
        raise ValueError("matrix must be unimodular")
    return (d//D, -b//D, -c//D, a//D)


def h_square(x: float, y: float) -> float:
    return sin(2*pi*x)*sin(2*pi*y)


def h_triangular(x: float, y: float) -> float:
    return sin(2*pi*x)*sin(2*pi*y)*sin(2*pi*(x+y))


def d6_character(A: Matrix, name: str) -> int:
    """Evaluate a D6 character for r=(-y,x+y), s=(-x-y,y)."""
    r: Matrix = (0, -1, 1, 1)
    s: Matrix = (-1, -1, 0, 1)
    chars = {
        "trivial": (1, 1),
        "determinant": (1, -1),
        "sublattice": (-1, 1),
        "mixed": (-1, -1),
    }
    if name not in chars:
        raise ValueError(f"unknown D6 character: {name}")
    cr, cs = chars[name]
    power = IDENTITY
    for j in range(6):
        if power == A:
            return cr**j
        if mul(power, s) == A:
            return cr**j * cs
        power = mul(power, r)
    raise ValueError("matrix is not in this D6 representation")


def fourier_projection(x: float, y: float, name: str,
                       k: tuple[int, int] = (1, 3)) -> complex:
    """Project a generic torus Fourier mode into a D6 character space."""
    total = 0j
    for A in lattice_point_group(TRIANGULAR_GRAM):
        inv = inverse_matrix(A)
        # Dual action k -> A^{-T}k.
        freq = (inv[0]*k[0]+inv[2]*k[1], inv[1]*k[0]+inv[3]*k[1])
        total += d6_character(A, name)*cexp(2j*pi*(freq[0]*x+freq[1]*y))
    return total


def semi_invariant_sign(h: Callable[[float, float], float], A: Matrix) -> int | None:
    samples = ((.137,.271), (.193,.347), (.311,.127), (.227,.419))
    signs: set[int] = set()
    for x, y in samples:
        before = h(x, y)
        after = h(*matvec(A, (x, y)))
        if abs(before) < 1e-9 or abs(after) < 1e-9:
            continue
        ratio = after/before
        if abs(ratio-1) < 1e-8:
            signs.add(1)
        elif abs(ratio+1) < 1e-8:
            signs.add(-1)
        else:
            return None
    return next(iter(signs)) if len(signs) == 1 else None


def verify() -> dict[str, int]:
    square_group = lattice_point_group(SQUARE_GRAM)
    tri_group = lattice_point_group(TRIANGULAR_GRAM)
    assert len(square_group) == 8
    assert len(tri_group) == 12

    closure_checks = 0
    for group in (square_group, tri_group):
        members = set(group)
        for A in group:
            assert any(mul(A, B) == IDENTITY for B in group)
            for B in group:
                assert mul(A, B) in members
                closure_checks += 1

    # D6 presentation and the triangular lattice's 60-degree generator.
    r: Matrix = (0, -1, 1, 1)
    s: Matrix = (-1, -1, 0, 1)
    assert r in tri_group and s in tri_group
    r2, r3 = mul(r, r), mul(mul(r, r), r)
    assert r2 != IDENTITY and r3 != IDENTITY and mul(r3, r3) == IDENTITY
    assert mul(s, s) == IDENTITY
    assert mul(mul(mul(s, r), s), r) == IDENTITY

    tri_signs = {A: semi_invariant_sign(h_triangular, A) for A in tri_group}
    square_signs = {A: semi_invariant_sign(h_square, A) for A in square_group}
    assert all(v in (-1, 1) for v in tri_signs.values())
    assert all(v in (-1, 1) for v in square_signs.values())
    assert tri_signs[r] == -1 and tri_signs[s] == 1

    character_checks = 0
    for group, signs in ((tri_group, tri_signs), (square_group, square_signs)):
        for A in group:
            for B in group:
                assert signs[mul(A, B)] == signs[A]*signs[B]
                character_checks += 1

    # A generic dual frequency has a free D6 orbit (12 distinct frequencies).
    orbit = set()
    for A in tri_group:
        inv = inverse_matrix(A)
        orbit.add((inv[0]+3*inv[2], inv[1]+3*inv[3]))
    assert len(orbit) == 12

    # Every real one-dimensional D6 character has a nonzero analytic Fourier
    # representative; check its semi-invariance at all group/sample pairs.
    fourier_checks = 0
    samples = ((.173,.287), (.119,.391), (.263,.137), (.311,.127))
    for name in ("trivial", "determinant", "sublattice", "mixed"):
        vals = [fourier_projection(x, y, name) for x, y in samples]
        assert any(abs(v) > 1e-8 for v in vals)
        for A in tri_group:
            sign = d6_character(A, name)
            for x, y in samples:
                lhs = fourier_projection(*matvec(A, (x,y)), name)
                rhs = sign*fourier_projection(x, y, name)
                assert abs(lhs-rhs) < 1e-8
                fourier_checks += 1

    # Exact periodic zero-set samples for the square and triangular products.
    zero_checks = 0
    for x in (0,.5,1,1.5):
        for y in (.13,.37,.81):
            assert abs(h_square(x,y)) < 1e-10
            zero_checks += 1
    for y in (0,.5,1,1.5):
        for x in (.17,.43,.79):
            assert abs(h_square(x,y)) < 1e-10
            zero_checks += 1
    for x in (0,.5,1,1.5):
        for y in (.17,.43,.79):
            assert abs(h_triangular(x,y)) < 1e-10
            zero_checks += 1
    for y in (0,.5,1,1.5):
        for x in (.13,.39,.73):
            assert abs(h_triangular(x,y)) < 1e-10
            zero_checks += 1
    for t in (.13,.37,.81):
        assert abs(h_triangular(t,-t)) < 1e-10
        assert abs(h_triangular(t,.5-t)) < 1e-10
        zero_checks += 2

    # Taylor leading orders 2 and 3 at the square crossing and triangular
    # triple vertex, respectively.
    taylor_checks = 0
    u, v = .37, -.61
    for eps in (1e-2,5e-3,2e-3,1e-3):
        square_lead = (2*pi)**2*u*v
        tri_lead = (2*pi)**3*u*v*(u+v)
        assert abs(h_square(eps*u,eps*v)/eps**2-square_lead) < 4e-3
        assert abs(h_triangular(eps*u,eps*v)/eps**3-tri_lead) < 1e-1
        taylor_checks += 2
    eps = 1e-5
    leading = (2*pi)**3*eps*(2*eps)*(3*eps)
    assert abs(h_triangular(eps,2*eps)/leading-1) < 1e-7
    taylor_checks += 1

    return {
        "square_lattice_point_group_order": len(square_group),
        "triangular_lattice_point_group_order": len(tri_group),
        "point_group_closure_and_inverse_checks": closure_checks,
        "D6_generator_relation_checks": 4,
        "point_group_character_checks": character_checks,
        "Fourier_projector_character_checks": fourier_checks,
        "nonzero_dual_orbit_frequencies": len(orbit),
        "periodic_zero_set_samples": zero_checks,
        "Taylor_vanishing_order_checks": taylor_checks,
    }


def main() -> None:
    square_group = lattice_point_group(SQUARE_GRAM)
    tri_group = lattice_point_group(TRIANGULAR_GRAM)
    r: Matrix = (0,-1,1,1)
    s: Matrix = (-1,-1,0,1)
    print("square point group:", len(square_group),
          "height signs:", sorted(set(semi_invariant_sign(h_square,A) for A in square_group)))
    print("triangular point group:", len(tri_group),
          "height signs:", sorted(set(semi_invariant_sign(h_triangular,A) for A in tri_group)))
    print("triangular D6 generators: chi(r)=", semi_invariant_sign(h_triangular,r),
          "chi(s)=", semi_invariant_sign(h_triangular,s))
    print("Fourier representatives exist for:",
          ("trivial", "determinant", "sublattice", "mixed"))
    print("verification:", verify())


if __name__ == "__main__":
    main()
