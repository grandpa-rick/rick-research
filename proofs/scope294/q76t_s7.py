"""Q76-T scan (computed). Key = (P1,P2) [left-cell convention of cellinv3: x_Q=RSK^-1(P1,Q)];
dual: key=(Q1,Q2) varying P. Uses klfast (validated vs klperm n<=6) and cellinv.py's rsk."""
import sys, time
from collections import defaultdict, Counter
from klfast import full_kl_fast, unpack
exec(open('cellinv.py').read().split("for n in range")[0].split("from collections")[1].split("\n",1)[1])
import networkx as nx
from networkx.algorithms.isomorphism import DiGraphMatcher

def interval_graph(x, y, P, ln):
    els = [z for z in P[y] if x in P[z]]
    G = nx.DiGraph(); G.add_nodes_from(els)
    byl = defaultdict(list)
    for z in els: byl[ln[z]].append(z)
    for z in els:
        for u in byl[ln[z]+1]:
            if z in P[u]: G.add_edge(z, u)
    return G

def scan(n, dual=False, iso=True, out=print):
    t = time.time()
    W, idx, ln, P = full_kl_fast(n)
    R = []
    for w in W:
        a, b = rsk(w); R.append((b, a) if dual else (a, b))   # R[k] = (keytab, fibertab)
    cells = defaultdict(lambda: defaultdict(list))  # fibertab -> keytab -> elem (unique)
    byQ = defaultdict(dict)
    for k, (kt, ft) in enumerate(R): byQ[ft][kt] = k
    grp = defaultdict(dict); allQ = defaultdict(set)
    for Q, d in byQ.items():
        items = list(d.items())
        for P1, x in items:
            for P2, y in items:
                key = (P1, P2); allQ[key].add(Q)
                p = P[y].get(x)
                if p is not None: grp[key][Q] = unpack(p)
    varying = [k for k, d in grp.items() if len(set(d.values())) > 1]
    full = [k for k, d in grp.items() if len(d) == len(allQ[k])]
    nontriv = [k for k in full if any(v != (1,) for v in grp[k].values())]
    multiQ = [k for k in nontriv if len(allQ[k]) > 1]
    viol = [k for k in full if len(set(grp[k].values())) > 1]
    out(f"n={n} dual={dual}: keys(with some comparable Q)={len(grp)} varying-overall={len(varying)} "
        f"all-Q-comparable={len(full)} nontrivP={len(nontriv)} nontriv&>1Q={len(multiQ)} VIOLATIONS={len(viol)}")
    out(f"   shapes of all-Q-comparable keys: {dict(Counter(tuple(map(len,k[0])) for k in full))}")
    out(f"   nontrivial poly distribution (per key): {dict(Counter(tuple(sorted(set(grp[k].values()))) for k in nontriv))}")
    out(f"   nontrivial keys by shape: {dict(Counter(tuple(map(len,k[0])) for k in nontriv))}")
    for k in viol[:10]:
        d = grp[k]; out(f"   VIOLATION {k}: " + "; ".join(f"{p}: e.g. Q={next(Q for Q in d if d[Q]==p)}" for p in set(d.values())))
    # control detail: varying keys among non-full
    out(f"   control: varying keys that are NOT all-Q-comparable = {len([k for k in varying if k not in set(full)])}")
    if iso:
        noniso = 0; sizes = []
        for k in nontriv:
            Gs = []
            for Q in allQ[k]:
                x = byQ[Q][k[0]]; y = byQ[Q][k[1]]
                Gs.append(interval_graph(x, y, P, ln))
            sizes.append(Gs[0].number_of_nodes())
            ok = all(DiGraphMatcher(Gs[0], G).is_isomorphic() for G in Gs[1:])
            if not ok:
                noniso += 1; out(f"   NON-ISOMORPHIC intervals for key {k}: sizes {[G.number_of_nodes() for G in Gs]}")
        out(f"   interval-iso gate: {len(nontriv)} nontriv keys, non-isomorphic={noniso}, interval sizes={sorted(Counter(sizes).items())}")
    out(f"   time {time.time()-t:.1f}s")
    return grp, allQ, full, nontriv

if __name__ == "__main__":
    lines = []
    def out(s): print(s, flush=True); lines.append(s)
    for n in (5, 6, 7):
        for dual in (False, True):
            scan(n, dual, out=out)
    open('q76t_s7_raw.txt', 'w').write("\n".join(lines) + "\n")
