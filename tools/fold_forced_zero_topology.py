#!/usr/bin/env python3
"""UF-007: fixed-point obstructions, minimal D6 semi-invariants, and dual graphs.

The D6 point group acts on the plane with r a 60-degree rotation and s a
reflection in the 15-degree crease. For each one-dimensional real character,
the program verifies an explicit polynomial semi-invariant and its forced
reflection axes. It also checks the dual-graph bipartite criterion for assigning
opposite signs to adjacent crease faces and the induced D6 face character.

Standard library only. Numeric checks verify explicit identities; the note
contains the exact algebraic proofs.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from math import cos, pi, sin
from typing import Iterable, Mapping, Optional

M = 6
ComplexPoint = complex


@dataclass(frozen=True, order=True)
class D6Element:
    rotation: int
    reflection: int

    def __post_init__(self) -> None:
        if not 0 <= self.rotation < M or self.reflection not in (0, 1):
            raise ValueError("invalid D6 element")


def compose(left: D6Element, right: D6Element) -> D6Element:
    """Return left after right, using s r s = r^(-1)."""
    k, e = left.rotation, left.reflection
    ell, f = right.rotation, right.reflection
    return D6Element((k + (-1 if e else 1) * ell) % M, e ^ f)


def act(g: D6Element, z: ComplexPoint) -> ComplexPoint:
    """Apply r^k s^epsilon; r=60 degrees, s is the 15-degree reflection."""
    out = z
    if g.reflection:
        out = complex(cos(pi / 6), sin(pi / 6)) * out.conjugate()
    angle = g.rotation * pi / 3
    return complex(cos(angle), sin(angle)) * out


def character(g: D6Element, name: str) -> int:
    if name == "trivial":
        return 1
    if name == "determinant":
        return -1 if g.reflection else 1
    if name == "sublattice":
        return -1 if g.rotation % 2 else 1
    if name == "mixed":
        return -1 if (g.rotation + g.reflection) % 2 else 1
    raise ValueError(f"unknown character: {name}")


def height(z: complex, name: str) -> float:
    if name == "determinant":
        return (z ** 6).real
    if name == "sublattice":
        return (complex(cos(-pi / 4), sin(-pi / 4)) * (z ** 3)).real
    if name == "mixed":
        return (complex(cos(pi / 4), sin(pi / 4)) * (z ** 3)).real
    raise ValueError(f"no polynomial representative for {name}")


def anti_reflection_axes(name: str) -> tuple[int, ...]:
    """Indices j where sigma_j=r^j s has character -1."""
    return tuple(j for j in range(M) if character(D6Element(j, 1), name) == -1)


def face_dual_bipartition(
    vertices: Iterable[int], edges: Iterable[tuple[int, int]]
) -> Optional[dict[int, int]]:
    """Return a +/-1 face colouring, or None if the dual graph is not bipartite.

    Self-loops are retained and correctly create an obstruction. A disconnected
    dual is supported by seeding each component independently with +1.
    """
    vertex_list = tuple(vertices)
    vertex_set = set(vertex_list)
    adjacency: dict[int, list[int]] = {v: [] for v in vertex_list}
    for u, v in edges:
        if u not in vertex_set or v not in vertex_set:
            raise ValueError("dual edge endpoint is not in vertex set")
        adjacency[u].append(v)
        adjacency[v].append(u)
    signs: dict[int, int] = {}
    for root in vertex_list:
        if root in signs:
            continue
        signs[root] = 1
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                expected = -signs[u]
                if v not in signs:
                    signs[v] = expected
                    queue.append(v)
                elif signs[v] != expected:
                    return None
    return signs


def induced_face_character(
    colouring: Mapping[int, int], permutation: Mapping[int, int]
) -> Optional[int]:
    """Return the global bipartition-preserve/swap sign of an automorphism."""
    signs = {colouring[permutation[v]] * colouring[v] for v in colouring}
    if len(signs) != 1:
        return None
    return next(iter(signs))


def sector_action(name: str, g: D6Element, sector: int) -> int:
    """Action on sectors of the sign-character's forced-axis arrangement."""
    if name == "determinant":
        count, reflection_offset, rotation_shift = 12, 11, 2
    elif name == "sublattice":
        count, reflection_offset, rotation_shift = 6, 4, 1
    elif name == "mixed":
        count, reflection_offset, rotation_shift = 6, 5, 1
    else:
        raise ValueError("sector action only defined for nontrivial characters")
    q = (reflection_offset - sector) % count if g.reflection else sector
    return (q + rotation_shift * g.rotation) % count


