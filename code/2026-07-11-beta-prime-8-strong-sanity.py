"""Day 89 Stage B — STRONG sanity check for β'(8) = 11.

Belt-and-braces after the mod 2^11 periodicity check.  Three checks:

  (S1) Direct-integer v_2 sweep of h_k^{(c=8)}(a, b) over (a, b) ∈ [0, 64]²
       with a+b even.  Reports min v_2 for each k WITHOUT going through
       mod 2^11 — an independent witness that the periodicity grid check
       isn't hiding a bug.

  (S2) Möbius reconstruction sanity — reconstruct H_8(a, b, j) from the
       h_k^{(c=8)} at 100+ test points (a, b, j) and cross-check against
       the pipeline H_c_template.  This is the "100-point sanity" the
       CODE.md plan calls for; the extract script only checked 21.

  (S3) Explicit β'(8) = 11 statement:  min v_2 lower bound (from S1) +
       exact witness (from V1: H_8(8,8,2) = 2^11 * 1661793608475).

Runs in ~3 min.
"""
import pickle
import time
from importlib import util
from math import factorial

from sympy import Poly, expand, symbols

a_s, b_s = symbols('a b')

# Load pipeline (Möbius sanity cross-check)
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
build_e2_tables = mod.build_e2_tables
H_c_template = mod.H_c_template


def v2_int(n):
    if n == 0:
        return float('inf')
    m = abs(int(n))
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    return r


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def load_h_c8():
    """Load h_k^{(c=8)}(a, b) as sympy Polys from the pickle."""
    with open('/home/agent/projects/code/2026-07-11-c8-hk-fits.pkl', 'rb') as f:
        d = pickle.load(f)
    h = {}
    for k, s in d.items():
        h[k] = Poly(expand(eval(s, {'a': a_s, 'b': b_s})), a_s, b_s, domain='ZZ')
    return h


def poly_int_eval(poly, a_val, b_val):
    """Fast integer evaluation of a Poly[a, b] via Horner / dict eval."""
    d = poly.as_dict()
    val = 0
    for (da, db), coef in d.items():
        val += int(coef) * (a_val ** da) * (b_val ** db)
    return val


def main():
    sep = "=" * 74
    print(sep)
    print("Day 89 Stage B — STRONG sanity for β'(8) = 11 (integer arithmetic)")
    print(sep)

    print("\n[Loading] h_k^{(c=8)}(a, b) from pickle...")
    h = load_h_c8()
    print(f"    Loaded {len(h)} polynomials (k = {sorted(h.keys())})")

    # ------------------------------------------------------------------
    # (S1) Direct-integer v_2 sweep
    # ------------------------------------------------------------------
    print("\n[S1] Direct-integer v_2 sweep of h_k^{(c=8)}(a, b),"
          " (a, b) ∈ [0, 64]² with a+b even")
    T = 11
    per_k_min = {}
    per_k_argmin = {}
    t_total = 0.0
    for k in sorted(h.keys()):
        t0 = time.time()
        p = h[k]
        m = float('inf')
        argmin = None
        for a in range(0, 64):
            for b in range(0, 64):
                if (a + b) % 2 != 0:
                    continue
                v = poly_int_eval(p, a, b)
                if v == 0:
                    continue
                vv = v2_int(v)
                if vv < m:
                    m = vv
                    argmin = (a, b, v)
        dt = time.time() - t0
        t_total += dt
        per_k_min[k] = m
        per_k_argmin[k] = argmin
        status = "PASS" if (m >= T or m == float('inf')) else "FAIL"
        pretty_m = "inf" if m == float('inf') else str(m)
        print(f"  k={k:>2d}: {status}  min v_2 = {pretty_m}"
              + (f"   argmin (a, b, val) = {argmin}" if argmin else "  (poly ≡ 0 on shell)")
              + f"   ({dt:.1f}s)")
    print(f"\n  Total sweep time: {t_total:.1f}s")
    S1_pass = all(m >= T or m == float('inf') for m in per_k_min.values())
    print(f"  → S1: {'PASS' if S1_pass else 'FAIL'}  (min v_2 ≥ {T} for all k = 0..15)")

    # ------------------------------------------------------------------
    # (S2) Möbius reconstruction — 100+ point sanity
    # ------------------------------------------------------------------
    print("\n[S2] Möbius reconstruction sanity: H_8(a, b, j) = Σ C(j,k) h_k^(8)(a,b)")
    tables = build_e2_tables(max_j=17)
    n_ok = 0
    n_fail = 0
    fails = []
    t0 = time.time()
    for a in range(8, 22):
        for b in range(8, a + 1):
            for j in range(0, 16):
                H_actual = H_c_template(a, b, 8, j, tables)
                if H_actual is None:
                    continue
                H_pred = 0
                for k in range(min(j, 15) + 1):
                    if k not in h:
                        H_pred = None
                        break
                    H_pred += Cn(j, k) * poly_int_eval(h[k], a, b)
                if H_pred is None:
                    continue
                if H_actual == H_pred:
                    n_ok += 1
                else:
                    n_fail += 1
                    if len(fails) < 3:
                        fails.append((a, b, j, H_actual, H_pred))
    dt = time.time() - t0
    print(f"  Tested {n_ok + n_fail} triples (a, b, j) in {dt:.1f}s")
    print(f"    Match: {n_ok}   Mismatch: {n_fail}")
    for f in fails:
        print(f"    FAIL (a,b,j)=({f[0]},{f[1]},{f[2]}): actual={f[3]}  pred={f[4]}")
    S2_pass = n_ok >= 100 and n_fail == 0
    print(f"  → S2: {'PASS' if S2_pass else 'FAIL'}  ({n_ok} match, {n_fail} fail — required ≥ 100 match, 0 fail)")

    # ------------------------------------------------------------------
    # (S3) β'(8) = 11 statement
    # ------------------------------------------------------------------
    print("\n[S3] β'(8) = 11 assembly")
    tables = build_e2_tables(max_j=17)
    H_witness = H_c_template(8, 8, 8, 2, tables)
    v_witness = v2_int(H_witness)
    odd_part = H_witness // (1 << v_witness)
    print(f"    Upper witness:  H_8(8, 8, 2) = {H_witness}")
    print(f"                   = 2^{v_witness} * {odd_part}   (odd? {odd_part % 2 == 1})")
    print(f"    Lower bound:    v_2(H_8(a, b, j)) ≥ min_k v_2(h_k^(8)(a, b))"
          f"  (a+b even) ≥ {T}   [S1 + polynomial 2^T-periodicity]")
    S3_pass = v_witness == T and S1_pass and S2_pass
    print(f"  → S3: {'PASS' if S3_pass else 'FAIL'}")

    print("\n" + sep)
    print("SUMMARY")
    print(sep)
    print(f"  S1 (direct integer sweep, min v_2 ≥ {T}):  {'PASS' if S1_pass else 'FAIL'}")
    print(f"  S2 (100+ point Möbius sanity):            {'PASS' if S2_pass else 'FAIL'}")
    print(f"  S3 (β'(8) = 11 assembled):                {'PASS' if S3_pass else 'FAIL'}")
    if S1_pass and S2_pass and S3_pass:
        print(f"\n  ∴ β'(8) = 11 — strongly verified.")
    else:
        print(f"\n  ! Some checks failed; investigate.")


if __name__ == "__main__":
    main()
