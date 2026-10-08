# Day 229 PROVE (2026-10-08): FPSAC round 3 + two-row Green via Young's rule

Writing session (stop-auditing rule; no novelty hunts, no browsing). Draft:
`work-in-progress/fpsac2027/fpsac2027-draft.tex`.

## Writing items (1–4) — DONE

- **Page check.** Body + references = 12 pp; AI disclosure on pp. 13–14 (\clearpage, uncounted).
  ~0.3 pp spare on p. 12. FPSAC page rule assumed to count references (conservative).
- **Line 140 notation.** The block-law proof idea now reads
  ω e⋆_λ|_{t=0} = H̃_λ(x;s) = s^{n(λ)} Q′_λ(x;s^{-1}), Q′_λ(x;u) = ∏(1−R_ij)/(1−uR_ij) h_λ,
  and R_ij^k has coefficient (u−1)u^{k−1} = −(s−1)s^{−k} at u = 1/s. The old "q" was Hikita's q = 1/s,
  so the old text was not wrong, just ambiguous next to the HL parameter t. Sanity check by hand: λ=(1,1):
  s(h_1^2 + (1/s−1)h_2) →ω s e_1^2 + (1−s)e_2 = e_1⋆e_1 at t=0 (Hikita Pieri, [2]_0=1). ✓
- **Title** kept, TODO marker dropped. **Abstract** rewritten, 123 words, no custom macros/cites:
  block law; exp-of-connected; connected-graph cumulant; Möbius (t=0) → Cayley (t=1); J separates from
  Dołęga's column cumulants for t≠0; box symmetry; all v=2 leads closed via residue formula for
  two-part Green polynomials.
- **Dołęga positioning.** J(t) = (t²+1)(t³+3t²+6t+6)/((t+1)(t²+t+2)²) re-derived from Thm G this session
  (sympy, `/tmp/j.py` inline: J(0)=3/2, J(1)=1). Gauge invariance: exponents of a, g(4), f(1), f(2) cancel
  (4+2−2·3=0; 1+1−2=0; f(1): 4−2·2=0; f(2): 2−2·1=0). Dołęga ⊕ ≡ 3/2 stated "by computation" (Day 228
  sep.py). Open problem 5 reworded: is there a Macdonald-cumulant construction whose leads are the
  ⋆-leads for all t?
- **AI disclosure (our part).** Model, tools, what the agent did; sub-agents; Clio's reviewed inputs listed
  exactly from registry (subset-formula inputs, Rem H / d-matrix location, W non-independence, DS support
  n≤7, Green dictionary numerics) and the NOT-reviewed list (block law, G, F, block-mult, Box, CT, 2pt,
  v2). Cold-recheck claim restricted to W and §5 (registry: thmW Day 223; v2 Day 226/227). Robin's \todo kept:
  wording, model list, human role, SoftConf field (comment).
- **\todo burn-down.** 16 → 7 in tex, all Robin's (title-thanks, affiliation, acks, disclosure ×3 + model list).
  Removed: l.95 scope note, l.147 UNAUDITED remark (rewritten from registry: t=0 classical in substance via
  DLT94 eq. (11); new = lower bound all t, exactness over Q(t), merge weights; CLR/KN gates belong to Thm H,
  which is a no-claim remark), l.222 "one search" (now: Mayer shape = moment–cumulant inversion of Thm G),
  l.257 Pieri package → "long version". Also removed leaked internal notes ("cold recheck Day 223 §4",
  "Present as ...", "wake 225 audit").
- **Clio Thm D** cited (bib `Clio26`, Robin to confirm citing an agent manuscript) in the two-row example:
  diagonal class X = t^{λ2} − t^{λ2−1} + m; for λ1>λ2, λ2≥3 odd it is −1 at t=−1, 1 at t=0 ⇒ root in
  (−1,0) ⇒ no cyclotomic product formula. Checked by hand.
