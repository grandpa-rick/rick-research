"""Fast full KL for S_n (n<=7), same conventions as prove281/klperm.py
(one-line perms, left mult s acts on VALUES s<->s+1, L(w)={s: pos[s+1]<pos[s]}).
Polynomials packed into python ints, base B=2^16 (exact: linear ops over Z, final coeffs in [0,B)).
Returns W (list sorted by length), idx, P (list of dicts: P[w][x] = packed poly, keys = lower interval of w). Computed tool."""
from itertools import permutations
SH = 16; MASK = (1 << SH) - 1
def inv(w): return sum(1 for i in range(len(w)) for j in range(i+1, len(w)) if w[i] > w[j])
def lmul(i, w): return tuple(i+1 if a == i else i if a == i+1 else a for a in w)
def Ldes(w):
    pos = {a: k for k, a in enumerate(w)}; return [i for i in range(1, len(w)) if pos[i+1] < pos[i]]
def unpack(p):
    out = []
    while p: out.append(p & MASK); p >>= SH
    return tuple(out)
def full_kl_fast(n):
    W = sorted(permutations(range(1, n+1)), key=inv); N = len(W)
    idx = {w: k for k, w in enumerate(W)}; ln = [inv(w) for w in W]
    LM = [[idx[lmul(s, w)] for s in range(1, n)] for w in W]   # LM[k][s-1]
    LD = [set(Ldes(w)) for w in W]
    P = [None]*N; mut = [[] for _ in range(N)]
    for w in range(N):
        if ln[w] == 0: P[w] = {w: 1}; continue
        s = min(LD[w]); v = LM[w][s-1]; Pv = P[v]
        below = set(Pv); below.update(LM[x][s-1] for x in Pv)
        terms = [(z, m, (ln[w]-ln[z])//2) for z, m in mut[v] if s in LD[z]]
        Pw = {}; lw = ln[w]
        for x in below:
            sx = LM[x][s-1]; a = Pv.get(sx, 0); b = Pv.get(x, 0)
            if s in LD[x]: col = a + (b << SH)
            else: col = (a << SH) + b
            for z, m, sh in terms:
                pz = P[z].get(x)
                if pz: col -= m * (pz << (SH*sh))
            Pw[x] = col
            d = lw - ln[x]
            if d % 2 == 1:
                c = (col >> (SH*((d-1)//2))) & MASK
                if c: mut[w].append((x, c))
        P[w] = Pw
    return W, idx, ln, P
if __name__ == "__main__":
    import sys, time, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../prove281'))
    from klperm import full_kl
    for n in (4, 5, 6):
        t = time.time(); W, idx, ln, P = full_kl_fast(n); t1 = time.time()-t
        W2, P2, _ = full_kl(n)
        cnt = 0; bad = 0
        for (x, y), p in P2.items():
            cnt += 1
            q = P[idx[y]].get(idx[x])
            if q is None or unpack(q) != tuple(p): bad += 1
        tot = sum(len(d) for d in P)
        print(n, "pairs klperm", cnt, "fast", tot, "mismatch", bad, "time", round(t1, 2))
