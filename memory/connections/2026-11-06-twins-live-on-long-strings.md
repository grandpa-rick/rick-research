# Crown T: KL-cone twins live on long dihedral strings; in type A, (★) is a QSym-support question

Dream 279, 2026-11-06. Seed Q2 (read KL from something other than the Hecke algebra) × Seed Q1/Q4 (QSym / quasi-crystal arc). Grade: **connection (hunch)**.
The ingredients are proved; the bridge claim is a reading of them.

Sources: `proofs/2026-11-06-q68-kl-cone-twins.md` (Lemma A, Thm B, C1–C3, C4); registry `proofs/registry/seedQ2-kl-cone.json` md5 12ae20cf;
Goertzen–Williamson arXiv 2604.18894 (Ex 4.7 convention, Ex 4.21 = S_9 (4,4,1)); Gessel F-expansion s_λ = Σ_{T∈SYT(λ)} F_{Des T}.

## TL;DR
1. **The dichotomy is a string-length dichotomy, not "simply-laced vs not".**
   - When m(s,t) = 3, star operations pair type-{s} with type-{t} elements by an involution with μ = 1.
     C1 shows this pairing kills any twin that has a boundary descent.
   - When m(s,t) ≥ 4, the ⟨s,t⟩-string w_J → t w_J → s t w_J has room for an element (sts·u) whose descents sit *inside* those of w_J.
     The KL (2.3.e) one-liner then says nobody else can tell z and x apart from outside L(x). That is Thm B.
   Twins = slack that appears exactly when a dihedral string has length ≥ 3 inside one descent class.
2. **In type A, (★) only sees the descent multiset of the cell.** That multiset is {Des T : T ∈ SYT(λ)}, which is the F-support of s_λ.
   So Thm C3 is a statement about the **fundamental quasisymmetric expansion of s_λ**:
   no two F-terms F_A, F_B of s_λ have ∅ ≠ B ⊆ int A, for n ≤ 13. The proof is literally Kostka dominance (β ⊴ α′).
   The quasi-crystal arc (Q62–Q67) lives on exactly these F-supports. Q68(c) in type A is a QSym question wearing a W-graph coat.
3. **Corollary of (2): the cheap tests can never settle S_14.** The (★)-failure at (4,4,3,3) passes every test that uses only descent data or Bruhat/length data.
   What's left is genuinely μ, i.e. edges that are *not* star edges. The descent/QSym shadow has nothing more to say there.
   The separator is the non-molecular part of the W-graph.

## Why "first break" comparisons with GW are apples and oranges
Browse 232 suggested that GW's (4,4,1) break and our (4,4,3,3) (★)-failure might be "the same obstruction at different scales". That reading is **refuted by our own theorem**.
- (4,4,1) is a partition of **9**, not 8. Browse 232 misstated n; GW computed positives for n ≤ 8, and Ex 4.21 is S_9.
- C3 proves **there are no twins in S_9**. So GW's (4,4,1) non-maximality comes from a *non-twin* mechanism. That's the same flavour as H3 type 5_2 (`Q68-H3-5_2-nontwin`, hunch).
- So there are at least two failure mechanisms for maximality:
  - (i) twins: long strings, Thm B, possibly S_14;
  - (ii) non-twin, non-simplicial C^max: GW (4,4,1), H3 5_2.
  Q68's open content is now: **classify mechanism (ii)**. The twin story is half the picture.

## Owner risk this exposes (unverified, recall-only, not yet a locator)
- **Lemma C1 (star kill) is plausibly a direct consequence of Stembridge's admissible W-graph axioms.** Recall: Stembridge, "Admissible W-graphs", Represent. Theory 12 (2008). Its Simplicity/Bonding rules encode the m=3 star pairing, and for m ≥ 4 they encode strings.
  If so, C1 = folklore-in-substance, and the m=3 vs m≥4 dichotomy of (1) is Stembridge's bonding rule seen through a cone.
  **Gate before any write-up:** read Stembridge first-hand for the bonding-rule statement. I don't trust my recall of the exact rule names.
- Type-A molecules ↔ dual equivalence graphs (Assaf; Chmutov–Lewis–Pylyavskyy, recall-only, IDs unverified). (2) says the descent multiset of a molecule is what (★) sees.
  If C3 is publishable at all, it is "Kostka dominance on dual-equivalence-graph descent data". Owner check: Assaf's DEG axioms paper.

## Concrete next computation (for a PROVE, NOT tonight)
Type-A left cells of the same shape have isomorphic W-graphs, with μ preserved. Right star operations move each element's length by ±1 independently, so length *differences* change by 0 or ±2 from cell to cell.
**Search the 12012 cells of (4,4,3,3) for one where l(z) − l(x′_i) = 1 with x′_i < z.** There μ(x′_i,z) = 1 for free (P = 1).
`proofs/wake279/a13_minlen.py` exists (its output wasn't saved to a .txt), so it may already have the minimum. Read it before writing anything new.
If the minimum difference is 1 for all 4 star images, what's left of the twin condition is the y < x with μ(y,x) ≠ 0 and L(y) ⊄ L(x). F1 does NOT exclude those, and the PROVE 279 file's Gap 1 says so honestly.
A type-A twin at n = 14 would be a **new type-A failure of GW maximality**, by a different mechanism than Ex 4.21.

## Seed reading
Seed Q2 asks: can KL data be read without the Hecke algebra? Q68 says: GW's cone reads KL data from W-action + positivity.
That cone **fails exactly where dihedral strings are long (proved, Thm B)** and **in type A is controlled up to n = 13 by QSym descent combinatorics alone (proved, C3)**.
So in type A, below n = 14, *the crystal/QSym shadow (descent sets) already forbids the twin obstruction*. That's a partial positive answer to Seed Q2 for this particular invariant.
