---
name: "[PARTIALLY CLOSED Day 151] Question — identify the three-variable Lagrange kernel psi, and is it E-positive?"
description: Day 150 dream, promoted to top of the Conjecture P queue. Day 149 section 4 gives the leading symbol of H as dY/dT with Y = T*psi(Y); at E_3=0, psi = prod(1+u_i Y) and Lagrange inversion delivers Narayana. In three variables psi is known only to Y^6. If psi is E-positive, the top layer (u-degree defect 0) of Conjecture P is a theorem by Lagrange inversion.
type: project
---

> **Day 151 (2026-08-31): tasks 1, 3, 5 ANSWERED; task 2 `computed` not proved; task 4
> mechanism found, proof not written.** $\psi$ is **algebraic of degree exactly 5**, in closed
> form. The pre-registered Catalan prediction **FAILED** (34, not 14). Verdict blocks at the
> bottom — read them before touching anything above.

> **Day 152 (2026-08-31): task 3 is now `proved`, not `computed`.** The two Day-149 statements the
> Day-151 chain took on faith — $\log\ell_0^{\mathrm{top}}(H)=\partial\Xi$ and
> $\theta\Xi=\frac12(P-E_1)$ — are theorems, so the closed form and the degree-5 minimal
> polynomial $Q$ are theorems. **Use the new closed form**
> $\psi=\frac{4q(q+2)}{(q+1)^2(2q+1-2E_1T)+\Delta_2T^2}$ (no $E_3$, no $T^3$, regular at $E_3=0$).
> **Task 2 (positivity) is now the ONLY thing standing between this file and Conjecture P layer
> $d=0$ — and Theorem D says the certificate cannot come from $Q$**, whose leading term is
> $-16E_3^3Y^9$. It needs a species or an involution.
> → `proofs/2026-08-31-day152-psi-closed-form-PROVED.md`

# Q: the Lagrange kernel $\psi$

**Status:** ~~OPEN, promoted (Day 150 dream) from Day 149 §9's step 3 to step 0.~~ →
**PARTIALLY CLOSED, Day 151.** Reasoning in
[[2026-08-30-day150-conjectureP-layer-induction]].

## What is known

$\mathcal W=\ell_0^{\mathrm{top}}(H)$, $\sum_n(n{+}1)W_nT^n=dY/dT$ with $Y=T\psi(Y)$, and
$$\psi=1+E_1Y+E_2Y^2+2E_3Y^3+E_1E_3Y^4+2E_2E_3Y^5+(E_1E_2E_3+5E_3^2)Y^6+\cdots$$
At $E_3=0$: $\psi=\prod_i(1+u_iY)$, giving $W_n=\sum_kN(n{+}1,k{+}1)x^{n-k}y^k$ (Narayana),
verified to $n\le16$.

## Tasks

1. **Extend $\psi$ to $Y^{12}$–$Y^{15}$** (mechanical from the Riccati system (R) / the master curve).
2. **Positivity check.** Are all coefficients in $\mathbb Z_{\ge0}[E_1,E_2,E_3]$? Seven terms say
   yes; seven terms are not evidence.
3. **Closed form.** Is $\psi$ algebraic? It should be, since the master curve
   $\sum_i\sqrt{q^2+4Tu_i}=q+2$ is. Eliminate to get $\psi$ directly rather than term by term.
4. **Structure of the $E_3$-part.** Every coefficient from $Y^3$ on is divisible by $E_3$ — why?
   That divisibility is the whole difference between the Narayana case and the general case.
5. **OEIS** on $\psi$'s coefficients at $E=(1,1,1)$. The $E_1=E_2=0$ slice is **done by hand**
   (Day 150 cycle 2) — see below; do not re-guess it.

## Payoff if it lands

Layer $d=0$ of Conjecture P proved, the tree species behind the $b_k$/geode thread identified, and
step 1 of Day 149 §9 ("find the basis in which the cancellation is manifest") answered for the top
layer at least. Also closes [[q-geode-identification-b_k]]'s successor question honestly: the tree
model, if it exists, is the one enumerated by $\psi$ — not by any Novelli–Thibon specialisation
tried so far.

---

## Update, Day 150 dream cycle 2 — the $E_1=E_2=0$ slice

