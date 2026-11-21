#!/usr/bin/env python3
"""UF-004: hexagonal lattice crease axes and the two D6 sign characters.

For h(z)=Re(z**6), the six zero lines are phi_j=pi/12+j*pi/6.
Reflection in each line is a Fold involution and sends h to -h. The
unlabelled honeycomb point group is D6. Alternating A/B labels on the
six vertices define a second character: a 60-degree rotation swaps A/B,
while the reflection through an opposite-vertex axis preserves them.

The arithmetic Frobenius-power model is not used here. Standard library only.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cos, gcd, pi, sin
from typing import Iterable

M = 6


@dataclass(frozen=True, order=True)
class D6Element:
    """An element r^k s^epsilon; s reflects in the 15-degree base crease."""
    rotation: int
    reflection: int

    def __post_init__(self) -> None:
        if not 0 <= self.rotation < M or self.reflection not in (0, 1):
            raise ValueError("invalid D6 element")


def multiply(left: D6Element, right: D6Element) -> D6Element:
    """Group product left * right, using s r s = r^(-1)."""
    k, e = left.rotation, left.reflection
    ell, f = right.rotation, right.reflection
    return D6Element((k + (-1 if e else 1) * ell) % M, e ^ f)


def inverse(x: D6Element) -> D6Element:
    return D6Element(x.rotation if x.reflection else (-x.rotation) % M,
                     x.reflection)


def closure(generators: Iterable[D6Element]) -> frozenset[D6Element]:
    identity = D6Element(0, 0)
    gens = tuple(generators)
    seen = {identity}
    todo = [identity]
    while todo:
        x = todo.pop()
        for g in gens:
            for y in (multiply(x, g), multiply(g, x)):
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
    return frozenset(seen)


def crease_angle(j: int) -> float:
    """The j-th h=Re(z^6) zero line, modulo pi: 15 + 30j degrees."""
    return pi / 12 + (j % M) * pi / M


def crease_reflection(j: int) -> D6Element:
    """Reflection across crease j; in D6 coordinates it is r^j s."""
    return D6Element(j % M, 1)


def apply_element(element: D6Element, z: complex) -> complex:
    """Apply r^k s^epsilon with r=60-degree rotation and s at 15 degrees."""
    out = z
    if element.reflection:
        out = complex(cos(pi / 6), sin(pi / 6)) * out.conjugate()
    angle = element.rotation * pi / 3
    return complex(cos(angle), sin(angle)) * out


def reflect_in_crease(j: int, z: complex) -> complex:
    phi = crease_angle(j)
    return complex(cos(2 * phi), sin(2 * phi)) * z.conjugate()


def height(z: complex) -> float:
    return (z ** 6).real


def chi_det(x: D6Element) -> int:
    return -1 if x.reflection else 1


def chi_sub(x: D6Element) -> int:
    return -1 if x.rotation % 2 else 1


def chi_mix(x: D6Element) -> int:
    return chi_det(x) * chi_sub(x)


def generated_by_axes(axes: Iterable[int]) -> frozenset[D6Element]:
    return closure(crease_reflection(j) for j in axes)


def rotation_order_of_axes(axes: Iterable[int]) -> int:
    js = sorted({j % M for j in axes})
    if not js:
        return 1
    g = M
    for j in js[1:]:
        g = gcd(g, j - js[0])
    return M // g


def verify() -> dict[str, int]:
    elements = tuple(D6Element(k, e) for k in range(M) for e in (0, 1))
    composition_checks = character_checks = action_checks = subset_checks = lattice_checks = 0
    identity = D6Element(0, 0)
    sample_points = (0.7 + 0.4j, -1.2 + 0.3j, 0.2 - 1.1j, 1.0 + 0j)

    for x in elements:
        assert multiply(identity, x) == x and multiply(x, identity) == x
        assert multiply(x, inverse(x)) == identity
        for y in elements:
            xy = multiply(x, y)
            assert chi_det(xy) == chi_det(x) * chi_det(y)
            assert chi_sub(xy) == chi_sub(x) * chi_sub(y)
            assert chi_mix(xy) == chi_mix(x) * chi_mix(y)
            composition_checks += 1
            character_checks += 3
        for z in sample_points:
            assert abs(height(apply_element(x, z)) - chi_det(x) * height(z)) < 1e-10
            action_checks += 1

    for j in range(M):
        phi = crease_angle(j)
        for radius in (0.5, 1.0, 2.3):
            z = radius * complex(cos(phi), sin(phi))
            assert abs(height(z)) < 1e-10
            action_checks += 1
        for z in sample_points:
            assert abs(height(reflect_in_crease(j, z)) + height(z)) < 1e-10
            assert abs(reflect_in_crease(j, reflect_in_crease(j, z)) - z) < 1e-10
            assert abs(reflect_in_crease(j, z) - apply_element(crease_reflection(j), z)) < 1e-10
            action_checks += 3

    for a in range(M):
        for b in range(M):
            assert multiply(crease_reflection(b), crease_reflection(a)) == D6Element((b-a) % M, 0)
            action_checks += 1

    z = 0.7 + 0.4j
    rot60 = complex(cos(pi / 3), sin(pi / 3))
    rot30 = complex(cos(pi / 6), sin(pi / 6))
    assert abs(height(rot60 * z) - height(z)) < 1e-10
    assert abs(height(rot30 * z) + height(z)) < 1e-10
    for j in range(M):
        shifted = 2 * (crease_angle(j) + pi / 6)
        next_angle = 2 * crease_angle((j + 1) % M)
        shifted_axis = complex(cos(shifted), sin(shifted))
        next_axis = complex(cos(next_angle), sin(next_angle))
        assert abs(shifted_axis - next_axis) < 1e-10
        action_checks += 1
    action_checks += 2

    for mask in range(1 << M):
        axes = tuple(j for j in range(M) if mask & (1 << j))
        expected = 1 if not axes else 2 * rotation_order_of_axes(axes)
        assert len(generated_by_axes(axes)) == expected
        subset_checks += 1

    all_axes, preserve, exchange = tuple(range(M)), (0, 2, 4), (1, 3, 5)
    group_all = generated_by_axes(all_axes)
    group_preserve = generated_by_axes(preserve)
    group_exchange = generated_by_axes(exchange)
    assert len(group_all) == 12 and len(group_preserve) == len(group_exchange) == 6
    assert group_preserve == frozenset(x for x in elements if chi_sub(x) == 1)
    assert group_exchange == frozenset(x for x in elements if chi_mix(x) == 1)
    assert frozenset(x for x in elements if chi_det(x) == 1) == frozenset(D6Element(k, 0) for k in range(M))

    for j in range(M):
        for n in range(M):
            n2 = (j - n) % M
            expected_sign = 1 if j % 2 == 0 else -1
            actual_sign = 1 if n2 % 2 == n % 2 else -1
            assert actual_sign == expected_sign
            lattice_checks += 1

    minimum_all = min(len(J) for size in range(1, 7) for J in combinations(all_axes, size)
                      if len(generated_by_axes(J)) == 12)
    minimum_preserve = min(len(J) for size in range(1, 4) for J in combinations(preserve, size)
                           if len(generated_by_axes(J)) == 6)
    minimum_exchange = min(len(J) for size in range(1, 4) for J in combinations(exchange, size)
                           if len(generated_by_axes(J)) == 6)
    assert (minimum_all, minimum_preserve, minimum_exchange) == (2, 2, 2)
    lattice_checks += 5

    return {
        "D6_group_product_checks": composition_checks,
        "D6_character_homomorphism_checks": character_checks,
        "hexagon_height_and_crease_action_checks": action_checks,
        "crease_subset_gcd_checks": subset_checks,
        "lattice_vertex_colour_and_minimum_checks": lattice_checks,
    }


def main() -> None:
    all_axes, preserve, exchange = tuple(range(M)), (0, 2, 4), (1, 3, 5)
    print("h(z)=Re(z^6) crease angles (degrees):",
          [round(crease_angle(j) * 180 / pi) for j in all_axes])
    print("all six crease axes generate D6 order:", len(generated_by_axes(all_axes)))
    print("A/B-preserving axes generate subgroup order:", len(generated_by_axes(preserve)))
    print("A/B-exchanging axes generate subgroup order:", len(generated_by_axes(exchange)))
    print("even-axis characters:", [(j, chi_det(crease_reflection(j)), chi_sub(crease_reflection(j)), chi_mix(crease_reflection(j))) for j in preserve])
    print("odd-axis characters:", [(j, chi_det(crease_reflection(j)), chi_sub(crease_reflection(j)), chi_mix(crease_reflection(j))) for j in exchange])
    print("bounded verification:", verify())


if __name__ == "__main__":
    main()
