# Q60: crystal locality of Baumann's HN factorisation Φ_θ (PROVE 272, 2026-11-02). UNSENT, proofs/ only

**Question.** Baumann 2401.10340 factors each polite basis element as Φ_θ(b) = (b_+, b_−) by cutting at stability θ. When does the
crystal operator ẽ_j move only one factor?

**Answer (type A).** Exactly when no root weight is "sandwiched": in type A, no index k has g(j+1) < g(k) < g(j), where θ(ε_a − ε_b) = g(a) − g(b).
- α_j on the negative side: ẽ_j acts on b_− only.
- α_j "adjacent" (T∪{α_j} biconvex): ẽ_j acts by Kashiwara's tensor rule on b_− ⊗ (α_j-string of b_+). The proof is sketched (Kashiwara embedding Ψ_j^*), and the rule is exact on 12672/12672 elements in A_4.
- Otherwise: an explicit flag minor moves BOTH factors. This is proved, and uses only BKK Rem 2.10 + Cauchy–Binet.

Why it matters for Seed Q1/Q4: the coproduct's θ-factorisation carries a crystal tensor rule exactly on the "adjacent" chambers, and nowhere else.
The rank-one Kashiwara embedding is the special case T = Δ_+∖{α_j}.

Full write-up: `proofs/2026-11-03-q60-local-factorisation.md`. Owner check for (b) still owed.
