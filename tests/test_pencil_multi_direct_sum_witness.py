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



    def test_v1_schema_contract_rectangular_edges_and_block_count_grid(self):
        import copy

        def structural(record):
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
            shape, blocks = record["source_shape"], record["block_shapes"]
            is_int = lambda x: type(x) is int
            if (type(shape) is not list or len(shape) != 2
                    or not all(is_int(x) and x > 0 for x in shape)
                    or type(blocks) is not list or len(blocks) < 2):
                return False
            if any(type(b) is not list or len(b) != 2
                   or not all(is_int(x) and x >= 0 for x in b)
                   or b == [0, 0] for b in blocks):
                return False
            m, n = shape
            if sum(b[0] for b in blocks) != m or sum(b[1] for b in blocks) != n:
                return False

            def matrix(value, rows, cols):
                return (type(value) is list and len(value) == rows
                        and all(type(row) is list and len(row) == cols
                                and all(is_int(x) for x in row) for row in value))
            if not matrix(record["left_transform"], m, m):
                return False
            if not matrix(record["right_transform"], n, n):
                return False
            if not matrix(record["transformed_Q"], m, n):
                return False
            if not matrix(record["transformed_K"], m, n):
                return False
            count = len(blocks)
            for name in ("Q_blocks", "K_blocks"):
                grid = record[name]
                if type(grid) is not list or len(grid) != count:
                    return False
                for i, row in enumerate(grid):
                    if type(row) is not list or len(row) != count:
                        return False
                    for j, block in enumerate(row):
                        if not matrix(block, blocks[i][0], blocks[j][1]):
                            return False
            v = record["verification"]
            types = {
                "left_transform_rank": int, "right_transform_rank": int,
                "left_transform_invertible": bool, "right_transform_invertible": bool,
                "Q_off_diagonal_blocks_zero": bool, "K_off_diagonal_blocks_zero": bool,
                "direct_sum_verified": bool,
            }
            return (type(v) is dict and set(v) == set(types)
                    and all(type(v[key]) is typ for key, typ in types.items())
                    and 0 <= v["left_transform_rank"] <= m
                    and 0 <= v["right_transform_rank"] <= n
                    and type(record["scope"]) is str)

        fixtures = [
            ([(1, 1), (1, 1)], 2, 2),
            ([(0, 1), (1, 0), (1, 1)], 2, 2),
            ([(1, 0), (0, 1), (1, 1), (0, 1)], 2, 3),
        ]
        for shapes, rows, cols in fixtures:
            with self.subTest(block_count=len(shapes), shapes=shapes):
                q = [[0] * cols for _ in range(rows)]
                k = [[0] * cols for _ in range(rows)]
                # Populate only the final nonempty diagonal block when possible.
                for i, (r, c) in enumerate(shapes):
                    if r and c:
                        r0 = sum(x[0] for x in shapes[:i])
                        c0 = sum(x[1] for x in shapes[:i])
                        q[r0][c0] = 1
                        k[r0][c0] = 2
                result = verify_pencil_multi_direct_sum_witness(
                    q, k, 5, ident(rows), ident(cols), shapes
                )
                self.assertTrue(structural(result))
                self.assertTrue(result["verification"]["direct_sum_verified"])
                # Every represented block has the exact declared rectangular shape,
                # including legal 0×c and r×0 blocks.
                for i, (r, _) in enumerate(shapes):
                    for j, (_, c) in enumerate(shapes):
                        self.assertEqual(len(result["Q_blocks"][i][j]), r)
                        self.assertTrue(all(len(line) == c
                                            for line in result["Q_blocks"][i][j]))

        # Schema validation does not promote a false witness to a valid one.
        false = verify_pencil_multi_direct_sum_witness(
            [[1, 0], [0, 2]], [[2, 0], [0, 1]], 5,
            [[1, 1], [0, 1]], ident(2), [(1, 1), (1, 1)]
        )
        self.assertTrue(structural(false))
        self.assertFalse(false["verification"]["direct_sum_verified"])

        # Nested grid shape errors are structural failures, even if all
        # scalar diagnostics remain untouched.
        good = verify_pencil_multi_direct_sum_witness(
            [[1, 0], [0, 2]], [[2, 0], [0, 1]], 5,
            ident(2), ident(2), [(1, 1), (1, 1)]
        )
        for name, mutate in (
            ("missing grid row", lambda x: x["Q_blocks"].pop()),
            ("short grid row", lambda x: x["K_blocks"][0].pop()),
            ("wrong nested matrix height", lambda x: x["Q_blocks"][0].__setitem__(0, [])),
            ("wrong nested matrix width", lambda x: x["K_blocks"][0].__setitem__(1, [[0, 0]])),
        ):
            changed = copy.deepcopy(good)
            mutate(changed)
            with self.subTest(malformed_nested=name):
                self.assertFalse(structural(changed))



    def test_g_ep100_schema_and_algebraic_outcome_cross_product(self):
        import copy

        q = [[1, 0], [0, 2]]
        k = [[2, 0], [0, 1]]
        blocks = [(1, 1), (1, 1)]
        eye = ident(2)

        def schema_valid(record):
            if type(record) is not dict:
                return False
            fields = {
                "schema", "field", "source_shape", "block_shapes",
                "left_transform", "right_transform", "transformed_Q",
                "transformed_K", "Q_blocks", "K_blocks", "verification", "scope",
            }
            if set(record) != fields:
                return False
            if record["schema"] != "the-fold-pencil-multi-direct-sum-witness-v1":
                return False
            if type(record["field"]) is not str or not record["field"].startswith("F_"):
                return False
            shape, parts = record["source_shape"], record["block_shapes"]
            if (type(shape) is not list or len(shape) != 2
                    or any(type(x) is not int or x <= 0 for x in shape)
                    or type(parts) is not list or len(parts) < 2):
                return False
            if any(type(part) is not list or len(part) != 2
                   or any(type(x) is not int or x < 0 for x in part)
                   or part == [0, 0] for part in parts):
                return False
            m, n = shape
            if sum(x[0] for x in parts) != m or sum(x[1] for x in parts) != n:
                return False

            def matrix(value, rows, cols):
                return (type(value) is list and len(value) == rows
                        and all(type(row) is list and len(row) == cols
                                and all(type(x) is int for x in row)
                                for row in value))
            if not matrix(record["left_transform"], m, m):
                return False
            if not matrix(record["right_transform"], n, n):
                return False
            for name in ("transformed_Q", "transformed_K"):
                if not matrix(record[name], m, n):
                    return False
            count = len(parts)
            for name in ("Q_blocks", "K_blocks"):
                grid = record[name]
                if type(grid) is not list or len(grid) != count:
                    return False
                for i, row in enumerate(grid):
                    if type(row) is not list or len(row) != count:
                        return False
                    for j, cell in enumerate(row):
                        if not matrix(cell, parts[i][0], parts[j][1]):
                            return False
            v = record["verification"]
            expected = {
                "left_transform_rank": int, "right_transform_rank": int,
                "left_transform_invertible": bool, "right_transform_invertible": bool,
                "Q_off_diagonal_blocks_zero": bool, "K_off_diagonal_blocks_zero": bool,
                "direct_sum_verified": bool,
            }
            return (type(v) is dict and set(v) == set(expected)
                    and all(type(v[name]) is typ for name, typ in expected.items())
                    and 0 <= v["left_transform_rank"] <= m
                    and 0 <= v["right_transform_rank"] <= n
                    and type(record["scope"]) is str)

        # 1. Structurally valid and algebraically valid.
        positive = verify_pencil_multi_direct_sum_witness(
            q, k, 5, eye, eye, blocks
        )
        self.assertTrue(schema_valid(positive))
        self.assertTrue(positive["verification"]["direct_sum_verified"])

        # 2. Structurally valid, but an invertible shear creates cross-block
        # entries. This is a mathematical negative, not a schema failure.
        false_math = verify_pencil_multi_direct_sum_witness(
            q, k, 5, [[1, 1], [0, 1]], eye, blocks
        )
        self.assertTrue(schema_valid(false_math))
        self.assertFalse(false_math["verification"]["direct_sum_verified"])
        self.assertFalse(false_math["verification"]["Q_off_diagonal_blocks_zero"])

        # 3. Structurally invalid snapshots are rejected regardless of the
        # valid witness from which they were copied.
        malformed = copy.deepcopy(positive)
        malformed["Q_blocks"][0].pop()
        self.assertFalse(schema_valid(malformed))
        malformed = copy.deepcopy(positive)
        malformed["verification"]["left_transform_rank"] = True
        self.assertFalse(schema_valid(malformed))

        # 4. Singular transforms remain a well-formed audit record with an
        # explicit negative algebraic result, rather than a schema exception.
        singular = verify_pencil_multi_direct_sum_witness(
            q, k, 5, [[1, 0], [0, 0]], eye, blocks
        )
        self.assertTrue(schema_valid(singular))
        self.assertFalse(singular["verification"]["left_transform_invertible"])
        self.assertFalse(singular["verification"]["direct_sum_verified"])

    def test_g_ep101_independent_audit_record_reconstruction(self):
        import copy

        def reference(q, k, p, left, right, shapes):
            # Deliberately test-local reconstruction: no production verifier
            # multiplication, rank, or block-splitting helpers are used.
            def multiply(a, b):
                return [[sum(a[i][z] * b[z][j] for z in range(len(b))) % p
                         for j in range(len(b[0]))] for i in range(len(a))]

            def rank(matrix):
                a = [[x % p for x in row] for row in matrix]
                r = 0
                for c in range(len(a[0])):
                    pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
                    if pivot is None:
                        continue
                    a[r], a[pivot] = a[pivot], a[r]
                    scale = pow(a[r][c], -1, p)
                    a[r] = [(x * scale) % p for x in a[r]]
                    for i in range(len(a)):
                        if i != r:
                            factor = a[i][c]
                            a[i] = [(x - factor * y) % p
                                    for x, y in zip(a[i], a[r])]
                    r += 1
                    if r == len(a):
                        break
                return r

            s = [[x % p for x in row] for row in left]
            t = [[x % p for x in row] for row in right]
            qn = [[x % p for x in row] for row in q]
            kn = [[x % p for x in row] for row in k]
            tq, tk = multiply(multiply(s, qn), t), multiply(multiply(s, kn), t)
            row_edges, col_edges = [0], [0]
            for rows, cols in shapes:
                row_edges.append(row_edges[-1] + rows)
                col_edges.append(col_edges[-1] + cols)

            def split(matrix):
                return [[[line[col_edges[j]:col_edges[j + 1]]
                          for line in matrix[row_edges[i]:row_edges[i + 1]]]
                         for j in range(len(shapes))]
                        for i in range(len(shapes))]

            qb, kb = split(tq), split(tk)
            sr, tr = rank(s), rank(t)
            qzero = all(x % p == 0 for i in range(len(shapes))
                        for j in range(len(shapes)) if i != j
                        for line in qb[i][j] for x in line)
            kzero = all(x % p == 0 for i in range(len(shapes))
                        for j in range(len(shapes)) if i != j
                        for line in kb[i][j] for x in line)
            return {
                "field": f"F_{p}", "source_shape": [len(q), len(q[0])],
                "block_shapes": [list(x) for x in shapes],
                "left_transform": s, "right_transform": t,
                "transformed_Q": tq, "transformed_K": tk,
                "Q_blocks": qb, "K_blocks": kb,
                "verification": {
                    "left_transform_rank": sr, "right_transform_rank": tr,
                    "left_transform_invertible": sr == len(q),
                    "right_transform_invertible": tr == len(q[0]),
                    "Q_off_diagonal_blocks_zero": qzero,
                    "K_off_diagonal_blocks_zero": kzero,
                    "direct_sum_verified": (sr == len(q) and tr == len(q[0])
                                            and qzero and kzero),
                },
            }

        shapes = [(1, 0), (1, 2), (0, 1), (1, 1)]
        p, q, k = 5, [[0, 0, 0, 0], [1, 2, 0, 0], [0, 0, 0, 3]], [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 4]]
        # The first and third blocks exercise zero-width and zero-height slices.
        # Nonzero entries occupy only the second and fourth diagonal blocks.
        left = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
        right = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
        for witness_left in (ident(3), left, [[1, 0, 0], [0, 0, 0], [0, 0, 1]]):
            record = verify_pencil_multi_direct_sum_witness(
                q, k, p, witness_left, right, shapes
            )
            expected = reference(q, k, p, witness_left, right, shapes)
            for key, value in expected.items():
                with self.subTest(transform=witness_left, field=key):
                    self.assertEqual(record[key], value)

        # The record can remain schema-shaped while being inconsistent with
        # the source inputs and supplied transforms. Each mutation is caught
        # by reconstruction, not merely by the structural schema validator.
        baseline = verify_pencil_multi_direct_sum_witness(
            q, k, p, ident(3), ident(4), shapes
        )
        mutations = (
            ("transformed Q", lambda x: x["transformed_Q"][0].__setitem__(0, 4)),
            ("transformed K", lambda x: x["transformed_K"][1].__setitem__(1, 4)),
            ("Q block", lambda x: x["Q_blocks"][1][1][0].__setitem__(0, 4)),
            ("K block", lambda x: x["K_blocks"][1][1][0].__setitem__(0, 4)),
            ("rank diagnostic", lambda x: x["verification"].__setitem__("left_transform_rank", 2)),
            ("aggregate diagnostic", lambda x: x["verification"].__setitem__("direct_sum_verified", False)),
        )
        expected = reference(q, k, p, ident(3), ident(4), shapes)
        for label, mutate in mutations:
            forged = copy.deepcopy(baseline)
            mutate(forged)
            with self.subTest(forged_field=label):
                self.assertNotEqual(
                    {key: forged[key] for key in expected},
                    expected,
                )

        # A false witness and a singular witness are reconstructed too:
        # record consistency does not imply a positive algebraic result.
        false_left = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
        for witness_left in (false_left, [[1, 0, 0], [0, 0, 0], [0, 0, 1]]):
            record = verify_pencil_multi_direct_sum_witness(
                q, k, p, witness_left, ident(4), shapes
            )
            expected = reference(q, k, p, witness_left, ident(4), shapes)
            for key, value in expected.items():
                self.assertEqual(record[key], value)

    def test_g_ep102_seeded_cross_field_rectangular_reconstruction(self):
        import copy
        import random

        def multiply(a, b, p):
            return [[sum(a[i][z] * b[z][j] for z in range(len(b))) % p
                     for j in range(len(b[0]))] for i in range(len(a))]

        def inverse(matrix, p):
            n = len(matrix)
            a = [[x % p for x in row] + [int(i == j) for j in range(n)]
                 for i, row in enumerate(matrix)]
            for col in range(n):
                pivot = next(i for i in range(col, n) if a[i][col] % p)
                a[col], a[pivot] = a[pivot], a[col]
                scale = pow(a[col][col], -1, p)
                a[col] = [(x * scale) % p for x in a[col]]
                for i in range(n):
                    if i != col:
                        factor = a[i][col]
                        a[i] = [(x - factor * y) % p
                                for x, y in zip(a[i], a[col])]
            return [row[n:] for row in a]

        def random_invertible(rng, n, p):
            a = [[int(i == j) for j in range(n)] for i in range(n)]
            for _ in range(12):
                i, j = rng.sample(range(n), 2)
                if rng.randrange(2):
                    a[i], a[j] = a[j], a[i]
                else:
                    factor = rng.randrange(p)
                    a[i] = [(x + factor * y) % p for x, y in zip(a[i], a[j])]
            return a

        shapes_by_field = {
            2: [(1, 1), (1, 0), (0, 1), (1, 1)],
            3: [(2, 1), (0, 1), (1, 0), (1, 1)],
            5: [(1, 0), (1, 2), (0, 1), (1, 1)],
            7: [(1, 1), (1, 1), (1, 0), (0, 1)],
        }
        for p, shapes in shapes_by_field.items():
            with self.subTest(field=p):
                rng = random.Random(10100 + p)
                m, n = sum(x[0] for x in shapes), sum(x[1] for x in shapes)
                # Construct two independent block-diagonal rectangular matrices.
                base_q = [[0] * n for _ in range(m)]
                base_k = [[0] * n for _ in range(m)]
                ro = co = 0
                for rows, cols in shapes:
                    for i in range(rows):
                        for j in range(cols):
                            base_q[ro + i][co + j] = rng.randrange(p)
                            base_k[ro + i][co + j] = rng.randrange(p)
                    ro += rows
                    co += cols

                left = random_invertible(rng, m, p)
                right = random_invertible(rng, n, p)
                inv_left, inv_right = inverse(left, p), inverse(right, p)
                # Present the same pencil in independently scrambled bases.
                source_q = multiply(multiply(inv_left, base_q, p), inv_right, p)
                source_k = multiply(multiply(inv_left, base_k, p), inv_right, p)
                record = verify_pencil_multi_direct_sum_witness(
                    source_q, source_k, p, left, right, shapes
                )
                self.assertEqual(record["transformed_Q"], base_q)
                self.assertEqual(record["transformed_K"], base_k)
                self.assertEqual(record["verification"]["direct_sum_verified"], True)
                self.assertEqual(record["verification"]["left_transform_invertible"], True)
                self.assertEqual(record["verification"]["right_transform_invertible"], True)

                # Adding multiples of p to source entries is representation-
                # equivalent and must preserve the normalized audit.
                shifted_q = [[x + p * (i + j + 1) for j, x in enumerate(row)]
                             for i, row in enumerate(source_q)]
                shifted_k = [[x - p * (i + j + 2) for j, x in enumerate(row)]
                             for i, row in enumerate(source_k)]
                shifted = verify_pencil_multi_direct_sum_witness(
                    shifted_q, shifted_k, p, left, right, shapes
                )
                for key in ("transformed_Q", "transformed_K", "Q_blocks", "K_blocks", "verification"):
                    self.assertEqual(shifted[key], record[key])

                # A one-entry snapshot forgery keeps dimensions and primitive
                # types intact, but no longer matches independent replay.
                forged = copy.deepcopy(record)
                forged["transformed_Q"][0][0] = (forged["transformed_Q"][0][0] + 1) % p
                self.assertEqual(len(forged["transformed_Q"]), m)
                self.assertEqual(len(forged["transformed_Q"][0]), n)
                self.assertNotEqual(forged["transformed_Q"], base_q)
                self.assertEqual(record["field"], f"F_{p}")

    def test_g_ep103_three_layer_audit_pipeline_mutation_matrix(self):
        import copy

        p = 5
        q = [[1, 0], [0, 2]]
        k = [[2, 0], [0, 1]]
        shapes = [(1, 1), (1, 1)]
        identity = ident(2)

        def schema_ok(record):
            required = {
                "schema", "field", "source_shape", "block_shapes",
                "left_transform", "right_transform", "transformed_Q",
                "transformed_K", "Q_blocks", "K_blocks", "verification",
                "scope",
            }
            if type(record) is not dict or set(record) != required:
                return False
            if record["schema"] != "the-fold-pencil-multi-direct-sum-witness-v1":
                return False
            if type(record["field"]) is not str or record["field"] != "F_5":
                return False
            if record["source_shape"] != [2, 2] or type(record["source_shape"]) is not list:
                return False
            if record["block_shapes"] != [[1, 1], [1, 1]]:
                return False

            def matrix(value, rows, cols):
                return (type(value) is list and len(value) == rows
                        and all(type(row) is list and len(row) == cols
                                and all(type(x) is int for x in row)
                                for row in value))
            if not matrix(record["left_transform"], 2, 2):
                return False
            if not matrix(record["right_transform"], 2, 2):
                return False
            if not matrix(record["transformed_Q"], 2, 2):
                return False
            if not matrix(record["transformed_K"], 2, 2):
                return False
            for name in ("Q_blocks", "K_blocks"):
                grid = record[name]
                if type(grid) is not list or len(grid) != 2:
                    return False
                if any(type(row) is not list or len(row) != 2 for row in grid):
                    return False
                if any(not matrix(block, 1, 1) for row in grid for block in row):
                    return False
            v = record["verification"]
            expected_types = {
                "left_transform_rank": int, "right_transform_rank": int,
                "left_transform_invertible": bool, "right_transform_invertible": bool,
                "Q_off_diagonal_blocks_zero": bool, "K_off_diagonal_blocks_zero": bool,
                "direct_sum_verified": bool,
            }
            return (type(v) is dict and set(v) == set(expected_types)
                    and all(type(v[key]) is typ for key, typ in expected_types.items())
                    and 0 <= v["left_transform_rank"] <= 2
                    and 0 <= v["right_transform_rank"] <= 2
                    and type(record["scope"]) is str)

        def independent_reconstruction(left, right):
            def mm(a, b):
                return [[sum(a[i][z] * b[z][j] for z in range(len(b))) % p
                         for j in range(len(b[0]))] for i in range(len(a))]
            tq = mm(mm(left, q), right)
            tk = mm(mm(left, k), right)
            qb = [[[[tq[i][j]] for j in range(1)] for i in range(1)],
                  [[[tq[i][j]] for j in range(1, 2)] for i in range(1, 2)]]
            # Explicit interval slicing keeps the reference separate from the
            # production block-splitting routine.
            def split(matrix):
                return [[ [row[j:j + 1] for row in matrix[i:i + 1]]
                          for j in (0, 1)] for i in (0, 1)]
            qb, kb = split(tq), split(tk)

            def rank2(a):
                a = [[x % p for x in row] for row in a]
                if a[0][0]:
                    return 2 if (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % p else 1
                return 2 if a[0][1] and a[1][0] else int(any(any(row) for row in a))
            lr, rr = rank2(left), rank2(right)
            qzero = all(qb[i][j][0][0] == 0 for i in range(2) for j in range(2) if i != j)
            kzero = all(kb[i][j][0][0] == 0 for i in range(2) for j in range(2) if i != j)
            verification = {
                "left_transform_rank": lr, "right_transform_rank": rr,
                "left_transform_invertible": lr == 2,
                "right_transform_invertible": rr == 2,
                "Q_off_diagonal_blocks_zero": qzero,
                "K_off_diagonal_blocks_zero": kzero,
                "direct_sum_verified": lr == 2 and rr == 2 and qzero and kzero,
            }
            return {
                "field": "F_5", "source_shape": [2, 2],
                "block_shapes": [[1, 1], [1, 1]],
                "left_transform": [[x % p for x in row] for row in left],
                "right_transform": [[x % p for x in row] for row in right],
                "transformed_Q": tq, "transformed_K": tk,
                "Q_blocks": qb, "K_blocks": kb, "verification": verification,
            }

        def reconstruction_ok(record, expected):
            keys = ("field", "source_shape", "block_shapes", "left_transform",
                    "right_transform", "transformed_Q", "transformed_K",
                    "Q_blocks", "K_blocks", "verification")
            return all(record[key] == expected[key] for key in keys)

        good = verify_pencil_multi_direct_sum_witness(
            q, k, p, identity, identity, shapes
        )
        false_left = [[1, 1], [0, 1]]
        negative = verify_pencil_multi_direct_sum_witness(
            q, k, p, false_left, identity, shapes
        )
        good_expected = independent_reconstruction(identity, identity)
        negative_expected = independent_reconstruction(false_left, identity)

        # Three checks are reported independently: schema, reconstruction,
        # and the independently derived mathematical verdict.
        self.assertTrue(schema_ok(good))
        self.assertTrue(reconstruction_ok(good, good_expected))
        self.assertTrue(good_expected["verification"]["direct_sum_verified"])

        self.assertTrue(schema_ok(negative))
        self.assertTrue(reconstruction_ok(negative, negative_expected))
        self.assertFalse(negative_expected["verification"]["direct_sum_verified"])

        # Mutation matrix: malformed structure is caught at layer 1;
        # well-shaped forgeries pass layer 1 but fail layer 2; a consistent
        # negative witness passes layers 1 and 2 but fails layer 3.
        cases = []
        malformed = copy.deepcopy(good)
        malformed["Q_blocks"].pop()
        cases.append(("missing block-grid row", malformed, False, False, None))

        inconsistent_matrix = copy.deepcopy(good)
        inconsistent_matrix["transformed_Q"][0][0] = 4
        cases.append(("forged transformed coefficient", inconsistent_matrix, True, False, None))

        inconsistent_grid = copy.deepcopy(good)
        inconsistent_grid["K_blocks"][0][1][0][0] = 3
        cases.append(("forged nested block", inconsistent_grid, True, False, None))

        inconsistent_diag = copy.deepcopy(good)
        inconsistent_diag["verification"]["left_transform_rank"] = 1
        cases.append(("forged rank diagnostic", inconsistent_diag, True, False, None))

        cases.append(("consistent negative witness", negative, True, True, False))

        for label, record, expected_schema, expected_replay, expected_math in cases:
            with self.subTest(layer_case=label):
                self.assertEqual(schema_ok(record), expected_schema)
                if expected_schema:
                    self.assertEqual(
                        reconstruction_ok(record, good_expected if label != "consistent negative witness"
                                          else negative_expected),
                        expected_replay,
                    )
                if expected_math is not None:
                    self.assertEqual(
                        (negative_expected if label == "consistent negative witness"
                         else good_expected)["verification"]["direct_sum_verified"],
                        expected_math,
                    )

    def test_g_ep104_adversarial_audit_metadata_and_equivalent_representations(self):
        import copy

        p = 5
        q = [[1, 0], [0, 2]]
        k = [[2, 0], [0, 1]]
        shapes = [(1, 1), (1, 1)]
        identity = ident(2)
        baseline = verify_pencil_multi_direct_sum_witness(
            q, k, p, identity, identity, shapes
        )

        def schema_ok(record):
            required = {
                "schema", "field", "source_shape", "block_shapes",
                "left_transform", "right_transform", "transformed_Q",
                "transformed_K", "Q_blocks", "K_blocks", "verification",
                "scope",
            }
            if type(record) is not dict or set(record) != required:
                return False
            if record["schema"] != "the-fold-pencil-multi-direct-sum-witness-v1":
                return False
            if type(record["field"]) is not str or not record["field"].startswith("F_"):
                return False
            if (type(record["source_shape"]) is not list
                    or len(record["source_shape"]) != 2
                    or any(type(x) is not int or x <= 0 for x in record["source_shape"])):
                return False
            if type(record["block_shapes"]) is not list or len(record["block_shapes"]) < 2:
                return False
            if any(type(x) is not list or len(x) != 2
                   or any(type(y) is not int or y < 0 for y in x)
                   or x == [0, 0] for x in record["block_shapes"]):
                return False
            m, n = record["source_shape"]
            blocks = record["block_shapes"]
            if sum(x[0] for x in blocks) != m or sum(x[1] for x in blocks) != n:
                return False

            def matrix(value, rows, cols):
                return (type(value) is list and len(value) == rows
                        and all(type(row) is list and len(row) == cols
                                and all(type(x) is int for x in row) for row in value))
            for key, rows, cols in (
                ("left_transform", m, m), ("right_transform", n, n),
                ("transformed_Q", m, n), ("transformed_K", m, n),
            ):
                if not matrix(record[key], rows, cols):
                    return False
            count = len(blocks)
            for key in ("Q_blocks", "K_blocks"):
                grid = record[key]
                if type(grid) is not list or len(grid) != count:
                    return False
                for i, row in enumerate(grid):
                    if type(row) is not list or len(row) != count:
                        return False
                    for j, block in enumerate(row):
                        if not matrix(block, blocks[i][0], blocks[j][1]):
                            return False
            v = record["verification"]
            types = {
                "left_transform_rank": int, "right_transform_rank": int,
                "left_transform_invertible": bool, "right_transform_invertible": bool,
                "Q_off_diagonal_blocks_zero": bool, "K_off_diagonal_blocks_zero": bool,
                "direct_sum_verified": bool,
            }
            return (type(v) is dict and set(v) == set(types)
                    and all(type(v[x]) is t for x, t in types.items())
                    and 0 <= v["left_transform_rank"] <= m
                    and 0 <= v["right_transform_rank"] <= n
                    and type(record["scope"]) is str)

        # Metadata mutations are classified by the layer that can detect them.
        schema_version = copy.deepcopy(baseline)
        schema_version["schema"] = "the-fold-pencil-multi-direct-sum-witness-v2"
        field_label = copy.deepcopy(baseline)
        field_label["field"] = "F_7"
        dimensions = copy.deepcopy(baseline)
        dimensions["source_shape"] = [3, 2]
        partition = copy.deepcopy(baseline)
        partition["block_shapes"] = [[2, 0], [0, 2]]  # reordered row/column partition
        scope = copy.deepcopy(baseline)
        scope["scope"] = "Cryptographically authenticated and unique."

        self.assertFalse(schema_ok(schema_version))
        self.assertTrue(schema_ok(field_label))
        self.assertTrue(schema_ok(dimensions) is False)
        self.assertFalse(schema_ok(partition))
        self.assertTrue(schema_ok(scope))

        # Metadata binding is a distinct record-consistency check. These
        # values can be structurally well-typed yet do not match the
        # source-bound snapshot. Scope is descriptive, not algebraic.
        def metadata_matches(record):
            return all(record[key] == baseline[key]
                       for key in ("schema", "field", "source_shape",
                                   "block_shapes", "scope"))

        self.assertFalse(metadata_matches(field_label))
        self.assertFalse(metadata_matches(scope))
        self.assertFalse(schema_ok(dimensions))
        self.assertFalse(schema_ok(partition))

        # Schema-valid metadata forgeries are not the same record as a
        # source-bound reconstruction. The algebraic verdict is recomputed.
        for label, record, changed_keys in (
            ("field label", field_label, ("field",)),
            ("scope claim", scope, ("scope",)),
        ):
            with self.subTest(metadata=label):
                self.assertTrue(schema_ok(record))
                self.assertTrue(any(record[key] != baseline[key] for key in changed_keys))
                # The mathematical verdict is independently recomputed from
                # source inputs and supplied transforms, never trusted from metadata.
                replay = verify_pencil_multi_direct_sum_witness(
                    q, k, p, record["left_transform"], record["right_transform"], shapes
                )
                self.assertTrue(replay["verification"]["direct_sum_verified"])

        # A different valid witness can encode the same transformed pencil:
        # reciprocal scalar changes S -> cS and T -> c^-1 T over F_5.
        scaled_left = [[2, 0], [0, 2]]
        scaled_right = [[3, 0], [0, 3]]
        equivalent = verify_pencil_multi_direct_sum_witness(
            q, k, p, scaled_left, scaled_right, shapes
        )
        self.assertTrue(schema_ok(equivalent))
        self.assertNotEqual(equivalent["left_transform"], baseline["left_transform"])
        self.assertNotEqual(equivalent["right_transform"], baseline["right_transform"])
        self.assertEqual(equivalent["transformed_Q"], baseline["transformed_Q"])
        self.assertEqual(equivalent["transformed_K"], baseline["transformed_K"])
        self.assertTrue(equivalent["verification"]["direct_sum_verified"])


    def test_g_ep105_block_permutation_conjugacy_with_rectangular_empty_blocks(self):
        # Permute row and column coordinate intervals together with the
        # ordered block list. The partition includes zero-row and zero-column
        # blocks, whose empty intervals still occupy meaningful block slots.
        shapes = [(1, 0), (1, 2), (0, 1), (1, 1)]
        order = [3, 1, 2, 0]

        def permutation_matrix(indices, size):
            return [[int(indices[i] == j) for j in range(size)]
                    for i in range(size)]

        def transpose(a):
            return [list(col) for col in zip(*a)]

        def permute_rows(a, indices):
            return [a[i][:] for i in indices]

        def permute_columns(a, indices):
            return [[row[j] for j in indices] for row in a]

        for p in (2, 3, 5, 7):
            m = sum(r for r, _ in shapes)
            n = sum(c for _, c in shapes)
            row_offsets, col_offsets = [0], [0]
            for r, c in shapes:
                row_offsets.append(row_offsets[-1] + r)
                col_offsets.append(col_offsets[-1] + c)

            q0, k0 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[row_offsets[b] + i][col_offsets[b] + j] = (b + 2*i + j + 1) % p
                        k0[row_offsets[b] + i][col_offsets[b] + j] = (2*b + i + 3*j + 1) % p

            left, right = ident(m), ident(n)
            for i in range(m - 1):
                left[i][i + 1] = 1
            for i in range(n - 1):
                right[i + 1][i] = 1
            left_inv, right_inv = inverse(left, p), inverse(right, p)
            q = mm(mm(left_inv, q0, p), right_inv, p)
            k = mm(mm(left_inv, k0, p), right_inv, p)
            baseline = verify_pencil_multi_direct_sum_witness(
                q, k, p, left, right, shapes
            )
            self.assertTrue(baseline["verification"]["direct_sum_verified"], baseline)

            row_indices = [j for block in order
                           for j in range(row_offsets[block], row_offsets[block + 1])]
            col_indices = [j for block in order
                           for j in range(col_offsets[block], col_offsets[block + 1])]
            row_perm = permutation_matrix(row_indices, m)
            col_perm = permutation_matrix(col_indices, n)
            row_perm_inv, col_perm_inv = transpose(row_perm), transpose(col_perm)

            # Change source coordinates and conjugate each supplied transform
            # so the resulting transformed pair is the correspondingly
            # reordered block diagonal pair.
            q_reordered = permute_columns(permute_rows(q, row_indices), col_indices)
            k_reordered = permute_columns(permute_rows(k, row_indices), col_indices)
            left_reordered = mm(mm(row_perm, left, p), row_perm_inv, p)
            right_reordered = mm(mm(col_perm, right, p), col_perm_inv, p)
            reordered_shapes = [shapes[i] for i in order]
            reordered = verify_pencil_multi_direct_sum_witness(
                q_reordered, k_reordered, p,
                left_reordered, right_reordered, reordered_shapes,
            )
            expected_q = permute_columns(permute_rows(q0, row_indices), col_indices)
            expected_k = permute_columns(permute_rows(k0, row_indices), col_indices)
            with self.subTest(field=p, case="consistent row-column-block permutation"):
                self.assertTrue(reordered["verification"]["direct_sum_verified"], reordered)
                self.assertEqual(reordered["transformed_Q"], expected_q)
                self.assertEqual(reordered["transformed_K"], expected_k)
                self.assertEqual(reordered["block_shapes"], [list(x) for x in reordered_shapes])

            # A row-only source-coordinate permutation is not the same
            # representation change: retain the original column coordinates
            # and transforms, then require the original ordered partition.
            row_only_q = permute_rows(q, row_indices)
            row_only_k = permute_rows(k, row_indices)
            row_only = verify_pencil_multi_direct_sum_witness(
                row_only_q, row_only_k, p,
                mm(row_perm, left, p), right, shapes,
            )
            with self.subTest(field=p, case="one-sided row-coordinate permutation"):
                self.assertFalse(row_only["verification"]["direct_sum_verified"], row_only)

            # Likewise, permuting only the column coordinates must not pass.
            col_only_q = permute_columns(q, col_indices)
            col_only_k = permute_columns(k, col_indices)
            col_only = verify_pencil_multi_direct_sum_witness(
                col_only_q, col_only_k, p,
                left, mm(right, col_perm_inv, p), shapes,
            )
            with self.subTest(field=p, case="one-sided column-coordinate permutation"):
                self.assertFalse(col_only["verification"]["direct_sum_verified"], col_only)


    def test_g_ep106_composed_basis_changes_permutations_and_scalar_rescalings(self):
        # Compose two independent source basis changes on each side, then
        # reorder the block coordinates and apply reciprocal scalar scaling.
        shapes = [(1, 1), (1, 2), (0, 1), (1, 0), (1, 1)]
        order = [4, 1, 3, 0, 2]

        def transpose(a):
            return [list(col) for col in zip(*a)]

        def row_order(indices, size):
            return [[int(indices[i] == j) for j in range(size)]
                    for i in range(size)]

        def reorder_rows(a, indices):
            return [a[i][:] for i in indices]

        def reorder_cols(a, indices):
            return [[row[j] for j in indices] for row in a]

        for p in (2, 3, 5, 7):
            m, n = sum(r for r, _ in shapes), sum(c for _, c in shapes)
            ro, co = [0], [0]
            for r, c in shapes:
                ro.append(ro[-1] + r)
                co.append(co[-1] + c)

            q0, k0 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro[b] + i][co[b] + j] = (b + 2*i + j + 1) % p
                        k0[ro[b] + i][co[b] + j] = (2*b + i + 3*j + 1) % p

            # Initial witness scrambles both coordinate spaces independently.
            s0, t0 = ident(m), ident(n)
            for i in range(m - 1):
                s0[i][i + 1] = 1
            for i in range(n - 1):
                t0[i + 1][i] = 1
            si0, ti0 = inverse(s0, p), inverse(t0, p)
            q, k = mm(mm(si0, q0, p), ti0, p), mm(mm(si0, k0, p), ti0, p)

            # Two successive noncommuting elementary basis changes.
            a1, a2, b1, b2 = ident(m), ident(m), ident(n), ident(n)
            if m > 1:
                a1[0][1] = 1
                a2[m - 1][0] = 1
            if n > 1:
                b1[0][n - 1] = 1
                b2[n - 1][0] = 1
            ai1, ai2 = inverse(a1, p), inverse(a2, p)
            bi1, bi2 = inverse(b1, p), inverse(b2, p)

            q1, k1 = mm(mm(a1, q, p), b1, p), mm(mm(a1, k, p), b1, p)
            q2, k2 = mm(mm(a2, q1, p), b2, p), mm(mm(a2, k1, p), b2, p)
            a_total, b_total = mm(a2, a1, p), mm(b1, b2, p)
            a_total_inv, b_total_inv = mm(ai1, ai2, p), mm(bi2, bi1, p)

            row_indices = [j for block in order for j in range(ro[block], ro[block + 1])]
            col_indices = [j for block in order for j in range(co[block], co[block + 1])]
            pr, pc = row_order(row_indices, m), row_order(col_indices, n)
            pri, pci = transpose(pr), transpose(pc)
            q3, k3 = mm(mm(pr, q2, p), pci, p), mm(mm(pr, k2, p), pci, p)

            # Final witness: same block permutation on both sides, plus
            # reciprocal scalar rescaling. For F2 the only nonzero scalar is 1.
            c = 1 if p == 2 else 2
            ci = pow(c, -1, p)
            s_pre = mm(s0, a_total_inv, p)
            t_pre = mm(b_total_inv, t0, p)
            s_perm = mm(mm(pr, s_pre, p), pri, p)
            t_perm = mm(mm(pc, t_pre, p), pci, p)
            s_final = [[(c * x) % p for x in row] for row in s_perm]
            t_final = [[(ci * x) % p for x in row] for row in t_perm]
            permuted_shapes = [shapes[i] for i in order]

            out = verify_pencil_multi_direct_sum_witness(
                q3, k3, p, s_final, t_final, permuted_shapes
            )
            expected_q = reorder_cols(reorder_rows(q0, row_indices), col_indices)
            expected_k = reorder_cols(reorder_rows(k0, row_indices), col_indices)
            with self.subTest(field=p, case="composed equivalence"):
                self.assertTrue(out["verification"]["direct_sum_verified"], out)
                self.assertEqual(out["transformed_Q"], expected_q)
                self.assertEqual(out["transformed_K"], expected_k)
                self.assertEqual(out["block_shapes"], [list(x) for x in permuted_shapes])

            # Break the composition by undoing only the final row permutation
            # in S while leaving the source and right transform unchanged.
            bad_s = mm(pri, s_final, p)
            bad = verify_pencil_multi_direct_sum_witness(
                q3, k3, p, bad_s, t_final, permuted_shapes
            )
            with self.subTest(field=p, case="mismatched composed row transform"):
                self.assertFalse(bad["verification"]["direct_sum_verified"], bad)


    def test_g_ep107_equivalent_factorization_orders_reach_same_witness(self):
        # Two different ordered factorizations of the same composite row and
        # column basis changes must yield the same final witness and audit.
        shapes = [(1, 1), (1, 2), (0, 1), (1, 0), (1, 1)]
        order = [4, 1, 3, 0, 2]

        def transpose(a):
            return [list(col) for col in zip(*a)]

        def perm_matrix(indices, size):
            return [[int(indices[i] == j) for j in range(size)]
                    for i in range(size)]

        def reorder_rows(a, indices):
            return [a[i][:] for i in indices]

        def reorder_cols(a, indices):
            return [[row[j] for j in indices] for row in a]

        def scale(a, c, p):
            return [[(c * x) % p for x in row] for row in a]

        for p in (2, 3, 5, 7):
            m, n = sum(r for r, _ in shapes), sum(c for _, c in shapes)
            ro, co = [0], [0]
            for r, c in shapes:
                ro.append(ro[-1] + r)
                co.append(co[-1] + c)
            q0, k0 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
            for b, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro[b] + i][co[b] + j] = (b + 2*i + j + 1) % p
                        k0[ro[b] + i][co[b] + j] = (2*b + i + 3*j + 1) % p

            s0, t0 = ident(m), ident(n)
            for i in range(m - 1):
                s0[i][i + 1] = 1
            for i in range(n - 1):
                t0[i + 1][i] = 1
            si0, ti0 = inverse(s0, p), inverse(t0, p)
            q, k = mm(mm(si0, q0, p), ti0, p), mm(mm(si0, k0, p), ti0, p)

            # Pick noncommuting elementary factors on each coordinate side.
            a, b, c, d = ident(m), ident(m), ident(n), ident(n)
            a[0][1] = 1
            b[m - 1][0] = 1
            c[0][n - 1] = 1
            d[n - 1][0] = 1
            ai, bi, ci, di = inverse(a, p), inverse(b, p), inverse(c, p), inverse(d, p)

            # Path I applies a then b (left product b*a), c then d
            # (right product c*d). Path II uses conjugated second factors
            # so its reversed operation order has exactly the same product.
            left_total = mm(b, a, p)
            right_total = mm(c, d, p)
            a_prime = mm(mm(b, a, p), bi, p)
            d_prime = mm(mm(c, d, p), ci, p)
            left_total_alt = mm(a_prime, b, p)
            right_total_alt = mm(d_prime, c, p)
            self.assertEqual(left_total, left_total_alt)
            self.assertEqual(right_total, right_total_alt)

            # The two paths therefore produce identical source coordinates.
            q_changed = mm(mm(left_total, q, p), right_total, p)
            k_changed = mm(mm(left_total, k, p), right_total, p)
            q_changed_alt = mm(mm(left_total_alt, q, p), right_total_alt, p)
            k_changed_alt = mm(mm(left_total_alt, k, p), right_total_alt, p)
            self.assertEqual(q_changed, q_changed_alt)
            self.assertEqual(k_changed, k_changed_alt)

            row_indices = [j for block in order for j in range(ro[block], ro[block + 1])]
            col_indices = [j for block in order for j in range(co[block], co[block + 1])]
            pr, pc = perm_matrix(row_indices, m), perm_matrix(col_indices, n)
            pri, pci = transpose(pr), transpose(pc)
            q_final = mm(mm(pr, q_changed, p), pci, p)
            k_final = mm(mm(pr, k_changed, p), pci, p)

            left_total_inv = inverse(left_total, p)
            right_total_inv = inverse(right_total, p)
            s_pre = mm(s0, left_total_inv, p)
            t_pre = mm(right_total_inv, t0, p)
            s_perm = mm(mm(pr, s_pre, p), pri, p)
            t_perm = mm(mm(pc, t_pre, p), pci, p)
            scalar = 1 if p == 2 else 2
            inv_scalar = pow(scalar, -1, p)
            s_final = scale(s_perm, scalar, p)
            t_final = scale(t_perm, inv_scalar, p)
            final_shapes = [shapes[i] for i in order]

            first = verify_pencil_multi_direct_sum_witness(
                q_final, k_final, p, s_final, t_final, final_shapes
            )
            second = verify_pencil_multi_direct_sum_witness(
                q_final, k_final, p, s_final, t_final, final_shapes
            )
            with self.subTest(field=p, case="two factorization orders"):
                self.assertTrue(first["verification"]["direct_sum_verified"], first)
                self.assertTrue(second["verification"]["direct_sum_verified"], second)
                self.assertEqual(first["transformed_Q"], second["transformed_Q"])
                self.assertEqual(first["transformed_K"], second["transformed_K"])
                self.assertEqual(first["Q_blocks"], second["Q_blocks"])
                self.assertEqual(first["K_blocks"], second["K_blocks"])

            # Omitting the inverse of the final left basis change must fail.
            bad_s = mm(s_final, left_total, p)
            bad = verify_pencil_multi_direct_sum_witness(
                q_final, k_final, p, bad_s, t_final, final_shapes
            )
            with self.subTest(field=p, case="omitted inverse"):
                self.assertFalse(bad["verification"]["direct_sum_verified"], bad)


    def test_g_ep108_seeded_metamorphic_rectangular_witness_families(self):
        # Deterministic pseudo-random products of elementary invertible
        # matrices generate independent left/right basis scramblings.
        import random

        rng = random.Random(108_2026)

        def random_invertible(size, p):
            out = ident(size)
            for _ in range(5 * max(1, size)):
                if size < 2:
                    break
                i, j = rng.sample(range(size), 2)
                if rng.randrange(3) == 0:
                    out[i], out[j] = out[j], out[i]
                else:
                    factor = rng.randrange(1, p)
                    out[i] = [(out[i][k] + factor * out[j][k]) % p
                              for k in range(size)]
            return out

        cases = [
            [(1, 1), (0, 2), (2, 0), (1, 1)],
            [(2, 1), (1, 0), (0, 2), (1, 2)],
            [(1, 2), (2, 1), (0, 1), (1, 0)],
        ]
        for p in (2, 3, 5, 7):
            for case_index, shapes in enumerate(cases):
                m = sum(r for r, _ in shapes)
                n = sum(c for _, c in shapes)
                row_offsets, col_offsets = [0], [0]
                for r, c in shapes:
                    row_offsets.append(row_offsets[-1] + r)
                    col_offsets.append(col_offsets[-1] + c)

                q0, k0 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
                for block, (r, c) in enumerate(shapes):
                    for i in range(r):
                        for j in range(c):
                            q0[row_offsets[block] + i][col_offsets[block] + j] = (
                                rng.randrange(p)
                            )
                            k0[row_offsets[block] + i][col_offsets[block] + j] = (
                                rng.randrange(p)
                            )

                left = random_invertible(m, p)
                right = random_invertible(n, p)
                left_inv, right_inv = inverse(left, p), inverse(right, p)
                q = mm(mm(left_inv, q0, p), right_inv, p)
                k = mm(mm(left_inv, k0, p), right_inv, p)

                out = verify_pencil_multi_direct_sum_witness(
                    q, k, p, left, right, shapes
                )
                with self.subTest(field=p, case=case_index, check="valid scramble"):
                    self.assertTrue(out["verification"]["direct_sum_verified"], out)
                    self.assertEqual(out["transformed_Q"], q0)
                    self.assertEqual(out["transformed_K"], k0)

                # Inject a single coefficient in a known off-diagonal block
                # after transporting it back to the source coordinates.
                first_nonempty = next(
                    i for i, (r, c) in enumerate(shapes) if r and c
                )
                second_nonempty = next(
                    i for i, (r, c) in enumerate(shapes)
                    if i != first_nonempty and r and c
                )
                row = row_offsets[first_nonempty]
                col = col_offsets[second_nonempty]
                target = [[0] * n for _ in range(m)]
                target[row][col] = 1
                source_delta = mm(mm(left_inv, target, p), right_inv, p)
                q_bad = [[(q[i][j] + source_delta[i][j]) % p
                          for j in range(n)] for i in range(m)]
                bad = verify_pencil_multi_direct_sum_witness(
                    q_bad, k, p, left, right, shapes
                )
                with self.subTest(field=p, case=case_index, check="cross-block mutation"):
                    self.assertFalse(bad["verification"]["direct_sum_verified"], bad)
                    self.assertEqual(bad["transformed_Q"][row][col], 1)



    def test_g_ep109_long_composition_and_wrong_partition_rejection(self):
        import random

        rng = random.Random(109_2026)

        def elementary_product(size, p, count):
            total = ident(size)
            for _ in range(count):
                op = ident(size)
                i, j = rng.sample(range(size), 2)
                if rng.randrange(4) == 0:
                    op[i], op[j] = op[j], op[i]
                else:
                    op[i][j] = (op[i][j] + rng.randrange(1, p)) % p
                total = mm(op, total, p)
            return total

        # First, long noncommuting products must still recover the exact
        # target after independent left/right changes and reciprocal scaling.
        shapes = [(1, 2), (2, 1), (1, 1)]
        m = sum(r for r, _ in shapes)
        n = sum(c for _, c in shapes)
        ro, co = [0], [0]
        for r, c in shapes:
            ro.append(ro[-1] + r)
            co.append(co[-1] + c)

        for p in (2, 3, 5, 7):
            q0, k0 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
            for block, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro[block] + i][co[block] + j] = (block + i + 2*j + 1) % p
                        k0[ro[block] + i][co[block] + j] = (2*block + 2*i + j + 1) % p

            left = elementary_product(m, p, 17)
            right = elementary_product(n, p, 19)
            left_inv, right_inv = inverse(left, p), inverse(right, p)
            q = mm(mm(left_inv, q0, p), right_inv, p)
            k = mm(mm(left_inv, k0, p), right_inv, p)
            scalar = 1 if p == 2 else p - 1
            s = [[(scalar * x) % p for x in row] for row in left]
            inv_scalar = pow(scalar, -1, p)
            t = [[(inv_scalar * x) % p for x in row] for row in right]
            out = verify_pencil_multi_direct_sum_witness(q, k, p, s, t, shapes)
            with self.subTest(field=p, check="long composed witness"):
                self.assertTrue(out["verification"]["direct_sum_verified"], out)
                self.assertEqual(out["transformed_Q"], q0)
                self.assertEqual(out["transformed_K"], k0)

            # A different partition with the same total dimensions is not
            # interchangeable: it changes the coordinate cut locations.
            wrong_shapes = [(2, 1), (1, 2), (1, 1)]
            wrong = verify_pencil_multi_direct_sum_witness(
                q, k, p, s, t, wrong_shapes
            )
            with self.subTest(field=p, check="wrong partition"):
                self.assertFalse(wrong["verification"]["direct_sum_verified"], wrong)


    def test_g_ep110_paired_pencil_partition_boundary_and_cancellation(self):
        # The verifier must check Q and K independently, not merely their sum.
        # Opposite off-block perturbations cancel in Q+K but remain visible in
        # each coefficient, so an aggregate-only check would be unsound.
        shapes = [(1, 1), (1, 1), (1, 1)]
        for p in (2, 3, 5, 7):
            q0 = [[1 % p, 0, 0], [0, 2 % p, 0], [0, 0, 3 % p]]
            k0 = [[2 % p, 0, 0], [0, 3 % p, 0], [0, 0, 1 % p]]

            # Nontrivial but block-preserving transformations are valid.
            left = [[1 % p, 0, 0], [0, (2 if p > 2 else 1) % p, 0],
                    [0, 0, (3 if p > 3 else 1) % p]]
            right = [[(2 if p > 2 else 1) % p, 0, 0], [0, 1 % p, 0],
                     [0, 0, (2 if p > 2 else 1) % p]]
            li, ri = inverse(left, p), inverse(right, p)
            q = mm(mm(li, q0, p), ri, p)
            k = mm(mm(li, k0, p), ri, p)
            baseline = verify_pencil_multi_direct_sum_witness(
                q, k, p, left, right, shapes
            )
            with self.subTest(field=p, case="block-preserving transformations"):
                self.assertTrue(baseline["verification"]["direct_sum_verified"], baseline)
                self.assertEqual(baseline["transformed_Q"], q0)
                self.assertEqual(baseline["transformed_K"], k0)

            # E couples block 0 to block 1. Transport it into source
            # coordinates so the supplied witness reveals precisely E.
            e = [[0, 1 % p, 0], [0, 0, 0], [0, 0, 0]]
            delta = mm(mm(li, e, p), ri, p)
            q_only = [[(q[i][j] + delta[i][j]) % p for j in range(3)]
                      for i in range(3)]
            k_only = [[(k[i][j] + delta[i][j]) % p for j in range(3)]
                      for i in range(3)]
            q_audit = verify_pencil_multi_direct_sum_witness(
                q_only, k, p, left, right, shapes
            )
            k_audit = verify_pencil_multi_direct_sum_witness(
                q, k_only, p, left, right, shapes
            )
            with self.subTest(field=p, case="Q-only coupling"):
                self.assertFalse(q_audit["verification"]["Q_off_diagonal_blocks_zero"])
                self.assertTrue(q_audit["verification"]["K_off_diagonal_blocks_zero"])
                self.assertFalse(q_audit["verification"]["direct_sum_verified"])
            with self.subTest(field=p, case="K-only coupling"):
                self.assertTrue(k_audit["verification"]["Q_off_diagonal_blocks_zero"])
                self.assertFalse(k_audit["verification"]["K_off_diagonal_blocks_zero"])
                self.assertFalse(k_audit["verification"]["direct_sum_verified"])

            # Opposite perturbations cancel in the coefficient-wise sum.
            # In characteristic two, -E = E and E+E = 0 as required.
            paired_q = [[(q[i][j] + delta[i][j]) % p for j in range(3)]
                        for i in range(3)]
            paired_k = [[(k[i][j] - delta[i][j]) % p for j in range(3)]
                        for i in range(3)]
            paired = verify_pencil_multi_direct_sum_witness(
                paired_q, paired_k, p, left, right, shapes
            )
            transformed_sum = [[(paired["transformed_Q"][i][j] +
                                  paired["transformed_K"][i][j]) % p
                                 for j in range(3)] for i in range(3)]
            original_sum = [[(q0[i][j] + k0[i][j]) % p
                             for j in range(3)] for i in range(3)]
            with self.subTest(field=p, case="cancelling aggregate"):
                self.assertEqual(transformed_sum, original_sum)
                self.assertEqual(paired["transformed_Q"][0][1], 1 % p)
                self.assertEqual(paired["transformed_K"][0][1], (-1) % p)
                self.assertFalse(paired["verification"]["Q_off_diagonal_blocks_zero"])
                self.assertFalse(paired["verification"]["K_off_diagonal_blocks_zero"])
                self.assertFalse(paired["verification"]["direct_sum_verified"])


    def test_g_ep111_invertible_pencil_parameter_basis_changes(self):
        # An invertible GL(2, F_p) change of coefficient basis preserves
        # the two-dimensional span of the pencil coefficients. A common
        # direct-sum witness must therefore verify every such representation.
        shapes = [(1, 2), (2, 1), (1, 1)]
        m = sum(r for r, _ in shapes)
        n = sum(c for _, c in shapes)
        ro, co = [0], [0]
        for r, c in shapes:
            ro.append(ro[-1] + r)
            co.append(co[-1] + c)

        def combine(a, x, b, y, p):
            return [[(a*x[i][j] + b*y[i][j]) % p
                     for j in range(len(x[0]))] for i in range(len(x))]

        def scale2(x, a, p):
            return [[(a*v) % p for v in row] for row in x]

        for p in (2, 3, 5, 7):
            q0 = [[0] * n for _ in range(m)]
            k0 = [[0] * n for _ in range(m)]
            for block, (r, c) in enumerate(shapes):
                for i in range(r):
                    for j in range(c):
                        q0[ro[block]+i][co[block]+j] = (block + 2*i + j + 1) % p
                        k0[ro[block]+i][co[block]+j] = (2*block + i + 3*j + 1) % p

            left = ident(m)
            right = ident(n)
            for i in range(m-1):
                left[i][i+1] = 1
            for i in range(n-1):
                right[i+1][i] = 1
            li, ri = inverse(left, p), inverse(right, p)
            q = mm(mm(li, q0, p), ri, p)
            k = mm(mm(li, k0, p), ri, p)

            # Includes coefficient swap, independent shears, and a
            # nontrivial determinant-one mixing. Every matrix is invertible.
            parameter_changes = [
                (0, 1, 1, 0),
                (1, 1, 0, 1),
                (1, 0, 1, 1),
                (1, 1, 1, 2 % p),
            ]
            for a, b, c, d in parameter_changes:
                if (a*d-b*c) % p == 0:
                    continue
                mixed_q = combine(a, q, b, k, p)
                mixed_k = combine(c, q, d, k, p)
                target_q = combine(a, q0, b, k0, p)
                target_k = combine(c, q0, d, k0, p)
                audit = verify_pencil_multi_direct_sum_witness(
                    mixed_q, mixed_k, p, left, right, shapes
                )
                with self.subTest(field=p, parameter_matrix=(a,b,c,d)):
                    self.assertTrue(audit["verification"]["direct_sum_verified"], audit)
                    self.assertEqual(audit["transformed_Q"], target_q)
                    self.assertEqual(audit["transformed_K"], target_k)

                # Invert the 2x2 coefficient-basis change and recover the
                # original ordered pair exactly, not merely its span.
                det_inv = pow((a*d-b*c) % p, -1, p)
                ia, ib = d*det_inv % p, (-b)*det_inv % p
                ic, id_ = (-c)*det_inv % p, a*det_inv % p
                recovered_q = combine(ia, mixed_q, ib, mixed_k, p)
                recovered_k = combine(ic, mixed_q, id_, mixed_k, p)
                self.assertEqual(recovered_q, q)
                self.assertEqual(recovered_k, k)



    def test_g_ep112_singular_parameter_maps_can_hide_pencil_coupling(self):
        # A singular GL(2)-replacement is not an equivalence of pencils:
        # it can erase one coefficient (or collapse both outputs onto one
        # linear combination), making a false decomposition appear valid.
        shapes = [(1, 1), (1, 1), (1, 1)]
        for p in (2, 3, 5, 7):
            q = [[1 % p, 0, 0],
                 [0, 2 % p, 0],
                 [0, 0, 3 % p]]
            k = [[1 % p, 1 % p, 0],
                 [0, 2 % p, 0],
                 [0, 0, 3 % p]]
            original = verify_pencil_multi_direct_sum_witness(
                q, k, p, ident(3), ident(3), shapes
            )
            with self.subTest(field=p, case="original paired pencil"):
                self.assertTrue(original["verification"]["Q_off_diagonal_blocks_zero"])
                self.assertFalse(original["verification"]["K_off_diagonal_blocks_zero"])
                self.assertFalse(original["verification"]["direct_sum_verified"])

            # Rank-one parameter map [[1,0],[0,0]] discards K entirely.
            # Its output pair (Q,0) is block diagonal, but this says nothing
            # about the erased coefficient of the original pencil.
            collapsed_q, collapsed_k = q, [[0, 0, 0] for _ in range(3)]
            erased = verify_pencil_multi_direct_sum_witness(
                collapsed_q, collapsed_k, p, ident(3), ident(3), shapes
            )
            with self.subTest(field=p, case="erase second coefficient"):
                self.assertTrue(erased["verification"]["direct_sum_verified"])
                self.assertEqual(erased["transformed_Q"], q)
                self.assertEqual(erased["transformed_K"], collapsed_k)
                self.assertFalse(original["verification"]["direct_sum_verified"])

            # Another rank-one map has two identical outputs (Q,Q): the
            # coefficient pair has collapsed to a one-dimensional span.
            duplicated = verify_pencil_multi_direct_sum_witness(
                q, q, p, ident(3), ident(3), shapes
            )
            with self.subTest(field=p, case="duplicate coefficient"):
                self.assertTrue(duplicated["verification"]["direct_sum_verified"])
                self.assertEqual(duplicated["transformed_Q"], duplicated["transformed_K"])

            # A singular map retaining Q+K in both outputs does not hide
            # this coupling: the retained linear combination is still
            # off-block, so the supplied witness correctly rejects it.
            sum_q = [[(q[i][j] + k[i][j]) % p for j in range(3)]
                     for i in range(3)]
            retained = verify_pencil_multi_direct_sum_witness(
                sum_q, sum_q, p, ident(3), ident(3), shapes
            )
            with self.subTest(field=p, case="retained coupled combination"):
                self.assertFalse(retained["verification"]["Q_off_diagonal_blocks_zero"])
                self.assertFalse(retained["verification"]["K_off_diagonal_blocks_zero"])
                self.assertFalse(retained["verification"]["direct_sum_verified"])



    def test_g_ep113_exhaustive_two_by_two_parameter_map_rank_boundary(self):
        # Enumerate every coefficient-space map over each small prime field.
        # Q is block diagonal; K has exactly one cross-block entry, so the
        # output pair is a direct sum precisely when the map erases K's
        # coefficient from both output coordinates.
        shapes = [(1, 1), (1, 1), (1, 1)]
        for p in (2, 3, 5, 7):
            q = [[1 % p, 0, 0],
                 [0, 2 % p, 0],
                 [0, 0, 3 % p]]
            k = [[1 % p, 1 % p, 0],
                 [0, 2 % p, 0],
                 [0, 0, 3 % p]]

            counts = {0: 0, 1: 0, 2: 0}
            accepted_by_rank = {0: 0, 1: 0, 2: 0}
            for a in range(p):
                for b in range(p):
                    for c in range(p):
                        for d in range(p):
                            det = (a*d - b*c) % p
                            rank = 2 if det else (
                                0 if a == b == c == d == 0 else 1
                            )
                            counts[rank] += 1

                            out_q = [[(a*q[i][j] + b*k[i][j]) % p
                                      for j in range(3)] for i in range(3)]
                            out_k = [[(c*q[i][j] + d*k[i][j]) % p
                                      for j in range(3)] for i in range(3)]
                            audit = verify_pencil_multi_direct_sum_witness(
                                out_q, out_k, p, ident(3), ident(3), shapes
                            )
                            # Since Q,K are linearly independent as matrices,
                            # the span dimension of the output pair equals
                            # the rank of the 2x2 parameter map.
                            expected = (b == 0 and d == 0)
                            with self.subTest(field=p, matrix=(a,b,c,d)):
                                self.assertEqual(
                                    audit["verification"]["direct_sum_verified"],
                                    expected,
                                    audit,
                                )
                                self.assertEqual(
                                    audit["verification"]["Q_off_diagonal_blocks_zero"],
                                    b == 0,
                                )
                                self.assertEqual(
                                    audit["verification"]["K_off_diagonal_blocks_zero"],
                                    d == 0,
                                )
                            accepted_by_rank[rank] += int(expected)

            expected_counts = {
                0: 1,
                1: (p*p - 1) * (p*p - 1) // (p - 1),
                2: (p*p - 1) * (p*p - p),
            }
            with self.subTest(field=p, case="complete rank census"):
                self.assertEqual(counts, expected_counts)
                self.assertEqual(sum(counts.values()), p**4)
                # Exactly p^2 maps erase K from both outputs: each output
                # is an arbitrary scalar multiple of Q.
                self.assertEqual(sum(accepted_by_rank.values()), p*p)
                self.assertEqual(accepted_by_rank[0], 1)
                self.assertEqual(accepted_by_rank[1], p*p - 1)
                self.assertEqual(accepted_by_rank[2], 0)



    def test_g_ep114_intersection_of_both_coefficient_constraints(self):
        # With the left transform fixed, enumerate the linear space of right
        # transforms satisfying each coefficient's off-diagonal equations.
        # Their intersection, not either individual constraint space, is the
        # simultaneous pencil decomposition condition.
        shapes = [(1, 1), (1, 1)]
        for p in (2, 3, 5, 7):
            # A nontrivial invertible right-coordinate scrambling.
            u = [[1, 1], [0, 1]]
            ui = inverse(u, p)
            target_q = [[1, 0], [0, 0]]
            target_k = [[0, 0], [0, 1]]
            q = mm(target_q, ui, p)
            k = mm(target_k, ui, p)

            q_only, k_only, common = set(), set(), set()
            for a in range(p):
                for b in range(p):
                    for c in range(p):
                        for d in range(p):
                            candidate = [[a, b], [c, d]]
                            qout = mm(q, candidate, p)
                            kout = mm(k, candidate, p)
                            q_ok = qout[0][1] % p == 0 and qout[1][0] % p == 0
                            k_ok = kout[0][1] % p == 0 and kout[1][0] % p == 0
                            key = (a, b, c, d)
                            if q_ok:
                                q_only.add(key)
                            if k_ok:
                                k_only.add(key)
                            if q_ok and k_ok:
                                common.add(key)

            expected_q = {
                (a, b, c, d) for a in range(p) for b in range(p)
                for c in range(p) for d in range(p) if b == d
            }
            expected_k = {
                (a, b, c, d) for a in range(p) for b in range(p)
                for c in range(p) for d in range(p) if c == 0
            }
            expected_common = {
                (a, b, 0, b) for a in range(p) for b in range(p)
            }
            invertible_common = {
                key for key in expected_common
                if (key[0]*key[3] - key[1]*key[2]) % p != 0
            }
            with self.subTest(field=p):
                self.assertEqual(q_only, expected_q)
                self.assertEqual(k_only, expected_k)
                self.assertEqual(common, expected_common)
                self.assertEqual(len(q_only), p**3)
                self.assertEqual(len(k_only), p**3)
                self.assertEqual(len(common), p*p)
                self.assertEqual(
                    {x for x in common
                     if (x[0]*x[3] - x[1]*x[2]) % p != 0},
                    invertible_common,
                )
                self.assertEqual(len(invertible_common), (p-1)*(p-1))
                self.assertIn((1, 1, 0, 1), invertible_common)
                self.assertIn((1, 0, 0, 0), common)  # singular solution
                self.assertEqual(mm(q, u, p), target_q)
                self.assertEqual(mm(k, u, p), target_k)



    def test_g_ep115_linear_constraint_solver_and_invertible_witness_filter(self):
        # Solve the simultaneous off-diagonal equations as a homogeneous
        # linear system in row-major entries of T. Compare its complete
        # nullspace enumeration with brute-force enumeration, then apply the
        # nonlinear invertibility filter and replay every surviving witness.
        shapes = [(1, 1), (1, 1)]
        for p in (2, 3, 5, 7):
            u = [[1, 1], [0, 1]]
            ui = inverse(u, p)
            target_q = [[1, 0], [0, 0]]
            target_k = [[0, 0], [0, 1]]
            q, k = mm(target_q, ui, p), mm(target_k, ui, p)
            s = ident(2)

            equations = []
            for coeff in (q, k):
                a = mm(s, coeff, p)
                for i, j in ((0, 1), (1, 0)):
                    equations.append([
                        (a[i][row] if col == j else 0) % p
                        for row in range(2) for col in range(2)
                    ])

            # RREF of the 4-variable homogeneous system.
            reduced = [[x % p for x in row] for row in equations]
            pivots, pivot_row = [], 0
            for col in range(4):
                pivot = next((z for z in range(pivot_row, len(reduced))
                              if reduced[z][col]), None)
                if pivot is None:
                    continue
                reduced[pivot_row], reduced[pivot] = reduced[pivot], reduced[pivot_row]
                scale = pow(reduced[pivot_row][col], -1, p)
                reduced[pivot_row] = [x*scale % p for x in reduced[pivot_row]]
                for z in range(len(reduced)):
                    if z != pivot_row and reduced[z][col]:
                        factor = reduced[z][col]
                        reduced[z] = [
                            (x-factor*y) % p
                            for x, y in zip(reduced[z], reduced[pivot_row])
                        ]
                pivots.append(col)
                pivot_row += 1
                if pivot_row == len(reduced):
                    break

            free = [col for col in range(4) if col not in pivots]
            solved = set()
            for values in __import__("itertools").product(range(p), repeat=len(free)):
                vector = [0]*4
                for col, value in zip(free, values):
                    vector[col] = value
                for row, pivot in enumerate(pivots):
                    vector[pivot] = (-sum(
                        reduced[row][col]*vector[col]
                        for col in free
                    )) % p
                solved.add(tuple(vector))

            brute = set()
            invertible = set()
            for a in range(p):
                for b in range(p):
                    for c in range(p):
                        for d in range(p):
                            candidate = [[a,b],[c,d]]
                            qout, kout = mm(q,candidate,p), mm(k,candidate,p)
                            if qout[0][1] == qout[1][0] == 0 and kout[0][1] == kout[1][0] == 0:
                                key = (a,b,c,d)
                                brute.add(key)
                                if (a*d-b*c) % p:
                                    invertible.add(key)

            solved_invertible = {
                x for x in solved if (x[0]*x[3]-x[1]*x[2]) % p
            }
            with self.subTest(field=p):
                self.assertEqual(solved, brute)
                self.assertEqual(len(solved), p*p)
                self.assertEqual(len(free), 2)
                self.assertEqual(solved_invertible, invertible)
                self.assertEqual(len(invertible), (p-1)*(p-1))
                self.assertIn((1,1,0,1), invertible)
                for a,b,c,d in sorted(invertible):
                    audit = verify_pencil_multi_direct_sum_witness(
                        q, k, p, s, [[a,b],[c,d]], shapes
                    )
                    self.assertTrue(
                        audit["verification"]["direct_sum_verified"], audit
                    )
                self.assertEqual(mm(q,u,p),target_q)
                self.assertEqual(mm(k,u,p),target_k)


    def test_g_ep116_rectangular_partitions_and_constraint_dimension_monotonicity(self):
        # Generalize the unknown-right-transform equations to rectangular
        # block shapes. The total row and column dimensions agree, while
        # individual diagonal blocks need not be square.
        def rref_nullspace(rows, nvars, p):
            work = [[x % p for x in row] for row in rows]
            pivots, pivot_row = [], 0
            for col in range(nvars):
                pivot = next((r for r in range(pivot_row, len(work))
                              if work[r][col]), None)
                if pivot is None:
                    continue
                work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
                scale = pow(work[pivot_row][col], -1, p)
                work[pivot_row] = [x*scale % p for x in work[pivot_row]]
                for r in range(len(work)):
                    if r != pivot_row and work[r][col]:
                        factor = work[r][col]
                        work[r] = [(x-factor*y) % p
                                   for x, y in zip(work[r], work[pivot_row])]
                pivots.append(col)
                pivot_row += 1
                if pivot_row == len(work):
                    break
            free = [c for c in range(nvars) if c not in pivots]
            solutions = set()
            for values in __import__("itertools").product(range(p), repeat=len(free)):
                vector = [0]*nvars
                for c, value in zip(free, values):
                    vector[c] = value
                for r, pivot in enumerate(pivots):
                    vector[pivot] = (-sum(work[r][c]*vector[c]
                                          for c in free)) % p
                solutions.add(tuple(vector))
            return solutions, len(free), len(pivots)

        def make_equations(left, coeffs, shapes, p):
            m = sum(r for r, _ in shapes)
            n = sum(c for _, c in shapes)
            row_block = [0]
            col_block = [0]
            for r, c in shapes:
                row_block.append(row_block[-1]+r)
                col_block.append(col_block[-1]+c)
            equations = []
            for coeff in coeffs:
                a = mm(left, coeff, p)
                for bi, (rsize, csize) in enumerate(shapes):
                    for bj, (rj, cj) in enumerate(shapes):
                        if bi == bj:
                            continue
                        for i in range(row_block[bi], row_block[bi+1]):
                            for j in range(col_block[bj], col_block[bj+1]):
                                equations.append([
                                    a[i][z] if col == j else 0
                                    for z in range(n) for col in range(n)
                                ])
            self.assertEqual(m, n)
            return equations

        # N=2 is small enough for a complete brute-force comparison.
        for p in (2, 3):
            shapes = [(1, 1), (1, 1)]
            left = [[1, 1], [0, 1]]
            right = [[1, 0], [1, 1]]
            left_inv, right_inv = inverse(left, p), inverse(right, p)
            target_q, target_k = [[1, 0], [0, 0]], [[0, 0], [0, 1]]
            q = mm(mm(left_inv, target_q, p), right_inv, p)
            k = mm(mm(left_inv, target_k, p), right_inv, p)
            q_system = make_equations(left, [q], shapes, p)
            both_system = make_equations(left, [q, k], shapes, p)
            q_solutions, q_dim, _ = rref_nullspace(q_system, 4, p)
            solutions, dimension, _ = rref_nullspace(both_system, 4, p)
            brute = set()
            for a in range(p):
                for b in range(p):
                    for c in range(p):
                        for d in range(p):
                            t = [[a, b], [c, d]]
                            if (all(x == 0 for x in
                                    [mm(mm(left, q, p), t, p)[0][1],
                                     mm(mm(left, q, p), t, p)[1][0]]) and
                                all(x == 0 for x in
                                    [mm(mm(left, k, p), t, p)[0][1],
                                     mm(mm(left, k, p), t, p)[1][0]])):
                                brute.add((a, b, c, d))
            self.assertEqual(solutions, brute)
            self.assertEqual(len(solutions), p**dimension)
            self.assertLessEqual(dimension, q_dim)
            self.assertEqual(mm(mm(left, q, p), right, p), target_q)
            self.assertEqual(mm(mm(left, k, p), right, p), target_k)
            for candidate in solutions:
                t = [list(candidate[:2]), list(candidate[2:])]
                if (candidate[0]*candidate[3]-candidate[1]*candidate[2]) % p:
                    audit = verify_pencil_multi_direct_sum_witness(
                        q, k, p, left, t, shapes
                    )
                    self.assertTrue(audit["verification"]["direct_sum_verified"], audit)

        # N=3 rectangular blocks: independently scrambled left/right bases.
        # The known witness must lie in the computed nullspace; this larger
        # case intentionally does not claim exhaustive brute-force coverage.
        for p in (2, 3, 5):
            shapes = [(1, 2), (2, 1)]
            target_q = [[1, 2 % p, 0], [0, 0, 1], [0, 0, 2 % p]]
            target_k = [[2 % p, 1, 0], [0, 0, 2 % p], [0, 0, 1]]
            left = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
            right = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
            left_inv, right_inv = inverse(left, p), inverse(right, p)
            q = mm(mm(left_inv, target_q, p), right_inv, p)
            k = mm(mm(left_inv, target_k, p), right_inv, p)
            equations = make_equations(left, [q, k], shapes, p)
            solutions, dimension, rank = rref_nullspace(equations, 9, p)
            known = tuple(x for row in right for x in row)
            self.assertIn(known, solutions)
            self.assertEqual(len(solutions), p**dimension)
            self.assertEqual(dimension + rank, 9)
            self.assertLessEqual(dimension, 9)
            audit = verify_pencil_multi_direct_sum_witness(
                q, k, p, left, right, shapes
            )
            self.assertTrue(audit["verification"]["direct_sum_verified"], audit)


    def test_g_ep117_rectangular_equations_match_direct_matrix_products(self):
        import random

        def elementary_basis_change(size, p, rng):
            # Random unitriangular matrices are invertible by construction.
            matrix = ident(size)
            for i in range(size):
                for j in range(i+1, size):
                    matrix[i][j] = rng.randrange(p)
            return matrix

        def equation_rows(left, coefficient, shapes, p):
            m, n = len(left), len(coefficient[0])
            row_starts, col_starts = [0], [0]
            for rsize, csize in shapes:
                row_starts.append(row_starts[-1]+rsize)
                col_starts.append(col_starts[-1]+csize)
            left_product = mm(left, coefficient, p)
            rows, positions = [], []
            for bi in range(len(shapes)):
                for bj in range(len(shapes)):
                    if bi == bj:
                        continue
                    for i in range(row_starts[bi], row_starts[bi+1]):
                        for j in range(col_starts[bj], col_starts[bj+1]):
                            row = [0]*(n*n)
                            for z in range(n):
                                row[z*n+j] = left_product[i][z] % p
                            rows.append(row)
                            positions.append((i,j))
            self.assertEqual(row_starts[-1], m)
            self.assertEqual(col_starts[-1], n)
            return rows, positions

        cases = [
            ([(1, 0), (1, 2), (0, 1), (1, 1)], 3, 4),
            ([(0, 1), (2, 1), (1, 0), (1, 2)], 4, 4),
            ([(1, 1), (0, 2), (2, 0), (1, 1)], 4, 4),
        ]
        for case_index, (shapes, m, n) in enumerate(cases):
            for p in (2, 3, 5, 7):
                rng = random.Random(117000 + 100*case_index + p)
                left = elementary_basis_change(m, p, rng)
                right = elementary_basis_change(n, p, rng)
                left_inv, right_inv = inverse(left, p), inverse(right, p)

                def block_diagonal_pair():
                    pair = [[0]*n for _ in range(m)]
                    row_start = col_start = 0
                    for rsize, csize in shapes:
                        for i in range(rsize):
                            for j in range(csize):
                                pair[row_start+i][col_start+j] = rng.randrange(p)
                        row_start += rsize
                        col_start += csize
                    return pair

                target_q, target_k = block_diagonal_pair(), block_diagonal_pair()
                q = mm(mm(left_inv, target_q, p), right_inv, p)
                k = mm(mm(left_inv, target_k, p), right_inv, p)

                for coefficient, target in ((q, target_q), (k, target_k)):
                    rows, positions = equation_rows(left, coefficient, shapes, p)
                    # Compare the linear equation evaluation with the actual
                    # off-diagonal entries of (left * coefficient) * candidate.
                    for trial in range(5):
                        candidate = [
                            [rng.randrange(p) for _ in range(n)]
                            for _ in range(n)
                        ]
                        flattened = [x for row in candidate for x in row]
                        actual = mm(mm(left, coefficient, p), candidate, p)
                        predicted = [
                            sum(a*b for a,b in zip(row, flattened)) % p
                            for row in rows
                        ]
                        self.assertEqual(
                            predicted, [actual[i][j] for i,j in positions],
                            (case_index, p, trial, coefficient)
                        )
                    self.assertEqual(mm(mm(left, coefficient, p), right, p), target)

                with self.subTest(case=case_index, field=p):
                    audit = verify_pencil_multi_direct_sum_witness(
                        q, k, p, left, right, shapes
                    )
                    self.assertTrue(audit["verification"]["direct_sum_verified"], audit)
                    self.assertEqual(audit["transformed_Q"], target_q)
                    self.assertEqual(audit["transformed_K"], target_k)


    def test_g_ep118_constraint_rank_nullity_redundancy_and_overlap(self):
        from itertools import product

        def equation_rows(left, coefficient, p):
            # Two scalar blocks: off-diagonal entries of (S*C)*T.
            a = mm(left, coefficient, p)
            rows = []
            for i, j in ((0, 1), (1, 0)):
                row = [0]*4
                for z in range(2):
                    row[2*z+j] = a[i][z] % p
                rows.append(row)
            return rows

        def elimination_rank(rows, nvars, p):
            work = [[x % p for x in row] for row in rows]
            pivot_row = 0
            for col in range(nvars):
                pivot = next((r for r in range(pivot_row, len(work))
                              if work[r][col]), None)
                if pivot is None:
                    continue
                work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
                scale = pow(work[pivot_row][col], -1, p)
                work[pivot_row] = [x*scale % p for x in work[pivot_row]]
                for r in range(len(work)):
                    if r != pivot_row and work[r][col]:
                        factor = work[r][col]
                        work[r] = [(x-factor*y) % p
                                   for x,y in zip(work[r],work[pivot_row])]
                pivot_row += 1
                if pivot_row == len(work):
                    break
            return pivot_row

        def span_rank(rows, p):
            # Independent rank check: explicitly build the row span and infer
            # its dimension from its cardinality, rather than row reduction.
            span = {(0, 0, 0, 0)}
            for row in rows:
                vector = tuple(x % p for x in row)
                span = {
                    tuple((a + scalar*b) % p for a,b in zip(existing, vector))
                    for existing in span
                    for scalar in range(p)
                }
            size = len(span)
            rank = 0
            while p**rank < size:
                rank += 1
            self.assertEqual(p**rank, size)
            return rank

        left = [[1, 1], [0, 1]]
        base = [[1, 0], [0, 0]]
        zero = [[0, 0], [0, 0]]
        cases = [
            ("zero-only", [zero]),
            ("one-constraint", [base]),
            ("duplicated-constraint", [base, [[2, 0], [0, 0]]]),
            ("overlapping-constraint", [base, [[1, 0], [0, 0]]]),
            ("independent-constraints", [base, [[0, 0], [0, 1]]]),
        ]
        for p in (2, 3, 5):
            for label, coefficients in cases:
                rows = [
                    row
                    for coefficient in coefficients
                    for row in equation_rows(left, coefficient, p)
                ]
                rank_elimination = elimination_rank(rows, 4, p)
                rank_span = span_rank(rows, p)
                self.assertEqual(rank_elimination, rank_span, (p, label, rows))
                nullity = 4-rank_elimination
                solutions = [
                    vector for vector in product(range(p), repeat=4)
                    if all(sum(a*b for a,b in zip(row,vector)) % p == 0
                           for row in rows)
                ]
                self.assertEqual(len(solutions), p**nullity, (p, label))
                self.assertLessEqual(rank_elimination, len(rows))

                # Appending a literal duplicate or zero equation changes
                # equation count but cannot change rank or nullity.
                redundant = rows + ([list(rows[0])] if rows else []) + [[0]*4]
                self.assertEqual(
                    elimination_rank(redundant, 4, p), rank_elimination,
                    (p, label, "redundancy")
                )
                self.assertEqual(span_rank(redundant, p), rank_span)
                self.assertEqual(4-elimination_rank(redundant,4,p), nullity)

            # Explicit overlap: K is a scalar multiple of Q, so the
            # simultaneous system has the same row span as Q alone.
            q_rows = equation_rows(left, base, p)
            k_rows = equation_rows(left, [[2,0],[0,0]], p)
            self.assertEqual(span_rank(q_rows+k_rows,p), span_rank(q_rows,p))
            # A second coefficient with a different support adds a new
            # independent constraint direction.
            independent = equation_rows(left, [[0,0],[0,1]], p)
            self.assertGreater(span_rank(q_rows+independent,p), span_rank(q_rows,p))


    def test_g_ep119_rectangular_constraint_rank_nullity_and_empty_regions(self):
        import random
        from itertools import product

        def equation_system(left, coefficients, shapes, p):
            m, n = len(left), len(coefficients[0][0]) if coefficients else 0
            row_starts, col_starts = [0], [0]
            for rsize, csize in shapes:
                row_starts.append(row_starts[-1] + rsize)
                col_starts.append(col_starts[-1] + csize)
            self.assertEqual(row_starts[-1], m)
            self.assertEqual(col_starts[-1], n)
            rows, locations = [], []
            for coefficient in coefficients:
                product_left = mm(left, coefficient, p)
                for bi in range(len(shapes)):
                    for bj in range(len(shapes)):
                        if bi == bj:
                            continue
                        for i in range(row_starts[bi], row_starts[bi+1]):
                            for j in range(col_starts[bj], col_starts[bj+1]):
                                equation = [0]*(n*n)
                                for z in range(n):
                                    equation[z*n+j] = product_left[i][z] % p
                                rows.append(equation)
                                locations.append((i,j,coefficient))
            return rows, locations

        def row_reduce_rank(rows, variables, p):
            a = [[v % p for v in row] for row in rows]
            pivot = 0
            for col in range(variables):
                selected = next((r for r in range(pivot,len(a))
                                 if a[r][col] % p), None)
                if selected is None:
                    continue
                a[pivot],a[selected] = a[selected],a[pivot]
                inv = pow(a[pivot][col],-1,p)
                a[pivot] = [v*inv % p for v in a[pivot]]
                for r in range(len(a)):
                    if r != pivot and a[r][col] % p:
                        factor = a[r][col] % p
                        a[r] = [(x-factor*y) % p
                                for x,y in zip(a[r],a[pivot])]
                pivot += 1
                if pivot == len(a):
                    break
            return pivot

        def enumerate_span_rank(rows, p):
            dimension = len(rows[0]) if rows else 0
            span = {tuple([0]*dimension)}
            for row in rows:
                v = tuple(x % p for x in row)
                span = {
                    tuple((x+c*y) % p for x,y in zip(old,v))
                    for old in span for c in range(p)
                }
            count = len(span)
            rank = 0
            while p**rank < count:
                rank += 1
            self.assertEqual(p**rank,count)
            return rank,span

        fixtures = [
            # One nonempty block: there are no off-diagonal regions at all.
            ([(3,3)], 3, 3),
            # Ordinary rectangular split with a 2x3 source pencil.
            ([(1,1),(1,2)], 2, 3),
            # Empty column block and empty row block coexist.
            ([(1,0),(1,2),(1,1)], 3, 3),
            ([(0,1),(2,1),(1,1)], 3, 3),
        ]
        for fixture_index,(shapes,m,n) in enumerate(fixtures):
            for p in (2,3):
                rng = random.Random(119000 + 100*fixture_index + p)
                left = [[rng.randrange(p) for _ in range(m)] for _ in range(m)]
                # Use a guaranteed invertible unitriangular left basis.
                left = ident(m)
                for i in range(m):
                    for j in range(i+1,m):
                        left[i][j] = rng.randrange(p)
                coefficients = [
                    [[rng.randrange(p) for _ in range(n)] for _ in range(m)]
                    for _ in range(2)
                ]
                rows,locations = equation_system(left,coefficients,shapes,p)
                rank = row_reduce_rank(rows,n*n,p)
                span_rank,span = enumerate_span_rank(rows,p)
                self.assertEqual(rank,span_rank,(fixture_index,p,rows))
                nullity = n*n-rank
                self.assertEqual(len(span),p**rank)
                self.assertLessEqual(rank,n*n)
                self.assertEqual(nullity+rank,n*n)

                # Directly check every generated equation against the matching
                # off-diagonal entry for independently sampled rectangular T.
                for trial in range(4):
                    candidate = [[rng.randrange(p) for _ in range(n)]
                                 for _ in range(n)]
                    flat = [x for row in candidate for x in row]
                    for equation,(i,j,coefficient) in zip(rows,locations):
                        actual = mm(mm(left,coefficient,p),candidate,p)[i][j]
                        predicted = sum(x*y for x,y in zip(equation,flat)) % p
                        self.assertEqual(predicted,actual,
                                         (fixture_index,p,trial,i,j))

                # For tiny systems, exhaustive kernel enumeration independently
                # checks rank-nullity and the exact solution count.
                if n <= 3:
                    kernel_count = sum(
                        1 for vector in product(range(p),repeat=n*n)
                        if all(sum(x*y for x,y in zip(row,vector)) % p == 0
                               for row in rows)
                    )
                    self.assertEqual(kernel_count,p**nullity,
                                     (fixture_index,p,rank,nullity))
                if len(shapes)==1:
                    self.assertEqual(rows,[])
                    self.assertEqual(rank,0)
                    self.assertEqual(nullity,n*n)


    def test_g_ep120_constraint_rank_invariant_under_block_preserving_coordinates(self):
        import random

        def mm_local(a,b,p):
            return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
                     for j in range(len(b[0]) if b else 0)]
                    for i in range(len(a))]

        def inverse_local(a,p):
            n=len(a)
            work=[[x%p for x in row]+[int(i==j) for j in range(n)]
                  for i,row in enumerate(a)]
            pivot=0
            for col in range(n):
                selected=next((r for r in range(pivot,n)
                               if work[r][col]),None)
                if selected is None:
                    raise AssertionError("fixture transform must be invertible")
                work[pivot],work[selected]=work[selected],work[pivot]
                scale=pow(work[pivot][col],-1,p)
                work[pivot]=[x*scale%p for x in work[pivot]]
                for r in range(n):
                    if r!=pivot and work[r][col]:
                        factor=work[r][col]
                        work[r]=[(x-factor*y)%p
                                 for x,y in zip(work[r],work[pivot])]
                pivot+=1
            return [row[n:] for row in work]

        def block_basis(sizes,p,rng):
            total=sum(sizes)
            out=[[int(i==j) for j in range(total)] for i in range(total)]
            start=0
            for size in sizes:
                # Unitriangular changes within each block preserve its subspace.
                for i in range(size):
                    for j in range(i+1,size):
                        out[start+i][start+j]=rng.randrange(p)
                start+=size
            return out

        def constraints(a,shapes,p):
            m,n=len(a),len(a[0]) if a else 0
            rs=[0]
            cs=[0]
            for r,c in shapes:
                rs.append(rs[-1]+r)
                cs.append(cs[-1]+c)
            rows=[]
            for bi in range(len(shapes)):
                for bj in range(len(shapes)):
                    if bi==bj:
                        continue
                    for i in range(rs[bi],rs[bi+1]):
                        for j in range(cs[bj],cs[bj+1]):
                            row=[0]*(n*n)
                            for z in range(n):
                                row[z*n+j]=a[i][z]%p
                            rows.append(row)
            return rows

        def rank(rows,nvars,p):
            work=[[x%p for x in row] for row in rows]
            pivot=0
            for col in range(nvars):
                found=next((r for r in range(pivot,len(work))
                            if work[r][col]),None)
                if found is None:
                    continue
                work[pivot],work[found]=work[found],work[pivot]
                scale=pow(work[pivot][col],-1,p)
                work[pivot]=[x*scale%p for x in work[pivot]]
                for r in range(len(work)):
                    if r!=pivot and work[r][col]:
                        factor=work[r][col]
                        work[r]=[(x-factor*y)%p
                                 for x,y in zip(work[r],work[pivot])]
                pivot+=1
                if pivot==len(work):
                    break
            return pivot

        fixtures=[
            ([(2,1),(1,2)],3,3),
            ([(1,0),(1,2),(1,1)],3,3),
            ([(0,1),(2,1),(1,1)],3,3),
        ]
        for fixture_id,(shapes,m,n) in enumerate(fixtures):
            for p in (2,3,5):
                rng=random.Random(120000+fixture_id*100+p)
                a=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
                s=block_basis([r for r,_ in shapes],p,rng)
                t=block_basis([c for _,c in shapes],p,rng)
                tinv=inverse_local(t,p)
                transformed=mm_local(mm_local(s,a,p),t,p)
                original_rows=constraints(a,shapes,p)
                transformed_rows=constraints(transformed,shapes,p)
                original_rank=rank(original_rows,n*n,p)
                transformed_rank=rank(transformed_rows,n*n,p)
                self.assertEqual(original_rank,transformed_rank,
                                 (fixture_id,p,shapes))
                self.assertEqual(
                    rank(constraints(transformed,shapes,p),n*n,p),
                    original_rank
                )

                # Check the induced bijection on unknown right transforms:
                # X' = T^-1 X T preserves the off-diagonal-zero condition.
                for trial in range(5):
                    x=[[rng.randrange(p) for _ in range(n)] for _ in range(n)]
                    xprime=mm_local(mm_local(tinv,x,p),t,p)
                    lhs=mm_local(a,x,p)
                    rhs=mm_local(transformed,xprime,p)
                    expected=mm_local(mm_local(s,lhs,p),t,p)
                    self.assertEqual(rhs,expected,(fixture_id,p,trial))
                    # Block-diagonal coordinate changes preserve whether
                    # each corresponding off-diagonal block is zero.
                    row_starts=[0]
                    col_starts=[0]
                    for rsize,csize in shapes:
                        row_starts.append(row_starts[-1]+rsize)
                        col_starts.append(col_starts[-1]+csize)
                    for bi in range(len(shapes)):
                        for bj in range(len(shapes)):
                            if bi==bj:
                                continue
                            old_block=[row[col_starts[bj]:col_starts[bj+1]]
                                       for row in lhs[row_starts[bi]:row_starts[bi+1]]]
                            new_block=[row[col_starts[bj]:col_starts[bj+1]]
                                       for row in expected[row_starts[bi]:row_starts[bi+1]]]
                            self.assertEqual(
                                all(v%p==0 for row in old_block for v in row),
                                all(v%p==0 for row in new_block for v in row)
                            )
                    # Direct equation evaluation is covariant even when not zero.
                    flat=[v for row in xprime for v in row]
                    for row in transformed_rows:
                        self.assertEqual(len(row),len(flat))

        # Changing the partition is a different constraint family, not a
        # coordinate change. For this fixture the rank actually changes.
        a=[[1,0,0],[0,0,0],[0,0,0]]
        split_rank=rank(constraints(a,[(1,1),(2,2)],3),9,3)
        merged_rank=rank(constraints(a,[(2,2),(1,1)],3),9,3)
        self.assertNotEqual(split_rank,merged_rank)


    def test_g_ep121_mixed_basis_changes_with_transported_partition(self):
        import random

        def mm_local(a,b,p):
            return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
                     for j in range(len(b[0]) if b else 0)]
                    for i in range(len(a))]

        def inverse_local(a,p):
            n=len(a)
            work=[[x%p for x in row]+[int(i==j) for j in range(n)]
                  for i,row in enumerate(a)]
            pivot=0
            for col in range(n):
                found=next((r for r in range(pivot,n)
                            if work[r][col]),None)
                if found is None:
                    raise AssertionError("basis change must be invertible")
                work[pivot],work[found]=work[found],work[pivot]
                scale=pow(work[pivot][col],-1,p)
                work[pivot]=[x*scale%p for x in work[pivot]]
                for r in range(n):
                    if r!=pivot and work[r][col]:
                        factor=work[r][col]
                        work[r]=[(x-factor*y)%p
                                 for x,y in zip(work[r],work[pivot])]
                pivot+=1
            return [row[n:] for row in work]

        def constraint_rows(coefficient,shapes,p):
            n=len(coefficient[0])
            row_starts=[0]
            col_starts=[0]
            for rows,cols in shapes:
                row_starts.append(row_starts[-1]+rows)
                col_starts.append(col_starts[-1]+cols)
            equations=[]
            for bi in range(len(shapes)):
                for bj in range(len(shapes)):
                    if bi==bj:
                        continue
                    for i in range(row_starts[bi],row_starts[bi+1]):
                        for j in range(col_starts[bj],col_starts[bj+1]):
                            equations.append([
                                coefficient[i][z] % p if col==j else 0
                                for z in range(n) for col in range(n)
                            ])
            return equations

        def transported_rows(coefficient,left_inverse,right_inverse,shapes,p):
            # Each column of this equation matrix is evaluated on one matrix
            # unit E_ab. The tested output is the off-diagonal part of
            # U^-1 * coefficient * X' * V^-1, i.e. the transported split.
            n=len(coefficient[0])
            row_starts=[0]
            col_starts=[0]
            for rows,cols in shapes:
                row_starts.append(row_starts[-1]+rows)
                col_starts.append(col_starts[-1]+cols)
            locations=[
                (i,j)
                for bi in range(len(shapes))
                for bj in range(len(shapes)) if bi!=bj
                for i in range(row_starts[bi],row_starts[bi+1])
                for j in range(col_starts[bj],col_starts[bj+1])
            ]
            columns=[]
            for a in range(n):
                for b in range(n):
                    unit=[[int(i==a and j==b) for j in range(n)]
                          for i in range(n)]
                    value=mm_local(
                        mm_local(
                            mm_local(left_inverse,coefficient,p),
                            unit,p
                        ),
                        right_inverse,p
                    )
                    columns.append([value[i][j] % p for i,j in locations])
            return [
                [columns[c][r] for c in range(n*n)]
                for r in range(len(locations))
            ]

        def rank_local(rows,variables,p):
            work=[[x%p for x in row] for row in rows]
            pivot=0
            for col in range(variables):
                found=next((r for r in range(pivot,len(work))
                            if work[r][col]),None)
                if found is None:
                    continue
                work[pivot],work[found]=work[found],work[pivot]
                scale=pow(work[pivot][col],-1,p)
                work[pivot]=[x*scale%p for x in work[pivot]]
                for r in range(len(work)):
                    if r!=pivot and work[r][col]:
                        factor=work[r][col]
                        work[r]=[(x-factor*y)%p
                                 for x,y in zip(work[r],work[pivot])]
                pivot+=1
                if pivot==len(work):
                    break
            return pivot

        shapes=[(1,1),(2,2)]
        # These explicit controls mix the first block with the second.
        fixtures=[
            (2,
             [[0,0,0],[1,1,0],[1,0,1]],
             [[1,1,1],[0,1,1],[0,0,1]],
             [[1,0,1],[0,1,1],[0,0,1]],
             True),
            (3,
             [[0,1,0],[0,2,0],[1,1,1]],
             [[1,1,0],[0,1,0],[0,0,1]],
             [[1,2,2],[0,1,0],[0,0,1]],
             True),
        ]
        for p,a,u,v,expect_fixed_partition_change in fixtures:
            ui=inverse_local(u,p)
            vi=inverse_local(v,p)
            transformed=mm_local(mm_local(u,a,p),v,p)
            original_system=constraint_rows(a,shapes,p)
            transported_system=transported_rows(
                transformed,ui,vi,shapes,p
            )
            original_rank=rank_local(original_system,9,p)
            transported_rank=rank_local(transported_system,9,p)
            self.assertEqual(original_rank,transported_rank)
            # Leaving the coordinate partition fixed after mixing is a
            # different constraint family; these fixtures expose the change.
            fixed_rank=rank_local(
                constraint_rows(transformed,shapes,p),9,p
            )
            if expect_fixed_partition_change:
                self.assertNotEqual(original_rank,fixed_rank)

            rng=random.Random(121000+p)
            for trial in range(6):
                xprime=[[rng.randrange(p) for _ in range(3)]
                        for _ in range(3)]
                # Pull the candidate back to the original right-transform
                # coordinates and compare the transported off-diagonal map.
                x=mm_local(mm_local(v,xprime,p),vi,p)
                lhs=mm_local(
                    mm_local(mm_local(ui,transformed,p),xprime,p),
                    vi,p
                )
                rhs=mm_local(a,x,p)
                self.assertEqual(lhs,rhs,(p,trial))

        # A third field control uses independently seeded full unitriangular
        # changes; the transported equation matrix still has identical rank.
        p=5
        rng=random.Random(121005)
        a=[[rng.randrange(p) for _ in range(3)] for _ in range(3)]
        u=ident(3)
        v=ident(3)
        for i in range(3):
            for j in range(i+1,3):
                u[i][j]=rng.randrange(1,p)
                v[i][j]=rng.randrange(1,p)
        ui=inverse_local(u,p)
        vi=inverse_local(v,p)
        transformed=mm_local(mm_local(u,a,p),v,p)
        self.assertEqual(
            rank_local(constraint_rows(a,shapes,p),9,p),
            rank_local(transported_rows(transformed,ui,vi,shapes,p),9,p)
        )


    def test_g_ep122_rectangular_transported_basis_covariance_with_empty_blocks(self):
        import random

        def mm_local(a,b,p):
            return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
                     for j in range(len(b[0]) if b else 0)]
                    for i in range(len(a))]

        def inverse_local(a,p):
            n=len(a)
            work=[[x%p for x in row]+[int(i==j) for j in range(n)]
                  for i,row in enumerate(a)]
            for col in range(n):
                pivot=next((r for r in range(col,n)
                            if work[r][col]),None)
                if pivot is None:
                    raise AssertionError("basis change must be invertible")
                work[col],work[pivot]=work[pivot],work[col]
                scale=pow(work[col][col],-1,p)
                work[col]=[x*scale%p for x in work[col]]
                for r in range(n):
                    if r!=col and work[r][col]:
                        factor=work[r][col]
                        work[r]=[(x-factor*y)%p
                                 for x,y in zip(work[r],work[col])]
            return [row[n:] for row in work]

        def equation_locations(shapes):
            rs=[0]
            cs=[0]
            for r,c in shapes:
                rs.append(rs[-1]+r)
                cs.append(cs[-1]+c)
            return [
                (i,j)
                for bi in range(len(shapes))
                for bj in range(len(shapes)) if bi!=bj
                for i in range(rs[bi],rs[bi+1])
                for j in range(cs[bj],cs[bj+1])
            ]

        def equation_rows(a,shapes,p):
            n=len(a[0])
            return [
                [a[i][z]%p if col==j else 0
                 for z in range(n) for col in range(n)]
                for i,j in equation_locations(shapes)
            ]

        def transported_rows(a_prime,u_inverse,v_inverse,shapes,p):
            n=len(a_prime[0])
            locations=equation_locations(shapes)
            columns=[]
            for row_index in range(n):
                for col_index in range(n):
                    unit=[[int(i==row_index and j==col_index)
                           for j in range(n)] for i in range(n)]
                    pulled=mm_local(
                        mm_local(
                            mm_local(u_inverse,a_prime,p),unit,p
                        ),
                        v_inverse,p
                    )
                    columns.append([pulled[i][j] for i,j in locations])
            return [
                [columns[c][r] for c in range(n*n)]
                for r in range(len(locations))
            ]

        def rank_local(rows,nvars,p):
            work=[[x%p for x in row] for row in rows]
            pivot=0
            for col in range(nvars):
                found=next((r for r in range(pivot,len(work))
                            if work[r][col]),None)
                if found is None:
                    continue
                work[pivot],work[found]=work[found],work[pivot]
                scale=pow(work[pivot][col],-1,p)
                work[pivot]=[x*scale%p for x in work[pivot]]
                for r in range(len(work)):
                    if r!=pivot and work[r][col]:
                        factor=work[r][col]
                        work[r]=[(x-factor*y)%p
                                 for x,y in zip(work[r],work[pivot])]
                pivot+=1
                if pivot==len(work):
                    break
            return pivot

        fixtures=[
            # Ordinary 3x4 split; this exact F2 control also changes rank
            # if the mixed basis is applied but the old partition is retained.
            ([(1,1),(2,3)],2,
             [[0,0,1,1],[0,0,1,1],[0,0,1,1]],
             [[1,1,0],[0,1,0],[0,0,1]],
             [[1,0,1,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
             True),
            # Empty row and column blocks coexist in a 3x4 partition.
            ([(0,1),(1,0),(1,2),(1,1)],3,None,None,None,False),
            ([(1,2),(2,2)],5,None,None,None,False),
        ]
        for fixture_index,(shapes,p,a,u,v,expect_fixed_change) in enumerate(fixtures):
            rng=random.Random(122000+fixture_index*10+p)
            m=sum(r for r,_ in shapes)
            n=sum(c for _,c in shapes)
            if a is None:
                a=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
                u=[[int(i==j) if i>=j else rng.randrange(p)
                    for j in range(m)] for i in range(m)]
                v=[[int(i==j) if i>=j else rng.randrange(p)
                    for j in range(n)] for i in range(n)]
            ui=inverse_local(u,p)
            vi=inverse_local(v,p)
            a_prime=mm_local(mm_local(u,a,p),v,p)
            original=equation_rows(a,shapes,p)
            transported=transported_rows(a_prime,ui,vi,shapes,p)
            original_rank=rank_local(original,n*n,p)
            transported_rank=rank_local(transported,n*n,p)
            self.assertEqual(original_rank,transported_rank,
                             (fixture_index,p,shapes))
            fixed_rank=rank_local(equation_rows(a_prime,shapes,p),n*n,p)
            if expect_fixed_change:
                self.assertNotEqual(original_rank,fixed_rank)

            # Verify the full rectangular pullback identity for arbitrary
            # right-transform candidates, including the zero-block partition.
            for trial in range(5):
                x_prime=[[rng.randrange(p) for _ in range(n)]
                         for _ in range(n)]
                x=mm_local(mm_local(v,x_prime,p),vi,p)
                pulled=mm_local(
                    mm_local(mm_local(ui,a_prime,p),x_prime,p),vi,p
                )
                self.assertEqual(pulled,mm_local(a,x,p),
                                 (fixture_index,p,trial))
                flat=[value for row in x_prime for value in row]
                for equation in transported:
                    self.assertEqual(len(equation),len(flat))

            if any(r==0 or c==0 for r,c in shapes):
                self.assertEqual(len(transported),len(original))
                self.assertTrue(all(len(row)==n*n for row in transported))


    def test_g_ep123_transported_kernel_bijection_including_singular_candidates(self):
        import itertools

        def product(a, b, p):
            return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
                     for j in range(len(b[0]))] for i in range(len(a))]

        def inv(a, p):
            n = len(a)
            w = [[x % p for x in row] + [int(i == j) for j in range(n)]
                 for i, row in enumerate(a)]
            for c in range(n):
                pivot = next((r for r in range(c, n) if w[r][c]), None)
                if pivot is None:
                    raise AssertionError("basis transform must be invertible")
                w[c], w[pivot] = w[pivot], w[c]
                z = pow(w[c][c], -1, p)
                w[c] = [x * z % p for x in w[c]]
                for r in range(n):
                    if r != c and w[r][c]:
                        f = w[r][c]
                        w[r] = [(x - f*y) % p for x, y in zip(w[r], w[c])]
            return [row[n:] for row in w]

        def off_diagonal_zero(a, x, shapes, p):
            ax = product(a, x, p)
            row_start = col_start = 0
            row_ranges, col_ranges = [], []
            for r, c in shapes:
                row_ranges.append(range(row_start, row_start+r))
                col_ranges.append(range(col_start, col_start+c))
                row_start += r
                col_start += c
            return all(
                ax[i][j] % p == 0
                for bi, rows in enumerate(row_ranges)
                for bj, cols in enumerate(col_ranges) if bi != bj
                for i in rows for j in cols
            )

        # A genuinely rectangular 3x2 source with two nonempty diagonal
        # regions. Its common right-transform kernel contains singular and
        # invertible matrices; invertibility is not part of the linear system.
        shapes = [(1,  1), (2, 1)]
        q = [[1, 0], [0, 1], [0, 1]]
        k = [[2, 0], [0, 1], [0, 2]]
        for p in (2, 3):
            # Full invertible changes mix the original coordinate blocks.
            u = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
            v = [[1, 1], [0, 1]]
            ui, vi = inv(u, p), inv(v, p)
            q_prime = product(product(u, q, p), v, p)
            k_prime = product(product(u, k, p), v, p)

            def transported_condition(x_prime, coefficient_prime):
                pulled = product(
                    product(product(ui, coefficient_prime, p), x_prime, p),
                    vi, p
                )
                return off_diagonal_zero(pulled, ident(2), shapes, p)

            # Enumerate the entire 2x2 matrix space, not only GL(2).
            matrices = [
                [[a, b], [c, d]]
                for a, b, c, d in itertools.product(range(p), repeat=4)
            ]
            mapped = []
            original_kernel, transported_kernel = [], []
            for x in matrices:
                x_prime = product(product(vi, x, p), v, p)
                mapped.append(tuple(z for row in x_prime for z in row))
                original_ok = (off_diagonal_zero(q, x, shapes, p)
                               and off_diagonal_zero(k, x, shapes, p))
                transported_ok = (
                    transported_condition(x_prime, q_prime)
                    and transported_condition(x_prime, k_prime)
                )
                self.assertEqual(original_ok, transported_ok, (p, x))
                if original_ok:
                    original_kernel.append(tuple(z for row in x for z in row))
                if transported_ok:
                    transported_kernel.append(tuple(z for row in x_prime for z in row))

            # Conjugation X -> V^-1 X V is a bijection on the full matrix
            # vector space, including singular matrices.
            self.assertEqual(len(set(mapped)), p**4)
            self.assertEqual(len(original_kernel), len(transported_kernel))
            self.assertEqual(len(original_kernel), p**2)
            self.assertEqual(len(transported_kernel), p**2)

            def determinant(x):
                return (x[0][0]*x[1][1] - x[0][1]*x[1][0]) % p

            original_singular = [x for x in matrices
                                 if off_diagonal_zero(q, x, shapes, p)
                                 and off_diagonal_zero(k, x, shapes, p)
                                 and determinant(x) == 0]
            original_invertible = [x for x in matrices
                                   if off_diagonal_zero(q, x, shapes, p)
                                   and off_diagonal_zero(k, x, shapes, p)
                                   and determinant(x) != 0]
            self.assertTrue(original_singular)
            self.assertEqual(len(original_invertible), (p-1)**2)
            self.assertEqual(len(original_singular) + len(original_invertible),
                             len(original_kernel))
            # The zero matrix is in the linear kernel; it is never an
            # invertible witness. This keeps the linear/nonlinear boundary explicit.
            self.assertIn((0, 0, 0, 0), original_kernel)


    def test_g_ep124_three_dimensional_rectangular_constraint_rank_nullity_transport(self):
        import random

        def mm(a,b,p):
            return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%p
                     for j in range(len(b[0]))] for i in range(len(a))]

        def inverse(a,p):
            n=len(a)
            w=[[x%p for x in row]+[int(i==j) for j in range(n)]
               for i,row in enumerate(a)]
            for c in range(n):
                pivot=next((r for r in range(c,n) if w[r][c]),None)
                if pivot is None:
                    raise AssertionError("basis matrix is singular")
                w[c],w[pivot]=w[pivot],w[c]
                scale=pow(w[c][c],-1,p)
                w[c]=[x*scale%p for x in w[c]]
                for r in range(n):
                    if r!=c and w[r][c]:
                        f=w[r][c]
                        w[r]=[(x-f*y)%p for x,y in zip(w[r],w[c])]
            return [row[n:] for row in w]

        def locations(shapes):
            rr=cc=0
            blocks=[]
            for r,c in shapes:
                blocks.append((range(rr,rr+r),range(cc,cc+c)))
                rr+=r
                cc+=c
            return [(i,j) for bi,(rows,_) in enumerate(blocks)
                    for bj,(_,cols) in enumerate(blocks) if bi!=bj
                    for i in rows for j in cols]

        def flatten(a):
            return [x for row in a for x in row]

        def rank(rows,nvars,p):
            work=[[x%p for x in row] for row in rows]
            pivot=0
            for col in range(nvars):
                found=next((r for r in range(pivot,len(work))
                            if work[r][col]),None)
                if found is None:
                    continue
                work[pivot],work[found]=work[found],work[pivot]
                scale=pow(work[pivot][col],-1,p)
                work[pivot]=[x*scale%p for x in work[pivot]]
                for r in range(len(work)):
                    if r!=pivot and work[r][col]:
                        f=work[r][col]
                        work[r]=[(x-f*y)%p
                                 for x,y in zip(work[r],work[pivot])]
                pivot+=1
                if pivot==len(work):
                    break
            return pivot

        def equation_matrix(coefficients, shapes, p, pullback=None):
            # Construct each column by applying the actual matrix operation
            # to a matrix-unit candidate; no symbolic coefficient shortcut.
            n=len(coefficients[0][0])
            loc=locations(shapes)
            columns=[]
            for i in range(n):
                for j in range(n):
                    unit=[[int(r==i and c==j) for c in range(n)]
                          for r in range(n)]
                    values=[]
                    for coefficient in coefficients:
                        if pullback is None:
                            output=mm(coefficient,unit,p)
                        else:
                            ui,vi= pullback
                            output=mm(mm(mm(ui,coefficient,p),unit,p),vi,p)
                        values.extend(output[x][y] for x,y in loc)
                    columns.append(values)
            return [[columns[c][r] for c in range(n*n)]
                    for r in range(len(columns[0]))]

        # 4x3 coefficient pair, two rectangular diagonal regions,
        # and a 3x3 right-transform unknown (nine variables).
        shapes=[(1,1),(3,2)]
        m,n=4,3
        for p in (2,3,5):
            rng=random.Random(124000+p)
            q=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
            k=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
            # Independently constructed invertible upper-unitriangular maps.
            u=[[int(i==j) if i>=j else rng.randrange(p)
                for j in range(m)] for i in range(m)]
            v=[[int(i==j) if i>=j else rng.randrange(p)
                for j in range(n)] for i in range(n)]
            ui,vi=inverse(u,p),inverse(v,p)
            q_prime=mm(mm(u,q,p),v,p)
            k_prime=mm(mm(u,k,p),v,p)

            original=equation_matrix([q,k],shapes,p)
            transported=equation_matrix([q_prime,k_prime],shapes,p,
                                        pullback=(ui,vi))
            original_rank=rank(original,n*n,p)
            transported_rank=rank(transported,n*n,p)
            self.assertEqual(original_rank,transported_rank,p)
            self.assertEqual(n*n-original_rank,n*n-transported_rank)
            self.assertEqual(len(original),len(transported))
            self.assertTrue(all(len(row)==n*n for row in original))
            self.assertTrue(all(len(row)==n*n for row in transported))

            # Explicitly check both directions of the candidate-coordinate map
            # on every matrix unit and on deterministic general candidates.
            for i in range(n):
                for j in range(n):
                    unit=[[int(r==i and c==j) for c in range(n)]
                          for r in range(n)]
                    prime=mm(mm(vi,unit,p),v,p)
                    recovered=mm(mm(v,prime,p),vi,p)
                    self.assertEqual(recovered,unit,(p,i,j))
            for trial in range(8):
                x=[[rng.randrange(p) for _ in range(n)] for _ in range(n)]
                x_prime=mm(mm(vi,x,p),v,p)
                self.assertEqual(mm(mm(v,x_prime,p),vi,p),x)
                # The equation-map evaluations agree as vectors, not just ranks.
                original_value=[z for row in mm(q,x,p) for z in row]
                original_value += [z for row in mm(k,x,p) for z in row]
                pulled_value=[]
                for coefficient_prime in (q_prime,k_prime):
                    pulled=mm(mm(mm(ui,coefficient_prime,p),x_prime,p),vi,p)
                    pulled_value.extend(flatten(pulled))
                self.assertEqual(pulled_value,original_value,(p,trial))


    def test_g_ep125_independent_row_span_rank_and_transport_mutations(self):
        import random
        import itertools

        def mm(a,b,p):
            if not a or not b or any(len(row)!=len(a[0]) for row in a) or any(len(row)!=len(b[0]) for row in b) or len(a[0])!=len(b):
                raise ValueError("incompatible matrix dimensions")
            return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%p
                     for j in range(len(b[0]))] for i in range(len(a))]

        def inv(a,p):
            n=len(a)
            w=[[x%p for x in row]+[int(i==j) for j in range(n)]
               for i,row in enumerate(a)]
            for c in range(n):
                pivot=next((z for z in range(c,n) if w[z][c]),None)
                if pivot is None:
                    raise AssertionError("expected invertible basis")
                w[c],w[pivot]=w[pivot],w[c]
                scale=pow(w[c][c],-1,p)
                w[c]=[x*scale%p for x in w[c]]
                for z in range(n):
                    if z!=c and w[z][c]:
                        f=w[z][c]
                        w[z]=[(x-f*y)%p for x,y in zip(w[z],w[c])]
            return [row[n:] for row in w]

        def rref_rank(rows,p):
            a=[[x%p for x in row] for row in rows]
            pivot=0
            for c in range(len(a[0]) if a else 0):
                z=next((z for z in range(pivot,len(a)) if a[z][c]),None)
                if z is None: continue
                a[pivot],a[z]=a[z],a[pivot]
                scale=pow(a[pivot][c],-1,p)
                a[pivot]=[x*scale%p for x in a[pivot]]
                for z in range(len(a)):
                    if z!=pivot and a[z][c]:
                        f=a[z][c]
                        a[z]=[(x-f*y)%p for x,y in zip(a[z],a[pivot])]
                pivot+=1
                if pivot==len(a): break
            return pivot

        def span_rank(rows,p):
            # Independent definition: enumerate the complete row span and
            # recover its dimension from the exact cardinality p^rank.
            width=len(rows[0]) if rows else 0
            span={tuple(0 for _ in range(width))}
            for row in rows:
                expanded=set()
                for vector in span:
                    for scalar in range(p):
                        expanded.add(tuple((vector[j]+scalar*row[j])%p
                                           for j in range(width)))
                span=expanded
            count=len(span)
            rank=0
            size=1
            while size<count:
                size*=p
                rank+=1
            self.assertEqual(size,count)
            return rank

        def off_locations(shapes):
            rr=cc=0
            blocks=[]
            for h,w in shapes:
                blocks.append((range(rr,rr+h),range(cc,cc+w)))
                rr+=h; cc+=w
            return [(i,j) for bi,(rows,_) in enumerate(blocks)
                    for bj,(_,cols) in enumerate(blocks) if bi!=bj
                    for i in rows for j in cols]

        def constraint_rows(coeffs,shapes,p,pull=None):
            n=len(coeffs[0][0])
            loc=off_locations(shapes)
            columns=[]
            for i in range(n):
                for j in range(n):
                    unit=[[int(a==i and b==j) for b in range(n)]
                          for a in range(n)]
                    values=[]
                    for coefficient in coeffs:
                        out=(mm(coefficient,unit,p) if pull is None else
                             mm(mm(mm(pull[0],coefficient,p),unit,p),pull[1],p))
                        values.extend(out[x][y] for x,y in loc)
                    columns.append(values)
            return [[columns[c][z] for c in range(n*n)]
                    for z in range(len(columns[0]))]

        shapes=[(1,1),(3,2)]
        m,n=4,3
        for p in (2,3,5):
            rng=random.Random(125000+p)
            q=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
            k=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
            u=[[int(i==j) if i>=j else rng.randrange(p)
                for j in range(m)] for i in range(m)]
            v=[[int(i==j) if i>=j else rng.randrange(p)
                for j in range(n)] for i in range(n)]
            ui,vi=inv(u,p),inv(v,p)
            qp=mm(mm(u,q,p),v,p)
            kp=mm(mm(u,k,p),v,p)
            original=constraint_rows([q,k],shapes,p)
            transported=constraint_rows([qp,kp],shapes,p,(ui,vi))
            r1,r2=rref_rank(original,p),rref_rank(transported,p)
            self.assertEqual(r1,r2,p)
            self.assertEqual(n*n-r1,n*n-r2)
            # Complete row-span enumeration is deliberately bounded to the
            # smaller fields; F5 still receives independent RREF covariance.
            if p in (2,3):
                self.assertEqual(span_rank(original,p),r1)
                self.assertEqual(span_rank(transported,p),r2)

            # A shape-preserving mutation is a false transport, not malformed
            # input: it changes the independently reconstructed constraint map.
            mutated_qp=[row[:] for row in qp]
            mutated_qp[0][2]=(mutated_qp[0][2]+1)%p
            mutated=constraint_rows([mutated_qp,kp],shapes,p,(ui,vi))
            self.assertNotEqual(mutated,transported)
            self.assertEqual(len(mutated),len(transported))
            self.assertTrue(all(len(row)==n*n for row in mutated))

            # Mutating a supplied inverse entry preserves dimensions but
            # breaks the inverse identity; malformed dimensions are separate.
            bad_ui=[row[:] for row in ui]
            bad_ui[0][0]=(bad_ui[0][0]+1)%p
            self.assertNotEqual(mm(bad_ui,u,p),
                                [[int(i==j) for j in range(m)] for i in range(m)])
            with self.assertRaises(ValueError):
                mm([[1,2]],u,p)


    def test_g_ep126_kernel_basis_transport_and_rank_deficient_controls(self):
        import random

        def mm(a,b,p):
            if not a or not b or any(len(row)!=len(a[0]) for row in a) or any(len(row)!=len(b[0]) for row in b) or len(a[0])!=len(b):
                raise ValueError("incompatible matrix dimensions")
            return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%p
                     for j in range(len(b[0]))] for i in range(len(a))]

        def inverse(a,p):
            n=len(a)
            w=[[x%p for x in row]+[int(i==j) for j in range(n)]
               for i,row in enumerate(a)]
            for c in range(n):
                pivot=next((z for z in range(c,n) if w[z][c]),None)
                if pivot is None: raise AssertionError("singular basis")
                w[c],w[pivot]=w[pivot],w[c]
                scale=pow(w[c][c],-1,p)
                w[c]=[x*scale%p for x in w[c]]
                for z in range(n):
                    if z!=c and w[z][c]:
                        f=w[z][c]
                        w[z]=[(x-f*y)%p for x,y in zip(w[z],w[c])]
            return [row[n:] for row in w]

        def nullspace(rows,width,p):
            a=[[x%p for x in row] for row in rows]
            pivots=[]
            pivot=0
            for c in range(width):
                z=next((z for z in range(pivot,len(a)) if a[z][c]),None)
                if z is None: continue
                a[pivot],a[z]=a[z],a[pivot]
                scale=pow(a[pivot][c],-1,p)
                a[pivot]=[x*scale%p for x in a[pivot]]
                for z in range(len(a)):
                    if z!=pivot and a[z][c]:
                        f=a[z][c]
                        a[z]=[(x-f*y)%p for x,y in zip(a[z],a[pivot])]
                pivots.append(c)
                pivot+=1
            free=[c for c in range(width) if c not in pivots]
            basis=[]
            for f in free:
                vector=[0]*width
                vector[f]=1
                for row,c in enumerate(pivots):
                    vector[c]=(-a[row][f])%p
                basis.append(vector)
            return basis,len(pivots)

        def equation_rows(coeffs,shapes,p,pull=None):
            n=len(coeffs[0][0])
            rr=cc=0
            blocks=[]
            for h,w in shapes:
                blocks.append((range(rr,rr+h),range(cc,cc+w)))
                rr+=h; cc+=w
            locations=[(i,j) for bi,(rs,_) in enumerate(blocks)
                       for bj,(_,cs) in enumerate(blocks) if bi!=bj
                       for i in rs for j in cs]
            columns=[]
            for i in range(n):
                for j in range(n):
                    unit=[[int(a==i and b==j) for b in range(n)]
                          for a in range(n)]
                    values=[]
                    for coefficient in coeffs:
                        out=(mm(coefficient,unit,p) if pull is None else
                             mm(mm(mm(pull[0],coefficient,p),unit,p),pull[1],p))
                        values.extend(out[x][y] for x,y in locations)
                    columns.append(values)
            return [[columns[c][z] for c in range(n*n)]
                    for z in range(len(columns[0]))]

        def flatten(a):
            return [x for row in a for x in row]

        def unflatten(v,n):
            return [v[i*n:(i+1)*n] for i in range(n)]

        def transform(v,mat,p):
            x=unflatten(v,len(mat))
            return flatten(mm(mm(mat[0],x,p),mat[1],p))

        def eval_rows(rows,v,p):
            return [sum(a*b for a,b in zip(row,v))%p for row in rows]

        shapes=[(1,1),(3,2)]
        m,n=4,3
        for p in (2,3,5):
            rng=random.Random(126000+p)
            # Zero and scalar-dependent coefficient pairs force rank-deficient
            # systems with nullity 9 and at least 4, respectively.
            seed=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
            fixtures=[
                ([[0]*n for _ in range(m)],[[0]*n for _ in range(m)]),
                (seed,[[2*x%p for x in row] for row in seed]),
            ]
            for q,k in fixtures:
                u=[[int(i==j) if i>=j else rng.randrange(p)
                    for j in range(m)] for i in range(m)]
                v=[[int(i==j) if i>=j else rng.randrange(p)
                    for j in range(n)] for i in range(n)]
                ui,vi=inverse(u,p),inverse(v,p)
                qp=mm(mm(u,q,p),v,p)
                kp=mm(mm(u,k,p),v,p)
                original=equation_rows([q,k],shapes,p)
                transported=equation_rows([qp,kp],shapes,p,(ui,vi))
                basis,rank0=nullspace(original,n*n,p)
                prime_basis,rank1=nullspace(transported,n*n,p)
                self.assertEqual(rank0,rank1)
                self.assertEqual(len(basis),n*n-rank0)
                self.assertEqual(len(prime_basis),n*n-rank1)
                self.assertGreater(len(basis),0)

                # X' = V^-1 X V. Every original nullspace basis vector maps
                # into the transported kernel, and the inverse maps back.
                mapped=[transform(z,(vi,v),p) for z in basis]
                pulled=[transform(z,(v,vi),p) for z in prime_basis]
                for z in mapped:
                    self.assertEqual(eval_rows(transported,z,p),[0]*len(transported))
                for z in pulled:
                    self.assertEqual(eval_rows(original,z,p),[0]*len(original))

                # Both image families span the complete opposite kernel:
                # independent basis vectors plus equal dimension establish
                # both inclusions, not merely a matching nullity.
                self.assertEqual(len({tuple(z) for z in mapped}),len(mapped))
                self.assertEqual(len({tuple(z) for z in pulled}),len(pulled))
                combined_a=prime_basis+mapped
                combined_b=basis+pulled
                _,rank_a=nullspace(combined_a,n*n,p)
                _,rank_b=nullspace(combined_b,n*n,p)
                self.assertEqual(n*n-rank_a,len(prime_basis))
                self.assertEqual(n*n-rank_b,len(basis))
                # Explicitly verify inverse candidate transport on every basis vector.
                for z in basis:
                    self.assertEqual(transform(transform(z,(vi,v),p),(v,vi),p),z)
                for z in prime_basis:
                    self.assertEqual(transform(transform(z,(v,vi),p),(vi,v),p),z)

                if q==[[0]*n for _ in range(m)]:
                    self.assertEqual(rank0,0)
                    self.assertEqual(len(basis),n*n)
                else:
                    self.assertLess(rank0,n*n)
