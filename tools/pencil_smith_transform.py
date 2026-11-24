"""Transformation-certified Smith reduction for small polynomial matrices."""
from __future__ import annotations
from typing import Sequence

from tools.pencil_smith import _trim, _add, _sub, _mul, _divmod, _monic
from tools.rectangular_pencil import _validate_pair


def _zero(p): return [0]
def _is_zero(a, p): return _trim(a, p) == [0]
def _identity(n): return [[([1] if i == j else [0]) for j in range(n)] for i in range(n)]
def _matrix_copy(a, p): return [[_trim(x, p) for x in row] for row in a]


def _matmul(a, b, p):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible polynomial matrix dimensions")
    out = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            value = [0]
            for k in range(len(b)):
                value = _add(value, _mul(a[i][k], b[k][j], p), p)
            row.append(value)
        out.append(row)
    return out


def _row_swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def _col_swap(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]


def _row_add(a, target, source, factor, p):
    a[target] = [_sub(x, _mul(factor, y, p), p)
                 for x, y in zip(a[target], a[source])]


def _col_add(a, target, source, factor, p):
    for row in a:
        row[target] = _sub(row[target], _mul(factor, row[source], p), p)


def _row_scale(a, row, scalar, p):
    a[row] = [_trim([(x * scalar) % p for x in entry], p) for entry in a[row]]


def _poly_matrix_equal(a, b, p):
    return len(a) == len(b) and all(
        len(x) == len(y) and all(_trim(u, p) == _trim(v, p) for u, v in zip(x, y))
        for x, y in zip(a, b)
    )


def polynomial_smith_transform(q: Sequence[Sequence[int]],
                               k: Sequence[Sequence[int]], p: int) -> dict:
    """Return U,V,D with U(Q+tK)V=D and U,V unimodular over F_p[t].

    This is a Smith reduction of the polynomial matrix Q+tK, not a full
    Kronecker canonical decomposition of the pencil.
    """
    rows, cols = _validate_pair(q, k, p)
    a = [[[int(q[i][j]) % p, int(k[i][j]) % p] for j in range(cols)]
         for i in range(rows)]
    original = _matrix_copy(a, p)
    u, v = _identity(rows), _identity(cols)
    operations = []

    def swap_rows(i, j):
        _row_swap(a, i, j); _row_swap(u, i, j)
        operations.append({"op": "swap_rows", "i": i, "j": j})

    def swap_cols(i, j):
        _col_swap(a, i, j); _col_swap(v, i, j)
        operations.append({"op": "swap_columns", "i": i, "j": j})

    def add_row(i, j, factor):
        _row_add(a, i, j, factor, p); _row_add(u, i, j, factor, p)
        operations.append({"op": "row_add", "target": i, "source": j,
                           "factor_low_degree_first": factor[:]})

    def add_col(i, j, factor):
        _col_add(a, i, j, factor, p); _col_add(v, i, j, factor, p)
        operations.append({"op": "column_add", "target": i, "source": j,
                           "factor_low_degree_first": factor[:]})

    def scale_row(i, scalar):
        _row_scale(a, i, scalar, p); _row_scale(u, i, scalar, p)
        operations.append({"op": "row_scale_unit", "row": i, "scalar": scalar})

    limit = min(rows, cols)
    pivot_count = 0
    for pivot_index in range(limit):
        candidates = [
            (len(_trim(a[i][j], p)), i, j)
            for i in range(pivot_index, rows)
            for j in range(pivot_index, cols)
            if not _is_zero(a[i][j], p)
        ]
        if not candidates:
            break
        _, pi, pj = min(candidates)
        if pi != pivot_index: swap_rows(pi, pivot_index)
        if pj != pivot_index: swap_cols(pj, pivot_index)

        while True:
            restarted = False
            pivot = _trim(a[pivot_index][pivot_index], p)
            for i in range(pivot_index + 1, rows):
                if _is_zero(a[i][pivot_index], p): continue
                quotient, remainder = _divmod(a[i][pivot_index], pivot, p)
                add_row(i, pivot_index, quotient)
                if not _is_zero(remainder, p):
                    swap_rows(i, pivot_index)
                    restarted = True
                    break
            if restarted: continue

            pivot = _trim(a[pivot_index][pivot_index], p)
            for j in range(pivot_index + 1, cols):
                if _is_zero(a[pivot_index][j], p): continue
                quotient, remainder = _divmod(a[pivot_index][j], pivot, p)
                add_col(j, pivot_index, quotient)
                if not _is_zero(remainder, p):
                    swap_cols(j, pivot_index)
                    restarted = True
                    break
            if restarted: continue

            pivot = _trim(a[pivot_index][pivot_index], p)
            offender = None
            for i in range(pivot_index + 1, rows):
                for j in range(pivot_index + 1, cols):
                    if not _is_zero(a[i][j], p):
                        _, remainder = _divmod(a[i][j], pivot, p)
                        if not _is_zero(remainder, p):
                            offender = (i, j)
                            break
                if offender: break
            if offender:
                # Since the pivot column below is zero, this adds an
                # offending trailing entry into the pivot row without
                # changing the pivot itself; Euclidean column reduction
                # then strictly lowers its degree.
                add_row(pivot_index, offender[0], [1])
                continue
            break

        pivot = _trim(a[pivot_index][pivot_index], p)
        inverse_lead = pow(pivot[-1], -1, p)
        if inverse_lead != 1:
            scale_row(pivot_index, inverse_lead)
        pivot_count += 1

    diagonal = [[_trim(a[i][j], p) for j in range(cols)] for i in range(rows)]
    diagonal_form = all(_is_zero(a[i][j], p) for i in range(rows)
                        for j in range(cols) if i != j)
    divisibility = True
    diagonal_entries = [_trim(a[i][i], p) for i in range(pivot_count)]
    for first, second in zip(diagonal_entries, diagonal_entries[1:]):
        _, rem = _divmod(second, first, p)
        if not _is_zero(rem, p):
            divisibility = False
    reconstructed = _matmul(_matmul(u, original, p), v, p)
    identity_verified = _poly_matrix_equal(reconstructed, diagonal, p)
    return {
        "schema": "the-fold-polynomial-smith-transform-v1",
        "field": f"F_{p}", "shape": [rows, cols], "pencil": "Q + t K",
        "left_transform_U": u,
        "right_transform_V": v,
        "smith_diagonal_low_degree_first": [
            diagonal[i][i] if i < min(rows, cols) else [0]
            for i in range(min(rows, cols))
        ],
        "reduced_matrix_low_degree_first": diagonal,
        "operation_log": operations,
        "normal_rank": pivot_count,
        "checks": {
            "U_times_P_times_V_equals_reduced_matrix": identity_verified,
            "reduced_matrix_is_diagonal": diagonal_form,
            "successive_nonzero_diagonal_entries_divide": divisibility,
            "transforms_are_products_of_unimodular_elementary_operations": True,
        },
        "verified_smith_form": identity_verified and diagonal_form and divisibility,
        "scope": (
            "Constructive Smith form over F_p[t] for Q+tK. The recorded "
            "elementary operations certify unimodularity. This is not a "
            "Kronecker canonical decomposition and does not expose minimal-index blocks."
        ),
    }
