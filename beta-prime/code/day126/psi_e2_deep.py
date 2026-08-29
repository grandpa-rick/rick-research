"""
Deep analysis of Psi(e_2^b) for the operator Psi = (1/V) * T * V,
where T is the falling-factorial monomial operator.

Weight: w(e1^a1 e2^a2 e3^a3) = a1 + a2 + 2*a3.

Goals:
  1. Verify w(Psi(e2^b)) <= b for b as high as feasible.
  2. Print full expansions for b = 1..5.
  3. Extract top-weight part (weight = b terms) and look for closed form.
  4. Check whether the weight bound holds TERM-BY-TERM before symmetrization
     (i.e. is cancellation essential?)
  5. Compare Psi(e_2^b) vs Psi(e_2)^b at top weight.
"""

import sys
from sympy import symbols, expand, Poly, Integer, Rational, prod, sympify, factor, simplify, together, groebner
from sympy.polys.orderings import lex, grevlex

u1, u2, u3 = symbols('u1 u2 u3')
E1, E2, E3 = symbols('E1 E2 E3')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)
e1_expr = u1 + u2 + u3
e2_expr = u1*u2 + u1*u3 + u2*u3
e3_expr = u1*u2*u3


def falling(x, k):
    if k == 0:
        return Integer(1)
    return prod([x - i for i in range(k)])


def T_of_monomial(a, b, c):
    return falling(u1, a) * falling(u2, b) * falling(u3, c)


def T(poly):
    poly = expand(poly)
    if poly == 0:
        return Integer(0)
    p = Poly(poly, u1, u2, u3)
    result = Integer(0)
    for monom, coeff in p.as_dict().items():
        a, b, c = monom
        result += coeff * T_of_monomial(a, b, c)
    return expand(result)


def Psi(f):
    """f is symmetric in u1,u2,u3; returns a symmetric polynomial."""
    numer = expand(T(expand(f * V)))
    # exact polynomial division by V
    q, r = Poly(numer, u1, u2, u3).div(Poly(V, u1, u2, u3))
    assert r.as_expr() == 0, f"Division by V failed! remainder = {r.as_expr()}"
    return q.as_expr()


# ---- Symmetric -> e-basis conversion via Groebner reduction ----
# We augment the ring with E1,E2,E3 and reduce a symmetric polynomial modulo
# {E1 - e1, E2 - e2, E3 - e3} using lex order eliminating u1,u2,u3.

def sym_to_ebasis(f):
    """Rewrite symmetric polynomial in u1,u2,u3 into polynomial in E1,E2,E3."""
    f = expand(f)
    if f == 0:
        return Integer(0)
    # Build Groebner basis to eliminate u1,u2,u3
    gens_ord = [u1, u2, u3, E1, E2, E3]
    ideal = [E1 - e1_expr, E2 - e2_expr, E3 - e3_expr]
    G = groebner(ideal, gens_ord, order='lex')
    reduced = G.reduce(f)[1]
    reduced = expand(reduced)
    # sanity: should be free of u_i
    if any(reduced.has(v) for v in (u1, u2, u3)):
        raise ValueError(f"reduction failed: {reduced}")
    return reduced


# Cheaper method: for symmetric polynomials, use direct algorithm.
# We do standard "highest monomial in lex" reduction.
def sym_to_ebasis_direct(f):
    """Direct algorithm: repeatedly subtract e-basis monomial matching leading term."""
    f = expand(f)
    result = Integer(0)
    while f != 0:
        p = Poly(f, u1, u2, u3)
        # Find leading monomial in lex order with u1 > u2 > u3
        monoms = sorted(p.as_dict().keys(), reverse=True)
        lead = monoms[0]
        coeff = p.as_dict()[lead]
        a, b, c = lead
        # Requires a >= b >= c since f is symmetric.
        if not (a >= b >= c):
            raise ValueError(f"Not symmetric or algorithm error: leading = {lead}")
        # e-basis monomial: e1^(a-b) * e2^(b-c) * e3^c
        i, j, k = a - b, b - c, c
        # As a symbolic thing in u:
        e_term_u = e1_expr**i * e2_expr**j * e3_expr**k
        # subtract
        f = expand(f - coeff * e_term_u)
        result += coeff * E1**i * E2**j * E3**k
    return result


