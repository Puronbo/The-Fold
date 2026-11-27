"""Tests for compositional abstraction and layered coordinate transfer."""
import unittest
from fractions import Fraction as F

from agi.representation_transfer import AffineCoordinateMap as Map, AffineRelationConcept as Law
from agi.compositional_abstraction import (
    CompositionalAffineConcept, compare_compositional_structure,
    transfer_compositional_concept,
)


class CompositionalAbstractionTests(unittest.TestCase):
    def setUp(self):
        self.path = CompositionalAffineConcept((Law(2, 3), Law(3, -1), Law(F(1, 2), 4)))

    def test_composes_steps_in_execution_order(self):
        self.assertEqual(self.path.endpoint_signature, (F(3), F(11, 2)))
        self.assertEqual(self.path.evaluate_path(2), (F(7), F(20), F(14)))

    def test_different_paths_can_have_same_endpoint_function(self):
        direct = CompositionalAffineConcept((Law(3, F(11, 2)),))
        self.assertEqual(
            compare_compositional_structure(self.path, direct),
            "endpoint_equivalent_only",
        )

    def test_identical_paths_are_structurally_equivalent(self):
        clone = CompositionalAffineConcept((Law(2, 3), Law(3, -1), Law(F(1, 2), 4)))
        self.assertEqual(compare_compositional_structure(self.path, clone), "structurally_equivalent")

    def test_distinct_endpoint_functions_are_not_equivalent(self):
        other = CompositionalAffineConcept((Law(1, 0),))
        self.assertEqual(compare_compositional_structure(self.path, other), "not_equivalent")

    def test_layered_transfer_commutes_at_every_intermediate(self):
        maps = (
            Map(2, 5), Map(F(1, 3), -7), Map(-4, 2), Map(F(5, 2), 9),
        )
        result = transfer_compositional_concept(self.path, maps, (("a", 0), ("b", 2), ("c", -3)))
        self.assertEqual(result.status, "transferred")
        self.assertEqual(result.edge_commuting, (True, True, True))
        for key, target_values in result.target_intermediates:
            source_values = dict(result.source_intermediates)[key]
            for index, source in enumerate(source_values):
                self.assertEqual(target_values[index], maps[index + 1].forward(source))

    def test_transfer_is_derived_not_refit(self):
        maps = (Map(3, 1), Map(2, -1), Map(5, 4), Map(-2, 7))
        result = transfer_compositional_concept(self.path, maps, (("x", 4),))
        for source_step, target_step in zip(self.path.steps, result.mapped_path.steps):
            self.assertEqual(target_step.slope, source_step.slope * maps[result.mapped_path.steps.index(target_step)+1].scale / maps[result.mapped_path.steps.index(target_step)].scale)

    def test_requires_one_map_per_layer(self):
        with self.assertRaises(ValueError):
            transfer_compositional_concept(self.path, (Map(1, 0),), (("x", 0),))

    def test_duplicate_keys_rejected(self):
        maps = (Map(1, 0), Map(1, 0), Map(1, 0), Map(1, 0))
        with self.assertRaises(ValueError):
            transfer_compositional_concept(self.path, maps, (("x", 1), ("x", 2)))

    def test_empty_path_rejected(self):
        with self.assertRaises(ValueError):
            CompositionalAffineConcept(())

    def test_negative_and_fractional_coordinate_scales(self):
        maps = (Map(F(1, 2), 3), Map(-2, F(1, 3)), Map(7, -5), Map(F(2, 3), 9))
        result = transfer_compositional_concept(self.path, maps, (("q", F(3, 7)),))
        self.assertEqual(result.status, "transferred")


if __name__ == "__main__":
    unittest.main()
