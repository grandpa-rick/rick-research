# Day 105 — MacBeth H² proof: deep read + relevance assessment for Claim B

**Date:** 2026-08-13
**Author:** Rick's research agent
**Source:** email uid 69 from scot.macbeth20@gmail.com, 2026-08-13
**Attachment:** `/home/agent/mail/attachments/69/2026-08-12-holonomy-composition-zs-bridge.md` (16.4 KB)
**Companion (peer-cited):** `2026-08-11-update-monad-liftings-holonomy-full.md` (proved);
`2026-07-20-orchestration-reentrancy-obstruction-analytic.tex` (`[ω]=ε`, Lean-verified).

---

## 1. What MacBeth proved (précis)

Setup: two update monads `Upd_{(S,P,↓)}`, `Upd_{(S,P',↓')}` sharing state `S`. A distributive
law between them is (Ahman–Uustalu 2013) a **matched pair** of monoids; the composite carrier is
`Q = P⋈P'`, the **Zappa–Szép** (ZS) product. `Q` acts on `S` by
`s ↓_⋈ (p,p') := (s↓p)↓'p'`.

**Theorem (a) — PROVED.** Composite `Upd_P ∘ Upd_{P'} = Upd_{(S,Q,↓_⋈)}`, and its degree-1
proof-relevant polynomial monad liftings are classified by
`Fun(𝔸(↓)⋈𝔸(↓'), Cat)` — i.e. the classifier of the composite is the ZS product of the two
factor action categories. (Rests on the proved 08-11 general update-monad classification.)

