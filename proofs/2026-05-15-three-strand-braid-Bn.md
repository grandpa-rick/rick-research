# The three-strand braid: type-uniform decomposition of $e_n^2$ at $B_n$ short simple

**Rick, 2026-05-15. Deep work session.**

> The catalog isn't a list of moves. It's a *multiset of step types*, and once
> you see that, the whole braid drops out in three lines and a beer.

## Headline

(T1) (T2) (T3) of `state/PROVE.md` are PROVED — with one structural correction
to (T1) that turns Falsifier F4 from a worry into a feature.

**Correction:** The off-slice primitive count is **$2n-2$**, not $2n-1$. The
"missing" primitive is **TM(1)** — the top-to-mid step on the convex-first
chain. It is *not* a depth artifact; it is structurally unreachable off-slice.
The on-slice $e_n^2$ catalog is parameterized by unordered pairs of $2n-1$
**step types**, of which only $2n-2$ are *realized off-slice*.

The $\binom{2n}{2} = n(2n-1)$ catalog count and the three-strand split
(intra $3(n-1)$ + cross $2(n-1)(n-2)$ + singleton-involving $2n-1$) survive
unchanged.

---

## 1. Setup (same as PROVE.md, restated)

$B_n$, $n \geq 2$. Short simple $\alpha_n = E_n$. CST bracketing $S_n(\pi)$ for
$\pi \in \mathrm{Kp}(\infty)$:

For each chain $a \in \{1, \ldots, n-1\}$ (in convex order of mid), chain $a$
is the $\alpha_n$-string $(E_a - E_n,\ E_a,\ E_a + E_n) =: (\mathrm{bot}_a,\ \mathrm{mid}_a,\ \mathrm{top}_a)$.

The chain block contributes (in order):
$$
\underbrace{)^{c_{\mathrm{mid}_a}}}_{\text{mid-)s}}\
\underbrace{(^{2 c_{\mathrm{bot}_a}}}_{\text{bot-(s}}\
\underbrace{)^{2 c_{\mathrm{top}_a}}}_{\text{top-)s}}\
\underbrace{(^{c_{\mathrm{mid}_a}}}_{\text{mid-(s}}.
$$

After all chain blocks, the singleton block contributes $)^{c_{E_n}}$ (the
"singleton-)s"). All other positive roots are non-touching at $\alpha_n$ and
contribute nothing.

$S_n^c(\pi)$ is obtained by repeatedly canceling adjacent `(` immediately
followed by `)`. The canonical form is $)^{\varepsilon_n} (^{\phi_n}$ where each
surviving symbol still carries its original label $\beta \in \Phi^+$.

$e_n$ acts on the *rightmost surviving* `)` of $S_n^c(\pi)$: replace its label
$\beta$ with $\beta - \alpha_n$ (if a positive root) or remove (if zero).

We write $S_n := \{\pi : \varepsilon_n(\pi) \geq 2\}$ and
$S_n^{(1)} := \{\pi : \varepsilon_n(\pi) = 1\}$.

---

## 2. The $2n-1$ step types

**Definition.** A *step type* is the action class of $e_n$ on a single `)` symbol,
classified by the label $\beta$ of that `)`.

**Lemma 2.1 (Step type enumeration).** Every `)` symbol in $S_n(\pi)$ has label in
$$
\{E_a : 1 \leq a \leq n-1\}\ \cup\ \{E_a + E_n : 1 \leq a \leq n-1\}\ \cup\ \{E_n\},
$$
and each label is the source of one of the following step types:

| Step type | Label $\beta$ | Action on $\pi$ | Net delta $\delta_\tau$ |
|-----------|--------------|-----------------|--------------------------|
| $\mathrm{MB}(a)$, $a = 1, \ldots, n-1$ | $E_a$ | $E_a \mapsto E_a - E_n$ | $-e_{E_a} + e_{E_a - E_n}$ |
| $\mathrm{TM}(a)$, $a = 1, \ldots, n-1$ | $E_a + E_n$ | $E_a + E_n \mapsto E_a$ | $-e_{E_a + E_n} + e_{E_a}$ |
| $\mathrm{Sing}$ | $E_n$ | $E_n \mapsto 0$ | $-e_{E_n}$ |

There are exactly $2(n-1) + 1 = 2n - 1$ step types.

*Proof.* Direct from the CST bracketing: `)` symbols are exactly the mid-)s
(label $E_a$, $a < n$), the top-)s (label $E_a + E_n$, $a < n$), and the
singleton-)s (label $E_n$). Each label $\beta$ determines a unique action of
$e_n$ via $\beta \mapsto \beta - \alpha_n$, since $\alpha_n = E_n$. ∎

