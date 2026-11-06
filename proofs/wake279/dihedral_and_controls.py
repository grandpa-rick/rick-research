"""Dihedral explicit matrices/witnesses (GW convention 'C') + negative controls. Computed, not proved."""
import numpy as np
from coxkl import *
from cones import *
np.set_printoptions(linewidth=150, precision=4, suppress=True)

def mid_cell(m):
    G = coxeter_group([[1, m], [m, 1]]); P, mu = kl(G); cells, D = left_cells(G, mu)
    c = [c for c in cells if len(c) == m - 1 and 0 in D[min(c, key=lambda w: G['length'][w])]][0]
    c = sorted(c, key=lambda w: G['length'][w])
    A = cell_module(G, mu, D, c, 'C')
    return G, c, D, A

for m in [4, 5, 6, 8]:
    G, c, D, A = mid_cell(m)
    print(f'--- I2({m}) middle cell, basis by length, words:', [''.join(str(s+1) for s in G['word'][w]) for w in c])
    print('  descents:', [sorted(s+1 for s in D[w]) for w in c])
    print('  1+s1 =\n', A[0]); print('  1+s2 =\n', A[1])
    # invariant subspaces: eigenvectors of A0+A1 (commutes? no) -> use rho
    # 1-dim submodules: common eigenvectors of A0, A1
    d = len(c)
    ev, V = np.linalg.eig(A[0] + 2.7 * A[1])
    for k in range(d):
        v = V[:, k].real
        if all(np.allclose(a @ v, (v @ a @ v) / (v @ v) * v, atol=1e-8) for a in A):
            v = v / np.abs(v).max()
            print('  1-dim submodule spanned by', v, 'eigs', [(v @ a @ v) / (v @ v) for a in A])
    surv = testB(A, eps=0.05, L=6)
    if surv:
        i, j, _, inv = surv[0]
        print(f'  testB witness: cone(C_KL, c_{i} - 0.05 c_{j}) closure pointed & invariant={inv}')
    # largest eps for which cone{e_k} + R+(e_0 - eps e_2) closes
    for eps in [0.1, 0.3, 0.5, 0.9, 1.0, 1.1, 1.5]:
        x = np.eye(d)[0] - eps * np.eye(d)[2]
        orbit = [x]; fr = [x]
        for _ in range(8):
            new = []
            for v in fr:
                for a in A:
                    u = a @ v
                    if (u > -1e-12).all() or np.abs(u).max() < 1e-12: continue
                    u = u / np.abs(u).max()
                    if any(np.allclose(u, o) for o in orbit): continue
                    new.append(u); orbit.append(u)
            fr = new
        gens = list(np.eye(d)) + orbit
        print(f'    eps={eps}: orbit size {len(orbit)}, pointed={pointed(gens)}, invariant={all(in_cone(gens, a @ g) for g in orbit for a in A)}')

# ---------- negative controls in A3 (GW convention, where KL passes) ----------
print('\n=== negative controls, A3 conv C')
G = coxeter_group([[1, 3, 2], [3, 1, 3], [2, 3, 1]]); P, mu = kl(G); cells, D = left_cells(G, mu)
c3 = [c for c in cells if len(c) == 3][0]
A = cell_module(G, mu, D, c3, 'C')
print('KL basis: A:', len(testA(A)[0]), '/3, B survivors:', testB(A))
# (i) wrong unitriangular basis: b_0 = c_0 + c_1 etc.
for (i, j) in [(0, 1), (1, 0), (0, 2), (2, 1)]:
    U = np.eye(3); U[j, i] = 1  # new basis vector i = c_i + c_j
    Ab = [np.linalg.solve(U, a @ U) for a in A]
    inv = min(a.min() for a in Ab) >= -1e-12
    r = len(testA(Ab)[0]) if inv else None
    print(f' basis c_{i}+c_{j}: invariant={inv}, testA reached={r}, testB survivors={len(testB(Ab)) if inv else "n/a"}')
# (ii) perturb a mu
for val in [0.5, 2.0]:
    Ap = [a.copy() for a in A]
    nz = [(s, r, k) for s in range(3) for r in range(3) for k in range(3) if r != k and A[s][r, k] == 1]
    s, r, k = nz[0]; Ap[s][r, k] = val
    # is it still a representation? check braid relation via rho
    R = [a - np.eye(3) for a in Ap]
    rep = all(np.allclose(x @ x, np.eye(3)) for x in R) and np.allclose(R[0]@R[1]@R[0], R[1]@R[0]@R[1])
    print(f' mu({r},{k}) for s{s+1} -> {val}: still a rep={rep}, testA reached={len(testA(Ap)[0])}/3, testB survivors={len(testB(Ap))}')
# (iii) A3 large cell, ensure an enlarged cone is detected if we feed a non-maximal basis:
#  use basis of 'fundamental weight'-type: dual basis of KL cone (rows of inverse) -> cone smaller than C^max
Ainv = [np.linalg.inv(np.eye(3)) for _ in A]
Mw = np.array([[2, 1, 0], [1, 2, 1], [0, 1, 2]], float)  # arbitrary positive change of basis inside C_KL
Ab = [np.linalg.solve(Mw, a @ Mw) for a in A]
inv = min(a.min() for a in Ab) >= -1e-12
print(f' basis = columns of positive matrix (cone strictly inside C_KL): invariant={inv}',
      (f'testA={len(testA(Ab)[0])}/3 testB={len(testB(Ab))}' if inv else ''))
