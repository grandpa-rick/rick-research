# OEIS submission draft — Day 188 (2026-09-11), for Robin (ON HOLD)

**Status.** ON HOLD until Sequence 3 ($p_k$) in
`/home/agent/projects/for-collaborator/day183/oeis-submissions.md`
has been resolved with Robin / OEIS. Ready to append as **Sequence 4** to
that submission package.

Fourth new integer sequence in Rick's path-graph CQF family:

$$\kappa_k \;=\; \text{Speicher--Nica free cumulants of the moment sequence } m_k := b_k.$$

Values agree with $a_k = \mathrm{INVERTi}(b_k)$ at $k = 1, 2$ (forced: at
$k=1$ the free / Boolean / classical cumulants all equal the mean; at
$k=2$ they all equal $m_2 - m_1^2$), then diverge from $k = 3$ onward.
$\kappa_k$ is a fourth distinct integer sequence in the family alongside
$b_k$, $a_k = \mathrm{INVERTi}(b_k)$, and $p_k$ (Lie primitive dims).

**Discovery.** Rick's Day 186 hunch: are the Speicher--Nica free cumulants
of $b_k$ equal to $a_k = \mathrm{INVERTi}(b_k)$? Answer: **no** — free
cumulants of $b_k$ are $\kappa_k$, agreeing with $a_k$ only at $k \le 2$
and differing from $k=3$ ($\kappa_3 = 228 \ne 282 = a_3$).  The hunch is
dead, but $\kappa$ is a genuinely new integer sequence, not in OEIS as of
2026-09-11.

**Caveat (formal power series only).** The Speicher--Nica moment /
free-cumulant Möbius formula
$$m_n \;=\; \sum_{\pi \in NC(n)} \prod_{V \in \pi} \kappa_{|V|}$$
is a **formal power-series identity** in $\mathbb Z[[z]]$ (equivalently
the Nica--Speicher functional equation $M(z) = 1 + K(zM(z))$).  It
determines $\kappa_k$ as an integer sequence regardless of whether the
underlying moment sequence $b_k$ corresponds to an honest probability
measure.  We do **not** claim positive-definiteness of the Hankel matrix
of $b_k$: the Hamburger moment conditions have not been checked, and are
not needed for the formal definition of $\kappa_k$.  Only the formal
power-series identity is invoked here.

---

## Sequence 4 — $\kappa_k$ (Speicher--Nica free cumulants of $b_k$)

**Data (12 terms):**

```
3, 18, 228, 3414, 57051, 1017198, 18964692, 365203998, 7207669047, 145020978804, 2963597628312, 61343252506002
```

**%N** Speicher--Nica free cumulants of the moment sequence $b_k$ (A[b_k]); the unique integer sequence $\kappa_k$ with $M(z) = 1 + K(zM(z))$, where $M(z) := 1 + \sum_{k\ge 1} b_k z^k$ and $K(z) := \sum_{k\ge 1} \kappa_k z^k$.

**%C** Equivalently, $b_n = \sum_{\pi \in NC(n)} \prod_{V \in \pi} \kappa_{|V|}$ where $NC(n)$ is the set of non-crossing partitions of $\{1, \ldots, n\}$ (Speicher--Nica moment / free-cumulant Möbius formula in free probability).

**%C** $b_k$ (A[b_k]) is defined by the algebraic identity $F(1-F)^3(3-4F) = z(3-2F)^2$ with $F(z) = \sum_{k\ge 1} b_k z^k$ (Rick Langer, Day 148 identity, 2026-08-30; unconditional proof of $F$ algebraic of degree 5 over $\mathbb Q(z)$). Hence $\kappa_k$ is a derived integer sequence attached to the same algebraic power series.

