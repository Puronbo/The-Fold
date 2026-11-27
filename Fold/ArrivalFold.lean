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


namespace Fold

/-- Pull a target predicate on Y back to X along a coordinate map e.
    This is the target-side operation paired with mapping states by e. -/
def coordinateTransportTarget {X Y : Type}
    (e : X → Y) (hit : Y → Prop) : X → Prop :=
  fun x => hit (e x)

/-- First arrival is unchanged by a coordinate map when the trajectory
    and target are transported together. No injectivity or surjectivity
    is needed for this forward comparison. -/
theorem firstArrival_coordinate_transport
    {α X Y : Type} (e : X → Y) (path : α → Nat → X)
    (hit : Y → Prop) (process : α) (time : Nat) :
    FirstArrival (fun p t => hit (e (path p t))) process time ↔
      FirstArrival
        (fun p t => coordinateTransportTarget e hit (path p t))
        process time := Iff.rfl

/-- If e and eInv are inverse coordinate maps, pulling a target back
    along e and then along eInv restores the original target on Y. -/
theorem coordinateTransportTarget_round_trip
    {X Y : Type} (e : X → Y) (eInv : Y → X)
    (rightInv : ∀ y, e (eInv y) = y) (hit : Y → Prop) :
    coordinateTransportTarget eInv
      (coordinateTransportTarget e hit) = hit := by
  funext y
  change hit (e (eInv y)) = hit y
  rw [rightInv y]

/-- A bijective coordinate change gives a reversible correspondence
    between first-arrival statements, with the target pulled back. -/
theorem firstArrival_bijective_coordinate_change
    {α X Y : Type} (e : X → Y) (eInv : Y → X)
    (leftInv : ∀ x, eInv (e x) = x)
    (rightInv : ∀ y, e (eInv y) = y)
    (path : α → Nat → X) (hit : Y → Prop)
    (process : α) (time : Nat) :
    FirstArrival (fun p t => hit (e (path p t))) process time ↔
      FirstArrival
        (fun p t => coordinateTransportTarget e hit (path p t))
        process time := by
  exact firstArrival_coordinate_transport e path hit process time

end Fold


namespace Fold

/-- A target predicate descends to the orbit chart exactly when it is
    invariant under the fold. The descended predicate is defined on
    quotient classes, not on a chosen representative. -/
def descendTarget {X : Type} (F : Fold X) (hit : X → Prop)
    (hinv : FoldInvariantTarget F hit) : Chart F → Prop :=
  desc F hit (fun x => propext (hinv x))

/-- On a chart projection, the descended target agrees with the original
    state-level target. -/
theorem descendTarget_chart {X : Type} (F : Fold X)
    (hit : X → Prop) (hinv : FoldInvariantTarget F hit) (x : X) :
    descendTarget F hit hinv (chart F x) ↔ hit x := by
  change desc F hit (fun y => propext (hinv y)) (chart F x) ↔ hit x
  rw [desc_chart]

/-- Exact descent criterion: a predicate on states is the pullback of
    some predicate on Fold-orbits iff it is invariant under the fold. -/
theorem target_descends_iff {X : Type} (F : Fold X)
    (hit : X → Prop) :
    (∃ chartHit : Chart F → Prop,
      ∀ x, chartHit (chart F x) ↔ hit x) ↔
        FoldInvariantTarget F hit := by
  constructor
  · rintro ⟨chartHit, hchart⟩ x
    calc
      hit (F.f x) ↔ chartHit (chart F (F.f x)) := (hchart (F.f x)).symm
      _ ↔ chartHit (chart F x) := by rw [chart_fold]
      _ ↔ hit x := hchart x
  · intro hinv
    refine ⟨descendTarget F hit hinv, ?_⟩
    intro x
    exact descendTarget_chart F hit hinv x

/-- First arrival at a descended chart target is equivalent to first
    arrival at its invariant state-level predicate. Thus first-arrival
    time is a well-defined property of Fold-orbits in precisely this
    invariant-target case. -/
