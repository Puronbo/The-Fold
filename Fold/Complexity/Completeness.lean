import Init

namespace Fold.Complexity

universe u
variable {Lang : Type u}

/-- A many-one reduction relation between decision languages.
    Its computational cost is abstracted by the closure hypothesis below. -/
def NPComplete
    (NPClass : Lang → Prop)
    (Reduces : Lang → Lang → Prop)
    (Target : Lang) : Prop :=
  NPClass Target ∧ ∀ Source, NPClass Source → Reduces Source Target

/-- If a language is NP-complete and belongs to P, then P = NP.
    hclosed packages closure of P under the chosen polynomial reductions. -/
theorem np_complete_in_P_implies_class_eq
    (PClass NPClass : Lang → Prop)
    (Reduces : Lang → Lang → Prop)
    (Target : Lang)
    (hsub : ∀ L, PClass L → NPClass L)
    (hclosed : ∀ Source Target, Reduces Source Target →
      PClass Target → PClass Source)
    (hcomplete : NPComplete NPClass Reduces Target)
    (htarget : PClass Target) :
    ∀ L, PClass L ↔ NPClass L := by
  intro L
  constructor
  · exact hsub L
  · intro hNP
    exact hclosed L Target (hcomplete.2 L hNP) htarget

/-- For an NP-complete target, membership in P is equivalent to P = NP. -/
theorem np_complete_in_P_iff_class_eq
    (PClass NPClass : Lang → Prop)
    (Reduces : Lang → Lang → Prop)
    (Target : Lang)
    (hsub : ∀ L, PClass L → NPClass L)
    (hclosed : ∀ Source Target, Reduces Source Target →
      PClass Target → PClass Source)
    (hcomplete : NPComplete NPClass Reduces Target) :
    PClass Target ↔ (∀ L, PClass L ↔ NPClass L) := by
  constructor
  · exact np_complete_in_P_implies_class_eq
      PClass NPClass Reduces Target hsub hclosed hcomplete
  · intro heq
    exact (heq Target).2 hcomplete.1

/-- If any NP-complete target is in P, the NP-over-P residual is empty. -/
theorem exists_np_complete_in_P_implies_residual_zero
    (PClass NPClass : Lang → Prop)
    (Reduces : Lang → Lang → Prop)
    (hsub : ∀ L, PClass L → NPClass L)
    (hclosed : ∀ Source Target, Reduces Source Target →
      PClass Target → PClass Source)
    (hTarget : ∃ Target, NPComplete NPClass Reduces Target ∧ PClass Target) :
    ∀ L, NPClass L → PClass L := by
  intro L hNP
  obtain ⟨Target, hcomplete, hP⟩ := hTarget
  exact hclosed L Target (hcomplete.2 L hNP) hP

end Fold.Complexity
