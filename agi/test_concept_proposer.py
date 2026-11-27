"""Regression tests for typed quantities, compound units and affine units."""

import unittest
from decimal import Decimal
from fractions import Fraction

from agi.concept_learner import ConceptLearner
from agi.concept_proposer import (
    UnitQuantityProposer,
    parse_measurement,
    parse_quantity,
    parse_unit_expression,
)


class CompoundUnitTests(unittest.TestCase):
    def test_speed_conversion_is_exact(self):
        kmh = parse_quantity({"value": 36, "unit": "km/h"})
        ms = parse_quantity({"value": 10, "unit": "m/s"})
        self.assertEqual(kmh.dimension, (1, 0, -1, 0))
        self.assertEqual(kmh.base_value, Fraction(10))
        self.assertEqual(kmh, ms)

    def test_acceleration_has_second_order_time_dimension(self):
        acceleration = parse_quantity({"value": 1, "unit": "m/s^2"})
        self.assertEqual(acceleration.dimension, (1, 0, -2, 0))
        self.assertEqual(acceleration.base_value, Fraction(1))

    def test_newton_matches_base_compound_expression(self):
        self.assertEqual(
            parse_quantity({"value": 1, "unit": "N"}),
            parse_quantity({"value": 1, "unit": "kg*m/s^2"}),
        )

    def test_derived_units_match(self):
        cases = [
            ({"value": 1, "unit": "J"}, {"value": 1, "unit": "N*m"}),
            ({"value": 1, "unit": "W"}, {"value": 1, "unit": "J/s"}),
            ({"value": 1, "unit": "Pa"}, {"value": 1, "unit": "N/m^2"}),
            ({"value": 1, "unit": "Hz"}, {"value": 1, "unit": "1/s"}),
        ]
        for left, right in cases:
            self.assertEqual(parse_quantity(left), parse_quantity(right))

    def test_inverse_and_repeated_unit_powers(self):
        self.assertEqual(parse_unit_expression("m/s^2"), ((1, 0, -2, 0), Fraction(1)))
        self.assertEqual(parse_unit_expression("km/h"), ((1, 0, -1, 0), Fraction(5, 18)))
        self.assertEqual(parse_unit_expression("m*m"), ((2, 0, 0, 0), Fraction(1)))

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


