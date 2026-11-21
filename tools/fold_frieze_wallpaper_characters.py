#!/usr/bin/env python3
"""UF-006: Z/2 characters of frieze and wallpaper symmetry groups.

Computes homomorphisms to C2 from group presentations by reducing relators
modulo 2. It then imposes strict periodicity by forcing every pure translation
generator to have sign +1. For wallpaper groups this periodic character space
is Hom(P,C2), where P is the finite point group.

This is an algebraic classification of possible global sign characters. It
does not assert that every character is realized by a particular fixed crease
motif or height function.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log2

Word = tuple[str, ...]


@dataclass(frozen=True)
class Presentation:
    name: str
    generators: tuple[str, ...]
    relators: tuple[Word, ...]
    translations: tuple[str, ...]
    point_group: str
    abstract_type: str
    note: str


def character_assignments(presentation: Presentation, periodic: bool = False):
    """Enumerate generator sign maps satisfying all relators in C2.

    Bit 0 means +1 (preserving); bit 1 means -1 (reversing). In C2, an
    inverse has the same image as its generator, so a relator is valid iff
    the XOR of its generator bits is zero.
    """
    index = {g: i for i, g in enumerate(presentation.generators)}
    translations = set(presentation.translations) if periodic else set()
    valid = []
    for bits in product((0, 1), repeat=len(presentation.generators)):
        if any(bits[index[g]] for g in translations):
            continue
        if all(sum(bits[index[g]] for g in word) % 2 == 0
               for word in presentation.relators):
            valid.append(dict(zip(presentation.generators, bits)))
    return tuple(valid)


def rank_from_count(count: int) -> int:
    if count < 1 or count & (count - 1):
        raise ValueError("character count must be a power of two")
    return int(log2(count))


def cyclic_character_assignments(n: int) -> tuple[int, ...]:
    """Possible images of a generator of C_n in C2."""
    if n < 1:
        raise ValueError("n must be positive")
    return (0,) if n % 2 else (0, 1)


def dihedral_character_assignments(n: int) -> tuple[tuple[int, int], ...]:
    """Images (r,s) for D_n=<r,s|r^n=s^2=1,srs=r^-1>, |D_n|=2n."""
    if n < 1:
        raise ValueError("n must be positive")
    return tuple((a, b) for a in cyclic_character_assignments(n) for b in (0, 1))


FRIEZE_GROUPS = (
    Presentation(
        "F1 (p2mm)", ("t", "h", "v"),
        (("h", "h"), ("v", "v"), ("h", "v", "h", "v"),
         ("t", "v", "t", "v"), ("t", "h", "t", "h")),
        ("t",), "D2", "D_infinity_times_C2",
        "two commuting involutions, one commutes with t and one inverts t",
    ),
    Presentation(
        "F2 (p2mg)", ("g", "h"), (("h", "h"), ("g", "h", "g", "h")), (),
        "D2", "D_infinity", "glide g and involution h; pure translation is g^2",
    ),
    Presentation(
        "F3 (p1m1)", ("t", "v"), (("v", "v"), ("v", "t", "v", "t")),
        ("t",), "C2", "D_infinity",
        "mirror-type involution reverses the translation axis",
    ),
    Presentation(
        "F4 (p2)", ("t", "r"), (("r", "r"), ("r", "t", "r", "t")),
        ("t",), "C2", "D_infinity", "half-turn r conjugates t to t^{-1}",
    ),
    Presentation(
        "F5 (p11m)", ("t", "h"), (("h", "h"), ("t", "h", "t", "h")),
        ("t",), "C2", "Z_times_C2",
        "mirror parallel to the translation direction commutes with t",
    ),
    Presentation(
        "F6 (p11g)", ("g",), (), (), "C2", "Z",
        "glide generator g; the primitive pure translation is g^2",
    ),
    Presentation(
        "F7 (p1)", ("t",), (), ("t",), "C1", "Z",
        "translations only; t is the primitive period",
    ),
)


# Point-group types for all 17 wallpaper groups. D_n has order 2n.
WALLPAPER_GROUPS = (
    ("p1", "C1"), ("p2", "C2"), ("pm", "C2"), ("pg", "C2"), ("cm", "C2"),
    ("pmm", "D2"), ("pmg", "D2"), ("pgg", "D2"), ("cmm", "D2"),
    ("p4", "C4"), ("p4m", "D4"), ("p4g", "D4"),
    ("p3", "C3"), ("p3m1", "D3"), ("p31m", "D3"),
    ("p6", "C6"), ("p6m", "D6"),
)


def point_group_character_count(kind: str) -> int:
    if kind.startswith("C"):
        return len(cyclic_character_assignments(int(kind[1:])))
    if kind.startswith("D"):
        return len(dihedral_character_assignments(int(kind[1:])))
    raise ValueError(f"unknown point group type: {kind}")


def verify() -> dict[str, int]:
    full_total = periodic_total = full_relator_checks = periodic_relator_checks = 0
    for group in FRIEZE_GROUPS:
        full = character_assignments(group)
        periodic = character_assignments(group, periodic=True)
        full_total += len(full)
        periodic_total += len(periodic)
        for assignment in full:
            for relator in group.relators:
                assert sum(assignment[g] for g in relator) % 2 == 0
                full_relator_checks += 1
        for assignment in periodic:
            assert all(assignment[g] == 0 for g in group.translations)
            for relator in group.relators:
                assert sum(assignment[g] for g in relator) % 2 == 0
                periodic_relator_checks += 1

    assert tuple(len(character_assignments(g)) for g in FRIEZE_GROUPS) == (8, 4, 4, 4, 4, 2, 2)
    assert tuple(len(character_assignments(g, True)) for g in FRIEZE_GROUPS) == (4, 4, 2, 2, 2, 2, 1)

    # F2 and F6 are glide-generated: the square of either glide is a pure
    # translation, and therefore always has sign +1, even when chi(g)=-1.
    for group in (FRIEZE_GROUPS[1], FRIEZE_GROUPS[5]):
        for assignment in character_assignments(group):
            assert (2 * assignment["g"]) % 2 == 0

    wallpaper_counts = {
        name: point_group_character_count(point_group)
        for name, point_group in WALLPAPER_GROUPS
    }
    assert wallpaper_counts == {
        "p1": 1, "p2": 2, "pm": 2, "pg": 2, "cm": 2,
        "pmm": 4, "pmg": 4, "pgg": 4, "cmm": 4,
        "p4": 2, "p4m": 4, "p4g": 4,
        "p3": 1, "p3m1": 2, "p31m": 2, "p6": 2, "p6m": 4,
    }
    wallpaper_total = sum(wallpaper_counts.values())
    assert wallpaper_total == 46

    for n in range(1, 13):
        assert len(cyclic_character_assignments(n)) == (1 if n % 2 else 2)
        assert len(dihedral_character_assignments(n)) == (2 if n % 2 else 4)

    return {
        "frieze_groups": len(FRIEZE_GROUPS),
        "full_frieze_character_maps": full_total,
        "periodic_frieze_character_maps": periodic_total,
        "full_frieze_relator_checks": full_relator_checks,
        "periodic_frieze_relator_checks": periodic_relator_checks,
        "cyclic_dihedral_formula_checks": 24,
        "wallpaper_groups": len(WALLPAPER_GROUPS),
        "wallpaper_periodic_character_maps": wallpaper_total,
        "wallpaper_groups_with_trivial_only_character": sum(v == 1 for v in wallpaper_counts.values()),
    }


def main() -> None:
    print("FRIEZE GROUP CHARACTERS")
    for group in FRIEZE_GROUPS:
        full = character_assignments(group)
        periodic = character_assignments(group, periodic=True)
        print(f"{group.name:12s} point={group.point_group:2s} abstract={group.abstract_type:24s} "
              f"all={len(full):2d} periodic={len(periodic):2d} "
              f"rank={rank_from_count(len(periodic))}")
    print("\\nWALLPAPER GROUP PERIODIC HEIGHT CHARACTERS")
    for name, point_group in WALLPAPER_GROUPS:
        count = point_group_character_count(point_group)
        print(f"{name:5s} point={point_group:2s} chars={count:2d} rank={rank_from_count(count)}")
    print("\\nverification:", verify())


if __name__ == "__main__":
    main()
