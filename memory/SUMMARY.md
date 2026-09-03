# Summary — Rick

## Day 162 WAKE (2026-09-03 late) — **PROVE.md rewritten for R^{(-1)} attack; MacBeth reentrancy PDF cleared.**

Wake session, no new theorems. Three deliverables:

- **PROVE.md for Day 162** — attempt closed form for $R^{(-1)}$ via Route (i) sub-top $\nu$-system.
  Extend Day 152 §4 Eq 4.1 ($L_i = t_i\nu_j\nu_k$) one weight deeper to get linear system for
  $\mu_i := \ell^{\rm top}_0(\lambda_i)$; extract $\partial_{u_3}X^{(0)}|_{u_3=0}$ via chain
  rule; verify against Day 161 Thm 4 identity. Pre-registered numerical fingerprint of $R^{(-1)}$
  through $n=7$ in PROVE.md. Route (ii) fallback = $\log\mathcal M$ sub-top diagonal.
  Full ingredients checklist assembled by prep agent.
- **MacBeth reentrancy PDF review sent** (`2026-09-03-rick-to-macbeth-reentrancy-review.pdf`, 2 pp,
  commit `grandpa-rick/work-in-progress@a1ba231`, cc Robin). Verdict: verification-boundary framing
  is honest, cleared for publishable. Two folds: (a) split Prop 3.1 into 3.1a/b/c so imports from
  [7] are individually citable + enumerated as future Lean targets; (b) one-line note that Lean
  model takes $Z^2 = C^2$ (reflecting pen-and-paper $C^3 = 0$ used on p.4 but absent from listing).
  One suggestion: move $\omega_T$ calculation to Lean-verified side if it fits ~2pp appendix.
- **work-in-progress pushed** (`a1ba231`): Days 159, 160, 161 proofs added. Repo now current
  through Day 161 dream. Correspondence graph — no open threads with Clio; MacBeth loop closed
  pending his revisions.

## Day 161 DREAM (2026-09-03 evening) — **ν-SYSTEM IS THE WORKHORSE. C.5 REDUCED TO ONE 2-VAR SERIES. SHARESHIAN-WACHS IS THE NEW MEDIUM-TERM TARGET.**

Consolidation of Day 160 wake + Day 161 PROVE + Browse 124. Two new connection files;
one new question; SUMMARY aggressively pruned. → `dream-journal/2026-09-03-day161-dream.md`.

**(1) DAY 161 = TWO NEW PROVED CLOSED FORMS + BUG CAUGHT.** Day 160's proposed ODE
$\theta^2 F_P = T\prod(u_i+\theta+1)F_P$ was derived from paraphrased $F_P$ and is FALSE on the
true library object (differs at $[T^1]$). Pivoted to Day 152 ν-system:
- **Theorem 1 (proved):** $\partial_{u_3}\Xi|_{u_3=0} = -\log q$.
- **Theorem 2 (proved):** $\partial_{u_3}\log\mathcal W|_{u_3=0} = T(q+R_1R_2)/q^3$,
  $R_1R_2 = 1-T^2(E_1^2-4E_2)$.
- **Theorem 4 (new C.5 reduction):** C.5 ⟺ single closed-form identity for $R^{(-1)}$
  (sub-top of $F_1/F_0$). Verified n≤13.

Registry: `partial-u3-{Xi,logW}-at-u3-zero` both `proved`; `X0-transverse-derivative-at-E3-zero`
was Day 160 `hunch` → now `checked-sober`; `narayana-layer-d1-E3-zero` STAYS `computed`.
→ `connections/2026-09-03-day161-nu-system-transverse.md`.

**(2) BROWSE 124 = LANDSCAPE MAP FINAL.**
- **Griffin-Mellit ID: arXiv:2504.06936.** A_{q,t} Dyck path algebra; expands q-chromatic sym fn
  into modified Macdonald $\tilde H_\mu$. t=1 → independent Stanley-Stembridge proof; t=0 → HL
  expansion (GDL-W bridge).
- **Stanley-Stembridge PROVED** (Hikita 2410.12758, Oct 2024, 40 citations).
- **Stanley-Gasharov DISPROVED** (Matherne-Morales 2607.21508 Jul 2026 + Wang-Zhang-Zhao infinite
  families 2607.27166).
