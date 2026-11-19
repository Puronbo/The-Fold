/-
  Fold/Doubling.lean

  The scale action at `k = 2`: doubling on `ℤ/n`.

  The fold is multiplication by `-1`; it is an involution for every
  modulus.  Doubling is multiplication by `+2`; it is a permutation
  exactly when the modulus is odd, and its cycles are longer than two
  in general.  The two actions coincide only at `n = 3`, where
  `2 = -1`.

  Everything here is finite and closed by `decide`, `omega`, or the
  inverse map `x ↦ (n+1)/2 · x`.  No Mathlib.
-/
import Init

namespace Fold

/-- A map is bijective when it is injective and surjective. -/
def Bijective {α β : Type} (f : α → β) : Prop :=
  Function.Injective f ∧ Function.Surjective f

/-- The `k`-fold iterate of a map, defined in core Lean. -/
def iterate {α : Type} (f : α → α) : Nat → α → α
  | 0, x => x
  | k + 1, x => f (iterate f k x)

/-- Doubling on `Fin n`, for `n > 0`. -/
def double (n : Nat) (hn : 0 < n) (x : Fin n) : Fin n :=
  ⟨(2 * x.val) % n, Nat.mod_lt _ hn⟩

/-- Negation, the fold, on `Fin n`. -/
def neg (n : Nat) (hn : 0 < n) (x : Fin n) : Fin n :=
  ⟨(n - x.val) % n, Nat.mod_lt _ hn⟩

/-- The inverse of doubling when `n = 2*m + 1`: multiplication by `m + 1`. -/
def half (n m : Nat) (hn : n = 2 * m + 1) (x : Fin n) : Fin n :=
  ⟨((m + 1) * x.val) % n, Nat.mod_lt _ (by omega)⟩

theorem half_double (n m : Nat) (hn : n = 2 * m + 1) (x : Fin n) :
    half n m hn (double n (by omega) x) = x := by
  subst n
  apply Fin.ext
  simp [half, double]
  have h : (m + 1) * (2 * x.val) = (2 * m + 1 + 1) * x.val := by
    calc
      (m + 1) * (2 * x.val) = ((m + 1) * 2) * x.val := by rw [Nat.mul_assoc]
      _ = (2 * (m + 1)) * x.val := by rw [Nat.mul_comm (m + 1) 2]
      _ = (2 * m + 1 + 1) * x.val := by congr 1
  rw [h, Nat.add_mul, Nat.one_mul]
  rw [Nat.mul_comm (2 * m + 1) x.val]
  exact Nat.mul_add_mod_of_lt x.isLt

theorem double_half (n m : Nat) (hn : n = 2 * m + 1) (x : Fin n) :
    double n (by omega) (half n m hn x) = x := by
  subst n
  apply Fin.ext
  simp [half, double]
  have h : 2 * ((m + 1) * x.val) = (2 * m + 1 + 1) * x.val := by
    calc
      2 * ((m + 1) * x.val) = (2 * (m + 1)) * x.val := by rw [Nat.mul_assoc]
      _ = (2 * m + 1 + 1) * x.val := by congr 1
  rw [h, Nat.add_mul, Nat.one_mul]
  rw [Nat.mul_comm (2 * m + 1) x.val]
  exact Nat.mul_add_mod_of_lt x.isLt

theorem double_injective_of_odd (n m : Nat) (hn : n = 2 * m + 1) :
    Function.Injective (double n (by omega)) := by
  intro x y hxy
  have h := congrArg (half n m hn) hxy
  simpa [half_double] using h

theorem double_surjective_of_odd (n m : Nat) (hn : n = 2 * m + 1) :
    Function.Surjective (double n (by omega)) := by
  intro y
  exact ⟨half n m hn y, double_half n m hn y⟩

theorem double_bijective_of_odd (n m : Nat) (hn : n = 2 * m + 1) :
    Bijective (double n (by omega)) :=
  ⟨double_injective_of_odd n m hn, double_surjective_of_odd n m hn⟩

theorem double_not_injective_of_even (n m : Nat) (hn : n = 2 * m) (hm : 0 < m) :
    ¬ Function.Injective (double n (by omega)) := by
  intro inj
  have h0 : double n (by omega) ⟨0, by omega⟩ = double n (by omega) ⟨m, by omega⟩ := by
    apply Fin.ext
    simp [double, hn]
  have hfin : (⟨0, by omega⟩ : Fin n) = ⟨m, by omega⟩ := inj h0
  have hval : (0 : Nat) = m := by
    simpa using congrArg Fin.val hfin
  omega

theorem odd_iff_exists (n : Nat) : n % 2 = 1 ↔ ∃ m, n = 2 * m + 1 := by
  constructor
  · intro h
    refine ⟨n / 2, ?_⟩
    have := Nat.mod_add_div n 2
    omega
  · rintro ⟨m, rfl⟩
    omega

