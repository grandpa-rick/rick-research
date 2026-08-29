"""By-hand symbolic derivation of Q_1(-2,b,c) and Q_2(-2,b,c).

Impulse term ignored (c generic).
Tables S_j: S_0={()}, S_1={(1,1)}, S_2={(2,2),(2,1,1)}, kappa=1 each.

Strategy: keep a,b symbolic; loop over concrete integer c so Pochhammer lengths
are concrete integers. Verify Q_k(-2,b,c) is b-independent (polynomial in b of
degree 0 after division) and equals target in c.  Do the a=general derivation
first to see the algebra, then specialize a=-2.
"""
import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, together, cancel

a, b, c = symbols('a b c')
x1, x2, x3 = a + 2, b + 1, c  # note: c is symbolic here for det-sums

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def fall(x, m):
    p = sp.Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def rise(x, L):
    """Rising Pochhammer (x)_L = x(x+1)...(x+L-1). L must be a Python int."""
    p = sp.Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


tables = {
    0: [((0, 0, 0), 1)],
    1: [((1, 1, 0), 1)],
    2: [((2, 2, 0), 1), ((2, 1, 1), 1)],
}


def ds(j):
    """Det-sum: sum_{mu in S_j} kappa_mu * det[(x_i)_down_{mu_col + 2 - col}]."""
    xs = (x1, x2, x3)
    total = sp.Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def H_c_expr(j, c_val):
    """H_c(a, b, j) at concrete integer c = c_val, symbolic a,b.

    H_c = (a+c+1-j) * (a+3)_{c-j-2} * (b+2)_{c-j-1} * ds(j) / [(a-b+1)(a-c+2)(b-c+1)]
    (impulse ignored).
    """
    L1 = c_val - j - 2
    L2 = c_val - j - 1
    if L1 < 0 or L2 < 0:
        raise ValueError(f"Pochhammer length negative at c={c_val}, j={j}")
    ds_j = ds(j).subs(c, c_val)
    poch_a = rise(a + 3, L1)
    poch_b = rise(b + 2, L2)
    num = (a + c_val + 1 - j) * poch_a * poch_b * ds_j
    den = (a - b + 1) * (a - c_val + 2) * (b - c_val + 1)
    expr = cancel(num / den)
    return expand(expr)


# =========================================================================
# k = 1
# =========================================================================
P("=" * 72)
P("k = 1: target Q_1(-2, b, c) = -c(c-1)")
P("=" * 72)

P("\ndet-sum ds_0 (mu = (0,0,0), shifts (2,1,0)):")
P("  ds_0 =", factor(ds(0)))
V = ds(0)
P("  = V(x1,x2,x3), the standard Vandermonde (a-b+1)(a-c+2)(b-c+1).")

P("\ndet-sum ds_1 (mu = (1,1,0), shifts (3,2,0)):")
P("  ds_1 =", factor(ds(1)))
q1, r1 = sp.div(Poly(ds(1), [a, b, c]), Poly(V, [a, b, c]))
P("  ds_1 / V  quotient =", factor(q1.as_expr()), ", remainder =", r1.as_expr())

# H_j(a,b,c) at concrete c
P("\n--- Q_1(-2, b, c) evaluated at c = 2, 3, ..., 8 ---")
P("h_1 = H_1 - H_0.  Q_1 = h_1 / [(a+3)_{c-2} (b+2)_{c-2}].")
P()
Q1_samples = []
for cv in [3, 4, 5, 6, 7, 8, 9]:
    H0 = H_c_expr(0, cv)
    H1 = H_c_expr(1, cv)
    h1 = expand(H1 - H0)
    h1_am2 = expand(h1.subs(a, -2))
    L = cv - 2  # c-1-k with k=1
    denom = rise(sp.Integer(1), L) * rise(b + 2, L)  # (a+3)_L at a=-2 = (1)_L = L!
    # divide as poly in b
    q_poly, rem = sp.div(Poly(h1_am2, b), Poly(denom, b))
    q_expr = q_poly.as_expr()
    rem_expr = rem.as_expr()
    target = -cv * (cv - 1)
    match = (simplify(q_expr - target) == 0) and (rem_expr == 0)
    Q1_samples.append((cv, q_expr, target, match))
    P(f"  c = {cv}: Q_1 = {q_expr},  target = {target},  match = {match},  rem = {rem_expr}")

