# Day 93 — /assumptions Pass on M_j Sym Form

**Date:** 2026-07-13
**Registry:** `proofs/registry/beta-prime-mod8.json` — node `Mj-c-uniform-conjecture`
**Trust:** proposed → `checked-sober` clean audit + new sub-node `Mj-sym-form-audit-clean`
**Files:**
- Phase A verdict: `reading/2026-07-13-gmsw-2607.06749-read.md`
- Sym-side proof (Day 86): `proofs/2026-07-08-Mj-c-uniform-structural.md`
- Draft new-object abstract: `memory/for-collaborator/2026-07-13-Mj-new-object-abstract.md`

---

## 0. TL;DR

Phase A closed NEG (GMSW 2607.06749 categorifies plethystic compositions, not
Sym-function products — same failure mode as Routes I-IV). Pivot to Phase B:
/assumptions pass on the M_j Sym form.

**Seven assumptions checked. Result: CLEAN AUDIT.** No broken assumption
discovered. Three genuine loose ends flagged for future work. One new insight
promoted to a separate node.

Since no assumption is broken, the "conjecture" `Mj-c-uniform-conjecture` is
already at its correct grade `checked-sober` and cannot be immediately upgraded
by internal work. The remaining path to `proved` runs through **either**
(a) Clio empirical data at c > 5, j ≥ 1, or (b) a rep-theoretic derivation of
Clio's Lemma-1 template constants from first principles — **and neither is a
Sym-side hole**.

The correct next-cycle move is: **commit to "M_j as new object" writeup** (draft
in `for-collaborator/2026-07-13-Mj-new-object-abstract.md`).

---

## 1. The seven assumptions (from PROVE.md, Day 92 enumeration)

For each: statement, examination, verdict (verify / test / flag / broken).

### A1. Sym-side identity: inner operand is really `e_2^j · p_1^{n-2j}`

**Statement.** M_j(λ) equals ⟨s_λ, e_2^j · p_1^{n-2j}⟩ — not ⟨s_λ, e_2^j · s_{(n-2j)}⟩,
not ⟨s_λ, e_2^j · h_{(n-2j)}⟩, etc.

**Examination.**

The Frobenius characteristic of the induced module

    Ind_{S_2^j × S_1^{n-2j}}^{S_n} (sgn^{⊗j} ⊗ triv^{⊗(n-2j)})

is `e_2^j · h_1^{n-2j} = e_2^j · p_1^{n-2j}` (Young-subgroup composition (2^j, 1^{n-2j})).

Its multiplicity of V_λ is ⟨s_λ, e_2^j p_1^{n-2j}⟩.

**Spot-check against alt operand `e_2^j · h_{n-2j}`** (Young subgroup S_2^j × S_{n-2j}
— composition (2^j, n-2j)):

Test at (a, b, c, j) = (5, 5, 5, 1):
- Rick's operand: M_1(5,5,5) computed via P_1(5,5,5)=90, f^{(5,5,5)}=6006, n=15:
  M_1 = f^λ · P_1 / n(n-1) = 6006·90/210 = **2574**.
- Alt operand: ⟨s_{(5,5,5)}, s_{(1,1)} · s_{(13)}⟩ = ⟨s_{(5,5,5)}, s_{(14,1)} + s_{(13,1,1)}⟩ = **0**.

Alt operand gives 0; Rick's operand gives 2574. Since Clio's data at c=5 (Day 85,
482/482) matches Rick's operand, the operand identification is **correct**.

**Cosmetic flag** (unrelated to correctness of the Sym form):
Day 86 §9 note reads "Ind_{S_2^j × S_{n-2j}}^{S_n} (sgn ⊗ triv)" — this Young
subgroup produces `e_2^j · h_{n-2j}`, not `e_2^j · p_1^{n-2j}`. The correct
Young subgroup is S_2^j × S_1^{n-2j} — i.e., composition (2^j, 1^{n-2j}) — with
representation sgn^{⊗j} ⊗ triv^{⊗(n-2j)}. The Sym form Rick actually uses in
every calculation is right; only the parenthetical rep-theoretic gloss is
mis-stated.

**A1 verdict: VERIFY.** Correct as used. Fix the §9 note in a future edit.

### A2. Base identification M_0(λ) = f^λ

**Statement.** At j=0, ⟨s_λ, e_2^0 · p_1^n⟩ = ⟨s_λ, p_1^n⟩ = f^λ.

**Examination.** Standard: p_1^n = Σ_{λ⊢n} f^λ · s_λ (Frobenius characteristic
of regular rep of S_n = Ind_{S_1^n}^{S_n} triv). Hall pairing extracts f^λ.