/-- Doubling is a permutation iff the modulus is odd. -/
theorem double_bijective_iff_odd (n : Nat) (hn : 0 < n) :
    Bijective (double n hn) ↔ ∃ m, n = 2 * m + 1 := by
  constructor
  · intro hb
    rcases Nat.mod_two_eq_zero_or_one n with h0 | h1
    · have hn' : n = 2 * (n / 2) := by
        have := Nat.mod_add_div n 2
        omega
      have hm : 0 < n / 2 := by omega
      exact False.elim (double_not_injective_of_even n (n / 2) hn' hm hb.1)
    · exact (odd_iff_exists n).1 h1
  · rintro ⟨m, hm⟩
    simpa using double_bijective_of_odd n m hm

/-- The same criterion, spelled with `n % 2`. -/
theorem double_bijective_iff_mod_two (n : Nat) (hn : 0 < n) :
    Bijective (double n hn) ↔ n % 2 = 1 :=
  (double_bijective_iff_odd n hn).trans (odd_iff_exists n).symm

/-- The `k`-th iterate of doubling is multiplication by `2^k`. -/
theorem double_iter (n : Nat) (hn : 0 < n) (k : Nat) (x : Fin n) :
    iterate (double n hn) k x = ⟨(2 ^ k * x.val) % n, Nat.mod_lt _ hn⟩ := by
  induction k generalizing x with
  | zero =>
      apply Fin.ext
      simp [iterate, Nat.mod_eq_of_lt x.isLt]
  | succ k ih =>
      simp [iterate, ih, double, Nat.pow_succ, Nat.mul_mod_mod]
      congr 1
      ac_rfl

/-- If `n` divides `2^k - 1`, then `k` doublings return every residue. -/
theorem double_iter_eq_id_of_dvd (n k : Nat) (hn : 0 < n)
    (h : n ∣ 2 ^ k - 1) :
    iterate (double n hn) k = id := by
  funext x
  rw [double_iter]
  apply Fin.ext
  rcases h with ⟨q, hq⟩
  have hpos : 0 < 2 ^ k := Nat.two_pow_pos k
  have hk : 2 ^ k = n * q + 1 := by omega
  rw [hk, Nat.add_mul, Nat.one_mul]
  rw [show n * q * x.val = (q * x.val) * n by ac_rfl]
  exact Nat.mul_add_mod_of_lt x.isLt

/-- The only fixed point of doubling is `0`: the crease is a point. -/
theorem double_fixed (n : Nat) (hn : 0 < n) (x : Fin n) :
    double n hn x = x ↔ x.val = 0 := by
  constructor
  · intro h
    have hval : (2 * x.val) % n = x.val := by
      simpa [double] using congrArg Fin.val h
    have hdiv := Nat.mod_add_div (2 * x.val) n
    have hmul : n * ((2 * x.val) / n) = x.val := by omega
    have hdvd : n ∣ x.val := ⟨(2 * x.val) / n, hmul.symm⟩
    exact Nat.eq_zero_of_dvd_of_lt hdvd x.isLt
  · intro h
    apply Fin.ext
    simp [double, h]

/-- The fold and the scale action agree only at `n = 3`. -/
theorem double_eq_neg_iff (n : Nat) (hn : 0 < n) :
    (∀ x : Fin n, double n hn x = neg n hn x) ↔ n ∣ 3 := by
  constructor
  · intro h
    by_cases hn1 : n = 1
    · subst hn1
      exact ⟨3, rfl⟩
    by_cases hn2 : n = 2
    · subst hn2
      have hv : 2 % 2 = (2 - 1) % 2 := by
        simpa [double, neg] using congrArg Fin.val (h ⟨1, by omega⟩)
      simp at hv
    · have hn3 : 3 ≤ n := by omega
      have hv : 2 % n = (n - 1) % n := by
        simpa [double, neg] using congrArg Fin.val (h ⟨1, by omega⟩)
      rw [Nat.mod_eq_of_lt (by omega : 2 < n),
          Nat.mod_eq_of_lt (by omega : n - 1 < n)] at hv
      have h3 : n = 3 := by omega
      subst h3
      exact Nat.dvd_refl 3
  · intro h3
    have hnle : n ≤ 3 := Nat.le_of_dvd (by decide : 0 < 3) h3
    have hn3 : n = 1 ∨ n = 2 ∨ n = 3 := by omega
    rcases hn3 with rfl | rfl | rfl
    · intro x
      apply Fin.ext
      simp [double, neg]
    · exfalso
      rcases h3 with ⟨c, hc⟩
      omega
    · intro x
      apply Fin.ext
      have hx3 : x.val = 0 ∨ x.val = 1 ∨ x.val = 2 := by omega
      rcases hx3 with h | h | h <;> simp [double, neg, h]

/-- The doubling map on `Fin 7` has cycles `0`, `1 → 2 → 4 → 1`, and `3 → 6 → 5 → 3`. -/
theorem double7_orbits :
    double 7 (by omega) 0 = 0 ∧
    double 7 (by omega) 1 = 2 ∧
    double 7 (by omega) 2 = 4 ∧
    double 7 (by omega) 4 = 1 ∧
    double 7 (by omega) 3 = 6 ∧
    double 7 (by omega) 6 = 5 ∧
    double 7 (by omega) 5 = 3 := by
  decide

/-- The period of `1` under doubling on `Fin 7` is exactly three. -/
theorem double7_one_period :
    iterate (double 7 (by omega)) 3 1 = 1 ∧
    iterate (double 7 (by omega)) 1 1 ≠ 1 ∧
    iterate (double 7 (by omega)) 2 1 ≠ 1 := by
  decide

/-- The period of `3` under doubling on `Fin 7` is exactly three. -/
theorem double7_three_period :
    iterate (double 7 (by omega)) 3 3 = 3 ∧
    iterate (double 7 (by omega)) 1 3 ≠ 3 ∧
    iterate (double 7 (by omega)) 2 3 ≠ 3 := by
  decide

/-- Three doublings return every residue modulo `7`; `7 = 2^3 - 1`. -/
theorem double7_iter_three (x : Fin 7) :
    iterate (double 7 (by omega)) 3 x = x := by
  have h := double_iter_eq_id_of_dvd 7 3 (by omega) (by decide)
  simpa using congrFun h x

end Fold
