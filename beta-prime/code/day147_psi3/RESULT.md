# Day 147 — Adams $\psi^3$ as the Frobenius lift in the Dwork reformulation

**Verdict: the $\lambda$-ring hypothesis does not deliver. $\psi^3$ is a perfectly
good Frobenius lift, but it is neither better nor worse than the naive $E_i\mapsto E_i^3$.
Two errors in the Day 146 framing were found and corrected, and one clean new
negative theorem was proved.**

---

## 0. Two corrections to the premises

### 0.1 $\tau$ is NOT "$E_1\mapsto E_1,\ E_2\mapsto E_2,\ E_3\mapsto E_3+\varphi_1$"

The $\tau$ actually implemented and used in Day 146 (`verify_master.py`, `core.py`) is

$$\tau(E_1)=E_1+3,\qquad \tau(E_2)=E_2+2E_1+3,\qquad \tau(E_3)=E_3+E_1+E_2+1 .$$

**This is exactly the substitution $u_i \mapsto u_i+1$ on the three roots** (verified
symbolically: $e_i(u+1)$ equals the three images above). So the answer to the brief's
"INTERPRETATION WARNING" is: **yes, $\tau$ comes from a $u$-substitution** — it is the
unit translation $u\mapsto u+1$, an automorphism of $\mathrm{Sym}_3$.

The brief's version only records the $E_3$-part; the $E_1,E_2$ part is hidden in Day 146's
"move to the shifted base point $(E_1+3,\,E_2+2E_1+3)$" (`general_pt.py`). The genuine
$\tau$ is the translation. All computations below use the genuine $\tau$.

### 0.2 The Dwork test needs $\varsigma\circ\tau$, not $\tau\circ\varsigma$

Dieudonné–Dwork applied to $H=\tau(F_P)/F_P$ requires
$$H(T)^3/\varsigma(H)(T^3),\qquad \varsigma(H)=\frac{\varsigma(\tau F_P)}{\varsigma(F_P)},$$
i.e. the numerator uses $(\varsigma\circ\tau)(F_P)$. So the correct object is
$$\boxed{\;\mathcal D \;:=\; \frac{K(\tau F_P)}{K(F_P)},\qquad K(G)=\frac{G(T)^3}{\varsigma(G)(T^3)}\;}$$
and this equals the literal $\tau(K)/K$ **only if $\tau\varsigma=\varsigma\tau$**.
Day 146's write-up states it as $\tau(K)/K$ and justifies the identification by
"$\varsigma$ and $\tau$ commute on the locus $\varphi_1=0$". Both orders were computed.

---

## 1. Task 1 — $\psi^3$ explicitly

With $E_i=e_i(u_1,u_2,u_3)$ and $\psi^3: u_i\mapsto u_i^3$ (verified by back-substitution):

$$\psi^3(E_1)=E_1^3-3E_1E_2+3E_3 \;=\; p_3 \qquad\text{(confirms the brief)}$$
$$\psi^3(E_2)=E_2^3-3E_1E_2E_3+3E_3^2$$
$$\psi^3(E_3)=E_3^3 \qquad\text{(agrees with the naive lift)}$$

Frobenius check: $\psi^3(E_i)-E_i^3 \in 3\,\mathbb Z[E]$ for all $i$ (differences
$-3E_1E_2+3E_3$, $-3E_1E_2E_3+3E_3^2$, $0$). So $\psi^3$ is a genuine Frobenius lift. ✓

Script: `task12_psi3.py`.

---

## 2. Task 2 — $\tau$-commutation: the mod-3 test is VACUOUS

**Both lifts commute with $\tau$ mod 3, for both versions of $\tau$. All six defects
$\tau\varsigma(E_i)-\varsigma\tau(E_i)$ are $\equiv 0 \bmod 3$.**

Rick's claim that "the naive lift only commutes with $\tau$ mod 3 on $\varphi_1=0$" is
**false**, and the reason is a one-line triviality:

