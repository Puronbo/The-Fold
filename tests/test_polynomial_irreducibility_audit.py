import unittest

from tools.polynomial_irreducibility_audit import (
    audit_irreducibility_agreement,
    count_monic_irreducibles,
)


class PolynomialIrreducibilityAuditTests(unittest.TestCase):
    def test_exact_irreducible_count_formula(self):
        self.assertEqual(count_monic_irreducibles(2, 1), 2)
        self.assertEqual(count_monic_irreducibles(2, 5), 6)
        self.assertEqual(count_monic_irreducibles(3, 4), 18)
        self.assertEqual(count_monic_irreducibles(2, 6), 9)
        for p in (2, 3, 5, 7):
            for degree in range(1, 9):
                count = count_monic_irreducibles(p, degree)
                self.assertGreaterEqual(count, 0)
                self.assertLessEqual(count, p ** degree)

    def test_count_formula_validation(self):
        for p, degree in ((4, 2), (True, 2), (3, 0), (3, 2.0)):
            with self.subTest(p=p, degree=degree):
                with self.assertRaises(ValueError):
                    count_monic_irreducibles(p, degree)

    def test_exhaustive_domain_matches_exact_theory(self):
        result = audit_irreducibility_agreement(2, 5, max_cases=32)
        self.assertEqual(result["domain_size"], 32)
        self.assertEqual(result["checked_count"], 32)
        self.assertEqual(result["mode"], "exhaustive")
        self.assertTrue(result["complete"])
        self.assertTrue(result["agreement"])
        self.assertEqual(result["mismatch_count"], 0)
        self.assertEqual(result["predicate_irreducible_count_in_checked_set"], 6)
        self.assertEqual(result["theoretical_irreducible_count"], 6)
        self.assertEqual(result["observed_irreducible_density_in_checked_set"], 6 / 32)
        self.assertEqual(result["theoretical_count_match"], True)
        self.assertEqual(result["theoretical_normalized_irreducible_density"], 30 / 32)

    def test_sampled_mode_is_reproducible_and_theory_is_not_sample_count(self):
        args = dict(p=3, degree=8, max_cases=100,
                    sample_count=75, seed=20261124)
        first = audit_irreducibility_agreement(**args)
        second = audit_irreducibility_agreement(**args)
        self.assertEqual(first, second)
        self.assertEqual(first["domain_size"], 3 ** 8)
        self.assertEqual(first["checked_count"], 75)
        self.assertEqual(first["mode"], "deterministic_sample")
        self.assertFalse(first["complete"])
        self.assertTrue(first["agreement"])
        self.assertIsNone(first["theoretical_count_match"])
        self.assertEqual(first["theoretical_irreducible_count"],
                         count_monic_irreducibles(3, 8))
        self.assertAlmostEqual(
            first["expected_irreducibles_in_checked_set"],
            75 * first["theoretical_irreducible_density"],
        )

    def test_sample_larger_than_domain_checks_each_member_once(self):
        result = audit_irreducibility_agreement(
            2, 3, max_cases=1, sample_count=100, seed=7
        )
        self.assertEqual(result["checked_count"], 8)
        self.assertEqual(result["mode"], "deterministic_sample")
        self.assertTrue(result["complete"])
        self.assertTrue(result["theoretical_count_match"])

    def test_validation(self):
        invalid = (
            {"p": 4, "degree": 2},
            {"p": 3, "degree": 0},
            {"p": 3, "degree": 2, "max_cases": 0},
            {"p": 3, "degree": 2, "sample_count": 0},
            {"p": True, "degree": 2},
            {"p": 3, "degree": 2.0},
        )
        for kwargs in invalid:
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    audit_irreducibility_agreement(**kwargs)


if __name__ == "__main__":
    unittest.main()
