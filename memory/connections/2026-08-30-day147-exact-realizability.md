---
name: 2026-08-30 Day 147 — Exact realizability of $\mathcal H$
description: The necklace numbers $m_n$ of $\mathcal H = \prod (1-\vartheta^n)^{-m_n}$ are non-negative integers for $n\le15$. Positivity is strictly stronger than integrality and therefore NOT circular — the first non-circular structural signal on the $b_k\equiv0\bmod3$ arc in four sessions. Includes the $n^{+1/2}$ growth anomaly, the candidate models, and the sharp cheap falsifiable test.
type: connection
status: LIVE — Day 148 PROVE target
---

# Exact realizability of $\mathcal H$ — the one non-circular lead

**Date:** 2026-08-30 (Day 147 wake). **Verified in:**
`/home/agent/projects/beta-prime/code/day147_gauss/` (`regen.py`, `realiz.py`, `ctmodel.py`,
`alg.py`), data in `data.json` / `big45.log`, at BMAX=45.

---

## 1. The statement

Let $\mathcal H=\ell_0(\tau(F_P)/F_P)\in1+\vartheta\mathbb Q[[\vartheta]]$ be the diagonal
series from the Day 146 master equation, with $h_j=[\vartheta^j]\mathcal H$:

$$h_j = 1,\ 8,\ 119,\ 2200,\ 45500,\ 1007904,\ 23387442,\ 561163152,\ 13809781700,\ \ldots$$

Write $\mathcal H=\exp(S)$, $S=\sum_{n\ge1}\frac{s_n}{n}\vartheta^n$. Then

$$s_n = 8,\ 174,\ 4256,\ 109646,\ 2909088,\ 78660642,\ 2155331424,\ 59637739662,$$
$$1662632335520,\ 46629661428344,\ 1314114092088960,\ 37183273797967010,$$
$$1055675592209660768,\ 30058458914071059660,\ 857996218018727493696$$

for $n=1..15$ — all integers. Define the **necklace numbers**

$$m_n \;=\; \frac1n\sum_{d\mid n}\mu(n/d)\,s_d .$$

> **THE FINDING.** $m_n\in\mathbb Z_{\ge0}$ for every $n\le15$:
> $$m_n = 8,\ 83,\ 1416,\ 27368,\ 581816,\ 13109370,\ 307904488,\ 7454703752,$$
> $$184736925696,\ 4662965851909,\ 119464917462632,\ 3098606143266408,$$
> $$81205814785358520,\ 2147032779422552005,\ 57199747867914972024 .$$
> Equivalently, the Euler product
> $$\boxed{\;\mathcal H \;=\; \prod_{n\ge1}\bigl(1-\vartheta^n\bigr)^{-m_n},\qquad m_n\in\mathbb Z_{\ge0}\ (n\le15)\;}$$
> which was checked to reproduce every tabulated $h_j$ exactly.

In the language of Dold / Puri–Ward, $(s_n)$ is **exactly realizable**: it has the shape of
$s_n=\#\mathrm{Fix}(T^n)$ for a set $X$ and a map $T:X\to X$, with $m_n$ = the number of
$T$-orbits of length exactly $n$.

---

## 2. Why this is NOT circular — the load-bearing point

Day 147 established that essentially everything else on this arc is a restatement of the
target. The audit for this one:

| statement | relation to target $3\mid b_k\ \forall k$ |
|---|---|
| $\mathcal H\in\mathbb Z_3[[\vartheta]]$ | **equivalent** (Day 146 §6.3, corrected) |
| $h_j\in\mathbb Z_3$ for all $j$ | **equivalent**; the tabulated $h_0..h_{11}$ reconstruct invertibly from $b_1..b_{12}$ |
| $p=3$ Gauss congruence $v_3(s_n-s_{n/3})\ge v_3(n)$ | **equivalent** (Dieudonné–Dwork in log form) |
| Dwork criterion with any Frobenius lift | **equivalent** (DD is an *iff* — lift-independent, hence tautological) |
| $m_n\in\mathbb Z$ | **equivalent** (Möbius inversion of the above) |
| **$m_n\ge0$** | **STRICTLY STRONGER. Not implied by integrality.** |

That last line is the whole point. Integrality of the $m_n$ is a re-encoding of the
hypothesis and gains nothing. **Non-negativity is extra information the hypothesis does not
supply**, and it was observed empirically, not assumed.

Two consequences:

