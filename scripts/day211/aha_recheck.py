"""Day 211: re-run Day 210's aha_221 comparison with EXACT normalisation.
Hypothesis: Day 196 compute_e_star_product uses t**(-f*(f-1)/2) = t**(-1.0) (Python float exponent),
so exact cancel() against TC-route rationals leaves float residue -> spurious MISMATCH."""
import sys; sys.path.insert(0,'/home/agent/projects/proofs/scripts/day196'); sys.path.insert(0,'/home/agent/projects/scripts/day210')
import sympy as sp, time
from itertools import combinations
from ds_test_221 import build_action, expand_symmetric_in_e_basis
from ds3 import elam
q,t = sp.symbols('q t'); s = sp.Symbol('s')
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
ok = True
for lam in [tuple(map(int, a.split(','))) for a in sys.argv[1:]]:
    m = sum(lam); t0 = time.time()
    ex = expand_symmetric_in_e_basis(star_exact(m, list(lam)), m, m)
    tc = elam((lam[2], lam[0], lam[1]))
    bad = [mu for mu in set(ex)|set(tc) if sp.cancel(sp.sympify(ex.get(mu,0)) - sp.sympify(tc.get(mu,0)).subs(s,1/q)) != 0]
    ok &= not bad
    print(lam, 'm=',m,'direct AHA (exact norm) vs TC-route:', 'MATCH' if not bad else f'MISMATCH {bad}', f'{time.time()-t0:.0f}s', flush=True)
print('ALL OK' if ok else 'FAIL')
