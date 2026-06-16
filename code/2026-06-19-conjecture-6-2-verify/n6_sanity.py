#!/usr/bin/env python3
"""
Day-74 STRETCH: sanity check the n=6 extension of the Day-73 bonus-coord trick
and Day-74 tight-cap argument.

n = 6 (even). BDI coords: M_2, M_3, M_4, M_5, B_1, T_1, ..., B_5, T_5, S.
Note: at even n, there's a Lambda coord. We approximate by using the same BDI
coord set extended with B_5, T_5, M_5.
"""

# At n = 6: M_2, M_3, M_4, M_5, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, B_5, T_5, S
BDI_COORDS = ["M2", "M3", "M4", "M5", "B1", "T1", "B2", "T2", "B3", "T3", "B4", "T4", "B5", "T5", "S"]
NB = len(BDI_COORDS)
IDX = {c: i for i, c in enumerate(BDI_COORDS)}

def vec(**kw):
    v = [0] * NB
    for k, n in kw.items():
        v[IDX[k]] = n
    return tuple(v)

def add(*vs):
    if not vs: return tuple([0] * NB)
    return tuple(sum(x) for x in zip(*vs))

def P(a, v):
    """P_a = 2 sum_{b<=a} (B_b - T_b) at n = 6 (a goes 1..5)."""
    return 2 * sum(v[IDX[f"B{b}"]] - v[IDX[f"T{b}"]] for b in range(1, a + 1))

def is_BDI_n6(v):
    """BDI feasibility at n = 6: T_a <= B_a for a = 1..5; P_a >= 0; M_a <= P_{a-1}, S <= P_5."""
    if any(x < 0 for x in v): return False
    for a in range(1, 6):
        if v[IDX[f"T{a}"]] > v[IDX[f"B{a}"]]: return False
        if P(a, v) < 0: return False
    for a in range(2, 6):
        if v[IDX[f"M{a}"]] > min(P(a-1, v), P(a, v)): return False
    if v[IDX["S"]] > P(5, v): return False
    return True

print("=" * 60)
print("Day-74 STRETCH: n = 6 sanity checks")
print("=" * 60)

# Test 1: bonus point b'_alpha = b_alpha + e_{M_2} at n = 6.
print("\n[1] Bonus point b'_alpha = e_{B_1} + alpha e_S + e_{M_2}")
print("-" * 60)
for alpha in range(4):
    target = vec(B1=1, S=alpha, M2=1)
    feasible = is_BDI_n6(target)
    print(f"  b'_{alpha}: {dict((k,v) for k,v in zip(BDI_COORDS, target) if v)}")
    print(f"    feasible at n=6: {feasible}")

# Test 2: tight-cap point g_{s_4} at n = 6.
print("\n[2] Tight-cap point g_{s_4} = e_{B_3} + e_{B_4} + e_{T_4} + 2 e_S")
print("-" * 60)
g_s4 = vec(B3=1, B4=1, T4=1, S=2)
print(f"  g_s4: {dict((k,v) for k,v in zip(BDI_COORDS, g_s4) if v)}")
print(f"  feasible at n=6: {is_BDI_n6(g_s4)}")
print(f"  P_5(g_s4) = {P(5, g_s4)}")
print(f"  S = {g_s4[IDX['S']]}, P_5 = {P(5, g_s4)} → S ≤ P_5: {g_s4[IDX['S']] <= P(5, g_s4)} TIGHT (S = P_5)")

# Test 3: tight-cap point g_{s_5} at n = 6 (analog of g_{s_4} at n = 5).
print("\n[3] Tight-cap point g_{s_5} = e_{B_4} + e_{B_5} + e_{T_5} + 2 e_S")
print("-" * 60)
g_s5 = vec(B4=1, B5=1, T5=1, S=2)
print(f"  g_s5: {dict((k,v) for k,v in zip(BDI_COORDS, g_s5) if v)}")
print(f"  feasible at n=6: {is_BDI_n6(g_s5)}")
print(f"  P_5(g_s5) = {P(5, g_s5)}")

