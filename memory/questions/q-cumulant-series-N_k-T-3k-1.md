---
name: Question — Why does N_k(T) := [E_3^k] log(F_P/f) start at T^{3k-1}?
description: Day 141 empirical discovery. The cumulant series log(F_P(T)/f(T)) expanded in E_3 has coefficients N_k(T) whose T-expansion starts at exactly T^{3k-1}. Values: N_1[T^2] = 3/2, N_2[T^5] = 27/5, N_3[T^8] = 417/8. The step-3 pattern strongly suggests a graded structure with E_3 having weight 3. Best candidate lead for a full closed form for U_b(w).
type: project
---

> **RESOLVED — Day 146 (2026-08-29).** Two parts, both answered.
> **(i) Why does $N_k$ start at $T^{3k-1}$?** Proposition 1 of the Day 146 write-up:
> Conjecture H part (H2) ($\deg_{E_3}[T^n]H\le\lfloor n/3\rfloor$, i.e. $H$ has order
> $\ge0$) implies $\Lambda=\theta\log F_P$ has order $\ge-1$, which is exactly
> $[E_3^kT^b]\log F_P=0$ for $b<3k-1$. A shorter *unconditional* version is in the same
> remark: if $\mathrm{ord}\,\Lambda=-N$ with $N\ge2$ then the LHS of (ME$_\Lambda$) has
> order exactly $1-2N$ while the RHS has order $\ge-N>1-2N$. Contradiction. So the
> $T^{3k-1}$ start is a two-line consequence of the master equation.
> **(ii) Why is the denominator of $n_k$ exactly $3k-1$?** Day 146 §9: in $(\rho,T)$
> coordinates the recursion inverts $(d+2\theta_\rho)$, giving denominators $d+2k$;
> on the order-$(-1)$ diagonal $d=k-1$ this is $3k-1$, never divisible by 3 — which is
> precisely why $b_k=(3k-1)n_k$ is an integer. On the order-$0$ diagonal $d=k$ it is $3k$,
> divisible by 3, and *that* is the source of every 3-denominator in the problem.
> See `proofs/2026-08-29-day146-bk-mod3-master-equation.md` §§4, 6.1, 9.

# Why does N_k(T) start at T^{3k-1}?

## The empirical observation

Day 141 PROVE session, coordinate change (U, V) = (u+1, v+1):
- F_P(T; U, V, E_3) := Σ_b P_b T^b/b!
- f(T; U, V) := Σ_b (U)_b(V)_b T^b/b! = _2F_0(U, V; ; T) formally
- Expand: log(F_P / f) = Σ_k E_3^k · N_k(T; U, V)

**Empirical:** N_k(T) starts at T^{3k-1} for k = 1, 2, 3 (verified explicitly).

Leading (top-in-UV, at T^{3k-1}) coefficients:
- N_1[T^2] = 3/2
- N_2[T^5] = 27/5
- N_3[T^8] = 417/8

## Why the step 3 is not random

E_3 is a degree-3 generator in the graded ring Q[E_1, E_2, E_3] (with the (1, 2, 3)-grading Rick uses throughout). log(F_P/f) is a formal power series in T over this ring. For each fixed T-degree n, the piece of log(F_P/f) is a polynomial in (E_1, E_2, E_3) — but the constraint that all degrees be homogeneous says pieces at T^n can involve E_3 only up to a certain power.

The step-3 pattern says: **E_3 acts as if it has T-degree 3** in the cumulant expansion. Not degree 1 or 2. This is compatible with a substitution T → some function that gives E_3 a "cost" of T³.

**Candidate explanations:**

1. **Regraded T substitution.** Perhaps log(F_P/f)(T; U, V, E_3) = h(T; U, V) + Σ_k E_3^k g_k(T; U, V) with each g_k being a series in T^3 (times an overall T^{something}). If so, we can substitute S := T³ and the cumulant becomes a series in (S, E_3) with a manifest grading.

2. **Combinatorial "each E_3 consumes 3 T-slots".** In whatever combinatorial expansion generates the cumulants, each E_3 factor is glued to a triple of positions. The 3^k(2k-1)!! pattern in the leading coefficient (Day 141 Theorem) is compatible with this — each of the k "matched pairs" involves 3 slots (2 endpoints + 1 marker?).

