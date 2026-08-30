# Day 147 — "diagonal descent" Dieudonné–Dwork test on $\mathcal H$

**Directory:** `/home/agent/projects/beta-prime/code/day147_diagonal/`
**Date:** 2026-08-30.  Reads (never modifies) `../day146_prove/`.

---

## VERDICT UP FRONT (Task 3)

**The descent test $D(\vartheta) := \mathcal H(\vartheta)^3/\mathcal H(\vartheta^3) \in 1+3\vartheta\mathbb Z_3[[\vartheta]]$ is VACUOUS.**

It is not "weak evidence"; it is a **theorem** about *any* power series with 3-integral
coefficients and unit constant term. It cannot fail on data we have already verified to be
integral, and therefore it carries exactly zero information about $b_k\equiv 0\ (3)$.

> **Proposition.** Let $f=\sum_{j\ge0} f_j\vartheta^j$ with $f_j\in\mathbb Z_p$ and
> $f_0\in\mathbb Z_p^\times$. Then $f(\vartheta)^p/f(\vartheta^p)\in \mathbb Z_p[[\vartheta]]$
> and is $\equiv 1 \pmod p$ (when $f_0=1$).
>
> *Proof.* In $\mathbb F_p[[\vartheta]]$, $\bar f(\vartheta)^p=\sum \bar f_j^{\,p}\vartheta^{pj}
> =\sum \bar f_j\vartheta^{pj}=\bar f(\vartheta^p)$, using Frobenius additivity and Fermat
> $\bar f_j^{\,p}=\bar f_j$ in $\mathbb F_p$. Since $f_0$ is a unit, $f(\vartheta^p)$ is
> invertible in $\mathbb Z_p[[\vartheta]]$; divide. $\square$

Moreover $[\vartheta^n]D$ is a polynomial in $h_0,\dots,h_n$ only. Hence:

$$h_0,\dots,h_N \in\mathbb Z_3 \;\Longrightarrow\; v_3\big([\vartheta^n](D-1)\big)\ge 1
\quad\text{for all } n\le N .$$

We already **know** $h_0,\dots,h_{12}\in\mathbb Z$ (they are the integers in `data.json`,
regenerated below). So the pass at $n\le 12$ was logically forced before any computation ran.

**Empirical confirmation of vacuity** (`vacuity.py`):
* 200 random integer sequences with $f_0=1$: **200/200 pass**, min $v_3$ over all degrees $=1$.
* Controlled failures: replacing $h_j\mapsto h_j/3$ for a $j$ with $v_3(h_j)=0$ makes the test
  fail **exactly at degree $n=j$** (tested $j=1,2,4,8$). So the test is not merely implied by
  the direct check $v_3(h_j)\ge 0$ — it is **degree-by-degree equivalent to it**, at strictly
  higher computational cost.

### What this means for the reduction chain

Nothing is refuted. Day 146's reduction is fine; today's test simply cannot probe it.
The Dieudonné–Dwork lemma is an *equivalence*, so plugging in already-integral data and
observing the equivalent condition hold is a tautology, not a check.

### The only non-circular use of Dieudonné–Dwork here

DD becomes a **proof tool** only if the congruence
$$\mathcal H(\vartheta)^3 \equiv \mathcal H(\vartheta^3) \pmod 3$$
is established from a source **independent of integrality** — e.g. a Frobenius lift on
$\mathbb Z[E_1,E_2,E_3]$, a functional equation for $\mathcal H=\mathrm{diag}(\tau(F_P)/F_P)$,
or a $\delta$-ring structure. Then DD *outputs* integrality. Numerically evaluating the
congruence on computed coefficients is precisely the circular move.

**Contrast with Day 146's own Dwork test (`day146_prove/dwork.py`):** there
$K=F_P(T)^3/\sigma(F_P)(T^3)$ with $F_P$ **not** integral (it carries $1/b!$), so
$\tau(K)/K\in 1+3T\mathbb Z_3[E][[T]]$ is **not** automatic — and indeed Day 146 recorded a
genuine numerical FAILURE when the $E_3\mapsto E_3^3$ twist was dropped. **That** test can
fail, hence carries information. `day146_prove/dwork2.py` ($H(T)^3/H(T^3)$), by contrast, is
vacuous for exactly the same reason as today's test, since $H$ is integral in the tested range.

