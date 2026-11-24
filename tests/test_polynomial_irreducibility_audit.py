import math
import unittest
from fractions import Fraction

from tools.polynomial_irreducibility_audit import (
    audit_irreducibility_agreement,
    audit_coprime_bad_proportion_ratio_bound,
    count_monic_irreducibles,
    irreducible_density_convergence,
    irreducible_density_factorization,
    irreducible_density_composition,
    coprime_defect_exponent_spectrum,
    evaluate_coprime_defect_spectrum,
    count_monic_irreducibles_over_field,
    irreducible_density_over_field,
    coprime_composition_excess_spectrum,
    irreducible_density_convergence_over_field,
    coprime_composition_excess_asymptotic,
    coprime_composition_excess_sign_certificate,
)


class PolynomialIrreducibilityAuditTests(unittest.TestCase):
    def test_exact_irreducible_count_formula(self):
        self.assertEqual(count_monic_irreducibles(2, 1), 2)
        self.assertEqual(count_monic_irreducibles(2, 5), 6)
        self.assertEqual(count_monic_irreducibles(3, 4), 18)
        self.assertEqual(count_monic_irreducibles(2, 6), 9)
        for p in (2, 3, 5, 7):
            for degree in range(1, 9):
                count = count_monic_irreducibles(p, degree)
                self.assertGreaterEqual(count, 0)
                self.assertLessEqual(count, p ** degree)

    def test_normalized_density_error_and_exact_uniform_bound(self):
        prime_case = irreducible_density_convergence(3, 5)
        self.assertEqual(prime_case["normalized_irreducible_density"], 1 - 3 ** -4)
        self.assertEqual(prime_case["signed_error_numerator"], 1)
        self.assertEqual(prime_case["signed_error_denominator"], 81)

        composite_case = irreducible_density_convergence(2, 6)
        self.assertAlmostEqual(composite_case["normalized_irreducible_density"],
                               1 - 2 ** -3 - 2 ** -4 + 2 ** -5)
        self.assertTrue(composite_case["uniform_bound_holds"])
        self.assertEqual(composite_case["distinct_prime_divisor_count"], 2)

        for p in (2, 3, 5, 7, 11):
            for degree in range(1, 41):
                with self.subTest(p=p, degree=degree):
                    result = irreducible_density_convergence(p, degree)
                    self.assertTrue(result["uniform_bound_holds"])
                    self.assertLessEqual(
                        result["absolute_error"],
                        result["uniform_prime_field_bound"] + 1e-15,
                    )
                    self.assertGreaterEqual(
                        result["divisor_count_bound"] + 1e-15,
                        result["absolute_error"],
                    )

    def test_factorization_identifies_exact_leading_correction(self):
        # Prime powers have one nontrivial squarefree divisor: the leading
        # correction is the complete correction, regardless of exponent.
        for degree, q in ((2, 2), (8, 2), (9, 3), (25, 5)):
            result = irreducible_density_factorization(3, degree)
            exponent = degree * (q - 1) // q
            self.assertEqual(result["distinct_prime_factors"], [q])
            self.assertTrue(result["leading_term_is_exact"])
            self.assertEqual(result["leading_correction_exponent"], exponent)
            self.assertEqual(result["remainder_numerator"], 0)
            self.assertTrue(result["remainder_bound_holds"])

        # For 6, the q1=2 term leads and the remaining terms are bounded
        # using q2=3.
        result = irreducible_density_factorization(2, 6)
        self.assertEqual(result["distinct_prime_factors"], [2, 3])
        self.assertEqual(result["leading_correction_exponent"], 3)
        self.assertEqual(result["leading_correction_numerator"], -1)
        self.assertEqual(result["leading_correction_denominator"], 8)
        self.assertTrue(result["remainder_bound_holds"])

    def test_factorization_remainder_bound_grid(self):
        for p in (2, 3, 5, 7):
            for degree in range(1, 81):
                with self.subTest(p=p, degree=degree):
                    result = irreducible_density_factorization(p, degree)
                    self.assertTrue(result["remainder_bound_holds"])
                    if result["distinct_prime_factor_count"] <= 1:
                        self.assertTrue(result["leading_term_is_exact"])

    def test_coprime_degree_composition_defect_is_exact(self):
        # A concrete counterexample: normalized density is not multiplicative.
        result = irreducible_density_composition(2, 2, 3)
        self.assertEqual(result["combined_degree"], 6)
        self.assertFalse(result["multiplicative"])
        self.assertEqual(result["composition_defect_numerator"], 15)
        self.assertEqual(result["composition_defect_denominator"], 32)

        # Degree one is the identity: R_p(1)=1.
        identity = irreducible_density_composition(3, 1, 5)
        self.assertTrue(identity["multiplicative"])
        self.assertEqual(identity["composition_defect_numerator"], 0)

        # Sweep small coprime pairs and independently reconstruct the
        # exact defect from the returned rational components.
        from fractions import Fraction
        for p in (2, 3, 5, 7):
            for left in range(1, 13):
                for right in range(1, 13):
                    import math
                    if math.gcd(left, right) != 1:
                        continue
                    with self.subTest(p=p, left=left, right=right):
                        item = irreducible_density_composition(p, left, right)
                        a = Fraction(item["left_density_numerator"],
                                     item["left_density_denominator"])
                        b = Fraction(item["right_density_numerator"],
                                     item["right_density_denominator"])
                        c = Fraction(item["combined_density_numerator"],
                                     item["combined_density_denominator"])
                        defect = Fraction(
                            item["composition_defect_numerator"],
                            item["composition_defect_denominator"])
                        self.assertEqual(defect, c - a * b)
                        self.assertEqual(item["multiplicative"], defect == 0)

    def test_composition_requires_coprime_positive_degrees(self):
        for p, left, right in ((4, 2, 3), (True, 2, 3),
                               (3, 0, 1), (3, 2, 4),
                               (3, 2.0, 3)):
            with self.subTest(p=p, left=left, right=right):
                with self.assertRaises(ValueError):
                    irreducible_density_composition(p, left, right)

    def test_factorization_report_validation(self):
        for p, degree in ((4, 2), (True, 2), (3, 0), (3, 1.5)):
            with self.subTest(p=p, degree=degree):
                with self.assertRaises(ValueError):
                    irreducible_density_factorization(p, degree)

    def test_convergence_report_validation(self):
        for p, degree in ((4, 2), (True, 3), (3, 0), (3, 2.5)):
            with self.subTest(p=p, degree=degree):
                with self.assertRaises(ValueError):
                    irreducible_density_convergence(p, degree)

    def test_count_formula_validation(self):
        for p, degree in ((4, 2), (True, 2), (3, 0), (3, 2.0)):
            with self.subTest(p=p, degree=degree):
                with self.assertRaises(ValueError):
                    count_monic_irreducibles(p, degree)

    def test_exhaustive_domain_matches_exact_theory(self):
        result = audit_irreducibility_agreement(2, 5, max_cases=32)
        self.assertEqual(result["domain_size"], 32)
        self.assertEqual(result["checked_count"], 32)
        self.assertEqual(result["mode"], "exhaustive")
        self.assertTrue(result["complete"])
        self.assertTrue(result["agreement"])
        self.assertEqual(result["mismatch_count"], 0)
        self.assertEqual(result["predicate_irreducible_count_in_checked_set"], 6)
        self.assertEqual(result["theoretical_irreducible_count"], 6)
        self.assertEqual(result["observed_irreducible_density_in_checked_set"], 6 / 32)
        self.assertEqual(result["theoretical_count_match"], True)
        self.assertEqual(result["theoretical_normalized_irreducible_density"], 30 / 32)

    def test_sampled_mode_is_reproducible_and_theory_is_not_sample_count(self):
        args = dict(p=3, degree=8, max_cases=100,
                    sample_count=75, seed=20261124)
        first = audit_irreducibility_agreement(**args)
        second = audit_irreducibility_agreement(**args)
        self.assertEqual(first, second)
        self.assertEqual(first["domain_size"], 3 ** 8)
        self.assertEqual(first["checked_count"], 75)
        self.assertEqual(first["mode"], "deterministic_sample")
        self.assertFalse(first["complete"])
        self.assertTrue(first["agreement"])
        self.assertIsNone(first["theoretical_count_match"])
        self.assertEqual(first["theoretical_irreducible_count"],
                         count_monic_irreducibles(3, 8))
        self.assertAlmostEqual(
            first["expected_irreducibles_in_checked_set"],
            75 * first["theoretical_irreducible_density"],
        )

    def test_sample_larger_than_domain_checks_each_member_once(self):
        result = audit_irreducibility_agreement(
            2, 3, max_cases=1, sample_count=100, seed=7
        )
        self.assertEqual(result["checked_count"], 8)
        self.assertEqual(result["mode"], "deterministic_sample")
        self.assertTrue(result["complete"])
        self.assertTrue(result["theoretical_count_match"])

    def test_validation(self):
        invalid = (
            {"p": 4, "degree": 2},
            {"p": 3, "degree": 0},
            {"p": 3, "degree": 2, "max_cases": 0},
            {"p": 3, "degree": 2, "sample_count": 0},
            {"p": True, "degree": 2},
            {"p": 3, "degree": 2.0},
        )
        for kwargs in invalid:
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    audit_irreducibility_agreement(**kwargs)


    def test_coprime_density_defect_sign_audit_is_exact_and_bounded(self):
        from tools.polynomial_irreducibility_audit import audit_coprime_density_defect_sign
        result = audit_coprime_density_defect_sign([2, 3, 5], 12)
        self.assertEqual(result["coprime_pair_count"], 102)
        self.assertEqual(result["positive_count"], 102)
        self.assertEqual(result["negative_count"], 0)
        self.assertEqual(result["zero_count"], 0)
        self.assertTrue(result["all_checked_defects_positive"])
        self.assertIsNone(result["first_nonpositive_defect"])
        self.assertIn("finite-grid evidence only", result["interpretation"])
        for primes, degree in (([], 4), ([4], 4), ([2, 2], 4), ([2], 2)):
            with self.subTest(primes=primes, degree=degree):
                with self.assertRaises(ValueError):
                    audit_coprime_density_defect_sign(primes, degree)


    def test_coprime_bad_proportion_order_audit(self):
        from tools.polynomial_irreducibility_audit import audit_coprime_bad_proportion_order
        result = audit_coprime_bad_proportion_order([2, 3, 5], 12)
        self.assertEqual(result["coprime_pair_count"], 102)
        self.assertEqual(result["strict_order_count"], 102)
        self.assertTrue(result["all_checked_pairs_strict"])
        self.assertIsNone(result["first_failure"])
        self.assertIsNotNone(result["largest_product_to_smaller_factor_bad_ratio"])
        for primes, degree in (([], 4), ([4], 4), ([2, 2], 4), ([2], 2)):
            with self.subTest(primes=primes, degree=degree):
                with self.assertRaises(ValueError):
                    audit_coprime_bad_proportion_order(primes, degree)



    def test_coprime_bad_proportion_ratio_bound_audit(self):
        result = audit_coprime_bad_proportion_ratio_bound([2, 3, 5], 12)
        self.assertEqual(result["coprime_pair_count"], 102)
        self.assertEqual(result["within_bound_count"], 102)
        self.assertTrue(result["all_checked_pairs_within_bound"])
        self.assertIsNone(result["first_failure"])
        largest = result["largest_observed_ratio"]
        self.assertEqual((largest["left_degree"], largest["right_degree"]), (2, 3))
        self.assertTrue(largest["attains_proposed_bound"])
        self.assertEqual(
            (largest["ratio_numerator"], largest["ratio_denominator"]),
            (5, 8),
        )
        for primes, degree in (([], 4), ([4], 4), ([2, 2], 4), ([2], 2)):
            with self.subTest(primes=primes, degree=degree):
                with self.assertRaises(ValueError):
                    audit_coprime_bad_proportion_ratio_bound(primes, degree)



