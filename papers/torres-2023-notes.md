# Torres 2023 — "The Virtual Cactus Group and Littelmann Paths"

**arXiv:** 2302.11560 (v1, 22 Feb 2023). Published Electron. J. Combin. 31(1) (2024).
**Author:** Jacinta Torres (Jagiellonian, Krakow).
**Length:** 10 pages.

## 1. Main theorem (one sentence)
For each folding pair X -> Y (twisted into simply-laced), there is a group monomorphism Phi : J_X -> J_Y, s_I |-> prod_{tilde I} s^Y_{tilde I}, and the resulting "virtual cactus group" J_X^v acts on the Littelmann-path crystal P(psi(lambda)) compatibly with the Pan-Scrimshaw virtualization Psi : P(lambda) -> P(psi(lambda)) — i.e., the diagram with xi^X_I and tilde xi_{sigma(I)} commutes (Thm 4).

## 2. Does it cover type B? — YES, but only as virtualization.
Folding pairs treated explicitly (table p.4):
- C_n into A_{2n-1}
- B_{2n-1} into D_{2n}
- B_{2n} into D_{2n+1}
- G_2 into D_4
- F_4 into E_6

So **type B IS covered** as J_{B_n} \hookrightarrow J_{D_{n+1}} via folding D_{n+1} -> B_n (the standard fold collapsing the two end-nodes n, n+1 of D_{n+1}). Branching point x_0 = n-1 in B_n.

## 3. Level of the action
At the level of **Littelmann paths** (= concrete realization of B(lambda)), via partial Schutzenberger-Lusztig involutions xi_I. Equivalently on normal g-crystals (per Halacheva 2020, Thm 1). NOT canonical bases, NOT MV cycles. Concrete combinatorial paths.

## 4. Constructive or abstract?
**Constructive at the virtual level only.** The B-side action is defined as
    xi^B_I (pi) := Psi^{-1} ( prod_{tilde I in sigma(I)} xi^D_{tilde I} ) Psi(pi)
where Psi^{-1} is "explicitly computed by writing out the corresponding path in form (6)" (Thm 4 proof). So you compute by:
1. embed pi (B_n path) into a D_{n+1} path Psi(pi);
2. apply the type-D partial SL involutions on the connected components of sigma(I);
3. read coefficients back to recover the B_n path.

The action is constructive *modulo* a constructive type-D action — which is the Brown-Elek-Halacheva (2024) territory or Halacheva/HK by SL involutions. There is **no intrinsic B-level local rule** here; the B-action is defined by lifting to D.

## 5. Relation to Kamnitzer-Tingley / Rouquier-White
Not mentioned. No reference to KT or RW abstract guarantees, no reference to coboundary categories beyond Henriques-Kamnitzer [HJK04]. The paper sits firmly in the Halacheva-style crystal-combinatorial line.

## 6. Specific obstruction to type B singled out?
**No.** Type B is treated symmetrically with C, F_4, G_2 — just another folding. The paper does NOT identify or discuss any obstruction unique to B. It does NOT claim a *direct* (un-virtualized) combinatorial cactus action on B-crystals. Implicit message: the "intrinsic" B problem is sidestepped by virtualizing into D. (For Rick: this is exactly the gap — Torres gives B via D, not via B-native moves on (w, pi)-pairs.)

## 7. Kostant partitions / (w, pi) decoration of W?
**Not at all.** No mention of:
- Kostant partitions
- (Weyl, partition) pairs
- PBW / canonical basis monomials
- MV polytopes
- Lusztig parametrizations

Torres works purely with Littelmann paths and SL involutions — orthogonal language to Rick's Aug~ candidate.

## 8. Reading-priority verdict for Rick: **B (useful, not urgent)**
Worth a 30-minute skim, NOT a deep read. Reasons:

PRO:
- Confirms the "B via D folding" route works abstractly; Rick's intrinsic-B candidate must be at least *consistent* with this.
- Provides a clean sanity check: any genuine B-cactus realization must satisfy the cactus relations 1-3 (Def 1) — Rick can test Aug~ against these.
- The folding table (p.4) gives precise theta_X, theta_Y data that Rick will need when comparing his (w, pi) involution to the SL-involution-from-D shadow.

CON:
- Does NOT address the type-B *intrinsic* problem Rick is working on.
- No language overlap with Kostant partitions / W-decorated pairs.
- Short; mostly a clean generalization of [ATFT22] (Azenhas-Tarighat Feller-Torres on C).

**Action item for Rick:** for B_3 dominant spin pairs, compute the type-D partial SL involutions xi^D_{tilde I} on D_4 paths via Psi, project back, and compare to Aug~. If Aug~ agrees on a positive-density subset, the bipartite-oracle 798/798 success may be Aug~ recovering exactly the virtualized cactus; the 84% greedy ceiling would then be the obstruction to expressing the virtualized D_4 SL-involution by *local* B_3 moves — i.e., non-locality is essential.

**Read next instead:** Gossow-Yacobi 2023 (likely closer to (w, pi)-decoration / canonical basis language). Torres 2023 = reference, not next read.

## Bibliographic note
Cites [ATFT22] = Azenhas-Tarighat Feller-Torres 2207.08446 (symplectic cacti, C_n case). Cites [Hal20] = Halacheva. Cites [PS18] = Pan-Scrimshaw, the virtualization map for Littelmann paths. No citation to Brown-Elek-Halacheva (2024 — too late) nor to Kamnitzer-Tingley.
