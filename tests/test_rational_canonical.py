import unittest

from tools.rational_canonical import rational_canonical_profile


class RationalCanonicalTests(unittest.TestCase):
    def test_identity_has_repeated_linear_invariant_factors(self):
        result = rational_canonical_profile([[1, 0], [0, 1]], 5)
        self.assertEqual(result["invariant_factors_coefficients_descending"],
                         [[1, 4], [1, 4]])
        self.assertTrue(result["similarity_class_complete_over_base_field"])

    def test_companion_of_x_squared_plus_one_is_cyclic(self):
        result = rational_canonical_profile([[0, -1], [1, 0]], 3)
        self.assertEqual(result["invariant_factors_coefficients_descending"],
                         [[1, 0, 1]])
        self.assertEqual(
            result["irreducible_primary_components"][0]
                ["elementary_divisor_exponents_descending"], [1]
        )

    def test_nilpotent_jordan_blocks_recovered(self):
        # J_3(0) direct sum J_1(0): elementary divisors x^3 and x.
        matrix = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        result = rational_canonical_profile(matrix, 2)
        primary = result["irreducible_primary_components"][0]
        self.assertEqual(primary["elementary_divisor_exponents_descending"],
                         [3, 1])
        self.assertEqual(result["invariant_factors_coefficients_descending"],
                         [[1, 0], [1, 0, 0, 0]])

    def test_similar_matrices_have_same_invariant_factors(self):
        a = [[1, 1], [0, 2]]
        # P=[[1,1],[1,0]], P^-1 exists over F_5.
        p = 5
        pinv = [[0, 1], [1, 4]]
        basis = [[1, 1], [1, 0]]
        def mm(x, y):
            return [[sum(x[i][k] * y[k][j] for k in range(2)) % p
                     for j in range(2)] for i in range(2)]
        conjugate = mm(mm(pinv, a), basis) # P^-1 A P
        left = rational_canonical_profile(a, p)
        right = rational_canonical_profile(conjugate, p)
        self.assertEqual(left["invariant_factors_coefficients_descending"],
                         right["invariant_factors_coefficients_descending"])

    def test_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            rational_canonical_profile([[1, 2]], 5)
        with self.assertRaises(ValueError):
            rational_canonical_profile([[1]], 4)


    def test_g_ep153_exhaustive_three_by_three_similarity_orbits_over_f2(self):
        from itertools import product

        p = 2
        matrices = list(product(range(p), repeat=9))

        def as_matrix(flat):
            return [list(flat[i * 3:(i + 1) * 3]) for i in range(3)]

        def multiply(a, b):
            return [[sum(a[i][k] * b[k][j] for k in range(3)) % p
                     for j in range(3)] for i in range(3)]

        def determinant(a):
            return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                    - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                    + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])) % p

        def characteristic_polynomial_local(a):
            trace = sum(a[i][i] for i in range(3)) % p
            principal = sum(
                (a[i][i] * a[j][j] - a[i][j] * a[j][i])
                for i, j in ((0, 1), (0, 2), (1, 2))
            ) % p
            return [1, (-trace) % p, principal, (-determinant(a)) % p]

        def polynomial_multiply(a, b):
            out = [0] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    out[i + j] = (out[i + j] + x * y) % p
            return out

        def inverse(a):
            augmented = [a[i][:] + [int(i == j) for j in range(3)]
                         for i in range(3)]
            for col in range(3):
                pivot = next((r for r in range(col, 3)
                              if augmented[r][col] % p), None)
                if pivot is None:
                    return None
                augmented[col], augmented[pivot] = (
                    augmented[pivot], augmented[col]
                )
                for row in range(3):
                    if row != col and augmented[row][col] % p:
                        factor = augmented[row][col] % p
                        augmented[row] = [
                            (x - factor * y) % p
                            for x, y in zip(augmented[row], augmented[col])
                        ]
            return [row[3:] for row in augmented]

        def flatten(a):
            return tuple(x % p for row in a for x in row)

        gl = []
        inverses = {}
        for flat in matrices:
            candidate = as_matrix(flat)
            inv = inverse(candidate)
            if inv is not None:
                key = flatten(candidate)
                gl.append(candidate)
                inverses[key] = inv
        self.assertEqual(len(gl), 168)

        profiles = {}
        cyclic_count = 0
        for flat in matrices:
            a = as_matrix(flat)
            result = rational_canonical_profile(a, p)
            char_poly = characteristic_polynomial_local(a)
            self.assertEqual(
                result["characteristic_polynomial_coefficients_descending"],
                char_poly,
            )
            product_poly = [1]
            for invariant in result["invariant_factors_coefficients_descending"]:
                product_poly = polynomial_multiply(product_poly, invariant)
            self.assertEqual(product_poly, char_poly)

            a2 = multiply(a, a)
            cyclic = False
            for vector in product(range(p), repeat=3):
                av = [sum(a[i][j] * vector[j] for j in range(3)) % p
                      for i in range(3)]
                a2v = [sum(a[i][j] * av[j] for j in range(3)) % p
                       for i in range(3)]
                krylov = [[vector[i], av[i], a2v[i]] for i in range(3)]
                if determinant(krylov):
                    cyclic = True
                    break
            self.assertEqual(cyclic, result["invariant_factor_count"] == 1)
            cyclic_count += int(cyclic)
            profile_key = tuple(
                tuple(poly)
                for poly in result["invariant_factors_coefficients_descending"]
            )
            profiles.setdefault(profile_key, []).append(flat)

        self.assertGreater(cyclic_count, 0)
        self.assertLess(cyclic_count, len(matrices))
        self.assertGreater(len(profiles), 1)

        for profile_key, fibre in profiles.items():
            representative = as_matrix(fibre[0])
            orbit = set()
            for basis in gl:
                basis_inverse = inverses[flatten(basis)]
                conjugate = multiply(multiply(basis_inverse, representative), basis)
                orbit.add(flatten(conjugate))
            self.assertEqual(orbit, set(fibre), msg=f"profile={profile_key}")


    def test_g_ep154_exhaustive_three_by_three_similarity_orbits_over_f3(self):
        from itertools import product

        p = 3
        flats = list(product(range(p), repeat=9))

        def as_matrix(flat):
            return [list(flat[i * 3:(i + 1) * 3]) for i in range(3)]

        def multiply(a, b):
            return [[sum(a[i][k] * b[k][j] for k in range(3)) % p
                     for j in range(3)] for i in range(3)]

        def determinant(a):
            return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                    - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                    + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])) % p

        def characteristic_polynomial_local(a):
            trace = sum(a[i][i] for i in range(3)) % p
            principal = sum(
                a[i][i] * a[j][j] - a[i][j] * a[j][i]
                for i, j in ((0, 1), (0, 2), (1, 2))
            ) % p
            return [1, (-trace) % p, principal, (-determinant(a)) % p]

        def polynomial_multiply(a, b):
            out = [0] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    out[i + j] = (out[i + j] + x * y) % p
            return out

        def inverse(a):
            augmented = [a[i][:] + [int(i == j) for j in range(3)]
                         for i in range(3)]
            for col in range(3):
                pivot = next((r for r in range(col, 3)
                              if augmented[r][col] % p), None)
                if pivot is None:
                    return None
                augmented[col], augmented[pivot] = (
                    augmented[pivot], augmented[col]
                )
                pivot_value = augmented[col][col] % p
                augmented[col] = [(x * pow(pivot_value, -1, p)) % p
                                  for x in augmented[col]]
                for row in range(3):
                    if row != col:
                        factor = augmented[row][col] % p
                        augmented[row] = [
                            (x - factor * y) % p
                            for x, y in zip(augmented[row], augmented[col])
                        ]
            return [row[3:] for row in augmented]

        def flatten(a):
            return tuple(x % p for row in a for x in row)

        gl = []
        inverses = {}
        for flat in flats:
            candidate = as_matrix(flat)
            inv = inverse(candidate)
            if inv is not None:
                key = flatten(candidate)
                gl.append(candidate)
                inverses[key] = inv
        self.assertEqual(len(gl), 11232)

        profiles = {}
        cyclic_count = 0
        for flat in flats:
            a = as_matrix(flat)
            result = rational_canonical_profile(a, p)
            char_poly = characteristic_polynomial_local(a)
            self.assertEqual(
                result["characteristic_polynomial_coefficients_descending"],
                char_poly,
            )
            product_poly = [1]
            for invariant in result["invariant_factors_coefficients_descending"]:
                product_poly = polynomial_multiply(product_poly, invariant)
            self.assertEqual(product_poly, char_poly)

            a2 = multiply(a, a)
            cyclic = False
            for vector in product(range(p), repeat=3):
                av = [sum(a[i][j] * vector[j] for j in range(3)) % p
                      for i in range(3)]
                a2v = [sum(a[i][j] * av[j] for j in range(3)) % p
                       for i in range(3)]
                krylov = [[vector[i], av[i], a2v[i]] for i in range(3)]
                if determinant(krylov):
                    cyclic = True
                    break
            self.assertEqual(cyclic, result["invariant_factor_count"] == 1)
            cyclic_count += int(cyclic)
            profile_key = tuple(
                tuple(poly)
                for poly in result["invariant_factors_coefficients_descending"]
            )
            profiles.setdefault(profile_key, []).append(flat)

        self.assertGreater(cyclic_count, 0)
        self.assertLess(cyclic_count, len(flats))
        self.assertGreater(len(profiles), 1)

        for profile_key, fibre in profiles.items():
            representative = as_matrix(fibre[0])
            orbit = set()
            for basis in gl:
                basis_inverse = inverses[flatten(basis)]
                conjugate = multiply(multiply(basis_inverse, representative), basis)
                orbit.add(flatten(conjugate))
            self.assertEqual(orbit, set(fibre), msg=f"profile={profile_key}")


    def test_g_ep155_compare_three_by_three_profiles_across_f2_and_f3(self):
        from itertools import product

        profiles_by_field = {}
        shapes_by_field = {}
        for p in (2, 3):
            profiles = set()
            shapes = set()
            for flat in product(range(p), repeat=9):
                matrix = [list(flat[i * 3:(i + 1) * 3]) for i in range(3)]
                result = rational_canonical_profile(matrix, p)
                invariant_factors = result["invariant_factors_coefficients_descending"]
                # Coefficients are canonical residues in the field currently
                # being enumerated; never interpret them as integers in Z.
                profile = tuple(tuple(coefficient % p for coefficient in poly)
                                for poly in invariant_factors)
                profiles.add(profile)
                shapes.add(tuple(len(poly) - 1 for poly in invariant_factors))
            profiles_by_field[p] = profiles
            shapes_by_field[p] = shapes

        # The degree-partition possibilities are shared, although their
        # polynomial representatives and irreducibility behavior depend on p.
        self.assertEqual(shapes_by_field[2], shapes_by_field[3])
        self.assertEqual(shapes_by_field[2], {(3,), (1, 2), (1, 1, 1)})
        self.assertTrue(all(profiles_by_field[p] for p in (2, 3)))

        # F_3 admits normalized coefficient 2, which cannot occur in F_2.
        self.assertTrue(any(
            coefficient == 2
            for profile in profiles_by_field[3]
            for polynomial in profile
            for coefficient in polynomial
        ))
        self.assertFalse(any(
            coefficient == 2
            for profile in profiles_by_field[2]
            for polynomial in profile
            for coefficient in polynomial
        ))


    def test_g_ep156_cubic_irreducible_factor_catalogs_over_f2_and_f3(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        inventories = {}
        patterns = {}
        for p in (2, 3):
            observed = set()
            observed_patterns = set()
            for lower in product(range(p), repeat=3):
                # Every monic cubic is a characteristic polynomial: use its
                # companion matrix, so this exhausts the degree-three cases.
                polynomial = (1,) + tuple(lower)
                factors = factor_polynomial(polynomial, p)
                reconstructed = [1]
                pattern = []
                for factor in factors:
                    if "degree" not in factor:
                        continue
                    coefficients = tuple(
                        value % p for value in factor["coefficients_descending"]
                    )
                    degree = factor["degree"]
                    self.assertEqual(len(coefficients), degree + 1)
                    self.assertEqual(coefficients[0], 1)
                    observed.add((degree, coefficients))
                    pattern.append((degree, factor["multiplicity"]))
                    for _ in range(factor["multiplicity"]):
                        product_poly = [0] * (len(reconstructed) + len(coefficients) - 1)
                        for i, x in enumerate(reconstructed):
                            for j, y in enumerate(coefficients):
                                product_poly[i + j] = (
                                    product_poly[i + j] + x * y
                                ) % p
                        reconstructed = product_poly
                self.assertEqual(reconstructed, list(polynomial))
                observed_patterns.add(tuple(sorted(pattern)))
            inventories[p] = observed
            patterns[p] = observed_patterns

            expected_counts = {
                1: p,
                2: (p * p - p) // 2,
                3: (p ** 3 - p) // 3,
            }
            for degree, expected in expected_counts.items():
                self.assertEqual(
                    sum(1 for d, _ in observed if d == degree), expected,
                    msg=f"F_{p}: degree-{degree} irreducible inventory",
                )

        # F_3, unlike F_2, has enough distinct linear factors for a
        # cubic to split into three distinct linear factors.
        common_patterns = {
            ((1, 1), (2, 1)),
            ((1, 3),),
            ((1, 1), (1, 2)),
            ((3, 1),),
        }
        three_distinct_linears = ((1, 1), (1, 1), (1, 1))
        self.assertEqual(patterns[2], common_patterns)
        self.assertEqual(patterns[3], common_patterns | {three_distinct_linears})
        self.assertNotEqual(inventories[2], inventories[3])


    def test_g_ep157_quartic_factorization_catalogs_over_f2_and_f3(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        inventories = {}
        patterns = {}
        for p in (2, 3):
            observed = set()
            observed_patterns = set()
            for lower in product(range(p), repeat=4):
                polynomial = (1,) + tuple(lower)
                factors = factor_polynomial(polynomial, p)
                reconstructed = [1]
                pattern = []
                for factor in factors:
                    if "degree" not in factor:
                        continue
                    coefficients = tuple(
                        value % p for value in factor["coefficients_descending"]
                    )
                    degree = factor["degree"]
                    multiplicity = factor["multiplicity"]
                    self.assertEqual(len(coefficients), degree + 1)
                    self.assertEqual(coefficients[0], 1)
                    observed.add((degree, coefficients))
                    pattern.append((degree, multiplicity))
                    for _ in range(multiplicity):
                        product_poly = [0] * (
                            len(reconstructed) + len(coefficients) - 1
                        )
                        for i, x in enumerate(reconstructed):
                            for j, y in enumerate(coefficients):
                                product_poly[i + j] = (
                                    product_poly[i + j] + x * y
                                ) % p
                        reconstructed = product_poly
                self.assertEqual(reconstructed, list(polynomial))
                observed_patterns.add(tuple(sorted(pattern)))
            inventories[p] = observed
            patterns[p] = observed_patterns

            # Number of monic irreducibles of degree d over F_p:
            # (1/d) * sum_{e|d} mu(e) * p^(d/e).
            expected_counts = {
                1: p,
                2: (p ** 2 - p) // 2,
                3: (p ** 3 - p) // 3,
                4: (p ** 4 - p ** 2) // 4,
            }
            for degree, expected in expected_counts.items():
                self.assertEqual(
                    sum(1 for d, _ in observed if d == degree), expected,
                    msg=f"F_{p}: degree-{degree} irreducible inventory",
                )

        # F_3 has three distinct monic linear irreducibles; one may repeat
        # to form a quartic with all three distinct linear factors present.
        all_three_with_repeat = ((1, 1), (1, 1), (1, 2))
        self.assertIn(all_three_with_repeat, patterns[3])
        self.assertNotIn(all_three_with_repeat, patterns[2])
        self.assertNotEqual(inventories[2], inventories[3])
        self.assertNotEqual(patterns[2], patterns[3])


    def test_g_ep158_quartic_pattern_catalogs_across_f2_f3_f5(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        patterns = {}
        inventories = {}
        for p in (2, 3, 5):
            observed_patterns = set()
            observed_irreducibles = set()
            for lower in product(range(p), repeat=4):
                polynomial = (1,) + tuple(lower)
                factors = factor_polynomial(polynomial, p)
                reconstructed = [1]
                pattern = []
                for factor in factors:
                    if "degree" not in factor:
                        continue
                    coefficients = tuple(
                        value % p for value in factor["coefficients_descending"]
                    )
                    degree = factor["degree"]
                    multiplicity = factor["multiplicity"]
                    self.assertEqual(len(coefficients), degree + 1)
                    self.assertEqual(coefficients[0], 1)
                    observed_irreducibles.add((degree, coefficients))
                    pattern.append((degree, multiplicity))
                    for _ in range(multiplicity):
                        product_poly = [0] * (
                            len(reconstructed) + len(coefficients) - 1
                        )
                        for i, x in enumerate(reconstructed):
                            for j, y in enumerate(coefficients):
                                product_poly[i + j] = (
                                    product_poly[i + j] + x * y
                                ) % p
                        reconstructed = product_poly
                self.assertEqual(reconstructed, list(polynomial))
                observed_patterns.add(tuple(sorted(pattern)))
            patterns[p] = observed_patterns
            inventories[p] = observed_irreducibles

            expected_counts = {
                1: p,
                2: (p ** 2 - p) // 2,
                3: (p ** 3 - p) // 3,
                4: (p ** 4 - p ** 2) // 4,
            }
            for degree, expected in expected_counts.items():
                self.assertEqual(
                    sum(1 for d, _ in observed_irreducibles if d == degree),
                    expected,
                    msg=f"F_{p}: degree-{degree} irreducible inventory",
                )

        # A larger field permits more pairwise-distinct linear factors.
        three_distinct_with_repeat = ((1, 1), (1, 1), (1, 2))
        four_distinct_linears = ((1, 1), (1, 1), (1, 1), (1, 1))
        self.assertNotIn(three_distinct_with_repeat, patterns[2])
        self.assertIn(three_distinct_with_repeat, patterns[3])
        self.assertIn(three_distinct_with_repeat, patterns[5])
        self.assertNotIn(four_distinct_linears, patterns[2])
        self.assertNotIn(four_distinct_linears, patterns[3])
        self.assertIn(four_distinct_linears, patterns[5])

        # F_2 has only one monic irreducible quadratic, so two distinct
        # irreducible quadratic factors first become possible over F_3.
        two_distinct_quadratics = ((2, 1), (2, 1))
        self.assertNotIn(two_distinct_quadratics, patterns[2])
        self.assertIn(two_distinct_quadratics, patterns[3])
        self.assertIn(two_distinct_quadratics, patterns[5])
        self.assertTrue(patterns[2] < patterns[3])
        self.assertTrue(patterns[3] < patterns[5])
        self.assertNotEqual(inventories[2], inventories[3])
        self.assertNotEqual(inventories[3], inventories[5])


    def test_g_ep159_quartic_factor_catalog_stabilizes_from_f5_to_f7(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        patterns = {}
        inventories = {}
        for p in (2, 3, 5, 7):
            observed_patterns = set()
            observed_irreducibles = set()
            for lower in product(range(p), repeat=4):
                polynomial = (1,) + tuple(lower)
                factors = factor_polynomial(polynomial, p)
                reconstructed = [1]
                pattern = []
                for factor in factors:
                    if "degree" not in factor:
                        continue
                    coefficients = tuple(
                        value % p for value in factor["coefficients_descending"]
                    )
                    degree = factor["degree"]
                    multiplicity = factor["multiplicity"]
                    self.assertEqual(len(coefficients), degree + 1)
                    self.assertEqual(coefficients[0], 1)
                    observed_irreducibles.add((degree, coefficients))
                    pattern.append((degree, multiplicity))
                    for _ in range(multiplicity):
                        product_poly = [0] * (
                            len(reconstructed) + len(coefficients) - 1
                        )
                        for i, x in enumerate(reconstructed):
                            for j, y in enumerate(coefficients):
                                product_poly[i + j] = (
                                    product_poly[i + j] + x * y
                                ) % p
                        reconstructed = product_poly
                self.assertEqual(reconstructed, list(polynomial))
                observed_patterns.add(tuple(sorted(pattern)))
            patterns[p] = observed_patterns
            inventories[p] = observed_irreducibles

            expected_counts = {
                1: p,
                2: (p ** 2 - p) // 2,
                3: (p ** 3 - p) // 3,
                4: (p ** 4 - p ** 2) // 4,
            }
            for degree, expected in expected_counts.items():
                self.assertEqual(
                    sum(1 for d, _ in observed_irreducibles if d == degree),
                    expected,
                    msg=f"F_{p}: degree-{degree} irreducible inventory",
                )

        # The full quartic degree/multiplicity catalog has stabilized by
        # F_5: at least four distinct linear factors and two distinct
        # irreducible quadratics are available.
        self.assertEqual(patterns[5], patterns[7])
        self.assertEqual(patterns[5], {
            ((1, 4),),
            ((1, 2), (1, 2)),
            ((1, 1), (1, 3)),
            ((1, 1), (1, 1), (1, 2)),
            ((1, 1), (1, 1), (1, 1), (1, 1)),
            ((1, 1), (1, 1), (2, 1)),
            ((1, 2), (2, 1)),
            ((2, 2),),
            ((2, 1), (2, 1)),
            ((4, 1),),
            ((1, 1), (3, 1)),
        })
        self.assertLess(patterns[2], patterns[3])
        self.assertLess(patterns[3], patterns[5])
        self.assertNotEqual(inventories[5], inventories[7])


    def test_g_ep160_quintic_factor_patterns_stabilize_at_f5(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        patterns = {}
        inventories = {}
        for p in (2, 3, 5, 7):
            observed_patterns = set()
            observed_irreducibles = set()
            for lower in product(range(p), repeat=5):
                polynomial = (1,) + tuple(lower)
                factors = factor_polynomial(polynomial, p)
                reconstructed = [1]
                pattern = []
                for factor in factors:
                    if "degree" not in factor:
                        continue
                    coefficients = tuple(
                        value % p for value in factor["coefficients_descending"]
                    )
                    degree = factor["degree"]
                    multiplicity = factor["multiplicity"]
                    self.assertEqual(len(coefficients), degree + 1)
                    self.assertEqual(coefficients[0], 1)
                    observed_irreducibles.add((degree, coefficients))
                    pattern.append((degree, multiplicity))
                    for _ in range(multiplicity):
                        product_poly = [0] * (
                            len(reconstructed) + len(coefficients) - 1
                        )
                        for i, x in enumerate(reconstructed):
                            for j, y in enumerate(coefficients):
                                product_poly[i + j] = (
                                    product_poly[i + j] + x * y
                                ) % p
                        reconstructed = product_poly
                self.assertEqual(reconstructed, list(polynomial))
                observed_patterns.add(tuple(sorted(pattern)))
            patterns[p] = observed_patterns
            inventories[p] = observed_irreducibles

            expected_counts = {
                1: p,
                2: (p ** 2 - p) // 2,
                3: (p ** 3 - p) // 3,
                4: (p ** 4 - p ** 2) // 4,
                5: (p ** 5 - p) // 5,
            }
            for degree, expected in expected_counts.items():
                self.assertEqual(
                    sum(1 for d, _ in observed_irreducibles if d == degree),
                    expected,
                    msg=f"F_{p}: degree-{degree} irreducible inventory",
                )

        # Degree-five factor shapes stabilize once there are enough distinct
        # irreducibles to realize every degree partition. F_5 has five
        # linears and at least two quadratics; F_7 adds no new shape.
        self.assertEqual(patterns[5], patterns[7])
        self.assertLess(patterns[2], patterns[3])
        self.assertLess(patterns[3], patterns[5])
        self.assertNotEqual(inventories[5], inventories[7])
        self.assertIn(((1, 1), (1, 1), (1, 1), (1, 1), (1, 1)), patterns[5])
        self.assertIn(((1, 1), (2, 1), (2, 1)), patterns[5])
        self.assertIn(((2, 1), (3, 1)), patterns[5])
        self.assertIn(((5, 1),), patterns[5])


    def test_g_ep161_sextic_factor_patterns_reach_full_catalog_at_f7(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        patterns = {}
        for p in (2, 3, 7):
            observed_patterns = set()
            observed_irreducibles = set()
            for lower in product(range(p), repeat=6):
                polynomial = (1,) + tuple(lower)
                factors = factor_polynomial(polynomial, p)
                reconstructed = [1]
                pattern = []
                for factor in factors:
                    if "degree" not in factor:
                        continue
                    coefficients = tuple(
                        value % p for value in factor["coefficients_descending"]
                    )
                    degree = factor["degree"]
                    multiplicity = factor["multiplicity"]
                    self.assertEqual(len(coefficients), degree + 1)
                    self.assertEqual(coefficients[0], 1)
                    observed_irreducibles.add((degree, coefficients))
                    pattern.append((degree, multiplicity))
                    for _ in range(multiplicity):
                        product_poly = [0] * (
                            len(reconstructed) + len(coefficients) - 1
                        )
                        for i, x in enumerate(reconstructed):
                            for j, y in enumerate(coefficients):
                                product_poly[i + j] = (
                                    product_poly[i + j] + x * y
                                ) % p
                        reconstructed = product_poly
                self.assertEqual(reconstructed, list(polynomial))
                observed_patterns.add(tuple(sorted(pattern)))
            patterns[p] = observed_patterns

            expected_counts = {
                1: p,
                2: (p ** 2 - p) // 2,
                3: (p ** 3 - p) // 3,
                4: (p ** 4 - p ** 2) // 4,
                5: (p ** 5 - p) // 5,
                6: (p ** 6 - p ** 3 - p ** 2 + p) // 6,
            }
            for degree, expected in expected_counts.items():
                self.assertEqual(
                    sum(1 for d, _ in observed_irreducibles if d == degree),
                    expected,
                    msg=f"F_{p}: degree-{degree} irreducible inventory",
                )

        # At p=7 there are at least six distinct linear irreducibles,
        # enough to realize every degree partition of six. Smaller tested
        # fields miss the all-distinct-linear pattern.
        all_sextic_shapes = {
            ((1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)),
            ((1, 1), (1, 1), (1, 1), (1, 1), (1, 2)),
            ((1, 1), (1, 1), (1, 1), (1, 1), (2, 1)),
            ((1, 1), (1, 1), (1, 1), (1, 3)),
            ((1, 1), (1, 1), (1, 1), (3, 1)),
            ((1, 1), (1, 1), (1, 2), (1, 2)),
            ((1, 1), (1, 1), (1, 2), (2, 1)),
            ((1, 1), (1, 1), (1, 4)),
            ((1, 1), (1, 1), (2, 1), (2, 1)),
            ((1, 1), (1, 1), (2, 2)),
            ((1, 1), (1, 1), (4, 1)),
            ((1, 1), (1, 2), (1, 3)),
            ((1, 1), (1, 2), (3, 1)),
            ((1, 1), (1, 3), (2, 1)),
            ((1, 1), (1, 5)),
            ((1, 1), (2, 1), (3, 1)),
            ((1, 1), (5, 1)),
            ((1, 2), (1, 2), (1, 2)),
            ((1, 2), (1, 2), (2, 1)),
            ((1, 2), (1, 4)),
            ((1, 2), (2, 1), (2, 1)),
            ((1, 2), (2, 2)),
            ((1, 2), (4, 1)),
            ((1, 3), (1, 3)),
            ((1, 3), (3, 1)),
            ((1, 4), (2, 1)),
            ((1, 6),),
            ((2, 1), (2, 1), (2, 1)),
            ((2, 1), (2, 2)),
            ((2, 1), (4, 1)),
            ((2, 3),),
            ((3, 1), (3, 1)),
            ((3, 2),),
            ((6, 1),),
        }
        self.assertEqual(patterns[7], all_sextic_shapes)
        self.assertLess(patterns[2], patterns[3])
        self.assertLess(patterns[3], patterns[7])
        self.assertNotIn(
            ((1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)),
            patterns[3],
        )



    def test_g_ep162_f5_sextics_approach_but_do_not_reach_full_catalog(self):
        from itertools import product
        from tools.spectral_fingerprint import factor_polynomial

        patterns = set()
        irreducibles = set()
        for lower in product(range(5), repeat=6):
            polynomial = (1,) + tuple(lower)
            factors = factor_polynomial(polynomial, 5)
            reconstructed = [1]
            pattern = []
            for factor in factors:
                coefficients = tuple(value % 5 for value in factor["coefficients_descending"])
                degree = factor["degree"]
                multiplicity = factor["multiplicity"]
                irreducibles.add((degree, coefficients))
                pattern.append((degree, multiplicity))
                for _ in range(multiplicity):
                    product_poly = [0] * (len(reconstructed) + len(coefficients) - 1)
                    for i, x in enumerate(reconstructed):
                        for j, y in enumerate(coefficients):
                            product_poly[i + j] = (product_poly[i + j] + x * y) % 5
                    reconstructed = product_poly
            self.assertEqual(reconstructed, list(polynomial))
            patterns.add(tuple(sorted(pattern)))

        expected_counts = {1: 5, 2: 10, 3: 40, 4: 150, 5: 624, 6: 2580}
        for degree, expected in expected_counts.items():
            self.assertEqual(sum(1 for d, _ in irreducibles if d == degree), expected)
        self.assertNotIn(((1, 1),) * 6, patterns)
        self.assertIn(((1, 1),) * 4 + ((1, 2),), patterns)
        self.assertIn(((1, 1),) * 4 + ((2, 1),), patterns)

if __name__ == "__main__":
    unittest.main()
