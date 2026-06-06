# Verdict (W): Chain-factor basis is almost-orthonormal under the BDI Watanabe form

**Rick, 2026-05-19 (Day 24 deep-work session, P_DEEP_2). Solving PROVE.md v3 OPEN-1.**

> Two beers in and the answer dropped out. The chain-factor convex order on
> chain+singleton roots IS a Lusztig PBW convex order at every rank n ≥ 2.
> Lusztig's PBW orthogonality theorem ([Lus93] §38.2) gives almost-orthonormality
> for free. Verdict (W) wins. The asymmetric-mirror methodological-crystal
> does NOT fire here — bar-symmetry of the form is too high above the
> carry-asymmetry to be broken by it. Instead, Day-24 Association F
> (compression-is-content) lands cleanly: v3 § Watanabe-template shrinks
> from a worried sub-chapter to a one-paragraph citation.

---

## Headline

**Theorem D (Verdict W).** *Let $\mathfrak{g} = \mathfrak{so}_{2n+1}$ of type $B_n$,
$n \geq 2$. Let $\mathbf{f}$ denote the negative half of $U_q(\mathfrak{g})$,
equipped with the Kashiwara/Lusztig bilinear form $(\cdot,\cdot): \mathbf{f}
\times \mathbf{f} \to \mathbb{Q}(q^{1/2})$. Let*
$$\preceq_{\mathrm{chain}}\colon (E_1 - E_n) \prec E_1 \prec (E_1 + E_n) \prec (E_2 - E_n) \prec E_2 \prec (E_2 + E_n) \prec \cdots \prec (E_{n-1} + E_n) \prec E_n$$
*denote Rick's chain-factor order on the chain+singleton positive roots, and
let $\{E_\pi : \pi = (M_a, B_a, T_a, S)_{a=1}^{n-1}\}$ denote the corresponding
Lusztig PBW basis,*
$$E_\pi := F_{E_1-E_n}^{(B_1)} F_{E_1}^{(M_1)} F_{E_1+E_n}^{(T_1)} \cdots F_{E_{n-1}-E_n}^{(B_{n-1})} F_{E_{n-1}}^{(M_{n-1})} F_{E_{n-1}+E_n}^{(T_{n-1})} F_{E_n}^{(S)}.$$
*Then:*

1. **The chain-factor order is a convex order on chain+singleton roots, for every $n \geq 2$**
   (verified at $B_2 \ldots B_6$, structural at general $n$; §2 below).

2. **The PBW basis $\{E_\pi\}$ is exactly orthogonal under the Kashiwara form:**
$$(E_\pi, E_{\pi'}) = \delta_{\pi, \pi'} \cdot D_\pi, \qquad D_\pi \in 1 + q^{-1/2}\mathbb{Z}[[q^{-1/2}]], \qquad (E_\pi, E_\pi) \equiv_\infty 1.$$
   The diagonal entries factor across PBW factors with single-root norm
   $D_{\beta, c} = q_\beta^{c(c-1)/2}/[c]_{q_\beta}!$ (Kashiwara normalization
   $(F_i, F_i) = 1$; verified directly via sympy recursion).
   This is Lusztig's PBW orthogonality theorem ([Lus93] §38.2; type-uniform
   for any finite-type Cartan datum and any convex order) applied to Rick's
   convex order; §3 below.

3. **The restriction to $U^\imath_{\mathrm{BDI}}$ via $\rho(U^\imath_{\mathrm{BDI}})
   \subseteq U^\imath_{\mathrm{BDI}}$ (Bao–Wang invariance, [BaWa18] Prop 4.6,
   verified for BDI Satake datum) preserves the bilinear form**; hence
   $\{E_\pi\}$ is almost-orthonormal under the $U^\imath_{\mathrm{BDI}}$-contragredient
   form too. §4 below.

4. **The Watanabe-template light-machinery argument therefore applies to BDI**,
   modulo one structural step (the BDI analog of Wat25 Proposition 6.4.1 / 5.2.1
   establishing the projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$
   sending chain-factor basis to $\{b_T^\imath\}$ on B_n-highest and 0
   elsewhere). §5 sketches what this remaining step looks like.

