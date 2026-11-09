"""Geck induction upper bound for left cells of D_n (coxeter3 labels: 1,2 fork on 3; chain 3..n).

Geck (2003, 'On the induction of Kazhdan-Lusztig cells'): for a parabolic W_I and a left cell G' of W_I,
X_I.G' is a union of left cells of W (X_I = minimal reps of left cosets wW_I).  Hence the left cell of
w = x.u (u in W_I) lies in X_I.G'(u).  We intersect over all maximal parabolics: U(w) = {v : for every I,
u_I(v) ~_L u_I(w) in W_I}.  Validated natively in D5/D6/D7 (validate()).
Native W_I cells come from coxeter3 `lcells` dumps in prove286/lc/.
"""
import re, sys, os
sys.path.insert(0, '/home/agent/projects/proofs/wake285')
from d8lib import rmul, rdes, ldes, length, word, from_word, inverse, lmul
LC = '/home/agent/projects/proofs/prove286/lc'

def perm_from_word(wd, m):
    p = list(range(1, m+2))
    for c in wd:
        i = int(c); p[i-1], p[i] = p[i], p[i-1]
    return tuple(p)

_cache = {}
def load(typ, m):
    """dict canonical-element -> cell id for native group typ m (A: S_{m+1} perms, D: signed perms)."""
    key = (typ, m)
    if key in _cache: return _cache[key]
    d = {}
    for line in open(f'{LC}/{typ}{m}_lc.txt'):
        mm = re.match(r'\s*(\d+)\s*:\s*\{(.*)\}', line)
        if not mm: continue
        cid = int(mm.group(1))
        for wd in mm.group(2).split(','):
            wd = wd.strip()
            if wd == '': wd = ''
            el = perm_from_word(wd, m) if typ == 'A' else from_word(wd, m)
            assert el not in d
            d[el] = cid
    _cache[key] = d
    return d

def components(n, k):
    """Components of the parabolic I = nodes minus {k} in D_n.  Each: (typ, m, {node: native label})."""
    nodes = set(range(1, n+1)) - {k}
    nb = {i: set() for i in range(1, n+1)}
    for a, b in [(1, 3), (2, 3)] + [(i, i+1) for i in range(3, n)]:
        nb[a].add(b); nb[b].add(a)
    comps = []; seen = set()
    for s in sorted(nodes):
        if s in seen: continue
        C = {s}; st = [s]
        while st:
            u = st.pop()
            for v in nb[u]:
                if v in nodes and v not in C: C.add(v); st.append(v)
        seen |= C
        C = sorted(C)
        if {1, 2, 3} <= set(C) and len(C) >= 4:   # D_j on nodes 1..j
            comps.append(('D', len(C), {c: c for c in C}))
        else:
            # type A chain; order it along the path
            if {1, 2, 3} <= set(C):   # D3 = A3 chain 1-3-2
                order = [1, 3, 2]
            elif C[0] in (1, 2) and len(C) > 1:   # chain c0 - 3 - 4 ... (c0 in {1,2}, 3 present)
                order = [C[0]] + [c for c in C if c >= 3]
            else:
                order = C
            comps.append(('A', len(C), {c: i+1 for i, c in enumerate(order)}))
    return comps

def right_part(w, I):
    """u in W_I with w = x u, x minimal in w W_I; returns reduced word (node labels) of u."""
    out = []
    while True:
        R = rdes(w) & I
        if not R: break
        s = min(R); out.append(s); w = rmul(w, s)
    return list(reversed(out))   # u = s_out[0] ... ; w_original = x * u

def comp_key(w, n, k, comps=None):
    if comps is None: comps = components(n, k)
    I = frozenset(range(1, n+1)) - {k}
    u = right_part(w, I)
    key = []
    for typ, m, lab in comps:
        sub = ''.join(str(lab[s]) for s in u if s in lab)
        if m == 1:
            key.append(len(sub) % 2)   # A1: cells {e},{s}
            continue
        el = perm_from_word(sub, m) if typ == 'A' else from_word(sub, m)
        key.append(load(typ, m)[el])
    return tuple(key)

def full_key(w, n, comps_all=None):
    if comps_all is None: comps_all = {k: components(n, k) for k in range(1, n+1)}
    return tuple(comp_key(w, n, k, comps_all[k]) for k in range(1, n+1))

def all_elements(n):
    from itertools import permutations, product
    for p in permutations(range(1, n+1)):
        for sg in product((1, -1), repeat=n):
            if sg.count(-1) % 2 == 0:
                yield tuple(a*b for a, b in zip(p, sg))

def validate(n):
    """Compare native D_n cells with Geck intersection classes."""
    nat = load('D', n)
    comps_all = {k: components(n, k) for k in range(1, n+1)}
    from collections import defaultdict
    cls = defaultdict(set); cell = defaultdict(set)
    for w, c in nat.items():
        cls[full_key(w, n, comps_all)].add(w); cell[c].add(w)
    # each native cell inside one class?
    bad = 0; exact = 0; sizes = []
    for c, S in cell.items():
        ks = {full_key(w, n, comps_all) for w in S}
        if len(ks) != 1: bad += 1; continue
        K = ks.pop()
        if cls[K] == S: exact += 1
        else: sizes.append((len(S), len(cls[K])))
    print(f'D{n}: {len(cell)} cells, {len(cls)} Geck classes, cells split across classes: {bad}, '
          f'exact: {exact}, non-exact (cell,class) sizes sample: {sorted(set(sizes))[:15]}')
    return bad, exact, sizes

if __name__ == '__main__':
    for n in map(int, sys.argv[1:]): validate(n)
