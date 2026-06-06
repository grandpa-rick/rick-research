# Cross-chain ↔ iSerre structural bijection at $B_4$: VERDICT

**Date:** 2026-05-17
**Task:** Sub-problem 4 / C2 in `state/PROVE.md` — verify the 12 cross-chain monomials at $B_4$ are in structural bijection with iSerre (Letzter / Bao-Wang) nested-commutator monomials.

## TL;DR

**NO STRUCTURAL MATCH.** The cross-chain count $2(n-1)(n-2) = 12$ at $n=4$ matches no natural family of iSerre nested-commutator monomials in the split iquantum group $U^\iota$ of type $B_n$. The numerical coincidence at $n=3$ (4 = 4) was small-rank. The cross-chain class is a **tensor-product-rule combinatorial shadow**, not an iSerre-relation shadow. The conjecture **C2 (cross-chain ↔ iSerre)** as formulated in PROVE.md is **WRONG at the structural level**.

The categorical home of the cross-chain class is the *cross-factor interaction term* in the Watanabe-style tensor product rule from the v2 keystone (`memory/connections/short-long-tensor-product-rule.md`), not an iSerre nested-commutator relation.

---

## 1. The iSerre relation in precise form

We use the canonical Serre presentation for the split iquantum group $U^\iota$ of type $B_n$ (Satake diagram trivial involution $\tau = \mathrm{id}$, no black nodes), as given by Balagović–Kolb [BK15, Thm. 3.7] and consolidated in Chen–Lu–Wang [CLW20, Thm. 3.1, eqs. (3.7)–(3.9) / Rmk. 3.2 eq. (3.11)].

**For $i \neq j \in I$ with parameters $\varsigma_i$ (and $\tau = \mathrm{id}$):**

$$
\sum_{n=0}^{1-a_{ij}} (-1)^n \binom{1-a_{ij}}{n}_{q_i} B_i^n B_j B_i^{1-a_{ij}-n}
\;=\;
\begin{cases}
0 & \text{if } a_{ij} = 0, \\[2pt]
q_i \varsigma_i \, B_j & \text{if } a_{ij} = -1, \\[2pt]
-[2]^2_{q_i}\, q_i \varsigma_i \, (B_i B_j - B_j B_i) & \text{if } a_{ij} = -2.
\end{cases}
$$

[CLW20 (3.11), pp. 9–10, arXiv:1810.12475v4.]

The Cartan matrix of $B_4$ with the short simple labeled $\alpha_4$ has:
- $a_{i,j} = -1$ for adjacent long-long pairs $(1,2), (2,3)$ and for long-short $(3,4)$;
- $a_{4,3} = -2$ for the short-long edge in the reverse direction (short acting on long);
- $a_{i,j} = 0$ for non-adjacent pairs.

**Monomial counts per ordered pair $(i,j)$:**
- $a_{ij} = 0$ (commutator): 2 monomials.
- $a_{ij} = -1$ (Serre at $-1$): 3 LHS + 1 RHS = 4 monomials.
- $a_{ij} = -2$ (the short-long edge, in the $i = n$ direction): 4 LHS + 2 RHS = **6 monomials**.

The short-long edge produces **6 monomials**, independent of $n$. This is the relation Rick's PROVE.md targets.

---

## 2. The 12 cross-chain entries

From `2026-05-14-multiorbit-aug-b4/characterize_moves_b4.py`, the 12 cross-chain entries are the unordered pairs of $(\text{chain}, \text{primitive})$ with distinct chains:

| chain pair | primitives | count |
|------------|------------|-------|
| AB | TM+TM, TM+MB, MB+TM, MB+MB | 4 |
| AC | TM+TM, TM+MB, MB+TM, MB+MB | 4 |
| BC | TM+TM, TM+MB, MB+TM, MB+MB | 4 |

Each chain $a \in \{A, B, C\}$ corresponds to a *long* simple $\alpha_a$, and the primitives TM, MB are the two non-trivial $e_n$-actions on roots in chain $a$'s $\alpha_n$-string.

---

## 3. Candidate bijection schemes — all fail

Tested in `verify_identification.py`:

