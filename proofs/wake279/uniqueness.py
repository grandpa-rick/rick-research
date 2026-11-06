"""Non-uniqueness probe (GW convention): for each dominated-twin witness v = c_z - c_x (cone(C_KL,v) invariant pointed),
compute the invariant closure of cone(C_KL, -v). If that is also pointed+invariant, two distinct maximal cones exist
(one contains v, other -v; a cone containing both is not pointed). Computed."""
import numpy as np
from coxkl import *; from cones import pointed, in_cone
CASES = {'I2(4)': [[1,4],[4,1]], 'I2(5)': [[1,5],[5,1]], 'I2(6)': [[1,6],[6,1]], 'I2(8)': [[1,8],[8,1]],
         'B3': [[1,4,2],[4,1,3],[2,3,1]], 'H3': [[1,5,2],[5,1,3],[2,3,1]]}
def closure(A, x, L=10):
    d = len(x); orbit = [x / np.abs(x).max()]; fr = list(orbit)
    for _ in range(L):
        new = []
        for v in fr:
            for a in A:
                u = a @ v
                if (u > -1e-12).all() or np.abs(u).max() < 1e-12: continue
                u = u / np.abs(u).max()
                if any(np.allclose(u, o, atol=1e-9) for o in orbit): continue
                new.append(u); orbit.append(u)
        fr = new
        if not fr or len(orbit) > 300: break
    gens = list(np.eye(d)) + orbit
    return pointed(gens), (not fr) or all(in_cone(gens, a @ g) for g in orbit for a in A), len(orbit)
for name, M in CASES.items():
    G = coxeter_group(M); P, mu = kl(G); cells, D = left_cells(G, mu)
    w = lambda u: ''.join(str(s + 1) for s in G['word'][u]) or 'e'
    for c in cells:
        pos = {u: i for i, u in enumerate(c)}
        A = cell_module(G, mu, D, c, 'C')
        for x in c:
            for z in c:
                if x == z or not D[z] <= D[x]: continue
                if not all(mu[y, z] >= mu[y, x] for y in c if D[y] - D[x]): continue
                v = np.zeros(len(c)); v[pos[z]] = 1; v[pos[x]] = -1
                p1 = closure(A, v); p2 = closure(A, -v)
                print(f'{name} d={len(c)} v=c_{w(z)}-c_{w(x)}: +v closure (pointed,inv,size)={p1}; -v closure={p2}')