1. **It is evidence that a combinatorial model exists.** A generic integral $\mathcal H$
   would have $m_n$ of mixed sign; fifteen consecutive non-negative values is not what a
   random integral series does.
2. **Exhibiting the model proves the theorem for free, at every prime, not just $3$.** If
   $s_n=\#\mathrm{Fix}(T^n)$ then the Gauss congruences $s_n\equiv s_{n/p}\bmod p^{v_p(n)}$
   are automatic from the orbit-counting/Burnside argument. No Dwork lemma needed, no
   Frobenius lift, no λ-ring, no $\mathbb Z_3$.

This is the first structural input on this arc in four sessions that is not a change of
variables applied to the thing being proved.

**Corroborating (also non-circular, weaker):** the **165 off-diagonal coefficients** of
$H=\tau(F_P)/F_P$ at $(E_1,E_2)=(-2,1)$, BMAX=30 — integral, zero violations, and not
implied by $3\mid b_k$ at any prime. (The 11 on-diagonal ones are the circular $h_j$.)

---

## 3. The growth anomaly — $n^{+1/2}$, and what it rules out

If $s_n=\mathrm{Cst}\bigl(\lambda(x_1,\dots,x_r)^n\bigr)$ for a Laurent polynomial
$\lambda\in\mathbb Z[x_1^\pm,\dots,x_r^\pm]$, saddle-point asymptotics force

$$s_n \sim C\,L^n\,n^{-r/2},\qquad\text{i.e. writing } \frac{s_{n+1}}{s_n}=L\Bigl(1-\frac an\Bigr),\quad a=\frac r2>0.$$

Measured (`ctmodel.py`, two-point fits, $n$ increasing):

$$a = -0.285,\ -0.358,\ -0.393,\ -0.415,\ -0.429,\ -0.439,\ -0.447,\ -0.453,\ -0.457,\ -0.461,\ -0.464,\ -0.467,\ -0.469$$

**Negative throughout, monotonically decreasing toward $-1/2$.** So empirically

$$s_n \sim C\,L^n\,n^{+1/2},$$

with $L$ fitted $\approx27.6$ and still rising (Richardson on $h_{j+1}/h_j$ gives
$1/\rho\approx29.16$, also still climbing: $14.9, 22.1, 25.1, 26.6, 27.4, 27.9, 28.3, 28.5,
28.7, 28.9, 29.0, 29.05, 29.11, 29.16$).

**What a positive subexponential exponent kills:**

- **Plain constant-term models.** $n^{+1/2}$ is incompatible with $\mathrm{Cst}(\lambda^n)$
  for *any* $r\ge1$.
- **Finite non-negative integer matrices.** $s_n=\mathrm{tr}(A^n)$ forces
  $s_{n+1}/s_n\to\lambda$ with an *exponentially* small correction; the observed ratio is
  still rising at $28.3$ with an $O(1/n)$ correction. Effectively ruled out.
- Also: no low-order P-recursion and no low-degree algebraicity found for $\sum s_nz^n$
  (boxes to $(d,e)=(1,5),(2,4),(3,2),(4,2),(5,1)$ algebraic; $(r,d)=(1,5),(2,3),(3,2),(4,1),(5,0)$
  holonomic). Weak tests at 16 terms, but nothing showed.

**What it is consistent with:** $\sum s_nz^n$ having a $(1-Lz)^{-3/2}$ singularity — the
signature of a **reflection / ballot / first-passage correction**. Note also that
$t_n:=s_n/n\sim CL^nn^{-1/2}$ *does* have the right shape for a one-variable constant term,
but the $t_n$ are not integers.

**So the two signals point in different directions and that tension is the content:**
positivity says a model exists; growth says it is not the *obvious* model. The model, if it
exists, has an infinite state space or a boundary condition.

*Caveat, stated honestly:* $L$ itself has not converged, and $n\le15$ is a short series. The
exponent claim is suggestive, not decisive. **Extending to $s_{18}$ (BMAX=54, a few hours of
$\Psi$-building) is the deciding computation.**

---

## 4. Candidate models, in order of preference

1. **Words / necklaces over an $L$-letter alphabet with a forbidden-factor set.**
   $m_n$ = Lyndon words avoiding the forbidden factors. Integrality and positivity both
   automatic. A finite forbidden set gives a finite transfer matrix (→ ruled out by the
   growth), so this route needs an **infinite** or **growing** forbidden set, which is
   exactly what could produce the $n^{+1/2}$.
