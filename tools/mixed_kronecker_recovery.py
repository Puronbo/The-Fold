"""Bounded constructive recovery of mixed Kronecker pencils.

The complete profile determines the canonical target. A structured search over
left bases then solves for right bases linearly; every returned witness is
checked by the independent strict-equivalence auditor. Failure is explicitly
inconclusive when the candidate budget is exhausted.
"""
from __future__ import annotations

from itertools import chain, permutations, product
from typing import Sequence

from tools.pencil_kronecker import rectangular_pencil_kronecker_profile
from tools.rectangular_pencil import _validate_pair
from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit
from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness


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

def _canonical_block_shapes(profile, p):
    """Return ordered rectangular sizes matching _canonical_target's block order."""
    shapes = []
    for e in profile["singular_part"]["right_minimal_indices"]:
        shapes.append((e, e + 1))
    for e in profile["singular_part"]["left_minimal_indices"]:
        shapes.append((e + 1, e))
    shapes.extend((len(q), len(q[0])) for q, _ in _regular_blocks(profile, p))
    return shapes


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


def _exhaustive_left_matrices(n, p):
    """Yield every n-by-n matrix over F_p exactly once, identity first."""
    identity = _identity(n)
    identity_flat = tuple(value for row in identity for value in row)
    yield identity
    for values in product(range(p), repeat=n*n):
        if values != identity_flat:
            yield _matrix_from_flat(list(values), n)


def _affine_vectors(particular, basis, p):
    """Enumerate every vector in a finite-field affine solution space once."""
    dimension = len(basis)
    for coefficients in product(range(p), repeat=dimension):
        yield [
            (particular[z] + sum(coefficients[j] * basis[j][z]
                                 for j in range(dimension))) % p
            for z in range(len(particular))
        ]


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



