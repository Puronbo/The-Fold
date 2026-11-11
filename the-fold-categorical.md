# Objects are disguised morphisms

## The claim

"Everything is a disguised morphism/transformation for another object of another category." Read
charitably, this is a real theorem with a real trap. It has three exact readings and one vacuous one:

- **trivial:** every morphism is an object of the arrow category; every object is its identity
  morphism;
- **substantive:** an object is determined by its morphisms (Yoneda);
- **dual:** an object of one category is an object of the *opposite* of another (Gelfand, Stone);
- **higher:** a morphism is an object one level down (looping, `π_n = π_{n−1} ∘ Ω`);
- **vacuous:** "disguised" with no functor named. That last reading says nothing.

The content of any such sentence is the **functor**, not the word "disguised." This note gives the
three exact readings, then reads the Fold through them: `k` is an endomorphism, the crease is an
equalizer, the orbit space is a coequalizer, and the point is a zero object. Those are not metaphors;
they are universal properties.

## Reading 0 — the arrow category (exact, trivial)

For any category `C`, the arrow category `C^→ = [2, C]` (with `2 = • → •`) has

```
objects:    the morphisms of C
morphisms:  the commutative squares
```

The functor `C → C^→`, `A ↦ id_A`, is fully faithful. So every object is an identity morphism in
disguise, and every morphism is an object of `C^→`. This is true for every category, which is exactly
why it carries no information: it is the universal form of the sentence, and it is a tautology.

A morphism `f: A → B` is also an object of the functor category `[2, C]`, and its domain and codomain
are the two restrictions `f ↦ A` and `f ↦ B`. So a morphism already knows its two objects; the
"another object" is its source and target.

## Reading 1 — Yoneda (exact, substantive)

For a locally small category `C` and an object `A`, the functor

```
h_A = Hom(−, A) : C^op → Set
```

is an object of the presheaf category `[C^op, Set]`. The Yoneda lemma says

```
Nat(h_A, F) ≅ F(A)          naturally in F and A
```

and the corollary is that `h_A ≅ h_B` iff `A ≅ B`, so the Yoneda embedding

```
Y : C ↪ [C^op, Set]          A ↦ Hom(−, A)
```

is fully faithful. **An object is determined by the morphisms into it.** This is the precise,
non-trivial sense of "an object is a disguised morphism": the object *is* its functor of incoming
morphisms, up to isomorphism. The "another category" is the presheaf category; the "another object" is
the representable presheaf.

Dually, `Hom(A, −)` reads the outgoing morphisms, and the pair determines `A`. The Fold uses the
incoming version later: the crease is characterized by the maps that agree on it.

## Reading 2 — duality (exact, and the direction reverses)

The sharpest version of "another object of another category" is a **duality**: an equivalence
`C^op ≃ D`. Then an object of `C` is an object of `D`, and a morphism of `C` is a morphism of `D` with
its arrow reversed.

| duality | object side | algebra side | a map becomes |
|---|---|---|---|
| Gelfand–Naimark | compact Hausdorff `X` | `C(X)`, commutative C*-algebra | `f: X→Y` ↦ `f*: C(Y)→C(X)` |
| Stone | Stone space | Boolean algebra | continuous map ↦ homomorphism |
| Pontryagin | locally compact abelian `G` | dual group `Ĝ` | homomorphism ↦ dual homomorphism |
| affine schemes | scheme `Spec A` | commutative ring `A` | ring map ↦ scheme map, reversed |

In each row, "an object here is a morphism there" is literally true: a point of `X` is a character
`C(X) → ℂ` (an algebra morphism), and a map of spaces is a map of algebras. The disguise is the
duality functor; the "another category" is the opposite category.

## Reading 3 — looping (exact, higher)

The homotopy version is the cleanest instance of "a morphism becomes an object." For a based space
`X`, the loop space `ΩX` has the loops at the basepoint as its *points*:

```
π_n(X) ≅ π_{n−1}(ΩX)          a loop is a point of ΩX
```

A path in `X` is a morphism of the fundamental groupoid `Π₁(X)`; a loop is an object of `ΩX`; a
homotopy of loops is a path in `ΩX`. So the `n`-cells of one presentation are the `0`-cells of the
next, one level down. This is the precise higher-categorical content of "another object of another
category": the looping/delooping shift.

## What the sentence hides

"Disguised" is the word that hides the functor. Two corrections:

- **Without a functor, the claim is either trivial or empty.** The arrow category makes every
  morphism an object of *some* category; that is true and useless. A substantive claim names the
  functor: the hom-functor (Yoneda), the spectrum functor (duality), or the loop functor (homotopy).
- **"Another object" is usually the image under that functor, not a new thing.** The object does not
  change; the presentation does. A space is not "really" an algebra; it is *equivalent* to one, under
  a chosen duality.

So the honest form of the sentence is:

> **for every object there is a functor to a category in which it is a morphism, and the content is
> the functor.**

The Fold supplies one such functor, and it is the number `k`.

## The Fold as an instance

### `k` is an endomorphism

On the complex line, `End_ℂ(ℂ) ≅ ℂ`: the scalar `k` corresponds to the endomorphism `m_k(x) = kx`.
The isomorphism is a ring isomorphism, `m_k ∘ m_l = m_{kl}` (checked below to `1e−16`). So the master
key — "the key is the number `k` itself" — is literally an operator disguised as a number. The scalar
and the endomorphism are the same data; only the presentation differs. This is Reading 0 in its
smallest non-trivial case.