# Structural piece: show H_0(-2,b,c) and H_1(-2,b,c) separately for c=5 (a rep case)
P("\n--- Structural: individual H_j(-2, b, c) as poly in b, c = 5 ---")
cv = 5
H0 = H_c_expr(0, cv)
H1 = H_c_expr(1, cv)
H0_am2 = expand(H0.subs(a, -2))
H1_am2 = expand(H1.subs(a, -2))
P(f"H_0(-2, b, 5) = {factor(H0_am2)}")
P(f"H_1(-2, b, 5) = {factor(H1_am2)}")
diff = expand(H1_am2 - H0_am2)
P(f"H_1 - H_0    = {factor(diff)}")
denom_5 = rise(sp.Integer(1), 3) * rise(b + 2, 3)  # (1)_3 = 6, (b+2)(b+3)(b+4)
P(f"Denom (1)_3 (b+2)_3 = {factor(denom_5)}")
qc, rc = sp.div(Poly(diff, b), Poly(denom_5, b))
P(f"Q_1(-2,b,5) = {qc.as_expr()}   (target -20)")

# =========================================================================
# k = 2
# =========================================================================
P("\n" + "=" * 72)
P("k = 2: target Q_2(-2, b, c) = c(c-2)(c-1)^2")
P("=" * 72)

P("\ndet-sum ds_2  (S_2 = {(2,2,0), (2,1,1)}, kappa = 1 each):")
P("  mu=(2,2,0): shifts (4,3,0);  mu=(2,1,1): shifts (4,2,1)")
P("  ds_2 =", factor(ds(2)))
q2, r2 = sp.div(Poly(ds(2), [a, b, c]), Poly(V, [a, b, c]))
P("  ds_2 / V quotient =", factor(q2.as_expr()), ", remainder =", r2.as_expr())

P("\n--- Q_2(-2, b, c) evaluated at c = 4, 5, ..., 10 ---")
Q2_samples = []
for cv in [4, 5, 6, 7, 8, 9, 10]:
    H0 = H_c_expr(0, cv)
    H1 = H_c_expr(1, cv)
    H2 = H_c_expr(2, cv)
    h2 = expand(H2 - 2 * H1 + H0)
    h2_am2 = expand(h2.subs(a, -2))
    L = cv - 3  # c-1-k with k=2
    denom = rise(sp.Integer(1), L) * rise(b + 2, L)
    q_poly, rem = sp.div(Poly(h2_am2, b), Poly(denom, b))
    q_expr = q_poly.as_expr()
    rem_expr = rem.as_expr()
    target = cv * (cv - 2) * (cv - 1) ** 2
    match = (simplify(q_expr - target) == 0) and (rem_expr == 0)
    Q2_samples.append((cv, q_expr, target, match))
    P(f"  c = {cv}: Q_2 = {q_expr},  target = {target},  match = {match},  rem = {rem_expr}")

# Structural: b-coefficients of h_1 and h_2 at a=-2, for a mid c.
P("\n" + "=" * 72)
P("STRUCTURAL: origin of b-independence at a = -2")
P("=" * 72)

def show_bcoefs(name, expr, var):
    pp = Poly(expr, var)
    P(f"{name}  b-degree {pp.degree()}:")
    for i in range(pp.degree() + 1):
        cf = pp.nth(i)
        if cf != 0:
            P(f"    b^{i}: {factor(cf)}")

P("\n--- c = 6: coefficients in b of H_0, H_1, H_2 at a=-2 ---")
cv = 6
H0 = expand(H_c_expr(0, cv).subs(a, -2))
H1 = expand(H_c_expr(1, cv).subs(a, -2))
H2 = expand(H_c_expr(2, cv).subs(a, -2))
show_bcoefs("H_0(-2,b,6)", H0, b)
show_bcoefs("H_1(-2,b,6)", H1, b)
show_bcoefs("H_2(-2,b,6)", H2, b)
show_bcoefs("h_1(-2,b,6) = H_1 - H_0", expand(H1 - H0), b)
show_bcoefs("h_2(-2,b,6) = H_2 - 2H_1 + H_0", expand(H2 - 2*H1 + H0), b)

