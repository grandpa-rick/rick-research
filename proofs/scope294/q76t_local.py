"""Q76 refinements (computed, 2026-11-13). R-global (Q76-T'), R-local (right {s_i,s_{i+1}} star op on all Bruhat
pairs), R-local-cell (x,y same recording tableau Q = same left cell in klfast convention), R-interval (Hasse iso).
Right mult by s_i swaps POSITIONS i,i+1; right descent i: w[i-1]>w[i]."""
import sys, time, random
from collections import defaultdict, Counter
from klfast import full_kl_fast, unpack
from q76t_s7 import interval_graph, rsk
from networkx.algorithms.isomorphism import DiGraphMatcher

def rmul(w, i): w = list(w); w[i-1], w[i] = w[i], w[i-1]; return tuple(w)
def rdes(w, i): return w[i-1] > w[i]

def star(w, i):
    """right {s_i,s_{i+1}} star; returns (w*, which) with which in {0:'s',1:'t'} or None."""
    a, b = rdes(w, i), rdes(w, i+1)
    if a == b: return None
    for which, j in ((0, i), (1, i+1)):
        v = rmul(w, j)
        if rdes(v, i) != rdes(v, i+1): return v, which
    raise RuntimeError

def run(n, out, iso_sample=2000, seed=1):
    t0 = time.time()
    W, idx, ln, P = full_kl_fast(n); N = len(W)
    R = [rsk(w) for w in W]; Qt = [r[1] for r in R]
    # ---- R-global ----
    byQ = defaultdict(dict)
    for k, (pt, qt) in enumerate(R): byQ[qt][pt] = k
    grp = defaultdict(dict); allQ = defaultdict(set); lens = defaultdict(set)
    for Q, d in byQ.items():
        it = list(d.items())
        for P1, x in it:
            for P2, y in it:
                key = (P1, P2); allQ[key].add(Q)
                p = P[y].get(x)
                if p is not None: grp[key][Q] = unpack(p); lens[key].add(ln[y]-ln[x])
    full = [k for k in grp if len(grp[k]) == len(allQ[k])]
    fullc = [k for k in full if len(lens[k]) == 1]
    nontriv = [k for k in fullc if any(v != (1,) for v in grp[k].values())]
    viol = [k for k in fullc if len(set(grp[k].values())) > 1]
    out(f"n={n} R-global (Q76-T'): all-Q-comparable={len(full)}, +const length diff={len(fullc)}, nontrivial={len(nontriv)}, VIOLATIONS={len(viol)}")
    for k in viol[:5]: out(f"   VIOL {k}: {grp[k]}")
    # ---- R-local ----
    ST = [[None]*(n-2) for _ in range(N)]
    for k, w in enumerate(W):
        for i in range(1, n-1):
            r = star(w, i)
            if r: ST[k][i-1] = (idx[r[0]], r[1])
    C = Counter(); ex = defaultdict(list); samereflfail = 0; samereflfail_cell = 0
    same_inst = []; same_inst_cell = []
    for y in range(N):
        Py = P[y]
        for x, px in Py.items():
            for i in range(n-2):
                sx, sy = ST[x][i], ST[y][i]
                if sx is None or sy is None: continue
                xs, wx = sx; ys, wy = sy
                cell = Qt[x] == Qt[y]
                d0 = ln[y]-ln[x]; d1 = ln[ys]-ln[xs]
                dirn = 'same' if d0 == d1 else 'opp'
                for tag in (('all',) + (('cell',) if cell else ())):
                    C[(tag, dirn, 'inst')] += 1
                    q = P[ys].get(xs)
                    if q is None:
                        C[(tag, dirn, 'notle')] += 1
                        if dirn == 'same' and len(ex[(tag, 'notle')]) < 5:
                            ex[(tag, 'notle')].append((W[x], W[y], W[xs], W[ys], unpack(px), None))
                    elif q != px:
                        C[(tag, dirn, 'Pdiff')] += 1
                        if dirn == 'same' and len(ex[(tag, 'Pdiff')]) < 5:
                            ex[(tag, 'Pdiff')].append((W[x], W[y], W[xs], W[ys], unpack(px), unpack(q)))
                    else:
                        C[(tag, dirn, 'Peq')] += 1
                    if dirn == 'same':
                        if wx != wy: C[(tag, 'same', 'diffrefl')] += 1
                        if q is not None and q == px and px != 1: C[(tag, 'same', 'nontrivPeq')] += 1
                if dirn == 'same':
                    same_inst.append((x, y, xs, ys))
                    if cell: same_inst_cell.append((x, y, xs, ys))
    for tag in ('all', 'cell'):
        for dirn in ('same', 'opp'):
            out(f"n={n} R-local[{tag}] {dirn}: inst={C[(tag,dirn,'inst')]} x*<=y* fails={C[(tag,dirn,'notle')]} "
                f"P differs={C[(tag,dirn,'Pdiff')]} P equal={C[(tag,dirn,'Peq')]}"
                + (f" nontrivial-P-equal={C[(tag,'same','nontrivPeq')]} different-simple-refl={C[(tag,'same','diffrefl')]}" if dirn == 'same' else ""))
        for kind in ('notle', 'Pdiff'):
            for e in ex[(tag, kind)]: out(f"   CE[{tag},{kind}] x={e[0]} y={e[1]} x*={e[2]} y*={e[3]} P_xy={e[4]} P_x*y*={e[5]}")
    # ---- R-interval ----
    rng = random.Random(seed)
    for tag, L in (('all', same_inst), ('cell', same_inst_cell)):
        # prioritise nontrivial-P instances, then fill with random
        nt = [e for e in L if P[e[1]][e[0]] != 1]
        smp = nt if len(nt) <= iso_sample // 2 else rng.sample(nt, iso_sample // 2)
        rest = [e for e in L if P[e[1]][e[0]] == 1]
        k = min(len(rest), iso_sample - len(smp))
        smp = smp + rng.sample(rest, k)
        if len(L) <= iso_sample: smp = L
        bad = 0; badex = []
        for x, y, xs, ys in smp:
            G1 = interval_graph(x, y, P, ln); G2 = interval_graph(xs, ys, P, ln)
            if not DiGraphMatcher(G1, G2).is_isomorphic():
                bad += 1
                if len(badex) < 3: badex.append((W[x], W[y], W[xs], W[ys], G1.number_of_nodes(), G2.number_of_nodes()))
        out(f"n={n} R-interval[{tag}] same-dir: tested {len(smp)} of {len(L)} (nontrivial-P among tested: "
            f"{sum(1 for e in smp if P[e[1]][e[0]] != 1)}), NON-isomorphic={bad}")
        for e in badex: out(f"   nonISO x={e[0]} y={e[1]} x*={e[2]} y*={e[3]} sizes {e[4]},{e[5]}")
    out(f"n={n} time {time.time()-t0:.1f}s")

if __name__ == "__main__":
    lines = []
    def out(s): print(s, flush=True); lines.append(s)
    ns = [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7]
    for n in ns: run(n, out)
    open('q76t_local_raw.txt', 'w').write("\n".join(lines) + "\n")