**%C** Agreement with $a_k = \mathrm{INVERTi}(b_k)$ (A[a_k]) at $k \le 2$ only: $\kappa_1 = a_1 = 3 = m_1$ and $\kappa_2 = a_2 = 18 = m_2 - m_1^2$ (the 1st and 2nd cumulants coincide for the classical, Boolean and free notions). From $k = 3$ onward they differ: $\kappa_3 = 228 \ne 282 = a_3$; $\kappa_4 = 3414 \ne 5268 = a_4$; etc.

**%C** Divisibility: $\kappa_k \equiv 0 \pmod 3$ for all $k \le 12$ (verified). Ratios $\kappa_k / 3 = 1, 6, 76, 1138, 19017, 339066, 6321564, 121734666, 2402556349, 48340326268, 987865876104, 20447750835334$. The mod-3 vanishing for $\kappa_k$ is a *formal* consequence of $b_k \equiv 0 \pmod 3$ (proved, Day 148) via the moment / free-cumulant Möbius formula: reducing that identity mod 3 gives a triangular system on $\kappa_k \bmod 3$ with vanishing forcing.

**%C** 3-adic valuations $v_3(\kappa_k)$ for $k = 1, \ldots, 12$: $1, 2, 1, 1, 3, 5, 5, 3, 1, 1, 2, 1$. The peaks $v_3(\kappa_6) = v_3(\kappa_7) = 5$ are notably higher than $v_3(b_k)$ and $v_3(a_k)$ at the same indices ($3$ and $2$ resp. at $k = 6$; $2$ and $2$ at $k = 7$). Structural explanation open.

**%C** **Caveat.** The identity above is a formal power-series identity in $\mathbb Z[[z]]$ (Nica--Speicher functional equation for the R-transform). It determines $\kappa_k$ as integers regardless of whether $b_k$ arises as the moment sequence of an honest probability measure; the Hamburger moment (positive-definiteness) conditions on the Hankel matrix of $b_k$ are not needed for the formal definition and have not been verified.

**%D** A. Nica and R. Speicher, *Lectures on the Combinatorics of Free Probability*, LMS Lecture Note Series 335, Cambridge University Press, 2006. See §11 (moment / cumulant Möbius formula, R-transform functional equation).

**%D** J. Novelli and J.-Y. Thibon, *Noncommutative geodes and Boolean/free/classical cumulants*, arXiv:2511.18366, 2025. (Places the moment / free-cumulant Möbius formula in a noncommutative-symmetric-function framework, distinct from Boolean / classical cumulants.)

**%F** Functional equation (Nica--Speicher): $M(z) = 1 + K(zM(z))$, where $M(z) = 1 + \sum_{k\ge1} b_k z^k$ and $K(z) = \sum_{k\ge1} \kappa_k z^k$.

**%F** Möbius form: $b_n = \sum_{\pi \in NC(n)} \prod_{V \in \pi} \kappa_{|V|}$, $NC(n)$ the non-crossing partitions of $\{1,\ldots,n\}$.

**%F** Inversion (small $n$):
$\kappa_1 = b_1$;
$\kappa_2 = b_2 - b_1^2$;
$\kappa_3 = b_3 - 3\,b_1 b_2 + 2\,b_1^3$;
$\kappa_4 = b_4 - 4\,b_1 b_3 - 2\,b_2^2 + 10\,b_1^2 b_2 - 5\,b_1^4$; etc. (The general formula uses the Kreweras-complement Möbius function on $NC(n)$.)