| Scheme | iSerre monomial subset | count |
|--------|------------------------|-------|
| 1 | LHS of all long-long iSerre at $B_4$ (i,j in {1,2,3}) | **16** ≠ 12 |
| 2 | All monomials of long-long iSerre | 20 ≠ 12 |
| 3 | All monomials of the $(4,3)$ short-long iSerre only | **6** ≠ 12 |
| 4 | All monomials of $(4,3) + (3,4)$ | 10 ≠ 12 |
| 5 | LHS-only of relations involving $B_4$ | 15 ≠ 12 |
| 6 | All monomials of relations involving $B_4$ | 18 ≠ 12 |
| 7 | LHS of unordered long-long Serre | 8 ≠ 12 |
| 8 | Tensor-product cross-factor interaction count | 12 ✓ (but this IS Rick's count itself, no shadow) |

**No fixed family of iSerre monomials gives 12 cleanly.** The closest count match (Scheme 1 = 16) fails by 4 — the four "non-adjacent" long-long commutator terms $\{B_1, B_3\}$. The count 12 only emerges under Scheme 8, which IS the combinatorial decomposition itself — not an external algebraic shadow.

---

## 4. Why no iSerre shadow can work — three independent obstructions

### (a) Locality vs n-dependence

The iSerre relations are LOCAL: each relation involves only one pair $(B_i, B_j)$. The short-long edge at $a_{n,n-1} = -2$ contributes exactly **6 monomials, independent of $n$**.

Rick's cross-chain count is $2(n-1)(n-2)$, which is **quadratic in $n$**.

A local relation cannot, by dimension counting, account for a quadratically growing combinatorial class.

### (b) Wrong adjacency structure

The cross-chain class at $B_4$ includes 4 entries for the **AC** chain pair (chains 1 and 3 in convex order). These are *non-adjacent* in the long-long Dynkin subdiagram ($a_{1,3} = 0$).

On the algebra side, $[B_1, B_3] = 0$ is a *commutator* relation, not a Serre relation. It has only 2 monomials, but cross-AC has 4 entries.

Any natural bijection "cross-chain pair AB ↔ iSerre relation $(B_1, B_2)$" would force "cross-chain pair AC ↔ commutator $(B_1, B_3)$" — but the monomial counts (4 vs 2) don't match.

### (c) Short-long count mismatch from below

The only iSerre relation directly involving the short simple $B_n$ is the $(n, n-1)$ short-long relation with 6 monomials. At $n=3$, cross-chain = 4 (off by 2); at $n=4$, cross-chain = 12 (off by 6); at $n=5$, cross-chain = 24 (off by 18). The discrepancy grows as $2(n-1)(n-2) - 6$.

---

## 5. What IS the right algebraic home? (Per v2 keystone)

The cross-chain class corresponds to the **cross-factor interaction term in the short-long-edge tensor product rule** (see `memory/connections/short-long-tensor-product-rule.md`, v2 keystone, 2026-05-16):

$$
\mathrm{Kp}(\infty)\big|_{B_n} \;\cong\; \bigotimes_{a=1}^{n-1} \mathcal{C}_a \;\otimes\; \mathcal{C}_{\mathrm{sing}}.
$$

Each chain factor $\mathcal{C}_a$ contributes 2 step types (TM, MB). The cross-chain class is **structurally** $\binom{n-1}{2} \times 2 \times 2$ = (pairs of factors) × (primitive choice per factor), giving $2(n-1)(n-2)$. This is the **second-order tensor-product interaction** — the analogue of the $\delta a \otimes \delta b$ correction in $e_n^2(\pi^{(1)} \otimes \pi^{(2)})$.

This is the genuine structural home of cross-chain. **It is NOT an iSerre relation in $U^\iota$**; it is the *crystal-level shadow* of the iSerre's nonlocality — the way iSerre information propagates as $e_n$ squared crosses chain boundaries via cancellation in the CST bracketing.

---

## 6. The "match at $n=3$" was small-rank coincidence

The "4 = 4 at $n=3$" calibration was a coincidence: the iSerre short-long relation at $a_{ij} = -2$ has **6 monomials**, not 4. The original "4 monomials" figure (in the previous Watanabe-quartic analysis, 2026-05-16) came from counting only the LHS expansion of the triple commutator $[B,[B,[B,X]]]$ — i.e., dropping the inhomogeneous RHS. That's not the full iSerre relation.

Even accepting "4 = LHS expansion", the count at $n=4$ would need a count growing quadratically in $n$ from a single fixed nested-commutator structure, which is structurally impossible.

---

## 7. Verdict and downstream implications

**Verdict on Sub-problem 4 / C2:**
- **STRUCTURAL MATCH:** ✗ NO.
- **PARTIAL MATCH:** ✗ NO (no natural restriction or count gives 12 structurally).
- **NO MATCH:** ✓ CONFIRMED.

**Downstream:**
1. C2 in PROVE.md needs to be retired or reformulated. The cross-chain class does NOT shadow iSerre.
2. The v2 keystone (`short-long-tensor-product-rule.md`) is *strengthened*, not weakened, by this negative result: the cross-chain class is the cross-factor interaction term of the tensor product rule, full stop. No external algebraic identification needed.
3. The dream-cycle reframing `memory/connections/watanabe-quartic-as-cross-chain-CONFIRMED.md` should be downgraded from ⭐⭐⭐⭐ to ⭐⭐ — the count match at $n=3,4,5$ via "$2 \times$ ordered pairs" is real, but it is the natural count of (ordered pair of chains) $\times$ (primitive choice per chain), not an iSerre count.

---

## 8. Open question — the ONE next step

The cross-chain class has structural count $2(n-1)(n-2)$ that exactly equals $2 \times$ (ordered pairs of distinct long simples). This is also the count of *off-diagonal commutator monomials* $[B_a, B_b]$ (for $a \neq b$ in $\{1, \ldots, n-1\}$, ordered, $\times 2$ for the two terms) in the long-simple subalgebra of $U^\iota$.

**Question:** Is the cross-chain class in structural bijection with the *2-element subsets of the long-long commutator monomials at the long-simple subalgebra* — i.e., not with iSerre nested commutators, but with the *commutativity ideal* of the chains-as-tensor-factors? This would be a cleaner algebraic shadow ("tensor factors commute up to interaction") and would automatically be quadratic in $n$. Worth testing at $B_5$ where cross-chain = 24.

---

## 9. References

- **Balagović–Kolb 2015**, arXiv:1507.06276, "Universal K-matrix for quantum symmetric pairs." Defines $B_c$ algebra and the general bar-involution / Serre framework (§5).
- **Chen–Lu–Wang 2020**, arXiv:1810.12475v4, "A Serre presentation for the $\iota$quantum groups." Theorem 3.1, eqs. (3.7)-(3.9); explicit relations for $|a_{ij}| \leq 3$ in eq. (3.11), Remark 3.2 (pp. 9-10).
- **Bao–Wang 2018**, Astérisque 402 / arXiv:1310.0103, "A new approach to Kazhdan-Lusztig theory of type B via quantum symmetric pairs." Definition of $U^\iota$ (Ch. 2 §1), with explicit cubic/quartic relations involving the $t$-generator (pp. 24–25, eqs. on p. 24).
- **Letzter 2003**, "Coideal subalgebras and quantum symmetric pairs." Original Serre presentation for finite type (Theorem 7.4, cited in CLW Remark 3.1).
- **Kolb 2014**, Adv. Math. arXiv:1207.6036, "Quantum symmetric Kac-Moody pairs." Theorems 7.4, 7.8 for $a_{ij} \in \{0,-1,-2\}$.

## 10. Files

- `/home/agent/projects/proofs/2026-05-17-iSerre-cross-chain-b4/verify_identification.py` — the bijection-tester.
- `/home/agent/papers/balagovic-kolb-1507.06276.pdf`, `/home/agent/papers/CLW-1810.12475.pdf`, `/home/agent/papers/bao-wang-1310.0103.pdf` — local cached PDFs.
- `/home/agent/projects/proofs/2026-05-14-multiorbit-aug-b4/characterize_moves_b4.py` — cross-chain catalog source.
- `/home/agent/projects/memory/connections/short-long-tensor-product-rule.md` — v2 keystone (the right home for cross-chain).
- `/home/agent/projects/memory/connections/watanabe-quartic-as-cross-chain-CONFIRMED.md` — needs downgrading per §7 above.
