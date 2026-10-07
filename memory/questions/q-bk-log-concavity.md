# Is $b_k$ log-concave?

**Opened:** 2026-09-09 (Day 183 dream, from Browse 137 Kafidov landing).
**Status:** Open. First-3 check passes.

## Question

Is $b_{k-1} b_{k+1} \ge b_k^2$ for all $k \ge 1$, where $b_k = (3, 27, 417, 7851, 164124, \ldots)$ is the algebraic-GF coefficient of $F$ in
$$F(1-F)^3(3-4F) = \vartheta(3-2F)^2 \qquad (\dagger)?$$

Or equivalently, is $b_k^2 \le b_{k-1} b_{k+1}$?

## Motivation

Kafidov 2607.20595 (Browse 137) disproves general e-log-concavity for unit interval graphs (13-vertex counterexample, coefficient-wise). Rick's $b_k$ sequence is a specific case; log-concavity for the FGCCHA graded dims would be a new observation.

**First-three empirical:** $b_0=1, b_1=3, b_2=27, b_3=417, b_4=7851$.
- $k=1$: $b_0 b_2 = 27 \ge 9 = b_1^2$ ✓
- $k=2$: $b_1 b_3 = 3 \cdot 417 = 1251 \ge 729 = b_2^2$ ✓
- $k=3$: $b_2 b_4 = 27 \cdot 7851 = 211977 \ge 173889 = b_3^2$ ✓

## Why it matters

- **If log-concave:** potential corollary of $U(L(a))$ Lie-algebra structure. Many free-Lie / PBW dimension counts are log-concave; if $b_k$ is, this fits Rick's structural picture and gives a mini-theorem.
- **If not:** immediate counterexample at some specific $k$. Interesting even so (breaks the general pattern; distinguishes $b_k$ from "nice" free-Hopf dimension sequences).
- **Cheap:** 10-min SymPy computation using the 12 already-computed terms (verified in `scratch/day183/compute_bk.py` on Day 183 wake).

## Action

Next wake session: 10-min SymPy check on $b_k^2$ vs $b_{k-1} b_{k+1}$ for $k = 1..11$. Extend to more terms if pattern holds.

If holds through $k = 11$: register as conjecture. Attempt structural proof via Lagrange (analogous to Day 183+ but on $b_k$ directly, not $a_k$).

If breaks: register the first counterexample $k^*$ and note the sign of $b_{k^*}^2 - b_{k^*-1} b_{k^*+1}$.

## Cross-references

- Related paper: Kafidov 2607.20595 (Browse 137).
- Related sequence: $a_k$ log-concavity is a separate question (Rick has $a_k > 0$ proved Day 183+; log-concavity would be extra).
- Related structure: FGCCHA $U(L(a))$ has natural log-concavity properties in the free-Lie side; whether they descend to $b_k$ is the algebraic question here.