theorem firstArrival_descended_target
    {α X : Type} (F : Fold X) (path : α → Nat → X)
    (hit : X → Prop) (hinv : FoldInvariantTarget F hit)
    (process : α) (time : Nat) :
    FirstArrival
        (fun p t => descendTarget F hit hinv (chart F (path p t)))
        process time ↔
      FirstArrival (fun p t => hit (path p t)) process time := by
  constructor
  · rintro ⟨hnow, hbefore⟩
    refine ⟨(descendTarget_chart F hit hinv (path process time)).mp hnow, ?_⟩
    intro earlier hearlier hhit
    exact hbefore earlier hearlier
      ((descendTarget_chart F hit hinv (path process earlier)).mpr hhit)
  · rintro ⟨hnow, hbefore⟩
    refine ⟨(descendTarget_chart F hit hinv (path process time)).mpr hnow, ?_⟩
    intro earlier hearlier hhit
    exact hbefore earlier hearlier
      ((descendTarget_chart F hit hinv (path process earlier)).mp hhit)

end Fold



namespace Fold

/-- Two state trajectories that induce the same orbit-chart trajectory
    have identical first-arrival behavior for every chart-level target.
    This is the precise information retained by quotienting: chart
    observations cannot distinguish representatives of the same orbit. -/
theorem firstArrival_chart_path_congr
    {α X : Type} (F : Fold X)
    (path₁ path₂ : α → Nat → X)
    (sameChart : ∀ process time,
      chart F (path₁ process time) = chart F (path₂ process time))
    (chartHit : Chart F → Prop) (process : α) (time : Nat) :
    FirstArrival
        (fun p t => chartHit (chart F (path₁ p t))) process time ↔
      FirstArrival
        (fun p t => chartHit (chart F (path₂ p t))) process time := by
  apply firstArrival_congr
  intro t
  exact Iff.of_eq (congrArg chartHit (sameChart process t))

/-- Any two representatives of the same orbit yield the same chart
    observation, hence the same first-arrival result for chart targets. -/
theorem firstArrival_orbit_representative_independent
    {α X : Type} (F : Fold X)
    (path₁ path₂ : α → Nat → X)
    (sameOrbit : ∀ process time,
      Orbit F (path₁ process time) (path₂ process time))
    (chartHit : Chart F → Prop) (process : α) (time : Nat) :
    FirstArrival
        (fun p t => chartHit (chart F (path₁ p t))) process time ↔
      FirstArrival
        (fun p t => chartHit (chart F (path₂ p t))) process time := by
  apply firstArrival_chart_path_congr F path₁ path₂
  · intro p t
    exact (chart_eq_iff F (path₁ p t) (path₂ p t)).2 (sameOrbit p t)


end Fold


namespace Fold

/-- The quotient-chart trajectory induced by a state trajectory. -/
def chartPath {α X : Type} (F : Fold X) (path : α → Nat → X) :
    α → Nat → Chart F :=
  fun process time => chart F (path process time)

/-- Two state trajectories have identical chart histories exactly when
    their states are orbit-equivalent at every process and every time.
    This characterizes all representative changes invisible to the chart. -/
theorem chartPath_eq_iff_pointwise_orbit
    {α X : Type} (F : Fold X) (path₁ path₂ : α → Nat → X) :
    chartPath F path₁ = chartPath F path₂ ↔
      ∀ process time, Orbit F (path₁ process time) (path₂ process time) := by
  constructor
  · intro h process time
    apply (chart_eq_iff F (path₁ process time) (path₂ process time)).1
    exact congrFun (congrFun h process) time
  · intro h
    funext process
    funext time
    exact (chart_eq_iff F (path₁ process time) (path₂ process time)).2
      (h process time)

/-- A trajectory step is invisible in the quotient precisely when its
    endpoints are representatives of the same Fold-orbit. -/
theorem chart_step_eq_iff_orbit
    {X : Type} (F : Fold X) (path : Nat → X) (time : Nat) :
    chart F (path (time + 1)) = chart F (path time) ↔
      Orbit F (path (time + 1)) (path time) := by
  exact chart_eq_iff F (path (time + 1)) (path time)

/-- Any property expressed solely through the chart trajectory is
    independent of the chosen state representatives. -/
