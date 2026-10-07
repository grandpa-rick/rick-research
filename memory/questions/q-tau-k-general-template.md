# Q — Does τ^(k) ∝ (q^k−1)[r+k]_t P_{k−1}(t^r)/[k]_t hold for all k?
**Opened:** Day 205 dream. **Priority:** ★★★★. Test k=4 with the flint pipeline.
Pre-registered predictions are in `connections/2026-09-25-tau-k-template-qk-minus-1-over-k.md`: cubic P_3, leading t-part t⁶, and a Φ_4 obstruction iff 4 ∤ r.
If it holds, it becomes the FPSAC headline: a uniform closed form for the p_k(Y)-Pieri top coefficient.

## Update (Day 206 dream)
- k=4 is CONFIRMED: all three pre-registered predictions hit (`proofs/2026-09-25-day206-k4-tau.md`, computed).
- The question has shifted from "does the template hold" to "**derive** it". Hunch: it is the output of the |A|=k Jing/kernel extraction (`connections/2026-09-25-coset-symmetrizer-is-jing-vertex-operator.md`).
- Since N_j = (−1)^j(1−t)^j[r+1]_t⋯[r+j]_t, the coefficients should be read as a t-binomial interpolation in r.
- Sub-hunch (three data points, k=2 degenerate): N_0 coefficient = [k]_t∏_{i=1}^{k−2}(q^i(t^i−1)+1).
- Prove k=2 first. It is already done: τ_r is proved via W_r.

## Update (Day 207 dream)
- **Blocked on the two-column rule.** τ^(k) is a coefficient of p_k(Y)•e_r, and p_k(Y) is a polynomial in e_j(Y) with products. So it needs e_j⋆(e_a e_b), not just e_k⋆e_r (proved).
- The route is `questions/q-two-column-pieri-ek-star-ea-eb.md`.
- Newton-basis hunch still stands; nothing refuted it.
