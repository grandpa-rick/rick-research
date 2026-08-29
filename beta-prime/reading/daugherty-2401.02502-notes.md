# Daugherty, "Extended Schur functions and bases related by involutions" (arXiv:2401.02502v2, Sep 2024)

**PDF:** `/home/agent/projects/beta-prime/reading/daugherty-2401.02502.pdf`

## Setting

- Ambient algebras: `QSym` (quasisymmetric functions) and `NSym` (noncommutative symmetric functions), dually paired via `<H_alpha, M_beta> = delta_{alpha,beta}`.
- Bases of interest: extended Schur basis `w*_alpha` in `QSym` (Assaf-Searles / Campbell-Feldman-Light-Shuldiner-Xu, indexed by shin-tableaux), and its dual, the shin basis `w_alpha` in `NSym`.
- Row-strict, reverse, row-strict-reverse variants live in a **system of 4 related bases** closed under three involutions `psi, rho, omega`.

## The three involutions (Definition 5.1)

Defined by their action on the fundamental basis `F_alpha` of `QSym` and the ribbon basis `R_alpha` of `NSym`, using composition operations:

- `alpha^c` = complement of composition (viewing alpha as bar-pattern in [n-1])
- `alpha^r` = reverse
- `alpha^t = (alpha^r)^c = (alpha^c)^r` = transpose

Definitions:

- `psi(F_alpha) = F_{alpha^c}`,  `psi(R_alpha) = R_{alpha^c}`
- `rho(F_alpha) = F_{alpha^r}`,  `rho(R_alpha) = R_{alpha^r}`
- `omega(F_alpha) = F_{alpha^t}`, `omega(R_alpha) = R_{alpha^t}`

Structure:
- All three commute pairwise and `omega = rho o psi = psi o rho`.
- `psi` on `QSym` and on `NSym` is a **Hopf algebra automorphism** (only nontrivial one preserving F-basis, per Jia-Wang-Yu 2017 [17]).
- `rho, omega` on `QSym` are **automorphisms**; on `NSym` they are **anti-automorphisms**.
- When restricted to `Sym`, both `rho` and `omega` collapse to the classical `omega: Sym -> Sym`, `omega(s_lambda) = s_{lambda'}`, `omega(e_lambda) = h_lambda`.

## Action on shin / extended Schur bases

Applying the involutions to `w*_alpha` and `w_alpha` produces the 4-basis system:
- `psi(w*_alpha) = Rw*_alpha`  (row-strict extended Schur)
- `rho(w*_alpha) = a*_{alpha^r}`  (reverse extended Schur)
- `omega(w*_alpha) = Ra*_{alpha^r}`  (row-strict reverse extended Schur)

Diagram (Figure 2): the four dual pairs sit at corners of a square, edges labeled `psi` (top/bottom), `rho` (sides), `omega` (diagonals).

## Antipode connection (the money quote for Rick)

Section 5.3, Corollary 5.40, page 26. Combining Theorem 5.35 and Prop 5.38:

- `S(w_alpha) = (-1)^{|alpha|} Ra_{alpha^r}` on `NSym`
- `S*(w*_alpha) = (-1)^{|alpha|} Ra*_{alpha^r}` on `QSym`

I.e. the antipode of a shin function equals `(-1)^n` times the row-strict-reverse shin function of the reversed composition. Written via involutions: `S = (-1)^n * omega o psi = (-1)^n * rho` on shin (since `omega = rho o psi`). More precisely, tracking the paper's identities:
  - `Rw_alpha = psi(w_alpha)`
  - `a_alpha = rho(w_{alpha^r})`
  - `Ra_alpha = omega(w_{alpha^r}) = psi(a_alpha) = rho(Rw_{alpha^r})`

The paper cites this as **an open problem previously**: describing `S(w_alpha), S*(w*_alpha)` explicitly. Their contribution here reduces it to a change-of-basis between row-strict-reverse and extended Schur.

Related antipode formulas cited:
- Malvenuto-Reutenauer [19]: `S*(F_alpha) = (-1)^{|alpha|} F_{alpha^t}` on `QSym`. Note: this is `(-1)^n * omega(F_alpha)`.
- Benedetti-Sagan [4]: `S(R_alpha) = (-1)^{|alpha|} R_{alpha^t}` on `NSym`. Same form: `(-1)^n * omega(R_alpha)`.

**Explicit form of "involution + antipode = shift":** the paper does not state a translation identity of the form `tau(E_k) = E_k + phi_1` for any generator. The closest structural statement is Prop 5.4/5.38 style identities of the form `X_alpha = involution(Y_{alpha^r})`, i.e. involutions permute the four bases.

## Action on elementary noncommutative symmetric functions E_alpha

In `NSym`, `E_alpha = sum_{alpha <= beta} (-1)^{|alpha| - ell(beta)} H_beta` (page 5). The paper does **not** give a clean single formula for `psi(E_alpha), rho(E_alpha), omega(E_alpha)`, but since `omega: Sym -> Sym` sends `e_lambda -> h_lambda`, one expects `omega` on `NSym` to interchange `E` and `H` up to composition-flip corrections. The paper works with these mostly implicitly through Pieri rules (Theorems 5.5, 5.22, 5.39). E.g. Theorem 5.22(2) gives `H_beta = sum K_{alpha^r, beta^r} a_alpha` (reverse-shin analog of the shin expansion).

## Other bases sitting in this diagram

- **Immaculate basis** `S_lambda` of Berg-Bergeron-Saliola-Serrano-Zabrocki [5]. Its dual is the dual immaculate basis in `QSym`. Related to shin via `s_lambda = w_lambda` and `S_lambda = s-hat_lambda` for partitions.
- **Young noncommutative Schur basis** (Luoto-Mykytiuk-van Willigenburg [18]): related to the standard Schur-like bases by `rho`.
- **Quasisymmetric Schur** (Haglund-Luoto-Mason-van Willigenburg [15]) and **Young quasisymmetric Schur** [18]: also related by `rho`.
- **Row-strict quasisymmetric Schur** [23] and skew row-strict [22]: related to Schur analogs by `psi` and `omega`.

## Key references to chase

- [17] Jia-Wang-Yu, "Rigidity for the Hopf Algebra of Quasisymmetric Functions", Electron. J. Comb. 26 (2017) - proves `psi, rho, omega` are the **only nontrivial graded algebra automorphisms of `QSym` that preserve the fundamental basis**. Crucial for Rick: if his `phi` preserves an `F`-like basis, it must be one of these three (or identity).
- [4] Benedetti-Sagan, "Antipodes and involutions", JCTA 148 (2017) - antipode formulas on Schur-like bases.
- [10] John Campbell, "On antipodes of immaculate functions", Ann. Comb. 27 (2023) - closest prior work on the S-vs-involution question.
- [19] Malvenuto-Reutenauer, J. Algebra 177 (1995) - foundational antipode formulas.
- [18] Luoto-Mykytiuk-van Willigenburg book on Young quasisymmetric Schur functions - source of the composition operations `c, r, t`.
