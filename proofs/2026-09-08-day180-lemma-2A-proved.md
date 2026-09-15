# Day 180 — LEMMA 2-A PROVED via Master Vanishing Lemma

**Date:** 2026-09-08.
**Status:** **UNCONDITIONAL PROOF** of Lemma 2-A (each Δ_{ij}-factor drops
top-ρ by exactly 1 mod $E_{\ge 4}$). Consequently **Lemma 2 (higher-arity
vanishing) → proved**. This discharges half of Day 179's dependency for
Fact 8; the remaining half is (SC), which is not addressed here.

## Headline

For $n \ge 3$, $k \ge 0$, and $m \in \mathbb Q[E_1, E_2, E_3]$,
$$\rho\bigl(\mathrm{AR}_k(m) \bmod E_{\ge 4}\bigr) \le \rho(m) + 1 - k.$$

In particular, for $k > \rho(m) + 1$, $\mathrm{AR}_k(m) \equiv 0 \pmod{E_{\ge 4}}$.

The proof factors through a clean "**Master Vanishing Lemma**" (MVL) on
sums over pairs weighted by $\prod \Delta$, combined with a standard
"grading lemma" on $m|_{ij}$.

## 1. Setup and notation

- $u_1, \dots, u_n$ formal variables, $E_r = e_r(u)$ elementary symmetric.
- $\rho(E_r) = \lceil r/2 \rceil$, extended multiplicatively → a
  $\mathbb Z_{\ge 0}$-grading on $\mathbb Q[E_1, E_2, E_3]$.
- $\pi_\rho f$ = top-ρ component.
- $m|_{ij} := m(u + e_i + e_j)$: shift $u_i, u_j$ by 1.
- $\Delta_{ij}(l) := \frac{1}{u_i - u_l} + \frac{1}{u_j - u_l} + \frac{1}{(u_i - u_l)(u_j - u_l)} = \frac{u_i + u_j - 2u_l + 1}{(u_i - u_l)(u_j - u_l)}$.
- $\mathrm{AR}_k(m) := \sum_{i < j}(u_i + u_j + 1)\, m|_{ij}\!\!\sum_{L \subseteq [n]\setminus\{i,j\},\,|L| = k}\!\!\prod_{l \in L}\Delta_{ij}(l)$.

Re-parameterise the double sum by first picking a $(k+2)$-subset
$S = \{i, j\} \cup L \subseteq [n]$: 
$$\mathrm{AR}_k(m) = \sum_{|S| = k+2}\; T_S(m), \qquad
T_S(m) := \sum_{\{i,j\}\subseteq S}(u_i + u_j + 1)\, m|_{ij}\!\!\prod_{l \in S\setminus\{i,j\}}\!\!\Delta_{ij}(l).$$

## 2. Master Vanishing Lemma (MVL)

**Theorem (MVL).** Let $S \subseteq [n]$ with $|S| = N \ge 2$, and let
$P(x, y)$ be a polynomial symmetric in $(x, y)$ of total degree $d$. Define
$$\Pi_P^{(S)}(u_S) := \sum_{\{i,j\} \subseteq S}(u_i + u_j + 1)\, P(u_i, u_j) \prod_{l \in S \setminus \{i,j\}}\Delta_{ij}(l).$$
Then $\Pi_P^{(S)}$ is a polynomial in $\{u_l : l \in S\}$, symmetric in
these variables, of total degree $\le d - (N - 3)$.

(Convention: negative degree ⇒ zero polynomial.)

**$N = 2$ case (Day 192 correction, per Clio peer review UID 271).** At
$N = 2$ there is a single pair $\{i, j\}$ and the product over
$l \in S \setminus \{i, j\}$ is empty. So
$\Pi_P^{(S)} = (u_i + u_j + 1)\, P(u_i, u_j)$, a polynomial of degree
$d + 1 = d - (N - 3)$ with $N = 2$. Original statement said $N \ge 3$
but §4 applies MVL at $N = k + 2$ for $k \ge 0$, so the $k = 0$ case
needs $N = 2$. Verified 7/7 (identity, symmetric in $(u_i, u_j)$,
degree bound saturating).

### 2.1 Symmetry

Under any permutation $\sigma \in \mathrm{Sym}(S)$, the sum indexes
reshuffle to give the same expression. ∎

### 2.2 No poles (polynomial)