class CoprimeDefectSpectrumTests(unittest.TestCase):
    def test_resonant_3_4_spectrum_and_evaluation(self):
        result = coprime_defect_exponent_spectrum(3, 4)
        self.assertEqual(
            result["spectrum"],
            [
                {"exponent": 2, "coefficient": 2},
                {"exponent": 4, "coefficient": -1},
                {"exponent": 6, "coefficient": -1},
                {"exponent": 8, "coefficient": -1},
                {"exponent": 10, "coefficient": 1},
            ],
        )
        self.assertEqual(result["leading_coefficient"], 2)
        self.assertEqual(
            evaluate_coprime_defect_spectrum(2, 3, 4),
            Fraction(2, 2**2) - Fraction(1, 2**4)
            - Fraction(1, 2**6) - Fraction(1, 2**8)
            + Fraction(1, 2**10),
        )

    def test_nonresonant_2_3_spectrum(self):
        result = coprime_defect_exponent_spectrum(2, 3)
        self.assertEqual(
            result["spectrum"],
            [
                {"exponent": 1, "coefficient": 1},
                {"exponent": 2, "coefficient": 1},
                {"exponent": 3, "coefficient": -2},
                {"exponent": 4, "coefficient": -1},
                {"exponent": 5, "coefficient": 1},
            ],
        )
        self.assertEqual(result["leading_coefficient"], 1)

    def test_spectrum_matches_density_identity_on_small_grid(self):
        for left in range(2, 13):
            for right in range(2, 13):
                if math.gcd(left, right) != 1:
                    continue
                spectrum = coprime_defect_exponent_spectrum(left, right)
                for field_size in (2, 3, 4, 5, 8, 9):
                    with self.subTest(left=left, right=right,
                                      field_size=field_size):
                        value = evaluate_coprime_defect_spectrum(
                            field_size, left, right
                        )
                        def bad_proportion(degree):
                            count = count_monic_irreducibles_over_field(
                                field_size, degree
                            )
                            normalized = Fraction(
                                degree * count, field_size ** degree
                            )
                            return 1 - normalized

                        expected = (
                            bad_proportion(left)
                            + bad_proportion(right)
                            - bad_proportion(left) * bad_proportion(right)
                            - bad_proportion(left * right)
                        )
                        self.assertTrue(spectrum["term_count"] > 0)
                        self.assertEqual(value, expected)
                        self.assertGreater(value, 0)

    def test_spectrum_rejects_invalid_degrees_and_field_sizes(self):
        for left, right in ((1, 3), (2, 2), (2, 0), (True, 3)):
            with self.subTest(left=left, right=right):
                with self.assertRaises(ValueError):
                    coprime_defect_exponent_spectrum(left, right)
        for field_size in (0, 1, True, 2.5):
            with self.subTest(field_size=field_size):
                with self.assertRaises(ValueError):
                    evaluate_coprime_defect_spectrum(field_size, 2, 3)



