"""Day 112: DIRECT verification and investigation of Sub-sub-claim (***).

Claim (***): For each fixed r >= 0, the (a,b)-layer at total (a,b)-degree
2j - r of  S_j(a, b, c) := ds_j(a, b, c) / V(a, b, c),  when viewed as a
polynomial in j with coefficients in (a,b,c), has j-degree <= r.

More precisely: consider all partitions mu = (mu_1, mu_2, mu_3) in S_j with
mu_3 = r (or, more generally, with mu_3 >= r contributing to the layer at
(a,b)-degree 2j - r). Each contributes kappa_mu * s*_mu(y_1, y_2, y_3), and
the top (a,b)-part of s*_mu is a certain polynomial in c times a fixed
monomial in (a, b). We want: the SUM of these contributions has j-poly-degree
<= r.

We verify (***) by:
  1. Compute S_j = ds_j/V symbolically over Q[a,b,c] for j = 0, 1, ..., J.
     (For speed, we may fix c = integer.)
  2. For each r = 0, 1, ..., R_max, extract the (a,b)-layer at total degree
     2j - r. In S_j this is a polynomial in a, b of degree exactly 2j - r
     (each monomial a^i b^{2j-r-i}).
  3. For a chosen slot ("displacement" from top-corner), collect samples
     across j and fit as polynomial in j.

We ALSO enumerate {mu in S_j : mu_3 = r} for varied j, and count kappa_mu.
We check the conjecture "kappa_mu at mu = (mu_1, mu_2, r) is a polynomial
in j of degree <= r".

TARGET: verify up to R = 6 (R_max = 6).
"""
import sys
import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, binomial, factorial, Integer

a, b, c = symbols('a b c')
x1, x2, x3 = a + 2, b + 1, c

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def fall(x, m):
    if m < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def rise(x, L):
    if L < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


def bt(M):
    """Build S_j tables (partition, kappa) via vertical 2-strip growth up to j = M."""
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
    for j in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[j] = rs
    return T


def compute_dsV_at_c(J, cv):
    """Substitute c = cv (integer) EARLY, do division in Q[a,b]."""
    P(f"[bt] Building partition tables up to j = {J}...")
    t0 = time.time()
    tables = bt(J)
    P(f"[bt] done in {time.time() - t0:.2f}s")

    dsV_at_c = {}
    V_symb = ds_symbolic_c(0, tables)
    V_cv = expand(V_symb.subs(c, cv))
    xs_cv = (a + 2, b + 1, Integer(cv))
    for j in range(J + 1):
        t0 = time.time()
        total = Integer(0)
        for mu, kap in tables[j]:
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs_cv[i], ks[col]) for col in range(3)] for i in range(3)]
            total += kap * det3(rows)
        dsj_cv = expand(total)
        if dsj_cv == 0:
            dsV_at_c[j] = Integer(0)
        else:
            q, r = sp.div(Poly(dsj_cv, [a, b]), Poly(V_cv, [a, b]))
            assert r.as_expr() == 0, f"ds_{j}/V not divisible at c={cv}"
            dsV_at_c[j] = q.as_expr()
        pab = Poly(dsV_at_c[j], a, b) if dsV_at_c[j] != 0 else None
        tdeg_ab = max((sum(m) for m, cf in pab.terms() if cf != 0), default=0) if pab else 0
        P(f"  j={j}: (a,b)-deg = {tdeg_ab}  ({time.time()-t0:.2f}s)")
    return tables, dsV_at_c


def ds_symbolic_c(j, tables):
    """Compute ds_j symbolically in a, b, c (used only for V and small j)."""
    xs = (x1, x2, x3)
    total = Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def layer_coeffs(H, tot_deg):
    """Return dict {(i, k) : coef} for monomials a^i b^k with i + k = tot_deg."""
    if H == 0:
        return {}
    pab = Poly(H, a, b)
    out = {}
    for monom, coef in pab.terms():
        (da, db) = monom
        if da + db == tot_deg:
            out[(da, db)] = coef
    return out


