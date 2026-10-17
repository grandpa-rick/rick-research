# Weld = regular bicomodule — decides Conjecture 5.1 (for review)

- UID: 405
- From: scot.macbeth20@gmail.com
- Date: 2026-10-17 00:11:00
- Message-ID: <6ad2bd1a.70c60f76.2e7ac9.8d11@mx.google.com>
- Attachments: 2026-10-17-weld-is-regular-bicomodule.pdf (252.1 KB)

---

Rick — attached (PDF, WIP content commit 2fd555a) is the full write-up of a result deciding Conjecture 5.1 of the workers-bicomodules-PRA draft: the BHM worker/harness weld B = ΔS◁ΔT IS the regular (ΔT,ΔS)-bicomodule (coactions λ = δ_{ΔS}◁ΔT, ρ = ΔS◁δ_{ΔT}), so the weld is a genuine prafunctor ΔT-Set → ΔS-Set. Two of the three clauses are positive — existence TRUE, and discarded = Σ-tail TRUE (the Σ-index is the branch-map set T^S) — and one is a clean refutation: worker = content is FALSE, because the represented content factor is the power (−)^S (directions S), not the worker A = Δ(S×T) (directions S×T), differing whenever |T| ≥ 2. Registry node weld-is-regular-bicomodule is [proved], with a machine-checked [computed] corroboration of all five bicomodule axioms over shape cases (|S|,|T|) in {(2,2),(2,3),(3,2),(1,2),(2,1)}.

What I'm least sure survives a careful read: clause (2)'s refutation (that no handedness choice repairs the directions mismatch), and whether the σ-embedding of A as the constant-branch slice T ⊆ T^S of the Σ-tail is stated correctly. Those are the two places I'd value your check.

— MacBeth
