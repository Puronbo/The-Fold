"""Regression tests for exact relational composition."""
import unittest
from fractions import Fraction as F
from agi.relation_discovery import RelationalConceptProposer
from agi.relation_composition import ComposedRelation


def hypothesis(relation, rows):
    proposer = RelationalConceptProposer()
    for key, x, y in rows:
        proposer.add_observation(key, x, y)
    return next(item for item in proposer.propose() if item.relation == relation)


class RelationCompositionTests(unittest.TestCase):
    def test_affine_after_affine(self):
        first = ComposedRelation.from_hypothesis(hypothesis("affine", [("a",0,1),("b",1,3),("c",2,5)]))
        second = ComposedRelation.from_hypothesis(hypothesis("affine", [("a",0,4),("b",1,7),("c",2,10)]))
        combined = first.then(second)
        self.assertEqual(combined.coefficients, (F(6), F(7), F(0), F(1)))
        self.assertEqual(combined.evaluate(2), F(19))
        self.assertEqual(combined.provenance, ("affine", "affine"))

    def test_proportional_after_affine(self):
        first = ComposedRelation.from_hypothesis(hypothesis("affine", [("a",0,2),("b",1,3),("c",2,4)]))
        second = ComposedRelation.from_hypothesis(hypothesis("proportional", [("a",1,5),("b",2,10)]))
        combined = first.then(second)
        self.assertEqual(combined.evaluate(3), F(20))
        self.assertEqual(combined.coefficients, (F(5), F(10), F(0), F(1)))

    def test_inverse_composition_tracks_intermediate_pole(self):
        first = ComposedRelation.from_hypothesis(hypothesis("inverse", [("a",1,6),("b",2,3),("c",3,2)]))
        second = ComposedRelation.from_hypothesis(hypothesis("affine", [("a",0,1),("b",1,3),("c",2,5)]))
        combined = first.then(second)
        self.assertEqual(combined.evaluate(2), F(7))
        self.assertIn(F(0), combined.domain_exclusions)
        with self.assertRaises(ZeroDivisionError):
            combined.evaluate(0)

    def test_outer_inverse_pole_pulled_back(self):
        first = ComposedRelation.from_hypothesis(hypothesis("affine", [("a",0,1),("b",1,2),("c",2,3)]))
        second = ComposedRelation.from_hypothesis(hypothesis("inverse", [("a",1,8),("b",2,4),("c",4,2)]))
        combined = first.then(second)
        self.assertIn(F(-1), combined.domain_exclusions)
        with self.assertRaises(ZeroDivisionError):
            combined.evaluate(-1)

    def test_refuted_hypothesis_cannot_be_composed(self):
        bad = hypothesis("proportional", [("a",1,2),("b",2,4),("c",3,8)])
        with self.assertRaises(ValueError):
            ComposedRelation.from_hypothesis(bad)

    def test_exact_fraction_coefficients(self):
        first = ComposedRelation((F(1,2), F(1,3), F(0), F(1)))
        second = ComposedRelation((F(3,2), F(0), F(0), F(1)))
        self.assertEqual(first.then(second).evaluate(1), F(5,4))

    def test_constant_map_and_zero_matrix(self):
        self.assertEqual(ComposedRelation((F(0),F(5),F(0),F(1))).evaluate(100), F(5))
        with self.assertRaises(ValueError):
            ComposedRelation((F(0),F(0),F(0),F(0)))


if __name__ == "__main__":
    unittest.main()
