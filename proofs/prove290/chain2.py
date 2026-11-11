# Memory-light version of chain.py: Hom_B(V,T) via cyclic generator of V = X (x) Y; indecomposability
# taken from the independent Wake 289 sweep (klo.py end_algebra on the tableau model), keyed by (lambda, mu).
import sys, json, itertools, numpy as np
sys.path.insert(0, '/home/agent/projects/proofs/wake289/klo75')
sys.path.insert(0, '/home/agent/projects/proofs/prove290')
from klo import connected_shapes, is_ribbon, star, lam_mu, rref_null, build_module
from indmodel import dense, induce
from chain import shape_mod, tops, P

SW = {}
for fn in ['out_sweep_2_7.jsonl', 'out_sweep_8_8.jsonl']:
    for line in open('/home/agent/projects/proofs/wake289/klo75/' + fn):
        r = json.loads(line)
        if 'local' in r: SW[(tuple(r['shape'][0]), tuple(r['shape'][1]))] = r['local']

def gen_index(comps):
    cells = star(comps); B, act, s = build_module(cells); return s

def homB_cyclic(GV, g, dV, GT, dT, Bidx, nr=4, seed=0):
    # BFS tree on V basis from g (B generators map basis->basis or 0)
    pred = {g: None}; order = [g]; q = [g]
    while q:
        c = q.pop(0)
        for i in Bidx:
            col = GV[i][:, c]; nz = np.nonzero(col)[0]
            if len(nz) == 1 and nz[0] != c and nz[0] not in pred:
                t = nz[0]; pred[t] = (c, i); order.append(t); q.append(t)
    assert len(pred) == dV, 'V not cyclic on g'
    def F_of(t):
        F = np.zeros((dT, dV), dtype=np.int64); F[:, g] = t % P
        for v in order[1:]:
            c, i = pred[v]; F[:, v] = np.mod(GT[i] @ F[:, c], P)
        return F
    if not Bidx: return [F_of(np.eye(dT, dtype=np.int64)[c]) for c in range(dT)]
    rng = np.random.default_rng(seed)
    U = rng.integers(0, P, size=(dV, nr))
    cols = []
    for c in range(dT):
        e = np.zeros(dT, dtype=np.int64); e[c] = 1
        F = F_of(e)
        res = [np.mod(np.mod(GT[i] @ F, P) @ U - F @ np.mod(GV[i] @ U, P), P) for i in Bidx]
        cols.append(np.concatenate([x.ravel() for x in res]))
    A = np.stack(cols, axis=1) % P
    A = A[np.any(A != 0, axis=1)]
    N = rref_null(A, P) if A.shape[0] else [np.eye(dT, dtype=np.int64)[c] for c in range(dT)]
    Hs = []
    for t in N:
        F = F_of(t)
        for i in Bidx:
            assert not ((GT[i] @ F - F @ GV[i]) % P).any(), 'verification failed'
        Hs.append(F)
    return Hs

def run(compsX, compsY):
    GX, a, dX = shape_mod(compsX); GY, b, dY = shape_mod(compsY)
    sX, sY = gen_index(compsX), gen_index(compsY)
    N = a + b
    GM, dM = induce(GX, a, dX, GY, b, dY)
    reps = [w for w in itertools.permutations(range(1, N + 1))
            if all(w[j] < w[j + 1] for j in range(a - 1)) and all(w[j] < w[j + 1] for j in range(a, N - 1))]
    dV = dX * dY
    GV = {}
    for i in range(1, N):
        if i < a: GV[i] = np.kron(GX[i], np.eye(dY, dtype=np.int64))
        elif i > a: GV[i] = np.kron(np.eye(dX, dtype=np.int64), GY[i - a])
    Bidx = [i for i in range(1, N) if i != a]
    topsX = tops(GX, a, dX); topsY = tops(GY, b, dY)
    wit = []
    for k in range(1, min(a, b) + 1):
        blocks = [t for t, w in enumerate(reps) if sum(1 for v in w[a:] if v <= a) == k]
        cols = np.concatenate([np.arange(t * dV, (t + 1) * dV) for t in blocks])
        GT = {i: GM[i][np.ix_(cols, cols)] for i in Bidx}
        H = homB_cyclic(GV, sX * dY + sY, dV, GT, len(cols), Bidx)
        for (Di, ei) in topsX:
            for (Ej, dj) in topsY:
                Z = set(Di) | {a} | {a + e for e in Ej}
                blk = {}; c = 0
                for v in range(1, N + 1):
                    blk[v] = c
                    if v not in Z: c += 1
                inWZ = lambda w: all(blk[w[p]] == blk[p + 1] for p in range(N))
                ev = np.kron(ei, dj) % P
                fz = np.concatenate([ev if inWZ(reps[t]) else np.zeros(dV, dtype=np.int64) for t in range(len(reps))])
                for i in range(1, N):
                    assert not ((fz @ GM[i] - (1 if i in Z else 0) * fz) % P).any()
                fk = fz[cols]
                if any(((fk @ h) % P).any() for h in H): wit.append((k, tuple(sorted(Di)), tuple(sorted(Ej))))
    return dict(a=a, b=b, dM=dM, wit=wit)

def lastrow(c): return c[-1][1] - c[-1][0] + 1

def main(nlo, nhi, ncomp):
    CS = {m: connected_shapes(m) for m in range(1, nhi)}
    tot = bad = 0
    for n in range(nlo, nhi + 1):
        for comp in itertools.product(range(1, n), repeat=ncomp):
            if sum(comp) != n: continue
            for cs in itertools.product(*[CS[m] for m in comp]):
                rib = [is_ribbon(c) for c in cs]
                dr = any(rib[t] and rib[t + 1] for t in range(ncomp - 1))
                key = lam_mu(star(list(cs)))
                indM = SW.get(key)
                for split in range(1, ncomp):
                    X, Y = list(cs[:split]), list(cs[split:])
                    if any(rib[t] and rib[t+1] for t in range(split - 1)) or any(rib[t] and rib[t+1] for t in range(split, ncomp - 1)):
                        continue
                    r = run(X, Y); tot += 1
                    crit_ind = (len(r['wit']) == 0)
                    ok = (crit_ind == (not dr)) and (indM is None or indM == crit_ind)
                    if not is_ribbon(X[-1]) and r['wit']: ok = False
                    for (k, Di, Ej) in r['wit']:
                        if not (set(range(r['a'] - k + 1, r['a'])) <= set(Di) and set(range(1, k)) <= set(Ej)): ok = False
                    if not ok: bad += 1; print('BAD', cs, split, r, indM, flush=True)
            print('n', n, 'comp', comp, 'tot', tot, 'bad', bad, flush=True)
    print('DONE tot', tot, 'bad', bad)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
