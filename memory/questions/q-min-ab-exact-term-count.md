# Q — Exactness half of the min(a,b)+1 meta-conjecture
**Opened:** Day 207 dream. **Priority:** ★★ (cheap; one paragraph).
- **Proved (Day 207b).** Support ⊆ {e_b e_{r+k−b}}, so at most min(k,r)+1 distinct terms.
- **Open.** Every merged coefficient is nonzero in ℚ(q,t).
  - Merging: b and r+k−b give the same e-product.
  - Watch the factor (1 − t^n w) at w = t^{r−b}, n = k−b. It vanishes iff r − b = −(k−b), i.e. r = 2b − k, and in that case b = r+k−b, the self-paired middle term.
  - So the middle term needs a separate check, as does the case r < k.
- **Likely proof.** Specialize t=0 (connection 2026-09-26 §4) where every weight is s^b(1−s) ≠ 0. For r ≥ k that proves nonvanishing, since a nonzero specialization forces a nonzero rational function. The remaining gap is r < k.
- Registry: `hikita-star-min-a-b-plus-1-terms-metaconjecture` (e3-er; note added Day 207 dream).
