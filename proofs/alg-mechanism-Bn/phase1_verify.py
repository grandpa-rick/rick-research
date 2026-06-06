"""Phase 1: verify (ALG) on V(lambda) as an sl_2-irrep at generic q.

Setup: V(lambda) of dimension d+1, basis v_0, ..., v_d with v_k = F^(k) v_0.
   F v_k = [k+1]_q v_{k+1}
   E v_k = [d-k+1]_q v_{k-1}
   K v_k = q^{d-2k} v_k

B = F + zeta * E K^{-1}.

We verify
   [E^(k), B] v_r = E^(k-1) * [mu - k + 1]_q v_r  +  zeta(1 - q^{-2k}) [k+1]_q E^(k+1) K^{-1} v_r
where mu = d - 2r.
"""

import sympy as sp
from sympy import Rational, Symbol, simplify, factorial, binomial, Poly, expand, cancel, together

q = sp.Symbol('q')
zeta = sp.Symbol('zeta')

def qnum(n):
    # [n]_q = (q^n - q^{-n}) / (q - q^{-1})
    return (q**n - q**(-n)) / (q - q**(-1))

def qfact(n):
    if n < 0:
        return None
    out = sp.Integer(1)
    for j in range(1, n+1):
        out *= qnum(j)
    return out

def qbinom(a, b):
    # [a; b]_q = [a]! / ([b]! [a-b]!), but a-b might be negative for finite-dim irreps;
    # use the product form: [a]_q [a-1]_q ... [a-b+1]_q / [b]!
    if b < 0:
        return sp.Integer(0)
    if b == 0:
        return sp.Integer(1)
    num = sp.Integer(1)
    for j in range(b):
        num *= qnum(a - j)
    return num / qfact(b)

def E_action(coeffs, d):
    """E . sum coeffs[r] v_r."""
    out = [sp.Integer(0)] * (d+1)
    for r in range(d+1):
        if r >= 1:
            out[r-1] += qnum(d - r + 1) * coeffs[r]
    return out

def F_action(coeffs, d):
    """F . sum coeffs[r] v_r."""
    out = [sp.Integer(0)] * (d+1)
    for r in range(d+1):
        if r+1 <= d:
            out[r+1] += qnum(r + 1) * coeffs[r]
    return out

def Kinv_action(coeffs, d):
    out = [sp.Integer(0)] * (d+1)
    for r in range(d+1):
        out[r] = q**(-(d - 2*r)) * coeffs[r]
    return out

def Edivk_action(coeffs, k, d):
    """E^(k) . v.  E^(k) v_r = qbinom(d-r+k, k) v_{r-k}."""
    out = [sp.Integer(0)] * (d+1)
    if k == 0:
        return list(coeffs)
    for r in range(d+1):
        if r - k >= 0:
            coef = qbinom(d - r + k, k)
            # Wait — that's not the right formula. Let me redo.
            # E v_r = [d-r+1] v_{r-1}.
            # E^j v_r = [d-r+1][d-r+2]...[d-r+j] v_{r-j} = ([d-r+j]!/[d-r]!) v_{r-j}.
            # E^(j) v_r = E^j v_r / [j]! = ([d-r+j]!/([d-r]! [j]!)) v_{r-j} = qbinom(d-r+j, j) v_{r-j}.
            coef = qbinom(d - r + k, k)
            out[r-k] += coef * coeffs[r]
    return out

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def sub(a, b):
    return [x - y for x, y in zip(a, b)]

def scale(s, a):
    return [s * x for x in a]

def B_action(coeffs, d):
    f = F_action(coeffs, d)
    ekinv = E_action(Kinv_action(coeffs, d), d)
    return add(f, scale(zeta, ekinv))

def commutator_EkB_on_vr(k, r, d):
    coeffs = [sp.Integer(0)] * (d+1)
    coeffs[r] = sp.Integer(1)
    Ek_B = Edivk_action(B_action(coeffs, d), k, d)
    B_Ek = B_action(Edivk_action(coeffs, k, d), d)
    return sub(Ek_B, B_Ek)

def RHS_on_vr(k, r, d):
    """CORRECTED (ALG):
       E^(k-1) [mu + k - 1]_q v_r + zeta (1 - q^{-2k}) [k+1]_q E^(k+1) K^{-1} v_r.
       (PROVE.md had wrong sign on offset; correct formula has [mu + k - 1]_q from [K; k-1].)"""
    coeffs = [sp.Integer(0)] * (d+1)
    coeffs[r] = sp.Integer(1)
    mu = d - 2*r
    term1 = scale(qnum(mu + k - 1), Edivk_action(coeffs, k - 1, d)) if k - 1 >= 0 else [sp.Integer(0)]*(d+1)
    if k - 1 < 0:
        term1 = [sp.Integer(0)]*(d+1)
    Kinv_v = Kinv_action(coeffs, d)
    term2 = scale(zeta * (1 - q**(-2*k)) * qnum(k+1), Edivk_action(Kinv_v, k+1, d))
    return add(term1, term2)

def check(k, r, d):
    lhs = commutator_EkB_on_vr(k, r, d)
    rhs = RHS_on_vr(k, r, d)
    diff = sub(lhs, rhs)
    diff_simp = [sp.simplify(sp.together(x)) for x in diff]
    return diff_simp, all(x == 0 for x in diff_simp)

if __name__ == "__main__":
    print("=== Phase 1 verification: (ALG) on sl_2 irreps ===")
    results = []
    for d in [2, 3, 4, 5]:
        for k in [1, 2, 3]:
            for r in range(d+1):
                if k > d + 1:
                    continue
                diff, ok = check(k, r, d)
                results.append((d, k, r, ok))
                if not ok:
                    print(f"FAIL d={d}, k={k}, r={r}: {diff}")
    fails = [r for r in results if not r[-1]]
    print(f"Checked {len(results)} cases, {len(fails)} failures.")
    if not fails:
        print("ALL PASS — (ALG) verified on sl_2 irreps for d in 2..5, k in 1..3, all weights.")
