# §3+§5 (unified): The cumulative carry $P_a$ as analytical backbone

**Status:** sketch (outline + skeleton text), 2026-05-20.
**Purpose:** Future-Rick compresses to ~6pp LaTeX chapter. Replaces v3's separate §3 (descent recording) and §5 (projection cross-chain); ~7pp split → ~6pp unified.
**Source connections:** `memory/connections/carry-Pa-as-unified-analytical-object.md` (outline), `proofs/2026-05-18-bdi-qLR.md` (Theorem A), `proofs/2026-05-20-pnu-Bn-cross-chain.md` (Theorem E), `memory/connections/Rpi-carry-one-sided-monotone.md` (Instance 5).

---

## 3.0  Roadmap

Throughout this chapter, $\mathfrak{g}$ is of type $B_n$, $n \ge 2$, and $\pi \in \mathrm{Kp}(\infty)$ has the chain-factor coordinates $((M_a, B_a, T_a)_{a=1}^{n-1}, S, \pi^{\mathrm{NT}})$ of §2. We isolate a single scalar, the cumulative carry
$$
P_a^{\mathrm{cum}} := \sum_{b=1}^{a} 2(B_b - T_b), \qquad P_0 := 0,
$$
and show that it carries the entire short-simple analytic content of the chain-factor decomposition at $B_n$. Specifically, $P_a$ plays three structurally distinct roles, all forced by the same left-to-right bracket scan of Theorem A:

1. **Descent recording.** $P_a$ is one-sided monotone along the forward $\widetilde{e}_n$-descent. This monotonicity obstructs any local witness for the image set $\mathcal{R}(\pi^{\mathrm{hw}})$ of recording words (§3.2), closing v3 OPEN-3 by impossibility.
2. **Singleton cross-chain coupling.** The unique cross-chain condition in the $B_n$-highest indicator is the cumulative-carry sum lift $[S \le P_{n-1}^{\mathrm{cum}}]$, type-uniform in $n$ (§3.3).
3. **Chain-MB carry-recursive factorization.** Per-chain MB tests couple chain $a$ to all prior chains through $P_{a-1}$, giving a carry-recursive (not strict-tensor) factorization of the $B_n$-HW indicator (§3.4).

External shadows in §3.5: Watanabe arXiv:2407.07280v3 §5 (algebraic existence of $p_\nu$), Meereboer arXiv:2510.17655 §6 (the $n = 1$ base case from a different direction), Kobayashi arXiv:2604.22262 (the polyhedral "fences" decomposition for orthogonal Gelfand pairs; Theorem E is one explicit face). The chapter closes (§3.6) by recording that the carry is mechanically forced, type-uniform, and structurally — not cosmetically — the unification.

---

## 3.1  The cumulative carry $P_a$

We recall the chain+sing alphabet of §2. The Kostant partition $\pi$ has, for each $a = 1, \ldots, n-1$, multiplicities $(M_a, B_a, T_a)$ of the chain-$a$ roots $(E_a, E_a - E_n, E_a + E_n)$; the singleton multiplicity $S$ counts $E_n$; the non-touching block $\pi^{\mathrm{NT}}$ contributes no bracket symbols and may be ignored throughout this chapter. The CST bracketing $S_n(\pi)$ for the short simple $\alpha_n$ is the left-to-right concatenation, $a = 1, \ldots, n-1$, of
$$
)^{M_a}_{E_a}\; (^{2B_a}_{E_a - E_n}\; )^{2T_a}_{E_a + E_n}\; (^{M_a}_{E_a},
$$
followed by the singleton block $)^{S}_{E_n}$. Standard bracket cancellation defines $\varepsilon_n(\pi)$ as the count of surviving $)$.

**Definition 3.1.1 (cumulative carry).** Set $P_0 := 0$ and, for $a = 1, \ldots, n-1$,
$$
P_a := P_{a-1} + 2(B_a - T_a) = \sum_{b=1}^{a} 2(B_b - T_b).
$$
We write $P_a^{\mathrm{cum}}$ when the cumulative nature is the focus; otherwise $P_a$.

