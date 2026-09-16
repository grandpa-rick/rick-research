"""Day 195: VERIFY closed form for e_4 ⋆ e_r Pieri rule (a=4).

Conjectured closed form (r ≥ 4):
  c_4(r) = q^{-4}
  c_3(r) = (q-1)/q^4 · [r-2]
  c_2(r) = (q-1)/q^4 · [r]/[2] · (q[r-1] - t[r-3])
  c_1(r) = (q-1)/q^4 · [r+2]/([2][3]) · ([r+1][r]q^2 - t[2][r-2][r]q + t^3[r-3][r-2])
  c_0(r) = (q-1)/q^4 · [r+4]/([2][3][4]) · P_4(q, t; r)

with
  P_4(q, t; r) = [r+1][r+2][r+3] q^3
                 - t·[3]·[r-1][r+1][r+2] q^2
                 + t^3·[3]·[r-2][r-1][r+1] q
                 - t^6·[r-3][r-2][r-1]

Verify at r=4, r=5 direct. For r=3, commute → e_3 ⋆ e_4 (Day 193 formula).
"""

import sympy as sp
q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


# ============================================================
# Closed forms (a=4, r ≥ 4)
# ============================================================
def c_4_of_r(r):
    return q**(-4)

def c_3_of_r(r):
    return (q - 1) / q**4 * qint(r - 2)

def c_2_of_r(r):
    P2 = q * qint(r - 1) - t * qint(r - 3)
    return (q - 1) / q**4 * qint(r) / qint(2) * P2

def c_1_of_r(r):
    P3 = (qint(r+1) * qint(r) * q**2
          - t * qint(2) * qint(r-2) * qint(r) * q
          + t**3 * qint(r-3) * qint(r-2))
    return (q - 1) / q**4 * qint(r + 2) / (qint(2) * qint(3)) * P3

def c_0_of_r(r):
    P4 = (qint(r+1) * qint(r+2) * qint(r+3) * q**3
          - t * qint(3) * qint(r-1) * qint(r+1) * qint(r+2) * q**2
          + t**3 * qint(3) * qint(r-2) * qint(r-1) * qint(r+1) * q
          - t**6 * qint(r-3) * qint(r-2) * qint(r-1))
    return (q - 1) / q**4 * qint(r + 4) / (qint(2) * qint(3) * qint(4)) * P4


