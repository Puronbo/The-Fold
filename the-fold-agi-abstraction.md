# Abstraction, concepts, and semantic structure

## The question

How can a system recognize that different objects, descriptions, or problems instantiate the same concept, while still retaining the differences that matter?

The AGI note defines premise closure as a test: a claim must be classified as exact, reformulation, rhyme, or false friend, and a non-exact claim must name the missing premise. This note adds the next capability: **constructing and reusing concepts across representations**.

The proposal is deliberately narrower than a definition of AGI. Concept formation is one capability an adaptive general system needs; it is not sufficient for general intelligence.

## 1. A concept is task-relative equivalence plus retained structure

Let X be a domain of observed instances. A task context c determines which distinctions matter. Define

\[
x \sim_c y
\quad\Longleftrightarrow\quad
\text{the task-relevant tests in context }c\text{ treat }x\text{ and }y\text{ as equivalent}.
\]

If the tests define an equivalence relation, its classes form a quotient:

\[
X/{\sim_c}.
\]

A concept is not simply a word attached to a class. It is a class together with the properties, relations, and permitted transformations that remain meaningful for the task.

For example, metres and centimetres are equivalent as descriptions of length after unit conversion. They are not equivalent as raw numerals, and the conversion does not make every numerical operation unit-independent.

The context subscript matters. Two objects can be equivalent for counting but not for colour; equivalent for collision prediction but not for chemical composition. There is no universal equivalence relation that is correct for every task.

**Exact:** quotienting by a genuine equivalence relation produces equivalence classes.

**Reformulation:** treating a learned concept as a task-relative quotient is a proposed architecture for concept representation.

## 2. The abstraction map

The quotient projection is

\[
q_c:X\to X/{\sim_c},\qquad q_c(x)=[x]_c.
\]

It maps each instance to its concept class. It is generally many-to-one: details irrelevant to context c are discarded.

A useful concept representation therefore has two parts:

\[
C_c(x)=\big(q_c(x),r_c(x)\big),
\]

where r_c(x) records task-relevant residual information that should not be erased by the abstraction.

This avoids a common failure: over-abstraction. If a system groups two instances together and later needs a distinction it discarded, it cannot recover that distinction from the quotient alone.

A robust learner should either preserve the residual, retain a reversible source reference, or explicitly report that the abstraction is lossy.

## 3. Concepts form a structured space

A collection of concepts can be ordered by inclusion of their extensions.

If concept A applies to every instance to which concept B applies, then

\[
B\subseteq A.
\]

For example:

\[
\text{sparrow}\subseteq\text{bird}\subseteq\text{animal}.
\]

This is a partial order, not necessarily a total order: two concepts can overlap without either containing the other.

Where the relevant meets and joins exist, concept families form a lattice. The meet represents the greatest shared specialization; the join represents the least common generalization. A learner must not assume every pair has a unique useful join in every representation.

A concept graph can encode:
- subclass and instance relations;
- part–whole relations;
- causal dependencies;
- temporal relations;
- analogies and structural correspondences;
- exceptions and context conditions.

These relation types must remain typed. “Part of,” “causes,” and “is a kind of” are not interchangeable edges.

## 4. The categorical view: representations and structure-preserving maps

A category C consists of objects, morphisms, identity morphisms, and associative composition.

For this application:
- objects may be representations of instances or models;
- morphisms may be admissible transformations between representations;
- composition represents successive transformations;
- identity means leaving a representation unchanged.

A functor

\[
F:\mathcal C\to\mathcal D
\]

maps objects to abstract representations and morphisms to abstract transformations while preserving identities and composition:

\[
F(1_X)=1_{F(X)},\qquad
F(g\circ f)=F(g)\circ F(f).
\]

This gives a precise criterion for a well-behaved abstraction across a family of transformations: the abstracted result should agree with abstracting after the original transformation, whenever the transformation is within the declared scope.

The commuting condition is

\[
q_Y\circ f = \bar f\circ q_X.
\]

Here f:X→Y is a concrete transformation, q_X,q_Y are abstraction maps, and \bar f is the corresponding abstract transformation.

The square commutes when both routes produce the same abstract result.

This is not a claim that all meanings are categorical or that a functor automatically discovers semantics. It is a formal tool for checking consistency once objects, maps, and abstraction rules have been specified.

## 5. Invariance is not sameness

A property I is invariant under a specified transformation family when

\[
I(f(x))=I(x)
\]

for every transformation f in that family.

Invariance can support recognition across changed viewpoints, units, or encodings. But invariance is always relative to a declared transformation family.

For example:
- Euclidean distance is invariant under rigid rotations and translations.
- Length is unchanged by a correct change of units, although its numerical coordinate changes.
- A photograph's pixel values are not invariant under lighting changes.
- Object identity is not guaranteed by any one visual feature.

