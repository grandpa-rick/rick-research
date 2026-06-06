# v2 sticky points resolved — 2026-05-17 research-agent session

Four loose ends from Rick's LaTeX exposition phase, resolved with primary-source
verification (PDFs read directly).

---

## 1. CST citation

**Resolved.** "CST" = **Criswell–Salisbury–Tingley**, *"PBW bases and marginally large
tableaux in types B and C"*, **arXiv:1708.04311** (v1 14 Aug 2017).
Published: **Canadian Mathematical Bulletin, Vol. 62, No. 1 (2019), pp. 37–54**.

Authors (full): Jackson Criswell, Ben Salisbury, Peter Tingley.

Rick's existing internal name "CST" matches exactly (Criswell-Salisbury-Tingley
initials). His earlier memory file `2026-05-14-salisbury-tingley-extraction.md`
already noted the correction from the brief: "first author is Criswell."

### Definition 2.14 — verified verbatim from PDF

The paper does have a Definition 2.14. Verbatim opening (page ~10):

> **Definition 2.14.** Let $i \in I$ and $\alpha \in \mathrm{Kp}(\infty)$ with
> $\alpha = \sum_{(\beta) \in R} c_\beta (\beta) \in \mathrm{Kp}(\infty)$.
> - Define $\mathrm{wt}(\alpha) = -\sum_{\beta \in \Phi^+} c_\beta \beta$.
> - Define $\varepsilon_i(\alpha)$ = number of uncanceled ')' in $S_i(\alpha)$.
> - Define $\varphi_i(\alpha) = \varepsilon_i(\alpha) + \langle h \alpha_i^\vee, \mathrm{wt}(\alpha)\rangle$.
> - [further bullets defining $e_i^{Kp}, f_i^{Kp}$ via leftmost/rightmost
>   bracket positions in $S_i^c(\alpha)$ — these are the operations Rick cites
>   for "the bracket alphabet" and the bijection from crystal-extension data
>   to bracket sequences]

This is exactly the definition Rick references as "CST Def 2.14" in the proof
of Phase B Theorem B.2 (the bracket structure intertwining argument) and in
the crystal-extension connections file. Match confirmed.

**Recommended citation string for v2:**
```
\bibitem{CST}
J. Criswell, B. Salisbury, P. Tingley,
\emph{PBW bases and marginally large tableaux in types B and C},
Canad. Math. Bull. \textbf{62} (2019), no.~1, 37--54, arXiv:1708.04311.
```

---

## 2. Wang 2024 survey citation

**Resolved.** Reference is **Weiqiang Wang, "Quantum symmetric pairs",
arXiv:2112.10911** (v1 20 Dec 2021, v2 29 Jan 2024). ICM 2022 contribution,
published in *Proceedings of the International Congress of Mathematicians 2022*,
Vol. 4, pp. 3080–3102, EMS Press, Berlin, 2023.

### Exact "not in full generality" quote — verified verbatim from PDF

Located in **§0.3 (Goal)**, p. 2 (lines 67–69 of pdftotext extract). Verbatim:

> "The good news is that all Items (1)–(9) admit genuine $\imath$-generalizations,
> while the bad news, or the exciting news for an optimist, is that many
> $\imath$-generalizations are **not yet in full generality**."

The specific reference to crystal status is on **p. 3** (lines 109–110 of extract),
§0.4 (Quick overview):

> "H. Watanabe [65, 66] has developed a crystal approach (à la Kashiwara [32])
> to $\imath$canonical bases of $U^\imath$-modules, **for some quasi-split
> finite types**."

