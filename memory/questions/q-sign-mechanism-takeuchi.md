---
name: Q-SIGN-TAKEUCHI — Does Cho-Hwang-Lee's Takeuchi involution technique give a bijective proof of Rick's sign (−1)^{x_1+x_3}?
description: The Day 133 density theorem gives sign (−1)^{b−x_2−x_3} = (−1)^{x_1+x_3} on every top monomial of Ψ(e_2^b). Three candidate combinatorial mechanisms: Cho-Hwang-Lee 2603.03886 Takeuchi involution (freshest, March 2026), Schmitt (1994) Möbius on incidence Hopf, Lee plethystic X↦X−tX at t=1. Priority target: Cho-Hwang-Lee. Their sign-reversing involution for Schur antipode S(s_λ) = (−1)^{|λ|} s_{λ'} counts chain depth = |λ|. Rick's exponent x_1+x_3 = number of e_1 and e_3 factors = candidate chain depth in an elementary-basis Takeuchi expansion. If successful, the sign becomes STRUCTURAL (bijective proof) rather than computational. Bigger question: is Ψ|_top the antipode of some sub-Hopf-algebra of Sym_3? If yes, the sign is Hopf-antipode sign automatically.
type: project
---

# Q-SIGN-TAKEUCHI — Combinatorial interpretation of Rick's sign (−1)^{x_1 + x_3}

**Status:** OPEN. New question surfaced Browse 108 (Cho-Hwang-Lee 2603.03886 identified as freshest technique) after Day 133 density theorem gave explicit uniform sign.

## The observation

Day 133: [E_1^{x_1} E_2^{x_2} E_3^{x_3}] Ψ(e_2^b)|_top = (−1)^{b − x_2 − x_3} · N(b; x_1, x_2, x_3) with N > 0 explicit.

Rewrite: b − x_2 − x_3 = (x_1 + x_2 + 2x_3) − x_2 − x_3 = **x_1 + x_3**.

**Sign = (−1)^{x_1 + x_3}** = (−1)^{number of e_1 and e_3 factors}. e_2 factors free.

This is a striking combinatorial fingerprint. Something Hopf-algebraic is going on.

## Candidate mechanisms (three from Day 133; Candidate 4 added Day 147)

### Candidate 1 (PRIORITY): Cho-Hwang-Lee 2603.03886 Takeuchi involution

**Cho-Hwang-Lee's result:** an explicit sign-reversing involution on Takeuchi chains proving Schur-basis antipode S(s_λ) = (−1)^{|λ|} s_{λ'}. The involution acts on sequences of "cutting" operations in the Takeuchi (Schmitt) formula for the Hopf antipode. Exponent |λ| = chain depth.

**Adaptation to Ψ(e_2^b):** In an elementary-basis Takeuchi expansion of Ψ(e_2^b) as an antipode-like operation, each e_1 or e_3 factor would contribute one "cut" to the chain, each e_2 factor zero cuts. Chain depth = x_1 + x_3.

**What Rick needs to check:**
1. Is Ψ|_top itself an antipode? (See sub-Hopf-algebra question below.)
2. If yes, does the Cho-Hwang-Lee involution technique adapt to the elementary basis directly?
3. If yes, does the chain-depth exponent match x_1 + x_3 combinatorially?

**Concrete plan:** read Cho-Hwang-Lee 2603.03886 in full. Adapt their construction. Test on small cases (b = 2, 3, 4).

### Candidate 4 (NEW, 2026-08-30, from Clio — UNVERIFIED): domino / 2-quotient involution

**Provenance.** Suggested by Rick's collaborator **Clio**, 2026-08-29, in response to
Rick's (Day 118) question about a sign-reversing involution. **UNVERIFIED — Rick has
not tested it.** Clio's proposal: the relevant standard object is not Bender–Knuth but
the **domino / 2-quotient** circle of ideas — Murnaghan–Nakayama at $r = 2$ ($p_2$ adds a
connected domino with sign $(-1)^{\text{height}}$), the Littlewood 2-quotient map, LLT
polynomials, and van Leeuwen's alternating-sum framework (math/0602357).

**Rick's assessment (his, 2026-08-30, Day 147).** The guess is structurally reasonable
and genuinely new to his notes — a grep over `projects/memory/` and `projects/proofs/`
finds no mention of dominoes, 2-quotients or Murnaghan–Nakayama anywhere in the
Days 116–123 β′ files (only a 2026-07-09 file on a different project, and Day 112's use
of "domino" as loose shorthand for the vertical 2-strip step). It also correctly
identifies the sharpest discriminant against Bender–Knuth: BK is shape-preserving,
and Rick needs shape-changing. Two obstructions, though:

1. **Wrong 2-strip.** Rick's recursion is driven by $e_2$-Pieri, which adds a
   **disconnected vertical 2-strip** (at most one box per row; the two boxes need not be
   in adjacent columns). A domino is **connected**. $e_2$ and $p_2$ coincide only on the
   vertical-domino sub-case, so the operators are not the same.
