# Aug~ as a Strict Extension of Kashiwara Crystal Action

> **Born 2026-05-14 from the CST-bridge verification (PARTIAL verdict, 0.75 conf).**

## What was verified

Hand-check at B_2 of the load-bearing CST claim "Rick's REDUCED quotient = Kashiwara's bracket-cancellation S_i → S_i^c via the CST bijection Ψ":

**Test 1 (B_2, π = 1·β_{1,1} + 2·γ_{1,2}, c = +2 at s_2 = s_n):** Operations AGREE term-by-term. Ψ ∘ e_2² = e_2² ∘ Ψ as expected from CST Thm 3.1.

**Test 2 (B_2, π = 2·β_{1,1} + 2·γ_{1,2}):** Operations DIVERGE.
- Tableau side: S_2(π) = `(((())))` cancels COMPLETELY → e_2 π = 0 in the crystal (π is at the bottom of its 2-string).
- Kp side: Rick's REDUCED multiset {(LL,+):1} still validly acts under donor-capacity constraint → π → 3·β_{1,1} + 1·γ_{1,2}.

**Conclusion: Aug~ is strictly broader than Kashiwara e_i / f_i.**

## The structural picture

Aug~ on Kp(∞) splits into two regimes:

### Open-crystal slice
Where Kashiwara operators e_i, f_i return non-zero. Here Aug~ pulls back through CST to a Z-linear combination of Kashiwara crystal operators, with a **unit-mismatch factor**:

> **One reduced orbit-swap step = k Kashiwara steps**, where k = units(st) = 1 for simply-laced, 1 or 2 for doubly-laced.

For a 2-unit swap (e.g., s_n at B_n on a long-long orbit), one Aug~ step equals **two** sequential e_i / f_i applications on the tableau side, each with its own intermediate bracket-cancellation pass.

### Off-slice
Where Kashiwara operators return zero (the i-signature has fully cancelled). Here Aug~ keeps going, sliding via donor-capacity constraint without a Kashiwara analog. This regime is the "(+, −) cancellation" gap — the doubly-laced gap between donor capacity and Kashiwara count.

In simply-laced types, every orbit has uniform unit-size 1, so "Kashiwara count exhausted" = "donor capacity exhausted." No gap, no off-slice. In doubly-laced types, 2-unit orbits create a gap: capacity ≥ 1 but Kashiwara count = 0.

## What this means for SU1

**SU1 REDUCED uniqueness is NOT a corollary of Kashiwara crystal uniqueness.** The two operations differ precisely off the open-crystal slice — which is where REDUCED has its non-trivial content. Rick's orbit-decomposition proof (Phase B of v1) is the right argument and is independent.

The CST bridge gives a **structural identification of Aug~ on the slice** — but the off-slice behavior is the doubly-laced novelty, and that is exactly what SU1 controls.

## What this means for the paper

- **v1 stands.** Section 2's REDUCED uniqueness is genuinely new, not "Kashiwara in disguise."
- **v2 or a sequel** can add a section (or a companion note) on the CST bridge: "Aug~ as a strict extension of Kashiwara crystal action on B_n / C_n marginally-large tableaux, with the doubly-laced off-slice gap as its non-trivial content."
- **Lee FPSAC paper (Choi-Kim-Lee 2412.20757) becomes a cleaner companion piece:** Lee builds the Lusztig q-weight polynomial via KR-crystal sums; Rick builds the BGG chain complex whose Euler characteristic is that polynomial, AND identifies the chain operator (Aug~) as a strict extension of crystal action with new doubly-laced content.

## What this means for the coideal commutativity test (Watanabe)

The type-AII coideal generators B_i = F_i + θ-twist live on the open-crystal slice (since F_i = f_i in the crystal limit). So the natural commutativity question splits:

- **On-slice commutativity:** does B_i commute with Aug~|_{slice}? Likely yes (or known) — this is a Watanabe-style check.
- **Off-slice extension:** does B_i, extended somehow, commute with the off-slice Aug~? This is the open and harder question — likely where the type-B BK involution gap (Gutiérrez) lives.

## Three concrete follow-up tests (from the verification agent)

1. **C_2 at i = n (long flip).** Type-C i = n branch in CST Def 2.14 has 3-4 special cases. Structural alignment will be subtler.
2. **B_3 case with multi-orbit interaction.** Pick a simple i (e.g., i = 1) where multiple s_1-orbits exist so the bracket sequence Φ_i^B genuinely mixes brackets from different orbits. Verify orbit-by-orbit decomposition still holds.
3. **Both e_i and f_i in sequence.** To check that Rick's *signed* multisets really do encode signed Kashiwara chains.

## Status

**Categorical-home picture clarified, not yet a theorem.** On-slice agreement verified at B_2. Off-slice divergence verified at B_2. Multi-rank / multi-orbit / mixed-direction checks still TBD.

**Priority order:**

- (P0 carry-over) Continue waiting for Robin's read of v1.
- (P0.3 NEW) C_2 i=n long-flip test — concrete, ~1 hour, tests type-C edge case.
- (P0.5 NEW) B_3 multi-orbit test — most informative remaining case.
- (P0.7 NEW) Mixed-direction signed-chain test.
- (P1) Coideal commutativity on-slice at B_2 — once on-slice picture stabilises.

Date: 2026-05-14 (PARTIAL verdict from bracket-cancellation hand-check).
