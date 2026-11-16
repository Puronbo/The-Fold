/-
  Fold/Arithmetic.lean

  The exact arithmetic of the calendar and the date formats.

  Four spellings of the same day, all congruent to `56` modulo `99`;
  the Gregorian cycle `146097 = 3³ · 7 · 773`; the Unix epoch as `1608`
  whole weeks; the weekday as a `ℤ/7` coordinate.  These are
  computations, not interpretations: `decide` closes each one.
-/
import Init

namespace Fold

/-- The four date formats agree modulo `99`. -/
theorem formats_mod_99 :
    (10262000 : Nat) % 99 = 56 ∧
    (26102000 : Nat) % 99 = 56 ∧
    (20001026 : Nat) % 99 = 56 ∧
    (20002610 : Nat) % 99 = 56 := by
  decide

/-- The four formats are pairwise distinct labels. -/
theorem formats_distinct :
    (10262000 : Nat) ≠ 26102000 ∧
    (10262000 : Nat) ≠ 20001026 ∧
    (10262000 : Nat) ≠ 20002610 ∧
    (26102000 : Nat) ≠ 20001026 ∧
    (26102000 : Nat) ≠ 20002610 ∧
    (20001026 : Nat) ≠ 20002610 := by
  decide

/-- The Gregorian cycle, exactly. -/
theorem gregorian_cycle : (146097 : Nat) = 27 * 7 * 773 := by
  decide

/-- The Unix epoch `972518400` is `1608` whole weeks. -/
theorem unix_weeks : (972518400 : Nat) = 1608 * 604800 := by
  decide

/-- `1608` weeks is `5` modulo `7`: the weekday is a residue, not an
absolute. -/
theorem unix_week_residue : (1608 : Nat) % 7 = 5 := by
  decide

/-- The Julian day number `2451844` is `3` modulo `7`. -/
theorem jdn_residue : (2451844 : Nat) % 7 = 3 := by
  decide

/-- The calendar check, in one statement. -/
theorem calendar_structure :
    (10262000 : Nat) % 99 = 56 ∧
    (26102000 : Nat) % 99 = 56 ∧
    (20001026 : Nat) % 99 = 56 ∧
    (20002610 : Nat) % 99 = 56 ∧
    (146097 : Nat) = 27 * 7 * 773 ∧
    (972518400 : Nat) = 1608 * 604800 :=
  ⟨formats_mod_99.1, formats_mod_99.2.1, formats_mod_99.2.2.1,
   formats_mod_99.2.2.2, gregorian_cycle, unix_weeks⟩

end Fold
