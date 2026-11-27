import Init

namespace Fold.Complexity

universe u
variable {Lang : Type u}

/-- Languages accepted in NP but not in P. -/
def NPResidual (PClass NPClass : Lang → Prop) : Lang → Prop :=
  fun L => NPClass L ∧ ¬ PClass L

/-- The residual is zero when no NP language lies outside P. -/
def ResidualZero (PClass NPClass : Lang → Prop) : Prop :=
  ∀ L, ¬ NPResidual PClass NPClass L

/-- A language witnessing a nonempty NP-over-P residual. -/
def SeparationWitness (PClass NPClass : Lang → Prop) : Prop :=
  ∃ L, NPResidual PClass NPClass L

theorem class_eq_iff_residual_zero
    (PClass NPClass : Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L) :
    (∀ L, PClass L ↔ NPClass L) ↔ ResidualZero PClass NPClass := by
  constructor
  · intro heq L hres
    exact hres.2 ((heq L).2 hres.1)
  · intro hzero L
    constructor
    · exact hsub L
    · intro hNP
      by_contra hnotP
      exact hzero L ⟨hNP, hnotP⟩

theorem class_ne_iff_residual_nonempty
    (PClass NPClass : Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L) :
    (¬ ∀ L, PClass L ↔ NPClass L) ↔ SeparationWitness PClass NPClass := by
  constructor
  · intro hne
    by_contra hnone
    apply hne
    intro L
    constructor
    · exact hsub L
    · intro hNP
      by_contra hnotP
      exact hnone ⟨L, hNP, hnotP⟩
  · rintro ⟨L, hNP, hnotP⟩ heq
    exact hnotP ((heq L).2 hNP)

/-- Boolean collapse indicator: zero for equality, one for separation. -/
def CollapseBit (PClass NPClass : Lang → Prop) : Nat :=
  if ResidualZero PClass NPClass then 0 else 1

theorem collapse_bit_zero_iff
    (PClass NPClass : Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L) :
    CollapseBit PClass NPClass = 0 ↔
      (∀ L, PClass L ↔ NPClass L) := by
  unfold CollapseBit
  by_cases hz : ResidualZero PClass NPClass
  · have heq := (class_eq_iff_residual_zero PClass NPClass hsub).2 hz
    simp [hz, heq]
  · have hne : ¬ (∀ L, PClass L ↔ NPClass L) := by
      intro heq
      exact hz ((class_eq_iff_residual_zero PClass NPClass hsub).mp heq)
    simp [hz, hne]

theorem collapse_bit_one_iff
    (PClass NPClass : Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L) :
    CollapseBit PClass NPClass = 1 ↔
      ¬ (∀ L, PClass L ↔ NPClass L) := by
  unfold CollapseBit
  by_cases hz : ResidualZero PClass NPClass
  · have heq := (class_eq_iff_residual_zero PClass NPClass hsub).2 hz
    simp [hz, heq]
  · have hne : ¬ (∀ L, PClass L ↔ NPClass L) := by
      intro heq
      exact hz ((class_eq_iff_residual_zero PClass NPClass hsub).mp heq)
    simp [hz, hne]

end Fold.Complexity
