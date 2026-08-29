"""Day 114 follow-up: Verify uniform ansatz at p = 4 and hunt for closed-form
alpha_{p,k}(j, sigma).

Ansatz (verified for p in {2, 3}, checking here for p = 4):
    A_p = sum_{k=0}^{p} alpha_{p,k}(j, sigma) * pi^k * (sigma - 2p - 1)^{↓(j - 2p)}
where pi = (b+1)*c, sigma = b + c + 1.

Empirical extremes so far:
    alpha_{p,p}(j, sigma) = (j)_p / p! * prod_{i=1..p} (sigma - j - i - 1)
    alpha_{p,0}(j, sigma) = C_p(j) * (sigma-1)(sigma-2)...(sigma-2p)

Goals of this script:
    (1) verify ansatz at p = 4 (need j >= 8, use j = 8..12);
    (2) print alpha_{p,k} tables for p in {2, 3, 4}, all k;
    (3) hunt for a closed-form pattern in the middle alpha_{p,k};
    (4) check vanishing pattern of A_p at partition points (shifted-Schur ideal);
    (5) dump everything to .txt.
"""

from collections import defaultdict
from itertools import combinations, product

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational, factor, binomial, Symbol

a, b, c = symbols('a b c')
u = a + 2
sig, pi_v = symbols('sigma pi')
j_sym = symbols('j')
tau = symbols('tau')

# ---------------------------------------------------------------------------
# Day-113 machinery.
# ---------------------------------------------------------------------------


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


def bt(M):
    def vs(mu):
        L = len(mu) + 2
        bb = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = bb.copy()
            for i in p:
                n[i] += 1
            ok = True
            for i in range(L - 1):
                if n[i] < n[i + 1]:
                    ok = False
                    break
            if not ok:
                continue
            while n and n[-1] == 0:
                n.pop()
            if len(n) > 3:
                continue
            r.append(tuple(n))
        return r
    cu = defaultdict(int)
    cu[()] = 1
    T = {0: [((0, 0, 0), 1)]}
    for jj in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[jj] = rs
    return T


