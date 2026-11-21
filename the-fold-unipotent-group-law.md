# UF-027 — Explicit group law for the seven-parameter unipotent automorphism kernel

## Convention

Work over characteristic zero in
\[
C=k[x,y]/(y²+x²,x⁴).
\]
For θ=(a,b,c,d,e,f,g)∈k⁷, let Φ_θ be the automorphism
\[
\begin{aligned}
x&\mapsto x+a x²+bxy+c x³+d x²y+f x³y,\\
y&\mapsto y-bx²+a xy-dx³+e x²y+g x³y.
\end{aligned}
\]
These are exactly the automorphisms acting trivially on m/m² (UF-026).

Use the composition convention Φ_θ∘Φ_Θ, where θ=(a,b,c,d,e,f,g) is the outer map and Θ=(A,B,C,D,E,F,G) is the inner map.

## Theorem — Closed composition law

The composite is Φ_{θ⋆Θ}, where
\[
\begin{aligned}
a'={}&a+A,\\
b'={}&b+B,\\
c'={}&c+C+2Aa-2Bb,\\
d'={}&d+D+2Ab+2Ba,\\
e'={}&e+E+2Aa-2Bb,\\
f'={}&f+F+2Aab+2Ad+Ba²-Bb²+Bc+Be+3Cb+3Da,\\
g'={}&g+G+Aa²-Ab²+Ac+Ae-2Bab-2Bd-3Db+3Ea.
\end{aligned}
\]
In particular, the group law is polynomial and makes the seven-dimensional affine space k⁷ into the unipotent group Aut₁(C).

**Proof.** Substitute the images under Φ_θ into the polynomial expressions defining Φ_Θ, expand, and reduce by y²=−x² and x⁴=0. The coefficients of x²,xy,x³,x²y,x³y in the image of x and y recover the seven displayed parameters. The two images satisfy the same constrained form from UF-026, so the result is exactly Φ_{θ⋆Θ}. ∎

## Identity and inverse

The identity is (0,0,0,0,0,0,0). Since the group is unipotent, every element has an inverse. It can be obtained uniquely by solving θ⋆Θ=0; the polynomial composition law provides a triangular system, beginning with A=−a and B=−b, then solving successively for C,D,E,F,G.

## Structural observations

- The first two coordinates form an additive quotient k².
- The next three coordinates acquire quadratic corrections, so the group is generally nonabelian.
- The final two coordinates record central-degree contributions, but whether the corresponding subgroup is the full center must be determined from the commutator law rather than inferred from degree alone.
- The law is a concrete coordinate presentation of the unipotent radical in UF-026; it can be used to calculate commutators, the center, and the lower central series.

## Reproducibility

Run `python3 tools/fold_unipotent_group_law.py`. The SymPy script composes two arbitrary seven-parameter substitutions, reduces them in C, and compares every coefficient with the displayed formula.

## Open problem UF-027-A

Derive the inverse and commutator formulas in closed form. Determine the center, derived subgroup, and lower central series of Aut₁(C). Then compare the resulting filtration with the m-adic degree filtration and test whether the associated graded Lie algebra has a canonical D16 action.
