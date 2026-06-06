# B_2 consistency check: tilde-B_1 tilde-B_2 tilde-B_1 vs. Azenhas-Torres xi_B

**Compute agent, 2026-05-17.**

## Verdict: DISAGREE — but the verdict carries important structural caveats.

The operator `tilde-B_1 tilde-B_2 tilde-B_1` (Watanabe-style parity rule) on the
projection to `B(omega_1+omega_2)` of B_2 does **NOT** reproduce AT's orthogonal
evacuation `xi_B`. Neither under the direct-on-B(lambda) interpretation nor
under the K_p(infty) embedding interpretation.

The specific blockers (in order of structural depth) are documented below.
Before Rick re-runs this, the *operator definition* needs to be tightened: the
"obvious" Watanabe-style parity rule fails the braid relation
`tilde-B_1 tilde-B_2 tilde-B_1 = tilde-B_2 tilde-B_1 tilde-B_2` on K_p(infty)
even on the depth-k slice (see Section 5 below), so the comparison against AT
is moot under any of the operator interpretations the compute agent could
extract from existing files.

## 1. Setup recap

- B(omega_1+omega_2) at B_2 has 16 vertices, built via the connected component of
  the highest-weight tensor (1, 12) in B(omega_1) ⊗ B(omega_2) under
  Kashiwara-tensor with non-spin-on-left (AT's reading-word convention,
  line 892 of arXiv:2409.12666). Verified: AT's xi_B table is an involution
  with all 16 pairings weight-negating, agrees with paper's Example 3.28
  on the explicit datum xi_B(0|2bar1) = (bar2|12).
- K_p(infty) at B_2 implemented per CST bracketing in
  `/home/agent/projects/proofs/remark47/coideal_check/b_i_b2.py`. Positive roots
  beta_11 = alpha_1 = e_1 - e_2 (long), beta_12 = alpha_1 + alpha_2 = e_1 (short),
  gamma_12 = alpha_1 + 2 alpha_2 = e_1 + e_2 (long), beta_22 = alpha_2 = e_2 (short).
- Rick's tilde-B_i interpreted via Watanabe Cor 2.3.7 parity rule:
  `tilde-B_i b = E_i b if phi_i(b) is even, F_i b if odd`.

## 2. Interpretation R1 — tilde-B_i directly on B(omega_1+omega_2)

Applying the Watanabe parity rule directly on the finite KN-crystal:

| b | tilde-B_1 B_2 B_1 (b) | AT xi_B(b) | Match? |
|---|---|---|---|
| (1\|12) | None | (bar1\|bar2bar1) | None falls off edge |
| (1\|1bar2) | None | (bar1\|2bar1) | None |
| (2\|12) | None | (bar2\|bar2bar1) | None |
| (0\|12) | None | (bar2\|2bar1) | None |
| (2\|1bar2) | (0\|1bar2) | (bar1\|1bar2) | DIFF |
| (bar2\|12) | (bar1\|2bar1) | (0\|2bar1) | DIFF |
| (0\|1bar2) | (2\|1bar2) | (bar1\|12) | DIFF |
| (bar2\|1bar2) | None | (2\|2bar1) | None |
| (2\|2bar1) | (0\|2bar1) | (bar2\|1bar2) | DIFF |
| (0\|2bar1) | (2\|2bar1) | (bar2\|12) | DIFF |
| (bar1\|12) | None | (0\|1bar2) | None |
| (bar1\|1bar2) | (bar2\|bar2bar1) | (2\|1bar2) | DIFF |
| (bar2\|2bar1) | None | (0\|12) | None |
| (bar2\|bar2bar1) | (bar1\|1bar2) | (2\|12) | DIFF |
| (bar1\|2bar1) | (bar2\|12) | (1\|1bar2) | DIFF |
| (bar1\|bar2bar1) | None | (1\|12) | None |

**R1 summary:** 0/16 match AT. 8/16 fall off the edge (None). The Watanabe rule
needs `e_i b` when phi_i is even, but on a finite KN-tableau crystal this is
None at the e_i-string boundary. The remaining 8 give non-AT pairings.

**Braid relation R1:** B_1 B_2 B_1 = B_2 B_1 B_2 fails on 14/16 vertices. So
on the finite B(omega_1+omega_2), the Watanabe-rule operator does NOT satisfy
the three-strand braid relation either.

## 3. Interpretation R2 — Embed B(omega_1+omega_2) into K_p(infty)

Embed via naive transport: HW (1,12) -> empty Kostant partition; transport f_i
in B(omega_1+omega_2) to f_i in K_p(infty).

**Blocker:** This embedding is *not injective*. 16 elements -> 14 distinct K_p
images. Three pairs of B(omega_1+omega_2)-elements share a single K_p image,
due to "different f-paths in B(lambda) give different K_p images":

```
(0|2bar1):       stored pi = 2*beta_12,        via f_1 from (0|1bar2): 1*beta_11 + 1*gamma_12
(bar1|1bar2):    stored pi = b11+b22+G12,      via f_1 from (bar2|1bar2): b12 + G12
(bar1|bar2bar1): stored pi = b11+b12+b22+G12,  via f_1 from (bar2|b2b1): b11 + 2*G12
```

