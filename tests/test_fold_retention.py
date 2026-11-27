import unittest
from dataclasses import replace
from fractions import Fraction

from tools.FoldConcept import Context, Instance
from tools.FoldRetention import (
    minimum_retention_features, retention_plan_proves_optimality,
    verify_retention_plan, verify_search_certificate,
)


class FoldRetentionTests(unittest.TestCase):
    def setUp(self):
        self.instances = (
            Instance.make("a", {"shape": "round", "colour": "red",
                                "material": "rubber", "weight": 1}),
            Instance.make("b", {"shape": "round", "colour": "blue",
                                "material": "rubber", "weight": 1}),
            Instance.make("c", {"shape": "round", "colour": "red",
                                "material": "metal", "weight": 2}),
            Instance.make("d", {"shape": "round", "colour": "red",
                                "material": "cardboard", "weight": 3}),
            Instance.make("e", {"shape": "round", "colour": "red",
                                "material": "rubber", "weight": 9}),
        )
        self.base = Context("object-task", ("shape",))
        self.must = (("a", "e"),)
        self.cannot = (("a", "b"), ("a", "d"))

    def test_finds_minimum_safe_residual_features(self):
        plan = minimum_retention_features(
            self.instances, self.base, ("colour", "material", "weight"),
            self.must, self.cannot,
        )
        self.assertIsNotNone(plan)
        self.assertEqual(plan.retained_features, ("colour", "material"))
        self.assertTrue(verify_retention_plan(
            self.instances, plan, self.must, self.cannot
        ))

    def test_nonuniform_rational_dual_certifies_optimum(self):
        instances = (
            Instance.make("w0", {"shape": "round", "f1": 0, "f2": 0, "f3": 0, "f4": 0}),
            Instance.make("w1", {"shape": "round", "f1": 1, "f2": 1, "f3": 0, "f4": 0}),
            Instance.make("w2", {"shape": "round", "f1": 1, "f2": 0, "f3": 1, "f4": 0}),
            Instance.make("w3", {"shape": "round", "f1": 0, "f2": 0, "f3": 0, "f4": 1}),
        )
        cannot = (("w0", "w1"), ("w0", "w2"), ("w0", "w3"))
        plan = minimum_retention_features(
            instances, self.base, ("f1", "f2", "f3", "f4"), (), cannot
        )
        self.assertIsNotNone(plan)
        objective = sum(
            (Fraction(n, d) for n, d in plan.dual_weights), Fraction(0)
        )
        self.assertEqual(objective, Fraction(2, 1))
        self.assertEqual(len(plan.retained_features), 2)
        self.assertTrue(retention_plan_proves_optimality(
            instances, self.base, ("f1", "f2", "f3", "f4"), (), cannot, plan
        ))

    def test_fractional_dual_certifies_beyond_pair_packing(self):
        instances = (
            Instance.make("t0", {"shape": "round", "fa": 0, "fb": 0, "fc": 0}),
            Instance.make("t1", {"shape": "round", "fa": 1, "fb": 0, "fc": 1}),
            Instance.make("t2", {"shape": "round", "fa": 1, "fb": 1, "fc": 0}),
            Instance.make("t3", {"shape": "round", "fa": 0, "fb": 1, "fc": 1}),
        )
        cannot = (("t0", "t1"), ("t0", "t2"), ("t0", "t3"))
        plan = minimum_retention_features(
            instances, self.base, ("fa", "fb", "fc"), (), cannot
        )
        self.assertIsNotNone(plan)
        objective = sum(
            (Fraction(n, d) for n, d in plan.dual_weights), Fraction(0)
        )
        self.assertEqual(objective, Fraction(3, 2))
        self.assertEqual(len(plan.lower_bound_pairs), 1)
        self.assertEqual(len(plan.retained_features), 2)
        self.assertTrue(retention_plan_proves_optimality(
            instances, self.base, ("fa", "fb", "fc"), (), cannot, plan
        ))

    def test_exhaustive_search_certificate_is_independently_checked(self):
        plan = minimum_retention_features(
            self.instances, self.base, ("colour", "material", "weight"),
            self.must, self.cannot,
        )
        self.assertIsNotNone(plan)
        self.assertTrue(verify_search_certificate(
            self.instances, self.base, ("colour", "material", "weight"),
            self.must, self.cannot, plan,
        ))
        corrupted = replace(plan, search_certificate=("depth",))
        self.assertFalse(verify_search_certificate(
            self.instances, self.base, ("colour", "material", "weight"),
            self.must, self.cannot, corrupted,
        ))
        self.assertTrue(retention_plan_proves_optimality(
            self.instances, self.base, ("colour", "material", "weight"),
            self.must, self.cannot, plan,
        ))

    def test_returns_none_when_no_safe_feature_set_exists(self):
        plan = minimum_retention_features(
            self.instances, self.base, ("colour", "weight"),
            self.must, self.cannot,
        )
        self.assertIsNone(plan)

    def test_no_memory_needed_when_base_already_separates_pairs(self):
        context = Context("shape-colour", ("shape", "colour"))
        plan = minimum_retention_features(
            self.instances, context, ("material", "weight"),
            self.must, (("a", "b"),),
        )
        self.assertIsNotNone(plan)
        self.assertEqual(plan.retained_features, ())

    def test_rejects_duplicate_candidates_and_unknown_ids(self):
        with self.assertRaises(ValueError):
            minimum_retention_features(
                self.instances, self.base, ("colour", "colour"),
                self.must, self.cannot,
            )
        with self.assertRaises(KeyError):
            minimum_retention_features(
                self.instances, self.base, ("colour",),
                (), (("a", "missing"),),
            )


if __name__ == "__main__":
    unittest.main()
