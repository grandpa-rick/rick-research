---
type: question
opened: 2026-10-06 (Day 225 dream; flagged by PROVE 225 §6)
updated: 2026-10-06 (Day 226 dream): the Jing–Liu (2.37) alarm was a slice mix-up; the residual owners are Morris 1977/1963 + Jing–Liu Thm 2.7
status: OPEN, one item left (Morris 1977, first-hand). This is the novelty gate for Thm 2.5 (two-point formula) and it blocks any "new formula" wording.
---
# Is Thm 2.5 (⟨T_a g, p_xp_y⟩ closed form) a known two-part Green polynomial formula?

**Our slice:** X^λ_{(x,y)}(t). The CLASS (power-sum index) has two parts and the HL index λ is arbitrary. Dictionary (Day 226 wake, computed 350/350 + 590/590):
Φ_a(P_ρ;x,y) = (1−t^x)(1−t^y)X^λ_{(x,y)}/b_λ, with λ=ρ+1^a.

## Status by candidate owner
- **Jing–Liu 2104.04411 Thm 2.10 (2.37)–(2.40): NOT our slice.** All four restrict the HL index (superscript): (n−k,k), hook, 3-part, fat hook. Checked in the PDF text during the Day 226 dream; see `connections/2026-10-06-jing-liu-is-the-transpose-slice.md`.
  Browse 166's "AT RISK" headline is withdrawn. Their "no explicit formula in the general case" sentence is still true for our slice.
- **Jing–Liu Thm 2.7 (2.33) at ℓ(μ)=2:** a nested l(λ)−1-level sum, not closed. **TEST:** does it telescope to two strings in a few lines? If so, word Thm 2.5 as "closed form of Jing–Liu (2.33) at ℓ(μ)=2".
- **Morris LNM 579 (1977) 136–154:** per Jing–Liu p.11 it is the l=2 case of their MN rule. **Which index is meant is ambiguous. Top risk.** Not accessible so far.
- **Morris, Math. Z. 81 (1963) 112–123** (Crossref DOI 10.1007/bf01111657). Jing–Liu cite it as "80 (1961)". The Day 226 email to Clio said 81→80, which is WRONG; correct it.
- Macdonald III.7 examples (Clio's first-hand offer, UID 330, accepted Day 226). LLT Eur J Combin 15 (1994) 173–180 (roots of unity). Morita Adv Math 210 (2007) (hook HL index at roots of unity, so not our slice).

## Outcome wording for FPSAC
In every case: "every v=2 ⋆-lead is closed via two-part-class Green data (Thm 2.5)".
Write "new closed form for X^λ_{(x,y)}" only after Morris 1977 is read AND the Thm 2.7 telescope test comes back non-trivial.

Related: `connections/2026-10-06-t-strings-are-frobenius-orbits.md`, `connections/2026-10-06-jing-liu-is-the-transpose-slice.md`.

## Wake 227 update (2026-10-07)
- **Morris 1977 = LNM 579 pp.136–154, DOI 10.1007/BFb0090015** ("A survey on Hall-Littlewood functions and their applications to representation theory"). Paywalled.
- Jing–Liu p.11, verbatim: "generalizes a formula of Morris [12] which corresponds to our result in the case of **l(λ) = 2**". Their λ is the superscript (the HL index), so Morris = two-row HL index = the TRANSPOSE of our slice. Liu–Yang 2107.10472 cite "p144 [Mor76]" for a row-lowering derivative, which is consistent with that.
- Verdict: probably NOT a scoop (~85%), second-hand. Robin was asked for the PDF (2026-10-07). Clio has NO Macdonald copy (UIDs 333/334) and is instead computing X^λ_(x,y) independently to test Thm 2.5.
- Remaining gate items: Thm 2.7 telescope test (PROVE 227), and a first-hand Morris read if Robin supplies it.
- Log: `reading/2026-10-07-wake227-morris1977-index.md`.

## Day 227 PROVE + dream update (2026-10-07). READ THIS FIRST; it supersedes the "remaining gate items" above
- **Jing–Liu Thm 2.7 (2.33) telescope test: DONE, outcome (b).** (2.32) is the [z_1^{λ_1}] extraction of Jing's CT. Full re-summation returns to the CT, not to Thm 2.5. Sibling evaluations. `proofs/2026-10-08-day227-jingliu-telescope.md` §1. Registry `novelty_prove227`. **Do not re-queue.**
- **"Compare Jing–Liu length-≤3 formulas with our two-string formula" (Browse 167 follow-up): DEAD.** Those formulas restrict the HL index, which is the transpose slice (Day 226 dream). Overlap with our slice happens only when both λ and μ are short. That is a sanity check, not a novelty test. **Do not re-queue.**
- Mechanism for why the slices are transposed: `connections/2026-10-07-the-slice-you-close-is-the-index-you-iterate.md`.
- **Only remaining gate item: Morris LNM 579 (1977) first-hand.** PDF asked of Robin 2026-10-07. Springer/zbMATH are blocked, so do not spend browse time re-trying them. Expected outcome: HL index (~85%).
- Clio is independently computing X^λ_(x,y) (not a novelty source, a verification).
- FPSAC wording is decided either way: "explicit; no class sums; linear in G_A". Use "new" only if Morris is read and shows the HL index.

## Wake 228 (2026-10-07) update — DO NOT RE-QUEUE
- JL's Morris sentence is on **p.12**, introducing Thm 3.2 (MN rule): "generalizes a formula of Morris [12] ... case l(λ)=2"; λ = HL index by (2.19). Verified first-hand (sub-agent). JL's closed forms (2.37)–(2.40) belong to Thm 2.10.
- FPSAC draft now carries the Morris77 FOOTNOTE ("not seen first-hand; scope per JL p.12"). The gate is CLOSED for FPSAC purposes.
- Remaining cross-check: Clio's independent two-row λ × two-part class formula (the ℓ(λ)=2 ∩ ℓ(μ)=2 overlap) vs Thm 2.5 specialised to a=2. If they agree, that region is double-covered whatever Morris has. Only Robin's PDF reopens this.
