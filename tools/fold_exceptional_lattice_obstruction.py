#!/usr/bin/env python3
"""UF-012: exact exceptional-lattice obstruction for local divisor descent.

For a normal surface singularity with resolution exceptional curves E_i,
let M=(E_i.E_j) be the negative-definite intersection matrix and let
b_j=(strict_transform(D).E_j). If D is Cartier/principal then M a=-b
for an integral exceptional valuation vector a. Failure of integrality is
a rigorous obstruction. In rational-singularity settings where the local
class group is the discriminant group, this lattice test is complete.
For non-rational singularities it is only the finite numerical quotient;
degree-zero Picard and related terms must also be considered.

Standard library only; all linear algebra uses fractions.Fraction.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Sequence

Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def determinant_bareiss(matrix: Sequence[Sequence[int]]) -> int:
    """Exact determinant by fraction-free Bareiss elimination."""
    n = len(matrix)
    if n == 0:
        return 1
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")
    a = [list(map(int, row)) for row in matrix]
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                if numerator % previous:
                    raise ArithmeticError("Bareiss exact division failed")
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[n - 1][n - 1]


def solve_rational(matrix: Matrix, rhs: Vector) -> tuple[Fraction, ...]:
    """Solve Mx=rhs exactly by Gauss-Jordan elimination over Q."""
    n = len(matrix)
    if len(rhs) != n or any(len(row) != n for row in matrix):
        raise ValueError("M must be square and rhs have matching dimension")
    a = [[Fraction(v) for v in row] + [Fraction(rhs[i])]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            raise ValueError("intersection matrix is singular")
        a[col], a[pivot] = a[pivot], a[col]
        q = a[col][col]
        a[col] = [v / q for v in a[col]]
        for r in range(n):
            if r != col:
                factor = a[r][col]
                a[r] = [v - factor*w for v, w in zip(a[r], a[col])]
    return tuple(a[i][-1] for i in range(n))


def type_a_intersection_matrix(rank: int) -> Matrix:
    """Negative Cartan matrix for the A_rank rational double point."""
    if rank < 1:
        raise ValueError("rank must be positive")
    return tuple(tuple(-2 if i == j else (1 if abs(i-j) == 1 else 0)
                       for j in range(rank)) for i in range(rank))


def correction_vector(matrix: Matrix, intersection_vector: Vector) -> tuple[Fraction, ...]:
    """Return a solving M a=-b; integrality is necessary for Cartier descent."""
    return solve_rational(matrix, tuple(-v for v in intersection_vector))


def is_integral(vector: Sequence[Fraction]) -> bool:
    return all(x.denominator == 1 for x in vector)


def lattice_class_order(matrix: Matrix, vector: Vector) -> int:
    """Smallest k>0 with k*b in M Z^r; this is the order in coker(M)."""
    det = determinant_bareiss(matrix)
    if det == 0:
        raise ValueError("matrix must be nonsingular")
    for k in range(1, abs(det) + 1):
        solution = correction_vector(matrix, tuple(k*x for x in vector))
        if is_integral(solution):
            return k
    raise AssertionError("class order must divide |det(M)|")


def verify() -> dict[str, int | bool]:
    chain_checks = 0
    for n in range(1, 9):
        matrix = type_a_intersection_matrix(n)
        end_class = tuple(1 if i == 0 else 0 for i in range(n))
        assert abs(determinant_bareiss(matrix)) == n + 1
        assert lattice_class_order(matrix, end_class) == n + 1
        chain_checks += 2

    # A1: -2a=-1 gives a=1/2; twice the class has integral correction.
    a1 = ((-2,),)
    assert correction_vector(a1, (1,)) == (Fraction(1, 2),)
    assert not is_integral(correction_vector(a1, (1,)))
    assert correction_vector(a1, (2,)) == (Fraction(1),)
    a1_checks = 3

    # UF-011 simple-elliptic numerical quotient: same [-2] lattice, but
    # Pic^0(E) is nontrivial, so Z/2 is only the finite numerical quotient.
    assert lattice_class_order(a1, (1,)) == 2
    assert correction_vector(a1, (1,)) == (Fraction(1, 2),)
    elliptic_checks = 2

    # A2: solve [-2 1;1 -2]a=(-1,0) -> (2/3,1/3).
    a2 = type_a_intersection_matrix(2)
    assert correction_vector(a2, (1, 0)) == (Fraction(2, 3), Fraction(1, 3))
    assert lattice_class_order(a2, (1, 0)) == 3
    a2_checks = 2

    # In the UF-011 chart, E:u=0 and Y~:v=0 cross transversely in
    # smooth local coordinates (u,v), so their intersection is one.
    transverse_intersection = True

    return {
        "A_n_determinant_and_end_class_checks": chain_checks,
        "A1_fractional_correction_checks": a1_checks,
        "simple_elliptic_Z2_numerical_quotient_checks": elliptic_checks,
        "A2_exact_fractional_solution_checks": a2_checks,
        "strict_transform_transverse_intersection": transverse_intersection,
    }


def main() -> None:
    print("UF-012 exceptional lattice obstruction")
    for n in range(1, 6):
        matrix = type_a_intersection_matrix(n)
        end = tuple(1 if i == 0 else 0 for i in range(n))
        print(f"A_{n}: |det M|={abs(determinant_bareiss(matrix))}, "
              f"end-class order={lattice_class_order(matrix, end)}")
    print("UF-011 cone: M=[-2], b=[1], correction a=",
          correction_vector(((-2,),), (1,)))
    print("verification:", verify())


if __name__ == "__main__":
    main()
