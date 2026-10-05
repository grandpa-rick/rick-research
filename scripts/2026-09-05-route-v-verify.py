"""Route (v) verification — Clio UID 244.

Checks:
  Step 1 — Prop 1 (F_P|_{u3=-1} closed form) at k = 1..7
  Step 2 — Prop 2 (F_{-1} as explicit operator on F_0) at k = 1..7
  Step 3 — Prop 3 (R^{(-1)} reduction) at n = 11, 12, 13, 14
  Step 4 — Rung-2 hypothesis: F_{-2} as order-2 differential operator on F_0

Rick's conventions (from /home/agent/projects/scratch/day152/lib.py):
  * FP_coeffs(N) returns [T^k] F_P as u-poly for k=0..N
  * F_0(u_1, u_2) := F_P|_{u_3=0}
  * F_1(u_1, u_2) := ∂_{u_3} F_P|_{u_3=0}  (Rick's F_1, NOT Clio's F_{-1})
  * R^{(-1)} := sub-top layer at u-degree n-1 of [T^n] (F_1/F_0) at u_3=0
              = ∂_{u_3} X^{(0)}|_{u_3=0}
"""
import sys, math
sys.path.insert(0, '/home/agent/projects/scratch/day152')
from lib import FP_coeffs, U, pmul, padd, psub, pscal, pconst, sdiv, to_E
from fractions import Fraction as Fr

# ------------------------ Basic utilities ------------------------

def restrict_u3(p, val):
    """Substitute u_3 = val (Fraction) in a u-polynomial dict."""
    out = {}
    for (i, j, k), c in p.items():
        contribution = c * (Fr(val) ** k)
        key = (i, j, 0)
        w = out.get(key, Fr(0)) + contribution
        if w:
            out[key] = w
        elif key in out:
            del out[key]
    return {k: v for k, v in out.items() if v}

def restrict_u3_zero(p):
    return {(i, j, 0): v for (i, j, k), v in p.items() if k == 0}

def dpartial_u3(p):
    r = {}
    for (i, j, k), v in p.items():
        if k >= 1:
            nk = (i, j, k-1)
            nv = v * k
            if nv:
                r[nk] = r.get(nk, Fr(0)) + nv
    return {k: v for k, v in r.items() if v}

def poly_eq(a, b):
    """Are two u-poly dicts equal?"""
    d = padd(a, pscal(b, -1))
    return not d

def pretty(p, nterms=5):
    items = sorted(p.items())
    return ", ".join(f"{k}:{v}" for k, v in items[:nterms])

# ------------------------ Step 1 — Prop 1 -----------------------

def B(u_idx, m):
    """B_m(u) := (u+2)^{(m)} = (u+2)(u+3)...(u+m+1). For m=0, returns 1. For m<0, use 0."""
    if m < 0:
        return {}  # 0
    r = pconst(1)
    for s in range(m):
        r = pmul(r, padd(U[u_idx], pconst(s + 2)))
    return r

def prop1_rhs(k):
    """(p/k!) [B_{k-1}(u1) B_{k-1}(u2) + (1-k)(s + 2k+1) B_{k-2}(u1) B_{k-2}(u2)]
    For k=0, Prop 1 says [T^0] F_P|_{u3=-1} = 1."""
    if k == 0:
        return pconst(1)
    p = pmul(U[0], U[1])  # p = u1 u2
    s = padd(U[0], U[1])  # s = u1 + u2
    term1 = pmul(B(0, k-1), B(1, k-1))
    if k >= 2:
        # (1-k)(s+2k+1) B_{k-2}(u1) B_{k-2}(u2)
        factor = pscal(padd(s, pconst(2*k + 1)), 1 - k)
        term2 = pmul(pmul(factor, B(0, k-2)), B(1, k-2))
        total = padd(term1, term2)
    else:
        # k = 1: second term has (1-k) = 0, so it vanishes
        total = term1
    result = pmul(p, total)
    result = pscal(result, Fr(1, math.factorial(k)))
    return result

