# Does Wang-Wang 2608.22184 cite Shareshian-Wachs 2016?

**Opened:** 2026-09-09 (Day 183 dream, from Browse 136 vs 137 discrepancy).
**Status:** Open. Blocks Wang-Wang letter decision.

## Question

Wang-Wang 2608.22184 (spider graphs, restricted modular law): does their reference list contain Shareshian-Wachs 2016 (or any SW citation for the path-graph base case)?

## The discrepancy

- **Browse 136 (2026-09-08):** "Wang-Wang cites SW 2016 for $X_{P_n}$ via path-clique bootstrap in Section 9."
- **Browse 137 (2026-09-09):** Semantic Scholar reference list for Wang-Wang contains NO SW 2016; path-graph foundation is entirely via Huh–Hwang–Kim–Kim–Oh 2504.09123.

One of the subagents is confabulating; likely Browse 136's, since Semantic Scholar structured data is usually reliable.

## Why it matters

**Rick's letter framing depends on this:**
- If Wang-Wang cites SW 2016 → their path-graph base case is SW 2016; Rick's Theorem B is a sharper (algebraic GF vs existence) alternative; letter framing = "SW 2016 gave you existence; Theorem B gives you the closed form you need for downstream refinements."
- If Wang-Wang cites Huh–Hwang–Kim–Kim–Oh 2504.09123 only → their path-graph facts are pulled from the restricted modular law paper, which itself doesn't compute path-graph e-coefficients. Rick's Theorem B is even more upstream than expected; letter framing = "you're using restricted modular law without knowing the algebraic GF for the base case that generates it."

## Action

Next wake session: direct HTML fetch of arXiv:2608.22184 abstract + bibliography (or PDF if abstract not enough). 10 min.

Search PDF/HTML for:
- "Shareshian" (author name)
- "Wachs" (author name)
- "2016" (year)
- "chromatic quasisymmetric functions" (topic)

Report Wang-Wang's actual path-graph citation. Update `feedback_webfetch_echoes_prompt_vocabulary.md` if this is another case of subagent confabulation.

## Cross-references

- Related feedback: `feedback_webfetch_echoes_prompt_vocabulary.md` (subagent hallucination pattern; may apply here).
- Related connection: `connections/2026-09-09-stanley-gasharov-dead-rick-territory.md` (Rick's letter opportunity depends on this).
- Related reading: `reading/2026-09-08-browse135.md` and `reading/2026-09-08.md` (Browse 135/136 where original claim originated).
- Related reading: `reading/2026-09-09-browse137.md` (today's contradiction).

**CLOSED 2026-09-25 (Day 206 dream prune).** Day 184 wake verified that Wang–Wang 2608.22184 cites SW 2016 correctly (Browse 136 right, Browse 137 wrong).
