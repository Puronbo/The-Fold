# G-EP6 — exact prime-field Jordan fingerprint engine

## Scope

The first executable layer implements the kernel-growth half of the spectral fingerprint in pure Python, using only the standard library. It computes Jordan profiles for eigenvalues supplied in the base prime field F_p.

It does **not** yet factor characteristic polynomials, discover eigenvalues, or construct extension fields. Those are separate layers; the interface reports this limitation explicitly rather than silently treating a base-field scan as a complete spectral decomposition.

## Implementation

- tools/spectral_fingerprint.py: modular Gaussian elimination, matrix multiplication and powers, nullity sequence, and Jordan-block reconstruction.
- tests/test_spectral_fingerprint.py: unit tests for modular rank, single and mixed Jordan blocks, diagonalizable repeated eigenvalues, non-eigenvalues, the ramified quarter-turn, validation, and output metadata.

For an input matrix A, prime p, and supplied λ in F_p, the engine computes
K_r = dim ker(A−λI)^r.
It returns the nullity sequence, first differences (blocks of size at least r), exact block-size multiplicities, and the recovered partition.

All row reduction is exact modulo the prime. No floating-point eigenvalue or rank tolerance is used.

## Interface

Example command:

~~~sh
python tools/spectral_fingerprint.py \
  --prime 7 \
  --matrix-json '[[0,1,0],[0,0,1],[0,0,0]]' \
  --eigenvalues 0
~~~

The expected Jordan partition is [3], with nullities [0,1,2,3].

The Python API is:

~~~python
from tools.spectral_fingerprint import spectral_fingerprint

result = spectral_fingerprint(
    [[0, 1], [0, 0]],
    p=5,
    eigenvalues=[0],
)
~~~

## Verification boundary

The core arithmetic was independently checked against four representative cases: a 3+2+1 partition, a non-eigenvalue, the ramified C_4 case modulo 2, and a diagonalizable repeated eigenvalue. The repository includes a broader unittest suite, but a full repository test run is not claimed here.

## Next layers

1. Add exact characteristic-polynomial computation and factorization over F_p.
2. Add extension-field arithmetic so irreducible factors can be split and profiled without confusing base-field eigenvalues with extension-field roots.
3. Add property-based tests comparing generated Jordan matrices with their recovered partitions.
4. Add optional adapters only after the exact algebra layer is stable.

This is a reusable diagnostic primitive, not a neural-network optimization. A machine-learning framework can supply a matrix, but conversion of model weights to a finite field requires an explicit encoding and does not preserve ordinary real-valued model behavior automatically.
