# Novelty check — Rick's h-basis compositional formula for $X_{P_n}(q)$

Date: 2026-09-11. Trust grade: `computed` (literature scan).

## Rick's formulas

- **(GF)** $F(z)[E(qz) - qE(z)] = (1-q)E(z)$ where $F(z) = \sum_n X_{P_n}(q)z^n$, $E(z) = \sum_n e_n z^n$.
- **(Re)** $X_{P_n}(q) = e_n + q\sum_{k=2}^n [k-1]_q e_k X_{P_{n-k}}(q)$.
- **(Comp)** $X_{P_n}(q) = \sum_{(k_1,\ldots,k_r)\vDash n,\ k_i\ge 2\ (i<r),\ k_r\ge 1} q^{r-1}[k_r]_q \prod_{i<r}[k_i-1]_q\, e_{k_1}\cdots e_{k_r}$.

## Verdict

**All three are KNOWN (2010 or earlier).**

### Primary hit — Shareshian–Wachs, "Eulerian quasisymmetric functions" (2010, arXiv:0812.0764)

**Theorem 7.2** (attributed to **Stanley, personal communication**) states, for $Y_{n,j}(x)$ = weighted enumerator of words of length $n$ with no adjacent repeats and descent number $j$ (= $X_{P_n}(q)$'s $q^j$ coefficient, Shareshian–Wachs $q$-refinement):

$$\sum_{n,j\ge 0} Y_{n,j}(x) t^j z^n = \frac{(1-t)E(z)}{E(zt) - tE(z)}.$$

This is Rick's (GF) verbatim (with $t \leftrightarrow q$). The paper explicitly identifies $Y_n$ with the chromatic (quasi)symmetric function of $P_n$ (lines 2174-2175 of arXiv PDF; §7 "Other occurrences"). Attribution goes back to **Stanley (personal communication)**; the classical $t=1$ case is **Carlitz–Scoville–Vaughan (1976)** eq. (7.5) on page 45.

- URL: https://arxiv.org/abs/0812.0764
- Location: Theorem 7.2, page 45 of arXiv v2.

### Secondary confirmations

**Ellzey, "Chromatic quasisymmetric functions of directed graphs" (arXiv:1709.00454)** — Proposition 6.9 with proof (line 1987+ of PDF) reproduces the SW10 GF and derives Rick's (Comp) formula as equation (6.7):

$$X_{\vec{P}_n}(x,t) = \sum_{\lambda\vdash n} e_\lambda \sum_{\mu:\lambda(\mu)=\lambda} [\mu_1]_t \cdot t[\mu_2-1]_t \cdots t[\mu_{l(\lambda)}-1]_t.$$

Ellzey's $[\mu_1]_t \prod_{i\ge 2} t[\mu_i-1]_t$ is Rick's $q^{r-1}[k_r]_q \prod_{i<r}[k_i-1]_q$ under $\mu_i \leftrightarrow k_{l+1-i}$. Ellzey cites [SW10, Thm 7.2] as source of the GF and references [SW16, Table 1] for (6.7). So Rick's (Comp) at general $q$ appears (published) in Ellzey 2017/2018 as eq. (6.7).

- URL: https://arxiv.org/abs/1709.00454 (full paper); the extended abstract is arXiv:1612.04786 (NOT 1611.06349, which is a Lie superalgebra paper — the ID in the user request was wrong).

**Alexandersson–Panova, "LLT polynomials, chromatic quasisymmetric functions and graphs with cycles"** (Discrete Math 2018, arXiv:1705.10353) — **Theorem 38** on page 20 restates the GF for $X_{P_n}(x;q)$ in exactly Rick's form:

$$\sum_n X_{P_n}(x;q) z^n = \frac{\sum_{i\ge 0}e_i(x)z^i}{1 - q\sum_{i\ge 2}[i-1]_q e_i(x) z^i},$$

with the note "The results in the following theorem has also been proved using different methods in [SW10, Ell16]." Their independent proof is by induction on $n$ and the number of variables (equation 22 gives Rick's (Re) recursion at the level of variable count).

- URL: https://arxiv.org/abs/1705.10353

### Guay-Paquet 2013 (arXiv:1306.2400)

Not the source of this formula — that paper is about the modular law for $(3+1)$-free posets, not path-graph GFs. Path-graph GF pre-dates it.

### Dahlberg / van Willigenburg

Their path-graph work concerns $e$-positivity of `spider-like` graphs, not this GF. Not the source.

### Shareshian–Wachs "Chromatic quasisymmetric functions" (2014, arXiv:1405.4629)

Extends the 2010 result to the full chromatic quasisymmetric framework. The path-graph GF is not the headline theorem there because it was already published in SW10.

### Sagan–Tom (arXiv:2407.06155), Foster Tom (arXiv:2311.08020), Athanasiadis 2014, D'Adderio–Riccardi–Siconolfi

None of these give the closed compositional formula for $X_{P_n}(q)$ — they treat other aspects (necessary conditions, signed $e$-expansions, $p$-basis, general interval orders).

## Final verdicts

| Formula                        | Status                              | Source                                                                 |
|--------------------------------|-------------------------------------|------------------------------------------------------------------------|
| (GF) at general $q$            | KNOWN (2010)                        | Shareshian–Wachs 2010, Thm 7.2 (attrib. Stanley pers. comm.)           |
| (Re) recursion at general $q$  | KNOWN (equivalent to (GF); explicit variable-count recursion in Alexandersson–Panova 2018 eq. (22)) | SW10 Thm 7.2 → immediate; A–P 2018 eq. (22)                            |
| (Comp) at general $q$          | KNOWN (2017)                        | Ellzey 2017/2018, eq. (6.7); a Lagrange-inversion expansion of the SW10 GF |
| (Comp) at $q=1$                | KNOWN (classical)                   | Carlitz–Scoville–Vaughan 1976 (GF form eq. (7.5) of SW10); Stanley 1995 |

## Implications for Rick

- The h-basis $q$-GF form $F(z)[E(qz)-qE(z)] = (1-q)E(z)$ is **not new**.
- The e-basis compositional formula (Comp) is **not new** at any $q$.
- The Day 187 "combinatorial proof of (Comp)" — if pursued as combinatorial proof of the *specific formula* — reproves Ellzey (6.7). Any novelty must come from either
  1. a *new proof method* (bijective / cumulant-flavored) that has independent value,
  2. a $(q,t)$-lift beyond Ellzey/A–P/SW10 (this is the Griffin–Mellit–Romero–Weigl–Wen / Hikita direction — genuinely open territory),
  3. framing (Re) as part of the h-basis atomic-data / restricted-modular-law program (positive/Boolean cumulants of $b_k$), which is the Day 186 thread and is genuinely new.

**Recommendation.** Rederive Ellzey (6.7) as warm-up but do NOT anchor a FPSAC 2027 abstract on it. Anchor instead on
- the atomic-data / restricted-modular-law reading, and/or
- a $(q,t)$-lift via Hikita Pieri (Day 187+ direction).

## Corrections to the request

- The user's citation "Ellzey 2017 arXiv:1611.06349" is wrong. That arXiv ID is a Bagci–Calixto–Macedo paper on Weyl functors for Lie superalgebras. Ellzey's paper is **arXiv:1709.00454** (full) or **arXiv:1612.04786** (extended abstract).
