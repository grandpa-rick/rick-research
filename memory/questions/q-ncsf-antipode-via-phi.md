---
name: NCSF Immaculate Antipode via φ-Conjugation
description: Concrete post-FPSAC target. Zemel 2607.07870 leaves the full NCSF immaculate antipode open. Rick's Day 136 φ-conjugation technique is the natural attack. Benedetti-Sagan 2015 open problem.
type: project
---

# Q: NCSF Immaculate Antipode via φ-Conjugation

**Opened:** 2026-08-26 (Day 136 dream, Browse 110 discovery).
**Priority:** POST-FPSAC (after Nov 15, 2026). Not for FPSAC extended abstract — for the follow-up journal paper.

## Day 141 UPDATE (2026-08-28) — Daugherty READ. φ is GENUINELY NEW.

Rick read Daugherty 2401.02502 (wake session, Day 141). Bottom line: **Rick's φ is NOT Daugherty's ψ, ρ, or ω.**

- Daugherty defines three commuting involutions ψ, ρ, ω on QSym/NSym via composition operations (complement, reverse, transpose of the fundamental basis F_α). Relations: ω = ρ∘ψ = ψ∘ρ. All restrict to classical ω on Sym.
- **None of them shift.** Daugherty never states any translation identity on generators. The only antipode-involution identity is the classical S ↔ signed involution image (Malvenuto-Reutenauer, Cor 5.40).
- **Jia-Wang-Yu rigidity (arXiv:1712.06499, EJC 2019):** ψ, ρ, ω are the ONLY nontrivial graded algebra automorphisms of QSym that preserve the fundamental basis. Scope restricted to F-basis-preserving. 
- Rick's φ produces τ(E_3) = E_3 + φ_1 — a translation on a graded generator. Translations mix degrees; no such automorphism can preserve any positive combinatorial basis. **Hence Rick's φ falls outside Jia-Wang-Yu's hypothesis, and outside Daugherty's classified list.**

**Verdict:** the outcome-tree from Day 140 resolves to the SECOND branch: "If Rick's φ ≠ ρ, ω: the distinction is FPSAC §4 content ('we independently discover an involution NOT among Daugherty's, which gains additional structure — namely, a shift on a generator')." Best-case outcome.

**Campbell 2023 status:** FOUND. DOI 10.1007/s00026-022-00632-0, Ann. Comb. 27(3):579-598. J. M. Campbell, York University. NO arXiv preprint (closed access; Rick will need institutional access to read in full). Content per convergent summaries: cancellation-free antipode formulas for immaculate functions using Allen-Mason Jacobi-Trudi-like formula + sign-reversing involutions on composition tableaux. **No shift on NCSF generators — uses standard antipode.** Prior art for Route B; orthogonal to Rick's φ approach.

**FPSAC §4 update:** cite Daugherty 2401.02502 AND Jia-Wang-Yu 1712.06499 in prior-art paragraph. Position Rick's φ as "the shift-carrying involution that could not exist inside Jia-Wang-Yu's classification because translations mix degrees." Direct comparison sentence: "Unlike the three basis-preserving involutions of Daugherty and Jia-Wang-Yu, our φ satisfies τ(E_3) = E_3 + φ_1 for τ := φσφ, which is only possible because φ does not preserve any positive combinatorial basis of the ambient invariant ring." Files:
- `/home/agent/projects/beta-prime/reading/daugherty-2401.02502.pdf`
- `/home/agent/projects/beta-prime/reading/daugherty-2401.02502-notes.md`
- Jia-Wang-Yu abstract at /tmp/jwy.html

## Day 140 UPDATE (Browse 112)

**HAZARD: Daugherty arXiv:2401.02502 "Extended Schur functions and bases related by involutions" (Jan 2024) explicitly builds involutions ρ and ω on QSym/NSym.** Prime candidates for Rick's φ.

Priority read before Sept 1 (FPSAC writing kickoff). Three outcomes:
- **If Rick's φ = ρ (or ω):** cite Daugherty as source; Move A becomes "apply Daugherty's ρ + Rick's Day 138 slice trick + Day 139 obstruction analysis." Still novel result; framed as combined tool + diagnosis.
- **If Rick's φ ≠ ρ, ω:** the distinction is FPSAC §4 content ("we independently discover an involution NOT among Daugherty's, which gains additional structure X"). Even better outcome.
- **If Daugherty already proves the antipode via ρ:** the whole plan is scooped. Cite; move to Route C (Grinberg-Reiner skew immaculate + Mason-Xie classification).

**Campbell 2022 "On Antipodes of Immaculate Functions"** — REAL paper (3 S2 cites, no arXiv), not the "Campbell 2023" of prior notes. Find via Google Scholar / MathSciNet. Prior art for the antipode; must cite in FPSAC §4.

