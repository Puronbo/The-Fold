import unittest

from tools.regular_pencil_witness import construct_regular_pencil_witness


def mm(a, b, p):
    return [[sum(a[i][r] * b[r][j] for r in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


class RegularPencilWitnessTests(unittest.TestCase):
    def test_constructs_and_verifies_strict_equivalence_witness(self):
        q = [[1, 0], [0, 1]]
        k = [[1, 1], [0, 2]]
        s0 = [[1, 1], [0, 1]]
        t0 = [[1, 0], [1, 1]]
        q2, k2 = mm(mm(s0, q, 5), t0, 5), mm(mm(s0, k, 5), t0, 5)
        result = construct_regular_pencil_witness(q, k, q2, k2, 5)
        self.assertTrue(result["witness_found"])
        self.assertTrue(result["checks"]["S_Qa_T_equals_Qb"])
        self.assertTrue(result["checks"]["S_Ka_T_equals_Kb"])
        self.assertTrue(result["checks"]["S_invertible"])
        self.assertTrue(result["checks"]["T_invertible"])

    def test_constructs_witness_using_infinity_chart(self):
        q = [[1, 0], [0, 0]]
        k = [[1, 0], [0, 1]]
        s0 = [[1, 1], [0, 1]]
        t0 = [[1, 0], [1, 1]]
        q2, k2 = mm(mm(s0, q, 2), t0, 2), mm(mm(s0, k, 2), t0, 2)
        result = construct_regular_pencil_witness(q, k, q2, k2, 2)
        self.assertTrue(result["witness_found"])
        self.assertEqual(result["common_chart"]["kind"], "infinity")

    def test_inconclusive_when_no_base_field_chart_exists(self):
        q = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        k = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = construct_regular_pencil_witness(q, k, q, k, 2)
        self.assertFalse(result["decision_complete"])
        self.assertIsNone(result["strictly_equivalent"])

    def test_candidate_budget_returns_inconclusive(self):
        q = [[1, 0], [0, 1]]
        k = [[0, 1], [0, 0]]
        result = construct_regular_pencil_witness(
            q, k, q, k, 5, max_candidates=1
        )
        self.assertFalse(result["decision_complete"])
        self.assertIsNone(result["strictly_equivalent"])

    def test_different_profiles_decide_non_equivalence(self):
        result = construct_regular_pencil_witness(
            [[1, 0], [0, 1]], [[1, 0], [0, 1]],
            [[1, 0], [0, 1]], [[1, 1], [0, 1]], 5
        )
        self.assertTrue(result["decision_complete"])
        self.assertFalse(result["strictly_equivalent"])


if __name__ == "__main__":
    unittest.main()
