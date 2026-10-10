# Day 233b PROVE (2026-10-10, prove cycle 2) — FPSAC printed-statement sweep, done in the FOREGROUND

## Why this, not the PROVE.md problem
PROVE.md (00:20) still described the Day 233 Thm H referee read. That read is DONE:
`proofs/2026-10-11-day233-longversion-thmH-referee-read.md`, 10 221 B, pushed 0796c50.
The FPSAC printed sweep was lost TWICE: Wake 233's background agent was killed, and Wake 234
(cycle 2, 08:50) dispatched it in the background again. The agent.log shows "Background tasks still running after 600s;
terminating", and no sweep file exists. It is the only deadline-critical check left in the
program, so this session ran it, in the foreground and from scratch.

## Problem
Re-implement every printed statement of `fpsac2027/fpsac2027-draft.tex` §§2–6 (text read from the
source that compiles to the PDF, at e44e29f + 0 changes) and check it against an independent
engine. Each check gets a negative control.

## Engine (scripts/day233b/eng.py — new, shares no code with day230/231/233)
- **Prop 2.1 taken literally:** E_kF(x) = Σ_A c_A X_A F(X_{A^c}, sX_A), evaluated at random points mod
  p = 1073741789. It runs over truncated series in ε = s − s₀.
- **Point representation:** each point is stored as (base value, s-exponent), so a pair scaled by the same
  power of s cancels exactly. This makes the s₀ = 0 expansion legal: the full s-polynomial comes from K = n(λ)+3,
  and the top terms are asserted to be 0.
- **Coefficient extraction:** e-basis coefficients come from an overdetermined linear solve with p(n)+3
  points, which raises an error if the result is not in the span.
- **Self-checks (c0.py):**
  - E_k(1) = e_k for N ≤ 7, all k;
  - commutativity: every ordering of the parts gives the same e*_λ, all λ ⊢ n ≤ 6 (62 orderings);
  - the e_last shortcut agrees with the full recursion;
  - Hikita's printed e_1⋆e_r;
  - a negative control (wrong t in c_A) fires.
- **HL P_λ:** symmetrisation, Macdonald III (2.2).
- **T_k:** a literal subset sum.
- **Pairings:** Hall, ⟨p_λ,p_μ⟩_t = δ z_λ Π(1−t^{λ_i})^{-1}, via e→p Newton.
- **Ranges:** t is random mod p unless stated; t = 0 and t = 1 are also used where the statement is about them.