def weight_of_e_monom(i, j, k):
    return i + j + 2*k


def max_weight(expr_in_E):
    """Given polynomial in E1,E2,E3, compute max (1,1,2)-weight."""
    expr_in_E = expand(expr_in_E)
    if expr_in_E == 0:
        return -1
    p = Poly(expr_in_E, E1, E2, E3)
    w = -1
    for monom, coeff in p.as_dict().items():
        if coeff == 0:
            continue
        i, j, k = monom
        w = max(w, weight_of_e_monom(i, j, k))
    return w


def top_weight_part(expr_in_E, target_w):
    """Extract monomials of exactly weight target_w."""
    expr_in_E = expand(expr_in_E)
    if expr_in_E == 0:
        return Integer(0)
    p = Poly(expr_in_E, E1, E2, E3)
    result = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if weight_of_e_monom(i, j, k) == target_w:
            result += coeff * E1**i * E2**j * E3**k
    return result


def all_e_monomials_with_weights(expr_in_E):
    expr_in_E = expand(expr_in_E)
    if expr_in_E == 0:
        return []
    p = Poly(expr_in_E, E1, E2, E3)
    out = []
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        out.append((weight_of_e_monom(i, j, k), (i, j, k), coeff))
    out.sort()
    return out


# ---- Termwise cancellation check ----
# In Psi(e_2^b), before dividing by V, the numerator T(e2^b * V) is a sum of
# T-terms coming from monomials of e2^b * V. We want to check: does any
# individual monomial contribution ALREADY have weight <= b when we naively
# convert it, or does each term individually violate the weight bound?
#
# But before symmetrization, "weight" doesn't quite apply. The natural check:
# take the numerator T(e2^b * V) as a sum of individual T_of_monomial(a,b,c)
# terms, each is a polynomial in u1,u2,u3. Divide each such term by V (which
# generally is NOT exact for individual terms). So termwise doesn't make sense
# as division-by-V.
#
# Better formulation: The sum T(e2^b * V) = sum_m c_m * T_of_monomial(m).
# When we finally divide by V, cancellations occur. The question: if we
# extract the leading monomial in each T_of_monomial(m) (which is u1^a u2^b u3^c
# itself, since T = product of falling factorials with leading term u^a),
# then look at what these leading terms contribute to Psi(e_2^b) if we naively
# treated them (i.e. the leading part of T is identity), we get e_2^b whose
# top weight is 2b - obviously above b for b >= 1.
#
# Alternate reasonable interpretation: group by monomials m of f*V, and see
# what "polynomial in E" each term would give if it were symmetric. But single
# terms are not symmetric.
#
# Reasonable check: for each monomial u1^a u2^b u3^c in expand(e2^b * V) with
# coefficient c_m, the T-image T_of_monomial(a,b,c) has leading term u1^a u2^b u3^c
# plus lower-order terms. The "naive image" (without T) would give back e2^b, of
# weight 2b. If T added lower order terms that cancel, the RESULT is weight <= b.
#
# I'll do this: symmetrize each SYMMETRY ORBIT of monomials in e2^b * V,
# apply T to that orbit-sum (still symmetric), divide by V (may not be exact),
# convert to e-basis (via the direct method) and see its weight. If ANY such
# orbit-sum-contribution has weight > b, then cancellation across orbits is
# essential.

def orbit_of_monomial(a, b, c):
    """S_3 orbit of (a,b,c) as multiset of tuples."""
    from itertools import permutations
    return set(permutations((a, b, c)))