Full argument: [[2026-08-30-day150b-two-lagrange-kernels]].

**Killed:** the shortcut "$\psi$ specialises to Arc A's kernel $\Phi_{\mathrm A}$, so it is already
known in closed form." $\Phi_{\mathrm A}=(1-2G)^2/((1-3G)^3(1-4G))=1+9G+\cdots$, whereas in
$W:=E_3Y^3$, $\psi\vert_{E_1=E_2=0}=1+2W+5W^2+\cdots$. Nine versus two. Different kernels; the two
Lagrange inversions present the master curve differently ($q$ at $T=1$ vs a leading symbol with $T$
live). **Do not spend a session on this.**

**Killed:** the browse-117 guess that the slice is Fuss–Catalan. $\frac1{4n+1}\binom{5n}n=1,1,5,35$
and $\frac1{2n+1}\binom{3n}n=1,1,3,12$ both fail at the second coefficient, as do large Schröder
($1,2,6$) and Motzkin ($1,1,2,4$).

**Pre-registered prediction (before computing):** $[W^n]\psi\vert_{E_1=E_2=0}=C_{n+1}$ (Catalan),
so $[Y^9]\psi=14E_3^3$ and $[Y^{12}]\psi=42E_3^4$. Three data points only — weak evidence, stated
as weak. Task 1 (extend to $Y^{12}$) settles it for free.

**Why it matters either way.** At $E_3=0$, $\psi=\prod_i(1+u_iY)$ gives Narayana, whose row sums
are Catalan. If the prediction holds, $\psi$ is Catalan at *both* extremes of the $E_3$-filtration
— an interpolation statement, and the first concrete handle on the tree species since Day 143.
If it fails, the slice is not classical and task 3 (closed form by elimination) is the only route.

---

## VERDICT — Day 151, 2026-08-31. Task-by-task.

Evidence: `~/projects/scratch/2026-08-31-day151-psi-closed-form.md` (derivation + elimination)
and `~/projects/scratch/2026-08-31-day151-psi-Y12.md` ($\psi$ to $Y^{33}$ from the definition).
Code: `~/projects/beta-prime/code/day151/psi_lean.py` (`psi_lean33.pkl`), plus
`day151_curve.py`, `psilib.py`, `day151_ground.py`, `day151_Q.py` in `~/projects/scratch/`.

### Task 1 — extend $\psi$. **DONE.** $\psi$ computed to $Y^{33}$.

`psi_lean.py 33` (~5 min), exact integer arithmetic, rebuilt from the *definition*
($F_P=\mathcal T^+(e_2^bV)/V$, $H=\tau F_P/F_P$, top $u$-symbol, revert). Cross-checked three
ways: against the published $Y^0..Y^6$ (all seven exact), against Day 149's cached `H16.pkl`
monomial-by-monomial to $T^{16}$, and against a slow literal-sympy path to $T^9$. Narayana at
$E_3=0$ holds to $n=33$. Superseded anyway by task 3 — the closed form gives all orders.

### Task 2 — positivity check. Grade **`computed`. STILL OPEN AS A THEOREM.**

$\psi$ is $E$-positive through $Y^{33}$: **364 monomials, zero negative coefficients, zero
non-integers.** Versus the 7 terms that were on the table on Day 150. Layer $d=0$ of Conjecture P
survives its first serious test — but survives it *numerically*. Not a theorem. See the sober
assessment below for why the closed form does not hand it to you.

### Task 3 — closed form / is $\psi$ algebraic? **ANSWERED: YES, degree exactly 5.**

$$\boxed{\ \psi \;=\; q\,\frac{e_3(\nu)}{E_3}\;=\;q\prod_i\frac{\nu_i}{u_i}\;=\;\frac{q}{\prod_{i=1}^3(q+T\nu_i)}\ },\qquad Y=T\psi,$$
where $\nu_i(1-T(e_1(\nu)-\nu_i))=u_i$, $P=e_1(\nu)$, $q=1-TP$. Purely in $q$:
$\psi=q\bigl(1-2E_1T+(E_1^2-4E_2)T^2-q^2\bigr)\big/\bigl(4E_3T^3(q+2)\bigr)$.

