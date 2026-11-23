"""Exact polynomial nullspace generators certifying pencil minimal indices."""
from __future__ import annotations
from typing import Sequence

from tools.pencil_minimal_indices import rectangular_pencil_minimal_indices, _convolution_matrix, _transpose
from tools.pencil_smith import rectangular_pencil_smith_profile
from tools.rectangular_pencil import _validate_pair


def _nullspace(matrix, p):
    """Return a basis of the right kernel; vectors are coordinate lists."""
    a = [[int(x) % p for x in row] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    pivots = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, pivot_col in enumerate(pivots):
            v[pivot_col] = (-a[i][f]) % p
        basis.append(v)
    return basis


def _insert_basis(basis, vector, p):
    """Insert a row vector into a normalized echelon basis, if independent."""
    v = [int(x) % p for x in vector]
    for pivot, row in basis:
        if v[pivot]:
            factor = v[pivot]
            v = [(x - factor*y) % p for x, y in zip(v, row)]
    pivot = next((i for i, x in enumerate(v) if x), None)
    if pivot is None:
        return False
    inv = pow(v[pivot], -1, p)
    v = [(x * inv) % p for x in v]
    # Keep reduced form so insertion order does not affect later membership.
    for i, (old_pivot, row) in enumerate(basis):
        if row[pivot]:
            factor = row[pivot]
            basis[i] = (old_pivot, [(x - factor*y) % p for x, y in zip(row, v)])
    basis.append((pivot, v))
    basis.sort(key=lambda item: item[0])
    return True


def _flatten_coefficients(coefficients, width, degree):
    out = [0] * ((degree + 1) * width)
    for j, block in enumerate(coefficients):
        out[j*width:(j+1)*width] = block
    return out


def _multiply_pencil(q, k, coefficients, p):
    rows, cols = len(q), len(q[0])
    out = []
    for power in range(len(coefficients) + 1):
        block = []
        for i in range(rows):
            value = 0
            if power < len(coefficients):
                value += sum(int(q[i][j]) * coefficients[power][j] for j in range(cols))
            if power > 0:
                value += sum(int(k[i][j]) * coefficients[power-1][j] for j in range(cols))
            block.append(value % p)
        out.append(block)
    return out


def _side_certificate(q, k, p, max_degree, expected_count):
    rows, cols = len(q), len(q[0])
    generators = []
    span_checks = []
    for degree in range(max_degree + 1):
        conv = _convolution_matrix(q, k, degree, p)
        kernel = _nullspace(conv, p)
        echelon = []
        for generator in generators:
            eps = generator["degree"]
            for shift in range(degree - eps + 1):
                shifted = [0] * ((degree + 1) * cols)
                flat = _flatten_coefficients(generator["coefficients_low_degree_first"], cols, degree)
                for j in range(eps + 1):
                    start = (j + shift) * cols
                    shifted[start:start+cols] = flat[j*cols:(j+1)*cols]
                _insert_basis(echelon, shifted, p)
        for vector in kernel:
            if _insert_basis(echelon, vector, p):
                blocks = [vector[j*cols:(j+1)*cols] for j in range(degree + 1)]
                actual_degree = max((j for j, block in enumerate(blocks) if any(block)), default=0)
                blocks = blocks[:actual_degree+1]
                product = _multiply_pencil(q, k, blocks, p)
                if any(any(block) for block in product):
                    raise ArithmeticError("constructed polynomial vector is not in the pencil kernel")
                generators.append({
                    "degree": actual_degree,
                    "coefficients_low_degree_first": blocks,
                    "verified_polynomial_product_is_zero": True,
                })
        expected_nullity = len(kernel)
        span_checks.append({
            "degree_bound": degree,
            "bounded_kernel_dimension": expected_nullity,
            "generated_shift_span_dimension": len(echelon),
            "spans_entire_bounded_kernel": len(echelon) == expected_nullity,
        })
    indices = sorted(g["degree"] for g in generators)
    complete = len(generators) == expected_count and all(
        item["spans_entire_bounded_kernel"] for item in span_checks
    )
    return {
        "generators": sorted(generators, key=lambda g: (g["degree"], g["coefficients_low_degree_first"])),
        "minimal_indices": indices if complete else None,
        "recovered_generator_count": len(generators),
        "expected_generator_count": expected_count,
        "bounded_span_checks": span_checks,
        "all_polynomial_products_verified_zero": all(
            g["verified_polynomial_product_is_zero"] for g in generators
        ),
        "complete": complete,
    }


def rectangular_pencil_nullspace_certificate(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Construct and verify polynomial bases for right and left pencil kernels.

    Coefficients are low-degree first. Completeness is certified only when the
    generators span every bounded-degree kernel through max_degree and their
    count equals the normal-rank deficiency. The degree cap remains explicit.
    """
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(max_degree, int) or max_degree < 0:
        raise ValueError("max_degree must be a non-negative integer")
    smith = rectangular_pencil_smith_profile(q, k, p, max_minors=max_minors)
    normal_rank = smith["finite_chart"]["normal_rank_over_rational_function_field"]
    right = _side_certificate(q, k, p, max_degree, cols-normal_rank)
    left = _side_certificate(_transpose(q), _transpose(k), p, max_degree, rows-normal_rank)
    return {
        "schema": "the-fold-pencil-nullspace-certificate-v1",
        "field": f"F_{p}", "shape": [rows, cols], "pencil": "Q + t K",
        "coefficient_order": "low_degree_first",
        "normal_rank_over_rational_function_field": normal_rank,
        "right": right, "left": left,
        "complete": right["complete"] and left["complete"],
        "scope": (
            "Exact polynomial nullspace generators over F_p[t], with bounded-degree "
            "span certificates. No unimodular transformation matrices are constructed."
        ),
    }
