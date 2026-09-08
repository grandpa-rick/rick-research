"""Day 170 Step 11 — Derive L_{-1} directly from F_{-1}, then agree with step13's L_actual.

Provenance script for the L_actual table used in step13_Lm1_corrected_SOURCE.py.
Replaces the untracked reference to "step 11" (which lived in scratch/day169).

Pipeline (all from the RAW definition F_P = T^+(e^{Te_2} V)/V, no closed forms used):

  1. Load FP_coeffs(N+2) from scratch/day152/lib.py — the clean-room umbral
     definition of F_P (u-poly coefficients, exact Fractions).
  2. Restrict u_3 -> -1 to obtain F_{-1} as a series in T with (u_1, u_2)-poly coeffs.
  3. Form G_{-1} := F_{-1}' / F_{-1} by series division.
  4. Extract the u-weight-m diagonal at [T^m] G_{-1} for m = 0..N. This IS L_{-1}[m]
     (the sub-sub-top layer of G_{-1}: [T^m] G_{-1} has top u-weight m+2, sub-top m+1,
      sub-sub-top m).
  5. Symmetrise in (u_1, u_2) to write each entry in E_1 = s, E_2 = p.
  6. Compare with the L_actual table hard-coded in step13.

Expected output: 11/11 PASS at m = 0..10, matching the table verbatim.

Reference: mechanics identical to scratch/day169/step5_top_layer.py (H_{-1}, K_{-1}, L_{-1})
and scratch/day169/step11_L_guess.py (L_{-1} extraction only). This script exists to
land those files under proofs/scripts as tracked provenance for Q8(b).
"""
import sys
import sympy as sp
from fractions import Fraction as Fr

# ---- Load the raw F_P definition from the clean-room library ----
sys.path.insert(0, '/home/agent/projects/scratch/day152')
from lib import FP_coeffs  # noqa: E402

N = 10           # extract L_{-1}[0..N]
Nplus = N + 2    # need two extra to compute F_{-1}' cleanly

print(f"[loading FP_coeffs at N={Nplus} — raw umbral definition of F_P]")
FP = FP_coeffs(Nplus)

# ---- Restrict u_3 -> -1 to obtain F_{-1} ----
u1s, u2s = sp.symbols('u1 u2')

def restrict_u3(pp, val):
    """Convert dict {(i, j, k): Fraction} -> sympy poly in u1, u2 with u3 = val."""
    r = sp.S(0)
    for (i, j, k), v in pp.items():
        c = sp.Rational(v.numerator, v.denominator) * (sp.Rational(val) ** k)
        r += c * u1s**i * u2s**j
    return sp.expand(r)

Fm1 = [restrict_u3(pp, -1) for pp in FP]
print(f"[F_-1 built, {len(Fm1)} coefficients]")

# ---- G_{-1} = F_{-1}' / F_{-1} by series division ----

def series_deriv(f, N):
    return [(k+1)*f[k+1] if k+1 < len(f) else sp.S(0) for k in range(N+1)]

def series_div(f, g, N):
    """f / g with g[0] != 0."""
    inv = [sp.S(0)]*(N+1)
    inv[0] = 1/g[0]
    for n in range(1, N+1):
        s0 = sp.S(0)
        for k in range(1, n+1):
            s0 -= g[k]*inv[n-k]
        inv[n] = s0/g[0]
    h = [sp.S(0)]*(N+1)
    for n in range(N+1):
        s0 = sp.S(0)
        for k in range(n+1):
            s0 += f[k]*inv[n-k]
        h[n] = sp.expand(s0)
    return h

Fm1_p = series_deriv(Fm1, Nplus - 1)
G = series_div(Fm1_p, Fm1, Nplus - 1)
print("[G_-1 built by F_-1'/F_-1]")

# ---- Extract the u-weight-m diagonal (sub-sub-top layer) ----

def wt_part(pp, w):
    """Return the u-weight-w part of a poly in u1, u2."""
    if pp == 0:
        return sp.S(0)
    if not pp.free_symbols:
        return pp if w == 0 else sp.S(0)
    pol = sp.Poly(pp, u1s, u2s)
    r = sp.S(0)
    for mono, coeff in pol.terms():
        if sum(mono) == w:
            r += coeff * u1s**mono[0] * u2s**mono[1]
    return sp.expand(r)

def to_E12(pp):
    """Symmetrise poly in u1, u2 to poly in E1 = u1+u2, E2 = u1 u2."""
    if pp == 0:
        return sp.S(0)
    if not pp.free_symbols:
        return pp
    E1s, E2s = sp.symbols('E1 E2')
    from sympy.polys.polyfuncs import symmetrize
    r, rem, _ = symmetrize(pp, [u1s, u2s], formal=True, symbols=[E1s, E2s])
    assert rem == 0
    return sp.expand(r)

L_derived = []
for m in range(N+1):
    # [T^m] G_-1 has top u-weight m+2, so sub-sub-top is u-weight (m+2) - 2 = m.
    lm = wt_part(G[m], m)
    L_derived.append(to_E12(lm))

print("\n=== L_{-1}[m] derived from F_{-1} directly ===")
for m in range(N+1):
    print(f"  m={m}: {L_derived[m]}")

# ---- Compare with step13's hard-coded L_actual (in the E1=s, E2=p naming) ----
# Numerical specialisation matches step13: s = 2, p = 3.
sv, pv = sp.Rational(2), sp.Rational(3)
E1s, E2s = sp.symbols('E1 E2')

L_actual = [
    sp.S(0), sp.S(0),
    -10*E2s,
    -49*E1s*E2s,
    -145*E1s**2*E2s - 95*E2s**2,
    -335*E1s**3*E2s - 658*E1s*E2s**2,
    -665*E1s**4*E2s - 2611*E1s**2*E2s**2 - 644*E2s**3,
    -1190*E1s**5*E2s - 7784*E1s**3*E2s**2 - 5758*E1s*E2s**3,
    -1974*E1s**6*E2s - 19362*E1s**4*E2s**2 - 28638*E1s**2*E2s**3 - 3777*E2s**4,
    -3090*E1s**7*E2s - 42420*E1s**5*E2s**2 - 104550*E1s**3*E2s**3 - 41360*E1s*E2s**4,
    -4620*E1s**8*E2s - 84546*E1s**6*E2s**2 - 312510*E1s**4*E2s**3 - 247225*E1s**2*E2s**4 - 20416*E2s**5,
]

print("\n=== Comparison: derived L_{-1} vs step13 L_actual table ===")
all_ok = True
for m in range(N+1):
    d = sp.expand(L_derived[m] - L_actual[m])
    ok = (d == 0)
    all_ok = all_ok and ok
    tag = 'OK' if ok else f'MISMATCH (diff = {d})'
    print(f"  m={m}: {tag}")

# Also cross-check the (s,p) = (2,3) specialisation used inside step13.
print(f"\n=== Numerical spot-check at (s,p) = ({sv},{pv}) ===")
for m in range(N+1):
    v_der = sp.expand(L_derived[m].subs({E1s: sv, E2s: pv}))
    v_act = sp.expand(L_actual[m].subs({E1s: sv, E2s: pv}))
    print(f"  m={m}: derived={v_der}, step13 numeric={v_act}, {'OK' if v_der == v_act else 'FAIL'}")

print(f"\nOverall: {'PASS — provenance established at 0..N=10' if all_ok else 'FAIL'}")
