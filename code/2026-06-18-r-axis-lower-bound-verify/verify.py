#!/usr/bin/env python3
"""
Day-73 PROVE verification: bonus-coord trick for R-AXIS(5) >= 3.

Checks:
1. b'_alpha = e_{B_1} + alpha e_S + e_{M_2} is BDI-feasible for alpha = 0, 1, 2.
2. The Day-70 routing lists for each AII coord.
3. Lemma 4.1 case analysis: the only feasible ray-image position
   realising b'_alpha (within Day-70 routings) is pi^{p_1} + pi^{l_2}
   with pi^{p_1} = b_alpha and pi^{l_2} = e_{M_2}.
"""
from itertools import product

# BDI coord indexing at n = 5.
# Order: M_2, M_3, M_4, B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S
BDI_COORDS = ["M2", "M3", "M4", "B1", "T1", "B2", "T2", "B3", "T3", "B4", "T4", "S"]
NB = len(BDI_COORDS)
IDX = {c: i for i, c in enumerate(BDI_COORDS)}

def vec(**kw):
    v = [0] * NB
    for k, n in kw.items():
        v[IDX[k]] = n
    return tuple(v)

def add(*vs):
    return tuple(sum(x) for x in zip(*vs)) if vs else tuple([0] * NB)

def scale(c, v):
    return tuple(c * x for x in v)

def P(a, v):
    """P_a = 2 sum_{b<=a} (B_b - T_b)."""
    s = 0
    for b in range(1, a + 1):
        s += v[IDX[f"B{b}"]] - v[IDX[f"T{b}"]]
    return 2 * s

def is_BDI_feasible(v):
    """BDI feasibility: T_a <= B_a, P_a >= 0, M_a <= min(P_{a-1}, P_a), S <= P_{n-1}, all >= 0."""
    if any(x < 0 for x in v):
        return False
    for a in range(1, 5):
        if v[IDX[f"T{a}"]] > v[IDX[f"B{a}"]]:
            return False
        if P(a, v) < 0:
            return False
    for a in range(2, 5):
        if v[IDX[f"M{a}"]] > min(P(a-1, v), P(a, v)):
            return False
    if v[IDX["S"]] > P(4, v):  # n - 1 = 4
        return False
    return True

# Day-69 / Day-72 named points.
b = [vec(B1=1, S=alpha) for alpha in range(3)]  # b_0, b_1, b_2
b_bonus = [add(b[alpha], vec(M2=1)) for alpha in range(3)]  # b'_alpha
c = [scale(k, add(vec(B4=1), vec(T4=1))) for k in range(3)]  # c_k
d = [vec(B1=k) for k in range(3)]  # d_k

print("=" * 60)
print("Day-73 PROVE verification: bonus-coord trick")
print("=" * 60)

print("\n[1] Feasibility of gap-point families")
print("-" * 60)
for alpha, v in enumerate(b):
    print(f"  b_{alpha} = {dict(zip(BDI_COORDS, v))} : BDI-feasible = {is_BDI_feasible(v)}")
for alpha, v in enumerate(b_bonus):
    print(f"  b'_{alpha} = {dict(zip(BDI_COORDS, v))} : BDI-feasible = {is_BDI_feasible(v)}")
for k, v in enumerate(c):
    print(f"  c_{k} = {dict(zip(BDI_COORDS, v))} : BDI-feasible = {is_BDI_feasible(v)}")
for k, v in enumerate(d):
    print(f"  d_{k} = {dict(zip(BDI_COORDS, v))} : BDI-feasible = {is_BDI_feasible(v)}")

