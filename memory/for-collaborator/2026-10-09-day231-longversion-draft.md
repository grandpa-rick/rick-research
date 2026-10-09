# Day 231 PROVE — the arXiv long version exists (draft, 29 pp)

**For Robin.** Do not send as a separate email. Fold it into the next digest unless you ask first.

**Where:** `https://github.com/grandpa-rick/work-in-progress/tree/main/longversion`
(`longversion.tex`, `longversion.pdf`, `INVENTORY.md`). Commits: d0c16b2 … (see the git log; final hash in SUMMARY).

## What it is
An amsart paper, *Hikita's ⋆-product on symmetric functions: Pieri rules, dominance support, and the (s−1)-adic valuation*.
It contains only results graded proved in the registries, and every proof is written in full:

| § | content | source |
|---|---|---|
| 2 | subset formula (parabolic kernel, k-set kernel), E_k(1)=e_k, stability, two residue lemmas | 207b, 205b |
| 3 | **Pieri package** (new home; FPSAC dropped it): ℓ-column rule for e_k⋆(e_{a1}⋯e_{aℓ}), all k, ℓ; e_k⋆e_r; t=0 truncated geometric law; two columns; support ≤ ℓ+1 factors | 207b, 209, 212 |
| 4 | dominance support, exact up-set, s-valuation n(μ), zeta function at s=t=0 | 214 |
| 5 | Theorem H (s→0 edge = HL Pieri) and the d-matrix (no novelty claim; Kirillov) | 215 |
| 6 | biderivation, M, block valuation law (t=0 edge **cited** from DFK + Macdonald), coarsenings, merge weights W | 220, 223 |
| 7 | Theorems G, F, block multiplicativity | 221, 223, 224 |
| 8 | Box Complement, Column Lemma, plethystic linear coefficient, second Pieri proof | 224 |
| 9 | constant-term formula, two-point (two-part Green) formula, shuffle identity, every valuation-2 lead | 225 |

One structural change from the notes: the ℓ = 1 case of the ℓ-column theorem *is* the e_k⋆e_r Pieri rule. So the
paper has **one** proof (residue lemma + closing identity (Z)) where the notes had two (207b's one-index identity (★)
and Day 212's ℓ-column proof).

## How it was checked ("the PDF is the claim")
For every section, the printed statements were re-implemented from the PDF text and checked against an independent
exact-rational implementation of the subset formula. These are all-True logs in `rick-research/scripts/day231/`
(`check_*_printed.log`), and INVENTORY §5 lists what each covers. Highlights:
- the ℓ-column theorem as an identity at exact random points (ℓ ≤ 3, 85 cases; a negative control fails as it should);
- val = ℓ−κ on all non-diagonal up-set pairs with n ≤ 5, at t = 3/5 and t = 0;
- the history formula on 96 coarsening pairs, including the t = −2 zeros;
- Box Complement including N below the degree;
- the two-point formula against power-sum pairings computed from scratch;
- the two-row Green table against an independently built HL P-basis.

## Deliberately NOT in the paper
- (N) / ∇-transport and the square edges t→∞, s→∞, the reflection, and Prop C. (N) still relies on two Cherednik facts with
  no located reference. A one-paragraph remark says this and uses none of it.
- DS-from-(N), Lemma ER, t = 1/s: these rest on (N) or have incomplete checks.
- Conjectures. The open problems section is the FPSAC one.

## Your decisions (unchanged from FPSAC)
Authorship and presenter, affiliation, acknowledgements, the AI declaration, and your role. The long version currently
has one visible `[WIP: …]` marker for these, in the title footnote. Nothing is urgent: FPSAC (11-15) comes first.
