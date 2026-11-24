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
        q0 = [[1, 0], [0, 2]]
        k0 = [[1, 0], [0, 2]]
        for p in (2, 3, 5, 7):
            # Use a nontrivial but invertible left transform; right is
            # independently invertible as well.
            s = [[1, 1], [0, 1]]
            t = [[1, 0], [1, 1]]
            si, ti = inverse(s, p), inverse(t, p)
            q = mm(mm(si, q0, p), ti, p)
            k = mm(mm(si, k0, p), ti, p)

            for label, source_q, expected in (
                ("valid", q, None),
                ("false", [[q[0][0]+1, q[0][1]], q[1][:]], False),
            ):
                original = verify_pencil_multi_direct_sum_witness(
                    source_q, k, p, s, t, shapes
                )
                serialized = json.dumps(original, sort_keys=True)
                restored = json.loads(serialized)
                with self.subTest(field=p, case=label):
                    self.assertTrue(exact_tree_equal(original, restored))
                    self.assertEqual(original["verification"]["direct_sum_verified"],
                                     label == "valid")

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

                # A type-substituted or incomplete serialized record cannot
                # survive exact replay comparison, even if Python considers
                # True equal to 1.
                typed = copy.deepcopy(restored)
                typed["verification"]["left_transform_rank"] = bool(
                    typed["verification"]["left_transform_rank"])
                self.assertFalse(exact_tree_equal(typed, replay))
                missing = copy.deepcopy(restored)
                del missing["Q_blocks"]
                self.assertFalse(exact_tree_equal(missing, replay))



if __name__=="__main__": unittest.main()