This is mathematically expected: B(lambda) is a *quotient* of B(infty), not a
subset. The naive "lift via f_i" only works when the lift respects the
star-Kashiwara structure, which here it does not. **A correct projection
K_p(infty) -> B(omega_1+omega_2) requires either Kashiwara's
epsilon-star functions (epsilon*_i, the dual e_i-string at the involution *)
or some other star-structure-aware projection that the agent does not have
implemented in the existing files.** This is a real blocker.

For the 14 distinct images, applying tilde-B_kp = (e_i if phi_i even else f_i)
on K_p(infty) and projecting back: 0/16 match AT; only 2/16 land in the image
of the embedding at all.

## 4. The explicit AT datum

AT: xi_B(0|2bar1) = (bar2|12).

- R1 result: tilde-B_1 B_2 B_1 (0|2bar1) = **(2|2bar1)**. DISAGREE.
- R2 result: braid_kp(pi=2*beta_12) is None (E_1 is None at this depth: pi_phi_1=0 even, e_1 needs eps_1>=1; eps_1(2*beta_12)=2 OK, e_1 -> 2*beta_22? actually traceable but final result projects out of image). DISAGREE.

## 5. The deeper issue: the braid relation fails on K_p(infty) for any Watanabe-style rule

I tested **four operator rules** for tilde-B_i on K_p(infty):

| Rule | Both-sides-defined count | Braid relation fails |
|------|---|---|
| phi-parity (Watanabe): e_i if phi_i even, else f_i | 12/56 on-slice pi | 100% fail |
| eps-parity (dual): e_i if eps_i even, else f_i | 49/56 | 100% fail |
| phi-parity with k(i) powers: e_i^k if phi even else f_i^k | 37/56 | 100% fail |
| Aug~ orbit-swap (deterministic, donor->receiver) parity-controlled | 8/56 | 100% fail |

None of them give the braid relation B_1 B_2 B_1 = B_2 B_1 B_2 on K_p(infty),
even when restricted to the slice {eps_1 >= 1, eps_2 >= 2}. So the Watanabe-style
rule is **not** the right operator for Rick's BDI setup, or the "braid relation"
in the user's task description is a different relation than the literal
B_1 B_2 B_1 = B_2 B_1 B_2.

Re-reading Rick's three-strand-braid proof at
`/home/agent/projects/proofs/2026-05-15-three-strand-braid-Bn.md`: the theorem
that was proved is about the catalog of `e_n^2`-net-moves (the SQUARE of
the short-simple e_n), not about an iquantum operator tilde-B_i satisfying a
braid relation. The theorem statement is "|C_n| = n(2n-1) catalog of e_n^2 moves
on the depth-k slice", with the "three-strand split" being the intra/cross/singleton
decomposition of those n(2n-1) moves. There is no proved braid relation among
distinct tilde-B_i operators.

So the user's task description, which says
"applying the braid relation tilde-B_1 tilde-B_2 tilde-B_1 = tilde-B_2 tilde-B_1 tilde-B_2",
appears to be an informal extrapolation or conjecture, not a theorem in
the existing proof. The actual operator that would make the user's task
well-defined has not yet been constructed in any file the compute agent could find.

## 6. Recommendations for Rick

1. **Specify the operator.** Watanabe's parity rule tilde-B_i = (e_i if phi_i
   even else f_i) on K_p(infty) does NOT satisfy the braid relation, even on
   the slice. If Rick has a different definition of tilde-B_i in mind (e.g., as
   a literal q=0 limit of F_i + zeta E_i K_i^{-1} on a specific basis), please
   write it as an algorithm so the compute agent can implement it precisely.
2. **Specify the projection.** The naive f_i-transport from B(lambda) to
   K_p(infty) is not injective. The correct projection requires either (a)
   Kashiwara's *-Kashiwara operators (eps*_i, e*_i) on K_p(infty), implemented
   via the involution * on B(infty), or (b) a direct realization of B(lambda)
   as a *quotient* of K_p(infty) by the *-string-length condition. The agent
   could implement (a) if the *-operators are spelled out for B(infty) at B_n,
   but the CST bracketing in b_i_b2.py does not include them.
3. **Plausibly the comparison is on a different model.** AT works on KN-tableaux
   directly. Rick's K_p(infty) is the lower-half infinity crystal, which is
   structurally different. The cleanest "bridge" might not be the
   projection K_p -> B(lambda) but rather a direct realization of B(omega_1+omega_2)
   on a model intrinsic to Rick's setup (e.g., Kostant partitions of a fixed
   total simple-root content equal to 2*lambda summed by suitable equivalence).

## 7. Files

- `/home/agent/projects/proofs/2026-05-17-AT-rick-bridge/b1_b2_b1_at_B2.py`:
  the full pipeline running both R1 and R2 with all outputs printed.
- `/home/agent/projects/memory/reading/papers/2026-05-17-azenhas-torres-2409-12666-notes.md`:
  AT notes including the full 16-row xi_B table.
- `/home/agent/projects/proofs/2026-05-15-three-strand-braid-Bn.md`:
  Rick's three-strand braid theorem (about e_n^2 catalog, not tilde-B braid).
- `/home/agent/projects/proofs/remark47/coideal_check/b_i_b2.py`:
  K_p(infty) at B_2 implementation (CST bracketing, no *-Kashiwara operators).
