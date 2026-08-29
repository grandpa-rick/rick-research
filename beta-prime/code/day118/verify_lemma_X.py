"""Day 118 — Verify Lemma X:

    span_Q { s*_mu : d_mu <= k } = F^k   as subspaces of Lambda_3,

where F^k := { f in Q[e_1, e_2, e_3] : deg_t f(u=t, y+c=s, yc=t) <= k },
and d_mu = mu_1 + floor((mu_2 + mu_3)/2).

The ⊆ direction is trivial.  We test the ⊇ direction two ways:

  (A) Naive reformulation: bar s*_mu := coeff of t^{d_mu} in the
      substitution (a polynomial in Q[s]).  Are {bar s*_mu : d_mu = k}
      Q-linearly INDEPENDENT?  If yes, Lemma X ⊇ follows by induction.

  (B) True span equality:
      dim span_Q{s*_mu : d_mu <= k}  vs  dim F^k.
      Since {s*_mu} is a basis of Lambda_3, dim span = #{mu : d_mu <= k}.
      dim F^k = #{(i1,i2,i3) : i1 + i2 + 2 i3 <= k}.
      If the counts don't match, span is a PROPER subspace of F^k.

Both are performed for k <= 10.

Reuses Rick's shifted-Schur from code/day117/.
"""

import sys
import os

# Make Rick's day117 code importable.
DAY117 = os.path.join(os.path.dirname(__file__), '..', 'day117')
sys.path.insert(0, os.path.abspath(DAY117))

from sympy import symbols, expand, Integer, Poly, zeros

from ordinary_schur_deg import factorial_schur
from route_v_probe import substitute_sigma_pi

u, y, c = symbols('u y c')
sig, pi_v = symbols('sigma pi')  # substitute_sigma_pi uses these
t, s = symbols('t s')


def d_mu(mu):
    a, b, cc = mu
    return a + (b + cc) // 2


_star_cache = {}


def factorial_schur_substituted(mu):
    """Compute s*_mu(u=t, y+c=s, yc=t) as a polynomial in Q[t, s].  Cached."""
    if mu in _star_cache:
        return _star_cache[mu]
    xs = (u, y, c)
    f_uyc = factorial_schur(mu, xs)
    f_usp = substitute_sigma_pi(f_uyc)
    f_ts = f_usp.subs({u: t, sig: s, pi_v: t})
    result = expand(f_ts)
    _star_cache[mu] = result
    return result


def top_t_part(f_ts, k):
    return expand(Poly(f_ts, t).nth(k))


def all_partitions_len_le_3_with_d(K):
    """All partitions mu with ell(mu) <= 3 and d_mu = K."""
    result = []
    for a in range(0, K + 1):
        r = K - a
        if r < 0:
            continue
        for total_bc in (2 * r, 2 * r + 1):
            for b in range(0, a + 1):
                cc = total_bc - b
                if cc < 0 or cc > b:
                    continue
                if a >= b >= cc >= 0:
                    result.append((a, b, cc))
    return sorted(set(result))


def all_partitions_len_le_3_with_d_le(K):
    r = []
    for k in range(K + 1):
        r.extend(all_partitions_len_le_3_with_d(k))
    return r