def j_degree_of_samples(samples):
    """Given list of (j_val, y_val), fit polynomial in j and return its degree.

    Uses exact rational fit. Returns -1 if all samples zero. Otherwise returns
    the smallest D such that a polynomial of degree D matches all samples.
    """
    if all(s[1] == 0 for s in samples):
        return -1
    n = len(samples)
    for D in range(n):
        rows = []
        yy = []
        for (jv, yv) in samples[:D + 1]:
            rows.append([jv ** i for i in range(D + 1)])
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
            if D == 0 or sp.simplify(sol[D]) != 0:
                return D
    return None


# =============================================================================
# (***) DIRECT verification: for each fixed r, does the layer at (a,b)-deg
# 2j - r of ds_j/V have j-poly-degree <= r?
# =============================================================================
def verify_ss_star(R_max, cv, tables, dsV_at_c, slack=2):
    """For each r in [0, R_max], test the conjecture: layer at (a,b)-deg
    2j - r of ds_j/V has j-poly-degree <= r, at each slot (alpha, 2j - r - alpha).

    Report the j-degree of each slot (parameterized by alpha = 0, 1, ...).

    Slot correspondence: instead of (i, k) = (alpha, k), which varies with j,
    we parameterize the slot in the shell by "displacement of a from origin"
    alpha = 0, 1, ..., 2j - r. To compare across j we use the FIXED alpha.
    """
    P("\n" + "=" * 72)
    P(f"(***) DIRECT verify: R_max = {R_max}, c = {cv}")
    P("=" * 72)

    # Enough j samples to fit poly in j of degree ~ R_max + slack.
    # For r shell to exist we need 2j >= r, i.e., j >= ceil(r/2).
    for r in range(R_max + 1):
        # Sample j from max(1, ceil(r/2) + 1) to J_max
        min_j = max((r + 1) // 2, 1)
        J_max = min(min_j + R_max + slack + 2, max(dsV_at_c.keys()))
        j_range = list(range(min_j, J_max + 1))
        if len(j_range) < r + 3:
            P(f"  r = {r}: too few j samples ({len(j_range)}), skip.")
            continue

        # For each alpha in [0, ..., 2j_min - r], collect (j, coef of a^alpha b^{2j - r - alpha}).
        min_span = min(2 * jv - r for jv in j_range)
        max_alpha = min(min_span, r + 2)  # slot displacement up to r+2
        P(f"\n  r = {r}: j in [{j_range[0]}, {j_range[-1]}], test alpha in [0, {max_alpha}]")
        alpha_degs = []
        max_jd = -1
        for alpha in range(max_alpha + 1):
            samples = []
            for jv in j_range:
                k_needed = 2 * jv - r - alpha
                if k_needed < 0:
                    continue
                slots = layer_coeffs(dsV_at_c[jv], 2 * jv - r)
                cf = slots.get((alpha, k_needed), Integer(0))
                samples.append((jv, cf))
            if len(samples) < 2:
                continue
            jd = j_degree_of_samples(samples)
            alpha_degs.append((alpha, jd))
            if jd is not None and jd > max_jd:
                max_jd = jd
        status = "OK" if max_jd <= r else "!!VIOLATION!!"
        P(f"    max j-deg across slots = {max_jd} (expect <= r = {r}) [{status}]")
        for (alpha, jd) in alpha_degs:
            P(f"      alpha = {alpha} (slot a^{alpha} b^{{2j-{r}-{alpha}}}): j-deg = {jd}")


# =============================================================================
# Kappa enumeration: {mu in S_j : mu_3 = r} and their kappa_mu.
# =============================================================================
def enumerate_kappa_by_mu3(J_max, tables):
    """For each r in [0, ...], j in [1, ..., J_max], print the partitions
    mu in S_j with mu_3 = r, together with kappa_mu.

    Fits kappa_mu = kappa_{(mu_1, mu_2, r)} as polynomial in j (for varied j
    with a fixed slot shape, if any).
    """
    P("\n" + "=" * 72)
    P("Enumerate {mu in S_j : mu_3 = r}, kappa_mu, and j-fit")
    P("=" * 72)

    # Group across j: for each r, for each "shape descriptor" (mu_1 - mu_2, mu_2 - r):
    # actually let's parameterize by (mu_2 - r, mu_1 - mu_2).
    # mu_1 + mu_2 + r = 2j so mu_1 = 2j - r - mu_2, and mu_2 >= r >= 0, mu_1 >= mu_2.
    #
    # For each r >= 0 and each fixed "d2 = mu_2 - (?)"... let me try:
    # As j -> infty (fixed r), mu_2 can range over [r, j - r/2] roughly.
    # For a "shape descriptor", we can use s = mu_1 - mu_2 (asymmetry) or
    # equivalently, mu_2 = (2j - r - s) / 2 (assuming s and 2j - r have matching parity).

    # SIMPLER: enumerate at each j, print all (mu_1, mu_2, r) with mu_3 = r,
    # along with kappa, then note kappa as function of j when we fix (r, mu_2 - r-related).

    # Also test the conjecture kappa_{(mu_1, mu_2, r)} is polynomial in j
    # of degree <= r for each fixed shape.
    #
    # Shape parameterization: let s := mu_2 - r (drop of mu_2 from mu_3).
    # Then mu_1 = 2j - r - mu_2 = 2j - 2r - s. So as j varies (fixed r, s), mu_1 grows linearly.

    print_r_range = 4  # print detail up to r = 4
    max_shape_s = 4
    for r in range(print_r_range + 1):
        P(f"\n--- r = {r} ---")
        # Table: shape s = mu_2 - r --> list of (j, kappa_{(mu_1=2j-2r-s, mu_2=r+s, r)})
        shape_data = defaultdict(list)  # s -> [(j, kappa)]
        for j in range(1, J_max + 1):
            for mu, kap in tables[j]:
                if mu[2] == r:
                    s = mu[1] - r
                    shape_data[s].append((j, kap))
        for s in sorted(shape_data.keys())[:max_shape_s + 1]:
            samples = shape_data[s]
            # Fit as polynomial in j
            jd = j_degree_of_samples(samples)
            row = ', '.join(f"(j={j}, k={k})" for (j, k) in samples[:8])
            extra = f", ...+{len(samples)-8}" if len(samples) > 8 else ""
            P(f"  s = mu_2 - r = {s} (mu_1 = 2j - {2*r + s}, mu_2 = {r + s}, mu_3 = {r}):")
            P(f"     kappa data: [{row}{extra}]")
            P(f"     j-degree fit: {jd}   (conjecture: <= r = {r})")


# =============================================================================
# Contribution per (mu_3 = r): compute sum over {mu : mu_3 = r} of
# kappa_mu * det[y^{mu+3-l}] as a polynomial in a, b, c.
# For each j, extract layer at (a,b)-deg = 2j - r; compare across j.
# =============================================================================
def verify_ss_star_per_r_layer(R_max, cv, tables, J_max, slack=2):
    """For each r, compute the sub-sum
        SubS_r(j) := sum over mu in S_j with mu_3 = r of  kappa_mu * det[y^{mu+3-l}] / V
      (equivalently the sum of kappa_mu * s*_mu over such mu).
    Extract the TOP (a,b)-layer of SubS_r(j), which lives at (a,b)-deg 2j - r
    (by rank-drop / determinant top-part analysis).
    Fit each slot's coefficient (as a function of j) — j-degree should be <= r.
    """
    P("\n" + "=" * 72)
    P(f"(***) PER-r layer verification: sub-sums by mu_3 = r  (R_max = {R_max}, c = {cv})")
    P("=" * 72)

    # Precompute V at cv
    V_symb = ds_symbolic_c(0, tables)
    V_cv = expand(V_symb.subs(c, cv))

    xs_cv = (a + 2, b + 1, Integer(cv))

    # For each j: for each r, gather mu with mu[2] = r and sum contributions.
    subS_at_j = defaultdict(dict)  # subS_at_j[j][r] = polynomial in a, b (after dividing by V)
    for j in range(1, J_max + 1):
        t0 = time.time()
        # Compute contributions grouped by mu_3.
        contrib_by_r = defaultdict(lambda: Integer(0))
        for mu, kap in tables[j]:
            r = mu[2]
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs_cv[i], ks[col]) for col in range(3)] for i in range(3)]
            contrib_by_r[r] += kap * det3(rows)
        for r, contr in contrib_by_r.items():
            contr_e = expand(contr)
            if contr_e == 0:
                subS_at_j[j][r] = Integer(0)
                continue
            # Divide by V_cv.
            # NOTE: individual sub-sums may not be divisible by V! We need the FULL sum to
            # be divisible. If a sub-sum isn't divisible, we work in Q(a,b,c) or track
            # numerator.
            try:
                q, rr = sp.div(Poly(contr_e, [a, b]), Poly(V_cv, [a, b]))
                if rr.as_expr() == 0:
                    subS_at_j[j][r] = q.as_expr()
                else:
                    # store as fraction: numerator / V
                    subS_at_j[j][r] = ('frac', contr_e)
            except Exception as e:
                subS_at_j[j][r] = ('err', str(e))
        P(f"  j={j}: r-groups computed in {time.time()-t0:.2f}s. r-values seen: {sorted(contrib_by_r.keys())}")

    # For each r, verify (***) using the sub-sums.
    for r in range(R_max + 1):
        # J values with r-group present:
        j_vals = [j for j in range(1, J_max + 1) if r in subS_at_j[j]]
        if len(j_vals) < r + 3:
            P(f"\n  r = {r}: too few j samples ({len(j_vals)}), skip.")
            continue
        # For each such j, get the top-(a,b)-layer of SubS_r(j).
        # Expected (a,b)-deg = 2j - r? Or could differ if the sub-sum has additional cancellations.
        # We probe by checking the actual (a,b)-top-deg.
        P(f"\n  r = {r}: j-samples = {j_vals}")
        top_deg_data = []
        for jv in j_vals:
            val = subS_at_j[jv][r]
            if isinstance(val, tuple):
                P(f"    j={jv}: sub-sum not divisible individually by V. Skipping this r for direct verification.")
                top_deg_data = None
                break
            if val == 0:
                top_deg_data.append((jv, -1, {}))
                continue
            pab = Poly(val, a, b)
            top_td = max((sum(m) for m, cf in pab.terms() if cf != 0), default=-1)
            layer = layer_coeffs(val, top_td)
            top_deg_data.append((jv, top_td, layer))
        if top_deg_data is None:
            continue
        # Show top-deg per j
        for (jv, td, _) in top_deg_data:
            P(f"    j={jv}: (a,b)-top-deg of sub-sum = {td}  (expected 2j - r = {2*jv - r})")
        # For each slot alpha in [0, r+2], compare across j.
        min_top = min(td for (_, td, _) in top_deg_data if td >= 0)
        max_alpha = min(min_top, r + 2)
        for alpha in range(max_alpha + 1):
            samples = []
            for (jv, td, layer) in top_deg_data:
                if td < 0:
                    continue
                # slot for alpha: (alpha, td - alpha)  (assuming td = 2j - r)
                # NOTE: td might not be 2j - r exactly (extra cancellations possible).
                # For consistency we take the TOP layer.
                k_needed = td - alpha
                if k_needed < 0:
                    continue
                cf = layer.get((alpha, k_needed), Integer(0))
                samples.append((jv, cf))
            if len(samples) < 3:
                continue
            jd = j_degree_of_samples(samples)
            status = "OK" if (jd is not None and jd <= r) else ("empty" if jd == -1 else "!!")
            P(f"      alpha = {alpha}: sub-sum layer j-deg = {jd}  (expect <= r = {r}) [{status}]")


# =============================================================================
# MAIN
# =============================================================================
def main():
    P("=" * 72)
    P("Day 112: DIRECT verification of Sub-sub-claim (***) up to R = 6")
    P("=" * 72)

    # Target R = 6, so we need j samples up to ~ 2R + slack + a few. To be safe use J = 20.
    # We use c = 25 (large enough that everything is polynomial, no impulse).
    C_VAL = 25
    J_MAX = 20

    tables, dsV_at_c = compute_dsV_at_c(J_MAX, C_VAL)

    # 1. Direct verification (***): layer of ds_j/V at (a,b)-total 2j-r
    verify_ss_star(6, C_VAL, tables, dsV_at_c, slack=3)

    # 2. Enumerate kappa by mu_3
    enumerate_kappa_by_mu3(J_MAX, tables)

    # 3. Verify per-r sub-sum layers directly
    verify_ss_star_per_r_layer(6, C_VAL, tables, J_MAX, slack=2)

    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(OUT))
    P(f"\nSaved log to {out_path}")


if __name__ == "__main__":
    main()
