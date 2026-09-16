"""Verify (4,3) data matches e_3 ⋆ e_4 Day 193 formula via commutativity.

e_a ⋆ e_b = e_b ⋆ e_a in Hikita's ⋆-product (Rick has argued commutativity).
So (4,3) data should = e_3 ⋆ e_4 closed form (Day 193 formula for a=3).

Also, checking: does the a=4 closed form give correct answer at r=3?
Note that for r < a, some qint(r-3) = qint(0) = 0, which zeroes out t^3, t^6 terms.
But the number of terms should be min(a,r)+1 = 4, not 5.
"""

import sympy as sp
q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


# a=3, r=4 formula (Day 193):
def c3_ea3_er(k, r):
    """Day 193 formula for c_k in e_3 ⋆ e_r, k = 0..3."""
    if k == 3:
        return q**(-3)
    if k == 2:
        return (q - 1) / q**3 * qint(r - 1)
    if k == 1:
        return (q - 1) / q**3 * qint(r + 1) / qint(2) * (q * qint(r) - t * qint(r - 2))
    if k == 0:
        return (q - 1) / q**3 * qint(r + 3) / (qint(2) * qint(3)) * (
            qint(r+1) * qint(r+2) * q**2
            - t * qint(2) * qint(r-1) * qint(r+1) * q
            + t**3 * qint(r-2) * qint(r-1))
    raise ValueError

# a=4, r formulas (Day 195):
def c4_ea4_er(k, r):
    if k == 4:
        return q**(-4)
    if k == 3:
        return (q - 1) / q**4 * qint(r - 2)
    if k == 2:
        P2 = q * qint(r - 1) - t * qint(r - 3)
        return (q - 1) / q**4 * qint(r) / qint(2) * P2
    if k == 1:
        P3 = (qint(r+1) * qint(r) * q**2
              - t * qint(2) * qint(r-2) * qint(r) * q
              + t**3 * qint(r-3) * qint(r-2))
        return (q - 1) / q**4 * qint(r + 2) / (qint(2) * qint(3)) * P3
    if k == 0:
        P4 = (qint(r+1) * qint(r+2) * qint(r+3) * q**3
              - t * qint(3) * qint(r-1) * qint(r+1) * qint(r+2) * q**2
              + t**3 * qint(3) * qint(r-2) * qint(r-1) * qint(r+1) * q
              - t**6 * qint(r-3) * qint(r-2) * qint(r-1))
        return (q - 1) / q**4 * qint(r + 4) / (qint(2) * qint(3) * qint(4)) * P4
    raise ValueError

# (4,3) data
data_43 = {
    0: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    1: (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**3,
    2: (q - 1)*(t**2 + t + 1)/q**3,
    3: q**(-3),
}

print("=== Verify (4,3) data = e_3 ⋆ e_4 (Day 193 formula, commutativity) ===")
for k in range(4):
    actual = sp.simplify(data_43[k])
    pred = sp.simplify(c3_ea3_er(k, 4))
    diff = sp.simplify(actual - pred)
    status = "PASS" if diff == 0 else "FAIL"
    print(f"  c_{k}: {status}   diff = {diff if status=='FAIL' else 'ok'}")

# Check: does a=4 formula at r=3 give sensible/correct thing?
# For a=4 r=3, partition (3+4-k, k) for k=0..3 (since min(4,3)=3, only 4 terms).
# Bottom k=4 in a=4 notation is partition (3, 4) which isn't a partition;
# So c_4(3) would map to partition (3,4) → invalid. Really at r < a we lose terms.
print("\n=== Does a=4 formula at r=3 yield partition (3, 4)? ===")
r = 3
print(f"  c_4^(4)(3) = {sp.simplify(c4_ea4_er(4, r))}")
print(f"    partition would be (r, 4) = (3, 4) — INVALID partition (not decreasing)")
print(f"    But by commutativity this belongs to (4, 3) term with e_{{(4,3)}}")
print(f"    which corresponds to c_3^(3)(4) = q^{{-3}}. Actual value: {sp.simplify(c4_ea4_er(4, r))}")
print(f"    → q^{{-4}} vs. expected q^{{-3}} - the formulas don't strictly match at r < a.")
print(f"    That's fine — the a=4 formula is valid for r ≥ 4.")

# Try if a=4 formula r=3 gives anything OTHER than the (4,3) values:
print("\n=== Compare a=4 r=3 formula to a=3 r=4 formula (should equal by comm) ===")
for k in range(4):
    v4 = sp.simplify(c4_ea4_er(k, 3))
    v3 = sp.simplify(c3_ea3_er(k, 4))
    # k in c4 counts from top of a=4; k in c3 counts from top of a=3.
    # Total degree for a=4, r=3 is 7. For k=0 in a=4, partition (7,).
    # For k=0 in a=3, r=4, partition (7,). Same. So they should match!
    diff = sp.simplify(v4 - v3)
    print(f"  c_{k} (a=4,r=3) vs c_{k} (a=3,r=4):  diff = {diff}    "
          f"[{'PASS' if diff==0 else 'DIFF'}]")
    if diff != 0:
        print(f"    a=4,r=3: {sp.factor(v4)}")
        print(f"    a=3,r=4: {sp.factor(v3)}")