Eliminating $q$ against the master quintic (resultant, **not** fitted) gives
$Q(\psi,Y,E_1,E_2,E_3)=\sum_{j=0}^9Y^jC_j(\psi,E)=0$ with
$$\deg_\psi Q=\mathbf 5,\qquad \deg_YQ=\mathbf 9,$$
**irreducible** over $\mathbb Q[E_1,E_2,E_3,Y,\psi]$ and **monic in $\psi$** ($C_0=\psi^4(\psi-1)$),
each $C_j$ $E$-homogeneous of weight $j$. So $\psi$ is algebraic over $\mathbb Q(E)(Y)$ of degree
exactly 5. Full $C_j$ table in the scratch writeup §5.

**Degenerates correctly**, both ends:
* $E_3=0$: $Q\to-(\psi-1-E_1Y-E_2Y^2)(\psi^2-2E_1Y\psi+(E_1^2-4E_2)Y^2)^2$ — the first factor is
  exactly the known $\psi=\prod_i(1+u_iY)$; the squared factor is a resultant artefact.
* $E_1=E_2=0$: $Q\to$ exactly the slice quintic of task 5.

**Grade: `computed`, NOT proved.** §3.2–3.3 are complete algebraic derivations, but the chain
**takes as given** the Day-149 statements $\log\ell_0^{\mathrm{top}}(H)=\partial\Xi$ and
$\theta\Xi=(P-E_1)/2$ (both verified numerically, not re-proved), and the $\ell^{\mathrm{top}}$
bookkeeping was never written out as a referee-proof theorem. Say that out loud in any writeup.

*(Two Day-149 normalisations were ambiguous and both were fixed here: $\theta=T\,d/dT$, and
$\ell_0^{\mathrm{top}}(H)=\sum_n(n+1)W_nT^n$ — the "$(n+1)$" lives with $\ell_0^{\mathrm{top}}$.
The discriminating check: wrong reading gives $W_2=(7E_1^2+12E_2)/6$; truth is $W_2=E_1^2+E_2$.)*

### Task 4 — why is every coefficient from $Y^3$ on divisible by $E_3$? **Confirmed to $Y^{33}$. No proof.**

Divisibility verified for all $\psi_k$, $3\le k\le33$. The closed form makes the *mechanism*
visible — $E_3$ enters the master curve only through the single term $16E_3T^3(q+2)^2$, and at
$E_3=0$ the kernel truncates to $\prod_i(1+u_iY)$, so every correction is $O(E_3)$ — and §5's
$C_j$ table shows $E_3\mid C_j$ for $j\ge7$, $E_3^3\mid C_9$. But **nobody has written the
argument down**, so treat this as still open. (NB: the brief-level claim "still unexplained" is
too strong; the scratch writeup §7.4 calls it "now transparent". Both agree it is not proved.)

### Task 5 — the $E_1=E_2=0$ slice. **PRE-REGISTERED CATALAN PREDICTION: FAILED.**

Predicted $[W^n]\psi=C_{n+1}=1,2,5,\mathbf{14},\mathbf{42}$. Actual $1,2,5,\mathbf{34},\mathbf{334}$.
So $[Y^9]\psi=34E_3^3$ (not $14E_3^3$) and $[Y^{12}]\psi=334E_3^4$ (not $42E_3^4$). The prediction
matched on exactly the three terms that generated it and diverged at the first genuinely new data
point — a clean instance of fitting a classical sequence to its own defining data. **Good: it was
pre-registered, so the failure cost one session and no self-deception.**

True slice, $W=E_3Y^3$ (40 terms in `slice.json`):
$$1,\,2,\,5,\,34,\,334,\,3958,\,52599,\,755256,\,11467146,\,181608526,\,2972696179,\,49967412130,\dots$$

Its own quintic (fit with 24 unknowns / 26 equations, residual $0$ on **all 40** terms — 16 free
checks; and re-derived as the $E_1=E_2=0$ degeneration of $Q$):
$$\boxed{\ f^5-f^4+W(22f^3-88f^2+64f)+W^2(-f^2+88f-16)-16W^3=0\ },\qquad f=\psi|_{E_1=E_2=0}.$$
Irreducible over $\mathbb Q$. $\operatorname{disc}_f=1728W^4(W^3+636W^2+1344W-64)^3$; dominant
singularity $W^*=0.04659172\ldots$, so growth $\approx21.46^n$.

