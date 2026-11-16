/-
  Fold/Pressure.lean

  The linear hydrostatic law in discrete units:

      p(h) = p0 + c h ,      c = ρ g > 0 .

  The exact content of "under the ocean it increases until infinity" is
  two statements: the law is strictly increasing, and it is unbounded
  over finite depths.  No finite depth has infinite pressure; the
  divergence is the limit, not a value.  The real-valued law is
  `p(h) = p0 + ρ g h`; this file is its integer skeleton.

  The datum `p0` is a gauge choice, not a fixed point of the world:
  changing it shifts every pressure by the same constant.
-/
import Init

namespace Fold

/-- The linear hydrostatic law: `p(h) = p0 + c h`, with `c = ρ g > 0`. -/
def pressure (c p0 h : Nat) : Nat := p0 + c * h

/-- Pressure is strictly increasing with depth. -/
theorem pressure_strict (c p0 : Nat) (hc : 0 < c) :
    ∀ a b : Nat, a < b → pressure c p0 a < pressure c p0 b := by
  intro a b hab
  unfold pressure
  have hmul : c * a < c * b := Nat.mul_lt_mul_of_pos_left hab hc
  omega

/-- Every target pressure is exceeded at some finite depth: the ideal
"until infinity" is an unboundedness statement, not a value at
infinity. -/
theorem pressure_unbounded (c p0 : Nat) (hc : 0 < c) (P : Nat) :
    ∃ h : Nat, P < pressure c p0 h := by
  refine ⟨P + 1, ?_⟩
  unfold pressure
  have hle : P + 1 ≤ c * (P + 1) := Nat.le_mul_of_pos_left (P + 1) hc
  omega

/-- The value at a finite depth is finite and is exactly the linear
law. -/
theorem pressure_finite (c p0 h : Nat) :
    pressure c p0 h = p0 + c * h := rfl

/-- The datum is a gauge choice: shifting it by `d` shifts every
pressure by `d`, and changes no difference. -/
theorem pressure_gauge (c p0 d h : Nat) :
    pressure c (p0 + d) h = pressure c p0 h + d := by
  unfold pressure
  omega

end Fold
