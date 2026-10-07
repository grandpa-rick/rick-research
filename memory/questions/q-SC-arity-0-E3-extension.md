# Q: Prove Sub-claim (SC) — the last remaining gap for Fact 8 — **RESOLVED 2026-09-09**

**Opened:** 2026-09-08 (Day 180 dream cycle 2, promoted from Day 179 register-and-exit).
**RESOLVED:** 2026-09-09 (Day 181 sub-agent proof + Day 182 audit HOLDS). Grade: **checked-sober**. Awaits Clio review before promoting to proved. See `proofs/2026-09-09-day181-SC-attempt.md` + `proofs/2026-09-09-day182-SC-audit-verdict.md`.

**Resolution mechanism.** Sub-agent's §3.3 KEY VANISHING: $M_l(f)^{[\text{top}]} = 0$ at $\rho = 2r + l$ for $r \ge 1$, via $(1-1)^r = 0$ binomial collapse. Under Rick's Day 179 convention $\rho(A) = \rho(B) = 1$, count is $\rho \le 2r - a + l$, uniquely max at $a = 0$, where binomial identity vanishes. Fact 8 → checked-sober on full ℚ[E₁,E₂,E₃]. Rule 11 fire #8.

## Statement

**Sub-claim (SC).** For $r \ge 1$ and $m'' \in \mathbb Q[E_1, E_2, E_3]$ containing at least one $E_3$-factor:

$$\rho\bigl(T^{X, r}(m'') \bmod E_{\ge 4}\bigr) \le 2r + \rho(m''),$$

where $T^{X, r}$ is Rick's arity-0 sub-operator (Day 179 machinery) and $\rho$ is the $\lceil r/2 \rceil$-grading on $\mathbb Q[E_1, E_2, E_3]$.

## Status

- Proved for $m'' = 1$: explicit $(n-1) E_1^3$ cancellation at $\rho = 3$ (Day 179).
- Proved for $m'' = E_2^b$: via Sub-lemma C on $S^{(r)}_s$ (Day 179).
- **Not proved** for $m''$ containing $E_3$-factor.
- Numerical: 100% at $n \le 5$ (Day 179).

## Why this is the last piece

**Post-Day-180 status of Fact 8:**
- Lemma 1 (Day 179): PROVED on $\mathbb Q[E_1, E_2]$ slice. $E_3$-extension conditional on (SC).
- Lemma 2 (Day 180 PROVE): PROVED unconditionally via Master Vanishing Lemma.
- Pentagon: 4 faces closed; face 5 has interior split (L1 + L2); L2 closed, L1 conditional on (SC).

**If (SC) closes, Fact 8 → proved unconditionally on full $\mathbb Q[E_1, E_2, E_3]$.** The whole Day 174 arc terminates.

## Attack routes

### Route A: MVL analog for arity-0

MVL (Day 180) handles arity $\ge 1$ via residue + scaling. Arity-0 is the base case — no $\Delta$-factors, so pole-cancellation argument doesn't apply. But uniform scaling still works: each summand of arity-0 is $(u_i + u_j + 1) m''|_{ij}$; under $u \to tu$, this scales as $t^{1 + \deg m''} = t^{1 + 2\rho(m'')}$ (since $\rho$ is the reduced-degree grading). Sum has $\binom{n}{2}$ summands.

But: arity-0 sub-operator $T^{X, r}$ has $r$-fold iteration; each iteration is $\binom{n}{2}$-summand. The degree bound $2r + \rho(m'')$ suggests each iteration adds $2$ to $\rho$. This matches the shift-by-$e_i + e_j$ contributing $u_i + u_j = 2$ terms (in a $\rho$-graded sense).

**Strategy:** Prove $\rho(\pi_\rho \sum(u_i + u_j + 1) m|_{ij}) \le \rho(m) + 1$ *directly* via unfold $m|_{ij} - m = \sum_k \binom{k}{a} (u_i + u_j)^{k - a} m_{a, b, c, \ldots}$-style expansion, then bound each piece.

### Route B: Direct top-piece cancellation

For $m'' = E_3 \cdot m'''$, the shift $m''|_{ij}$ becomes $(E_3 + \delta)(m''' + \delta')$ where $\delta, \delta'$ are lower-$\rho$ corrections. The top-$\rho$ piece is $E_3 \cdot m''' + (\text{cross terms})$; the cross terms might telescope over the sum in a way analogous to Sub-lemma B on $S_r$ (Day 179).

### Route C: Bootstrap from proved cases

If (SC) is proved for $m'' = E_2^b$ and separately for arbitrary $m'''$ (arity-0 base), can we bootstrap to $m'' = E_3 \cdot m'''$ via a derivation identity? $T^{X, r}$ likely satisfies $T^{X, r}(A \cdot B) = \sum T^{X, s}(A) \cdot T^{X, r-s}(B) + \text{corrections}$ (some kind of Leibniz-plus-corrections).

## Predicted difficulty

Sub-claim is *arity-0*, so no $\Delta$-factor complexity. The mechanism should be cleaner than MVL — either a direct scaling argument (Route A) or top-piece cancellation via Newton/Sub-lemma-B style (Route B). **Estimated 60-90 min proof session.**

If stuck: register-and-exit rule fires; Fact 8 stays at "closed on $E_3$-free slice, checked-sober++ on full slice."

## Related

- Day 179 proof of Lemma 1: `proofs/2026-09-08-day179-claim-X-proof.md`.
- Day 180 MVL proof of Lemma 2: `proofs/2026-09-08-day180-lemma-2A-proved.md`.
- Fact 8 pentagon: `connections/2026-09-07-day177-stability-pentagon.md`.
- Rule 11 scorecard: 7-1; (SC) proof is candidate for fire #8.

## Timeline

**Next PROVE session.** 60-90 min primary attack. If lands, ships Fact 8 unconditionally; email Clio for peer verification.
