# PROVE 283 — independent verification of mu(x,z), instance 13 (S_16)

Code was written from scratch here: kl.py, validate.py, validate2.py, run16.py. Nothing in prove283/*.c, *.py or prove282/ was read.
Method: memoised R-polynomial recursion (strip common right/left descents first, then branch on a right descent of v),
then the inversion q^{l(z)-l(y)} P_{y,z}(1/q) - P_{y,z}(q) = sum_{y<t<=z} R_{y,t} P_{t,z}, solved top-down over [x,z].
Every y was checked for full consistency of the identity (assert). Bruhat order uses the tableau criterion. The interval
is built by BFS over downward reflection covers from z, keeping elements >= x. No Dyer path counting is used.

## Validation
- Tableau-criterion Bruhat order matches the transitive closure of reflection covers in S_4 and S_5 (0 mismatches).
- Brute force over the full group with the classical C'_s recursion (mu-correction): compared against the interval method
  on all 213 comparable pairs of S_4, all 3781 of S_5 (394 nontrivial), and 401 random pairs of S_6 (94 nontrivial,
  including (e,w0)). 0 mismatches.
- S_4: P_{1324,3412} = 1+q and P_{2143,4231} = 1+q; every P_{e,w} has constant term 1.

## S_16 instance
x = [7,3,2,11,10,6,5,1,15,9,8,4,16,14,13,12], z = [10,6,2,14,11,7,3,1,15,12,8,4,16,13,9,5]
- l(x) = 42, l(z) = 55, x <= z: TRUE
- |[x,z]| = 20160; comparable pairs inside the interval = 4,877,299
- **P_{x,z} = 1 + 8q + 24q^2 + 35q^3 + 26q^4 + 9q^5 + q^6**
- **mu(x,z) = 1** (coefficient of q^6, with (55-42-1)/2 = 6)
- L(x) = {1,2,4,5,6,8,9,10,12,13,14}, L(z) = {1,5,9,13}
- R(x) = R(z) = {1,2,4,5,6,7,9,10,11,13,14,15}
- Runtime: 374 s (single core, CPython 3.12); 201,391 memoised R-entries.

**Verdict: AGREE with the claim** (interval size, P_{x,z} and mu).