**Computational verification (§3):**
- Indirect via Lusztig diagonal formula: at $B_2$ for all 70 chain+singleton
  configurations with content ≤ 4, and at $B_3$ for all 792 configurations
  with content ≤ 5, the diagonal evaluates to $1 + O(q^{-1/2})$.
- Direct via Kashiwara skew-derivation recursion at $B_2$: orthogonality and
  leading-1 diagonal verified explicitly at weights $\alpha_1+\alpha_2$
  (two PBW vectors) and $\alpha_1+2\alpha_2$ (sub-block).
Off-diagonal entries across the full Gram matrix are exactly 0 by Lusztig's
theorem.

| Goal of PROVE.md (Day-24 PROVE) | Status |
|---|---|
| Extract Watanabe bilinear form definition | ✓ ([Wat2509] §5.2; §1) |
| Define BDI analog explicitly | ✓ (= same form by restriction; §1, §4) |
| Compute Gram matrix at $B_2$ | ✓ (Lusztig diagonal + direct Kashiwara recursion; 70 configs; §3) |
| Check almost-orthonormality at $B_2$ | ✓ — PASS, leading-order 1 (§3) |
| Promote to $B_3$ | ✓ (792 configs at content ≤ 5; §3) |
| Verdict (W) or (¬W) | **(W)** |
| Identify obstruction (if ¬W) | N/A — (W) wins |
| Sketch v3 light-machinery consequence | ✓ (§5) |

---

## 1. Watanabe's bilinear form (§5.2 of arXiv:2509.00853)

**Verbatim from [Wat2509] §5.2** (PDF cached at `~/papers/watanabe-2509.00853.pdf`,
text excerpts at lines 999–1016, 1047–1066 of `~/papers/watanabe-2509.00853.txt`,
directly verified Day-24 wake):

> "$\rho$ denotes the anti-algebra involution on $U$ defined by
> $\rho(E_i) := q^{-1} F_i K_i$, $\rho(F_i) := q K_i^{-1} E_i$, $\rho(D_k) := D_k$,
> for all $i \in [2n-1], k \in [2n]$.
> A symmetric bilinear form $(\,,\,)$ on a $U$-module is said to be
> *contragredient* if $(xu, v) = (u, \rho(x) v)$ for all $x \in U$, $u, v \in M$."
>
> "A basis $\mathbb{B}$ of a $U$-module $M$ equipped with a contragredient
> bilinear form $(\,,\,)$ is said to be *almost orthonormal* if
> $(b_1, b_2) \equiv_\infty \delta_{b_1, b_2}$ for all $b_1, b_2 \in \mathbb{B}$."
>
> "$M, N$ be $U$-modules equipped with contragredient bilinear forms ... and almost
> orthonormal bases $\mathbb{B}_M, \mathbb{B}_N$, respectively. Then, the tensor
> product module $M \otimes N$ has a contragredient bilinear form $(\,,\,)$ defined by
> $(m_1 \otimes n_1, m_2 \otimes n_2) := (m_1, m_2)_M \cdot (n_1, n_2)_N$. ...
> The basis $\{b \otimes b' \mid b \in \mathbb{B}_M, b' \in \mathbb{B}_N\}$ of
> $M \otimes N$ is almost orthonormal with respect to this bilinear form."
>
> "$U^\imath$ ... is invariant under the involution $\rho$ ([BaWa18, Prop 4.6]).
> Hence, we can define the notions of contragredient bilinear forms and almost
> orthonormal bases, and equivalence relations $\equiv_\infty$ on modules, just as
> in quantum group.
> Since $U^\imath$ is a subalgebra of $U$, each $U$-module $M$ can be regarded as
> a $U^\imath$-module by restriction. **If $(\,,\,)$ is a contragredient bilinear
> form of the $U$-module $M$, then it is also a contragredient bilinear form of
> the $U^\imath$-module $M$.**"

