/-
  Fold/Basic.lean

  The exact core of the Fold, in the smallest form that compiles.

  A fold is an involution.  Its fixed set is the crease, the scar, the
  horizon, or the critical line, depending on the instance.  Its orbits
  are the two sides.  The quotient of the orbits is the chart.  A cut is
  a retraction onto the fixed set that is constant on orbits; it is the
  observer.

  No Mathlib: the only import is `Init`.
-/
import Init

/-- A fold on a type `X`: an operation `f` with `f (f x) = x`.

The same structure carries the geometric fold, the navel inversion
`z ↦ ρ²/z̄` (on the appropriate domain), the conjugation `z ↦ z̄`, and
the reflection `k ↦ 1/k` on the completed parameter.  What changes
between instances is the space and the fixed set, not the shape. -/
structure Fold (X : Type) where
  f : X → X
  invol : ∀ x : X, f (f x) = x

namespace Fold

variable {X : Type}

/-- The fixed set of a fold: the crease, the scar, the horizon. -/
def Fix (F : Fold X) : X → Prop := fun x => F.f x = x

/-- The fold preserves its fixed set in both directions. -/
theorem fix_iff (F : Fold X) (x : X) : Fix F (F.f x) ↔ Fix F x := by
  unfold Fix
  rw [F.invol x]
  exact eq_comm

theorem fix_image (F : Fold X) {x : X} (h : Fix F x) : Fix F (F.f x) :=
  (fix_iff F x).2 h

theorem image_fix (F : Fold X) {x : X} (h : Fix F (F.f x)) : Fix F x :=
  (fix_iff F x).1 h

/-- The orbit of `x`: the point and its image.  These are the two sides
of the fold at `x`; when `x` is fixed, the two sides coincide. -/
def Orbit (F : Fold X) (x : X) : X → Prop := fun y => y = x ∨ y = F.f x

theorem orbit_self (F : Fold X) (x : X) : Orbit F x x := Or.inl rfl

theorem orbit_image (F : Fold X) (x : X) : Orbit F x (F.f x) := Or.inr rfl

/-- The fold permutes each orbit. -/
theorem orbit_invariant (F : Fold X) (x y : X) :
    Orbit F x (F.f y) ↔ Orbit F x y := by
  constructor
  · intro h
    rcases h with h | h
    · right
      calc
        y = F.f (F.f y) := (F.invol y).symm
        _ = F.f x := congrArg F.f h
    · left
      calc
        y = F.f (F.f y) := (F.invol y).symm
        _ = F.f (F.f x) := congrArg F.f h
        _ = x := F.invol x
  · intro h
    rcases h with h | h
    · rw [h]
      exact orbit_image F x
    · rw [h, F.invol x]
      exact orbit_self F x

/-- The orbit relation is symmetric: the two sides are the same orbit. -/
theorem orbit_symm (F : Fold X) {x y : X} (h : Orbit F x y) : Orbit F y x := by
  rcases h with h | h
  · rw [h]
    exact orbit_self F x
  · rw [h]
    exact Or.inr (F.invol x).symm

/-- The orbit relation is transitive: the sides compose. -/
theorem orbit_trans (F : Fold X) {x y z : X}
    (h1 : Orbit F x y) (h2 : Orbit F y z) : Orbit F x z := by
  rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2
  · rw [h2, h1]
    exact orbit_self F x
  · rw [h2, h1]
    exact orbit_image F x
  · rw [h2, h1]
    exact orbit_image F x
  · rw [h2, h1, F.invol x]
    exact orbit_self F x

/-- Orbits partition the space. -/
theorem orbit_equivalence (F : Fold X) : Equivalence (Orbit F) where
  refl := orbit_self F
  symm := orbit_symm F
  trans := orbit_trans F

/-- The setoid of orbits. -/
def orbitSetoid (F : Fold X) : Setoid X where
  r := Orbit F
  iseqv := orbit_equivalence F

/-- The chart: the quotient of the space by the fold. -/
def Chart (F : Fold X) : Type := Quotient (orbitSetoid F)

/-- The canonical projection to the chart. -/
def chart (F : Fold X) (x : X) : Chart F := Quotient.mk (orbitSetoid F) x

/-- Two points have the same chart iff they lie on the same orbit. -/
theorem chart_eq_iff (F : Fold X) (x y : X) :
    chart F x = chart F y ↔ Orbit F x y := by
  constructor
  · intro h
    exact Quotient.exact h
  · intro h
    exact Quotient.sound h