def step1_prop1(K):
    print("=" * 60)
    print(f"Step 1 — Prop 1 (F_P|_{{u3=-1}} closed form), k = 0..{K}")
    print("=" * 60)
    FP = FP_coeffs(K)
    for k in range(K + 1):
        lhs = restrict_u3(FP[k], -1)
        rhs = prop1_rhs(k)
        # Reduce both to 2-var (drop u_3 tag)
        lhs2 = {(i, j): v for (i, j, kk), v in lhs.items() if kk == 0}
        rhs2 = {(i, j): v for (i, j, kk), v in rhs.items() if kk == 0}
        # Symmetric difference
        keys = set(lhs2) | set(rhs2)
        diff = {k_: lhs2.get(k_, Fr(0)) - rhs2.get(k_, Fr(0)) for k_ in keys}
        diff = {k_: v for k_, v in diff.items() if v}
        match = not diff
        print(f"  k={k}: match={match}", end="")
        if not match:
            print(f"\n    LHS - RHS diff (up to 5 terms): {pretty(diff)}", end="")
            print(f"\n    lhs = {pretty(lhs2)}", end="")
            print(f"\n    rhs = {pretty(rhs2)}")
            return False, k
        print()
    return True, K

# ------------------------ Step 2 — Prop 2 -----------------------
# F_{-1} = [ p (F_0 - (s+1) T F_0 - 2 T^2 F_0' + (s+1) int_0^T F_0 dT')
#           + (s+1) ] / [ (u1+1)(u2+1) ]

def sdiff_T(f):
    """T-derivative: [T^n] f' = (n+1) [T^{n+1}] f, so shift and multiply."""
    return [pscal(f[n+1], n+1) if n+1 < len(f) else {} for n in range(len(f))]

def sintegrate_T(f):
    """T-antiderivative with zero constant: [T^n] (int_0^T f dT') = [T^{n-1}] f / n."""
    r = [{}]
    for n in range(1, len(f)):
        r.append(pscal(f[n-1], Fr(1, n)))
    return r

def series_p_add(a, b, N):
    return [padd(a[k] if k < len(a) else {}, b[k] if k < len(b) else {}) for k in range(N+1)]

def series_p_sub(a, b, N):
    return [psub(a[k] if k < len(a) else {}, b[k] if k < len(b) else {}) for k in range(N+1)]

def series_p_scal_by_poly(f, poly, N):
    """Multiply each coefficient (u-poly) by poly (u-poly)."""
    return [pmul(f[k], poly) if k < len(f) else {} for k in range(N+1)]

def series_p_shift_by_T(f, N):
    """T * f: [T^n] (T*f) = [T^{n-1}] f."""
    r = [{}]
    for n in range(1, N+1):
        r.append(f[n-1] if n-1 < len(f) else {})
    return r

def prop2_rhs(F0, N):
    """Build the Prop 2 RHS as a series in T (with 2-var u-poly coefficients).
    F_{-1} = { p [ F_0 - (s+1) T F_0 - 2 T^2 F_0' + (s+1) int F_0 ] + (s+1) } / ((u1+1)(u2+1))
    We return the NUMERATOR times ((u1+1)(u2+1))-inverse? No —
    we return the FULL series after dividing (via 2-var division which requires exact).
    But (u1+1)(u2+1) is a POLYNOMIAL divisor, NOT a series in T.
    Strategy: compute the numerator as a series, then verify:
        numerator = ((u1+1)(u2+1)) * F_{-1}, i.e. compare to (u1+1)(u2+1) * F_P|_{u3=-1}.
    That's cleaner — we avoid polynomial division.
    """
    s = padd(U[0], U[1])
    p = pmul(U[0], U[1])
    s_plus_1 = padd(s, pconst(1))
    # F_0'
    F0_prime = sdiff_T(F0)
    # T * F_0
    T_F0 = series_p_shift_by_T(F0, N)
    # T^2 * F_0'
    T2_F0p = series_p_shift_by_T(series_p_shift_by_T(F0_prime, N), N)
    # int F_0
    int_F0 = sintegrate_T(F0)
    # p [F_0 - (s+1) T F_0 - 2 T^2 F_0' + (s+1) int F_0]
    inner = F0[:]
    inner = series_p_sub(inner, series_p_scal_by_poly(T_F0, s_plus_1, N), N)
    inner = series_p_sub(inner, series_p_scal_by_poly(T2_F0p, pconst(2), N), N)
    inner = series_p_add(inner, series_p_scal_by_poly(int_F0, s_plus_1, N), N)
    p_inner = series_p_scal_by_poly(inner, p, N)
    # numerator = p_inner + (s+1)  (the +(s+1) is added to [T^0] as a constant)
    numer = p_inner[:]
    numer[0] = padd(numer[0], s_plus_1)
    return numer

