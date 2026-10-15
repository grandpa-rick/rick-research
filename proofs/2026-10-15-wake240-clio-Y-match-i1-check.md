# Wake 240 — check of Clio's Y-match (review 2026-10-14, item 1 / F3)

Grade: **computed** (N=2,3 on 13/23 monomials of deg<=3 plus 3 Laurent monomials; N=4 on 18 monomials deg<=2 plus 3 Laurent), with a 4-line hand derivation (below), not cold-read.

Script: `/home/agent/projects/work-in-progress/scripts/day240/clio_ymatch.py`; output: `.../day240/clio_ymatch.out`.

## Printed definitions used
- **DFK** (arXiv 1704.00154, `deformDAHA.tex`, subsection "The functional representation of the DAHA", ~l.127–133):
  rho(T_i) = theta s_i + (theta - theta^-1)/(x_i x_{i+1}^-1 - 1) (s_i - 1); rho(T_i^-1) = rho(T_i) - theta + theta^-1;
  rho(pi) f = f(x_2,...,x_N, q^-1 x_1); rho(Y_i) = rho(T_i ... T_{N-1} pi^-1 T_1^-1 ... T_{i-1}^-1).
  Def. (subsec. "More commuting operators", ~l.180): Y_{i,n} = (X_1...X_{i-1})^-n Y_i (X_1...X_i)^n, n in Z; "Y_{1,n} = Y_1 X_1^n".
- **Hikita** (arXiv 2503.23597, p.10–11): (1) T_i•F = t s_i(F) + (t-1)(F - s_i F)/(1 - X_i X_{i+1}^-1); (2) Pi•F = X_1 F(X_2,...,X_m, q^-1 X_1);
  (3) Y_i := t^{m-i} T_{i-1}...T_1 Pi T_{m-1}^-1 ... T_i^-1, followed by "Note that our Y_i essentially corresponds to Y_i^-1 in the usual convention for DAHA (see e.g. [6])."
  T_i^-1•F = s_i(F) + (1-t^-1)(X_i X_{i+1}^-1 F - s_i(F))/(1 - X_i X_{i+1}^-1) (proof of Lemma 2.11).
  *Parse note:* my first reading of that text layer put X_iX_{i+1}^-1 outside the numerator. That version is not the inverse of (1) (it sends 1 to 1, not t^-1). The script now asserts T^-1 T = id for both families.
- Words act as operators with the rightmost factor applied first. "n" is DFK's integer twist index in Y_{i,n}.

## Dictionary (Clio 2.1): CONFIRMED
T^H_i = theta·rho(T_i) and (T^H_i)^-1 = theta^-1·rho(T_i^-1) at t = theta^2; Pi = x_1·rho(pi). Asserted for N=2,3,4. Controls C1 ({Y^H_i} commute) and C2 ({Y_{i,n}} commute, n=-1,0,1) PASS.

## Clio's i=1 identity, literal: PASS
Y^H_1 ∘ Y^DFK_{1,n} = theta^{N-1} x_1^{n+1}·id holds on every test monomial for N=2,3,4 and n = -2,-1,0,1,2.

## i>=2 (Clio's Q463): her finding is reproduced, but she only tested n=0,1, and that is the gap
For n = -2, 0, 1, 2, Y^H_i ∘ Y^DFK_{i,n} is not a multiplication operator (5–20 distinct ratios). This reproduces her n=0,1 result.
**At n = -1 it is the scalar theta^{N-1}, for every i (N=2,3,4).** Equivalently, as operators,

  **Y^H_i = theta^{N-1} (Y^DFK_{i,-1})^{-1} for all i** (0 bad on all test sets). The same identity with n=+1 fails on every monomial.

Hand derivation: Y^H_i = theta^{N-1} T_{i-1}...T_1 x_1 pi T_{N-1}^-1...T_i^-1. Then T_{N-1}^-1...T_i^-1 commutes past (x_1...x_{i-1})^{-n}, and pi (x_1...x_{i-1})^{-n} pi^-1 = (x_2...x_i)^{-n}. This gives
Y^H_i ∘ Y^DFK_{i,n} = theta^{N-1} · [T_{i-1}...T_1 · x_1 (x_2...x_i)^{-n} · T_1^-1...T_{i-1}^-1] · (x_1...x_i)^n.
The bracket is a multiplication operator iff x_1(x_2...x_i)^{-n} is symmetric in x_1..x_i. For i>=2 that means n = -1, and then the result is theta^{N-1}. For i=1 there is no conjugation, so every n works. That is why i=1 looked special.
So Q463 resolves positively: Hikita's level-one Y_i is the theta-rescaled inverse of DFK's **n = -1** twisted Y. It is not a match with n=+1.

## Controls that must break: ALL BROKE (i=1, n=0,1; N=2,3,4)
- K1, inversion dropped (Y^H_1 ∘ (Y_{1,n})^-1): not a multiplication operator (12/13, 22/23, 17/18 monomials bad).
- K2, t = theta instead of theta^2: breaks.
- K3, theta -> theta^-1 on the DFK side: breaks.
- K4, reversed order Y^DFK_{1,n} ∘ Y^H_1: breaks.
- The n=+1 version of the exact identity: fails on every monomial.

## Convention flag for Rick (not resolved here)
longversion.tex l.189 says Thm subset "is the analogue, for n=1", and suggests comparing with (Y_{i,1})^-1. The computed match is with (Y_{i,-1})^-1 instead. Then e_k(Y^H) = theta^{k(N-1)} e_k(Y_{·,-1}^{-1}) = theta^{k(N-1)} e_{N-k}(Y_{·,-1})/e_N(Y_{·,-1}). That points to M_{N-k;-1}, not directly to M_{k;1}. Whether DFK's tau_+ route (Lemma 2.12 / Thm 2.17) still yields E_k = t^{k(m-k)} M_{k;1} through some other identification (q-inversion, the sign convention of tau_+) has **not** been checked. It should be checked before anything is upgraded from "analogue".
