# The date numbers

## The question

One date has four usual spellings, and each spelling is an integer:

```
10/26/2000   10262000
26/10/2000   26102000
2000-10-26   20001026
2000/26/10   20002610
```

Two number-theoretic facts hold across these four labels. All of them are `56` modulo `99`, and their
divisor counts are `80, 80, 8, 8`. The first fact is structural: it follows from the lengths of the
blocks. The second is not: it follows from where the trailing zeros fall. **The residue is a function
of the date; the divisor count is a function of the numeral.** That split is the finding.

## The four labels

| label | format | factorization | `τ` | even digit sum | odd digit sum | `mod 99` |
|---|---|---|---|---|---|---|
| 10262000 | 10/26/2000 | `2⁴ · 5³ · 7 · 733` | 80 | 6 | 5 | 56 |
| 26102000 | 26/10/2000 | `2⁴ · 5³ · 31 · 421` | 80 | 6 | 5 | 56 |
| 20001026 | 2000-10-26 | `2 · 383 · 26111` | 8 | 6 | 5 | 56 |
| 20002610 | 2000/26/10 | `2 · 5 · 2000261` | 8 | 6 | 5 | 56 |
| 10262 | 10/26/2 | `2 · 7 · 733` | 8 | — | — | 65 |
| 26102 | 26/10/2 | `2 · 31 · 421` | 8 | — | — | 65 |

The five-digit rows are the prefixes that the two year-last labels append `000` to. The factorizations
and counts are reproduced by `tools/date_numbers.py`; the concrete residues are in
`Fold/Arithmetic.lean`.

## Why `99`

Because `10² = 100 ≡ 1 (mod 99)`, the powers of ten alternate:

```
10⁰ ≡ 1,  10¹ ≡ 10,  10² ≡ 1,  10³ ≡ 10,  ...
```

So an eight-digit label `n = Σ dᵢ 10ⁱ` satisfies

```
n ≡ E + 10·O  (mod 99),      E = Σ_{i even} dᵢ,   O = Σ_{i odd} dᵢ.
```

For all four labels `E = 6` and `O = 5`, hence `6 + 50 = 56`. The split is structural: the nonzero
digits are `1, 2, 2, 6`, and in the blocks `10`, `26`, `2000` the `6` always sits in an even position
while `1, 2, 2` sit in odd positions. The zeros do not matter.

The reason the positions are stable is the block lengths:

> **Block lemma.** If a decimal number is a concatenation of blocks of even length, permuting the
> blocks preserves its residue modulo `99`.

Concatenating an even-length block shifts the digits already written by an even number of places, and
`10^{2m} ≡ 1`. So each digit keeps the parity of its position, and `E`, `O` are unchanged. All six
permutations of `10 | 26 | 2000` give `56`; the four formats use four of them.

The lemma is about blocks, not digits. Swap two digits inside a block and the residue moves:

```
10262000 ≡ 56      10622000 ≡ 92      01262000 ≡ 47
```

The hypothesis is also real. With two-digit days and months and a four-digit year, every block has even
length. Drop the padding and the parity can move: 2 January 2000 reads `02012000 ≡ 23` and
`20000201 ≡ 23` when padded, but `1202000 ≡ 41` and `2000012 ≡ 14` when not.

## Why `80` and `8`

The divisor count is multiplicative over prime powers: `τ(∏ p^e) = ∏ (e+1)`.

- `10262000 = 10262 · 1000 = (2 · 7 · 733) · (2³ · 5³)`. The exponents are `4, 3, 1, 1`, so
  `τ = 5 · 4 · 2 · 2 = 80`.
- `26102000 = (2 · 31 · 421) · (2³ · 5³)`, the same exponents, so `τ = 80`.
- `20001026 = 2 · 383 · 26111`, three distinct primes, so `τ = 2³ = 8`.
- `20002610 = 2 · 5 · 2000261`, three distinct primes, so `τ = 8`.

The two year-last labels end in `000`, so `1000 = 2³ · 5³` divides them and contributes the factor
`5 · 4 = 20` instead of `2 · 1 = 2`: a net factor `10`. In general, if `m = 2^a 5^b q` with
`gcd(q, 10) = 1`, then

```
τ(1000·m) = (a+4)(b+4)·τ(q).
```

For `m = 10262` and `m = 26102`, `a = 1`, `b = 0`, `τ(q) = 4`, so `τ(1000m) = 5 · 4 · 4 = 80`. The
`80 = 8 · 10` is therefore exact but local: the multiplier is `10` only because the prefix carries
exactly one factor of `2` and no factor of `5`.

The year-first labels have no trailing zeros. Their `2000` is internal, and the digits that follow kill
the factor `5³`; `20001026` is twice an odd number and ends in `26`, while `20002610` ends in `10` and
keeps a single `5`. Both are squarefree with three prime factors, so both have `8` divisors — for
different reasons.

## What the date does not determine

The four labels denote the same date, so the date is invariant under the change of format. The residue
modulo `99` is invariant too, by the block lemma. The divisor count is not:

```
10262000  τ = 80       20001026  τ = 8
```

So "the date determines its divisor count" is false, and "the format determines the number" is false
in the other direction: the residue is date-level, while `τ` is numeral-level. This is not a defect of
the date. It is what the two functions read. `mod 99` reads the parity of digit positions, which the
format preserves. `τ` reads the factorization, which the format changes by moving zeros.

The calendar's own exact content is elsewhere: the closure is the least common multiple
(`146097 = 3³ · 7 · 773` days, and `7 ∣ 146097`), and the leap rule is the fold. Nothing in that
structure is counted by `τ`. The divisor lattice of a label is not the arithmetic of the calendar;
the chart note is `the-fold-chart.md`.

## The zones

| claim | zone | what it rests on |
|---|---|---|
| the four labels are all `56 mod 99`, with `E = 6` and `O = 5` | exact | `10² ≡ 1 (mod 99)` and the digit split |
| permuting even-length decimal blocks preserves the residue modulo `99` | exact | each block shifts the existing digits by an even number of places |
| `τ(10262000) = τ(26102000) = 80` and `τ(20001026) = τ(20002610) = 8` | exact | the factorizations and `τ(∏p^e) = ∏(e+1)` |
| any permutation of the digits preserves the residue | false friend | `10622000 ≡ 92` and `01262000 ≡ 47` |
| the date determines its divisor count | false friend | the same date is `80` in one format and `8` in another |
| the divisor count measures the date | rhyme | `τ` tracks trailing zeros, and the calendar has no such count; this is not a derivation |
| the date's integer is the calendar | false friend | the calendar is a quotient of periods with a closure; the integer is a decimal label |

## What is missing

**A formal block lemma.** `Fold/Arithmetic.lean` proves the four concrete residues by `decide`, but the
general statement about permuting even-length blocks is not in Lean: it needs a formalization of
decimal blocks and their positions. The prose proof above is two lines; the library has the instances,
not the lemma.

**A calendar meaning for `τ`.** None is claimed. The divisor count is a property of the numeral and
changes under a change of notation that preserves the date, so it cannot be an invariant of the
calendar.

**A reason for base ten.** The modulus is `99 = 10² − 1`, which is an accident of ten fingers. In base
`b` the same argument gives invariance modulo `b² − 1` for even-length blocks. The exact object is the
pair (label, base); the date supplies the label, and the culture supplies the base.

## The finding in one sentence

**The date is invariant under format, and so is its residue modulo `99` when every block has even
length, because `10² ≡ 1`; its divisor count is not, because `τ` reads the numeral's factorization and
the same date is `80` when the year is last and `8` when it is first.**
