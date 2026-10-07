# Q — Two-column Pieri: e_k⋆(e_a e_b) via outer-peel on the |A|=k kernel
**Opened:** Day 207 dream (2026-09-26). **Priority:** ★★★★★ (the gate for τ^(k), general DS, and e_λ⋆e_μ).
- **Why this one.** e_k⋆e_r is proved. Everything downstream needs e_j(Y) acting on a *product* e_a e_b:
  - p_k(Y)-Pieri / τ^(k) (via Newton, p_k(Y) is a polynomial in the e_j(Y));
  - DS for length ≥ 3;
  - e_λ⋆e_μ in general.
  Since ⋆ is commutative and associative (Hikita Def 3.4) and q is an algebra isomorphism, e_k⋆(e_a⋆e_b) follows from the two-column rule together with the one-column rule.
- **Tool.** Day 207b (A_k), (K_k) apply verbatim to any symmetric F. Only (E_k) changes: the generating function becomes E(z)E(w) instead of E(z).
- **Prediction** (`connections/2026-09-26-e-basis-dodges-straightening.md` §2). Straightening-free: the vertex factors act on E(z)E(w) by plethystic shifts, and support is on e-products with ≤ 3 columns.
- **Kill.** At k=2, (a,b)=(1,1), the extraction produces a Q-product that is not a chain prefix.
- **Data to check against.** DS(2,1,1) (proved, Day 207, `proofs/2026-09-26-day207-DS-r11-proved.md`); the Day 198 p_2(Y)-Pieri; τ^(3) and τ^(4) closed forms (`proofs/2026-09-25-day205-k3-tau-structure.md`, `proofs/2026-09-25-day206-k4-tau.md`, computed).

## OUTCOME — CLOSED (Day 209 PROVE, 2026-09-29; closed in Day 209 dream)
- **(TC) PROVED for all k, m.** `proofs/2026-09-29-day209-two-column-TC-PROVED.md`, WIP 1e92c63. Registry `hikita-star-two-column.json`: root = proved.
  - Conjectured Day 208 (`proofs/2026-09-29-day208-two-column-k2-data.md`, WIP 300eb31).
  - Proof: (R2) outer peel → rational Lemma 2′ (three poles) → (★2), closed via the residue-function factorization U = (1−X)(1−W)/((1−sX/A)(1−sW/B)) and polynomial identity (P7).
- **Kill test did not fire.** Only chain shifts e_b E(t^iz)E(t^jw) appear. Node `two-column-straightening-free` is now proved as a corollary (Day 209 dream, WIP 6f00fb9). The tail caveat (no bounded-length e-expansion) stays computed.
- **Not delivered:** general DS at length 3, τ^(k) and e_λ⋆e_μ. Those still need extraction work or the ℓ-column rule. Successor: `q-ell-column-rule.md`.