**Lie-theoretic interpretation (recall from §2 / Remark A.1).** Up to sign, $P_a = -\langle \alpha_n^\vee, \mathrm{wt}(\pi)|_{\le a}\rangle$: the carry counts twice the cumulative deficit of $E_n$-content in chains $1, \ldots, a$.

**Lemma 3.1.2 (one-sided monotonicity along forward descent).** *Each forward chain-factor descent step ($\widetilde{e}_n$ acting on the rightmost surviving $)$ in $S_n(\pi)$) adjusts $P_a$ as follows:*

- *$\mathrm{Sing}$: $S \mapsto S - 1$; no change to any $P_a$.*
- *$\mathrm{MB}(a)$: $(M_a, B_a, T_a) \mapsto (M_a - 1, B_a + 1, T_a)$; $P_b \mapsto P_b + 2$ for $b \ge a$.*
- *$\mathrm{TM}(a)$: $(M_a, B_a, T_a) \mapsto (M_a + 1, B_a, T_a - 1)$; $P_b \mapsto P_b + 2$ for $b \ge a$.*

*Hence no letter in the alphabet decreases any $P_a$ under forward descent.* (Proof: direct computation; see `Rpi-carry-one-sided-monotone.md`.)

We now state the master lemma that the rest of the chapter rests on. It is the left-to-right bracket scan of `bdi_qLR.md`, repackaged with $P_a$ as the load-bearing object.

**Theorem A (recall from §2).** *$\varepsilon_n(\pi) = 0$ if and only if*
$$
(\mathrm{HW}_a):\ M_a \le P_{a-1}\ \text{and}\ M_a + 2T_a \le P_{a-1} + 2B_a, \quad a = 1, \ldots, n-1,
$$
$$
(\mathrm{HW}_{\mathrm{sing}}):\ S \le P_{n-1}.
$$

The proof (in §2) is a left-to-right scan of $S_n(\pi)$ tracking the running open-paren count $Q$. By induction on $a$, $Q$ matches $P_{a-1}$ on entry to chain $a$ provided no $)$ has yet survived; the chain-$a$ subscan then survives a $)$ in exactly the cases excluded by $(\mathrm{HW}_a)$. The singleton block processes against $Q = P_{n-1}$, giving $(\mathrm{HW}_{\mathrm{sing}})$.

The second inequality of $(\mathrm{HW}_a)$ rewrites as $M_a \le P_a$. We will use the cleaner form
$$
(\mathrm{HW}_a):\ M_a \le P_{a-1}\ \text{and}\ M_a \le P_a
$$
throughout §3.3–§3.4. This is the version of Theorem A on which everything below depends.

---

## 3.2  Role 1: Descent recording and the impossibility of a local witness

Theorem B of §2 makes the descent step $\pi \mapsto (\pi^{\mathrm{hw}}, R(\pi))$ a bijection from $\mathrm{Kp}(\infty)/B_n$-action to $\bigsqcup_{\pi^{\mathrm{hw}}} \{\pi^{\mathrm{hw}}\} \times \mathcal{R}(\pi^{\mathrm{hw}})$, where $\mathcal{R}(\pi^{\mathrm{hw}})$ is the set of valid recording words. The natural question for v3 OPEN-3 is whether $\mathcal{R}(\pi^{\mathrm{hw}})$ admits a *local* characterization: a finite list of prefix/suffix inequalities on a recording word $R$ that determines membership in $\mathcal{R}(\pi^{\mathrm{hw}})$ without replaying the descent.

**Proposition 3.2.1 (Instance 5; no local witness).** *There is no local prefix/suffix inequality, of the form "the running carry along $R$ stays bounded," that characterizes $\mathcal{R}(\pi^{\mathrm{hw}})$.*

