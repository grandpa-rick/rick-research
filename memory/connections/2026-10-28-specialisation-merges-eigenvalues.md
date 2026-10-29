# Crown O (hunch on top of a theorem): a specialisation merges eigenvalues of ⊗L, and dependence classes are its "blocks"

**The theorem underneath (proved, PROVE 262).** `proofs/2026-10-29-q46-principal.md`, node `q488-Q46-principal-separation` (proved),
long draft Rem 4.19 `rem:onegrading` (WIP a0da3a9). For a regular grading a, rank{π_a ch_ρ : ρ⊆κ} = #{(w_ρω_m, a) : ρ⊆κ}.
The kernel dimension is Σ_bins (bin size − 1).

**Why it's true, in one line.** Localisation writes ch_ρ(j) = Σ_{v≤w_ρ} R_v(x)·x^{j·vω}. As a function of j, the character is
an exponential polynomial whose *bases* are the eigenvalues of "tensor with L" at the T-fixed points. The recursion in j only
sees those eigenvalues. A specialisation x ↦ q^a sends x^{vω} ↦ q^{(vω,a)}, so it **merges eigenvalues** that have equal a-value.
Vandermonde then says rank = number of distinct eigenvalues left. Nothing deeper is needed.

**What it corrects.** Crown M's separator hierarchy "x=1 blind < principal q < full T" is WRONG in the middle. Principal q (a=ρ_C)
has rank |κ|+1, *exactly* the x=1 rank, and its kernel → Crown K's kernel at q=1. Principal q is just as blind as x=1. The real
hierarchy is "number of bins": ρ_C gives bins = |ρ| (as blind as possible), Kac 2ρ^∨ gives bins = 2|ρ|−ℓ(ρ) (first fails at κ=(4,2)), and
generic a separates everything. So a one-parameter specialisation is only as good as the linear functional's injectivity on the
Bruhat-interval weights. Type C has two "principal" ones, and they differ (feedback `feedback_which_principal_specialisation.md`).

**Seed hunch (Path 3, labelled analogy, NOT checked).** This has the shape of a linkage principle. In Hecke algebras at a root of unity,
Jucys–Murphy eigenvalues (contents) merge mod e, and the blocks are the fibres of the residue map (Brundan–Kleshchev 0808.2032, a Seed
Path 3 key paper). Here the eigenvalues of ⊗L at fixed points merge under π_a, and the dependence classes are the fibres of
ρ ↦ (w_ρω, a). **Where the analogy is weaker:** the (3,1) kernel vector ch_21 − (q²−q+1)/(q²+1)ch_3 − … involves ch_2, ch_1 from
*other* bins, so dependence is block-*triangular* (leading terms sit in one bin), not block-diagonal. Separator test before anyone
promotes this: is there a filtration by bin value whose associated graded splits by bins at every κ, m≤4? Cheap. Post-11-15.

**Why I care.** It's the first time this arc touched the Seed Q4 question ("what survives at a special parameter") with a *sharp*
answer instead of a single example. What survives is exactly the image of the eigenvalue spectrum.

**PROVE 263 update (2026-10-29): Q49 is EMPTY.** gr_b = 1 for every bin automatically (min-exponent bottom term + Σ gr_b = #bins), so
the bin filtration is a degenerate test and does not separate the linkage analogy. The real separator would need a non-filtration
invariant, e.g. whether the kernel is spanned by differences within a bin modulo lower bins with coefficients that are *residue-like*.
The hunch stays a hunch. `proofs/2026-10-29-q49-bin-filtration.md`.