# Test 4: tight-cap point for n=6 with both engines: g_{s_4 + s_5}
print("\n[4] Combined tight-cap: g = e_{B_3} + e_{B_4} + e_{T_4} + e_{B_5} + e_{T_5} + 2 e_S")
print("-" * 60)
g_combined = vec(B3=1, B4=1, T4=1, B5=1, T5=1, S=2)
print(f"  g_combined: {dict((k,v) for k,v in zip(BDI_COORDS, g_combined) if v)}")
print(f"  feasible at n=6: {is_BDI_n6(g_combined)}")
print(f"  P_5 = {P(5, g_combined)}, S = {g_combined[IDX['S']]}, S ≤ P_5: {g_combined[IDX['S']] <= P(5, g_combined)}")

# Test 5: Lemma B / Lemma C points at n = 6.
print("\n[5] Lemma B targets: c_k = k(e_{B_5} + e_{T_5}) at n = 6")
print("-" * 60)
for k in range(4):
    target = vec(B5=k, T5=k)
    print(f"  c_{k}: {dict((k_,v) for k_,v in zip(BDI_COORDS, target) if v)}, feasible: {is_BDI_n6(target)}")

print("\n[6] Lemma C targets: d_k = k e_{B_1} at n = 6")
print("-" * 60)
for k in range(4):
    target = vec(B1=k)
    print(f"  d_{k}: {dict((k_,v) for k_,v in zip(BDI_COORDS, target) if v)}, feasible: {is_BDI_n6(target)}")

# Test 7: R-double piece's pi^{p_1} = b_2 with tight S = P_5 = 2.
print("\n[7] R-double pi^{p_1} = b_2 at n = 6")
print("-" * 60)
b2 = vec(B1=1, S=2)
print(f"  b_2: {dict((k,v) for k,v in zip(BDI_COORDS, b2) if v)}")
print(f"  feasible at n=6: {is_BDI_n6(b2)}")
print(f"  P_5(b_2) = {P(5, b2)}, S = 2, TIGHT: {2 == P(5, b2)}")

# Test 8: F3 at j=2 forcing of pi^{s_2} at n = 6.
print("\n[8] F3 at j=2 forcing: pi^{p_1} + pi^{s_2} feasibility")
print("-" * 60)
print(f"  Canonical pi^{{s_2}} = e_B2 + e_T2: sum = {dict((k,v) for k,v in zip(BDI_COORDS, add(b2, vec(B2=1, T2=1))) if v)}, feasible: {is_BDI_n6(add(b2, vec(B2=1, T2=1)))}")
print(f"  Divert pi^{{s_2}} = e_S: sum = {dict((k,v) for k,v in zip(BDI_COORDS, add(b2, vec(S=1))) if v)}, feasible: {is_BDI_n6(add(b2, vec(S=1)))}")

print("\n[9] Tight-cap at all four 'engine' columns in n=6")
print("-" * 60)
# At n = 6, the R-double engine adds to S the columns: l_n, 2 s_{n-1}, 2 s_1, alpha p_1.
# Tight-cap points for n=6 should appear at each "engine boundary."
for j in [3, 4, 5]:
    if j < 5:
        # g_{s_j} = e_{B_{j-1}} + e_{B_j} + e_{T_j} + 2 e_S
        kw = {f"B{j-1}": 1, f"B{j}": 1, f"T{j}": 1, "S": 2}
    else:
        # j = 5: g_{s_5} = e_{B_4} + e_{B_5} + e_{T_5} + 2 e_S
        kw = {f"B{j-1}": 1, f"B{j}": 1, f"T{j}": 1, "S": 2}
    target = vec(**kw)
    P5_val = P(5, target)
    feas = is_BDI_n6(target)
    tight = (target[IDX["S"]] == P5_val) if feas else False
    print(f"  g_{{s_{j}}} = e_B{j-1} + e_B{j} + e_T{j} + 2 e_S: feasible {feas}, S=2, P_5={P5_val}, TIGHT={tight}")

print("\n" + "=" * 60)
print("All sanity checks done")
print("=" * 60)
