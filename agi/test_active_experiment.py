"""Tests for exact active experiment design."""
import unittest
from fractions import Fraction

from agi.active_experiment import design_discriminating_experiment
from agi.relation_composition import ComposedRelation
from agi.relation_selection import RelationCandidate


def affine(a, b):
    return ComposedRelation((Fraction(a), Fraction(b), Fraction(0), Fraction(1)))


class ActiveExperimentTests(unittest.TestCase):
    def test_selects_input_with_largest_exact_disagreement(self):
        candidates = (
            RelationCandidate("identity", (affine(1, 0),)),
            RelationCandidate("double", (affine(2, 0),)),
            RelationCandidate("offset", (affine(1, 3),)),
        )
        result = design_discriminating_experiment(candidates, (0, 1, 2))
        self.assertEqual(result.status, "input_selected")
        self.assertEqual(result.selected_input, Fraction(2))
        self.assertEqual(result.selected_option.pairwise_disagreement, Fraction(7))

    def test_domain_failure_reduces_coverage(self):
        inverse = ComposedRelation((0, 1, 1, 0), (Fraction(0),))
        candidates = (
            RelationCandidate("inverse", (inverse,)),
            RelationCandidate("identity", (affine(1, 0),)),
        )
        result = design_discriminating_experiment(candidates, (0, 1))
        self.assertEqual(result.selected_input, Fraction(1))
        at_zero = next(option for option in result.ranked_options if option.input_value == 0)
        self.assertEqual(at_zero.defined_candidates, 1)
        self.assertIsNone(at_zero.predictions[0].value)

    def test_no_disagreement_is_explicit(self):
        candidates = (
            RelationCandidate("a", (affine(1, 2),)),
            RelationCandidate("b", (affine(1, 2),)),
        )
        result = design_discriminating_experiment(candidates, (0, 1, 2))
        self.assertEqual(result.status, "no_discriminating_input")
        self.assertIsNone(result.selected_input)

    def test_equivalent_candidate_paths_do_not_create_false_disagreement(self):
        direct = RelationCandidate("direct", (affine(1, 1),))
        split = RelationCandidate("split", (affine(1, 0), affine(1, 1)))
        result = design_discriminating_experiment((direct, split), (0, 1))
        self.assertEqual(result.status, "no_discriminating_input")

    def test_exact_fraction_inputs_and_outputs(self):
        candidates = (
            RelationCandidate("identity", (affine(1, 0),)),
            RelationCandidate("half", (affine(Fraction(1, 2), 0),)),
        )
        result = design_discriminating_experiment(candidates, (Fraction(1, 3),))
        self.assertEqual(result.selected_option.pairwise_disagreement, Fraction(1, 6))

    def test_rejects_float_and_boolean_inputs(self):
        candidate = (RelationCandidate("identity", (affine(1, 0),)),)
        with self.assertRaises(TypeError):
            design_discriminating_experiment(candidate, (0.5,))
        with self.assertRaises(TypeError):
            design_discriminating_experiment(candidate, (True,))

    def test_rejects_duplicate_ids_and_inputs(self):
        one = RelationCandidate("same", (affine(1, 0),))
        two = RelationCandidate("same", (affine(2, 0),))
        with self.assertRaises(ValueError):
            design_discriminating_experiment((one, two), (0, 1))
        with self.assertRaises(ValueError):
            design_discriminating_experiment((one,), (1, 1))

    def test_empty_domain_returns_no_discriminating_input(self):
        candidates = (
            RelationCandidate("one", (affine(1, 0),)),
            RelationCandidate("two", (affine(2, 0),)),
        )
        result = design_discriminating_experiment(candidates, ())
        self.assertEqual(result.status, "no_discriminating_input")
        self.assertEqual(result.ranked_options, ())


if __name__ == "__main__":
    unittest.main()