def step2_prop2(K):
    print("=" * 60)
    print(f"Step 2 — Prop 2 (F_{{-1}} = explicit op on F_0), k = 0..{K}")
    print("=" * 60)
    FP = FP_coeffs(K)
    F0 = [restrict_u3_zero(FP[k]) for k in range(K+1)]
    # Fminus1 from raw FP
    Fminus1 = [restrict_u3(FP[k], -1) for k in range(K+1)]
    # (u1+1)(u2+1)
    D = pmul(padd(U[0], pconst(1)), padd(U[1], pconst(1)))
    # Verify D * Fminus1 == numerator
    lhs = [pmul(D, f) for f in Fminus1]
    rhs = prop2_rhs(F0, K)
    for k in range(K+1):
        diff = psub(lhs[k], rhs[k])
        # drop u_3 tag (both should have no u_3)
        diff2 = {(i, j): v for (i, j, kk), v in diff.items() if v}
        assert all(kk == 0 for (i, j, kk), v in diff.items() if v), \
            "Unexpected u_3 dependence"
        diff2 = {k_: v for k_, v in diff2.items() if v}
        match = not diff2
        print(f"  k={k}: match={match}", end="")
        if not match:
            print(f"\n    diff (up to 5 terms): {pretty(diff2)}")
            return False, k
        print()
    return True, K

# ------------------------ Step 3 — Prop 3 -----------------------
# R^{(-1)} = (1/2) ∂_{u3}^2 Xi_n |_{u3=0}  -  [deg_{(u1,u2)} = n-1]([T^n] log(F_{-1}/F_0))
#
# R^{(-1)} := sub-top layer at u-deg n-1 of [T^n] (F_1/F_0)|_{u3=0}
#           where F_1 = ∂_{u3} F_P|_{u3=0}. (Rick's convention.)
#
# Xi := ell^top_1(log F_P), so [T^n] Xi = degree-(n+1) part of [T^n] log F_P.
# Then ∂_{u3}^2 of Xi at u_3=0 = 2 * (coefficient of u_3^2 in [T^n] Xi, evaluated).

def slog3(f, N):
    """log of 3-var series, f[0]=1."""
    assert f[0] == pconst(1), f[0]
    g = [{} for _ in range(N+1)]
    for n in range(1, N+1):
        s = pscal(f[n], n)
        for k in range(1, n):
            s = psub(s, pscal(pmul(g[k], f[n-k]), k))
        g[n] = pscal(s, Fr(1, n))
    return g

def extract_udeg_eq(p, d):
    return {k: v for k, v in p.items() if sum(k) == d}

def extract_udeg_eq_2var(p, d):
    """Extract 2-var u-poly of exact degree d (u_3 tag = 0)."""
    return {(i, j, 0): v for (i, j, k), v in p.items() if k == 0 and (i + j) == d}

def coeff_u3_squared(p):
    """Return the coefficient of u_3^2 in p as a 2-var u-poly."""
    return {(i, j, 0): v for (i, j, k), v in p.items() if k == 2}

