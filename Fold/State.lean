/- 
  Fold/State.lean

  The state-level Fold invariants: collapse erases the observed value but
  preserves the retained reference, direction, and history.  The retained
  signature characterizes exactly when two collapsed states are equal.
-/
import Init

namespace Fold

structure State where
  value : Int
  reference : Int
  direction : Int
  history : List Int
  deriving DecidableEq, Repr

def collapse (s : State) : State :=
  { s with value := 0 }

def turn (s : State) : State :=
  { s with direction := -s.direction, history := s.history ++ [s.direction] }

def observe (s : State) : Int :=
  s.value

/-- A pure direction reversal, without appending an event to history. -/
def flipDirection (s : State) : State :=
  { s with direction := -s.direction }

/-- A logged turn records the previous direction, so it is not a pure flip. -/
theorem flipDirection_involutive (s : State) :
    flipDirection (flipDirection s) = s := by
  cases s
  simp [flipDirection]

theorem flipDirection_injective :
    Function.Injective flipDirection := by
  intro s t h
  cases s with
  | mk sv sr sd sh =>
    cases t with
    | mk tv tr td th =>
      simp [flipDirection] at h
      rcases h with ⟨rfl, rfl, rfl, rfl⟩
      rfl

/-- Collapse is not injective: different values can have the same image. -/
theorem collapse_not_injective :
    ¬ Function.Injective collapse := by
  intro hinj
  let s : State := ⟨1, 7, 1, []⟩
  let t : State := ⟨2, 7, 1, []⟩
  have heq : collapse s = collapse t := by
    simp [s, t, collapse]
  have hst : s = t := hinj heq
  have hv := congrArg State.value hst
  simp [s, t] at hv

/-- A logged turn grows history by exactly one entry. -/
theorem turn_history_length (s : State) :
    (turn s).history.length = s.history.length + 1 := by
  simp [turn]

/-- The metadata that collapse leaves untouched. -/
def retainedSignature (s : State) : Int × Int × List Int :=
  (s.reference, s.direction, s.history)

theorem collapse_sets_value_to_zero (s : State) :
    (collapse s).value = 0 := rfl

theorem collapse_preserves_reference (s : State) :
    (collapse s).reference = s.reference := rfl

theorem collapse_preserves_signature (s : State) :
    retainedSignature (collapse s) = retainedSignature s := rfl

theorem collapse_idempotent (s : State) :
    collapse (collapse s) = collapse s := by
  cases s
  rfl

theorem turn_twice_restores_direction (s : State) :
    (turn (turn s)).direction = s.direction := by
  simp [turn]

theorem collapsed_observation_independent (s t : State) :
    observe (collapse s) = observe (collapse t) := rfl

theorem observation_only_classifier_cannot_recover_reference
    (classifier : Int → Bool) (s t : State) :
    classifier (observe (collapse s)) =
      classifier (observe (collapse t)) := rfl

/-- Two collapsed states are equal exactly when all retained metadata agrees. -/
theorem collapse_eq_iff_retained_signature_eq (s t : State) :
    collapse s = collapse t ↔ retainedSignature s = retainedSignature t := by
  cases s <;> cases t <;> simp [collapse, retainedSignature]

/-- Full states agree exactly when both the erased value and retained metadata agree. -/
theorem state_eq_iff_value_and_signature (s t : State) :
    s = t ↔ s.value = t.value ∧ retainedSignature s = retainedSignature t := by
  cases s <;> cases t <;> simp [retainedSignature]

theorem distinct_references_survive_collapse
    (s t : State) (h : s.reference ≠ t.reference) :
    collapse s ≠ collapse t := by
  intro hc
  have hr := congrArg (fun state : State => state.reference) hc
  exact h (by simpa [collapse] using hr)

/-- Post-processing cannot undo a collision already created by a map. -/
theorem comp_not_injective_of_not_injective
    {α β γ : Type} (f : α → β) (g : β → γ)
    (hf : ¬ Function.Injective f) :
    ¬ Function.Injective (g ∘ f) := by
  intro hcomp
  apply hf
  intro x y hxy
  apply hcomp
  exact congrArg g hxy

/-- No later state transformation can recover injectivity after collapse. -/
theorem postprocess_cannot_restore_collapse_injectivity
    (g : State → State) :
    ¬ Function.Injective (g ∘ collapse) := by
  exact comp_not_injective_of_not_injective collapse g collapse_not_injective

/-- Composition of injective transitions remains injective. -/
theorem comp_injective_of_injective
    {α β γ : Type} (f : α → β) (g : β → γ)
    (hf : Function.Injective f) (hg : Function.Injective g) :
    Function.Injective (g ∘ f) := by
  intro x y h
  apply hf
  apply hg
  exact h

/-- Restore the one field erased by collapse, using a retained value. -/
def restoreValue (s : State) (originalValue : Int) : State :=
  { s with value := originalValue }

/-- The collapsed state plus its original value reconstructs the full state. -/
theorem restoreValue_collapse (s : State) :
    restoreValue (collapse s) s.value = s := by
  cases s
  rfl

