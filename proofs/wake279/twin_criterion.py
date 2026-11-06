"""Sufficient criterion for NON-maximality of C_KL (GW convention, (1+s)e_x = 0 if s in D(x), else 2e_x + sum_{y: s in D(y)} mu e_y):
'dominated twin' x != z in a left cell with D(z) subset D(x) and mu(y,z) >= mu(y,x) for every y in the cell
having some s in D(y) \\ D(x).  Then v = c_z - c_x satisfies (1+s)v in {0, (1+s)c_z, 2v + (nonneg)} so
cone(C_KL, v) is invariant and pointed (v has mixed signs).  Hand-checkable; scan is computed."""
import sys
from coxkl import *
def Amat(n): return [[1 if i == j else (3 if abs(i - j) == 1 else 2) for j in range(n)] for i in range(n)]
CASES = {'A3': Amat(3), 'A4': Amat(4), 'A5': Amat(5), 'B3': [[1,4,2],[4,1,3],[2,3,1]], 'B4': [[1,4,2,2],[4,1,3,2],[2,3,1,3],[2,2,3,1]],
         'D4': [[1,3,2,2],[3,1,3,3],[2,3,1,2],[2,3,2,1]], 'H3': [[1,5,2],[5,1,3],[2,3,1]],
         'I2(4)': [[1,4],[4,1]], 'I2(5)': [[1,5],[5,1]], 'I2(6)': [[1,6],[6,1]], 'I2(8)': [[1,8],[8,1]]}
for name in sys.argv[1].split(','):
    G = coxeter_group(CASES[name]); P, mu = kl(G); cells, D = left_cells(G, mu)
    w = lambda u: ''.join(str(s + 1) for s in G['word'][u]) or 'e'
    hits = 0; cells_hit = 0
    for c in cells:
        found = []
        for x in c:
            for z in c:
                if x == z or not D[z] <= D[x]: continue
                ok = all(mu[y, z] >= mu[y, x] for y in c if D[y] - D[x])
                if ok: found.append((w(z), w(x)))
        if found:
            cells_hit += 1; hits += len(found)
            print(f'  {name} cell(d={len(c)}, rep {w(min(c, key=lambda u: G["length"][u]))}): witnesses c_z - c_x, (z,x) =', found[:4])
    print(f'{name}: |W|={G["N"]} cells={len(cells)} cells with dominated twin: {cells_hit}')
