# Day 146 PROVE — master equation; $b_k\equiv0\ (3)$ reduced to Conjecture H

Full write-up: `~/projects/proofs/2026-08-29-day146-bk-mod3-master-equation.md`

## Headline

    L F_P = E3 T^2 [ -3 + T(E1 + 6 + 2*theta) ] tau(F_P)          (MASTER EQUATION)

    rho = E3 T^2 ,  vartheta = E3 T^3 ,  H = tau(F_P)/F_P ,  Hcal = diag(H)

    F^2 - F = vartheta * Hcal * (2F - 3)                          (MAIN IDENTITY)

    ==>  b_k = 0 mod 3 for all k   <==>   Hcal in Z_3[[vartheta]]

    CONJECTURE H:  tau(F_P)/F_P in Z[E1,E2,E3][[T]] , deg_E3 [T^n] <= floor(n/3).
    Verified symbolically to T^14, numerically to T^36.  Implies the theorem.

## Also proved

* Lemma A: deg_E3 P_b <= floor(b/2)                        (path argument)
* Lemma B: v_3([E3^k] Psi_b) >= max(0, 3k-b)               (path argument, sharp)
  => deg_E3 (Psi_b mod 3) <= floor(b/3), and mod 3
     Psi_{3m+3} = a*b*E2 Psi_{3m} + E1 E3 sigma(Psi_{3m}),  a=E2-E1+1, b=E2+E1+1
* Prop 1: Conjecture H (part 2) => Day 143 leading-T vanishing lemma (previously only numeric)
* [E3^k] P_{2k} = 3^k (2k-1)!!   (exact top boundary; F_P|_{T=0,rho fixed} = e^{3 rho/2})
* e^{-3 rho/2} F_P = sum_d T^d G_d, G_d polynomial in rho, weighted deg <= 2d

## Why the naive mod-3 attacks all fail

b_k is extracted by dividing by (3k-1)!, v_3 ~ 3k/2. So a_k mod 3 is NOT a function
of {P_b mod 3}.  In Gamma_Z[[T]] = {sum c_b T^b/b! : c_b in Z} (a ring containing
F_P, F_P^{-1}, L F_P, X) mod-3 reduction is fine but there is no division by (3k-1)!.

## Files

| file | purpose |
|---|---|
| `core.py` | dict-based Z[E1,E2,E3] arithmetic, Psi/P recursion |
| `verify_master.py` | verifies the master recursion identically for b<=16 |
| `logtab.py` | v_3 table of log F_P; b_k for k<=11 |
| `Hdiag.py` | H at (U,V)=(0,0): order>=0, integrality, diagonal h_j |
| `eta.py` | coefficients of H are integers |
| `symH.py` | H integral **symbolically** in Z[E1,E2,E3] to T^14 |
| `general_pt.py` | main identity + Conjecture H at four base points |
| `secdiag.py` | a_k is (E1,E2)-free; second diagonal linear in E1 |
| `bigdata.py` | b_k to k=12, h_j to j=12, H integral to T^36 |
| `search.py` | no P-recurrence (order<=4, deg<=4) for b_k or h_j |
| `Fd.py`, `graded.py` | (rho,T)-expansion; exponential normal form |

## New data

b_k (k=1..12): 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739,
               50751637140, 1276862920140, 32626363346505, 844375375808301
v_3(b_k):      1, 3, 1, 1, 2, 3, 2, 2, 1, 1, 2, 1
Hcal (j=0..12): 1, 8, 119, 2200, 45500, 1007904, 23387442, 561163152,
               13809781700, 346645093984, 8840919351575, 228449188011224,
               5968029850876084

## Late addition: Dwork reformulation

With Frobenius lift sigma(E_i) = E_i^3 and K := F_P(T)^3 / sigma(F_P)(T^3):

    Conjecture H1  <==>  tau(K)/K  in  1 + 3T Z_3[E][[T]]      (verified to T^22, 3 points)

Lemma C (PROVED): F_P(T)^3 = 1 and sigma(F_P)(T^3) = 1 in Gamma_{F_3}[[T]],
so K in 1 + 3*Gamma_{Z_3}.  [char-3 Frobenius + v_3( (3b)!/(b!)^3 ) = s_3(b) >= 1]

Writing K = 1+3W:  H1  <==>  (tau W - W)/(1+3W)  in  T Z_3[E][[T]].
NOTE: without the E3 -> E3^3 twist the Dwork criterion FAILS numerically (unit
coefficient at T^9) -- the twist is essential.  See dwork.py, dwork2.py.