# ============================================================
# Data (a=4, r=4, 5): partitions (r+4-k, k) for k = 0..4
# ============================================================
data_r4 = {  # e_4 ⋆ e_4, part (8-k, k) for k=0..4
    0: (q - 1)*(t**4 + 1)*(q**3*t**12 + q**3*t**11 + 2*q**3*t**10 + 3*q**3*t**9 + 4*q**3*t**8 + 4*q**3*t**7 + 5*q**3*t**6 + 4*q**3*t**5 + 4*q**3*t**4 + 3*q**3*t**3 + 2*q**3*t**2 + q**3*t + q**3 - q**2*t**11 - 2*q**2*t**10 - 4*q**2*t**9 - 5*q**2*t**8 - 7*q**2*t**7 - 7*q**2*t**6 - 7*q**2*t**5 - 5*q**2*t**4 - 4*q**2*t**3 - 2*q**2*t**2 - q**2*t + q*t**9 + 2*q*t**8 + 3*q*t**7 + 3*q*t**6 + 3*q*t**5 + 2*q*t**4 + q*t**3 - t**6)/q**4,
    1: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**4,
    2: (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**4,
    3: (q - 1)*(t + 1)/q**4,
    4: q**(-4),
}
data_r5 = {  # e_4 ⋆ e_5, part (9-k, k) for k=0..4
    0: (q - 1)*(t**2 + t + 1)*(t**6 + t**3 + 1)*(q**3*t**12 + q**3*t**10 + q**3*t**9 + 2*q**3*t**8 + q**3*t**7 + 2*q**3*t**6 + q**3*t**5 + 2*q**3*t**4 + q**3*t**3 + q**3*t**2 + q**3 - q**2*t**11 - q**2*t**10 - 2*q**2*t**9 - 2*q**2*t**8 - 3*q**2*t**7 - 3*q**2*t**6 - 3*q**2*t**5 - 2*q**2*t**4 - 2*q**2*t**3 - q**2*t**2 - q**2*t + q*t**9 + q*t**8 + 2*q*t**7 + q*t**6 + 2*q*t**5 + q*t**4 + q*t**3 - t**6)/q**4,
    1: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**4,
    2: (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**4,
    3: (q - 1)*(t**2 + t + 1)/q**4,
    4: q**(-4),
}

print("=" * 70)
print("Verify closed form for e_4 ⋆ e_r, r = 4, 5")
print("=" * 70)

funcs = [c_0_of_r, c_1_of_r, c_2_of_r, c_3_of_r, c_4_of_r]

for r, dat in [(4, data_r4), (5, data_r5)]:
    print(f"\n--- r = {r} ---")
    for k in range(5):
        actual = sp.simplify(dat[k])
        pred = sp.simplify(funcs[k](r))
        diff = sp.simplify(actual - pred)
        status = "PASS" if diff == 0 else "FAIL"
        print(f"  c_{k}(r={r}): {status}   diff = {diff if status=='FAIL' else 'ok'}")


# ============================================================
# Print closed form nicely
# ============================================================
print("\n" + "=" * 70)
print("FINAL CLOSED FORM (a=4, r ≥ 4):")
print("=" * 70)
print("""
  e_4 ⋆ e_r = c_0(r)·e_{r+4} + c_1(r)·e_{r+3,1} + c_2(r)·e_{r+2,2} + c_3(r)·e_{r+1,3} + c_4(r)·e_{r,4}

  c_4(r) = q^{-4}
  c_3(r) = (q-1)/q^4 · [r-2]
  c_2(r) = (q-1)/q^4 · [r]/[2] · (q[r-1] - t[r-3])
  c_1(r) = (q-1)/q^4 · [r+2]/([2][3]) · ([r+1][r]q^2 - t[2][r-2][r]q + t^3[r-3][r-2])
  c_0(r) = (q-1)/q^4 · [r+4]/([2][3][4]) · P_4(q, t; r)

  P_4(q, t; r) = [r+1][r+2][r+3] q^3
                 - t·[3]·[r-1][r+1][r+2] q^2
                 + t^3·[3]·[r-2][r-1][r+1] q
                 - t^6·[r-3][r-2][r-1]
""")

# ============================================================
# Meta-shape audit: the structural symmetry of P_l
# ============================================================
print("=" * 70)
print("META-SHAPE: P_l coefficients across l=1..4")
print("=" * 70)
print("""
P_1(q,t;r,a) = [1]  = 1
P_2(q,t;r,a) = q[r+3-a] - t[r+1-a]
P_3(q,t;r,a) = [r+5-a][r+4-a] q^2 - t[2][r+2-a][r+4-a] q + t^3 [r+1-a][r+2-a]
P_4(q,t;r,a) = [r+7-a][r+6-a][r+5-a] q^3
              - t[3][r+3-a][r+5-a][r+6-a] q^2
              + t^3[3][r+2-a][r+3-a][r+5-a] q       <-- wait, let me recheck the shifts
              - t^6[r+1-a][r+2-a][r+3-a]

At a=4: for P_4, r+7-a = r+3, r+6-a = r+2, r+5-a = r+1, r+3-a = r-1, r+2-a = r-2, r+1-a = r-3

Check the middle terms:
  q^2 coeff: [3][r-1][r+1][r+2]  → r+3-a = r-1, r+5-a = r+1, r+6-a = r+2  ✓
  q^1 coeff: [3][r-2][r-1][r+1]  → r+2-a = r-2, r+3-a = r-1, r+5-a = r+1  → matches [r+2-a][r+3-a][r+5-a]  ✓
""")

# Check the P_4 shift-based formula at a=4
def P4_shifted(r, a):
    P = (qint(r+7-a)*qint(r+6-a)*qint(r+5-a) * q**3
         - t*qint(3)*qint(r+3-a)*qint(r+5-a)*qint(r+6-a) * q**2
         + t**3*qint(3)*qint(r+2-a)*qint(r+3-a)*qint(r+5-a) * q
         - t**6*qint(r+1-a)*qint(r+2-a)*qint(r+3-a))
    return P

# Alternate expression:
def c0_a_generic(a, r):
    """Generic c_0^(a)(r) = (q-1)/q^a · [r+a]/([2][3]...[a]) · P_a."""
    denom = sp.Integer(1)
    for j in range(2, a+1):
        denom *= qint(j)
    if a == 3:
        Pa = (qint(r+2)*qint(r+1) * q**2
              - t*qint(2)*qint(r-1)*qint(r+1) * q
              + t**3 * qint(r-2)*qint(r-1))
    elif a == 4:
        Pa = P4_shifted(r, a)
    return (q - 1) / q**a * qint(r + a) / denom * Pa

# Verify at r=4, 5:
print("\n=== Verify generic formula (a=4 shifted) at r=4, 5 ===")
for r in [4, 5]:
    c0_pred = c0_a_generic(4, r)
    c0_actual = data_r4[0] if r == 4 else data_r5[0]
    diff = sp.simplify(c0_pred - c0_actual)
    print(f"  r={r}: diff = {diff}   [{'PASS' if diff==0 else 'FAIL'}]")

# ============================================================
# Bonus: what does e_4 ⋆ e_r|_{t=0} look like?
# ============================================================
print("\n" + "=" * 70)
print("BONUS: e_4 ⋆ e_r at t=0 (r=4, 5)")
print("=" * 70)
for r, dat in [(4, data_r4), (5, data_r5)]:
    print(f"\n--- r={r}, t=0 ---")
    for k in range(5):
        v = sp.simplify(dat[k].subs(t, 0))
        pred_at_0 = sp.simplify(funcs[k](r).subs(t, 0))
        print(f"  c_{k}({r})|_{{t=0}} = {sp.factor(v)}  (pred: {sp.factor(pred_at_0)})")