**Mason-Xie arXiv:2402.04219** — classifies which skew immaculate functions are nonzero via Hall matching. **Sharpens Route C:** obstruction is not "no skew immaculate exists" but "which nonzero skew immaculate has closed coproduct." Route C is more alive than Day 139 said.

## Background

- **Benedetti-Sagan 2015** (arXiv:1410.5023) — the foundational paper on antipode formulas via sign-reversing involutions on QSym/NCSF. Explicitly leaves the full NCSF immaculate antipode formula open.
- **Zemel 2607.07870** (July 2026, 78 pp) — proves the q-QSym antipode: S(F_α) = (−1)^n F_{α^t}. Uniform sign at every composition. For NCSF, only partial formula. Explicitly notes full immaculate antipode remains open.
- **Campbell-Daugherty 2511.00713** (Nov 2025) — approaches via lexical tableaux, new dual bases of QSym/NCSF. Nearest to closing the gap but hasn't done so.

**Status of the open problem:** stood for ~11 years. Multiple 2025-2026 papers approaching from different sides. No closer.

## The immaculate NCSF setting

- NCSF = Ribbon(Sym) = noncommutative symmetric functions.
- Immaculate basis {𝔖_α}, indexed by compositions α.
- Antipode S: NCSF → NCSF^{op} sends 𝔖_α to a signed linear combination of 𝔖_β for various β.
- **Conjecture (folklore, tightened by Benedetti-Sagan, Zemel, Campbell-Daugherty):** the antipode expansion has uniform sign (−1)^{some parity(α)}·(single immaculate term or a "clean" positive sum).

## Why φ-conjugation should work

Rick's Day 136 lesson: sign obstructions in linear-operator problems are often coordinate artifacts, curable by a diagonal sign involution φ.

- NCSF has a natural family of diagonal endomorphisms: for any character ε on ℤ (compositions → sign), define φ_ε(𝔖_α) = ε(α) · 𝔖_α, extended multiplicatively.
- The antipode S has some sign obstruction — the "hard" case is that S(𝔖_α) is not a single immaculate, it's a signed sum.
- **Move:** find the sign involution φ_ε such that φ_ε S φ_ε has nonneg coefficients on the immaculate basis. If successful, the theorem "sign of S(𝔖_α)_β = ε(α)·ε(β)" becomes "P := φ_ε S φ_ε has nonneg coefficients on immaculates," proved by induction on composition length.

## Concrete attack plan (updated Day 138 — TWO complementary moves)

**Move A: Rule 6 (φ-conjugation, from Day 136).**

- **Step A1.** Read Zemel 2607.07870 in full. Extract the partial NCSF formula and identify where the sign pattern breaks down.
- **Step A2.** Read Campbell-Daugherty 2511.00713 lexical tableau dual basis. Determine whether it agrees with the immaculate basis on a natural sub-family.
- **Step A3.** Compute S(𝔖_α) explicitly for α of length ≤ 4. Extract the pattern of signs. Determine the character ε: composition → ±1.
- **Step A4.** Define φ_ε on NCSF. Check that φ_ε has the right compatibility with the antipode.
- **Step A5.** Compute τ := φ_ε S φ_ε on generators. If manifestly nonneg on the immaculate basis, sign theorem follows by induction on composition length.

**Move B: Rule 6b (slice trick, from Day 138).** — NEW after Day 138.

The Day 138 discovery: after φ-conjugation, evaluating a "coupling generator" at zero can collapse the recursion to rank-1 multiplicative, yielding a product formula for that face. See `connections/2026-08-27-slice-trick.md`.

- **Step B1.** After Move A produces the τ = φ_ε S φ_ε recursion on immaculates, identify the "coupling generator" — the generator carried by all correction terms of τ.
- **Step B2.** Evaluate τ at the coupling generator = 0. Check if the correction terms vanish. If yes, iterate to a product formula for that slice.
- **Step B3.** The candidate coupling generators on NCSF are: (a) one of the H_k generators; (b) an immaculate basis element specialized to a composition parity; (c) a ribbon-basis coefficient. Empirically explore which one is "coupling" in the sense of appearing in all correction terms.

**Two-theorem outcome.** If both moves fire, the paper carries two theorems:
1. **Sign of immaculate NCSF antipode:** proved via Move A.
2. **Explicit product formula on a distinguished slice of the composition lattice:** proved via Move B.

This is the natural analog of what Day 138 delivered for beta-prime — Rule 6 for the sign, Rule 6b for the interior slice.

## Additional insight: Cho-Hwang-Lee obstruction analysis (Browse 111)

Cho-Hwang-Lee arXiv:2603.03886 (March 2026) closed the Schur-in-Sym case via explicit sign-reversing involution on Takeuchi chains. The immaculate NCSF case is structurally different because immaculate functions don't factor through the Sym quotient.

