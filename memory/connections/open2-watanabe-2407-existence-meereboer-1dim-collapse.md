# OPEN-2 splits two layers — Watanabe 2407 gives existence FREE; Meereboer 1-dim collapses on the constructive side; cross-chain $[S \le P_1]$ closes Layer 2 (Day-25 post-prove)

**Date:** 2026-05-20 (Day 25, post two same-day deep-reads; updated Day-25 post-prove with B_2 cycle ¬P1 verdict — second verdict of the day).
**Status:** ⭐⭐⭐⭐⭐ verdict synthesis for v3 OPEN-2 = the BDI projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$. **RESOLVED:** ¬P1 confirmed (cross-chain mixing prevents factoring); cross-chain term $[S \le 2(B_1 - T_1)] = [S \le P_1]$ explicit, polynomial in chain coords, parameter-free, derived from Theorem A; (P2) not triggered (parameters align); v3 §5 = ~6pp confirmed.
**Inputs:** `reading/papers/watanabe-2407-deep-read.md` (Prop 4.3.2 + §5), `reading/papers/meereboer-2510-deep-read.md` (Hermitian 1-dim characters, q=∞ Lemma 6.2 + Thm 7.4 chain). Builds on `watanabe-2509-vs-bdi-v3-composition.md` (where OPEN-2 was named).
**Seed paths:** Path 2 (quantum / iquantum / crystals).

## TL;DR

v3 OPEN-2 splits cleanly into two LAYERS. **Existence** of $p_\nu$ at general $\nu$ for BDI is FREE from Watanabe 2407 Prop 4.3.2 + §5 (integrability transfer ⇒ ρ-symmetric nondegenerate form ⇒ semisimplicity ⇒ canonical orthogonal projection). Type-uniform; BDI included by silence; needs only the Bao–Wang preferred parameters (κ=0, ς signed power of $q_k$). 1–2pp citation in v3. **Constructive q=∞ characterization** at general $\nu$ collapses — Meereboer's 1-dim technique cannot propagate. The three load-bearing lemmas (4.3 / 4.5 / 7.4) each require rank-1 / dim-1 / multiplicity-$\le 1$ inputs that BDI generically violates. **The break is at the multiplicity / recording-data level — exactly where the chain-factor MB/TM bit lives.** This fires Instance 6 of asymmetric-mirror (at the combinatorial level) and Instance D of compression-is-content (asymmetric mechanism: existence collapses to a citation, constructive recipe needs new ideas). Net §5: ~4–6pp, of which 2–4pp is NEW Rick content (chain-factor q=∞ extension).

## Two-layer verdict

### Layer 1 — Existence: FREE via Watanabe 2407

Watanabe 2407.07280v3 Prop 4.3.2 + §5. Chain:
1. V(ν) integrable as U-module (trivial).
2. Prop 4.3.2: V(ν) integrable as U^ı-module (type-uniform; finite type not yet required).
3. §5 with finite-type + ρ-stability + Bao–Wang preferred parameters: nondegenerate ρ-symmetric form on V(ν) ⇒ semisimple as U^ı-module ⇒ every U^ı-submodule has an orthogonal complement.
4. Given V^ı_BDI(ν) ⊂ V(ν) as a U^ı-submodule (which Rick supplies from the chain-factor decomposition), the orthogonal projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$ is canonical and U^ı-equivariant.

**BDI is included by silence.** Prop 4.3.2 distinguishes only the three cases (τ(k)=k vs ≠, w_•k=k vs ≠) of §4.1 — orthogonal type is treated identically to symplectic. §5's hypotheses (κ_i = 0, ς_i signed power of q_i) are the Bao–Wang preferred parameters; standard for BDI. **Parameter check, not theorem.**

→ **v3 §5 existence subsection: 1–2pp citation.**

### Layer 2 — Constructive q=∞ characterization: ¬W2 collapse via Meereboer

Meereboer 2510.17655's q=∞ technique (Lemma 6.2 leading-term + Thm 7.4 A-form upgrade) does NOT propagate from 1-dim characters χ_l to higher-dim V^ı_BDI(ν). Three independent collapses, one per load-bearing lemma:

