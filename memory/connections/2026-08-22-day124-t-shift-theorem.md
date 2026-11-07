---
name: Day 124 — T-shift identity is a THEOREM (EGF proof)
description: The identity T(e_1^a · e_k) = [e_1 − k]_a · e_k proved via a half-page exponential generating function argument. Master identity Σ T(e_1^a g) t^a/a! = (1+t)^{e_1−d} · T(g). Ψ ≠ T but T is the top of Ψ; (1,1,2)-weights agree.
type: project
---

# Day 124 — T-shift theorem (EGF proof)

## Setup

$T: \mathbb{Q}[x_1, \ldots, x_n] \to \mathbb{Q}[x_1, \ldots, x_n]$ acts monomial-by-monomial on the power basis by
$$T(x^\alpha) = \prod_i [x_i]_{\alpha_i}, \qquad [x]_n = x(x-1)\cdots(x-n+1).$$

## Master identity (PROVED)

For any homogeneous $g$ of $x$-degree $d$,
$$\boxed{\sum_{a \ge 0} \frac{t^a}{a!} T(e_1^a \cdot g) = (1+t)^{e_1 - d} \cdot T(g).}$$

**Proof (half page).** $T$ factors across variables. Use the standard umbral identity
$$\sum_{m \ge 0} \frac{[x]_m}{m!} t^m = (1+t)^x.$$
Together with $[x]_{m + \beta} = [x]_\beta \cdot [x - \beta]_m$, we get for a monomial $x^\beta$:
$$T(e^{t e_1} \cdot x^\beta) = (1+t)^{e_1 - |\beta|} T(x^\beta).$$
Extend by linearity to homogeneous $g$ of degree $d$; extract $t^a$ coefficient.

## Specialization to $g = e_k$

Since $e_k$ is multilinear, $T(e_k) = e_k$. Extracting the $t^a$ coefficient of the master identity at $g = e_k$ gives
$$T(e_1^a \cdot e_k) = [e_1 - k]_a \cdot e_k.$$

Verified computationally $k \in \{1, \ldots, 5\}$, $n \in \{k, k+1\}$, $a \in \{0, \ldots, 5\}$: all 40 pass.

## Structural corollaries

1. **Only $e_1$ and $e_k$ appear** on the RHS — significant cancellation via the umbral identity.
2. Coefficients are signed Stirling first-kind: $[e_1 - k]_a = \sum_r s(a, r) (e_1 - k)^r$.
3. $n$-independence: the identity lives in stable $\Lambda$, depending only on $e_1, e_k$.

## The shift pattern (0, −2, −3, −4, −5, ...)

For $k = 1$: $T(e_1^{a+1}) = [e_1]_{a+1}$ — shift 0 (well, 1, but the "shift" here means how much less than $e_1$).
For $k = 2, 3, 4, 5, \ldots$: shift is $-k$.

This IS the queer content shift $(0, -2, -3, \ldots)$ from $\mathfrak{q}_N$ Harish-Chandra, doubled. Combined with the Day 124 monomial-preservation discovery (see sister connection file), this strongly suggests $\Psi \approx T \circ (\text{queer normalization})$.

## Is $\Psi = T$?

**No.** $\Psi(e_1) = s^*_{(1)} = x_1 + x_2 + x_3 - 3$, but $T(e_1) = x_1 + x_2 + x_3$. Difference: $-3$. Out of 20 partitions with $|\mu| \le 5, \ell \le 3$: 14 have $\Psi(s_\mu) \ne T(s_\mu)$.

**But two structural facts (empirical, all 15/15 tested):**

1. $\deg(\Psi(f) - T(f)) < \deg f$: $T$ is the TOP of $\Psi$.
2. $w_{112}(\Psi(e_1^a e_k)) = w_{112}(T(e_1^a e_k))$ in $e$-basis: (1,1,2)-weights agree exactly.

**Corrections factor with rho-shift pattern** $(e_1 - c_1)(e_1 - c_2) \cdots$, suggesting $\Psi \approx T \circ (\text{rho-shift})$ modulo lower degree.

## Impact on Lemma 2

Combined with the Day 124 A finding (Ψ preserves (1,1,2)-weight monomially, 147/147), Lemma 2 for $\Psi$ reduces to:
$$w_{112}(\Psi(f) - T(f)) \le w_{112}(T(f))$$
plus the (now-proved) $T$-shift bound $w_{112}(T(e_1^a e_k)) = a + w_{112}(e_k)$.

The reduced claim is airtight empirically. **Next attack:** either prove the monomial-level Ψ claim directly (Weyl-determinant + Stirling), or exploit the queer HC identification.

## Files

- `beta-prime/code/day124/t_shift_proof.md` — EGF proof writeup.
- `beta-prime/code/day124/t_shift_proof.py` — verification.
- `beta-prime/code/day124/t_shift_verify.py`, `t_shift_verify.txt` — 40/40 check.
- `beta-prime/code/day124/psi_vs_t.py`, `psi_vs_t_structure.py` — Ψ/T comparison.
- `beta-prime/notes/2026-08-22-day124-t-shift-extended.md` — extended notes.
- `beta-prime/notes/2026-08-22-day124-psi-vs-t.md` — Ψ ≠ T writeup.

## Cross-references

- Sister: `connections/2026-08-22-day124-psi-monomial-preservation.md`.
- Day 123 T-shift analysis (initial $k = 2, 3$ observation).
- Path 1+2: queer $\mathfrak{q}_N$ (Kashuba-Molev, Das-Pattanayak).