def verify_mixed_kronecker_negative_certificate(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int,
    result: dict,
) -> dict:
    """Replay an exhaustive negative-result claim, failing closed on bad data.

    Caller-supplied pencil inputs are validated first and raise ValueError when
    malformed. A malformed certificate/result instead returns verified=False.
    """
    # Keep invalid caller data distinct from an untrusted/malformed certificate.
    if (not isinstance(q, Sequence) or isinstance(q, (str, bytes))
            or not isinstance(k, Sequence) or isinstance(k, (str, bytes))
            or not q or not k):
        raise ValueError("Q and K must be non-empty matrix sequences")
    for matrix in (q, k):
        for row in matrix:
            if (not isinstance(row, Sequence) or isinstance(row, (str, bytes))
                    or not row or any(not isinstance(value, int) or isinstance(value, bool)
                                      for value in row)):
                raise ValueError("Q and K must contain non-empty rows of integer entries")
    try:
        rows, cols = _validate_pair(q, k, p)
    except (TypeError, IndexError) as exc:
        raise ValueError("Q, K, and p are invalid replay inputs") from exc

    if not isinstance(result, dict):
        return {"verified": False, "reason": "certificate result must be a dictionary"}
    required = {
        "schema": "the-fold-mixed-kronecker-recovery-v1",
        "field": f"F_{p}",
        "source_shape": [rows, cols],
        "recovered": False,
        "decision_complete": True,
        "search_mode": "exhaustive",
    }
    if any(key not in result or result[key] != value for key, value in required.items()):
        return {"verified": False, "reason": "result metadata does not describe a completed exhaustive negative"}
    max_degree = result.get("profile_max_degree")
    max_minors = result.get("profile_max_minors")
    if (not isinstance(max_degree, int) or isinstance(max_degree, bool) or max_degree < 0
            or not isinstance(max_minors, int) or isinstance(max_minors, bool) or max_minors < 1):
        return {"verified": False, "reason": "profile-bound metadata is invalid"}
    budget = result.get("max_candidates")
    claimed_count = result.get("candidates_examined")
    if (not isinstance(budget, int) or isinstance(budget, bool) or budget < 1
            or not isinstance(claimed_count, int) or isinstance(claimed_count, bool)
            or claimed_count < 0 or claimed_count > budget):
        return {"verified": False, "reason": "candidate budget metadata is invalid"}
    if not isinstance(result.get("profile"), dict):
        return {"verified": False, "reason": "certificate profile must be a dictionary"}

    try:
        profile = rectangular_pencil_kronecker_profile(
            q, k, p, max_degree=max_degree, max_minors=max_minors
        )
        if (not profile.get("complete_kronecker_structure_data")
                or result["profile"] != profile):
            return {"verified": False, "reason": "profile is incomplete or does not match recomputed input profile"}
        target_q, target_k = _canonical_target(profile, p)
        if (len(target_q), len(target_q[0])) != (rows, cols):
            return {"verified": False, "reason": "recomputed canonical target has inconsistent dimensions"}

        examined = 0
        for flat_s in product(range(p), repeat=rows * rows):
            if examined >= budget:
                return {"verified": False, "reason": "replay exceeds claimed candidate budget"}
            s = _matrix_from_flat(list(flat_s), rows)
            examined += 1
            if _det(s, p) == 0:
                continue
            equations, rhs = _right_transform_equations(s, q, k, target_q, target_k, p)
            affine = _solve_affine(equations, rhs, cols * cols, p)
            if affine is None:
                continue
            particular, basis = affine
            for vector in _affine_vectors(particular, basis, p):
                if examined >= budget:
                    return {"verified": False, "reason": "replay exceeds claimed candidate budget"}
                examined += 1
                t = _matrix_from_flat(vector, cols)
                if _det(t, p) != 0:
                    return {"verified": False, "reason": "replay found an invertible strict-equivalence witness"}

        if examined != claimed_count:
            return {"verified": False, "reason": "reported candidate count differs from replay"}
        if result.get("reason") != "all invertible S and all affine T solutions were exhausted; no strict-equivalence witness exists":
            return {"verified": False, "reason": "negative-result explanation metadata is inconsistent"}
        if result.get("scope") != "Complete finite-field non-equivalence decision for the profile-derived canonical target.":
            return {"verified": False, "reason": "negative-result scope metadata is inconsistent"}
    except (TypeError, KeyError, IndexError, AttributeError, ArithmeticError, OverflowError):
        return {"verified": False, "reason": "malformed certificate data could not be replayed"}

    return {
        "verified": True,
        "candidates_replayed": examined,
        "profile_recomputed": True,
        "all_left_matrices_exhausted": True,
        "all_affine_right_solutions_exhausted": True,
        "no_invertible_witness_found": True,
    }



