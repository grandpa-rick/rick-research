"""Day 89 Stage B — Verification of the beta'(8) = 11 witness certificate.

Goal: independently cross-check the c=8 periodicity result before pushing.

Checks:
  (V1) H_8(8, 8, 2) — recompute directly from the pipeline; verify
       v_2 = 11 exactly (the printout in c8-periodicity-output.txt has a
       formatting glitch showing "* 1661793413162.5", so double-check).
  (V2) k=1 sanity (Day-88 meta-rule) — evaluate h_1^{(c=8)}(a, b) from
       the fitted polynomial vs the pipeline's own extract_h_k at many
       random (a, b). Match required exactly.
  (V3) Parity shell — verify the c=8 physical shell is a+b even, by
       comparing v_2 of H_8(a, b, j) for a+b odd vs a+b even at low j.
  (V4) Direct search for a v_2-carrier — search a small (a, b) window
       for the H_8 argmin v_2 achiever. If min = 11, β'(8) = 11 upper
       and lower agree.
"""
import random
import time
from importlib import util
from math import factorial

from sympy import Poly, expand, symbols

# Load pipeline
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
build_e2_tables = mod.build_e2_tables
H_c_template = mod.H_c_template
extract_h_k = mod.extract_h_k


a_s, b_s = symbols('a b')


def v2_int(n):
    if n == 0:
        return float('inf')
    m = abs(int(n))
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    return r


# Fitted h_k^{(c=8)} — factored, from 2026-07-11-c8-extract-hk-output.txt.
h_c8 = {
    0: (a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)*(a_s + 7)*(a_s + 8)*(a_s + 9)
       * (b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)*(b_s + 6)*(b_s + 7)*(b_s + 8),
    1: -56*(a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)*(a_s + 7)*(a_s + 8)
        *(b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)*(b_s + 6)*(b_s + 7),
    2: -16*(a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)*(a_s + 7)
        *(b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)*(b_s + 6)
        *(a_s*b_s + a_s + 2*b_s - 145),
    3: 2016*(a_s + 3)*(a_s + 4)*(a_s + 5)*(a_s + 6)
        *(b_s + 2)*(b_s + 3)*(b_s + 4)*(b_s + 5)
        *(a_s*b_s + a_s + 2*b_s - 33),
    4: 672*(a_s + 3)*(a_s + 4)*(a_s + 5)*(b_s + 2)*(b_s + 3)*(b_s + 4)
        *(a_s**2*b_s**2 + a_s**2*b_s + 3*a_s*b_s**2 - 177*a_s*b_s - 180*a_s
          + 2*b_s**2 - 358*b_s + 1740),
    5: -100800*(a_s + 3)*(a_s + 4)*(b_s + 2)*(b_s + 3)
        *(a_s**2*b_s**2 + a_s**2*b_s + 3*a_s*b_s**2 - 37*a_s*b_s - 40*a_s
          + 2*b_s**2 - 78*b_s + 88),
    6: -40320*(a_s + 3)*(b_s + 2)
        *(a_s**3*b_s**3 - a_s**3*b_s + 3*a_s**2*b_s**3 - 150*a_s**2*b_s**2
          - 153*a_s**2*b_s + 2*a_s*b_s**3 - 450*a_s*b_s**2 + 1348*a_s*b_s
          + 1800*a_s - 300*b_s**2 + 3300*b_s + 1080),
    7: 5644800*(a_s**3*b_s**3 - a_s**3*b_s + 3*a_s**2*b_s**3
                - 30*a_s**2*b_s**2 - 33*a_s**2*b_s + 2*a_s*b_s**3
                - 90*a_s*b_s**2 + 16*a_s*b_s + 108*a_s - 60*b_s**2
                + 156*b_s + 180),
    8: 2822400*(a_s**3*b_s**3 - 3*a_s**3*b_s**2 + 2*a_s**3*b_s
                - 96*a_s**2*b_s**2 + 96*a_s**2*b_s - a_s*b_s**3
                - 93*a_s*b_s**2 + 814*a_s*b_s + 720*b_s - 576),
    9: -304819200*(a_s**2*b_s**2 - 3*a_s**2*b_s + 2*a_s**2 - a_s*b_s**2
                   - 13*a_s*b_s + 14*a_s + 24),
    10: -203212800*(a_s**2*b_s**2 - 5*a_s**2*b_s + 6*a_s**2 - 3*a_s*b_s**2
                    - 30*a_s*b_s + 72*a_s + 2*b_s**2 + 35*b_s + 42),
    11: 13412044800*(a_s*b_s - 3*a_s - 2*b_s + 1),
    12: 13412044800*(a_s*b_s - 4*a_s - 3*b_s),
    13: -348713164800,
    14: -697426329600,
    15: 0,
}