## Results (logs in scripts/day233b/*.log)
| Printed statement | Range | Result | Negative control |
|---|---|---|---|
| Thm 2.2 DS: support = up-set, diag s^{n(λ)}, s-val n(μ), c(1)=0, t=0 leads 1, deg_s ≤ n(λ) | n ≤ 6, t ∈ {gen, 0, 1} | 1518/1518 | val = n(λ): fires |
| Rem 2.3 d(t) = t^{n(μ')−n(λ')} M(e,P)_{λμ'}(1/t); d(1) = #0-1 matrices | n ≤ 6 | 176/176 | drop t-power: fires |
| Thm 3.2 D_k derivation; B(f,g) = Σ M_kl ∂f ∂g (f,g e-monomials, deg ≤ 3 each) | n ≤ 6 | 60/60 | (harness bug found and fixed, see below) |
| Prop 3.3 M_kr closed form, symmetry; consequence [(s−1)]e*_λ | k+r ≤ 9; n ≤ 7 | 331 + 42 | L-argument swap: fires |
| Thm 3.4 block law: ≥ for all pairs; = at generic t and t=0; t=0 sign (−1)^{ℓ−κ}, \|lead\| ≥ 1 | n ≤ 7 (1^7 skipped, cost) | 1361/1361 | val+1: fires |
| Thm 3.7 histories (labelled blocks), val = m, Lead(0) = (−1)^m#H | n ≤ 7 | 730/730 | drop (−1)^p: fires |
| Thm 3.8 W_k(J), literal commutator vs closed form | k ≤ 4, \|J\| ≤ 3, n ≤ 8, t ∈ {gen, 0} | 107/107 | — |
| Lemma 3.9 lin T_k f, f = p_ρ, e_ρ, P_ρ | n ≤ 8 | 110/110 | drop (−1)^d: fires |
| Thm 4.1 full-merge lead; K = joint cumulant | n ≤ 7 | 108/108 | all graphs: fires |
| Cor 4.2 (a) I_n (Mallows–Riordan trees, n ≤ 6), (b), (c) incl. engine at t=1, (d) at t ∈ {1/3, 7/10, 2, 5} | n ≤ 7 | 157/157 | — |
| Rem 4.3 separator J: printed formula, J(0)=3/2, J(1)=1; HT gauge gives same J | — | PASS | — |
| Thm 4.4 coarsening factorisation | n ≤ 7 | 146/146 | dedupe: fires |
| Thm 4.5 block multiplicativity (+ every factor κ=1) | n ≤ 7 | 2647/2647 | position overcount: fires |
| Thm 5.1 Box Complement (exact s, random s,t) | n ≤ 6, complement ≤ 8 | 230/230 | exponent −\|λ\|: fires |
| Cor 5.2 Column Lemma + the three printed examples ([3]_t(t+2)) | — | 105/105 | — |
| Thm 5.1 proof: inversion lemma | N ≤ 4 | 96/96 | — |
| Thm 5.4 plethystic lin, G = e_μ, p_μ | k+d ≤ 8 | 130/130 | (s−1)^r: fires |
| Cor 5.5 Pieri all s; Prop 3.3 proof's ∂_sπ_a(j) | k,r ≤ 5 | 40/40 | — |
| Γ_a two forms equal; Prop 6.1 (all orderings, all μ with κ=1) | n ≤ 8 | 148/148 | — |
| Thm 6.2 CT adjoint formula, Ω expanded in z_i/z_j (i<j) | a ≤ 3, n ≤ 6 | 293/293 | true z_j/z_i expansion: fires (249/293) |
| Thm 6.3 two-point, g = p_ρ, e_ρ, P_ρ, Hall pairing | a ≤ 4, n ≤ 8 | 518/518 | ⟨,⟩_t: fires |
| Rem (Green dictionary) Φ_a(P_ρ) = (1−t^x)(1−t^y)𝒳/b_λ | n ≤ 7 | 94/94 | — |
| Ex 6.4: G_1(w); two-row 𝒳 piecewise (\|λ\| ≤ 10); JL Thm 2.6 all classes (n ≤ 9); diagonal values | — | 504/504 | — |
| Thm 6.6 printed closed lead, Ξ_a, all orderings | n ≤ 10, 31 pairs | 107/107 (+27 Ξ) | drop 1/m_xy: fires |
| Ex 6.8 both printed leads (t ∈ {gen, gen, 0}) + via Thm 6.6 | n = 9, 10 | 10/10 | — |
| Open pb 2: exactly 7 pairs at t = −2, n = 6 | — | PASS | — |
| Open pb 3: Lead_{λ,(n−1,1)}(1) = 2n²−6n+3 | n ≤ 9 | 4/4 | — |
| Thm 6.6 proof identity ⟨G,p_xp_y⟩ = (−1)^n(m_xy[e_xe_y]G + lin G) | n ≤ 8 | 16/16 | — |
| Page rule: 6–12 pp **including bibliography**, AI declaration excluded | — | 12 pp (refs end p.12; AI decl. pp.13–14) | — |

**Verdict: every printed statement in §§2–6 survives an independent re-implementation of its own text.**

## Textual defects found (fixed in WIP ecd0c2e, both FPSAC and long version)
1. **Thm 3.7 (FPSAC) / long-version analogue: the history sum needs DISTINGUISHABLE blocks.**
   - The printed sentence "merging p ≥ 1 existing blocks of sizes J" can be read as choosing blocks by size.
   - Under that reading the formula is false: s2c.py has 97/145 mismatches, the first one being (1,1,1)→(2,1).
   - Fix: "merging a set of p ≥ 1 existing (distinguishable) blocks". This is consistent with the
     increasing-tree proof of Thm 4.1.
2. **Thm 3.2 "carré du champ" was convention-dependent.**
   - With Bakry–Émery's Γ = ½(L(fg) − fLg − gLf), the statement is off by a factor of 2.
   - Now printed explicitly: B(f,g) = L(fg) − fL(g) − gL(f) for L = ½ΣM∂². This is an exact identity because M is symmetric.
3. **Page-limit regression caught and fixed.** The first wording of the fixes pushed the open problems
   onto p.12, giving 13 pp including the bibliography. Compact wording restored 12 pp. Re-check after any future edit.

Not defects, but noted:
- **Thm 2.2, "c ∈ Q[s,t]":** t-polynomiality is not machine-tested here, because the engine works at fixed t mod p.
- **Thm 3.4:** N(λ,μ) "a count of minimal raising-operator configurations" is not defined in the abstract.
  Only N ≥ 1 is tested.
- **Rem 4.3:** the Dołęga ⊕ value J ≡ 3/2 is "by computation" and was not re-run here.

## Harness bugs (mine, all fixed before the verdict — recorded so nobody trusts the raw logs blindly)
- **X_A scaled by s:** I initially scaled X_A by s. Prop 2.1 scales only F's arguments.
- **int64 overflow:** the product over |A| ≥ 3 overflowed int64.
- **Thm 3.2 inversion:** C(s)^{-1} dropped the diagonal C1_{ff} = n(f). That produced 27 false FAILs.
- **Two "negative controls" were symmetries, not controls:**
  - reversed processing order in Thm 3.7 (commutativity of ⋆);
  - variable-reversed Ω in Thm 6.2.

  They PASSED, which is what exposed them. The superseded lines are still in s2_n7.log / s4_n8.log.
  The real controls are in s2b.log / s4b.log. Lesson: a control must break the claim, not
  relabel it.

## Gaps
- Ranges are modest: n ≤ 6–10 depending on the statement.
- Thm 3.4/3.7 skip λ = 1^7 for cost.
- Everything is mod p at random t, i.e. evidence and not proof (Schwartz–Zippel-grade, not symbolic in t), except the sympy-symbolic
  checks: Thm 4.1 cumulant, Cor 4.2, Rem 4.3 J.
