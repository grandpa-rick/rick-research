"""Day 90/91 CODE — Compute Δ_k^{(c)} catalog for the SCP-uniform PROVE.

Definition (from state/PROVE.md, Day 90 wake insight):
    h_k^{(c)}(a, b) = (a+3)_{L} · (b+2)_{L} · Q_k(a, b, c),   L = c-1-k.
    LB_k^{(c)} = min_{shell} v_2(h_k^{(c)}(a, b))
              = 2 v_2(L!) + Δ_k^{(c)}                      [clean regime k ≤ c-1]

where Δ_k^{(c)} := min v_2(Q_k(a, b, c)) over (a, b) ∈ SHELL ∩ POCHMIN_LOCUS.

- SHELL: a + b ≡ c (mod 2).
- POCHMIN_LOCUS: {(a, b) : (a+2) & L == 0 AND (b+1) & L == 0}
  (Kummer: (a+3)_L / L! = C(a+2+L, L) is odd iff (a+2) & L = 0 by Lucas.)

Range: c ∈ {5, 6, 7, 8, 9, 10, 11}, k ∈ {0, 1, ..., c-1}.

For k ≤ 6, we use the catalogued Q_k (symbolic in a, b, c).
For k ≥ 7, we extract h_k(a, b) as a bivariate polynomial per c, divide
symbolically by the Pochhammer factor, and evaluate.

Output:
  - JSON catalog: code/2026-07-12-Delta-k-c-catalog.json
  - Log: code/2026-07-12-Delta-k-c-catalog-output.txt
"""
import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, Poly, sympify, Rational, expand, Integer

# Load pipeline for k>=7 extraction.
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)

# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def v2_int(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def lucas_odd(x, L):
    """Return True iff C(x + L, L) is odd; equivalently x & L == 0."""
    return (int(x) & int(L)) == 0


def load_Q_catalog():
    """Load Q_k(a, b, c) as sympy polynomials from JSON catalog."""
    d = json.load(open('/home/agent/projects/code/2026-07-11-Qk-catalog.json'))
    a, b, c = symbols('a b c')
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


def poly_at_c(Q_kabc, c_val):
    """Substitute c = c_val into Q_k(a, b, c) to get poly in (a, b) only."""
    a, b, c = symbols('a b c')
    return expand(Q_kabc.subs(c, c_val))