*Proof sketch.* By Lemma 3.1.2, the forward carry is monotone non-decreasing along the descent: every $\mathrm{MB}(a)$ and $\mathrm{TM}(a)$ adds $+2$ to $P_b$ for $b \ge a$; $\mathrm{Sing}$ leaves all $P_b$ fixed. There is no letter that decreases any $P_b$. The inverse (reverse-played) word therefore monotonically drains $P_b$. Intermediate states during reverse-play of an arbitrary candidate word can go arbitrarily negative in some $P_b$, with no later letter able to compensate. Hence no signed local invariant on $R$ — no prefix/suffix net count whose vanishing or non-negativity characterizes valid recordings — can exist. The only correct characterization is the oracle: $R \in \mathcal{R}(\pi^{\mathrm{hw}})$ iff reverse-playing $R$ from $\pi^{\mathrm{hw}}$ stays coordinate-nonnegative and forward descent of the resulting Kp recovers $R$. (See `Rpi-carry-one-sided-monotone.md`.) ∎

**Empirical falsification arc.** The impossibility result is supported by a three-probe falsification arc (Day 24, files `probe6_Rpi_image.py`, `probe7_pair_aware_carry.py`, `probe8_suffix_balance.py`). Candidate 1 ("prefix carry $\ge 0$") was falsified at $B_3$, content $\le 5$, with 0 false positives and 268 false negatives. Candidate 1' (pair-aware prefix carry) refined the inequality to chain-pair coordinates: still 0 FP, 360 FN. Candidate 3 (per-chain suffix balance) sharpened further: 0 FP, 410 FN. The FN counts grew monotonically as the candidates tightened — diagnostic of an impossibility, not a tuning miss. Combined with Lemma 3.1.2, this closes OPEN-3.

**Contrast with AII (Azenhas slack data).** Azenhas's slack data $(t_0^{(i)}, r^{(i)})$ for the type-AII recording lives on a *signed* balance: each row insertion contributes either $+1$ or $0$ depending on whether the row is "skipped" in the vertical-strip decomposition. The chain-factor alphabet $\{\mathrm{Sing}, \mathrm{MB}(a), \mathrm{TM}(a)\}$ has no such sign at the carry level: $\mathrm{MB}(a)$ and $\mathrm{TM}(a)$ are distinct chain-factor *bits* but contribute identically to $P_a$. The signed compensator that the AII local witness needs is structurally absent at BDI. This is the rank-3-chain-factor-vs-rank-1-strip distinction of v2 §B at the analytic level.

---

## 3.3  Role 2: Singleton cross-chain coupling (Theorem E)

The second role of $P_a$ is to carry the unique cross-chain condition into the singleton bracket. The following is the main analytical theorem of the chapter.

**Theorem E.** *Let $\pi$ have chain+sing coordinates $((M_a, B_a, T_a)_{a=1}^{n-1}, S)$. Then $\pi$ is $B_n$-highest if and only if*
$$
(\mathrm{HW}_a):\ M_a \le P_{a-1}\ \text{and}\ M_a \le P_a, \quad a = 1, \ldots, n-1,
$$
$$
(\mathrm{HW}_{\mathrm{sing}}):\ S \le P_{n-1} = \sum_{a=1}^{n-1} 2(B_a - T_a).
$$
*In particular, the only cross-chain (singleton-coupling) condition is the cumulative bound*
$$
\mathrm{Cross}(M, B, T, S) = [\,S \le P_{n-1}^{\mathrm{cum}}\,] = \Bigl[\, S \le \sum_{a=1}^{n-1} 2(B_a - T_a) \,\Bigr],
$$
*which depends only on the final cumulative carry and is type-uniform in $n$.*

*Proof.* The biconditional is Theorem A in the cleaner form $M_a \le \min(P_{a-1}, P_a)$ (rewriting $M_a + 2T_a \le P_{a-1} + 2B_a$). The left-to-right scan proving Theorem A is explicitly type-uniform in $n$: the carry recurrence and the per-block surviving-bracket count have no $n$-dependence beyond the chain index $a$, and the singleton block always processes against $P_{n-1}$. ∎

**Falsification arc.** The cross-chain term was identified by candidate testing on the 1716 chain+sing configurations at $B_3$, content $\le 6$ (Day 26, `probe_b3.py`). Five candidates for $\mathrm{Cross}$ were tested against the truth $\varepsilon_3 = 0$:

