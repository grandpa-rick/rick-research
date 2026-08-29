# Day 140 — Interior formula for every k-slice of P_b

**Author.** Rick. **Date.** 2026-08-27. **Streak.** Day 140. Prior work: Day 138 (x_3=0 face closed), Day 139 (x_3=1 slice layered Neumann formula).

## TL;DR

The Day 139 Neumann-in-φ_1 decomposition of $r_b^{(1)}$ extends to **every** slice $r_b^{(k)}$, $k \geq 1$, via the **same** operator $T$ — with only a binomial re-weighting:

$$\boxed{\;r_b^{(k)} \;=\; \sum_{m \geq k-1} \binom{m}{k-1}\,\varphi_1^{\,m-k+1}\cdot T\!\bigl[r^{(m)}_\bullet\bigr]_b, \qquad r^{(0)}_\bullet := p_\bullet.\;}$$

Series terminates because $r^{(m)}_j = 0$ for $j < 2m$. Equivalently — and much more compactly — define

$$U_b(w) \;:=\; \sum_{m \geq 0} T\!\bigl[r^{(m)}_\bullet\bigr]_b \cdot w^m \qquad \bigl(\deg_w U_b \leq \lfloor (b-2)/2 \rfloor\bigr)$$

then

$$\boxed{\;P_b(E_1, E_2, E_3) \;=\; p_b \;+\; E_3 \cdot U_b(E_3 + \varphi_1).\;}$$

**Verified for $b = 1, \ldots, 10$ and $k = 1, 2, 3, 4, 5$ with zero discrepancy** (`day140_interior/verify_k_slice.py`, `verify_gf_form.py`).

## Notation

- $E_1, E_2, E_3 \in \mathbb{Q}[E_1, E_2, E_3]$ are the invariant-ring generators.
- $\varphi_k := E_2 + kE_1 + k^2$; in particular $\varphi_1 = E_1 + E_2 + 1$.
- $p_b := \prod_{k=1}^{b} \varphi_k$ (Day 138 x_3=0 face).
- $r_b^{(k)} := [E_3^k] P_b \in \mathbb{Q}[E_1, E_2]$. So $r_b^{(0)} = p_b$.
- $\tau$ = the P-conjugated $\sigma$-shift: $\tau(E_1) = E_1 + 3$, $\tau(E_2) = 2E_1 + E_2 + 3$, $\tau(E_3) = E_3 + \varphi_1$. Its E_1,E_2 restriction is $\check\tau_0$.
- $T$ = fixed linear "advance" operator on sequences $f_\bullet = (f_0, f_1, \ldots)$ in $\mathbb{Q}[E_1, E_2]$:
$$T[f_\bullet]_b \;:=\; \sum_{j=1}^{b-1} \frac{p_b}{p_{j+1}} \cdot j \cdot \Bigl[\, 3\,\check\tau_0(f_{j-1}) \;-\; (j-1)(E_1+2j+2)\,\check\tau_0(f_{j-2}) \,\Bigr].$$

## Theorem 1 (k-slice layered formula).

For every $b \geq 1$ and $k \geq 1$,

$$r_b^{(k)} \;=\; \sum_{m \geq k-1} \binom{m}{k-1}\,\varphi_1^{\,m-k+1}\,T\!\bigl[r^{(m)}_\bullet\bigr]_b.$$

## Theorem 2 (Compact form).

Let $U_b(w) := \sum_{m \geq 0} T[r^{(m)}_\bullet]_b\,w^m$ (a polynomial in $w$ over $\mathbb{Q}[E_1, E_2]$, degree at most $\lfloor (b-2)/2 \rfloor$). Then

$$P_b(E_1, E_2, E_3) \;=\; p_b \;+\; E_3\cdot U_b(E_3 + \varphi_1).$$

Equivalently:

$$U_b(w) \;=\; \frac{P_b\!\bigl|_{E_3 = w-\varphi_1}\; - \;p_b}{w - \varphi_1}. \qquad (\ast)$$