def analyze_termwise(b_val):
    """For Psi(e_2^b), check termwise weights (orbit by orbit in f*V)."""
    f = e2_expr**b_val
    fv = expand(f * V)
    p = Poly(fv, u1, u2, u3)
    monoms = p.as_dict()
    seen_orbits = set()
    per_orbit_contribs = []
    for (a, bb, c), coeff in monoms.items():
        orbit_key = tuple(sorted((a, bb, c), reverse=True))
        if orbit_key in seen_orbits:
            continue
        seen_orbits.add(orbit_key)
        # Sum the coefficients over the orbit (each permutation)
        orbit_sum = Integer(0)
        for (aa, bbb, ccc) in orbit_of_monomial(a, bb, c):
            c_perm = monoms.get((aa, bbb, ccc), 0)
            orbit_sum += c_perm * T_of_monomial(aa, bbb, ccc)
        orbit_sum = expand(orbit_sum)
        # This sum IS symmetric only if the orbit has consistent coefficients.
        # Actually f*V is anti-symmetric... wait: f is symmetric, V is anti-symmetric,
        # so f*V is anti-symmetric. Then T(f*V) is... not necessarily anti-symmetric,
        # but Psi(f) = T(f*V)/V is symmetric.
        # So the "orbit sum" of anti-symmetric-coefficient monomials is NOT symmetric.
        # Instead, group by orbits and see what each contributes.
        per_orbit_contribs.append((orbit_key, orbit_sum))
    return per_orbit_contribs


def analyze_termwise_v2(b_val):
    """
    Alternative: examine each individual T-monomial contribution to numerator.
    Numerator N = T(e2^b * V) = sum over monomials m of e2^b*V of c_m * T[m].
    Each T[m] = falling(u1,a)*falling(u2,b')*falling(u3,c).
    Expand T[m] into monomials, then divide by V symbolically.
    Since V is anti-symmetric, dividing each T[m] by V is generally not exact.
    But we can anti-symmetrize each T[m] first (which makes it divisible by V
    up to a factor), and then divide.

    More concretely: N is not itself anti-symmetric (checking!)...
    Actually N = T(f*V). Under a transposition (u1<->u2), we have (f*V) -> -f*V,
    but T is defined monomial-wise and does NOT commute with permutations in
    general (falling factorials are symmetric per variable but T[m] treats
    variables identically per position). So T(sigma . g) != sigma . T(g).
    But by inspection: T is defined by
      T(u1^a u2^b u3^c) = [u1]_a [u2]_b [u3]_c
    and this DOES commute with permutations of u1,u2,u3 (T is equivariant).
    So T(sigma . g) = sigma . T(g). Therefore T(f*V) is anti-symmetric (since
    f*V is anti-symmetric). Hence T(f*V) is divisible by V, and Psi(f) is
    symmetric. Good.

    Termwise check: group monomials of f*V by S_3 orbit. Each orbit's sum
    (with signed coefficients) is anti-symmetric on its own IF the orbit has
    the right sign pattern. For f*V with f symmetric and V anti-symmetric,
    the coefficients of monomials in one orbit are related by sign(sigma).
    So YES, each orbit-summed contribution is anti-symmetric and hence
    divisible by V.

    So: for each S_3 orbit O of monomials in f*V, define
        N_O = sum_{sigma in S_3} c_{sigma.m0} * T[sigma.m0]
             = sum over orbit
    where sign convention is baked into c_{sigma.m0}. Then N_O / V is a
    well-defined symmetric polynomial. Convert to e-basis, compute weight.
    """
    f = e2_expr**b_val
    fv = expand(f * V)
    p = Poly(fv, u1, u2, u3)
    monoms = p.as_dict()
    seen_orbits = set()
    orbit_contribs = []
    for (a, bb, c), coeff in monoms.items():
        orbit_key = tuple(sorted((a, bb, c), reverse=True))
        if orbit_key in seen_orbits:
            continue
        seen_orbits.add(orbit_key)
        # Build orbit sum
        orbit_sum = Integer(0)
        for (aa, bbb, ccc) in orbit_of_monomial(*orbit_key):
            c_perm = monoms.get((aa, bbb, ccc), 0)
            if c_perm != 0:
                orbit_sum += c_perm * T_of_monomial(aa, bbb, ccc)
        orbit_sum = expand(orbit_sum)
        if orbit_sum == 0:
            continue
        # divide by V
        try:
            q, r = Poly(orbit_sum, u1, u2, u3).div(Poly(V, u1, u2, u3))
            if r.as_expr() != 0:
                # Not divisible by V - orbit isn't self-antisymmetric
                orbit_contribs.append((orbit_key, "NOT DIVISIBLE", None))
                continue
            q_expr = q.as_expr()
            # convert to e-basis
            q_e = sym_to_ebasis_direct(q_expr)
            w = max_weight(q_e)
            orbit_contribs.append((orbit_key, q_e, w))
        except Exception as e:
            orbit_contribs.append((orbit_key, f"ERROR: {e}", None))
    return orbit_contribs


