"""Day 211: re-run Day 196 length-4 DS cases with exact t-normalisation (float-exponent bug fixed)."""
import sys; sys.path.insert(0,'/home/agent/projects/proofs/scripts/day196'); sys.path.insert(0,'/home/agent/projects/scripts/day211')
import sympy as sp
from ds_test_221 import expand_symmetric_in_e_basis, dominates, partitions_of
from itertools import combinations
from ds_test_221 import build_action
q, t = sp.symbols('q t')
def star_exact(m, factors):
    X, Ti, Tinv, Pi, Y = build_action(m)
    F = sp.Integer(1); sc = sp.Integer(1)
    for f in factors:
        sc *= t**sp.Integer(-(f*(f-1)//2))
        new = sp.Integer(0)
        for I in combinations(range(1, m+1), f):
            piece = F
            for i in I: piece = Y(piece, i)
            new = sp.expand(new + piece)
        F = new
    return sp.expand(sc*F)
for lam in [(1,1,1,1), (2,1,1,1), (2,1,1), (3,1,1), (2,2,1)]:
    n = sum(lam)
    ex = expand_symmetric_in_e_basis(star_exact(n, list(lam)), n, n)
    supp = sorted([mu for mu, v in ex.items() if sp.cancel(v) != 0], reverse=True)
    up = sorted([mu for mu in partitions_of(n) if dominates(mu, lam)], reverse=True)
    nl = sum(i*x for i, x in enumerate(lam))
    print(lam, 'support==full up-set:', supp == up, ' lead==q^-n(lam):', sp.cancel(ex[lam] - q**(-nl)) == 0,
          ' offdiag(q=1)=0:', all(sp.cancel(ex[mu].subs(q, 1)) == 0 for mu in supp if mu != lam), ' supp:', supp, flush=True)
