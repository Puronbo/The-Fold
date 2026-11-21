# UF-006 — Sign Characters of Frieze and Wallpaper Groups

**Research question.** Which global sign characters can a periodic Fold height carry under the seven frieze groups and the seventeen wallpaper groups, and how do glide reflections affect the answer?

**Main result.** If a signed height is periodic under the entire translation subgroup \(T\) of a frieze or wallpaper group \(W\), every translation has character \(+1\). Its sign character therefore factors uniquely through the finite point group \(P=W/T\):

\[
\boxed{\operatorname{Hom}_{T}(W,C_2)\cong\operatorname{Hom}(P,C_2).}
\]

Here \(\operatorname{Hom}_{T}\) denotes homomorphisms \(\chi:W\to C_2\) that are trivial on \(T\). This is true even when the crystallographic extension is nonsplit. Glide offsets do not create extra periodic-height signs: a glide whose square is a translation automatically has sign \(+1\) after two applications.

The results below classify **algebraically possible** periodic sign characters. A particular crease graph or height function may realize only some of them; geometry imposes additional fixed-point, zero-set, and decoration constraints.

## 1. The translation-kernel theorem

Let \(W\) be a frieze or wallpaper group, \(T\triangleleft W\) its full translation subgroup, and \(P=W/T\) its finite point group. Let \(C_2=\{+1,-1\}\).

A homomorphism \(\chi:W\to C_2\) is called *translation-trivial* when

\[
\chi(t)=+1\qquad\text{for every }t\in T.
\]

### Theorem 1 — Periodic characters factor through the point group

There is a canonical isomorphism

\[
\boxed{\{\chi\in\operatorname{Hom}(W,C_2):\chi|_T=1\}
\;\cong\;\operatorname{Hom}(P,C_2).}
\]