def verify() -> dict[str, int]:
    elements = tuple(D6Element(k, e) for k, e in product(range(6), (0, 1)))
    group_checks = character_checks = polynomial_checks = fixed_line_checks = 0
    degree_bound_checks = dual_graph_checks = induced_character_checks = 0
    samples = (0.37 + 0.82j, -1.13 + 0.29j, 0.7 - 1.4j, 1.2 + 0.6j)
    names = ("determinant", "sublattice", "mixed")

    for a in elements:
        for b in elements:
            ab = compose(a, b)
            assert ab in elements
            group_checks += 1
            for name in names:
                assert character(ab, name) == character(a, name) * character(b, name)
                character_checks += 1

    for name in names:
        for g in elements:
            for z in samples:
                lhs = height(act(g, z), name)
                rhs = character(g, name) * height(z, name)
                assert abs(lhs - rhs) < 1e-9, (name, g, z, lhs, rhs)
                polynomial_checks += 1

    expected_degrees = {"determinant": 6, "sublattice": 3, "mixed": 3}
    for name in names:
        axes = anti_reflection_axes(name)
        assert len(axes) == expected_degrees[name]
        for j in axes:
            phi = (2 * j + 1) * pi / 12
            for radius in (0.4, 1.0, 2.1):
                z = radius * complex(cos(phi), sin(phi))
                assert abs(height(z, name)) < 1e-9
                fixed_line_checks += 1
        # The exact zero-set descriptions are in the paper; this checks
        # representative points away from all forced axes are nonzero.
        for theta in (0.013, 0.231, 0.517, 0.901, 1.173, 1.491):
            z = complex(cos(theta), sin(theta))
            distance_to_axes = min(
                abs(((theta - ((2*j+1)*pi/12) + pi/2) % pi) - pi/2)
                for j in axes
            )
            if distance_to_axes > 1e-3:
                assert abs(height(z, name)) > 1e-6
        degree_bound_checks += 1

    # Face-sign consistency iff the dual graph is bipartite.
    c6 = face_dual_bipartition(range(6), ((i, (i+1) % 6) for i in range(6)))
    c12 = face_dual_bipartition(range(12), ((i, (i+1) % 12) for i in range(12)))
    c3 = face_dual_bipartition(range(3), ((0, 1), (1, 2), (2, 0)))
    loop = face_dual_bipartition((0,), ((0, 0),))
    assert c6 is not None and c12 is not None
    assert c3 is None and loop is None
    dual_graph_checks += 4

    # D6 actions on each forced-zero network's sectors induce exactly its
    # corresponding one-dimensional sign character.
    for name in names:
        count = 12 if name == "determinant" else 6
        colouring = face_dual_bipartition(
            range(count), ((i, (i+1) % count) for i in range(count))
        )
        assert colouring is not None
        for g in elements:
            permutation = {i: sector_action(name, g, i) for i in range(count)}
            assert set(permutation.values()) == set(range(count))
            edges = {(i, (i+1) % count) for i in range(count)}
            image_edges = {
                tuple(sorted((permutation[u], permutation[v]))) for u, v in edges
            }
            assert image_edges == {tuple(sorted(edge)) for edge in edges}
            sign = induced_face_character(colouring, permutation)
            assert sign == character(g, name), (name, g, sign, character(g, name))
            induced_character_checks += 1

    return {
        "D6_group_products": group_checks,
        "D6_character_homomorphism_checks": character_checks,
        "polynomial_equivariance_checks": polynomial_checks,
        "forced_fixed_line_samples": fixed_line_checks,
        "polynomial_degree_minimality_cases": degree_bound_checks,
        "dual_graph_bipartite_cases": dual_graph_checks,
        "induced_dual_character_checks": induced_character_checks,
    }


def main() -> None:
    print("D6 sign-character forced-zero and polynomial representatives")
    for name in ("determinant", "sublattice", "mixed"):
        print(
            f"{name:12s} anti-reflection axes={anti_reflection_axes(name)} "
            f"minimal polynomial degree={len(anti_reflection_axes(name))}"
        )
    print("dual graph examples: C6/C12 bipartite; C3/self-loop obstructed")
    print("verification:", verify())


if __name__ == "__main__":
    main()