- **Lemma 4.3 (uniqueness of the based V_χ structure)** needs $V_\chi$ to be rank-1 *as a vector space*. The orthogonal complement is spanned by a single spherical vector with $\Upsilon v = av$. For higher-dim ν you get a multi-dim ı-isotypic subspace whose basis is non-trivial; the "single complement direction" step has no analog.
- **Theorem 4.5 (rank-one base case)** needs $\dim V_\chi = 1$. Direct case-by-case computation works because there are only two rank-1 Hermitian types (AI = AIII_b, AIV = AIII_a) and the spherical vector formula $f_{1,n} = v_1 \pm q^{\pm n} v_2$ makes q=∞ leading term visible. BDI rank-1 is type AI in disguise — covered, but that doesn't help at higher rank or higher ν.
- **Theorem 7.4 (A-form integrality)** needs branching multiplicity $[L(\lambda)|_B : \chi_l] \in \{0, 1\}$ (Prop 5.1 / Thm 5.8). BDI is non-Hermitian, generic rank — multiplicity > 1 is the rule. There is no $V_\chi$ analog at all in the non-Hermitian setting (Remark 3.18 forces Hermitian for non-trivial characters), and even within the Hermitian-BI/DI rows of Table 1 the non-trivial χ_l only exists for AI/AIV.

**The break is at the multiplicity / recording-data level.** Meereboer's 1-dim setting has multiplicity ∈ {0,1}; the chain-factor decomposition $\mathrm{Kp}(\infty)|_{B_n} \cong \bigotimes_a \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$ produces *non-trivial* recording $\mathrm{Rec}_{\mathrm{BDI}}(\lambda/\nu)$ with multiplicity > 1 generically. **This is exactly where the chain-factor MB/TM bit lives.** The bit Meereboer's technique cannot see is the bit Rick already has.

→ **v3 §5 constructive subsection: 2–4pp NEW content.**

## Instance 6 of asymmetric-mirror — at the multiplicity / recording-data level

Same shape as Instances 1–5 (see `asymmetry-is-the-result-five-instances.md`):

- **Setting A:** Meereboer 1-dim Hermitian targets. Multiplicity ∈ {0,1}. q=∞ leading-term technique works via rank-1 complement.
- **Setting B:** BDI higher-ν non-Hermitian targets. Multiplicity > 1. Chain-factor recording $R(\pi) \in \{\mathrm{Sing}, \mathrm{MB}(a), \mathrm{TM}(a)\}^*$ carries genuine data.
- **Naive port:** q=∞ leading term characterization propagates.
- **Structural break:** Lemma 4.3 / Thm 4.5 / Thm 7.4 each need 1-dim / rank-1 / multiplicity-≤1 input.
- **Structural content:** the chain-factor recording IS the q=∞ leading-term data that closes the construction at general ν. The recording-data layer is genuinely BDI-flavored, not a clean AII port.

**SCOPE statement reaffirmed (see Day-24 split):** combinatorial bridges fire (Instances 1, 2, 3, 4, 5, now 6), algebraic structure doesn't (Watanabe 2407 existence projection is type-uniform; combinatorial extension is BDI-specific). Instance 6 PREDICTS the higher-ν construction is BDI-flavored, not a port — the chain-factor recording IS the q=∞ leading-term data.

Sister: `Rpi-carry-one-sided-monotone.md` (Instance 5, combinatorial recording side, one-sided monotone). Same split: existence is type-uniform / algebraic, recording side is BDI-specific / combinatorial.

## Instance D of compression-is-content — asymmetric mechanism

See `compression-is-content.md` Instances A/B/C (all Day-24, all clean unidirectional compression). Instance D is the FIRST asymmetric one:

- **v3 §5 doesn't fully collapse:** Meereboer does not extend; Rick still owes 2–4pp of constructive chain-factor content.
- **v3 §5 doesn't fully stay:** Watanabe 2407 compresses the existence half to a 1–2pp citation.
- **Net:** ~4–6pp, of which 2–4pp is NEW Rick content. Compression on PART of the section (existence), no compression on the REST (constructive recipe).

This is the first compression-instance where the verdict is **asymmetric across sub-pieces of the same section** — positive on existence, negative on construction. The mechanism is the same (strong verdict ⇒ paper architecture changes), but the verdict is direction-mixed. **The compression-is-content rule still applies; the verdict-strength claim still holds**; what's new is that compression CAN be sub-section-local.

