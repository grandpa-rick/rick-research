"""Cover ALL cells of a violator type by orbits under <right stars, sigma> (sigma = 1<->2 diagram automorphism,
w -> e w e, e = sign change of coordinate 1), deciding one certified cell per orbit.
usage: decide_all.py TYPE NCELLS seed"""
import sys, pickle, random, time, json
sys.path.insert(0, '/home/agent/projects/proofs/prove286'); sys.path.insert(0, '/home/agent/projects/proofs/wake285')
from decide import *
from orbit import orbit
def sigma(w):
    return (-w[0],) + w[1:] if False else tuple((-v if abs(v) == 1 else v) * (-1 if i == 0 else 1) for i, v in enumerate(w))
if __name__ == '__main__':
    K = sys.argv[1]; N = int(sys.argv[2]); random.seed(int(sys.argv[3]))
    T = C8[K]; tgt = T['dist']; dim = T['dim']
    tag = K.replace('[', '').replace(']', '').replace('.', '_').replace('+', 'P')
    logf = open(f'/home/agent/projects/proofs/prove286/all_{tag}.txt', 'a')
    def log(s): print(s, flush=True); logf.write(s + '\n'); logf.flush()
    # sigma sanity: automorphism swapping generators 1 and 2
    from d8lib import from_word
    w = from_word('1342', n); sw = from_word('2341', n); assert sigma(w) == sw, (sigma(w), sw)
    log(f'=== {K} dim {dim} ncells {N}')
    A = sorted({A for A, B in pickle.load(open('/home/agent/projects/proofs/wake285/targets8.pkl', 'rb'))[K]['cand']}, key=sorted)[0]
    xs = [inverse(u) for u in same_R(n, A)]; random.shuffle(xs)
    Bd = Bounder(n); pools = {}; covered = set(); seenP = set(); ncov = 0; M = MU(); orbs = []
    for x in xs:
        if ncov >= N: break
        if x in covered or x in seenP: continue
        P = f2_closure(x, n, cap=3000)
        if P is None: continue
        seenP |= P
        if len(P) > dim or not leq(dist(P), tgt): continue
        R = rdes(x)
        if R not in pools: pools[R] = same_R(n, R)
        U = bound(x, Bd, pools[R], log=lambda s: None)
        if not (len(U) == dim and dict(dist(U)) == tgt): continue
        O = orbit(U); O2 = orbit(frozenset(sigma(u) for u in U))
        cells = dict(O); cells.update(O2)
        new = [k for k in cells if not (cells[k] & covered)]
        assert all(not (C & covered) for C in cells.values()) or all(C <= covered for C in cells.values())
        res = kill_pairs(U, M, log)
        verd = Counter(r['verdict'] for r in res)
        orbs.append(dict(seed=word(x), R=sorted(R), orbit=len(O), sigma_orbit_same=bool(set(O) == set(O2)), cells=len(cells), verdicts=dict(verd)))
        for C in cells.values(): covered |= C
        ncov += len(cells)
        log(f'  ORBIT seed {word(x)} R={sorted(R)}: |O|={len(O)} |O u sigma O|={len(cells)} verdicts {dict(verd)} -> covered {ncov}/{N}')
        for r in res:
            if r['verdict'] != 'NO': log('  !! ' + json.dumps(r))
    log(f'  DONE {K}: covered {ncov}/{N} cells with {len(orbs)} orbits; pol calls {M.cox.ncalls}')
    log('  ' + json.dumps(orbs))
    M.cox.close()