> If $\varsigma$ is any Frobenius lift and $\tau$ any ring endomorphism of a
> $\mathbb Z_3$-algebra $R$, then for all $x$:
> $\tau\varsigma(x)\equiv\tau(x^3)=\tau(x)^3\equiv\varsigma\tau(x) \pmod 3$.

So mod-3 commutation carries **zero information** and cannot discriminate between lifts.
(The $u$-level statement $(u+1)^3\equiv u^3+1$ is a special case of the same triviality.)

Explicit defects (over $\mathbb Z$), genuine $\tau$ (`task12_psi3.py`):

| | $E_1$ | $E_2$ | $E_3$ |
|---|---|---|---|
| $\psi^3$ | $3E_1^2+3E_1-6E_2$ | $3E_1^2E_2-6E_1^2E_3+6E_1^2+3E_1E_2^2+9E_1E_2-21E_1E_3+6E_1+3E_2^2-3E_2E_3-3E_2-27E_3$ | $3E_1^2E_2+3E_1^2E_3+3E_1^2+3E_1E_2^2+9E_1E_2E_3+9E_1E_2+3E_1E_3^2+6E_1E_3+3E_1+3E_2^2E_3+3E_2^2+3E_2E_3^2+6E_2E_3+3E_2$ |
| naive $E_i^3$ | $9E_1^2+27E_1+24$ | $6E_1^3+12E_1^2E_2+36E_1^2+6E_1E_2^2+36E_1E_2+54E_1+9E_2^2+27E_2+24$ | (same shape, $\varphi_1$-remainder $E_2^2+E_2$) |

At the $\delta$-ring level (defect$/3$ mod 3, `task2b_mod9.py`) **neither** lift commutes:
both have nonzero defect, and neither defect vanishes on $\varphi_1=0$. So $\psi^3$ has no
advantage there either.

### 2b. NEW THEOREM (negative, clean)

> **No Frobenius lift of $\mathbb Z_3[E_1,E_2,E_3]$ commutes with $\tau$ exactly.**

*Proof.* $\varsigma\tau=\tau\varsigma$ on $E_1$ forces $f_1:=\varsigma(E_1)$ to satisfy
$f_1\circ\tau=f_1+3$. A particular solution is $f_1=E_1$; the homogeneous solutions are the
$\tau$-invariants, i.e. (translation invariants of a monic cubic) $\mathbb Q[q_2,q_3]$ with
$q_2=E_1^2-3E_2$, $q_3=2E_1^3-9E_1E_2+27E_3$. Grade by $\mathrm{wt}(E_i)=i$: $q_2,q_3$ are
weighted-homogeneous of weights $2,3$, so $\mathbb Q[q_2,q_3]$ has zero weight-$1$ part and
no element of it contains the monomial $E_1$. Hence every solution has
$[E_1]f_1=1$, so $f_1-E_1^3$ has $E_1$-coefficient $1\not\equiv 0 \bmod 3$. $\square$

Verified by brute-force linear solve for all weighted degrees $\le 15$ (`no_commute_thm.py`).

**Consequence:** the slogan "the $\tau$-variation of the Frobenius defect of $F_P$" cannot be
made literally correct. One must always use $K(\tau F_P)/K(F_P)$.

---

## 3. Task 3 — the Dwork defect, recomputed

### Method
All lift/`τ` substitutions are computed **symbolically in $\mathbb Z[E_1,E_2,E_3]$ first**
(sympy), and only then specialised at $E_1=a$, $E_2=b$ with $E_3=x$ kept as a polynomial
variable. So the "specialise-before-lift" error the brief warns about is avoided.
A fully symbolic run (all three $E_i$ free) was also done. Framework: `dwork_gen.py`.

