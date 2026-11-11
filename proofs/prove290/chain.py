# Numerical check of the PROVE 290 proof chain for KLO Conj 7.5.
# M = X [x] Y, X = X_{C_1*...*C_j}, Y = X_{C_{j+1}*...}, in the explicit word model (indmodel.induce).
# Checks, per case:
#  (A) criterion: M decomposable <=> exists k>=1, top pair (i,j): f_{ij1} o Hom_B(V, M_k) != 0
#  (B) any witness k satisfies [a-k+1,a-1] in D_i and [1,k-1] in E_j
#  (C) if last comp of X is non-ribbon: no witness exists (that's the theorem)  [implied by A + data]
#  (D) witness => X is a direct summand of Ind(Res_{H_{a-k}} X [x] C_full)  (Key Lemma), tested via
#      random composite X -> L -> X invertible
import sys, itertools, numpy as np
sys.path.insert(0, '/home/agent/projects/proofs/wake289/klo75')
from klo import cells_of, build_module, connected_shapes, is_ribbon, star, rref_null, desL
from indmodel import dense, induce

P = 32003
rng = np.random.default_rng(7)

def shape_mod(comps):
    cells = star(comps); B, act, s = build_module(cells)
    return dense(act, len(B)), len(cells), len(B)

def homB(GV, GT, dV, dT, idx):
    """maps F: V -> T (dT x dV) with F GV_i = GT_i F for i in idx"""
    rows = [(np.kron(np.eye(dV, dtype=np.int64), GT[i]) - np.kron(GV[i].T, np.eye(dT, dtype=np.int64))) % P for i in idx]
    N = rref_null(np.vstack(rows), P) if rows else [np.eye(dV*dT, dtype=np.int64)[c] for c in range(dV*dT)]
    return [v.reshape(dT, dV, order='F') for v in N]

def tops(G, n, d):
    """all (Z, functional f as row vector) with f pi_i = chi_Z(i) f"""
    out = []
    for r in range(n):
        for Z in itertools.combinations(range(1, n), r):
            rows = [((G[i].T - (1 if i in Z else 0) * np.eye(d, dtype=np.int64)) % P) for i in range(1, n)]
            N = rref_null(np.vstack(rows), P) if rows else [np.ones(d, dtype=np.int64)]
            for v in N: out.append((frozenset(Z), v))
    return out

def is_indec(G, n, d):
    E = homB(G, G, d, d, list(range(1, n)))
    if len(E) == 1: return True, 1
    F = sum(int(rng.integers(P)) * e for e in E) % P
    c = (int(np.trace(F)) * pow(d, P - 2, P)) % P
    A = (F - c * np.eye(d, dtype=np.int64)) % P
    R = A.copy()
    for _ in range(int(np.ceil(np.log2(d))) + 1):
        R = np.mod(R @ R, P)
    return (not R.any()), len(E)

def run(compsX, compsY):
    GX, a, dX = shape_mod(compsX); GY, b, dY = shape_mod(compsY)
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
    indM, nE = is_indec(GM, N, dM)
    witnesses = []
    for k in range(1, min(a, b) + 1):
        blocks = [t for t, w in enumerate(reps) if sum(1 for v in w[a:] if v <= a) == k]
        cols = np.concatenate([np.arange(t * dV, (t + 1) * dV) for t in blocks])
        GT = {i: GM[i][np.ix_(cols, cols)] for i in Bidx}
        # sanity: block is B-stable
        for i in Bidx:
            assert not GM[i][np.ix_(np.setdiff1d(np.arange(dM), cols), cols)].any()
        H = homB(GV, GT, dV, len(cols), Bidx)
        for (Di, ei) in topsX:
            for (Ej, dj) in topsY:
                Z = set(Di) | {a} | {a + e for e in Ej}
                # f_{ij1} on M: solve for functional with label Z restricted to agree with ei x dj on 1 (x) V
                # explicit formula: f(T_w (x) v) = [w in W_Z] (ei x dj)(v)
                def inWZ(w):
                    # w (one-line, positions->values) in parabolic W_Z: every value moved stays in its Z-block
                    blk = {}; c = 0
                    for v in range(1, N + 1):
                        blk[v] = c
                        if v not in Z: c += 1
                    return all(blk[w[p]] == blk[p + 1] for p in range(N))
                ev = np.kron(ei, dj) % P
                fz = np.concatenate([ev if inWZ(reps[t]) else np.zeros(dV, dtype=np.int64) for t in range(len(reps))])
                # check fz is a module map M -> C_Z
                for i in range(1, N):
                    assert not ((fz @ GM[i] - (1 if i in Z else 0) * fz) % P).any(), "f_ij1 formula not a module map"
                fk = fz[cols]
                if any(((fk @ h) % P).any() for h in H):
                    witnesses.append((k, tuple(sorted(Di)), tuple(sorted(Ej))))
    return dict(a=a, b=b, dM=dM, ind=indM, nE=nE, wit=witnesses)