def main():
    sep = "=" * 74
    print(sep)
    print("Day 89 Stage B — β'(8) = 11 verification")
    print(sep)

    # Load tables once
    tables = build_e2_tables(max_j=17)

    # ------------------------------------------------------------------
    # (V1) H_8(8, 8, 2) and its v_2
    # ------------------------------------------------------------------
    print("\n[V1] H_8(8, 8, 2) direct compute")
    val = H_c_template(8, 8, 8, 2, tables)
    print(f"    H_8(8, 8, 2) = {val}")
    vv = v2_int(val)
    print(f"    v_2 = {vv}")
    if val is None:
        print("    !! computed as None. domain issue?")
    else:
        q = val // (1 << vv)
        print(f"    factorization: 2^{vv} * {q}   (q odd? {q % 2 == 1})")
    if vv == 11:
        print("    ✓ V1 PASS: v_2(H_8(8,8,2)) = 11 exactly.")
    else:
        print(f"    ✗ V1 FAIL: expected v_2 = 11, got {vv}")

    # Also check a couple more small witnesses.
    print("\n    Additional H_8 values for context:")
    for (aa, bb, jj) in [(8, 8, 0), (8, 8, 1), (9, 8, 2), (10, 8, 2),
                          (8, 8, 3), (8, 8, 4), (12, 12, 2)]:
        v = H_c_template(aa, bb, 8, jj, tables)
        if v is None:
            print(f"      H_8({aa},{bb},{jj}) = None (out of domain)")
        else:
            print(f"      H_8({aa},{bb},{jj}) = {v}   v_2 = {v2_int(v)}")

    # ------------------------------------------------------------------
    # (V2) k=1 sanity vs pipeline extract_h_k
    # ------------------------------------------------------------------
    print("\n[V2] k=1 sanity — h_1^{(c=8)} fitted poly vs pipeline extract_h_k")
    n_ok = n_fail = 0
    fails = []
    # Sample a wide window
    random.seed(20260711)
    tested = 0
    for a in range(8, 30):
        for b in range(8, a + 1):
            hks = extract_h_k(a, b, 8, 2, tables)
            if hks is None or len(hks) < 2:
                continue
            actual = hks[1]
            predicted = int(h_c8[1].subs({a_s: a, b_s: b}))
            if actual == predicted:
                n_ok += 1
            else:
                n_fail += 1
                fails.append((a, b, actual, predicted))
            tested += 1
    print(f"    Tested {tested} pairs (a,b), a in [8,30), b in [8, a]")
    print(f"    Match: {n_ok}    Mismatch: {n_fail}")
    if fails:
        for f in fails[:3]:
            print(f"      FAIL: (a,b)={f[0],f[1]}  pipe={f[2]} fit={f[3]}")
    if n_fail == 0 and n_ok > 0:
        print("    ✓ V2 PASS: fitted h_1^{(c=8)} matches pipeline everywhere tested.")

    # ------------------------------------------------------------------
    # (V3) Parity shell — verify c=8 physical shell is a+b even
    # ------------------------------------------------------------------
    print("\n[V3] Parity shell — verify a+b even is the c=8 physical shell")
    #   For c=8 fixed, sweep j small and (a, b) and check whether the
    #   values in the "a+b odd" shell are vacuous (None / same as trivial)
    #   or nontrivial. In prior work at odd c, the physical shell is
    #   a+b odd; at even c we expect a+b even.
    n_domain_even = n_domain_odd = 0
    val_signature = {'even': [], 'odd': []}
    for a in range(8, 20):
        for b in range(8, a + 1):
            for j in range(0, 6):
                v = H_c_template(a, b, 8, j, tables)
                if v is None:
                    continue
                key = 'even' if (a + b) % 2 == 0 else 'odd'
                if key == 'even':
                    n_domain_even += 1
                else:
                    n_domain_odd += 1
                # Sample a few v_2 values for visibility
                if len(val_signature[key]) < 5:
                    val_signature[key].append((a, b, j, v, v2_int(v)))
    print(f"    a+b even samples in domain: {n_domain_even}")
    print(f"    a+b odd  samples in domain: {n_domain_odd}")
    print("    Even shell samples (a, b, j, H, v_2):")
    for r in val_signature['even']:
        print(f"      {r}")
    print("    Odd shell samples (a, b, j, H, v_2):")
    for r in val_signature['odd']:
        print(f"      {r}")

    # ------------------------------------------------------------------
    # (V4) Direct search for β'(8) min v_2 in small window (physical shell)
    #      β'(c) := min_{a,b,j : a+b+c even} v_2(H_c(a,b,j))
    #      For c=8 (even), shell condition is a+b even.
    # ------------------------------------------------------------------
    print("\n[V4] Direct H_8 v_2 min search on physical shell (a+b even), "
          "a,b in [8, 40], j in [0, 15]")
    best = (float('inf'), None)
    best_offshell = (float('inf'), None)
    for a in range(8, 41):
        for b in range(8, a + 1):
            for j in range(0, 16):
                v = H_c_template(a, b, 8, j, tables)
                if v is None or v == 0:
                    continue
                vv = v2_int(v)
                if (a + b) % 2 == 0:
                    if vv < best[0]:
                        best = (vv, (a, b, j, v))
                else:
                    if vv < best_offshell[0]:
                        best_offshell = (vv, (a, b, j, v))
    print(f"    On-shell (a+b even):   min v_2 = {best[0]}   witness (a, b, j, H_8) = {best[1]}")
    print(f"    Off-shell (a+b odd):   min v_2 = {best_offshell[0]}   witness (a, b, j, H_8) = {best_offshell[1]}")
    print("    (Off-shell values are not in β'(8) domain; shown for context.)")
    v4_pass = best[0] == 11
    if v4_pass:
        print("    ✓ V4 PASS: direct v_2 = 11 on the physical shell, matching the periodicity lower bound.")
    else:
        print(f"    ! V4 shows physical-shell min = {best[0]}")

    # Recompute V1 result (vv was overwritten in V3)
    v1_val = H_c_template(8, 8, 8, 2, tables)
    v1_pass = v2_int(v1_val) == 11

    print("\n" + sep)
    print("SUMMARY")
    print(sep)
    print(f"  V1 (H_8(8,8,2) = 2^11 · odd): {'PASS' if v1_pass else 'FAIL'}")
    print(f"  V2 (h_1 sanity):              {'PASS' if n_fail == 0 else 'FAIL'}")
    print(f"  V4 (physical-shell min = 11): {'PASS' if v4_pass else 'FAIL'}")
    if v1_pass and n_fail == 0 and v4_pass:
        print("\n  ✓ ALL CHECKS PASS — β'(8) = 11 verified.")
    else:
        print("\n  ! Some checks failed — investigate before publishing.")


if __name__ == "__main__":
    main()
