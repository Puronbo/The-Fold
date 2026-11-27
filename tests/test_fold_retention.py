import unittest

from tools.FoldConcept import Context, Instance
from tools.FoldRetention import minimum_retention_features, verify_retention_plan


class FoldRetentionTests(unittest.TestCase):
    def setUp(self):
        self.instances = (
            Instance.make("a", {"shape": "round", "colour": "red",
                                "material": "rubber", "weight": 1}),
            Instance.make("b", {"shape": "round", "colour": "blue",
                                "material": "rubber", "weight": 1}),
            Instance.make("c", {"shape": "round", "colour": "red",
                                "material": "metal", "weight": 2}),
            Instance.make("d", {"shape": "square", "colour": "red",
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
