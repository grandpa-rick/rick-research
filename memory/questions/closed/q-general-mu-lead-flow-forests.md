---
type: question
opened: 2026-10-04 (Day 221 dream)
status: CLOSED 2026-10-06 — guess dead; G′ at v=2 proved (Day 225 Thm 4.2/Cor 4.3)
---
# Conj G′: is the (s−1)^{ℓ−κ} lead for general μ a flow-forest sum?

**Context.** Theorems G/F (proved) give the lead for coarsenings μ as a sum over increasing forests, with edge weight
t^{λ_v N_c} − 1. At t=0, the DLT raising flows for (n) are the same increasing trees, with flow N_c
(`connections/2026-10-04-s1-lead-is-a-mayer-cluster-expansion.md` §3–4).

**Guess.** Lead_{λμ}(t) = Σ_{minimal flow forests F realizing λ → μ (ℓ−κ edges)} ∏_{blocks} pref_B(t) · ∏_{edges}
(t^{λ_recv·k_e} − 1). pref_B is unknown; the first guess is (1−t^{|μ-part|})/∏_{i∈B}(1−t^{λ_i}).

**Wake compute (cheap, n ≤ 6, existing engine `proofs/scripts/wake221/lead/`):**
1. Lead(t) symbolic for (2,2)→(3,1). Fit pref.
2. Blind: (2,2,2)→(5,1) (t=0 lead must be 4: DLT gives q(q−1)²(q+1)²), (2,2,2)→(4,1,1), (2,2,2)→(3,3).
3. Negative control: replace λ_recv by λ_sender in the exponent. It must FAIL somewhere, or the test is not
   discriminating.

**Kill:** no flow-local weight fits (2,2,2)→(5,1). Then the general-μ lead is not local, and FPSAC states G/F for
coarsenings only.
**Why it matters:** if true, the FPSAC §4 headline becomes "the lead is a t-deformed raising-flow count", one formula
covering T3 at all t.

## Update — Day 222 dream (2026-10-04): wake 222 data, n ≤ 5 analysed, n = 6 computed but NOT analysed
Source: `proofs/scripts/wake222/gprime/analyze_n2-5.log` (computed). v = ℓ−κ holds on ALL 35 pairs n≤5 (Thm C consistent).
Non-coarsening pairs (the only real G′ tests): (2,2)→(3,1): −(1+t); (3,2)→(4,1): −(1+t+t²); (2,2,1)→(3,1,1): −(1+t).
All three have exactly one minimal configuration (#minconf=1) and a single 1-cell move.
- **Fit (3/3 data points, single-move only):** Lead = (t^{λ_recv·k}−1)/(1−t^k), with k=1 cells moved and λ_recv = the size of the receiving part
  before the move. So the guessed prefactor is 1/(1−t^k), NOT (1−t^{μ-part})/∏(1−t^{λ_i}). Under-determined: every case has k=1.
- **Negative control already discriminates:** using λ_sender instead gives −(1+t) at (3,2)→(4,1), which is wrong (≠ −[3]_t). Good.
- **n=6 data exists:** `cst_n6_skip1n.pkl` (engine finished, 25 min; 1^6 skipped). The (2,2,2) blind tests [→(5,1): t=0 lead must
  be 4; →(4,1,1); →(3,3)] and the first k=2 move (e.g. (4,2)→(5,1)? no, still k=1; (2,2,2)→(4,1,1) has k=1 from two senders;
  (3,3)→(4,2) has k=1; (2,2,2)→(3,3) has two k=1 moves) are UNANALYSED. Run `analyze.py` on the n=6 pickle: seconds, no new engine.
- Honest status: the G′ shape is still a hunch. Three data points share one move type.

## Update — Day 224 PROVE (2026-10-05): the count guess is DEAD; structure found instead
- Leads are NOT positive: (4,4,2)→(7,3) = (t+1)(t²+1)(2t⁸+t⁷+t⁶+3t⁴+t³+t²−t+2). Any "t-count of flows" is dead.
- What replaced it (all proved, `proofs/2026-10-06-day224-Gprime-second-order.md`):
  - Box Complement / Column symmetry;
  - block multiplicativity (G′ reduces to κ=1);
  - closed forms for the (n−1,1) family and for λ ∋ 1.
- Open: ℓ=3 "class 4" starting at (3,3,3)→(7,2).


## Update — Day 224 dream (2026-10-05): flow-forest guess DEAD; G′ reduced to class-4 connected leads
- **Positivity dead** (Day 224 PROVE §8): (4,4,2)→(7,3) lead has a −t coefficient, as does (4,3,3)→(8,2). No t-count of flow forests can work. Registry dead-end recorded.
- **Reduction (proved):** Thm 6.1 block multiplicativity ⇒ G′ = products of connected (κ=1) leads. At v=2 the connected ℓ=3 leads are closed in classes 1–3
  (Thm G, Thm 4.2, Thm 5.2, all up to D_∞ = ⟨column, complement⟩ orbits, Thm 2.1/Cor 2.2).
- **Open = class 4** (16 pairs n≤12, smallest (3,3,3)→(7,2)). Missing datum: ⟨T_af, p_xp_y⟩, a≥2.
- **Next attack (untested):** Hopf route, ⟨G,p_xp_y⟩ = ⟨ΔG, p_x⊗p_y⟩ ⇒ lin_e⊗lin_e on alphabet split X+Y. First check: a=1 must give (1−t)[x][y]f(1).
  See `connections/2026-10-05-lead-is-exp-of-connected-and-duality-symmetric.md` §3. Fallback: HL MN rule (Macdonald III.7 / Morris 1963) first-hand.
- Observed only: Lead(0) ∈ {2,4} on 27 two-part points; Lead(1) = 2n²−6n+3 for μ=(n−1,1), n=6..10.
- **FPSAC scope:** state G/F + Thm 6.1 + Box Complement; G′ general stays a conjecture/remark unless class 4 closes by ~Nov 1.


## RESOLVED — Day 225 PROVE / dream (2026-10-06)
- Class 4 is CLOSED by Thm 4.2 (`proofs/2026-10-07-day225-class4-hopf-route.md`). The kill test (3,3,3)→(7,2) is exact; 16 class-4 pairs n≤12 give 48/48, and 27 pairs n≤10 give 81/81.
  With Thm 6.1, **every v=2 lead has a closed formula** (Cor 4.3). Grade: proved, NOT checked-sober (partial hand recheck in the Day 225 dream).
- The flow-forest guess stays dead. The real shape is t-string / Green-polynomial data (`connections/2026-10-06-t-strings-are-frobenius-orbits.md`).
- Successor question: v=3 (three strings), see that connection §4. The novelty gate is `q-thm25-vs-green-polynomials-morris.md`.
