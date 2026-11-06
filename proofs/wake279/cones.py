"""Maximality tests for the KL cone in left-cell modules. Computed, not proved."""
import numpy as np, itertools, sys, json
from scipy.optimize import linprog
from coxkl import *

TOL = 1e-9

# ---------------- irreducible decomposition ----------------
def decompose(G, A, rng):
    d = A[0].shape[0]; I = np.eye(d)
    R = rho_all(G, A)
    chi = np.array([np.trace(r) for r in R])
    norm = chi @ chi / G['N']
    # commutant
    rows = []
    for s in range(G['n']):
        X = A[s] - I
        rows.append(np.kron(np.eye(d), X) - np.kron(X.T, np.eye(d)))  # vec(XC - CX), column-major
    Mx = np.vstack(rows)
    _, sv, vt = np.linalg.svd(Mx)
    null = vt[np.sum(sv > 1e-8):]
    comm = [v.reshape(d, d, order='F') for v in null]
    Xg = sum(rng.normal() * c for c in comm)
    ev, V = np.linalg.eig(Xg)
    # group eigenvalues
    groups = []
    for i, e in enumerate(ev):
        for g in groups:
            if abs(ev[g[0]] - e) < 1e-6: g.append(i); break
        else: groups.append([i])
    Vi = np.linalg.inv(V)
    pieces = []
    for g in groups:
        Pr = V[:, g] @ Vi[g, :]
        ch = np.array([np.trace(Pr @ r).real for r in R])
        pieces.append(np.round(ch, 6))
    return chi, round(norm, 6), len(comm), pieces, comm


# ---------------- test (A): GW-style certificate on dual cone ----------------
def words(n, L):
    for l in range(1, L + 1):
        for w in itertools.product(range(n), repeat=l):
            yield w

def dominant(P):
    ev, V = np.linalg.eig(P)
    a = np.abs(ev); o = np.argsort(-a)
    lam = a[o[0]]
    if lam < TOL: return None
    if len(ev) > 1 and a[o[1]] > lam * (1 - 1e-7): return None
    if abs(ev[o[0]].imag) > 1e-9: return None
    e = V[:, o[0]].real
    evl, U = np.linalg.eig(P.T)
    j = np.argmin(np.abs(evl - ev[o[0]]))
    y = U[:, j].real
    if e.sum() < 0: e = -e
    if y.sum() < 0: y = -y
    e = e / np.abs(e).max(); y = y / np.abs(y).max()
    e[np.abs(e) < 1e-10] = 0; y[np.abs(y) < 1e-10] = 0
    return e, y

def testA(A, L=6):
    """B_s = A_s^T acts on dual coords; any invariant pointed cone C' >= C_KL has dual K <= orthant,
    full-dim, B-invariant.  Derive vectors forced into K; success iff all e_i forced."""
    n = len(A); d = A[0].shape[0]
    B = [a.T for a in A]
    perron = []
    seen = set()
    for w in words(n, L):
        # use only words that are not proper powers duplicates: fine to keep all
        P = np.eye(d)
        for s in w: P = B[s] @ P
        r = dominant(P)
        if r is None: continue
        e, y = r
        if (e < -1e-9).any() or (y < -1e-9).any():  # should not happen for nonneg P
            continue
        k = tuple(np.round(e, 7))
        if k in seen: continue
        seen.add(k); perron.append((e, y, w))
    S = []; keys = set()
    def add(x):
        if x.max() < 1e-12: return False
        x = x / x.max()
        k = tuple(np.round(x, 7))
        if k in keys: return False
        keys.add(k); S.append(x); return True
    for e, y, w in perron:  # rule 1: limit from any strictly positive vector
        add(e)
    changed = True; rounds = 0
    while changed and rounds < 50:
        changed = False; rounds += 1
        for x in list(S):
            if len(S) > 3000: break
            for b in B:
                if add(b @ x): changed = True
            for e, y, w in perron:
                if y @ x > 1e-9 and add(e): changed = True
        if len(S) > 4000: break
    reached = [i for i in range(d) if any(np.count_nonzero(z > 1e-9) == 1 and z[i] > 0 for z in S)]
    return reached, len(perron), S


# ---------------- Perron vector of F^T and orbit ratio ----------------
def perron_F(A):
    d = A[0].shape[0]
    F = sum(a.T for a in A) / len(A)
    ev = np.linalg.eigvals(F)
    lam = max(ev.real)
    mult = int(np.sum(np.abs(ev - lam) < 1e-7))
    return lam, mult


# ---------------- test (B): perturbation ----------------
def pointed(gens):
    """cone(gens) pointed iff exists f with f.g >= 1 for all g."""
    G = np.array(gens); d = G.shape[1]
    res = linprog(np.zeros(d), A_ub=-G, b_ub=-np.ones(len(G)), bounds=[(None, None)] * d, method='highs')
    return res.status == 0

def in_cone(gens, x):
    G = np.array(gens).T
    res = linprog(np.zeros(G.shape[1]), A_eq=G, b_eq=x, bounds=[(0, None)] * G.shape[1], method='highs')
    return res.status == 0

def testB(A, eps=0.05, L=8, maxgen=400):
    d = A[0].shape[0]
    survivors = []
    for i in range(d):
        for j in range(d):
            if i == j: continue
            x = np.eye(d)[i] - eps * np.eye(d)[j]
            orbit = [x]; frontier = [x]; ok = True
            for l in range(L):
                new = []
                for v in frontier:
                    for a in A:
                        u = a @ v
                        if (u > -1e-12).all(): continue
                        u = u / np.abs(u).max()
                        if any(np.allclose(u, o, atol=1e-9) for o in orbit): continue
                        new.append(u); orbit.append(u)
                frontier = new
                if not frontier: break
                if len(orbit) > maxgen: break
                if not pointed(list(np.eye(d)) + orbit): ok = False; break
            if ok and pointed(list(np.eye(d)) + orbit):
                # is the cone closed (invariant)?
                gens = list(np.eye(d)) + orbit
                inv = all(in_cone(gens, a @ g) for g in orbit for a in A)
                survivors.append((i, j, len(orbit), inv))
    return survivors
