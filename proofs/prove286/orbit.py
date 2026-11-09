"""Right-star orbit of a left cell (KL-free).  KL79 Thm 4.3 / record Lemma S (right version):
if a left cell G lies in D_R(s,t) then G* is a left cell and x -> x* is a W-graph isomorphism
(preserves L and mu~).  So a twin verdict is constant along the orbit.  usage: orbit.py rep.pkl"""
import sys, pickle
sys.path.insert(0, '/home/agent/projects/proofs/prove286'); sys.path.insert(0, '/home/agent/projects/proofs/wake285')
from d8lib import rdes, ldes, edges, length
from refine import rstar
from collections import Counter
def orbit(G, n=8):
    E = edges(n)
    G = frozenset(G); seen = {min(G): G}; st = [G]
    while st:
        C = st.pop(); R = rdes(next(iter(C)))
        for s, t in E:
            if (s in R) == (t in R): continue
            D = frozenset(rstar(w, s, t) for w in C)
            assert len(D) == len(C) and len({rdes(w) for w in D}) == 1
            k = min(D)
            if k not in seen: seen[k] = D; st.append(D)
            else: assert seen[k] == D, 'overlapping non-equal images'
    return seen
if __name__ == '__main__':
    d = pickle.load(open(sys.argv[1], 'rb'))
    O = orbit(d['U'])
    allel = set().union(*O.values())
    # sanity: star preserves L elementwise and length parity differences
    print(d['K'], 'orbit cells', len(O), 'elements', len(allel), '(disjoint:', len(allel) == sum(map(len, O.values())), ')',
          'distinct R sets', len({rdes(next(iter(C))) for C in O.values()}))
