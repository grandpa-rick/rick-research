# Sweep: classify, End dims, top labels. usage: python3 run.py n ribbon_cap
import sys, json, time
from shapes import *; from endo import endo
import numpy as np, scipy.sparse as sps
from scipy.sparse.csgraph import connected_components
def tops(lam, mu):
    """dim Hom(X, C_I) for every I subset [n-1]; C_I: pi_i -> 0 for i in I, 1 otherwise. Returns {I: mult}."""
    B, acts = action(lam, mu); m = len(B); n = sum(lam)-sum(mu); res = {}
    F = {i: np.asarray(f) for i, f in acts.items()}; ar = np.arange(m)
    for r in range(n):
        for I in itertools.combinations(range(1, n), r):
            I = set(I); zero = np.zeros(m, dtype=bool); E1 = []; E2 = []
            for i, f in F.items():
                fix = f == ar; kill = f < 0; sw = ~fix & ~kill
                if i in I:   # chi=0: phi_T = 0 for fixed T, phi_{s_iT}=0 for swaps
                    zero |= fix; zero[f[sw]] = True
                else:        # chi=1: phi_T = 0 for killed T, phi_{s_iT} = phi_T
                    zero |= kill; E1.append(ar[sw]); E2.append(f[sw])
            if E1:
                e1 = np.concatenate(E1); e2 = np.concatenate(E2)
                g = sps.csr_matrix((np.ones(len(e1)), (e1, e2)), shape=(m, m))
                k, lab = connected_components(g, directed=False)
            else: k, lab = m, ar
            bad = np.zeros(k, dtype=bool); bad[lab[zero]] = True
            c = int((~bad).sum())
            if c: res[''.join(map(str, sorted(I))) or '-'] = c
    return res
n = int(sys.argv[1]); cap = int(sys.argv[2]); labs = sys.argv[3].split(',') if len(sys.argv) > 3 else ['CONN', 'CONJ', 'RIBBON-PAIR']
import os
done = set()
if os.path.exists(f'out_n{n}.jsonl'):
    for l in open(f'out_n{n}.jsonl'):
        r = json.loads(l); done.add((tuple(r['lam']), tuple(r['mu'])))
out = open(f'out_n{n}.jsonl', 'a')
for lam, mu in basic_shapes(n):
    comps, rib, lab = classify(lam, mu)
    if lab not in labs or (lam, mu) in done: continue
    m = len(syt(lam, mu))
    if (lab == 'RIBBON-PAIR' and m > cap) or (lab == 'CONN' and m > int(os.environ.get('CONNCAP', 10**9))): 
        out.write(json.dumps(dict(lam=lam, mu=mu, lab=lab, m=m, skipped=True))+'\n'); continue
    t = time.time(); r = endo(lam, mu)
    rec = dict(lam=lam, mu=mu, lab=lab, comps=comps, rib=rib, m=m, srcW=len(r['srcW']), dimEnd=r['dimEnd'], dimJ=r['dimJ'], dimEndJ=r['dimEndJ'], sec=round(time.time()-t, 2))
    if lab == 'CONJ': rec['top'] = tops(lam, mu)
    out.write(json.dumps(rec)+'\n'); out.flush()
