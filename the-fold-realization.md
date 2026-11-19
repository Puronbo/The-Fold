# Realization: what "mathematics is physical" can mean

## Three candidate meanings

The sentence "mathematics can be explained physically" has three readings, and only one survives.

| reading | claim | status |
|---|---|---|
| simulate | a computer can compute any mathematical object | true up to error and resources, and it explains nothing |
| derive | physics entails mathematical truth | impossible: physics is a contingent theory, mathematics is not |
| **realize** | a physical system's structure **is** the mathematical object, up to a stated error and limit | achievable, and it is the only one that carries content |

Simulating `ℤFC` does not explain `ℤFC`; deriving `2 + 2 = 4` from the Standard Model is a category
error. Realization is the middle path: an isomorphism between a physical system and a mathematical
structure, with the isomorphism exhibited, not asserted.

## The definition

A realization is a functor from a category of physical systems to a category of mathematical structures,
together with three data:

```
R : Phys → Math ,      an object S ↦ R(S) ,
an error  ε  ,        an inverse map on a subcategory, up to ε ,
a limit   Λ  ,        the topology in which ε → 0 .
```

A mathematical object is **physical** when it lies in the essential image of some `R`. That is a
definition, so it can be used; it is not a thesis about the world. And it immediately produces the
classification, because the three data are not always available.

## Every finding sorts into three classes

This is what the corpus has actually been building, finding by finding:

| finding | what it realizes | class | what the class costs |
|---|---|---|---|
| the fold `σ`, the quotient `F` | an involution and its orbit space | finite, exact | nothing |
| `x² = t`, the discriminant | a branched cover, `w₁`, `A_k` | exact over `ℂ`; a boundary over `ℝ` | the field must be named |
| the hexagon `D₆`, `(ℤ/2)²` | a finite group and its characters | finite, exact | nothing |
| the integer line, `ℤ/n` | a discrete involution, the clock | finite, exact | the doubling leaves the set |
| the cone's deficit | Gauss–Bonnet at one point | exact per `n`; a limit `n → ∞` for the circle | a sequence and a rate |
| friction | a flux across a codimension-one set | host-required | `τ`, `p*`, `N` must be supplied |
| the crease network | six index theorems | exact at the boundary | a bundle must be supplied |
| the Dirac zero | a winding number | exact in the tight-binding host | a Hamiltonian must be supplied |

Three classes, and they are exhaustive for a reason:

- **finite, exact** — a finite structure needs nothing but itself. No topology, no limit, no material.
  Every finite isomorphism class is realizable in principle;
- **limit-realized** — an infinite structure is the limit of finite ones. It needs a sequence, a
  topology, and a rate. This is where analysis, spectra and statistical mechanics live;
- **host-required** — the structure needs a substance the Fold does not have: a stress, a Hamiltonian,
  a measure, a bath. The Fold supplies the shape of the interface and nothing behind it.

So "the entirety of mathematics" fails, but not for the reason usually given. It fails in three
different ways, and each has its own repair.

## Four ceilings

**1. Cardinality.** A realization must be *specifiable*. The finitely describable structures are
countable; the class of all structures is not even a set. So at most countably many structures can be
named, and the rest cannot be pointed at, let alone realized. This ceiling is not about physics; it is
about reference.

**2. Finiteness.** No finite system is isomorphic to `ℕ` — there is no injection from `ℕ` into a finite
set. So arithmetic is never realized *as* a finite system; it is realized as a limit, with a rate. That
is the whole content of the second class, and it is exact.

**3. Compactness.** If a first-order theory has an infinite model, it has models of every infinite
cardinality. So a physical realization, being one model, never pins down the intended one. Realization
is model-building, and **models never determine theories**. The choice of theory is not physical; it is
a premise, and naming it is the corpus's whole discipline. This is the deepest ceiling, because it says
the ambiguity is structural, not a gap in our knowledge.

**4. Undecidability.** If the physical process is computable, it cannot decide all arithmetic truth
(Gödel, Tarski, Turing). "Decide" is therefore out of reach in principle, while "realize" is not. The
premise is *physics is computable*; the Malament–Hogarth spacetimes would break it, and then this
ceiling weakens — the cardinality ceiling does not.

The four ceilings are independent. Dropping any one of them still leaves the other three, which is why
no future physics can make "the entirety" true in the strong sense.

## What is actually available

Not a reduction — an **atlas with three colours and an error column**:

1. the finite part, realized exactly, with the isomorphism written down (`the-fold-lean.md` is the
   beginning of this column);
2. the describable infinite part, realized as limits, with a rate per entry (the cone's `n → ∞`, the
   lattice's continuum limit, the thermodynamic limit);
3. the rest, marked absent — not because it is mysterious, but because it fails one of the four
   ceilings, and the note says which.

That is "something close". It is close in the only sense that survives inspection: **every
finely-describable structure has a row, and every row says what it costs.** A reduction would be one
colour; an atlas is honest.

## The measured form

The corpus is itself a finite object, and its growth is measurable. Over the last seven readings of the
zone map:

| reading | exact | total | exact fraction |
|---|---|---|---|
| 1 | 105 | 147 | 0.714 |
| 2 | 110 | 157 | 0.701 |
| 3 | 114 | 166 | 0.687 |
| 4 | 119 | 173 | 0.688 |
| 5 | 124 | 181 | 0.685 |
| 6 | 127 | 184 | 0.690 |
| 7 | 129 | 188 | 0.686 |

The exact count rises monotonically — `24` new exact claims in six notes — but the **fraction** does
not: `0.693 ± 0.010`, with a slope of `−0.004` per note, which is inside the noise. New work is as mixed
as old work: the marginal note is `24/41 = 0.585` exact.

Two consequences, both exact about the process and not about the world:

- progress is **absolute**, not proportional. Purity does not improve; the number of exact objects does;
- the `31%` that is rhyme or false friend is not waste — it is the price of finding the `69%`, and it is
  stable, so it can be budgeted.

"The entirety of mathematics explained physically" is therefore an asymptote with a measured slope, not
a state to be reached. The honest restatement is: *a corpus whose exact column grows without bound, and
whose ratio does not.* That is what "close" means here.

## The zones of this note

- the four ceilings are exact mathematics, and they do not depend on the Fold;
- the definition of realization is a definition, not a claim;
- the three-class table is exact for the rows that name their class, and the class of a row is itself a
  judgement that can be audited;
- "this is what the corpus has been building" is a reading of the corpus, not a theorem about it. The
  audit is the table.

The one sentence: mathematics is not physics, but every structure has a price — nothing, a limit, or a
substance — and the corpus is the ledger of which price each one pays.
