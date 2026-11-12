# Basic skew shapes, components, ribbon flags, SYT, 0-Hecke action (KLO 2310.20571 convention).
import itertools
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for p in partitions(n-k, k): yield (k,)+p
def subpartitions(lam):
    """all mu subset lam (len(mu)=len(lam), zeros allowed) with mu_i < lam_i"""
    def rec(i, prev):
        if i == len(lam): yield (); return
        for m in range(min(prev, lam[i]-1), -1, -1):
            for r in rec(i+1, m): yield (m,)+r
    yield from rec(0, 10**9)
def compositions(n):
    if n == 0: yield (); return
    for k in range(1, n+1):
        for c in compositions(n-k): yield (k,)+c
def basic_shapes(n):
    """basic skew shapes lam/mu, |lam/mu|=n, no empty rows/cols, translation-normalised (mu_last=0, column 0 used).
    Built bottom-up from row lengths r: mu_i in [max(mu_{i+1}, lam_{i+1}-r_i), lam_{i+1}] (lam_{i+1}>=mu_i <=> no empty column)."""
    out = []
    for r in compositions(n):
        k = len(r)
        def rec(i, mu_next, lam_next, acc):
            if i < 0: 
                mu = tuple(m for m, _ in acc); lam = tuple(l for _, l in acc)
                out.append((lam, mu)); return
            for m in range(max(mu_next, lam_next - r[i]), lam_next + 1):
                rec(i-1, m, m + r[i], [(m, m + r[i])] + acc)
        rec(k-2, 0, r[-1], [(0, r[-1])])
    return out
def cells(lam, mu): return [(i, j) for i in range(len(lam)) for j in range(mu[i], lam[i])]
def components(lam, mu):
    """row-blocks; rows i,i+1 edge-connected iff lam_{i+1} > mu_i. Listed top (NE) to bottom (SW)."""
    comps = []; cur = [0]
    for i in range(1, len(lam)):
        if lam[i] > mu[i-1]: cur.append(i)
        else: comps.append(cur); cur = [i]
    comps.append(cur)
    return comps
def is_ribbon(lam, mu, rows):
    for i in rows[:-1]:
        # 2x2 square in rows i,i+1: overlap of [mu_i,lam_i) and [mu_{i+1},lam_{i+1}) of size>=2
        lo = max(mu[i], mu[i+1]); hi = min(lam[i], lam[i+1])
        if hi - lo >= 2: return False
    return True
def classify(lam, mu):
    comps = components(lam, mu)
    rib = [is_ribbon(lam, mu, r) for r in comps]
    if len(comps) == 1: lab = 'CONN'
    elif any(rib[k] and rib[k+1] for k in range(len(rib)-1)): lab = 'RIBBON-PAIR'
    else: lab = 'CONJ'
    return comps, rib, lab
def syt(lam, mu):
    C = cells(lam, mu); n = len(C); res = []
    T = {}
    def addable(c):
        i, j = c
        if (i, j-1) in Cs and (i, j-1) not in T: return False
        if (i-1, j) in Cs and (i-1, j) not in T: return False
        return True
    Cs = set(C)
    def rec(k):
        if k > n: res.append(dict(T)); return
        for c in C:
            if c not in T and addable(c):
                T[c] = k; rec(k+1); del T[c]
    rec(1)
    # store as tuple pos[k] = cell of entry k
    out = []
    for t in res:
        pos = [None]*(n+1)
        for c, k in t.items(): pos[k] = c
        out.append(tuple(pos[1:]))
    return out
def action(lam, mu):
    """returns basis list and for each i in 1..n-1 an array f_i: f_i[t] = t (fixed), -1 (zero), or index of s_i t."""
    B = syt(lam, mu); idx = {b: k for k, b in enumerate(B)}; n = sum(lam) - sum(mu)
    acts = {}
    for i in range(1, n):
        f = []
        for t, b in enumerate(B):
            ci, cj = b[i-1], b[i]   # cells of entries i, i+1
            if ci[1] < cj[1]: f.append(t)
            elif ci[1] == cj[1]: f.append(-1)
            else:
                nb = list(b); nb[i-1], nb[i] = nb[i], nb[i-1]; f.append(idx[tuple(nb)])
        acts[i] = f
    return B, acts