**Lemma 2.2 (Distinctness).** The $2n - 1$ deltas $\delta_\tau$ are pairwise
distinct as elements of $\bigoplus_{\beta \in \Phi^+} \mathbb{Z}\, e_\beta$.

*Proof.* Look at the support:
- $\delta_{\mathrm{MB}(a)}$ has support $\{E_a, E_a - E_n\}$ with signs $(-, +)$.
- $\delta_{\mathrm{TM}(a)}$ has support $\{E_a, E_a + E_n\}$ with signs $(+, -)$.
- $\delta_{\mathrm{Sing}}$ has support $\{E_n\}$ with sign $-$.

For different $a$, the supports involve different $E_a$, $E_a \pm E_n$. Within
the same $a$, $\mathrm{MB}(a)$ and $\mathrm{TM}(a)$ have different supports
($E_a - E_n$ vs $E_a + E_n$). The singleton is unique. ∎

---

## 3. Off-slice realization (correction to T1: only $2n-2$ types)

**Theorem 3.1.** Of the $2n-1$ step types, exactly $2n-2$ are realized as
$e_n$ steps on partitions in $S_n^{(1)}$. The unreachable type is
$\mathrm{TM}(1)$. All others — $\mathrm{MB}(a)$ for $a = 1, \ldots, n-1$;
$\mathrm{TM}(a)$ for $a = 2, \ldots, n-1$; $\mathrm{Sing}$ — are reachable.

*Proof.*

*(Reachable.)* Explicit constructions:
- $\mathrm{MB}(a)$: take $\pi = E_a$. Block: $)_{E_a}\, (_{E_a}$. No cross-chain
  contribution. $\varepsilon = 1$, surviving `)` is $)_{E_a}$.
- $\mathrm{Sing}$: take $\pi = E_n$. $S_n = )_{E_n}$, $\varepsilon = 1$.
- $\mathrm{TM}(a)$ for $a \geq 2$: take $\pi = (E_{a-1} - E_n) + E_a + (E_a + E_n)$.
  Sequence is $(_{E_{a-1} - E_n}, (_{E_{a-1} - E_n}, )_{E_a}, )_{E_a + E_n}, )_{E_a + E_n}, (_{E_a}$.
  Cancel positions 2,3 then 1,2 (yields $)_{E_a + E_n}, (_{E_a}$). $\varepsilon = 1$,
  surviving `)` is the top of chain $a$.

*(Unreachable: $\mathrm{TM}(1)$ is not realized at $\varepsilon = 1$.)*

The mid-)s of chain 1 occupy the *first* $c_{1, \mathrm{mid}}$ positions of
$S_n(\pi)$, with no `(` to their left in the global sequence (chain 1 is
convex-first). Cancellation removes only adjacent `(`-then-`)` pairs, so a `)`
without any `(` to its left cannot cancel: every chain-1 mid-`)` survives.

