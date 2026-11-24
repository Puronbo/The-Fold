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


if __name__ == "__main__":
    unittest.main()