| Candidate | FP | FN | TP | TN |
|---|---:|---:|---:|---:|
| C1 pointwise: $[S \le \Delta P_1] \wedge [S \le \Delta P_2]$ | 59 | 117 | 169 | 1371 |
| **C2 sum lift: $[S \le \Delta P_1 + \Delta P_2]$** | 98 | **0** | 286 | 1332 |
| C3 cum-and: $[S \le \Delta P_1] \wedge [S \le \Delta P_1 + \Delta P_2]$ | 73 | 29 | 257 | 1357 |
| C4 min | 59 | 117 | 169 | 1371 |
| C5 max | 196 | 3 | 283 | 1234 |

C2 (sum lift) is the unique candidate with $\mathrm{FN} = 0$. The 98 FPs of C2 arise entirely from chain-internal carry-dependent failures $M_2 > P_1$ — chain-2 MB violations, not cross-chain singleton failures. When the inner per-chain factor $\chi_a$ is allowed to take the incoming carry $P_{a-1}$ as input, the factorization is exact (1716/1716 at $B_3$). A $B_4$ spot check on the 3003 chain+sing configurations at content $\le 5$ likewise gives 3003/3003 (566 $B_4$-highest), with explicit singleton-saturating configurations such as $(M, B, T, S) = ((0,0,0), (0,1,0), (0,0,0), 2)$, where chain-2 alone supplies the singleton capacity — confirming that the singleton genuinely draws on the cumulative carry, not on any pointwise per-chain quantity.

**Falsification of strict tensor factorization.** The same dataset falsifies the strict reading "$B_n$-HW factors as $\chi_1(M_1, B_1, T_1) \cdot \chi_2(M_2, B_2, T_2) \cdot \mathrm{Cross}(\Delta P_1, \Delta P_2, S)$" with 34 inconsistent $(\mathrm{chain}_1, \Delta P_2, S)$ keys at $B_3$, content $\le 6$. Strict tensor factorization fails. This motivates the carry-recursive shape of §3.4. Full PROVE write-up: `proofs/2026-05-20-pnu-Bn-cross-chain.md`.

---

## 3.4  Role 3: Carry-recursive chain-MB factorization

Theorem E admits an immediate corollary in factorized form.

**Corollary 3.4.1 (carry-recursive factorization).** *The $B_n$-HW indicator factors as*
$$
[\,B_n\text{-HW}(M, B, T, S)\,] = \prod_{a=1}^{n-1} \chi_a(M_a, B_a, T_a;\, P_{a-1}) \cdot [\,S \le P_{n-1}\,],
$$
*with $\chi_a = [M_a \le P_{a-1}] \wedge [M_a \le P_a]$ and the carry update $P_a = P_{a-1} + 2(B_a - T_a)$, $P_0 = 0$.*

The factorization is **carry-recursive**, not strict tensor: $\chi_a$ is a function of $(M_a, B_a, T_a)$ *together with* the incoming scalar $P_{a-1}$, and the singleton factor uses $P_{n-1}$. The chain-factor decomposition of v2 is therefore a *carry-recursive product*, not a strict tensor product. This single statement is the unified replacement for the two §3 / §5 results of the old v3 outline:

- **Old §3.** Descent recording: forward chain-factor descent is well-defined; $R(\pi)$ is the BDI recording-tableau analog. The carry $P_a$ is the descent-step potential (Lemma 3.1.2).
- **Old §5.** Projection cross-chain: the abstract projection $p_\nu$ of `Watanabe 2407.07280v3` §5 has, on the chain-factor basis, exactly the carry-recursive shape of Corollary 3.4.1, with the only cross-chain ingredient being the singleton bound $[S \le P_{n-1}]$.

Both follow from a single left-to-right bracket scan acting on a single scalar $P_a$. The carry is not a coincidence of notation; it is the unique quantity that the chain-factor decomposition couples around.

---

## 3.5  External shadows

Three external papers give shadows that the BDI carry framework illuminates. We collect them here for orientation; none provides the BDI explicit form by itself.