**Theorem (b') — REFUTATION of (b).** The naive isotropy law
`Stab_{P⋈P'}(s) ≅ Stab_P(s)⋈Stab_{P'}(s)` is FALSE. Containment ⊆ always holds; properness
occurs in 268 of 448 exhaustive point-checks across `S₃, S₄, A₄, D₄, ℤ/2×ℤ/2`. Explicit
witness: `G=S₃`, `P=A₃`, `P'=⟨(12)⟩`, `s=1` — both factor stabilisers trivial, composite
`Stab_G(1)=⟨(23)⟩≅C₂`. The nontrivial `(23)` factors as `((123),(12))` where neither leg fixes
`1`. **Emergent holonomy:** the round-trip out-by-p then back-by-p' is a fibre automorphism
though neither leg is a stabiliser.

**Theorem (c') — PROVED, scoped.** In the *aligned abelian normal* regime — i.e. `s` such
that containment is equality, `A := Stab_P(s)` abelian and normal in `E := Stab_Q(s)`,
`B := Stab_{P'}(s)` — the extension `1 → A → E → B → 1` has a class
`[ω] ∈ H²(B; A)`. For trivial action (the `ℤ/2` witness), `[ω]=0 ⟺ E≅A×B ⟺` every
composite holonomy is **unentangled** (`ρ(A)` and `ρ(B)` commute in `Aut(C_s)`);
`[ω]≠0 ⟺ E` non-direct (e.g. `ℤ/4`) `⟺` the regular representation is entangled.
The witness table:

| `[ω]` | `E` | composite holonomy    |
| ----- | ------ | --------------------- |
| `0`   | `ℤ/2×ℤ/2` | unentangled `ρ_A⊠ρ_B` |
| `ε`   | `ℤ/4`    | entangled order-4 aut |

MacBeth is explicit and honest: `[ω]` is an **H² class certifying whether an H¹ datum
(the two factor representations) assembles as a commuting product** — never an equality
of the two. He also explicitly *refuses* to identify this stabiliser-level `[ω]` with the
handoff-category `[ω(K_ε)]=ε` from his prior reentrancy result (cites his own past
"fusion-category conflation" as the cautionary error).

**Guardrail behaviour.** Both PROVE guardrails fired productively: the degree-mismatch
guardrail forced the H¹/H² clarification; the compute-first guardrail *refuted* (b) before
proof. Refutation-as-discovery. This is the kind of proof I trust.

---

## 2. Relevance to Rick's Claim B

Restating Claim B: `Q_{2R}(R−2, R, c)` is a rational polynomial in `c`; let
`C_R := v_2(Q_{2R}(R−2, R, c))|_{c=R}`. Conjecture: for `c ≡ R (mod 16)`,
`v_2(Q_{2R}(R−2, R, c)) = C_R` (constant on the class). Proved individually for
`R ∈ {2,4,6,10}` by sympy. Uniform-in-R is OPEN.

### 2.1 2-adic / p-adic ingredient in MacBeth?

**Only via the `ℤ/2` accident.** MacBeth's witness happens to be `H²(ℤ/2; ℤ/2) ≅ 𝔽₂`,
so the obstruction lives in a 2-torsion group. But this is because the finite groups
he chose to sweep have 2-torsion. There is **no 2-adic valuation, no `v_2` filtration,
no lift-to-2-adic-integers step** anywhere in the proof. His `𝔽₂` is a group cohomology
`H²` for a finite group with `A=B=ℤ/2` — not a 2-adic phenomenon. Rick's Claim B is
about `v_2` of a *rational* polynomial value; that is a filtration-of-ℤ₂ statement.
The vocabulary "2" appears in both places for entirely unrelated reasons.

### 2.2 Class-uniformity pattern?

**Weak analogy only.** MacBeth's `[ω]` is either `0` or `ε` — a *binary* dichotomy of
extension classes. The *statement*  "`[ω]=0` iff every composite holonomy is unentangled"
is a class-uniform statement in the trivial sense that the class label determines the
qualitative outcome. But Claim B's structure is **completely different**: it asserts
that a *numerical valuation* is constant on a residue class of `c`, uniformly in a
*second* parameter `R` (the R-uniformity is the open part).

The residue-class uniformity in Claim B is over `c ∈ ℤ` (mod 16); MacBeth has no
comparable indexing set. His "uniformity" is over finite groups sharing a cohomology
class label, which is a *classification* statement, not a *parametric-valuation*
statement.

### 2.3 Does "H² certifies splitting" transfer?

The Ψ: H²_Sb → H²_Gp shape MacBeth cites (Rathee–Yadav 2601.12371) is the skew-brace
transport where a *special* second cohomology maps into ordinary group H² and its
vanishing splits a matched-pair extension. MacBeth's (c') is exactly that shape.

**But: what would this obstruct for Claim B?** For an H² obstruction argument to bite
on `v_2(Q_{2R}(R−2, R, c))`, one would need:

1. an extension `1 → A → E → B → 1` of groups intrinsic to the anchor family
   `Q_{2R}(R−2, R, c)`;
2. `A` a 2-primary abelian group whose class in `H²(B; A)` controls a 2-adic invariant
   (say, via a Bockstein or connecting-map argument giving `v_2` of some evaluation);
3. an R-parametric version, so that the *same* `[ω]` (or its vanishing) certifies
   uniformity across `R`.

None of these ingredients are present in Rick's current toolkit for Claim B. His epsilon
patterns (Day 103) are `min(g(R), 4)` saturation candidates; they are numerical fits, not
extension-class statements. The `mod 16` residue class is a 2-adic filtration level, not
a group-cohomological one.

**The Ψ transport MacBeth flags is real math in his domain** (matched pairs of monoids ↔
skew braces, both being ZS phenomena). But mapping "vanishing of a 2-cocycle class" onto
"constancy of a 2-adic valuation on a residue class" would require inventing the
intermediate structure — the extension, its module, the connecting map — from scratch.
That is not a transfer; that is speculating a whole new proof.

### 2.4 Concrete: is there anything to try?

I have to be honest: I do not see a productive transfer path. The one avenue I would flag
for Rick (not endorse):

- Does the family `Q_{2R}(R−2, R, c)` factor through some *group ring* or *Hecke algebra*
  that carries a `H²`-classified central extension? If yes, the vanishing of that H² class
  in a particular 2-primary component *could* be the obstruction that makes `v_2` constant
  on `c ≡ R (mod 16)`. Rick would need to identify the group/module structure first.
  Otherwise it is vocabulary matching.

The Day 105 Kummer-728 read (Sothanaphan's Erdős proof) landed **more actionable** for
Claim B than this: Kummer at least gives a per-digit local invariant. MacBeth's H² is one
level of abstraction too high to directly grip the arithmetic.

---

## 3. Verdict

**RELEVANCE TO CLAIM B: LOW.**

- Vocabulary resonance is real ("H² certifies splitting", ZS structure, cohomological
  obstruction). This is why MacBeth flagged it — his instinct to cross-pollinate is sound.
- **Mathematical bite is not present.** No 2-adic ingredient; no residue-class parametric
  statement; no `R`-uniformity mechanism. His `𝔽₂` is coincidental group-cohomological
  torsion, not the 2-adic filtration of Claim B.
- To upgrade to MEDIUM: Rick would need to *first* discover a group-cohomological
  structure on the `Q_{2R}` anchor family. That is a research task in its own right, not
  a transfer.

I recommend Rick acknowledge the H² arc as a genuinely nice piece of orchestration theory
(and the S₃ emergent-holonomy witness is elegant), thank MacBeth for the Ψ analogy, but
**not** redirect Claim B work to hunt for a cohomological reformulation. Claim B's
open R-uniformity is more likely to yield to a Kummer-carry-style local valuation
argument (Day 105 Sothanaphan read) or continued epsilon-family sweep, not H².

---

## 4. Independent registry assessment

**Is MacBeth's result Lean-verified?** No — MacBeth writes "I'm mid-arc formalising the S₃
emergent-holonomy witness in Lean". Current status: informal proof, exhaustive finite
sweep (`zs_holonomy.py`, 448 point-checks), rests on his own proved 08-11 classification
and Ahman–Uustalu 2013 (published). The S₃ witness is elementary and hand-verifiable in
minutes.

**Registry node recommendation.** Register at `peer-proved` (not `peer-lean-verified`).
Node name matching MacBeth's own convention: `holonomy-composition-zs-bridge`, with three
children as he suggests:

- `zs-composition-classifier` (part a) — `peer-proved`
- `isotropy-composition-fails` (part b as refutation) — `peer-proved` (elementary
  group-theoretic S₃ witness; independently checkable)
- `h2-unentangled-splitting-aligned-abelian` (part c') — `peer-proved`, scoped to aligned
  + abelian + normal `A`; witness `A=B=ℤ/2` compute-verified.

The S₃ witness is worth an independent 10-minute check on our side before promoting from
`peer-claimed` to `peer-proved`. The (c') proof is standard extension theory
(Eilenberg–Mac Lane); the load-bearing novelty is the *identification* of this H² class
with the isotropy-composition obstruction, which is MacBeth's contribution and rests on
(a)+(b'). I would register (c') as `peer-proved` conditional on (a) and (b').

**Cross-edge to Rick's registry:** MacBeth flags the Ψ: H²_Sb → H²_Gp shape as the same
skeleton as his (c'). If Rick's Ψ machinery lives in the registry, adding a
`cross-edge/macbeth-c-prime` note pointing both ways is warranted — as a *shape analogy*,
not a claim of shared theorem.

---

## 5. Files touched

- Attachment: `/home/agent/mail/attachments/69/2026-08-12-holonomy-composition-zs-bridge.md`
- Email envelope: `/home/agent/mail/inbox/20260813_230921_scot.macbeth20.json`
- Prior peer registry: `/home/agent/projects/peers/macbeth/registry/peer-claims.json`
- Companion Day 105 read (Kummer): `/home/agent/projects/reading/2026-08-13-day105-kummer-728-deep-read.md`
- Current Claim B state: `/home/agent/projects/proofs/2026-08-13-day103-epsilon-pattern.md`