/-- Retaining the erased value makes the collapse encoding injective. -/
def collapseWithValue (s : State) : State × Int :=
  (collapse s, s.value)

theorem collapseWithValue_injective :
    Function.Injective collapseWithValue := by
  intro s t h
  have hs : collapse s = collapse t := congrArg Prod.fst h
  have hv : s.value = t.value := congrArg Prod.snd h
  cases s with
  | mk sv sr sd sh =>
    cases t with
    | mk tv tr td th =>
      simp [collapse] at hs
      simp_all

/-- Pair a transformed observation with auxiliary retained memory. -/
def retainPair {α β γ : Type} (f : α → β) (r : α → γ) :
    α → β × γ :=
  fun x => (f x, r x)

/-- Equality of augmented representations is componentwise equality. -/
theorem retainPair_eq_iff {α β γ : Type}
    (f : α → β) (r : α → γ) (x y : α) :
    retainPair f r x = retainPair f r y ↔
      f x = f y ∧ r x = r y := by
  simp [retainPair]

/-- An injective primary representation stays injective after augmentation. -/
theorem retainPair_injective_of_primary_injective
    {α β γ : Type} (f : α → β) (r : α → γ)
    (hf : Function.Injective f) :
    Function.Injective (retainPair f r) := by
  intro x y h
  apply hf
  exact congrArg Prod.fst h

/--
The augmented representation is injective exactly when the retained
channel separates every collision left by the primary transformation.
-/
theorem retainPair_injective_iff {α β γ : Type}
    (f : α → β) (r : α → γ) :
    Function.Injective (retainPair f r) ↔
      ∀ x y, f x = f y → r x = r y → x = y := by
  constructor
  · intro h x y hf hr
    apply h
    exact Prod.ext hf hr
  · intro h x y hp
    exact h x y (congrArg Prod.fst hp) (congrArg Prod.snd hp)

/-- A sufficient-memory condition guarantees exact reconstruction. -/
theorem retainPair_injective_of_separates_collisions
    {α β γ : Type} (f : α → β) (r : α → γ)
    (h : ∀ x y, f x = f y → r x = r y → x = y) :
    Function.Injective (retainPair f r) :=
  retainPair_injective_iff f r |>.2 h

/--
A process arrival records its rate, elapsed time, and traversed distance.
The model deliberately leaves the travel law abstract: physical systems may
use different rate and path metrics.
-/
structure SynchronizedArrival
    (Rate Time Distance : Type)
    (travelDistance : Rate → Time → Distance) where
  speed : Rate
  time : Time
  distance : Distance
  distance_eq : distance = travelDistance speed time

/--
At a shared elapsed time, an injective rate-to-distance law forces distinct
rates to correspond to distinct path distances.  Thus simultaneous arrival
does not mean equal speed or equal path length.
-/
theorem different_speeds_require_different_distances
    {Rate Time Distance : Type}
    (travelDistance : Rate → Time → Distance)
    (a b : SynchronizedArrival Rate Time Distance travelDistance)
    (hTime : a.time = b.time)
    (hInjective : Function.Injective (fun rate => travelDistance rate a.time))
    (hSpeed : a.speed ≠ b.speed) :
    a.distance ≠ b.distance := by
  intro hDistance
  apply hSpeed
  apply hInjective
  calc
    travelDistance a.speed a.time = a.distance := a.distance_eq.symm
    _ = b.distance := hDistance
    _ = travelDistance b.speed a.time := by
      rw [hTime]
      exact b.distance_eq

/--
A first arrival at natural-number time t means the target is reached at t
and is not reached at any strictly earlier time.
-/ 
def FirstArrival {α : Type} (reaches : α → Nat → Prop)
    (process : α) (t : Nat) : Prop :=
  reaches process t ∧ ∀ earlier, earlier < t → ¬ reaches process earlier

/--
Once a process has a first-arrival time, every time at which it reaches
the target is at least that time.
-/
theorem firstArrival_le_any_arrival
    {α : Type} (reaches : α → Nat → Prop)
    (process : α) (first later : Nat)
    (hFirst : FirstArrival reaches process first)
    (hLater : reaches process later) :
    first ≤ later :=
  Nat.le_of_not_gt (fun hEarlier => (hFirst.2 later hEarlier) hLater)

/--
A family is synchronized at its first-arrival boundary when every member
reaches the target there and none reaches it earlier.
-/
def SynchronizedFirstArrival
    {α : Type} (reaches : α → Nat → Prop)
    (processes : List α) (t : Nat) : Prop :=
  ∀ process, process ∈ processes → FirstArrival reaches process t

/--
Synchronization gives a common lower bound: no listed process can reach
the target before the shared first-arrival time.
-/
theorem synchronized_first_arrival_is_common_lower_bound
    {α : Type} (reaches : α → Nat → Prop)
    (processes : List α) (first later : Nat)
    (hSync : SynchronizedFirstArrival reaches processes first)
    (process : α) (hMember : process ∈ processes)
    (hLater : reaches process later) :
    first ≤ later :=
  firstArrival_le_any_arrival reaches process first later
    (hSync process hMember) hLater

end Fold
