# Q77 — the q=0 reverse Schur–Weyl centraliser fails (PROVE 295, 2026-11-13)

Draft note for Clio cc Robin, never MacBeth. UNSENT. Dream 294: theorem cold read PASS (0 MUST, 4 NIT, one typo fixed). Ready for Wake to send as a WIP PDF.

**Setup.** H = H_N(0) acts on (kⁿ)^{⊗N} by v_w·π_i = v_{ws_i} on ascents and v_w otherwise.
Let A be the image of H, S = End_H = S_0(n,N) (owned by Deng–Yang / Jung–Oh), and B = End_S. Then A ⊆ B.

**Theorem (proved, written).** For n ≥ 2 and N ≥ 2n+1, A ⊊ B.
- Let h = π̄_{w0[1,n−1]}·π̄_{w0[N−n+1,N−1]}, where π̄ = 1−π. For any set C of weights, v ↦ (v·1_C)·h commutes with S.
- It is not in A whenever C separates two weights all of whose parts are ≥ 2.
- For n = 2 the witness is "(1−π_1)(1−π_{N−1}) on the weight space with N−2 ones", for every N ≥ 5.
- Proof idea: call a word *bad* if some letter 1,…,n is missing, or the first occurrences of 1,…,n are not in increasing order of position, or the last occurrences are not. Bad words are closed under the 0-Hecke moves, so they span a submodule Y. Being good is a necessary condition for reaching prefix = suffix = 12⋯n (no equivalence is claimed). Y is killed by h. Every cross-weight S-generator lands in Y. A local-idempotent argument shows the split operator is not in A.
- The proof is short and needs only standard facts.
- One-line picture: h maps V^{⊗N} into det ⊗ V^{⊗(N−2n)} ⊗ det, where det is the q=0 antisymmetriser line on n positions. S_0 cannot move weight through a det end, and H cannot tell two middle weights apart.

**Surprise.** The census hunch "fails iff N ≥ 2n+1" is wrong. (3,6) also fails, by an exact ℤ certificate, and the mechanism there is different (non-split).
The witness there is a·1_μ with a = π̄_{w0[1,2]}·π_3·π̄_{w0[4,5]} and μ = (1,2,3) or μ = (1,3,2).
- (4,8) also fails. In general, at N = 2n the element a_n = π̄_{w0[1,n−1]}π_nπ̄_{w0[n+1,2n−1]} gives a_n·1_μ ∈ B. That half is proved; the "not in A" half is checked exactly only at n = 3, 4.
- Open: is (4,7) A = B? That decides between "A = B ⟺ N ≤ n+2" and "A = B ⟺ N ≤ 2n−1 (n ≥ 3)".

**n=2 numbers.**
- dim A = Catalan(N) (computed for N ≤ 10; not proved).
- dim B = 43, 142, 493, 1768, 6475, 24052 for N = 5..10. No closed form yet.

**Questions for Robin.**
1. Is an MO 406152 answer wanted? It is the "naive Schur–Weyl duality for 0-Hecke" question.
2. Is Deng–Yang §4 accessible to you? The novelty gate is still "not found".

Files: proofs/2026-11-13-q77-zero-schur-weyl-dc-fails.md, proofs/prove295/*.py.
