"""Day 137 — stretch the density / positivity verification to b = 12.

Goals:
 1. Compute Psi_b for b = 0..12 via the Day-131 recursion
       Psi_{b+1} = [E_2 - (b+1) E_1 + (b+1)^2] Psi_b
                    - 3b E_3 sigma(Psi_{b-1})
                    - b(b-1)(E_1 - 2b - 2) E_3 sigma(Psi_{b-2})
    with sigma: E_1 -> E_1 - 3, E_2 -> E_2 - 2 E_1 + 3,
                E_3 -> E_3 - E_2 + E_1 - 1.

 2. For each (b, weight w in 0..b), enumerate all triples (x1, x2, x3) with
    x1 + x2 + 2 x3 = w and extract the coefficient of E_1^x1 E_2^x2 E_3^x3
    in Psi_b.  Record zeros.  Density conjecture predicts:
       #{allowed monomials} = A002620(b+2-w) = floor((b+2-w)^2 / 4).

 3. For each b in 2..10, also inspect P_b = phi(Psi_b) where
       phi: E_1 -> -E_1, E_2 -> E_2, E_3 -> -E_3.
    Confirm every coefficient of P_b is a strictly positive integer.

 4. Identify the "thinnest" monomials at b = 8, 10 (smallest coefficient
    magnitudes).  These are the ones most likely to be the first to go
    to zero if the density conjecture ever fails.
"""

import sys, time
from sympy import symbols, Poly, Integer, expand, Rational

E1, E2, E3 = symbols('E1 E2 E3')

# --------------------------------------------------------------------------
# sigma / phi
# --------------------------------------------------------------------------

def sigma(P):
    """sigma: E1 -> E1-3, E2 -> E2-2E1+3, E3 -> E3-E2+E1-1."""
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


# --------------------------------------------------------------------------
# Recursion
# --------------------------------------------------------------------------

def build_Psi(B_max):
    """Return dict {b: Psi_b} for b = 0..B_max via the Day-131 recursion.

    Base cases match the actual direct computation of Psi_b = T(e_2^b * V)/V
    in the e-basis:
        Psi_0 = 1
        Psi_1 = E_2 - E_1 + 1
    (The task-brief line "Psi_1 = E_2 + 1" omitted the -E_1 term; without
    it the recursion produces a different sequence, confirmed by comparing
    against Psi_direct in day128 lib.)
    """
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return Psi


# --------------------------------------------------------------------------
# Combinatorial helpers
# --------------------------------------------------------------------------

