---
name: Day 142 — Frobenius ODE L·F_P = F_P·X, boundary decomposition of X_1
description: Day 142 PROVE. Derived L := T(U+θ)(V+θ) - θ annihilating f = ₂F₀(U,V;;T). Applied to F_P → Frobenius identity L·F_P = F_P·X with X starting at E_3^1 and having universal (U,V)-independent leading coefficient -3, -18, -255, -4620, -94500 at [E_3^k T^{3k-1}]. Derived ODE for N_1 = [E_3^1] log(F_P/f): T·θ²N_1 + [T(U+V) - 1 + 2Tφ]·θN_1 = X_1. X_1 admits boundary decomposition but has full rank b-1 in the (U,V)-interior, so no rank-1 closure. FPSAC Theorem 3.3 corollary material.
type: project
---

# Day 142 — The Frobenius identity and the ODE for N_1

## Setup

Rick's leading EGF (Day 141):
- f(T; U, V) = Σ_b (U)_b(V)_b T^b/b! = ₂F₀(U, V; ; T) formally
- F_P(T; U, V, E_3) = Σ_b P_b T^b/b!
- N_k(T; U, V) := [E_3^k] log(F_P / f)

## The differential operator L

f satisfies
$$L \cdot f = 0, \quad L := T (U + \theta_T)(V + \theta_T) - \theta_T$$

where θ_T = T · d/dT. Derivation: coefficient recurrence (U)_{b+1}(V)_{b+1} = (U+b)(V+b)(U)_b(V)_b is the b-th coefficient of L·f under T-shift.

## The Frobenius identity

**Theorem (Day 142).** L · F_P = F_P · X(T, E_3, U, V), where X is a formal series in T with coefficients polynomial in (U, V, E_3), of E_3-degree ⌊b/2⌋ at T^b.

Verified up to T^18.

**Universal invariant.** [E_3^k T^{3k-1}] X = -3, -18, -255, -4620, -94500 for k=1..5. **(U, V)-independent.**

Sequence -3, -18, -255, -4620, -94500 is **NOT in OEIS**. Prime 17 in factorization at k=3 rules out simple polynomial-in-k formulas. It's a genuine new Rick-invariant.

## The ODE for N_1

Writing log F_P = log f + R with R = Σ_k E_3^k N_k(T; U, V), and X = Σ_k E_3^k X_k, substituting into L(f e^R)/(f e^R) = X and extracting [E_3^1]:

**Theorem (Day 142).**
$$T \cdot \theta^2 N_1 + [T(U + V) - 1 + 2 T \phi] \cdot \theta N_1 = X_1$$

where θ = T d/dT and φ := θf / f (a formal series in T with coefficients in ℤ[U, V]).

**Verified** to T^9 with full (U, V) polynomial coefficients.

This is a **first-order linear ODE for M := θN_1** with formal integrating factor
$$\mu = T^{-(U+V)} \cdot e^{-1/T} \cdot f^{-2}.$$

## Explicit X_1 formulas

### On the boundary V = 0

$$X_1[T^b]\bigg|_{V=0} = -(U+1)_{b-3} \cdot \big[(2b-1)U + (b-2)(b-1)\big]$$

Verified b = 3..8. Clean product form.

### Symmetric boundary decomposition (full (U, V))

$$X_1[T^b] = \underbrace{-(2b-1)\big[(U)_{b-2} + (V)_{b-2}\big] - \frac{(b-2)(b-1)}{(b-3)!}\, (U+1)_{b-3}(V+1)_{b-3}}_{\text{"boundary" part}} + U V \cdot R_b(U, V)$$

where R_b is a symmetric polynomial of bidegree (b-3, b-3). The boundary part IS a closed form; R_b is a residual "interior" object with no rank-1 structure.

**Obstruction to full closure:** X_1 has rank b-1 in the (U, V) monomial basis. It genuinely has b-1 independent "modes" in the interior. The V=0 axis cleanliness is a coordinate-axis artifact — not a lift to full (U, V).

## What this gives Rick

1. **A concrete second-order linear ODE for N_1** in one variable T with (U, V, φ)-coefficients.
2. **A closed form for X_1 on the two boundaries V=0, U=0.**
3. **A boundary + correction decomposition** that isolates the tractable structure.
4. **A universal (U, V)-independent invariant** -3, -18, -255, -4620, -94500 = the leading [E_3^k T^{3k-1}] of X.

Enough for **FPSAC Theorem 3.3 statement (leading closed form) + Corollary 3.4 (Frobenius identity) + Conjecture 4.1 (full closed form for X_1)**.

## What this does NOT give

- No closed form for the interior R_b of X_1.
- No closed form for X_k, k ≥ 2 (harder).
- No proof of the universal (-3, -18, ...) invariant — only empirical.

## Next moves (post-FPSAC)

- **Try substitution U = α+β, V = αβ (Vieta / roots of a quadratic).** Might trivialize R_b.
- **Try change of basis on the interior.** The (U, V) monomial basis has b-1 independent modes; a different basis (e.g. Chebyshev, Schur, immaculate) might reveal rank-1.
- **Look at X_k jointly.** The universal leading in k suggests a "top-grading" invariant that's cleaner than X_1 alone.

## Rule attribution

- **Rule 9 (change-coordinates)** fires **THIRD TIME** if the ODE for N_1 turns out to be trivially solvable by an integrating-factor substitution.
- **Rule 8 CANDIDATE (Taylor around shifted base)** — still pending firing #2. NOT this cycle.

## Files

- `~/projects/beta-prime/code/day142_angle4_ode/{ode_ansatz_v3.py, analyze_LFPFP.py, lift_X1_v5.py, lead_ODE_N1.py, RESULT.md}`
- `~/projects/beta-prime/code/day142_huang_riccati/RESULT.md` — the Huang negative

## Related

- `q-huang-riccati-Ub.md` — RESOLVED (NEG), predecessor
- `q-cumulant-series-N_k-T-3k-1.md` — the T^{3k-1} pattern (now has a partial explanation via the ODE)
- `connections/2026-08-28-day141-UV-coordinates-and-leading-EGF.md` — the leading EGF this ODE lifts
