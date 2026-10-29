"""Q50 compute (Wake 264): Sum_{rho ⊆ kappa ⊆ stair_m} V(kappa/rho) =? 3^m.

Definitions (proofs/2026-10-30-q48-ls-vmap.md): strict partitions with parts <= m <-> shifted diagrams in
{(a,b): 0<=a<=b<=m-1}; diagonal d=b-a; V-map on theta=kappa/rho = strictly order-preserving g: theta->{e<o}
with g=e on diagonal (d=0) boxes. V(theta) = #V-maps.

Particle model: strict partition <-> S ⊆ {1..m} (set of parts). Addable box on row with part p<m (p+1 notin S) =
hop p->p+1 (box diagonal p); new row (diagonal box) addable iff 1 notin S = injection at site 1.
"""
import itertools, sys
from collections import defaultdict
from functools import lru_cache

def strict_parts(m):
    for r in range(m + 1):
        for c in itertools.combinations(range(m, 0, -1), r):
            yield tuple(c)  # decreasing

def diagram(lam):
    return frozenset((a, a + j) for a, p in enumerate(lam) for j in range(p))

def vmaps_brute(kap, rho):
    D = diagram(kap) - diagram(rho)
    if not diagram(rho) <= diagram(kap):
        return 0
    boxes = sorted(D)
    n = len(boxes)
    less = [(i, j) for i in range(n) for j in range(n) if i != j and boxes[i][0] <= boxes[j][0] and boxes[i][1] <= boxes[j][1]]
    cnt = 0
    for mask in range(1 << n):  # bit=1 -> o
        ok = True
        for i in range(n):
            if (mask >> i) & 1 and boxes[i][1] == boxes[i][0]:
                ok = False; break
        if not ok: continue
        for i, j in less:  # need g(i) < g(j): i=e, j=o
            if (mask >> i) & 1 or not (mask >> j) & 1:
                ok = False; break
        if ok: cnt += 1
    return cnt

def steps(S, m, inject):
    """All S' reachable by one parallel update: any subset of movable particles hop right; optional injection."""
    S = frozenset(S)
    movers = [p for p in S if p < m and (p + 1) not in S]
    if inject and 1 not in S:
        movers.append(0)  # reservoir particle at site 0
    for r in range(len(movers) + 1):
        for sub in itertools.combinations(movers, r):
            T = set(S)
            for p in sub:
                T.discard(p); T.add(p + 1)
            yield frozenset(T), len(sub)

def S_of(lam): return frozenset(lam)
def lam_of(S): return tuple(sorted(S, reverse=True))

def triples(m, inj1=True, inj2=False):
    """V[(kappa,rho)] = #lambda; via particle model."""
    V = defaultdict(int)
    for rho in strict_parts(m):
        for S1, _ in steps(S_of(rho), m, inj1):
            for S2, _ in steps(S1, m, inj2):
                V[(lam_of(S2), rho)] += 1
    return V

if __name__ == "__main__":
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    BR = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    for m in range(1, M + 1):
        V = triples(m)
        tot = sum(V.values())
        line = f"m={m}: total={tot} 3^m={3**m} {'OK' if tot == 3**m else 'FAIL'}"
        if m <= BR:  # cross-check particle model against brute-force V-map count, all pairs
            bad = 0
            for kap in strict_parts(m):
                for rho in strict_parts(m):
                    if vmaps_brute(kap, rho) != V.get((kap, rho), 0):
                        bad += 1
            line += f"  brute V-map vs particle mismatches: {bad}"
        print(line, flush=True)
