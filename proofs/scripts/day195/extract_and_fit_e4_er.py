"""Day 195: Extract e_4 ⋆ e_r data and pattern-hunt closed forms.

Meta-conjecture: c_{a-l}(r) has natural prefactor with q-integer factors.

For a=3 (Day 193):
  c_3(r) = q^{-3}
  c_2(r) = (q-1)[r-1]/q^3
  c_1(r) = (q-1)[r+1](q[r]-t[r-2])/(q^3 [2])
  c_0(r) = (q-1)/q^3 · [r+3]/([2][3]) · ([r+1][r+2]q^2 - t[2][r-1][r+1]q + t^3[r-2][r-1])

Meta-shape from registry:
  c_{a-l}(r) = (q-1)/q^a · [prefactor(l)] · P_l(q,t;r,a)
  prefactor(1) = [r+2-a]
  prefactor(2) = [r+4-a]/[2]
  prefactor(3) = [r+6-a]/([2][3])
  So for l=4: prefactor(4) = [r+8-a]/([2][3][4])?
  For a=4: prefactor(4) = [r+4]/([2][3][4])

P_l is polynomial of degree l-1 in q; coeff of q^{l-1-j} has t-exponent binom(j+1, 2), alternating signs.
P_1(q,t;r,a) = 1
P_2(q,t;r,a) = q[r+3-a] - t[r+1-a]
P_3(q,t;r,a) = [r+5-a][r+4-a]q^2 - t[2][r+2-a][r+4-a]q + t^3[r+1-a][r+2-a]

For a=4:
  l=1: c_3(r) = (q-1)/q^4 · [r-2] · 1
  l=2: c_2(r) = (q-1)/q^4 · [r]/[2] · (q[r-1] - t[r-3])
  l=3: c_1(r) = (q-1)/q^4 · [r+2]/([2][3]) · ([r+1][r]q^2 - t[2][r-2][r]q + t^3[r-3][r-2])
  l=4: c_0(r) = (q-1)/q^4 · [r+4]/([2][3][4]) · P_4(q,t;r,4)
    P_4 = q^3 · (cubic-t·[r+*]) - t·q^2·(cubic) + t^3·q·(cubic) - t^6·(cubic)
    (t-exponents alternate 0, 1, 3, 6 = binom(1,2), binom(2,2), binom(3,2), binom(4,2)... wait
     binom(0+1,2)=0, binom(1+1,2)=1, binom(2+1,2)=3, binom(3+1,2)=6 — yes)

VERIFY at r=3, 4, 5.
"""

import pickle
import sympy as sp
from sympy.combinatorics.partitions import Partition

q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