# Divisibility: does h_1(-2,b,c) equal (b+2)_{c-2} * [const in c]?
P("\n--- Factor h_1(-2,b,c) for each c: expect (1)_{c-2}(b+2)_{c-2} * (-c(c-1)) ---")
for cv in [3, 4, 5, 6, 7]:
    h1v = expand((H_c_expr(1, cv) - H_c_expr(0, cv)).subs(a, -2))
    P(f"  c = {cv}: h_1(-2,b,{cv}) = {factor(h1v)}")

P("\n--- Factor h_2(-2,b,c) for each c: expect (1)_{c-3}(b+2)_{c-3} * c(c-2)(c-1)^2 ---")
for cv in [4, 5, 6, 7, 8]:
    h2v = expand(
        (H_c_expr(2, cv) - 2 * H_c_expr(1, cv) + H_c_expr(0, cv)).subs(a, -2)
    )
    P(f"  c = {cv}: h_2(-2,b,{cv}) = {factor(h2v)}")

# ---------------------------------------------------------------------------
# Deeper structural probe: the V-cancellation
# ---------------------------------------------------------------------------
P("\n" + "=" * 72)
P("V-CANCELLATION: ds_j / V is a polynomial for j = 0, 1, 2")
P("=" * 72)
for j in [0, 1, 2]:
    q_j, r_j = sp.div(Poly(ds(j), [a, b, c]), Poly(V, [a, b, c]))
    P(f"  ds_{j} / V = {factor(q_j.as_expr())}   remainder = {r_j.as_expr()}")

P("\nSo H_c(a,b,j) = (a+c+1-j) * (a+3)_{c-j-2} * (b+2)_{c-j-1} * (ds_j/V)")
P("(the three linear denominators exactly cancel V).")
P("H_c is thus a POLYNOMIAL in (a,b,c) up to the two Pochhammer factors.")

# Explore ds_j/V evaluated at a = -2
P("\n--- (ds_j / V) evaluated at a = -2 ---")
for j in [0, 1, 2]:
    q_j, _ = sp.div(Poly(ds(j), [a, b, c]), Poly(V, [a, b, c]))
    qe = q_j.as_expr()
    qe_am2 = expand(qe.subs(a, -2))
    P(f"  j = {j}: (ds_{j}/V)(a=-2, b, c) = {factor(qe_am2)}")
    # Compare against b_falling_j * (c-1)_falling_j
    fj = fall(b, j) * fall(c - 1, j)
    P(f"      compare to b_down_{j} * (c-1)_down_{j} = {factor(fj)},"
      f"  match = {simplify(qe_am2 - fj) == 0}")

# The a=-2 pattern:  (ds_j / V)|_{a=-2} = (b)_down_j * (c-1)_down_j
# So H_j(-2,b,c) = (c-j-1)! * (b+2)_{c-j-1} * (b)_down_j * (c-1)_down_j / [(c-j-1)... factors]?
# Let's reduce H_j(-2,b,c) into a closed form.
P("\n--- Closed form of H_j(-2, b, c)  (using ds_j/V|_{a=-2} = b_dn_j * (c-1)_dn_j) ---")
P("  H_j(-2, b, c) = (c - j) * (1)_{c-j-2} * (b+2)_{c-j-1} * b_dn_j * (c-1)_dn_j")
P("               = (c - j)! * (b+2)_{c-j-1} * b_dn_j * (c-1)_dn_j / (c - j)")
P("               = (c - j - 1)! * (b+2)_{c-j-1} * b_dn_j * (c-1)_dn_j")
# check numerically
for cv in [5, 6, 7]:
    for jj in [0, 1, 2]:
        L1 = cv - jj - 2
        L2 = cv - jj - 1
        pred = sp.factorial(cv - jj - 1) * rise(b + 2, L2) * fall(b, jj) * fall(cv - 1, jj)
        actual = expand(H_c_expr(jj, cv).subs(a, -2))
        d = simplify(expand(pred - actual))
        P(f"  c={cv}, j={jj}: closed - actual = {d}")

