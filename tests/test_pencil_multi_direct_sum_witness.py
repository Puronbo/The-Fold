import unittest
from tools.pencil_multi_direct_sum_witness import verify_pencil_multi_direct_sum_witness

def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]
def mm(a,b,p):
    return [[sum(a[i][z]*b[z][j] for z in range(len(b)))%p for j in range(len(b[0]))] for i in range(len(a))]
def inverse(a,p):
    n=len(a)
    x=[[v%p for v in row]+[int(i==j) for j in range(n)] for i,row in enumerate(a)]
    for c in range(n):
        pivot=next(i for i in range(c,n) if x[i][c])
        x[c],x[pivot]=x[pivot],x[c]
        z=pow(x[c][c],-1,p); x[c]=[v*z%p for v in x[c]]
        for i in range(n):
            if i!=c and x[i][c]:
                f=x[i][c]; x[i]=[(u-f*v)%p for u,v in zip(x[i],x[c])]
    return [row[n:] for row in x]

class MultiDirectSumTests(unittest.TestCase):
    def test_scrambled_three_rectangular_blocks(self):
        q0=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1]]
        k0=[[0,1,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1]]
        s=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]]
        t=[[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,1]]
        si=[[1,4,1,4],[0,1,4,1],[0,0,1,4],[0,0,0,1]]
        ti=[[1,4,1,4,1],[0,1,4,1,4],[0,0,1,4,1],[0,0,0,1,4],[0,0,0,0,1]]
        q=mm(mm(si,q0,5),ti,5); k=mm(mm(si,k0,5),ti,5)
        out=verify_pencil_multi_direct_sum_witness(q,k,5,s,t,[(2,2),(1,2),(1,1)])
        self.assertTrue(out["verification"]["direct_sum_verified"])
        self.assertEqual(len(out["Q_blocks"]),3)
        self.assertEqual(len(out["Q_blocks"][0]),3)

    def test_generated_rectangular_partitions_are_invariant_under_independent_basis_changes(self):
        # The zero-row and zero-column blocks are retained in the ordered
        # partition; all total dimensions remain positive.
        shapes=[(1,0),(1,2),(0,1),(1,1)]
        m,n=sum(r for r,c in shapes),sum(c for r,c in shapes)
        for p in (2,3,5,7):
            q0=[[0]*n for _ in range(m)]
            k0=[[0]*n for _ in range(m)]
            ro=co=0
            for bi,(r,c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro+i][co+j]=(bi+i+2*j+1)%p
                        k0[ro+i][co+j]=(2*bi+3*i+j+1)%p
                ro+=r; co+=c
            # Independent unitriangular row and column basis changes.
            left=ident(m)
            for i in range(m-1):
                left[i][i+1]=1
            right=ident(n)
            for i in range(n-1):
                right[i][i+1]=1
            li,ri=inverse(left,p),inverse(right,p)
            q=mm(mm(li,q0,p),ri,p)
            k=mm(mm(li,k0,p),ri,p)
            with self.subTest(field=p):
                out=verify_pencil_multi_direct_sum_witness(q,k,p,left,right,shapes)
                self.assertTrue(out["verification"]["direct_sum_verified"],out)
                self.assertEqual(out["transformed_Q"],q0)
                self.assertEqual(out["transformed_K"],k0)
                self.assertEqual(out["block_shapes"],[list(x) for x in shapes])

    def test_detects_coupling_in_both_coefficients(self):
        out=verify_pencil_multi_direct_sum_witness(
          [[1,1,0],[0,1,0],[0,0,1]],[[0,0,0],[0,0,1],[0,0,0]],
          5,ident(3),ident(3),[(1,1)]*3)
        self.assertFalse(out["verification"]["direct_sum_verified"])
        self.assertFalse(out["verification"]["Q_off_diagonal_blocks_zero"])
        self.assertFalse(out["verification"]["K_off_diagonal_blocks_zero"])

    def test_singular_transform_does_not_certify(self):
        out=verify_pencil_multi_direct_sum_witness(
          [[1,0],[0,1]],[[0,0],[0,1]],5,[[1,0],[0,0]],ident(2),[(1,1)]*2)
        self.assertFalse(out["verification"]["left_transform_invertible"])
        self.assertFalse(out["verification"]["direct_sum_verified"])

    def test_invalid_partitions_and_moduli(self):
        q=[[1,0],[0,1]]; k=[[0,0],[0,1]]
        for shapes in [[(1,1)],[(1,1),(0,0)],[(1,1),(1,0)]]:
            with self.assertRaises(ValueError):
                verify_pencil_multi_direct_sum_witness(q,k,5,ident(2),ident(2),shapes)
        with self.assertRaises(ValueError):
            verify_pencil_multi_direct_sum_witness(q,k,4,ident(2),ident(2),[(1,1)]*2)


    def test_basis_scrambled_rectangular_witness_adversarial_mutations(self):
        # Reuse the G-EP90 rectangular edge case, but mutate the transformed
        # coordinates one off-diagonal block at a time before scrambling back.
        shapes = [(1, 0), (1, 2), (0, 1), (1, 1)]
        m, n = sum(r for r, c in shapes), sum(c for r, c in shapes)
        row_offsets, col_offsets = [0], [0]
        for r, c in shapes:
            row_offsets.append(row_offsets[-1] + r)
            col_offsets.append(col_offsets[-1] + c)

        for p in (2, 3, 5, 7):
            q0 = [[0] * n for _ in range(m)]
            k0 = [[0] * n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[row_offsets[b] + i][col_offsets[b] + j] = (b + i + 2*j + 1) % p
                        k0[row_offsets[b] + i][col_offsets[b] + j] = (2*b + 3*i + j + 1) % p

            left, right = ident(m), ident(n)
            for i in range(m - 1):
                left[i][i + 1] = 1
            for i in range(n - 1):
                right[i][i + 1] = 1
            left_inv, right_inv = inverse(left, p), inverse(right, p)
            q = mm(mm(left_inv, q0, p), right_inv, p)
            k = mm(mm(left_inv, k0, p), right_inv, p)

            with self.subTest(field=p, case="valid baseline"):
                baseline = verify_pencil_multi_direct_sum_witness(
                    q, k, p, left, right, shapes
                )
                self.assertTrue(baseline["verification"]["direct_sum_verified"], baseline)

            # Only blocks with positive row and column dimensions can contain
            # entries. Exercise each directed off-diagonal block separately
            # in Q and K, including both directions between the two populated
            # diagonal blocks.
            populated = [i for i, (r, c) in enumerate(shapes) if r and c]
            for source_block in populated:
                for target_block in populated:
                    if source_block == target_block:
                        continue
                    for coefficient in ("Q", "K"):
                        changed_q0 = [row[:] for row in q0]
                        changed_k0 = [row[:] for row in k0]
                        target = changed_q0 if coefficient == "Q" else changed_k0
                        target[row_offsets[source_block]][col_offsets[target_block]] = 1 % p
                        changed_q = mm(mm(left_inv, changed_q0, p), right_inv, p)
                        changed_k = mm(mm(left_inv, changed_k0, p), right_inv, p)
                        audit = verify_pencil_multi_direct_sum_witness(
                            changed_q, changed_k, p, left, right, shapes
                        )
                        with self.subTest(field=p, source_block=source_block,
                                          target_block=target_block, coefficient=coefficient):
                            self.assertFalse(audit["verification"]["direct_sum_verified"], audit)
                            if coefficient == "Q":
                                self.assertFalse(audit["verification"]["Q_off_diagonal_blocks_zero"])
                                self.assertTrue(audit["verification"]["K_off_diagonal_blocks_zero"])
                            else:
                                self.assertTrue(audit["verification"]["Q_off_diagonal_blocks_zero"])
                                self.assertFalse(audit["verification"]["K_off_diagonal_blocks_zero"])

            # Mutate both source coefficient matrices while preserving all
            # dimensions and the invertibility of the supplied transforms.
            changed_q0, changed_k0 = [row[:] for row in q0], [row[:] for row in k0]
            changed_q0[row_offsets[1]][col_offsets[3]] = 1 % p
            changed_k0[row_offsets[3]][col_offsets[1]] = 1 % p
            both = verify_pencil_multi_direct_sum_witness(
                mm(mm(left_inv, changed_q0, p), right_inv, p),
                mm(mm(left_inv, changed_k0, p), right_inv, p),
                p, left, right, shapes,
            )
            with self.subTest(field=p, case="both coefficients"):
                self.assertFalse(both["verification"]["Q_off_diagonal_blocks_zero"])
                self.assertFalse(both["verification"]["K_off_diagonal_blocks_zero"])
                self.assertFalse(both["verification"]["direct_sum_verified"])

            # Wrong but still invertible transforms are structured false
            # witnesses, not malformed inputs.
            wrong_left = [row[:] for row in left]
            wrong_left[0][2] = (wrong_left[0][2] + 1) % p
            wrong_right = [row[:] for row in right]
            wrong_right[0][2] = (wrong_right[0][2] + 1) % p
            for label, s, t in (
                ("wrong invertible left", wrong_left, right),
                ("wrong invertible right", left, wrong_right),
                ("wrong invertible pair", wrong_left, wrong_right),
            ):
                audit = verify_pencil_multi_direct_sum_witness(q, k, p, s, t, shapes)
                with self.subTest(field=p, case=label):
                    self.assertTrue(audit["verification"]["left_transform_invertible"])
                    self.assertTrue(audit["verification"]["right_transform_invertible"])
                    self.assertFalse(audit["verification"]["direct_sum_verified"])

            # Singular square transforms are well-formed but mathematically
            # invalid witnesses: return an audit rather than raising.
            singular_left = [row[:] for row in left]
            singular_left[-1] = [0] * m
            singular_right = [row[:] for row in right]
            singular_right[-1] = [0] * n
            for s, t in ((singular_left, right), (left, singular_right),
                         (singular_left, singular_right)):
                audit = verify_pencil_multi_direct_sum_witness(q, k, p, s, t, shapes)
                with self.subTest(field=p, case="singular transform"):
                    self.assertFalse(audit["verification"]["direct_sum_verified"])

            # Malformed matrices/entries are caller-input errors, distinct
            # from the failed audits above.
            for bad_s, bad_t in (
                ([[1], [0], [0]], right),
                ([[True, 0, 0], [0, 1, 0], [0, 0, 1]], right),
                (left, [[1], [0], [0], [0]]),
                (left, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1.0]]),
            ):
                with self.subTest(field=p, case="malformed transform"):
                    with self.assertRaises(ValueError):
                        verify_pencil_multi_direct_sum_witness(q, k, p, bad_s, bad_t, shapes)


    def test_equivalent_representations_preserve_multi_block_audit(self):
        shapes = [(1, 0), (1, 2), (0, 1), (1, 1)]
        m, n = sum(r for r, c in shapes), sum(c for r, c in shapes)
        ro, co = [0], [0]
        for r, c in shapes:
            ro.append(ro[-1] + r); co.append(co[-1] + c)

        for p in (2, 3, 5, 7):
            q0, k0 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro[b]+i][co[b]+j] = (b + 2*i + j + 1) % p
                        k0[ro[b]+i][co[b]+j] = (2*b + i + 3*j + 1) % p

            # Distinct, independently invertible row and column scramblings.
            left, right = ident(m), ident(n)
            for i in range(m-1):
                left[i+1][i] = 1
            for i in range(n-1):
                right[i][i+1] = 1
            li, ri = inverse(left, p), inverse(right, p)
            q, k = mm(mm(li, q0, p), ri, p), mm(mm(li, k0, p), ri, p)

            baseline = verify_pencil_multi_direct_sum_witness(q, k, p, left, right, shapes)
            self.assertTrue(baseline["verification"]["direct_sum_verified"])

            # Adding multiples of p changes representatives, not field elements.
            q_mod, k_mod = [row[:] for row in q], [row[:] for row in k]
            q_mod[0][0] += 3*p
            k_mod[-1][-1] -= 2*p
            modular = verify_pencil_multi_direct_sum_witness(
                q_mod, k_mod, p, left, right, shapes
            )
            self.assertTrue(modular["verification"]["direct_sum_verified"])
            self.assertEqual(modular["transformed_Q"], baseline["transformed_Q"])
            self.assertEqual(modular["transformed_K"], baseline["transformed_K"])

            # Reciprocal scalar rescaling leaves S Q T and S K T unchanged.
            for scalar in range(1, p):
                scaled_left = [[scalar*x % p for x in row] for row in left]
                inv_scalar = pow(scalar, -1, p)
                scaled_right = [[inv_scalar*x % p for x in row] for row in right]
                scaled = verify_pencil_multi_direct_sum_witness(
                    q, k, p, scaled_left, scaled_right, shapes
                )
                with self.subTest(field=p, scalar=scalar):
                    self.assertTrue(scaled["verification"]["direct_sum_verified"])
                    self.assertEqual(scaled["transformed_Q"], baseline["transformed_Q"])
                    self.assertEqual(scaled["transformed_K"], baseline["transformed_K"])

            # Reorder the diagonal blocks and their row/column coordinate
            # intervals together. This is a distinct valid ordered partition.
            order = [3, 1, 2, 0]
            perm_shapes = [shapes[i] for i in order]
            perm_q0, perm_k0 = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
            new_ro, new_co = [0], [0]
            for r, c in perm_shapes:
                new_ro.append(new_ro[-1]+r); new_co.append(new_co[-1]+c)
            for new_i, old_i in enumerate(order):
                r, c = shapes[old_i]
                for i in range(r):
                    for j in range(c):
                        perm_q0[new_ro[new_i]+i][new_co[new_i]+j] = q0[ro[old_i]+i][co[old_i]+j]
                        perm_k0[new_ro[new_i]+i][new_co[new_i]+j] = k0[ro[old_i]+i][co[old_i]+j]
            permuted_q = mm(mm(li, perm_q0, p), ri, p)
            permuted_k = mm(mm(li, perm_k0, p), ri, p)
            permuted = verify_pencil_multi_direct_sum_witness(
                permuted_q, permuted_k, p, left, right, perm_shapes
            )
            self.assertTrue(permuted["verification"]["direct_sum_verified"])
            self.assertEqual(permuted["block_shapes"], [list(x) for x in perm_shapes])


    def test_near_equivalences_are_rejected_without_confusing_input_errors(self):
        shapes = [(1, 0), (1, 2), (0, 1), (1, 1)]
        m, n = sum(r for r, c in shapes), sum(c for r, c in shapes)
        ro, co = [0], [0]
        for r, c in shapes:
            ro.append(ro[-1] + r); co.append(co[-1] + c)

        for p in (2, 3, 5, 7):
            q0, k0 = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro[b]+i][co[b]+j] = (b + i + j + 1) % p
                        k0[ro[b]+i][co[b]+j] = (2*b + i + 2*j + 1) % p
            left, right = ident(m), ident(n)
            for i in range(m-1):
                left[i][i+1] = 1
            for i in range(n-1):
                right[i+1][i] = 1
            li, ri = inverse(left, p), inverse(right, p)
            q, k = mm(mm(li, q0, p), ri, p), mm(mm(li, k0, p), ri, p)
            valid = verify_pencil_multi_direct_sum_witness(q, k, p, left, right, shapes)
            self.assertTrue(valid["verification"]["direct_sum_verified"])

            # Change a single source coefficient after the basis change.
            # Dimensions and entries remain valid, but the supplied witness
            # no longer maps to the requested direct sum.
            changed_q = [row[:] for row in q]
            changed_q[0][0] += 1
            source_mutation = verify_pencil_multi_direct_sum_witness(
                changed_q, k, p, left, right, shapes
            )
            with self.subTest(field=p, case="source coefficient mutation"):
                self.assertFalse(source_mutation["verification"]["direct_sum_verified"])

            # Perturb one entry in each transform while retaining invertibility.
            perturbed_left = [row[:] for row in left]
            perturbed_left[0][m-1] = (perturbed_left[0][m-1] + 1) % p
            perturbed_right = [row[:] for row in right]
            perturbed_right[n-1][0] = (perturbed_right[n-1][0] + 1) % p
            for label, s, t in (
                ("left transform entry", perturbed_left, right),
                ("right transform entry", left, perturbed_right),
            ):
                audit = verify_pencil_multi_direct_sum_witness(q, k, p, s, t, shapes)
                with self.subTest(field=p, case=label):
                    self.assertTrue(audit["verification"]["left_transform_invertible"])
                    self.assertTrue(audit["verification"]["right_transform_invertible"])
                    self.assertFalse(audit["verification"]["direct_sum_verified"])

            # Permute only the block-shape list, leaving the transformed
            # coordinate matrices in their original order. This is not the
            # equivalent simultaneous permutation tested in G-EP92.
            order = [3, 1, 2, 0]
            one_sided_shapes = [shapes[i] for i in order]
            one_sided = verify_pencil_multi_direct_sum_witness(
                q, k, p, left, right, one_sided_shapes
            )
            with self.subTest(field=p, case="one-sided block permutation"):
                self.assertFalse(one_sided["verification"]["direct_sum_verified"])

            # A malformed transform is a caller-input error, not a false
            # algebraic witness.
            with self.subTest(field=p, case="malformed transform"):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(
                        q, k, p, [[1, 0], [0, 1]], right, shapes
                    )


    def test_audit_records_match_independent_algebraic_reconstruction(self):
        # These local routines intentionally do not call the verifier's
        # private multiplication, splitting, or rank helpers.
        def independent_product(a, b, p):
            return [[sum(a[i][z]*b[z][j] for z in range(len(b))) % p
                     for j in range(len(b[0]))] for i in range(len(a))]

        def independent_rank(a, p):
            work = [[x % p for x in row] for row in a]
            rows, cols, pivot_row = len(work), len(work[0]), 0
            for col in range(cols):
                pivot = next((r for r in range(pivot_row, rows)
                              if work[r][col] % p), None)
                if pivot is None:
                    continue
                work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
                scale = pow(work[pivot_row][col], -1, p)
                work[pivot_row] = [(x*scale) % p for x in work[pivot_row]]
                for r in range(rows):
                    if r != pivot_row:
                        factor = work[r][col] % p
                        work[r] = [(x-factor*y) % p
                                   for x, y in zip(work[r], work[pivot_row])]
                pivot_row += 1
                if pivot_row == rows:
                    break
            return pivot_row

        shapes = [(1, 0), (1, 2), (0, 1), (1, 1)]
        m, n = sum(r for r, c in shapes), sum(c for r, c in shapes)
        row_cuts, col_cuts = [0], [0]
        for r, c in shapes:
            row_cuts.append(row_cuts[-1]+r)
            col_cuts.append(col_cuts[-1]+c)

        for p in (2, 3, 5, 7):
            q0, k0 = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[row_cuts[b]+i][col_cuts[b]+j] = (b+i+2*j+1) % p
                        k0[row_cuts[b]+i][col_cuts[b]+j] = (2*b+2*i+j+1) % p
            s, t = ident(m), ident(n)
            for i in range(m-1):
                s[i][i+1] = 1
            for j in range(n-1):
                t[j+1][j] = 1
            si, ti = inverse(s, p), inverse(t, p)
            q = mm(mm(si, q0, p), ti, p)
            k = mm(mm(si, k0, p), ti, p)

            # Also exercise a false but well-formed witness. The same
            # independent calculation must explain every reported flag.
            cases = [("valid", q, k, s, t, True)]
            bad_q = [row[:] for row in q]
            bad_q[0][0] += 1
            cases.append(("mutated source", bad_q, k, s, t, False))
            bad_s = [row[:] for row in s]
            bad_s[0][m-1] = (bad_s[0][m-1] + 1) % p
            cases.append(("perturbed transform", q, k, bad_s, t, False))

            for label, source_q, source_k, left, right, expected in cases:
                audit = verify_pencil_multi_direct_sum_witness(
                    source_q, source_k, p, left, right, shapes
                )
                transformed_q = independent_product(
                    independent_product(left, source_q, p), right, p
                )
                transformed_k = independent_product(
                    independent_product(left, source_k, p), right, p
                )
                self.assertEqual(audit["transformed_Q"], transformed_q)
                self.assertEqual(audit["transformed_K"], transformed_k)

                expected_q_blocks, expected_k_blocks = [], []
                q_off_zero = k_off_zero = True
                for i in range(len(shapes)):
                    q_row, k_row = [], []
                    for j in range(len(shapes)):
                        qb = [row[col_cuts[j]:col_cuts[j+1]]
                              for row in transformed_q[row_cuts[i]:row_cuts[i+1]]]
                        kb = [row[col_cuts[j]:col_cuts[j+1]]
                              for row in transformed_k[row_cuts[i]:row_cuts[i+1]]]
                        q_row.append(qb); k_row.append(kb)
                        if i != j:
                            q_off_zero &= all(x % p == 0 for row in qb for x in row)
                            k_off_zero &= all(x % p == 0 for row in kb for x in row)
                    expected_q_blocks.append(q_row)
                    expected_k_blocks.append(k_row)
                self.assertEqual(audit["Q_blocks"], expected_q_blocks)
                self.assertEqual(audit["K_blocks"], expected_k_blocks)

                sr, tr = independent_rank(left, p), independent_rank(right, p)
                checks = audit["verification"]
                self.assertEqual(checks["left_transform_rank"], sr)
                self.assertEqual(checks["right_transform_rank"], tr)
                self.assertEqual(checks["left_transform_invertible"], sr == m)
                self.assertEqual(checks["right_transform_invertible"], tr == n)
                self.assertEqual(checks["Q_off_diagonal_blocks_zero"], q_off_zero)
                self.assertEqual(checks["K_off_diagonal_blocks_zero"], k_off_zero)
                self.assertEqual(checks["direct_sum_verified"],
                                 sr == m and tr == n and q_off_zero and k_off_zero)
                with self.subTest(field=p, case=label):
                    self.assertEqual(checks["direct_sum_verified"], expected)


    def test_json_round_trip_and_replay_reject_forged_audit_metadata(self):
        import copy
        import json

        def exact_tree_equal(a, b):
            if type(a) is not type(b):
                return False
            if isinstance(a, dict):
                return (a.keys() == b.keys()
                        and all(exact_tree_equal(a[k], b[k]) for k in a))
            if isinstance(a, list):
                return (len(a) == len(b)
                        and all(exact_tree_equal(x, y) for x, y in zip(a, b)))
            return a == b

        shapes = [(1, 1), (1, 1)]
        s = t = ident(2)
        q = [[1, 0], [0, 2]]
        k = [[2, 0], [0, 1]]
        false_q = [[1, 1], [0, 2]]

        for p in (2, 3, 5, 7):
            for label, source_q, expected in (
                ("valid", q, True),
                ("false", false_q, False),
            ):
                original = verify_pencil_multi_direct_sum_witness(
                    source_q, k, p, s, t, shapes
                )
                serialized = json.dumps(original, sort_keys=True)
                restored = json.loads(serialized)
                with self.subTest(field=p, case=label):
                    self.assertTrue(exact_tree_equal(original, restored))
                    self.assertEqual(original["verification"]["direct_sum_verified"],
                                     expected)

                # Serialized diagnostics are data, not authority: rebuild
                # the audit from the original inputs and compare all fields.
                replay = verify_pencil_multi_direct_sum_witness(
                    source_q, k, p, s, t, shapes
                )
                self.assertTrue(exact_tree_equal(restored, replay))

                forged = copy.deepcopy(restored)
                forged["verification"]["direct_sum_verified"] = not (
                    forged["verification"]["direct_sum_verified"])
                forged["verification"]["left_transform_rank"] = True
                forged["verification"]["Q_off_diagonal_blocks_zero"] = (
                    not forged["verification"]["Q_off_diagonal_blocks_zero"])
                with self.subTest(field=p, case=label+" forged record"):
                    self.assertFalse(exact_tree_equal(forged, replay))
                    self.assertIs(type(forged["verification"]["left_transform_rank"]), bool)
                    self.assertIs(type(replay["verification"]["left_transform_rank"]), int)

                typed = copy.deepcopy(restored)
                typed["verification"]["left_transform_rank"] = bool(
                    typed["verification"]["left_transform_rank"])
                self.assertFalse(exact_tree_equal(typed, replay))
                missing = copy.deepcopy(restored)
                del missing["Q_blocks"]
                self.assertFalse(exact_tree_equal(missing, replay))



    def test_json_boundary_rejects_ambiguous_and_malformed_audit_snapshots(self):
        import copy
        import json

        def reject_duplicate_keys(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError("duplicate JSON object key")
                result[key] = value
            return result

        def reject_nonfinite(token):
            raise ValueError("non-finite JSON number: " + token)

        def strict_loads(payload):
            return json.loads(payload, object_pairs_hook=reject_duplicate_keys,
                              parse_constant=reject_nonfinite)

        def exact_tree_equal(a, b):
            if type(a) is not type(b):
                return False
            if isinstance(a, dict):
                return (a.keys() == b.keys()
                        and all(exact_tree_equal(a[k], b[k]) for k in a))
            if isinstance(a, list):
                return (len(a) == len(b)
                        and all(exact_tree_equal(x, y) for x, y in zip(a, b)))
            return a == b

        q, k = [[1, 0], [0, 2]], [[2, 0], [0, 1]]
        identity = ident(2)
        expected = verify_pencil_multi_direct_sum_witness(
            q, k, 5, identity, identity, [(1, 1), (1, 1)]
        )
        payload = json.dumps(expected, sort_keys=True)
        restored = strict_loads(payload)
        self.assertTrue(exact_tree_equal(restored, expected))

        # Duplicate keys are ambiguous under ordinary JSON decoding, which
        # silently keeps one value; the strict boundary must reject them.
        duplicate = payload[:-1] + ', "schema": "forged-version"}'
        with self.assertRaisesRegex(ValueError, "duplicate"):
            strict_loads(duplicate)

        for malformed in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(nonfinite=malformed):
                with self.assertRaisesRegex(ValueError, "non-finite"):
                    strict_loads('{"rank": ' + malformed + '}')

        mutations = []
        wrong_version = copy.deepcopy(restored)
        wrong_version["schema"] = "the-fold-pencil-multi-direct-sum-witness-v2"
        mutations.append(("schema version", wrong_version))
        malformed_grid = copy.deepcopy(restored)
        malformed_grid["Q_blocks"] = [[["not-a-row"]]]
        mutations.append(("nested array", malformed_grid))
        floating_rank = copy.deepcopy(restored)
        floating_rank["verification"]["left_transform_rank"] = 2.0
        mutations.append(("floating numeric", floating_rank))
        boolean_rank = copy.deepcopy(restored)
        boolean_rank["verification"]["left_transform_rank"] = True
        mutations.append(("boolean numeric", boolean_rank))
        missing_field = copy.deepcopy(restored)
        del missing_field["right_transform"]
        mutations.append(("missing required field", missing_field))

        for label, record in mutations:
            with self.subTest(malformed=label):
                encoded = json.dumps(record)
                decoded = strict_loads(encoded)
                self.assertFalse(exact_tree_equal(decoded, expected))

        # Malformed snapshots are certificate-data failures in this
        # test-side boundary; malformed original caller inputs remain the
        # verifier's separate ValueError boundary.
        for bad_q in (None, [], [[1, 2], [3]]):
            with self.subTest(caller_input=bad_q):
                with self.assertRaises(ValueError):
                    verify_pencil_multi_direct_sum_witness(
                        bad_q, k, 5, identity, identity, [(1, 1), (1, 1)]
                    )



    def test_deterministic_mutation_sweep_covers_every_snapshot_field(self):
        import copy
        import json

        def exact_tree_equal(a, b):
            if type(a) is not type(b):
                return False
            if isinstance(a, dict):
                return (a.keys() == b.keys()
                        and all(exact_tree_equal(a[k], b[k]) for k in a))
            if isinstance(a, list):
                return (len(a) == len(b)
                        and all(exact_tree_equal(x, y) for x, y in zip(a, b)))
            return a == b

        q = [[1, 0], [0, 2]]
        k = [[2, 0], [0, 1]]
        identity = ident(2)
        baseline = verify_pencil_multi_direct_sum_witness(
            q, k, 5, identity, identity, [(1, 1), (1, 1)]
        )
        snapshot = json.loads(json.dumps(baseline, sort_keys=True))

        # Enumerate every dict field and every list slot recursively. Replace
        # exactly one location at a time, then require exact replay mismatch.
        paths = []

        def collect(value, path=()):
            if isinstance(value, dict):
                for key, child in value.items():
                    paths.append(path + (("key", key),))
                    collect(child, path + (("key", key),))
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    paths.append(path + (("index", index),))
                    collect(child, path + (("index", index),))

        collect(snapshot)
        self.assertGreater(len(paths), 20)

        def replace_at(root, path):
            changed = copy.deepcopy(root)
            parent = changed
            for kind, part in path[:-1]:
                parent = parent[part]
            kind, part = path[-1]
            parent[part] = "__G_EP97_MUTATION__"
            return changed

        for path in paths:
            with self.subTest(path=path):
                mutated = replace_at(snapshot, path)
                encoded = json.dumps(mutated, sort_keys=True)
                decoded = json.loads(encoded)
                self.assertFalse(exact_tree_equal(decoded, baseline))

        # The sweep itself must be deterministic and include both the outer
        # record and nested verification/block-grid structures.
        self.assertIn((("key", "verification"),), paths)
        self.assertIn((("key", "Q_blocks"),), paths)
        self.assertIn((("key", "K_blocks"),), paths)
        self.assertTrue(any(path[:2] == (("key", "verification"),
                                         ("key", "direct_sum_verified"))
                            for path in paths))
        self.assertTrue(any(path[:2] == (("key", "Q_blocks"),
                                         ("index", 0)) for path in paths))



    def test_v1_audit_snapshot_schema_contract_is_separate_from_algebra(self):
        import copy

        q, k = [[1, 0], [0, 2]], [[2, 0], [0, 1]]
        identity = ident(2)
        valid = verify_pencil_multi_direct_sum_witness(
            q, k, 5, identity, identity, [(1, 1), (1, 1)]
        )

        def is_int(value, minimum=None):
            return (type(value) is int
                    and (minimum is None or value >= minimum))

        def matrix_shape(value, rows, cols):
            return (type(value) is list and len(value) == rows
                    and all(type(row) is list and len(row) == cols
                            and all(is_int(x) for x in row) for row in value))

        def structurally_valid(record):
            if type(record) is not dict:
                return False
            required = {
                "schema", "field", "source_shape", "block_shapes",
                "left_transform", "right_transform", "transformed_Q",
                "transformed_K", "Q_blocks", "K_blocks", "verification",
                "scope",
            }
            if set(record) != required:
                return False
            if record["schema"] != "the-fold-pencil-multi-direct-sum-witness-v1":
                return False
            if type(record["field"]) is not str or not record["field"].startswith("F_"):
                return False
            shape = record["source_shape"]
            blocks = record["block_shapes"]
            if (type(shape) is not list or len(shape) != 2
                    or not all(is_int(x, 1) for x in shape)
                    or type(blocks) is not list or len(blocks) < 2):
                return False
            if any(type(b) is not list or len(b) != 2
                   or not all(is_int(x, 0) for x in b)
                   or b == [0, 0] for b in blocks):
                return False
            m, n = shape
            if sum(b[0] for b in blocks) != m or sum(b[1] for b in blocks) != n:
                return False
            count = len(blocks)
            if not matrix_shape(record["left_transform"], m, m):
                return False
            if not matrix_shape(record["right_transform"], n, n):
                return False
            if not matrix_shape(record["transformed_Q"], m, n):
                return False
            if not matrix_shape(record["transformed_K"], m, n):
                return False
            for grid_name in ("Q_blocks", "K_blocks"):
                grid = record[grid_name]
                if type(grid) is not list or len(grid) != count:
                    return False
                for i, grid_row in enumerate(grid):
                    if type(grid_row) is not list or len(grid_row) != count:
                        return False
                    for j, block in enumerate(grid_row):
                        if not matrix_shape(block, blocks[i][0], blocks[j][1]):
                            return False
            verification = record["verification"]
            expected_types = {
                "left_transform_rank": int,
                "right_transform_rank": int,
                "left_transform_invertible": bool,
                "right_transform_invertible": bool,
                "Q_off_diagonal_blocks_zero": bool,
                "K_off_diagonal_blocks_zero": bool,
                "direct_sum_verified": bool,
            }
            if type(verification) is not dict or set(verification) != set(expected_types):
                return False
            if any(type(verification[key]) is not typ
                   for key, typ in expected_types.items()):
                return False
            if not (0 <= verification["left_transform_rank"] <= m
                    and 0 <= verification["right_transform_rank"] <= n):
                return False
            return type(record["scope"]) is str

        self.assertTrue(structurally_valid(valid))
        # A correctly shaped but mathematically false witness is still a
        # structurally valid v1 record: algebraic truth is a separate layer.
        wrong_left = [[1, 1], [0, 1]]
        false_witness = verify_pencil_multi_direct_sum_witness(
            q, k, 5, wrong_left, identity, [(1, 1), (1, 1)]
        )
        self.assertTrue(structurally_valid(false_witness))
        self.assertFalse(false_witness["verification"]["direct_sum_verified"])

        mutations = []
        for field, value in (
            ("schema", "unknown-v2"),
            ("source_shape", [2, True]),
            ("block_shapes", [[1, 1], [1, 0]]),
            ("left_transform", [[1, 0.0], [0, 1]]),
            ("transformed_Q", [[1, 0]]),
            ("Q_blocks", []),
            ("K_blocks", [[[1]]]),
            ("scope", None),
        ):
            changed = copy.deepcopy(valid)
            changed[field] = value
            mutations.append((field, changed))
        changed = copy.deepcopy(valid)
        changed["verification"]["left_transform_rank"] = True
        mutations.append(("boolean rank", changed))
        changed = copy.deepcopy(valid)
        changed["verification"]["unexpected"] = 0
        mutations.append(("unexpected diagnostic", changed))
        for label, record in mutations:
            with self.subTest(malformed_schema=label):
                self.assertFalse(structurally_valid(record))

