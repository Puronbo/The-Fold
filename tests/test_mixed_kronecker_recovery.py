import unittest
from itertools import permutations
from unittest.mock import patch
from itertools import product

from tools.mixed_kronecker_recovery import (
    _affine_vectors, _det, _exhaustive_left_matrices, recover_mixed_kronecker_pencil,
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


if __name__ == "__main__":
    unittest.main()
