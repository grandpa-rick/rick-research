# PROVE 283 option (a): feasibility + exact mu for open26 S_16 instances

Grade: everything below was COMPUTED. None of it is proved.

## 1. Q search (qsearch.py, anneal.py -> qbest.json, anneal_w0.json)
I sampled 300 hook-walk Qs per instance, added the row and column superstandard Qs, then hill-climbed the
20 best via k<->k+1 swaps. Simulated annealing (4 restarts x 20k steps) did not improve any instance.
Also checked: rsk(x)[0]==Px, rsk(z)[0]==Pz, and Ld(x)==A.

| idx | lam | min l(z) | l(x) | gap | x<z |
|---|---|---|---|---|---|
|0|6433|52|33|19|Y|
|1|6433|52|29|23|Y|
|2|55411|53|34|19|Y|
|3|55411|53|28|25|Y|
|4|5533|57|34|23|Y|
|5|53332|57|34|23|Y|
|6|53332|57|26|31|Y|
|7|5443|52|31|21|Y|
|8|5443|52|31|21|Y|
|9|5443|47|24|23|Y|
|10|5443|47|24|23|Y|
|11|5542|43|28|15|Y|
|12|5542|43|28|15|Y|
|13|44431|55|42|**13**|Y|
|14|44431|55|42|**13**|Y|
|15|44431|47|32|15|Y|
|16|44431|47|32|15|Y|
|17|444211|62|39|23|Y|
|18|444211|62|39|23|Y|
|19|54331|49|32|17|Y|
|20|54331|49|32|17|Y|
|21|54421|52|25|27|Y|
|22|54421|52|31|21|Y|
|23|44332|61|38|23|Y|
|24|44332|61|38|23|Y|
|25|44422|57|38|19|Y|

The gap depends on Q. Under these Qs it gets as low as 13, compared with 19-23 before.

## 2. Bruhat interval sizes (interval.py: BFS down through covers, kept only if >= x)
- inst 13 (Q=qbest[13].Q): x=[7,3,2,11,10,6,5,1,15,9,8,4,16,14,13,12], z=[10,6,2,14,11,7,3,1,15,12,8,4,16,13,9,5],
  |[x,z]| = **20160** (exact; rank sizes 1,18,135,576,1593,3064,4269,4398,3355,1855,706,168,21,1).
  Five positions (0-based 2,7,8,11,12) are fixed on the whole interval. The flattened pair in S_11 is
  x'=[4,1,8,7,3,2,6,5,11,10,9], z'=[7,3,11,8,4,1,9,5,10,6,2]. The decide() toolkit still returns None on it.
- inst 14: |[x,z]| = 20160 (same rank profile).  inst 11: |[x,z]| = 86512 (exact, gap 15).

## 3. Exact KL via Dyer's path formula on the interval (dyer.c, kl.py)
R~_{u,y} = sum over Bruhat-graph paths u->y whose transposition labels increase in a reflection order (lex on position pairs).
P_{u,z} is computed for all u in [x,z], top-down, from q^l P(1/q) - P = sum R_{u,y}P_{y,z}. Only the interval is used.

**Validation (kl.py main)**: brute-force KL over all of S_4, S_5, S_6 (standard recursion). Inverse-invariance
fails 0 times. Max mu=1. Nontrivial-mu counts are 2/38/560, and S_4 matches the textbook pairs.
On random intervals [x,z] (x=e or random), Dyer gives:
- lex order: 0 failures out of 166, 879 and 2403 P-values in S_4, S_5 and S_6.
- revlex: 0 failures.
- Negative controls (colex and a random order, neither a reflection order) fail massively (e.g. 1400/1750 in S_6).

**Results**
| inst | lam | |[x,z]| | gap | P_{x,z} | mu(x,z) |
|---|---|---|---|---|---|
|13|44431|20160|13|1+8q+24q^2+35q^3+26q^4+9q^5+q^6|**1**|
|14|44431|20160|13|1+8q+24q^2+35q^3+26q^4+9q^5+q^6|**1**|
|11|5542|86512|15|1+11q+48q^2+106q^3+126q^4+80q^5+23q^6+q^7|**1**|

Cross-checks for inst 13 (crosscheck.py, recheck.py):
- revlex order gives the same P.
- The inverse pair (x^-1,z^-1) gives the same P.
- Three other Qs give the same P and mu=1. All have gap 13 and the same interval size, so this check is weak.
- The classical recursion P_{x,z} = P_{sx,sz} + qP_{x,sz} - sum mu(y,sz)... was run for each s in L(x)∩L(z)={1,5,9,13}.
  Its ingredients come from Dyer on different intervals ([sx,sz], [x,sz], [x,y]). All 4 match.

**Conclusion (computed):** mu(x,z)=1 for open26 instances 11, 13 and 14. Lemma I predicts 0, so as stated it
appears FALSE at S_16, assuming open26.json encodes (Px,Pz) in the rskmod.rsk convention used here.
Caveats: no fully independent second implementation exists (the recursion check reuses dyer.c on other intervals).
The Dyer code is validated only up to S_6.
Not yet run: the remaining 23 instances. Inst 12/15/16 likely have intervals around 1e5.
