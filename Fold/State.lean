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

/-- A process cannot have two different first-arrival times. -/
theorem firstArrival_unique
    {α : Type} (reaches : α → Nat → Prop)
    (process : α) (t u : Nat)
    (ht : FirstArrival reaches process t)
    (hu : FirstArrival reaches process u) :
    t = u := by
  apply Nat.le_antisymm
  · exact firstArrival_le_any_arrival reaches process t u ht hu.1
  · exact firstArrival_le_any_arrival reaches process u t hu ht.1

/--
If every process in a nonempty family has a first-arrival time and all
those first-arrival times equal t, then the family is synchronized at t.
-/
theorem synchronized_of_common_first_arrival
    {α : Type} (reaches : α → Nat → Prop)
    (processes : List α) (t : Nat)
    (hCommon : ∀ process, process ∈ processes →
      FirstArrival reaches process t) :
    SynchronizedFirstArrival reaches processes t :=
  hCommon

/--
Exact discrete linear arrival: a process moving at positive natural-number
rate v reaches a target at distance d at tick t when d = v * t.
-/
def LinearArrival (speed distance time : Nat) : Prop :=
  distance = speed * time

/--
Two processes have a shared exact arrival tick precisely when their
distances are generated by their respective rates at one common tick.
This is the constructive synchronization criterion for the linear model.
-/
theorem linear_arrivals_synchronize_iff
    (speed₁ distance₁ speed₂ distance₂ : Nat) :
    (∃ time, LinearArrival speed₁ distance₁ time ∧
      LinearArrival speed₂ distance₂ time) ↔
    (∃ time, distance₁ = speed₁ * time ∧
      distance₂ = speed₂ * time) := by
  rfl

/--
At a positive common tick, different positive speeds imply different
travelled distances under the exact linear travel law.
-/
theorem different_speeds_give_different_linear_distances
    (speed₁ speed₂ time : Nat)
    (hInjective : Function.Injective (fun speed : Nat => speed * time))
    (hSpeed : speed₁ ≠ speed₂) :
    speed₁ * time ≠ speed₂ * time := by
  intro h
  exact hSpeed (hInjective h)

/--
The rate-distance scaling law: at a common positive tick, the distance
ratio is represented without division by cross multiplication.
-/
theorem synchronized_linear_cross_product
    (speed₁ distance₁ speed₂ distance₂ time : Nat)
    (h₁ : LinearArrival speed₁ distance₁ time)
    (h₂ : LinearArrival speed₂ distance₂ time) :
    distance₁ * speed₂ = distance₂ * speed₁ := by
  rw [h₁, h₂]
  simp [Nat.mul_left_comm, Nat.mul_comm]

/-- A process has reached or passed a target by a given discrete tick. -/
def ThresholdReached (speed target time : Nat) : Prop :=
  target ≤ speed * time

/--
A first threshold crossing is the earliest tick at which linear progress
reaches or passes the target. The target may be crossed rather than hit
exactly, which models discrete-time overshoot.
-/
def FirstThresholdCrossing (speed target time : Nat) : Prop :=
  FirstArrival (fun (_ : Unit) tick =>
    ThresholdReached speed target tick) () time

/-- A process has at most one first threshold-crossing tick. -/
theorem first_threshold_crossing_unique
    (speed target t u : Nat)
    (ht : FirstThresholdCrossing speed target t)
    (hu : FirstThresholdCrossing speed target u) :
    t = u :=
  firstArrival_unique
    (fun (_ : Unit) tick => ThresholdReached speed target tick)
    () t u ht hu

/--
At its first threshold crossing, a process is at or beyond the target;
every earlier tick remains strictly below it.
-/
theorem first_threshold_crossing_boundary
    (speed target time : Nat)
    (h : FirstThresholdCrossing speed target time) :
    target ≤ speed * time ∧
      ∀ earlier, earlier < time → speed * earlier < target := by
  constructor
  · exact h.1
  · intro earlier hEarlier
    exact Nat.not_le.mp (h.2 earlier hEarlier)

/--
At a positive first-crossing tick, the target lies in the one-tick
progress interval: progress at the preceding tick is below the target,
while progress at the crossing tick reaches or exceeds it.
-/
theorem first_threshold_crossing_interval
    (speed target time : Nat)
    (hPositiveTick : ∃ previous, time = previous + 1)
    (h : FirstThresholdCrossing speed target time) :
    ∃ previous, time = previous + 1 ∧
      speed * previous < target ∧ target ≤ speed * time := by
  obtain ⟨previous, hTime⟩ := hPositiveTick
  refine ⟨previous, hTime, ?_, h.1⟩
  have hEarlier : previous < time := by
    rw [hTime]
    exact Nat.lt_succ_self previous
  exact Nat.not_le.mp (h.2 previous hEarlier)

/--
Two processes synchronize at a positive first-crossing tick exactly
within their respective one-tick progress intervals. Their speeds may
differ; each target is constrained by its own rate over the same tick.
-/
theorem synchronized_threshold_intervals
    (speed₁ target₁ speed₂ target₂ time : Nat)
    (hPositiveTick : ∃ previous, time = previous + 1)
    (h₁ : FirstThresholdCrossing speed₁ target₁ time)
    (h₂ : FirstThresholdCrossing speed₂ target₂ time) :
    ∃ previous, time = previous + 1 ∧
      speed₁ * previous < target₁ ∧ target₁ ≤ speed₁ * time ∧
      speed₂ * previous < target₂ ∧ target₂ ≤ speed₂ * time := by
  obtain ⟨previous, hTime, hLower₁, hUpper₁⟩ :=
    first_threshold_crossing_interval speed₁ target₁ time hPositiveTick h₁
  obtain ⟨previous₂, hTime₂, hLower₂, hUpper₂⟩ :=
    first_threshold_crossing_interval speed₂ target₂ time hPositiveTick h₂
  have hPrevious : previous₂ = previous :=
    Nat.add_right_cancel (hTime₂.symm.trans hTime)
  exact ⟨previous, hTime, hLower₁, hUpper₁,
    by simpa [hPrevious] using hLower₂,
    by simpa [hTime₂, hTime] using hUpper₂⟩

/--
Concrete synchronized first crossing: rates 2 and 3 both first reach
target 4 at tick 2, despite moving at different speeds.
-/
theorem distinct_speeds_can_synchronize :
    FirstThresholdCrossing 2 4 2 ∧
      FirstThresholdCrossing 3 4 2 := by
  decide [FirstThresholdCrossing, FirstArrival, ThresholdReached]

/--
For this example the first crossing is simultaneous, not merely an
eventual coincidence: both processes are below 4 at tick 1 and at or
above 4 at tick 2.
-/
theorem distinct_speeds_shared_first_tick :
    2 * 1 < 4 ∧ 4 ≤ 2 * 2 ∧
      3 * 1 < 4 ∧ 4 ≤ 3 * 2 := by
  decide

end Fold
