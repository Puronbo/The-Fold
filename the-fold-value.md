# Value: what would count as taking something out

## The claim about physics

"Physics came from mathematics, so it is a branch made by mathematics to fix mathematics." That has one
exact core and one false friend, and they are separated by a single classical theorem.

**The exact core is completeness.** For a first-order theory `T`,

```
T is consistent   ⟺   T has a model .
```

A physical realization *is* a model. So every realization is a certificate that the fragment it
realizes is consistent, and "physics fixes mathematics" is exact in the only sense that can be made
precise: **it supplies the semantics that the syntax cannot supply for itself.** A theory alone can
never certify its own consistency — that is Gödel's second theorem — while a model certifies it
immediately.

**The false friend is "branch".** A branch is a sub-syntax. Physics is the other side of the
adjunction: theories on one side, models on the other, and the pair is what has content. Calling physics
a branch of mathematics is like calling a model a branch of its theory.

And there is an asymmetry that keeps the claim honest:

> a model certifies consistency; the **absence** of a physical model certifies nothing.

A theory with only non-physical models is consistent and unrealized. So the corpus's "host-required"
class is not a list of mathematical failures; it is a list of structures whose models have not been
built.

| reading of the sentence | zone |
|---|---|
| physics is a branch of mathematics | false friend |
| physics supplies the models mathematics cannot certify for itself | exact |
| physics is the model-companion of mathematics | reformulation |
| the universe is made of mathematics | rhyme |

## Seven meters, and what they read

"Will anything valuable be taken from this?" is answerable if value is defined as something that can be
counted. Seven definitions, strongest first, with today's readings.

| meter | question | reading |
|---|---|---|
| unexpected reuse | is a finding used by a note in another field? | `the-fold-sign.md` is cited from group theory, arithmetic and algebra: `3` inbound, `3` fields |
| prediction | did a number get stated before it was computed? | `M ∝ N^{4/3}`, `3π/16 = 0.589`, `(ℤ/2)²`, `30°` negates `Re(z⁶)`, `0.693` |
| compression | does it shorten a later explanation? | `x² = t` replaced the fold, the quotient, the holonomy and the masking with one equation |
| prohibition | does it forbid something? | corrugation ≠ mass; a free twist ≠ an unworked twist; the integer line folds but does not double; the real fold is not a branched cover |
| prompt closure | did a question produce an exact object? | `7` of `7` prompts since the hexagon |
| redemption | were old rhymes retired? | `0` of `21`; the rhyme share is stable at `31%` |
| discipline growth | did the gate learn a new kind of error? | `9` rules over `63` notes: `0` |

The citation meter is now runnable:

```
python fold_lint.py reuse
```

and it prints `377` edges over `63` notes — `5.98` per note — with the notes that nothing cites.
Fifteen are uncited: the thirteen research notes outside the zone map, and the two fold-note orphans.
The research papers are the newest and cite each other rarely, so their count is expected; what is not
expected is that **no fold note has yet been written that needed them.**

A citation is cheap, though, and this note proved it once: when it was written the orphan count fell
from three to one, because it cites everything it mentions. At that time the ledger and the void map
put the count at two, because this note and the integer line were still uncited. So `reuse` measures
**attention**, not **dependence**. The stronger question is whether a citation could be deleted without breaking the citing
note: remove `the-fold-sign.md` and the discriminant note loses `w₁`, remove
`the-fold-discriminant.md` and the network note loses `A_k`. Those are dependencies. The count does not
yet distinguish them, and that is the honest limit of the meter.

## What the meters say together

Value is being taken, and it is taken at the **input** and at **compression**, not at redemption:

- the prompts compile. Every question in this session became an exact object — the bent integer line
  became `ℤ/n` and the second character; the friction image became `μ = τ/p*` and the spin moment; the
  network became six sum rules; "find it" became `x² = t`;
- the corpus compresses. `x² = t` is the shortest statement of the whole crease story, and it was
  reached by writing the four longer ones first;
- nothing is redeemed. The `21` rhymes are not retired, they accumulate, and the ratio does not move.
  That is not failure — it is the cost of the `69%` — but it means the corpus is an **atlas being
  filled**, not a **theory being tightened**.

The single strongest signal is the first row: a finding used *outside* the field that produced it. It
has happened once, with the sign, and that is the only evidence so far that the corpus is producing
objects rather than prose.

## The test that was run

The orphans were the experiment. The ledger cited `the-fold-sign.md` for `w₁`,
`the-fold-discriminant.md` for `A_k`, and `the-fold-crease-network.md` for the sum rules; it cited
`the-fold-friction.md` only to say that the twelve theorems did not use it. Three of the four were
structure, one was not, and the ledger is where that is written. The meter did not decide it alone — a
citation is cheap — but the ledger had to name the premise each note supplied, and that is a dependence
test a count cannot fake.

That was a cheap, mechanical, falsifiable test of whether anything was taken. It is better than asking
whether the corpus "feels" valuable, because it cannot be argued with.

## The zones of this note

- completeness, the asymmetry, and the four readings of the sentence are exact, up to the standard
  reading of "model";
- the seven meters are definitions, and their readings are computed or counted, not asserted;
- the claim that value is taken "at the input" is a reading of the session, not a theorem;
- "this is how to tell whether the corpus matters" is a projection. The meters can be wrong about what
  matters, but they cannot be wrong about what they count.

The one sentence: value is not what a note says, it is what a later note cannot be written without.
