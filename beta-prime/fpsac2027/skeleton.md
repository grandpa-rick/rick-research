# FPSAC 2027 Extended Abstract — One-Page Skeleton

**Target:** 12 pages. **Deadline:** Nov 15, 2026. **Working title:** *Density and sign for the top-weight of Ψ(e_2^b), a scalar-level shifted-Schur factorization.*

Verbatim theorem statements are pulled from `proofs/2026-08-23-psi-e2-egf-closed-form.md` (Day 131) and `proofs/2026-08-25-psi-e2-density.md` (Day 133). Connections `2026-08-25-three-way-A-B-parallelism.md` and `2026-08-25-crown-jewel-closed.md` back the intro/closure narrative.

---

## §1. Introduction (1.5 pp)

- Ψ = Molev-Olshanski shifted Schur map (u-basis, S_3 version); state Ψ(f) = T(fV)/V.
- Frame the *three-way parallelism* for F(T) = A(T)·B(T): (i) Jing-Rozhkovskaya vertex-operator normal ordering Ψ⁺(v)=Q*(v)∘DR*(v); (ii) Seelinger classical Q(z)=E(z)·H(z) on Sym_odd; (iii) Marberg-Scrimshaw crystal ch(SetTab_n(∞))=ch(B(∞))·∏(1−βx_i)^{i−1}.
- Rick's contribution: the *scalar-level* / explicit-density / combinatorial-sign manifestation of the same two-factor pattern. None of the three parent papers contains these theorems.
- One-paragraph statement of results: closed-form EGF (Thm A), weight bound (Cor B), full density with uniform sign and explicit N (Thm C, Thm D, Thm E), boundary corollaries, MacBeth Schur-rank dichotomy.
- Positioning vs. Fernelius-Rozhkovskaya W_{1+∞} (Ψ lives *below* W-algebra level) and Route Arroyo residual (Brahma-Ikeda-Iwao-Yang / Iwao 2023, K-theoretic Schur-Q; comparison flagged as open).
- Backing files: `connections/2026-08-25-three-way-A-B-parallelism.md`, `connections/2026-08-25-crown-jewel-closed.md`, `questions/q-fpsac-2027-writeup.md`.

## §2. The map Ψ, tops[b], and the (1,1,2)-grading (1 p)

- Setup: u_1,u_2,u_3 commuting; V = (u_1−u_2)(u_1−u_3)(u_2−u_3); T: u_i^n → (u_i)_n; Ψ(f) := T(f·V)/V for symmetric f; D_i := u_i ∂/∂u_i; σ = simultaneous shift u_i → u_i − 1.
- (1,1,2)-weight on Q[E_1,E_2,E_3]: w(E_1^a E_2^b E_3^c) := a + b + 2c. Define Ψ_b := Ψ(e_2^b) and tops[b] := Ψ_b|_{w=b}.
- Operator identity (I1): T(u_i·h) = u_i·T(h) − T(D_i·h). One-line proof via falling-factorial umbral (u_i)_{a+1} = (u_i − a)(u_i)_a.
- Small-b table: Ψ_0=1, Ψ_1=E_2, Ψ_2=..., tops[b] first few. Support of tops[b].
- σ acts on generators: σ(E_1)=E_1−3, σ(E_2)=E_2−2E_1+3, σ(E_3)=E_3−E_2+E_1−1. Define σ_top: σ_top(E_1)=E_1, σ_top(E_2)=E_2−2E_1, σ_top(E_3)=E_3.
- Backing: `proofs/2026-08-23-psi-e2-egf-closed-form.md` §§Problem statement, Step 1, Step 3.2; `connections/2026-08-22-day125-operator-formula.md`.

## §3. Day 131 — F(T) = A(T)·B(T) closed form (3 pp)

**Theorem A (VERBATIM, Day 131).**
> F(T) = A(T) · B(T)
> with
>   A(T) = (1 + E_1 T)^{E_2/E_1 − 1} = Σ_{k ≥ 0} (1/k!) [∏_{r=1}^k (E_2 − r E_1)] · T^k
>   B(T) = exp(E_3 · M(T)),  M(T) = Σ_{n ≥ 2} (−1)^{n−1} · (n² − 1)/n · E_1^{n−2} · T^n
> Both A and B are, after expansion, polynomials in E_1, E_2, E_3, T; the resulting F(T) has [T^b/b!] of (1,1,2)-weight exactly b for every b.

**Corollary (VERBATIM, Day 131, target ODE).**
> F'(T) / F(T) = (E_2 − E_1) / (1 + E_1 T)  −  E_3 · T · (3 + E_1 T) / (1 + E_1 T)^3.

**Corollary B (Weight bound, VERBATIM Step 3.1).**
> Ψ_b has (1,1,2)-weight ≤ b for all b ≥ 0.