class PrimePowerFieldTests(unittest.TestCase):
    def test_irreducible_counts_over_prime_power_fields(self):
        self.assertEqual(count_monic_irreducibles_over_field(4, 2), 6)
        self.assertEqual(count_monic_irreducibles_over_field(8, 3), 168)
        self.assertEqual(count_monic_irreducibles_over_field(9, 2), 36)
        self.assertEqual(count_monic_irreducibles_over_field(2, 5), 6)

    def test_exact_density_over_prime_power_fields(self):
        result = irreducible_density_over_field(4, 2)
        self.assertEqual(result["irreducible_count"], 6)
        self.assertEqual(
            (result["normalized_density_numerator"],
             result["normalized_density_denominator"]),
            (3, 4),
        )
        self.assertEqual(
            (result["bad_proportion_numerator"],
             result["bad_proportion_denominator"]),
            (1, 4),
        )

    def test_rejects_non_prime_powers(self):
        for value in (0, 1, 6, 10, 12, True, 2.5):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    count_monic_irreducibles_over_field(value, 2)




class CoprimeCompositionExcessTests(unittest.TestCase):
    def test_two_three_composition_resonance(self):
        result = coprime_composition_excess_spectrum([2, 3])
        self.assertEqual(
            result["spectrum"],
            [
                {"exponent": 4, "coefficient": 1},
                {"exponent": 5, "coefficient": -1},
            ],
        )
        self.assertEqual(result["sign_for_sufficiently_large_field"],
                         "positive")

    def test_three_four_composition_excess_is_negative(self):
        result = coprime_composition_excess_spectrum([3, 4])
        self.assertEqual(
            result["spectrum"],
            [
                {"exponent": 4, "coefficient": -1},
                {"exponent": 6, "coefficient": 1},
                {"exponent": 8, "coefficient": 1},
                {"exponent": 10, "coefficient": -1},
            ],
        )
        self.assertEqual(result["sign_for_sufficiently_large_field"],
                         "negative")

    def test_pairwise_coprime_multi_factor_spectrum(self):
        result = coprime_composition_excess_spectrum([2, 3, 5])
        self.assertEqual(result["composite_degree"], 30)
        self.assertGreater(result["term_count"], 0)

    def test_rejects_invalid_composition_degrees(self):
        for degrees in ([], [2], [2, 2], [2, 3, 6], [1, 3], [True, 3]):
            with self.subTest(degrees=degrees):
                with self.assertRaises(ValueError):
                    coprime_composition_excess_spectrum(degrees)