def verify_mixed_kronecker_recovery_certificate(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int,
    result: dict,
) -> dict:
    """Replay the profile and canonical target for any recovery outcome.

    Positive witnesses are re-audited algebraically. Negative exhaustive
    outcomes delegate to the exhaustive search replay. Incomplete or bounded
    failures are checked as accurately described outcomes, never as negatives.
    """
    def validate_caller_matrix(matrix, name):
        if not isinstance(matrix, (list, tuple)) or not matrix:
            raise ValueError(f"{name} must be a nonempty matrix sequence")
        if not all(isinstance(row, (list, tuple)) and row for row in matrix):
            raise ValueError(f"{name} must contain nonempty row sequences")
        width = len(matrix[0])
        if any(len(row) != width for row in matrix):
            raise ValueError(f"{name} must be rectangular")
        if any(not isinstance(value, int) or isinstance(value, bool)
               for row in matrix for value in row):
            raise ValueError(f"{name} entries must be integers (excluding booleans)")

    validate_caller_matrix(q, "q")
    validate_caller_matrix(k, "k")
    rows, cols = _validate_pair(q, k, p)
    if not isinstance(result, dict):
        return {"verified": False, "reason": "certificate result must be a dictionary"}
    common = {
        "schema": "the-fold-mixed-kronecker-recovery-v1",
        "field": f"F_{p}",
        "source_shape": [rows, cols],
    }
    if any(result.get(key) != value for key, value in common.items()):
        return {"verified": False, "reason": "recovery metadata does not match the supplied pencil"}
    degree = result.get("profile_max_degree")
    minors = result.get("profile_max_minors")
    budget = result.get("max_candidates")
    mode = result.get("search_mode")
    if (not isinstance(degree, int) or isinstance(degree, bool) or degree < 0
            or not isinstance(minors, int) or isinstance(minors, bool) or minors < 1
            or not isinstance(budget, int) or isinstance(budget, bool) or budget < 1
            or mode not in ("structured", "exhaustive")):
        return {"verified": False, "reason": "recovery parameter metadata is invalid"}
    if not isinstance(result.get("profile"), dict):
        return {"verified": False, "reason": "recovery profile must be a dictionary"}
    try:
        profile = rectangular_pencil_kronecker_profile(
            q, k, p, max_degree=degree, max_minors=minors
        )
        if result["profile"] != profile:
            return {"verified": False, "reason": "stored profile differs from recomputed profile"}
        if not profile["complete_kronecker_structure_data"]:
            valid = (
                result.get("recovered") is False
                and result.get("decision_complete") is False
                and result.get("reason") == "Kronecker profile is incomplete or its dimension identities failed"
            )
            return {
                "verified": bool(valid),
                "profile_recomputed": True,
                "canonical_target_reconstructed": False,
                "reason": None if valid else "incomplete-profile outcome metadata is inconsistent",
            }
        target_q, target_k = _canonical_target(profile, p)
        if (len(target_q), len(target_q[0])) != (rows, cols):
            return {"verified": False, "reason": "canonical target dimensions are inconsistent"}
        if result.get("recovered") is True:
            if result.get("decision_complete") is not True:
                return {"verified": False, "reason": "positive witness must be marked decision complete"}
            if (result.get("canonical_Q") != target_q or result.get("canonical_K") != target_k
                    or result.get("right_minimal_indices") != profile["singular_part"]["right_minimal_indices"]
                    or result.get("left_minimal_indices") != profile["singular_part"]["left_minimal_indices"]
                    or result.get("regular_dimension") != profile["regular_part"]["dimension"]
                    or result.get("canonical_block_shapes") != [list(x) for x in _canonical_block_shapes(profile, p)]):
                return {"verified": False, "reason": "positive canonical-target metadata is inconsistent"}
            s, t = result.get("left_transform_S"), result.get("right_transform_T")

            def valid_square_transform(matrix, dimension):
                return (
                    isinstance(matrix, (list, tuple))
                    and len(matrix) == dimension
                    and all(
                        isinstance(row, (list, tuple))
                        and len(row) == dimension
                        and all(isinstance(value, int) and not isinstance(value, bool)
                                for value in row)
                        for row in matrix
                    )
                )

            if not (valid_square_transform(s, rows)
                    and valid_square_transform(t, cols)):
                return {"verified": False, "reason": "positive transform matrices are malformed"}
            audit = strict_pencil_equivalence_audit(q, k, p, target_q, target_k, s, t)
            if not audit["strict_equivalence_certified"] or result.get("verification") != audit:
                return {"verified": False, "reason": "positive strict-equivalence witness failed replay"}
            multi = verify_pencil_multi_direct_sum_witness(
                q, k, p, s, t, _canonical_block_shapes(profile, p)
            )
            if result.get("multi_block_direct_sum_audit") != multi or not multi["verification"]["direct_sum_verified"]:
                return {"verified": False, "reason": "positive multi-block audit failed replay"}
            count = result.get("candidates_examined")
            if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= budget:
                return {"verified": False, "reason": "positive candidate count is invalid"}
            expected_method = (
                "exhaustive finite-field S/T witness search"
                if mode == "exhaustive"
                else "profile-derived canonical target plus structured S search and exact affine solve for T"
            )
            if result.get("method") != expected_method:
                return {"verified": False, "reason": "positive method metadata does not match its search mode"}
            if result.get("scope") != "Positive strict-equivalence witnesses are exact and independently verified.":
                return {"verified": False, "reason": "positive scope metadata is inconsistent"}
            return {
                "verified": True, "profile_recomputed": True,
                "canonical_target_reconstructed": True,
                "strict_equivalence_replayed": True,
                "multi_block_audit_replayed": True,
            }
        if result.get("recovered") is not False:
            return {"verified": False, "reason": "recovery flag is malformed"}
        if mode == "exhaustive" and result.get("decision_complete") is True:
            negative = verify_mixed_kronecker_negative_certificate(q, k, p, result)
            return {
                **negative,
                "canonical_target_reconstructed": negative.get("verified", False),
            }
        count = result.get("candidates_examined")
        valid = (
            result.get("decision_complete") is False
            and isinstance(count, int) and not isinstance(count, bool)
            and 0 <= count <= budget
            and result.get("reason") == "search budget exhausted or structured search family was incomplete"
        )
        return {
            "verified": bool(valid),
            "profile_recomputed": True,
            "canonical_target_reconstructed": True,
            "reason": None if valid else "bounded-failure metadata is inconsistent",
        }
    except (TypeError, ValueError, KeyError, IndexError, AttributeError,
            ArithmeticError, OverflowError):
        return {"verified": False, "reason": "malformed recovery certificate could not be replayed"}


