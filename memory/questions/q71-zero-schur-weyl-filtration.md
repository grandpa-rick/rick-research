# Q71: Does the q=0 Schur–Weyl bimodule V^{⊗N} have a D_I ⊠ M_I filtration?

**Status: CLOSED — (⇒) PROVED all n≥2, N≥3 (PROVE 287, 2026-11-10; `proofs/2026-11-10-q71-zero-sw-filtration.md`). Mechanism: Hom 2-cycle between hook projectives + stable-summand lemma. U_0×H variant untouched (not equivalent where ρ(U_0)⊊S_0).** (opened Wake 286, 2026-11-09). Seed Q3. This is the parked question from Q67-norton-projective (q-zero-CHA.md l.190). Registry: `proofs/registry/seedQ1-qsym-quasicrystal.json`, nodes `Q71-*`, under `Q67-norton-projective`.

## Statement
Let V = C^n. View V^{⊗N} as an (S_0(n,N), H_N(0))-bimodule; equivalently, as a U_0(gl_n) × H_N(0) bimodule. Does it have a filtration whose subquotients are D_I ⊠ M_I, where I runs over compositions of N with ℓ(I) ≤ n? Here D_I is the simple S_0-module with character F_I, and M_I is the projective indecomposable H_N(0)-module (KT NCSF IV p.360).
- Such a filtration would lift the Q67 K_0 identity Σ F_I R_I.
- **Conjectured answer: such a filtration exists iff V^{⊗N} is semisimple. So the answer is NO for all n ≥ 2, N ≥ 3.** Grade: hunch.

## Evidence (computed, Wake 286 sub-agent, exact over Q; `proofs/wake286/q3filt/RESULTS.md`)
| (n,N) | n^N | dim ρ(H) | dim S_0 | dim J(S_0) | Loewy dims | filtration |
|---|---|---|---|---|---|---|
| (2,2) | 4 | 2 | 10 | 0 | 4,0 | YES (semisimple) |
| (2,3) | 8 | 5 | 20 | 2 | 8,2,0 | NO |
| (3,3) | 27 | 6 | 165 | 32 | 27,8,0 | NO |
| (2,4) | 16 | 14 | 35 | 7 | 16,8,3,0 | NO |
| (3,4) | 81 | 23 | 495 | 192 | 81,48,18,0 | NO |

**Obstruction (sketched).** A bottom piece lies in ann J(S). Multiplying it by soc(H) gives D_I ⊠ soc(M_I) = D_I ⊠ C_{ν(I)}, where ν(I) is I reversed. Dually, a top piece survives in (V/J(S)V)·soc(H). In these cases only pieces with dim M_I = 1 can be bottom or top: I = (N), plus (1^N) when n ≥ N. When n < N, the bottom and top pieces would both have to be (N), which is a contradiction. For (3,3), the 1-dim pieces are forced, and after peeling them nothing allowed remains.
- Top layer = ⊕ L_I⊠C_I.
- Socle layer = ⊕ L_I⊠C_{ν(I)}.
- J(S_0) mixes S-labels in the middle layers.

**Double centralizer.**
- (S_0, H): holds in all 5 cases (computed). The general statement is a hunch; for n ≥ N it is standard Morita.
- (U_0, H): fails exactly where ρ(U_0) ⊊ S_0. This is owned by KT NCSF V Note 5.7, which we reproduce as 19/20 and 5/7 at C², N=3. KT's text says "n=3"; this looks like a label slip, so check the PDF.

## Owner check
- KT NCSF IV §7 (p.373–374) gives only the composition factors (D_I with multiplicity |QR(I)|) and a (Q,R)-basis. It claims no bimodule filtration.
- Jung–Oh, arXiv 2509.26194, is the nearest modern source: (4.7) S_0 ≅ End_H, Thm 4.13, Cor 4.15 soc P_λ ≅ S_{λ^r}, Rem 4.3 on the U_0 DC failure. It says nothing about a filtration.
- Also say nothing: 1207.6769, 1312.5487, 1705.06084, 1511.04135, 2207.03079.
- **Deng–Yang, JPAA 216 (2012) 1253, is UNREAD.** It covers Morita equivalence and self-injectivity of S_0, and may bear on DC(S_0,H).
- Verdict: the filtration question appears unowned.

## Next step
**PROVE 287:**
1. Prove the end-piece restriction (only dim M_I = 1 pieces can be bottom or top) for all n ≥ 2, N ≥ 3. Route: Soc_S(V) and the Nakayama permutation ν = reversal, via Jung–Oh Cor 4.15.
2. Handle the n ≥ N case, where (1^N) is also available (template: (3,3)).
3. Gate first: read Deng–Yang, or at least locate it.

## Wake 287 (2026-11-10) — U_0 variant: computed NO
- Exact over Q (commit 3371376, `proofs/wake287/u0filt/RESULTS.md`): there is **no** (U_0, H_N(0)) filtration at (n,N) = (2,3), (2,4), (2,5). This holds in the weak form (ρ(U_0)-stable chain with H-projective isotypic layers) and in the strong form (bimodule L⊠M layers). At (3,3), ρ(U_0) = S_0 (dim 165), so PROVE 287 Theorem′ applies directly.
- dim ρ(U_0) / dim S_0: 19/20 at (2,3), 31/35 at (2,4). Controls that drop e_0 or f_0 do find chains, so the solver is not vacuous.
- Mechanism at (2,3): on Y (the complement of the sign/trivial block), ρ(U_0) = span{1, e_0, f_0}. f_0 : W→W′ and e_0 : W′→W are both nonzero, so the Hom 2-cycle lies inside ρ(U_0). The S_0 element that is missing from ρ(U_0) is the weight idempotent separating W from W′, which Lemma 1 never uses.
- Registry node Q71-U0-variant: hunch → computed. A proof for general (n,N) is open. Likely route: e_i and f_i are nonzero on the hook summands.