---

## Task 0 — regeneration of $h_j$

`gen.py` (a parametrised copy of `day146_prove/bigdata.py`, using the same `core.py`
$\Psi$-recursion) at `BMAX=36`, runtime **91.9 s** (91.6 s of which is `build_P`):

```
h_j (j=0..12) = 1, 8, 119, 2200, 45500, 1007904, 23387442, 561163152,
                13809781700, 346645093984, 8840919351575, 228449188011224,
                5968029850876084
b_k (k=1..12) = 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739,
                50751637140, 1276862920140, 32626363346505, 844375375808301
H integral up to T^36: YES     H order >= 0: YES
```

**All 13 values of $h_j$ and all 12 values of $b_k$ match Rick's list exactly.** CONFIRMED.

<<EXTENSION>>

### Independent cross-check of the MAIN IDENTITY (`relation.py`)

Solving $F^2-F=\vartheta\,\mathcal H\,(2F-3)$ for $F$ order-by-order from the $h_j$ alone
(with $F(0)=0$) reproduces $f_k=b_k$ for $k=1..12$ **exactly**. So

$$F(\vartheta)=\sum_{k\ge1} b_k\vartheta^k,\qquad
\boxed{\ \mathcal H=\frac{F(1-F)}{\vartheta\,(3-2F)}\ }$$

This makes the Day 146 equivalence a two-line consequence (worth recording):
$3-2F$ has constant term $3$, i.e. is **not** a unit in $\mathbb Z_3[[\vartheta]]$.
Write $F=3G$: then $\mathcal H=G(1-3G)/(\vartheta(1-2G))$, and $1-2G$ *is* a unit.
So $G\in\mathbb Z_3[[\vartheta]]$ (i.e. $3\mid b_k$) $\Rightarrow \mathcal H\in\mathbb Z_3[[\vartheta]]$.
Conversely, from $F(1-F)=\vartheta\mathcal H(3-2F)$ reduced mod 3,
$F\big(1-F-\vartheta\mathcal H\big)\equiv 0$, and the second factor has constant term 1, hence
$F\equiv0$. $\square$

**Caution for Rick:** this shows the passage $b_k\Rightarrow\mathcal H$ is a *change of
variables through a unit*, not a strengthening. The only reason $\mathcal H$ is worth studying
is that it has an **independent** definition, $\mathcal H=\mathrm{diag}(\tau(F_P)/F_P)$.
Any argument that goes back through the main identity is circular by construction
(this matches the Day 146 dream note "main-identity route provably circular").

---

## Tasks 1 & 2 — the $v_3$ tables (`descent.py`)

$D=\mathcal H(\vartheta)^3/\mathcal H(\vartheta^3)$ computed over $\mathbb Q$ with
`fractions.Fraction`; all coefficients came out **integral** (as expected, $h_0=1$).

| $n$ | $[\vartheta^n]D$ | $v_3$ |
|---|---|---|
| 0 | 1 | 0 |
| 1 | 24 | **1** |
| 2 | 549 | 2 |
| 3 | 12816 | 2 |
| 4 | 307239 | **1** |
| 5 | 7536384 | 2 |
| 6 | 188433630 | 2 |
| 7 | 4786905528 | 2 |
| 8 | 123231729393 | 2 |
| 9 | 3208229566056 | 2 |
| 10 | 84327653306850 | **1** |
| 11 | 2234924281186344 | 4 |
| 12 | 59659268779516860 | 2 |

$v_3$ for $n=1..12$: `1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 4, 2`. **All $\ge 1$: the test PASSES.**

**Slack (Task 2).** Three coefficients ($n=1,4,10$) sit at $v_3$ exactly 1, so the test is
"tight" in the naive sense — but this tightness is *also* uninformative: it merely measures the
size of the freshman's-dream error term $\big(\mathcal H^3-\mathcal H(\vartheta^3)\big)/3$,
which has no reason to be further divisible. A "vacuous but tight" test is still vacuous.

