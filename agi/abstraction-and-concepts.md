# Abstraction, concepts, and semantic structure

## Question

How can a system recognize that different objects, descriptions, or problems instantiate the same concept, while retaining the differences that matter?

The AGI programme in the parent note uses premise closure: classify a claim as exact, reformulation, rhyme, or false friend, and name the missing premise whenever the claim is not exact. This note adds a proposed capability: construct and reuse concepts across representations.

Concept formation is one capability a general intelligent system needs. It is not, by itself, a definition or sufficient condition for AGI.

## 1. Task-relative equivalence

Let X be a domain of observed instances. A task context c determines which distinctions matter. Define

\[
x\sim_c y
\]

when the task-relevant tests in context c treat x and y as equivalent.

If and only if this relation is reflexive, symmetric, and transitive, it partitions X into equivalence classes:

\[
X/{\sim_c}.
\]

A concept is not merely a word attached to a class. It is a class together with the properties, relations, and transformations that remain meaningful for the task.

Metres and centimetres are equivalent as descriptions of length after unit conversion. They are not equivalent as raw numerals, and this conversion does not make every numerical operation unit-independent.

The context subscript matters. Two objects can be equivalent for counting but not for colour; equivalent for collision prediction but not for chemical composition. No single equivalence relation is automatically correct for every task.

- **Exact:** quotienting by a genuine equivalence relation produces equivalence classes.
- **Reformulation:** treating a learned concept as a task-relative quotient is a proposed architecture for concept representation.

## 2. Abstraction map and residual information

The quotient projection is

\[
q_c:X\to X/{\sim_c},\qquad q_c(x)=[x]_c.
\]

It maps each instance to its concept class. It is generally many-to-one: details irrelevant to context c are discarded.

A useful concept representation therefore retains both the abstract class and task-relevant residual information:

\[
C_c(x)=\big(q_c(x),r_c(x)\big).
\]

The residual r_c(x) records distinctions that another task may need. If a system groups two instances and later needs a distinction it discarded, that distinction cannot be recovered from the quotient alone.

A robust learner should preserve residuals, retain a reversible source reference, or explicitly mark the abstraction as lossy.

## 3. Concept order and typed relations

A collection of concepts can be ordered by inclusion of their extensions. If every instance of B is an instance of A, then

\[
B\subseteq A.
\]

For example:

\[
\text{sparrow}\subseteq\text{bird}\subseteq\text{animal}.
\]

This is a partial order, not necessarily a total order: two concepts can overlap without either containing the other.

Where the relevant meets and joins exist, concept families form a lattice. A meet gives a greatest shared specialization; a join gives a least common generalization. A learner must not assume every pair has a unique useful join in every representation.

A concept graph may encode subclass, instance, part–whole, causal, temporal, analogical, and structural relations. These relation types must remain typed. “Part of,” “causes,” and “is a kind of” are not interchangeable edges.

## 4. Categorical representation

A category consists of objects, morphisms, identity morphisms, and associative composition. For this application, objects may be representations of instances or models; morphisms may be admissible transformations between them.

A functor

\[
F:\mathcal C\to\mathcal D
\]

maps objects and morphisms while preserving identities and composition:

\[
F(1_X)=1_{F(X)},\qquad
F(g\circ f)=F(g)\circ F(f).
\]

This gives a consistency condition for abstraction. If f:X→Y is a concrete transformation, q_X and q_Y are abstraction maps, and \bar f is the abstract transformation, require

\[
q_Y\circ f=\bar f\circ q_X.
\]

The diagram commutes when both routes produce the same abstract result.

This does not mean that all meaning is categorical or that a functor discovers semantics automatically. It is a formal test once the objects, maps, and abstraction rules have been specified.

## 5. Invariance is scoped

A property I is invariant under a transformation family when

\[
I(f(x))=I(x)
\]

for every transformation f in that family.

Invariance can support recognition across changed viewpoints, units, or encodings, but it is always relative to a declared family:
- Euclidean distance is invariant under rigid rotations and translations.
- Length is unchanged by a correct unit conversion, although its numerical coordinate changes.
- Pixel values are not invariant under arbitrary lighting changes.
- No single visual feature guarantees object identity.

“Same concept” without a task and a transformation scope is underspecified.

## 6. Candidate concept-formation loop

A proposed learner can use this cycle:

1. Collect instances with context and provenance.
2. Propose distinctions, features, relations, and constraints.
3. Propose equivalences only relative to a declared task.
4. Check reflexivity, symmetry, and transitivity before claiming a quotient.
5. Test which properties survive the transformations in scope.
6. Preserve residual information or mark the abstraction as lossy.
7. Construct typed relations between concepts.
8. Generate predictions from the proposed concept.
9. Search for counterexamples that separate grouped instances.
10. Revise, split, merge, or reject the concept.

The loop must be able to split concepts as well as merge them. A system that only accumulates categories preserves early mistakes.

## 7. Example: equivalent equations, lossy summary

Consider