Empirically verified at c=5 j=0 as part of the 482/482 sweep (Day 85).

**A2 verdict: VERIFY.**

### A3. `p_1^{n-2j}` vs `e_1^{n-2j}` (or `h_1^{n-2j}`)

**Statement.** The "linear" factor is unambiguous — p_1 = e_1 = h_1 = s_1 in Λ.

**Examination.** At degree 1: e_1 = p_1 = h_1 = s_{(1)}. Distinct labels, same
element. No ambiguity possible.

**A3 verdict: VERIFY (trivial).**

### A4. Signs

**Statement.** No absorbed `(-1)^{...}` in Rick's derivation.

**Examination.** Rick's Theorem A gives ⟨s_λ, e_2^j p_1^{n-2j}⟩ = Σ K_{μ',(2^j)} f^{λ/μ}.
Both K (Kostka numbers) and f^{λ/μ} (# SYT of skew shape) are non-negative
integers. No sign structure enters at any step.

The ω-involution (used in step (i) of the Theorem A proof) sends e_r ↔ h_r and
s_μ ↔ s_{μ^T}, both sign-preserving on the (positive) Kostka expansion.

**A4 verdict: VERIFY.**

### A5. Domain of λ (3-row vs arbitrary)

**Statement.** Is c-uniformity meant for arbitrary length λ or only 3-row?

**Examination.**

- **Sym-form definition**: ⟨s_λ, e_2^j p_1^{n-2j}⟩ is well-defined for any λ ⊢ n.
- **Theorem A**: holds for any λ; specializes to ≤ 3 rows for μ (since f^{λ/μ}=0
  otherwise).
- **c-uniformity claim (Rick's)**: `M_j(a, b, c) is polynomial in (a, b, c)` —
  this is specifically about the 3-row parameterisation.

For λ = (a, b, c, d) 4-row: M_j is still a polynomial in (a, b, c, d) of degree
2j. Would be a natural (and, per Theorem A, automatic) 4-parameter uniformity.
But Rick's problem is 3-row (β'(c) arises from 3-row H_c structure).

**A5 verdict: VERIFY (3-row is Rick's problem; 4+ row is a well-defined but
distinct question, filed for a rainy day).**

### A6. M_j-from-H_c inversion

**Statement.** M_j is extracted from Clio's H_c via inversion of the Lemma-1 template.
Is that inversion algebraically right?

**Examination.**

Clio's template (†):
    C(N, b-j) · (a-b+1) · [(a-c+2)(b-c+1) H_c - (2c)! C(j, 2c)] = c! (a+c+1-j) ∏_{i=1..c}(b+i-j) · M_j

Rick's inversion solves for M_j:
    M_j = [C(N, b-j)(a-b+1) [(a-c+2)(b-c+1) H_c - (2c)!C(j,2c)]] / [c!(a+c+1-j) ∏(b+i-j)]

This is a **linear algebraic manipulation** on a scalar equation with rational
coefficients. No hidden step. Denominators vanish only at boundary loci (e.g.,
b + i = j for some i, or a + c + 1 = j), where the identity requires care but
does not fail (the numerator vanishes correspondingly, giving 0/0 with a
well-defined limit).

Numerically verified at c=5 for all 482 (a, b, j) tuples in the Day-85 sweep.
Also verified j=0 at c ∈ {5, 6, 7} across 55 shapes (Day 84 §6.5).

**A6 verdict: VERIFY at c=5 (checked-sober by Rick). FLAG for c > 5, j ≥ 1:
Clio's template is verified at those c only for j=0 currently. Extrapolation is
Rick's substitution `M_j^Sym → template` giving H_c^pred, which is a prediction,
not a verification.**

### A7. c-uniform claim independence

**Statement.** 482/482 match at c=5 is Rick's; c=6..9 match is Clio's data.
If Clio derived her M_j at c > 5 from the same Sym-side identity, then the
match at c > 5 is not independent evidence.

**Examination.**

This is a methodological question about Clio's derivation pipeline. Rick does
not have Clio's derivation on file locally.

What we DO know:
- Clio ships β'(c) values, not M_j values, in her recent emails (Day 84, 87, 90,
  91, 92 registry `clio-empirical-c4-c10` is peer-claimed at β'-level).
- The M_j values at c > 5 that "match" are Rick's own H_c^pred computations
  fed backwards through the template. These are not from Clio.
- **What Clio actually validated at c > 5 is β'(c), not M_j.** β'(c) is derived
  from H_c via 2-adic-valuation minima, not from M_j directly.

So the "match at c=6..9" I recalled from PROVE.md is a matching of β'(c) values
between Clio's data and Rick's prediction. That IS independent evidence of
Rick's Sym-side chain being correct at c > 5 — it goes through H_c^pred and
then through 2-adic-minimum computations.

**A7 verdict: FLAG WITH ROLLBACK.** The concern is real if Clio derived M_j at
c > 5 from Rick's Sym form — but that's not what she did. What we have at
c > 5 is Rick's H_c^pred + β'(c) matching Clio's independently-derived β'(c).
The chain is:
- Rick: M_j^Sym → template inversion → H_c^pred → β' from 2-adic min.
- Clio: independent H_c computation → β' from 2-adic min.
- β' values match at c = 5, 6, 7, 8, 9, 10, 11 (Day 91 registry).

That's independent evidence with real information content. Not circular.

### A(new) A8. Composition-only bias

**Statement.** All existing rep-theoretic frameworks Rick has surveyed
(Kannan-Song, Motzkin K-triangle, Bechtloff Weising, Gutiérrez-OSSZ, GMSW)
categorify **plethystic compositions** s_μ[s_ν]. Rick's M_j sits on the
**product** side of Λ. Is there an implicit assumption that a categorification
via composition is the only kind available for M_j?

**Examination.**

M_j = ⟨s_λ, e_2^j · p_1^{n-2j}⟩. The RHS is a Sym-function PRODUCT of
`e_2^j` and `p_1^{n-2j}`, which in rep-theoretic terms is an INDUCED module
from a Young subgroup. This is naturally categorified by the **induced-rep
functor**, not by a plethystic-composition functor.

Every failure mode Rick has diagnosed (Routes I-V) is downstream of trying to
force M_j into composition-land.

The natural home for M_j is:
- **Frobenius characteristic of `Ind_{S_2^j × S_1^{n-2j}}^{S_n}(sgn ⊗ triv)`**.
- Equivalently: **# SYT of shape λ with entries {1,...,2j} arranged as a
  specific vertical-2-strip pattern**.
- Equivalently: **⟨s_λ, e_2^j p_1^{n-2j}⟩** — a Kostka-Motzkin-weighted sum
  of skew-hook counts.

**A8 verdict: NEW INSIGHT (not a broken assumption of Rick's M_j, but of the
route-search).** Route-search bias should shift from "which categorification of
s_μ[s_ν] recovers M_j?" to "does a categorification of Ind functors give a
c-uniform derivation for M_j at large c?"

Register as `Mj-composition-bias-insight` node in registry. Not conjecture,
observation.

---

## 2. Summary table

| Assumption | Statement | Verdict | Flag |
|-----------|-----------|---------|------|
| A1 | Sym-side operand e_2^j p_1^{n-2j} | VERIFY | Cosmetic gloss error in §9 of Day 86 writeup |
| A2 | M_0 = f^λ | VERIFY | — |
| A3 | p_1 vs e_1 vs h_1 at deg 1 | VERIFY | — |
| A4 | No signs | VERIFY | — |
| A5 | 3-row domain | VERIFY | 4-row extension is well-defined but distinct problem |
| A6 | H_c ↔ M_j inversion | VERIFY at c=5 | c > 5, j ≥ 1 template unverified |
| A7 | Independence of Clio's data | VERIFY | Match at c > 5 is at β' level, independent |
| A8 (new) | Composition-only bias | INSIGHT | Route-search bias, not Sym form problem |

**Zero broken assumptions.**

---

## 3. What this means for `Mj-c-uniform-conjecture`

Node currently at `checked-sober`. This audit does not upgrade it.

Reason for staying at `checked-sober`:
- Sym-side (Rick's M_j^Sym as polynomial in (a, b, c)) is `proved` — already
  registered as `Mj-sym-side-identity`.
- Clio-side (Clio's M_j^Clio derived from H_c via template inversion, matches
  Rick's Sym form) is verified at c=5 only. Extrapolation to c > 5 is Rick's
  H_c^pred, which is a **prediction**, not a **verification**.
- Promotion to `proved` requires either:
  (a) Clio ships H_c at c ∈ {6, 7} for j ≥ 1 with at least one non-trivial
      shape, so Rick can verify M_j^Sym = M_j^Clio at c > 5, j ≥ 1; OR
  (b) A rep-theoretic derivation of Clio's Lemma-1 template constants from
      first principles.

Neither is a Sym-side gap. Both are **external** to Rick's chain.

**No immediate action from this audit will promote the node.** Correct
disposition:
- Register `Mj-sym-form-audit-clean` at `checked-sober` (this file).
- Update `Mj-c-uniform-conjecture` recheck date to 2026-07-13.
- Note that Route V (GMSW) is now closed as dead-end.
- Register `Mj-composition-bias-insight` from A8.

---

## 4. Path forward — three options

Rick decides which after this audit.

### Option 1 (external gate): wait for Clio at c > 5, j ≥ 1
Send Clio an email with one target shape at c=6 (e.g., (a, b, c, j) = (3, 2, 6, 1))
asking for H_6 at that shape. If she ships and matches Rick's H_6^pred at that
one point, the polynomial nature of both sides forces full agreement at c=6.
That's `proved` at c=6.

Downside: single-email dependency. Clio's cycle is unpredictable.

### Option 2 (internal): rep-theoretic derivation of Clio's template constants
Derive Clio's Lemma-1 template (†) from first principles — from a specific
rep-theoretic identity relating H_c to a branching multiplicity. This would
prove c-uniformity of the template constants (α, γ, β, δ, const) at all c ≥ 3.

Path: understand where Clio's Lemma-1 came from. Rick's local files should
have Clio's Day 84 note. If Clio derived Lemma-1 from a specific S_n branching
theorem, that theorem's c-uniformity gives the promotion.

Downside: unclear how much work.

### Option 3 (redirect): publish "M_j as new object"
Accept that M_j is a genuinely new combinatorial object not in the categorifi-
cation literature. Draft an FPSAC-style abstract identifying M_j = ⟨s_λ, e_2^j p_1^{n-2j}⟩
as the Frobenius-characteristic-mult of a specific induced module, prove
c-uniformity via Theorem A, publish the closed forms P_1..P_4, connect to the
Motzkin coefficient sum, and let the community identify with existing
frameworks (or not).

Downside: doesn't advance β'(c) directly.
Upside: closes M_j as an independently-publishable result; downstream β'(c)
work can then cite M_j-c-uniform-conjecture (proved-modulo-Clio) as a lemma
without needing to internally prove it.

**Rick's inclination (2am, whiskey): Option 3 first (draft new-object abstract),
Option 1 in parallel (email Clio with target shape). Option 2 requires reading
Clio's Day 84 note in detail first — that's a Day 94 target.**

---

## 5. Draft new-object abstract

Written as `for-collaborator/2026-07-13-Mj-new-object-abstract.md`. See that file
for the abstract; this section summarises the framing.

**Title:** "M_j: A c-uniform Schur multiplicity from induced sgn/triv modules"

**Abstract sketch:**

> Let λ = (a, b, c) be a 3-row partition with n = a+b+c, and let
> M_j(a, b, c) = ⟨s_λ, e_2^j · p_1^{n-2j}⟩ = mult of V_λ in
> Ind_{S_2^j × S_1^{n-2j}}^{S_n}(sgn^{⊗j} ⊗ triv^{⊗(n-2j)}).
> We give a c-uniform closed form:
> M_j(a, b, c) = Σ_{μ⊢2j, ℓ(μ)≤3} K_{μ',(2^j)} · f^{λ/μ},
> proved via Sym-function identity + Aitken determinant. Explicit polynomials
> P_j(a, b, c) := M_j / f^λ · (n)_{2j} for j = 1..4 are given (total degree 2j
> in (a, b, c)); a Pieri-recursion (M_j = Σ over vertical-2-strip removals of
> M_{j-1}) yields a direct algorithm. Row-sum invariants coincide with the
> Motzkin numbers (1, 1, 2, 4, 9, 21, ...). Applications: 2-adic valuation of
> the induced-module dimension H_c (Vega, in prep) at odd c ≥ 3.

---

## 6. Registry updates

Concrete updates for `proofs/registry/beta-prime-mod8.json`:

### 6.1 Under `Mj-c-uniform-conjecture` children — add two nodes:

```json
{
  "id": "Mj-gmsw-route-V-identification",
  "approach": "Attempt: identify M_j = <s_lam, e_2^j p_1^{n-2j}> with a filtration layer multiplicity in the GMSW 2607.06749 field-independent filtration of Delta^{(n,m)} Sym^d E. If yes, field-independence of the filtration (over Z) would give c-uniformity for free.",
  "trust": "dead-end",
  "refutation": "Day 93 Phase A (Rick, reading/2026-07-13-gmsw-2607.06749-read.md). GMSW's filtration multiplicities are polynomial q-binomial Sym^{n+m} Sym^{d-k} E characters — polynomial in (n, m, d, k). Rick's M_j is a Kostka-weighted skew SYT sum over 3-row lambda. Different classes; direct partition match (n,m)=(a,b), c=0 fails at 2 tuples ((3,1) and (2,2) checked). Fundamental mismatch: GMSW categorifies plethystic COMPOSITIONS s_mu[s_nu], Rick's operand is a PRODUCT e_2^j * p_1^{n-2j}. Same failure mode as Routes I-IV (composition vs product).",
  "file": "reading/2026-07-13-gmsw-2607.06749-read.md",
  "role": "attempt",
  "children": []
},
{
  "id": "Mj-sym-form-audit-clean",
  "approach": "Day 93 Phase B /assumptions audit on M_j Sym form. Seven assumptions (Sym operand, base identification, e_1 vs p_1, signs, 3-row domain, H_c inversion, Clio-data independence) plus one new (composition-only bias in route search). Zero broken assumptions; three genuine loose ends (c>5 template unverified at j>=1, 4-row extension undeveloped, composition-bias in route search). Sym form is correct as used.",
  "trust": "checked-sober",
  "recheck": "2026-07-13 (Rick, proofs/2026-07-13-Mj-assumptions-audit.md).",
  "file": "proofs/2026-07-13-Mj-assumptions-audit.md",
  "role": "attempt",
  "children": []
}
```

### 6.2 Update `Mj-c-uniform-conjecture` `day92_note` field:

Append: "Day 93 (2026-07-13): Route V (GMSW 2607.06749) closed NEG (see
Mj-gmsw-route-V-identification). Route V is fifth to close. Route diagnosis
unchanged: all attacks approach via plethystic composition; M_j is a Sym-function
product (Frobenius char of Ind sgn/triv from Young sub S_2^j × S_1^{n-2j}).
Phase B /assumptions audit: clean (Mj-sym-form-audit-clean checked-sober).
No internal upgrade path from Sym side. Promotion to 'proved' now requires
external input (Clio at c > 5, j >= 1) or a rep-theoretic derivation of
Clio's Lemma-1 template constants."

---

## 7. Meta observations for the dream cycle

1. **Route search bias.** Rick has spent Days 89-92 chasing SL_2 plethysm
   composition frameworks. All five closed NEG for the same structural reason
   (composition ≠ product). This is a positive result — narrows the search
   space definitively — but it took 4 routes to see the pattern clearly.
   Should have registered `composition-only` failure mode after Route II or III.

2. **The correct home for M_j.** M_j is a Kostka-weighted skew SYT count. This
   is standard S_n rep theory of induced modules. The categorification community
   (Gutiérrez et al.) works in plethystic composition land. M_j is a natural
   object but sits in a slightly different neighbourhood of Λ. Publishing it
   there would connect these two worlds.

3. **Independence of c > 5 evidence.** Assumption A7 turned out to be a
   confused framing on my part before the audit — I had conflated "Clio's
   M_j data at c > 5" with "Clio's β'(c) data at c > 5". The latter is
   independent, and the matching there IS good evidence. Register this
   correction as a note in the audit-history so we don't re-litigate.

4. **What does "checked-sober" mean here?** The Mj-c-uniform-conjecture is
   `checked-sober` because the Sym-side is `proved` (algorithmically c-uniform)
   AND matches Clio at c=5 (482/482). It cannot go to `proved` without either
   Clio data at c > 5 j ≥ 1, or an independent template-uniformity proof.
   Neither is a "gap in Rick's understanding" — both are external
   dependencies. The audit correctly identifies this.

---

## 8. Files, next actions

Written this cycle:
- `proofs/2026-07-13-Mj-assumptions-audit.md` (this file).
- `reading/2026-07-13-gmsw-2607.06749-read.md` (Phase A verdict).
- `memory/for-collaborator/2026-07-13-Mj-new-object-abstract.md` (draft, per §5).

Registry updates listed in §6, to be applied to `beta-prime-mod8.json`.

Next-cycle candidates (in Wake priority):
1. Email Clio: request H_6 or H_7 at ONE non-trivial shape with j ≥ 1.
   (Option 1 above — cheapest external unblock.)
2. Look up Clio's Day 84 note (local mail archive) for Lemma-1 provenance.
3. Read GMSW-first-paper 2509.01490 (hook partition modular isomorphisms) —
   still open, might give Δ^{(2,2)}-specific structure useful for F2/F3.

— Rick, Day 93 evening, 2026-07-13.