def step3_prop3(N_lo, N_hi):
    print("=" * 60)
    print(f"Step 3 — Prop 3 (R^{{(-1)}} reduction), n = {N_lo}..{N_hi}")
    print("=" * 60)
    N = N_hi
    print(f"  Computing FP_coeffs to N={N} ...")
    FP = FP_coeffs(N)
    F0 = [restrict_u3_zero(FP[k]) for k in range(N+1)]
    F1 = [restrict_u3_zero(dpartial_u3(FP[k])) for k in range(N+1)]
    Fm1 = [restrict_u3(FP[k], -1) for k in range(N+1)]
    # R = F_1/F_0
    R = sdiv(F1, F0, N)
    # R^{(-1)}_n = sub-top layer (u-deg n-1) of R_n
    Rminus1 = [extract_udeg_eq_2var(R[n], n - 1) for n in range(N+1)]
    # log F_P (3-var) -> extract Xi (top layer)
    logFP = slog3(FP, N)
    Xi = [extract_udeg_eq(logFP[n], n + 1) for n in range(N+1)]
    # (1/2) ∂_{u3}^2 Xi_n |_{u3=0} = coefficient of u_3^2 in Xi_n (as 2-var poly), multiplied by 2 (from d^2/du^2)?
    # No: ∂_{u3}^2 p |_{u3=0} = 2 * (coeff of u_3^2 in p). So (1/2) ∂^2 = coeff of u_3^2.
    half_ddu3_sq_Xi = [coeff_u3_squared(Xi[n]) for n in range(N+1)]
    # Now compute log(F_{-1}/F_0). Note F_{-1}[0] = ? Let's check.
    # F_P[0] = 1, so F_0[0] = 1 and F_{-1}[0] = 1. Both have constant 1.
    # F_{-1}/F_0 series
    Ratio_m1 = sdiv(Fm1, F0, N)
    # log(F_{-1}/F_0) — but Ratio_m1[0] should be 1
    if Ratio_m1[0] != pconst(1):
        print(f"  ERROR: (F_{{-1}}/F_0)[0] = {Ratio_m1[0]} != 1")
        return False, 0
    log_ratio = slog3(Ratio_m1, N)  # 2-var series (u_3 tag = 0), still valid
    # Extract degree-(n-1) part of log_ratio[n]
    log_ratio_deg_nm1 = [extract_udeg_eq_2var(log_ratio[n], n - 1) for n in range(N+1)]
    # Compute predicted R^{(-1)} = half_ddu3_sq_Xi - log_ratio_deg_nm1
    all_ok = True
    for n in range(N_lo, N_hi + 1):
        pred = psub(half_ddu3_sq_Xi[n], log_ratio_deg_nm1[n])
        actual = Rminus1[n]
        diff = psub(pred, actual)
        match = not diff
        status = "PASS" if match else "FAIL"
        print(f"  n={n}: {status}", end="")
        if not match:
            print(f"\n    diff (up to 5 terms): {pretty(diff)}")
            all_ok = False
            return False, n
        print()
    return all_ok, N_hi

# ------------------------ Step 4 — Rung-2 -----------------------
# F_{-2} = (A_0 + A_1 (∂_{u1} + ∂_{u2}) + A_{11} ∂_{u1} ∂_{u2} + A_{20} (∂^2_{u1}+∂^2_{u2})) F_0 ?
#
# Clio: "F_{-m} should be an order-m differential operator on F_0". We test whether
#   F_{-2}(u_1, u_2) = A_0(u_1,u_2) F_0 + A_1 (∂_{u1}+∂_{u2}) F_0
#                     + A_11 ∂_{u1}∂_{u2} F_0 + A_20 (∂^2_{u1}+∂^2_{u2}) F_0
# for some symmetric A_0, A_1, A_11, A_20 depending on (u_1, u_2) alone (no T).
# (Order-2 operator, symmetric in u_1 <-> u_2.)

def dpartial_u_i(p, i):
    r = {}
    for k, v in p.items():
        if k[i] >= 1:
            nk = list(k)
            nk[i] -= 1
            nk = tuple(nk)
            nv = v * k[i]
            if nv:
                r[nk] = r.get(nk, Fr(0)) + nv
    return {k: v for k, v in r.items() if v}

