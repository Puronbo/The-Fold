import Init

namespace Fold.Complexity

universe u
variable {Lang : Type u}

/-- Languages accepted in NP but not in P. -/
def NPResidual (PClass NPClass : Lang → Prop) : Lang → Prop :=
  fun L => NPClass L ∧ ¬ PClass L

/-- The residual vanishes when every NP language is also in P. -/
def ResidualZero (PClass NPClass : Lang → Prop) : Prop :=
  ∀ L, NPClass L → PClass L

/-- A language witnessing a nonempty NP-over-P residual. -/
def SeparationWitness (PClass NPClass : Lang → Prop) : Prop :=
  ∃ L, NPResidual PClass NPClass L

theorem class_eq_iff_residual_zero
    (PClass NPClass : Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L) :
    (∀ L, PClass L ↔ NPClass L) ↔ ResidualZero PClass NPClass := by
  constructor
  · intro heq L hNP
    exact (heq L).2 hNP
  · intro hzero L
    constructor
    · exact hsub L
    · intro hNP
      exact hzero L hNP

theorem class_ne_iff_residual_nonempty
    (PClass NPClass : Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L) :
    (¬ ∀ L, PClass L ↔ NPClass L) ↔ SeparationWitness PClass NPClass := by
  constructor
  · intro hne
    apply Classical.byContradiction
    intro hnone
    apply hne
    intro L
    constructor
    · exact hsub L
    · intro hNP
      cases Classical.em (PClass L) with
      | inl hP => exact hP
      | inr hnotP => exact False.elim (hnone ⟨L, hNP, hnotP⟩)
  · intro hex heq
    cases hex with
    | intro L hres =>
      exact hres.2 ((heq L).2 hres.1)

end Fold.Complexity
