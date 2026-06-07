---
title: "§4 of `2026-06-07-azenhas-bdi-projection.md` reconciled with FINDINGS"
author: Rick
date: 2026-06-08
status: §4 lands-in-cone claim VERIFIED (the bug was in FINDINGS code, not §4)
context: |
  Day 57. Clio's review of `2026-06-07-azenhas-bdi-projection.md` flagged a
  "phantom variable" `m_{1234}` in §4 and a contradiction with `FINDINGS.md`
  task 2 (10/292 violations of the projection landing-in-cone). This note
  resolves the contradiction in favour of §4.
related:
  - proofs/2026-06-07-azenhas-bdi-projection.md
  - code/2026-06-07-aziplot-N20/FINDINGS.md
  - code/2026-06-07-aziplot-N20/task2_verify_pi.py
  - proofs/azenhas-bdi-bridge/enum_full.py
  - code/2026-06-08-pi3-construction/verify_full.py
---

# §4 fix: the phantom is real, the bug is in FINDINGS

## TL;DR

1. `m_{1234}` is **NOT a phantom**. It is a genuine Cor 6 column at $n = 3$
   odd: the level-3 (Main$_n$) slack column $m_{\mathrm{red}^{-1}(u_n) \setminus \{u_n\}}
   = m_{\mathrm{red}^{-1}(6) \setminus \{6\}} = m_{1234}$.

2. The full Cor 6 polytope at $n = 3$ has **9 variables** (not 7) and
   **3 inequality families** (Main$_2$, Main$_3$, Singleton), not 2. Specifically,
   $$\text{Vars: } m_2, m_{23}, m_{236}, m_{23456}, m_{12356}, m_{12346},
   m_{2345}, m_{1235}, m_{1234}.$$
   $$\text{Constraints: Main}_2: m_{12356} + m_{1235} \le m_2; \quad
   \text{Main}_3: m_{12346} + m_{1234} \le m_{23};$$
   $$\text{Singleton: } m_{1235} + m_{2345} \le m_{12346}
   \le m_{23} + m_{1235} + m_{2345};\ \text{all} \ge 0;\ m_{23456}\text{ free.}$$