def rising_fact(x, n):
    """Falling? No, RISING: (x)_n = x(x+1)...(x+n-1). n <= 0 -> 1."""
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def extract_hk_bivariate(c_val, k_target, sample_range=(None, None), max_deg=None):
    """Extract h_{k_target}^{(c=c_val)}(a, b) as a bivariate polynomial via
    fitting on pipeline samples with a >= b >= c.

    Returns sympy poly in (a, b), or None if fit fails.
    """
    tables = hkfit.build_e2_tables(max_j=k_target + 2)
    # Sample: a in [c, c+width), b in [c, a+1]
    if sample_range == (None, None):
        # heuristic: width w gives w(w+1)/2 samples; need >= binom(D+2, 2)
        # for total deg D. h_k has degree (c-1-k)+(c-1-k) = 2L in (a,b),
        # plus polynomial-in-a,b factor of degree 2k (from Q_k). So total
        # deg ~ 2(c-1). Take width = 2c + max(0, 20-2c) → ~2c+2.
        w = max(2 * c_val + 5, 25)
    else:
        w = sample_range[1] - sample_range[0]
    samples = []
    a_s, b_s = symbols('a b')
    for a in range(c_val, c_val + w):
        for b in range(c_val, a + 1):
            hks = hkfit.extract_h_k(a, b, c_val, k_target, tables)
            if hks is None:
                continue
            samples.append((a, b, hks[k_target]))
    if not samples:
        return None
    # Fit as bivariate poly in (a, b).
    if max_deg is None:
        max_deg = 2 * (c_val - 1)  # generous upper bound
    from sympy import Matrix, Rational
    for D in range(max_deg + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            continue
        rows = []
        yvals = []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != N:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        ok = True
        for cc in sol:
            if not isinstance(cc, Rational) or cc.q != 1:
                ok = False
                break
        if not ok:
            continue
        poly = 0
        for (da, db), cc in zip(monomials, sol):
            poly += int(cc) * a_s ** da * b_s ** db
        poly = expand(poly)
        # verify
        bad = False
        for (av, bv, yv) in samples:
            if poly.subs({a_s: av, b_s: bv}) != yv:
                bad = True
                break
        if bad:
            continue
        return poly
    return None


def Q_k_at_c_from_hk(c_val, k_target):
    """Extract Q_k(a, b) at fixed c via direct h_k extraction and symbolic
    division by Pochhammer factor. Slower but works for k > 6 too.
    """
    hk_ab = extract_hk_bivariate(c_val, k_target)
    if hk_ab is None:
        return None
    a_s, b_s = symbols('a b')
    L = c_val - 1 - k_target
    if L < 0:
        # Boundary regime — skip for now (Γ-ratio needed).
        return None
    poch_a = rising_fact(a_s + 3, L)
    poch_b = rising_fact(b_s + 2, L)
    denom = expand(poch_a * poch_b)
    # Q = hk / denom as a polynomial (should divide cleanly if conjecture holds)
    from sympy import div, cancel
    q, r = div(hk_ab, denom, domain='QQ')
    if r != 0:
        # Try cancel
        candidate = cancel(hk_ab / denom)
        # Verify by multiplication
        if expand(candidate * denom) == hk_ab:
            return expand(candidate)
        return None
    return expand(q)


# --------------------------------------------------------------------------- #
# Δ_k^{(c)} computation
# --------------------------------------------------------------------------- #

def compute_delta(Q_ab, c_val, k, search_T=10, verbose=False):
    """Compute Δ_k^{(c)} = min v_2(Q(a, b)) over (a, b) in shell ∩ Poch-min.

    search_T: search (a, b) in [0, 2^search_T).
    Returns (Δ, list of (a, b, v_2) at min).
    """
    L = c_val - 1 - k
    if L < 0:
        return None, []
    parity = c_val % 2  # a+b ≡ c (mod 2)
    a_s, b_s = symbols('a b')
    # Lambdify for fast integer evaluation
    from sympy import lambdify
    f = lambdify((a_s, b_s), Q_ab, modules='math')
    # Build Poch-min set for a: {a >= 0 : (a+2) & L == 0}
    # For L given, valid (a+2) are integers with bits disjoint from L.
    # Enumerate up to 2^search_T.
    N = 1 << search_T
    valid_a2 = [x for x in range(N) if (x & L) == 0]  # a+2 values
    valid_a = [x - 2 for x in valid_a2 if x - 2 >= 0]
    valid_b1 = [x for x in range(N) if (x & L) == 0]  # b+1 values
    valid_b = [x - 1 for x in valid_b1 if x - 1 >= 0]
    if verbose:
        print(f"    L={L}, |valid_a|={len(valid_a)}, |valid_b|={len(valid_b)}")

    min_v = float('inf')
    achievers = []
    for a in valid_a:
        for b in valid_b:
            if (a + b) % 2 != parity:
                continue
            try:
                val = int(f(a, b))
            except Exception:
                continue
            v = v2_int(val)
            if v < min_v:
                min_v = v
                achievers = [(a, b, v)]
            elif v == min_v and len(achievers) < 5:
                achievers.append((a, b, v))
            if min_v == 0:
                break  # can't beat 0
        if min_v == 0:
            break
    return min_v, achievers


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main():
    print("=" * 74)
    print("Day 90/91 CODE — Δ_k^{(c)} catalog for SCP-uniform PROVE")
    print("=" * 74)

    Q_catalog = load_Q_catalog()
    print(f"\nLoaded Q_k(a,b,c) from catalog for k ∈ {sorted(Q_catalog.keys())}")

    catalog = {}  # (c, k) -> {'Delta': ..., 'achievers': [...], 'L': ..., '2v2Lfact': ...}
    c_range = list(range(5, 12))  # 5..11
    for c_val in c_range:
        print("\n" + "=" * 74)
        print(f"c = {c_val}, shell parity a+b ≡ {c_val % 2}")
        print("=" * 74)
        for k in range(c_val):  # k = 0..c-1 (clean regime)
            L = c_val - 1 - k
            v2Lfact = v2_int(factorial(L)) if L > 0 else 0
            t0 = time.time()
            # Get Q_k(a, b) at c = c_val
            if k in Q_catalog:
                Q_ab = poly_at_c(Q_catalog[k], c_val)
            else:
                print(f"  k={k}: extracting Q_k via pipeline (k not in catalog)")
                Q_ab = Q_k_at_c_from_hk(c_val, k)
                if Q_ab is None:
                    print(f"    EXTRACTION FAILED, skip.")
                    catalog[(c_val, k)] = {
                        'Delta': None,
                        'achievers': [],
                        'L': L,
                        'v2Lfact': v2Lfact,
                        'LB': None,
                        'status': 'extraction_failed',
                    }
                    continue
            search_T = 8 if L >= 4 else 10
            delta, ach = compute_delta(Q_ab, c_val, k, search_T=search_T)
            dt = time.time() - t0
            LB = 2 * v2Lfact + delta if delta is not None else None
            ach_str = ", ".join(f"({a},{b},v2={v})" for a, b, v in ach[:3])
            print(f"  k={k}: L={L}, v_2(L!)={v2Lfact}, Δ={delta}, "
                  f"LB_k = 2·{v2Lfact} + {delta} = {LB}   [{dt:.1f}s]")
            print(f"       achievers: {ach_str}")
            catalog[(c_val, k)] = {
                'Delta': delta,
                'achievers': [list(x) for x in ach[:5]],
                'L': L,
                'v2Lfact': v2Lfact,
                'LB': LB,
                'status': 'ok',
            }

    # Save
    print("\n" + "=" * 74)
    print("SUMMARY MATRIX")
    print("=" * 74)
    print(f"\nΔ_k^{{(c)}} for c ∈ [5..11], k ∈ [0..c-1]:\n")
    header = "  c\\k |" + "".join(f"{k:>7d}" for k in range(11))
    print(header)
    print("  " + "-" * (len(header) - 2))
    for c_val in c_range:
        row = f"  {c_val:>3d} |"
        for k in range(11):
            if (c_val, k) in catalog:
                d = catalog[(c_val, k)]['Delta']
                s = str(d) if d is not None else "-"
            else:
                s = "-"
            row += f"{s:>7s}"
        print(row)

    print(f"\nLB_k^{{(c)}} = 2 v_2(L!) + Δ_k^{{(c)}}, L = c-1-k:\n")
    print(header)
    print("  " + "-" * (len(header) - 2))
    for c_val in c_range:
        row = f"  {c_val:>3d} |"
        for k in range(11):
            if (c_val, k) in catalog:
                lb = catalog[(c_val, k)]['LB']
                s = str(lb) if lb is not None else "-"
            else:
                s = "-"
            row += f"{s:>7s}"
        print(row)

    print(f"\nmin_k LB_k^{{(c)}} per c (predicted β'(c)):\n")
    for c_val in c_range:
        lbs = [catalog[(c_val, k)]['LB'] for k in range(c_val)
               if (c_val, k) in catalog and catalog[(c_val, k)]['LB'] is not None]
        if not lbs:
            print(f"  c={c_val}: no data")
            continue
        min_lb = min(lbs)
        argmin = [k for k in range(c_val)
                  if (c_val, k) in catalog and catalog[(c_val, k)]['LB'] == min_lb]
        print(f"  c={c_val}: min LB = {min_lb} at k* ∈ {argmin}")

    # Save JSON
    out = {
        'note': 'Δ_k^{(c)} catalog for SCP-uniform proof (Day 90/91).',
        'definition': 'h_k^{(c)}(a,b) = (a+3)_L (b+2)_L Q_k(a,b,c), L=c-1-k. '
                      'Δ_k^{(c)} = min v_2(Q_k(a,b,c)) over shell (a+b ≡ c mod 2) '
                      'AND Poch-min locus ((a+2)&L=0 AND (b+1)&L=0).',
        'LB_formula': 'LB_k^{(c)} = 2 v_2(L!) + Δ_k^{(c)}   [clean regime k ≤ c-1]',
        'source_Q_catalog': 'code/2026-07-11-Qk-catalog.json',
        'data': {f"c{c},k{k}": v for (c, k), v in catalog.items()},
    }
    with open('/home/agent/projects/code/2026-07-12-Delta-k-c-catalog.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("\nSaved /home/agent/projects/code/2026-07-12-Delta-k-c-catalog.json")

    return catalog


if __name__ == "__main__":
    main()