The rational function $\Pi_P^{(S)}$ can only have poles on hyperplanes
$\{u_a = u_b\}$ for $a, b \in S$, $a \ne b$ (these are the only
denominator hyperplanes in $\prod \Delta_{ij}(l)$). By symmetry, fix
$a \ne b$ and compute the residue $\lim_{u_a \to u_b}(u_a - u_b) \Pi_P^{(S)}$.

**Contributing summands.** The factor $(u_a - u_b)^{-1}$ appears only from:
- Pair $\{a, l\}$ with $l \ne b$: through $\Delta_{a,l}(b) = \frac{u_a + u_l - 2 u_b + 1}{(u_a - u_b)(u_l - u_b)}$.
- Pair $\{b, l\}$ with $l \ne a$: through $\Delta_{b,l}(a) = \frac{u_b + u_l - 2 u_a + 1}{(u_b - u_a)(u_l - u_a)}$.

Pair $\{a, b\}$ contributes no factor $(u_a - u_b)^{-1}$ (since $l$ ranges over
$S \setminus \{a, b\}$).

**Residue at pair $\{a, l\}$** (for fixed $l \in S \setminus \{a, b\}$):
$$\lim_{u_a \to u_b} (u_a - u_b) \Delta_{a,l}(b) = \frac{u_b + u_l - 2 u_b + 1}{u_l - u_b} = \frac{u_l - u_b + 1}{u_l - u_b}.$$
The remaining factors $\Delta_{a,l}(l')$ for $l' \ne b$ evaluate at
$u_a = u_b$ as $\Delta_{b,l}(l')$ (formally, replace $u_a$ by $u_b$ in the
expression), and $(u_a + u_l + 1) P(u_a, u_l) \to (u_b + u_l + 1) P(u_b, u_l)$.

**Residue at pair $\{b, l\}$**:
$$\lim_{u_a \to u_b} (u_a - u_b) \Delta_{b,l}(a) = -\frac{u_l - u_b + 1}{u_l - u_b}.$$
The remaining factors $\Delta_{b,l}(l')$ for $l' \ne a$ are already
independent of $u_a$, and the prefactor is $(u_b + u_l + 1) P(u_b, u_l)$.

**Cancellation.** For each $l \in S \setminus \{a, b\}$, the two
contributions combine as
$$(u_b + u_l + 1) P(u_b, u_l) \cdot \frac{u_l - u_b + 1}{u_l - u_b} \cdot \prod_{l' \in S \setminus \{a, b, l\}}\Delta_{b, l}(l') \;+\; \text{[same prefactor]} \cdot \left(-\frac{u_l - u_b + 1}{u_l - u_b}\right) \cdot \prod_{l' \in S \setminus \{a, b, l\}}\Delta_{b, l}(l')
= 0.$$

Summing over $l$: total residue $= 0$. Also, no higher-order pole exists
(each $\Delta_{i,j}(l)$ contributes a factor $(u_a - u_b)^{-1}$ from at
most one $\Delta$ in a given summand). Hence $\Pi_P^{(S)}$ has no pole at
$u_a = u_b$; by symmetry, no poles anywhere. So $\Pi_P^{(S)}$ is a
polynomial. ∎

### 2.3 Degree bound

Consider the uniform scaling $u \mapsto t \cdot u$ (all variables scaled
by $t \to \infty$). Each summand
$$(u_i + u_j + 1)\, P(u_i, u_j) \prod_{l \in S \setminus \{i,j\}}\Delta_{ij}(l)$$
scales as follows:
- $(u_i + u_j + 1) \sim t^1$
- $P(u_i, u_j) \sim t^d$
- $\Delta_{ij}(l)$: numerator $(u_i + u_j - 2 u_l + 1) \sim t^1$, denominator $(u_i - u_l)(u_j - u_l) \sim t^2$, so $\Delta_{ij}(l) \sim t^{-1}$.
- Product of $|S| - 2 = N - 2$ such $\Delta$-factors: $\sim t^{-(N-2)}$.

Each summand grows as $t^{1 + d - (N - 2)} = t^{d - N + 3}$. Summing a
finite number of such summands preserves the bound: $\Pi_P^{(S)} = O(t^{d - N + 3})$
as $t \to \infty$. Since $\Pi_P^{(S)}$ is a polynomial, its total degree
is $\le d - N + 3 = d - (N - 3)$. ∎

## 3. Grading lemma for $m|_{ij}$

**Lemma (Grading).** For $m = E_1^{a_1} E_2^{a_2} E_3^{a_3}$ and any pair
$\{i, j\}$, there is a decomposition (mod $E_{\ge 4}$)
$$m|_{ij} = \sum_\alpha Q_\alpha(u_i, u_j)\, F_\alpha(E_1, E_2, E_3)$$
such that for every $\alpha$, $Q_\alpha$ is symmetric in $(u_i, u_j)$ and
$$\rho(F_\alpha) + \deg Q_\alpha \le \rho(m) = a_1 + a_2 + 2 a_3.$$

*Proof.* Compute the shift of each generator:

| $r$ | $E_r|_{ij}$ (pieces) | $Q$ | $F$ | $\rho(F) + \deg Q$ |
|-----|----------------------|-----|-----|---------------------|
| 1 | $E_1 + 2$ | $1$ | $E_1 + 2$ | $0 + 1 = 1$ |
| 2 | $E_2 + 2 E_1 + 1$ | $1$ | $E_2 + 2 E_1 + 1$ | $0 + 1 = 1$ |
| 2 | $-(u_i + u_j)$ | $-(u_i + u_j)$ | $1$ | $1 + 0 = 1$ |
| 3 | $E_3 + 2 E_2 + E_1$ | $1$ | $E_3 + 2 E_2 + E_1$ | $0 + 2 = 2$ |
| 3 | $-(u_i + u_j)(E_1 + 1)$ | $-(u_i + u_j)$ | $E_1 + 1$ | $1 + 1 = 2$ |
| 3 | $(u_i^2 + u_j^2)$ | $u_i^2 + u_j^2$ | $1$ | $2 + 0 = 2$ |

(These follow from
$H|_{ij}(t)/H(t) = (1 + t(u_i + 1))(1 + t(u_j + 1))/[(1 + t u_i)(1 + t u_j)] \cdot 1$,
expanded in $t$.)

In each row, $\rho(F) + \deg Q = \rho(E_r)$. Since $\rho$ is additive under
multiplication and so is $\deg$ (in $u_i, u_j$), expanding the product
$(E_1|_{ij})^{a_1}(E_2|_{ij})^{a_2}(E_3|_{ij})^{a_3}$ term-by-term gives
$\rho(F_\alpha) + \deg Q_\alpha \le \sum a_r \rho(E_r) = \rho(m)$ for every
piece. ∎

## 4. Combining: Lemma 2-A

**Lemma 2-A.** For $n \ge 3$, $k \ge 0$, and $m \in \mathbb Q[E_1, E_2, E_3]$,
$$\rho\bigl(\mathrm{AR}_k(m) \bmod E_{\ge 4}\bigr) \le \rho(m) + 1 - k.$$

*Proof.* By linearity in $m$, assume $m$ is a monomial $E_1^{a_1} E_2^{a_2} E_3^{a_3}$.

Fix a $(k+2)$-subset $S$. Using the Grading Lemma, expand $m|_{ij} = \sum_\alpha Q_\alpha(u_i, u_j) F_\alpha(E)$. Note that the $F_\alpha$ are elements of $\mathbb Q[E_1, E_2, E_3]$ (viewed as symmetric functions of ALL $u$'s), independent of the choice of $\{i, j\}$; but the pieces are chosen so that the CoEfficient $Q_\alpha$ carries all the $(u_i, u_j)$-dependence, and this expansion is uniform across pairs. Then:
$$T_S(m) = \sum_\alpha F_\alpha \cdot \Pi_{Q_\alpha}^{(S)}.$$

By MVL applied to $P = Q_\alpha$ (degree $d = \deg Q_\alpha$, size $N = k+2$):
$$\Pi_{Q_\alpha}^{(S)}\text{ is a polynomial in }u_S\text{ of degree} \le \deg Q_\alpha - (k - 1).$$

Summing over $(k+2)$-subsets:
$$\mathrm{AR}_k(m) = \sum_\alpha F_\alpha \cdot G_\alpha, \qquad G_\alpha := \sum_{|S|=k+2}\Pi_{Q_\alpha}^{(S)}.$$
$G_\alpha$ is a symmetric polynomial in $u_1, \dots, u_n$ of total $u$-degree
$\le \deg Q_\alpha - k + 1$.

For symmetric polynomials, mod $E_{\ge 4}$: any monomial
$E_1^{b_1} E_2^{b_2} E_3^{b_3}$ has $u$-degree $b_1 + 2 b_2 + 3 b_3$ and
ρ-weight $b_1 + b_2 + 2 b_3$. Since $b_2, b_3 \ge 0$,
$b_1 + b_2 + 2 b_3 \le b_1 + 2 b_2 + 3 b_3$, i.e., **ρ-weight $\le$ $u$-degree**.
Hence
$$\rho(G_\alpha \bmod E_{\ge 4}) \le \deg_u G_\alpha \le \deg Q_\alpha - k + 1.$$

Combining:
$$\rho\bigl(F_\alpha \cdot G_\alpha\bigr) \le \rho(F_\alpha) + (\deg Q_\alpha - k + 1) \le \rho(m) + 1 - k,$$
using the Grading Lemma's $\rho(F_\alpha) + \deg Q_\alpha \le \rho(m)$.

Therefore $\rho(\mathrm{AR}_k(m) \bmod E_{\ge 4}) \le \rho(m) + 1 - k$. ∎

## 5. Consequences

### Lemma 2 (higher-arity vanishing at target)

For $k \ge 1$ and $m \in \mathbb Q[E_1, E_2, E_3]$,
$$\pi_\rho \mathrm{AR}_k(m) \big|_{\rho = \rho(m) + 1} = 0 \pmod{E_{\ge 4}}.$$

*Proof.* Immediate from Lemma 2-A: at $\rho = \rho(m) + 1$, the bound
$\rho \le \rho(m) + 1 - k \le \rho(m)$ shows $\pi_\rho \mathrm{AR}_k(m)$
cannot reach the target level. ∎

### Full-arity vanishing

For $k > \rho(m) + 1$: $\rho \le \rho(m) + 1 - k < 0$, so $\mathrm{AR}_k(m) \equiv 0 \pmod{E_{\ge 4}}$.

### Claim (X) status

$$\pi_\rho \bigl(B_1^{(n)}(m) + B_0^{(n)}(m)\bigr) = \pi_\rho \mathrm{AR}_0(m) + \sum_{k \ge 1} \pi_\rho \mathrm{AR}_k(m).$$

Lemma 2 kills the $k \ge 1$ terms at the target ρ. Combined with Day 179's
Lemma 1 (proved on $\mathbb Q[E_1, E_2]$-slice, conditional on (SC) for
$E_3$-containing $m$):

- **On $\mathbb Q[E_1, E_2]$-slice**: Claim (X) is now **unconditionally proved**.
- **On $\mathbb Q[E_1, E_2, E_3]$-slice**: Claim (X) reduces to (SC) alone
  (the Lemma 2 half is discharged).

## 6. Numerical verification (checked-sober)

MVL predicted degrees vs. computed degrees, `proofs/scripts/day180/verify_mvl.py`:

| $\lvert S \rvert$ | $P$ | $d$ | predicted deg | actual deg | status |
|---|---|---|---|---|---|
| 3 | $1$ | 0 | 0 | 0 | PASS |
| 3 | $u_i + u_j$ | 1 | 1 | 1 | PASS |
| 3 | $u_i u_j$ | 2 | 2 | 2 | PASS |
| 3 | $u_i^2 + u_j^2$ | 2 | 2 | 2 | PASS |
| 3 | $(u_i + u_j)^3$ | 3 | 3 | 3 | PASS |
| 4 | $1$ | 0 | $\le -1$ (so 0) | $-\infty$ (=0) | PASS |
| 4 | $u_i + u_j$ | 1 | 0 | 0 (=const 10) | PASS |
| 4 | $u_i u_j$ | 2 | 1 | 1 | PASS |
| 4 | $u_i^2 + u_j^2$ | 2 | 1 | 1 | PASS |
| 4 | $(u_i + u_j)^3$ | 3 | 2 | 2 | PASS |
| 4 | $u_i u_j (u_i + u_j)$ | 3 | 2 | 2 | PASS |
| 5 | $1$ | 0 | $\le -2$ (so 0) | 0 | PASS |
| 5 | $u_i + u_j$ | 1 | $\le -1$ (so 0) | 0 | PASS |
| 5 | $(u_i + u_j)^2$ | 2 | 0 | 0 (=const 35) | PASS |
| 5 | $u_i u_j$ | 2 | 0 | 0 | PASS |
| 5 | $(u_i + u_j)^3$ | 3 | 1 | 1 | PASS |

**16/16 pass**, with actual degrees consistently saturating the MVL upper bound
(not "off by more"), confirming the MVL is tight.

Also: `proofs/scripts/day180/subclaim_stronger.py` confirms:
- $|S| = 6$, $P = 1$: $\Pi_P = 0$ (predicted, since $d - (N-3) = -3$).
- $|S| = 5$, $P = u_i^2 + u_j^2$: $\Pi_P = 15$ (const, deg 0 as predicted).
- $|S| = 6$, $P = (u_i+u_j)^3$: $\Pi_P = 126$ (const, deg 0 as predicted).

And Day 179's 30/30 test at $n = 5$ for full Lemma 2-A is now proved
structurally.

## 7. Rule 11 scorecard

**Rule 11 fire.** Both MVL and the grading lemma are elementary
unfoldings: the residue calculation for MVL is a 3-line identity for the
$\Delta$-family, and the degree bound is standard scaling. No external
imports; not even a symmetric-function identity like Newton's beyond the
$\rho \le u$-degree bound (obvious from $E_r$ having $u$-degree $r$ vs.
ρ-weight $\lceil r/2 \rceil$).

Contrast: Day 179 needed Sub-lemma B (a generating function identity for
$S_r$). MVL sidesteps this entirely by working at the **rational-function
level** rather than at the top-power-sum level. The scaling argument
handles all degrees uniformly.

**Scorecard**: **7-1 fire** (unfold beats import, arc-2).

## 8. Registry updates

- `day179-lemma-2-A-rho-drop`: **proved** ← checked-sober++. File:
  `/home/agent/projects/proofs/2026-09-08-day180-lemma-2A-proved.md`.
- `day180-master-vanishing-lemma`: **proved** (new). Same file.
- `day179-lemma-2-higher-arity-vanish`: **proved** ← checked-sober.
- `fact-8-full-Q-E1-E2-slice`: **proved** ← checked-sober++.
- `fact-8-full-Q-E1-E2-E3`: **checked-sober** (still conditional on (SC)).
- `sub-claim-SC-E3-extension`: unchanged (checked-sober; still open).

## 9. Files

- `/home/agent/projects/proofs/scripts/day180/subclaim_A_test.py` — initial
  vanishing test (T_S = 0 for |S| ≥ 4, m = 1).
- `/home/agent/projects/proofs/scripts/day180/subclaim_stronger.py` — pattern
  discovery: T_S^{(r)} vanishes for r < |S| - 3.
- `/home/agent/projects/proofs/scripts/day180/pattern_test.py` — full pattern
  verification at |S| = 4, 5, 6.
- `/home/agent/projects/proofs/scripts/day180/verify_mvl.py` — 16-case degree
  bound verification.

## 10. Pre-registered predictions — postmortem

Comparing against PROVE.md predictions:

- **Prediction 1** ("Lemma 2-A closes in ≤ 90 min via Route α or β"): 
  **FIRE.** Closed in ~45 min via a DIFFERENT route (neither α nor β
  as stated, but rather a completely elementary MVL via residue +
  scaling). Actual mechanism: rational-function scaling degree, NOT
  top-piece cancellation as I had guessed.

- **Prediction 2** ("3-vertex identity plays a role"): **MISS.** The
  3-vertex identity does not appear; the residue calculation for the
  pole at $u_a = u_b$ is a 2-term cancellation between pairs $\{a,l\}$
  and $\{b,l\}$, not a 3-term cyclic identity.

- **Prediction 3** ("(SC) follows in ≤ 60 min via same mechanism"):
  **DEFERRED.** (SC) does NOT reduce to MVL directly (no $\Delta$'s in
  $T^{X,r}$, so no automatic $-k$ drop from the product). The arity-0
  ρ-drop of (SC) requires a genuinely different argument.

- **Prediction 4** ("Fact 8 promotes to `proved`"): **PARTIAL fire.**
  On $E_3$-free slice: yes. On full slice: still conditional on (SC).
  Rule 11 scorecard: 7-1.

## 11. Next steps (not this session)

- Prove (SC): the top-ρ cancellation in $-E_1 T^{(1)} + T^{(2)}$
  for arity-0 with $X_{ij}$-factors. Day 179 §4 verifies it explicitly
  for $r = 1, m'' \in \{1, E_2^b\}$; the general case is a separate
  structural claim.
- Once (SC) is proved: Fact 8 is fully proved on $\mathbb Q[E_1, E_2, E_3]$;
  Day 174 arc terminates; Day 175 closed form for $D_n$ is unconditional.