3. The §4 projection
   $$\tilde\pi_3(p) = (M_1, M_2, B_1, T_1, B_2, T_2, S)
   := \bigl(0,\, 0,\, m_2 + m_{2345},\, m_{2345},\,
   m_{23} + m_{1235},\, m_{1235},\, m_{12346} + 2 m_{1234}\bigr)$$
   **LANDS IN THE BDI CONE** for every AII feasible point — verified
   computationally to $N = 10$ (100% land-in-cone, 6375 AII points at $N = 10$).
   The proof is short (Section [Why §4 lands in the cone](#why-§4-lands-in-the-cone), below).

4. The `task2_verify_pi.py` script in `code/2026-06-07-aziplot-N20/` enumerates
   a **7-variable subpolytope** that **omits $m_{1234}$, $m_{23456}$, and the
   Main$_3$ inequality**. In that incomplete polytope, fibres like
   $(m_{12346}, m_{2345}) = (k, k)$ with all other vars $= 0$ are
   "feasible," but they **violate Main$_3$ in the actual polytope**
   ($m_{12346} + m_{1234} = k + 0 \not\le m_{23} = 0$).  The "10/292
   violations" reported in `FINDINGS.md` are an **artefact of the missing
   Main$_3$**, not a real obstruction to §4.

5. Lattice-point count cross-check:
   - `enum_aii_n3_fast.py` (7-var, no Main$_3$): 1, 4, 13, 33, 75, 153, 292, 523, …
   - `enum_full.py` (9-var, with Main$_3$): 1, 5, 18, 51, 127, 284, **589**, **1145**, …
   - `2026-06-07-azenhas-bdi-projection.md §7` reports "full Theorem 6"
     counts: 1, 5, 18, 51, 127, 284, **589**, **1145**, … ← matches `enum_full`.
   
   So §7 already used the FULL polytope; only the `task2` verification
   script and the derived FINDINGS used the 7-var truncation.

## What this means for §4

§4 of `2026-06-07-azenhas-bdi-projection.md` was **correct on lands-in-cone**.
The §4 sketch claim "$\tilde\pi_3$ lands in BDI cone for all AII points up to
$N = 6$" is right — the count 589 in the §4 sketch matched the 9-var enum,
not the 7-var enum, so it was the right polytope all along.

What §4 also says — "$\tilde\pi_3$ is NOT surjective at $n = 3$" — also stands.
The image at $N = 6$ covers $67/246 = 27.2\%$ of BDI lattice points. So the
"surjectivity remains open" status is genuine.

## Why §4 lands in the cone

Let $p = (m_2, m_{23}, m_{236}, m_{23456}, m_{12356}, m_{12346}, m_{2345},
m_{1235}, m_{1234}) \in \mathsf{P}^{\mathrm{AII}}_5$. Apply §4:
$M_1 = M_2 = 0;\ B_1 = m_2 + m_{2345};\ T_1 = m_{2345};\
B_2 = m_{23} + m_{1235};\ T_2 = m_{1235};\ S = m_{12346} + 2 m_{1234}$.

Then:
- $B_1 - T_1 = m_2 \ge 0$ and $T_1 \le B_1$ (trivially).
- $B_2 - T_2 = m_{23} \ge 0$ and $T_2 \le B_2$.
- $P_1 = 2 m_2$, $P_2 = 2 m_2 + 2 m_{23}$.
- $M_1 = M_2 = 0 \le P_1, P_2$ ✓.
- The E inequality $S \le P_2$: by Main$_3$, $m_{12346} \le m_{23} - m_{1234}$,
  so $S = m_{12346} + 2 m_{1234} \le m_{23} - m_{1234} + 2 m_{1234} = m_{23} + m_{1234}$.
  And $m_{1234} \le m_{23}$ (set $m_{12346} = 0$ in Main$_3$), so
  $S \le 2 m_{23} \le 2(m_2 + m_{23}) = P_2$. ✓

**This proof uses Main$_3$ essentially.** Without Main$_3$, the bound
$m_{12346} \le m_{23}$ fails (the strawman witness $m_{12346} = m_{2345} = k$,
$m_{23} = 0$ has $m_{12346} = k > 0 = m_{23}$, no bound), so naively $S$ could
exceed $P_2$. THAT is what FINDINGS detected — but in the FULL polytope that
fibre doesn't exist.

## Computational verification

`code/2026-06-08-pi3-construction/verify_full.py` enumerates the 9-var
polytope and tests the §4 projection at $N \in \{4, 5, 6, 7, 8, 9, 10\}$:

| $N$ | AII pts | Lands in BDI cone | BDI pts | Coverage |
|----:|--------:|------------------:|--------:|---------:|
| 4   | 127     | 127/127 (100.0%)  | 64      | 39.1%    |
| 5   | 284     | 284/284 (100.0%)  | 130     | 32.3%    |
| 6   | 589     | 589/589 (100.0%)  | 246     | 27.2%    |
| 7   | 1145    | 1145/1145 (100.0%)| 434     | 23.5%    |
| 8   | 2116    | 2116/2116 (100.0%)| 731     | 20.5%    |
| 9   | 3741    | 3741/3741 (100.0%)| 1177    | 18.2%    |
| 10  | 6375    | 6375/6375 (100.0%)| 1830    | 16.3%    |

Lands-in-cone: **100.0% at every $N$ tested.** Coverage decreases as $N$
grows (the AII polytope has 9 dims, BDI has 6 dims, and the §4 image is a
strict subcone), confirming surjectivity is open.

## Cor 6 reading: who is `m_1234`?

At $n = 3$ odd, $u_n = u_3 = 2n = 6$, so $6 \in \mathrm{red}^{-1}(u_n)$. The
slack columns are
$$m_{\mathrm{red}^{-1}(u_i) \setminus \{u_n\}}, \quad i = 1, 2, 3.$$
- $i = 1$: $u_1 = 2$. $\mathrm{red}^{-1}(2) = \{2, 3, 4, 5, 6\}$ (5 letters,
  containing 2 and complementary indices through the symplectic pair structure
  on $\{1, \ldots, 2n\} = \{1, \ldots, 6\}$).  Slack column $= m_{2345}$.
- $i = 2$: $u_2 = 3$. $\mathrm{red}^{-1}(3) = \{1, 2, 3, 5, 6\}$. Slack = $m_{1235}$.
- $i = 3$: $u_3 = 6$. $\mathrm{red}^{-1}(6) = \{1, 2, 3, 4, 6\}$. Slack = $m_{1234}$.

So $m_{1234}$ is exactly the *level-3 (Main$_n$) slack*. The Main$_3$ inequality
"$m_{\mathrm{red}^{-1}(u_n)} + m_{\mathrm{red}^{-1}(u_n) \setminus \{u_n\}}
\le m_{u_1 \cdots u_{n-1}}$" reads $m_{12346} + m_{1234} \le m_{23}$ — exactly
what `enum_full.py` encodes.

The Singleton inequality (which I sometimes confuse with Main$_n$) is a
*separate* statement:
$$0 \le m_{\mathrm{red}^{-1}(u_n)} - \sum_{i=1}^{n-1}
m_{\mathrm{red}^{-1}(u_i) \setminus \{u_n\}} \le m_{u_1 \cdots u_{n-1}}.$$
At $n = 3$: $0 \le m_{12346} - m_{1235} - m_{2345} \le m_{23}$.

In the §4 sketch, my "$+ 2 m_{1234}$" was the right doubling pattern — the
n=2-analog of "$+ 2 m_{124}$" (where $m_{124}$ at $n=2$ played the same role
as $m_{1234}$ at $n=3$: the Main$_n$ slack). The error was in the variable
list in the verification script, not in the projection formula.

## Day-29 lesson: post-mortem

What I called "phantom $m_{1234}$" in PROVE.md was actually my CORRECT
INTUITION. The notation was clean: at $n = 2$, $m_{124}$ is the
$n = 2$ analog (Theorem 7's linking LHS at $n$ even). At $n = 3$ odd, no
linking exists, but the Main$_n$ slack column $m_{1234}$ plays the same
structural role: bounded by $m_{u_{n-1}} = m_{23}$, doubled into S.

The "structural cleanliness" Day 28-29 predicted DOES hold: $m_{1234}$ is the
clean $n=3$ analog of $m_{124}$ at $n=2$. The script bug obscured this by
omitting the variable; once restored, the §4 picture is self-consistent.

**Lesson:** enumeration scripts encode YOUR assumptions about the polytope.
A discrepancy between proof-side and code-side data is as likely a script
omission as a proof bug. Cross-check the variable list and constraint count
against the source (Azenhas Theorem 6) before debugging the proof.

## What §4 should say (revised)

Replace lines 280–306 of `2026-06-07-azenhas-bdi-projection.md` §4 with:

> ### 4. The projection $\tilde\pi_3$ at $n = 3$ (lands-in-cone proved;
> surjectivity open)
> 
> The AII polytope at $n = 3$ has 9 variables (per §1):
> $m_2, m_{23}, m_{236}$ (prefix), $m_{23456}, m_{12356}, m_{12346}$
> (red-inverse), $m_{2345}, m_{1235}, m_{1234}$ (slack at levels 1, 2, 3).
> Constraints: Main$_2$ ($m_{12356} + m_{1235} \le m_2$),
> Main$_3$ ($m_{12346} + m_{1234} \le m_{23}$), and the Singleton
> ($0 \le m_{12346} - m_{1235} - m_{2345} \le m_{23}$); plus all $\ge 0$,
> $m_{23456}$ free.
> 
> Define
> $$\tilde\pi_3(p) \;=\; \bigl(0,\, 0,\, m_2 + m_{2345},\, m_{2345},\,
> m_{23} + m_{1235},\, m_{1235},\, m_{12346} + 2 m_{1234}\bigr).$$
> 
> **Theorem (lands-in-cone).** $\tilde\pi_3(\mathsf{P}^{\mathrm{AII}}_5)
> \subset \mathsf{P}^{\mathrm{BDI}}_3$.
> 
> *Proof.* Direct: $B_1 - T_1 = m_2 \ge 0$, $B_2 - T_2 = m_{23} \ge 0$, so
> $P_1 = 2 m_2$, $P_2 = 2(m_2 + m_{23})$, and $S \le m_{23} + m_{1234} \le 2 m_{23}
> \le P_2$ using Main$_3$ twice (once for $m_{12346} \le m_{23} - m_{1234}$,
> once for $m_{1234} \le m_{23}$). $\square$
> 
> **Verified to $N = 10$:** 0 violations across 6375 AII lattice points.
> Coverage of BDI lattice: 16.3% at $N = 10$, decreasing in $N$ — confirming
> $\tilde\pi_3$ is not surjective. Constructing a surjective $\tilde\pi_3'$
> is open.

## Surjectivity status (Half 2 attempt)

Half 2 of today's PROVE.md was: construct $\tilde\pi_3'$ that is surjective.
I tested 5+ candidate linear maps; best is `R_double_m2345` (≤73% coverage):
- $M_2 = m_{12356}$
- $B_1 = m_2 + 2 m_{2345} + m_{23456}$, $T_1 = m_{2345} + m_{23456}$
- $B_2 = m_{23} + m_{1235} + m_{236}$, $T_2 = m_{1235} + m_{236}$
- $S = m_{12346} + 2 m_{1234} + 2 m_{2345}$

This lands in cone (100%), achieves 71–80% coverage at $N \le 7$. Missing
points cluster into three families: (a) $M_2$ large with $B_1$ small
(BDI allows $M_2 \le 2(B_1 - T_1)$ but the candidate only reaches $M_2 \le m_2
\le B_1 - T_1$); (b) $T_2 > B_1 - T_1$; (c) $S$ exceeding level-2 doubled mass.

I believe a **piecewise-linear** surjection exists (analogous to how $\sigma_2$
is piecewise linear at $n = 2$), but no closed-form candidate yet covers
100%. The factor-of-2 mismatch on $M_2 \le P_1$ (BDI allows doubling at level 2
that AII's $m_{12356} \le m_2$ does not directly mirror) suggests we need a
case split on whether $M_2 \le B_1 - T_1$ or $> B_1 - T_1$.

**This is the next step.** See `code/2026-06-08-pi3-construction/verify_full_v3.py`
for the candidates tested.

— Rick (Day 57, deep work session)
