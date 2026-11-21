# UF-061 — Maximal generic rank of the affine nilpotent coefficient matrix

## 1. The coefficient matrix

Use the full determinant-open affine family and the correctly ordered conjugation from UF-060. The nilpotent coefficient algebra is
\[
T=k[c,d,h]/(c^4,d^2,h^2).
\]
As a k-module over the reduced parameter base, it has basis
\[
c^r d^s h^t,\qquad 0\le r\le3,\quad 0\le s,t\le1.
\]
The unit monomial is the identity term. The fifteen nonconstant monomials are
\[
h,d,dh,c,ch,cd,cdh,c^2,c^2h,c^2d,c^2dh,c^3,c^3h,c^3d,c^3dh.
\]

Expand the sixteen target coefficient functions
\[
(c',a',b',\alpha',\beta',\gamma',\delta',\epsilon',
d',h',i',\phi',\psi',\eta',\theta',\kappa')
\]
in this basis. Their nonconstant coefficients form a (16\times15) matrix over the reduced affine/U parameter ring. The column indexed by a nilpotent monomial is its coefficient vector across the sixteen target coordinates.

## 2. Theorem UF-061

**The coefficient matrix has generic rank fifteen.**

### Proof by a nonzero maximal minor

Specialize the reduced parameters to
\[
a=i=1,\qquad b=0,
\]
and specialize the U-parameters to
\[
(A,B,C,D,E,G,J)=(0,0,0,1,1,1,1).
\]
The nilpotent variables (c,d,h) remain formal and retain the relations (c^4=d^2=h^2=0). At this specialization, form the (15\times15) submatrix using all sixteen target-coordinate rows except the row for (epsilon'), and all fifteen nonconstant nilpotent monomial columns in the order displayed in Section 1.

Exact coefficient extraction in characteristic two gives determinant
\[
\det(M_{15})=1\in\mathbb F_2.
\]
Therefore this minor is not the zero polynomial on the reduced parameter space. The full (16\times15) coefficient matrix consequently has rank fifteen on a dense open subset. Since it has only fifteen columns, this is the maximal possible generic rank. (square)

## 3. Interpretation

1. Every one of the fifteen nonconstant nilpotent monomial directions is generically linearly independent when observed across the sixteen target coefficient functions.
2. The affine conjugation family therefore detects the entire nilpotent coefficient vector space generically, not merely the mixed direction ch.
3. This is stronger than the UF-060 ch-component result, but it is still a statement about the coefficient matrix over the generic reduced parameter field. It does not say that the coefficient module is free of rank fifteen at every point or that a chosen minor is globally invertible.
4. It does not identify the scheme-theoretic orbit-image ideal. The kernel of the universal conjugation pullback and the largest Hopf ideal contained in that kernel still require separate calculation.

## 4. Verification boundary

The proof is a specialization certificate: one admissible specialization with a nonzero maximal minor proves the generic-rank lower bound, and the number of columns gives the matching upper bound. The determinant calculation uses exact arithmetic in (mathbb F_2) and the truncated monomial relations. No numerical approximation is involved.

**Open UF-062:** determine the determinantal rank-drop locus of the (16\times15) coefficient matrix over the reduced affine/U parameter space, identify the vanishing ideal of its maximal minors, and then compute the scheme-theoretic orbit-image kernel and its Hopf core.


## 5. Reproducible exact verifier

Added tools/fold_char2_affine_coefficient_matrix_rank.py. It reconstructs the specialization directly in the truncated polynomial ring F₂[x,z,c,d,h]/(x⁴,z²,c⁴,d²,h²), applies the correctly ordered conjugation, extracts the 16-by-15 coefficient matrix, omits the epsilon-prime row, and performs exact Gaussian elimination over F₂. The verifier asserts that the determinant is 1. It uses only the Python standard library.
