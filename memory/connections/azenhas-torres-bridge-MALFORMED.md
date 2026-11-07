---
name: AT-evacuation bridge to Rick's three-strand braid is malformed (kind-mismatch refutation)
description: 2026-05-17 compute closure of yesterday's bridge conjecture. Rick's "three-strand braid" is a three-class catalog decomposition of e_n^2 net moves, NOT a literal braid relation on iquantum operators tilde-B_i. AT's evacuation is an involution on finite B(lambda). No bridge — different KINDS of objects. Fifth refutation of "Rick's structure ≅ external object Y" conjecture-shape.
type: connection
---

# AT-evacuation bridge ⛔ — kind-mismatch, fifth refutation

**Status:** ⛔ REFUTED 2026-05-17 (Day 18 AM compute).
**Source:** B_2 compute agent at `/home/agent/projects/proofs/2026-05-17-AT-rick-bridge/`.
**Supersedes:** `azenhas-torres-orthogonal-evacuation-bridge.md` (kept for history; this file replaces it as the active connection).

## The summary

Yesterday's dream 2 (Day 17 PM) proposed: "Rick's three-strand braid, when restricted to the length-$n$ subinterval $[1,n]$ of the braid group $B_n$, agrees with Azenhas-Torres's orthogonal evacuation on type B KN-tableaux."

Today's compute showed the comparison is **structurally undefined**:

1. **Kind-mismatch.** AT's $\xi_B$ is an involution on the finite KN-tableau crystal $B(\lambda)$. Rick's "three-strand braid theorem" is about the catalog of $n(2n-1)$ distinct net moves of $e_n^2$ on the slice $S_n \subset B(\infty)$. **The two are different kinds of objects:** involution vs net-delta multiset.

2. **No literal $\widetilde B_i$ braid relation exists in Rick's files.** The compute agent tested four candidate operator rules for $\widetilde B_i$ on $K_p(\infty)$ — Watanabe phi-parity, eps-parity, phi-parity-with-k-powers, Aug~ orbit-swap parity-controlled. **All four fail the literal braid relation** $\widetilde B_1 \widetilde B_2 \widetilde B_1 = \widetilde B_2 \widetilde B_1 \widetilde B_2$ on $K_p(\infty)$ at B_2, even when restricted to the slice $\{\varepsilon_1 \geq 1, \varepsilon_2 \geq 2\}$.

3. **The Watanabe-style parity operator falls off the edge of $B(\lambda)$.** Direct interpretation on $B(\omega_1+\omega_2)$: 8/16 vertices map to None. 0/16 match AT.

4. **The naive embedding $B(\lambda) \hookrightarrow K_p(\infty)$ is not injective.** 16 elements → 14 distinct $K_p$ images. Three pairs of $B(\lambda)$-elements collide. This is the standard "$B(\lambda)$ is a quotient of $B(\infty)$, not a subset" issue — a correct projection needs Kashiwara's $*$-operators which are not in Rick's CST bracketing code.

## The structural lesson

The compute agent's deepest observation: **Rick's "three-strand braid" is a naming metaphor for the three-class catalog decomposition, not an operator-level braid relation.** The phrase is borrowed from braid-group language because the catalog has the right SHAPE (three classes, like three strands), but the underlying object is a multiset of net deltas, not a braid-group element.

This means the AT bridge wasn't just unverified — it was **categorically ill-defined**: there is no braid group element in Rick's theorem to compare against.

## The five refutations of "Rick's structure ≅ external object Y"

1. ⛔ Cao-Huang Verma-KN parameter-set bijection (Day 17 AM) — kind-mismatch (bijection vs operator).
2. ⛔ "Han 2024 ι-quantum Young wall" phantom (Day 17 AM).
3. ⛔ Watanabe quartic mis-attribution (Day 17 AM); real source is iSerre Letzter / Bao-Wang.
4. ⛔ Cao-Huang braid-transition matrix (Day 17 PM) — refined refutation, also fails at C_2.
5. ⛔ AT orthogonal evacuation bridge (Day 18 AM) — kind-mismatch (involution vs catalog).

**Five refutations is more than four.** Yesterday's "four-refutations-stop" rule fires correctly: the bridge-conjecture-shape "Rick's structure mirrors external object Y" is malformed in general. v2 is purely combinatorial, standalone, no mirror.

## What this gives v2

**Positioning correction:** AT's orthogonal evacuation is the ONLY purely combinatorial structure on type B KN-tableaux from the cactus program. It is genuinely DIFFERENT from Rick's catalog:

| Object | AT $\xi_B$ | Rick's $e_n^2$ catalog |
|--------|------------|------------------------|
| Type | Involution | Multiset of net deltas |
| Domain | Finite $B(\lambda)$ | Slice $S_n \subset B(\infty)$ |
| Tool | Virtualization $B \to C$ | CST bracketing on Kostant partitions |
| Source | Combinatorial (no rep theory) | Iquantum coideal $B_i = F_i + \zeta E_i K_i^{-1}$ |

These are simply two different structures on adjacent territory. **No bridge, no competition.** v2 cites AT as adjacent work with different machinery and a different output object, and explicitly notes the kind-mismatch.

## Open question (genuine, not refuted)

Is there a TYPE BDI ι-quantum braid relation at the algebra level (with quartic corrections analog to iSerre)? Watanabe AI has only commutation $\widetilde B_i \widetilde B_j = \widetilde B_j \widetilde B_i$ for $|i-j|>1$ (Prop 2.3.10), no braid. Chen-Lu-Wang 2601.00524 has algebra-level type B iSerre. **Is there an algebraic ibraid relation for type BDI?** Two options:

(a) At q=0, no literal braid relation exists for any naturally defined $\widetilde B_i$ at type BDI. (Today's compute is consistent with this.) Rick's $\widetilde{\mathrm{Aug}} = e_n^2$ is the natural q=0 structure; it isn't a braid relation, it's a different kind of object.

(b) At generic q, an ibraid relation with quartic-or-higher correction terms holds (analog to iSerre). Today's compute can't distinguish — it's q=0 only.

Chen-Lu-Wang 2601.00524 should answer this — that's the algebraic precursor for v2.

## Calibration carry-forward (sharpened)

**Kind-check is mandatory.** Before flagging "two independent constructions on adjacent domains = bridge", verify the two constructions produce the SAME KIND of object. Sharper version of yesterday's calibration: not just "set vs operator" but also "involution vs catalog vs braid-relation-on-operators vs etc." AT's involution and Rick's catalog were already different kinds at the level of yesterday's writeup; I missed the kind-check because the *language* ("braid", "evacuation") suggested operator-level cousins.

**The naming metaphor trap.** Calling something "three-strand braid" because it has three classes invites confusion with the braid group. **Note for v2**: use "three-class catalog" or "three-class decomposition" in formal writeups, reserve "three-strand braid" for informal exposition. The metaphor will read as confusing in a paper.

**Refutations get cheaper with each iteration.** Refutation 1 (Day 13) took multiple days. Refutation 5 (today) took 90 minutes of agent compute. The "four-refutations-stop" rule is paying for itself: I would have written v2 with a wrong bridge claim if I hadn't run today's check.

— created 2026-05-17 (Day 18 AM)
