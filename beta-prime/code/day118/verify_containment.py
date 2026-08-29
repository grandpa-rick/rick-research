"""Day 118 — Containment check: closes the last gap in the proof of the
shifted-Pieri filtration claim.

Rick's proof of d_{s*_mu} = d_{s_mu} = mu_1 + floor((mu_2+mu_3)/2) modulo:

  s*_mu(x_1,x_2,x_3) = sum_lambda c^mu_lambda * s_lambda(x_1,x_2,x_3)

with every nonzero term having d_lambda <= d_mu.

HYPOTHESIS to verify: the ordinary-Schur expansion of s*_mu is supported ONLY
on lambda with lambda ⊆ mu (containment as partitions).  If that holds, then
by the closed d-formula d_lambda <= d_mu follows term-by-term automatically:

  lambda_1 <= mu_1 and lambda_2 + lambda_3 <= mu_2 + mu_3
  ⇒  d_lambda = lambda_1 + floor((lambda_2+lambda_3)/2)
             <= mu_1     + floor((mu_2 + mu_3)/2) = d_mu.

We use Rick's factorial_schur / ord_schur conventions from day117 to avoid any
convention drift.  For each mu with |mu| <= 8, ell(mu) <= 3, expand s*_mu into
ordinary Schurs and check both:
  (i)  containment lambda ⊆ mu for every lambda with c^mu_lambda != 0;
  (ii) d_lambda <= d_mu (Rick's real requirement).
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from ordinary_schur_deg import (
    ord_schur, factorial_schur, all_partitions_len_le_3,
)
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from factorial_in_ordinary import expand_in_ordinary_schur
from sympy import symbols, expand, Poly, Integer
import time

u, y, c = symbols('u y c')
xs = (u, y, c)


def pad3(mu):
    return tuple(list(mu) + [0] * (3 - len(mu)))


def contains(mu, lam):
    """lam ⊆ mu iff lam_i <= mu_i for all i (after padding to length 3)."""
    mp, lp = pad3(mu), pad3(lam)
    return all(lp[i] <= mp[i] for i in range(3))


def d_formula(mu):
    """Closed form d_mu = mu_1 + floor((mu_2+mu_3)/2) for ell(mu) <= 3."""
    m = pad3(mu)
    return m[0] + (m[1] + m[2]) // 2


def d_symbolic(mu):
    """(u,pi)-deg computed symbolically from ord_schur, for cross-check."""
    s = ord_schur(pad3(mu), xs)
    return joint_u_pi_deg(substitute_sigma_pi(s))


def analyze_mu(mu, max_size):
    """Expand s*_mu into ordinary Schurs; report containment / d-bound checks."""
    s_star = factorial_schur(pad3(mu), xs)
    coeffs = expand_in_ordinary_schur(s_star, xs, max_size=max_size)
    d_mu = d_formula(mu)
    containment_fail = []
    d_bound_fail = []
    rows = []
    for lam, cv in sorted(coeffs.items(), key=lambda kv: (sum(kv[0]), kv[0]), reverse=True):
        if cv == 0:
            continue
        d_lam = d_formula(lam)
        cont = contains(mu, lam)
        d_ok = d_lam <= d_mu
        rows.append((lam, cv, d_lam, cont, d_ok))
        if not cont:
            containment_fail.append((lam, cv, d_lam))
        if not d_ok:
            d_bound_fail.append((lam, cv, d_lam))
    return d_mu, rows, containment_fail, d_bound_fail


if __name__ == "__main__":
    MAX_SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    print(f"# Containment check for s*_mu = sum_lambda c^mu_lambda s_lambda")
    print(f"# Testing all mu with |mu| <= {MAX_SIZE}, ell(mu) <= 3")
    print()
    print(f"{'mu':>12} {'d_mu':>4} {'#terms':>7} {'containment':>12} {'d-bound':>8} {'time':>7}")
    print('-' * 70)
    all_containment_ok = True
    all_dbound_ok = True
    containment_failures = []  # list of (mu, lam, cv, d_lam)
    dbound_failures = []
    t_total = 0.0
    n_cases = 0
    all_rows = {}
    for N in range(MAX_SIZE + 1):
        for mu in all_partitions_len_le_3(N):
            if mu == (0, 0, 0):
                continue
            n_cases += 1
            t0 = time.time()
            d_mu, rows, cfails, dfails = analyze_mu(mu, max_size=N)
            dt = time.time() - t0
            t_total += dt
            all_rows[mu] = rows
            cflag = "OK" if not cfails else f"FAIL x{len(cfails)}"
            dflag = "OK" if not dfails else f"FAIL x{len(dfails)}"
            if cfails:
                all_containment_ok = False
                for lam, cv, d_lam in cfails:
                    containment_failures.append((mu, lam, cv, d_lam))
            if dfails:
                all_dbound_ok = False
                for lam, cv, d_lam in dfails:
                    dbound_failures.append((mu, lam, cv, d_lam))
            print(f"{str(mu):>12} {d_mu:>4} {len(rows):>7} {cflag:>12} {dflag:>8} {dt:>7.2f}")
    print()
    print(f"Total: {n_cases} cases, {t_total:.2f} s")
    print()
    print(f"Containment lambda ⊆ mu for ALL nonzero terms: {all_containment_ok}")
    print(f"d-bound  d_lambda <= d_mu   for ALL nonzero terms: {all_dbound_ok}")
    print()
    if containment_failures:
        print("=== CONTAINMENT FAILURES (lambda NOT ⊆ mu) ===")
        for mu, lam, cv, d_lam in containment_failures:
            d_mu = d_formula(mu)
            print(f"  mu = {mu}  (d_mu = {d_mu})")
            print(f"    lambda = {lam}  d_lam = {d_lam}   coeff = {cv}")
            print(f"    dominance check: sum(lam) = {sum(lam)} vs sum(mu) = {sum(mu)}")
    if dbound_failures:
        print("=== D-BOUND FAILURES (d_lambda > d_mu) ===")
        for mu, lam, cv, d_lam in dbound_failures:
            d_mu = d_formula(mu)
            print(f"  mu = {mu}  (d_mu = {d_mu})")
            print(f"    lambda = {lam}  d_lam = {d_lam}   coeff = {cv}")

    # Cross-check the closed-form d against symbolic d for a few mu
    print()
    print("Cross-check: d_formula vs d_symbolic (spot check)")
    for mu in [(2, 1, 0), (3, 2, 1), (4, 2, 2), (5, 3, 0)]:
        df = d_formula(mu)
        ds = d_symbolic(mu)
        print(f"  mu={mu}: formula={df}, symbolic={ds}, {'OK' if df == ds else 'MISMATCH'}")