**$v_3(h_j)$, $j=0..12$:** `0,0,0,0,0,1,1,1,0,0,0,0,0`.
Only $j=5,6,7$ are divisible by 3, each exactly once; no $j=9$ or higher hits. There is **no**
visible 3-divisibility pattern — $\mathcal H$ is a 3-adic *unit* series with a sporadic run of
three 3-divisible coefficients. (Compare $v_3(b_k)=1,3,1,1,2,3,2,2,1,1,2,1$: also patternless
beyond $\ge1$.)

---

## Task 4 — is $\mathcal H$ a known / holonomic sequence? (`prec.py`, `algfit.py`)

**P-recursion search.** Solved $\sum_{i=0}^{R}p_i(j)\,h_{j+i}=0$, $\deg p_i\le D$, exactly over
$\mathbb Q$, reporting *only* genuinely overdetermined systems (equations $\ge$ unknowns $+3$):

| $R$ | $D$ tested (overdetermined) | nullity |
|---|---|---|
| 1 | 0,1,2,3 | 0 |
| 2 | 0,1 | 0 |
| 3 | 0 | 0 |
| 4 | 0 | 0 |

**Result: none found.** Same for $b_k$. With only 13 (resp. 12) terms the higher $(R,D)$ cells
are underdetermined and were honestly *not tested* — Day 146's `search.py` silently skipped
them too, so "no P-recurrence order $\le4$ deg $\le4$" was and remains **partially unverified**;
what is genuinely ruled out is the low-complexity corner above.

**Algebraic-equation fit.** $\sum_{a\le A,b\le B}c_{ab}\vartheta^a S(\vartheta)^b=0$ for
$S=F$ and $S=\mathcal H$: nullity 0 in every overdetermined cell ($(A,B)$ with
$(A+1)(B+1)\le 10$). So neither $F$ nor $\mathcal H$ is algebraic of very low bidegree.
This is consistent with, but does not prove, transcendence.

**OEIS.** No internet access in this container; `1, 8, 119, 2200, 45500, 1007904, 23387442`
should be searched by hand. It is *not* in any of the local data. (Day 144 already recorded
that $b_k$ is not in OEIS.)

**Growth.** $r_j=h_{j+1}/h_j$ = 8, 14.875, 18.487, 20.682, 22.152, 23.204, 23.994, 24.609,
25.101, 25.504, 25.840, 26.124. Monotonically increasing, and

* $\log_{27}(h_j/h_{j-1})$ = 0.631, 0.819, 0.885, 0.919, 0.940, 0.954, 0.964, 0.972, 0.978,
  0.983, 0.987, 0.990 — creeping to 1.
* $27-r_j$ = 19.0, 12.1, 8.51, 6.32, 4.85, 3.80, 3.01, 2.39, 1.90, 1.50, 1.16, 0.876;
  successive ratios 0.64…0.755 (slowly rising).

So the data are consistent with $r_j\to \mathbf{27}=3^3$, i.e. $h_j\sim C\cdot 27^j\cdot(\text{sub-exponential})$
— a pleasing constant given $\vartheta=E_3T^3$. But it is **not** a clean $C\cdot r^j$: the
correction $27-r_j$ decays roughly geometrically rather than like $c/j$
($j(27-r_j)$ rises to $\approx19.4$ at $j=4$ then falls to $9.6$, so no $j^{a}$ power law fits),
and $h_j/27^j$ = 1, .296, .163, .112, .0856, …, .0398 is still visibly decreasing at $j=12$
with no established positive limit. **More terms are needed before any asymptotic claim.**

---

## Files

| file | purpose |
|---|---|
| `core.py` | copy of Day 146 $\mathbb Z[E_1,E_2,E_3]$ arithmetic / $\Psi$ recursion (unmodified) |
| `gen.py` | parametrised regeneration of $b_k$, $h_j$ (`python3 gen.py BMAX`) |
| `descent.py` | Task 1/2: $D=\mathcal H^3/\mathcal H(\vartheta^3)$ and $v_3$ tables |
| `vacuity.py` | Task 3: random-integer-sequence + controlled-failure demonstration |
| `relation.py` | recovers $F=\sum b_k\vartheta^k$ from the main identity + $h_j$ |
| `prec.py` | P-recursion scan + growth analysis |
| `algfit.py` | algebraic-equation fit for $F$ and $\mathcal H$ |
| `data_36.json`, `data_51.json` | regenerated data |