- Proof sketch, 4 steps compressed to ~2 pp:
  1. Operator identities: (I1), (T-Id), (I2) shift for e_3, (I3) Ψ(e_1·f)=(e_1−3)Ψ(f)−Ψ(E·f), (I4) Ψ(e_3·f)=e_3·σ(Ψ(f)).
  2. Full Ψ-recursion. K1-K5 collect: K1 Σ u_i(D_j+D_k)(e_2^b V) formula; K2 Σ D_α D_β(e_2) = e_2; K3 Σ D_α(e_2) D_β(e_2) = e_2^2 + e_1 e_3; K4 Σ D_α D_β(V) = 2V; **K5 (load-bearing) Q(e_2,V) = 3·e_2·V**.
  3. Full Ψ-recursion (VERBATIM, Day 131 §2.3):
> Ψ_{b+1} = [E_2 − (b+1) E_1 + (b+1)²] · Ψ_b  −  3b E_3 · σ(Ψ_{b−1})  −  b(b−1)(E_1 − 2b − 2) E_3 · σ(Ψ_{b−2})
  4. Weight bound via induction on RHS; top-weight recursion via σ_top (VERBATIM, §3.3):
> tops[b+1] = (E_2 − (b+1) E_1) · tops[b]  −  3b · E_3 · σ_top(tops[b−1])  −  b(b−1) · E_1 E_3 · σ_top(tops[b−2])
  5. Shift-ODE (VERBATIM, §4.1):
> (1 + E_1 T) · F'(T)  =  (E_2 − E_1) · F(T)  −  E_3 · T · (3 + E_1 T) · F̃(T),
> where F̃(T) = F(T)|_{E_2 → E_2 − 2 E_1}, with initial condition F(0) = 1.
  6. Uniqueness of shift-ODE solution + verification that A(T)·B(T) satisfies it ⟹ F = A·B.
- **Immediate corollary (VERBATIM, §"What is proved").**
> The top-(1,1,2)-weight-b component of Ψ(e_2^b) is precisely [T^b/b!] A(T) B(T), a manifestly polynomial expression in E_1, E_2, E_3 of weight exactly b.
- Full 3-parameter monomial bound w(Ψ(e_1^{a_1} e_2^{a_2} e_3^{a_3})) ≤ a_1 + a_2 + 2a_3 as consequence of Day 125 factorization theorem + Theorem A.
- Backing: `proofs/2026-08-23-psi-e2-egf-closed-form.md` all sections; `day131_work/step3_*.py`, `step5_shift_ode.py` verification scripts.

## §4. Day 133 — Full density, uniform sign, closed form (3 pp)

