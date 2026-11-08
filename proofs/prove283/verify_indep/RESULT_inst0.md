# PROVE 283 — independent verification, instance 0 (S_16)

x = [5,4,3,1,9,8,7,2,15,14,11,6,13,10,12,16] (l=33), z = [14,8,4,1,15,9,5,2,16,10,6,3,11,7,12,13] (l=52).
Everything here is my own code (kl.py, parab.py, parab2.py). I did not read dyer*.c or any other prove283/prove282 code.

## |[x,z]|
Full BFS over downward reflection covers from z, keeping w >= x (tableau Bruhat criterion), using kl.interval: **894,344** (probe.py, 135 s).

## Method for P
L(z) = {3,7,13}, R(z) = J = {1,2,3,5,6,7,9,10,11,13}. x is already maximal in W_I x W_J.
Deodhar's parabolic KL on W^J (minimal right-coset reps), using the left-module R^J recursion on a left descent s of tau:
sσ<σ: R^J(sσ,sτ); sσ>σ, sσ∈W^J: (q-1)R^J(σ,sτ)+qR^J(sσ,sτ); sσ∉W^J: q·R^J(σ,sτ) (the u=-1 case).
The inversion formula is applied on the W^J interval [x_min, z_min], and the result is P^J_{σ,τ} = P_{σw_J, τw_J}.
Left I-invariance (P constant on W_I y W_J) is also used: each double-coset orbit is solved once, and the full identity is still asserted for every solved y.
The convention was chosen empirically. With u=q there are hundreds of mismatches; with u=-1 there are none.

## Validation (against my earlier interval code, which was itself checked against brute force on all of S_4/S_5)
- parab.py (u=-1), random J (90% nonempty) and random pairs: S_5 752+1275 tests, S_6 440+965 tests, 0 mismatches (u=q: 315/607/257/564 mismatches).
- parab2.py (the optimised version that also uses the left-I orbits), arbitrary comparable random pairs where every z has nonempty L(z) and R(z): S_5 2048, S_6 1796, 0 mismatches (625 with nontrivial P).
- Gap-13 instance: parab.py and parab2.py both give 1+8q+24q^2+35q^3+26q^4+9q^5+q^6, which matches the earlier 374 s full-interval run.

## Instance 0 result
W^J interval: 22,208 elements, 5,525 orbit reps, 3.38M comparable pairs. Run time 222 s.
**P_{x,z} = 1+12q+62q^2+181q^3+328q^4+381q^5+279q^6+119q^7+26q^8+q^9, mu(x,z) = 1** (deg 9 = (52-33-1)/2).

**Verdict: AGREE** (|[x,z]| = 894,344, P_{x,z} and mu all match the claim).