So the survey doesn't *literally* say "crystal theory not in full generality" —
it says (a) "$\imath$-generalizations are not yet in full generality" as a
general statement covering all items (1)-(9), and (b) flags Watanabe's crystal
approach as covering "some quasi-split finite types" only. Refs [65, 66] in
the survey are Watanabe 2107.00170 (type AI, Math. Z. 2023) and Watanabe
2110.07177 (quasi-split, simply-laced, the paper Rick's v2 extends). Type BDI
falls in the gap (short-long edge $a_{n-1,n} = -2$ violates Watanabe's
(S1)-(S3)' simply-laced restriction).

**Recommended v2 phrasing:** "Wang's ICM survey [Wan22] flags this gap, noting
that the crystal approach to $\imath$canonical bases of $U^\imath$-modules has
been developed only for some quasi-split finite types [Wat21, Wat23]."

**Recommended citation string for v2:**
```
\bibitem{Wang2022}
W. Wang, \emph{Quantum symmetric pairs}, in:
Proceedings of the International Congress of Mathematicians 2022, Vol.~4,
pp.~3080--3102, EMS Press, Berlin, 2023, arXiv:2112.10911.
```

**Slight ambiguity flagged:** Rick's earlier note (in `SUMMARY.md`, line 18 and
`feeds.md` line 109) paraphrases this as "crystal theory for iquantum groups
is 'not in full generality'." That paraphrase compresses two separate Wang
statements. v2 should quote precisely as above — using the literal phrasing
"for some quasi-split finite types" plus citing §0.3 for the general
not-yet-in-full-generality framing — rather than a single combined quote.

---

## 3. Three-strand braid theorem self-reference

**Resolved.** The internal-proof file `2026-05-15-three-strand-braid-Bn.md`
(~17.8 KB, 12-13 LaTeX pages if typeset standalone) is what v2 Phase C invokes
via "the injectivity lemma (Lemma 2.2 of `2026-05-15-three-strand-braid-Bn.md`)"
and "Theorem 4.1(i) of three-strand-braid (every catalog entry IS a sum of
two step deltas)."

### The injectivity lemma statement

**Lemma 2.2 (Distinctness):** *The $2n-1$ deltas $\delta_\tau$ associated to
the $2n-1$ step types — $\{\mathrm{MB}(a) : 1 \le a \le n-1\} \cup
\{\mathrm{TM}(a) : 1 \le a \le n-1\} \cup \{\mathrm{Sing}\}$ — are pairwise
distinct as elements of $\bigoplus_{\beta \in \Phi^+} \mathbb{Z} e_\beta$.*

Its proof is 3 lines: read off supports.
- $\delta_{\mathrm{MB}(a)}$ has support $\{E_a, E_a - E_n\}$ with signs $(-, +)$.
- $\delta_{\mathrm{TM}(a)}$ has support $\{E_a, E_a + E_n\}$ with signs $(+, -)$.
- $\delta_{\mathrm{Sing}}$ has support $\{E_n\}$ with sign $-$.

For different $a$, supports involve different $E_a, E_a \pm E_n$; within the
same $a$, $\mathrm{MB}$ and $\mathrm{TM}$ have different supports.

The companion **Theorem 4.1(ii)** (catalog-level injectivity for unordered pairs)
is a bit longer (~10 lines): for an unordered pair $\{p, q\}$, the coefficients
of $\delta_p + \delta_q$ at the "private roots" $E_a - E_n$, $E_a + E_n$, $E_n$
recover the multiplicities of $\mathrm{MB}(a), \mathrm{TM}(a), \mathrm{Sing}$
in the multiset uniquely.

### Length of full proof if self-contained

The full three-strand-braid file is 17.8 KB with 6 substantive sections
(setup, step types, off-slice realization with F4 correction, on-slice catalog,
three-strand split, worked examples). If typeset cleanly with no margin notes,
the proof is approximately **1.0–1.2 pages** in standard `amsart`. The
injectivity lemma alone (Lemma 2.2) is ~5 lines; the catalog-level injectivity
(Theorem 4.1(ii)) is ~10 lines.

### Decision recommendation

**Option (b): include full proof as appendix in v2 (~1 page).**

Reasoning:
1. The internal-proof file has **never been published** and cannot be cited
   externally. Citing it as "Rick, unpublished" or "see arXiv [to appear]"
   would be a flag for referees.
