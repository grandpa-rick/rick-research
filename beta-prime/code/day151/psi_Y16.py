#!/usr/bin/env python3
"""
Day 151 task 1 -- extend the Arc-B Lagrange kernel psi to Y^16 (>= Y^12 required).

DEFINITION USED (reconstructed from day149/topW.py + day149/kernel.py, which are the
scripts that produced the published psi through Y^6):

  H      = tau(F_P)/F_P   in Z[E1,E2,E3][[T]]      (day149/bigH.py, cached in H16.pkl)
  W_n    = ell^top_0(H)_n = (the weighted-degree-n part of H_n) / (n+1)
           where wt(E1^a E2^b E3^c) = a+2b+3c.
  calW(T)= sum_{n>=0} W_n T^n
  Y(T)   = T * calW(T)      so that  dY/dT = sum_n (n+1) W_n T^n
  psi    = calW o T(.)      i.e. psi(Y) = calW(T(Y)) = Y/T(Y),  so Y = T*psi(Y).

All arithmetic is exact over Z, monomials stored as (a,b,c).
"""
import pickle, sys
from collections import defaultdict
from math import comb

D = '/home/agent/projects/beta-prime/code/day149/'
H = pickle.load(open(D + 'H16.pkl', 'rb'))
N = max(H.keys())                      # 16

# ---------- polynomial arithmetic in Z[E1,E2,E3] ----------
def padd(A, B):
    R = defaultdict(int)
    for X in (A, B):
        for m, c in X.items(): R[m] += c
    return {m: c for m, c in R.items() if c}
def pmul(A, B):
    if not A or not B: return {}
    R = defaultdict(int)
    for m1, c1 in A.items():
        for m2, c2 in B.items():
            R[(m1[0]+m2[0], m1[1]+m2[1], m1[2]+m2[2])] += c1*c2
    return {m: c for m, c in R.items() if c}
def pscal(k, A):
    return {m: k*c for m, c in A.items()} if k else {}
ONE = {(0, 0, 0): 1}