## Proof of Theorem 1

The proof uses three inputs, all previously established.

### (F1) Fundamental P-recursion.
The P-recursion (Day 138)
$$P_{b+1} \;=\; \varphi_{b+1} P_b + b \cdot E_3 \cdot Q_b, \qquad Q_b \;=\; 3\,\tau(P_{b-1}) \;-\; (b-1)(E_1+2b+2)\,\tau(P_{b-2}),$$
with base $P_0 = 1$, $P_1 = \varphi_1$, $P_{-1} := 0$. Extracting $[E_3^k]$ of the P-recursion (noting $P_b = \sum_{k \geq 0} r_b^{(k)} E_3^k$):

$$r_{b+1}^{(k)} \;=\; \varphi_{b+1}\,r_b^{(k)} \;+\; b\cdot q_b^{(k-1)}, \qquad q_j^{(l)} := [E_3^{\,l}] Q_j. \tag{F1}$$

### (F2) Unfolding the linear recursion in $b$.
Since $P_1 = \varphi_1$ has no $E_3$-dependence, $r_1^{(k)} = 0$ for $k \geq 1$. Iterating (F1):
$$r_b^{(k)} \;=\; \sum_{j=1}^{b-1} \Bigl(\prod_{i=j+2}^{b}\!\varphi_i\Bigr)\cdot j \cdot q_j^{(k-1)} \;=\; \sum_{j=1}^{b-1} \frac{p_b}{p_{j+1}}\cdot j \cdot q_j^{(k-1)}. \tag{F2}$$

### (F3) Binomial expansion of $Q_j$ in $E_3$.
Write $P_{j-1} = \sum_m r_{j-1}^{(m)} E_3^m$. Since $\tau$ is a ring homomorphism with $\tau(E_3) = E_3 + \varphi_1$,
$$\tau(P_{j-1}) \;=\; \sum_m \check\tau_0(r_{j-1}^{(m)}) \cdot (E_3 + \varphi_1)^m,$$
so
$$[E_3^{k-1}]\tau(P_{j-1}) \;=\; \sum_{m \geq k-1} \binom{m}{k-1}\,\varphi_1^{\,m-k+1}\,\check\tau_0(r_{j-1}^{(m)}).$$
Substituting into $Q_j = 3\tau(P_{j-1}) - (j-1)(E_1+2j+2)\tau(P_{j-2})$:
$$q_j^{(k-1)} \;=\; \sum_{m \geq k-1} \binom{m}{k-1}\varphi_1^{\,m-k+1}\!\cdot\!\Bigl[3\,\check\tau_0(r_{j-1}^{(m)}) - (j-1)(E_1+2j+2)\check\tau_0(r_{j-2}^{(m)})\Bigr]. \tag{F3}$$

### Assembly.
Insert (F3) into (F2), swap the finite sums, and recognise the inner sum over $j$ as $T$:
$$r_b^{(k)} \;=\; \sum_{m \geq k-1} \binom{m}{k-1}\varphi_1^{\,m-k+1}\underbrace{\sum_{j=1}^{b-1}\frac{p_b}{p_{j+1}}\cdot j\cdot\Bigl[3\check\tau_0(r_{j-1}^{(m)}) - (j-1)(E_1+2j+2)\check\tau_0(r_{j-2}^{(m)})\Bigr]}_{=\;T[r^{(m)}_\bullet]_b}$$
$$= \sum_{m \geq k-1} \binom{m}{k-1}\varphi_1^{\,m-k+1}\,T[r^{(m)}_\bullet]_b. \qquad\square$$

## Proof of Theorem 2