# Now h_k = sum (-1)^(k-i) C(k,i) H_i(-2,b,c). With the closed form
#   H_i(-2,b,c) = (c-i-1)! * (b+2)_{c-i-1} * b_dn_i * (c-1)_dn_i
# and (b+2)_{c-i-1} = (b+2)_{c-1-k} * (b+c-k+1)_{k-i}    (splitting rising factorial)
# and (c-i-1)! = (c-1-k)! * (c-k)_{k-i}
# So H_i / [(c-1-k)! (b+2)_{c-1-k}] = (c-k)_{k-i} * (b+c-k+1)_{k-i} * b_dn_i * (c-1)_dn_i
# Then Q_k(-2,b,c) = (1/(c-1-k)!) * sum_i (-1)^{k-i} C(k,i) *
#                    (c-k)_{k-i} * (b+c-k+1)_{k-i} * b_dn_i * (c-1)_dn_i
# The Pochhammer denom in Q is (a+3)_{c-1-k}|_{a=-2} * (b+2)_{c-1-k}
#                              = (1)_{c-1-k} * (b+2)_{c-1-k}
#                              = (c-1-k)! * (b+2)_{c-1-k}
# All consistent. That's the CLOSED FORM for Q_k(-2,b,c).
P("\n--- CLOSED FORM RECIPE ---")
P("  H_i(-2, b, c) = (c-i-1)! * (b+2)_{c-i-1} * b_dn_i * (c-1)_dn_i")
P("  Q_k(-2, b, c) = sum_{i=0}^{k} (-1)^{k-i} C(k,i) *")
P("                   [ (c-k)_{k-i} * (b+c-k+1)_{k-i} * b_dn_i * (c-1)_dn_i ]")
P("  (b+c-k+1)_{k-i} carries all b-dependence; it must sum to b-independent value.")

# Verify closed form of Q_k for k=1,2, symbolic in b for concrete c
P("\n--- Verify closed-form recipe for Q_1, Q_2 symbolically in b at concrete c ---")
for k in [1, 2]:
    for cv in [5, 6, 7]:
        total = sp.Integer(0)
        for i in range(k + 1):
            term = ((-1) ** (k - i)) * sp.binomial(k, i) * \
                   rise(c - k, k - i).subs(c, cv) * \
                   rise(b + cv - k + 1, k - i) * \
                   fall(b, i) * fall(cv - 1, i)
            total += term
        total_e = expand(total)
        # This should equal Q_k(-2, b, cv) which is b-independent
        pb = Poly(total_e, b)
        deg = pb.degree() if pb.degree() >= 0 else 0
        const = pb.nth(0)
        tgt = (-cv * (cv - 1)) if k == 1 else (cv * (cv - 2) * (cv - 1) ** 2)
        P(f"  k={k}, c={cv}: closed-form sum = {total_e},  b-degree={deg},"
          f"  const={const},  target={tgt},  match = {simplify(const-tgt)==0 and deg<=0}")

# Report Q1, Q2 verification table
P("\n" + "=" * 72)
P("VERIFICATION TABLE")
P("=" * 72)
P("k=1:")
for (cv, q, t, m) in Q1_samples:
    P(f"  c={cv}: Q_1={q},  target={t},  match={m}")
P("k=2:")
for (cv, q, t, m) in Q2_samples:
    P(f"  c={cv}: Q_2={q},  target={t},  match={m}")

all_k1 = all(m for (_, _, _, m) in Q1_samples)
all_k2 = all(m for (_, _, _, m) in Q2_samples)
P(f"\nk=1: ALL MATCH = {all_k1}")
P(f"k=2: ALL MATCH = {all_k2}")

# Save
with open('/home/agent/projects/beta-prime/code/2026-08-18-k1-k2-by-hand.txt', 'w') as f:
    f.write('\n'.join(OUT))
P("\nSaved to 2026-08-18-k1-k2-by-hand.txt")