# Day-70 §6 routing lists (under D-pi assumption at n=5):
ROUTINGS = {
    "p1": [vec(B1=1, S=alpha) for alpha in range(3)],  # {b_0, b_1, b_2}
    "p2": [vec(B2=1), vec(B2=1, S=1)],  # BINARY by D-pi
    "p3": [vec(B3=1), vec(B3=1, S=1)],  # BINARY by D-pi
    "p4": [vec(B4=1)],  # RIGID
    "p5": [scale(k, add(vec(B4=1), vec(T4=1))) for k in range(3)],  # AXIS, Lemma B mult
    "l1": [vec(B1=k) for k in range(3)],  # {0, e_B1, 2e_B1}, Lemma C
    "l2": [vec(M2=1), vec(S=1)],  # BINARY canonical/divert
    "l3": [vec(M3=1), vec(S=1)],
    "l4": [vec(M4=1), vec(S=1)],
    "l5": [vec(S=1)],  # RIGID
    "s1": [vec(B1=1, T1=1), vec(B1=1, S=1)],  # canonical/divert (divert with B_1 needed for feasibility)
    "s2": [vec(B2=1, T2=1), vec(S=1)],  # canonical/divert
    "s3": [vec(B3=1, T3=1), vec(S=1)],
    "s4": [vec(B4=1, T4=1), vec(S=1)],
    "s5": [tuple([0]*NB)],  # RIGID 0
}

# AII rays at n = 5 (odd, no Lambda).
# Each ray gives one image generator.
# Rays:
#   e_{p_j} for j = 1..5: image = pi^{p_j}
#   e_{l_1}: image = pi^{l_1}
#   e_{s_1}: image = pi^{s_1}
#   e_{p_{j-1}} + e_{l_j} for j = 2..5: image = pi^{p_{j-1}} + pi^{l_j}
#   e_{p_{j-1}} + e_{s_j} for j = 2..5: image = pi^{p_{j-1}} + pi^{s_j}

AII_RAYS = []
for j in range(1, 6):
    AII_RAYS.append(("p", j, [(f"p{j}", 1)]))
AII_RAYS.append(("l", 1, [("l1", 1)]))
AII_RAYS.append(("s", 1, [("s1", 1)]))
for j in range(2, 6):
    AII_RAYS.append(("l", j, [(f"p{j-1}", 1), (f"l{j}", 1)]))
for j in range(2, 6):
    AII_RAYS.append(("s", j, [(f"p{j-1}", 1), (f"s{j}", 1)]))

assert len(AII_RAYS) == 15, f"expected 15 rays, got {len(AII_RAYS)}"

print(f"\n[2] AII rays at n=5: {len(AII_RAYS)} rays")

def feasible_ray_images_for(ray_terms):
    """Return all feasible ray-image vectors for a ray, given Day-70 routing constraints."""
    imgs = set()
    cols = [coord for coord, _ in ray_terms]
    coefs = [c for _, c in ray_terms]
    choices = product(*[ROUTINGS[c] for c in cols])
    for choice in choices:
        v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
        if is_BDI_feasible(v):
            imgs.add(v)
    return imgs

print("\n[3] Lemma 4.1 case analysis: which rays can realise b'_alpha?")
print("-" * 60)
for alpha in range(3):
    target = b_bonus[alpha]
    print(f"\n  Target b'_{alpha} = {dict((k,v) for k,v in zip(BDI_COORDS, target) if v)}")
    matches = []
    for ray_type, j, ray_terms in AII_RAYS:
        # For this ray, enumerate feasible (column-choice) combinations and check if any equals target.
        cols = [coord for coord, _ in ray_terms]
        coefs = [c for _, c in ray_terms]
        for choice in product(*[ROUTINGS[c] for c in cols]):
            v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
            if v == target:
                col_str = ", ".join(f"pi^{c} = {dict((k,vv) for k,vv in zip(BDI_COORDS, ch) if vv)}" for c, ch in zip(cols, choice))
                matches.append(f"    Ray R_{ray_type}{j} (terms: {ray_terms}): {col_str}")
    for m in matches:
        print(m)
    if not matches:
        print("    (no feasible-routing ray-image realises this — Lemma 4.1 then needs a different ray)")

print("\n[4] Verify Lemma 4.1 conclusion: unique ray for b'_alpha is R_{l_2}")
print("-" * 60)
for alpha in range(3):
    target = b_bonus[alpha]
    expected_ray = ("l", 2)
    expected_choice = (b[alpha], vec(M2=1))  # (pi^{p_1} = b_alpha, pi^{l_2} = e_{M_2})
    expected_v = add(expected_choice[0], expected_choice[1])
    assert expected_v == target, f"alpha={alpha}: expected {expected_v} == {target}"
    print(f"  alpha={alpha}: pi^p_1 + pi^l_2 = b_{alpha} + e_M_2 = {dict((k,v) for k,v in zip(BDI_COORDS, target) if v)} ✓")

