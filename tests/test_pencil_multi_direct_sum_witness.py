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

if __name__=="__main__": unittest.main()
