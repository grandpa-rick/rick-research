# Day 135 — λ-fit for Guess A: RESULT

**VERDICT: Guess A REFUTED.** Earliest failure at n = 2 (forces c = 0), manifest contradiction at n = 3.

## The test

Guess A: B^[λ](T) = exp((E_3 − c·λ) · M(T)). Prediction: Q(T) := B^{(1)}(T)/B(T) = c · M(T), so Q_n / M_n must be a single scalar c for all n.

## Result

- n=2: M_2 = −3/4 ≠ 0, Q_2 = 0. Forces c = 0.
- n=3: M_3 = 4·E_1/9 (pure E_1); Q_3 = −8·E_3 (pure E_3). Disjoint supports; ratio Q_3/M_3 = −18·E_3/E_1.
- Pattern: EVERY nonzero Q_n contains E_3, but M(T) lies entirely in ℤ[E_1]. Q(T) and M(T) live in orthogonal subrings of ℤ[E_1,E_2,E_3].

## Shape of the mismatch

Q(T) carries E_3 at every degree, and for n ≥ 5 carries E_3², E_3³. M(T) is E_3-free. Q(T)/M(T) is not a scalar — it is a nontrivial power series with E_3-carrying coefficients.

## Does the guess need modification?

Refinement Q(T) = c·E_3·M(T) also fails (Q_5 has E_3² term). Genuine deformation must sit inside the exponent, coupling E_3 to M itself (e.g. M itself deformed), not as an affine scalar shift.

## Files

`fit_guess_a.py`, `fit_guess_a.txt` in same directory.