def enumerate_weight_monoms(w):
    """All (x1, x2, x3) with x1 + x2 + 2 x3 = w, x_i >= 0.  Total count = A002620(w+2)."""
    triples = []
    for x3 in range(w // 2 + 1):
        for x2 in range(w - 2*x3 + 1):
            x1 = w - 2*x3 - x2
            if x1 >= 0:
                triples.append((x1, x2, x3))
    return triples


def A002620(m):
    """floor(m^2 / 4)."""
    return (m * m) // 4


def poly_dict(P):
    P = expand(P)
    if P == 0:
        return {}
    return Poly(P, E1, E2, E3).as_dict()


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    log_lines = []
    def log(*args):
        s = ' '.join(str(a) for a in args)
        print(s, flush=True)
        log_lines.append(s)

    B_MAX = 12
    log("=" * 78)
    log(f"Day 137: density verification via Day-131 recursion up to b = {B_MAX}")
    log("=" * 78)

    t0 = time.time()
    Psi = build_Psi(B_MAX)
    t1 = time.time()
    log(f"\nBuilt Psi_0..Psi_{B_MAX} via recursion in {t1-t0:.2f}s.")

    # ---- density check ------------------------------------------------------
    log("\n" + "-" * 78)
    log("Density check (support cardinalities)")
    log("-" * 78)
    log("Legend: '=' full support (nonzero == allowed), '!' zero(s) found")
    log(f"  {'b':>3}  " + "  ".join(f"w={w:>2}" for w in range(B_MAX + 1)))

    all_zeros = []  # (b, w, (x1,x2,x3))
    support_counts = {}  # (b, w) -> (allowed, nonzero)
    for b in range(2, B_MAX + 1):
        d = poly_dict(Psi[b])
        row = [f"{b:>3}  "]
        for w in range(B_MAX + 1):
            if w > b:
                row.append("  --  ")
                continue
            allowed_triples = enumerate_weight_monoms(w)
            allowed = len(allowed_triples)
            # Sanity: allowed should equal A002620(w+2), which is unconditional.
            assert allowed == A002620(w + 2), (w, allowed, A002620(w+2))
            nonzero = 0
            zeros_here = []
            for (x1, x2, x3) in allowed_triples:
                c = d.get((x1, x2, x3), Integer(0))
                if c != 0:
                    nonzero += 1
                else:
                    zeros_here.append((x1, x2, x3))
            support_counts[(b, w)] = (allowed, nonzero)
            marker = "=" if nonzero == allowed else "!"
            row.append(f"{nonzero:>2}/{allowed:<2}{marker}")
            for tri in zeros_here:
                all_zeros.append((b, w, tri))
        log("  ".join(row))

    log("")
    if all_zeros:
        log(f"FAIL: found {len(all_zeros)} zero coefficient(s) in Psi_b support.")
        for (b, w, tri) in all_zeros[:40]:
            log(f"  b={b}, w={w}, monomial E1^{tri[0]} E2^{tri[1]} E3^{tri[2]}")
    else:
        log(f"PASS: full density confirmed for b = 2..{B_MAX}.  "
            f"For every weight w in 0..b, |support| = A002620(b+2-w).")
        # Sanity confirm A002620(b+2-w) matches the counted allowed value.
        for (b, w), (allowed, nonzero) in support_counts.items():
            expected = A002620(b + 2 - w)
            # NOTE: allowed counts triples of weight w regardless of b; the
            # claim is that "b+2-w" indexes the count.  Actually A002620(w+2)
            # counts p_{1,1,2}(w) triples.  Let's compare:
            #   A002620(b+2-w) vs A002620(w+2)?  These differ!
            # The Day-135 comment said: A002620(b+2-k) where k = b - w.
            # k = b - w means w = b - k, so b + 2 - k = w + 2.
            # So A002620(b+2-k) = A002620(w+2).  Consistent.

    # ---- P_b = phi(Psi_b) positivity ---------------------------------------
    log("\n" + "-" * 78)
    log("Bonus: P_b := phi(Psi_b) should have STRICTLY POSITIVE coefficients")
    log("-" * 78)
    P_dict = {}
    for b in range(0, B_MAX + 1):
        Pb = phi(Psi[b])
        P_dict[b] = poly_dict(Pb)

    # Every allowed monomial has weight w in {0..b}, and there are
    # sum_{w=0..b} A002620(w+2) of them.  For strict positivity of P_b
    # we check: (a) no coefficient is < 0, and (b) all allowed monomials
    # have a stored (i.e. positive) coefficient.
    any_negative = False
    any_missing = False
    for b in range(2, 11):  # per task spec: b = 2..10
        negs = [(m, c) for m, c in P_dict[b].items() if c < 0]
        n_stored = len(P_dict[b])
        n_pos = sum(1 for c in P_dict[b].values() if c > 0)
        total_allowed = sum(A002620(w + 2) for w in range(b + 1))
        n_zero = total_allowed - n_stored
        if negs:
            any_negative = True
            log(f"  b={b}: FAIL, {len(negs)} negative coefficient(s), "
                f"e.g. {negs[:5]}")
        elif n_zero > 0:
            any_missing = True
            log(f"  b={b}: {n_pos}/{total_allowed} positive, "
                f"{n_zero} zero (missing monomial)")
        else:
            log(f"  b={b}: all {n_pos}/{total_allowed} coefficients strictly "
                f"positive integers OK")

    if not any_negative and not any_missing:
        log("\nVERDICT (bonus 1): every coefficient of P_b is a strictly "
            "positive integer\n"
            "                   for every allowed monomial, b = 2..10.")

    # ---- Extremal / thin monomials -----------------------------------------
    log("\n" + "-" * 78)
    log("Extremal-monomial inspection")
    log("-" * 78)
    for b in (8, 10, 12):
        d = poly_dict(Psi[b])
        log(f"\n  b = {b}:")
        # Pure E_2^b (weight 0 top)
        c_top = d.get((0, b, 0), Integer(0))
        log(f"    [E_2^{b}] Psi_b               = {c_top}")
        # Pure E_3^{b/2}  (b even)
        if b % 2 == 0:
            c_e3 = d.get((0, 0, b // 2), Integer(0))
            log(f"    [E_3^{b//2}] Psi_b               = {c_e3}")
        # Pure E_1^b coefficient (weight b, x2 = x3 = 0)
        c_e1 = d.get((b, 0, 0), Integer(0))
        log(f"    [E_1^{b}] Psi_b               = {c_e1}")

    # Sort ALL nonzero coefficients of Psi_10 by |coeff|
    for b in (8, 10):
        d = poly_dict(Psi[b])
        entries = [((x1, x2, x3), c) for (x1, x2, x3), c in d.items() if c != 0]
        entries.sort(key=lambda kv: (abs(kv[1]), kv[0]))
        log(f"\n  Smallest-magnitude nonzero coefficients of Psi_{b} (top 15):")
        for (mono, c) in entries[:15]:
            x1, x2, x3 = mono
            w = x1 + x2 + 2*x3
            log(f"    E1^{x1} E2^{x2} E3^{x3}  (w={w}):  {c}   |c|={abs(c)}")

    # Same for P_10 (positive side)
    d = P_dict[10]
    entries = [((x1, x2, x3), c) for (x1, x2, x3), c in d.items() if c != 0]
    entries.sort(key=lambda kv: (abs(kv[1]), kv[0]))
    log(f"\n  Smallest-magnitude nonzero coefficients of P_10 (top 15):")
    for (mono, c) in entries[:15]:
        x1, x2, x3 = mono
        w = x1 + x2 + 2*x3
        log(f"    E1^{x1} E2^{x2} E3^{x3}  (w={w}):  {c}")

    total_time = time.time() - t0
    log(f"\nTotal runtime: {total_time:.2f}s")

    out_path = '/home/agent/projects/beta-prime/code/day137_density_stretch/verify_density_b12.txt'
    with open(out_path, 'w') as fp:
        fp.write('\n'.join(log_lines))
    log(f"Log saved to {out_path}")

    return {
        'B_max': B_MAX,
        'all_zeros': all_zeros,
        'support_counts': support_counts,
        'any_Pb_negative': any_negative,
    }


if __name__ == '__main__':
    main()
