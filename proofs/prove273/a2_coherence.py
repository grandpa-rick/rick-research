#!/usr/bin/env python3
"""PROVE 273. Honest A2 polynomial check (BKK Ex 2.3 basis, Phi from the coproduct) of the three
lemmas behind the P0-free proof of Q60(a),(b):
  L1  alpha_j in T  =>  eps_j(b) = eps_j(b_-)            [control: eps_j(b) = eps_j(b_+) must fail]
  L2  coherence: T' = T u {beta} adjacent, Phi_th'(b) = (p,q), Phi_th(q) = (r,s)
      =>  Phi_th(b) = (Phi_th'^{-1}(p,r), s)            [control: Phi_th(b)_- = q must fail]
  L3  simple wall beta = alpha_j: r = zeta_j^m with m = eps_j(b_+) = eps*_j(q) = top-edge length.
"""
import sys, itertools
sys.path.insert(0, '../seedQ1')
from a2_polite_factorisation import *   # basis, components, split_pure_tensor, eps, eps_r, wt

H = 5
keys = sorted(basis, key=lambda k: (k[1] + 2 * k[2] + 2 * k[3], k))
roots = [(1, 0), (0, 1), (1, 1)]
TH = {'++': (1.0, 0.37), '+-a': (1.0, -0.43), '+-b': (0.39, -1.0),
      '-+a': (-0.45, 1.0), '-+b': (-1.0, 0.35), '--': (-1.0, -0.33)}
Tset = {n: frozenset(r for r in roots if t[0]*r[0] + t[1]*r[1] < 0) for n, t in TH.items()}
comp = {k: components(basis[k]) for k in keys if basis[k] != 1}

def Phi(name):
    t1, t2 = TH[name]; out = {}
    one = [k for k in keys if basis[k] == 1][0]
    for k in keys:
        if basis[k] == 1: out[k] = (k, k); continue
        mu = max(comp[k], key=lambda nu: t1*nu[0] + t2*nu[1])
        s = split_pure_tensor(comp[k][mu]); assert s and s[0] != 'NEG'; out[k] = s
    return out, one
P = {n: Phi(n) for n in TH}
ok = {'L1': [0, 0], 'L1ctl': [0, 0], 'L2': [0, 0], 'L2ctl': [0, 0], 'L3': [0, 0]}
for n in TH:
    F, one = P[n]
    for j, aj in ((1, (1, 0)), (2, (0, 1))):
        if aj not in Tset[n]: continue
        for k in keys:
            bp, bm = F[k]
            ok['L1'][0] += eps(j, basis[k]) == eps(j, basis[bm]); ok['L1'][1] += 1
            ok['L1ctl'][0] += eps(j, basis[k]) == eps(j, basis[bp]); ok['L1ctl'][1] += 1
for n, n2 in itertools.permutations(TH, 2):
    T, T2 = Tset[n], Tset[n2]
    if not (T < T2 and len(T2 - T) == 1): continue
    (beta,) = T2 - T
    F, _ = P[n]; F2, _ = P[n2]
    inv2 = {v: k for k, v in F2.items()}
    for k in keys:
        p, q = F2[k]; r, s = F[q]
        pred = (inv2.get((p, r)), s)
        ok['L2'][0] += F[k] == pred; ok['L2'][1] += 1
        ok['L2ctl'][0] += F[k][1] == q; ok['L2ctl'][1] += 1
        if beta in ((1, 0), (0, 1)):
            j = 1 if beta == (1, 0) else 2
            m = wt(basis[r])[j-1] if basis[r] != 1 else 0
            bp = F[k][0]
            ok['L3'][0] += (m == eps(j, basis[bp]) == eps_r(j, basis[q])); ok['L3'][1] += 1
for kk, (a, b) in ok.items(): print(f"{kk}: {a}/{b}")
