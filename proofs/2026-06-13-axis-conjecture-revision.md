---
title: "Day 68 PROVE: # AXIS conjecture revised — uniform 3 across n ≥ 3"
author: Rick
date: 2026-06-13
status: Day-62 conjecture # AXIS(n) = 3 - [n even] REFUTED at n=4 (Day-67).
        Replaced with C1: # AXIS(n) = 3 uniformly, with AXIS triple
        {prefix[1], prefix[n], long[1]} at all n ≥ 3 where the R-double
        backbone is BDI-feasible. Decomposition: 1 (R-double / adj(sl_2))
        + 2 (bulk Bucket-2). Prediction at n=5: # AXIS = 3.
related:
  - proofs/2026-06-12-bucket0-algebraic-origin.md (Day-66 R-double = adj(sl_2))
  - proofs/2026-06-12-azenhas-inequalities-read.md (Day-67 Azenhas verdict)
  - code/2026-06-12-n4-rdouble-correction/ (Day-67 # AXIS = 3 at n=4)
  - code/2026-06-13-axis-n3-verify/ (Day-68 # AXIS = 3 at n=3 verified)
---

# §1. Day-67 refutation recap

The Day-62 conjecture stated
$$
\#\mathrm{AXIS}(n) = f(n) = 3 - [n \text{ even}]
\qquad (\text{predicting 3 at odd } n, 2 \text{ at even } n).
$$
It was claimed verified at $n = 3$ (3 AXIS vars: $m_2, m_{236}, m_{23456}$)
and at $n = 4$ (2 AXIS vars: $\mathrm{long}[1], \mathrm{prefix}[4]$ —
the Day-64 REPORT).

**Day-67 CODE refuted the $n = 4$ count.** The Day-64 20-piece $n = 4$
piece registry **missed the R-double family** — three BDI-feasible
pieces with $\alpha \in \{0, 1, 2\}$ differing only in
$c_{\mathrm{prefix}[1]}[S] = \alpha$. Adding them yields a 23-piece
corrected registry where $\mathrm{prefix}[1]$ is **AXIS** (3 distinct
columns, 3 pair-collisions on $\{\mathrm{prefix}[1] = 0\}$), giving
$$
\#\mathrm{AXIS}(n = 4) = 3 \neq 2 = f(4).
$$

This is the genuine refutation: the Day-62 formula $3 - [n\text{ even}]$
gave 2 at $n = 4$, but the actual count (with the complete piece
registry) is 3. The Day-64 "verification" was an artifact of a
**registry incompleteness**, not a structural identity.

We had three replacement candidates on the table going into Day 68:

- **(C1) Uniform-3:** $\#\mathrm{AXIS}(n) = 3$ for all $n \ge 3$.
- **(C2) Split:** $\#\mathrm{AXIS}_{\text{core}}(n) = 3 - [n\text{ even}]$
  + $\#\mathrm{AXIS}_{\text{R-double}}(n) = 1$. Combined: $4 - [n\text{ even}]$.
- **(C3) Wrong invariant:** parity belongs to a different sub-count.

# §2. Phase 1 — n = 3 re-derivation with R-double family

## 2.1. The question

Was the Day-62 count $\#\mathrm{AXIS}(n = 3) = 3$ computed with the
R-double family included, or under an incomplete registry?

## 2.2. The data

The $n = 3$ minimal 26-piece cover (`MIN_COVER_26` in
`code/2026-06-10-toric-quotient/analyze_torus.py`) **explicitly includes**
the three R-double pieces:
- `R_double_m2345` ($\alpha = 0$)
- `P5d_Rdouble_plus_m2` ($\alpha = 1$)
- `P7_Rdouble_m2_dbl_S` ($\alpha = 2$)

These are the Bucket-0 family identified in Day-66 as the weight
multiset of $\mathrm{adj}(\mathfrak{sl}_2) = V(2\omega_1)$.

## 2.3. The verification (computed today)

Running `code/2026-06-13-axis-n3-verify/n3_axis_verify.py` on the
26-piece cover with the same strict-AXIS criterion as Day-67 ("coord
wall with $\ge 3$ rank-1 piece-pair collisions"):

| Registry | # pieces | AXIS variables | # AXIS |
|---|---|---|---|
| n=3 FULL 26-piece (R-double IN)   | 26 | $\{m_2, m_{236}, m_{23456}\}$  | **3** |
| n=3 MINUS R-double (23-piece)     | 23 | $\{m_{236}, m_{23456}\}$        | 2 |

(Detailed output: `code/2026-06-13-axis-n3-verify/results.json`.)

## 2.4. The mechanism

**Identical to $n = 4$.** The 3 R-double pieces share identical
columns on every AII variable EXCEPT $m_2$ (at $n = 3$) /
$\mathrm{prefix}[1]$ (at $n = 4$); they differ only in the $S$-entry
of the $m_2$ / $\mathrm{prefix}[1]$ column by $\alpha \in \{0, 1, 2\}$.

Hence pairwise differences among the 3 R-double pieces are rank-1
matrices supported entirely on the $\mathrm{prefix}[1]$ column. This
yields exactly $\binom{3}{2} = 3$ piece-pair collisions on the wall
$\{\mathrm{prefix}[1] = 0\}$, meeting the strict $\ge 3$ threshold.

**Striking $n = 3$ observation.** At $n = 3$, $m_2$ already had 4
distinct column types across the 26 pieces, but **only 1**
piece-pair collision on $\{m_2 = 0\}$ if R-double is removed (so it
would fail the strict $\ge 3$ AXIS test). The R-double family
**provides exactly the 3 additional pair-collisions** that push $m_2$
into AXIS by the strict criterion.

At $n = 4$, $\mathrm{prefix}[1]$ has only 1 distinct column under the
Day-64 registry (RIGID by colcount); the R-double family provides
the **first 3 distinct columns**, immediately also providing 3
pair-collisions.

The 3-pieces-3-pair-collisions structure is universal:
$\binom{3}{2} = 3$ from any 3-piece $A_1$-orbit on $\{0, 1, 2\}$.

## 2.5. Conclusion for n = 3 and n = 4

$$
\boxed{\#\mathrm{AXIS}(n = 3) = \#\mathrm{AXIS}(n = 4) = 3, \quad
\text{with AXIS triple } \{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}.}
$$

**Candidate C1 (uniform-3) is the answer.** C2 (split with parity)
would require $\mathrm{prefix}[1]$ at $n = 4$ to NOT be AXIS even
with the R-double family; the data refutes this. C3 (wrong
invariant) is unnecessary now that C1 fits.

The Day-62 conjecture happened to coincide with the truth at $n = 3$
($3 = f(3)$) but for the wrong reason — and broke at $n = 4$.

# §3. Phase 2 — Structural argument and n = 5 prediction

## 3.1. The decomposition

The three AXIS variables have distinct structural origins:

**(i) prefix[1] is AXIS via the R-double family (rep-theoretic origin).**

The R-double $n$-backbone (Day-66, §5):
$$
\begin{aligned}
M_2 \leftarrow L_2,\quad M_i \leftarrow L_i \ (3 \le i \le n - 1),\\
B_1 \leftarrow P_1 + 2 S_1 + L_1,\quad T_1 \leftarrow S_1 + L_1,\\
B_i \leftarrow P_i + S_i + P_{i+1},\quad T_i \leftarrow S_i + P_{i+1}, \quad 2 \le i \le n - 1,\\
B_n \leftarrow P_n + S_n + \Lambda,\quad T_n \leftarrow S_n + \Lambda,\\
S \leftarrow L_n + 2 S_n + 2 S_1 + \alpha\,P_1.
\end{aligned}
$$
(At $n = 3$ this collapses to the $m_2 + 2 m_{2345} + m_{23456}$ /
$m_{2345} + m_{23456}$ / etc. spec; at $n = 4$ to the spec in
`make_r_double_n4` of `n4_rdouble_corrected.py`.)

**BDI-feasibility caps $\alpha \le 2$** (constraint $S \le P_2$). The
cap is sharp at $n = 3$ and $n = 4$ — verified computationally.

Hence the R-double family gives 3 BDI-feasible variants with
$c_{P_1}[S] = \alpha \in \{0, 1, 2\}$. These contribute $\binom{3}{2}
= 3$ piece-pair collisions on $\{\mathrm{prefix}[1] = 0\}$, making
$\mathrm{prefix}[1]$ strict-AXIS.

This is the $V(2\omega_1) = \mathrm{adj}(\mathfrak{sl}_2)$ slot:
its 3-dimensionality is rep-theoretic, **uniform in $n$**.

**(ii) prefix[n] is AXIS via Bucket-2 combinatorics (combinatorial origin).**

$\mathrm{prefix}[n]$ is the "free top prefix" — at $n = 3$, $m_{236}$
(the length-$n$ symplectic HW column); at $n = 4$, $\mathrm{prefix}[4]$.

In Azenhas's Cor 6 / Theorem D (or E), $\mathrm{prefix}[n]$ is one of
the **free-extrusion directions** (Day-67 verdict, §1e): it does not
appear in any nontrivial mixed inequality. In the Rick framework,
this corresponds to many possible BDI routings (M_2 or M_i, T, B,
or S layers).

The Bucket-2 piece registry exhibits 7 distinct columns for
$\mathrm{prefix}[n]$ at $n = 4$ (10 at $n = 3$); the column-wall
$\{\mathrm{prefix}[n] = 0\}$ has $\ge 21$ piece-pair collisions
($\ge 23$ at $n = 3$). Far above the $\ge 3$ AXIS threshold.

**(iii) long[1] is AXIS via Bucket-2 combinatorics (combinatorial origin).**

$\mathrm{long}[1]$ is the "free bottom direction" / red-inverse
engine column $\bar\varepsilon_1$ — at $n = 3$, $m_{23456}$.

In Azenhas's framework, $\mathrm{long}[1]$ is also a free-extrusion
direction. In the Rick framework, $\mathrm{long}[1]$ appears in many
piece routings (T_1, M_2, S, mixed). Bucket-2 gives 9 distinct
columns at $n = 4$ (9 at $n = 3$) with the largest pair-collision
count on $\{\mathrm{long}[1] = 0\}$ ($\ge 44$ at $n = 4$, $\ge 9$ at
$n = 3$).

## 3.2. Why no other AII variable is AXIS

- **Bounded prefix variables** $\mathrm{prefix}[2], \ldots,
  \mathrm{prefix}[n - 1]$: each is bounded above by some other
  variable through Cor 6 / Theorem D upper-bound inequalities (e.g.
  $\mathrm{prefix}[2]$ bounds combinations of bumped variables).
  These force the column types and they are RIGID (1 col each at
  both $n = 3, 4$).
- **Balanced long variables** $\mathrm{long}[2], \ldots,
  \mathrm{long}[n]$: bound to specific $(B_i, T_i)$ routings
  (the "$M_i$ engine" channel). RIGID or BINARY.
- **Short / slack variables**: BINARY at $n = 3$, gauge-tied at
  even $n$ (artifact of Cor 8 substitution). Pair-collision counts
  on their coord walls are 1–3, mostly off-axis (mixed-coord walls).

## 3.3. The unified statement

**Theorem (Day-68 working theorem, $n = 3, 4$ verified, $n \ge 5$ conjectural):**
For all $n \ge 3$ where the R-double backbone is BDI-feasible,
$$
\#\mathrm{AXIS}(n) = 3
\qquad \text{with AXIS triple}\quad
\{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}.
$$
The decomposition
$$
\#\mathrm{AXIS}(n) = \underbrace{1}_{\substack{\text{R-double / } V(2\omega_1) \\ \text{(prefix}[1]\text{)}}}
+ \underbrace{2}_{\substack{\text{Bucket-2 / free-extrusion} \\ \text{(prefix}[n], \mathrm{long}[1]\text{)}}}
$$
is the head-vs-bulk split established in Day-66 (Bucket-0 + Bucket-1
$\cong \mathfrak{gl}_2$-rep-theoretic head + Bucket-2 combinatorial
bulk).

## 3.4. Prediction at n = 5

$$
\boxed{\#\mathrm{AXIS}(n = 5) = 3, \quad \text{AXIS} = \{\mathrm{prefix}[1], \mathrm{prefix}[5], \mathrm{long}[1]\}.}
$$

- $\mathrm{prefix}[1]$: 3 R-double pieces ($\alpha \in \{0, 1, 2\}$;
  the $n = 5$ R-double backbone is constructible by the recipe in
  §3.1, and the $\alpha \le 2$ cap should hold by the same
  $S \le P_2$ argument).
- $\mathrm{prefix}[5]$: free-extrusion top prefix.
- $\mathrm{long}[1]$: free-extrusion bottom direction.

**Verification target.** Construct the $n = 5$ piece registry analog
of `n4_rdouble_corrected.py` (with R-double family included from the
start, no Day-64-style incomplete-registry artifact). Verify
# AXIS = 3 and identify the 3 AXIS vars. (Open as Day-68 CODE
follow-up.)

## 3.5. Where the predictions could fail

- **R-double backbone fails BDI-feasibility at some $n$.** Day-66
  conjectures the family extends to all $n \ge 3$; if it fails at,
  e.g., $n = 6$ even, then $\mathrm{prefix}[1]$ would lose its AXIS
  status and the count drops to 2. **Check at $n = 5, 6$.**
- **The $\alpha \le 2$ cap changes at some $n$.** If, e.g., the cap
  becomes $\alpha \le 3$ at large $n$ (4-piece $A_1$-orbit
  $\{0,1,2,3\}$), then $\#\mathrm{AXIS}(n)$ stays at 3 but the
  R-double piece-pair count on $\{\mathrm{prefix}[1] = 0\}$ jumps
  to $\binom{4}{2} = 6$. **Test the cap analytically.**
- **Bulk-AXIS variables shift identity at some $n$.** If the bulk
  combinatorics produce a different free-extrusion structure (e.g.,
  more or fewer free directions), then the AXIS triple may shift.
  **Watch the bulk piece counts.**

# §4. Phase 3 — Connection to Azenhas dim-gap parity + v4 §3 impact

## 4.1. The Day-58 dim-gap parity (recall)

Azenhas's Theorem D (odd $n$): $n$ inequalities, no linking equality.
Theorem E (even $n$): same $n$ inequalities + Cor 8 linking equality.
The linking equality reduces the AII polytope dim by 1 at even $n$
(Day-58 / Day-59 confirmation):
$$
\begin{aligned}
\dim P^{AII}(n)  &= 3n \ (n \text{ odd}),\quad 3n - 1\ (n \text{ even}); \\
\dim P^{BDI}(n)  &= 3n - 3 \ (\text{uniform}); \\
\Delta(n) := \dim P^{AII} - \dim P^{BDI} &= 3\ (n \text{ odd}),\quad 2\ (n \text{ even}).
\end{aligned}
$$
So $\Delta(n) = 3 - [n\text{ even}]$, the **same formula** as the
Day-62 # AXIS conjecture. At $n = 3$, $\Delta(3) = 3 = \#\mathrm{AXIS}(3)$;
coincidence. At $n = 4$, $\Delta(4) = 2 \ne 3 = \#\mathrm{AXIS}(4)$;
the identity breaks.

## 4.2. The dim-gap parity survives — but is NOT an # AXIS identity

The dim-gap parity 3-vs-2 is a robust feature of the **AII polytope
dimension** at parity of $n$, traceable to the Cor 8 linking equality
(an Azenhas Theorem E vs D structural asymmetry). It is independent
of the Rick-side # AXIS count.

**Old v4 §3 narrative:**
> "Three coordinate walls at odd $n$, two at even $n$, controlled by
> Azenhas Theorem D vs E parity via $\Delta(n) = \#\mathrm{AXIS}(n)$."

**New v4 §3 narrative:**
> "Three coordinate walls at every $n \ge 3$ where the R-double
> backbone is BDI-feasible. Decomposition: 1 rep-theoretic
> ($\mathrm{adj}(\mathfrak{sl}_2)$-derived $\mathrm{prefix}[1]$ AXIS) +
> 2 combinatorial (free-extrusion $\mathrm{prefix}[n]$ and
> $\mathrm{long}[1]$ AXIS).
>
> The dim-gap parity $\Delta(n) = 3 - [n\text{ even}]$ is a separate
> structural identity, controlled by Azenhas's Cor 8 linking
> equality (Theorem E) at even $n$, with $\Delta$ measured at the
> AII polytope dimension, NOT at the # of AXIS walls. The Day-62
> coincidence $\Delta(3) = \#\mathrm{AXIS}(3) = 3$ at $n = 3$ is
> resolved: it's a numerical accident, not a structural identity."

## 4.3. The Azenhas link that does survive

The 2 bulk-AXIS variables ($\mathrm{prefix}[n], \mathrm{long}[1]$)
ARE among the 3 free-extrusion directions of Azenhas's $\mathfrak k$-HW
subpolytope (Day-67 §3d). The 3rd free-extrusion direction at $n = 3$
is $m_{1234}$ (weight-0 bumped column) — which is BINARY in Rick's
framework, not AXIS. The R-double-derived AXIS variable
$\mathrm{prefix}[1]$ is NOT free in Azenhas's polytope (it is the
RHS of the $m_{12356} + m_{1235} \le m_2$ upper bound, Cor 6).

So the Rick AXIS triple is **not** the Azenhas free-extrusion
triple. The overlap is 2 variables (the bulk AXIS / 2 of 3
Azenhas-free), differing in the third slot:
- Rick AXIS 3rd: $\mathrm{prefix}[1]$ (rep-theoretic R-double).
- Azenhas free 3rd: weight-0 bumped column ($m_{1234}$).

This is a structural distinction between the rep-theoretic head
(prefix[1] in Rick) and the combinatorial-trivial slot (m_1234 in
Azenhas) — the head is what Rick's AXIS classification sees that
Azenhas's HW polytope doesn't.

## 4.4. Impact on v4 §3 reference text (revised from Day-67)

| Item | Old (Day-62 / Day-64 era) | New (Day-68) |
|---|---|---|
| # AXIS formula | $f(n) = 3 - [n\text{ even}]$ | $\#\mathrm{AXIS}(n) = 3$ uniform |
| AXIS triple | varies with parity | $\{\mathrm{prefix}[1], \mathrm{prefix}[n], \mathrm{long}[1]\}$ uniform |
| Dim-gap parity link | $\Delta(n) = \#\mathrm{AXIS}(n)$ | $\Delta(n) \ne \#\mathrm{AXIS}(n)$ at even $n$; $\Delta$ is a separate AII-side identity |
| Source of parity | Cor 8 → AXIS collapse | Cor 8 → AII dim drop (only); AXIS is parity-independent |
| Head-vs-bulk split | (not in old narrative) | 1 (head, R-double / $\mathrm{adj}(\mathfrak{sl}_2)$) + 2 (bulk, Bucket-2 free-extrusion) |

## 4.5. Open questions raised

- **OQ-AXIS-N5** (Day-68 NEW): Construct $n = 5$ piece registry,
  verify $\#\mathrm{AXIS}(5) = 3$ and AXIS triple. (Day 68 CODE
  follow-up.)
- **OQ-RDOUBLE-EXTENDS** (Day-68 NEW): Does the R-double backbone
  recipe yield a BDI-feasible 3-piece family at all $n \ge 3$? The
  $\alpha \le 2$ cap — is it sharp at all $n$? (Theoretical analysis
  of $S \le P_2$ constraint.)
- **OQ-DIMGAP-RESIDUE** (Day-68 NEW): If $\#\mathrm{AXIS}$ no longer
  encodes the dim-gap parity, does some other Rick-side invariant
  encode it? Candidates: # walls in the bulk Bucket-2 (could it be
  3 - [n even]?), # AXIS-into-$M_2$ coordinates specifically (the
  C3 candidate from the PROVE trigger), dim of bulk fiber over a
  generic cone point.
- **OQ-AZENHAS-3RD-DIRECTION** (Day-68 NEW): The 3rd Azenhas free
  direction at $n = 3$ is $m_{1234}$; at $n = 4$ what is it? Test
  whether the 3rd Azenhas-free direction is *always* Rick-non-AXIS
  (= weight-0 bumped or analog), distinguishing the rep-theoretic
  Rick-AXIS slot from the Azenhas combinatorial-trivial slot.

# §5. Output artifacts

- This file: `proofs/2026-06-13-axis-conjecture-revision.md`
- Verification script: `code/2026-06-13-axis-n3-verify/n3_axis_verify.py`
- Results: `code/2026-06-13-axis-n3-verify/results.json`
- Collaborator note (to write): `memory/for-collaborator/2026-06-13-axis-conjecture-revision.md`
- Connection update (to write): `memory/connections/cross-programme-dim-gap-codim.md`
  addendum with revised # AXIS story.

— Rick, 2026-06-13 (Day 68 PROVE)
