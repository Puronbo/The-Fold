import unittest

from tools.prime_spectral_profile import (
    compare_prime_profiles,
    prime_spectral_profile,
)


class PrimeSpectralProfileTests(unittest.TestCase):
    def test_same_rank_can_have_different_frobenius_orbit_profiles(self):
        matrices = {
            "identity": [[1, 0], [0, 1]],
            "quarter_turn": [[0, -1], [1, 0]],
        }
        result = compare_prime_profiles(matrices, [3, 5, 7])
        for comparison in result["comparisons"]:
            entries = comparison["matrices"]
            self.assertEqual(entries["identity"]["rank"], 2)
            self.assertEqual(entries["quarter_turn"]["rank"], 2)
            self.assertTrue(entries["quarter_turn"]["same_rank_as_reference"])
        # x^2+1 is irreducible over F_3 and F_7, but splits over F_5.
        by_prime = {item["prime"]: item for item in result["profiles"]["quarter_turn"]["profiles"]}
        self.assertEqual(by_prime[3]["frobenius_orbit_degree_histogram"], {"2": 2})
        self.assertEqual(by_prime[7]["frobenius_orbit_degree_histogram"], {"2": 2})
        self.assertEqual(by_prime[5]["frobenius_orbit_degree_histogram"], {"1": 2})
        comparisons = {item["prime"]: item for item in result["comparisons"]}
        at_three = comparisons[3]["matrices"]["quarter_turn"]
        at_five = comparisons[5]["matrices"]["quarter_turn"]
        self.assertFalse(at_three["same_orbit_degree_histogram_as_reference"])
        self.assertFalse(at_three["same_full_frobenius_profile_as_reference"])
        self.assertTrue(at_five["same_orbit_degree_histogram_as_reference"])
        self.assertFalse(at_five["same_full_frobenius_profile_as_reference"])

    def test_profile_accounts_for_full_dimension_with_multiplicity(self):
        result = prime_spectral_profile([[2, 0], [0, 2]], [3])
        profile = result["profiles"][0]
        self.assertEqual(profile["represented_eigenvalue_count_with_multiplicity"], 2)
        self.assertEqual(profile["frobenius_orbit_degree_histogram"], {"1": 2})

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            prime_spectral_profile([[1]], [])
        with self.assertRaises(ValueError):
            compare_prime_profiles({}, [3])
        with self.assertRaises(ValueError):
            compare_prime_profiles({"a": [[1]], "b": [[1, 0], [0, 1]]}, [3])


if __name__ == "__main__":
    unittest.main()