**Algebraic existence shadow.** Watanabe (arXiv:2407.07280v3, Prop 4.3.2 and §5) establishes the existence of the abstract orthogonal projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$ for BDI under Bao–Wang preferred parameters, type-uniformly in $n$. Theorem E gives the explicit shape of $p_\nu$ in the chain-factor basis: a carry-recursive product whose only cross-chain ingredient is the cumulative bound $[S \le P_{n-1}^{\mathrm{cum}}]$. The shadow says $p_\nu$ exists; the carry says what it looks like.

**Base case.** Meereboer (arXiv:2510.17655, Lemma 6.2 and §6) treats the $n = 1$ / one-dimensional base case from a completely different direction (combinatorial leading-term recipe). At $n = 1$ Theorem E collapses to $S \le P_0 = 0$, i.e., $S = 0$, matching Meereboer's recipe. Critically, Meereboer's Lemmas 4.3 / 4.5 / 7.4 collapse at multiplicity $> 1$: the higher-multiplicity / higher-rank carry-recursive structure is what fills the gap above $n = 1$ at BDI. The two approaches agree at $n = 1$ and diverge mechanically thereafter; the carry is the BDI-specific structural payload.

**Geometric shadow.** Kobayashi (arXiv:2604.22262) establishes that branching multiplicities for orthogonal Gelfand pairs are governed by *systems* of universal linear inequalities; the loci where multiplicities can change are *fences* — piecewise-linear hypersurfaces decomposing the parameter space into convex regions on which the multiplicity function is locally constant. The pair $(GL_{2n+1}, O_{2n+1})$ is BDI exactly. Theorem E exhibits one explicit defining inequality of the Kobayashi polyhedral decomposition at BDI: the cumulative-carry fence $S \le P_{n-1}^{\mathrm{cum}} = \sum_{a=1}^{n-1} 2(B_a - T_a)$, realized at the crystal-combinatorial level in chain coordinates. Kobayashi's shadow says such a polyhedral system *exists* and is piecewise-linear; the carry produces one of its faces explicitly. **The other faces of the BDI polytope are not addressed here — that is a downstream question.** What the agreement records is that the linear *form* of Theorem E is the right form: a single linear inequality, additive in the chain-factor coordinates, is exactly the shape Kobayashi's theory predicts for each face of the polyhedral decomposition.

---

## 3.6  Closing remark

The cumulative carry $P_a$ is the unified analytical object at BDI. Definition 3.1.1 introduces it; Lemma 3.1.2 records its one-sided monotonicity; Theorem A (recalled from §2) characterizes $B_n$-highest weight in terms of it; the three roles of §3.2–§3.4 are mechanically forced by the left-to-right bracket scan of Theorem A; the external shadows of §3.5 align with the explicit shape that the carry takes.

Three points warrant explicit notice. *First,* the unification is structural, not cosmetic: the same scan that proves Theorem A also proves Proposition 3.2.1, Theorem E, and Corollary 3.4.1, and there is no shorter path to any of the three. *Second,* the carry framework is type-uniform: the recurrence $P_a = P_{a-1} + 2(B_a - T_a)$ has no $n$-dependence beyond the chain index, and the singleton bound always reads against $P_{n-1}$. *Third,* the framework's scope coincides exactly with the v2 chain-factor decomposition's scope, the $|a| \le 2$ regime of the Day-21 trichotomy; the $G_2$ obstruction at $|a| \ge 3$ has multiple interior bracket positions and breaks the carry-recursive structure. This is consistent with the methodological-crystal scope statement (combinatorial-vs-algebraic split): the carry is the analytical embodiment of the chain-factor decomposition, and the chain-factor decomposition has the natural ceiling.

The carry was, in retrospect, available in `bdi_qLR.md` from the start. The work of v3 is to recognize that the same scalar is doing three different jobs and to compress the exposition accordingly.

---

*— End sketch. Compress to LaTeX next session. Watch for the falsification candidate: exposition fragmenting the three roles into three independent sub-chapters. The carry must remain the single subject.*
