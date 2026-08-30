# Day 147 — Gauss congruence route to $3\mid b_k$: verdicts

**Date:** 2026-08-30. Code in this directory: `regen.py`, `gauss.py`, `realiz.py`, `identity.py`, `alg.py`, `offdiag.py`, `dworkdefect.py`, `ctmodel.py`. Data: `data.json`, `big45.log`.

---

## TASK 1 VERDICT — **THE REDUCTION IS SOUND. IT IS NOT VACUOUS.**
### But it is an *equivalence*, its diagonal evidence is *circular*, and the writeup contains three real overclaims.

**(a) Would $h_j\in\mathbb Z$ for all $j$ prove $3\mid b_k$?**
**YES** — that is exactly Theorem 3 of the Day 146 writeup, and the implication is correct.
But this is not vacuity: **"$h_j\in\mathbb Z$ for all $j$" is not known.** Only $j\le 15$ has been
computed (independently regenerated and extended today). The reduction quantifies over an infinite set; the
table is finite data. No misstatement here.

**(b)/(c) What the writeup gets wrong.** Three genuine defects, in §6.3 / §10 / §11:

1. **Line 294 is FALSE as written:**
   > "So (H1) is not merely sufficient — it is *equivalent* to the theorem."

   (H1) is $H=\tau(F_P)/F_P\in\mathbb Z[E_1,E_2,E_3][[T]]$: **all** coefficients, over $\mathbb Z$,
   at **all** primes. What line 293 actually proves is
   $\mathcal H=\ell_0(H)\in\mathbb Z_3[[\vartheta]]\iff 3\mid b_k\ \forall k$ — a statement about the
   $\ell_0$-**diagonal only**, and **3-adically only**. (H1) $\Rightarrow$ target, but not
   conversely: (H1) is **strictly stronger**. Correct sentence:
   > "The *diagonal, 3-adic shadow* of (H1) is equivalent to the theorem; (H1) itself is strictly stronger."

2. **Line 456 (FPSAC Theorem 3.10) drops a hypothesis.** It asserts
   $F^2-F=\vartheta\mathcal H(2F-3)$ and the equivalence unconditionally. But §6.2 Theorem 2 begins
   "**Assume (H2).**" (line 252), and the equivalence in §6.3 is derived from (6.1). So the headline
   equivalence is proved **only modulo (H2)**. Unconditionally we do not yet have the main identity.

3. **Line 466 repeats defect 1:** "Conjecture H is equivalent (via §6.3) to the target theorem."
   Same error — only its diagonal 3-adic shadow is.

*(Side note, not a defect: line 369 uses the Frobenius lift $\varsigma(E_i)=E_i^3$, while the Day 146 dream
journal concluded the lift "should be" the Adams $\psi^3$. **Both are legitimate lifts** — $\varsigma$ mod 3
agrees with Frobenius on generators, and $\psi^3(p_n)=p_{3n}$ likewise — so Dieudonné–Dwork is valid for
either. They simply give *different* criteria; the useful one is whichever commutes with $\tau$. No
contradiction between the two records.)*

**Corrected statement (use this one):**
> **Assume (H2).** Then $F^2-F=\vartheta\,\mathcal H\,(2F-3)$ with $\mathcal H=\ell_0(\tau(F_P)/F_P)$, and
> $$\mathcal H\in\mathbb Z_3[[\vartheta]]\iff 3\mid b_k\ \forall k.$$
> (H1) implies the left side but is strictly stronger than it.

I re-checked the converse direction myself and it is correct: if $3\mid b_k\ \forall k$ then
$(F^2-F)/\vartheta\in3\mathbb Z_3[[\vartheta]]$ and $2F-3=-3(1-\tfrac23F)$ with $1-\tfrac23F$ a unit
in $\mathbb Z_3[[\vartheta]]$, so $\mathcal H\in\mathbb Z_3[[\vartheta]]$. The two $3$'s cancel exactly.