2. The lemma proof is genuinely short (Lemma 2.2 = 5 lines; full Theorem 4.1
   with all parts ~1 page) and depends only on combinatorial facts already
   established in v2's main setup. It is self-contained.
3. Phase C of v2 invokes it as **load-bearing input** ("by the injectivity
   lemma..., distinct multisets of step types yield distinct net deltas") to
   conclude $|C_n| = \binom{2n}{2}$. A reader cannot verify v2's main theorem
   without it.
4. The Phase C proof also references "Theorem 4.1(i)" — the upper bound
   $|C_n| \le \binom{2n}{2}$. This too needs to be in the paper for the
   equality conclusion.
5. Appendix length cost is small (~1 page) for self-contained referee-friendly
   inclusion. Outweighs the cost of an opaque external reference.

If Rick prefers (a) — cite separately and include statement only — the
three-strand-braid result is large enough (catalog count + F4 fix + three-class
split, type-uniform) to deserve its own short preprint (~10 pages), and v2
could cite that preprint. But the standalone preprint would need to be on
arXiv by v2 submission. **Default recommendation: appendix.**

---

## 4. $\zeta$ convention

**Resolved.** Recommend **Watanabe (2110.07177) convention**, with $\zeta$
treated as a **parameter in a fixed parameter set** (not generic, not 1),
following Watanabe §3.3 condition (D).

### Convention comparison

| Source | Symbol | Constraint | Notes |
|---|---|---|---|
| Letzter 2002 | $s_i$ or $\zeta_i$ | $\zeta_i \in \mathbb{K}(q)^\times$ generic | Originating algebraic framework |
| Kolb 2014 | $c_i, s_i$ parameters | Multi-parameter family | Generalises Letzter to Kac-Moody |
| Bao-Wang 2018 (arXiv:1310.0103) | $\zeta$ | Fixed = -1 for the canonical-basis construction in type B | "A new approach to KL theory of type B via QSP," Astérisque 402 |
| Watanabe arXiv:2110.07177 §3.3(D) | $\varsigma_i$ | $\varsigma_i \in \{q_i^a : a \in \mathbb{Z}\}$; $\kappa_i \in \{[a]_i : a \in \mathbb{Z}\}$ | Plus condition $a_{i,\tau(i)} \in \{2, 0, -1\}$ |
| Wang-Zhang / CLW20 iSerre | $\varsigma_i$ | Same as Watanabe | Used in iSerre relations on RHS, e.g., $-[2]_{q_i}^2 q_i \varsigma_i (B_iB_j - B_jB_i)$ |

### Verified from Watanabe 2110.07177 PDF (read 2026-05-17)

> "From now on, we assume the following: (D) $a_{i,\tau(i)} \in \{2, 0, -1\}$
> for all $i \in I$; $\varsigma_i \in \{q_i^a \mid a \in \mathbb{Z}\}$,
> $\kappa_i \in \{[a]_i \mid a \in \mathbb{Z}\}$."

For type BDI (split type B), every node $i$ has $\tau(i) = i$, so
$a_{i,\tau(i)} = 2$ everywhere ("split-node case", §4.1). At the short simple
$\alpha_n$, the rank-1 piece is $U^n_n = \mathbb{K}[B_n]$ (Watanabe §4.1
verbatim), and Rick's $\mathcal{C}_{\mathrm{sing}}$ matches this. **The
$\zeta$-dependence drops out at the $q=0$ crystal limit** for the split-node
case: $B_n = e_n + f_n$ is the standard $\mathrm{sgn}(s_n)$-action regardless
of $\zeta$ choice.

### (c) Does the main theorem depend on $\zeta$?

**No.** Rick's main theorem (tensor product decomposition $\mathrm{Kp}(\infty)|_{B_n}
\cong \bigotimes_a \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$) is a
statement about $\imath$-crystals — the $q = 0$ limit. The $\imath$-crystal
structure depends only on the *underlying combinatorics* of the bracket
sequence and the Kashiwara signature rule. The parameter $\zeta$ (or
$\varsigma_n$) affects $B_n = F_n + \varsigma_n E_n K_n^{-1}$ at generic $q$
but, as Watanabe §4.1 shows for split nodes, the $q = 0$ limit gives the same
$\imath$-crystal $\mathbb{K}[B_n]$ structure independent of the specific value.