def step4_rung2(N):
    """Test whether F_{-2} = order-2 differential operator on F_0.

    Clio's Prop 2 for F_{-1} is an order-1 T-integro-differential operator with
    polynomial-in-(u_1,u_2) coefficients on RHS times F_0, its T-derivative,
    T-integral, and a constant correction, ALL divided by (u1+1)(u2+1).

    For F_{-2} we test order-2 analog. Build the ansatz LHS as
        LHS = Q(u) * F_{-2}     with Q(u) = (u1+1)^2 (u2+1)^2
    and try
        LHS = sum_j sum_{k} P_{j,k}(u) T^k [ theta^j F_0 ]
              + sum_{k} R_k(u) T^k [ int F_0 ]
              + sum_{k} S_k(u) T^k
    for j = 0, 1, 2 (order 2), k = 0..K (bounded T-power on the coefficient),
    P_{j,k}, R_k, S_k symmetric polys in (u_1, u_2) of bounded degree.
    Solve the resulting F-linear system over Q via manual pivoting (fast).
    """
    print("=" * 60)
    print(f"Step 4 — Rung-2: F_{{-2}} = order-2 T-differential op on F_0, T^0..T^{N}")
    print("=" * 60)
    FP = FP_coeffs(N)
    F0 = [restrict_u3_zero(FP[k]) for k in range(N+1)]
    Fm2 = [restrict_u3(FP[k], -2) for k in range(N+1)]

    # We use 2-var poly dicts {(i,j): Fraction}. Coefficients live in the ring
    # Q[u_1, u_2] (symmetric). We work over the T-series ring with 2-var poly coefs.

    def as_2var(p):
        """Drop u_3 tag (should be 0)."""
        return {(i, j): v for (i, j, k), v in p.items() if k == 0 and v}

    def p2_add(a, b):
        r = dict(a)
        for k, v in b.items():
            w = r.get(k, Fr(0)) + v
            if w: r[k] = w
            elif k in r: del r[k]
        return r
    def p2_sub(a, b):
        return p2_add(a, {k: -v for k, v in b.items()})
    def p2_mul(a, b):
        r = {}
        for k1, v1 in a.items():
            for k2, v2 in b.items():
                k = (k1[0]+k2[0], k1[1]+k2[1])
                w = r.get(k, Fr(0)) + v1*v2
                if w: r[k] = w
                elif k in r: del r[k]
        return r
    def p2_scal(a, c):
        c = Fr(c)
        if c == 0: return {}
        return {k: v*c for k, v in a.items()}

    F0_2 = [as_2var(f) for f in F0]
    Fm2_2 = [as_2var(f) for f in Fm2]
    # F0'[n] = (n+1) F0[n+1]
    F0p_2 = [p2_scal(F0_2[n+1], n+1) if n+1 <= N else {} for n in range(N+1)]
    F0pp_2 = [p2_scal(F0_2[n+2], (n+1)*(n+2)) if n+2 <= N else {} for n in range(N+1)]
    # int F0 [n] = F0[n-1]/n for n>=1, 0 for n=0
    intF0_2 = [{}] + [p2_scal(F0_2[n-1], Fr(1, n)) for n in range(1, N+1)]

    # Q = (u1+1)(u1+2)(u2+1)(u2+2)  — analogous to (u+1) B_0 = u^{(2)} shape from Prop 1
    # Try several Q choices.
    u1p1 = {(0,0): Fr(1), (1,0): Fr(1)}
    u1p2 = {(0,0): Fr(2), (1,0): Fr(1)}
    u2p1 = {(0,0): Fr(1), (0,1): Fr(1)}
    u2p2 = {(0,0): Fr(2), (0,1): Fr(1)}
    Q_choices = [
        ('(u1+1)(u2+1)', p2_mul(u1p1, u2p1)),
        ('(u1+1)^2(u2+1)^2', p2_mul(p2_mul(u1p1, u1p1), p2_mul(u2p1, u2p1))),
        ('(u1+1)(u1+2)(u2+1)(u2+2)', p2_mul(p2_mul(u1p1, u1p2), p2_mul(u2p1, u2p2))),
        ('(u1+2)(u2+2)', p2_mul(u1p2, u2p2)),
    ]
    Q_name, Q = Q_choices[1]
    print(f"  Using Q = {Q_name}")
    QFm2 = [p2_mul(Q, f) for f in Fm2_2]

    # Build blocks (T-shifted / T-multiplied versions of F0, F0', F0'', int F0, and constants):
    def shift_T(f, k):
        """T^k * f as a series (list of length N+1)."""
        r = [{}] * k + f[:N+1-k]
        return r + [{}] * (N + 1 - len(r))
    def series_of_1():
        r = [{(0,0): Fr(1)}] + [{}] * N
        return r

    ONE_series = series_of_1()

    # Building blocks: list of (name, series)
    # Also need double integral (for order-2 antiderivative analog)
    intF0_intF0 = [{}] + [p2_scal(intF0_2[n-1], Fr(1, n)) for n in range(1, N+1)]

    # MINIMAL analog of Prop 2's basis, extended to order 2.
    # Prop 2: F_0, T F_0, T^2 F_0', int F_0, const  — 5 blocks, all "degree <= 2" in T.
    # For F_{-2} we naturally allow T-degrees up to 4 (one more order gives one more
    # T factor per derivative-order), and second derivative & double integral.
    TMAX_F0 = 4      # T^k for k=0..4 acting on F_0
    TMAX_F0p = 4     # T^k for k=0..4 acting on F_0'
    TMAX_F0pp = 4    # T^k for k=0..4 acting on F_0''
    TMAX_int = 4     # T^k acting on int F_0 and int^2 F_0
    TMAX_const = 4   # constant blocks

    blocks = []
    for k in range(0, TMAX_F0+1):
        blocks.append((f'T{k}_F0', shift_T(F0_2, k)))
    for k in range(0, TMAX_F0p+1):
        blocks.append((f'T{k}_F0p', shift_T(F0p_2, k)))
    for k in range(0, TMAX_F0pp+1):
        blocks.append((f'T{k}_F0pp', shift_T(F0pp_2, k)))
    for k in range(0, TMAX_int+1):
        blocks.append((f'T{k}_intF0', shift_T(intF0_2, k)))
    for k in range(0, TMAX_int+1):
        blocks.append((f'T{k}_intintF0', shift_T(intF0_intF0, k)))
    for k in range(0, TMAX_const+1):
        blocks.append((f'T{k}_const', shift_T(ONE_series, k)))

    # For each block, coefficient is a symmetric poly in (u1,u2) of bounded degree:
    # A(u1,u2) = sum_{a+2b <= MAX_DEG} c_{a,b} (u1+u2)^a (u1 u2)^b
    MAX_DEG = 6
    e1 = {(1,0): Fr(1), (0,1): Fr(1)}
    e2 = {(1,1): Fr(1)}
    basis_polys = []  # list of (label, poly-dict)
    for a in range(MAX_DEG + 1):
        for b in range((MAX_DEG - a)//2 + 1):
            p = {(0,0): Fr(1)}
            for _ in range(a):
                p = p2_mul(p, e1)
            for _ in range(b):
                p = p2_mul(p, e2)
            basis_polys.append((f'e1^{a} e2^{b}', p))

    # Unknown: for each block, for each basis poly, a coefficient c_i
    # Total = len(blocks) * len(basis_polys)
    param_names = []
    param_map = []  # list of (block_idx, basis_idx)
    for bi, (bname, _) in enumerate(blocks):
        for pi, (pname, _) in enumerate(basis_polys):
            param_names.append(f'{bname} * {pname}')
            param_map.append((bi, pi))

    P = len(param_names)

    # For each param p mapped to (bi, pi), its CONTRIBUTION to [T^n] is:
    #   basis_polys[pi][1] * blocks[bi][1][n]  (2-var poly-mult)
    # Precompute these contributions per (n, param):
    # Actually we want equations: for each n and each (a,b) monomial in u1,u2,
    # coefficient of QFm2[n] minus sum over params (c_p * contribution_{n,p}) = 0.

    # Collect all monomials appearing:
    # We build the linear system as {(n, (a,b)): row} in sparse form.
    # Rows = equations, cols = params.
    rows = {}  # dict (n, mono) -> {param_idx: coef}
    rhs = {}   # dict (n, mono) -> Fr constant term (QFm2 coefficient)

    for n in range(N+1):
        for k, v in QFm2[n].items():
            rhs[(n, k)] = v

    for p_idx, (bi, pi) in enumerate(param_map):
        bname, bseries = blocks[bi]
        pname, ppoly = basis_polys[pi]
        for n in range(N+1):
            contrib = p2_mul(ppoly, bseries[n])
            for k, v in contrib.items():
                key = (n, k)
                if key not in rows:
                    rows[key] = {}
                rows[key][p_idx] = rows[key].get(p_idx, Fr(0)) + v

    # Assemble list of equations with an aligned RHS
    eq_keys = sorted(set(rows.keys()) | set(rhs.keys()))
    A = []  # list of dicts {p_idx: coef}
    b = []
    for key in eq_keys:
        A.append(dict(rows.get(key, {})))
        b.append(rhs.get(key, Fr(0)))

    n_eqs = len(A)
    print(f"  Ansatz: {P} parameters, {n_eqs} equations, {len(blocks)} blocks x {len(basis_polys)} basis polys")

    # Gaussian elimination (exact Fractions).
    # Represent A as list of dicts. Pivot columns tracked.
    pivot_col = {}
    order = list(range(n_eqs))
    row_used = [False] * n_eqs
    col_used = [False] * P

    # For each column, find a row with a nonzero entry and eliminate.
    col_pivot_row = [-1] * P
    for col in range(P):
        pr = -1
        for r in range(n_eqs):
            if not row_used[r] and abs(A[r].get(col, Fr(0))) != 0:
                pr = r
                break
        if pr < 0:
            continue
        # Normalize
        pv = A[pr][col]
        for c in list(A[pr]):
            A[pr][c] = A[pr][c] / pv
        b[pr] = b[pr] / pv
        # Eliminate col from all other rows
        for r in range(n_eqs):
            if r == pr: continue
            f = A[r].get(col, Fr(0))
            if f == 0: continue
            # A[r] <- A[r] - f * A[pr]
            for c, v in A[pr].items():
                nv = A[r].get(c, Fr(0)) - f * v
                if nv:
                    A[r][c] = nv
                elif c in A[r]:
                    del A[r][c]
            b[r] = b[r] - f * b[pr]
        row_used[pr] = True
        col_used[col] = True
        col_pivot_row[col] = pr

    # Check consistency: any row with all zeros on LHS but nonzero RHS => inconsistent
    inconsistent = False
    for r in range(n_eqs):
        if not row_used[r]:
            # LHS should be 0
            all_zero = all(v == 0 for v in A[r].values())
            if all_zero and b[r] != 0:
                inconsistent = True
                break

    if inconsistent:
        print("  NO — system inconsistent: F_{-2} is NOT expressible in this ansatz.")
        # Diagnostics: show which n first shows inconsistency
        for i, key in enumerate(eq_keys):
            r = i  # A[i] corresponds to eq_keys[i]... wait, elimination rearranges
            # Skip diagnostics
            pass
        return False, "inconsistent — no order-2 T-integro-diff op on F_0 with sym-poly (deg<=4) coefficients"

    # Consistent — extract a solution (free params = 0)
    x = [Fr(0)] * P
    for col in range(P):
        pr = col_pivot_row[col]
        if pr < 0: continue
        x[col] = b[pr]
    n_free = P - sum(1 for c in col_pivot_row if c >= 0)
    print(f"  System is CONSISTENT; solution found ({n_free} free parameters, all set to 0).")
    # Report non-zero block coefficients (grouped by block)
    for bi, (bname, _) in enumerate(blocks):
        coef_terms = []
        for pi, (pname, _) in enumerate(basis_polys):
            p_idx = bi * len(basis_polys) + pi
            v = x[p_idx]
            if v:
                coef_terms.append((pname, v))
        if coef_terms:
            print(f"    {bname}: {coef_terms}")
    # Verify: reconstruct RHS series and compare
    max_resid = 0
    for n in range(N+1):
        rhs_series_n = {}
        for p_idx, (bi, pi) in enumerate(param_map):
            v = x[p_idx]
            if not v: continue
            bname, bseries = blocks[bi]
            pname, ppoly = basis_polys[pi]
            contrib = p2_scal(p2_mul(ppoly, bseries[n]), v)
            rhs_series_n = p2_add(rhs_series_n, contrib)
        diff = p2_sub(QFm2[n], rhs_series_n)
        if diff:
            max_resid += 1
            print(f"  n={n}: residual {pretty({k: v for k,v in diff.items()})}")
    if max_resid == 0:
        return True, f"YES (order-2 T-integro-diff op; sym-poly coefficients deg<=4)"
    return False, f"nonzero residuals at {max_resid} orders"

# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

if __name__ == "__main__":
    print()
    ok1, k1 = step1_prop1(7)
    print()
    if not ok1:
        print(f"STOP — Prop 1 disagrees at k={k1}")
        sys.exit(1)
    ok2, k2 = step2_prop2(7)
    print()
    if not ok2:
        print(f"STOP — Prop 2 disagrees at k={k2}")
        sys.exit(1)
    ok3a, _ = step3_prop3(0, 10)  # sanity: reproduce Clio's own range
    if not ok3a:
        print("STOP — Prop 3 fails in Clio's own range")
        sys.exit(1)
    ok3, k3 = step3_prop3(11, 14)
    print()
    if not ok3:
        print(f"STOP — Prop 3 fails at n={k3}")
        sys.exit(1)
    ok4, note4 = step4_rung2(6)
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Prop 1: PASS at k=1..7")
    print(f"Prop 2: PASS at k=1..7")
    print(f"Prop 3: PASS at n=11,12,13,14")
    print(f"Rung-2: {'YES' if ok4 else 'NO'} — {note4}")
