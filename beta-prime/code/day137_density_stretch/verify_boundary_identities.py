"""Day 137 boundary-identity verification for the P_b density stretch.

Verifies:
 1. P_b via phi(Psi_b) agrees with P_b via P-recursion, b = 0..10.
 2. Q_b via definition agrees with Q_b via Q-recursion, b = 2..10.
 3. Critical density boundary identity:
        [E_3^{(b+1)/2}] P_{b+1} = b * [E_3^{(b-1)/2}] Q_b   for odd b in {1,3,5,7,9}.
 4. Pure-E_3 boundary chain for Q_b (odd b in {1,3,5,7,9}):
        - [E_3^{(b-1)/2}] Q_b > 0,
        - Recursion:    [E_3^{(b-1)/2}] Q_b = 3(b-2) * [E_3^{(b-3)/2}] tau(Q_{b-2})  (b >= 5)
        - Nonneg lift:  [E_3^{(b-3)/2}] tau(Q_{b-2}) >= [E_3^{(b-3)/2}] Q_{b-2}.
 5. tau-nondegeneracy spot check: tau(f) - f has nonneg coefficients
    for f in {P_2, Q_3, E_1^2 E_2 + 3 E_3 + 5}.
 6. Mechanical full-density check: for every admissible monomial mu of weight
    w = 0..b+1 in P_{b+1}, at least one of the four positive contributions
    (from the P-recursion applied to P_b and Q_b) is strictly positive.
"""

import sys, time
from sympy import symbols, Poly, Integer, expand

E1, E2, E3 = symbols('E1 E2 E3')


# --------------------------------------------------------------------------
# Ring maps: sigma, phi, tau = phi sigma phi
# --------------------------------------------------------------------------

def sigma(P):
    """sigma: E1 -> E1-3, E2 -> E2-2 E1+3, E3 -> E3-E2+E1-1."""
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
        simultaneous=True))


def phi(P):
    """phi: E1 -> -E1, E2 -> E2, E3 -> -E3."""
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, -E1), (E3, -E3)], simultaneous=True))


def tau(P):
    """tau = phi sigma phi: E1 -> E1+3, E2 -> 2 E1+E2+3, E3 -> E1+E2+E3+1."""
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 + 3), (E2, 2*E1 + E2 + 3), (E3, E1 + E2 + E3 + 1)],
        simultaneous=True))


# --------------------------------------------------------------------------
# Psi recursion (from verify_density_b12.py)
# --------------------------------------------------------------------------

def build_Psi(B_max):
    """Return dict {b: Psi_b} for b = 0..B_max via the Day-131 recursion."""
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b + 1)*E1 + (b + 1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b - 1])
        term3 = b*(b - 1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b - 2]) if b >= 2 \
            else Integer(0)
        Psi[b + 1] = expand(term1 - term2 - term3)
    return Psi


# --------------------------------------------------------------------------
# P-recursion, Q-definition, Q-recursion
# --------------------------------------------------------------------------

def build_P_via_Prec(B_max, P0=None, P1=None):
    """Build P_b via the P-recursion up to b = B_max.

    P_{b+1} = [E_2 + (b+1) E_1 + (b+1)^2] P_b + b * E_3 * Q_b
      where Q_b := 3 tau(P_{b-1}) - (b-1)(E_1+2b+2) tau(P_{b-2}).
    Base: P_0 = 1, P_1 = E_1 + E_2 + 1 (matches phi of Psi_1 = E_2 - E_1 + 1
    with the sign flip E_1 -> -E_1).
    """
    if P0 is None: P0 = Integer(1)
    if P1 is None: P1 = E1 + E2 + 1
    P = {0: P0, 1: P1}
    Q = {}
    # Compute Q_b for b >= 1 via the definition, then use in P-rec.
    # Definition: Q_b = 3 tau(P_{b-1}) - (b-1)(E_1+2b+2) tau(P_{b-2}).
    # For b = 1: uses P_0, P_{-1}; the coefficient (b-1) = 0 kills the P_{-1} term.
    # We loop b = 1..B_max so that Q is defined at b = B_max as well.
    # P_{b+1} is only computed when b + 1 <= B_max.
    for b in range(1, B_max + 1):
        Pbm1 = P[b - 1]
        if b >= 2:
            Pbm2 = P[b - 2]
            Q_b = expand(3 * tau(Pbm1) - (b - 1) * (E1 + 2*b + 2) * tau(Pbm2))
        else:
            # b = 1: (b-1) = 0, no Pbm2 term.
            Q_b = expand(3 * tau(Pbm1))
        Q[b] = Q_b
        if b + 1 <= B_max and b >= 1:
            # Advance P via P-recursion.  P[b] already known (or set as base).
            if (b + 1) not in P:
                P[b + 1] = expand(
                    (E2 + (b + 1)*E1 + (b + 1)**2) * P[b] + b * E3 * Q_b)
    return P, Q