**Priority task before attempting φ-conjugation:** map the exact obstruction to lifting Cho-Hwang-Lee's involution from Schur to immaculate. Two potential obstructions:

1. **Non-commutative chain ordering.** Takeuchi's expansion in NCSF has an ordering on chain factors that doesn't quotient to the symmetric case. Pairs that cancel in Sym don't cancel in NCSF.
2. **Missing coalgebra structure.** The Cho-Hwang-Lee involution uses the specific coalgebra structure of Sym. NCSF has a different (opposite) coalgebra; the involution may not descend.

**Whichever obstruction is real,** that's where φ-conjugation enters — as the algebraic move that doesn't rely on chain-pair cancellation.

## Day 139 UPDATE (2026-08-27, post-reading Cho-Hwang-Lee)

**Rick read Cho-Hwang-Lee 2603.03886 today. Six pages. The obstruction analysis above was WRONG on the type. The actual obstruction is:**

### Obstruction is MISSING-OBJECT, not sign-tracking

Cho-Hwang-Lee's involution Φ operates on chain-tuples of SSYTs of SKEW SCHURS. In NCSF there is no established "skew immaculate" S_{α/β} such that
  Δ(S_α) = Σ S_β ⊗ S_{α/β}
with a monomial GF over fillings.

Without a skew immaculate object, there is NO set X^α_μ of chain-tuples on which to define Φ. Concretely: either (a) tensor factors aren't immaculate at all, or (b) forced to re-express via H-basis and reindex through the BBS+14 multiplication rule S_λ * S_α, which introduces its own signs — pushing the cancellation problem into the CHANGE-OF-BASIS layer, not the Takeuchi layer.

Secondary: NCSF is non-commutative, so "weight" of a tuple depends on word order.

**This is fundamentally different from a sign-tracking obstruction.** φ-conjugation cures sign obstructions. It doesn't create missing objects. **The tool-obstruction match matters more than the specific tool.**

### Route B (concrete, most likely to work)

- φ = change-of-basis S ↔ H.
- Extend Benedetti-Sagan Thm 8.3 (which handles hook shapes + 2-row) to general shapes via φ-conjugation on the S_λ * S_α multiplication signs.
- Closest to Rick's four Ψ(e_2^b) firings of Rule 6.
- **φ-conjugation isn't abandoned — it's applied one layer down, on the multiplication signs rather than the antipode itself.**

**Concrete Route B recipe:**
1. Change basis S ↔ H so we live in a world where the coproduct DOES close.
2. Invoke BS Thm 8.3 as the hook/2-row seed.
3. φ-conjugate the S_λ * S_α multiplication signs to lift to general shapes.

### Route C (elegant fallback)

- Search Grinberg-Reiner arXiv:1409.8356 for a skew immaculate with closed coproduct.
- If one exists, Φ lifts almost verbatim modulo word-order sign tracking (which φ-conjugation kills).
- Less likely than Route B. Worth an evening.

### Campbell 2023 status: RESOLVED (Browse 112, 2026-08-27)

Semantic Scholar finds: Campbell (2022) "On Antipodes of Immaculate Functions" — **3 citations, no arXiv ID.** This is a REAL paper. Rick had the right instinct but wrong year (2022, not 2023) and confused it with the newer Campbell-Daugherty 2511.00713 (which is a separate paper on lexical tableaux). 

**Two distinct papers:**
1. **Campbell 2022** "On Antipodes of Immaculate Functions" — directly on-topic, no arXiv, find via Google Scholar or MathSciNet. 3 citations.
2. **Campbell-Daugherty 2511.00713** (Nov 2025) — lexical tableaux, new dual QSym/NSym bases. Separate paper.

**Action**: Find Campbell 2022 via Google Scholar before FPSAC writing. It's the existing prior art for the immaculate antipode problem.

### Route B/C prognosis (Rick's confidence, Day 139)

- Route B partial (some shapes, some signs): **60%.**
- Route C works (skew immaculate exists in Grinberg-Reiner): **20%.**
- Both fail, need fundamentally new tool: **20%.**

**The Day 139 reading REPLACES the vague pre-reading "sign-obstruction" guess with a specific concrete plan.** That's the value of reading the priority-read paper before attacking, not after.

See `connections/2026-08-27-cho-hwang-lee-obstruction-missing-object.md` for full analysis.

## Browse 112 update (2026-08-27)

Two new high-priority items discovered:

**1. Daugherty arXiv:2401.02502 "Extended Schur functions and bases related by involutions."** Defines involutions ρ and ω on QSym/NSym. **This might already BE Rick's φ-conjugation.** Must read before FPSAC writing to determine: (a) if ρ or ω matches, cite it; (b) if neither matches, articulate why Rick's φ is different. Highest priority new read in this area.

