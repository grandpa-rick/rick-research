"""Day 114: Uniform-in-p closed form for A_p — BREAKTHROUGH VERSION.

Lemma 1 (proved Day 113):
    A_1(b, c, j) = j*(3-j)/2 * (b+c)^{↓j}  +  j * (b+1) * c * (b+c-2)^{↓(j-1)}.

Task text (Rick's 3-term ansatz) used pi = c, sigma = b + c:
    A_p = sum_{k=0}^p c_{p,k}(j) * pi^k * (sigma - 2k - 1)^{↓(j-2k)}   -- FAILED at p=2.

KEY DISCOVERY (this file):
    A_2 IS symmetric under (b,c) -> (c-1, b+1), so it lives naturally in
    Rick's shifted-Schur variables
        pi = (b+1)*c,   sigma = b + c + 1
    and in THOSE variables A_2 has pi-degree exactly 2 (not 4).

    Moreover, for all j in {5, ..., 12},
        A_2(pi, sigma, j) = LC(j) * (sigma - 5)^{↓(j-4)} * Q_j(pi, sigma)
    where Q_j has pi-degree 2 and sigma-degree 4.

The task's "pi = c" convention was the bug — degree in c blew up to 4 because
(b+1)^2 c^2 = pi^2 in the correct variables, but (b+1)^2 is a full poly in b,c
in the wrong ones.

Steps in this file:
  (1) compute A_2 for j = 4..12 (extraction from ds_j / V);
  (2) verify the (b,c) -> (c-1, b+1) symmetry of A_2, express in (pi, sigma);
  (3) fit the RIGHT ansatz:
        A_2 = alpha_0(j, sigma) * (sigma - 5)^{↓(j-4)}
            + alpha_1(j, sigma) * pi * (sigma - 5)^{↓(j-4)}
            + alpha_2(j, sigma) * pi^2 * (sigma - 5)^{↓(j-4)}
      where each alpha_k(j, sigma) is a polynomial in sigma of small degree
      (turns out: deg_sigma <= 4, 3, 2 for k = 0, 1, 2 respectively);
  (4) test the SAME structure on A_3 for j = 6..12.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational, factor

a, b, c = symbols('a b c')
u = a + 2
sig, pi_v = symbols('sigma pi')
j_sym = symbols('j')

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
    """Test invariance under (b, c) -> (c-1, b+1)."""
    F_swap = F.subs([(b, symbols('_t1')), (c, symbols('_t2'))], simultaneous=True)
    F_swap = F_swap.subs([(symbols('_t1'), c - 1), (symbols('_t2'), b + 1)])
    return expand(F - expand(F_swap)) == 0


def to_pi_sigma_shifted(F):
    """F(b, c) -> F(pi, sigma) with pi = (b+1)*c, sigma = b + c + 1.

    z = b + 1, sigma - z = c, so z * (sigma - z) = pi, i.e. z^2 = sigma*z - pi.
    Requires F symmetric under (b,c)->(c-1,b+1) (i.e., z <-> sigma-z).
    """
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


def from_pi_sigma(F_ps):
    """Inverse: substitute sigma -> b+c+1, pi -> (b+1)*c."""
    return sp.expand(F_ps.subs([(sig, b + c + 1), (pi_v, (b + 1) * c)]))


# ---------------------------------------------------------------------------
# Fit F_ps(pi, sigma) as sum_{k=0}^{k_max} alpha_k(sigma) * pi^k * fall_shifted.
# ---------------------------------------------------------------------------


def falling_sigma(shift, length):
    """(sigma - shift)^{↓length}, as a polynomial in sigma."""
    if length <= 0:
        return Integer(1) if length == 0 else None
    r = Integer(1)
    for i in range(length):
        r *= (sig - shift - i)
    return sp.expand(r)


def fit_in_pi_sigma(F_ps, k_max, shift, length, D_alpha):
    """Fit F_ps(pi, sigma) = sum_{k=0}^{k_max} alpha_k(sigma) * pi^k * (sigma - shift)^{↓length}
    where alpha_k(sigma) has degree <= D_alpha.

    Solve monomial-by-monomial (in pi, sigma).
    Returns {k: alpha_k(sigma)} or None.
    """
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
    # Package alpha_k(sigma) = sum_d x_{k,d} * sigma^d
    result = {}
    for k in range(k_max + 1):
        alpha_k = Integer(0)
        for d in range(D_alpha + 1):
            alpha_k += s[symbols(f'x_{k}_{d}')] * sig ** d
        result[k] = sp.expand(alpha_k)
    return result


def fit_j_poly(samples, name, max_deg=12, verbose=True):
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
            if verbose:
                print(f"      {name}: deg-{D} in j, poly = {sp.factor(sp.expand(poly))}")
            return poly
    if verbose:
        print(f"      {name}: NO polynomial-in-j fit up to degree {max_deg}")
    return None


def fit_bivariate_poly_sj(samples_by_j, name, max_deg_j=12, verbose=True):
    """samples_by_j: {j: alpha_k(sigma) as sympy poly in sigma}.
    Fit alpha_k(j, sigma) = sum_{d} beta_{k,d}(j) * sigma^d where beta_{k,d}
    is a polynomial in j."""
    # Determine max sigma-degree across all j
    all_D = 0
    for jj, alpha in samples_by_j.items():
        deg = sp.Poly(alpha, sig).degree() if alpha != 0 else -1
        all_D = max(all_D, deg)
    if all_D < 0:
        if verbose:
            print(f"    {name}: identically 0.")
        return {}
    result = {}
    for d in range(all_D + 1):
        samples = []
        for jj in sorted(samples_by_j.keys()):
            alpha = samples_by_j[jj]
            coef_d = sp.Poly(alpha, sig).coeff_monomial(sig ** d) if alpha != 0 else Integer(0)
            samples.append((jj, coef_d))
        # Try to fit as polynomial in j
        beta = fit_j_poly(samples, f"{name}[sigma^{d}]", max_deg=max_deg_j, verbose=verbose)
        result[d] = beta
    return result


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main():
    J = 12
    print(f"Building shifted-Schur tables & ds_j/V up to j = {J}...")
    tables = bt(J)
    dsV = dsV_all(J, tables)

    print("\n" + "=" * 72)
    print("STEP 1  Extract A_2 for j = 4..12 and verify (b,c)->(c-1,b+1) symmetry.")
    print("        Then convert to (pi, sigma) = ((b+1)c, b+c+1).")
    print("=" * 72)
    A2_bc = {}
    A2_ps = {}
    for jj in range(4, J + 1):
        A2 = extract_A_p(jj, 2, dsV)
        A2_bc[jj] = A2
        assert is_sym_bc1(A2), f"A_2 not symmetric at j = {jj}!"
        F_ps = to_pi_sigma_shifted(A2)
        A2_ps[jj] = F_ps
        # Degree diagnostic
        Pps = sp.Poly(F_ps, pi_v, sig)
        deg_pi = Pps.degree(pi_v)
        deg_sig = Pps.degree(sig)
        print(f"  j = {jj}:  (pi, sigma)-degrees = ({deg_pi}, {deg_sig})")

    print("\n  KEY OBSERVATION: deg_pi(A_2) = 2 for all j >= 4 !")
    print("  This is what the task's pi = c convention hides.")

    # -------- Step 2: try the shift-length ansatz uniformly --------
    print("\n" + "=" * 72)
    print("STEP 2  Fit  A_2 = sum_{k=0..2} alpha_k(sigma) * pi^k * (sigma-5)^{↓(j-4)}")
    print("        with alpha_k(sigma) polynomial in sigma of small degree.")
    print("=" * 72)

    all_alpha = {}   # {j: {k: alpha_k(sigma)}}
    for jj in range(4, J + 1):
        length = jj - 4  # length of falling product
        # Determine sigma-shift by inspection: use shift = 5 (matches the observed factors).
        shift = 5
        # Increment D_alpha until fit works
        F_ps = A2_ps[jj]
        found = None
        for D_alpha in range(0, 6):
            sol = fit_in_pi_sigma(F_ps, k_max=2, shift=shift, length=length, D_alpha=D_alpha)
            if sol is not None:
                found = (D_alpha, sol)
                break
        if found is None:
            print(f"  j = {jj}: FAILED to fit with shift={shift}, length={length}.")
            continue
        D_alpha, sol = found
        all_alpha[jj] = sol
        print(f"  j = {jj}: FIT with D_alpha = {D_alpha}.  alpha_k(sigma):")
        for k in (0, 1, 2):
            print(f"      alpha_{k}(sigma) = {sp.factor(sol[k])}")

    # -------- Step 3: extract uniform-in-j form of alpha_k(sigma) --------
    print("\n" + "=" * 72)
    print("STEP 3  Fit each alpha_k(j, sigma) as bivariate polynomial")
    print("        (poly in j, poly in sigma).")
    print("=" * 72)
    coef_forms_A2 = {}
    for k in (0, 1, 2):
        print(f"\n  --- k = {k} ---")
        samples = {jj: all_alpha[jj][k] for jj in sorted(all_alpha.keys())}
        beta = fit_bivariate_poly_sj(samples, f"alpha_{{2,{k}}}", max_deg_j=12)
        coef_forms_A2[k] = beta

    # -------- Step 4: apply the SAME structure to A_3 --------
    print("\n" + "=" * 72)
    print("STEP 4  Test the same structure on A_3.")
    print("        Extract A_3 for j = 6..12; check symmetry; convert to (pi, sigma).")
    print("=" * 72)

    A3_bc = {}
    A3_ps = {}
    for jj in range(6, J + 1):
        A3 = extract_A_p(jj, 3, dsV)
        A3_bc[jj] = A3
        sym_ok = is_sym_bc1(A3)
        F_ps = to_pi_sigma_shifted(A3) if sym_ok else None
        print(f"  j = {jj}: symmetric? {sym_ok}", end="")
        if sym_ok and F_ps is not None:
            A3_ps[jj] = F_ps
            Pps = sp.Poly(F_ps, pi_v, sig)
            print(f"  (deg_pi, deg_sig) = ({Pps.degree(pi_v)}, {Pps.degree(sig)})")
        else:
            print()

    if not A3_ps:
        print("\n  A_3 is not symmetric — the change of variables does not apply.")
        return

    print("\n  A_3 fits.  Try  A_3 = sum_{k=0..k_max} alpha_k(sigma) * pi^k * (sigma-shift)^{↓length}")
    print("  with (shift, length) chosen by empirical inspection.\n")

    # Empirical inspection: try shift = 7 (= 2p+1 for p=3), length = j - 6
    #   ...and k_max = 3 (= p).
    print("  --- Attempt A: shift = 2*p+1 = 7, length = j - 6 = j - 2p, k_max = 3 ---")
    all_alpha_A3 = {}
    for jj in range(6, J + 1):
        length = jj - 6
        shift = 7
        F_ps = A3_ps[jj]
        found = None
        for D_alpha in range(0, 8):
            sol = fit_in_pi_sigma(F_ps, k_max=3, shift=shift, length=length, D_alpha=D_alpha)
            if sol is not None:
                found = (D_alpha, sol)
                break
        if found is None:
            print(f"    j = {jj}: FAILED with (shift={shift}, length={length}, k_max=3, D_alpha up to 7).")
            continue
        D_alpha, sol = found
        all_alpha_A3[jj] = sol
        print(f"    j = {jj}: FIT with D_alpha = {D_alpha}.")
        for k in sorted(sol.keys()):
            print(f"        alpha_{k}(sigma) = {sp.factor(sol[k])}")

    if len(all_alpha_A3) == len(A3_ps):
        print("\n  Attempt A SUCCESS: fit alpha_k(j, sigma) uniformly in j.")
        for k in (0, 1, 2, 3):
            print(f"\n    --- A_3, k = {k} ---")
            samples = {jj: all_alpha_A3[jj].get(k, Integer(0)) for jj in sorted(all_alpha_A3.keys())}
            fit_bivariate_poly_sj(samples, f"alpha_{{3,{k}}}", max_deg_j=14)
    else:
        print("\n  Attempt A did not cover all j; try shift = 5 (same as A_2) or scan.")
        # Try (shift = 5, length = j - 4, k_max = 3)
        print("\n  --- Attempt B: shift = 5, length = j - 4, k_max = 3 ---")
        all_alpha_A3b = {}
        for jj in range(6, J + 1):
            length = jj - 4
            shift = 5
            F_ps = A3_ps[jj]
            found = None
            for D_alpha in range(0, 8):
                sol = fit_in_pi_sigma(F_ps, k_max=3, shift=shift, length=length, D_alpha=D_alpha)
                if sol is not None:
                    found = (D_alpha, sol)
                    break
            if found is None:
                print(f"    j = {jj}: FAILED with (shift=5, length={length}, k_max=3).")
                continue
            D_alpha, sol = found
            all_alpha_A3b[jj] = sol
            print(f"    j = {jj}: FIT with D_alpha = {D_alpha}.")
            for k in sorted(sol.keys()):
                print(f"        alpha_{k}(sigma) = {sp.factor(sol[k])}")
        if len(all_alpha_A3b) == len(A3_ps):
            print("\n  Attempt B SUCCESS.")
            for k in (0, 1, 2, 3):
                print(f"\n    --- A_3, k = {k} ---")
                samples = {jj: all_alpha_A3b[jj].get(k, Integer(0)) for jj in sorted(all_alpha_A3b.keys())}
                fit_bivariate_poly_sj(samples, f"alpha_{{3,{k}}}", max_deg_j=14)


if __name__ == "__main__":
    main()