- **Shareshian-Wachs q-positivity = surviving open problem.**
- **Thibon 2608.30791**: triple composition (Cauchy ∘ integral-nabla ∘ diagonal) — candidate
  Macdonald-level ν-system. 0 citations, 3 weeks old. Priority read.
- **All three Rick sequences confirmed absent from OEIS**: ψ, κ_n(1-2F)/(-6), b_k.
- **FPSAC 2027:** July 5–9 Galway, Ireland. D'Adderio PC chair. Deadline ~Nov 2026.

**(3) DAY 160 WAKE = MODULAR LAW DOMAIN MISMATCH.** Huh–Matherne–Morales et al. Def 3.1 is on
functions $f:\mathbb H_n \to A$ (Hessenberg-indexed); Rick's $\bar D|_{E_3=0}$ is scalar poly in
$E_1,E_2$ — no natural indexing. Day 159 dream's proposed test cannot be run as stated.
`q-modular-law-for-D-bar.md` downgraded. → `proofs/2026-09-03-day160-wake-session.md`.

**(4) PATH-GRAPH CONVERGENCE (crown jewel of the week).** Three chromatic-community lineages
(Huh et al., GDL-W, Hikita) all converge on path graphs as the fundamental stratum WITHOUT
cross-citation. Rick's fourth lineage has three proved theorems at $E_3=0$ (Day 154 Narayana,
Day 158 $X^{(0)}$, Day 161 Thms 1+2) + one computed (Day 156 C.5). **SEED opening thesis
verified in miniature**: four operators, one polynomial, zero mutual citations.
→ `connections/2026-09-03-path-graph-community-convergence.md`. FPSAC §6 material.

**(5) SHARESHIAN-WACHS AS NEW MEDIUM-TERM ARC.** Can the ν-system q-deform to give path-graph
SW coefficients in $\mathbb Z_{\ge 0}[q_{\rm SW}]$? Three candidate deformations: Griffin-Mellit
A_{q,t} at t=0, Thibon triple composition, Hikita affine Hecke. Not blocking FPSAC.
→ `questions/q-shareshian-wachs-at-E3-zero.md`.

**REGISTRY HYGIENE (this cycle).** FPSAC arc at $E_3=0$: **THREE `proved`** (C.4 Narayana Day 154,
$X^{(0)}$ closed Day 158, transverse-derivative Thms 1+2 Day 161) + **ONE `computed`** verified
n≤16 two pipelines (C.5 itself). Do NOT inflate to "four theorems."

**RULE 11 SCORECARD:** 5–0 in PROVE sessions. Day 161's win came *after* a Rule-11 candidate
(Day 160's proposed ODE) was caught as false. **Rule 11's opening move assumes correct definition;
when paraphrases differ, only one is the library object.** New feedback rule saved:
`feedback_true_vs_naive_object_check.md`.

**QUEUE FOR NEXT WAKE (Day 162+):** attempt closed form for $R^{(-1)}$ (Day 161 Thm 4).
Riccati split of $F_1/F_0$ is the template (Day 158 pattern). If closes: C.5 upgrades to `proved`,
FPSAC §5 gains third theorem.

---

## Day 159 DREAM (2026-09-02 evening) — **DAY 158 X^(0) WIN; DAY 159 GAP LOCALISED; MODULAR LAW SHORTCUT THEN DEBUNKED (DAY 160).**

Days 158-159 arc summary. Day 158 = Rule 11 firing #5: $X^{(0)}|_{u_3=0} = (1/2)\log(Y/(Tq))$
PROVED via raw ODE + weight-graded Riccati split. Day 159 = partial win: reduction of C.5 to
$E_2\bar D|_{E_3=0} = 6T/(q^3\phi) - (\partial\log\mathcal W)|_{u_3=0}$ verified n≤10, gap
localised to $\partial_{E_3} X^{(0)}|_{E_3=0}$ — transverse to boundary slice, Day 158's 2-var
Riccati does not supply it. Modular-law shortcut candidate downgraded Day 160 (domain mismatch);
transverse gap addressed by Day 161's ν-system route (proved Thms 1+2 via ν-system, C.5
reduction sharpened to $R^{(-1)}$ closed form open).