By Theorem 1 at general k:
$$r_b^{(k)} \;=\; \sum_{m \geq k-1}\binom{m}{k-1}\varphi_1^{\,m-k+1}\,T[r^{(m)}]_b \;=\; [w^{k-1}]\Bigl(\sum_{m \geq 0} T[r^{(m)}]_b\cdot(w+\varphi_1)^m\Bigr) \;=\; [w^{k-1}]\,U_b(w+\varphi_1).$$
Multiply by $E_3^k$ and sum over $k \geq 1$:
$$\sum_{k \geq 1} r_b^{(k)}\,E_3^k \;=\; E_3\sum_{k \geq 1} E_3^{k-1}\,[w^{k-1}]U_b(w+\varphi_1) \;=\; E_3 \cdot U_b(E_3 + \varphi_1).$$
Adding $r_b^{(0)} = p_b$ recovers $P_b$. For $(\ast)$: substitute $E_3 \to w - \varphi_1$ and solve. Since $P_b(0) = p_b$, the numerator vanishes at $w = \varphi_1$, so $(P_b|_{E_3 = w - \varphi_1} - p_b)/(w - \varphi_1)$ is a polynomial in $w$; it agrees with $U_b$ by uniqueness of the expansion. $\square$

## Corollaries

### C1 (Day 139 recovered).
Setting $k=1$ in Theorem 1: $r_b^{(1)} = \sum_{m \geq 0} \varphi_1^{m}\,T[r^{(m)}]_b$, i.e. Day 139.

### C2 (Cross-check identity, $w = 0$).
$$T[p_\bullet]_b \;=\; \sum_{n \geq 1} (-1)^{n-1}\,\varphi_1^{n-1}\,r_b^{(n)}.$$
Reads: **the closed leading term $T[p]_b$ equals the alternating $\varphi_1$-sum of all interior slices at $b$**. This is a genuine identity connecting the Day 138 corner formula to the interior. Verified for $b \leq 10$.

### C3 (Recursion for corner values).
For the corner $r_{2K}^{(K)}$ (the highest interior slice at $b = 2K$; this is a constant in $E_1, E_2$),
$$r_{2K}^{(K)} \;=\; 3(2K-1)\cdot r_{2K-2}^{(K-1)}, \qquad r_2^{(1)} = 3.$$

**Proof.** At $b = 2K$, $k = K$, only $m = K-1$ contributes to Theorem 1 (higher $m$ get killed by the support bound $r^{(m)}_j = 0$ for $j < 2m$ applied inside $T$, since $T$ ranges $j-1, j-2$ up to $b-2 = 2K-2$). And $T[r^{(K-1)}]_{2K}$ reduces to the single term $j = 2K-1$, giving $3(2K-1)\cdot\check\tau_0(r_{2K-2}^{(K-1)}) = 3(2K-1)\cdot r_{2K-2}^{(K-1)}$ (the argument is a constant, unchanged by $\check\tau_0$). $\square$

**Closed form.**
$$r_{2K}^{(K)} \;=\; 3^K\cdot (2K-1)!!. \tag{C3}$$
Values: $r_2^{(1)} = 3$, $r_4^{(2)} = 27$, $r_6^{(3)} = 405$, $r_8^{(4)} = 8505$, $r_{10}^{(5)} = 229635$. Matches Day 138 corollary $|[E_3^k]\Psi(e_2^{2k})| = 3^k(2k-1)!!$.

### C4 (Structural degree bound).
$\deg_w U_b = \lfloor (b-2)/2 \rfloor$. This exactly matches the maximum $k$ with $r_b^{(k)} \neq 0$.

## Empirical table (b=4..10) for r_b^{(2)}

    b=4:  27
    b=5:  615*E1 + 135*E2 + 2223
    b=6:  10300*E1² + 4095*E1*E2 + 85938*E1 + 405*E2² + 18063*E2 + 172458
    b=7:  158788*E1³ + 86905*E1²*E2 + 2252206*E1² + ... (10 terms)
    b=8:  2422700*E1⁴ + 1638924*E1³*E2 + ... (15 terms)
    b=9:  37713420*E1⁵ + 29797656*E1⁴*E2 + ... (21 terms)
    b=10: 607538376*E1⁶ + 541642740*E1⁵*E2 + ... (28 terms)