def recover_mixed_kronecker_pencil(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
    max_candidates: int = 100_000,
    search_mode: str = "structured",
) -> dict:
    """Recover a mixed Kronecker target and constant witnesses when found.

    The profile discovers both minimal-index lists and the regular elementary
    divisors. In structured mode, a bounded family of S candidates is tried.
    In exhaustive mode, every S over F_p and every corresponding affine T
    solution is enumerated, subject to max_candidates. Positive witnesses are
    independently audited; a completed exhaustive negative search is a
    finite-field non-equivalence certificate. Budget exhaustion is inconclusive.
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
        return {"schema": "the-fold-mixed-kronecker-recovery-v1",
                "field": f"F_{p}", "source_shape": [rows, cols],
                "recovered": False, "decision_complete": False,
                "profile_max_degree": max_degree, "profile_max_minors": max_minors,
                "max_candidates": max_candidates, "search_mode": search_mode,
                "reason": "Kronecker profile is incomplete or its dimension identities failed",
                "profile": profile}
    target_q, target_k = _canonical_target(profile, p)
    if (len(target_q), len(target_q[0])) != (rows, cols):
        raise ArithmeticError("profile-derived canonical target has inconsistent dimensions")

    examined = 0
    if search_mode == "exhaustive":
        left_iterator = _exhaustive_left_matrices(rows, p)
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
            vectors = _affine_vectors(particular, basis, p)
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
                    "profile_max_degree": max_degree, "profile_max_minors": max_minors,
                    "max_candidates": max_candidates,
                    "recovered": True, "decision_complete": True,
                    "right_minimal_indices": profile["singular_part"]["right_minimal_indices"],
                    "left_minimal_indices": profile["singular_part"]["left_minimal_indices"],
                    "regular_dimension": profile["regular_part"]["dimension"],
                    "canonical_Q": target_q, "canonical_K": target_k,
                    "left_transform_S": s, "right_transform_T": t,
                    "candidates_examined": examined, "profile": profile,
                    "verification": audit,
                    "multi_block_direct_sum_audit": verify_pencil_multi_direct_sum_witness(
                        q, k, p, s, t, _canonical_block_shapes(profile, p)
                    ),
                    "canonical_block_shapes": [list(shape) for shape in _canonical_block_shapes(profile, p)],
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
        "profile_max_degree": max_degree, "profile_max_minors": max_minors,
        "recovered": False, "decision_complete": complete_negative,
        "candidates_examined": examined, "max_candidates": max_candidates,
        "search_mode": search_mode,
        "reason": ("all invertible S and all affine T solutions were exhausted; no strict-equivalence witness exists"
                   if complete_negative else "search budget exhausted or structured search family was incomplete"),
        "profile": profile,
        "scope": ("Complete finite-field non-equivalence decision for the profile-derived canonical target."
                  if complete_negative else "Profile data may be complete, but explicit witness search is bounded and failure is inconclusive."),
    }