class PrimePowerConvergenceTests(unittest.TestCase):
    def test_prime_power_uniform_density_bound(self):
        for field_size in (4, 8, 9, 16, 25):
            for degree in range(1, 25):
                with self.subTest(field_size=field_size, degree=degree):
                    result = irreducible_density_convergence_over_field(
                        field_size, degree
                    )
                    self.assertTrue(result["uniform_bound_holds"])
                    self.assertGreaterEqual(
                        result["absolute_error"], 0.0
                    )

    def test_prime_power_convergence_rejects_invalid_fields(self):
        for field_size in (0, 1, 6, 10, True, 2.5):
            with self.subTest(field_size=field_size):
                with self.assertRaises(ValueError):
                    irreducible_density_convergence_over_field(
                        field_size, 4
                    )


    def test_coprime_composition_leading_resonance_classification(self):
        for b in (3, 5, 7, 11, 13):
            with self.subTest(b=b):
                result = coprime_composition_excess_asymptotic([2, b])
                self.assertEqual(result["leading_regime"], "leading_resonance")
                self.assertTrue(result["two_factor_resonance_iff_two_and_odd_prime"])
                self.assertEqual(
                    result["exact_spectrum"]["spectrum"],
                    [
                        {"exponent": 2 * b - 2, "coefficient": 1},
                        {"exponent": 2 * b - 1, "coefficient": -1},
                    ],
                )

        for b in (9, 15, 21, 25):
            with self.subTest(b=b):
                result = coprime_composition_excess_asymptotic([2, b])
                self.assertEqual(result["leading_regime"],
                                 "negative_without_leading_cancellation")
                self.assertFalse(result["two_factor_resonance_iff_two_and_odd_prime"])

        for pair in ((3, 4), (3, 8), (4, 5), (5, 6), (7, 9)):
            with self.subTest(pair=pair):
                result = coprime_composition_excess_asymptotic(list(pair))
                self.assertEqual(result["leading_regime"],
                                 "negative_without_leading_cancellation")

    def test_multi_factor_composition_excess_is_eventually_negative(self):
        for degrees in ([2, 3, 5], [2, 3, 7], [3, 4, 5],
                        [2, 5, 9], [3, 5, 7, 11]):
            with self.subTest(degrees=degrees):
                result = coprime_composition_excess_asymptotic(degrees)
                self.assertEqual(result["leading_regime"],
                                 "negative_without_leading_cancellation")
                self.assertGreater(result["product_first_exponent"],
                                   result["sum_of_input_first_exponents"])
                self.assertIsNone(result["exact_spectrum"])

    def test_composition_asymptotic_validation(self):
        for degrees in ([], [2], [2, 2], [2, 3, 6], [2, True], [2, 3.0]):
            with self.subTest(degrees=degrees):
                with self.assertRaises(ValueError):
                    coprime_composition_excess_asymptotic(degrees)