Four lifts were compared:
* **`psi`** $=\psi^3$ (canonical $\lambda$-ring lift)
* **`naive`** $\varsigma(E_i)=E_i^3$ (a genuine Frobenius lift of the full ring)
* **`E3only`** $E_1\mapsto E_1,E_2\mapsto E_2,E_3\mapsto E_3^3$ — **what Day 146 actually
  computed**: it is the canonical lift of $\mathbb Z_3[E_3]$ *after* specialising $E_1,E_2$
  to $\mathbb Z_3$-constants (Frobenius on $\mathbb Z_3$ is the identity, so constants must be
  fixed). Not a Frobenius lift of the full ring.
* **`ident`** no twist at all — `day146_prove/dwork.py`. Not a Frobenius lift.

### Sanity: the framework reproduces Day 146 exactly
`ident` fails at $T^9$ (matches `dwork.py`); `E3only` passes; $H$'s coefficients
$1,2,6,(24,8),(120,90),\dots$ and $h_j=1,8,119,\dots$ reproduce `Hdiag.py`. (`sanity.py`)

### Result A — specialised base points, $N=30$ (`deep.py`, `main2.py`)

Correct order ($\varsigma\circ\tau$), points $(E_1,E_2)\in\{(-2,1),(0,0),(1,1),(2,-1),(0,1),(3,3),(-1,-1)\}$
(i.e. $\varphi_1=0,1,3,2,2,7,-1$):

| lift | PASS at all 7 points? | reached | min $v_3$ over $T^{\ge1}$ |
|---|---|---|---|
| `psi` | **YES** | $T^{30}$ | 1 |
| `naive` | **YES** | $T^{30}$ | 1 |
| `E3only` | **YES** | $T^{30}$ | 1 |
| `ident` | NO — fails at $T^9$ everywhere | — | 0 |

The per-$T$-degree minimum-$v_3$ rows for `psi`, `naive`, `E3only` are **identical** at
$(-2,1)$ and $(1,1)$ (all $=1$) and differ at $(0,0)$ in exactly one place ($n=9$: `psi` gives
2, the others 1).

Literal $\tau(K)/K$ (wrong order, $\tau\circ\varsigma$), $N=21$, same 7 points:
`psi` passes at 2/7, `naive` at 0/7, `E3only` at 4/7, `ident` at 0/7 — all failures at $T^9$.
This is the *only* place where $\psi^3$ beats the naive lift, and it is an artefact of the
wrong composition order (cf. §2b: neither commutes, so this quantity is not the Dwork defect).

### Result B — fully symbolic in $\mathbb Z[E_1,E_2,E_3]$, $N=15$ (`symbolic.py`)

| lift | criterion $\mathcal D\in 1+3T\,\mathbb Z_3[E][[T]]$ |
|---|---|
| $\psi^3$ | **PASS** to $T^{15}$ |
| naive $E_i^3$ | **PASS** to $T^{15}$ |
| `E3only` | **FAIL** at $T^3,T^6,T^9,T^{12},T^{15}$ (e.g. $[E_1T^3]\mathcal D=2290$, $[E_1^3T^3]\mathcal D=56$) |

This is the one honest structural gain of today: **Day 146's Dwork verification was a
fibrewise statement over $\mathbb Z_3$ (constants $E_1,E_2$), not a statement over
$\mathbb Z_3[E_1,E_2,E_3]$.** The `E3only` twist is *not* a Frobenius lift of the full ring and
genuinely fails there. Both $\psi^3$ and $E_i^3$ fix this.

$v_3$ histograms of all $\mathcal D$-coefficients, $T^1..T^{15}$ (884 coefficients each):

```
psi     v3=1:284  v3=2:386  v3=3:127  v3=4:63  v3=5:13  v3=6:6  v3=7:4  v3=8:1
naive   v3=1:284  v3=2:389  v3=3:131  v3=4:52  v3=5:21  v3=6:7
E3only  v3=0:30   v3=1:273  v3=2:347  v3=3:160  v3=4:51  v3=5:20  v3=6:3
```
`psi` and `naive` have **exactly the same number (284) of coefficients at the critical
valuation $v_3=1$**. The bound $v_3\ge1$ is sharp for both; $\psi^3$ gives no margin.