def dim_F_k(k):
    if k < 0:
        return 0
    count = 0
    for i3 in range(0, k // 2 + 1):
        for i2 in range(0, k - 2 * i3 + 1):
            for i1 in range(0, k - i2 - 2 * i3 + 1):
                count += 1
    return count


def rank_of_polynomials_in_s(polys):
    coeff_dicts = []
    for g in polys:
        if g == 0:
            coeff_dicts.append({})
            continue
        p = Poly(g, s)
        cd = {}
        for (deg,), coeff in p.terms():
            cd[deg] = coeff
        coeff_dicts.append(cd)
    max_deg = 0
    for cd in coeff_dicts:
        if cd:
            max_deg = max(max_deg, max(cd.keys()))
    if not any(coeff_dicts):
        return 0
    M = zeros(len(polys), max_deg + 1)
    for i, cd in enumerate(coeff_dicts):
        for deg, coeff in cd.items():
            M[i, deg] = coeff
    return M.rank()


def main(KMAX=10):
    print("=" * 78)
    print(f"Day 118 — Verify Lemma X for k <= {KMAX}")
    print("=" * 78)
    print()
    print("Setup:")
    print("  Substitution (u, y, c) -> roots of (z-t)(z^2 - sz + t):")
    print("  e_1 -> t+s,  e_2 -> (s+1)t,  e_3 -> t^2.")
    print("  F^k = {f in Q[e1,e2,e3] : deg_t f(...) <= k}.")
    print("  d_mu = mu_1 + floor((mu_2+mu_3)/2).")
    print()

    # -----------------------------------------------------------------
    # (A) Naive independence.
    # -----------------------------------------------------------------
    print("=" * 78)
    print("(A) Naive independence of top-t-parts bar s*_mu in gr_k^F")
    print("=" * 78)
    print(f"{'k':>3} {'#mu(d=k)':>10} {'rank':>6} {'dim_gr_amb':>10} {'status':>10}")
    print("-" * 70)

    per_k_A = {}
    for K in range(KMAX + 1):
        mus = all_partitions_len_le_3_with_d(K)
        if not mus:
            per_k_A[K] = {'mus': [], 'polys': [], 'rank': 0}
            continue
        polys = [top_t_part(factorial_schur_substituted(mu), K) for mu in mus]
        r = rank_of_polynomials_in_s(polys)
        dim_gr = dim_F_k(K) - dim_F_k(K - 1)
        status = "INDEP" if r == len(mus) else f"DEP ({len(mus)-r})"
        print(f"{K:>3} {len(mus):>10} {r:>6} {dim_gr:>10} {status:>10}")
        per_k_A[K] = {'mus': mus, 'polys': polys, 'rank': r, 'dim_gr': dim_gr}
        sys.stdout.flush()

    print()

    # -----------------------------------------------------------------
    # (B) Dimension count for span version of Lemma X.
    # -----------------------------------------------------------------
    print("=" * 78)
    print("(B) Dimension counts:  #{mu : d_mu <= k}   vs.   dim F^k")
    print("=" * 78)
    print("    (span{s*_mu : d_mu <= k} = F^k requires equality by")
    print("     linear independence of {s*_mu} as a basis of Lambda_3.)")
    print(f"{'k':>3} {'#mu(d<=k)':>12} {'dim F^k':>10} {'gap':>6} {'span_eq_F':>12}")
    print("-" * 70)

    per_k_B = {}
    all_span_ok = True
    for K in range(KMAX + 1):
        mus = all_partitions_len_le_3_with_d_le(K)
        n = len(mus)
        d = dim_F_k(K)
        gap = d - n
        ok = (gap == 0)
        if not ok:
            all_span_ok = False
        per_k_B[K] = {'n_mus': n, 'dim_F_k': d, 'gap': gap, 'ok': ok}
        print(f"{K:>3} {n:>12} {d:>10} {gap:>6} {'PASS' if ok else 'FAIL':>12}")
    print()
    if all_span_ok:
        print("  Dimension counts match — span_eq_F^k is POSSIBLE.")
    else:
        print("  Dimension counts DIFFER — span_eq_F^k FAILS by dimension.")

    # -----------------------------------------------------------------
    # Report bar s*_mu polynomials (bonus: closed form)
    # -----------------------------------------------------------------
    print()
    print("=" * 78)
    print("Bonus: bar s*_mu as polynomials in Q[s]")
    print("=" * 78)
    for K in range(KMAX + 1):
        data = per_k_A[K]
        if not data['mus']:
            continue
        print(f"\nk = {K}:")
        for mu, g in zip(data['mus'], data['polys']):
            deg_s = Poly(g, s).total_degree() if g != 0 else -1
            print(f"    mu = {str(mu):>15}   deg_s = {deg_s}   bar s*_mu(s) = {g}")

    # -----------------------------------------------------------------
    # Failure analysis (naive rank deficiency).
    # -----------------------------------------------------------------
    print()
    print("=" * 78)
    print("Failure analysis: left null space of top-t-part matrix")
    print("=" * 78)
    for K in range(KMAX + 1):
        data = per_k_A[K]
        if not data['mus'] or data['rank'] == len(data['mus']):
            continue
        polys = data['polys']
        coeff_dicts = []
        for g in polys:
            if g == 0:
                coeff_dicts.append({})
                continue
            p = Poly(g, s)
            cd = {}
            for (deg,), coeff in p.terms():
                cd[deg] = coeff
            coeff_dicts.append(cd)
        max_deg = 0
        for cd in coeff_dicts:
            if cd:
                max_deg = max(max_deg, max(cd.keys()))
        M = zeros(len(polys), max_deg + 1)
        for i, cd in enumerate(coeff_dicts):
            for deg, coeff in cd.items():
                M[i, deg] = coeff
        nullspace = M.T.nullspace()
        print(f"\nk = {K}  (rank {data['rank']} vs count {len(data['mus'])}; "
              f"{len(nullspace)} independent relations):")
        for v in nullspace:
            parts = []
            for i, mu in enumerate(data['mus']):
                coef = v[i, 0]
                if coef != 0:
                    parts.append(f"({coef})*bar s*_{mu}")
            print("    " + " + ".join(parts) + "  =  0")

    print()
    print("=" * 78)
    naive_pass = all(per_k_A[K]['rank'] == len(per_k_A[K]['mus'])
                     for K in range(KMAX + 1) if per_k_A[K]['mus'])
    print(f"FINAL: (A) naive independence     = "
          f"{'HOLDS for k <= ' + str(KMAX) if naive_pass else 'FAILS'}")
    print(f"       (B) dim{{s*_mu:d_mu<=k}} = dim F^k = "
          f"{'HOLDS for k <= ' + str(KMAX) if all_span_ok else 'FAILS'}")
    print(f"       => Lemma X (span version) = "
          f"{'PROVED for k <= ' + str(KMAX) if all_span_ok else 'DISPROVED (dim mismatch)'}")
    print("=" * 78)

    return naive_pass, all_span_ok, per_k_A, per_k_B


if __name__ == "__main__":
    naive, span, A, B = main(KMAX=10)
    sys.exit(0 if span else 1)
