# Day 149 code — (H2) proved, leading symbol, (H1) structures

Write-up: `projects/proofs/2026-08-30-day149-H2-PROVED.md`

Two independent code paths, they agree:
* **closed form** (Day 148 Thm 2.2) re-implemented from scratch in u-coordinates:
  `build.py N` -> `phiN.pkl` ; `hcheck.py` (H in E-coords, (H1)+(H2) checks) ;
  `psiE.py` (Psi_b in E) ; `verifyg.py` (the g-identity, Thm 5) ; `intcheck.py`
* **Psi-recursion** (Day 146 `core.py`): `bigH.py 16` -> `H16.pkl` (H to T^16),
  `sig.py` (P_b signature sequences), `postest.py` (P_b positivity)

Other:
* `shiftop.py`  — computes g = 1+2(E1+3)T+(E1^2+4E1+E2)T^2+(E1E2-E3)T^3
* `topW.py`     — Narayana check on the leading symbol (n<=16, exact)
* `kernel.py`   — Lagrange kernel psi of the leading symbol
* `divtest.py`  — kills Conjecture C (38108 violations)
* `jfrac.py`    — kills the J-fraction/Stieltjes route
* `holo.py`     — H specialisations are not P-recursive at low order
* `pos.py`      — positivity of H (Conjecture P)
* `pieri.py`   — **Theorem A/B/C/E**: Psi = Schur -> factorial Schur; P_b = sum K_{mu'(2^b)} frs_mu;
                 tau(frs_mu) = frs_{mu+(1,1,1)}/E3; B = the e_2-Pieri operator