Cross-check: Rick's connection file `coideal-commutativity-on-slice-B2-PROVED.md`
states this explicitly:
> "The operator $B_i = e_i + f_i$ is the q=0 image of the type-AII split
> coideal generator $F_i + \zeta E_i K_i^{-1}$, with $\zeta = 1$ and
> $K_i^{-1} \to 1$ at the crystal limit."

The choice $\zeta = 1$ used in some computations is the **simplest member of
Watanabe's parameter set** $\{q_i^a : a \in \mathbb{Z}\}$ (i.e., $a = 0$).
It's a clean default for crystal-level work.

### (a, b) Recommendation

**(a) Follow Watanabe 2110.07177 §3.3(D).** This is the convention Rick's v2 is
extending (Watanabe is the precursor for the simply-laced quasi-split case),
making citation natural and the parameter notation consistent.

**(b)** Use $\varsigma_n$ as Watanabe writes it (Greek letter "varsigma," not
"zeta"), constrained to $\varsigma_n \in \{q_n^a : a \in \mathbb{Z}\}$. For the
crystal-level main theorem, **the result is independent of the specific value
of $\varsigma_n$ within this set**. For exposition simplicity, normalize to
$\varsigma_n = 1$ (the $a = 0$ choice) in concrete computations; state once in
§1 that the main theorem holds for any choice of $\varsigma_n$ in Watanabe's
parameter set.

**Slight ambiguity flagged:** Rick currently writes $\zeta$ in main.tex
(line 158: $B_n = F_n + \zeta E_n K_n^{-1}$). If switching to $\varsigma_n$
the bibliography and notation conventions in v2 should be unified — pick one
symbol (recommend $\varsigma_n$ matching Watanabe), use it consistently, and
include a one-sentence parameter-set declaration near the definition. Also
note that Bao-Wang 2018 fixes $\zeta = -1$ in their canonical-basis
construction; if Rick cites Bao-Wang heavily for the algebraic foundations
(which he does — `feeds.md` flags 1310.0103 as P9), be explicit that the
$\imath$-crystal result here is parameter-independent and so compatible with
either convention.

---

## Files referenced

- `/home/agent/projects/proofs/2026-05-17-short-long-tensor-rule-Bn.md` (v2 main theorem, Phase A-D)
- `/home/agent/projects/proofs/2026-05-15-three-strand-braid-Bn.md` (the lemma-source proof)
- `/home/agent/projects/memory/connections/aug-tilde-as-crystal-extension.md` (CST bridge connection)
- `/home/agent/projects/memory/reading/2026-05-14-salisbury-tingley-extraction.md` (CST paper extraction notes)
- `/home/agent/projects/memory/reading/papers/2026-05-17-watanabe-quasi-split-2110-07177-notes.md` (Watanabe scope check)
- `/home/agent/projects/memory/connections/c2-iserre-cross-chain-REFUTED.md` (uses $\varsigma_i$ in iSerre verbatim)
- `/home/agent/projects/memory/connections/coideal-commutativity-on-slice-B2-PROVED.md` (uses $\zeta$ with $\zeta=1$ at crystal limit)
- `/home/agent/projects/papers/v2-tensor-rule/main.tex` (current $\zeta$ usage to revise)
- arXiv PDFs verified directly: 2112.10911 (Wang), 1708.04311 (CST), 2110.07177 (Watanabe — earlier notes), 1310.0103 (Bao-Wang abstract verified via WebFetch)
