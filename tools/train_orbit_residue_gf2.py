#!/usr/bin/env python3
"""Learn Frobenius-normalized orbit residues as an exact GF(2)-linear map.

For a fixed irreducible Q and orbit length L, the target is
    y = sum_{j=0}^{L-1} Frob_{k_Q}^{-j}(alpha_j)
in k_Q = GF(2)[S]/(Q).

The script trains an unknown binary linear map from random input/output
examples by Gaussian elimination over GF(2), checks full feature rank,
and evaluates on independent sequences. This is exact system identification,
not a floating-point neural-network training run.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Iterable


def degree(a: int) -> int:
    return a.bit_length() - 1


def add(a: int, b: int) -> int:
    return a ^ b


def mul(a: int, b: int) -> int:
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def mod(a: int, q: int) -> int:
    dq = degree(q)
    while a and degree(a) >= dq:
        a ^= q << (degree(a) - dq)
    return a


def mul_mod(a: int, b: int, q: int) -> int:
    return mod(mul(a, b), q)


def square_mod(a: int, q: int) -> int:
    return mul_mod(a, a, q)


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, mod(a, b)
    return a


def prime_divisors(n: int) -> list[int]:
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def is_irreducible(q: int) -> bool:
    n = degree(q)
    if n < 1:
        return False
    x = mod(0b10, q)
    for ell in prime_divisors(n):
        y = x
        for _ in range(n // ell):
            y = square_mod(y, q)
        if gcd(add(y, x), q) != 1:
            return False
    y = x
    for _ in range(n):
        y = square_mod(y, q)
    return y == x


def irreducibles(max_degree: int) -> list[int]:
    return [
        q
        for d in range(1, max_degree + 1)
        for q in range(1 << d, 1 << (d + 1))
        if is_irreducible(q)
    ]


def inverse_frobenius(a: int, j: int, q: int) -> int:
    d = degree(q)
    for _ in range((-j) % d):
        a = square_mod(a, q)
    return mod(a, q)


def normalized_orbit(alphas: list[int], q: int) -> int:
    out = 0
    for j, alpha in enumerate(alphas):
        out ^= inverse_frobenius(alpha, j, q)
    return mod(out, q)


def encode_input(alphas: list[int], d: int) -> int:
    out = 0
    for j, alpha in enumerate(alphas):
        out |= alpha << (j * d)
    return out


def solve_gf2(rows: list[int], rhs: list[int], nvars: int) -> tuple[int, int]:
    """Solve A*x=b over GF(2); return (solution bitmask, rank).

    The least set bit is used as pivot. Free variables are set to zero.
    """
    basis: dict[int, tuple[int, int]] = {}
    for row, value in zip(rows, rhs):
        row &= (1 << nvars) - 1
        value &= 1
        while row:
            pivot = (row & -row).bit_length() - 1
            if pivot in basis:
                old_row, old_value = basis[pivot]
                row ^= old_row
                value ^= old_value
            else:
                basis[pivot] = (row, value)
                break
        if row == 0 and value:
            raise ArithmeticError("inconsistent GF(2) training equations")

    rank = len(basis)
    solution = 0
    for pivot in sorted(basis, reverse=True):
        row, value = basis[pivot]
        higher = row & ~((1 << (pivot + 1)) - 1)
        parity = (higher & solution).bit_count() & 1
        bit = value ^ parity
        if bit:
            solution |= 1 << pivot
    return solution, rank


def apply_linear_map(x: int, rows: list[int]) -> int:
    out = 0
    for i, row in enumerate(rows):
        if (x & row).bit_count() & 1:
            out |= 1 << i
    return out


def train_for_field(
    q: int, stages: int, train_count: int, test_count: int, seed: int
) -> dict:
    rng = random.Random(seed)
    d = degree(q)
    nvars = d * stages
    xs: list[int] = []
    ys: list[int] = []
    for _ in range(train_count):
        alphas = [rng.randrange(1 << d) for _ in range(stages)]
        xs.append(encode_input(alphas, d))
        ys.append(normalized_orbit(alphas, q))

    learned_rows = []
    ranks = []
    for output_bit in range(d):
        rhs = [(y >> output_bit) & 1 for y in ys]
        row, rank = solve_gf2(xs, rhs, nvars)
        learned_rows.append(row)
        ranks.append(rank)

    if min(ranks) != nvars:
        raise ArithmeticError(
            f"training features do not span input space for Q={q}: ranks={ranks}, n={nvars}"
        )

    correct = 0
    for _ in range(test_count):
        alphas = [rng.randrange(1 << d) for _ in range(stages)]
        x = encode_input(alphas, d)
        target = normalized_orbit(alphas, q)
        prediction = apply_linear_map(x, learned_rows)
        if prediction == target:
            correct += 1

    # Check the learned matrix directly on every coordinate basis vector.
    basis_checks = 0
    for bit in range(nvars):
        x = 1 << bit
        stage = bit // d
        residue_bit = bit % d
        alphas = [0] * stages
        alphas[stage] = 1 << residue_bit
        expected = normalized_orbit(alphas, q)
        assert apply_linear_map(x, learned_rows) == expected
        basis_checks += 1

    return {
        "Q_bits": q,
        "Q_degree": d,
        "stages": stages,
        "input_bits": nvars,
        "training_samples": train_count,
        "feature_rank": min(ranks),
        "test_samples": test_count,
        "test_correct": correct,
        "test_accuracy": correct / test_count if test_count else 1.0,
        "basis_checks": basis_checks,
        "learned_output_rows": learned_rows,
    }


def self_test() -> None:
    qs = irreducibles(4)
    assert len(qs) == 8
    for i, q in enumerate(qs):
        d = degree(q)
        result = train_for_field(
            q=q,
            stages=3,
            train_count=12 * d,
            test_count=128,
            seed=1000 + i,
        )
        assert result["feature_rank"] == 3 * d
        assert result["test_correct"] == 128
        assert result["basis_checks"] == 3 * d
    # Adjacent Cartier/Frobenius relation cancels in every finite field.
    for q in qs:
        d = degree(q)
        for a in range(1 << d):
            assert normalized_orbit([a, square_mod(a, q)], q) == 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-degree", type=int, default=5)
    parser.add_argument("--stages", type=int, default=5)
    parser.add_argument("--train-multiplier", type=int, default=12)
    parser.add_argument("--test-count", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.max_degree < 1 or args.stages < 1 or args.train_multiplier < 1:
        parser.error("max-degree, stages, and train-multiplier must be positive")
    if args.test_count < 0:
        parser.error("test-count must be nonnegative")
    if args.self_test:
        self_test()
        print("self-test: exact GF(2) system-identification checks passed", file=sys.stderr)

    for i, q in enumerate(irreducibles(args.max_degree)):
        d = degree(q)
        result = train_for_field(
            q=q,
            stages=args.stages,
            train_count=args.train_multiplier * d * args.stages,
            test_count=args.test_count,
            seed=args.seed + i,
        )
        print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