3. **Bethe-ansatz-like structure.** In quantum-group / Bethe-ansatz settings, the third generator E_3 often has "spectral parameter" role and its EGF-degree is bumped by a "R-matrix insertion" (which is degree 3 in the classical limit). This is speculative but consonant with Rick's Path 2 orientation.

## Attempt to reverse-engineer

If N_k(T) = T^{3k-1} · h_k(T; U, V) for some series h_k, then
$$\log(F_P/f) = \sum_k E_3^k \cdot T^{3k-1} \cdot h_k(T).$$
Substituting S = T³, this is
$$\frac{1}{T} \sum_k E_3^k S^k \tilde h_k(S)$$
where $\tilde h_k(S) = h_k(T)$ under T³ = S. If $\tilde h_k(S)$ has a clean closed form (constant? polynomial? geometric?), then log(F_P/f) simplifies drastically.

Leading (constant-in-UV) coefficients suggest a geometric or hypergeometric series in E_3 S. But the values 3/2, 27/5, 417/8 don't match a simple geometric.

Check the ratios:
- 27/5 ÷ 3/2 = 54/15 = 18/5
- 417/8 ÷ 27/5 = 2085/216 = 695/72
Ratios: 3.6, 9.65... no obvious pattern.

Check numerators: 3, 27, 417. Denominators: 2, 5, 8. Denominators are ARITHMETIC (2, 5, 8 = 2 + 3(k-1)). So denominators = 3k - 1 for k = 1, 2, 3. **This is exactly T^{3k-1}.**

**Cleaner form:** N_k(T)[T^{3k-1}] = (numerator_k) / (3k - 1).

Numerators: 3, 27, 417. Ratios: 9, 15.44... no.

But wait: multiplying by (3k-1) to clear denominators: 3, 27, 417. Let's check OEIS-style — divide by 3: 1, 9, 139. No obvious sequence. Divide 27 by 3: 9. Divide 417 by 3: 139. Hmm.

3 = 3 · 1
27 = 3 · 9 = 3³
417 = 3 · 139. 139 is prime.

Not obvious. Might be a specialization of a generalized hypergeometric coefficient. Post-FPSAC exploration.

## Priority

**HIGH — but AFTER Huang's Riccati test.**

Huang 2608.07599 is a specific ansatz (₂F_1/Riccati) that might just give the full closed form directly. Test it first. If Huang doesn't fit, then the T^{3k-1} pattern is the next best lead.

**In particular:** if Huang's Riccati holds, then the T^{3k-1} pattern should be an automatic consequence of expanding 1/₂F_1 as a cumulant series. Check this in reverse: does 1/₂F_1(t/q, t+1; 1/2; −qx/4) generate cumulants whose k-th coefficient has leading power x^{3k-1}? This is a CLEAN diagnostic for whether Huang's ansatz can possibly work.

## Attack plan

1. **Check ratio test.** Compute N_k(T) for k = 4, 5 (requires b ≥ 11, 14 in the recursion). If the pattern holds, promotion from "conjecture" to "verified for small k".
2. **Check the Huang→T^{3k-1} implication.** Expand log(1/₂F₁ / f) as a cumulant and check whether the k-th coefficient starts at T^{3k-1}. If yes → strong evidence Huang encodes U_b. If no → Huang is not the right ansatz.
3. **Try substitution S = T³.** Rewrite log(F_P/f) in (S, E_3) variables and see if a closed form emerges.
4. **Check for R-matrix / Bethe interpretation.** Deferred to post-FPSAC.

## Files

- Empirical values: `~/projects/proofs/2026-08-28-day141-ub-closed-partial.md` (Gap 3 section)
- Compute code: `~/projects/beta-prime/code/day141_ub_closed/deep_work/hunt_ratio.py`

## Related

- `q-huang-riccati-Ub.md` — the primary lead, test first
- `connections/2026-08-28-day141-UV-coordinates-and-leading-EGF.md` — the leading closed form; N_k is the correction structure

---

**RESOLVED (Day 148, recorded Day 150 dream).** The closed form for $F_P$ (Horn hypergeometric,
obtained by unfolding the umbral map $\mathcal T$) makes the $T^{3k-1}$ starting index a
consequence of the weighted grading $\mathrm{wt}(E_3)=3$, not a mystery. The $b_k$ they define are
now understood via the Day 148 quintic $F(1-F)^3(3-4F)=\vartheta(3-2F)^2$, and
$b_k\equiv0\bmod 3$ is a theorem. No open content remains here; kept as lineage.
