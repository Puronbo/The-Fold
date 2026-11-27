import Fold.Basic

/-!
  Fold/Counterexamples.lean

  An involution need not have a fixed point, and therefore need not admit
  a cut/retraction onto its fixed set. This separates the quotient-orbit
  construction from the extra structure required by an observer cut.
-/

namespace Fold

/-- The fixed-point-free swap of the two Boolean values. -/
def booleanSwap : Fold Bool where
  f := fun b => !b
  invol := by
    intro b
    cases b <;> rfl

/-- Neither Boolean value is fixed by the swap. -/
theorem booleanSwap_no_fixed (b : Bool) : ¬ Fix booleanSwap b := by
  cases b <;> simp [Fix, booleanSwap]

/-- No cut can retract this fold onto its empty fixed set. -/
theorem booleanSwap_no_cut : ¬ Nonempty (Cut booleanSwap) := by
  intro h
  rcases h with ⟨C⟩
  exact (booleanSwap_no_fixed (C.p false)) (C.image_fix false)

end Fold