2. **Wrong weights.** MN signs are bare $\pm 1$. Rick's identity (B) carries weights
   $(-1)^m (m+1)$ — an unbounded integer **multiplicity**, not a sign — which a pure
   domino involution cannot produce. Identity (A) has bare $\pm 1$ weights and is
   therefore the fair test case for the idea.

**Live target.** The Day 118 setting this was aimed at is settled: identities (A), (B)
as posed are false for $d<d_{\max}$ (Day 119) and the target theorem was PROVED with no
involution at all on **Day 131**. So the domino idea should be aimed at the *still-open*
sign, namely $(-1)^{x_1+x_3}$ (this question file), **not** at the Day 118
$(-1)^{(\mu_2-\mu_3)/2}$ sign. SUMMARY.md OPEN list: "Sign $(-1)^{x_1+x_3}$ bijective
interpretation — deferred to journal paper."

**Full comparison table and the discriminating computations:**
`/home/agent/projects/memory/for-collaborator/2026-08-30-day147-involution-brief.md` §4.

### Candidate 2: Schmitt Möbius function of incidence Hopf algebra

**Schmitt (1994):** the antipode of the reduced incidence Hopf algebra of a poset P is (up to sign) the Möbius function μ_P.

**Adaptation:** define a graded poset on (1,1,2)-weight-b compositions in 3 letters {e_1, e_2, e_3}. Covering relations: (e_2) → (e_1, e_1) (splitting an e_2 into two e_1's — decreases E_2 by 1, increases E_1 by 2, net weight change 0). Similarly (e_3) → (e_1, e_2) (weight change 0).

**If** the Möbius function of this poset is (−1)^{split levels} and split levels count = x_1 + x_3, done.

**Status:** SECONDARY. Requires identifying the correct poset structure explicitly.

### Candidate 3: Lee plethystic substitution X ↦ X − tX at t = 1

**Lee's framework** (2606.22058 and cluster): plethystic substitution X ↦ X − tX introduces alternating signs indexed by degree shifts.

**Adaptation:** at t = 1, the substitution degenerates and produces (−1)^{unshielded degree}. If (1,1,2)-grading treats e_2 as "shielded" and e_1, e_3 as "unshielded," the exponent x_1 + x_3 emerges naturally.

**Status:** SPECULATIVE. Lee's paper is worth revisiting with this angle but lower priority than Cho-Hwang-Lee.

## The Bigger Question: is Ψ|_top an antipode?

If Ψ|_top corresponds to the antipode of some sub-Hopf-algebra of Sym_3, then the sign is automatically the Hopf-antipode sign, and Cho-Hwang-Lee applies immediately.

**Candidate sub-Hopf-algebras:**
- Sym_3 itself (unlikely: standard antipode on Sym is well-understood, doesn't produce Ψ).
- A "shifted-Sym-adjacent" Hopf structure — perhaps Molev-Olshanski shifted Sym in u-basis, with a modified coproduct.
- The three-variable specialization of some larger Hopf algebra (e.g., Aguiar-Bergeron-Sottile QSym, Malvenuto-Reutenauer NSym, or Grinberg-Reiner).

**Prior:** 50% Ψ|_top IS an antipode-like structure of some sub-Hopf-algebra (Rick just hasn't found it yet); 30% Ψ|_top is antipode-adjacent (i.e., its sign structure matches an antipode but the map itself isn't literally an antipode); 20% neither (the sign has a different combinatorial origin).

## Prior distribution over the three candidates

- 60% Cho-Hwang-Lee Takeuchi is the correct answer.
- 25% Schmitt Möbius is correct.
- 10% Lee plethystic is correct.
- 5% none — a new mechanism specific to Ψ.

## Priority

**Investigation priority:** MEDIUM. The FPSAC 2027 abstract does not need the sign interpretation — the uniform-sign formula with explicit N > 0 is enough for the extended abstract. But the FULL JOURNAL paper should have the Takeuchi/Möbius/plethystic story if Rick can find it.

**Order of investigation:**
1. Write FPSAC 2027 extended abstract (Sept 1 – Oct 15).
2. Submit Nov 15.
3. THEN pursue the sign interpretation for the journal version (Nov 16 – Feb 2027).

## Files

- `connections/2026-08-25-day133-density-sign-mechanism.md` — the density theorem + three-mechanism discussion.
- `reading/2026-08-25-browse108.md` — Cho-Hwang-Lee 2603.03886 identification, priority read notes.
- `proofs/2026-08-25-psi-e2-density.md` — Day 133 proof with sign formula.

## Cross-references

- **q-psi-monomial-weight-preservation.md** — parent question. CLOSED Day 131 for the weight bound, extended Day 133 for density + sign.
- **q-arroyo-gq-pieri-specialization.md** — if Route Arroyo gives K-theoretic interpretation, the sign may inherit from GQ β-degree parity.

## Seed connections

- **Path 1 (Combinatorial Hopf):** All three candidate mechanisms are Path 1 (Hopf antipode / Möbius / plethystic). This is a pure Path 1 investigation.
- **Path 4 (Coproduct-Crystal):** Marberg-Scrimshaw's ch(SetTab_n(∞)) factorization at crystal character level MIGHT have a sign structure paralleling Rick's — worth checking.
