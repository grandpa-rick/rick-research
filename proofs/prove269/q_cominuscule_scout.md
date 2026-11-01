# Q55 cominuscule scout (PROVE 269 compute agent, 2026-11-01). Grade: COMPUTED only.

Script `q_cominuscule_scout.py` (run with no args, or with name filters). Outputs: `q_cominuscule_scout.out` (cominuscule
cases up to E6), `q_cominuscule_scout_part2.out` (E7 and all controls). Total run time is about 2 min.

## Definitions used
- Elements of W are stored as w(rho) in fundamental-weight coordinates. W^J (minimal left-coset reps, J = nodes KEPT) is the
  orbit of lambda_J = sum of omega_k over k not in J. Bruhat order is the deterministic lifting recursion (Z). No enumeration
  of W is needed, so E6 and E7 run directly.
- (a) [x,y] inside W^J is a Boolean lattice (atom test, as in q55.py).
- (b) [x,y]_W ⊆ W^J. Tested as: there are no v in [x,y]_{W^J} and s in J with vs ≤ y. This is equivalent, because the
  projection w -> w^J preserves order and the subword property holds. It was cross-checked against the full interval (0 bad)
  on every group with |W| ≤ 192.
- (c) y = s_{i1}...s_{ik} x, with the i_j distinct and pairwise commuting and every step going up in W^J. This is the
  "antichain skew heap" in left weak order. When W^J is distributive, it was cross-checked against "J(y)∖J(x) is an
  antichain in the join-irreducible poset": 0 mismatches in every distributive case.
- (d) P^{J,q}_{x,y} = 1. This is Deodhar's R-recursion on W^J, the `parKL` code copied verbatim from prove268/q55.py, with
  stay-factor −1. (d−) is the u = −1 version (stay-factor q). Cross-checks: P^{J,q} = Σ_{u∈W_J}(−1)^{ℓ(u)}P_{xu,y} and
  P^{J,−1} = P_{xw_J,yw_J}, both 0 bad, on A3, A4, B3 (both quotients), D4 (3 quotients), G2 and the A3 controls.
- Minuscule/cominuscule is a property of the root system, but W^J depends only on (W,J). So C_n-Lagrangian = B_n-spinor and
  B_n-quadric = C_n-projective space as test cases.

## Results: cominuscule and minuscule (W,J). All implications among a, b, c, d hold: 0 failures
| (W,J) | |W^J| | pairs | a⇔b⇔c⇔d fails | d−⇒a fails | a⇒d− fails |
|---|---|---|---|---|---|
| A3 Gr(2,4) | 6 | 20 | 0 | 6 | 0 |
| A4 Gr(2,5) | 10 | 50 | 0 | 20 | 0 |
| A5 Gr(2,6) | 15 | 105 | 0 | 49 | 0 |
| A5 Gr(3,6) | 20 | 175 | 0 | 78 | 0 |
| C3 LG(3,6) = B3 spinor (sanity) | 8 | 35 | 0 | 15 | 0 |
| B3 node 1 (B: cominuscule quadric; C: minuscule P^5) | 6 | 21 | 0 | 10 | 0 |
| B4 spinor = C4 LG(4,8) | 16 | 126 | 0 | 58 | 0 |
| D4 node 1 / node 4 | 8 | 35 each | 0 | 15 each | 0 |
| D5 node 1 | 10 | 54 | 0 | 27 | 0 |
| D5 node 5 | 16 | 126 | 0 | 58 | 0 |
| E6 node 1 | 27 | 351 | 0 | 154 | 0 |
| E7 node 7 | 56 | 1463 | 0 | 507 | 0 |

So u = −1 is NOT equivalent in any case: P^{J,−1} = 1 on a strict superset of the Boolean pairs.

## Controls (non-cominuscule)
| (W,J) | |W^J| | pairs | distributive | b⇒a fails | a⇒c fails | b⇔d fails | a⇒b, c⇒all fail |
|---|---|---|---|---|---|---|---|
| A3, J={s2} (non-maximal) | 12 | 64 | no | 2 | 12 | 0 | 0 |
| A3, J={s1} (non-maximal) | 12 | 65 | no | 2 | 16 | 0 | 0 |
| B3 node 2 | 12 | 72 | no | 1 | 6 | 0 | 0 |
| C4 node 2 | 24 | 260 | no | 2 | 12 | 0 | 0 |
| D4 node 2 (adjoint) | 24 | 246 | no | 3 | 18 | 0 | 0 |
| F4 node 4 | 24 | 284 | no | 1 | 6 | 0 | 0 |
| E6 node 2 (adjoint) | 72 | 2166 | no | 5 | 30 | 0 | 0 |
| G2 node 1 / node 2 | 6 | 21 | yes (chain) | 0 | 0 | 0 | 0 |

- In the controls, the chain of implications c ⇒ a ⇒ b ⇔ d survives. b ⇒ a breaks. Every b-not-a pair seen is a rank-3
  interval with rank sizes 1,2,2,1, i.e. a hexagon (2-crown). Example: A3, J={s2}, x = s1, y = s2s3s2s1, P^{J,q} = 1.
  So **(b)⇔(d) looks general** (consistent with the general-Coxeter half of Theorem K: interval inside W^J makes the
  alternating sum collapse). **(a)⇔(b) needs the hypothesis.** a ⇒ c also breaks, but the weak-order (c) is only a proxy
  outside the fully commutative/distributive setting.
- G2 is a non-breaking control: both quotients are chains, so the equivalences hold trivially.
- Cominuscule is not visibly the sharp hypothesis. Every case where everything held had a distributive W^J (minuscule
  quotient or a chain), and every case that failed was non-distributive. A guess to test next, not a claim: the hypothesis
  is "W^J distributive" or "elements fully commutative".
