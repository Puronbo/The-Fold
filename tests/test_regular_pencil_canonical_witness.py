import unittest

from tools.regular_pencil_canonical_witness import regular_pencil_canonical_witness


def mm(a, b, p):
    return [[sum(a[i][r] * b[r][j] for r in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


class RegularPencilCanonicalWitnessTests(unittest.TestCase):
    def assert_certificate(self, result, p):
        self.assertTrue(result["canonical_profile_verified"])
        self.assertTrue(result["witness_found"])
        s, t = result["left_transform_S"], result["right_transform_T"]
        self.assertEqual(mm(mm(s, self.q, p), t, p), result["canonical_Q"])
        self.assertEqual(mm(mm(s, self.k, p), t, p), result["canonical_K"])
        self.assertTrue(result["witness_details"]["checks"]["S_invertible"])
        self.assertTrue(result["witness_details"]["checks"]["T_invertible"])

    def test_chart_based_canonical_certificate(self):
        self.q = [[1, 0], [0, 1]]
        self.k = [[1, 1], [0, 2]]
        result = regular_pencil_canonical_witness(self.q, self.k, 5)
        self.assert_certificate(result, 5)
        self.assertEqual(result["construction_method"], "shared-chart operator intertwiner")

    def test_no_chart_canonical_certificate(self):
        self.q = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        self.k = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = regular_pencil_canonical_witness(
            self.q, self.k, 2, max_candidates=100_000
        )
        self.assert_certificate(result, 2)
        self.assertEqual(result["construction_method"], "bounded direct finite-field search")


if __name__ == "__main__":
    unittest.main()
