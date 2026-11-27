import Init

namespace Fold.Complexity

universe u

/-- A polynomial-time many-one reduction between two decision problems.
    The runtime predicate is explicit: a bare computable map is not enough. -/
structure PolyManyOneReduction
    (A B : Type u)
    (acceptA : A → Prop)
    (acceptB : B → Prop)
    (PolyTime : (A → B) → Prop) where
  map : A → B
  preserves : ∀ a, acceptA a ↔ acceptB (map a)
  cost : PolyTime map

/-- Polynomial-time reductions compose when the chosen runtime predicate
    is closed under function composition. -/
def composePolyManyOne
    {A B C : Type u}
    {acceptA : A → Prop} {acceptB : B → Prop} {acceptC : C → Prop}
    {PolyTimeAB : (A → B) → Prop}
    {PolyTimeBC : (B → C) → Prop}
    {PolyTimeAC : (A → C) → Prop}
    (RAB : PolyManyOneReduction A B acceptA acceptB PolyTimeAB)
    (RBC : PolyManyOneReduction B C acceptB acceptC PolyTimeBC)
    (PolyTimeComp : ∀ f g, PolyTimeAB f → PolyTimeBC g →
      PolyTimeAC (fun a => g (f a)))
    : PolyManyOneReduction A C acceptA acceptC PolyTimeAC where
  map := fun a => RBC.map (RAB.map a)
  preserves := by
    intro a
    exact (RAB.preserves a).trans (RBC.preserves (RAB.map a))
  cost := PolyTimeComp RAB.map RBC.map RAB.cost RBC.cost

/-- The composed map preserves yes-instances exactly. -/
theorem composed_membership_iff
    {A B C : Type u}
    {acceptA : A → Prop} {acceptB : B → Prop} {acceptC : C → Prop}
    {PTAB : (A → B) → Prop} {PTBC : (B → C) → Prop}
    (RAB : PolyManyOneReduction A B acceptA acceptB PTAB)
    (RBC : PolyManyOneReduction B C acceptB acceptC PTBC)
    (a : A) :
    acceptA a ↔ acceptC (RBC.map (RAB.map a)) :=
  (RAB.preserves a).trans (RBC.preserves (RAB.map a))

end Fold.Complexity
