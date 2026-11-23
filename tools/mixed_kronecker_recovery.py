"""Bounded constructive recovery of mixed Kronecker pencils.

The complete profile determines the canonical target. A structured search over
left bases then solves for right bases linearly; every returned witness is
checked by the independent strict-equivalence auditor. Failure is explicitly
inconclusive when the candidate budget is exhausted.
"""
from __future__ import annotations

from itertools import permutations, product
from typing import Sequence

from tools.pencil_kronecker import rectangular_pencil_kronecker_profile
from tools.rectangular_pencil import _validate_pair
from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit


def _identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def _transpose(a):
    return [list(row) for row in zip(*a)]


def _matmul(a, b, p):
    return [[sum(int(a[i][z]) * int(b[z][j]) for z in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def _det(a, p):
    x = [[int(v) % p for v in row] for row in a]
    n, value = len(x), 1
    for c in range(n):
        pivot = next((r for r in range(c, n) if x[r][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            x[c], x[pivot] = x[pivot], x[c]
            value = -value
        value = value * x[c][c] % p
        inv = pow(x[c][c], -1, p)
        for r in range(c + 1, n):
            factor = x[r][c] * inv % p
            for j in range(c + 1, n):
                x[r][j] = (x[r][j] - factor * x[c][j]) % p
    return value % p


def _inverse(a, p):
    n = len(a)
    x = [[int(v) % p for v in row] + _identity(n)[i]
         for i, row in enumerate(a)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if x[r][c]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        x[c], x[pivot] = x[pivot], x[c]
        inv = pow(x[c][c], -1, p)
        x[c] = [v * inv % p for v in x[c]]
        for r in range(n):
            if r != c and x[r][c]:
                factor = x[r][c]
                x[r] = [(u - factor*v) % p for u, v in zip(x[r], x[c])]
    return [row[n:] for row in x]


def _block_diag_rect(blocks):
    if not blocks:
        return [], []
    nr = sum(len(q) for q, _ in blocks)
    nc = sum(len(q[0]) for q, _ in blocks)
    qout, kout = [[0]*nc for _ in range(nr)], [[0]*nc for _ in range(nr)]
    ro = co = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qout[ro+i][co+j], kout[ro+i][co+j] = q[i][j], k[i][j]
        ro += len(q)
        co += len(q[0])
    return qout, kout


def _right_block(e):
    return ([[int(i == j) for j in range(e+1)] for i in range(e)],
            [[int(j == i+1) for j in range(e+1)] for i in range(e)])


def _regular_blocks(profile, p):
    from tools.regular_pencil_canonical import (
        _companion_from_low, _nilpotent_jordan,
    )
    blocks = []
    for factor in profile["regular_part"]["finite_smith_invariant_factors_low_degree_first"]:
        coeffs = [int(x) % p for x in factor]
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        if len(coeffs) > 1:
            companion = _companion_from_low(coeffs, p)
            blocks.append(([[(-x) % p for x in row] for row in companion],
                           _identity(len(companion))))
    for factor in profile["regular_part"]["infinity_reversed_smith_invariant_factors_low_degree_first"]:
        valuation = 0
        for coefficient in factor:
            if int(coefficient) % p:
                break
            valuation += 1
        if valuation:
            blocks.append((_identity(valuation), _nilpotent_jordan(valuation)))
    return blocks

def _canonical_target(profile, p):
    blocks = []
    for e in profile["singular_part"]["right_minimal_indices"]:
        blocks.append(_right_block(e))
    for e in profile["singular_part"]["left_minimal_indices"]:
        q, k = _right_block(e)
        blocks.append((_transpose(q), _transpose(k)))
    blocks.extend(_regular_blocks(profile, p))
    return _block_diag_rect(blocks)


def _solve_affine(matrix, rhs, columns, p):
    a = [[int(x) % p for x in row] + [int(y) % p]
         for row, y in zip(matrix, rhs)]
    pivots, r = [], 0
    for c in range(columns):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [x * inv % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [(x-f*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    if any(not any(row[:columns]) and row[-1] for row in a[r:]):
        return None
    free = [c for c in range(columns) if c not in pivots]
    particular = [0] * columns
    for i, c in enumerate(pivots):
        particular[c] = a[i][-1]
    basis = []
    for f in free:
        v = [0] * columns
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = -a[i][f] % p
        basis.append(v)
    return particular, basis


def _matrix_from_flat(v, n):
    return [v[i*n:(i+1)*n] for i in range(n)]


def _left_candidates(n, p, limit):
    """Yield identity, permutations/scalings, then one-shear variants."""
    emitted = 0
    identity = _identity(n)
    yield identity
    emitted += 1
    for perm in permutations(range(n)):
        if emitted >= limit:
            return
        base = [[int(perm[i] == j) for j in range(n)] for i in range(n)]
        for scales in product(range(1, p), repeat=n):
            if emitted >= limit:
                return
            yield [[base[i][j] * scales[i] % p for j in range(n)] for i in range(n)]
            emitted += 1
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    for c in range(1, p):
                        if emitted >= limit:
                            return
                        candidate = [row[:] for row in base]
                        candidate[i] = [(candidate[i][z] + c*candidate[j][z]) % p
                                        for z in range(n)]
                        yield [[candidate[r][z] * scales[r] % p for z in range(n)]
                               for r in range(n)]
                        emitted += 1


def _right_transform_equations(s, q, k, q_target, k_target, p):
    m, n = len(q), len(q[0])
    equations, rhs = [], []
    for source, target in ((q, q_target), (k, k_target)):
        left = _matmul(s, source, p)
        for i in range(m):
            for j in range(n):
                row = [0] * (n*n)
                for z in range(n):
                    row[z*n+j] = left[i][z]
                equations.append(row)
                rhs.append(target[i][j])
    return equations, rhs


def recover_mixed_kronecker_pencil(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
    max_candidates: int = 100_000,
    search_mode: str = "structured",
) -> dict:
    """Recover a mixed Kronecker target and constant witnesses when found.

    The profile discovers both minimal-index lists and the regular elementary
    divisors. A structured finite-field search constructs S; for each S the
    equations for T are solved exactly as an affine linear system. This is a
    bounded witness constructor, not a polynomial-time canonical-form
    algorithm. A failed bounded search is inconclusive.
    """
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(max_candidates, int) or isinstance(max_candidates, bool) or max_candidates < 1:
        raise ValueError("max_candidates must be a positive integer")
    if search_mode not in ("structured", "exhaustive"):
        raise ValueError("search_mode must be 'structured' or 'exhaustive'")
    profile = rectangular_pencil_kronecker_profile(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    if not profile["complete_kronecker_structure_data"]:
        return {"recovered": False, "decision_complete": False,
                "reason": "Kronecker profile is incomplete or its dimension identities failed",
                "profile": profile}
    target_q, target_k = _canonical_target(profile, p)
    if (len(target_q), len(target_q[0])) != (rows, cols):
        raise ArithmeticError("profile-derived canonical target has inconsistent dimensions")

    examined = 0
    if search_mode == "exhaustive":
        identity = _identity(rows)
        identity_flat = tuple(value for row in identity for value in row)
        left_iterator = iter([identity])
        left_iterator = (
            matrix for matrix in (
                [identity] + [
                    _matrix_from_flat(list(values), rows)
                    for values in product(range(p), repeat=rows*rows)
                    if values != identity_flat
                ]
            )
        )
    else:
        left_iterator = _left_candidates(rows, p, max_candidates)

    exhausted = True
    for s in left_iterator:
        if examined >= max_candidates:
            exhausted = False
            break
        examined += 1
        if _det(s, p) == 0:
            continue
        equations, rhs = _right_transform_equations(s, q, k, target_q, target_k, p)
        affine = _solve_affine(equations, rhs, cols*cols, p)
        if affine is None:
            continue
        particular, basis = affine
        total = p ** len(basis)
        if search_mode == "structured" and total > max_candidates - examined:
            vectors = iter([particular])
            fully_enumerated = False
        else:
            vectors = (
                [(particular[z] + sum(values[j]*basis[j][z]
                                      for j in range(len(basis))) ) % p
                 for z in range(cols*cols)]
                for values in product(range(p), repeat=len(basis))
            )
            fully_enumerated = True
        for vector in vectors:
            if examined >= max_candidates:
                exhausted = False
                break
            examined += 1
            t = _matrix_from_flat(vector, cols)
            if _det(t, p) == 0:
                continue
            audit = strict_pencil_equivalence_audit(
                q, k, p, target_q, target_k, s, t
            )
            if audit["strict_equivalence_certified"]:
                return {
                    "schema": "the-fold-mixed-kronecker-recovery-v1",
                    "field": f"F_{p}", "source_shape": [rows, cols],
                    "recovered": True, "decision_complete": True,
                    "right_minimal_indices": profile["singular_part"]["right_minimal_indices"],
                    "left_minimal_indices": profile["singular_part"]["left_minimal_indices"],
                    "regular_dimension": profile["regular_part"]["dimension"],
                    "canonical_Q": target_q, "canonical_K": target_k,
                    "left_transform_S": s, "right_transform_T": t,
                    "candidates_examined": examined, "profile": profile,
                    "verification": audit,
                    "method": ("exhaustive finite-field S/T witness search" if search_mode == "exhaustive"
                               else "profile-derived canonical target plus structured S search and exact affine solve for T"),
                    "search_mode": search_mode,
                    "scope": "Positive strict-equivalence witnesses are exact and independently verified.",
                }
        if not fully_enumerated and search_mode == "structured":
            exhausted = False
        if not exhausted:
            break
    complete_negative = search_mode == "exhaustive" and exhausted

    return {
        "schema": "the-fold-mixed-kronecker-recovery-v1",
        "field": f"F_{p}", "source_shape": [rows, cols],
        "recovered": False, "decision_complete": complete_negative,
        "candidates_examined": examined, "max_candidates": max_candidates,
        "search_mode": search_mode,
        "reason": ("all invertible S and all affine T solutions were exhausted; no strict-equivalence witness exists"
                   if complete_negative else "search budget exhausted or structured search family was incomplete"),
        "profile": profile,
        "scope": ("Complete finite-field non-equivalence decision for the profile-derived canonical target."
                  if complete_negative else "Profile data may be complete, but explicit witness search is bounded and failure is inconclusive."),
    }
