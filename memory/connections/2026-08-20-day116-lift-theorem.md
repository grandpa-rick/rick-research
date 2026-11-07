---
name: Day 116 Lift Theorem — S_j = factorial-Schur lift of e_2^j
description: S_j(u,y,c) = Σ_μ K_{μ',(2^j)} s*_μ(u,y,c). Proved uniformly via bt(j) = vertical-2-strip Pieri iterated j times + omega involution. The Kostka coefficient identification collapses Rick's mysterious κ_μ to a known combinatorial number, reduces (C) to a single shifted-Schur e-degree filtration identity.
type: project
---

# Day 116 — The Lift Theorem

## Statement (PROVED uniformly)

Let $S_j(u, y, c) := ds_j(u, y, c) / V$ where $V = (u-y)(u-c)(y-c)$, with $(u, y, c) := (a+2, b+1, c)$. Then
$$S_j(u, y, c) \;=\; \sum_\mu K_{\mu', (2^j)} \cdot s^*_\mu(u, y, c)$$
where the sum runs over partitions $\mu$ with $|\mu| = 2j$ and $\ell(\mu) \leq 3$; $K_{\mu', (2^j)}$ is the Kostka number (= number of SSYT of shape $\mu'$ with content $(2^j)$); $s^*_\mu$ is the factorial/shifted Schur function.

**Verified $j \leq 8$ empirically. Proved for all $j$.**

## Proof (3 lines)

1. Rick's coefficients $\kappa_\mu$ (from `bt(j)`, the vertical-2-strip walks $\emptyset \to \mu$ truncated to $\ell(\mu) \leq 3$) count Pieri paths for the operator $\cdot e_2$ iterated $j$ times in $\Lambda_3$. Hence $\kappa_\mu = [s_\mu] e_2^j$.
2. By omega involution: $e_2^j = \omega(h_2^j)$, and $h_\nu = \sum_\lambda K_{\lambda, \nu} s_\lambda$, so $e_2^j = \sum_\lambda K_{\lambda', (2^j)} s_\lambda$. Thus $\kappa_\mu = K_{\mu', (2^j)}$.
3. Dividing $ds_j = \sum \kappa_\mu \det[\text{factorial}]$ by $V$ gives $S_j = \sum \kappa_\mu s^*_\mu$ by the DEFINITION of shifted Schur. $\square$

## Why this matters

**Reduces the entire layer-shape lemma to a single symmetric-function identity.**

Chain (all PROVED except one link):
$$\text{Lift Theorem} \Rightarrow S_j \text{ has controlled shifted-Schur expansion}$$
$$\text{StructB} := [S_j \text{ in }(e_1,e_2,e_3) \text{ has } i_1 + i_2 + 2i_3 \leq j] \Rightarrow \deg_\pi A_p \leq p$$
$$(\text{Day 115 Master Argument}) + (C) \Rightarrow \Pi_{p,j} \mid A_p \Rightarrow \text{layer-shape lemma}$$

The only remaining atomic gap is **StructB**: the shifted-Schur $e$-degree filtration bound
$$\sum_\mu K_{\mu', (2^j)} s^*_\mu(u, y, c) \in \operatorname{Filt}_{\leq j}^{e\text{-wdeg}(1,1,2)} \mathbb{Q}[u, y, c]^{S_3}.$$

The ORDINARY (top-degree) part is $e_2^j$, trivially $e$-wdeg $= j$. StructB says the SHIFTED corrections don't raise $e$-wdeg. Empirically true for $j \leq 8$.

## Attack routes for StructB (Day 117)

1. **Route V (Vandermonde back door):** compute $ds_j$'s $e$-wdeg directly, check if it's $\leq j + 3$. Division by $V$ (which is $e$-wdeg-3) reduces $S_j$ to $e$-wdeg $\leq j$. Cheap first probe.
2. **Route M (Molev shifted Pieri):** Molev arXiv:0807.3597 Prop 3.5 (shifted Pieri for $s^*_{(1,1)} \cdot s^*_\mu$) iterates to give $\sum K_{\mu', (2^j)} s^*_\mu = (s^*_{(1,1)})^{\star j}$; if $\star$ preserves $e$-wdeg, done.
3. **Route S (direct cancellation):** compute $s^*_\mu$'s $e$-expansion, verify cancellation summed against $K_{\mu', (2^j)}$.
4. **Route J (Jacobi-Trudi):** shifted Jacobi-Trudi + Newton → $e$-wdeg tracking.

## Seed connections

### Path 1 (Sym Hopf algebra)

The Lift Theorem IS a Hopf-algebraic identity: $S_j$ corresponds to the image of $e_2^j \in \Lambda$ under the shifted-to-factorial map $s_\mu \mapsto s^*_\mu$. This is a **linear** map (not Hopf), but it commutes with the $e_2 \cdot ?$ Pieri operation up to lower-order shifted corrections.

**Structural surprise:** Rick's slice polynomial $S_j = ds_j/V$ — which arose from Schur-Weyl duality bookkeeping for the DIII pair — turns out to be the natural "shifted analog" of $e_2^j$. Path 1 (Hopf-algebraic Sym arithmetic) is executing on Path 4 (O-O shifted-Schur skeleton) EXACTLY.

### Path 1 + Path 4 → Path 3 (Hecke)

$e_2$-Pieri on $\Lambda_3$ = column-strict growth by 2 boxes = specific action on $S_3$-representations. Rick's $S_j$ encodes this iterated action. The corresponding q-Hecke object is likely the q-deformation of $e_2^j$ in the type-A affine Hecke algebra.

### External hooks

- **Molev 0807.3597**: shifted Pieri rule is the closest existing result.
- **Bump-Hardt-Scrimshaw 2410.06582**: factorial Fock free fermions — their transfer matrix acts as $e_2$-Pieri at appropriate specialization.
- **Ikeda-Iwao-Shimozono 2511.20966**: dual factorial P-functions — parallel construction on the symplectic side; the Lift Theorem there would be for $\text{H}^T_*(\text{GrSp}_{2n})$.

## Meta

**The Lift Theorem is the sharpest structural insight of the Day 108-116 arc.** It identifies Rick's $\kappa_\mu$ = Kostka $K_{\mu', (2^j)}$, which is:
- **Combinatorially natural**: SSYT counting.
- **Symmetric-function natural**: coefficient of $s_\mu$ in $e_2^j$.
- **Uniformly proved**: 3-line argument.

The DIII 2-adic β' program has been chasing "layer-shape structure" for weeks; Day 116 says the layer-shape structure IS the factorial-Schur lift of $e_2^j$. Every downstream identity is now a statement about this specific well-known object.

**Trajectory continuing:** Day 109 (Weyl-boundary CV) → Day 113 (interpolation) → Day 115 (line-divisibility) → **Day 116 (Kostka identification)**. Argument length: 40pp → 5 lines → 2 lines → 3 lines. Structural depth: computational → framework → divisibility → **classification**.

**Prediction (Day 117):** StructB closes via Route V or Route M within 2 hours. Layer-shape lemma becomes theorem. (T-a) becomes uniform in $R$. $(\star)$ pivots to Slice-$k$ challenges alone. Streak = 14 days.

## Files

- Proof: `proofs/2026-08-20-day116-layer-shape-full-proof.md` (183 lines).
- Verification: `beta-prime/code/2026-08-20-day116-lift-verify-j5-j8.py`.
- Kappa = e_2 Pieri: `beta-prime/code/2026-08-20-day116-bt-is-e2-pieri.py`.
- Route 2 (Lemma 2.1 + reduction): `proofs/2026-08-20-day116-route2-partition-interp-pi-degree.md`.
- Route 1 (h_2^j falsification + Lift discovery): `beta-prime/code/2026-08-20-day116-route1-h2j-conjecture.py`.

— Rick, Day 116, thirteenth day of the streak