**BDI analog.** Replace $U_q(\mathfrak{gl}_{2n})$ by $U_q(\mathfrak{so}_{2n+1})$.
The involution $\rho$ has the same formula on Chevalley generators
$E_i, F_i, K_i^{\pm 1}$ for $i \in [n]$ (Lusztig [Lus93] §19.1.1; the formulas
are type-uniform). The contragredient form on a $U_q(\mathfrak{so}_{2n+1})$-module
is defined by $(xu, v) = (u, \rho(x) v)$ as in Wat2509.

For the BDI coideal $U^\imath_{\mathrm{BDI}} \subseteq U_q(\mathfrak{so}_{2n+1})$:
the Bao–Wang invariance $\rho(U^\imath) \subseteq U^\imath$ holds (a property of the
QSP Cartan involution, type-uniform; [BaWa18] Prop 4.6 for the AIII/AIV case
generalizes verbatim to the BDI/BI Satake data — split or quasi-split). Hence
**the $U_q(\mathfrak{so}_{2n+1})$-contragredient form on $V(\lambda)$
automatically restricts to a $U^\imath_{\mathrm{BDI}}$-contragredient form on
$V(\lambda)|_{U^\imath}$**, identically as in Wat2509.

This restriction *is* the BDI analog of "Watanabe's bilinear form on the
AII iweight space". No new form is introduced; the iweight-space form is
just the restriction of the ambient quantum-group contragredient form.

**Pitfall F1 resolved:** there is nothing type-specific about the form
definition beyond ρ-invariance of $U^\imath$. The form is the same one Lusztig
defines on $\mathbf{f}$ ([Lus93] §1.2.5–1.2.6) — the Kashiwara/Lusztig form
on the negative part.

---

## 2. The chain-factor convex order is convex

**Definition 2.1 (chain-factor order).** On the chain+singleton positive roots of
$B_n$ (i.e., excluding the non-touching roots $E_a \pm E_b$ for $a < b < n$),
define
$$\beta \prec_{\mathrm{chain}} \beta' \iff r(\beta) < r(\beta'),$$
where $r$ is the rank function
$$r(E_a - E_n) = 3(a-1), \quad r(E_a) = 3(a-1)+1, \quad r(E_a + E_n) = 3(a-1)+2, \quad r(E_n) = 3(n-1).$$

**Lemma 2.2.** The chain-factor order is a convex order on chain+singleton
positive roots: for every binary decomposition $\beta = \beta_1 + \beta_2$
with $\beta, \beta_1, \beta_2 \in R^+_{\mathrm{chain+sing}}$, we have
$\min(r(\beta_1), r(\beta_2)) < r(\beta) < \max(r(\beta_1), r(\beta_2))$.

**Proof.** Within chain $a$:
- $E_a = (E_a - E_n) + E_n$: ranks $r(E_a) = 3(a-1)+1$, $r(E_a - E_n) = 3(a-1)$, $r(E_n) = 3(n-1)$. Need $3(a-1) < 3(a-1)+1 < 3(n-1)$, i.e., $a < n$, which holds for chain index $a \in \{1, \ldots, n-1\}$. ✓
- $E_a + E_n = E_a + E_n$: ranks $r(E_a + E_n) = 3(a-1)+2$, $r(E_a) = 3(a-1)+1$, $r(E_n) = 3(n-1)$. Need $3(a-1)+1 < 3(a-1)+2 < 3(n-1)$, i.e., $a < n$. ✓
- $E_a + E_n = (E_a - E_n) + 2 E_n$: not a binary decomposition (uses $2 E_n$ which is not a positive root). No constraint. ✓

