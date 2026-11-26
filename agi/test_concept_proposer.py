"""Tests for exact compound-unit concept proposals."""

import unittest
from decimal import Decimal
from fractions import Fraction

from agi.concept_learner import ConceptLearner
from agi.concept_proposer import (
    UnitQuantityProposer,
    parse_quantity,
    parse_unit_expression,
)


class CompoundUnitTests(unittest.TestCase):
    def test_speed_conversion_is_exact(self):
        kmh = parse_quantity({"value": 36, "unit": "km/h"})
        ms = parse_quantity({"value": 10, "unit": "m/s"})
        self.assertEqual(kmh.dimension, (1, 0, -1))
        self.assertEqual(kmh.base_value, Fraction(10))
        self.assertEqual(kmh, ms)

    def test_acceleration_has_second_order_time_dimension(self):
        acceleration = parse_quantity({"value": 1, "unit": "m/s^2"})
        self.assertEqual(acceleration.dimension, (1, 0, -2))
        self.assertEqual(acceleration.base_value, Fraction(1))

    def test_newton_matches_base_compound_expression(self):
        newton = parse_quantity({"value": 1, "unit": "N"})
        base = parse_quantity({"value": 1, "unit": "kg*m/s^2"})
        self.assertEqual(newton, base)

    def test_derived_units_match(self):
        cases = [
            ({"value": 1, "unit": "J"}, {"value": 1, "unit": "N*m"}),
            ({"value": 1, "unit": "W"}, {"value": 1, "unit": "J/s"}),
            ({"value": 1, "unit": "Pa"}, {"value": 1, "unit": "N/m^2"}),
            ({"value": 1, "unit": "Hz"}, {"value": 1, "unit": "1/s"}),
        ]
        # The grammar intentionally has no standalone scalar '1' token.
        for left, right in cases[:-1]:
            self.assertEqual(parse_quantity(left), parse_quantity(right))
        self.assertIsNone(parse_quantity(cases[-1][1]))

    def test_inverse_and_repeated_unit_powers(self):
        self.assertEqual(
            parse_unit_expression("m/s^2"),
            ((1, 0, -2), Fraction(1)),
        )
        self.assertEqual(
            parse_unit_expression("km/h"),
            ((1, 0, -1), Fraction(5, 18)),
        )
        self.assertEqual(
            parse_unit_expression("m*m"),
            ((2, 0, 0), Fraction(1)),
        )

    def test_malformed_or_unsupported_expressions_are_rejected(self):
        for unit in ("", "m/", "/s", "m**s", "m//s", "m s", "(m/s)", "m^99", "unknown"):
            self.assertIsNone(parse_unit_expression(unit))

    def test_exact_decimal_and_float_policy(self):
        self.assertEqual(
            parse_quantity({"value": Decimal("0.1"), "unit": "m"}).base_value,
            Fraction(1, 10),
        )
        self.assertIsNone(parse_quantity({"value": 0.1, "unit": "m"}))

    def test_proposer_discovers_speed_and_force_equivalence(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("speed_kmh", {"value": 36, "unit": "km/h"})
        learner.add_instance("speed_ms", {"value": 10, "unit": "m/s"})
        learner.add_instance("force_newton", {"value": 1, "unit": "N"})
        learner.add_instance("force_base", {"value": 1, "unit": "kg*m/s^2"})
        learner.add_instance("energy_joule", {"value": 1, "unit": "J"})

        batch = UnitQuantityProposer().apply(learner)
        self.assertTrue(learner.equivalent("speed_kmh", "speed_ms"))
        self.assertTrue(learner.equivalent("force_newton", "force_base"))
        self.assertFalse(learner.equivalent("force_newton", "energy_joule"))
        self.assertTrue(batch.counterexamples)

    def test_proposer_keeps_dimension_vectors_separate(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("one_metre", {"value": 1, "unit": "m"})
        learner.add_instance("one_second", {"value": 1, "unit": "s"})
        UnitQuantityProposer().apply(learner)
        self.assertFalse(learner.equivalent("one_metre", "one_second"))


if __name__ == "__main__":
    unittest.main()