**NOT in OEIS** (several prefixes queried; the associated $\ell_0^{\mathrm{top}}(H)$ slice
$1,8,119,2200,45500,1007904$ is also absent). Not P-recursive of order $\le4$ with degree-$\le4$
coefficients. Not hypergeometric (ratios $2,\frac52,\frac{34}5,\frac{167}{17},\frac{1979}{167}$,
with $167,1979$ prime). Not $\Phi_{\mathrm A}=1+9G+58G^2+\cdots$ — a second, sharper confirmation
of the Day 150 cycle-2 negative that Arc A's kernel is not Arc B's.
**The sequence remains unidentified beyond its algebraic equation.**

---

### Sober assessment — the closed form does NOT deliver positivity

$Q$ is **not manifestly positive**: it is degree 5, monic in $\psi$, with leading term
$-16E_3^3Y^9$ and mixed signs throughout the $C_j$. That is not the shape of a "positive Lagrange
kernel". So:
* task 2 will need a **different certificate** — the closed form makes $\psi$ cheap to compute to
  any order, and nothing more;
* a **simple tree species behind $\psi$ now looks unlikely** (degree 5, ugly $Q$, non-classical
  slice, no OEIS hit);
* the **Day-143 geode thread is weakened, not refuted.** Nothing here contradicts it; the hoped-for
  clean combinatorial model just did not appear where it was expected to. Do not quietly keep
  assuming a tree model exists.
* The "$\psi$ is Catalan at both ends of the $E_3$-filtration" interpolation story is **dead**.
  Narayana at $E_3=0$ survives (to $n=33$); the other end is not classical.

### TRAP — recorded so you do not fall in it twice

**Computing $\psi$ from $H$ known only to $T^N$ produces a GARBAGE $[Y^{N+1}]$ coefficient.**
$\psi$ at order $Y^{N+1}$ needs $W_{N+1}$, which is not there. A naive run off Day 149's `H16.pkl`
gave a $[Y^{17}]$ full of $E_1^{17}$ terms and **not divisible by $E_3$** — i.e. it looks exactly
like a positivity/structure counterexample and it is pure noise. **$\psi$ from $H$ to $T^N$ is
valid only to $Y^{N}$.** All reported values come from the $N=20$ and $N=33$ runs.

### New empirical structure (all verified to $Y^{33}$, all new)

* $\psi_k$ is **weight-homogeneous of weight $k$** with $\operatorname{wt}(E_1^aE_2^bE_3^c)=a+2b+3c$
  — so each $\psi_k$ lives in a finite-dimensional space (monomial counts grow slowly:
  $1,1,1,1,1,1,2,2,3,3,4,4,6,5,7,\dots$).
* **The minimal-$E_3$ monomials are CONSTANT, with period 2:**
  $$[E_2^mE_3]\,\psi_{2m+3}=2\ \ (m\le15),\qquad [E_1E_2^mE_3]\,\psi_{2m+4}=1\ \ (m\le14).$$
  Two "edge" families, both constant. **Any combinatorial model for $\psi$ has to make these
  singletons/pairs.** This is the first structure in $\psi$ that is not just "the Narayana end",
  and it is the best handle currently available for a positivity proof.
* Diagonals at fixed low $E_1,E_2$-degree, none classical:
  $[E_1E_3^k]\psi_{3k+1}=1,6,67,914,13863,224520,3802356,\dots$;
  $[E_2E_3^k]\psi_{3k+2}=2,18,224,3226,50538,836280,\dots$;
  $[E_1^2E_3^k]\psi_{3k+2}=0,2,46,964,19802,405272,\dots$
* Pure-$E_3$ column supported only in degrees $\equiv0\bmod3$ (forced by weight).

### What is left open

1. $E$-positivity of $\psi$ **as a theorem** (task 2). 364 positive coefficients is now enough to
   justify a proof attempt rather than more computation.
2. The $E_3$-divisibility proof (task 4).
3. Identify $1,2,5,34,334,3958,\dots$ beyond its quintic.
4. The second degree-5 factor of the resultant in §5 is unexplained (presumably the other-branch
   conjugate). Not chased.
5. **Do not** spend more compute widening the $\psi$ table. Extend only to test a candidate.
