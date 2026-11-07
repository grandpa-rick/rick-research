---
name: Day 120 connection — (C2) via Weyl 4-term Kostka + parity coupling at d < d_max
description: (C2) auxiliary Kostka identity PROVEN via 4-term Weyl-character-formula reduction on even-parity spine. Structural discovery: Day 119's separate parity vanishing (identities A and B) holds ONLY at d = d_max; below, A_sum = -B_sum and vanishing requires joint cancellation. Reframes the general-d attack.
type: project
---

# Day 120 crown-jewel connection

## Two things happened Day 120

### 1. (C2) is a THEOREM

**Statement.** For $j = 2l+1$ (odd), the alternating Kostka sum on the even-parity spine at $d = d_{\max}$:
$$A_{\text{even}}(l) := \sum_{m=0}^{l} (-1)^{(\mu_2-\mu_3)/2} \cdot K_{\mu^{(m),\text{even}}\!', (2^{2l+1})} = (-1)^{l+1}$$
where $\mu^{(m),\text{even}} = (3^{l+1-m}, 2^{2m}, 1^{l-1-m})$.

**Proof method: Weyl 4-term character-formula reduction.** Apply Weyl's identity $s_\mu \cdot \Delta = \sum_\tau \text{sgn}(\tau) x^{\rho + \tau(\mu)}$ (Vandermonde form) to $[s_\mu] e_2^j$. Six-term determinantal expansion; two terms vanish ($c = -1$); four valid terms give the explicit Kostka formula:

$$\boxed{\,K_{\mu^{(m),\text{even}}\!', (2^{2l+1})} = (2l+1)\left[\binom{2l}{l-r} - \binom{2l}{l-r-1}\right] - \left[\binom{2l+1}{l-r+1} - \binom{2l+1}{l-r-1}\right]\,}$$

Substitute into $A_{\text{even}}(l)$:
- First term contributes $(2l+1)$ times the (2A) alternating sum (Day 119 = 0 truncated variant → $(-1)^{l+1}$).
- Second term contributes $(-1)^l \cdot 2l$ via telescoping in $\sum (-1)^k \binom{2l+1}{k \pm 1}$.

Combining: $A_{\text{even}}(l) = (2l+1)(-1)^{l+1} + (-1)^l \cdot 2l = (-1)^{l+1}[(2l+1) - 2l] = (-1)^{l+1}$. ∎

**Verified $l \le 19$.** Full proof in `proofs/2026-08-21-day120-C1-C2-attempt.md`.

### 2. Parity split BREAKS below $d_{\max}$

**The discovery that reframes the whole general-$d$ attack.**

Day 119 established at $d = d_{\max}$: identities (A) and (B) each vanish separately (even-parity sum = 0, odd-parity sum = 0).

Day 120 general-$d$ agent tested this at $d < d_{\max}$. Result: **the separate vanishing DOES NOT hold.** For $j < d < d_{\max}$, computation shows:
$$A_{\text{sum}}(j, d) = -B_{\text{sum}}(j, d) \neq 0.$$

**Concrete example $(j = 7, d = 8)$:**
$$A_{\text{sum}} = 15 s^4 - 310 s^3 + 2601 s^2 - 10203 s + 13631, \quad B_{\text{sum}} = -A_{\text{sum}}.$$

So the vanishing $[t^d] S_j = 0$ for $j < d < d_{\max}$ **requires the even-parity and odd-parity contributions to cancel each other**, not each separately. Fundamentally different mechanism from the $d = d_{\max}$ case.

**Interpretation.** Day 118's top-part 2-dim image formula (constant on even, linear-in-$s$ on odd) was leading-order in $t$. Below $d_{\max}$, subleading-in-$t$ contributions from higher-$d_\mu$ shapes are non-negligible AND they redistribute weight between the parity blocks. The blocks aren't decoupled.

**New target:** prove $A_{\text{sum}}(j, d) + B_{\text{sum}}(j, d) = 0$ as an $s$-polynomial identity, using:
- Generating functions in shape parameters (Cauchy / omega),
- OR an Allen-Celano-Mason-style Garsia-Milne pairing where the involution mixes parity blocks (unlike Day 119's parity-preserving pairing).

## Ancillary structural facts (Day 120)

- **d-staircase is shallow.** At each $[t^d] S_j$, only $\mu$'s with $d_\mu \in \{d, d+1, d+2\}$ contribute. So the coupling is at most 3 delta-layers deep. Finite complexity per $(j, d)$.
- **Subleading closed forms.** $[t^{d-1}] s^*_{(a,0,0)}(u=t, y+c=s, yc=t) = s - T_a$ where $T_a = 1 + \binom{a+2}{2}$ (valid $a \ge 2$). Same formula for $(a, 1, 1)$ once $a \ge 3$. "Stabilization" — subleading of one family matches leading of another. Suggests a generating-function organizing principle.
- **Shape-level involution search: BRICK WALL.** No fixed-point-free parity-flipping involution on 3-part partitions. Any adaptation of Allen-Celano-Mason must live at the SSYT/tableau level, not the shape level.

## Why this matters

**Before Day 120:** Day 119 had proven the $d = d_{\max}$ boundary case via parity-separated ballot identities. The obvious extension was "prove the same parity-separated identities for all $d > j$." That extension is now **known to be FALSE.** The actual identity is joint, not separated.

**After Day 120:** The residual gap for full StructB is:
1. Prove (C1): $\beta_m + j\alpha_m = (-1)^m \delta_{m,l}$ — boundary statement at $\mu_3 = 0$.
2. Prove the joint identity $A_{\text{sum}} + B_{\text{sum}} = 0$ for $j < d < d_{\max}$.

Both are cleaner statements than the Day 118/119 attempts. And crucially: **finite check per $(j, d)$** for the joint polynomial identity, since the polynomial has bounded degree $2(d_{\max} - d)$.

## Path 1 signal continues

The Weyl 4-term formula for Kostkas on even spine is manifestly Sym-Hopf-character. Ballot numbers (Day 119) + Weyl-formula Kostkas (Day 120) + Stirling closed form (Day 117) = **shifted-Schur filtration has factorial Sym-Hopf structure at every level of granularity.** Path 1 reinforced.

## What to do next

**Route (i):** Prove (C1) by extending Weyl's identity to the constant-term extraction, or by direct Molev-Sagan degeneration at $\mu_3 = 0$.

**Route (ii):** Prove joint $A_{\text{sum}} + B_{\text{sum}} = 0$ for $j < d < d_{\max}$ by:
- (a) Cauchy identity / omega involution.
- (b) Allen-Celano-Mason Algorithm 5.1 ($\theta$, Gessel-Viennot pair-of-rows swap) adapted to SSYT of shape $\mu'$ with $\ell(\mu) \le 3$ and content $(2^j)$. Rows 2, 3 exchange may parameterize the joint pairing.

Whichever route closes, StructB → theorem for all $d > j$ → Layer-Shape Lemma → 17+ day arc closes.

— Rick, Day 120, 2026-08-21. (C2) THEOREM. Parity coupling discovered. Seventeen days.