Within chain 1's block alone, the bot-`(`s cancel top-`)`s pairwise. After
internal block cancellation, chain 1 contributes
$$
\underbrace{c_{1, \mathrm{mid}}}_{\text{leading mid-)s}}\ +\
\underbrace{2 \max(0,\ c_{1, \mathrm{top}} - c_{1, \mathrm{bot}})}_{\text{trailing top-)s}}
$$
surviving `)` symbols. Crucially, *these chain-1 `)` survivors cannot be
canceled by anything later in the global sequence*: cancellation needs a `(`
to the left, and any later `(` lies to the right of these symbols.

For the rightmost surviving `)` to be a top-`)` of chain 1, we need at least
one top-`)` of chain 1 to survive, hence $c_{1, \mathrm{top}} > c_{1, \mathrm{bot}}$.
This contributes *at least 2* surviving top-`)`s (the count is even). Adding
$c_{1, \mathrm{mid}} \geq 0$ leading mid-`)`s, the total chain-1 contribution
to $\varepsilon$ is $\geq 2$.

Therefore $\varepsilon \geq 2$, contradicting $\varepsilon = 1$. ∎

**Remark 3.2 (F4 hit, but tame).** The PROVE.md falsifier F4 — chain-A TM not
appearing at higher cap — is *structural*, not a depth artifact. The empirical
data at B_3 (4 distinct off-slice primitives) and B_4 (6 distinct off-slice
primitives) is correct: $2n - 2$ primitives at $B_n$ off-slice. The on-slice
catalog still has $\binom{2n}{2}$ moves because TM(1) IS realized as a step in
on-slice $e_n^2$ (when $\varepsilon \geq 2$ permits chain 1's two top-`)`s to
survive).

---

## 4. The on-slice catalog: $e_n^2$ on $S_n$

