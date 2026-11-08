# PROVE 283: exact mu for open26 instance 0 (and mirror instance 1), lambda = (6,4,3,3) (2026-11-08)

Grade: **COMPUTED**, not proved. The code is validated against brute force in S_5 and S_6, and it reproduces the
earlier dyer.c values for instances 11 and 13.

## Result
**mu(inst 0) = mu(inst 1) = 1.**

| pair | |[x,z]| | Bruhat-graph edges | double-max targets | l(x), l(z) | P_{x,z} | mu | wall |
|---|---|---|---|---|---|---|---|
| inst 0, qbest Q | 894344 | 10144296 | 5525 | 33, 52 | 1+12q+62q^2+181q^3+328q^4+381q^5+279q^6+119q^7+26q^8+q^9 | **1** | 63 s |
| inst 0, inverse pair (x^-1,z^-1) | 894344 | same | 5525 | 33, 52 | identical | 1 | 63 s |
| inst 0, alternate Q (x=[5,4,3,9,1,8,7,2,15,14,11,6,13,10,12,16]) | 894344 | same | 13546 | 34, 53 | identical | 1 | 103 s |
| inst 1 (evacuation mirror), Q with gap 19: x=[1,5,7,4,11,6,3,2,15,10,9,16,14,8,13,12], z=[4,5,10,6,14,11,7,1,15,12,8,16,13,2,9,3] | 1049576 | 11920172 | 23996 | 35, 54 | 1+13q+72q^2+220q^3+403q^4+455q^5+314q^6+123q^7+26q^8+q^9 | **1** | 180 s |

The instance-1 run is the strongest cross-check. It uses a different cell pair, a different interval, a different P and a different target set, and it still gives mu=1.
The inst-1 qbest Q (gap 23) has an interval of 7.08M elements and 99M edges. That run was OOM-killed at about 19 GB, so it is not used here.

Consequence, per q68-consequences.md: pairs 353 and 364 are **TWIN**. The S_16 census becomes 114 / 296 / 0.
Pairs 352 and 365 then have a genuine (ii)-element with mu(y,z)=1, so **Q68-ii-kills is FALSE**. This holds only if the q68-consequences.md mapping is right; I did not recheck it here.

## Method
1. **Q search** (altq.py). I took 3000 hook-walk Qs per instance plus row and column superstandard Qs, then one round of swap neighbours of the best 50.
   - The minimum gap is 19 for both instances.
   - Every pair I used satisfies rsk(x)[0]=Px and rsk(z)[0]=Pz (asserted in the script).
   - Descent push does nothing: L(z) ⊆ L(x) and R(z) ⊆ R(x) already hold for instances 0 and 1, so no s gives sx>x with sz<z.
2. **dyer2.c** (new; C rewrite of dyer.c).
   - It generates [x,z] by downward cover BFS with a rank-matrix >= x test, then builds the full Bruhat graph on the interval.
   - It uses Dyer's path formula with lex reflection order on position pairs, as in dyer.c.
   - R~_{u,y} is computed by DP over edges, with label-sorted in-edge prefix sums.
   - **Double-coset shortcut.** P_{y,z} = P_{rep(y),z}, where rep(y) = max of W_K y W_J, K=L(z), J=R(z). This is the standard identity P_{y,z}=P_{sy,z} for sz<z, and its right-hand analogue.
   - So the inversion formula q^{l(z)-l(u)}P_{u,z}(1/q) - P_{u,z} = sum_y R_{u,y} P_{rep(y),z} only has to be solved at double-max u.
   - All R_{u,y} are still exact. Only the set of u is reduced, from 894k to 5525.
3. **Validation.**
   - `dyer2 all` (no shortcut) and `dyer2 coset` both give the known inst-13 P (1+8q+24q^2+35q^3+26q^4+9q^5+q^6).
   - Coset mode gives the known inst-11 P (1+11q+48q^2+106q^3+126q^4+80q^5+23q^6+q^7).
   - val2.py compares every double-max P_{u,z} against brute-force KL in S_5 and S_6: 0/106 and 0/137 failures.
   - A naive restriction of Dyer's formula to the induced graph on coset-max elements does **not** work (partest.py fails, e.g. 56/536 in S_6). Only the aggregated version above is correct.

Caveats:
- This is the same Dyer/lex machinery as dyer.c, so it is not a fully independent algorithm. The KL-recursion cross-check used for inst 13 was not repeated here.
- Brute-force validation only reaches S_6.
- Peak memory for the 0.9M interval is about 2.5 GB, and G is stored as ll[24] per edge.
Files: dyer2.c, val2.py, partest.py, altq.py, countmax.py, desc0.py.
