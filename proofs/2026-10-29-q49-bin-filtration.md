# Q49: the bin filtration is degenerate (gr_b = 1 for every bin), so Q49 is EMPTY

PROVE 263 warm-up, 2026-10-29. Registry node `q488-Q49-bin-filtration`. Script: `work-in-progress/scripts/q48/q49_check.py`.
Conventions as in `proofs/2026-10-29-q46-principal.md`: ε_ρ = w_ρω (−1 at positions m+1−k, k ∈ ρ), ℓ(w_ρ) = |ρ|.

**Claim.** Fix a regular dominant grading a (e.g. ρ_C = (m,…,1) or 2ρ^∨ = (2m−1,…,1)) and κ. For ρ ⊆ κ put
f_ρ(j) = π_a ch_ρ(j) = Σ_{σ⊆ρ} a_{ρσ}(q) t_σ^j, with t_σ = q^{(ε_σ,a)} and a_{ρρ} ≠ 0 (Q46 Step 2). Let bin(ρ) = (ε_ρ,a),
F_{≥b} = span{f_ρ : bin(ρ) ≥ b}, and gr_b = F_{≥b}/F_{>b}. Then dim gr_b = 1 for every bin b that occurs.

**Sign check (TODO (i) of PROVE.md).** For σ ⊊ ρ, w_σ < w_ρ, and ω is dominant, so ε_σ − ε_ρ ∈ Q_+∖0 and (ε_σ,a) > (ε_ρ,a).
The bottom term at w_ρ is therefore the **minimum** exponent of f_ρ.

**Proof.** Let E_{≥b} (resp. E_{>b}) be the span of the j ↦ t^j with t = q^s, s ≥ b (resp. s > b). By the sign check,
f_ρ ∈ E_{≥bin(ρ)}, so F_{>b} ⊆ E_{>b}. If bin(ρ) = b, then f_ρ has coefficient a_{ρρ} ≠ 0 on q^{jb}. Distinct exponentials
are linearly independent, so f_ρ ∉ E_{>b} ⊇ F_{>b}, and gr_b ≠ 0. Also Σ_b dim gr_b = dim span = #bins (Q46, proved). There
are #bins summands, each ≥ 1, so each is exactly 1. ∎

**Verdict.** Triangularity is automatic, and the filtration cannot separate anything: it is a degenerate test, and the
Crown O linkage analogy is untouched by it. A real separator would need a non-filtration invariant, e.g. whether the
kernel is spanned by differences within a bin modulo lower bins with *residue-like* coefficients. Q49 is CLOSED (empty).

**Machine (TODO (ii)).** `q49_check.py 3`: for all 8 κ at m = 3 and both gradings a = (3,2,1), (5,3,1), dim gr_b = 1 for
every bin, with 0 failures (ranks at q = 7, Vandermonde rows j = 0..#S−1).