def ds_symbolic(jj, tables):
    xs = (u, b + 1, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def V_of():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def dsV_all(J, tables):
    V = V_of()
    cache = {}
    for jj in range(J + 1):
        dsj = ds_symbolic(jj, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0
        cache[jj] = q.as_expr()
    return cache


def extract_A_p(jj, p, dsV_cache):
    S = dsV_cache[jj]
    if jj - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == jj - p:
            result += cf * b**db * c**dc
    return expand(result)


# ---------------------------------------------------------------------------
# Symmetry test and change of variables.
# ---------------------------------------------------------------------------


def is_sym_bc1(F):
    F_swap = F.subs([(b, symbols('_t1')), (c, symbols('_t2'))], simultaneous=True)
    F_swap = F_swap.subs([(symbols('_t1'), c - 1), (symbols('_t2'), b + 1)])
    return expand(F - expand(F_swap)) == 0


def to_pi_sigma_shifted(F):
    """F(b, c) -> F(pi, sigma) with pi = (b+1)*c, sigma = b + c + 1."""
    z = symbols('_z_pi_sig_')
    Fz = expand(F.subs([(b, z - 1), (c, sig - z)]))
    Pz = sp.Poly(Fz, z)
    D = Pz.degree()
    coefs = [Pz.coeff_monomial(z ** i) for i in range(D + 1)]
    while len(coefs) > 2:
        top = coefs[-1]
        d = len(coefs) - 1
        if top == 0:
            coefs.pop()
            continue
        coefs[d - 1] = sp.expand(coefs[d - 1] + sig * top)
        coefs[d - 2] = sp.expand(coefs[d - 2] - pi_v * top)
        coefs.pop()
    while len(coefs) < 2:
        coefs.append(Integer(0))
    if sp.simplify(coefs[1]) != 0:
        return None
    return sp.expand(coefs[0])


# ---------------------------------------------------------------------------
# Fit F_ps(pi, sigma) as sum_{k=0..k_max} alpha_k(sigma) * pi^k * fall_shifted.
# ---------------------------------------------------------------------------


def falling_sigma(shift, length):
    if length <= 0:
        return Integer(1) if length == 0 else None
    r = Integer(1)
    for i in range(length):
        r *= (sig - shift - i)
    return sp.expand(r)


def fit_in_pi_sigma(F_ps, k_max, shift, length, D_alpha):
    fall_sig = falling_sigma(shift, length)
    unknowns = []
    basis_map = {}
    for k in range(k_max + 1):
        for d in range(D_alpha + 1):
            basis_map[(k, d)] = sp.expand(pi_v ** k * fall_sig * sig ** d)
            unknowns.append((k, d))
    syms = symbols(' '.join(f'x_{k}_{d}' for (k, d) in unknowns))
    if not isinstance(syms, tuple):
        syms = (syms,)
    expr = sp.expand(sum(syms[i] * basis_map[unknowns[i]] for i in range(len(unknowns))) - F_ps)
    P = sp.Poly(expr, pi_v, sig)
    eqs = [cf for _, cf in P.terms()]
    sol = sp.solve(eqs, syms, dict=True)
    if not sol:
        return None
    s = sol[0]
    for x in syms:
        if x not in s:
            s[x] = Integer(0)
    pred = sp.expand(sum(s[syms[i]] * basis_map[unknowns[i]] for i in range(len(unknowns))))
    if sp.expand(pred - F_ps) != 0:
        return None
    result = {}
    for k in range(k_max + 1):
        alpha_k = Integer(0)
        for d in range(D_alpha + 1):
            alpha_k += s[symbols(f'x_{k}_{d}')] * sig ** d
        result[k] = sp.expand(alpha_k)
    return result


def fit_j_poly(samples, name, max_deg=14, log=None):
    n = len(samples)
    for D in range(min(n, max_deg + 1)):
        rows = []
        yy = []
        for (jv, yv) in samples[:D + 1]:
            rows.append([Rational(jv) ** i for i in range(D + 1)])
            yy.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        try:
            sol = M.solve(y)
        except Exception:
            continue
        ok = True
        for (jv, yv) in samples[D + 1:]:
            pred = sum(sol[i] * jv ** i for i in range(D + 1))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            poly = sum(sol[i] * j_sym ** i for i in range(D + 1))
            msg = f"      {name}: deg-{D} in j, poly = {sp.factor(sp.expand(poly))}"
            if log is not None:
                log.append(msg)
            print(msg)
            return poly
    msg = f"      {name}: NO polynomial-in-j fit up to degree {max_deg}"
    if log is not None:
        log.append(msg)
    print(msg)
    return None


def fit_bivariate_poly_sj(samples_by_j, name, max_deg_j=14, log=None):
    all_D = 0
    for jj, alpha in samples_by_j.items():
        deg = sp.Poly(alpha, sig).degree() if alpha != 0 else -1
        all_D = max(all_D, deg)
    if all_D < 0:
        msg = f"    {name}: identically 0."
        if log is not None:
            log.append(msg)
        print(msg)
        return {}
    result = {}
    for d in range(all_D + 1):
        samples = []
        for jj in sorted(samples_by_j.keys()):
            alpha = samples_by_j[jj]
            coef_d = sp.Poly(alpha, sig).coeff_monomial(sig ** d) if alpha != 0 else Integer(0)
            samples.append((jj, coef_d))
        beta = fit_j_poly(samples, f"{name}[sigma^{d}]", max_deg=max_deg_j, log=log)
        result[d] = beta
    return result


# ---------------------------------------------------------------------------
# Utility: reconstruct alpha_{p,k}(j, sigma) as bivariate poly, factor over
#   (sigma), (sigma - j), and factor beta polynomials in j.
# ---------------------------------------------------------------------------


def alpha_pk_as_bivariate(coef_forms):
    """coef_forms: {d: beta(j)} -> polynomial in (j, sigma)."""
    result = Integer(0)
    for d, beta in coef_forms.items():
        if beta is None:
            beta = Integer(0)
        result += beta * sig ** d
    return sp.expand(result)


def specialize_j(F_js, jv):
    return sp.expand(F_js.subs(j_sym, jv))


def try_tau_substitution(F_js, log=None):
    """Substitute sigma -> tau + j and factor. Reveals if alpha depends on
    sigma - j only, or has clean structure in tau."""
    G = sp.expand(F_js.subs(sig, tau + j_sym))
    G_f = sp.factor(G)
    msg = f"      substitute sigma = tau + j:  {G_f}"
    if log is not None:
        log.append(msg)
    print(msg)
    return G


# ---------------------------------------------------------------------------
# Vanishing pattern hunt: evaluate A_p at partition points (b, c) = mu shifts.
# ---------------------------------------------------------------------------


def hunt_vanishing_A_p(dsV, p, jj, log=None):
    """For A_p(b, c, j=jj), find (b, c) values (integers, small) where A_p = 0.

    Shifted-Schur intuition: pi = (b+1)c, sigma = b+c+1 corresponds to a
    partition mu = (mu_1, mu_2) with mu_1 = c (top row), mu_2 = b + 1 (via
    the (c-1, b+1) symmetry -> partition-like). The shifted-Schur basis
    s^*_lambda vanishes on partitions of size < |lambda|.

    Scan a small box of (b, c) integer values; report zeros.
    """
    A_p = extract_A_p(jj, p, dsV)
    zeros = []
    box = 6  # scan (b, c) in [-box, box]^2
    for bv in range(-2, box + 1):
        for cv in range(0, box + 1):
            val = sp.expand(A_p.subs([(b, bv), (c, cv)]))
            if val == 0:
                zeros.append((bv, cv))
    msg = f"    A_{p}(j={jj}) vanishes at {len(zeros)} integer (b, c) pts in [-2..{box}] x [0..{box}]"
    if log is not None:
        log.append(msg)
    print(msg)
    for z in zeros:
        bv, cv = z
        piv = (bv + 1) * cv
        sgv = bv + cv + 1
        msg = f"      (b, c) = {z}   pi = {piv}, sigma = {sgv}"
        if log is not None:
            log.append(msg)
        print(msg)
    return zeros


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main():
    log = []

    def W(msg=""):
        print(msg)
        log.append(msg)

    J = 12
    W(f"Building shifted-Schur tables & ds_j/V up to j = {J}...")
    tables = bt(J)
    dsV = dsV_all(J, tables)

    # -----------------------------------------------------------------
    # STEP (1): Verify ansatz for p = 4, j = 8..12
    # -----------------------------------------------------------------
    W("\n" + "=" * 72)
    W("STEP 1  Verify ansatz at p = 4.")
    W("        Fit A_4 = sum_{k=0..4} alpha_k(sigma) * pi^k * (sigma-9)^{↓(j-8)}")
    W("=" * 72)

    A4_ps = {}
    all_alpha_A4 = {}
    for jj in range(8, J + 1):
        A4 = extract_A_p(jj, 4, dsV)
        sym_ok = is_sym_bc1(A4)
        F_ps = to_pi_sigma_shifted(A4)
        A4_ps[jj] = F_ps
        Pps = sp.Poly(F_ps, pi_v, sig)
        W(f"  j = {jj}: symmetric under (b,c)->(c-1,b+1)? {sym_ok};  "
          f"(deg_pi, deg_sig) = ({Pps.degree(pi_v)}, {Pps.degree(sig)})")

    W("")
    for jj in range(8, J + 1):
        length = jj - 8
        shift = 9  # 2p + 1
        F_ps = A4_ps[jj]
        found = None
        for D_alpha in range(0, 10):
            sol = fit_in_pi_sigma(F_ps, k_max=4, shift=shift, length=length, D_alpha=D_alpha)
            if sol is not None:
                found = (D_alpha, sol)
                break
        if found is None:
            W(f"  j = {jj}: FAILED to fit with shift={shift}, length={length}, k_max=4.")
            continue
        D_alpha, sol = found
        all_alpha_A4[jj] = sol
        W(f"  j = {jj}: FIT with D_alpha = {D_alpha}.")
        for k in range(5):
            alpha_k = sol[k]
            deg_sig_k = sp.Poly(alpha_k, sig).degree() if alpha_k != 0 else -1
            W(f"      alpha_{{4,{k}}}(sigma) [deg_sig={deg_sig_k}] = {sp.factor(alpha_k)}")

    W("\nAnsatz status at p=4: " + ("VERIFIED" if len(all_alpha_A4) == 5 else "FAILED"))

    # -----------------------------------------------------------------
    # STEP (2): Extract alpha_{p,k} bivariate poly form for p in {2,3,4}
    # -----------------------------------------------------------------

    # First recompute for p = 2, 3 to have everything unified
    W("\n" + "=" * 72)
    W("STEP 2  Extract alpha_{p,k}(j, sigma) for p in {2, 3, 4}, all k.")
    W("=" * 72)

    def collect_alphas_for_p(p, j_start, shift, k_max, D_alpha_cap=10):
        """Returns {jj: {k: alpha_k(sigma)}}."""
        alphas = {}
        for jj in range(j_start, J + 1):
            A_p = extract_A_p(jj, p, dsV)
            if not is_sym_bc1(A_p):
                continue
            F_ps = to_pi_sigma_shifted(A_p)
            if F_ps is None:
                continue
            length = jj - 2 * p
            found = None
            for D_alpha in range(0, D_alpha_cap):
                sol = fit_in_pi_sigma(F_ps, k_max=k_max, shift=shift, length=length, D_alpha=D_alpha)
                if sol is not None:
                    found = sol
                    break
            if found is not None:
                alphas[jj] = found
        return alphas

    # (Re)compute A_2, A_3, A_4 alphas
    alphas_all = {}   # {p: {jj: {k: alpha_k(sigma)}}}
    alphas_all[2] = collect_alphas_for_p(p=2, j_start=4, shift=5, k_max=2)
    alphas_all[3] = collect_alphas_for_p(p=3, j_start=6, shift=7, k_max=3)
    alphas_all[4] = all_alpha_A4

    coef_forms = {}   # {p: {k: {d: beta(j)}}}
    for p in (2, 3, 4):
        coef_forms[p] = {}
        W(f"\n  === p = {p} ===")
        for k in range(p + 1):
            W(f"\n  --- alpha_{{{p},{k}}}(j, sigma) ---")
            samples = {jj: alphas_all[p][jj].get(k, Integer(0)) for jj in sorted(alphas_all[p].keys())}
            beta_dict = fit_bivariate_poly_sj(samples, f"alpha_{{{p},{k}}}", log=log)
            coef_forms[p][k] = beta_dict

    # -----------------------------------------------------------------
    # STEP (3): Hunt for closed-form pattern.
    # -----------------------------------------------------------------
    W("\n" + "=" * 72)
    W("STEP 3  Hunt for closed-form pattern in alpha_{p,k}.")
    W("=" * 72)

    # (3a) Confirm alpha_{p,p} formula
    W("\n  --- (3a) Check alpha_{p,p} = (j)_p/p! * prod_{i=1..p} (sigma - j - i - 1) ---")
    for p in (2, 3, 4):
        conjecture = sp.Rational(1)
        # (j)_p / p! = binomial(j, p)
        conjecture = binomial(j_sym, p)
        for i in range(1, p + 1):
            conjecture *= (sig - j_sym - i - 1)
        emp = alpha_pk_as_bivariate(coef_forms[p][p])
        diff = sp.expand(emp - conjecture)
        status = "MATCH" if diff == 0 else "MISMATCH"
        W(f"    p = {p}: {status}")
        W(f"      conjecture = {sp.factor(conjecture)}")
        W(f"      empirical  = {sp.factor(emp)}")
        if diff != 0:
            W(f"      diff = {sp.expand(diff)}")

    # (3b) Check alpha_{p,0} = C_p(j) * (sigma-1)_↓(2p)
    W("\n  --- (3b) Check alpha_{p,0} = C_p(j) * (sigma-1)^{↓(2p)}; report C_p(j) ---")
    C_ps = {}
    for p in (2, 3, 4):
        emp = alpha_pk_as_bivariate(coef_forms[p][0])
        # (sigma-1)_(2p) falling: (sigma-1)(sigma-2)...(sigma-2p)
        fall = falling_sigma(1, 2 * p)
        # Divide emp / fall as polynomial in sigma
        q, r = sp.div(sp.Poly(emp, sig), sp.Poly(fall, sig))
        rem = sp.expand(r.as_expr())
        if rem != 0:
            W(f"    p = {p}: DOES NOT DIVIDE cleanly by (sigma-1)^↓{2*p}; remainder = {rem}")
            continue
        C = sp.expand(q.as_expr())
        # C should be poly in j only
        C_ps[p] = C
        W(f"    p = {p}: C_p(j) = {sp.factor(C)}")
        # Sanity: does C contain sigma?
        if sig in sp.sympify(C).free_symbols:
            W(f"       WARNING: C contains sigma!")

    # (3c) Middle alpha_{p,k}: try various factorizations
    W("\n  --- (3c) Middle alpha_{p,k}: try factorization hunts ---")
    for p in (2, 3, 4):
        for k in range(p + 1):
            emp = alpha_pk_as_bivariate(coef_forms[p][k])
            W(f"\n    alpha_{{{p},{k}}}(j, sigma):")
            W(f"      raw factored:  {sp.factor(emp)}")
            # Try sigma -> tau + j substitution
            try_tau_substitution(emp, log=log)
            # Try sigma -> tau + 2p substitution (near shift)
            G = sp.expand(emp.subs(sig, tau + 2 * p))
            W(f"      substitute sigma = tau + 2p (= tau + {2*p}):  {sp.factor(G)}")
            # Try factorization of leading sigma coefficient in j (Pochhammer hunt)
            deg_sig = sp.Poly(emp, sig).degree() if emp != 0 else -1
            if deg_sig >= 0:
                lead = sp.Poly(emp, sig).LC()
                W(f"      leading sigma^{deg_sig} coefficient = {sp.factor(lead)}")
                trail = sp.Poly(emp, sig).nth(0) if deg_sig >= 0 else 0
                W(f"      sigma^0 coefficient = {sp.factor(trail)}")

    # (3d) Try binomial(j, p-k) factorization: does alpha_{p,k} / binomial(j, p-k)
    # have clean form?
    W("\n  --- (3d) Check alpha_{p,k} / binomial(j, p-k) for cleanness ---")
    for p in (2, 3, 4):
        for k in range(p + 1):
            emp = alpha_pk_as_bivariate(coef_forms[p][k])
            binom = binomial(j_sym, p - k)
            binom_ex = sp.expand(binom * sp.factorial(p - k))  # polynomial form
            # Numerator: alpha * (p-k)!
            emp_scaled = sp.expand(emp * sp.factorial(p - k))
            # Try to divide out (j)(j-1)...(j-p+k+1)
            fj = Integer(1)
            for i in range(p - k):
                fj *= (j_sym - i)
            q, r = sp.div(sp.Poly(emp_scaled, j_sym), sp.Poly(fj, j_sym))
            if sp.expand(r.as_expr()) == 0:
                Q = sp.expand(q.as_expr())
                W(f"    alpha_{{{p},{k}}} / binomial(j, {p-k})  =  {sp.factor(Q)}")
            else:
                W(f"    alpha_{{{p},{k}}}: (j)_{p-k} does NOT divide cleanly")

    # -----------------------------------------------------------------
    # STEP (4): Vanishing pattern of A_p at partition points
    # -----------------------------------------------------------------
    W("\n" + "=" * 72)
    W("STEP 4  Vanishing pattern of A_p at integer (b, c) points.")
    W("        Corresponds to shifted-Schur vanishing at 'partitions'.")
    W("=" * 72)

    for p in (1, 2, 3):
        W(f"\n  ~~ A_{p} vanishing scan ~~")
        j_min = max(2 * p, p + 1)
        for jj in range(max(j_min, 4), min(j_min + 3, J + 1)):
            hunt_vanishing_A_p(dsV, p, jj, log=log)

    # (4b) Try substituting partition points in (pi, sigma)-form and see structure
    W("\n  ~~ A_p(pi, sigma) evaluated at partition-point (pi, sigma) values ~~")
    W("     (b, c) integer points -> compute (pi, sigma), evaluate A_p_ps.")
    for p in (2, 3):
        for jj in [2 * p, 2 * p + 1, 2 * p + 2]:
            if jj > J:
                continue
            A_p = extract_A_p(jj, p, dsV)
            if not is_sym_bc1(A_p):
                continue
            F_ps = to_pi_sigma_shifted(A_p)
            W(f"\n    A_{p}(j={jj}) in (pi, sigma):")
            # Test small "partition" points: (mu_1, mu_2) with mu_1 >= mu_2 >= 0
            # via z = b+1, sigma - z = c, so partition (mu_1, mu_2) ~ pairs (z=mu_1, sigma - z = mu_2)
            # meaning pi = mu_1 * mu_2, sigma = mu_1 + mu_2
            zeros_ps = []
            for mu1 in range(0, 7):
                for mu2 in range(0, mu1 + 1):
                    pi_val = mu1 * mu2
                    sig_val = mu1 + mu2
                    val = sp.expand(F_ps.subs([(pi_v, pi_val), (sig, sig_val)]))
                    if val == 0:
                        zeros_ps.append((mu1, mu2, pi_val, sig_val))
            W(f"      zeros at partition pts (mu_1 >= mu_2 >= 0, mu_1 <= 6): {len(zeros_ps)} found")
            for (m1, m2, pv, sv) in zeros_ps[:20]:
                W(f"        mu = ({m1}, {m2}), (pi, sigma) = ({pv}, {sv}), |mu| = {m1+m2}")

    # -----------------------------------------------------------------
    # STEP (5): save log
    # -----------------------------------------------------------------
    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-day114-A4-verify-and-alpha-closed-forms.txt"
    with open(out_path, "w") as f:
        f.write("\n".join(log))
    W(f"\n[log saved to {out_path}]")


if __name__ == "__main__":
    main()
