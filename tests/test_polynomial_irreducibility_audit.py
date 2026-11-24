import unittest

from tools.polynomial_irreducibility_audit import (
    audit_irreducibility_agreement,
)


class PolynomialIrreducibilityAuditTests(unittest.TestCase):
    def test_exhaustive_domain(self):
        result = audit_irreducibility_agreement(2, 5, max_cases=32)
        self.assertEqual(result["domain_size"], 32)
        self.assertEqual(result["checked_count"], 32)
        self.assertEqual(result["mode"], "exhaustive")
        self.assertTrue(result["complete"])
        self.assertTrue(result["agreement"])
        self.assertEqual(result["mismatch_count"], 0)
        self.assertEqual(result["predicate_irreducible_count_in_checked_set"], 6)

    def test_sampled_mode_is_reproducible_and_incomplete(self):
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

    def test_sample_larger_than_domain_checks_each_member_once(self):
        result = audit_irreducibility_agreement(
            2, 3, max_cases=1, sample_count=100, seed=7
        )
        self.assertEqual(result["checked_count"], 8)
        self.assertEqual(result["mode"], "deterministic_sample")
        self.assertFalse(result["complete"])

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