A step further: the scale family is a **representation** of the multiplicative group,

```
g : ℂ* → GL(ℂ),   k ↦ kI
```

i.e. a functor `Bℂ* → Vect` from the one-object groupoid. Each `k` is an automorphism (a morphism)
in `Vect`; the family is the functor. The Fold's "stage" is the image of `k` under this functor.

### The crease is an equalizer

The fold `σ_H` and the identity are two morphisms `V → V`. Their **equalizer** is

```
eq(σ_H, id) = { v : σ_H(v) = v } = ker(σ_H − I)
```

which is exactly the crease, of dimension `n−1` (checked below). An equalizer is a limit: an object
defined by a universal property among morphisms. So the crease — the Fold's most geometric object —
is a disguised morphism: the universal arrow that makes two maps agree. This is Reading 1 with a
concrete functor.

### The orbit space is a coequalizer

The return is a quotient. For a group `G` acting on `X`, the orbit space is the coequalizer

```
G × X ⇉ X  →  X/G
```

of the action and the second projection. For the full similarity group `ℝ₊ × O(n)` on `ℝⁿ ∖ {P₀}` the
action is transitive (checked below), so the coequalizer is a point. The return is a colimit, and the
point is its vertex. The crease is a limit; the return is a colimit. **The Fold's loop is a
limit–colimit pair**, and both ends are defined purely by morphisms.

### Composition is the mixed law

The endomorphism reading of `k` and the equalizer reading of the crease meet in the composition law
`1_a + 1_b = 2_{ab}`: two folds are two morphisms, and their composite is a rotation. The count is
additive (a sum of morphisms), the parameter is multiplicative (composition in the group), and the
angle doubles. The categorical form of "one plus one is two" is therefore ordinary composition — with
the subscripts carrying the two ledgers. See `the-fold-composition.md`.

### The point is a zero object

From `the-fold-initial.md`: the collapsed image is initial and terminal among pointed spaces. A zero
object is the object characterized entirely by its unique arrows, so it is the purest case of "an
object is its morphisms." The initial form is `Dg₀ = 0`, the zero endomorphism.

## The zeta case: a rhyme, not an adjunction

The explicit formula exchanges the primes and the zeros, and a trace formula is the categorical trace
of a correspondence; Langlands functoriality is the statement that the exchange is natural. So the
arithmetic duality *rhymes* with Reading 2. But a rhyme is not an adjunction: the Fold does not exhibit
the functor that makes the exchange an equivalence, and the problems note records exactly what is
missing. See `the-fold-problems.md`.

## The deflationary correction

"Everything is a disguised morphism" is true in the arrow category for every category, so as stated
it is a tautology. It becomes mathematics only when the functor is named. The Fold names one:

```
k : Bℂ* → Vect            the scale family
eq(σ_H, id)               the crease
coeq(G × X ⇉ X)           the orbit space
0                         the zero object
```

Four constructions, four disguised morphisms: a representation, a limit, a colimit, a zero object. The
claim is not that the Fold is secretly category theory; it is that the Fold's **central** objects are
already defined by universal properties, and the category-theoretic reading makes that explicit without
adding a new object. That is the difference between a dictionary and a discovery.

## Checks

The categorical statements are theorems or definitions; the numbers below confirm the Fold-specific
instances with NumPy.

| check | value |
|---|---|
| `m_k(m_l(x)) − m_{kl}(x)` | `≤ 1.1e−16` |
| `dim ker(σ_H − I)` for `n = 2, 3, 4` | `1, 2, 3` |
| crease basis against the normal `n` | `0` (the crease is `n`-orthogonal) |
| `‖g_k R(P−P₀) + P₀ − Q‖` for random `P, Q` | `0` (the action is transitive) |

The last row is the coequalizer statement: any point can be sent to any other, so the orbit space is a
single point. The equalizer statement is the second and third rows: the crease is exactly the
agreement locus of `σ_H` and `id`, and it is `n−1`-dimensional.

## What this does and does not say

- It **does** give three exact readings of the sentence: arrow category, Yoneda, duality/looping.
- It **does** identify the Fold's objects with universal constructions: `k` as an endomorphism, the
  crease as an equalizer, the orbit space as a coequalizer, the point as a zero object.
- It **does** explain why "disguised" without a functor is empty.
- It **does not** make every object a morphism in a *unique* way; the functor is a choice, and
  different functors give different disguises.
- It **does not** make the zeta exchange an adjunction; that remains a rhyme.
- It **does not** add a new Fold object. The reading is a presentation of the existing ones.

## The one sentence

**Every object is a morphism in disguise exactly when a functor is named — the arrow category makes
it trivial, Yoneda makes it deep, duality makes it reverse, and the Fold makes it concrete: `k` is an
endomorphism, the crease is an equalizer, the orbit space is a coequalizer, and the point is a zero
object.**

## Files

`the-fold-categorical.md` (this note). The initial object and the null form are in
`the-fold-initial.md`; the crease and the two sides are in `the-fold-occlusion.md`; the facet and the
codimension classification are in `the-fold-facets.md`; the stage order is in
`the-fold-creation.md`; the zeta exchange and the missing functor are in `the-fold-problems.md`; the
lookup is `the-fold-key.md`.