A learner should record both the invariant and the transformations under which it is invariant. “Same concept” without a scope is underspecified.

## 6. A candidate concept-formation loop

A system can attempt concept formation through the following cycle:

1. **Collect instances.** Store observations with provenance and context.
2. **Propose distinctions.** Identify candidate features, relations, and constraints.
3. **Propose equivalences.** Group instances only relative to a declared task.
4. **Test consistency.** Check reflexivity, symmetry, and transitivity if an equivalence quotient is claimed.
5. **Find invariants.** Test which properties survive the transformations in scope.
6. **Retain residuals.** Preserve distinctions needed by other tasks or mark the abstraction as lossy.
7. **Construct relations.** Link concepts using typed relations.
8. **Generate predictions.** Derive consequences from the proposed concept.
9. **Seek counterexamples.** Try to separate instances that were grouped.
10. **Revise or reject.** Update the concept, its scope, or its evidence.

The loop must be able to split a concept as well as merge concepts. A system that only accumulates categories will preserve early mistakes.

## 7. A concrete example: the same equation in different clothes

Consider the system

\[
a+b=10,\quad b+c=12,\quad a+c=8.
\]

Its solution is (a,b,c)=(3,7,5).

Renaming the variables to (x,y,z) does not change the structure. Expressing the same equations as a weighted graph also preserves the underlying constraint system if the node and edge meanings are mapped correctly.

But replacing the three equations with only their sum gives

\[
2(a+b+c)=30.
\]

That abstraction preserves the total a+b+c=15, but loses enough information that the three individual values cannot be reconstructed.

Thus:
- variable renaming is a reversible representation change;
- a faithful graph encoding can be an isomorphic representation;
- retaining only the total is a lossy abstraction.

A capable system must tell these cases apart.

## 8. Premise closure applied to concepts

The existing four-zone gate can be extended from claims to concept mappings.

For every proposed mapping, emit:

| Field | Required content |
|---|---|
| Source | The original instance or representation |
| Target | The proposed concept or abstract representation |
| Context | The task for which the mapping is claimed |
| Preserved structure | Relations and properties that survive |
| Discarded structure | Information removed by abstraction |
| Evidence | Proof, data, or explicit assumptions |
| Zone | exact / reformulation / rhyme / false friend |
| Missing premise | What would make a non-exact mapping exact |

A mapping is not exact merely because two descriptions look alike. The relevant structures and the map between them must be specified.

This extends the original premise-closure discipline without weakening it.

## 9. A falsifiable evaluation protocol

Use paired tasks with transformations that preserve the declared structure, alongside hard negatives that look similar but do not preserve it.

For each task, score:

1. **Recognition:** does the system identify the intended equivalence?
2. **Scope:** does it state the context in which the equivalence holds?
3. **Preservation:** does it identify the correct invariants?
4. **Residual awareness:** does it name information discarded?
5. **Transfer:** can it solve a new instance after a representation change?
6. **Counterexample response:** does it revise the concept when a valid counterexample appears?
7. **Calibration of claim type:** does it distinguish proof from analogy?

A benchmark should hold out transformation families and compositional combinations, not merely new surface examples. Otherwise a model can memorize the test distribution without learning the underlying structure.

The test must also include cases where the right answer is “not equivalent under this task.”

## 10. Relation to the Fold

The Fold's quotient construction already provides a small exact model of abstraction.

For an involution F, the orbit relation identifies

\[
y=x\quad\text{or}\quad y=F(x).
\]

The quotient chart identifies the two representatives. The existing Lean results Fold.orbit_equivalence, Fold.chart_eq_iff, and Fold.desc establish that:
- the orbit relation is an equivalence;
- equal chart values correspond exactly to the same orbit;
- a function constant on orbits descends to the quotient.

That is an exact mathematical instance of representation-invariant abstraction.

It is not yet a general concept learner. The Fold supplies a specified involution and quotient; an AGI system would have to discover useful transformations, infer task context, test candidate invariants, and revise its concepts from evidence.

## 11. Eigenprime boundary

An Eigenprime signature can be treated as one possible feature map:

\[
A\mapsto\operatorname{Spec}(A)\cap\mathbb P.
\]

It is invariant under similarity, but it is lossy and does not classify arbitrary operators up to similarity. Equality of Eigenprime signatures does not imply equality of spectra or equivalence of the represented systems.

Therefore it may contribute a structural feature to a concept representation, but it cannot serve as a universal semantic identity test.

## 12. The proposed AGI extension

Extend the architecture in the existing AGI note with a concept layer:

\[
\mathcal A_{\rm concept}
=
(X,\mathcal C,\sim_c,q_c,\mathcal R,\mathcal T,\mathcal I,\mathcal E,\mathcal V).
\]

