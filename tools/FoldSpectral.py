"""Finite modular spectral tools for the Fold quarter-turn.

The quarter-turn J(x, y) = (-y, x) satisfies J^2 = -I.  Over Z/pZ,
an eigenvalue therefore must satisfy lambda^2 = -1.  This module computes
and verifies such eigenpairs directly; it does not assume p is prime.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModularEigenpair:
    eigenvalue: int
    eigenvector: tuple[int, int]


def quarter_turn(vector: tuple[int, int], modulus: int) -> tuple[int, int]:
    """Apply J(x, y) = (-y, x) in Z/modulus Z."""
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    x, y = vector
    return (-y % modulus, x % modulus)


def quarter_turn_eigenpairs(modulus: int) -> tuple[ModularEigenpair, ...]:
    """Return all eigenpairs witnessed by v=(lambda, 1), for lambda²=-1."""
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    pairs = []
    for eigenvalue in range(modulus):
        if (eigenvalue * eigenvalue + 1) % modulus == 0:
            vector = (eigenvalue, 1)
            pairs.append(ModularEigenpair(eigenvalue, vector))
    return tuple(pairs)


def verify_quarter_turn_eigenpair(
    pair: ModularEigenpair, modulus: int
) -> bool:
    """Check J(v)=lambda*v and v is nonzero modulo the given modulus."""
    if modulus < 2:
        return False
    eigenvalue = pair.eigenvalue % modulus
    x, y = (coordinate % modulus for coordinate in pair.eigenvector)
    if x == 0 and y == 0:
        return False
    turned = quarter_turn((x, y), modulus)
    scaled = (eigenvalue * x % modulus, eigenvalue * y % modulus)
    return turned == scaled
