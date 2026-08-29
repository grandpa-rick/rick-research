"""Day 139 — Study the C_b polynomial: q_b^{(0)} = q̌_b + φ_1 · C_b.

Every correction factored with (E_1+E_2+1) = φ_1. So write:
    q_b^{(0)} = q̌_b + φ_1 · C_b

We want to understand C_b.

Note: q̌_b = 3·τ̌₀(p_{b-1}) - (b-1)(E_1+2b+2)·τ̌₀(p_{b-2})
with τ̌₀(f)(E1,E2) = f(E_1+3, 2E_1+E_2+3).

The (E_1+E_2+1) = φ_1 factor is DEEP: it means the E_3 → φ_1 substitution
in τ̌ picks up φ_1 times SOMETHING. Let's see if C_b factors further —
maybe C_b = φ_1·D_b + something, or C_b is a nice sum.

Direct test: since τ̌(P_{j-1}) - τ̌₀(p_{j-1}) = τ̌([E_3^{≥1}] P_{j-1})
and each E_3 in the argument becomes φ_1 = E_1+E_2+1 upon τ̌, we get

  τ̌(P_{j-1}) - τ̌₀(p_{j-1}) = τ̌(r_{j-1}^{(1)}·E_3 + r_{j-1}^{(2)}·E_3^2 + ...)
                               = r_{j-1}^{(1)}(E1+3, 2E1+E2+3)·φ_1
                                 + r_{j-1}^{(2)}(E1+3, 2E1+E2+3)·φ_1^2 + ...

So the recursion for q_b^{(0)}:
    q_b^{(0)} = q̌_b + φ_1 · [3(b-1)·τ̌₀(r_{b-1}^{(1)}) + higher-order φ_1 corrections from r_{b-1}^{(k)}, r_{b-2}^{(k)}]

Wait — I need to recompute. Recall Day 137 form:
  P_{b+1} = A_b P_b + b E_3 Q_b
=> Q_b = (P_{b+1} - A_b P_b)/(b E_3)

And Day 138 Remark 1.1 said Q_b = 3·τ(P_{b-1}) - (b-1)(E_1+2b+2)·τ(P_{b-2}).
(Note: full τ, not τ̌.)

So Q_b = 3·τ(P_{b-1}) - (b-1)(E_1+2b+2)·τ(P_{b-2}).
At [E_3^0]:  q_b^{(0)} = 3·τ(P_{b-1})|_{E_3=0} - (b-1)(E_1+2b+2)·τ(P_{b-2})|_{E_3=0}
                       = 3·τ̌(P_{b-1}) - (b-1)(E_1+2b+2)·τ̌(P_{b-2})

Now τ̌(P_{b-1}) = τ̌₀(p_{b-1}) + sum_{k≥1} τ̌₀(r_{b-1}^{(k)})·φ_1^k

So the CORRECTION is:
    3·[τ̌(P_{b-1}) - τ̌₀(p_{b-1})] - (b-1)(E_1+2b+2)·[τ̌(P_{b-2}) - τ̌₀(p_{b-2})]
  = 3·sum_k τ̌₀(r_{b-1}^{(k)})·φ_1^k - (b-1)(E_1+2b+2) · sum_k τ̌₀(r_{b-2}^{(k)})·φ_1^k

So correction = φ_1 · [3·τ̌₀(r_{b-1}^{(1)}) - (b-1)(E_1+2b+2)·τ̌₀(r_{b-2}^{(1)})]
              + φ_1^2 · [3·τ̌₀(r_{b-1}^{(2)}) - (b-1)(E_1+2b+2)·τ̌₀(r_{b-2}^{(2)})]
              + ...

**Beautiful.** This gives an EXACT recursion.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, collect, Rational, factorial

E1, E2, E3 = symbols('E1 E2 E3')


def sigma(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
        simultaneous=True))


def phi_map(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, -E1), (E3, -E3)], simultaneous=True))


def build_P(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}


def phi_k(k):
    return E2 + k*E1 + k*k


def p_b(b):
    r = Integer(1)
    for k in range(1, b + 1):
        r *= phi_k(k)
    return expand(r)


def tau_check0(f):
    return expand(f.subs([(E1, E1+3), (E2, 2*E1+E2+3)], simultaneous=True))


B_MAX = 8
P = build_P(B_MAX)

phi1 = phi_k(1)  # E1 + E2 + 1

# Extract r_b^{(k)} for all k, b
def r_k(b, k):
    return expand(Poly(P[b], E3).as_dict().get((k,), Integer(0)))


# The claim:
# q_b^{(0)} = q̌_b^{(0)} + φ_1·q_b^{(1)}(shifted) + φ_1^2·q_b^{(2)}(shifted) + ...
# where
#   q̌_b^{(0)}    = 3·τ̌₀(p_{b-1}) - (b-1)(E_1+2b+2)·τ̌₀(p_{b-2})
#   q_b^{(k)}(shifted) = 3·τ̌₀(r_{b-1}^{(k)}) - (b-1)(E_1+2b+2)·τ̌₀(r_{b-2}^{(k)})

# Let's define these and verify the full identity.

def q_check_0(b):
    """Pure boundary q̌_b^{(0)}."""
    if b < 1:
        return Integer(0)
    v = 3 * tau_check0(p_b(b-1))
    if b >= 2:
        v -= (b-1)*(E1 + 2*b + 2) * tau_check0(p_b(b-2))
    return expand(v)


def q_full_from_r(b, k_max=5):
    """q_b^{(0)} predicted by full formula summing over k."""
    if b < 1:
        return Integer(0)
    v = q_check_0(b)
    for k in range(1, k_max + 1):
        # 3·τ̌₀(r_{b-1}^{(k)}) - (b-1)(E_1+2b+2)·τ̌₀(r_{b-2}^{(k)}), times φ_1^k
        r_bm1 = r_k(b-1, k) if b-1 >= 0 else Integer(0)
        r_bm2 = r_k(b-2, k) if b-2 >= 0 else Integer(0)
        contrib = 3 * tau_check0(r_bm1)
        if b >= 2:
            contrib -= (b-1)*(E1 + 2*b + 2) * tau_check0(r_bm2)
        v += phi1**k * contrib
    return expand(v)


# Compute actual q_b^{(0)}
Q_polys = {}
q0 = {}
for b in range(1, B_MAX):
    A_b = phi_k(b+1)
    diff = expand(P[b+1] - A_b * P[b])
    d = Poly(diff, E3).as_dict()
    Q = Integer(0)
    for (kk,), c in d.items():
        if kk >= 1:
            Q += c * E3**(kk-1)
    Q = expand(Q / b)
    q0[b] = expand(Poly(Q, E3).as_dict().get((0,), Integer(0)))


print("=" * 78)
print("VERIFY: q_b^{(0)} = Σ_{k≥0} φ_1^k · [3·τ̌₀(r_{b-1}^{(k)}) - (b-1)(E_1+2b+2)·τ̌₀(r_{b-2}^{(k)})]")
print("=" * 78)
for b in range(1, B_MAX):
    predicted = q_full_from_r(b)
    diff = expand(q0[b] - predicted)
    print(f"  b={b}: {'OK' if diff == 0 else 'FAIL diff='+str(diff)}")


# BEAUTIFUL: this gives a full recursive structure.
# Now, this can be UNFOLDED all the way. Let's write out the full expansion for r_b^{(1)}:
# r_b^{(1)} = Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · q_j^{(0)}
# and q_j^{(0)} = Σ_k φ_1^k · [3·τ̌₀(r_{j-1}^{(k)}) - (j-1)(E_1+2j+2)·τ̌₀(r_{j-2}^{(k)})]

# When we substitute, the k=0 term gives the "pure boundary" piece (Rick's ř_b^{(1)}).
# The k=1 term gives: r_b^{(1)} depending on r_{j-1}^{(1)}, r_{j-2}^{(1)} shifted!
# This is like a RECURSION FOR r_b^{(1)} in terms of r_{j}^{(1)} shifted (for j < b),
# plus a "seed" from τ̌₀(p_{j-1}) etc.

# Full formula:
# r_b^{(1)} = Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · [3·τ̌₀(p_{j-1}) - (j-1)(E_1+2j+2)·τ̌₀(p_{j-2})]
#           + Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · φ_1 · [3·τ̌₀(r_{j-1}^{(1)}) - (j-1)(E_1+2j+2)·τ̌₀(r_{j-2}^{(1)})]
#           + Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · φ_1^2 · [...r_{...}^{(2)}]
#           + ...

# This SEPARATES the k=0 boundary contribution from higher E_3-level feedback.

# ***** REFRAME as a LINEAR OPERATOR *****
# Define operator T on functions r_b(E_1, E_2):
#   (T[f])_b = Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · [3·τ̌₀(f_{j-1}) - (j-1)(E_1+2j+2)·τ̌₀(f_{j-2})]
#
# Then r_b^{(1)} = (T[p_·])_b + φ_1 · (T[r^{(1)}_·])_b + φ_1^2 · (T[r^{(2)}_·])_b + ...
#
# We could truncate: since r_b^{(k)} = 0 for k > b/2, this is a finite sum for each b.

# For a CLOSED FORM formula for r_b^{(1)}, this suggests we CAN write r_b^{(1)} as a series in φ_1
# where each layer feeds forward. But the higher-k slices r_b^{(k)} for k ≥ 2 introduce their own
# recursions...

# **Try**: does r_b^{(1)} = (T[p_·])_b + φ_1 · (T[r^{(1)}_·])_b   (ignoring k≥2)?
print("\n" + "=" * 78)
print("Testing SIMPLIFIED recursion — only k=0 and k=1 in the φ_1 expansion")
print("=" * 78)
def T_op(f_seq, b):
    """T[f]_b = Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · [3·τ̌₀(f_{j-1}) - (j-1)(E_1+2j+2)·τ̌₀(f_{j-2})]"""
    s = Integer(0)
    for j in range(1, b):
        factor_prod = Integer(1)
        for kk in range(j+2, b+1):
            factor_prod *= phi_k(kk)
        f_jm1 = f_seq.get(j-1, Integer(0))
        f_jm2 = f_seq.get(j-2, Integer(0)) if j >= 2 else Integer(0)
        inner = 3 * tau_check0(f_jm1)
        if j >= 2:
            inner -= (j-1)*(E1 + 2*j + 2) * tau_check0(f_jm2)
        s += factor_prod * j * inner
    return expand(s)


# f_seq for p
p_seq = {b: p_b(b) for b in range(0, B_MAX + 1)}
# f_seq for r^{(1)}
r1_seq = {b: r_k(b, 1) for b in range(0, B_MAX + 1)}
r2_seq = {b: r_k(b, 2) for b in range(0, B_MAX + 1)}
r3_seq = {b: r_k(b, 3) for b in range(0, B_MAX + 1)}
r4_seq = {b: r_k(b, 4) for b in range(0, B_MAX + 1)}

print("Test r_b^{(1)} = T[p]_b + φ_1·T[r^{(1)}]_b + φ_1²·T[r^{(2)}]_b + ...")
for b in range(2, B_MAX + 1):
    predicted = expand(T_op(p_seq, b) + phi1 * T_op(r1_seq, b) + phi1**2 * T_op(r2_seq, b)
                       + phi1**3 * T_op(r3_seq, b) + phi1**4 * T_op(r4_seq, b))
    actual = r_k(b, 1)
    diff = expand(actual - predicted)
    print(f"  b={b}: {'OK' if diff == 0 else 'FAIL diff terms='+str(len(diff.args) if hasattr(diff,'args') else 1)}")


# Also give closed form for T[p]_b — this is the leading "pure boundary" contribution
print("\n" + "=" * 78)
print("Compute T[p]_b — leading 'pure boundary' contribution to r_b^{(1)}")
print("(This equals Rick's ř_b^{(1)} from tau_check_probe.py)")
print("=" * 78)
for b in range(2, B_MAX + 1):
    v = T_op(p_seq, b)
    print(f"\n  T[p]_{b} = {v}")
    # numeric at 0
    v0 = int(v.subs([(E1, 0), (E2, 0)]))
    print(f"  T[p]_{b}(0,0) = {v0}")


# Sequence for T[p]_b(0,0):
seq_leading = [int(T_op(p_seq, b).subs([(E1,0),(E2,0)])) for b in range(2, B_MAX+1)]
print(f"\nLeading contribution to r_b^{{(1)}}(0,0) for b=2..{B_MAX}: {seq_leading}")
seq_actual = [int(r_k(b, 1).subs([(E1,0),(E2,0)])) for b in range(2, B_MAX+1)]
print(f"Actual r_b^{{(1)}}(0,0):                        {seq_actual}")
seq_correction = [a - l for a, l in zip(seq_actual, seq_leading)]
print(f"Difference (higher-level feedback):            {seq_correction}")