theorem chartPath_property_representative_independent
    {α X : Type} (F : Fold X) (path₁ path₂ : α → Nat → X)
    (sameOrbit : ∀ process time,
      Orbit F (path₁ process time) (path₂ process time))
    (property : (α → Nat → Chart F) → Prop) :
    property (chartPath F path₁) ↔ property (chartPath F path₂) := by
  have hpath := (chartPath_eq_iff_pointwise_orbit F path₁ path₂).2 sameOrbit
  rw [hpath]

end Fold


namespace Fold

/-- Reconstruct a state from its quotient class and one bit recording
    whether to use the chosen representative or its folded partner. -/
def reconstructState {X : Type} (F : Fold X)
    (representative : Chart F → X) (folded : Bool) (q : Chart F) : X :=
  if folded then F.f (representative q) else representative q

/-- Reconstruction always returns to the supplied quotient class. -/
theorem chart_reconstructState {X : Type} (F : Fold X)
    (representative : Chart F → X)
    (representative_chart : ∀ q, chart F (representative q) = q)
    (folded : Bool) (q : Chart F) :
    chart F (reconstructState F representative folded q) = q := by
  cases folded <;> simp [reconstructState, representative_chart, chart_fold]

/-- Every state in a quotient class can be recovered from a chosen
    representative and at most one binary choice: keep it or fold it.
    At fixed points, either choice may represent the same state. -/
theorem reconstructState_exists_selector {X : Type} (F : Fold X)
    (representative : Chart F → X)
    (representative_chart : ∀ q, chart F (representative q) = q)
    (q : Chart F) (x : X) (hchart : chart F x = q) :
    ∃ folded : Bool, reconstructState F representative folded q = x := by
  have hsame : chart F (representative q) = chart F x := by
    rw [representative_chart q, hchart]
  have horbit : Orbit F (representative q) x :=
    (chart_eq_iff F (representative q) x).1 hsame
  rcases horbit with hx | hx
  · refine ⟨false, ?_⟩
    simp [reconstructState, hx]
  · refine ⟨true, ?_⟩
    simp [reconstructState, hx]

/-- If the selector reconstructs the original state at every tick,
    then the reconstructed and original trajectories have exactly the
    same first-arrival predicate, for every state-level target. -/
theorem firstArrival_reconstruction_exact
    {α X : Type} (F : Fold X)
    (representative : Chart F → X)
    (selector : α → Nat → Bool)
    (chartTrajectory : α → Nat → Chart F)
    (path : α → Nat → X)
    (hit : X → Prop) (process : α) (time : Nat)
    (exact : ∀ p t,
      reconstructState F representative (selector p t)
        (chartTrajectory p t) = path p t) :
    FirstArrival
        (fun p t => hit (reconstructState F representative
          (selector p t) (chartTrajectory p t))) process time ↔
      FirstArrival (fun p t => hit (path p t)) process time := by
  apply firstArrival_congr
  intro t
  rw [exact process t]

end Fold


namespace Fold

/-- The two selector choices reconstruct the same state exactly on the
    fixed set. Away from the crease, choosing the representative or its
    folded partner gives genuinely different states. -/
theorem reconstructState_choices_equal_iff_fixed {X : Type}
    (F : Fold X) (representative : Chart F → X)
    (q : Chart F) :
    reconstructState F representative false q =
      reconstructState F representative true q ↔
        Fix F (representative q) := by
  simp [reconstructState, Fix, eq_comm]

/-- Off the fixed set, the Boolean selector is uniquely determined by
    the reconstructed state. -/
theorem reconstructState_selector_unique_off_crease {X : Type}
    (F : Fold X) (representative : Chart F → X)
    (q : Chart F) (hnotFixed : ¬ Fix F (representative q))
    (b₁ b₂ : Bool)
    (heq : reconstructState F representative b₁ q =
      reconstructState F representative b₂ q) :
    b₁ = b₂ := by
  cases b₁ <;> cases b₂
  · rfl
  · have hfix := (reconstructState_choices_equal_iff_fixed
      F representative q).2 (heq.symm)
    exact False.elim (hnotFixed hfix)
  · have hfix := (reconstructState_choices_equal_iff_fixed
      F representative q).2 heq
    exact False.elim (hnotFixed hfix)
  · rfl

end Fold