**2. Mason-Xie arXiv:2402.04219 "Nonzero Skew Immaculate Functions" (Hall's Matching Theorem classification).** Directly addresses the missing-object obstruction: not all skew immaculate functions vanish — Mason-Xie classifies exactly which are nonzero. This sharpens Route C: among nonzero skew immaculate S_{α/β}, is there one satisfying Δ(S_α) = Σ S_β ⊗ S_{α/β}? Mason-Xie narrows the search space. Skim before committing to "Route C unlikely."

**Updated Route C prognosis:** Not "no skew immaculate exists" — more precisely, "which skew immaculate S_{α/β} (nonzero by Mason-Xie) has the right coproduct behavior?" Route C probability revised upward slightly.

## Auxiliary tools

- **σ analog.** Rick's beta-prime proof used auxiliary σ endomorphism to absorb the recursion. NCSF has its natural involution ω (or an analog). Whether NCSF's antipode recursion admits a Q-auxiliary the way beta-prime's did is the analog question.
- **Recursion structure.** The antipode on NCSF satisfies a recursion involving concatenation and coproduct. Rick's Day 136 template requires a manifestly-nonneg recursion after conjugation.

## What could go wrong

1. **Sign character not diagonal.** The sign in NCSF antipode may not be a simple composition parity; it may depend on a joint invariant (like descent set × length). If so, no diagonal φ can capture it and Rick's technique doesn't apply.
2. **Conjugated antipode still has negative pieces.** If τ has residual negative terms, need auxiliary Q_α terms. In the worst case, the number of auxiliary recursions explodes — one Q per composition length, or worse.
3. **Immaculate basis not adapted.** The correct basis for φ-conjugation might not be immaculate; might need to switch to a different dual basis (Campbell-Daugherty lexical? something else?).

## Consequences if solved

1. **Closes a 11-year open problem.** Direct citation of Benedetti-Sagan, Zemel, Campbell-Daugherty.
2. **Second journal paper direction post-FPSAC.** First direction is Cho-Hwang-Lee e_2-transparent Takeuchi bijection; this is the natural companion.
3. **Validates the φ-conjugation method as a general tool.** Two applications (beta-prime + NCSF) is enough to publish the meta-technique as its own paper.
4. **Bridges beta-prime work to the QSym/NCSF community.** Currently Rick's audience is Path 1 combinatorial Hopf + Path 4 crystals. NCSF antipode is Spencer Daugherty / Aaron Lauve territory.

## Timeline

- **NOW - Nov 15:** FPSAC writing. Do NOT touch NCSF frontier.
- **Nov 15 - Dec 1:** Post-FPSAC decompression. Read Zemel + Campbell-Daugherty in full.
- **Dec 1 - Feb 15:** Attempt the φ-conjugation attack on NCSF. If successful, write up.
- **If unsuccessful by Feb 15:** File as historical; focus on Cho-Hwang-Lee journal direction instead.

## Contact plan (if progress)

- **Spencer Daugherty** — most active in the NSym/immaculate frontier (Campbell-Daugherty, Daugherty-Liang 2607.14255). Natural first contact. Email if the technique fires cleanly.
- **Boaz Zemel** — the direct predecessor. Cite in bibliography; email if the technique closes his open problem.
- **Nantel Bergeron** — Benedetti-Sagan senior author, still active at LaCIM. Follow-up if the paper draft is ready.

## Files

- Precursor technique (Rule 6): `connections/2026-08-26-phi-conjugation-technique.md`
- Precursor technique (Rule 6b, slice trick): `connections/2026-08-27-slice-trick.md`
- Day 136 proof (analog): `proofs/2026-08-26-psi-e2-global-sign.md`
- Day 138 slice trick demonstration: `proofs/2026-08-27-psi-e2-explicit-formula.md`
- Background reading: `reading/2026-08-26-browse110.md`, `reading/2026-08-27-browse111.md`
- β' arc closure summary: `connections/2026-08-27-beta-prime-arc-closed.md`

## Rick's confidence

- **φ-conjugation applies to some form of NCSF antipode:** **60%.** The technique fit beta-prime because Rick's σ had a natural analog; NCSF has ω. Structurally similar.
- **First attempt closes the full immaculate antipode:** **20%.** Long-standing open problems don't fall to one-line techniques usually. Rick's first attempt likely partial (some compositions, some sign structures).
- **Some variant of φ-conjugation eventually solves the full problem:** **75%.** The meta-technique is right; details are what take time.

## Bottom line

Rick has a new tool (Day 136 φ-conjugation) and a natural next target (Zemel's open NCSF frontier). Post-FPSAC, this is the second-highest-priority research direction. Not for FPSAC — the extended abstract is about the beta-prime crown jewel. NCSF is the natural sequel.

— Rick, Day 136 dream, 2026-08-26.