**%o** (Python/SymPy)
```python
import sympy as sp

N = 13  # compute kappa_1..kappa_{N-1}
z = sp.symbols('z')

# 1. b_k from F(1-F)^3(3-4F) = z(3-2F)^2, via series inversion.
b_syms = sp.symbols('b1:13')
F = sum(b_syms[i] * z**(i+1) for i in range(N-1))
diff = sp.expand(sp.series(F*(1-F)**3*(3-4*F) - z*(3-2*F)**2, z, 0, N).removeO())
b_vals = {}
for k in range(1, N):
    c = sp.Poly(diff, z).coeff_monomial(z**k).subs(b_vals)
    b_vals[b_syms[k-1]] = sp.solve(c, b_syms[k-1])[0]
b = [1] + [int(b_vals[b_syms[k-1]]) for k in range(1, N)]

# 2. Solve M(z) = 1 + K(z*M(z)) for kappa_1..kappa_{N-1}.
M = sum(b[k] * z**k for k in range(N))
k_syms = sp.symbols('k1:13')
u = sp.Symbol('u')
K_of_u = sum(k_syms[i] * u**(i+1) for i in range(N-1))
K_ser = sp.expand(sp.series(K_of_u.subs(u, z*M), z, 0, N).removeO())
kappa_vals = {}
for k in range(1, N):
    c = sp.Poly(K_ser, z).coeff_monomial(z**k).subs(kappa_vals)
    kappa_vals[k_syms[k-1]] = sp.solve(sp.Eq(c, b[k]), k_syms[k-1])[0]
print([int(kappa_vals[k_syms[i]]) for i in range(N-1)])
# [3, 18, 228, 3414, 57051, 1017198, 18964692, 365203998,
#  7207669047, 145020978804, 2963597628312, 61343252506002]
```

**%Y** Cf. A[b_k] (moment sequence; algebraic OGF, degree 5). This sequence is $\kappa$ = free-cumulant transform of A[b_k] in the Speicher--Nica sense.

**%Y** Cf. A[a_k] = INVERTi(b_k) (Boolean-cumulant / free-generator counts). $\kappa_k \ne a_k$ for $k \ge 3$; they agree only at $k = 1, 2$.

**%Y** Cf. A[p_k] (Lie-primitive dimensions of the FGCCHA with dimension sequence $b_k$; graded Witt formula from $b_k$).

**%Y** Cf. arXiv:2505.06941 (Andrews--Gagnon--Gélinas--Schlums--Zabrocki, Hopf-algebra framework for INVERTi).

**%Y** Cf. arXiv:2511.18366 (Novelli--Thibon, noncommutative-symmetric-function framework distinguishing Boolean / free / classical cumulants).

**%K** nonn,hard,new

---

## Provenance (Rick's private notes)

- $\kappa_k$ discovered Day 186 (2026-09-10), first five terms computed
  in `/home/agent/projects/proofs/scripts/day186/free_cumulant_test.py`
  as diagnostic output of a **refuted** hunch (free cumulants of $b_k$
  were conjectured to equal $a_k$; they don't).
- $\kappa_k$ extended to $k = 12$ Day 188 (2026-09-11) in
  `/home/agent/projects/proofs/scripts/day188/kappa_extended.py`.
- $b_k$ recomputed by series-inversion of the Day 148 algebraic identity;
  matches the 12-term list in
  `/home/agent/projects/for-collaborator/day183/oeis-submissions.md`.
- $\kappa_k$ mismatch with $a_k$ at $k = 3$ ($228$ vs $282$) rules out
  the FGCCHA-free-generator-counts interpretation.
- OEIS non-inclusion re-confirmed 2026-09-11 (sequence begins
  `3, 18, 228, 3414` — no OEIS hits).
- Trust grade: **computed** (single SymPy script, values reproduced from
  Rick's Day 186 script at $k \le 5$).

## Reason for hold

Robin is currently resolving Sequence 3 ($p_k$) with OEIS (Day 183
submission package). Do not send $\kappa_k$ until:

1. $p_k$ submission is accepted (or the family gets a batch A-number
   block), and
2. Rick sober-verifies $\kappa_k$ values via an independent Möbius-formula
   direct computation (script exists as diagnostic in
   `/home/agent/projects/proofs/scripts/day186/free_cumulant_test.py`
   but only through $k = 5$).

Optional stretch: check whether $\kappa_k$ has a closed algebraic form
via the R-transform of $M(z)$; if $F$ is algebraic of degree 5, then $K$
is algebraic (possibly of higher degree) — worth a Groebner-basis
computation before submitting.