def build_Q_via_Qrec(P, B_max):
    """Compute Q_b via the Q-recursion:
        Q_b = [(2b+4) E_1 + 3 E_2 + (b^2+3b+5)] tau(P_{b-2})
              + 3(b-2)(E_1+E_2+E_3+1) tau(Q_{b-2})
    for b >= 2.  Base: Q_1 = 3, Q_2 = 8 E_1 + 3 E_2 + 15.
    Requires P (dict) already computed.
    """
    Q = {1: Integer(3), 2: 8*E1 + 3*E2 + 15}
    for b in range(3, B_max + 1):
        term_a = ((2*b + 4)*E1 + 3*E2 + (b*b + 3*b + 5)) * tau(P[b - 2])
        term_b = 3*(b - 2)*(E1 + E2 + E3 + 1) * tau(Q[b - 2])
        Q[b] = expand(term_a + term_b)
    return Q


# --------------------------------------------------------------------------
# Utilities
# --------------------------------------------------------------------------

def poly_dict(P):
    P = expand(P)
    if P == 0:
        return {}
    return {tuple(k): v for k, v in Poly(P, E1, E2, E3).as_dict().items()}


def coef_pure_E3(P, k):
    """Coefficient of E_1^0 E_2^0 E_3^k in P.  (After setting E_1 = E_2 = 0.)"""
    return poly_dict(P).get((0, 0, k), Integer(0))


