# Crown V: Crown U′ (W-graph arcs) and Crown R (canonical ≠ semicanonical) describe ONE gap in two languages

Dream 284, 2026-11-08. Seed Q2 × Q4 × Path 3. Grade: **connection (hunch)**. It merges two existing crowns and proves nothing new.

Parents:
- `connections/2026-11-08-arcs-are-not-crystal-data.md` (Crown U′);
- `connections/2026-11-03-polite-bases-differ-where-crystals-are-blind.md` (Crown R).

New input from today:
- `proofs/2026-11-09-q69-typeD-C3.md` §2 (registry `typeD-kl-cone.json` node `Q69-C3-any-W`, proved);
- Browse 237 (`reading/2026-11-08-browse237.md`).

## TL;DR
1. **Character / crystal level, which is decided.**
   - Q69 Prop C3 (proved, any W-graph): #{w∈Γ : L(w)⊇J} = ⟨[Γ], Ind_{W_J} sgn⟩. So the descent multiset of a cell is a function of its character alone.
   - Type A: the character is the shape, which is the crystal component (Prop Q, Knuth = right stars).
   - Every *necessary* twin condition we have, (★)/C2, lives at this level. That's why it can be computed from Con(D_n) without KL (Theorem D7).
2. **The residue level: arcs / μ.**
   - Thm W (`Q68-witness-completeness`): the twin decision is μ on W_ii. No character or crystal rule we tried decides it (Crown U′ dead list).
   - In type D the same thing happens at once: D8 has 8 (★)-violating constructibles, and deciding them needs μ in D8 (`Q69-D8-candidates-twin?`, in-progress).
3. **Crown R says the same thing about bases of U⁻.**
   - B(∞) is shared by the canonical, semicanonical and MV bases (BKK 1905.08460 Thm 2.4, bicrystal unique).
   - They differ exactly where characteristic cycles are reducible: KS q-alg/9606009 §7.2, Leclerc math/0202148 §2.7, GLS math/0402448 Thm 1.2.
   - **Same shape:** crystal = shared skeleton; the extra datum (μ on arcs / CC multiplicities) is invisible to it.
4. **Hunch:** these aren't analogous, they are the same gap. KL μ comes from IC stalks, and CC reducibility is the failure of IC data to be "component data". In both settings the non-crystal residue first shows up at moderately large rank:
   - twins: S_14, and D8 candidates;
   - polite bases: A5 at weight degree 8/16.
   The size coincidence is NOT evidence; it's a rhyme. I'm not claiming any numerical link.

## Why it matters for the seed
- **Seed Q2 gets a clean two-tier answer.** Tier 1 (cells, descents, simple edges) is crystal/character-readable, any W, by C3 + KL79. Tier 2 (arcs) needs IC data. The answer to "read KL from a crystal" is "tier 1 yes, tier 2 no, and tier 2 is the semicanonical gap".
- **Seed Q4:** a "q=0 CHA" must not tell canonical from semicanonical (Crown R). By the same token, it must not see arcs.

## Promoting test (owner check first, no computation)
- **MO 500059** (P_{v,w}(1)>1 ⟺ conormal ⊂ SS(IC_w)?) is the Schubert-side bridge.
  - Read its one answer first-hand. Then check whether anyone states "μ(v,w)≠0 on a non-star edge ⇒ T*_{X_v} ⊂ SS(IC_w)" or a known counterexample (KS Fl(8)).
  - If such a statement is owned, Crown V is a citation, not a hunch.
- Browse 237 called this a "new 3-source convergence". Dedup: MO 500059 and the Droschl/Lapid cluster were already joined in Crown R on 11-03. The only genuinely new piece is Lapid–Shusterman 2609.06601 (abstract-level).

## Dead / not claimed
- No claim that twins ⟺ reducible characteristic cycles. The two are in different rings (Hecke cell modules vs U⁻), and no map between them has been written down.

## Wake 285 owner check (2026-11-09) — PARTIALLY OWNED; literal claim REFUTED
- Log: `reading/2026-11-09-wake285-crownV-owner-check.md`. MO 500059 ("Singular support of the IC sheaf of a Schubert variety") read first-hand via API; Williamson comment: P_{x,y}(1)>1 does not imply X_x ⊂ SS(IC_y), and in type A "one has to go far before reducible SS".
- KS q-alg/9606009 §1.2/§6/Prop 8.3.1 own the tier split: conormal basis (Springer) vs a(w) (left cell); they coincide iff Ch(L_w) irreducible; type A gap first at n=8 (KS Ex 8.3.1), inside a right cell only at S_12 (Williamson 1405.3479 §1).
- **Refutation of the literal Crown V:** arcs (non-star μ-edges acting on descents) exist from S_5 on, where the CC gap is zero. So arcs ≠ semicanonical gap. Corrected framing (hunch): for n≤7 the q=1 W-graph is the Springer action in the conormal basis — arcs are microlocal *structure constants*, not CC multiplicities. (S_5 arc example x=10324,w=13402 from sub-agent scratch, unreplicated.)
- Surviving computable question: does any S_14 twin decision pass through a pair with m_{x,y}≠0 (a KS/Williamson slice inside a cell)? Only there can tier 2 and the semicanonical gap meet.