\[
a+b=10,\quad b+c=12,\quad a+c=8.
\]

The solution is (a,b,c)=(3,7,5). Renaming the variables to (x,y,z) preserves the structure. A faithful graph encoding can also preserve the constraint system if node and edge meanings are mapped correctly.

But adding the three equations and retaining only the sum gives

\[
2(a+b+c)=30.
\]

This preserves a+b+c=15 but loses enough information that the three individual values cannot be reconstructed.

Thus variable renaming is reversible; a faithful graph encoding can be isomorphic; retaining only the total is lossy. A capable system must distinguish these cases.

## 8. Premise closure for concept mappings

For every proposed mapping, record:

| Field | Required content |
|---|---|
| Source | Original instance or representation |
| Target | Proposed concept or abstract representation |
| Context | Task for which equivalence is claimed |
| Preserved structure | Relations and properties that survive |
| Discarded structure | Information removed |
| Evidence | Proof, data, or explicit assumptions |
| Zone | exact / reformulation / rhyme / false friend |
| Missing premise | What would make a non-exact mapping exact |

A mapping is not exact merely because two descriptions look alike. The relevant structures and the map between them must be specified.

## 9. Falsifiable evaluation

Use paired tasks with transformations that preserve the declared structure, alongside hard negatives that look similar but do not preserve it.

Score:
1. recognition of the intended equivalence;
2. explicit scope and context;
3. identification of preserved invariants;
4. awareness of discarded information;
5. transfer to a new instance after representation change;
6. revision after a valid counterexample;
7. distinction between proof and analogy.

Hold out transformation families and compositional combinations, not merely new surface examples. Include cases where the correct answer is “not equivalent under this task.” Otherwise the system may memorize the test distribution.

## 10. The Fold as an exact small model

The Fold's quotient construction supplies a small exact instance of abstraction.

For an involution F, the orbit relation identifies y=x or y=F(x). The quotient chart identifies the two representatives. The existing Lean results Fold.orbit_equivalence, Fold.chart_eq_iff, and Fold.desc establish:
- the orbit relation is an equivalence;
- equal chart values correspond exactly to the same orbit;
- a function constant on orbits descends to the quotient.

This is an exact mathematical instance of representation-invariant abstraction. It is not yet a general concept learner. The Fold supplies a specified involution and quotient; an AGI system would need to discover useful transformations, infer task context, test invariants, and revise concepts from evidence.

## 11. Eigenprime boundary

An Eigenprime signature is one possible feature map:

\[
A\mapsto\operatorname{Spec}(A)\cap\mathbb P.
\]

It is invariant under similarity, but it is lossy and does not classify arbitrary operators up to similarity. Equality of Eigenprime signatures does not imply equality of spectra or equivalence of represented systems.

It may contribute a structural feature to a concept representation, but it cannot serve as a universal semantic identity test.

## 12. Proposed AGI concept layer

Extend the parent architecture with

\[
\mathcal A_{\rm concept}
=
(X,\mathcal C,\sim_c,q_c,\mathcal R,\mathcal T,\mathcal I,\mathcal E,\mathcal V).
\]

Here X is the instance domain; C is the set of task contexts; \sim_c is context-dependent equivalence; q_c is the abstraction map; R is typed relations; T is admissible transformations; I is tested invariants; E is evidence, counterexamples, and provenance; V is verification and evaluation.

The system should maintain multiple abstractions of the same instance when different tasks require different distinctions. A single irreversible compression is not a sufficient universal memory.

## 13. Executable prototype

The first deterministic prototype is in `agi/concept_learner.py`, with standard-library tests in `agi/test_concept_learner.py`.

Run from the repository root:

```sh
python -m unittest agi.test_concept_learner
python agi/concept_learner.py
```

The learner stores original instance payloads, accepts scored candidate-equivalence links, and accepts explicit counterexamples. It rebuilds a partition in descending confidence order, rejecting a proposed merge if it would violate a counterexample. Thus a new counterexample can split a previously formed class without deleting the observations or evidence.

This is **not** autonomous concept discovery: the candidate links and counterexamples are supplied explicitly. Confidence is a prioritization heuristic, not a calibrated probability. The prototype is a controlled test bed for partition consistency, evidence conflict, and preservation of residual data.

## 14. Zones and status

- The quotient construction, equivalence-relation requirements, partial orders, and functor laws are **exact** mathematics.
- The Fold orbit quotient is an **exact** existing formal instance.
- The concept architecture and learning loop are **reformulations**: proposed engineering structures, not theorems that guarantee intelligence.
- The claim that this architecture alone produces AGI is a **rhyme**, not a result.
- Treating a shared label or visual resemblance as proof of semantic equivalence is a **false friend**.

## The one sentence

**A useful concept is a task-scoped abstraction that groups what can be treated alike, preserves the relationships needed for reasoning, and records what it has deliberately forgotten.**

The next test is implementation: build a small concept learner that proposes equivalence classes, checks their laws, preserves residual information, and revises a class when a counterexample appears.
