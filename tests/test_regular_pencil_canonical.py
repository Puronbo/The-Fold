import unittest

from tools.regular_pencil_canonical import regular_pencil_canonical_form


class RegularPencilCanonicalTests(unittest.TestCase):
    def test_finite_linear_divisor_block(self):
        result = regular_pencil_canonical_form([[-3]], [[1]], 7)
        self.assertEqual(result["canonical_Q"], [[-3 % 7]])
        self.assertEqual(result["canonical_K"], [[1]])
        self.assertTrue(result["checks"]["canonical_profile_matches_source"])

    def test_pure_infinity_block(self):
        q = [[1, 0], [0, 1]]
        k = [[0, 1], [0, 0]]
        result = regular_pencil_canonical_form(q, k, 5)
        self.assertEqual(result["infinity_blocks"][0]["size"], 2)
        self.assertEqual(result["canonical_Q"], [[1, 0], [0, 1]])
        self.assertEqual(result["canonical_K"], [[0, 1], [0, 0]])

    def test_mixed_finite_and_infinity_blocks(self):
        q = [[2, 0], [0, 1]]
        k = [[1, 0], [0, 0]]
        result = regular_pencil_canonical_form(q, k, 5)
        self.assertEqual(result["dimension"], 2)
        self.assertEqual(len(result["finite_blocks"]), 1)
        self.assertEqual(result["infinity_blocks"], [{"size": 1, "Q_block": [[1]], "K_block": [[0]]}])
        self.assertTrue(result["checks"]["canonical_profile_matches_source"])

    def test_no_rational_projective_pivot(self):
        q = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        k = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = regular_pencil_canonical_form(q, k, 2)
        self.assertTrue(result["checks"]["canonical_profile_matches_source"])
        self.assertEqual(result["dimension"], 3)

    def test_rejects_singular_pencil(self):
        with self.assertRaises(ValueError):
            regular_pencil_canonical_form([[1, 0], [0, 0]], [[0, 0], [0, 0]], 3)


if __name__ == "__main__":
    unittest.main()
