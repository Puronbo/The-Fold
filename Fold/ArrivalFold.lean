/-
  Fold/ArrivalFold.lean

  First-arrival preservation under a fold.  The target must be invariant
  under the fold; involutivity alone does not preserve an arbitrary target.
-/
import Fold.Basic
import Fold.Synchronization

namespace Fold

/-- A target predicate is fold-invariant when folding a state neither
    creates nor destroys target membership. -/
def FoldInvariantTarget (F : Fold X) (hit : X → Prop) : Prop :=
  ∀ x, hit (F.f x) ↔ hit x

/-- Folding every state along a trajectory preserves its first-arrival
    time exactly when the target predicate is fold-invariant.

    This is the precise condition: the involution by itself is not enough
    for an arbitrary, non-invariant target. -/
theorem firstArrival_preserved_by_fold
    {X : Type} (F : Fold X) (path : X → Nat → X)
    (hit : X → Prop) (process : X) (time : Nat)
    (hinv : FoldInvariantTarget F hit) :
    FirstArrival (fun p t => hit (F.f (path p t))) process time ↔
      FirstArrival (fun p t => hit (path p t)) process time := by
  constructor
  · rintro ⟨hnow, hbefore⟩
    refine ⟨(hinv (path process time)).mp hnow, ?_⟩
    intro earlier hearlier hhit
    exact hbefore earlier hearlier ((hinv (path process earlier)).mpr hhit)
  · rintro ⟨hnow, hbefore⟩
    refine ⟨(hinv (path process time)).mpr hnow, ?_⟩
    intro earlier hearlier hhit
    exact hbefore earlier hearlier ((hinv (path process earlier)).mp hhit)

/-- The fixed-point target (the crease) is invariant under the fold:
    folding a state cannot change whether that state is fixed. -/
theorem fixedTarget_fold_invariant (F : Fold X) :
    FoldInvariantTarget F (Fix F) := by
  intro x
  exact fix_iff F x

/-- A trajectory and its pointwise-folded image have the same first
    arrival at the crease. -/
theorem firstArrival_at_crease_preserved
    (F : Fold X) (path : X → Nat → X) (process : X) (time : Nat) :
    FirstArrival
        (fun p t => Fix F (F.f (path p t))) process time ↔
      FirstArrival (fun p t => Fix F (path p t)) process time :=
  firstArrival_preserved_by_fold F path (Fix F) process time
    (fixedTarget_fold_invariant F)

end Fold
