# UF-022 — Modular D4 symmetry and a precise bad-prime invariant

## The group and its invariant ring

Let G be the order-eight symmetry group of the square, acting on S=k[x,y] by signed permutations:
\[
(x,y)\mapsto(\pm x,\pm y),\qquad (x,y)\mapsto(\pm y,\pm x).
\]
Assume first that char(k) is not 2. Invariance under the two sign changes forces even exponents in x and y; invariance under swapping x² and y² then gives
\[
S^G=k[x²+y²,x²y²]=k[p,q].
\]
Thus the vertex algebra is the coinvariant algebra
\[
C=S/(S^G_+S)=k[x,y]/(x²+y²,x²y²)=R_0.
\]
The monic presentation from UF-021 shows S is free of rank eight over k[p,q], so dim_k C=8.

## Theorem 1 — regular representation away from 2

If char(k) does not divide 8, the nonmodular reflection-group theorem applies: the coinvariant algebra C is isomorphic, as a k[G]-module, to the regular representation k[G].

For the dihedral group of order eight, the regular representation decomposes over an algebraically closed field of odd characteristic as
\[
C\cong \mathbf1\oplus\chi_1\oplus\chi_2\oplus\chi_3\oplus E\oplus E,
\]
where the four one-dimensional characters are the four characters of G/[G,G]≅C₂×C₂, and E is the unique two-dimensional irreducible representation. The dimensions add to 1+1+1+1+2+2=8.

This recovers the multiplicity pattern found in the analytic D4 decomposition (UF-015), now interpreted as the regular representation of the finite group. No odd prime is exceptional: 8 is invertible in every odd residue characteristic, and the four one-dimensional characters remain distinct because 1≠−1.

## Theorem 2 — characteristic two is genuinely modular

In characteristic two, each sign change acts trivially because −1=1. The action factors through the order-two coordinate swap. Hence
\[
S^G=k[x+y,xy],
\]
not k[x²+y²,x²y²]. In fact
\[
p=x²+y²=(x+y)²,\qquad q=x²y²=(xy)².
\]
Therefore the ideal (p,q) is a proper subideal of the positive-degree invariant ideal (x+y,xy), and R0 is no longer the coinvariant algebra for the effective action.

Moreover, the group order 8 is zero in k, so Maschke's theorem does not apply. The four characteristic-zero sign characters all collapse: a one-dimensional representation sends every element of order two to a scalar u with u²=1, and in a field of characteristic two this forces u=1. Thus the character-projector decomposition cannot survive as a direct sum of four distinct one-dimensional eigenspaces plus two E copies.

This is a representation-theoretic explanation of the exceptional prime 2 from UF-021. It is not a failure of the abstract Frobenius algebra: its length-eight basis and perfect pairing remain intact.

## A precise, project-local meaning of “eigenprime”

For this project, define a **modular eigenprime** of a specified integral G-module M to be a prime ℓ at which reduction M⊗F̄_ℓ no longer has the same semisimple irreducible-character multiplicities as its characteristic-zero representation.

For the D4 coinvariant module C, the only modular eigenprime is
\[
\boxed{\ell=2}.
\]
This definition is intentionally relative to a named group action and module. It is not a claim that prime numbers are eigenvalues, nor that every Fold construction has the same bad-prime set. For a different integral representation, the bad primes must be recomputed.

## Project consequence

The arithmetic story now has three distinct layers:

1. The local Frobenius algebra has a perfect coefficient pairing in every characteristic (UF-020).
2. The parameter family is generically étale precisely in the expected discriminant complement in odd characteristic; characteristic two is everywhere non-étale (UF-021).
3. The D4 coinvariant representation is semisimple and regular in every odd characteristic, but becomes modular at 2 (this note).

The same prime 2 appears in layers 2 and 3 for related but distinct reasons: inseparability of the quotient map and failure of semisimple D4 representation theory.

## Open problem UF-022-A

For other finite symmetry groups introduced by Fold extensions, compute the minimal bad-prime set from the integral group action, invariant ring, and character projectors. Determine when it equals the set of prime divisors of |G| and when extra primes arise from denominators in the chosen integral model or deformation parameters.

## Reproducibility

Run `python3 tools/fold_modular_d4.py`. The verifier checks the group-order arithmetic, the characteristic-two root-of-unity collapse, and the dimension count of the regular decomposition. The invariant-ring identification and the general coinvariant-regular theorem are proved by the arguments above and the nonmodular reflection-group theorem, not by this finite script.