# Now verify uniqueness rigorously by exhaustively checking all 15 rays.
print("\n[5] Exhaustive uniqueness check: for each alpha, count rays that can realise b'_alpha")
print("-" * 60)
for alpha in range(3):
    target = b_bonus[alpha]
    realising_rays = []
    for ray_type, j, ray_terms in AII_RAYS:
        cols = [coord for coord, _ in ray_terms]
        coefs = [c for _, c in ray_terms]
        for choice in product(*[ROUTINGS[c] for c in cols]):
            v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
            if v == target:
                realising_rays.append((ray_type, j, choice))
                break  # one realisation suffices to mark this ray
    print(f"  alpha={alpha}: {len(realising_rays)} ray(s) can realise b'_{alpha}: {[(rt, j) for rt, j, _ in realising_rays]}")

print("\n[6] Verify forcings at p_5 and l_1 (parallel structure)")
print("-" * 60)
print("\n  p_5 forcing (Lemma B targets c_k):")
for k in range(3):
    target = c[k]
    realising_rays = []
    for ray_type, j, ray_terms in AII_RAYS:
        cols = [coord for coord, _ in ray_terms]
        coefs = [coef for _, coef in ray_terms]
        for choice in product(*[ROUTINGS[col] for col in cols]):
            v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
            if v == target:
                realising_rays.append((ray_type, j, choice))
                break
    print(f"    c_{k}: {len(realising_rays)} ray(s): {[(rt, j) for rt, j, _ in realising_rays]}")

print("\n  l_1 forcing (Lemma C targets d_k):")
for k in range(3):
    target = d[k]
    realising_rays = []
    for ray_type, j, ray_terms in AII_RAYS:
        cols = [coord for coord, _ in ray_terms]
        coefs = [coef for _, coef in ray_terms]
        for choice in product(*[ROUTINGS[col] for col in cols]):
            v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
            if v == target:
                realising_rays.append((ray_type, j, choice))
                break
    print(f"    d_{k}: {len(realising_rays)} ray(s): {[(rt, j) for rt, j, _ in realising_rays]}")

print("\n[7] Bonus-coord trick at p_5: try c_k + e_{B_2} + e_{T_2}")
print("-" * 60)
for k in range(3):
    target = add(c[k], vec(B2=1, T2=1))
    if not is_BDI_feasible(target):
        print(f"    c'_{k} = c_{k} + e_B2 + e_T2 INFEASIBLE")
        continue
    realising_rays = []
    for ray_type, j, ray_terms in AII_RAYS:
        cols = [coord for coord, _ in ray_terms]
        coefs = [coef for _, coef in ray_terms]
        for choice in product(*[ROUTINGS[col] for col in cols]):
            v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
            if v == target:
                realising_rays.append((ray_type, j, choice))
                break
    print(f"    c'_{k} = c_{k} + e_B2+e_T2: {len(realising_rays)} ray(s): {[(rt, j) for rt, j, _ in realising_rays]}")

print("\n[8] Bonus-coord trick at l_1: try d_k + e_{T_1}")
print("-" * 60)
for k in range(3):
    target = add(d[k], vec(T1=1))
    if not is_BDI_feasible(target):
        print(f"    d'_{k} = d_{k} + e_T1 INFEASIBLE")
        continue
    realising_rays = []
    for ray_type, j, ray_terms in AII_RAYS:
        cols = [coord for coord, _ in ray_terms]
        coefs = [coef for _, coef in ray_terms]
        for choice in product(*[ROUTINGS[col] for col in cols]):
            v = add(*[scale(coef, ch) for coef, ch in zip(coefs, choice)])
            if v == target:
                realising_rays.append((ray_type, j, choice))
                break
    print(f"    d'_{k} = d_{k} + e_T1: {len(realising_rays)} ray(s): {[(rt, j) for rt, j, _ in realising_rays]}")

print("\n" + "=" * 60)
print("Verification complete.")
print("=" * 60)
