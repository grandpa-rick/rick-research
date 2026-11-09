"""Find left-star orbits in D8 realising each violator type (orbit descent distribution == predicted)."""
import pickle, random, sys, time
from collections import Counter
from d8lib import *
n = 8
T = pickle.load(open('targets8.pkl', 'rb'))
want = set(sys.argv[1].split(',')) if len(sys.argv) > 1 else set(T)
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
Lx = {}
for k in want:
    for A, B in T[k]['cand']: Lx.setdefault(A, set()).add(k)
found = {}; tried = 0; seenorb = set(); t0 = time.time(); sizes = Counter()
def rand_elt():
    p = list(range(1, n+1)); random.shuffle(p)
    sg = [random.choice((1, -1)) for _ in range(n)]
    if sg.count(-1) % 2: sg[0] *= -1
    return tuple(a*b for a, b in zip(p, sg))
while len(found) < len(want) and time.time() - t0 < float(sys.argv[3] if len(sys.argv) > 3 else 600):
    w = rand_elt()
    L = ldes(w)
    if L not in Lx: continue
    if not (Lx[L] - set(found)): continue
    if w in seenorb: continue
    tried += 1
    orb = star_orbit(w, n, cap=1200)
    if orb is None: sizes['>1200'] += 1; continue
    seenorb |= orb
    sizes[len(orb)] += 1
    dist = Counter(ldes(u) for u in orb)
    for k in Lx[L] - set(found):
        if dict(dist) == T[k]['dist']:
            found[k] = (w, len(orb)); print('FOUND', k, w, word(w), len(orb), f'{time.time()-t0:.1f}s', flush=True)
print('tried', tried, 'orbit sizes', sorted(sizes.items(), key=str)[:40])
pickle.dump(found, open('reps_%s.pkl' % (sys.argv[2] if len(sys.argv) > 2 else '1'), 'wb'))