- Overfull boxes fixed (Lemma linT, §4 title, Box proof, Thm 2pt multline, Thm v2, two-row cases display).
  Remaining: 7.5pt (l.81) and the Penrose bib TODO line.
- **Bib TODOs still open (need a browse/wake with fetch):** DLT94 Art. B32c, DFK19 title, Dołęga title,
  HT 2609.29957 title, Penrose 1967, plus one more "verify title and pages" entry.

## Item 5 (math): two-row Green = Young's rule (crown-1 hunch resolved at the trace level)

**Claim.** For λ=(n−k,k), ρ=(x,y) with x≥y≥1, x+y=n, and π_j = number of j-subsets of [n] fixed by
a permutation of cycle type ρ:

  X^λ_ρ(t) = Σ_{j=0}^{k} t^{k−j}(π_j − π_{j−1}) = π_k + (t−1) Σ_{j<k} t^{k−1−j} π_j.

**Proof.** (i) Macdonald III (7.6′): X^λ_ρ(t) = Σ_μ χ^μ_ρ K_{μλ}(t) (read first-hand in the local scan,
`/home/agent/data-cache/macdonald.txt` l.~12380). (ii) K_{μλ}≠0 needs μ ⊵ λ, so μ = (n−j,j), j≤k. There
is exactly one SSYT of shape (n−j,j) and content (n−k,k) (second row is all 2's), so K(1)=1; K is monic of
degree n(λ)−n(μ) = k−j (III (6.5)); hence K = t^{k−j}. (iii) Young's rule: the permutation module on
j-subsets M^{(n−j,j)} = ⊕_{i≤j} S^{(n−i,i)}, so χ^{(n−j,j)} = π_j − π_{j−1} (π_{−1}=0). (iv) Abel summation.
∎

**Evaluation.** A fixed j-subset is a union of cycles. For 0<j≤k≤n/2: π_j = m·[j=y], where m = 2 if x=y and
1 otherwise (if j=x then x=y=k=n/2, covered by m); π_0=1. Hence
- y<k: X = (t−1)(t^{k−1} + t^{k−1−y}) = (t−1)t^{k−1−y}(1+t^y);
- y=k: X = m + (t−1)t^{k−1};
- y>k: X = (t−1)t^{k−1}.
This is exactly the Day 228 Example (proved there by substitution into Thm 2.5, 155/155 numerics), so the two
proofs agree. Spot check λ=ρ=(2,2): π=(1,0,2) → X = 2 + (t−1)t = t²−t+2 ✓.

**Consequences.**
- The λ1-independence (crown 1) is explained: X depends on λ only through k and on ρ only through fixed
  subsets. No cup diagrams or Springer fibres are needed at the trace level. The graded virtual module is
  (1−q)⊕_{j<k} q^j M_j ⊕ q^k M_k after t ↦ 1/t·t^k normalisation (Q̃ = t^{n(λ)}X(1/t) gives
  (1−q)Σ_{j<k} q^j π_j + q^k π_k, nonnegative "Springer" side). The cup-diagram question survives only as
  "is there a cup-diagram basis realising this telescoped permutation-module filtration", which is a
  Russell–Tymoczko question. POST-FPSAC; probably known.
- For FPSAC: added one sentence to the Example (direct derivation from III (7.6′)). The Example is
  therefore classical; the paper already says it is in Morris's range.

**Grade:** proved (this file). Registry: note added to `two-row-specialisation-thm25` (second, elementary proof).

## Verification
- `latexmk` clean. 14 pp total = 12 (body+refs) + 2 (disclosure). Pages 6 and 10 visually inspected.
- J(t): sympy from the Thm G formula, matches the draft's closed form exactly.
- Two-row Young formula: hand check vs the Day 228 formula in all three cases + (2,2).

## Gaps
- None in the mathematics added today. Open writing items for Robin only, plus bib verification (needs fetch).
