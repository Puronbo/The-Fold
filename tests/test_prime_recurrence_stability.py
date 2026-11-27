import unittest
from fractions import Fraction
from tools.prime_recurrence_stability import prime_recurrence_stability


class PrimeRecurrenceStabilityTests(unittest.TestCase):
    def test_persistent_geometry(self):
        result = prime_recurrence_stability(
            [3, 5, 7, 11], 0.0, [2, 3], required_consecutive=2,
            decay=Fraction(1, 2), angle_tolerance=0.0,
            radial_relative_tolerance=1.0, gap_relative_tolerance=0.0)
        self.assertEqual(result["stable_returns"]["geometry"][0],
                         {"anchor_index": 1, "first_arrival_index": 2,
                          "stable_arrival_index": 3, "run_start_index": 2,
                          "consecutive_matches": 2, "anchor_prime": 3,
                          "stable_arrival_prime": 7})
        self.assertEqual(len(result["stable_returns"]["geometry"]), 2)
        self.assertEqual(len(result["memory_by_index"]), 4)

    def test_required_run_length(self):
        with self.assertRaises(ValueError):
            prime_recurrence_stability([3, 5], 0.0, [2], required_consecutive=1)

    def test_decay_type(self):
        with self.assertRaises(ValueError):
            prime_recurrence_stability([3, 5], 0.0, [2], decay=0.5)


if __name__ == "__main__":
    unittest.main()