def main():
    log_lines = []
    def log(*args):
        s = ' '.join(str(a) for a in args)
        print(s)
        log_lines.append(s)

    log("=" * 70)
    log("Psi(e_2^b) deep analysis")
    log("=" * 70)

    # Precompute Psi(e_2^b) in e-basis for b = 1..MAX
    MAX_B = 12  # try 12, can push to 15 if fast
    results_e = {}
    weights = {}

    for b in range(1, MAX_B + 1):
        import time
        t0 = time.time()
        f = e2_expr**b
        psi_u = Psi(f)
        t1 = time.time()
        psi_e = sym_to_ebasis_direct(psi_u)
        t2 = time.time()
        w = max_weight(psi_e)
        weights[b] = w
        results_e[b] = psi_e
        log(f"\n--- b = {b} ---")
        log(f"  Psi time = {t1-t0:.2f}s, symtoE time = {t2-t1:.2f}s")
        log(f"  max weight = {w}  (bound: b = {b}) {'OK' if w <= b else 'VIOLATION!'}")
        if b <= 5:
            log(f"  Psi(e_2^{b}) in E-basis:")
            log(f"    {psi_e}")
        # top-weight part
        tw = top_weight_part(psi_e, b)
        log(f"  top-weight (w = {b}) part: {tw}")

    log("\n" + "=" * 70)
    log("Summary of top-weight parts (weight = b) for b = 1..{}".format(MAX_B))
    log("=" * 70)
    top_parts = {}
    for b in range(1, MAX_B + 1):
        tw = top_weight_part(results_e[b], b)
        top_parts[b] = tw
        log(f"  b={b}: {tw}")

    # Also check: is top-weight part == Psi(e_2)^b top-weight part?
    log("\n" + "=" * 70)
    log("Psi(e_2)^b top-weight comparison (Q5)")
    log("=" * 70)
    psi_e2 = results_e[1]  # already computed
    log(f"  Psi(e_2) = {psi_e2}")
    tw_of_psi_e2 = top_weight_part(psi_e2, 1)
    log(f"  top-weight of Psi(e_2) (w=1) = {tw_of_psi_e2}")
    for b in range(1, min(MAX_B, 8) + 1):
        pe2_b = expand(psi_e2**b)
        # convert this to E-basis (already in E) - actually psi_e2 is in E already
        pe2_b_top = top_weight_part(pe2_b, b)  # weight bound of psi_e2^b: b * w(psi_e2)
        log(f"  b={b}: Psi(e_2)^b top-weight (w={b}) = {pe2_b_top}")
        log(f"        Psi(e_2^b) top-weight       (w={b}) = {top_parts[b]}")
        diff = expand(pe2_b_top - top_parts[b])
        log(f"        difference = {diff}")

    # Termwise cancellation analysis (Q4)
    log("\n" + "=" * 70)
    log("Termwise cancellation check (Q4) for b = 1..6")
    log("=" * 70)
    for b in range(1, min(MAX_B, 6) + 1):
        log(f"\n  -- b = {b} --")
        contribs = analyze_termwise_v2(b)
        max_orbit_w = -1
        n_over = 0
        for orbit_key, q_e, w in contribs:
            if isinstance(q_e, str):
                log(f"    orbit {orbit_key}: {q_e}")
                continue
            over = w > b
            if over:
                n_over += 1
            max_orbit_w = max(max_orbit_w, w)
            marker = "  *ABOVE BOUND*" if over else ""
            log(f"    orbit {orbit_key}: weight={w}{marker}")
            log(f"       -> {q_e}")
        log(f"    max per-orbit weight = {max_orbit_w} vs. bound b = {b}")
        log(f"    #orbits violating bound = {n_over} / {len(contribs)}")
        log(f"    (Cancellation essential? {'YES' if max_orbit_w > b else 'NO'})")

    # Write results
    with open('/home/agent/projects/beta-prime/code/day126/psi_e2_deep_results.txt', 'w') as f:
        f.write('\n'.join(log_lines))
    log("\nWrote results to psi_e2_deep_results.txt")


if __name__ == '__main__':
    main()