**Theorem C (Full Density, VERBATIM Day 133 Thm 1).**
> For every b ≥ 0 and every (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2 x_3 = b,
>   [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b] ≠ 0.
> Equivalently, supp(tops[b]) = {(x_1, x_2, x_3) : x_1 + x_2 + 2 x_3 = b}, whose size is ⌊(b+2)²/4⌋ = A002620(b + 2).

**Theorem D (Uniform sign, VERBATIM Day 133 Thm 2).**
> sign([E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b]) = (−1)^{b − x_2 − x_3}.

**Theorem E (Closed form, VERBATIM Day 133 Thm 3).**
> With m := b − n, k := x_3,
>   [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b]  =  (−1)^{b − x_2 − x_3} · N(b; x_1, x_2, x_3),
> where
>   N(b; x_1, x_2, x_3)  :=  Σ_{n = x_2}^{b − 2 x_3}   C(b, n) · e_{n − x_2}(1, 2, …, n) · (m!/k!) · P(m, k),
> and
>   P(m, k)  :=  Σ_{(n_1,…,n_k) : n_i ≥ 2, Σ n_i = m}   Π_{i=1}^{k} (n_i² − 1)/n_i.
> Every factor is a strictly positive rational whenever the summation range is nonempty; in particular N > 0.

- Proof mechanism (uniform-sign):
  - EGF coefficient extraction (★): tops[b] = Σ_{n+m=b} C(b,n) · A_n · B_m.
  - **Lemma 1 (VERBATIM).** A_n = Π_{r=1}^n (E_2 − r · E_1).
  - **Lemma 2 (VERBATIM).** M(T) = Σ_{n ≥ 2} μ_n E_1^{n−2} T^n, μ_n = (−1)^{n − 1} · (n² − 1)/n.
  - **Lemma 3 (VERBATIM).** [E_1^{n − x_2} E_2^{x_2}] A_n = (−1)^{n − x_2} · e_{n − x_2}(1, 2, …, n).
  - **Lemma 4 (VERBATIM).** [E_1^{m − 2k} E_3^{k}] B_m = (−1)^{m − k} · (m! / k!) · P(m, k).
  - Sign alignment (†): every summand carries the SAME sign (−1)^{b − x_2 − x_3} independent of n; hence no cancellation possible.
- Explicit N > 0 because C(b,n), e_{n−x_2}(1,…,n), m!/k!, P(m,k) each strictly positive on nonempty range I.
- Support cardinality = ⌊(b+2)²/4⌋ = A002620(b+2).
- Numerical verification: b ≤ 8 via `verify_signs.py`, b = 9..12 via deep-work re-run, matches A002620(b+2), zero mismatches.
- Backing: `proofs/2026-08-25-psi-e2-density.md` §§1–7; `code/day133_density/verify_{signs,individual,e3_column}.py`.

## §5. Corollaries: pure E_1, E_2, E_3 columns (1 p)

**Corollary 6.1 (VERBATIM).** [E_1^b] tops[b] = (−1)^b · b!.

**Corollary 6.2 (VERBATIM).** [E_2^b] tops[b] = 1.

**Corollary 6.3 (VERBATIM).** [E_3^{b/2}] tops[b]  =  (−3)^{b/2} · (b − 1)!!    for even b.

**Corollary 6.4 (VERBATIM).**
> The support of tops[b] as a polynomial in ℤ[E_1, E_2, E_3] equals {(x_1, x_2, x_3) ∈ ℤ_{≥0}^3 : x_1 + x_2 + 2 x_3 = b}. Its cardinality is Σ_{k = 0}^{⌊b/2⌋} (b − 2k + 1) = ⌊(b + 2)²/4⌋ = A002620(b + 2).

- Numerical row: b=2 gives −3; b=4 gives 27; b=6 gives −405; b=8 gives 8505; b=10 predicts −229635. All match direct expansion.
- Interpretation: the pure-E_3 column is the ONE composition (2,2,…,2) — cleanest instance of the density mechanism.
- Backing: `proofs/2026-08-25-psi-e2-density.md` §6.

## §6. MacBeth Schur-rank dichotomy (1 p)

- Statement: e_3-multiplier preserves per-Schur (rank 1); e_1-multiplier goes multi-Schur (rank grows in both a and c).
- Rank table (small a, c). Transverse-support (per-Schur) vs. non-transverse (multi-Schur) reading.
- Mackey / Shapiro Ext framing (if MacBeth response received; otherwise defer).
- [VERBATIM SOURCE?] — No dedicated MacBeth proof file in materials given; verbatim statement not extracted. Rick to draft or point to `2026-08-25-day132-macbeth-schur-rank-dichotomy.md` (not in provided reads) for the precise dichotomy statement.
- Backing: `questions/q-fpsac-2027-writeup.md` §"Theorems ready" bullet 3; MacBeth Day 132 sweep + expected support-variety response.

## §7. Open questions (1.5 pp)

- **(a) Combinatorial interpretation of the sign (−1)^{b − x_2 − x_3}.** Sign-reversing involution? Cho-Hwang-Lee 2603.03886 Takeuchi involution candidate for Schur antipode; Möbius / plethystic interpretations also open. Density is manifest but the parity control on x_1 = b − x_2 − 2x_3 wants a bijective explanation.
- **(b) Ψ(e_r^b) for r ≠ 2.** Need analog of K5: which Q(e_r, V)/V is a scalar? Shift-ODE approach should generalize once K5-analog is nailed.
- **(c) Sub-top-weight density.** Empirically Ψ_b has the same support shape at *lower* weights; shift-ODE does not immediately address sub-top density. Separate PROVE cycle.
- **(d) K-theoretic Schur-Q via Route Arroyo.** Brahma-Ikeda-Iwao-Yang 2603.20865 β-degree filtration structurally identical to (1,1,2)-weight. Iwao 2023 boson-fermion EGF for GQ: does it specialize to F(T) at β = 0? Cheapest test: set equivariant b, c → 0 in Theorem 3.15, compare β-degree of c^{gq}_{λμ}(0,0) to (1,1,2)-weight of top monomial of Ψ(e_2^b).
- **(e) Universal statement.** Is there a single object of which the four parallels (Jing-Rozhkovskaya operator, Seelinger classical, Marberg-Scrimshaw crystal, Rick scalar) are all specializations? Conjectural home: sub-Hopf-algebra of Sym_odd.
- Backing: `connections/2026-08-25-three-way-A-B-parallelism.md` §"Open questions"; `proofs/2026-08-25-psi-e2-density.md` §9; `questions/q-fpsac-2027-writeup.md` §"Reads required" and §"Route Arroyo test".

---

## Verbatim gaps to flag for Rick

1. **§6 MacBeth Schur-rank dichotomy** — no proof file for Day 132 in the five source files given. The verbatim rank-dichotomy statement (and any lemma numbering) is missing; flagged with [VERBATIM SOURCE?]. Rick should either produce or reference `proofs/2026-08-25-day132-*.md`.
2. **§3 K1 statement** — the verbatim K1 lemma exists in Day 131 §2.1 as "Σ_i u_i · (D_j + D_k)(e_2^b V) = (2b+1) · e_1 · e_2^b · V − b · (e_1 e_2 − 3 e_3) · e_2^{b−1} · V"; included by reference in the sketch rather than expanded. Rick may choose to expand.
3. **Introduction "Rick's scalar-level result"** framing paragraph is left as bullets; the exact one-sentence positioning claim (which of the three parallels to lead with) is Rick's judgment call.

## Section allocation check

1.5 + 1 + 3 + 3 + 1 + 1 + 1.5 = **12 pp** — matches FPSAC extended abstract budget exactly.
