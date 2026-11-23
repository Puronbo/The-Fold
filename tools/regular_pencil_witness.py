"""Construct strict-equivalence witnesses in a shared invertible chart."""
from __future__ import annotations

from itertools import product
from typing import Sequence

from tools.regular_pencil_profile import (
    _add_scaled, _inverse_mod, _matmul, _mod_pair, _chart_candidates,
    _chart_operator,
)
from tools.rectangular_pencil import _validate_pair
from tools.rational_canonical import rational_canonical_profile


def _nullspace(matrix, p, columns):
    """Basis for the nullspace of a row-major matrix with given columns."""
    a = [[int(x) % p for x in row] for row in matrix]
    pivot_cols = []
    row = 0
    for col in range(columns):
        pivot = next((r for r in range(row, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(x * inv) % p for x in a[row]]
        for r in range(len(a)):
            if r != row and a[r][col]:
                factor = a[r][col]
                a[r] = [(x - factor*y) % p for x, y in zip(a[r], a[row])]
        pivot_cols.append(col)
        row += 1
        if row == len(a):
            break
    free_cols = [c for c in range(columns) if c not in pivot_cols]
    basis = []
    for free in free_cols:
        vector = [0] * columns
        vector[free] = 1
        for r, pivot_col in enumerate(pivot_cols):
            vector[pivot_col] = (-a[r][free]) % p
        basis.append(vector)
    return basis


def _intertwiner_space(a, b, p):
    n = len(a)
    equations = []
    # B*P - P*A = 0; unknowns are P[i][j] in row-major order.
    for i in range(n):
        for j in range(n):
            row = [0] * (n*n)
            for r in range(n):
                row[r*n + j] += b[i][r]
                row[i*n + r] -= a[r][j]
            equations.append([x % p for x in row])
    return _nullspace(equations, p, n*n)


def _matrix_from_vector(vector, n):
    return [vector[i*n:(i+1)*n] for i in range(n)]



def _matvec(matrix, vector, p):
    return [sum(int(x) * int(y) for x, y in zip(row, vector)) % p for row in matrix]

def _krylov_matrix(matrix, vector, p):
    n = len(matrix)
    columns = []
    current = [int(x) % p for x in vector]
    for _ in range(n):
        columns.append(current)
        current = _matvec(matrix, current, p)
    return [[columns[j][i] for j in range(n)] for i in range(n)]

def _find_cyclic_vector(matrix, p, budget):
    n = len(matrix)
    examined = 0
    for vector in product(range(p), repeat=n):
        if examined >= budget:
            break
        examined += 1
        if not any(vector):
            continue
        krylov = _krylov_matrix(matrix, vector, p)
        if _is_invertible(krylov, p):
            return list(vector), krylov, examined
    return None, None, examined

def _cyclic_intertwiner(a, b, p, budget):
    va, ka, used_a = _find_cyclic_vector(a, p, budget)
    if va is None:
        return None, used_a
    vb, kb, used_b = _find_cyclic_vector(b, p, budget)
    if vb is None:
        return None, used_a + used_b
    candidate = _matmul(kb, _inverse_mod(ka, p), p)
    if (_matrices_equal(_matmul(candidate, a, p), _matmul(b, candidate, p), p)
            and _is_invertible(candidate, p)):
        return candidate, used_a + used_b
    raise ArithmeticError('cyclic-basis intertwiner failed exact verification')

def _is_invertible(matrix, p):
    try:
        _inverse_mod(matrix, p)
        return True
    except ValueError:
        return False


def _matrices_equal(a, b, p):
    return len(a) == len(b) and all(
        len(x) == len(y) and all((int(u)-int(v)) % p == 0
                                 for u, v in zip(x, y))
        for x, y in zip(a, b)
    )


def _chart_pivot(q, k, p, chart):
    if chart["kind"] == "finite":
        return _add_scaled(q, k, chart["lambda"], p)
    return k



def _solve_affine(matrix, rhs, p, columns):
    """Return one solution and a nullspace basis for Mx=rhs, or None."""
    a = [[int(x) % p for x in row] + [int(y) % p]
         for row, y in zip(matrix, rhs)]
    pivot_cols = []
    row = 0
    for col in range(columns):
        pivot = next((r for r in range(row, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(x * inv) % p for x in a[row]]
        for r in range(len(a)):
            if r != row and a[r][col]:
                factor = a[r][col]
                a[r] = [(x - factor*y) % p for x, y in zip(a[r], a[row])]
        pivot_cols.append(col)
        row += 1
        if row == len(a):
            break
    for r in range(row, len(a)):
        if all(a[r][c] == 0 for c in range(columns)) and a[r][-1] != 0:
            return None
    free_cols = [c for c in range(columns) if c not in pivot_cols]
    particular = [0] * columns
    for r, col in enumerate(pivot_cols):
        particular[col] = a[r][-1]
    basis = []
    for free in free_cols:
        vector = [0] * columns
        vector[free] = 1
        for r, col in enumerate(pivot_cols):
            vector[col] = (-a[r][free]) % p
        basis.append(vector)
    return particular, basis


def _right_transform_space(s, qa, ka, qb, kb, p):
    """Solve simultaneously S*Qa*T=Qb and S*Ka*T=Kb for T."""
    n = len(qa)
    equations, rhs = [], []
    for left, right in ((qa, qb), (ka, kb)):
        product_left = _matmul(s, left, p)
        for i in range(n):
            for j in range(n):
                row = [0] * (n*n)
                for c in range(n):
                    row[c*n + j] = product_left[i][c] % p
                equations.append(row)
                rhs.append(right[i][j] % p)
    return _solve_affine(equations, rhs, p, n*n)


def _generic_no_chart_witness(qa, ka, qb, kb, p, budget):
    """Bounded exact search over left transforms, solving linearly for T."""
    n = len(qa)
    examined = 0
    for flat_s in product(range(p), repeat=n*n):
        if examined >= budget:
            return {"complete": False, "examined": examined}
        examined += 1
        s = _matrix_from_vector(list(flat_s), n)
        if not _is_invertible(s, p):
            continue
        solution = _right_transform_space(s, qa, ka, qb, kb, p)
        if solution is None:
            continue
        particular, basis = solution
        remaining = budget - examined
        count = p ** len(basis)
        if count > remaining:
            return {"complete": False, "examined": budget}
        for coefficients in product(range(p), repeat=len(basis)):
            examined += 1
            vector = particular[:]
            for scalar, direction in zip(coefficients, basis):
                if scalar:
                    vector = [(x + scalar*y) % p
                              for x, y in zip(vector, direction)]
            t = _matrix_from_vector(vector, n)
            if not _is_invertible(t, p):
                continue
            if (_matrices_equal(_matmul(_matmul(s, qa, p), t, p), qb, p)
                    and _matrices_equal(_matmul(_matmul(s, ka, p), t, p), kb, p)):
                return {"complete": True, "examined": examined, "S": s, "T": t}
    return {"complete": True, "examined": examined}


def construct_regular_pencil_witness(
    q_a: Sequence[Sequence[int]], k_a: Sequence[Sequence[int]],
    q_b: Sequence[Sequence[int]], k_b: Sequence[Sequence[int]],
    p: int, *, max_candidates: int = 100_000,
) -> dict:
    """Find and verify S,T with Q_b=S Q_a T and K_b=S K_a T.

    Uses a shared invertible projective chart and searches the linear space
    of operator intertwiners for an invertible member. The finite-field
    search is bounded explicitly; failure to find a witness within budget
    is inconclusive, never a proof of inequivalence.
    """
    ra, ca = _validate_pair(q_a, k_a, p)
    rb, cb = _validate_pair(q_b, k_b, p)
    if ra != ca or rb != cb or (ra, ca) != (rb, cb):
        raise ValueError("both pencils must be square and have the same shape")
    if not isinstance(max_candidates, int) or max_candidates < 1:
        raise ValueError("max_candidates must be a positive integer")
    qa, ka = _mod_pair(q_a, k_a, p)
    qb, kb = _mod_pair(q_b, k_b, p)
    n = ra

    for lam, kind in _chart_candidates(p):
        chart = ({"kind": kind, "lambda": lam,
                  "projective_point": [1, lam]} if kind == "finite"
                 else {"kind": "infinity", "lambda": None,
                       "projective_point": [0, 1]})
        ha, hb = _chart_pivot(qa, ka, p, chart), _chart_pivot(qb, kb, p, chart)
        if not _is_invertible(ha, p) or not _is_invertible(hb, p):
            continue
        a = _chart_operator(qa, ka, p, chart)
        b = _chart_operator(qb, kb, p, chart)
        profile_a = rational_canonical_profile(a, p)
        profile_b = rational_canonical_profile(b, p)
        sig_a = profile_a["invariant_factors_coefficients_descending"]
        sig_b = profile_b["invariant_factors_coefficients_descending"]
        if sig_a != sig_b:
            return {
                "schema": "the-fold-regular-pencil-witness-v1",
                "decision_complete": True, "strictly_equivalent": False,
                "common_chart": chart,
                "reason": "normalized operators have different rational-canonical invariant factors",
                "witness_found": False,
            }

        found = None
        construction_method = 'linear-intertwiner-space'
        cyclic_examined = 0
        if (profile_a['invariant_factor_count'] == 1
                and profile_b['invariant_factor_count'] == 1):
            found, cyclic_examined = _cyclic_intertwiner(a, b, p, max_candidates)
            if found is not None:
                construction_method = 'cyclic-krylov-bases'
        basis = [] if found is not None else _intertwiner_space(a, b, p)
        dimension = len(basis)
        candidate_count = p ** dimension
        if found is None and candidate_count > max_candidates:
            return {
                "schema": "the-fold-regular-pencil-witness-v1",
                "decision_complete": False, "strictly_equivalent": None,
                "common_chart": chart, "intertwiner_space_dimension": dimension,
                "candidate_count_required": candidate_count,
                "max_candidates": max_candidates,
                "witness_found": False,
                "reason": "intertwiner search exceeds candidate budget; equivalence profile agrees but no witness was constructed",
            }

        examined = cyclic_examined
        if found is None:
            for coefficients in product(range(p), repeat=dimension):
                examined += 1
                vector = [0] * (n*n)
                for scalar, basis_vector in zip(coefficients, basis):
                    if scalar:
                        vector = [(x + scalar*y) % p for x, y in zip(vector, basis_vector)]
                candidate = _matrix_from_vector(vector, n)
                if _is_invertible(candidate, p):
                    found = candidate
                    break
        if found is None:
            # Similar matrices have an invertible intertwiner; this indicates
            # either an arithmetic bug or inconsistent profile assumptions.
            raise ArithmeticError("matching similarity profiles but no invertible intertwiner exists")

        ha_inv = _inverse_mod(ha, p)
        found_inv = _inverse_mod(found, p)
        s = _matmul(_matmul(hb, found, p), ha_inv, p)
        t = found_inv
        q_check = _matmul(_matmul(s, qa, p), t, p)
        k_check = _matmul(_matmul(s, ka, p), t, p)
        q_ok = _matrices_equal(q_check, qb, p)
        k_ok = _matrices_equal(k_check, kb, p)
        if not (q_ok and k_ok):
            raise ArithmeticError("constructed strict-equivalence witness failed verification")
        return {
            "schema": "the-fold-regular-pencil-witness-v1",
            "field": f"F_{p}", "shape": [n, n],
            "decision_complete": True, "strictly_equivalent": True,
            "witness_found": True, "common_chart": chart,
            "normalized_operator_intertwiner_P": found,
            "intertwiner_construction_method": construction_method,
            "left_transform_S": s, "right_transform_T": t,
            "intertwiner_space_dimension": dimension,
            "candidates_examined": examined,
            "cyclic_vector_candidates_examined": cyclic_examined,
            "checks": {
                "P_times_A_equals_B_times_P": _matrices_equal(
                    _matmul(found, a, p), _matmul(b, found, p), p),
                "S_Qa_T_equals_Qb": q_ok,
                "S_Ka_T_equals_Kb": k_ok,
                "S_invertible": _is_invertible(s, p),
                "T_invertible": _is_invertible(t, p),
            },
            "scope": "Constructive witness in a shared base-field invertible chart; bounded finite-field search; no-chart pencils remain unsupported.",
        }

    # No base-field chart: use the complete finite/infinity divisor profile
    # to decide equivalence, then search for a constant witness directly.
    from tools.regular_pencil_classification import compare_regular_pencils_complete
    comparison = compare_regular_pencils_complete(qa, ka, qb, kb, p)
    if not comparison["strictly_equivalent"]:
        return {
            "schema": "the-fold-regular-pencil-witness-v2",
            "decision_complete": True, "strictly_equivalent": False,
            "witness_found": False, "reason": "complete regular-pencil profiles differ",
            "comparison": comparison,
        }
    search = _generic_no_chart_witness(qa, ka, qb, kb, p, max_candidates)
    if "S" not in search:
        return {
            "schema": "the-fold-regular-pencil-witness-v2",
            "decision_complete": True, "strictly_equivalent": True,
            "witness_found": False, "search_complete": search["complete"],
            "candidates_examined": search["examined"],
            "reason": ("exhaustive bounded search found no witness" if search["complete"]
                       else "generic witness search exceeded candidate budget"),
            "comparison": comparison,
        }
    s, t = search["S"], search["T"]
    return {
        "schema": "the-fold-regular-pencil-witness-v2",
        "field": f"F_{p}", "shape": [n, n],
        "decision_complete": True, "strictly_equivalent": True,
        "witness_found": True, "common_chart": None,
        "left_transform_S": s, "right_transform_T": t,
        "candidates_examined": search["examined"],
        "checks": {
            "S_Qa_T_equals_Qb": _matrices_equal(_matmul(_matmul(s, qa, p), t, p), qb, p),
            "S_Ka_T_equals_Kb": _matrices_equal(_matmul(_matmul(s, ka, p), t, p), kb, p),
            "S_invertible": _is_invertible(s, p),
            "T_invertible": _is_invertible(t, p),
        },
        "scope": "No-chart witness via bounded direct finite-field search; complete regular-pencil profiles decide equivalence, while explicit witness search may hit its budget.",
    }
