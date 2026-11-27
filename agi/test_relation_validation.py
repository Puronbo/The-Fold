"""Independent held-out validation tests for composed relational paths."""
import unittest
from fractions import Fraction as F
from agi.relation_composition import ComposedRelation
from agi.relation_validation import ValidationObservation, validate_composed_path

class RelationValidationTests(unittest.TestCase):
    def test_held_out_rows_validate_affine_composition(self):
        first = ComposedRelation((F(2), F(1), F(0), F(1)), provenance=("affine-1",))
        second = ComposedRelation((F(3), F(4), F(0), F(1)), provenance=("affine-2",))
        rows = [
            ValidationObservation.create("heldout-a", 3, 25, (7, 25)),
            ValidationObservation.create("heldout-b", 5, 37, (11, 37)),
        ]
        report = validate_composed_path((first, second), rows)
        self.assertEqual(report.status, "validated_on_independent_observations")
        self.assertEqual(report.output_matches, 2)
        self.assertEqual(report.intermediate_matches, 4)

    def test_endpoint_match_does_not_hide_wrong_intermediate(self):
        first = ComposedRelation((F(2), F(0), F(0), F(1)))
        second = ComposedRelation((F(1,2), F(0), F(0), F(1)))
        row = ValidationObservation.create("path", 4, 4, (7, 4))
        report = validate_composed_path((first, second), (row,))
        self.assertEqual(report.output_matches, 1)
        self.assertEqual(report.intermediate_mismatches, 1)
        self.assertEqual(report.status, "refuted_on_independent_observations")

    def test_endpoint_counterexample_refutes_path(self):
        relation = ComposedRelation((F(2), F(1), F(0), F(1)))
        rows = (ValidationObservation.create("good", 2, 5),
                ValidationObservation.create("bad", 3, 99))
        report = validate_composed_path((relation,), rows)
        self.assertEqual(report.status, "refuted_on_independent_observations")
        self.assertEqual(report.output_mismatches, 1)

    def test_domain_failure_is_reported_not_crash(self):
        inverse = ComposedRelation((F(0), F(1), F(1), F(0)), (F(0),))
        row = ValidationObservation.create("zero", 0, 0)
        report = validate_composed_path((inverse,), (row,))
        self.assertEqual(report.output_mismatches, 1)
        self.assertIsNotNone(report.rows[0].error)

    def test_empty_data_is_insufficient(self):
        relation = ComposedRelation((F(1), F(0), F(0), F(1)))
        report = validate_composed_path((relation,), ())
        self.assertEqual(report.status, "insufficient_validation_data")

    def test_duplicate_keys_and_bad_intermediate_shape_rejected(self):
        relation = ComposedRelation((F(1), F(0), F(0), F(1)))
        row = ValidationObservation.create("same", 1, 1)
        with self.assertRaises(ValueError):
            validate_composed_path((relation,), (row, row))
        wrong = ValidationObservation.create("wrong", 1, 1, (1, 1))
        with self.assertRaises(ValueError):
            validate_composed_path((relation,), (wrong,))

    def test_float_expectations_rejected(self):
        with self.assertRaises(ValueError):
            ValidationObservation.create("float", 1.25, 2)

if __name__ == "__main__":
    unittest.main()