**The circularity Rick must internalise.** `identity.py` reconstructs $h_0,\dots,h_{11}$ from
$b_1,\dots,b_{12}$ alone (via $\mathcal H=(F^2-F)/(\vartheta(2F-3))$) and gets **exact agreement** with the
independently computed $h_j$. The map is invertible and its denominators are powers of $3$ only.
Therefore: **"$h_j\in\mathbb Z_3$ for $j\le11$" and "$3\mid b_k$ for $k\le12$" are the same fact.**
The 13 tabulated $h_j$ are **zero independent evidence** for the mod-3 problem. All genuinely new
content lives (i) off the $\ell_0$ diagonal, and (ii) at primes $\ne3$.

---

## TASK 0 — regeneration and extension (independent)

`regen.py` rebuilds $\Psi_b\to P_b\to F_P$ from the recursion in `core.py` with **freshly written**
series algebra, computes $H=\tau(F_P)/F_P$ at $(E_1,E_2)=(-2,1)\to(1,0)$ and extracts
$h_j=[E_3^jT^{3j}]H$. Run at `BMAX=36` (93s) and then `BMAX=45` (558s):

* $h_j$ ($j=0..12$): $1, 8, 119, 2200, 45500, 1007904, 23387442, 561163152, 13809781700,$
  $346645093984, 8840919351575, 228449188011224, 5968029850876084$ — **reproduces Rick's table exactly**, all integers; extended to $h_{15}$.
* $b_k$ ($k=1..12$): reproduces Rick's list exactly; extended to $b_{15}$.
* Main identity (6.1) verified on this independent data through $\vartheta^{12}$ (`identity.py`).

$S=\log\mathcal H=\sum s_n\vartheta^n/n$. **Confirmed** $s_1..s_6 = 8, 174, 4256, 109646, 2909088, 78660642$
and **extended to $n=15$** — all integers:

| $n$ | $s_n$ | | $n$ | $s_n$ |
|--:|--:|---|--:|--:|
|1|8|  |9|1662632335520|
|2|174|  |10|46629661428344|
|3|4256|  |11|1314114092088960|
|4|109646|  |12|37183273797967010|
|5|2909088|  |13|1055675592209660768|
|6|78660642|  |14|30058458914071059660|
|7|2155331424|  |15|857996218018727493696|
|8|59637739662|  | | |

