"""Negative control: express A3 / GW-convention cell modules in the DUAL KL basis (invariant-form dual),
whose cone is C^min (strictly smaller than C^max). Test must report non-maximal. Computed."""
import numpy as np
from coxkl import *; from cones import *
G = coxeter_group([[1,3,2],[3,1,3],[2,3,1]]); P, mu = kl(G); cells, D = left_cells(G, mu)
for c in cells:
    if len(c) < 2: continue
    A = cell_module(G, mu, D, c, 'C'); d = len(c)
    # invariant form: Q symmetric with A_s^T Q = Q A_s
    rows = [np.kron(np.eye(d), a.T) - np.kron(a.T, np.eye(d)) for a in A]  # vec(A^T Q - Q A) column-major
    _, sv, vt = np.linalg.svd(np.vstack(rows)); Q = vt[-1].reshape(d, d, order='F'); Q = (Q + Q.T) / 2
    if np.trace(Q) < 0: Q = -Q
    M = np.linalg.inv(Q)  # columns = dual basis vectors
    Ab = [np.linalg.solve(M, a @ M) for a in A]
    inv = min(x.min() for x in Ab) >= -1e-9
    print(d, 'Q posdef', np.all(np.linalg.eigvalsh(Q) > 0), 'dual-basis cone invariant', inv,
          'testA reached', len(testA(Ab)[0]), '/', d, 'testB survivors', len(testB(Ab)))
