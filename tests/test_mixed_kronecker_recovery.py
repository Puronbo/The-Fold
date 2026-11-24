import unittest
from itertools import permutations
from unittest.mock import patch
from itertools import product

from tools.mixed_kronecker_recovery import (
    _affine_vectors, _det, _exhaustive_left_matrices, recover_mixed_kronecker_pencil,
    verify_mixed_kronecker_negative_certificate,
    verify_mixed_kronecker_recovery_certificate,
)


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b, p):
    return [[sum(a[i][z]*b[z][j] for z in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a, p):
    n = len(a)
    x = [[v % p for v in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for c in range(n):
        pivot = next(i for i in range(c, n) if x[i][c])
        x[c], x[pivot] = x[pivot], x[c]
        inv = pow(x[c][c], -1, p)
        x[c] = [v*inv % p for v in x[c]]
        for i in range(n):
            if i != c and x[i][c]:
                f = x[i][c]
                x[i] = [(u-f*v) % p for u, v in zip(x[i], x[c])]
    return [row[n:] for row in x]


def block_diag(blocks):
    rows = sum(len(q) for q, _ in blocks)
    cols = sum(len(q[0]) for q, _ in blocks)
    qout, kout = [[0]*cols for _ in range(rows)], [[0]*cols for _ in range(rows)]
    ro = co = 0
    for q, k in blocks:
        for i in range(len(q)):
            for j in range(len(q[0])):
                qout[ro+i][co+j], kout[ro+i][co+j] = q[i][j], k[i][j]
        ro += len(q)
        co += len(q[0])
    return qout, kout


def right_block(e):
    return ([[int(i == j) for j in range(e+1)] for i in range(e)],
            [[int(j == i+1) for j in range(e+1)] for i in range(e)])


class MixedKroneckerRecoveryTests(unittest.TestCase):
    def mixed_pair(self):
        rq, rk = right_block(1)
        lq, lk = transpose(rq), transpose(rk)
        return block_diag([(rq, rk), (lq, lk), ([[1]], [[0]])])

    def test_positive_recovery_certificate_replays_canonical_target_and_witness(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, 5, result)["verified"])
        for key, value in (
            ("canonical_Q", [[0]]), ("canonical_K", [[0]]),
            ("right_minimal_indices", [99]), ("regular_dimension", 99),
            ("profile_max_degree", 1), ("max_candidates", 1),
            ("search_mode", "exhaustive"),
        ):
            with self.subTest(key=key):
                forged = dict(result)
                forged[key] = value
                self.assertFalse(verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)["verified"])

    def test_positive_recovery_rejects_malformed_nested_transforms(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, 5, result)["verified"])
        malformed = (
            None, 7, [], [[1]], [[1, 0], [1]], [[True]], [[1.0]],
            [[0, 0, 0, 0]] * 4,
        )
        for key in ("left_transform_S", "right_transform_T"):
            for value in malformed:
                with self.subTest(key=key, value=value):
                    forged = dict(result)
                    forged[key] = value
                    audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)
                    self.assertFalse(audit["verified"], audit)

        for key in ("left_transform_S", "right_transform_T"):
            forged = dict(result)
            forged[key] = [[0] * 4 for _ in range(4)]
            audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)
            self.assertFalse(audit["verified"], audit)

    def test_positive_recovery_rejects_profile_and_canonical_metadata_type_forgery(self):
        from copy import deepcopy

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, 5, result)["verified"])

        def replace_first_integer(value):
            if isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, int) and not isinstance(item, bool):
                        value[index] = True
                        return True
                    if replace_first_integer(item):
                        return True
            elif isinstance(value, dict):
                for item in value.values():
                    if replace_first_integer(item):
                        return True
            return False

        mutations = []
        forged = deepcopy(result)
        self.assertTrue(replace_first_integer(forged["profile"]))
        mutations.append(("profile integer replaced by boolean", forged))
        forged = deepcopy(result)
        forged["source_shape"][0] = True
        mutations.append(("source shape boolean alias", forged))
        forged = deepcopy(result)
        forged["canonical_Q"][0][0] = True
        mutations.append(("canonical matrix boolean alias", forged))
        forged = deepcopy(result)
        forged["regular_dimension"] = True
        mutations.append(("regular dimension boolean alias", forged))
        forged = deepcopy(result)
        forged["canonical_block_shapes"][0][0] = True
        mutations.append(("canonical block-shape boolean alias", forged))
        forged = deepcopy(result)
        forged["right_minimal_indices"] = tuple(forged["right_minimal_indices"])
        mutations.append(("noncanonical index container", forged))
        for label, forged in mutations:
            with self.subTest(label=label):
                audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)
                self.assertFalse(audit["verified"], audit)

    def test_positive_recovery_replays_and_rejects_forged_nested_audits(self):
        from copy import deepcopy

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, 5, result)["verified"])
        mutations = []
        forged = deepcopy(result)
        forged["verification"]["strict_equivalence_certified"] = False
        mutations.append(("strict success flag", forged))
        forged = deepcopy(result)
        del forged["verification"]["constant_strict_equivalence_Q_verified"]
        mutations.append(("missing strict audit field", forged))
        forged = deepcopy(result)
        forged["verification"] = []
        mutations.append(("strict audit wrong container", forged))
        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["verification"]["direct_sum_verified"] = False
        mutations.append(("multi-block success flag", forged))
        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["verification"]["left_transform_rank"] = -1
        mutations.append(("multi-block forged rank", forged))
        forged = deepcopy(result)
        del forged["multi_block_direct_sum_audit"]["Q_blocks"]
        mutations.append(("missing multi-block matrix data", forged))
        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"] = "verified"
        mutations.append(("multi-block wrong container", forged))
        for label, forged in mutations:
            with self.subTest(label=label):
                audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)
                self.assertFalse(audit["verified"], audit)

    def test_positive_recovery_verifier_keeps_caller_input_errors_distinct(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        for bad_q, bad_k, bad_p in (
            (None, k, 5), ([], k, 5), ([[True]], [[0]], 5),
            ([[1.5]], [[0]], 5), (q, k, True), (q, k, 4),
        ):
            with self.subTest(q=bad_q, k=bad_k, p=bad_p):
                with self.assertRaises(ValueError):
                    verify_mixed_kronecker_recovery_certificate(
                        bad_q, bad_k, bad_p, result
                    )

    def test_incomplete_and_bounded_recovery_outcomes_replay_without_negative_claim(self):
        q, k = self.mixed_pair()
        incomplete = recover_mixed_kronecker_pencil(q, k, 5, max_degree=0)
        audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, incomplete)
        self.assertTrue(audit["verified"])
        self.assertFalse(audit["canonical_target_reconstructed"])
        bounded = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=2, max_candidates=1, search_mode="exhaustive"
        )
        audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, bounded)
        self.assertTrue(audit["verified"])
        self.assertFalse(bounded["decision_complete"])

    def test_recovers_unscrambled_mixed_pencil(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["right_minimal_indices"], [1])
        self.assertEqual(result["left_minimal_indices"], [1])
        self.assertEqual(result["regular_dimension"], 1)
        self.assertTrue(result["verification"]["strict_equivalence_certified"])
        self.assertTrue(result["multi_block_direct_sum_audit"]["verification"]["direct_sum_verified"])
        self.assertEqual(len(result["canonical_block_shapes"]), 3)

    def test_recovers_after_left_basis_shear(self):
        p = 5
        q, k = self.mixed_pair()
        scramble = [[1, 1, 0, 0], [0, 1, 0, 0],
                    [0, 0, 1, 0], [0, 0, 0, 1]]
        right_scramble = [[1, 0, 0, 0], [0, 1, 1, 0],
                          [0, 0, 1, 0], [0, 0, 0, 1]]
        si, ti = inverse(scramble, p), inverse(right_scramble, p)
        q = mm(mm(si, q, p), ti, p)
        k = mm(mm(si, k, p), ti, p)
        result = recover_mixed_kronecker_pencil(q, k, p, max_degree=2)
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertTrue(result["verification"]["strict_equivalence_certified"])
        self.assertTrue(result["multi_block_direct_sum_audit"]["verification"]["direct_sum_verified"])


    def test_exhaustive_mode_finds_exact_witness(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=2, max_candidates=1000,
            search_mode="exhaustive",
        )
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["search_mode"], "exhaustive")
        self.assertTrue(result["verification"]["strict_equivalence_certified"])
        self.assertTrue(result["multi_block_direct_sum_audit"]["verification"]["direct_sum_verified"])

    def test_exhaustive_budget_exhaustion_is_inconclusive(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=2, max_candidates=1,
            search_mode="exhaustive",
        )
        self.assertFalse(result["recovered"])
        self.assertFalse(result["decision_complete"])

    def test_rejects_unknown_search_mode(self):
        q, k = self.mixed_pair()
        with self.assertRaises(ValueError):
            recover_mixed_kronecker_pencil(
                q, k, 5, max_degree=2, search_mode="approximate"
            )

    def test_incomplete_profile_is_not_claimed_as_recovery(self):
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=0, max_candidates=20
        )
        self.assertFalse(result["recovered"])
        self.assertFalse(result["decision_complete"])


    def test_recovery_boundary_grid_across_indices_and_prime_fields(self):
        # Canonical inputs provide a positive control at each size. These
        # cases vary the singular indices and finite field independently.
        for p in (2, 3, 5):
            for right_index, left_index in ((1, 1), (2, 1), (2, 2)):
                with self.subTest(p=p, right_index=right_index, left_index=left_index):
                    rq, rk = right_block(right_index)
                    lq, lk = transpose(right_block(left_index)[0]), transpose(right_block(left_index)[1])
                    q, k = block_diag([
                        (rq, rk), (lq, lk), ([[1]], [[0]])
                    ])
                    result = recover_mixed_kronecker_pencil(
                        q, k, p, max_degree=3, max_candidates=5000
                    )
                    self.assertTrue(result["profile"]["complete_kronecker_structure_data"])
                    self.assertTrue(result["recovered"], result.get("reason"))
                    self.assertTrue(result["decision_complete"])
                    self.assertEqual(result["right_minimal_indices"], [right_index])
                    self.assertEqual(result["left_minimal_indices"], [left_index])
                    self.assertTrue(result["verification"]["strict_equivalence_certified"])

    def test_profile_incompleteness_and_search_budget_are_distinct_boundaries(self):
        q, k = self.mixed_pair()
        profile_limited = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=0, max_candidates=100
        )
        self.assertFalse(profile_limited["recovered"])
        self.assertFalse(profile_limited["decision_complete"])
        self.assertFalse(profile_limited["profile"]["complete_kronecker_structure_data"])
        self.assertIn("profile", profile_limited["reason"])

        search_limited = recover_mixed_kronecker_pencil(
            q, k, 5, max_degree=2, max_candidates=1,
            search_mode="exhaustive",
        )
        self.assertFalse(search_limited["recovered"])
        self.assertFalse(search_limited["decision_complete"])
        self.assertTrue(search_limited["profile"]["complete_kronecker_structure_data"])
        self.assertEqual(search_limited["candidates_examined"], 1)
        self.assertIn("budget", search_limited["reason"])


    def test_structured_budget_failure_is_resolved_by_exhaustive_search(self):
        q, k = self.mixed_pair()
        structured = recover_mixed_kronecker_pencil(
            q, k, 2, max_degree=2, max_candidates=1,
            search_mode="structured",
        )
        self.assertFalse(structured["recovered"])
        self.assertFalse(structured["decision_complete"])
        self.assertEqual(structured["search_mode"], "structured")

        exhaustive = recover_mixed_kronecker_pencil(
            q, k, 2, max_degree=2, max_candidates=5000,
            search_mode="exhaustive",
        )
        self.assertTrue(exhaustive["recovered"], exhaustive.get("reason"))
        self.assertTrue(exhaustive["decision_complete"])
        self.assertEqual(exhaustive["search_mode"], "exhaustive")
        self.assertEqual(
            exhaustive["profile"]["singular_part"]["right_minimal_indices"],
            structured["profile"]["singular_part"]["right_minimal_indices"],
        )
        self.assertTrue(exhaustive["verification"]["strict_equivalence_certified"])

    def test_small_field_structured_and_exhaustive_agree_on_positive_controls(self):
        for p in (2, 3):
            with self.subTest(p=p):
                q, k = self.mixed_pair()
                structured = recover_mixed_kronecker_pencil(
                    q, k, p, max_degree=2, max_candidates=5000,
                    search_mode="structured",
                )
                exhaustive = recover_mixed_kronecker_pencil(
                    q, k, p, max_degree=2, max_candidates=5000,
                    search_mode="exhaustive",
                )
                self.assertTrue(structured["recovered"], structured.get("reason"))
                self.assertTrue(exhaustive["recovered"], exhaustive.get("reason"))
                self.assertEqual(structured["right_minimal_indices"], exhaustive["right_minimal_indices"])
                self.assertEqual(structured["left_minimal_indices"], exhaustive["left_minimal_indices"])
                self.assertTrue(structured["verification"]["strict_equivalence_certified"])
                self.assertTrue(exhaustive["verification"]["strict_equivalence_certified"])


    def test_exhaustive_left_matrix_enumerator_is_complete_and_duplicate_free(self):
        for p in (2, 3):
            for n in (1, 2):
                with self.subTest(p=p, n=n):
                    matrices = list(_exhaustive_left_matrices(n, p))
                    flattened = [tuple(value for row in matrix for value in row)
                                 for matrix in matrices]
                    self.assertEqual(len(flattened), p ** (n*n))
                    self.assertEqual(len(set(flattened)), p ** (n*n))
                    identity = tuple(int(i == j) for i in range(n) for j in range(n))
                    self.assertEqual(flattened[0], identity)
                    self.assertEqual(set(flattened), set(
                        __import__("itertools").product(range(p), repeat=n*n)
                    ))

    def test_affine_solution_enumerator_matches_brute_force(self):
        # x + 2y = 1 and z - y = 2 over F_3.
        p = 3
        matrix = [[1, 2, 0], [0, 2, 1]]
        rhs = [1, 2]
        from tools.mixed_kronecker_recovery import _solve_affine
        particular, basis = _solve_affine(matrix, rhs, 3, p)
        generated = list(_affine_vectors(particular, basis, p))
        brute_force = [
            list(candidate)
            for candidate in __import__("itertools").product(range(p), repeat=3)
            if all(sum(a*b for a, b in zip(row, candidate)) % p == target
                   for row, target in zip(matrix, rhs))
        ]
        self.assertEqual(len(generated), p ** len(basis))
        self.assertEqual(len(set(map(tuple, generated))), len(generated))
        self.assertEqual(set(map(tuple, generated)), set(map(tuple, brute_force)))

    def test_affine_enumerator_handles_unique_and_unconstrained_spaces(self):
        self.assertEqual(list(_affine_vectors([2, 1], [], 5)), [[2, 1]])
        generated = list(_affine_vectors([0, 0], [[1, 0], [0, 1]], 2))
        self.assertEqual(set(map(tuple, generated)), {(0, 0), (0, 1), (1, 0), (1, 1)})


    def test_affine_solver_matches_exhaustive_solution_sets_on_small_system_grid(self):
        # Exhaust every coefficient matrix and right-hand side for dimensions
        # 0..2 over F_2 and F_3. The comparison enumerates candidate vectors
        # independently, rather than relying on the solver's nullspace basis.
        from tools.mixed_kronecker_recovery import _solve_affine

        checked = 0
        for p in (2, 3):
            for rows in range(3):
                for columns in range(3):
                    for flat in product(range(p), repeat=rows * columns):
                        matrix = [
                            list(flat[i * columns:(i + 1) * columns])
                            for i in range(rows)
                        ]
                        for rhs in product(range(p), repeat=rows):
                            expected = {
                                tuple(candidate)
                                for candidate in product(range(p), repeat=columns)
                                if all(
                                    sum(a * x for a, x in zip(row, candidate)) % p == target
                                    for row, target in zip(matrix, rhs)
                                )
                            }
                            affine = _solve_affine(matrix, rhs, columns, p)
                            if not expected:
                                self.assertIsNone(affine, (p, matrix, rhs))
                            else:
                                self.assertIsNotNone(affine, (p, matrix, rhs))
                                particular, basis = affine
                                actual_vectors = list(_affine_vectors(particular, basis, p))
                                actual = {tuple(vector) for vector in actual_vectors}
                                self.assertEqual(len(actual_vectors), len(actual))
                                self.assertEqual(actual, expected, (p, matrix, rhs))
                            checked += 1
        self.assertGreater(checked, 900)


    def test_determinant_filter_matches_independent_permutation_formula(self):
        # Compare the elimination determinant's zero/nonzero decision with
        # the Leibniz formula, independently enumerated over permutations.
        for p in (2, 3):
            for n in (1, 2, 3):
                for flat in product(range(p), repeat=n*n):
                    matrix = [list(flat[i*n:(i+1)*n]) for i in range(n)]
                    expected = 0
                    for perm in permutations(range(n)):
                        inversions = sum(
                            perm[i] > perm[j]
                            for i in range(n) for j in range(i + 1, n)
                        )
                        term = (-1 if inversions % 2 else 1)
                        for i in range(n):
                            term *= matrix[i][perm[i]]
                        expected = (expected + term) % p
                    self.assertEqual(_det(matrix, p), expected, (p, matrix))
                    self.assertEqual(_det(matrix, p) != 0, expected != 0)

    def test_exhaustive_negative_requires_full_left_and_affine_streams(self):
        # Force a same-shape but impossible target to exercise the negative
        # branch: the only invertible 1x1 S yields an inconsistent T system.
        q, k = [[1]], [[0]]
        impossible_target = ([[0]], [[1]])
        with patch(
            "tools.mixed_kronecker_recovery._canonical_target",
            return_value=impossible_target,
        ):
            complete = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_candidates=10,
                search_mode="exhaustive",
            )
            self.assertFalse(complete["recovered"])
            self.assertTrue(complete["decision_complete"])
            self.assertEqual(complete["candidates_examined"], 2)

            cutoff = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_candidates=1,
                search_mode="exhaustive",
            )
            self.assertFalse(cutoff["recovered"])
            self.assertFalse(cutoff["decision_complete"])
            self.assertEqual(cutoff["candidates_examined"], 1)

    def test_exhaustive_budget_counts_left_and_right_candidates(self):
        # On the canonical mixed control, identity S and identity T are the
        # first two examined candidates and together suffice for a witness.
        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(
            q, k, 2, max_degree=2, max_candidates=2,
            search_mode="exhaustive",
        )
        self.assertTrue(result["recovered"], result.get("reason"))
        self.assertEqual(result["candidates_examined"], 2)
        self.assertTrue(result["verification"]["strict_equivalence_certified"])


    def test_negative_certificate_is_independently_replayed(self):
        q, k = [[1]], [[0]]
        impossible_target = ([[0]], [[1]])
        with patch(
            "tools.mixed_kronecker_recovery._canonical_target",
            return_value=impossible_target,
        ):
            result = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_candidates=10,
                search_mode="exhaustive",
            )
            audit = verify_mixed_kronecker_negative_certificate(
                q, k, 2, result,
            )
        self.assertTrue(audit["verified"], audit.get("reason"))
        self.assertEqual(audit["candidates_replayed"], result["candidates_examined"])
        self.assertTrue(audit["all_left_matrices_exhausted"])
        self.assertTrue(audit["all_affine_right_solutions_exhausted"])

    def test_negative_certificate_replay_rejects_metadata_mutations(self):
        q, k = [[1]], [[0]]
        impossible_target = ([[0]], [[1]])
        with patch(
            "tools.mixed_kronecker_recovery._canonical_target",
            return_value=impossible_target,
        ):
            original = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_candidates=10,
                search_mode="exhaustive",
            )
            mutations = {
                "candidate count": ("candidates_examined", 1),
                "budget": ("max_candidates", 1),
                "search mode": ("search_mode", "structured"),
                "completion flag": ("decision_complete", False),
                "recovery flag": ("recovered", True),
                "explanation": ("reason", "fabricated"),
                "scope": ("scope", "universal non-equivalence"),
                "profile degree bound": ("profile_max_degree", 1),
            }
            for label, (key, value) in mutations.items():
                with self.subTest(label=label):
                    forged = dict(original)
                    forged[key] = value
                    audit = verify_mixed_kronecker_negative_certificate(
                        q, k, 2, forged,
            )
                    self.assertFalse(audit["verified"])

    def test_negative_certificate_replay_rejects_budget_limited_result(self):
        q, k = [[1]], [[0]]
        impossible_target = ([[0]], [[1]])
        with patch(
            "tools.mixed_kronecker_recovery._canonical_target",
            return_value=impossible_target,
        ):
            cutoff = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_candidates=1,
                search_mode="exhaustive",
            )
            audit = verify_mixed_kronecker_negative_certificate(
                q, k, 2, cutoff,
            )
        self.assertFalse(audit["verified"])


    def test_negative_certificate_replay_rejects_malformed_result_containers(self):
        q, k = [[1]], [[0]]
        for malformed in (None, [], "certificate", 7):
            with self.subTest(result=malformed):
                audit = verify_mixed_kronecker_negative_certificate(q, k, 2, malformed)
                self.assertFalse(audit["verified"])

    def test_negative_certificate_replay_uses_bound_metadata_and_rejects_invalid_bounds(self):
        q, k = [[1]], [[0]]
        impossible_target = ([[0]], [[1]])
        with patch(
            "tools.mixed_kronecker_recovery._canonical_target",
            return_value=impossible_target,
        ):
            original = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_minors=17, max_candidates=10,
                search_mode="exhaustive",
            )
            self.assertEqual(original["profile_max_degree"], 0)
            self.assertEqual(original["profile_max_minors"], 17)
            self.assertTrue(verify_mixed_kronecker_negative_certificate(q, k, 2, original)["verified"])
            for key, value in (
                ("profile_max_degree", True), ("profile_max_degree", -1),
                ("profile_max_degree", 0.5), ("profile_max_minors", False),
                ("profile_max_minors", 0), ("profile_max_minors", 1.5),
            ):
                with self.subTest(key=key, value=value):
                    forged = dict(original, **{key: value})
                    self.assertFalse(verify_mixed_kronecker_negative_certificate(q, k, 2, forged)["verified"])


    def test_negative_certificate_replay_rejects_missing_and_malformed_fields(self):
        q, k = [[1]], [[0]]
        base = {
            "schema": "the-fold-mixed-kronecker-recovery-v1",
            "field": "F_2",
            "source_shape": [1, 1],
            "recovered": False,
            "decision_complete": True,
            "search_mode": "exhaustive",
            "max_candidates": 10,
            "profile_max_degree": 0,
            "profile_max_minors": 2000,
            "candidates_examined": 2,
            "profile": {},
            "reason": "all invertible S and all affine T solutions were exhausted; no strict-equivalence witness exists",
            "scope": "Complete finite-field non-equivalence decision for the profile-derived canonical target.",
        }
        for key in ("schema", "field", "source_shape", "recovered",
                    "decision_complete", "search_mode", "max_candidates",
                    "profile_max_degree", "profile_max_minors", "candidates_examined", "profile", "reason", "scope"):
            with self.subTest(missing=key):
                forged = dict(base)
                del forged[key]
                self.assertFalse(
                    verify_mixed_kronecker_negative_certificate(q, k, 2, forged)["verified"]
                )
        for malformed_profile in (None, [], "bad", {"complete_kronecker_structure_data": []}):
            with self.subTest(profile=malformed_profile):
                forged = dict(base, profile=malformed_profile)
                self.assertFalse(
                    verify_mixed_kronecker_negative_certificate(q, k, 2, forged)["verified"]
                )

    def test_negative_certificate_replay_validates_caller_matrix_and_field_inputs(self):
        valid_result = None
        q, k = [[1]], [[0]]
        impossible_target = ([[0]], [[1]])
        with patch(
            "tools.mixed_kronecker_recovery._canonical_target",
            return_value=impossible_target,
        ):
            valid_result = recover_mixed_kronecker_pencil(
                q, k, 2, max_degree=0, max_candidates=10,
                search_mode="exhaustive",
            )
            for bad_q, bad_k, bad_p in (
                (None, k, 2),
                ([], k, 2),
                ([[1, 2], [3]], [[0, 0], [0, 0]], 2),
                ([[True]], [[0]], 2),
                ([[1.5]], [[0]], 2),
                ([[1]], [[0, 0]], 2),
                (q, k, True),
                (q, k, 4),
            ):
                with self.subTest(q=bad_q, k=bad_k, p=bad_p):
                    with self.assertRaises(ValueError):
                        verify_mixed_kronecker_negative_certificate(
                            bad_q, bad_k, bad_p, valid_result,
            )



    def test_positive_recovery_replay_cross_field_basis_scrambles(self):
        for p in (2, 3, 5, 7):
            with self.subTest(p=p):
                q, k = self.mixed_pair()
                left = [[1, 1, 0, 0], [0, 1, 0, 0],
                        [0, 0, 1, 0], [0, 0, 0, 1]]
                right = [[1, 0, 0, 0], [0, 1, 1, 0],
                         [0, 0, 1, 0], [0, 0, 0, 1]]
                q = mm(mm(inverse(left, p), q, p), inverse(right, p), p)
                k = mm(mm(inverse(left, p), k, p), inverse(right, p), p)
                result = recover_mixed_kronecker_pencil(
                    q, k, p, max_degree=2, max_candidates=20000
                )
                self.assertTrue(result["recovered"], result.get("reason"))
                self.assertTrue(
                    verify_mixed_kronecker_recovery_certificate(q, k, p, result)["verified"]
                )
                forged_field = dict(result, field=f"F_{p + 2}")
                self.assertFalse(
                    verify_mixed_kronecker_recovery_certificate(q, k, p, forged_field)["verified"]
                )
                from copy import deepcopy
                forged_transform = deepcopy(result)
                forged_transform["left_transform_S"][0][0] = True
                self.assertFalse(
                    verify_mixed_kronecker_recovery_certificate(q, k, p, forged_transform)["verified"]
                )

    def test_positive_recovery_replay_accepts_distinct_valid_witnesses(self):
        from copy import deepcopy
        for p in (3, 5, 7):
            with self.subTest(p=p):
                q, k = self.mixed_pair()
                result = recover_mixed_kronecker_pencil(q, k, p, max_degree=2)
                self.assertTrue(result["recovered"], result.get("reason"))
                alternative = deepcopy(result)
                scalar = p - 1
                alternative["left_transform_S"] = [
                    [(scalar * value) % p for value in row]
                    for row in result["left_transform_S"]
                ]
                inverse_scalar = pow(scalar, -1, p)
                alternative["right_transform_T"] = [
                    [(inverse_scalar * value) % p for value in row]
                    for row in result["right_transform_T"]
                ]
                from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit
                from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness
                alternative["verification"] = strict_pencil_equivalence_audit(
                    q, k, p, alternative["canonical_Q"], alternative["canonical_K"],
                    alternative["left_transform_S"], alternative["right_transform_T"],
                )
                alternative["multi_block_direct_sum_audit"] = verify_pencil_multi_direct_sum_witness(
                    q, k, p, alternative["left_transform_S"],
                    alternative["right_transform_T"], alternative["canonical_block_shapes"],
                )
                audit = verify_mixed_kronecker_recovery_certificate(q, k, p, alternative)
                self.assertTrue(audit["verified"], audit)
                self.assertNotEqual(
                    alternative["left_transform_S"], result["left_transform_S"]
                )


    def test_positive_recovery_replay_rejects_missing_and_type_forged_metadata(self):
        from copy import deepcopy

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, 5, result)["verified"])
        required = (
            "schema", "field", "source_shape", "profile_max_degree",
            "profile_max_minors", "max_candidates", "search_mode", "profile",
            "recovered", "decision_complete", "canonical_Q", "canonical_K",
            "right_minimal_indices", "left_minimal_indices", "regular_dimension",
            "canonical_block_shapes", "left_transform_S", "right_transform_T",
            "verification", "multi_block_direct_sum_audit", "candidates_examined",
            "method", "scope",
        )
        for key in required:
            with self.subTest(missing=key):
                forged = deepcopy(result)
                del forged[key]
                self.assertFalse(
                    verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)["verified"]
                )

        for key, value in (
            ("schema", True), ("field", 5), ("source_shape", (4, 4)),
            ("profile_max_degree", True), ("profile_max_minors", False),
            ("max_candidates", True), ("search_mode", []),
            ("recovered", 1), ("decision_complete", 1),
            ("candidates_examined", True), ("method", None), ("scope", {}),
        ):
            with self.subTest(key=key, value=value):
                forged = deepcopy(result)
                forged[key] = value
                self.assertFalse(
                    verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)["verified"]
                )

    def test_positive_recovery_replay_rejects_nested_audit_type_aliases(self):
        from copy import deepcopy

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, 5, result)["verified"])
        mutations = []
        forged = deepcopy(result)
        forged["verification"]["left_determinant_mod_p"] = True
        mutations.append(("strict rank boolean alias", forged))
        forged = deepcopy(result)
        forged["verification"]["constant_strict_equivalence_Q_verified"] = 1
        mutations.append(("strict flag integer alias", forged))
        forged = deepcopy(result)
        forged["verification"]["field"] = (forged["verification"]["field"],)
        mutations.append(("strict rank container substitution", forged))
        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["verification"]["left_transform_rank"] = True
        mutations.append(("multi-block rank boolean alias", forged))
        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["verification"]["direct_sum_verified"] = 1
        mutations.append(("multi-block flag integer alias", forged))
        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["block_shapes"] = tuple(
            forged["multi_block_direct_sum_audit"]["block_shapes"]
        )
        mutations.append(("multi-block shape container substitution", forged))
        for label, forged in mutations:
            with self.subTest(label=label):
                audit = verify_mixed_kronecker_recovery_certificate(q, k, 5, forged)
                self.assertFalse(audit["verified"], audit)

    def test_positive_recovery_replay_rejects_cross_field_transform_substitution(self):
        from copy import deepcopy

        q, k = self.mixed_pair()
        results = {}
        for p in (3, 5, 7):
            result = recover_mixed_kronecker_pencil(q, k, p, max_degree=2)
            self.assertTrue(result["recovered"], result.get("reason"))
            self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, p, result)["verified"])
            results[p] = result

        from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness
        for target_p, source_p in ((3, 5), (5, 7), (7, 3)):
            with self.subTest(target_field=target_p, source_field=source_p):
                transplanted = deepcopy(results[target_p])
                transplanted["left_transform_S"] = deepcopy(results[source_p]["left_transform_S"])
                transplanted["right_transform_T"] = deepcopy(results[source_p]["right_transform_T"])
                # Witness provenance is irrelevant: if the transplanted pair
                # also satisfies the target-field identities, it is valid.
                transplanted["verification"] = strict_pencil_equivalence_audit(
                    q, k, target_p, transplanted["canonical_Q"],
                    transplanted["canonical_K"], transplanted["left_transform_S"],
                    transplanted["right_transform_T"],
                )
                transplanted["multi_block_direct_sum_audit"] = verify_pencil_multi_direct_sum_witness(
                    q, k, target_p, transplanted["left_transform_S"],
                    transplanted["right_transform_T"], transplanted["canonical_block_shapes"],
                )
                self.assertTrue(
                    verify_mixed_kronecker_recovery_certificate(
                        q, k, target_p, transplanted
                    )["verified"]
                )

                # A cross-field witness mutation is rejected even after both
                # nested audits are freshly recomputed for the target field.
                mutated = deepcopy(transplanted)
                mutated["left_transform_S"][0][0] = (
                    mutated["left_transform_S"][0][0] + 1
                ) % target_p
                mutated["verification"] = strict_pencil_equivalence_audit(
                    q, k, target_p, mutated["canonical_Q"], mutated["canonical_K"],
                    mutated["left_transform_S"], mutated["right_transform_T"],
                )
                mutated["multi_block_direct_sum_audit"] = verify_pencil_multi_direct_sum_witness(
                    q, k, target_p, mutated["left_transform_S"],
                    mutated["right_transform_T"], mutated["canonical_block_shapes"],
                )
                self.assertFalse(
                    verify_mixed_kronecker_recovery_certificate(
                        q, k, target_p, mutated
                    )["verified"]
                )


    def test_positive_replay_rejects_canonical_block_order_dimension_and_matrix_tampering(self):
        from copy import deepcopy
        from tools.strict_pencil_equivalence import strict_pencil_equivalence_audit
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = self.mixed_pair()
        p = 5
        result = recover_mixed_kronecker_pencil(q, k, p, max_degree=2)
        self.assertTrue(verify_mixed_kronecker_recovery_certificate(q, k, p, result)["verified"])
        mutations = []

        forged = deepcopy(result)
        forged["canonical_block_shapes"][0], forged["canonical_block_shapes"][1] = (
            forged["canonical_block_shapes"][1], forged["canonical_block_shapes"][0]
        )
        mutations.append(("block-order swap", forged))

        forged = deepcopy(result)
        forged["canonical_block_shapes"][0][1] += 1
        mutations.append(("block dimension change", forged))

        forged = deepcopy(result)
        forged["canonical_Q"][0][0] = (forged["canonical_Q"][0][0] + 1) % p
        mutations.append(("canonical matrix entry", forged))

        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["transformed_Q"][0][0] = (
            forged["multi_block_direct_sum_audit"]["transformed_Q"][0][0] + 1
        ) % p
        mutations.append(("nested transformed matrix entry", forged))

        forged = deepcopy(result)
        forged["multi_block_direct_sum_audit"]["Q_blocks"][0][0][0][0] = (
            forged["multi_block_direct_sum_audit"]["Q_blocks"][0][0][0][0] + 1
        ) % p
        mutations.append(("nested block matrix entry", forged))

        for label, forged in mutations:
            with self.subTest(label=label):
                audit = verify_mixed_kronecker_recovery_certificate(q, k, p, forged)
                self.assertFalse(audit["verified"], audit)

        # A block permutation is a valid direct-sum presentation when its
        # transforms and ordered block-shape list are permuted consistently.
        # The recovery certificate intentionally retains one canonical order.
        row_order = [0, 3, 1, 2]       # right, regular, left
        col_order = [0, 1, 3, 2]
        row_perm = [[int(row_order[i] == j) for j in range(4)] for i in range(4)]
        col_perm = [[int(col_order[i] == j) for j in range(4)] for i in range(4)]
        reordered_s = mm(row_perm, result["left_transform_S"], p)
        reordered_t = mm(result["right_transform_T"], col_perm, p)
        reordered_shapes = [
            result["canonical_block_shapes"][0],
            result["canonical_block_shapes"][2],
            result["canonical_block_shapes"][1],
        ]
        reordered_audit = verify_pencil_multi_direct_sum_witness(
            q, k, p, reordered_s, reordered_t, reordered_shapes
        )
        self.assertTrue(reordered_audit["verification"]["direct_sum_verified"])
        reordered_q = mm(mm(row_perm, result["canonical_Q"], p), col_perm, p)
        reordered_k = mm(mm(row_perm, result["canonical_K"], p), col_perm, p)
        alternative = deepcopy(result)
        alternative["canonical_Q"] = reordered_q
        alternative["canonical_K"] = reordered_k
        alternative["canonical_block_shapes"] = reordered_shapes
        alternative["left_transform_S"] = reordered_s
        alternative["right_transform_T"] = reordered_t
        alternative["verification"] = strict_pencil_equivalence_audit(
            q, k, p, reordered_q, reordered_k, reordered_s, reordered_t
        )
        alternative["multi_block_direct_sum_audit"] = reordered_audit
        self.assertFalse(
            verify_mixed_kronecker_recovery_certificate(q, k, p, alternative)["verified"]
        )


    def test_multi_block_verifier_accepts_every_valid_block_permutation(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = self.mixed_pair()
        p = 5
        result = recover_mixed_kronecker_pencil(q, k, p, max_degree=2)
        shapes = [tuple(shape) for shape in result["canonical_block_shapes"]]
        self.assertEqual(len(shapes), 3)
        row_offsets = [0]
        col_offsets = [0]
        for rows, cols in shapes:
            row_offsets.append(row_offsets[-1] + rows)
            col_offsets.append(col_offsets[-1] + cols)

        for order in permutations(range(len(shapes))):
            with self.subTest(order=order):
                row_order = [
                    index
                    for block in order
                    for index in range(row_offsets[block], row_offsets[block + 1])
                ]
                col_order = [
                    index
                    for block in order
                    for index in range(col_offsets[block], col_offsets[block + 1])
                ]
                row_perm = [
                    [int(row_order[i] == j) for j in range(len(row_order))]
                    for i in range(len(row_order))
                ]
                col_perm = [
                    [int(col_order[i] == j) for i in range(len(col_order))]
                    for j in range(len(col_order))
                ]
                s = mm(row_perm, result["left_transform_S"], p)
                t = mm(result["right_transform_T"], col_perm, p)
                ordered_shapes = [list(shapes[i]) for i in order]
                audit = verify_pencil_multi_direct_sum_witness(
                    q, k, p, s, t, ordered_shapes
                )
                self.assertTrue(audit["verification"]["direct_sum_verified"], audit)

    def test_multi_block_verifier_rejects_overlapping_or_inconsistent_partitions(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        s, t = result["left_transform_S"], result["right_transform_T"]
        invalid_partitions = (
            [], [[1, 2]], [[1, 2], [1, 2], [1, 1]],
            [[1, 2], [2, 1], [2, 1]],
            [[1, 2], [2, 1], [0, 0]],
            [[1, 2], [2, 1], [True, 1]],
            [[1, 2], [2, 1], [1, 1.0]],
            [[1, 2], [2, 1], [1]],
        )
        for shapes in invalid_partitions:
            with self.subTest(shapes=shapes):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(q, k, 5, s, t, shapes)

        for bad in (
            [[True, 0, 0, 0]] + [[0, 1, 0, 0]] * 3,
            [[1.5, 0, 0, 0]] + [[0, 1, 0, 0]] * 3,
        ):
            with self.subTest(matrix=bad):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(q, k, 5, bad, t, result["canonical_block_shapes"])
        with self.assertRaises(ValueError):
            verify_pencil_multi_direct_sum_witness(
                [[True, 0, 0, 0]] + [[0, 1, 0, 0]] * 3,
                k, 5, s, t, result["canonical_block_shapes"]
            )


    def test_multi_block_verifier_returns_failed_audit_for_singular_transforms(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        s, transform_t = result["left_transform_S"], result["right_transform_T"]
        singular_s = [row[:] for row in s]
        singular_s[-1] = [0] * len(singular_s[-1])
        audit_s = verify_pencil_multi_direct_sum_witness(
            q, k, 5, singular_s, transform_t, result["canonical_block_shapes"]
        )
        self.assertFalse(audit_s["verification"]["left_transform_invertible"])
        self.assertTrue(audit_s["verification"]["right_transform_invertible"])
        self.assertFalse(audit_s["verification"]["direct_sum_verified"])

        singular_t = [row[:] for row in transform_t]
        singular_t[-1] = [0] * len(singular_t[-1])
        audit_t = verify_pencil_multi_direct_sum_witness(
            q, k, 5, s, singular_t, result["canonical_block_shapes"]
        )
        self.assertTrue(audit_t["verification"]["left_transform_invertible"])
        self.assertFalse(audit_t["verification"]["right_transform_invertible"])
        self.assertFalse(audit_t["verification"]["direct_sum_verified"])

    def test_multi_block_verifier_normalizes_modularly_equivalent_inputs(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        s, t = result["left_transform_S"], result["right_transform_T"]
        shapes = result["canonical_block_shapes"]
        baseline = verify_pencil_multi_direct_sum_witness(q, k, 5, s, t, shapes)
        shift = lambda matrix, amount: [
            [value + amount * (i + j + 1) for j, value in enumerate(row)]
            for i, row in enumerate(matrix)
        ]
        equivalent = verify_pencil_multi_direct_sum_witness(
            shift(q, 5), shift(k, 10), 5, shift(s, 15), shift(t, 20), shapes
        )
        for key in ("source_shape", "block_shapes", "transformed_Q", "transformed_K",
                    "Q_blocks", "K_blocks", "verification"):
            with self.subTest(field=key):
                self.assertEqual(equivalent[key], baseline[key])

    def test_multi_block_verifier_field_boundaries_and_small_prime_controls(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = [[1, 0], [0, 1]], [[0, 0], [0, 1]]
        identity = [[1, 0], [0, 1]]
        shapes = [[1, 1], [1, 1]]
        for bad_p in (True, 2.0, 1, 4, 9):
            with self.subTest(bad_p=bad_p):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(
                        q, k, bad_p, identity, identity, shapes
                    )
        for p in (2, 3):
            with self.subTest(prime=p):
                audit = verify_pencil_multi_direct_sum_witness(
                    q, k, p, identity, identity, shapes
                )
                self.assertTrue(audit["verification"]["direct_sum_verified"], audit)

    def test_multi_block_verifier_rejects_malformed_nested_caller_matrices(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = self.mixed_pair()
        result = recover_mixed_kronecker_pencil(q, k, 5, max_degree=2)
        s, t, shapes = (
            result["left_transform_S"], result["right_transform_T"],
            result["canonical_block_shapes"],
        )
        malformed = (
            (None, k, s, t), ([], k, s, t),
            ([[1, 0], [0]], k, s, t),
            (q, [[0, 1], [0]], s, t),
            (q, k, [[1, 0], [0]], t),
            (q, k, s, [[1, 0], [0]]),
            (q, k, [[1], [0]], t),
            (q, k, s, [[1], [0]]),
        )
        for bad_q, bad_k, bad_s, bad_t in malformed:
            with self.subTest(q=bad_q, k=bad_k, s=bad_s, t=bad_t):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(
                        bad_q, bad_k, 5, bad_s, bad_t, shapes
                    )



    def test_multi_block_verifier_generated_rectangular_partitions_across_prime_fields(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        # Every partition has at least two blocks, positive total dimensions,
        # and includes zero-row and/or zero-column blocks without any 0x0 block.
        partitions = (
            [(0, 1), (1, 0), (1, 1)],
            [(1, 0), (0, 2), (2, 1)],
            [(1, 2), (2, 0), (0, 1), (1, 1)],
            [(2, 1), (0, 1), (1, 0), (1, 2)],
            [(1, 1), (1, 2), (2, 1)],
        )
        for p in (2, 3, 5, 7):
            for case, shapes in enumerate(partitions):
                with self.subTest(prime=p, case=case, shapes=shapes):
                    m, n = sum(r for r, _ in shapes), sum(c for _, c in shapes)
                    q = [[0] * n for _ in range(m)]
                    k = [[0] * n for _ in range(m)]
                    row_offsets, col_offsets = [0], [0]
                    for rows, cols in shapes:
                        row_offsets.append(row_offsets[-1] + rows)
                        col_offsets.append(col_offsets[-1] + cols)
                    # Populate only within-block entries. Empty row/column
                    # blocks naturally contribute no entries.
                    for block, (rows, cols) in enumerate(shapes):
                        for i in range(rows):
                            for j in range(cols):
                                q[row_offsets[block] + i][col_offsets[block] + j] = (
                                    case + block + i + 2 * j + 1
                                ) % p
                                k[row_offsets[block] + i][col_offsets[block] + j] = (
                                    2 * case + block + i + j + 1
                                ) % p
                    identity_m = [[int(i == j) for j in range(m)] for i in range(m)]
                    identity_n = [[int(i == j) for j in range(n)] for i in range(n)]
                    audit = verify_pencil_multi_direct_sum_witness(
                        q, k, p, identity_m, identity_n, shapes
                    )
                    self.assertTrue(audit["verification"]["direct_sum_verified"], audit)
                    self.assertEqual(audit["block_shapes"], [list(x) for x in shapes])

                    # If two blocks both have positive dimensions, injecting
                    # one cross-block coefficient must invalidate the witness.
                    cross_pair = next(
                        ((i, j) for i, (ri, _) in enumerate(shapes)
                         for j, (_, cj) in enumerate(shapes)
                         if i != j and ri > 0 and cj > 0),
                        None,
                    )
                    if cross_pair is not None:
                        i, j = cross_pair
                        mutated_q = [row[:] for row in q]
                        mutated_q[row_offsets[i]][col_offsets[j]] = 1 % p
                        rejected = verify_pencil_multi_direct_sum_witness(
                            mutated_q, k, p, identity_m, identity_n, shapes
                        )
                        self.assertFalse(
                            rejected["verification"]["Q_off_diagonal_blocks_zero"],
                            rejected,
                        )
                        self.assertFalse(
                            rejected["verification"]["direct_sum_verified"],
                            rejected,
                        )

    def test_multi_block_verifier_generated_partition_shape_rejections(self):
        from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

        q, k = [[0, 0], [0, 0]], [[0, 0], [0, 0]]
        identity = [[1, 0], [0, 1]]
        invalid = (
            [(0, 0), (2, 2)],
            [(0, 1), (0, 1)],  # no rows in the total partition
            [(1, 0), (1, 0)],  # no columns in the total partition
            [(1, 1), (1, 2)],  # column total mismatch
            [(1, 1), (2, 1)],  # row total mismatch
        )
        for shapes in invalid:
            with self.subTest(shapes=shapes):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(
                        q, k, 5, identity, identity, shapes
                    )


if __name__ == "__main__":
    unittest.main()
