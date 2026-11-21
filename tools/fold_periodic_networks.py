#!/usr/bin/env python3
"""UF-005: symmetry groups and sign characters of finite periodic crease nets.

Exact finite-torus model: affine symmetries x -> A x + b (mod N), where A is
an integral isometry of a 2D lattice Gram matrix and b is a torus translation.
The motif has vertices, crease-crossing bonds, and optional signed fields.

This is a finite reference model, not a complete classifier of all 17 wallpaper
groups or a substitute for continuous geometric verification.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import ceil, sqrt
from typing import Iterable, Mapping, Optional

Point = tuple[int, int]
Matrix = tuple[int, int, int, int]
Edge = tuple[Point, Point]
Gram = tuple[int, int, int]


def det(A: Matrix) -> int:
    a, b, c, d = A
    return a * d - b * c


def matmul(A: Matrix, B: Matrix) -> Matrix:
    a, b, c, d = A
    e, f, g, h = B
    return (a * e + b * g, a * f + b * h,
            c * e + d * g, c * f + d * h)


def matvec(A: Matrix, x: Point) -> Point:
    a, b, c, d = A
    u, v = x
    return (a * u + b * v, c * u + d * v)


def quadratic(G: Gram, x: Point, y: Point) -> int:
    g11, g12, g22 = G
    return (g11 * x[0] * y[0] + g12 * (x[0] * y[1] + x[1] * y[0])
            + g22 * x[1] * y[1])


def preserves_metric(A: Matrix, G: Gram) -> bool:
    e1, e2 = matvec(A, (1, 0)), matvec(A, (0, 1))
    return (
        quadratic(G, e1, e1) == G[0]
        and quadratic(G, e1, e2) == G[1]
        and quadratic(G, e2, e2) == G[2]
        and abs(det(A)) == 1
    )


def _entry_bound(G: Gram) -> int:
    """Finite coefficient bound from the least eigenvalue of the Gram matrix."""
    g11, g12, g22 = G
    discriminant = (g11 - g22) ** 2 + 4 * g12 ** 2
    lambda_min = (g11 + g22 - sqrt(discriminant)) / 2
    if lambda_min <= 0:
        raise ValueError("Gram matrix must be positive definite")
    return max(1, ceil(sqrt(max(g11, g22) / lambda_min)))


def lattice_point_group(G: Gram) -> tuple[Matrix, ...]:
    """Enumerate A in GL(2,Z) with A^T G A = G."""
    bound = _entry_bound(G)
    result = []
    for a, b, c, d in product(range(-bound, bound + 1), repeat=4):
        A = (a, b, c, d)
        if abs(det(A)) == 1 and preserves_metric(A, G):
            result.append(A)
    return tuple(sorted(set(result)))


def torus_point(N: int, p: Point) -> Point:
    return (p[0] % N, p[1] % N)


def canonical_edge(N: int, u: Point, v: Point) -> Edge:
    a, b = torus_point(N, u), torus_point(N, v)
    if a == b:
        raise ValueError("loops are not represented by this simple-edge model")
    return (a, b) if a < b else (b, a)


@dataclass(frozen=True, order=True)
class AffineSymmetry:
    A: Matrix
    b: Point


def apply_affine(N: int, g: AffineSymmetry, p: Point) -> Point:
    q = matvec(g.A, p)
    return ((q[0] + g.b[0]) % N, (q[1] + g.b[1]) % N)


def compose_affine(N: int, left: AffineSymmetry, right: AffineSymmetry) -> AffineSymmetry:
    """Composition left after right."""
    A = matmul(left.A, right.A)
    Ab = matvec(left.A, right.b)
    b = ((Ab[0] + left.b[0]) % N, (Ab[1] + left.b[1]) % N)
    return AffineSymmetry(A, b)


def inverse_matrix(A: Matrix) -> Matrix:
    a, b, c, d = A
    determinant = det(A)
    if abs(determinant) != 1:
        raise ValueError("matrix is not unimodular")
    return (d // determinant, -b // determinant,
            -c // determinant, a // determinant)


def inverse_affine(N: int, g: AffineSymmetry) -> AffineSymmetry:
    Ai = inverse_matrix(g.A)
    q = matvec(Ai, g.b)
    return AffineSymmetry(Ai, ((-q[0]) % N, (-q[1]) % N))


@dataclass(frozen=True)
class PeriodicCreaseNetwork:
    N: int
    gram: Gram
    vertices: frozenset[Point]
    crease_bonds: frozenset[Edge]
    height: Optional[Mapping[Point, int]] = None
    colour: Optional[Mapping[Point, int]] = None

    def __post_init__(self) -> None:
        if self.N < 2:
            raise ValueError("N must be at least 2")
        if not self.vertices:
            raise ValueError("network needs at least one vertex")
        for p in self.vertices:
            if torus_point(self.N, p) != p:
                raise ValueError("vertices must be canonical torus points")
        for u, v in self.crease_bonds:
            if u not in self.vertices or v not in self.vertices:
                raise ValueError("crease bond endpoint is not a network vertex")
        for name, field in (("height", self.height), ("colour", self.colour)):
            if field is not None:
                if set(field) != set(self.vertices):
                    raise ValueError(f"{name} field must be defined on every vertex")
                if any(value not in (-1, 0, 1) for value in field.values()):
                    raise ValueError(f"{name} values must be -1, 0, or +1")
                if not any(field.values()):
                    raise ValueError(f"{name} field cannot be identically zero")


def _mapped_edges(N: int, g: AffineSymmetry, edges: Iterable[Edge]) -> frozenset[Edge]:
    return frozenset(
        canonical_edge(N, apply_affine(N, g, u), apply_affine(N, g, v))
        for u, v in edges
    )


def field_sign(
    N: int, g: AffineSymmetry, vertices: Iterable[Point],
    field: Optional[Mapping[Point, int]]
) -> Optional[int]:
    """Return chi if f(gx)=chi*f(x) globally, otherwise None."""
    if field is None:
        return 1
    signs: set[int] = set()
    for p in vertices:
        before = field[p]
        after = field[apply_affine(N, g, p)]
        if before == 0 or after == 0:
            if before != after:
                return None
            continue
        signs.add(after * before)
    if len(signs) != 1:
        return None
    return next(iter(signs))


def candidate_affine_group(network: PeriodicCreaseNetwork) -> tuple[AffineSymmetry, ...]:
    point_group = lattice_point_group(network.gram)
    return tuple(
        AffineSymmetry(A, (u, v))
        for A in point_group
        for u in range(network.N)
        for v in range(network.N)
    )


def network_symmetries(network: PeriodicCreaseNetwork) -> tuple[AffineSymmetry, ...]:
    """Affine torus isometries preserving the vertices and crease-crossing bonds."""
    out = []
    V = network.vertices
    for g in candidate_affine_group(network):
        mapped_vertices = frozenset(apply_affine(network.N, g, p) for p in V)
        if mapped_vertices != V:
            continue
        if _mapped_edges(network.N, g, network.crease_bonds) != network.crease_bonds:
            continue
        out.append(g)
    return tuple(out)


def sign_symmetries(
    network: PeriodicCreaseNetwork,
    require_height: bool = True,
    require_colour: bool = True,
) -> tuple[tuple[AffineSymmetry, int, int], ...]:
    """Symmetries carrying each requested field to itself up to one global sign."""
    out = []
    for g in network_symmetries(network):
        height_sign = field_sign(network.N, g, network.vertices, network.height) if require_height else 1
        colour_sign = field_sign(network.N, g, network.vertices, network.colour) if require_colour else 1
        if height_sign is not None and colour_sign is not None:
            out.append((g, height_sign, colour_sign))
    return tuple(out)


def character_image(
    symmetries: Iterable[tuple[AffineSymmetry, int, int]]
) -> frozenset[tuple[int, int]]:
    return frozenset((height_sign, colour_sign)
                     for _, height_sign, colour_sign in symmetries)


def checkerboard_square_example(N: int = 4) -> PeriodicCreaseNetwork:
    """Square torus with stripe creases and independent height/colour signs.

    h(x,y)=(-1)^x; marked bonds cross each h-zero line. The independent
    site decoration c(x,y)=(-1)^y supplies a second sign character.
    """
    if N % 2:
        raise ValueError("checkerboard example needs even N")
    vertices = frozenset((x, y) for x in range(N) for y in range(N))
    height = {p: (-1) ** p[0] for p in vertices}
    colour = {p: (-1) ** p[1] for p in vertices}
    bonds = set()
    for x, y in vertices:
        u, v = (x, y), ((x + 1) % N, y)
        if height[u] != height[v]:
            bonds.add(canonical_edge(N, u, v))
    return PeriodicCreaseNetwork(
        N, (1, 0, 1), vertices, frozenset(bonds), height, colour
    )


def triangular_lattice_example(N: int = 4) -> PeriodicCreaseNetwork:
    """Uncoloured triangular Bravais net with nearest-neighbour bonds."""
    vertices = frozenset((x, y) for x in range(N) for y in range(N))
    bonds = set()
    directions = ((1, 0), (0, 1), (1, -1))
    for x, y in vertices:
        for dx, dy in directions:
            bonds.add(canonical_edge(N, (x, y), (x + dx, y + dy)))
    return PeriodicCreaseNetwork(N, (2, 1, 2), vertices, frozenset(bonds))


def verify() -> dict[str, int]:
    square_group = lattice_point_group((1, 0, 1))
    hex_group = lattice_point_group((2, 1, 2))
    oblique_group = lattice_point_group((4, 1, 7))
    assert len(square_group) == 8
    assert len(hex_group) == 12
    assert len(oblique_group) == 2

    square = checkerboard_square_example(4)
    network_group = network_symmetries(square)
    joint_group = sign_symmetries(square)
    assert len(network_group) == 64
    assert len(joint_group) == 64
    image = character_image(joint_group)
    assert image == frozenset({(1, 1), (1, -1), (-1, 1), (-1, -1)})
    kernel = [g for g, h, c in joint_group if h == c == 1]
    assert len(kernel) == 16

    # Check closure and the two character laws for all group-element pairs.
    character_map = {g: (h, c) for g, h, c in joint_group}
    character_checks = 0
    for left in joint_group:
        for right in joint_group:
            product_g = compose_affine(square.N, left[0], right[0])
            assert product_g in character_map
            assert character_map[product_g] == (left[1] * right[1], left[2] * right[2])
            character_checks += 1

    action_checks = 0
    for g, _, _ in joint_group:
        inv = inverse_affine(square.N, g)
        for point in square.vertices:
            assert apply_affine(square.N, inv, apply_affine(square.N, g, point)) == point
            action_checks += 1

    triangle = triangular_lattice_example(4)
    triangular_group = network_symmetries(triangle)
    assert len(triangular_group) == 12 * 16
    nearest_neighbour = {
        (1, 0), (0, 1), (1, -1), (-1, 0), (0, -1), (-1, 1)
    }
    for A in hex_group:
        assert {matvec(A, v) for v in nearest_neighbour} == nearest_neighbour

    return {
        "square_lattice_point_group": len(square_group),
        "hexagonal_lattice_point_group": len(hex_group),
        "generic_oblique_point_group": len(oblique_group),
        "square_periodic_network_symmetries": len(network_group),
        "joint_sign_symmetry_subgroup": len(joint_group),
        "independent_sign_character_image": len(image),
        "joint_sign_kernel": len(kernel),
        "character_homomorphism_checks": character_checks,
        "affine_inverse_action_checks": action_checks,
        "triangular_periodic_net_symmetries": len(triangular_group),
    }


def main() -> None:
    print("point-group orders: square / hexagonal / generic oblique =",
          len(lattice_point_group((1, 0, 1))),
          len(lattice_point_group((2, 1, 2))),
          len(lattice_point_group((4, 1, 7))))
    network = checkerboard_square_example(4)
    symmetries = sign_symmetries(network)
    print("square periodic crease graph symmetries:", len(network_symmetries(network)))
    print("height+colour sign symmetries:", len(symmetries))
    print("height/colour sign image:", sorted(character_image(symmetries)))
    print("common sign-preserving kernel:", sum(h == c == 1 for _, h, c in symmetries))
    print("bounded verification:", verify())


if __name__ == "__main__":
    main()