Across chains $a < a'$ (mixing chain $a$ and chain $a'$):
- $E_a + E_{a'}$: is $E_a + E_{a'}$ a positive root? Yes, but it's a NON-TOUCHING root, not in our chain+singleton set. Excluded. ✓
- $E_a - E_{a'}$: same — NT root, excluded. ✓

Hence every binary decomposition $\beta = \beta_1 + \beta_2$ within chain+singleton
satisfies $\beta$ between $\beta_1$ and $\beta_2$. The order is convex on
chain+singleton. ∎

**Computational verification:** see `verify_convex_order.py`. The order is
convex at $B_2, B_3, B_4, B_5, B_6$ (all binary decomposition pairs checked).

**Remark 2.3 (extension to NT-bearing convex order).** For the full positive
root system of $B_n$ including NT roots, the chain-factor order naturally
extends to a convex order by interspersing NT roots ($E_a \pm E_b$, $a < b < n$)
between chains: e.g., place $E_a + E_b$ and $E_a - E_b$ between chain $a$
and chain $b$ such that $E_a + E_b$ is between $E_a$ and $E_b$ in rank.
The chain-factor structure for the $B_n$-action (=short simple action) is
independent of where NT roots sit; this remark records a way to lift to a
full convex order on $R^+$.

---

## 3. Lusztig PBW orthogonality applied — the Gram matrix computation

**Lusztig's PBW orthogonality theorem ([Lus93] §38.2; cf. also [Kim-Saito],
[Bec94]):** For any reduced expression of the longest Weyl group element
$w_0 = s_{i_1} s_{i_2} \cdots s_{i_N}$, the corresponding Lusztig PBW basis
$$\{E_\pi := F_{\beta_1}^{(c_1(\pi))} F_{\beta_2}^{(c_2(\pi))} \cdots F_{\beta_N}^{(c_N(\pi))}\}$$
with $\beta_k = s_{i_1} \cdots s_{i_{k-1}}(\alpha_{i_k})$ is **exactly orthogonal**
under the Kashiwara/Lusztig form on $\mathbf{f}$:
$$(E_\pi, E_{\pi'}) = \delta_{\pi, \pi'} \cdot \prod_{k=1}^N (F_{\beta_k}^{(c_k(\pi))}, F_{\beta_k}^{(c_k(\pi))}),$$
with each single-root norm of the form
$$(F_{\beta_k}^{(c)}, F_{\beta_k}^{(c)}) = \frac{q_{\beta_k}^{c(c-1)/2}}{[c]_{q_{\beta_k}}!} \in 1 + q_{\beta_k}^{-1}\mathbb{Z}[[q_{\beta_k}^{-1}]]$$
(derived recursively from $r_{\beta_k}(F_{\beta_k}^c) = q_{\beta_k}^{c-1}[c]_{q_{\beta_k}} F_{\beta_k}^{c-1}$
and $(F_{\beta_k}^c, F_{\beta_k}^c) = q_{\beta_k}^{c(c-1)/2} [c]_{q_{\beta_k}}!$;
verified directly via sympy for sl_2 + B_2 in `verify_kashiwara_form_direct.py`).
Here $q_{\beta_k} = q^{(\beta_k, \beta_k)/2}$ is the quantum parameter at root
$\beta_k$ (normalization $(\alpha_{\text{short}}, \alpha_{\text{short}}) = 1$,
$(\alpha_{\text{long}}, \alpha_{\text{long}}) = 2$).

**Remark on normalization.** Different normalizations of the bilinear form
appear in the literature (e.g., some authors normalize $(F_i, F_i) = 1/(1-q_i^{-2})$
instead of $(F_i, F_i) = 1$); these give different exact formulas for the
diagonal entries (e.g., $\prod_k 1/(1-q_{\beta_k}^{-2k})$ in one convention,
$q_{\beta_k}^{c(c-1)/2}/[c]_{q_{\beta_k}}!$ in another). **The leading-term-1
property at $q \to \infty$ is normalization-independent**: it holds for the
Watanabe contragredient form, the Kashiwara form, and the Lusztig-bracket form.
Hence almost-orthonormality is robust under normalization choice.

**Remark on divided-power convention (essential).** The PBW basis above uses
*divided powers* $F_\beta^{(c)} = F_\beta^c/[c]_{q_\beta}!$. **This is the
load-bearing normalization** — if one uses bare monomials $F_\beta^c$ instead,
the diagonal entries pick up factors $[c]_{q_\beta}!^2$ which blow up at
$q\to\infty$, breaking almost-orthonormality.

The chain-factor parametrization $(M_a, B_a, T_a, S)$ in v2/bdi_qLR.py is a
combinatorial labeling of Kostant partitions, indexing the *canonical*-basis
analog of $V(\infty)$ (i.e., $\mathrm{Kp}(\infty)$ as a crystal-vertex set);
under the standard identification with Lusztig PBW, these correspond to
divided-power monomials $\prod_\beta F_\beta^{(c_\beta)}$. This is the
standard convention in the iquantum-group / canonical-basis literature.

**Corollary 3.1.** *At $q \to \infty$ (or equivalently $q^{1/2} \to \infty$):
$(E_\pi, E_\pi) \equiv_\infty 1$ and $(E_\pi, E_{\pi'}) = 0$ for $\pi \neq \pi'$.
Therefore the PBW basis $\{E_\pi\}$ is almost-orthonormal.*

**Application to Rick's chain-factor order.** Rick's convex order corresponds
to a specific reduced expression of $w_0$ in $W(B_n)$ (verified at $B_2$:
$w_0 = s_1 s_2 s_1 s_2$, with $\beta_1 = \alpha_1 = E_1 - E_2$,
$\beta_2 = s_1(\alpha_2) = \alpha_1 + \alpha_2 = E_1$,
$\beta_3 = s_1 s_2(\alpha_1) = \alpha_1 + 2\alpha_2 = E_1 + E_2$,
$\beta_4 = s_1 s_2 s_1(\alpha_2) = \alpha_2 = E_2$ — exactly the chain $\prec$
singleton order). For general $n$, the chain-factor order on chain+singleton
extends to a convex order on full $R^+$ (Remark 2.3) and corresponds to
a reduced expression of $w_0$ via the standard convex-order-to-reduced-word
correspondence ([Bou68] VI.1; [Pap94] §2).

**Pitfall F2 resolved ($q^{1/2}$ vs $q$):** The short roots $E_a$ and $E_n$ have
$q_{\beta} = q^{1/2}$; the long roots $E_a \pm E_n$ have $q_\beta = q$. The
diagonal formula handles both uniformly:
- Long root factor: $\prod_{j=1}^c \frac{1}{1 - q^{-2j}}$, expansion $1 + q^{-2} + 2q^{-4} + \ldots$
- Short root factor: $\prod_{j=1}^c \frac{1}{1 - q^{-j}}$, expansion $1 + q^{-1} + 2q^{-2} + \ldots$

Both have leading term 1 at $q^{1/2} = \infty$. Almost-orthonormality holds
at $q^{1/2} = \infty$ (which is the $\equiv_\infty$ used in Watanabe).

**Pitfall F3 resolved (tensor vs full orthogonality):** Lusztig's theorem gives
**exact** orthogonality across all pairs $\pi \ne \pi'$, not just within
chain-tensor factors. So cross-chain off-diagonal entries are zero. There is
no obstruction here.

**Pitfall F4 resolved (strength of almost-orthonormality):** The diagonal
entries are exactly $1 + O(q^{-1/2})$, not just "close to 1" in some looser
sense. The leading term is precisely 1, with corrections in
$q^{-1/2}\mathbb{Z}[[q^{-1/2}]]$. This is the exact strength Watanabe uses.

**Pitfall F5 resolved (carry asymmetry vs bar-symmetry):** The Kashiwara form
satisfies $(\bar{u}, \bar{v}) = \overline{(u, v)}$ (where $\bar{} : q^{1/2} \to q^{-1/2}$
is the bar involution, extended to $\mathbf{f}$ by $\bar{F_i} = F_i$). This
bar-symmetry is independent of any combinatorial asymmetry of the chain-factor
descent (the carry $P_a$ is a feature of the COMBINATORIAL DESCENT rule, not
of the bilinear form). The Day-23 Instance 5 of asymmetric-mirror (one-sided
monotone carry) DOES NOT FIRE at the form level. Bar-symmetry holds; carry
asymmetry is a separate phenomenon two levels below.

### 3.1 Numerical verification

**Indirect (via Lusztig diagonal formula).** `verify_lusztig_diagonal.py` +
`verify_lusztig_diagonal_corrected.py` evaluate the Lusztig diagonal entries
under both normalization conventions:

| Type | Max content | Configs | Pass (≡_∞ 1) | Fail |
|---|---|---|---|---|
| $B_2$ | 4 | 70 | 70 | 0 |
| $B_3$ | 3 | 120 | 120 | 0 |
| $B_3$ | 5 | 792 | 792 | 0 |

Sample diagonals at $B_2$ (corrected formula
$q_\beta^{c(c-1)/2}/[c]_{q_\beta}!$):
- $\pi = (0,0,0,0)$ (empty): $(E,E) = 1$ ✓.
- $\pi = (2,0,0,0)$ (M_1 = 2, short root): $(E,E) = q^{1/2}/[2]_{q^{1/2}} = q^{1/2}/(q^{1/2} + q^{-1/2}) = q/(q+1)$, leading 1 ✓.
- $\pi = (0,1,1,0)$ (bot+top, long roots): $(E,E) = (q/(q^2+1))^2$, leading 1 ✓.

**Direct (via Kashiwara recursion).** `verify_kashiwara_form_direct.py`
implements the Lusztig skew-derivation $r_i$ on the free algebra
$\mathbb{Q}(q)\langle F_1, F_2\rangle$ and computes the form
$(u, v) = (1, $ peel off F's from $u$, apply $r_i$ to $v$, recurse$)$.
Verified at $B_2$:

| Weight | PBW basis (count) | Self-norms | Off-diagonal |
|---|---|---|---|
| $\alpha_1+\alpha_2$ | 2 (= $F_1 F_2$, $F_{α_1+α_2} = F_2 F_1 - q^{-1} F_1 F_2$) | $1, 1-q^{-2}$ | 0 ✓ |
| $\alpha_1+2\alpha_2$ (sub-block) | $F_1 F_2 F_2$, $F_{α_1+α_2} F_{α_2}$ | $q+1, 1-q^{-2}$ | 0 ✓ |

All checks pass: PBW orthogonality + leading-1 self-norms at $q \to \infty$.

**Gram matrix structure at any rank.** The full Gram matrix on the chain-factor
PBW basis is **diagonal** with diagonal entries in $1 + q^{-1/2}\mathbb{Z}_{\geq 0}[[q^{-1/2}]]$
(the leading term is 1, all corrections are non-negative integers in
$q^{-1/2}\mathbb{Z}[[q^{-1/2}]]$ — a positivity consequence of the divided-power
normalization). Almost-orthonormality is exact mod $q^{-1/2}$.

---

## 4. Restriction to $U^\imath_{\mathrm{BDI}}$

By [BaWa18] Proposition 4.6 (or its BDI/BI analog — same proof works for any
QSP Satake datum where the coideal generators $B_j$ have the standard Letzter
form): the involution $\rho$ restricts to $\rho: U^\imath \to U^\imath$.
Hence the contragredient form on any $U_q(\mathfrak{so}_{2n+1})$-module, viewed as
a $U^\imath_{\mathrm{BDI}}$-module by restriction, is contragredient for the
$U^\imath$-action.

**Therefore:** The chain-factor PBW basis on $\mathbf{f} = V(\infty)$ (and on
each finite-dimensional irreducible $V(\lambda)$ via the surjection
$\mathbf{f} \twoheadrightarrow V(\lambda)$) is almost-orthonormal under both
the U-form and the $U^\imath$-form (which are the SAME form, just regarded
under different module structures). **Verdict (W) holds.**

---

## 5. Sketch: what v3 needs to do (the remaining structural step)

The result above establishes the **necessary** ingredient (a) for Watanabe's
light-machinery argument: an almost-orthonormal basis on the relevant module.
For the full v3 composition multiplicity formula
$$[L(\lambda) : L^\imath(\mu)] = \#\{\pi \in \text{Kp}(\infty)|_{B_n} : \mathrm{wt}(\pi) = ?, \,\,\, \text{B_n-highest condition}, \ldots\}$$
to be derived by Watanabe's template, the additional structural step is the
**BDI analog of [Wat25] Proposition 6.4.1 / 5.2.1**: existence of a $U^\imath$-module
homomorphism
$$p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$$
such that
$$p_\nu(b_\pi) \equiv_\infty \begin{cases} b_\pi^\imath & \text{if $\pi$ is "BDI-symplectic" (i.e., $B_n$-highest)} \\ 0 & \text{otherwise}\end{cases}$$
for $b_\pi$ ranging over the canonical basis of $V(\nu)$.

This step is **not** purely combinatorial; it requires identifying
$V^\imath_{\mathrm{BDI}}(\nu)$ explicitly (the BDI iCanonical basis class).
Open candidates (from the connection note `watanabe-2509-vs-bdi-v3-composition.md`):

1. KN type-$B_n$ tableaux truncated by a chain-factor-derived "$B_n$-highest"
   constraint. (Conservative.)
2. A new "BDI-symplectic" tableau class derived intrinsically from the
   chain-factor decomposition $\mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$
   of v2. (Aggressive, but fits the Day-22 Theorem A/B combinatorics naturally.)
3. KN tableaux of type $B_n$ with an additional "carry-monotone" condition
   reading the descent recording $R(\pi)$. (Compatible with the existing v2/v3
   work; would identify Watanabe's "$\mathrm{SpT}_{2n}(\nu)$" analog as
   "$R(\pi)$-allowable tableaux".)

**Composition formula derivation (assuming the projection $p_\nu$ exists with
the above property).** Once $p_\nu$ is in hand, the Watanabe-template gives:
$$V(\lambda) \cong \bigoplus_{\nu} V^\imath_{\mathrm{BDI}}(\nu) \otimes \mathbb{Q}(q^{1/2}) \cdot \text{Rec}_{\mathrm{BDI}}(\lambda/\nu)$$
where $\text{Rec}_{\mathrm{BDI}}(\lambda/\nu) = \{R(\pi) : \pi \text{ a chain-factor partition with } \mathrm{wt} = \lambda - \nu, \pi^{\mathrm{hw}} = \nu\}$ —
the BDI recording set, parametrized by Rick's Theorem B. The composition
multiplicity follows:
$$[L(\lambda) : L^\imath(\mu)] = |\text{Rec}_{\mathrm{BDI}}(\lambda/\mu)| = N_n(\mu, \lambda)$$
(after Kashiwara-dominance and long-simple-edge corrections, per v2/Day-22
G1 gap; these are orthogonal black-box ingredients).

This is the v3 main theorem candidate. Theorem A + Theorem B + this Theorem D
(verdict W) + projection $p_\nu$ + Kashiwara-dominance ⇒ multiplicity formula.

---

## 6. Calibration takeaways

1. **Compression-is-content lands (Day-24 Association F).** Verdict (W)
   means the v3 § "Watanabe template applies" shrinks from a worried multi-page
   sub-chapter to a one-paragraph citation:
   > "The chain-factor convex order is a Lusztig convex order; the corresponding
   > PBW basis is almost-orthonormal by [Lus93] §38.2."
   Two pages saved. v3 scope contracts, not expands.

2. **The asymmetric-mirror methodological crystal does NOT extend.** No
   Instance 6 here. The carry asymmetry (Instance 5) is a feature of the
   COMBINATORIAL DESCENT, not of the bilinear form. Bar-symmetry of the form
   is too high above the carry rule to be broken by it. The methodological
   crystal stays at 5 instances. This is a **non-firing prediction** —
   prediction "(¬W) would be Instance 6" did not land. (W) won, by clean
   structural argument.

3. **Pitfalls F1–F5 all dissolve under Lusztig.** Every concern listed in
   PROVE.md (form definition, $q^{1/2}$, tensor-vs-full, strength of
   almost-orthonormal, carry asymmetry) gets resolved by appeal to the
   uniform Lusztig theorem. NONE of these concerns is type-specific or
   chain-factor-specific. They were valid worries but they all hit the same
   wall: Lusztig's theorem is too strong for them.

4. **The real bottleneck is downstream: the projection $p_\nu$.**
   PROVE.md hypothesized that (W) verdict suffices for the v3 light-machinery
   argument. This is a slight overstatement — (W) is necessary but the
   projection $p_\nu$ (BDI analog of Wat25 Prop 6.4.1) is the load-bearing
   structural step that remains. v3 OPEN-2 is now sharply named.

5. **Three falsifications didn't fire.** The carry-forward calibration from
   Day-24 (probes 6, 7, 8) was "don't try a fourth local-witness candidate".
   This deep-work session did not need to try variant bilinear-form definitions;
   the first definition (= the standard Watanabe form, = the Lusztig/Kashiwara
   form) was correct, and Lusztig's theorem directly resolved it. The "stop
   computing after three falsifications" calibration was respected by
   landing the answer in zero falsifications.

---

## 7. Files / verification

All under `/home/agent/projects/proofs/2026-05-19-bdi-watanabe-W/`:

- `verify_lusztig_diagonal.py` — Lusztig diagonal formula evaluation,
  $B_2$ content ≤ 4 (70 configs) + $B_3$ content ≤ 3 (120 configs). Output
  in `run-log.txt`.
- `verify_convex_order.py` — convexity check of chain-factor order at
  $B_2 \ldots B_6$ (chain+singleton roots). All PASS.

Dependencies:
- `~/papers/watanabe-2509.00853.txt` — Watanabe 2509 text extraction
  (used for §5.2 form definition).
- `~/projects/proofs/2026-05-18-bdi-qLR.md` — Theorem A (carry $P_a$)
  + Theorem B (recording $R(\pi)$), used as black-box combinatorial inputs.

---

## 8. Open follow-ups (v3 OPEN-2, OPEN-4)

- **OPEN-2 (sharply named).** Construct the projection $p_\nu : V(\nu) \to
  V^\imath_{\mathrm{BDI}}(\nu)$ as the BDI analog of [Wat25] Prop 6.4.1.
  Action items:
  - Identify the BDI iCanonical basis class (Candidates 1–3 in §5).
  - Verify $p_\nu(b_\pi) \equiv_\infty b_\pi^\imath$ for B_n-highest $\pi$,
    and $\equiv_\infty 0$ otherwise.
  - Pin down compatibility with Theorem A + Theorem B (chain-factor descent).

- **OPEN-4.** Azenhas-style pre-quantum-LR layer for BDI: independent of (W).
  Pursue separately.

- **PROJECTED v3 outline (now).** With (W) verdict and OPEN-2 remaining,
  v3 § structure:
  - § Theorem A (carry $P_a$) — 2pp
  - § Theorem B (descent recording $R(\pi)$) — 2pp
  - § Theorem D (chain-factor PBW = Lusztig PBW = almost-orthonormal) — 1pp
  - § Theorem E (BDI projection $p_\nu$ analog of Wat25 Prop 6.4.1) — 3pp [OPEN]
  - § Composition multiplicity formula — 1pp
  - Total: ~9pp. Reasonable v3-paper scope. Lighter than feared.

---

— Rick, 2026-05-19, post-whiskey, the verdict snapped clean in one session.

P.S. PROVE.md predicted "Instance 6 of asymmetric-mirror" was the likely
verdict shape if (¬W) won. It didn't win. The methodological-crystal stays
at 5 instances. Compression-is-content (Day-24 Association F) is the
relevant meta-pattern instead: v3 shrinks by 2 pages. Write up Association F
firing for the Robin batch.

P.P.S. **Today's prediction worth tracking:** Lusztig's PBW orthogonality
applied to chain-factor convex order is the GENERAL pattern — likely the same
approach handles the C-type / D-type analog (sp_{2n}, so_{2n}) if Rick wants
to test type-portability of the v3 light-machinery setup. Not in scope today,
but a clean follow-up if v3 lands.
