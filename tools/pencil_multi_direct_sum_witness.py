"""Verify supplied multi-block direct-sum witnesses for matrix pencils."""
from __future__ import annotations
from typing import Sequence

def _shape(matrix, name):
    if not isinstance(matrix, (list, tuple)) or not matrix:
        raise ValueError(f"{name} must be a nonempty matrix")
    if not all(isinstance(row, (list, tuple)) for row in matrix):
        raise ValueError(f"{name} must contain rows")
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise ValueError(f"{name} must be nonempty and rectangular")
    return len(matrix), width

def _rank(matrix, p):
    if not matrix: return 0
    a = [[int(x) % p for x in row] for row in matrix]
    rows, cols, rank = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None: continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [x*inv % p for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                f = a[i][col]
                a[i] = [(x-f*y) % p for x,y in zip(a[i],a[rank])]
        rank += 1
        if rank == rows: break
    return rank

def _matmul(a, b, p):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix dimensions")
    return [[sum(int(a[i][z])*int(b[z][j]) for z in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]

def verify_pencil_multi_direct_sum_witness(q: Sequence[Sequence[int]],
        k: Sequence[Sequence[int]], p: int,
        left_transform: Sequence[Sequence[int]],
        right_transform: Sequence[Sequence[int]],
        block_shapes: Sequence[tuple[int,int]]) -> dict:
    """Verify supplied transforms split both coefficients into rectangular blocks."""
    if not isinstance(p,int) or isinstance(p,bool) or p < 2:
        raise ValueError("p must be an integer prime")
    if any(p % d == 0 for d in range(2,int(p**0.5)+1)):
        raise ValueError("p must be prime")
    m,n = _shape(q,"q")
    if _shape(k,"k") != (m,n): raise ValueError("q and k must have the same shape")
    if _shape(left_transform,"left_transform") != (m,m):
        raise ValueError("left_transform must be square with row dimension of q")
    if _shape(right_transform,"right_transform") != (n,n):
        raise ValueError("right_transform must be square with column dimension of q")
    if not isinstance(block_shapes,(list,tuple)) or len(block_shapes)<2:
        raise ValueError("block_shapes must contain at least two block shapes")
    shapes=[]
    for shape in block_shapes:
        if (not isinstance(shape,(list,tuple)) or len(shape)!=2
            or any(not isinstance(x,int) or isinstance(x,bool) or x<0 for x in shape)
            or (shape[0]==0 and shape[1]==0)):
            raise ValueError("each block shape must be a nonzero pair of nonnegative integers")
        shapes.append((shape[0],shape[1]))
    if sum(r for r,c in shapes)!=m or sum(c for r,c in shapes)!=n:
        raise ValueError("block shapes must partition full row and column dimensions")
    s=[[int(x)%p for x in row] for row in left_transform]
    t=[[int(x)%p for x in row] for row in right_transform]
    q0=[[int(x)%p for x in row] for row in q]
    k0=[[int(x)%p for x in row] for row in k]
    sqt=_matmul(_matmul(s,q0,p),t,p)
    skt=_matmul(_matmul(s,k0,p),t,p)
    rc=[0]; cc=[0]
    for r,c in shapes: rc.append(rc[-1]+r); cc.append(cc[-1]+c)
    def split(matrix):
        return [[[row[cc[j]:cc[j+1]] for row in matrix[rc[i]:rc[i+1]]]
                 for j in range(len(shapes))] for i in range(len(shapes))]
    qb,kb=split(sqt),split(skt)
    sr,tr=_rank(s,p),_rank(t,p)
    qzero=all(all(int(x)%p==0 for row in qb[i][j] for x in row)
              for i in range(len(shapes)) for j in range(len(shapes)) if i!=j)
    kzero=all(all(int(x)%p==0 for row in kb[i][j] for x in row)
              for i in range(len(shapes)) for j in range(len(shapes)) if i!=j)
    return {
      "schema":"the-fold-pencil-multi-direct-sum-witness-v1","field":f"F_{p}",
      "source_shape":[m,n],"block_shapes":[list(x) for x in shapes],
      "left_transform":s,"right_transform":t,"transformed_Q":sqt,"transformed_K":skt,
      "Q_blocks":qb,"K_blocks":kb,
      "verification":{"left_transform_rank":sr,"right_transform_rank":tr,
        "left_transform_invertible":sr==m,"right_transform_invertible":tr==n,
        "Q_off_diagonal_blocks_zero":qzero,"K_off_diagonal_blocks_zero":kzero,
        "direct_sum_verified":sr==m and tr==n and qzero and kzero},
      "scope":"Exact verification of a supplied constant witness for an ordered multi-block direct sum with rectangular blocks. It does not discover transformations, prove uniqueness, or assert regularity."
    }