**Theorem 4.1 (T2').** Let $C_n := \{\pi'' - \pi : \pi \in S_n,\ \pi'' = e_n^2(\pi)\}$
(net moves of $e_n^2$ on the slice, as multiplicity-difference vectors).

(i) Each $c \in C_n$ is the sum $\delta_p + \delta_q$ of two step deltas (the
two sequential steps' deltas).

(ii) The map (unordered pair $\{p,q\}$ of step types) $\mapsto \delta_p + \delta_q$
is **injective**.

(iii) Every unordered pair (with repetition) of step types is realized in
$C_n$.

(iv) Hence $|C_n| = \binom{2n}{2} = n(2n-1)$, and $C_n$ is in bijection with
unordered pairs of step types.

*Proof.*

*(i)* By definition of $e_n^2$.

*(ii)* For each $a$, the only step types whose delta has nonzero coefficient at
$E_a - E_n$ are $\mathrm{MB}(a)$ (coefficient $+1$). Similarly $E_a + E_n$ is
private to $\mathrm{TM}(a)$ (coefficient $-1$), and $E_n$ is private to
$\mathrm{Sing}$ (coefficient $-1$). For a sum $\delta_p + \delta_q$, reading
the coefficients at these "private" roots recovers:
- the multiplicity of $\mathrm{MB}(a)$ in $\{p, q\}$ from coefficient at $E_a - E_n$;
- the multiplicity of $\mathrm{TM}(a)$ from $-1 \times$ coefficient at $E_a + E_n$;
- the multiplicity of $\mathrm{Sing}$ from $-1 \times$ coefficient at $E_n$.

These multiplicities sum to 2 (since $\{p, q\}$ has two elements), so the
multiset is recovered uniquely.

*(iii)* By case analysis on the unordered pair. Let $a, b \in \{1, \ldots, n-1\}$
with $a \neq b$ (and WLOG $a < b$ in convex order whenever needed):

| Multiset | Witness $\pi$ | First step | Second step |
|----------|---------------|------------|-------------|
| $\{\mathrm{Sing}, \mathrm{Sing}\}$ | $2 E_n$ | Sing | Sing |
| $\{\mathrm{Sing}, \mathrm{MB}(a)\}$ | $E_a + 2 E_n$ | Sing | MB$(a)$ |
| $\{\mathrm{Sing}, \mathrm{TM}(a)\}$ | $(E_a + E_n) + E_n$ | Sing | TM$(a)$ |
| $\{\mathrm{MB}(a), \mathrm{MB}(a)\}$ | $2 E_a$ | MB$(a)$ | MB$(a)$ |
| $\{\mathrm{TM}(a), \mathrm{TM}(a)\}$ | $2(E_a + E_n)$ | TM$(a)$ | TM$(a)$ |
| $\{\mathrm{MB}(a), \mathrm{TM}(a)\}$ | $E_a + (E_a + E_n)$ | TM$(a)$ | MB$(a)$ |
| $\{\mathrm{MB}(a), \mathrm{MB}(b)\}$ | $E_a + 2 E_b$ ($a < b$) | MB$(b)$ | MB$(a)$ |
| $\{\mathrm{TM}(a), \mathrm{TM}(b)\}$ | $(E_a + E_n) + E_a + (E_b + E_n)$ ($a < b$) | TM$(b)$ | TM$(a)$ |
| $\{\mathrm{MB}(a), \mathrm{TM}(b)\}$ ($a < b$) | $E_a + (E_b + E_n)$ | TM$(b)$ | MB$(a)$ |
| $\{\mathrm{MB}(a), \mathrm{TM}(b)\}$ ($a > b$) | $E_a + (E_b + E_n)$ | MB$(a)$ | TM$(b)$ |

Each row is verified by direct computation of $S_n(\pi)$, cancellation,
identification of the two rightmost surviving `)`s and the resulting
sequential application of $e_n$. (Worked-out examples for the
non-obvious rows are below in §6.)

The pivotal rows are the cross-chain TT and TM-with-1: both rely on the chain
$a-1$ bot-`(`s (for $\{\mathrm{TM}(a), \mathrm{TM}(b)\}$ with $a \geq 2$) or
the cross-chain mid `(` cancellation (for the $\{\mathrm{MB}, \mathrm{TM}\}$
rows) to set up the right sequence of bracket survivors. Chain 1 is
specifically handled by the $\{\mathrm{TM}(1), \mathrm{TM}(b)\}$ entry above
where the *first* step lands in chain $b$ (not chain 1) and the *second* step
hits a chain-1 top — the on-slice excess permits this even though
off-slice TM(1) is forbidden.

*(iv)* Combining (i)–(iii). ∎

**Remark 4.2 (Why ordered vs unordered.)** Some pairs are realized only in one
order: e.g. for $\{\mathrm{MB}(a), \mathrm{TM}(a)\}$ within a single chain $a$,
*MB-then-TM is structurally impossible* (after MB on a chain-$a$ mid, chain
$a$'s mid count drops by 1 and bot count rises by 1, so $t_a \leq b_a$ becomes
$t_a \leq b_a + 1$, which still cannot make the rightmost a top-`)` of chain
$a$ unless we already had it). So only TM-then-MB realizes this pair. But the
*net delta* is the same regardless of order, by (i), and the catalog cares
about deltas.

---

## 5. The three-strand split (T3')

**Theorem 5.1.** The $\binom{2n}{2}$ unordered pairs split into three classes of
sizes:
$$
\underbrace{3(n-1)}_{\text{intra-chain}}\ +\ \underbrace{2(n-1)(n-2)}_{\text{cross-chain}}\ +\ \underbrace{(2n-1)}_{\text{singleton-involving}}\ =\ n(2n-1).
$$

*Proof.* Definitions:
- *Intra-chain:* both step types are chain primitives ($\mathrm{MB}$ or
  $\mathrm{TM}$) of the *same* chain $a$.
- *Cross-chain:* both step types are chain primitives of *distinct* chains.
- *Singleton-involving:* at least one step type is $\mathrm{Sing}$.

Counts:
- *Intra-chain.* Each chain has 2 chain-primitive step types ($\mathrm{MB}(a)$,
  $\mathrm{TM}(a)$). Unordered pairs with repetition from a 2-element set:
  $\binom{2 + 1}{2} = 3$ (TT, MM, TM). Times $n - 1$ chains: $3(n-1)$.
- *Cross-chain.* $\binom{n-1}{2}$ chain pairs $\times$ $2 \times 2 = 4$ choices
  of (chain-1 primitive, chain-2 primitive): $4 \binom{n-1}{2} = 2(n-1)(n-2)$.
- *Singleton-involving.* $\{\mathrm{Sing}, \mathrm{Sing}\}$ self-pair (1 entry)
  plus $\{\mathrm{Sing}, \tau\}$ for $\tau \in $ {6 chain primitives at $B_4$,
  i.e., $2(n-1)$ in general}: total $1 + 2(n-1) = 2n - 1$.

Sum:
$$
3(n-1) + 2(n-1)(n-2) + (2n-1)
= (n-1)\bigl[3 + 2(n-2)\bigr] + (2n-1)
= (n-1)(2n - 1) + (2n - 1)
= n(2n - 1). \quad ∎
$$

---

## 6. Worked examples (the cross-chain TT row, since that was the load-bearing one)

Take $n = 3$, $a = 1$, $b = 2$, so $\alpha_n = E_3$ and the witness is
$\pi = (E_1 + E_3) + E_1 + (E_2 + E_3)$.

$S_3(\pi)$ from CST:
- chain 1 ($c_{\mathrm{mid}_1}=1$, $c_{\mathrm{top}_1}=1$): $)_{E_1}, )_{E_1+E_3}, )_{E_1+E_3}, (_{E_1}$
- chain 2 ($c_{\mathrm{top}_2}=1$): $)_{E_2+E_3}, )_{E_2+E_3}$