/-- The fold is invisible in the chart: it moves a point only within its
orbit.  This is the exact sense in which a fold is a change of chart and
not a change of the quotient. -/
theorem chart_fold (F : Fold X) (x : X) : chart F (F.f x) = chart F x :=
  Quotient.sound (orbit_symm F (orbit_image F x))

/-- Descent: a function that is constant on orbits factors through the
chart.  This is the quotient universal property, stated without any
choice of representative. -/
def desc {Y : Type} (F : Fold X) (g : X → Y)
    (h : ∀ x : X, g (F.f x) = g x) : Chart F → Y :=
  Quotient.lift g (fun a b hab => by
    rcases hab with rfl | rfl
    · rfl
    · exact (h a).symm)

/-- The descended map computes the original function on representatives. -/
theorem desc_chart {Y : Type} (F : Fold X) (g : X → Y)
    (h : ∀ x : X, g (F.f x) = g x) (x : X) :
    desc F g h (chart F x) = g x := rfl

/-- If a function separates orbits, its descent is injective.  This is
the converse of `chart_eq_iff` in the form a quotient map needs: equal
values force equal orbits, so no two orbits are merged. -/
theorem desc_injective {Y : Type} (F : Fold X) (g : X → Y)
    (h : ∀ x : X, g (F.f x) = g x)
    (sep : ∀ x y : X, g x = g y → Orbit F x y) :
    Function.Injective (desc F g h) := by
  intro q r
  refine Quotient.inductionOn q ?_
  intro x
  refine Quotient.inductionOn r ?_
  intro y hxy
  exact Quotient.sound (sep x y hxy)

/-- An invariant, separating, surjective function is the quotient map:
its descent is a bijection onto the target.  The Joukowski map
`J(z) = z + 1/z` is the instance where `Y` is the plane, `g = J`, and
the fiber of `J` is exactly the orbit `{z, 1/z}`. -/
theorem desc_bijective {Y : Type} (F : Fold X) (g : X → Y)
    (h : ∀ x : X, g (F.f x) = g x)
    (sep : ∀ x y : X, g x = g y → Orbit F x y)
    (surj : ∀ y : Y, ∃ x : X, g x = y) :
    Function.Injective (desc F g h) ∧ Function.Surjective (desc F g h) :=
  ⟨desc_injective F g h sep, fun y => by
    rcases surj y with ⟨x, hx⟩
    exact ⟨chart F x, by rw [desc_chart, hx]⟩⟩

/-- A cut: an observer's retraction onto the fixed set, constant on
orbits.  `p` sends every point to a fixed point and cannot distinguish
the two sides. -/
structure Cut (F : Fold X) where
  p : X → X
  image_fix : ∀ x : X, Fix F (p x)
  fix_eq : ∀ x : X, Fix F x → p x = x
  orbit_eq : ∀ x : X, p (F.f x) = p x

namespace Cut

variable {F : Fold X}

/-- A cut is idempotent: it lands on the fixed set. -/
theorem idem (C : Cut F) (x : X) : C.p (C.p x) = C.p x :=
  C.fix_eq (C.p x) (C.image_fix x)

/-- A cut cannot see the fold. -/
theorem invisible (C : Cut F) (x : X) : C.p (F.f x) = C.p x :=
  C.orbit_eq x

/-- A cut detects exactly the fixed set. -/
theorem fix_iff (C : Cut F) (x : X) : Fix F x ↔ C.p x = x := by
  constructor
  · exact C.fix_eq x
  · intro h
    have hfix : Fix F (C.p x) := C.image_fix x
    rwa [h] at hfix

/-- A cut is constant on each orbit. -/
theorem orbit_const (C : Cut F) {a b : X} (h : Orbit F a b) : C.p a = C.p b := by
  rcases h with rfl | rfl
  · rfl
  · exact (C.orbit_eq a).symm

/-- A cut factors through the chart. -/
def lift (C : Cut F) : Chart F → X :=
  Quotient.lift C.p (fun _a _b h => C.orbit_const h)

theorem lift_chart (C : Cut F) (x : X) : C.lift (chart F x) = C.p x := rfl

/-- The image of the lifted cut is fixed. -/
theorem lift_fix (C : Cut F) (q : Chart F) : Fix F (C.lift q) := by
  induction q using Quotient.ind with
  | _ x => exact C.image_fix x

end Cut

end Fold