**NEW DATA (BMAX=45, extends Rick's tables past $k=12$):**
$$h_{13}=157362931790134880,\quad h_{14}=4182508112784714612,\quad h_{15}=111938320276080080544$$
$$b_{13}=22087492351683636,\quad b_{14}=583048865756462670,\quad b_{15}=15511745688519457404$$
with $v_3(b_{13,14,15})=1,2,2$ — **three new confirmations of $3\mid b_k$.**
Full $v_3(b_k)$, $k=1..15$: $1,3,1,1,2,3,2,2,1,1,2,1,1,2,2$.

---

## TASK 2 — Gauss congruences

$M_n:=\sum_{d\mid n}\mu(n/d)s_d$. **All congruences HOLD for $1\le n\le15$, at every prime.**

| $n$ | $M_n$ | $M_n \bmod n$ |
|--:|--:|--:|
|1|8|0|
|2|166|0|
|3|4248|0|
|4|109472|0|
|5|2909080|0|
|6|78656220|0|
|7|2155331416|0|
|8|59637630016|0|
|9|1662632331264|0|
|10|46629658519090|0|
|11|1314114092088952|0|
|12|37183273719196896|0|
|13|1055675592209660760|0|
|14|30058458911915728070|0|
|15|857996218018724580360|0|

No failures. Prime-by-prime $s_n\equiv s_{n/p}\bmod p^{v_p(n)}$: OK at $p=2,3,5,7,11$ for every
applicable $n\le15$. **Slack at $p=3$:** $v_3(s_n-s_{n/3})=v_3(n)+1$ in **all five** cases
$n=3,6,9,12,15$ (valuations $2,2,3,3,2$ vs $v_3(n)=1,1,2,1,1$) — exactly one more $3$ than Gauss demands,
every time. This now looks like a real pattern, not noise. No such uniform slack at $p=5,7$ ($v_p$ equals
$v_p(n)$ exactly); $p=2$ has large erratic slack.

### Circularity audit — **the $p=3$ Gauss congruence is LOGICALLY EQUIVALENT to the target.**

*Proof.* Dieudonné–Dwork: for $\mathcal H=\exp(S)\in1+\vartheta\mathbb Q_3[[\vartheta]]$,
$\mathcal H\in\mathbb Z_3[[\vartheta]]\iff \mathcal H(\vartheta)^3/\mathcal H(\vartheta^3)\in1+3\vartheta\mathbb Z_3[[\vartheta]]$.
Taking $\log$ (legitimate: $\exp/\log$ are inverse bijections $3\mathbb Z_3\leftrightarrow1+3\mathbb Z_3$ since $1>\frac1{p-1}=\frac12$),
$\log\big(\mathcal H^3/\mathcal H(\vartheta^3)\big)=3S(\vartheta)-S(\vartheta^3)=\sum_n\tfrac3n(s_n-s_{n/3})\vartheta^n$
(with $s_{n/3}:=0$ if $3\nmid n$). So the criterion reads $v_3(s_n-s_{n/3})\ge v_3(n)$ — the $p=3$
Gauss congruence. And $s_n\in\mathbb Z_3$ follows from $h_j\in\mathbb Z_3$ by Newton
$s_n=nh_n-\sum_{j<n}s_jh_{n-j}$. Combining with §6.3:
$$\big[s_n\in\mathbb Z_3\ \&\ \text{Gauss at }p=3\big]\iff\mathcal H\in\mathbb Z_3[[\vartheta]]\iff 3\mid b_k\ \forall k.\qquad\square$$

**Consequence: neither strictly stronger nor weaker — EXACTLY equivalent.** Proving the $p=3$
Gauss congruence directly is precisely as hard as the original problem. It is a restatement, and
the numerical verification at $n\le12$ is the same data as $3\mid b_k$ at $k\le12$. The congruences
at $p=2,5,7,11$ are likewise restatements of $h_j\in\mathbb Z$.

### The one genuinely new fact today

`realiz.py`: the necklace numbers $m_n=M_n/n$ are **non-negative integers** for all $n\le12$:
$$8,\;83,\;1416,\;27368,\;581816,\;13109370,\;307904488,\;7454703752,\;184736925696,$$
$$4662965851909,\;119464917462632,\;3098606143266408,\;81205814785358520,$$
$$2147032779422552005,\;57199747867914972024.$$
So $(s_n)$ is **exactly realizable** on $n\le15$ (Dold / Puri–Ward): it looks like
$s_n=\#\mathrm{Fix}(f^n)$ for a map $f$ with $m_n$ orbits of length $n$.
**Positivity of $m_n$ is NOT implied by $h_j\in\mathbb Z$ and is not circular.** This is the only
non-circular signal in today's numerics, and it is exactly the hypothesis a necklace/cyclic-sieving
argument would need. **If Rick can exhibit the model $f$ (or a matrix $M$ with $s_n=\operatorname{tr}M^n$,
or a set of words closed under rotation), the congruence follows at all primes at once — including
$p=3$ — and that would be a real, non-circular proof.** That is the whole value of the Gossow lead.

---

## TASK 4 — OEIS and holonomy

**P-recursion:** exact nullspace search over $\mathbb Q$ for $\sum_{i=0}^r p_i(n)u_{n+i}=0$, $\deg p_i\le d$,
demanding strictly more equations than unknowns. **NONE found** for $s_n$, $h_j$, or $b_k$.
Honest caveat — with only 12–13 terms the testable box is small:
$r=1,d\le4$; $r=2,d\le2$; $r=3,d\le1$; $r\ge4,d=0$. A moderate-order holonomic recurrence is **not** excluded.

**Algebraicity:** searched $\sum_{j\le d}P_j(\vartheta)G^j=0$ for $G=\mathcal H$ and $G=F$, boxes up to
$(d,e)=(1,4),(2,3),(3,2),(4,1)$. **NONE.** So neither $\mathcal H$ nor $F$ is algebraic of low degree
(consistent: the identity $F^2-F=\vartheta\mathcal H(2F-3)$ is one equation in two unknowns and
constrains neither alone).

**Growth:** $s_{n+1}/s_n = 21.8, 24.5, 25.8, 26.5, 27.0, 27.4, 27.7, 27.9, 28.0, 28.2, 28.3$ —
still increasing; no clean limit yet, so a *finite* matrix-trace model $s_n=\operatorname{tr}M^n$
(which would force a constant ratio $\to\lambda$) is not yet supported by the growth data.
$h_{j+1}/h_j\to\approx26.1$, $b_{k+1}/b_k\to\approx25.9$, both still rising.

**OEIS (queried directly at `oeis.org/search?fmt=text`, all returned `No results.`):**

| sequence | query | result |
|---|---|---|
| $s_n$ | `8,174,4256,109646,2909088,78660642` | **NOT FOUND** |
| $s_n$ prefix | `8,174,4256,109646` / `8,174,4256` | **NOT FOUND** |
| $h_j$ | `1,8,119,2200,45500,1007904` | **NOT FOUND** |
| $h_j$ prefixes | `1,8,119,2200,45500` / `1,8,119,2200` / `8,119,2200,45500,1007904` | **NOT FOUND** |
| necklace $m_n$ | `8,83,1416,27368,581816` / `8,83,1416,27368` | **NOT FOUND** |
| Gossow $c_n$ | `8,55,808,14891,307624` | **NOT FOUND** |
| $b_k$ (re-confirmed) | `3,27,417,7851,164124,3661389` | **NOT FOUND** |

Not even 3- or 4-term prefixes match. Every sequence in this circle of ideas is absent from OEIS.

---

## TASK 3 — Gossow arXiv:2410.05678 — **VERDICT: NOT APPLICABLE.**

PDF: `/home/agent/papers/gossow-gauss-2410.05678.pdf` (text: `gossow-gauss.txt`).

**What the theorems quantify over.** *Gauss congruence is a standing HYPOTHESIS throughout, never a
conclusion derived from weaker data.*
* **Thm 3.3 (=1.1):** for integer sequences on a ranked semigroup, Gauss congruence $\iff$ $\exists$
  integer $(b_s)$ with $a_s=\sum_{t|s}b_t\mathrm{rk}(t)$ $\iff$ $\exists$ integer $(c_s)$ (composition form).
  This is **Möbius inversion** — a restatement, not a criterion.
* **Thm 4.16 (=1.2):** takes "$(a_s)$ **satisfying Gauss congruence**" as given, outputs $q$-analogues.
* **Thm 5.2 (=1.3):** the *only* theorem producing Gauss congruence. Hypothesis = a **Lyndon structure**:
  finite sets $X_s$ with $C_{\mathrm{rk}(s)}$-actions and a **proof** that $\#X_s^{C_d}=\sum_{t\in s/d}\#X_t$.
  That fixed-point identity is logically equivalent to the congruence you want.
* **Thms 6.4/6.5/8.2:** go the other way (Gauss congruence $\Rightarrow$ festoon model), constructive but
  **tautological** — the bead-colour data *is* $(c_s)$. Remark 5.3: a Lyndon structure exists iff $b_s\ge0$.
* **Thm 6.10** needs $D\in\mathbb Z((t))$ with $C=xD(C)$; our $D=8+\tfrac{55}{8}t+\tfrac{3439}{512}t^2+\cdots$
  has 2-power denominators, so $D\notin\mathbb Z((t))$ and 6.10 does not apply over $\mathbb Z$.

**Input, not output.** Rick would have to supply the Lyndon structure (or the integrality of $b_n$/$c_n$),
i.e. supply the answer. What he'd get: a $q$-analogue, a CSP, and a festoon interpretation. **Zero
progress on the congruence.** Note his $b_n$ (= our necklace numbers $8,83,1416,27368,581816,13109370,\dots$)
and $c_n=-[z^n]\mathcal H^{-1}=8,55,808,14891,307624,6811089$ are all positive in range, so Thm 6.4 *would*
hand him a festoon model **after** the proof, as decoration. **This would be name-match #9.**

### Secondary papers
* **Pomerat–Straub 2406.12010** — Thm 1.1 is about $p^r$-th roots; not applicable. Their **Cor. 4.2** is
  exactly the Dieudonné–Dwork additive criterion I re-derived above (i.e. the circularity), and **Cor. 4.3**
  is a graded/quantified refinement ($f^{1/p^r}\in\mathbb Z_p[[x]]\iff f(x)^p\equiv f(x^p)\bmod p^{r+1}$)
  that could be usable if the 3-adic gap between $\mathcal H^3$ and $\mathcal H(\vartheta^3)$ is measurable —
  note our observed **slack of exactly one power of 3** is precisely this kind of datum. **Marginal.**
* **Delaygue–Rivoal 2501.16281** — Thm 1: for $\eta$ **algebraic over $\overline{\mathbb Q}(x)$**,
  $y'=\eta y$ has an algebraic solution $\iff$ $x\eta$ has the Gauss property $\iff$ Cartier property.
  With $\eta=\mathcal H'/\mathcal H$ this is formally our situation and is the only equation-based criterion
  of the three. **Two killers:** (a) algebraicity of $\eta$ must be *supplied*, and our searches found
  neither a low-order P-recursion nor low-degree algebraicity for $\mathcal H$ or $F$; (b) their "Gauss
  property" means Gauss congruences **for almost all primes**, proved via Eisenstein — the excluded set is
  exactly where $p\mid\lambda$, and "$3\nmid\lambda$" is the 3-integrality being sought. **Circular at $p=3$.
  NOT APPLICABLE.**

### The one genuinely actionable lead (from Delaygue–Rivoal §2.3, not their main theorem)

**Constant-term / trace representations give Gauss congruences at EVERY prime with no algebraicity and no
combinatorial model**, via $\lambda(x)^p\equiv\lambda(x^p)\bmod p$:
* Jänichen (1921): $s_n=\operatorname{Tr}(A^n)$, $A$ an integer matrix.
* **Bostan–Straub–Yurkevich**, *J. Number Theory* **253** (2023) 235–256: $s_n=\mathrm{Cst}(\lambda^n)$ for
  $\lambda\in\mathbb Z[x_1^\pm,\dots,x_r^\pm]$.
* **Beukers–Houben–Straub**, "Gauss congruences for rational functions in several variables,"
  *Acta Arith.* **184.4** (2018) 341–362 — criteria for **diagonals of rational functions**, the closest
  hypothesis class to Rick's actual object ($\mathcal H$ *is* a diagonal, $\ell_0(\tau F_P/F_P)$).

**TARGET TO AIM AT: write $s_n=\mathrm{Cst}\big(\lambda(x_1,\dots,x_r)^n\big)$ for some Laurent polynomial
$\lambda$ over $\mathbb Z$ (or $s_n=\mathrm{cst}\operatorname{Tr}(A^n)$).** That yields Gauss congruence at
$p=3$ immediately and non-circularly. The empirical support is the exact-realizability finding above
($m_n\ge0$ for $n\le12$). **Caveat:** the growth ratios $s_{n+1}/s_n$ are still *rising* at $28.3$, which
argues against a *finite* integer matrix $A$ (that would force a constant limit $\lambda$); a
constant-term/Laurent-polynomial model is the better bet.

### Bonus reformulation (verified numerically)
From $F^2-F=\vartheta\mathcal H(2F-3)$: $\ \mathcal H^{-1}=\dfrac{3\vartheta}{F}+\dfrac{\vartheta}{1-F}$.
Since $\vartheta/(1-F)\in\mathbb Z[[\vartheta]]$ unconditionally and $3\vartheta/F=1/G$ with
$G:=F/(3\vartheta)=\sum_k(b_k/3)\vartheta^{k-1}$, $G(0)=1$:
$$\text{Gauss at }p{=}3\iff\mathcal H\in\mathbb Z_{(3)}[[\vartheta]]\iff G\in\mathbb Z_{(3)}[[\vartheta]]\iff 3\mid b_k\ \forall k .$$
A one-line proof of the circularity, independent of the Dieudonné–Dwork argument above.

---

## Addendum — the Dwork defect $K:=\mathcal H(\vartheta)^3/\mathcal H(\vartheta^3)$ (`dworkdefect.py`)

$v_3([\vartheta^n]K)$ for $n=0..15$: $0,\ \mathbf1,\ 2,\ 2,\ \mathbf1,\ 2,\ 2,\ 2,\ 2,\ 2,\ \mathbf1,\ 4,\ 2,\ \mathbf1,\ 2,\ 2$.
**$\min_{n\ge1}v_3=1$, attained at $n=1,4,10,13$.** So $K\in1+3\vartheta\mathbb Z_3[[\vartheta]]$ **exactly** —
there is **no uniform extra power of 3**, and **Pomerat–Straub Cor. 4.3 gives no refinement here.**
(The slack $v_3(s_n-s_{n/3})=v_3(n)+1$ is real and now 5/5, but it is confined to $3\mid n$, where the extra
$3$ is invisible in $K$ because the $3\nmid n$ coefficients already sit at $v_3=1$.)

**Singularity estimate.** Richardson on $h_{j+1}/h_j$ gives $1/\rho\approx29.16$ and still climbing
($14.9,22.1,25.1,26.6,27.4,27.9,28.3,28.5,28.7,28.9,29.0,29.05,29.11,29.16$). Consistent with an algebraic singularity but
not converged; not enough terms to pin the exponent.

---

## Addendum — how much of Conjecture H's evidence is NOT circular (`offdiag.py`)

At $(E_1,E_2)=(-2,1)$, $\mathrm{BMAX}=30$, the series $H=\tau(F_P)/F_P$ has **176 nonzero coefficients**:
* **11** lie on the $\ell_0$ diagonal $b=3k$ — these are the $h_j$, and their integrality is *circular*
  with $3\mid b_k$ (shown above);
* **165** lie **off** the diagonal — their integrality is **genuinely independent evidence for (H1)**,
  not implied by $3\mid b_k$ at any prime.
* **0** violations of (H1) integrality, **0** violations of (H2) order $\ge0$.

**So Conjecture H is a real conjecture with real evidence.** What is circular is only the specific
inference "the $h_j$ are integers, therefore $\mathcal H\in\mathbb Z_3[[\vartheta]]$ is well-supported."
Rick should quote the **165 off-diagonal coefficients** as his evidence, not the 13 $h_j$.

---

## Recommendation — and one pre-emptive warning about the next name-match

**Do NOT spend a session on Gossow.** It is a $q$-analogue/CSP paper; Gauss congruence is its hypothesis.

**The Beukers–Houben–Straub / Bostan–Straub–Yurkevich lead is better but has a hypothesis mismatch that
must be checked before investing.** BHS is about **diagonals of RATIONAL functions** in several variables.
$\mathcal H=\ell_0(\tau(F_P)/F_P)$ is a diagonal of a **ratio of divided-power series** — and $F_P$ is not
rational, not algebraic, not even convergent: $F_P|_{E_3=0}={}_2F_0(U,V;;T)$ is divergent, and §9 of the
Day 146 writeup gives $F_P=e^{3\rho/2}\Pi(\rho,T)$, an irregular/Gevrey object. **The hypothesis class does
not match as stated.** Do not treat "$\mathcal H$ is a diagonal" as a licence to apply BHS — that would be
name-match #10. What *would* work is a genuine constant-term representation:
$$s_n=\mathrm{Cst}\big(\lambda(x_1,\dots,x_r)^n\big),\qquad \lambda\in\mathbb Z[x_1^\pm,\dots,x_r^\pm],$$
which gives Gauss congruence at **every** prime from $\lambda^p\equiv\lambda(x^p)\bmod p$ — no algebraicity,
no combinatorial model, non-circular. **This is the only route surfaced today that is not a restatement.**

**Empirical support FOR its existence:** exact realizability ($m_n\ge0$, $n\le12$) — verified, and
equivalently the Euler product
$$\mathcal H=\prod_{n\ge1}(1-\vartheta^n)^{-m_n},\qquad m_n\in\mathbb Z_{\ge0}\ (n\le12)$$
which I confirmed reproduces all 13 $h_j$ exactly.

**Empirical evidence AGAINST it (`ctmodel.py`) — read this before investing.** If $s_n=\mathrm{Cst}(\lambda^n)$
for $\lambda\in\mathbb Z[x_1^\pm,\dots,x_r^\pm]$, saddle-point asymptotics force
$s_n\sim CL^n n^{-r/2}$, i.e. writing $s_{n+1}/s_n=L(1-a/n)$ one must have $a=r/2>0$. Two-point fits give
$$a=-0.285,\,-0.358,\,-0.393,\,-0.415,\,-0.429,\,-0.439,\,-0.447,\,-0.453,\,-0.457,\,-0.461,\,-0.464,\,-0.467,\,-0.469$$
— **$a<0$ throughout and decreasing monotonically toward $-1/2$**, i.e. $s_n\sim CL^nn^{+1/2}$
($L$ fitted $\approx27.6$ and still rising; Richardson on $h$ says $\approx29.2$). A *positive* subexponential exponent is **incompatible with
$s_n=\mathrm{Cst}(\lambda^n)$ for any $r\ge1$.** It is however consistent with $\sum s_nz^n$ having a
$(1-Lz)^{-3/2}$ singularity — and note $t_n:=s_n/n\sim CL^nn^{-1/2}$ *does* have the right shape for a
one-variable constant term, but the $t_n$ are not integers.

Corroborating: `ctmodel.py` finds $\sum_{n\ge0}s_nz^n$ (with $s_0=1$) **neither algebraic** (boxes to
$(d,e)=(1,5),(2,4),(3,2),(4,2),(5,1)$) **nor holonomic** (boxes to $(r,d)=(1,5),(2,3),(3,2),(4,1),(5,0)$) —
though 16 terms still make these weak tests.

**Net: the constant-term route is the best-shaped lead available, but the asymptotics currently point away
from it. Rick should test the exponent on more terms before committing a session.** With $n\le12$ and
$L$ itself unconverged this is suggestive, not decisive.

**Empirical evidence against a finite integer matrix $s_n=\operatorname{Tr}(A^n)$:** that forces
$s_{n+1}/s_n\to\lambda$ with *exponentially* small correction; ours is still rising at $28.3$ with an
$O(1/n)$ correction. Effectively ruled out.

---

## Pending
`BMAX=45` **COMPLETED** (558s, `big45.log`) — all tables above are at $n\le15$. Next cheapest step:
`BMAX=54` for $s_{18}$, to settle whether the asymptotic exponent $a$ really goes to $-1/2$ (the deciding
question for the constant-term route). Expect a few hours of $\Psi$-building.
