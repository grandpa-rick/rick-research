# For Robin: the Remark-4.7 obstruction has a structural answer

**Date:** 2026-05-06
**Context:** OQ2 / sharpening Choi–Kim–Lee
**Length:** ~600 words. Skim-friendly.

## TL;DR

The Choi–Kim–Lee Remark 4.7 example $\mathrm{KL}^{B_2}_{(1,0),(0,0)}(q,t) = qt - q + t$ has a structural explanation. The polynomial **is** the bigraded Euler characteristic of the BGG-Verma resolution of $V(\omega_1)$ restricted to weight 0. The negative coefficient comes from a precise **bidegree-disjointness** between $M(\omega_1)_0$ and $M(s_2\!\cdot\!\omega_1)_0$:

* $M(\omega_1)_0$ has $(q,t)$-bigraded support $\{(0,1), (1,1)\}$ — the two paths from $(1,0)$ to $0$ in $\mathrm{Sym}(\mathfrak n_+)$.
* $M(s_2\!\cdot\!\omega_1)_0$ has $(q,t)$-bigraded support $\{(1,0)\}$ — the single long-root step from $(1,-1)$ to $0$.
* These supports are **disjoint**, so $-q$ has nothing to cancel against.

This rules out *any* positive combinatorial formula on a fixed set: the coefficient at bidegree $(1,0)$ is intrinsically negative.

## What I actually proved

In `~/projects/proofs/2026-05-06-remark-47-obstruction.md` (full writeup; this note is the elevator):

**Theorem (the Euler-characteristic identity, easy but central).** For any finite simple Lie algebra **g** with split root system, with the Macdonald-style two-parameter Lusztig polynomial,

$$
\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \sum_{i\ge 0} (-1)^i \dim_{q,t}\Bigl(\bigoplus_{\ell(w)=i}M(w\!\cdot\!\lambda)_\mu\Bigr).
$$

This is just the WCF + Kostant. But it gives a **bidegree-by-bidegree** equation:
$$
[q^a t^b]\,\mathrm{KL}^{\mathfrak g}_{\lambda,\mu}(q,t) \;=\; \mathrm{mult}_{(a,b)}\!\Bigl(\bigoplus_{\text{even }w}M(w\!\cdot\!\lambda)_\mu\Bigr) \;-\; \mathrm{mult}_{(a,b)}\!\Bigl(\bigoplus_{\text{odd }w}M(w\!\cdot\!\lambda)_\mu\Bigr).
$$

So the coefficient is negative ⟺ at bidegree $(a,b)$ the odd-$w$ multiplicities exceed the even-$w$ multiplicities.

For the Remark-4.7 case, the bidegree $(1,0)$ has multiplicity 0 in $M(\omega_1)_0$ but multiplicity 1 in $M(s_2\!\cdot\!\omega_1)_0$ — and there's nothing else around to cancel it. **This is the obstruction, sharply.**

## What it means for OQ2

The energy-sum-on-crystal formula (CKL Thm 4.1, 4.6) is *necessarily* a single positive sum, hence cannot reach polynomials with negative coefficients. For non-spin type B (and conjecturally all "non-aligned" cases, type D, etc.), the right replacement is **not** a single positive sum but one of:

1. **The signed BGG-Verma sum** itself (canonical but trivially built-in signed).
2. **A 2-term virtual class** $\mathcal E^+(q,t) - \mathcal E^-(q,t)$ where each $\mathcal E^\pm$ is a positive sum over Kostant partitions of even/odd-length Weyl elements respectively. For Remark 4.7: $\mathcal E^+ = t + qt$, $\mathcal E^- = q$.
3. **An honest Tor / derived structure** where positivity holds in degree 0 but H^1 is nonzero. This is the natural "derived Brylinski" picture and connects directly to the Almousa–Lu Koszul/derived-ribbon viewpoint we just absorbed.

The H^0/H^1 picture is *exactly* what Almousa–Lu's acyclic ribbon complex categorifies in the *positive* case (NSym ribbon-product expansion). Non-spin type B is the **first natural example where the analogous complex is non-acyclic**.

## Why spin saves the day, in one line

The half-shift $\mu \to \mu + (\frac12)^n$ shifts the $\beta_w$-displacements by integer amounts that **align** odd-length-Verma bigraded supports with even-length supports — making the alternating sum genuinely positive. I verified this for several B_2 spin pairs (`bgg_decomposition.py`).

## Where I'm asking for help

* Conjecture 4.1 (a closed-form positivity criterion in terms of (λ, μ) for B_n, $n \ge 3$) needs verification.
* Conjecture 4.2 (existence of an honest bigraded chain complex with the right Euler char) needs construction. The natural candidate is the BGG-Verma complex with bidegree shifts; making the differentials genuinely bigraded is the technical issue.
* I haven't connected this back to the *unequal-parameter Hecke algebra Kazhdan–Lusztig* picture (Geck–Pfeiffer-style). The negative coefficients are presumably the well-known unequal-parameter K-L positivity failure, but I haven't dotted that line.

If you have (a) views on how to make the bigraded BGG complex into an honest chain complex, or (b) a sense of whether the unequal-parameter K-L people have a clean positivity-criterion for our (λ, μ), that would be useful.

## Files
- `~/projects/proofs/2026-05-06-remark-47-obstruction.md` — the full writeup.
- `~/projects/proofs/remark47/compute_kl_B2.py` — direct WCF computation, scanned dominant pairs $\lambda_1 \le 4$.
- `~/projects/proofs/remark47/bgg_decomposition.py` — Verma decomposition by Weyl element (visible bidegree supports per term).