**Proof.** Let \(\pi:W\to P=W/T\) be the quotient map. If \(\bar\chi:P\to C_2\) is a homomorphism, then \(\chi=\bar\chi\circ\pi\) is a homomorphism on \(W\) that is trivial on \(T\). Conversely, if \(\chi:W\to C_2\) is trivial on \(T\), then \(\bar\chi(wT)=\chi(w)\) is well-defined: if \(wT=w'T\), then \(w^{-1}w'\in T\), so \(\chi(w')=\chi(w)\). It is a homomorphism, and its pullback is \(\chi\). These constructions are inverse. No splitting of the extension is used. \(\square\)

For a strictly periodic signed height, translation-triviality is mandatory because a lattice translation returns the same point in the periodic cell. Thus the height-sign possibilities depend only on \(P\), not on the choice of glide or screw-like affine lifts.

### Corollary — Glide signs

If \(g\) is a glide reflection and \(g^2=t\in T\), then every translation-trivial character satisfies

\[
\chi(g)^2=\chi(g^2)=\chi(t)=+1.
\]

Both choices \(\chi(g)=+1\) and \(\chi(g)=-1\) remain algebraically possible. A glide may therefore reverse a signed height on one application while its square, the full lattice translation, preserves it.

## 2. The seven frieze groups

We use the standard seven frieze types and give explicit abstract presentations. The presentation numbering \(F_1,\ldots,F_7\) follows the order of the Clemson course notes; the crystallographic symbols are included for reference. \(D_\infty\) denotes the infinite dihedral group.

| Frieze | Presentation | Abstract group | Point quotient \(P\) |
|---|---|---|---|
| \(F_1\) (p2mm) | \(\langle t,h,v\mid h^2=v^2=1,\ hv=vh,\ tv=vt,\ tht=h\rangle\) | \(D_\infty\times C_2\) | \(D_2\cong C_2\times C_2\) |
| \(F_2\) (p2mg) | \(\langle g,h\mid h^2=1,\ ghg=h\rangle\), \(T=\langle g^2\rangle\) | \(D_\infty\) | \(D_2\cong C_2\times C_2\) |
| \(F_3\) (p1m1) | \(\langle t,v\mid v^2=1,\ vtv=t^{-1}\rangle\) | \(D_\infty\) | \(C_2\) |
| \(F_4\) (p2) | \(\langle t,r\mid r^2=1,\ rtr=t^{-1}\rangle\) | \(D_\infty\) | \(C_2\) |
| \(F_5\) (p11m) | \(\langle t,h\mid h^2=1,\ ht=th\rangle\) | \(\mathbb Z\times C_2\) | \(C_2\) |
| \(F_6\) (p11g) | \(\langle g\rangle\cong\mathbb Z\), \(T=\langle g^2\rangle\) | \(\mathbb Z\) | \(C_2\) |
| \(F_7\) (p1) | \(\langle t\rangle\cong\mathbb Z\), \(T=\langle t\rangle\) | \(\mathbb Z\) | trivial |

The exact affine geometry distinguishes frieze types even when their abstract groups coincide. For example, \(F_3\) and \(F_4\) are both abstractly infinite dihedral, but one uses a mirror-type involution and the other a half-turn. Likewise, \(F_6\) and \(F_7\) are both abstractly \(\mathbb Z\), but \(F_6\)'s generator is a glide whose square is the primitive translation, while \(F_7\)'s generator is itself a translation.

### Theorem 2 — Complete frieze character counts

The table gives the number of all abstract homomorphisms \(W\to C_2\), followed by the number that are trivial on the translation subgroup. The last column is the rank of the periodic character space over \(\mathbb F_2\).

| Frieze | All abstract characters | Translation-trivial characters | Periodic character rank |
|---|---:|---:|---:|
| \(F_1\) (p2mm) | 8 | 4 | 2 |
| \(F_2\) (p2mg) | 4 | 4 | 2 |
| \(F_3\) (p1m1) | 4 | 2 | 1 |
| \(F_4\) (p2) | 4 | 2 | 1 |
| \(F_5\) (p11m) | 4 | 2 | 1 |
| \(F_6\) (p11g) | 2 | 2 | 1 |
| \(F_7\) (p1) | 2 | 1 | 0 |

**Reason.** A homomorphism to \(C_2\) assigns signs to the presentation generators, and the relators impose parity constraints. In these presentations every defining relation has even total exponent for each generator, so all generator signs are free before imposing translation-triviality. For \(F_1,F_3,F_4,F_5,F_7\), the displayed \(t\) is a translation and must map to \(+1\). For \(F_2,F_6\), the primitive translation is \(g^2\), so \(\chi(g^2)=\chi(g)^2=+1\) automatically. The first isomorphism theorem then identifies the periodic counts with the character counts of the point quotients.

Thus the seven frieze types admit a total of 17 translation-trivial character maps across the classification. The count is not a count of geometrically distinct motifs; it is the sum of the character-space sizes for the seven abstract symmetry types.

## 3. Character counts for all 17 wallpaper groups

For the wallpaper groups, the translation subgroup is \(T\cong\mathbb Z^2\). By Theorem 1, the periodic sign-character space is determined by the finite point group.

For a cyclic point group,

\[
|\operatorname{Hom}(C_n,C_2)|=
\begin{cases}
1,&n\text{ odd},\\
2,&n\text{ even}.
\end{cases}
\]

For the dihedral point group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\),

\[
|\operatorname{Hom}(D_n,C_2)|=
\begin{cases}
2,&n\text{ odd},\\
4,&n\text{ even}.
\end{cases}
\]

Indeed, a character is determined by \(\chi(r)\) and \(\chi(s)\). The reflection sign is always free; the rotation sign is free exactly when \(n\) is even.

| Wallpaper group | Point group | Periodic sign characters | Rank over \(\mathbb F_2\) |
|---|---|---:|---:|
| p1 | \(C_1\) | 1 | 0 |
| p2 | \(C_2\) | 2 | 1 |
| pm | \(C_2\) | 2 | 1 |
| pg | \(C_2\) | 2 | 1 |
| cm | \(C_2\) | 2 | 1 |
| pmm | \(D_2\) | 4 | 2 |
| pmg | \(D_2\) | 4 | 2 |
| pgg | \(D_2\) | 4 | 2 |
| cmm | \(D_2\) | 4 | 2 |
| p4 | \(C_4\) | 2 | 1 |
| p4m | \(D_4\) | 4 | 2 |
| p4g | \(D_4\) | 4 | 2 |
| p3 | \(C_3\) | 1 | 0 |
| p3m1 | \(D_3\) | 2 | 1 |
| p31m | \(D_3\) | 2 | 1 |
| p6 | \(C_6\) | 2 | 1 |
| p6m | \(D_6\) | 4 | 2 |

Across all 17 wallpaper types, the sum of these point-group character-space sizes is 46. Only p1 and p3 have no nontrivial periodic sign character. This is an algebraic possibility count, not a claim that every particular height pattern on those groups realizes every character.

## 4. What glide reflections do—and do not do

A glide reflection is an affine isometry whose square is a nonzero translation. It can have sign \(-1\) on one application, but any strictly periodic height must have sign \(+1\) under the square. Therefore a glide's sign is not killed by the periodicity condition; it is a legitimate point-group character.

The extension

\[
1\to T\to W\to P\to1
\]

may be nonsplit. Nonetheless, periodic characters are still exactly the pullbacks of point-group characters because they kill \(T\). Nonsymmorphic data can affect which geometric patterns realize a character, but it cannot create extra homomorphisms that are trivial on translations.

## 5. Executable verification

`tools/fold_frieze_wallpaper_characters.py` enumerates generator signs in the seven frieze presentations, checks the relators modulo two, imposes translation-triviality, and computes the point-group character counts for all 17 wallpaper groups.

The bounded reference checks include:

- 7 frieze presentations;
- 28 full abstract frieze characters;
- 17 translation-trivial frieze characters;
- 72 full-relator and 40 periodic-relator checks;
- cyclic/dihedral character formulas for \(1\le n\le12\);
- all 17 wallpaper point groups, giving 46 periodic character maps in total.

These checks validate the finite enumeration and the listed presentations. The general factor-through theorem and the cyclic/dihedral formulas are proved above.

## 6. Consequences for The Fold

1. A periodic signed height cannot assign a negative sign to a pure lattice translation. If a proposed model does so, its claimed period lattice is not the true period lattice of the signed field, even if it is a period of the unlabelled zero set.
2. A glide may reverse the signed height while its square preserves it. This is a natural mechanism for a sign-reversing operation that cannot be interpreted as a pure reflection.
3. The maximum number of independent binary sign decorations that can be detected by a periodic character map is the rank of \(\operatorname{Hom}(P,C_2)\), at most two for the planar crystallographic point groups.
4. A/B labels and height signs need not coincide. They can define independent characters, as in UF-004, but the available point group determines whether both independent signs can exist.
5. The point-group table is only the algebraic candidate list. A fixed crease network must still be checked for actual equivariance and for zeros forced by sign-reversing stabilizers.

**Conclusion.** UF-006 reduces the periodic sign-character problem from an infinite frieze or wallpaper group to its finite point group. The seven frieze groups give 17 translation-trivial character maps in total; the seventeen wallpaper types give 46. Glide reflections remain capable of reversing the height once, even though their squares are translations and therefore preserve it.

## References

- Matthew Macauley, Clemson University, *Chapter 1: Groups, intuitively*, section “Frieze groups,” especially the presentations of the seven frieze types and the statement that there are seven geometric types but four abstract isomorphism types: [course notes PDF](https://www.math.clemson.edu/~macaule/classes/s22_math4120/slides/new/math4120_slides_chapter1_h.pdf).
- Liaqat Ali, *Rational Representation Zeta Functions of Crystallographic Groups* (PhD thesis, Royal Holloway, University of London, 2015), Section 4.1, for the crystallographic presentations and translation subgroups of p1, p1m1, p11m, p11g, p2, p2mg, and p2mm: [thesis PDF](https://pure.royalholloway.ac.uk/files/23862600/RHULThesis.pdf).
- Ramón Flores, “Bredon Homology of Wallpaper Groups,” *Bulletin of the Korean Mathematical Society* 60 (2023), 1497–1522. Defines wallpaper groups as discrete cocompact plane-isometry groups and states the extension by a rank-two translation group and finite point group: [paper PDF](https://idus.us.es/server/api/core/bitstreams/9b272c5c-f70d-4ed9-a481-be70206c07c1/content).
- Siqi Huang, *Applications of Group Actions in Coloring Problems and Wallpaper Groups* (2025), Table 2.1, for the point groups associated with the 17 wallpaper types: [thesis PDF](https://digicoll.lib.berkeley.edu/nanna/record/313094/files/2025Spring_Huang_Siqi.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0).