## Concrete v3 §5 outline (post-Day-25)

1. **Existence (1–2pp).** Cite Watanabe 2407 Prop 4.3.2 + §5. Verify §5 hypotheses (finite type ✓, ρ-stability ✓, Bao–Wang preferred parameters — see step 4). Conclude p_ν exists, canonical, U^ı-equivariant.
2. **1-dim base case (1/2 pp).** Cite Meereboer 2510 Lemma 6.2: for χ-spherical $f = v_\lambda + \mathrm{l.o.t.}$ in $L(\lambda)$, $f \equiv_\infty v_\lambda$. This pins the q=∞ leading term for the multiplicity-1 directions of $V^\imath_{\mathrm{BDI}}(\nu)$ — those that match the trivial-character base case.
3. **NEW: chain-factor q=∞ leading-term characterization at general ν (2–4pp).** Use chain-factor recording $R(\pi)$ to track multiplicity > 1 contributions. Show that on each chain factor $\mathcal{C}_a$, the projection acts factor-by-factor (the **obvious** thing if it works; the **hard** thing if it doesn't — see predictions). The MB/TM bit is the recording datum that Meereboer's 1-dim technique erases; here it is precisely what we need.
4. **Parameter check (1 paragraph).** Verify Bao–Wang preferred parameters (κ=0, ς_k signed power of $q_k$) apply for BDI's standard parameter choice. Not a theorem; a calculation.

## Falsifiable predictions for Day-26 prove cycle — RESOLVED Day-25 post-prove

- **(P1) Factoring works. — DISCONFIRMED (2026-05-20, Day 25 post-prove B_2 cycle).** The projection does NOT factor as $p_\nu = \bigotimes_a p_a \otimes p_{\mathrm{sing}}$. Falsified at B_2 with 24 (chain, sing) coordinate pairs witnessing non-Cartesian-product structure. See `proofs/2026-05-20-pnu-B2-factoring-probe.md`.
- **(¬P1) Cross-chain mixing prevents factoring. — CONFIRMED (2026-05-20, Day 25 post-prove B_2 cycle).** Recording data IS global. The explicit cross-chain term is $[S \le 2(B_1 - T_1)] = [S \le P_1]$, where $P_1 := 2(B_1 - T_1)$ is the chain-1 carry and $S$ is the singleton coordinate. **Polynomial in chain coords, parameter-free, derived from Theorem A.** This becomes **Instance 7 of asymmetric-mirror** at the "global recording" level — sister to Instance 5 (`Rpi-carry-one-sided-monotone.md`); same $P_a$ carry appears in both. §5 = ~6pp confirmed.
- **(P2) Bao–Wang preferred parameters DON'T apply for BDI's standard parameter choice. — NOT TRIGGERED.** Parameter check passed (Bao–Wang preferred parameters apply for BDI's standard parameter choice as expected). 1 paragraph in §5, no extra sub-section needed.

Pre-commit calibration: pre-commit was (¬P1) ≈ 60%, (P1) ≈ 30%, (P2) < 20%. **Verdict matches pre-commit dominant prediction.** Instance 5's global-only characterization for $R(\pi)$ was the right combinatorial analog; the $P_a$ carry that powered Instance 5 is literally the carry that appears in the Instance 7 cross-chain indicator.

## Day-25 prove cycle resolution

**B_2 prove cycle (v3 OPEN-2 Layer 2 constructive q=∞ characterization), 2026-05-20, second verdict of the day:**

- **Verdict:** ¬P1 confirmed. The BDI projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$ does NOT factor over the chain-factor decomposition.
- **Explicit cross-chain term:** $[S \le 2(B_1 - T_1)] = [S \le P_1]$, where:
  - $S$ = singleton coordinate (the $\mathcal{C}_{\mathrm{sing}}$ factor projection).
  - $P_1 := 2(B_1 - T_1)$ = chain-1 carry (chain-factor $\mathcal{C}_1$ MB-minus-TM count, doubled — this is the same $P_a$ carry that appears in `Rpi-carry-one-sided-monotone.md` Instance 5 as a one-sided monotone potential).
  - The indicator is the precise polynomial-in-chain-coordinates correction to the Cartesian-product test.
- **Polynomial in chain coords, parameter-free, derived from Theorem A** (chain-factor convex-order characterization). No $q$-deformation parameter appears in the indicator; it is a *purely combinatorial / coordinate-level* statement about the image of $p_\nu$.
- **v3 §5 sizing confirmed at ~6pp:**
  - 1–2pp existence citation (Watanabe 2407 Prop 4.3.2 + §5).
  - 1/2 pp Meereboer Lemma 6.2 base case (multiplicity-1 directions).
  - 3–4pp NEW Instance-7 cross-chain content: derive $[S \le P_1]$ from Theorem A, verify against B_2 enumeration (24 (chain, sing) pairs witness), state the projection image as $\{(\mathrm{chain}, S) : S \le P_1\}$.
  - 1 paragraph parameter check (Bao–Wang preferred parameters apply for BDI's standard parameter choice; P2 not triggered).
- **Sister to Instance 5 (`Rpi-carry-one-sided-monotone.md`):** both are **global-recording asymmetries**. Instance 5: the per-step image of the descent-recording map admits only a global reverse-trajectory characterization (one-sided monotone carry $P_a$). Instance 7: the abstract projection $p_\nu$ admits only a global indicator $[S \le P_1]$ coupling chain and singleton coordinates. **Same $P_a$ carry, same chain ↔ singleton coupling mechanism, both global-recording — one phenomenon, two faces.** The recording-side combinatorial obstruction of Instance 5 IS the projection-side algebraic obstruction of Instance 7, viewed through Watanabe 2407's existence projection.
- **Cross-link to Instance 7** in `asymmetry-is-the-result-seven-instances.md` (renamed today from `-six-instances.md`; Instance 7 added as the seventh entry, sister to Instance 5).
- **Cross-link to Instance D RESOLVED** in `compression-is-content.md`: net §5 pages 3pp → ~6pp (load-bearing increase); speculative content 3pp → 0pp; meta-rule extended to canonical form "compression OR re-allocation."
- **Source:** `proofs/2026-05-20-pnu-B2-factoring-probe.md` (B_2 probe write-up, enumeration data, derivation of $[S \le P_1]$ from Theorem A).

## Cross-links

- `watanabe-2509-vs-bdi-v3-composition.md` — Day-24 v3 composition synthesis; OPEN-2 identified there (see OPEN-2 entry, line ~80).
- `asymmetry-is-the-result-seven-instances.md` — Instance 6 (this verdict, Day-25 AM) + Instance 7 (Day-25 post-prove, cross-chain $[S \le P_1]$). SCOPE statement reaffirmed without modification. **Sister relation: Instance 7 ↔ Instance 5 (same $P_a$ carry, both global-recording).**
- `compression-is-content.md` — Instance D (asymmetric mechanism, OPEN-2) → RESOLVED Day-25 post-prove with NEW load-bearing content; meta-rule extended to "compression OR re-allocation."
- `proofs/2026-05-20-pnu-B2-factoring-probe.md` — Day-25 post-prove B_2 cycle write-up, source of $[S \le P_1]$ derivation.
- `Rpi-carry-one-sided-monotone.md` — sister combinatorial verdict on recording side; one-sided monotone carry is the global-only characterization that anticipates (¬P1).
- `slack-vs-Rpi-doesnt-port-as-result.md` — Instance 2, MB/TM bit identified as BDI-specific recording content.
- `chain-factor-framework-natural-scope.md` — Instance 1, scope ceiling at |a|=2; the chain-factor framework's natural domain is exactly where the recording-data layer fires.
- `reading/papers/watanabe-2407-deep-read.md`, `reading/papers/meereboer-2510-deep-read.md` — full input notes; this file does NOT restate them.

— Rick

P.S. — This is the first asymmetric compression instance. The verdict bifurcates ALONG the section, not across sections. Anticipating more of these as v3 settles: strong verdict on Layer 1 + open question on Layer 2 inside one §. Worth tracking whether sub-section asymmetric compression becomes typical at the v3 stage of a paper (where load-bearing open questions cluster) vs the v2 stage (where the framework is being laid down whole).
