# Related-work patch: Chen-Lu-Pan-Ruan-Wang arXiv:2601.00524

**Status:** DRAFTED (Day 42, 2026-05-27). **NOT shipped to Robin.** Tarball
remains byte-identical. Held in reserve until v3 hits arXiv or Robin asks
for a related-work update.

**Verdict basis:** `/home/agent/projects/proofs/2026-05-27-chen-lu-bdi-orthogonal.md`
(OQ-CHEN-LU = ORTHOGONAL).

---

## Intended insertion point

`main.tex` §1.4 ("Related work and external shadows"), after the existing
"Algebra-level type-B foundations" paragraph (which currently mentions
Chen-Lu-Wang `\cite{CLW}` and Jian-Luo-Wu `\cite{JLW}`). Insert as a new
short paragraph BEFORE the Watanabe-2107 paragraph or as a one-sentence
addition to the existing CLW/JLW paragraph.

## Draft text (option A — one new sentence, minimal)

> Most recently, Chen-Lu-Pan-Ruan-Wang \cite{ChenLuPanRuanWang2601} have
> constructed dual canonical bases for the universal $\imath$quantum group
> $\widetilde{U}^\imath$ of arbitrary finite type (including split BDI) via
> the iHopf algebra framework of \cite{CLPRW25}; this is a parallel lane on
> the canonical-basis side that does not interact with the crystal-level
> chain-singleton decomposition addressed here.

## Draft text (option B — short paragraph, more contextual, ~80 words)

> Most recently, Chen-Lu-Pan-Ruan-Wang \cite{ChenLuPanRuanWang2601}
> constructed dual canonical bases for the universal $\imath$quantum group
> $\widetilde{U}^\imath$ associated to any quasi-split Satake diagram of
> finite type, via the iHopf algebra framework of \cite{CLPRW25}, and proved
> ibraid-group invariance. Their construction covers the split type-$B$
> Satake diagram parametrically (alongside all other finite types) but is
> type-uniform, with no chain-singleton decomposition or short-long-edge
> analysis; the carry $P_a$ does not feature in their machinery. The
> present paper's contribution is complementary, working at $q = 0$ on
> the PBW (Kostant partition) lattice rather than on the canonical basis.

## BibTeX entry to add

```bibtex
@article{ChenLuPanRuanWang2601,
  author  = {Chen, Jiayi and Lu, Ming and Pan, Xiaolong and Ruan, Shiquan and Wang, Weiqiang},
  title   = {{iQuantum} groups and {iHopf} algebras {II}: Dual canonical bases},
  journal = {Preprint, arXiv:2601.00524},
  year    = {2026},
  note    = {arXiv:2601.00524 [math.QA]},
  url     = {https://arxiv.org/abs/2601.00524},
}
```

## Recommendation

**Option A** (one sentence) is sufficient. v3's audience does not need
a longer treatment — the orthogonality is structural and immediate once
named. Option B is reserved for the case where a reviewer specifically
asks for elaboration on the canonical-basis-side lane.

## Companion patch already drafted

`papers/v3-bdi-unified-carry/related-work-kobayashi-patch.md` (Day 41,
also held in reserve). Both patches can ship together when v3 hits arXiv
or when Robin requests a related-work refresh.

— Rick, Day 42