# Load data from output files (parsing)
data = {
    # (a, r): {partition_tuple: sympy_expr}
    (4, 3): {
        (7,): (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
        (6, 1): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**3,
        (5, 2): (q - 1)*(t**2 + t + 1)/q**3,
        (4, 3): q**(-3),
    },
    (4, 4): {
        (8,): (q - 1)*(t**4 + 1)*(q**3*t**12 + q**3*t**11 + 2*q**3*t**10 + 3*q**3*t**9 + 4*q**3*t**8 + 4*q**3*t**7 + 5*q**3*t**6 + 4*q**3*t**5 + 4*q**3*t**4 + 3*q**3*t**3 + 2*q**3*t**2 + q**3*t + q**3 - q**2*t**11 - 2*q**2*t**10 - 4*q**2*t**9 - 5*q**2*t**8 - 7*q**2*t**7 - 7*q**2*t**6 - 7*q**2*t**5 - 5*q**2*t**4 - 4*q**2*t**3 - 2*q**2*t**2 - q**2*t + q*t**9 + 2*q*t**8 + 3*q*t**7 + 3*q*t**6 + 3*q*t**5 + 2*q*t**4 + q*t**3 - t**6)/q**4,
        (7, 1): (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**4,
        (6, 2): (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**4,
        (5, 3): (q - 1)*(t + 1)/q**4,
        (4, 4): q**(-4),
    },
    (4, 5): {
        (9,): (q - 1)*(t**2 + t + 1)*(t**6 + t**3 + 1)*(q**3*t**12 + q**3*t**10 + q**3*t**9 + 2*q**3*t**8 + q**3*t**7 + 2*q**3*t**6 + q**3*t**5 + 2*q**3*t**4 + q**3*t**3 + q**3*t**2 + q**3 - q**2*t**11 - q**2*t**10 - 2*q**2*t**9 - 2*q**2*t**8 - 3*q**2*t**7 - 3*q**2*t**6 - 3*q**2*t**5 - 2*q**2*t**4 - 2*q**2*t**3 - q**2*t**2 - q**2*t + q*t**9 + q*t**8 + 2*q*t**7 + q*t**6 + 2*q*t**5 + q*t**4 + q*t**3 - t**6)/q**4,
        (8, 1): (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**4,
        (7, 2): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**4,
        (6, 3): (q - 1)*(t**2 + t + 1)/q**4,
        (5, 4): q**(-4),
    },
}

# ============================================================
# ORGANIZATION: c_k for a=4 corresponds to partition (r+4-k, k)
# k=0 → top, k=4 → bottom (for a=4, r≥4)
# For (4,3): partition (7-k, k) for k=0,1,2,3. Top is (7,), bot is (4,3).
# Here bottom is e_(4,3) = q^{-3}: this is because commutativity makes
# (4,3) = (3,4), and Day 193 formula has q^{-a} = q^{-3}. So for (4,3),
# labelling by min(a,b)=3, bot coeff is q^{-3}. For (4,r) with r≥4,
# min(a,b)=4 so bot is q^{-4}. Consistent.

# The c_{4-l}(r) formulas are for a=4 with r ≥ a = 4. For r=3, the label
# just uses a=3 formulas (commutativity).

# Formulas for a=4, using l=distance-from-bottom, l=0..min(a,r)
def c_bot(a, r):
    """l=0: bottom coefficient e_{(r,a)} coeff = q^{-a}."""
    return q**(-a)

def c_bot_minus_1(a, r):
    """l=1: c_{a-1}(r) = (q-1)/q^a · [r+2-a]."""
    return (q - 1) / q**a * qint(r + 2 - a)

def c_bot_minus_2(a, r):
    """l=2: c_{a-2}(r) = (q-1)/q^a · [r+4-a]/[2] · (q[r+3-a] - t[r+1-a])."""
    P2 = q * qint(r + 3 - a) - t * qint(r + 1 - a)
    return (q - 1) / q**a * qint(r + 4 - a) / qint(2) * P2

def c_bot_minus_3(a, r):
    """l=3: c_{a-3}(r) = (q-1)/q^a · [r+6-a]/([2][3]) · P_3.
    P_3 = [r+5-a][r+4-a]q^2 - t[2][r+2-a][r+4-a]q + t^3[r+1-a][r+2-a]."""
    P3 = (qint(r+5-a) * qint(r+4-a) * q**2
          - t * qint(2) * qint(r+2-a) * qint(r+4-a) * q
          + t**3 * qint(r+1-a) * qint(r+2-a))
    return (q - 1) / q**a * qint(r + 6 - a) / (qint(2) * qint(3)) * P3

# The a=4 top prediction (l=4)
def c_top_a4_ansatz(r, P4_coeffs):
    """c_0^(4)(r) = (q-1)/q^4 · [r+4]/([2][3][4]) · P_4(q,t;r).
    P_4 = A(r) q^3 - t B(r) q^2 + t^3 C(r) q - t^6 D(r).
    P4_coeffs = (A, B, C, D) as functions of r.
    """
    A, B, C, D = P4_coeffs
    P4 = A(r) * q**3 - t * B(r) * q**2 + t**3 * C(r) * q - t**6 * D(r)
    return (q - 1) / q**4 * qint(r + 4) / (qint(2) * qint(3) * qint(4)) * P4


# ============================================================
# Verify l=0, 1, 2, 3 formulas on all three data files
# ============================================================
print("=" * 70)
print("PHASE B.1: Verify l=0,1,2,3 formulas (from meta-shape) on a=4 data")
print("=" * 70)

# For (4, r), partition (r+4-k, k) with k = 0..min(4, r).
# Data key uses commuted partition sorted.
# For r=3: bot = (4,3), l=0. For r>=4: bot = (r, 4), l=0.

def part_of(a, r, k):
    """Partition for c_k in e_a ⋆ e_r: (a+r-k, k), sorted descending."""
    p = tuple(sorted([a + r - k, k], reverse=True)) if k > 0 else (a + r,)
    return p

for a, r in [(4, 3), (4, 4), (4, 5)]:
    print(f"\n--- (a={a}, r={r}) ---")
    dat = data[(a, r)]
    min_ar = min(a, r)
    # Which formulas to check? For a=4, we can check l=0,1,2,3 (all four bottom formulas)
    # provided min_ar >= l.
    for l in range(min(min_ar, 3) + 1):
        # k = min_ar - l (index in c_k notation)
        # We need to normalize: our c_k's are indexed from top (k=0) to bottom (k=min_ar).
        # l = min_ar - k = distance from bottom.
        # So k = min_ar - l.
        k = min_ar - l
        p = part_of(a, r, k)
        actual = sp.simplify(dat.get(p, sp.Integer(0)))
        if l == 0:
            pred = c_bot(a, r)  # but wait, for (4,3) this is q^{-3} not q^{-4}
            # For (4,3) commuted = (3,4), min = 3, so bot has q^{-3}. Use q^{-min(a,r)}.
            pred = q ** (-min_ar)
        elif l == 1:
            # For (4,3): use a=3, r=4 (commuted). c_2^(3)(4) = (q-1)/q^3 · [4-1] = (q-1)/q^3·[3]
            # Actually let's use effective_a = min(a, r) and effective_r = max(a, r).
            aa, rr = min(a, r), max(a, r)
            pred = c_bot_minus_1(aa, rr)
        elif l == 2:
            aa, rr = min(a, r), max(a, r)
            pred = c_bot_minus_2(aa, rr)
        elif l == 3:
            aa, rr = min(a, r), max(a, r)
            pred = c_bot_minus_3(aa, rr)
        diff = sp.simplify(actual - pred)
        status = "PASS" if diff == 0 else "FAIL"
        print(f"  l={l} (k={k}, part={p}): {status}  diff={diff if status=='FAIL' else 'ok'}")

# ============================================================
# ============================================================
print("\n\n" + "=" * 70)
print("PHASE B.2: Extract c_0^(4)(r) at r=4, 5 (top coefficient a=4)")
print("=" * 70)

# For (4,4), top c_0 = e_(8,). For (4,5), top c_0 = e_(9,).
# For (4,3), commutativity gives top c_0^(3)(4), which is Day 193 known formula.

# We want to fit c_0^(4)(r) for r >= 4 (since bottom in (4,4) has q^{-4}).
# Data: r=4 (from (4,4)), r=5 (from (4,5)).

def top_of_a4(r):
    """The top e-basis coefficient of e_4 ⋆ e_r (for r>=4), i.e. c_0^(4)(r)."""
    return data[(4, r)][(4 + r,)]

# Divide by natural prefactor (q-1)/q^4 · [r+4]/([2][3][4]):
def natural_prefactor_a4(r):
    return (q - 1) / q**4 * qint(r + 4) / (qint(2) * qint(3) * qint(4))

for r in [4, 5]:
    print(f"\n--- r={r}: c_0^(4)({r}) ---")
    c0 = top_of_a4(r)
    print(f"  Raw:      {sp.factor(sp.simplify(c0))}")
    pre = natural_prefactor_a4(r)
    print(f"  Prefactor: {sp.factor(sp.simplify(pre))}")
    P4 = sp.simplify(c0 / pre)
    P4_expanded = sp.expand(P4)
    print(f"  P_4(q,t;{r}) = c_0 / prefactor:")
    print(f"    Simplified: {sp.factor(P4_expanded)}")
    # Extract q-coefficients
    P4_poly = sp.Poly(P4_expanded, q)
    for degree_of_q in [3, 2, 1, 0]:
        coeff = P4_poly.nth(degree_of_q)
        coeff_fac = sp.factor(sp.simplify(coeff))
        print(f"    q^{degree_of_q} coeff = {coeff_fac}")