def main2(nmax):
    CS = {m: connected_shapes(m) for m in range(1, nmax)}
    bad = 0; tot = 0
    for n in range(2, nmax + 1):
        for a in range(1, n):
            b = n - a
            for C1 in CS[a]:
                for C2 in CS[b]:
                    r = run([C1], [C2]); tot += 1
                    rib = (is_ribbon(C1), is_ribbon(C2))
                    ok = (r['ind'] == (len(r['wit']) == 0)) and (r['ind'] == (not (rib[0] and rib[1])))
                    kmax_ok = all(k <= (C1[-1][1] - C1[-1][0] + 1) and k <= (C2[0][1] - C2[0][0] + 1) for (k, _, _) in r['wit'])
                    if not ok or not kmax_ok:
                        bad += 1; print('BAD', C1, C2, rib, r, flush=True)
        print('n', n, 'tot', tot, 'bad', bad, flush=True)

def keylemma_summand(compsX, k):
    """is X a direct summand of Ind_{H_{a-k} x H_k}^{H_a}(Res_{H_{a-k}} X [x] C_full)?"""
    GX, a, dX = shape_mod(compsX)
    GR = {i: GX[i] for i in range(1, a - k)}
    Gc = {i: np.ones((1, 1), dtype=np.int64) for i in range(1, k)}
    GL, dL = induce(GR, a - k, dX, Gc, k, 1)
    H1 = homB(GX, GL, dX, dL, list(range(1, a)))
    H2 = homB(GL, GX, dL, dX, list(range(1, a)))
    if not H1 or not H2: return False
    for t in range(3):
        F1 = sum(int(rng.integers(P)) * h for h in H1) % P
        F2 = sum(int(rng.integers(P)) * h for h in H2) % P
        C = np.mod(F2 @ F1, P)
        if len(rref_null(C, P)) == 0: return True
    return False

def main3(nmax):
    CS = {m: connected_shapes(m) for m in range(1, nmax)}
    tot = bad = 0
    for n in range(3, nmax + 1):
        for comp in itertools.product(range(1, n), repeat=3):
            if sum(comp) != n: continue
            for cs in itertools.product(*[CS[m] for m in comp]):
                rib = [is_ribbon(c) for c in cs]
                dr = (rib[0] and rib[1]) or (rib[1] and rib[2])
                for split in (1, 2):
                    X, Y = list(cs[:split]), list(cs[split:])
                    rX = (rib[0] and rib[1]) if split == 2 else False
                    rY = (rib[1] and rib[2]) if split == 1 else False
                    if rX or rY: continue   # factor itself decomposable; criterion needs indecomposable factors
                    r = run(X, Y); tot += 1
                    ok = (r['ind'] == (len(r['wit']) == 0)) and (r['ind'] == (not dr))
                    lastX = X[-1]
                    if not is_ribbon(lastX) and r['wit']: ok = False
                    if not ok: bad += 1; print('BAD3', cs, split, r, flush=True)
        print('n3', n, 'tot', tot, 'bad', bad, flush=True)

def mainKL(nmax):
    CS = {m: connected_shapes(m) for m in range(1, nmax)}
    tot = bad = 0
    for n in range(2, nmax + 1):
        for a in range(1, n):
            for C1 in CS[a]:
                for C2 in CS[n - a]:
                    r = run([C1], [C2])
                    for k in sorted({w[0] for w in r['wit']}):
                        tot += 1
                        if not keylemma_summand([C1], k): bad += 1; print('KLBAD', C1, C2, k, flush=True)
        print('KL n', n, 'tot', tot, 'bad', bad, flush=True)

if __name__ == '__main__':
    m = sys.argv[1]; nmax = int(sys.argv[2])
    {'2': main2, '3': main3, 'kl': mainKL}[m](nmax)
