# FPSAC 2027 Extended Abstract — Day 146 Addendum

**Status:** Day 146 (2026-08-29). Writing kickoff Sept 1 (in 2 days).
Skeleton `skeleton.md` was written Days 133/134; needs additions for
Days 141/143/145 results and REVISED §5 framing given Day 146 negatives.

## Additions to §3 (Day 131-133 base + Days 141/143/145 extensions)

### §3.5 (NEW) — Interior of $P_b$: leading closed form for $U_b(w)$ (Day 141)

**Theorem 3.6 (VERBATIM Day 141).** In P-frame coordinates $(U, V) = (u+1, v+1)$
with $E_1 = u+v$, $E_2 = uv$:
$$P_b = p_b + E_3 \cdot U_b(E_3 + \varphi_1), \qquad p_b := \prod_{k=1}^{b} \varphi_k.$$
The polynomial $U_b(w)$ has degree $\lfloor (b-2)/2 \rfloor$ and leading coefficient
$$[U^{b-2k} V^{b-2k}] r_b^{(k)} = 3^k (2k-1)!! \binom{b}{2k}.$$

**EGF form of leading part:**
$$F_P^{\text{top-in-UV}}(T) = f(T; U, V) \cdot \exp(\tfrac{3}{2} E_3 T^2), \quad f := \sum_b (U)_b (V)_b T^b/b!.$$

**Corollary:** the corner $r_{2K}^{(K)} = 3^K (2K-1)!!$ (unifying Day 138's
pure-$E_3$ corner as one-term instance).

Files: `proofs/2026-08-28-day141-ub-closed-partial.md`.

### §3.6 (NEW) — Quadratic identity for the universal invariant (Day 143)

**Theorem 3.7 (VERBATIM Day 143).** Define $a_k := [E_3^k T^{3k-1}] X$ where
$X$ is the RHS of the Frobenius identity $L F_P = F_P X$ (Day 142). Then
$$a_k = -b_k + \sum_{i + j = k, \; i, j \ge 1} b_i b_j$$
where $b_k := (3k-1) \cdot [T^{3k-1}] N_k(T)$, $N_k(T) := [E_3^k] \log(F_P/f)$.

**Equivalently:** if $A(\tau) := \sum a_k \tau^k$ and $F(\tau) := \sum b_k \tau^k$,
then in $\mathbb{Q}[[\tau]]$:
$$(1 - 2 F(\tau))^2 = 1 + 4 A(\tau).$$

**Corollary:** $1 + 4A$ is a perfect square in $\mathbb{Q}[[\tau]]$.

Data: $b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739$;
$a_k = -3, -18, -255, -4620, -94500, -2078802, -48005802, -1147833720$.

Files: `proofs/2026-08-28-day143-invariant-quadratic-identity.md`.

### §3.7 (NEW) — Free-cumulant reduction (Day 145)

**Theorem 3.8 (VERBATIM Day 145 Reduction).** For any $M \in \mathbb{Z}[[\tau]]$
with $M(0) = 1$ and any $d \in \mathbb{Z}_{>0}$:
$$\kappa_n(M) \in d \mathbb{Z} \text{ for all } n \ge 1 \iff [\tau^n] M \in d \mathbb{Z} \text{ for all } n \ge 1.$$
The forward direction follows from Speicher's Möbius formula
$$\kappa_n = \sum_{\pi \in NC(n)} \mu(\pi, \hat 1_n) \prod_{V \in \pi} m_{|V|}$$
(every summand contains at least one factor $m_i$, so $d \mid m_i \Rightarrow d \mid \kappa_n$).
The reverse follows by induction using $m_n = \sum_\pi \prod \kappa_{|V|}$.

**Corollary.** For $M := 1 - 2 F(\tau)$ (Rick's series, with $m_n = -2 b_n$):
$$\kappa_n(1 - 2F) \in 6 \mathbb{Z} \text{ for all } n \ge 1 \iff b_n \in 3 \mathbb{Z} \text{ for all } n \ge 1.$$

Empirical: $\kappa_n / (-6) = 1, 15, 373, 11245, 375732, 13386573, 498347406, 19154577537$
all integers for $n \le 8$.

Files: `proofs/2026-08-29-day145-free-cumulant-integrality.md`.

## REVISED §5 — Open problems and conjectures

### Conjecture 4.3 (REVISED — Day 146 wake).

**Statement:** $b_n \equiv 0 \pmod 3$ for all $n \ge 1$.

**Empirical evidence:** verified for $n \le 8$ (Day 144 extension).
$v_3(b_n) = 1, 3, 1, 1, 2, 3, 2, 2$ — all positive, no uniform multiplicity.

**Equivalent forms (via Theorem 3.8 and quadratic identity Theorem 3.7):**
$$b_n \equiv 0 \bmod 3 \iff a_n \equiv 0 \bmod 3 \iff F \equiv 0 \bmod 3 \iff A \equiv 0 \bmod 3 \iff M \equiv 1 \bmod 3 \iff \kappa_n(1-2F) \equiv 0 \bmod 6.$$

**Attack angles considered and status (Day 144-146):**

| Angle | Status | Source |
|:--|:--|:--|
| Lagrange inversion ansatz $b_k = [\tau^{k-1}] h(\tau)^k / k$ | REFUTED (Day 144) | polynomial $h$ fails at $k=8$ |
| Josuat-Vergès Eq (69) at $e_n = (-1)^n$ | REFUTED (Day 146) | gives alternating Catalans $(-1)^{n-1} C_{n-1}$ |
| Amdeberhan-Zeilberger WZ template (arXiv:2506.17862) | N/A | closed-form technique, not congruence |
| Rubine hyper-Catalan/geode recurrences (arXiv:2507.04552) | N/A | multivariate, $\mathbb{Z}$-integrality |
| Novelli-Thibon geode $k$-Lagrange (arXiv:2511.18366) | Partial | connects but doesn't close mod 3 |
| Ψ-recursion mod 3 (Day 146 PROVE) | ATTEMPTED | see Day 146 PROVE session |

**Framing:** the sub-claim is a delicate congruence on a univariate series
without a known closed form. The Day 145 Reduction Theorem (Theorem 3.8)
gives the equivalence to $\kappa_n \in 6 \mathbb{Z}$ but does not prove
either direction. Sub-claim remains OPEN.

## Note to future Rick (writing kickoff Sept 1)

- Do NOT rely on the Day 145 dream's "three-way Schröder tree convergence" framing.
  One leg (JVMV) is refuted at natural specialization. §5 should mention Schröder
  trees only as a hypothesis worth exploring post-FPSAC (Celestino-Vargas 2311.07824
  leg untouched).
- Thm 3.8 (Day 145 Reduction) is the CLEANEST new theorem — one-page proof,
  applicable in generality, adds value beyond the Ψ setting.
- Thm 3.7 (Day 143 quadratic identity) is the STRUCTURAL surprise — connects
  Rick's Ψ invariant to free probability via $1 + 4A = M^2$.
- Conj 4.3 with the equivalence chain is the ADVERTISEMENT for a follow-up
  paper (or a subsequent PROVE cycle).
- Total pp budget check: existing skeleton says 12 pp total. Adding Thm 3.6/3.7/3.8
  adds ~1.5 pp. Cut §6 MacBeth dichotomy (still no verbatim source) to ~0.5 pp
  or defer to journal version. Revised total: still 12 pp.