class CompositionExcessSignCertificateTests(unittest.TestCase):
    def test_exact_finite_field_sign_and_threshold(self):
        positive = coprime_composition_excess_sign_certificate([2, 3], 2)
        self.assertEqual(positive["exact_sign"], "positive")
        self.assertEqual(
            (positive["exact_value_numerator"],
             positive["exact_value_denominator"]),
            (1, 32),
        )
        self.assertEqual(positive["sufficient_field_size_threshold"], 2)
        self.assertEqual(positive["eventual_sign"], "positive")

        negative = coprime_composition_excess_sign_certificate([3, 4], 2)
        self.assertEqual(negative["exact_sign"], "negative")
        self.assertEqual(negative["sufficient_field_size_threshold"], 4)
        self.assertEqual(negative["eventual_sign"], "negative")

    def test_threshold_guarantee_on_prime_power_grid(self):
        for degrees in ([2, 3], [3, 4], [2, 5, 9], [3, 5, 7]):
            probe = coprime_composition_excess_sign_certificate(degrees, 2)
            threshold = probe["sufficient_field_size_threshold"]
            expected = probe["eventual_sign"]
            for field_size in range(threshold, threshold + 12):
                # Restrict to prime powers by testing the shared validator
                # through the public API; composites with multiple primes
                # are intentionally skipped.
                from tools.polynomial_irreducibility_audit import _is_prime_power
                if not _is_prime_power(field_size):
                    continue
                result = coprime_composition_excess_sign_certificate(
                    degrees, field_size
                )
                self.assertEqual(result["exact_sign"], expected)

    def test_sign_certificate_rejects_invalid_field_sizes(self):
        for field_size in (0, 1, 6, 10, True, 2.5):
            with self.subTest(field_size=field_size):
                with self.assertRaises(ValueError):
                    coprime_composition_excess_sign_certificate(
                        [2, 3], field_size
                    )

if __name__ == "__main__":
    unittest.main()
