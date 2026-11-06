"""B3 irreducible 3-dim left cells (GW convention): explicit witness that C_KL is not maximal.
Exact rational verification with sympy. Computed."""
import numpy as np, sympy as sp
from coxkl import *; from cones import *
np.set_printoptions(linewidth=150, precision=4, suppress=True)
G = coxeter_group([[1,4,2],[4,1,3],[2,3,1]]); P, mu = kl(G); cells, D = left_cells(G, mu)
for c in sorted(cells, key=lambda c: (len(c), min(G['length'][w] for w in c))):
    if len(c) != 3: continue
    c = sorted(c, key=lambda w: G['length'][w])
    A = cell_module(G, mu, D, c, 'C')
    print('cell', [''.join(str(s+1) for s in G['word'][w]) for w in c], 'descents', [sorted(s+1 for s in D[w]) for w in c])
    for k, a in enumerate(A): print(f' 1+s{k+1} =', a.tolist())
    surv = testB(A, eps=0.05, L=6); print(' testB survivors', surv)
    # scan eps for the survivor pair
    i, j = surv[0][0], surv[0][1]
    best = None
    for eps in [0.05, 0.1, 0.2, 0.25, 0.3, 1/3, 0.4, 0.5, 0.6, 2/3, 0.75, 0.9, 1.0, 1.2, 1.5, 2.0]:
        x = np.eye(3)[i] - eps*np.eye(3)[j]
        imgs = [a @ x for a in A]
        gens = list(np.eye(3)) + [x]
        ok = all(in_cone(gens, u) for u in imgs) and pointed(gens)
        if ok: best = eps
        print(f'   eps={eps:.3f}: cone(C_KL, x) itself invariant & pointed: {ok}; images {[u.tolist() for u in imgs]}')
    # exact check at best eps
    e = sp.Rational(best).limit_denominator(12)
    x = sp.zeros(3,1); x[i] = 1; x[j] = -e
    Gm = sp.Matrix.hstack(sp.eye(3)[:, [k for k in range(3) if k != i]], x)  # simplicial generators
    ok = True
    for a in A:
        coeffs = Gm.solve(sp.Matrix(a.astype(int)) * x)
        ok &= all(cc >= 0 for cc in coeffs)
    print(f'  EXACT: cone{{c_k (k!={i}), c_{i} - {e} c_{j}}} contains C_KL, is simplicial, and invariant: {ok}')
    break
