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
def FoldInvariantTarget {X : Type} (F : Fold X) (hit : X → Prop) : Prop :=
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
theorem fixedTarget_fold_invariant {X : Type} (F : Fold X) :
    FoldInvariantTarget F (Fix F) := by
  intro x
  exact fix_iff F x

/-- A trajectory and its pointwise-folded image have the same first
    arrival at the crease. -/
theorem firstArrival_at_crease_preserved
    {X : Type} (F : Fold X) (path : X → Nat → X) (process : X) (time : Nat) :
    FirstArrival
        (fun p t => Fix F (F.f (path p t))) process time ↔
      FirstArrival (fun p t => Fix F (path p t)) process time :=
  firstArrival_preserved_by_fold F path (Fix F) process time
    (fixedTarget_fold_invariant F)

end Fold


namespace Fold

/-- A concrete involution showing why target invariance is necessary:
    the Boolean flip sends the target value true to false. -/
def booleanFlip : Fold Bool where
  f := fun b => !b
  invol := by
    intro b
    cases b <;> rfl

/-- A constant trajectory already at the Boolean target. -/
def constantTrueTrajectory (_process : Unit) (_time : Nat) : Bool := true

/-- Without target invariance, folding can destroy a first hit immediately.
    The original path hits true at tick zero; its folded image does not. -/
theorem noninvariant_target_can_change_first_arrival :
    _root_.Fold.FirstArrival
        (fun _ t => constantTrueTrajectory () t = true) () 0 ∧
      ¬ _root_.Fold.FirstArrival
        (fun _ t => booleanFlip.f (constantTrueTrajectory () t) = true) () 0 := by
  simp [_root_.Fold.FirstArrival, constantTrueTrajectory, booleanFlip]

end Fold


namespace Fold

/-- Transport a target backwards through a fold. A state x belongs to
    the transported target precisely when its folded image belongs to
    the original target. -/
def foldTransportTarget {X : Type} (F : Fold X)
    (hit : X → Prop) : X → Prop :=
  fun x => hit (F.f x)

/-- Transporting a target twice through an involution returns the
    original target. This is the target-side counterpart of F² = id. -/
theorem foldTransportTarget_involutive {X : Type} (F : Fold X)
    (hit : X → Prop) :
    foldTransportTarget F (foldTransportTarget F hit) = hit := by
  funext x
  change hit (F.f (F.f x)) = hit x
  rw [F.invol x]

/-- Exact first-arrival transport: folding the trajectory while keeping
    the target fixed is equivalent to keeping the trajectory and
    transporting the target backwards through the fold. No invariance
    assumption is needed because the target is transformed as well. -/
theorem firstArrival_fold_target_transport
    {X : Type} (F : Fold X) (path : X → Nat → X)
    (hit : X → Prop) (process : X) (time : Nat) :
    FirstArrival (fun p t => hit (F.f (path p t))) process time ↔
      FirstArrival (fun p t => foldTransportTarget F hit (path p t))
        process time := Iff.rfl

/-- For an involution, transporting a target twice is identity, so the
    correspondence between folded trajectories and transformed targets
    is reversible. -/
theorem fold_target_transport_round_trip
    {X : Type} (F : Fold X) (hit : X → Prop) :
    foldTransportTarget F (foldTransportTarget F hit) = hit :=
  foldTransportTarget_involutive F hit


/-- Transport each process's own target backwards through its own
    involution. The family may use different folds and different targets. -/
def foldTransportFamilyTarget {α X : Type}
    (fold : α → Fold X) (hit : α → X → Prop) : α → X → Prop :=
  fun process state => hit process ((fold process).f state)

/-- Synchronization is exactly preserved when every process target is
    transported along that process's fold. This requires no common target,
    common fold, or target-invariance assumption. -/
theorem synchronizedBoundary_fold_target_transport
    {α X : Type} (processes : List α)
    (fold : α → Fold X) (path : α → Nat → X)
    (hit : α → X → Prop) (time : Nat) :
    SynchronizedBoundary
        (fun process t => hit process ((fold process).f (path process t)))
        processes time ↔
      SynchronizedBoundary
        (fun process t =>
          foldTransportFamilyTarget fold hit process (path process t))
        processes time := Iff.rfl

/-- Transporting every process target twice restores the original family
    of targets, process by process. -/
theorem foldTransportFamilyTarget_involutive
    {α X : Type} (fold : α → Fold X) (hit : α → X → Prop) :
    foldTransportFamilyTarget fold
      (foldTransportFamilyTarget fold hit) = hit := by
  funext process
  funext state
  change hit process ((fold process).f ((fold process).f state)) =
    hit process state
  rw [(fold process).invol state]

end Fold