class TypedAndAffineQuantityTests(unittest.TestCase):
    def test_energy_and_torque_are_distinct_when_typed(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("energy", {"value": 1, "unit": "J", "kind": "energy"})
        learner.add_instance("torque", {"value": 1, "unit": "N*m", "kind": "torque"})
        batch = UnitQuantityProposer().apply(learner)
        self.assertFalse(learner.equivalent("energy", "torque"))
        self.assertTrue(batch.counterexamples)

    def test_equal_dimension_without_kind_remains_untyped(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("energy", {"value": 1, "unit": "J", "kind": "energy"})
        learner.add_instance("untyped", {"value": 1, "unit": "N*m"})
        UnitQuantityProposer().apply(learner)
        self.assertFalse(learner.equivalent("energy", "untyped"))

    def test_celsius_fahrenheit_kelvin_absolute_temperature(self):
        values = [
            parse_quantity({"value": 0, "unit": "degC"}),
            parse_quantity({"value": 32, "unit": "degF"}),
            parse_quantity({"value": Decimal("273.15"), "unit": "K"}),
        ]
        self.assertEqual(values[0], values[1])
        self.assertEqual(values[1], values[2])
        self.assertEqual(values[0].kind, "absolute_temperature")

    def test_temperature_affine_conversion_uses_offset(self):
        freezing = parse_quantity({"value": 0, "unit": "degC"})
        boiling = parse_quantity({"value": 100, "unit": "degC"})
        self.assertEqual(boiling.base_value - freezing.base_value, Fraction(100))

    def test_temperature_intervals_are_not_absolute_temperatures(self):
        ten_c = parse_quantity({"value": 10, "unit": "deltaC"})
        eighteen_f = parse_quantity({"value": 18, "unit": "deltaF"})
        absolute = parse_quantity({"value": 10, "unit": "degC"})
        self.assertEqual(ten_c, eighteen_f)
        self.assertNotEqual(ten_c, absolute)
        self.assertEqual(ten_c.kind, "temperature_interval")

    def test_affine_units_cannot_be_used_in_compound_expression(self):
        for unit in ("degC/s", "K*m", "degF^2"):
            self.assertIsNone(parse_unit_expression(unit))

    def test_affine_unit_kind_cannot_be_overridden(self):
        self.assertIsNone(parse_quantity({"value": 20, "unit": "degC", "kind": "temperature_interval"}))

    def test_proposer_finds_affine_temperature_equivalence(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("celsius", {"value": 0, "unit": "degC"})
        learner.add_instance("fahrenheit", {"value": 32, "unit": "degF"})
        learner.add_instance("kelvin", {"value": Decimal("273.15"), "unit": "K"})
        UnitQuantityProposer().apply(learner)
        self.assertTrue(learner.equivalent("celsius", "fahrenheit"))
        self.assertTrue(learner.equivalent("fahrenheit", "kelvin"))


class MeasurementUncertaintyTests(unittest.TestCase):
    def test_overlapping_intervals_are_compatible_not_equivalent(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("celsius_range", {
            "value": 10, "unit": "degC",
            "uncertainty": {"type": "interval", "lower": 9, "upper": 11},
        })
        learner.add_instance("fahrenheit_range", {
            "value": 50, "unit": "degF",
            "uncertainty": {"type": "interval", "lower": 49, "upper": 51},
        })
        batch = UnitQuantityProposer().apply(learner)
        self.assertFalse(learner.equivalent("celsius_range", "fahrenheit_range"))
        self.assertEqual(len(batch.compatibilities), 1)
        self.assertLessEqual(
            batch.compatibilities[0].overlap_lower,
            batch.compatibilities[0].overlap_upper,
        )

    def test_nonoverlapping_intervals_are_not_compatible(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("low", {
            "value": 1, "unit": "m",
            "uncertainty": {"type": "interval", "lower": 0, "upper": 2},
        })
        learner.add_instance("high", {
            "value": 4, "unit": "m",
            "uncertainty": {"type": "interval", "lower": 3, "upper": 5},
        })
        batch = UnitQuantityProposer().propose(learner)
        self.assertEqual(batch.compatibilities, ())
        self.assertEqual(batch.equivalences, ())

    def test_exact_observation_can_be_compatible_with_interval(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("exact", {"value": 10, "unit": "m"})
        learner.add_instance("measured", {
            "value": 11, "unit": "m",
            "uncertainty": {"type": "interval", "lower": 9, "upper": 12},
        })
        batch = UnitQuantityProposer().propose(learner)
        self.assertEqual(len(batch.compatibilities), 1)
        self.assertEqual(batch.equivalences, ())

    def test_calibration_correction_is_applied_before_normalization(self):
        corrected = parse_measurement({
            "value": 99, "unit": "cm", "calibration_correction": 1,
        })
        one_metre = parse_measurement({"value": 1, "unit": "m"})
        self.assertEqual(corrected.quantity.base_value, one_metre.quantity.base_value)

    def test_interval_bounds_receive_calibration_correction(self):
        measured = parse_measurement({
            "value": 10, "unit": "m", "calibration_correction": 1,
            "uncertainty": {"type": "interval", "lower": 9, "upper": 11},
        })
        self.assertEqual(measured.lower, Fraction(10))
        self.assertEqual(measured.upper, Fraction(12))
        self.assertEqual(measured.quantity.base_value, Fraction(11))

    def test_invalid_or_unspecified_probability_models_are_not_inferred(self):
        for uncertainty in (
            {"type": "interval", "lower": 2, "upper": 1},
            {"type": "interval", "lower": 0, "upper": 0},
            {"type": "standard", "value": 0.1},
            {"type": "expanded", "value": 2, "coverage_factor": 2},
        ):
            payload = {"value": 1, "unit": "m", "uncertainty": uncertainty}
            self.assertIsNone(parse_measurement(payload))

    def test_absolute_temperature_interval_normalizes_affinely(self):
        celsius = parse_measurement({
            "value": 0, "unit": "degC",
            "uncertainty": {"type": "interval", "lower": -1, "upper": 1},
        })
        fahrenheit = parse_measurement({
            "value": 32, "unit": "degF",
            "uncertainty": {"type": "interval", "lower": 30.2, "upper": 33.8},
        })
        # Floats are deliberately rejected; decimal text is exact.
        self.assertIsNone(fahrenheit)
        fahrenheit = parse_measurement({
            "value": 32, "unit": "degF",
            "uncertainty": {
                "type": "interval",
                "lower": Decimal("30.2"), "upper": Decimal("33.8"),
            },
        })
        self.assertEqual(celsius.lower, fahrenheit.lower)
        self.assertEqual(celsius.upper, fahrenheit.upper)


class StageNineRegressionTests(unittest.TestCase):
    def test_single_unit_equivalence_and_hard_negative(self):
        learner = ConceptLearner("physical quantity equality")
        learner.add_instance("m", {"value": 1, "unit": "m"})
        learner.add_instance("cm", {"value": 100, "unit": "cm"})
        learner.add_instance("s", {"value": 1, "unit": "s"})
        batch = UnitQuantityProposer().apply(learner)
        self.assertTrue(learner.equivalent("m", "cm"))
        self.assertFalse(learner.equivalent("m", "s"))
        self.assertTrue(batch.counterexamples)

    def test_unknown_units_and_invalid_numeric_values_are_skipped(self):
        for payload in (
            {"value": 1, "unit": "parsec"},
            {"value": 0.1, "unit": "m"},
            {"value": True, "unit": "m"},
            {"value": Decimal("NaN"), "unit": "m"},
            {"value": Decimal("Infinity"), "unit": "m"},
            {"value": "1", "unit": "m"},
            ["1", "m"],
        ):
            self.assertIsNone(parse_quantity(payload))

    def test_wrong_context_is_rejected(self):
        learner = ConceptLearner("visual similarity")
        learner.add_instance("a", {"value": 1, "unit": "m"})
        with self.assertRaises(ValueError):
            UnitQuantityProposer().propose(learner)


if __name__ == "__main__":
    unittest.main()
