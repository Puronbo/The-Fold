import unittest
from fractions import Fraction

from tools.prime_recurrence_chronology import prime_recurrence_chronology


class PrimeRecurrenceChronologyTests(unittest.TestCase):
    def test_first_returns_and_simultaneous_arrivals(self):
        result = prime_recurrence_chronology(
            [3, 5, 7, 11], 0.0, [2, 3], decay=Fraction(1, 2),
            angle_tolerance=0.0, radial_relative_tolerance=1.0,
            gap_relative_tolerance=0.0,
        )
        self.assertEqual(
            result["first_returns"]["geometry"],
            [
                {"anchor_index": 1, "arrival_index": 2, "latency": 1,
                 "anchor_prime": 3, "arrival_prime": 5},
                {"anchor_index": 2, "arrival_index": 3, "latency": 1,
                 "anchor_prime": 5, "arrival_prime": 7},
                {"anchor_index": 3, "arrival_index": 4, "latency": 1,
                 "anchor_prime": 7, "arrival_prime": 11},
            ],
        )
        self.assertEqual(len(result["memory_by_index"]), 4)
        self.assertEqual(result["final_memory"]["geometry"],
                         {"numerator": 7, "denominator": 4})

    def test_decay_must_be_fraction(self):
        with self.assertRaises(ValueError):
            prime_recurrence_chronology([3, 5], 0.0, [2], decay=0.5)


if __name__ == "__main__":
    unittest.main()