Where:
- X: observed instances and representations;
- C: task contexts;
- \sim_c: context-dependent equivalence;
- q_c: abstraction or quotient map;
- R: typed relations;
- T: admissible transformations;
- I: tested invariants;
- E: evidence, counterexamples, and provenance;
- V: verification and evaluation.

The system should maintain multiple abstractions of the same instance when different tasks require different distinctions. A single irreversible compression is not a sufficient universal memory.

## 13. The zones of this note

- The quotient construction, equivalence-relation requirements, partial orders, and functor laws are **exact** mathematical statements.
- The Fold orbit quotient is an **exact** existing formal instance.
- The concept architecture and learning loop are **reformulations**: proposed engineering structures, not theorems that guarantee intelligence.
- The claim that this architecture alone produces AGI is a **rhyme**, not a result.
- Treating a shared label or visual resemblance as proof of semantic equivalence is a **false friend**.

## The one sentence

**A useful concept is a task-scoped abstraction that groups what can be treated alike, preserves the relationships needed for reasoning, and records what it has deliberately forgotten.**

The next test is not to add more definitions. It is to implement one small concept learner that proposes equivalence classes, checks their laws, preserves residual information, and revises a class when a counterexample appears.


## 14. Executable prototype: FoldConcept

The first small learner is implemented in `tools/FoldConcept.py` (standard library only).

It provides:
- records with stable identifiers, feature values, and provenance;
- explicit task contexts listing the features relevant to a task;
- a quotient classifier induced by equality of projected feature signatures;
- finite exhaustive checks of reflexivity, symmetry, and transitivity;
- concept views that retain the original source record and identify features omitted from the current projection;
- counterexample-driven context refinement, which adds a feature only when it actually separates a pair previously grouped together;
- a held-out-instance check showing that a new record can map to an existing task-relative class.

Run it with:

```sh
python tools/FoldConcept.py
```

The regression suite contains nine checks. The implementation is intentionally explicit: it does not infer features, choose a task context, or discover semantic equivalence by itself. The equivalence classes are exact relative to the supplied feature projection; whether those features are appropriate is an empirical and task-dependent question.

This prototype demonstrates a narrow executable loop — project, group, preserve residual, test, refine — not autonomous concept discovery, general reasoning, or AGI. The next engineering step is to let a model propose candidate features and contexts, while an independent verifier checks the resulting partitions and records counterexamples.


## 15. Constraint-guided Fold feedback loop

`tools/FoldLoop.py` adds a deterministic feedback controller around the concept learner.

The caller supplies:
- observations with stable identifiers and preserved provenance;
- a starting task context;
- candidate features proposed by an upstream model or researcher;
- pair constraints, each explicitly marked as must-link (same concept) or cannot-link (different concepts), with an optional reason.

The loop audits the current abstraction, then greedily selects a candidate feature that separates the largest number of currently violated cannot-link pairs without splitting any must-link pair. Every selected feature and the pairs it separates are recorded. If the constraints conflict or the available features cannot resolve them, the loop returns the remaining violations instead of pretending success.

Run from the repository root:

```sh
python tools/FoldConcept.py
python tools/FoldLoop.py
```

The loop is deterministic and does not execute model-generated code. It is a constrained feature-selection baseline, not semantic understanding. In particular, correctness depends on the quality and consistency of the supplied pair constraints; the greedy strategy is not guaranteed to find a solution whenever one exists. Its value is that a model's proposed abstraction becomes inspectable and falsifiable before it is accepted.


## 16. Append-only, auditable memory

`tools/FoldMemory.py` adds a persistent JSONL event ledger.

Each event records:
- event type and subject;
- content, task, and source provenance;
- confidence in the range 0–1;
- tags for retrieval;
- an optional reference to the event it supersedes;
- the previous event digest and its own SHA-256 digest.

Corrections append a new event; they do not erase the earlier claim. Normal recall hides superseded claims by default, while audit recall can include the full history. The verifier checks sequence numbers, the digest chain, and optionally a separately retained expected head digest. Retaining that expected head is important: a hash chain alone cannot detect an attacker who rewrites the entire ledger and recomputes every digest.

Run:

```sh
python tools/FoldMemory.py
```

The module uses only the Python standard library. Its tests cover provenance, task/tag retrieval, append-only correction, audit history, chain validation, truncation detection against a trusted head, and tamper detection.

The memory is a local prototype. It does not provide encryption, access control, multi-process locking, semantic retrieval, or protection if an attacker can alter both the ledger and its trusted head. Confidence is recorded metadata, not a calibrated probability.

The intended architecture now has three separable layers: concept projection (`FoldConcept`), constraint/counterexample refinement (`FoldLoop`), and auditable persistent history (`FoldMemory`). A future model can propose memories and abstractions, but it must not be allowed to rewrite the evidence or certify its own claims.