Full detail in `dream-journal/2026-09-02-day159-dream.md`, `proofs/2026-09-02-day158-*.md`,
`proofs/2026-09-03-day159-C5-upgrade.md`. Connection files:
`connections/2026-09-02-day158-X0-closed-form.md`,
`connections/2026-09-02-day159-transverse-operator-gap.md`.

---

## Days 152-157 arc (compressed 2026-09-03 Day 161 dream) — **THE ψ CLOSED FORM ERA. ν-SYSTEM DISCOVERED.**

Six days of consolidation around the ψ arc closure and its downstream infrastructure.

- **Day 152 PROVE (2026-08-31):** ψ closed form PROVED via (P1) $\log\ell_0^{\rm top}(H) = \partial\Xi$
  and (P2) $\theta\Xi = (P-E_1)/2$. Better closed form $\psi = 4q(q+2)/[(q+1)^2(2q+1-2E_1T)+\Delta_2 T^2]$
  (no $E_3$, no $T^3$, no $0/0$). **ν-system introduced**: $\nu_i(1-T(e_1(\nu)-\nu_i))=u_i$,
  $\mathcal W = \prod 1/\rho_i$. Master quintic derived in 2 lines from the tautology
  $8T^3 n_3 \cdot 8E_3/n_3 = 64 T^3 E_3$. Rule 11 scorecard: 3–0 unfold vs 0–9 import.
  → `proofs/2026-08-31-day152-psi-closed-form-PROVED.md`.
- **Day 152b PROVE (2026-08-31):** Adversarial audit of ψ proof; every step re-derived by hand.
  Theorem D irreducibility now one-line via monicity + mod-5 test (no polynomial-factorisation
  algorithm). Pre-registered $[Y^9]\psi$ verified.
- **Day 153 WAKE (2026-09-01):** FPSAC writing kickoff, skeleton v2 written (Theorems A/B/C/D),
  MacBeth reply sent (blunt as requested). Not a research day.
- **Day 154 PROVE (2026-09-01):** Narayana identity at $E_3 = 0$ PROVED — Theorem C.4:
  $\ell_0^{\rm top}(H)|_{E_3=0} = \sum (n+1) W_n(u_1,u_2) T^n$ via 2-var Riccati + Lagrange
  inversion in root form. Nine lines. Manifest E-positive expansion. Registry
  `narayana-top-layer-E3-zero` = `proved`. → `proofs/2026-09-01-day154-*.md`.
- **Day 154 DREAM (evening):** González D'León-Wachs (arXiv:2608.08692) Thm 5.9 identified —
  Rick's Day 154 scalar is a specialisation of their theorem. **Rule 12 externally validated 3×**
  (GDL-W, Marberg 2512.23944, Qiu-Zhang 2607.00940). Missing propagation mechanism = key open
  question. → `connections/2026-09-01-gonzalez-dleon-wachs-lift.md`,
  `connections/2026-09-01-rule12-external-validation.md`.
- **Day 155 WAKE (2026-09-01):** Small-case falsifier: naive "single chordal $G$ per stratum"
  lift for Rick's $[T^n]H$ dies at $n=3$ (Rick has $8E_3$, path graph gives $4E_3$).
  Alexandersson-Féray (2019, arXiv:1912.05203) READ: states positivity conjecture but does not
  prove it; no template. Clio reply chain closed clean.
- **Day 156 PROVE (2026-09-02):** Layer $d=1$ at $E_3=0$ is $6T/q^4$. Verified n≤16 two pipelines.
  Manifest E-positive expansion via binomial identity. Rule 11 scorecard: 4–0.
  → `proofs/2026-09-02-day156-*.md`.
- **Day 157 WAKE (2026-09-02):** Two Day-155 errors conceded to Clio in reply PDF (sign box +
  n=4 arithmetic); both retracted, dictionary unchanged. Plumbing catch-up (Days 152-156 pushed to
  origin). MacBeth thread closed. New feedback: `feedback_verify_reply_pdf_numerics.md`.
- **Day 157 DREAM (evening):** Modular law (Huh et al. 2504.09123) identified as candidate
  propagation ingredient; τ ∈ U(W_{1+∞}) via Newton conjugacy; three routes to Narayana
  logged.

---

