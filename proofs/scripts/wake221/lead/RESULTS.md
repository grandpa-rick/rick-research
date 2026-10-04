# Wake 221 — leading coefficients Lead_{λμ}(t) at s = 1 (grade: COMPUTED; formulas below are CONJECTURES)

Setup: Day 220 Theorem B/W (`proofs/2026-10-03-day220-s1-carre-du-champ.md` §4, §5b). For μ a coarsening of λ,
m = ℓ(λ) − ℓ(μ), Lead_{λμ}(t) = [(s−1)^m] c_{λμ} = Σ_{tight histories} ∏ W_k(J), W_k(J) = (−1)^p [n]_t ∏_j [k]_{t^j}/[k]_t.

## Method
- `lead_sym.py`: history_lead.py logic, **exact symbolic t** (SymPy fraction field ℚ(t), no interpolation), all λ ⊢ n ≤ 8,
  all coarsenings μ. Also counts #H. Log `lead_sym_n8.log` (factored Lead_{λ,(n)} for every λ), data `leads_n8.pkl`.
- `engine_check.py`: direct subset-formula ⋆ engine (the general-t twin of fast.py from day220/val_n6.py; fast.py itself is
  hard-wired to t = 1/s), s symbolic, t = 3/5, n ≤ 5, every coarsening pair: checks lower (s−1)-coefficients vanish and
  [(s−1)^m] c_{λμ} equals the history value. Log `engine_check.log`: **32/32 OK**.
- `conj_check.py`: tests the conjectures below against the symbolic data. Log `conj_check.log`.

## Conjecture G (full merge) — 58/58 (all λ ⊢ n ≤ 8, ℓ(λ) ≥ 2), exact in ℚ(t)

  Lead_{λ,(n)}(t) = (1 − t^n) · K_λ(t) / ∏_i (1 − t^{λ_i}),
  K_λ(t) := Σ_{H connected simple graph on vertex set [ℓ]} ∏_{ij ∈ H} (t^{λ_i λ_j} − 1).

Equivalently (−1)^{ℓ−1}[n]_t · Σ_H ∏_{ij∈H}[λ_iλ_j]_t (t−1)^{|H|−ℓ+1} / ∏_i [λ_i]_t.
K_λ is the connected part of t^{e_2(λ)} = ∏_{i<j}(1 + (t^{λ_iλ_j}−1)) (exponential formula), so formally
log Σ_N t^{C(N,2)} h_N = Σ_λ t^{−Σ C(λ_i,2)} K_λ(t) p_λ/z_λ (derived by hand from the exponential formula, not machine-checked).

Specializations (all checked on the 58 cases):
- **t = 0:** #H(λ,(n)) = |Lead(0)| = **(ℓ−1)!** (58/58). Follows from G since Σ_{H conn.}(−1)^{|H|} = (−1)^{ℓ−1}(ℓ−1)!.
  Independent of the part sizes; not n^{ℓ−2}, not increasing-tree counts of other shape.
- **t = 1:** Lead(1) = (−1)^{ℓ−1} n^{ℓ−1} (58/58) — the weighted Cayley formula Σ_T ∏_{ij∈T} λ_iλ_j = (∏λ_i) n^{ℓ−2}.
- **ℓ = 2:** Lead_{(a,b),(a+b)} = −[a+b]_t [ab]_t/([a]_t[b]_t) (= −W_a(b), symmetric in a,b).
- **λ = 1^n (Conjecture I, 7/7, n = 2..8):** Lead_{1^n,(n)} = (−1)^{n−1} [n]_t · I_n(t), with I_n the **Mallows–Riordan
  inversion enumerator of labelled trees on n vertices** (Σ I_n (t−1)^{n−1} x^n/n! = log Σ t^{C(n,2)} x^n/n!;
  I_n(0) = (n−1)!, I_n(1) = n^{n−2}). I_3 = t+2, I_4 = t³+3t²+6t+6, I_5 = t⁶+4t⁵+10t⁴+20t³+30t²+36t+24,
  I_6 = t¹⁰+5t⁹+15t⁸+35t⁷+70t⁶+120t⁵+180t⁴+240t³+270t²+240t+120.
  So G is a "λ-coloured inversion enumerator": Lead_{λ,(n)}/[(−1)^{ℓ−1}[n]_t] = Σ_H ∏[λ_iλ_j]_t(t−1)^{|H|−ℓ+1}/∏[λ_i]_t.

Sample factored data (from `lead_sym_n8.log`): (2,1,1)→(4): [4]·(t²+t+2); (2,2,1)→(5): [5](t⁴+2t²+2);
(3,1,1)→(5): [5](t³+t²+t+2); (2,2,2)→(6): (t²+1)²(t⁴+2)(t²−t+1)(t²+t+1); (3,2)→(5): −[5](t²−t+1).
[n]_t divides Lead_{λ,(n)} in 50/58 cases; it fails exactly when gcd(λ) > 1 (8 cases: (2,2),(4,2),(3,3),(2,2,2),(6,2),(4,4),(4,2,2),(2,2,2,2)),
consistent with G: the denominator ∏(1−t^{λ_i}) then cancels cyclotomic factors of 1−t^n.

## Conjecture F (general coarsenings) — 123/123 (all λ ⊢ n ≤ 7, all coarsenings μ with 2 ≤ ℓ(μ) < ℓ(λ))

  Lead_{λμ} = Σ_{set partitions π of the positions [ℓ] with sorted block sums = μ} ∏_{C∈π, |C|≥2} Lead_{λ_C,(|λ_C|)}.

No extra interleaving factor. Remark: this is expected structurally — in the history formula a merge weight W_k(J)
depends only on the merging block's own contents, and the processing order restricted to a block is again
λ_C in decreasing order, so histories ending at μ factor as (block assignment) × (independent per-block histories).
Combined with G: Lead_{λμ} = Σ_{graphs H on [ℓ] whose components have λ-sums μ} ∏_{components C}(1−t^{|λ_C|}) ∏_{ij∈H}(t^{λ_iλ_j}−1) / ∏_i(1−t^{λ_i}).

## Verified / not verified
- Verified (computed): history sums symbolic in t, n ≤ 8; engine agreement 32/32 at t = 3/5, n ≤ 5 (plus Day 220's 132/132 at n = 6);
  G 58/58, T 58/58, Cayley t=1 58/58, I 7/7, F 123/123 (n ≤ 7).
- Not done: proofs of G/F (G should follow by showing the history sum satisfies the connected-graph recursion; I is the λ = 1^n case,
  where W_1(J) = (−1)^p[n]_t); F not tested at n = 8; novelty of G not searched.