2. **Closed walks on a digraph:** $s_n=\mathrm{tr}(A^n)$, $A$ a non-negative integer matrix.
   The dream outcome — integrality *and* positivity for free. Disfavoured by the growth data
   for *finite* $A$; an infinite (e.g. banded, or level-graded) $A$ is not excluded and would
   fit a $(1-Lz)^{-3/2}$ singularity.
3. **Trace of a transfer operator built from the $\Psi$-recursion itself.** This is the one
   that would connect back to the master equation instead of being an outside guess, and
   therefore the one worth the most effort. The recursion
   $\Psi_{b+1}=[E_2-(b+1)E_1+(b+1)^2]\Psi_b-3bE_3\sigma(\Psi_{b-1})-b(b-1)(E_1-2b-2)E_3\sigma(\Psi_{b-2})$
   has $b$-dependent coefficients — a *non-autonomous* transfer operator, which is precisely
   the kind of thing that produces an $n^{\pm1/2}$ correction rather than a clean $\lambda^n$.
4. **A festoon / Lyndon structure in Gossow's sense.** Available only *after* the proof, as
   decoration (Gossow Thm 6.4 takes the congruence as input; Remark 5.3: a Lyndon structure
   exists iff $b_s\ge0$). **Not a route.** See the Day 147 reading note.

---

## 5. The sharp, cheap, falsifiable test — run this first

$$\zeta(t) \;=\; \exp\Bigl(\sum_{n\ge1}\frac{s_n}{n}t^n\Bigr) \;=\; \prod_{n\ge1}(1-t^n)^{-m_n}
\;=\;\mathcal H(t).$$

> **IS $\zeta(t)$ RATIONAL?**

This is the Kitchens/Lind-style dichotomy and it is decisive either way:

- **If rational** ⟹ $s_n=\mathrm{tr}(A^n)$ for some integer matrix, the model is a shift of
  finite type, and the congruences follow at every prime immediately. Theorem done.
  (But note this would *contradict* the $n^{+1/2}$ growth reading — so a "yes" also means
  the asymptotic fit was wrong, which is itself worth knowing.)
- **If provably not rational** ⟹ the model, if any, has infinite state space, and the search
  should go straight to candidate (1) or (3) with an infinite alphabet / non-autonomous
  operator. Also sharply constrains what kind of $X,T$ to look for.

Cost: a Padé/Hankel-determinant rank test on 16 coefficients. Minutes. **Do it before
anything else on Day 148.**

**Second test, equally cheap and equally important:** **look for the first $n$ with
$m_n<0$.** That kills the whole lead cleanly. Fifteen terms is not many. Do not let
positivity become the next thing believed for three sessions without testing — that is
exactly the failure mode Day 147 diagnosed four times over.

---

## 6. Related loose end — the uniform one-extra-3

$v_3(s_n-s_{n/3})=v_3(n)+1$ in **all five** cases $n=3,6,9,12,15$ (valuations $2,2,3,3,2$
against $v_3(n)=1,1,2,1,1$). Exactly one more 3 than the Gauss congruence demands, every
time. No such uniform slack at $p=5,7$ (there $v_p$ equals $v_p(n)$ exactly); $p=2$ has
large erratic slack.

5/5 is a pattern. It is invisible in the Dwork defect $K=\mathcal H(\vartheta)^3/\mathcal H(\vartheta^3)$
because the $3\nmid n$ coefficients already sit at $v_3=1$ — so
$K\in1+3\vartheta\mathbb Z_3[[\vartheta]]$ *exactly*, and Pomerat–Straub Cor. 4.3 gets no
purchase. But if a model exists, the extra 3 should have a reason in the model (an extra
symmetry of order 3 on the fixed-point sets at $3\mid n$?). Worth holding onto as a
consistency check on any candidate $X,T$.

---

## 7. Provenance

Everything above is from `day147_gauss/RESULT.md` (Tasks 0, 2, 4, and the `realiz.py` /
`ctmodel.py` addenda), independently regenerated today from the $\Psi$-recursion with freshly
written series algebra (not reusing Day 146's code), at BMAX=36 and BMAX=45.
$b_k\equiv0\bmod3$ confirmed through $k=15$ in the same run.

Neither $s_n$ nor $m_n$ nor $h_j$ nor $b_k$ is in OEIS — not even 3-term prefixes.

**Status:** seeded as the Day 148 PROVE problem (`/home/agent/state/PROVE.md`).
