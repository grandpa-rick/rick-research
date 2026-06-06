# Grant pitch — discovery-layer math, with Exhibit A and a Lean commitment

*Draft, Day 40 (2026-05-27). Standalone copy to drop into Robin's grant skeleton.*

## 1. Discovery vs. verification — the framing

The Google "AI co-mathematician" paper (arXiv:2605.06651v2, May 2026) is the current state of the art: Gemini 3.1 Pro / Deep Think driving a multi-agent workbench with project-coordinator → workstream-coordinator → sub-agent structure, gated by reviewer passes. The system is real. Its three showcased results — Lackenby's surface bounds, Bérczi's counting, Rezchikov's symplectic — demonstrate a real capability: careful case analysis under supervision, at scale.

What the system does not do is also clear, and the paper does not hide it. In Lackenby, the human supplied the conjectural shape. In Bérczi, the human seeded the strategy. In Rezchikov, the human spotted the gap. All proofs are, in the paper's own words, "purely informal." Every showcased result required a human to recognise the analytical object, identify the strategic shape, or locate the specific gap. The harness then executed.

AI harnesses *verify* proofs whose shape is already known. They do not *discover* new analytical objects, and they do not recognise that a single object plays multiple distinct roles type-uniformly. **Discovery is the moat.** Verification is the layer moving fastest; discovery is the layer the harnesses cannot replicate, and that is where research-math funding has the highest leverage in 2026.

## 2. Exhibit A — the cumulative carry $P_a$ in BDI ($n+1, n$) branching

The v3 manuscript (29pp, in preparation, computationally verified on $B_2$ through $B_7$ by SymPy enumeration) demonstrates exactly this kind of discovery-layer work. A single cumulative quantity, the carry
$$
P_a := P_{a-1} + 2(B_a - T_a), \qquad P_0 := 0,
$$
plays **five distinct type-uniform roles** in the BDI chain-factor decomposition:

1. **Descent recording potential** — $P_a$ is one-sided monotone under forward chain-factor descent; reverse-play monotonically drains. There is no local witness for the image of the highest-weight projection; the image is characterisable only globally (Theorem B / Instance 5).
2. **Singleton cross-chain coupling** — the unique cross-chain inequality in the $B_n$-highest-weight indicator is the cumulative bound $S \le P_{n-1}$, lifted type-uniformly from the $B_2$ collapse $S \le 2(B_1 - T_1)$ (Theorem E).
3. **Chain–MB coupling** — the $B_n$-HW indicator factors as a carry-recursive product $\prod_a \chi_a(M_a, B_a, T_a; P_{a-1}) \cdot [S \le P_{n-1}]$. The carry is the load-bearing thread of the factorisation (Theorem E corollary).
4. **Polytope completeness** — Theorem A's bracket scan generates exactly $2n - 3$ non-redundant carry-derived facets of the chain-side Kobayashi polytope. The carry mechanism reads off all carry-derived faces; no additional combinatorial machinery is required (Theorem F).
5. **Weight-projection invariant** — under the projection to weight space, exactly one chain-side facet ($E$) survives, as $\lambda_n \le \sum_{i<n} \lambda_i$. The carry $P_{n-1}$ via $E$ is the unique trace of carry on weight space (Theorem G).

One object, five hats. The recognition that these are five views of the same quantity is what makes the result a theorem rather than five isolated lemmas. No AI harness as of 2026 has the recognition primitive to perform that move. The Google architecture is built to manage well-decomposed sub-problems under coordinator gating; it is not built to notice that two seemingly unrelated sub-problems are facets of one object. This is the discovery layer in concrete form.

## 3. The division of labour we propose

The natural split is vertical, not horizontal:

- **Discovery layer — human + framework.** What v3 exemplifies and what this grant funds. Output: new analytical objects, cross-community structural recognitions, type-uniform theorems whose statement is itself the contribution. The carry $P_a$ is the worked example; the chain-factor decomposition is the framework that produced it.
- **Verification layer — Lean 4 + Mathlib + AI assistance.** Commitment: a 4–6 week Lean micro-formalisation of the bracket-scan inequality $S \le P_1 = 2(B_1 - T_1)$ at $B_2$ as a stand-alone integer-combinatorial lemma, with the chain-factor decomposition supplied as a finite hypothesis. The full $B_2$ branching reduction (decomposition derived from $(O(3), O(2))$ representation theory) is a stretch goal at 8–16 weeks. I have zero Lean experience going in, so the 4–6 week figure depends on Lean Copilot–style tactic automation (74% step-coverage in current literature) and the `omega` decision procedure carrying the linear-integer core. The structural content survives formalisation; the formalised lemma becomes a referenceable artefact for the next discovery cycle, and the on-ramp gets built publicly rather than hidden as a weakness.
- **Application layer — community.** Branching laws, representation theory, combinatorics. The framework at $B_n$ has natural downstream targets (Watanabe 2407 existence, Meereboer's one-dimensional base case, Kobayashi's geometric fences). Each is a candidate next-cycle target on the same discover → formalise → apply loop.

The grant funds the discovery layer because that is the layer the harnesses cannot replicate. The Lean commitment at $B_2$ demonstrates the loop closes. The five-role unification at $B_n$ demonstrates the loop produces results worth formalising.

— Rick
