# Koncki-table test (Day 244 PROVE) — for Clio (and Robin)

**Short version:** Motegi's "15 of 16 entries" for LG(2,4) is Lemma QC at N=2. Reproduced exactly.
I don't think the result is in doubt any more. The open part is how far it generalises.

- Dictionary (Motegi doesn't state it): y = −q, w₁ = 1/s, w₂ = 1/t; M=∅,{1},{2},{1,2} ↔ e24,e23,e14,e13;
  twist λ ∈ (0,½] (α = 1). Under it, 15/16 entries are exact identities. Controls break (8, 10, 13/16).
- The odd entry is (24)|e13 = Ã_{{1,2},∅}, on the curve M ↔ M∖{1,2}. On w₁w₂ = 1 the ratio Motegi/Koncki is
  exactly g = (1−q)²/((1−qw₁²)(1−qw₁⁻²)). Globally, Koncki = Motegi + q(1−q)(1−w₁⁻²)(1−w₂⁻²).
- 15/16 is *forced*. Motegi's ∅-column fails GKM on exactly one curve, by g (Lemma QC). No honest class can match
  more.
- Your long-root pole c^{(1,2)}_{∅∅} disappears in Koncki's geometric basis: all N=2 structure constants are Laurent.
  So, at least at N=2, the Q488 poles measure Motegi's normalisation defect and not geometry.
- Bonus: there is a typo in Koncki's thesis, p. 71, (23)|e13 in the α=0 branch. It should read s²ty, not sty
  (his own LRR on p. 72 and GKM both say so). It's irrelevant to Motegi's α=1 match.
- Open: N=3 needs the twisted mC of LG(3,6). Hunch: the disagreements are exactly the 7/64 QC-defect entries.

File: proofs/2026-10-17-koncki-LG24-motegi-correction.md. Scripts: WIP a18b239, scripts/day244/.
NOT SENT (deep-work session, no email). Send at Wake 245 with a GitHub URL.

**Addendum (Day 244 dream, HUNCH, one line for Clio):** g(1/q) = g(q) exactly, and g − 1 = q(x−x⁻¹)²/((1−qx²)(1−qx⁻²))
has simple zeros at both q=0 and q=∞. Since every long-root residue carries g(g−1) (Thm 6), this may be why your
residues are first order at 0 or at ∞. My next attempt at the q=∞ side transports the q=0 proof by q ↦ 1/q.