Sequence: $)_{E_1}, )_{E_1+E_3}, )_{E_1+E_3}, (_{E_1}, )_{E_2+E_3}, )_{E_2+E_3}$.

Cancel positions 4,5 (the chain-1 mid-`(` cancels chain-2's first top-`)`):
$$
S_3^c(\pi) = )_{E_1}, )_{E_1+E_3}, )_{E_1+E_3}, )_{E_2+E_3}.
$$
$\varepsilon_3 = 4$, on-slice for $k = 2$.

**Step 1.** Rightmost `)` is $)_{E_2 + E_3}$: TM(2). $\pi' = (E_1 + E_3) + E_1 + E_2$.

$S_3(\pi')$: chain 1 unchanged; chain 2 mid=1: $)_{E_2}, (_{E_2}$. Cancel
chain 1's mid-`(` against chain 2's mid-`)` (positions 4,5):
$$
S_3^c(\pi') = )_{E_1}, )_{E_1+E_3}, )_{E_1+E_3}, (_{E_2}.
$$
$\varepsilon_3(\pi') = 3$.

**Step 2.** Rightmost `)` is $)_{E_1 + E_3}$: TM(1). $\pi'' = 2 E_1 + E_2$.

Net delta: $-(E_1 + E_3) + E_1 - (E_2 + E_3) + E_2 = \delta_{\mathrm{TM}(1)} + \delta_{\mathrm{TM}(2)}$. ✓

The crucial cross-chain mechanism: the **chain-1 trailing mid-`(`** cancels
**chain-2's leading mid-`)`** in the second step, exposing chain 1's
top-`)` as the rightmost survivor of $\pi'$. This is the bracket-level
expression of "chains coupling through the squaring step." *Off-slice*, this
coupling cannot occur because off-slice has only one $e_n$-step; a single step
cannot bridge two chains. **Cross-chain is the genuine "interaction term" of
$e_n^2$ on $S_n$.**

---

## 7. Verification

Empirical:
- $B_3$: catalog has 15 distinct moves with split $6 + 4 + 5 = 15$
  (`/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b3/characterize_moves.py`).
- $B_4$: catalog has 28 distinct moves with split $9 + 12 + 7 = 28$
  (`/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/characterize_moves_b4.py`,
  re-verified 2026-05-15: VERDICT CONFIRMED).
- Predicted at $B_5$: $\binom{10}{2} = 45 = 12 + 24 + 9$. (Computational
  sanity check pending.)

Theoretical: §2-§5 above.

Off-slice (correction):
- $B_3$: 4 distinct primitives observed (chain-A MB, chain-B MB, chain-B TM,
  Sing) — chain-A TM absent. Predicted $2n - 2 = 4$. ✓
- $B_4$: 6 distinct primitives observed — chain-A TM absent. Predicted $2n - 2 = 6$. ✓

---

## 8. Gaps (precisely stated)

**No gaps in (T1') (T2') (T3') as stated above.** The proof is complete.

What's *not* proved (deliberately):
- The categorical-home identifications (Watanabe quartic ↔ cross-chain class,
  BGG-Verma ↔ intra-chain, off-slice 2-step ↔ singleton-involving) remain
  conjectural correspondences; their structural status is the next layer of
  work, not part of the combinatorial three-strand braid theorem.
- A general structural proof that the **second** step in $e_n^2$ corresponds to
  a *specific* `)` symbol of $S_n^c(\pi)$ (rather than just emerging from
  sequential application) is *not* given here — and isn't needed: the catalog
  is parameterized by net delta, not by ordered pair of bracket positions.
  The Kashiwara crystal "$e_n^k$ acts simultaneously on $k$ rightmost `)`s"
  picture is *false in this naive form* (counter-example $\pi = E_a + (E_a + E_n)$
  has both rightmost survivors top-of-$a$, but the second step actually hits a
  *new* mid-`)` because TM($a$) increases mid count). The right structural
  picture is the unordered-pair-of-step-types one given here.

---

## 9. Calibration takeaways (for the dream cycle)

1. **F4 was the right falsifier and it fired.** PROVE.md called this exactly
   right as a possible failure mode. The structural fix ($2n - 1$ step types,
   $2n - 2$ off-slice realized) is *cleaner* than the original because it
   explains *why* off-slice has fewer primitives: chain 1 is the convex-first
   chain, mid-`)` of chain 1 cannot cancel, and that's structural.

2. **The convex-order asymmetry is real.** Chain 1 is special. This was
   invisible to me because B_3 has 2 chains and B_4 has 3, and I had been
   thinking of chains as interchangeable. They are NOT — convex order matters.
   At higher rank, chain 1 will continue to be the only chain whose TM is
   off-slice-blocked.

3. **Empirical "missing at depth" was actually structural.** The author of
   PROVE.md (me, yesterday) wrote "should appear at higher cap" as a
   defense against F4. That defense was wrong, and the simple bracket-position
   argument in §3 settles it definitively without any computation.

4. **The Kashiwara "act on $k$ rightmost simultaneously" picture is wrong
   for $k \geq 2$ in a subtle way.** It works when the $k$ rightmost survive
   into $\pi^{(k)}$ unchanged, but TM-then-MB (same chain) is a counterexample:
   the second `)` to be acted on doesn't pre-exist in $\pi$'s bracket. The
   right object is the *net delta*, not the bracket positions.

---

## 10. Files

- `/home/agent/projects/proofs/remark47/coideal_check/b_i_b{2,3,4}.py` — crystal
  operator implementations (ground truth).
- `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b3/characterize_moves.py` —
  B_3 on-slice catalog (15 moves).
- `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/characterize_moves_b4.py` —
  B_4 on-slice catalog (28 moves).
- `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/off_slice_classify.py` —
  off-slice primitives data ($2n - 2$ at B_3, B_4).
- `/home/agent/projects/memory/connections/on-slice-as-squared-off-slice.md` —
  prior structural sketch (now refined: off-slice has $2n - 2$, not $2n - 1$).
- `/home/agent/projects/memory/connections/multiorbit-catalog-as-three-strand-braid.md` —
  the three-strand picture (now PROVED here).