def enumerate_weight_monoms(w):
    """All (x1, x2, x3) with x1 + x2 + 2 x3 = w."""
    triples = []
    for x3 in range(w // 2 + 1):
        for x2 in range(w - 2*x3 + 1):
            x1 = w - 2*x3 - x2
            if x1 >= 0:
                triples.append((x1, x2, x3))
    return triples


def all_admissible_monoms(b):
    """All admissible mu for P_b: weight w in 0..b, all triples of weight w."""
    triples = []
    for w in range(b + 1):
        triples.extend(enumerate_weight_monoms(w))
    return triples


def poly_is_nonneg(P):
    """Return (bool, list_of_neg_terms) — does P have all nonneg coefficients?"""
    d = poly_dict(P)
    negs = [(m, c) for m, c in d.items() if c < 0]
    return (len(negs) == 0), negs


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    log_lines = []
    def log(*args):
        s = ' '.join(str(a) for a in args)
        print(s, flush=True)
        log_lines.append(s)

    B_MAX = 10
    log("=" * 78)
    log(f"Day 137 boundary identities — verifying up to b = {B_MAX}")
    log("=" * 78)

    t0 = time.time()

    # ------------------------------------------------------------------
    # 1. Build Psi and P via phi(Psi).
    # ------------------------------------------------------------------
    Psi = build_Psi(B_MAX)
    P_from_phi = {b: expand(phi(Psi[b])) for b in range(B_MAX + 1)}
    t1 = time.time()
    log(f"\nBuilt Psi_0..Psi_{B_MAX} and P_b = phi(Psi_b) in {t1-t0:.2f}s.")

    # ------------------------------------------------------------------
    # 2. Build P via P-recursion, cross-check.
    # ------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Check (2): P_b via P-recursion  vs  P_b = phi(Psi_b)")
    log("-" * 78)
    P_from_rec, Q_from_def = build_P_via_Prec(B_MAX)

    p_mismatches = []
    for b in range(0, B_MAX + 1):
        diff = expand(P_from_rec[b] - P_from_phi[b])
        if diff != 0:
            p_mismatches.append((b, diff))
            log(f"  b={b}: MISMATCH, diff = {diff}")
        else:
            log(f"  b={b}: OK  (deg(P_b) match, coefficient dicts equal)")
    if not p_mismatches:
        log("Cross-check (2): OK for all b = 0..10.")
    else:
        log(f"Cross-check (2): FAIL — mismatches at b = {[m[0] for m in p_mismatches]}")

    # ------------------------------------------------------------------
    # 3. Cross-check Q_b definition vs Q_b recursion.
    # ------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Check (3): Q_b via definition  vs  Q_b via Q-recursion")
    log("-" * 78)

    Q_from_rec = build_Q_via_Qrec(P_from_rec, B_MAX)

    # Q_from_def has b = 1..B_MAX (b=1 uses only 3 tau(P_0)).
    q_mismatches = []
    for b in range(1, B_MAX + 1):
        d = expand(Q_from_def[b] - Q_from_rec[b])
        if d != 0:
            q_mismatches.append((b, d))
            log(f"  b={b}: MISMATCH, diff = {d}")
        else:
            log(f"  b={b}: OK")
    if not q_mismatches:
        log("Cross-check (3): OK for all b = 1..10.")
    else:
        log(f"Cross-check (3): FAIL — mismatches at b = {[m[0] for m in q_mismatches]}")

    Q = Q_from_def  # use the definition-based Q from here on

    # ------------------------------------------------------------------
    # 4. Critical density boundary identity for odd b.
    # ------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Check (4): [E_3^{(b+1)/2}] P_{b+1} = b * [E_3^{(b-1)/2}] Q_b")
    log("-" * 78)
    log(f"  {'b':>3}  {'k_P=(b+1)/2':>12}  {'k_Q=(b-1)/2':>12}  "
        f"{'LHS':>12}  {'RHS':>12}  {'match':>6}")
    id4_ok = True
    for b in (1, 3, 5, 7, 9):
        k_P = (b + 1) // 2
        k_Q = (b - 1) // 2
        LHS = coef_pure_E3(P_from_rec[b + 1], k_P)
        RHS = b * coef_pure_E3(Q[b], k_Q)
        match = (LHS == RHS)
        if not match:
            id4_ok = False
        log(f"  {b:>3}  {k_P:>12}  {k_Q:>12}  {str(LHS):>12}  {str(RHS):>12}  "
            f"{'OK' if match else 'FAIL':>6}")
    log(f"Check (4): {'OK' if id4_ok else 'FAIL'}")

    # ------------------------------------------------------------------
    # 5. Q pure-E_3 boundary chain.
    # ------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Check (5): pure-E_3 boundary chain in Q")
    log("-" * 78)

    log("  (5a) [E_3^{(b-1)/2}] Q_b > 0  for odd b in {1,3,5,7,9}:")
    log(f"    {'b':>3}  {'k=(b-1)/2':>10}  {'coef':>12}")
    pos_ok = True
    coefs_Q_pureE3 = {}
    for b in (1, 3, 5, 7, 9):
        k = (b - 1) // 2
        c = coef_pure_E3(Q[b], k)
        coefs_Q_pureE3[b] = c
        if c <= 0:
            pos_ok = False
        log(f"    {b:>3}  {k:>10}  {str(c):>12}")
    log(f"  (5a) {'OK' if pos_ok else 'FAIL'} — all values strictly positive.")

    log("\n  (5b) recursion: [E_3^{(b-1)/2}] Q_b = 3(b-2) * [E_3^{(b-3)/2}] tau(Q_{b-2})")
    log("       for b >= 5 (i.e. b in {5, 7, 9}).")
    log(f"    {'b':>3}  {'LHS':>12}  {'RHS = 3(b-2) * [E3^{(b-3)/2}] tau(Q_{b-2})':>50}  {'match':>6}")
    rec_ok = True
    for b in (5, 7, 9):
        k = (b - 1) // 2
        kprev = (b - 3) // 2
        LHS = coef_pure_E3(Q[b], k)
        tau_Qbm2 = tau(Q[b - 2])
        RHS = 3 * (b - 2) * coef_pure_E3(tau_Qbm2, kprev)
        match = (LHS == RHS)
        if not match:
            rec_ok = False
        log(f"    {b:>3}  {str(LHS):>12}  {str(RHS):>50}  "
            f"{'OK' if match else 'FAIL':>6}")
    log(f"  (5b) {'OK' if rec_ok else 'FAIL'}")

    log("\n  (5c) nonneg tau-lift: [E_3^{(b-3)/2}] tau(Q_{b-2}) >= [E_3^{(b-3)/2}] Q_{b-2}")
    log("       for b in {5, 7, 9}.")
    log(f"    {'b':>3}  {'[E3^k] tau(Q_{b-2})':>20}  {'[E3^k] Q_{b-2}':>16}  {'ok':>4}")
    lift_ok = True
    for b in (5, 7, 9):
        kprev = (b - 3) // 2
        L = coef_pure_E3(tau(Q[b - 2]), kprev)
        R = coef_pure_E3(Q[b - 2], kprev)
        ok = (L >= R)
        if not ok:
            lift_ok = False
        log(f"    {b:>3}  {str(L):>20}  {str(R):>16}  "
            f"{'OK' if ok else 'FAIL':>4}")
    log(f"  (5c) {'OK' if lift_ok else 'FAIL'}")

    check5_ok = pos_ok and rec_ok and lift_ok
    log(f"Check (5): {'OK' if check5_ok else 'FAIL'}")

    # ------------------------------------------------------------------
    # 6. tau-nondegeneracy spot check.
    # ------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Check (6): tau(f) - f has nonneg coefficients (spot check)")
    log("-" * 78)
    test_polys = [
        ('P_2', P_from_rec[2]),
        ('Q_3', Q[3]),
        ('E1^2 E2 + 3 E3 + 5', E1**2 * E2 + 3*E3 + 5),
    ]
    tau_ok = True
    for name, f in test_polys:
        diff = expand(tau(f) - f)
        ok, negs = poly_is_nonneg(diff)
        if not ok:
            tau_ok = False
            log(f"  f = {name}: FAIL — negative term(s): {negs[:5]}")
        else:
            # Report the diff polynomial briefly.
            log(f"  f = {name}: OK  (tau(f) - f has all coefficients >= 0)")
            log(f"       tau(f) - f = {diff}")
    log(f"Check (6): {'OK' if tau_ok else 'FAIL'}")

    # ------------------------------------------------------------------
    # 7. Full P density check via P-rec induction.
    #    For each b in 0..B_MAX-1 and each mu admissible for P_{b+1},
    #    check that at least one positive contribution is > 0.
    # ------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Check (7): mechanical P-rec density induction, b = 0..9")
    log("           (verifying every admissible mu in P_{b+1} has a")
    log("            strictly-positive contribution from the P-recursion)")
    log("-" * 78)

    # Cache dicts.
    P_dicts = {b: poly_dict(P_from_rec[b]) for b in range(B_MAX + 1)}
    Q_dicts = {b: poly_dict(Q[b]) for b in range(1, B_MAX + 1)}

    counterexamples = []
    total_checked = 0
    for b in range(0, B_MAX):
        # We check P_{b+1}, so admissible monomials of weight 0..b+1.
        admiss = all_admissible_monoms(b + 1)
        for mu in admiss:
            x1, x2, x3 = mu
            w = x1 + x2 + 2*x3
            contribs = {}  # label -> value

            # (a) (b+1)^2 * [mu] P_b       — only if w <= b
            if w <= b:
                c_a = P_dicts[b].get(mu, Integer(0))
                contribs['a'] = (b + 1)**2 * c_a
            # (b) 1 * [(x1, x2-1, x3)] P_b — only if x2 >= 1
            if x2 >= 1:
                c_b = P_dicts[b].get((x1, x2 - 1, x3), Integer(0))
                contribs['b'] = 1 * c_b
            # (c) (b+1) * [(x1-1, x2, x3)] P_b — only if x1 >= 1
            if x1 >= 1:
                c_c = P_dicts[b].get((x1 - 1, x2, x3), Integer(0))
                contribs['c'] = (b + 1) * c_c
            # (d) b * [(x1, x2, x3-1)] Q_b — only if x3 >= 1 and b >= 1
            if x3 >= 1 and b >= 1:
                c_d = Q_dicts[b].get((x1, x2, x3 - 1), Integer(0))
                contribs['d'] = b * c_d

            total_checked += 1
            any_pos = any(v > 0 for v in contribs.values())
            if not any_pos:
                counterexamples.append((b, mu, contribs))

    log(f"  Total admissible mu checked (b = 0..9, mu in P_{{b+1}}): {total_checked}")
    if counterexamples:
        log(f"  COUNTEREXAMPLE(S) found ({len(counterexamples)}):")
        for (b, mu, contribs) in counterexamples[:20]:
            log(f"    b={b}, mu={mu}, contribs={contribs}")
    else:
        log("  No counterexamples — every admissible mu has at least one")
        log("  strictly positive contribution in the P-recursion.")
    check7_ok = (len(counterexamples) == 0)
    log(f"Check (7): {'OK' if check7_ok else 'FAIL'}")

    # ------------------------------------------------------------------
    # Summary.
    # ------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("SUMMARY")
    log("=" * 78)
    log(f"  Check (2) — P_b cross-check:              "
        f"{'OK' if not p_mismatches else 'FAIL'}")
    log(f"  Check (3) — Q_b cross-check:              "
        f"{'OK' if not q_mismatches else 'FAIL'}")
    log(f"  Check (4) — density boundary identity:    "
        f"{'OK' if id4_ok else 'FAIL'}")
    log(f"  Check (5) — Q pure-E3 boundary chain:     "
        f"{'OK' if check5_ok else 'FAIL'}")
    log(f"  Check (6) — tau nondegeneracy spot check: "
        f"{'OK' if tau_ok else 'FAIL'}")
    log(f"  Check (7) — mechanical density induction: "
        f"{'OK' if check7_ok else 'FAIL'}")

    total_time = time.time() - t0
    log(f"\nTotal runtime: {total_time:.2f}s")

    out_path = ('/home/agent/projects/beta-prime/code/day137_density_stretch/'
                'verify_boundary_identities.txt')
    with open(out_path, 'w') as fp:
        fp.write('\n'.join(log_lines))
    log(f"Log saved to {out_path}")


if __name__ == '__main__':
    main()
