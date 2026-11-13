# Q76-T scan, n<=7 (computed, 2026-11-13)

Scripts: `klfast.py` (full KL S_n, packed-int polys; validated = klperm.py on all 98407 pairs n=6, 0 mismatch;
S_7 Bruhat pairs 3550919, 2.6 s), `q76t_s7.py` (scan; conventions/RSK from cellinv.py/cellinv3.py),
`q76t_verify.py` (independent re-check via klperm recursion on lower ideal + RSK^-1 round trip). Raw output: `q76t_s7_raw.txt`.

## Regression (computed)
n=5: 30 all-Q-comparable keys, 0 nontrivial. n=6: 106 keys, 2 nontrivial (both 1+q, shapes (3,3),(2,2,2)). MATCHES cellinv3.py.

## n=7 (computed) -- Q76-T REFUTED
- keys with some comparable Q: 4304; varying overall: 912 (control: 898 of these not all-Q-comparable -> detector works)
- all-Q-comparable keys: 376; nontrivial P: 22 (shapes (4,3):2, (3,3,1):9, (3,2,2):9, (2,2,2,1):2)
- VIOLATIONS: 14 (all shapes (3,3,1)/(3,2,2)). Polynomial sets per nontrivial key:
  {1+q}: 8 keys (constant); {1, 1+q}: 8; {1, 1+q, 1+2q+q^2, 1+3q+q^2}: 4; {1+q^2, 1+q}: 1; {1+q, 1+2q+q^2}: 1.
- Example: P1=((1,3,6),(2,4,7),(5,)), P2=((1,2,3),(4,5,6),(7,)):
  Q=((1,3,6),(2,4,7),(5,)): x=2154376, y=4175263, P=1+2q+q^2, l(y)-l(x)=5
  Q=((1,3,5),(2,4,6),(7,)): x=2154763, y=4152763, P=1, l-diff 1
  Q=((1,3,5),(2,4,7),(6,)): P=1+3q+q^2, l-diff 5;  Q=((1,3,4),(2,5,7),(6,)): P=1+q, l-diff 3
  (independently re-verified by q76t_verify.py)
- Length gate: l(y_Q)-l(x_Q) is Q-independent for all all-Q-comparable keys at n=5,6 and for 362/376 at n=7;
  the 14 length-varying keys are EXACTLY the 14 violations.
- Interval-isomorphism gate (networkx DiGraphMatcher on Hasse diagrams): n=6 both nontrivial keys isomorphic
  (size 10). n=7: 8 non-violating nontrivial keys isomorphic; 14 violating keys NON-isomorphic (sizes vary 2/10/20/34/52).
- Dual convention (fix Q, vary P): identical numbers at n=5,6,7 (expected: w->w^{-1} swaps P,Q and preserves Bruhat and KL).

## Refinements, 2026-11-13 (computed; script `q76t_local.py`, raw `q76t_local_raw.txt`, n=4..7 total 53 s)
Conventions: right star = {s_i,s_{i+1}} on POSITIONS (right desc i: w[i-1]>w[i]); "cell" = same recording tableau Q
(the fibre of the Q76 scan; right star preserves insertion P1 and maps Q-fibre to Q'-fibre).
- **R-global Q76-T' (const length diff): SURVIVES n<=7.** keys / nontrivial / violations:
  n=4 11/0/0, n=5 30/0/0, n=6 106/2/0, n=7 362/8/0.
- **R-local (all Bruhat pairs), same direction:** x*<=y* NEVER fails (n=4..7). P differs: n=4 0/96, n=5 136/2632,
  n=6 10440/92480, n=7 726168/4190892. -> P-invariance FALSE for arbitrary pairs.
  e.g. n=5 x=12435 y=34152 x*=14235 y*=34512: P=1 vs 1+q.
  Opposite direction: x*<=y* fails n=7 1695564/3802572; P equal only 354652 (P differs 1752356).
  Same direction with DIFFERENT simple reflection on x,y happens (n=7: 1441824 instances) -> "same dir => same refl" FALSE in general.
- **R-local-cell (same Q), same direction:** x*<=y* never fails; P differs: n=4 0/44, n=5 0/528, **n=6 40/7520, n=7 1288/118760**
  -> single-star P-invariance FALSE inside a left cell from n=6.
  CE n=6: x=132465 y=341562 (same Q), star i=2 (both ·s_3): x*=134265 y*=345162, l-diff 4 both, P=1+q vs 1+2q.
  CE n=7: x=1243576 y=1452673 -> x*=1245376 y*=1456273, P=1+q vs 1+2q.
  Within a cell same-direction always uses the same simple reflection (0 exceptions; forced: same Q => same right descent set).
  Opposite dir in cell: n=7 17974 inst, x*<=y* fails 12358, P equal 360.
  Q76-T' survives anyway because these pairs do not lie in all-Q-comparable const-length keys.
- **R-interval:** same-dir all pairs non-iso n=5 397/2000, n=7 825/2000 (half sampled nontrivial-P). Same-dir cell:
  n=4 0/44, n=5 0/528, n=6 42/2000, n=7 82/2000 (sizes e.g. 20 vs 22; printed non-iso examples at n=6 are P-changing pairs -- coincidence with Pdiff set NOT checked).

## PROVE 294 (2026-11-13): n=8 separator -- Q76-T' REFUTED (computed + independent replay)
1478 hypothesis keys (keys8.py direct = good8.py c-form); l(c)>=3: 114, nontrivial 77, VIOLATIONS 8 (all l(c) in {5,6}).
Witness P1=1357/2468, c=14263758: P in {1+2q+q^2 (4 Q), 1+3q+q^2 (10 Q)}; verify8.py (klperm lower ideal) = coxeter3 14/14.
Lemma A (const l-diff => y_Q x_Q^-1 const) proved mod F3 (f3check.py exhaustive n<=8). Write-up: proofs/2026-11-13-q76-cell-transport.md.