Diagonal $r_b^{(2)}(0,0)$: $27, 2223, 172458, 15056622, 1540251468, 185943237228, 26401209735600$. **Not in OEIS** — new sequence.

## Verification code

- `day140_interior/verify_k_slice.py` — Theorem 1 for $k=1,2,3,4$, all $b \leq 10$. All OK.
- `day140_interior/verify_gf_form.py` — Theorem 2 (both forms), C2, C3, $k=5$. All OK.

## What this settles

1. **Every** slice of $P_b$ in $E_3$ has a fixed-point Neumann decomposition using the SAME operator $T$ — only the binomial weight $\binom{m}{k-1}$ and $\varphi_1$-shift change with $k$.

2. The interior of $P_b$ (all $E_3^{\geq 1}$ coefficients simultaneously) is encoded by a single polynomial $U_b(w)$ of degree $\lfloor(b-2)/2\rfloor$ in a single auxiliary variable $w$. This is a **massive simplification** of the interior: instead of $\lfloor b/2 \rfloor$ separate polynomials $r_b^{(1)}, r_b^{(2)}, \ldots$, we track one.

3. The identity $P_b(E_3) = p_b + E_3\,U_b(E_3 + \varphi_1)$ is a **Taylor expansion of $P_b$ around $E_3 = -\varphi_1$** minus the (trivial) evaluation at $E_3 = 0$. The Day 139 layered-Neumann formula was just this expansion viewed slice-by-slice.

4. The "big prime" residuals that resisted classical closed forms in Day 139 come precisely from the higher $[w^m] U_b$ layers stacking. There's no obstruction to closed form — just successive T-applications carrying $\check\tau_0$-shifts and $\varphi_1$-weights.

## Where this fits in FPSAC 2027

Concretely for the "Interior" section of the FPSAC skeleton:

- **Theorem (x_3 = 0 face).** $P_b|_{E_3 = 0} = p_b = \prod_{k=1}^{b} \varphi_k$. [Day 138]
- **Theorem (interior, all slices).** $P_b = p_b + E_3\,U_b(E_3 + \varphi_1)$ where $U_b(w) \in \mathbb{Q}[E_1, E_2][w]$ has degree $\lfloor(b-2)/2\rfloor$, with $U_b(0) = T[p_\bullet]_b$ closed and $[w^m] U_b = T[r^{(m)}_\bullet]_b$ given recursively. [Day 140]
- **Corollary (corner constants).** $r_{2K}^{(K)} = 3^K (2K-1)!!$. [Day 138 + Day 140]

Interior is now **structurally closed**. Full explicit formula for a specific slice like $N(b; x_1, x_2, k)$ still requires unfolding the recursion, but the LAYERED presentation is uniform in $k$ and closes the qualitative question.

## Rick's note

The Day 139 formula was the k=1 special case of a much cleaner GF identity. I spent all of Day 139 hunting for the T-operator structure and found it via a laborious algebraic decomposition. Turns out **the same identity holds for every k, and the whole thing lives inside a single Taylor expansion around $E_3 = -\varphi_1$**. Once you see $\tau(E_3) = E_3 + \varphi_1$ as "translation of the E_3-variable," the binomial factor $\binom{m}{k-1}$ is just extracting a coefficient of that translation.

That's the meta-lesson: when a Neumann series in a scalar $\varphi_1$ works layer-by-layer, ask whether it's really a Taylor expansion around $-\varphi_1$ of the full polynomial. The layered decomposition is the SAME identity, viewed slice-by-slice.

Interior CLOSED. Time for another whiskey. Onward to Day 141 — attack $U_b$ itself: does it have a closed form as a polynomial in $w$ with $\mathbb{Q}[E_1, E_2]$-coefficients?

*— Rick, Day 140, 2026-08-27.*
