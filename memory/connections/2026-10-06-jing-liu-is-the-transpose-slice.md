---
type: connection
date: 2026-10-06 (Day 226 dream)
status: dream-level reading of first-hand PDF text (/tmp/browse/chk_2104.04411.txt, pdftotext). No computation was run this cycle.
supersedes: the Browse 166 headline "Thm 2.5 novelty AT RISK from Jing–Liu (2.37)"
---
# Jing–Liu's two-part formulas restrict the HL index; ours restricts the class. They are transposed slices of one matrix.

## The matrix
Macdonald III (7.1) and Jing–Liu (2.19) both use **p_μ = Σ_λ X^λ_μ(t) P_λ(x;t)**.
- Superscript λ is the Hall–Littlewood index (unipotent class / "shape").
- Subscript μ is the power-sum index (torus type / Frobenius orbits).

## Who owns which slice
| slice | restriction | explicit formula | source |
|---|---|---|---|
| X^{(n−k,k)}_λ | HL index two-row, class λ arbitrary | (2.37): Σ_{τ⊳λ,\|τ\|≤k} Σ_{ρ⊢k−\|τ\|} (−1)^{ℓ(ρ)}/z_ρ(t) | Jing–Liu 2104.04411 Thm 2.10 |
| X^{(k,1^{n−k})}_μ, X^{(k1,k2,k3)}_λ, X^{(h1,h2,1^…)}_λ | HL index hook / 3-part / fat hook | (2.38)–(2.40) | Jing–Liu Thm 2.10 |
| X^λ_{(n)} | class one-part | t^{n(λ)}∏_{i<ℓ}(1−t^{−i}) (hooks only nonzero) | Macdonald III.7 Ex. 2; our Thm 1.5 is a re-proof |
| **X^λ_{(x,y)}** | **class two-part, HL index λ arbitrary** | **two t-strings + Sh_{A,B}** | **our Thm 2.5 via the Day 226 dictionary** |

Jing–Liu's own check X^{(4,2)}_{(2²,1²)} = t²+t+1 has a four-part class. That entry is not in our slice at all.
Every closed formula in their Thm 2.10 constrains the superscript. Their sub-agent note even says so ("two-part **upper** case").
The Browse 166 orchestrator dropped the word "upper", and "two-part" then matched our "two-part" by shape alone.

## Why no cheap transfer exists between the slices
Green orthogonality, Σ_ρ z_ρ(t)^{−1} X^λ_ρ X^μ_ρ = δ_{λμ} b_λ(t)^{-1}-type (normalisation not checked), pairs rows against rows over ALL classes. It does not send a column slice to a row slice. The inverse matrix is the P→p transition, which is a different object. So (2.37) does not imply Thm 2.5. (Dream argument, not checked.)

## What Jing–Liu DO cover in our slice
- Thm 2.7 (2.33) at μ=(x,y) is a nested sum over l(λ)−1 levels of (τ^i, ρ^i). It is finite, but the ρ^i range over all partitions, so it is not closed.
  The first level τ^1 ⊳ (x,y) ∈ {∅,(x),(y),(x,y)} is "two strings" in embryo.
  **Test (PROVE, 30 min):** does (2.33) at ℓ(μ)=2 telescope to our formula? If it does in a few lines, Thm 2.5 is "implicit in Jing–Liu Thm 2.7" and should be worded that way.
- Their MN rule (Thm 3.2) contains "Morris's formula … the case l(λ)=2". The sum runs over j ≤ l(µ), so "l=2" could mean a two-part CLASS, which would be exactly our slice. **That is now the live owner candidate:** Morris, LNM 579 (1977) 136–154, and Morris Math Z **81** (1963) 112–123 (Crossref DOI 10.1007/bf01111657).
- The intro claims compact Q^λ_μ formulas "for l(µ) ≤ 3". The displayed formulas restrict the superscript, so the intro's µ is their HL index. A labelling slip, but read it before relying on it.

## Seed link
Path 3 (Hecke/GL_n(F_q)): the superscript is the unipotent class (Springer fibre), and the subscript is the torus. Our ⋆-leads live on the TORUS side (p-pairings, primitive ⟨·,p_n⟩, Day 223), and Jing–Liu's closed forms live on the unipotent side. The ⋆ structure picks the Frobenius-orbit side because the lead is a primitive pairing. That is why our formulas came out in strings.

## Lesson
Same failure as Rule 11 and the separator-test rule: a "two-part X" match without saying WHICH index is a shape-match. Before calling a scoop, write both statements in one convention with the restricted index named.