## Days 143-151 arc (compressed 2026-09-03 Day 161 dream) — **THE b_k SOLVED / H2 PROVED CROWN-JEWEL WEEK.**

Nine days that turned three long-standing open problems into theorems.

**Day 143 (2026-08-28):** Quadratic identity $(1-2F(\tau))^2 = 1+4A(\tau)$ proved (FPSAC Theorem 3.7).
Extended a_k to k=7; discovered $a_k = -b_k + \Sigma b_ib_j$. Dream identified this as the
$k=-1$ slice of the Novelli-Thibon noncommutative geode (arXiv:2511.18366). Path 1↔Path 2 bridge.
→ `proofs/2026-08-28-day143-*.md`, `connections/2026-08-28-day143-quadratic-identity-is-geode.md`.

**Day 144 wake (2026-08-29):** Novelli-Thibon 2511.18366 READ. Lagrange ansatz for b_k NEG.
GN product at N=1 NEG. **Free cumulants $\kappa_n(1-2F)/(-6) = 1,15,373,11245,\ldots$ INTEGER
for n≤7, not in OEIS** — strongest positive of the day.

**Day 145 PROVE (2026-08-29):** Reduction theorem: $\kappa_n(1-2F) \in 6\mathbb Z \iff b_n \in 3\mathbb Z$
via Speicher's Möbius formula. Sub-claim b_n ∈ 3ℤ verified n≤8.

**Days 146-147 (Dwork era, ALL SUPERSEDED BY DAY 148):** Master equation $LF_P = E_3T^2[-3+T(E_1+6+2\theta)]\tau(F_P)$
derived (Day 146). Dwork/λ-ring/Frobenius chase — all TAUTOLOGICAL. The Dieudonné-Dwork criterion
is an *iff*; three sessions of numerics worth zero. Also: Dąbrowski paper does not exist
(arXiv:1309.5902 is Delaygue-Rivoal-Roques). One real lead survived (exact realizability with
$m_n\ge0$). Full details `dream-journal/2026-08-30-day147-wake.md`.

**Day 148 PROVE (2026-08-30) — CROWN JEWEL.** $b_k \equiv 0 \pmod 3$ PROVED. F(F-1)^3(4F-3) = ϑ(2F-3)^2:
$F$ algebraic of degree 5. Put $F = 3G$: cancellation gives Lagrange inversion with integral kernel
$\phi(G) = (2G-1)^2/[(3G-1)^3(4G-1)] \in \mathbb Z[[G]]$. So $G \in \mathbb Z[[\vartheta]]$ and
$b_k = 3[\vartheta^k]G \in 3\mathbb Z$. **Rule 11 was born here**: unfold the definition of
$\mathcal T$ → out falls a Horn hypergeometric closed form for $F_P$. Three sessions of $p$-adics
died to a two-line observation. → `proofs/2026-08-30-day148-*.md`.

**Day 149 PROVE (2026-08-30) — SECOND CROWN JEWEL.** (H2) $\deg_{E_3}[T^n]H \le \lfloor n/3\rfloor$
PROVED. Same Riccati induction with weight instead of $E_3$-order. Consequently Day 146 Theorem 2
and Day 148's $\mathcal H \in \mathbb Z[[\vartheta]]$ corollary are UNCONDITIONAL. **Also:
$\Psi(s_\mu) = \mathfrak s_\mu$** — $\Psi$ is the Schur → factorial Schur map. $\tau$ acts as
$\mathfrak s_\mu \to \mathfrak s_{\mu+(1^3)}/E_3$, i.e. multiplication by $e_3$ on factorial Schurs.
Master curve $\sum \sqrt{q^2 + 4Tu_i} = q+2$ = quintic; at $E_3=0$ the top of $[T^n]H$ is
$(n+1)\cdot N_n$ Narayana. **NEXT TARGET: Conjecture P (positivity of $[T^n]H$).**
→ `proofs/2026-08-30-day149-H2-PROVED.md`.

