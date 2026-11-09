"""Find D8 left cells (as F2-closures, KL-free) realising violator types; also test on D6/D7 vs coxeter3."""
import pickle, random, sys, time
from collections import Counter
from d8lib import *
n = 8
T = pickle.load(open('targets8.pkl', 'rb'))
want = sys.argv[1].split('|') if sys.argv[1] != 'all' else list(T)
random.seed(int(sys.argv[2])); tmax = float(sys.argv[3])
Lx = {}
for k in want:
    for A, B in T[k]['cand']: Lx.setdefault(A, set()).add(k)
found = {}; tried = 0; seen = set(); t0 = time.time(); sizes = Counter()
def rand_elt():
    p = list(range(1, n+1)); random.shuffle(p)
    sg = [random.choice((1, -1)) for _ in range(n)]
    if sg.count(-1) % 2: sg[0] *= -1
    return tuple(a*b for a, b in zip(p, sg))
while len(found) < len(want) and time.time() - t0 < tmax:
    w = rand_elt(); L = ldes(w)
    if L not in Lx or not (Lx[L] - set(found)) or w in seen: continue
    tried += 1
    cl = f2_closure(w, n, cap=1500)
    if cl is None: sizes['>1500'] += 1; continue
    seen |= cl; sizes[len(cl)] += 1
    dist = dict(Counter(ldes(u) for u in cl))
    for k in Lx[L] - set(found):
        if dist == T[k]['dist']:
            found[k] = (w, len(cl)); print('FOUND', k, w, len(cl), f'{time.time()-t0:.1f}s', flush=True)
print('tried', tried, 'closure sizes', sorted(sizes.items(), key=str))
old = {}
try: old = pickle.load(open('reps8.pkl', 'rb'))
except Exception: pass
old.update(found); pickle.dump(old, open('reps8.pkl', 'wb'))