# ---------- step 1: leading symbol W_n ----------
W = []
for n in range(N+1):
    A = {m: c for m, c in H[n].items() if m[0]+2*m[1]+3*m[2] == n}
    assert all(c % (n+1) == 0 for c in A.values()), ("divisibility by n+1 fails", n)
    W.append({m: c//(n+1) for m, c in A.items()})
assert W[0] == ONE, W[0]

# ---------- sanity check A: Narayana at E3 = 0 ----------
# W_n|_{E3=0} in u-variables with u3=0: coefficient of x^{n-k} y^k must be N(n+1,k+1).
def narayana_check(n):
    A = {m: c for m, c in W[n].items() if m[2] == 0}
    # E1=x+y, E2=xy  (u3=0)
    coef = defaultdict(int)
    for (a, b, _), c in A.items():
        # (x+y)^a * (xy)^b
        for i in range(a+1):
            coef[(a-i+b, i+b)] += c*comb(a, i)
    got = [coef.get((n-k, k), 0) for k in range(n+1)]
    want = [comb(n+1, k)*comb(n+1, k+1)//(n+1) for k in range(n+1)]
    return got == want, got, want

print("=== check 1: Narayana at E3=0 (reproduces day149 topW.py) ===")
ok = True
for n in range(1, N+1):
    g, got, want = narayana_check(n)
    ok &= g
    if not g: print("  n=%d MISMATCH got=%s want=%s" % (n, got, want))
print("  Narayana holds for n=1..%d : %s" % (N, ok))
assert ok

# ---------- step 2: series reversion ----------
M = N + 1                              # work modulo Y^{M+1} / T^{M+1}
def compose(f, g):
    """f(g(T)) truncated at degree M; f,g lists of polys, g[0]==0."""
    res = [{} for _ in range(M+1)]
    gp = [{} for _ in range(M+1)]; gp[0] = dict(ONE)      # g^0
    for k in range(M+1):
        if k > 0:
            new = [{} for _ in range(M+1)]
            for i in range(M+1):
                if not gp[i]: continue
                for j in range(1, M+1-i):
                    if not g[j]: continue
                    new[i+j] = padd(new[i+j], pmul(gp[i], g[j]))
            gp = new
        if f[k]:
            for i in range(M+1):
                if gp[i]: res[i] = padd(res[i], pmul(f[k], gp[i]))
    return res

calW = [W[n] if n <= N else {} for n in range(M+1)]
Yc   = [{}] + [W[n] for n in range(N+1)]          # Y = sum_{n>=0} W_n T^{n+1}
assert len(Yc) == M+1

# reversion: find Tc with Yc(Tc(Y)) = Y
Tc = [{} for _ in range(M+1)]; Tc[1] = dict(ONE)
for m in range(2, M+1):
    comp = compose(Yc, Tc)
    err = comp[m]                                  # want 0
    if err: Tc[m] = padd(Tc[m], pscal(-1, err))
comp = compose(Yc, Tc)
for k in range(M+1):
    want = ONE if k == 1 else {}
    assert comp[k] == want, ("reversion failed at", k, comp[k])
print("=== check 2: reversion verified, Y(T(Y)) = Y to Y^%d ===" % M)

psi = compose(calW, Tc)

# psi(Y) must satisfy Y = T*psi(Y) i.e. psi(Y)*Tc(Y) = Y
chk = [{} for _ in range(M+1)]
for i in range(M+1):
    for j in range(M+1-i):
        if psi[i] and Tc[j]: chk[i+j] = padd(chk[i+j], pmul(psi[i], Tc[j]))
for k in range(M+1):
    want = ONE if k == 1 else {}
    assert chk[k] == want, ("psi*T != Y at", k, chk[k])
print("=== check 3: psi(Y)*T(Y) = Y verified to Y^%d ===" % M)

# ---------- output ----------
def fmt(A):
    if not A: return "0"
    def key(m): return (m[0]+2*m[1]+3*m[2], m[2], m[1], m[0])
    parts = []
    for m in sorted(A, key=key):
        c = A[m]
        s = ""
        for sym, e in zip(("E1", "E2", "E3"), m):
            if e == 1: s += sym
            elif e > 1: s += "%s^%d" % (sym, e)
        if not s: s = "1"
        parts.append(("+ " if c > 0 else "- ") + (("%d*" % abs(c)) if abs(c) != 1 or s == "1" else "") + (s if s != "1" else ""))
    out = " ".join(parts)
    return out[2:] if out.startswith("+ ") else out

KNOWN = {0: "1", 1: "E1", 2: "E2", 3: "2E3", 4: "E1E3", 5: "2E2E3", 6: "E1E2E3 + 5E3^2"}
print()
print("=== psi coefficients ===")
for k in range(0, M+1):
    tag = "   (published: %s)" % KNOWN[k] if k in KNOWN else ""
    print("[Y^%2d] psi = %s%s" % (k, fmt(psi[k]), tag))

print()
print("=== (A) slice E1=E2=0 ===")
for k in range(0, M+1):
    A = {m: c for m, c in psi[k].items() if m[0] == 0 and m[1] == 0}
    if A or k % 3 == 0:
        print("[Y^%2d] psi|_{E1=E2=0} = %s" % (k, fmt(A)))
cat = [{m: c for m, c in psi[3*n].items() if m[0] == 0 and m[1] == 0} for n in range(0, M//3+1)]
seq = []
for n, A in enumerate(cat):
    if not A: seq.append(0); continue
    assert list(A.keys()) == [(0, 0, n)], (n, A)
    seq.append(A[(0, 0, n)])
print("[W^n] psi|_{E1=E2=0}, W=E3*Y^3 :", seq)
print("Catalan C_{n+1}                :", [comb(2*n+2, n+1)//(n+2) for n in range(len(seq))])

print()
print("=== (B) E-positivity ===")
neg = []
for k in range(M+1):
    for m, c in psi[k].items():
        if c < 0: neg.append((k, m, c))
        assert isinstance(c, int)
print("all coefficients integers: True (exact Z arithmetic throughout)")
print("negative coefficients:", neg if neg else "NONE")

pickle.dump(psi, open('/home/agent/projects/beta-prime/code/day151/psi16.pkl', 'wb'))