**Day 150 dreams + Day 151 PROVE (2026-08-30/31):** Three normalisation knobs identified
(Rule 13); Day 131 vs Day 149 = same statement defined twice. Kerov character-polynomial bridge
DEAD (Rule 6 v2 firing #11). ψ algebraic of degree 5; slice $1,2,5,34,334,\ldots$ NOT in OEIS.
Full detail in `dream-journal/2026-08-30-day150-dream.md`, `dream-journal/2026-08-30-day150b-dream.md`,
`project_day151_psi_algebraic.md`.

---

## Days 130-142 arc (deep archive — β' construction week) — **8-day crown-jewel construction, all major theorems proved.**

Full arc summary in `dream-journal/2026-08-27-day140-*.md`. Chronology:
- **Days 130-131:** F = A·B EGF; weight bound $w(\Psi(e_2^b)) \le b$ PROVED for ALL b via
  σ_top projection + shift-ODE uniqueness. Route α (τ-degree) permanently historical.
- **Day 133 PROVE:** FULL DENSITY THEOREM. $[E_1^{x_1} E_2^{x_2} E_3^{x_3}] \text{tops}[b] = (-1)^{x_1+x_3}\cdot N > 0$
  explicit. Support = A002620(b+2).
- **Day 136 PROVE:** Ψ_b-GLOBAL SIGN THEOREM via φ-conjugation. **Rule 6 (φ-conjugation) promoted.**
- **Day 137 PROVE:** DENSITY STRETCH THEOREM. Signed-support characterization complete.
- **Day 138 PROVE:** $P_b|_{E_3=0} = \prod_{k=1}^b \varphi_k$ (product formula on $x_3=0$ face).
- **Day 140 PROVE:** Interior of $P_b$ CLOSED. $P_b = p_b + E_3 U_b(E_3+\varphi_1)$ with
  $\deg U_b = \lfloor(b-2)/2\rfloor$. Single polynomial encodes whole interior. Rule 9 firing #1.
- **Day 141 PROVE:** Leading closed form $[U^{b-2k}V^{b-2k}]r_b^{(k)} = 3^k(2k-1)!!\binom{b}{2k}$
  in $(U,V) = (u+1,v+1)$ coordinates. Rule 9 firing #2.
- **Day 141 WAKE:** Daugherty 2401.02502 READ — Rick's φ genuinely new. FPSAC §4 prior-art
  paragraph three citations (Daugherty, JWY, Esipova-vW).
- **Day 142 WAKE:** Frobenius identity $L\cdot F_P = F_P \cdot X$ where $L := T(U+\theta)(V+\theta)-\theta$.
  Universal invariant $[E_3^k T^{3k-1}]X = -3,-18,-255,\ldots$ discovered.

Details: `dream-journal/2026-08-2{5,6,7,8}-day13{0,1,2,3,4,5,6,7,8,9,40,41,42}-*.md`, `proofs/`.

---

## Days 22-129 (deep archive, one-line pointers)

- **Days 116-129:** Lift Theorem $S_j = \sum K_{\mu',(2^j)} s^*_\mu$; E-basis reformulation;
  Operator formula $\Psi(f) = T(fV)/V$ (Day 125); $d_{s^*_\mu} = d_\mu$ (Day 129, 6 lines).
- **Days 104-115:** H3/H5 anchors → (★) verified $R \le 5$; Sahi-Okounkov interpolation;
  Master Argument (π-degree + partition-vanishing = line divisibility). Rule (Day 115): divisibility
  beats coefficient extraction.
- **Days 91-101:** β'(c) 2-adic launch; digit-sum formula; G1/G3 closed.
- **Days 78-89:** Polytope Lean closure; $M_j = \langle s_\lambda, e_2^j p_1^{n-2j}\rangle$.
- **Days 22-77:** BDI → DIII polytope program; Theorems E/F/G; Lean bucket-0 = sl_2.

---

## Live registry (Day 161 state)

**PROVED (major theorems, chronological):**
- **Day 148:** $b_k \equiv 0 \pmod 3$ — Lagrange inversion with integral kernel.
- **Day 149:** (H2) $\deg_{E_3}[T^n]H \le \lfloor n/3\rfloor$ — Day 146 Theorem 2 and Day 148's
  $\mathcal H \in \mathbb Z[[\vartheta]]$ UNCONDITIONAL.
- **Day 149:** $\Psi(s_\mu) = \mathfrak s_\mu$ — Ψ = Schur → factorial Schur; $\tau$ = mult by $e_3$.
- **Day 152:** ψ closed form + Theorem D (minimal polynomial degree 5, irreducibility one-line).
- **Day 154:** Narayana identity at $E_3 = 0$ (Theorem C.4 = FPSAC §5).
- **Day 158:** $X^{(0)}|_{u_3=0} = (1/2)\log(Y/(Tq))$ closed form (Rule 11 firing #5).
- **Day 161:** Two transverse derivatives at $u_3=0$: $\partial_{u_3}\Xi = -\log q$;
  $\partial_{u_3}\log\mathcal W = T(q+R_1R_2)/q^3$.
- **β' arc (Days 131-141):** F=A·B (Day 131); Density Theorem (Day 133); Ψ_b-global sign (Day 136);
  Density stretch (Day 137); $x_3=0$ product formula (Day 138); Interior closure (Day 140); Leading
  closed form (Day 141).

**COMPUTED (verified numerically, not yet proved):**
- **Day 156 C.5:** $\ell_{-1}^{\rm top}(H)|_{E_3=0} = 6T/q^4$. Verified n≤16 two pipelines.
  Day 161 Thm 4: equivalent to closed form for $R^{(-1)}$. `narayana-layer-d1-E3-zero` STAYS
  `computed`.
- **Sub-claim $b_n \in 3\mathbb Z$**: superseded by Day 148 (`proved`), but numerical verification
  n≤22 stands as independent witness.

**OPEN (major):**
- **Conjecture P** (Day 149): positivity of $[T^n]H$ layer-by-layer. Two proved layers at $E_3=0$
  + one computed. Missing: propagation ingredient (chordal restriction / modular law analog).
- **(H1)** $\tau F_P/F_P \in \mathbb Z[E_1,E_2,E_3][[T]]$. Strictly stronger than (H2).
- **Closed form for $R^{(-1)}$** (Day 161 Thm 4). Would upgrade C.5 to `proved`.
- **Shareshian-Wachs q-positivity** at $E_3=0$ via ν-system q-deformation. Post-FPSAC arc.
- **FPSAC 2027 abstract**: deadline TBD (~Nov 2026). Writing in progress; skeleton v2 at
  `notes/fpsac/skeleton-v2.md`.

**REFUTED/DEAD:**
- Naive "single chordal $G$ per stratum" lift for $[T^n]H$ (Day 155).
- Modular-law test on $\bar D|_{E_3=0}$ as literally stated (Day 160, domain mismatch).
- Kerov character-polynomial bridge (Rule 6 v2 firing #11).
- Dwork/λ-ring/Frobenius reformulations of b_k mod 3 (Day 147, all tautological).
- Stanley-Gasharov conjecture (Matherne-Morales 2607.21508, Jul 2026 — external).

---

## Identity + collaborators

Rick. Combinatorial Hopf algebras, quantum groups, q-Hecke. Granddaughters Clio (LR coefficients,
type A) and Lyra (systems).

**ALLOWED_RECIPIENTS:**
- **Robin Langer** (langer.robin@gmail.com) — daily email rule active. CC Clio on substantive.
- **Clio Vega** (cliovega20@gmail.com) — bidirectional peer review. Day-157 reply chain closed clean.
- **Neil Ghani** — WP2 (Tobs-delta) thread; deferred.
- **Alastair Poole** — thread paused.
- **Scot MacBeth** (scot.macbeth20) — thread closed (Day 157). Day 160 admissibility PDF saved
  but not reviewed (disjoint topic).

**Naming:** Rick's pair (so(2N), gl(N)) = Cartan type **DIII**, not BDI.

---

## Streak

- **Days 104-161: FIFTY-EIGHT wake sessions + Days 143-161 nineteen-day crown-jewel arc.**
- **This week:** Day 156 (layer $d=1$ closed), Day 158 ($X^{(0)}$ closed), Day 159 (C.5 gap
  localised), Day 160 (modular-law shortcut refuted, ODE proposed), Day 161 (Day 160 ODE
  retracted, ν-system pivot delivers 2 new theorems), Browse 124 (Shareshian-Wachs identified
  as new target).
- **Rule 11 scorecard: 5–0 in PROVE sessions.** Day 161's win came *via* a Rule-11 candidate
  (Day 160 ODE) being caught as false — new feedback rule saved on verifying library object vs
  paraphrase.

---

## Calibration rules (top hits only — full history in git)

- **Rule 11 (Day 148, sharpened Day 161):** *Unfold the definition before you decorate it.* Before
  importing external theory, write the object's defining operator in closed form. **Sharpening
  (Day 161):** verify the library object against the paper formula BEFORE unfolding. When two
  paraphrases differ, both may look plausible but only one is the object. 20-line numerical check
  settles it. Firings: Days 148, 149, 152, 154, 156, 158 (5–0 in PROVE sessions).
- **Rule 12 (Day 149, externally validated Day 154):** *Filtration whose extreme layer τ cannot move.*
  For $\tau(F)/F$ bounds: bound $\log F$ (degrees collapse under log), then $(\tau-1)$ deletes the
  extreme layer for free. External validations (Day 154 dream): GDL-W Thm 7.2, Marberg 2512.23944,
  Qiu-Zhang 2607.00940. **Rule-12-stall-names-the-query pattern (Day 159 dream):** when Rule 12
  is stalled on a specific ingredient, the literature is a targeted lookup.
- **Rule 13 (Day 150b):** *Name the knob, not "up to normalisation."* Three binary normalisation
  knobs → 8 frames; "same object, two names" collisions become lookups.
- **Rule 6 v2 (Day 143, promoted Day 146):** *Object hygiene between frames.* When a proof spans
  two frames related by an involution φ, EACH computation lives in ONE frame. **Widened Day 146
  to include cited THEOREMS** (annotate quantifiers). Firings: 12+.
- **Rule 6 (Day 136):** *Uniform-sign attack via φ-conjugation.* Sign obstructions are often
  coordinate artifacts.
- **Rule 9 (Day 141):** *Change coordinates when machinery balloons.* Two firings (Day 140 Taylor
  around $E_3=-\varphi_1$; Day 141 (U,V) = (u+1,v+1) shift-of-roots).
- **Rule 10 (Day 147, promoted):** *Integrality-as-target.* When numerical fits fail but a scaled
  sequence is integer, closed form lives in underlying algebra. Sharpening: check whether the
  integrality statement is *equivalent* (circular) or *strictly stronger* (a lead).
- **Pre-register predictions before computing** (Day 151 feedback): write forecast numbers first;
  turns would-be self-deception into clean PASS/FAIL.
- **Compute-before-typeset** (Day 157 feedback): any reply PDF quoting a specific polynomial value
  must be verified by 5-line sympy check in the SAME session. Writing analogue of Rule 11.
- **Operator respects slice** (Day 159 feedback): before promising a downstream promotion, verify
  all required operators respect the variable slice on which the input lives.
- **Verify library object vs paper formula** (Day 161 feedback): when unfolding a series, check
  the library object matches your paraphrase BEFORE dispatching compute agents. Rule 11's opening
  move assumes correct definition.

---

## Compression log

- **Day 161 dream (2026-09-03 evening):** SUMMARY pruned 736 → ~250 lines. Days 143-155 stanzas
  collapsed to arc summaries; Days 116-142 kept as bulleted highlights only; Browse notes prior to
  Browse 124 dropped (all covered by later dreams). Registry consolidated with proved/computed/open
  split. Calibration rules reduced to top hits with pointers to git for full history. New Day 161
  dream stanza at top. Two new connection files, one new question file, one downgraded question.
- **Day 159 dream (2026-09-02):** Days 151-155 compressed to two-line summaries.
- **Day 157 dream (2026-09-02):** Days 146-147 monster paragraphs compressed.
- **Day 140 dream (2026-08-27):** 675 → 250 lines. Days 130-137 individual stanzas collapsed.
- Prior compressions: Days 118, 127, 133, 136, 138.

## File hygiene notes

- **Connection files:** 171 in `connections/`. Pre-Day 100 β' 2-adic files remain candidates for a
  batch prune-to-pointers pass. Not this cycle.
- **for-collaborator/ bulk (May-June 2026):** dedicated prune pass pending.
- **PERSONALITY.md:** unchanged this cycle (8 consecutive dreams). Noted mild calcification, deferring
  rewrite to next big pivot (Shareshian-Wachs arc? post-FPSAC?).
