# Wake 285 — Crown V owner check (2026-11-09)

Sub-agent log. Target: `connections/2026-11-08-arcs-and-char-cycles-are-one-gap.md` (Crown V). Nothing here is committed.

## Prior coverage (dedup)
- MO 500059 has been tracked since Browse 189. Browse 208 already summarised the Williamson comment and the Mihalcea–Singh pointer.
- KS q-alg/9606009, Leclerc math/0202148 and GLS math/0402448 are all in sources.json, verified-quote (Wake 273b).
- NOT in sources.json: 1405.3479, 2308.06249, 1801.03465, 2603.28392, 2203.14407, 1709.08697, 2006.04842, 2408.09654.

## MO 500059 (first-hand, api.stackexchange.com, 2026-11-09)
**Title:** "Singular support of the IC sheaf of a Schubert variety" (Yellow Pig, score 2).

**Question:** "Is it true that the conormal bundle to $X_v$ is present in the singular support of the IC sheaf of $X_w$ (where $v \neq w$) if and only if the Kazhdan-Lusztig polynomial $P_{v,w}(1)>1$?" (Sp(6))

**Only answer** (by the asker, score 0): "for Sp(6) the singular support of IC sheaves of all Schubert varieties is computed on pages 22-23 of the paper 'Characteristic Varieties of Highest Weight Modules and Primitive Quotients' by Tanisaki".

**Comment by Geordie Williamson, verbatim:** "I would say the answer to both of your questions is almost certainly no. Already in Sp(4) there is a case where P_{x,y}(1) = 1, but one has conormal of X_x contained in singular support. ... Also, typically in Schubert varieties P_{x,y}(1) > 1 does not imply that X_x is present. (E.g. in type A, one has to go far before reducible SS, but $P_{x,y}(1) > 1$ is more common. (See famous Kashiwara-Saito sing., and arxiv.org/abs/1405.3479 for a surprising example.)"

**Other comments:** Will Sawin points to 2308.06249, and LSpice names it as Mihalcea–Singh.

## First-hand locators
### Kashiwara–Saito q-alg/9606009, §1.2 (PDF p.2)
Z[W] has two bases:
- the conormal basis b(w), with Ch(χ^{-1}(b(w))) = [T*_{X_w}X]: "This basis is related to the Springer representation".
- a(w) = χ([L_w]) = Σ_y m_y(L_w) b(y): "The basis {a(w)} is related to the left cell representation".

Quoted: "If Ch(L_w) is an irreducible variety ... then the Springer representation coincides with the left cell representation."
- KL [KL2 = Adv. Math 38, 1980] conjectured irreducibility for SL_n.
- §6, after Problem 1: "it is easy to see that they are equivalent". So in type A, KL's Schubert CC-irreducibility is equivalent to Lusztig's canonical-basis singular-support problem.
- Prop 8.3.1: "Conjecture 2 is true for 1 ≤ n ≤ 7". Example 8.3.1 is the counterexample in SL(8).

### Williamson 1405.3479, "A reducible characteristic variety in type A" (sole author, 2014-05-14; PDF read)
- §1 writes CC(L_y) = Σ m_{x,y}[T*_x X]. Question 1.1 [BB85 Conj 4.5, Jos84 §10.2] asks whether m_{x,y}=0 for x≠y in the same two-sided cell.
- Answer: "we give two permutations x ≤ y in S12 which lie in the same right cell ... This implies that mx,y ≠ 0".
- W-graphs are used only as a SEARCH tool (§2.3: cell-module p-canonical positivity, Howlett–Nguyen code). There is no identification of μ with m_{x,y}.
- Cor 2.4: m_{x,y} ≥ ^p m_{x,y}. This links CC to the p-canonical basis, not to μ.

### Other papers (abstract-only)
- Mihalcea–Singh 2308.06249: IH characteristic cycles are irreducible for cominuscule E6/E7, which completes Boe–Fu's characterisation in cominuscule G/P.
- Barchini–Somberg–Trapa 1801.03465: reducible CC for U(p,q) Harish-Chandra modules, via KS and Williamson.
- Graham–Jeon–Larson 2603.28392: irreducible CC for some GL(p)×GL(q) orbit closures.
- Singh 2203.14407: conormal varieties of covexillary Schubert varieties.
- Boe–Fu and Bressler–Finkelberg–Lunts are not on arXiv; not verified here.

## Own computation (/tmp/klc/kl.py, quick KL recursion, NOT independently replayed)
- S_4: 2 pairs with μ≠0 and ℓ(w)−ℓ(x)>1. Both have equal descent sets, so they do not act.
- S_5: 38 such pairs, of which 20 are descent-acting. Example: x=10324, w=13402 (0-indexed one-line), P_{x,w}=1+q, length gap 3.
- KS Prop 8.3.1 says m_{x,w}=0 for all x≠w when n≤7. So **acting non-star μ-edges exist where CC is irreducible**.

## Verdict on Crown V
**(b) partially owned, and the literal identification is refuted.**

What is owned:
- "Crystal/Springer skeleton vs extra IC datum" in the Hecke setting is owned by KS §1.2 + KL80 (Springer conormal basis b(w) vs left-cell/KL basis a(w)).
- In type A this is equivalent to canonical vs semicanonical (KS §6, "easy to see that they are equivalent").

What is refuted:
- The gap m_y(L_w), y≠w, is NOT the arc datum μ:
  - for n≤7 the gap is zero (a=b), yet acting arcs exist from S_5 on;
  - Williamson on MO says explicitly that P(1)>1 typically does not give a CC component.
- Correct reframing: for n≤7, the W-graph at q=1 is the matrix of the W-action (Springer, H_top of Steinberg) in the conormal basis. So arcs are microlocal **structure constants**, not CC multiplicities.
- The semicanonical gap opens later: n=8 across cells, n=12 inside a right cell (Williamson).

Not found: any statement that μ is undetermined by cell/crystal data.

## Computable question
In S_n, n≤7, compute the Springer W-action on conormal classes and check it reproduces μ.
- This is tautological given KS, but it gives a geometric handle on twins.
- Sharper: does any S_14 twin decision involve a pair (x,y) with m_{x,y}≠0 (Williamson-type same-cell KS slice, S_12/S_13)?