---

## 4. Task 4 — the three predictions

**(a) "$\psi^3$ passes at least as far as the naive lift did."**
**PASS, but vacuously.** Both reach $T^{30}$ at 7 base points and $T^{15}$ symbolically, with
identical behaviour. $\psi^3$ is not *further*.

**(b) "$\psi^3$ passes at base points with $\varphi_1\ne0$ where the naive lift fails."**
**FAIL.** With the correct composition order both lifts pass at **all** tested points,
$\varphi_1\in\{-1,0,1,2,2,3,7\}$. There is no point where naive fails and $\psi^3$ succeeds.
(With the *incorrect* order $\tau\circ\varsigma$, $\psi^3$ passes at $\varphi_1=1,7$ where
naive fails at all points — but that quantity is not the Dwork defect.)

**(c) "$v_3$ of the defect coefficients is better (larger) under $\psi^3$."**
**FAIL.** Minimum $v_3$ is exactly 1 for both, at every $T$-degree $\ge1$ at every base point
(except one entry at $(0,0)$, $n=9$). Symbolically, both have 284 coefficients with $v_3=1$.
No improvement.

---

## 5. The load-bearing conclusion: the Dwork reformulation is a tautology

Dieudonné–Dwork is an **iff**: for a $3$-torsion-free, $3$-adically complete $\mathbb Z_3$-algebra
$R$ with *any* Frobenius lift $\varsigma$, and $G\in1+TR_{\mathbb Q}[[T]]$,
$$G\in 1+TR[[T]] \iff \frac{G(T)^3}{\varsigma(G)(T^3)}\in 1+3T\,R[[T]].$$
Applying it to $G=H=\tau(F_P)/F_P$: **the truth value of the criterion does not depend on
which Frobenius lift is used.** So

* passing the Dwork test with $\psi^3$ is exactly as strong as passing it with $E_i^3$,
  and both are exactly as strong as verifying $H\in 1+T\mathbb Z_3[E][[T]]$ directly
  (which `symH.py`/`bigdata.py` already did, to $T^{14}$ symbolically / $T^{36}$ numerically);
* the Day 146 numerics "verified to $T^{22}$ at three base points" are **not independent
  evidence** — they are a re-encoding of the same $H$-integrality data;
* the remark "without the $E_3\mapsto E_3^3$ twist the criterion genuinely fails" is correct
  but content-free: `ident` is simply not a Frobenius lift.

Choosing a *canonical* lift can only help if the lift interacts with the **master equation**
(so that $\varsigma(F_P)$ satisfies something computable). $\psi^3$ does not: it fails to
commute with $\tau$, and by §2b **no** lift can. Any real gain must come from a mechanism
that controls $\varsigma(F_P)$ directly, not from the choice of $\varsigma$.

---

## 6. Files

| file | purpose |
|---|---|
| `task12_psi3.py` | $\psi^3(E_i)$; $\tau$ is $u\mapsto u+1$; mod-3 commutation defects (all $\equiv0$) |
| `task2b_mod9.py` | $\delta$-level (defect$/3$ mod 3) comparison — neither lift commutes |
| `no_commute_thm.py` | proof + brute-force check: no Frobenius lift commutes with $\tau$ |
| `dwork_gen.py` | general framework: lift applied symbolically, then $(E_1,E_2)$ specialised, $E_3$ kept |
| `sanity.py` | reproduces Day 146 `dwork.py` / `Hdiag.py` |
| `main2.py` | 4 lifts × 7 base points × both composition orders, $N=21$ |
| `deep.py` | $N=30$, per-$T$-degree $v_3$ tables, $H$-integrality cross-check |
| `symbolic.py` | fully symbolic in $\mathbb Z[E_1,E_2,E_3]$, $N=15$; writes `D_*.pkl` |
