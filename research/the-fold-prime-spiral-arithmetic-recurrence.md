# Comparing spiral recurrence with arithmetic recurrence

**Status:** finite-data diagnostic. The comparison is exact about the supplied records and thresholds; it is not a theorem about prime distribution.

## Geometry under test

Use the index spiral

\[
z_n=n e^{in\omega}.
\]

For two indices \(i<j\), define circular angular distance

\[
\delta_\theta(i,j)=
\left|\operatorname{atan2}\bigl(\sin((j-i)\omega),
\cos((j-i)\omega)\bigr)\right|
\]

and relative radial distance

\[
\delta_r(i,j)=\frac{j-i}{j}.
\]

A geometric recurrence is recorded only when both

\[
\delta_\theta(i,j)\leq\varepsilon_\theta,\qquad
\delta_r(i,j)\leq\varepsilon_r
\]

hold. The radial scale \(a>0\) cancels from this relative test. A small angular difference alone is not treated as a return: the spiral may have moved substantially outward.

## Independent arithmetic channels

For the supplied increasing prime list, the comparison independently checks:

- **Gap recurrence:** relative difference between the gaps from the previous supplied entry, with the first entry having no preceding gap.
- **Residue recurrence:** equality of all selected residues \(p\bmod m\).
- **Spectral recurrence (optional):** equality of modular rank and Frobenius orbit-degree histogram for a supplied matrix, only when both finite-field factorizations are marked complete.

Gaps are differences between supplied entries. They are consecutive-prime gaps only when the input contains consecutive primes. Residue signatures depend on selected moduli. Spectral signatures depend on the chosen matrix and reduction modulo the prime.

## Executable interface

The module tools/prime_recurrence_comparison.py exposes compare_spiral_arithmetic_recurrence. It returns every index pair, its angular and radial distances, each independent recurrence flag, and aggregate match counts. Thresholds are explicit function parameters.

Example input:

\[
(p_1,p_2,p_3,p_4)=(3,5,7,11),\quad
\omega=0,\quad (m_1,m_2)=(2,3).
\]

With zero angular tolerance, radial tolerance \(1\), and zero gap tolerance:

- all six index pairs satisfy the geometric criterion because all angles are equal and every relative radial distance is at most one;
- exactly one pair has equal supplied-entry gaps: the pair at indices 2 and 3, both with gap 2;
- exactly one pair has equal residues modulo both 2 and 3: prime labels 5 and 11.

This intentionally simple example demonstrates that geometric matches, gap matches, and residue matches are different predicates. The counts are consequences of the stated finite input and thresholds.

## Interpretation discipline

A high geometric match count does not imply a high arithmetic match count. Nor does either count establish a general law. To investigate an apparent pattern, vary omega, tolerances, radial encoding, moduli, and prime window; compare against label-shuffled or other explicitly defined baselines; and report the full parameters alongside counts. Do not select thresholds after inspecting the desired pair.

The comparison is a diagnostic bridge between the prime spiral and its arithmetic afterimage: geometry asks whether encoded positions recur; arithmetic asks whether independent prime features recur.
