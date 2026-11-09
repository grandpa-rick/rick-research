"""Count non-local candidate mu-edges between P1 and the other same-R pieces; time persistent coxeter3 pol calls."""
import pickle, time, random
from d8lib import *
g = pickle.load(open('glue_280.pkl', 'rb')); P1 = list(g['P1']); Ps = g['P2s']
L = {}; ln = {}
for P in [P1] + [list(p) for p in Ps]:
    for u in P: L[u] = ldes(u); ln[u] = length(u)
pairs = []   # (lo, hi): lo < hi, L(lo) strictly contains L(hi), odd gap  (hi in one piece, lo in another)
for pi, P in enumerate(Ps):
    for y in P:
        for u in P1:
            for lo, hi in ((y, u), (u, y)):
                if ln[lo] < ln[hi] and (ln[hi]-ln[lo]) % 2 == 1 and L[lo] > L[hi]:
                    pairs.append((pi, lo, hi))
print('non-local candidate pairs P1<->others (length/descent prefilter, before Bruhat):', len(pairs))
random.seed(0); samp = random.sample(pairs, 40)
C = Cox('D', 8); t = time.time(); nz = 0; nb = 0
for pi, lo, hi in samp:
    P = C.pol(word(lo), word(hi))
    if P is None: nb += 1; continue
    if mu_from(P, ln[lo], ln[hi]): nz += 1
dt = time.time() - t
print(f'40 pol calls: {dt:.1f}s ({dt/40:.2f}s/call); not-Bruhat {nb}; mu!=0 {nz}')
C.close()
