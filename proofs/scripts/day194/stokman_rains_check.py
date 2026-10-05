"""
Day 194 PROVE: Test whether Stokman-Rains Lemma 10 (DAHA) lifts to Hikita's
level-1 AHA of GL_m.

Claim to test (AS WRITTEN):

  Y_{m-1} Y_m  ==  t^{-1} (Pi T_1 T_2 ... T_{m-2})^2

as operators on the polynomial rep Q(q,t)[X_1, ..., X_m].

Test at m=3 and m=4 against a spanning basis of test polynomials.

Method:
 - Reuse the actions from day191/e2_star_e2.py:  T_i, T_i^{-1}, Pi, Y_i
 - LHS: apply Y_m first, then Y_{m-1}
 - RHS: A = Pi . T_1 . T_2 ... T_{m-2}  as an operator
        RHS_f = t^{-1} * A . (A . f)
        Careful with composition order: (Pi T_1 T_2 ... T_{m-2}) . g
        means the RIGHTMOST operator (T_{m-2}) hits g first, then T_{m-3}, ...,
        then T_1, then Pi.
 - Compare LHS - RHS via sp.simplify / sp.cancel.
 - PASS iff difference is identically zero as a polynomial in X_i (with
   coefficients in Q(q,t)).

Sober: this tests the identity literally; we do not insert any level-1
correction.  If it fails, we report the obstruction polynomial factored.
"""

import sys
import time
import sympy as sp

sys.path.insert(0, '/home/agent/projects/proofs/scripts/day191')
from e2_star_e2 import build_action, e_r_X, q, t


def apply_A(F, m, Ti_apply, Pi_apply):
    """Apply A = Pi . T_1 . T_2 . ... . T_{m-2}  to F.

    Composition order: A . g means T_{m-2} acts first, then T_{m-3}, ...,
    then T_1, then Pi.  (Rightmost operator is applied first.)

    Special case m=2:  A = Pi (the T-chain is empty).
    Special case m=3:  A = Pi . T_1  (just one T).
    """
    G = F
    # Apply T_{m-2}, T_{m-3}, ..., T_1  (rightmost first)
    for j in range(m - 2, 0, -1):   # j = m-2, m-3, ..., 1
        G = Ti_apply(G, j)
    # Then Pi
    G = Pi_apply(G)
    return sp.expand(G)


def test_identity_at_m(m, test_polys, out_lines):
    """Test Y_{m-1} Y_m == t^{-1} A^2 on each f in test_polys.

    Returns list of (label, PASS/FAIL, difference_polynomial).
    """
    header = f"\n{'='*72}\nTesting at m = {m}\n{'='*72}"
    print(header)
    out_lines.append(header)

    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)

    results = []
    for label, f in test_polys:
        t_start = time.time()
        # LHS: Y_{m-1} . (Y_m . f)
        Ym_f = Y_apply(f, m)
        lhs = Y_apply(Ym_f, m - 1)

        # RHS: t^{-1} * A . (A . f)
        Af = apply_A(f, m, Ti_apply, Pi_apply)
        AAf = apply_A(Af, m, Ti_apply, Pi_apply)
        rhs = sp.expand(AAf / t)

        diff = sp.expand(lhs - rhs)
        diff_simpl = sp.cancel(diff)
        # Extra sanity: if diff_simpl is a rational function, together it
        # will collect over common denominator; check numerator.
        try:
            diff_simpl = sp.simplify(diff_simpl)
        except Exception:
            pass

        elapsed = time.time() - t_start

        if diff_simpl == 0:
            status = "PASS"
            line = f"  [m={m}] f = {label}: {status}   ({elapsed:.2f}s)"
            print(line)
            out_lines.append(line)
            results.append((label, "PASS", sp.Integer(0)))
        else:
            status = "FAIL"
            line = f"  [m={m}] f = {label}: {status}   ({elapsed:.2f}s)"
            print(line)
            out_lines.append(line)
            # Try to factor
            try:
                dfact = sp.factor(diff_simpl)
            except Exception:
                dfact = diff_simpl
            fline = f"    difference (factored): {dfact}"
            print(fline)
            out_lines.append(fline)
            # Also raw expanded form (may be huge; truncate print)
            raw = sp.expand(diff_simpl)
            raw_str = str(raw)
            if len(raw_str) > 500:
                raw_str = raw_str[:500] + " ... [truncated]"
            rline = f"    difference (expanded, maybe truncated): {raw_str}"
            print(rline)
            out_lines.append(rline)
            results.append((label, "FAIL", diff_simpl))
    return results


def build_test_polys(m):
    """Return list of (label, poly) for testing at given m.

    Covers deg 0, 1, 2, 3 with a spanning-enough basis.
    """
    X = sp.symbols(f'X1:{m+1}')
    polys = []
    polys.append(("1", sp.Integer(1)))
    # All X_i, degree 1
    for i in range(m):
        polys.append((f"X{i+1}", X[i]))
    # Degree 2 monomials
    polys.append(("X1^2", X[0]**2))
    if m >= 2:
        polys.append(("X1*X2", X[0] * X[1]))
    if m >= 3:
        polys.append(("X2*X3", X[1] * X[2]))
    # Degree 3
    if m >= 3:
        polys.append(("X1*X2*X3", X[0] * X[1] * X[2]))
    polys.append(("X1^3", X[0]**3))
    # Elementary symmetric
    polys.append(("e_2(X)", e_r_X(m, 2)))
    if m >= 3:
        polys.append(("e_3(X)", e_r_X(m, 3)))
    return polys


def main():
    t_wall = time.time()
    out_lines = []
    hdr = ("Day 194 PROVE: Stokman-Rains Lemma 10 lift to Hikita level-1 AHA?\n"
           "Testing:  Y_{m-1} Y_m  ==  t^{-1} (Pi T_1 T_2 ... T_{m-2})^2\n"
           "on the polynomial rep Q(q,t)[X_1, ..., X_m], for m in {3, 4}.\n")
    print(hdr)
    out_lines.append(hdr)

    all_results = {}
    for m in [3, 4]:
        polys = build_test_polys(m)
        if m == 4:
            # Guard against SymPy hangs: keep the deg 0..2 basis + a few
            # deg-3 monomials + e_2, e_3.  We already have that above.
            pass
        results = test_identity_at_m(m, polys, out_lines)
        all_results[m] = results

    # Summary
    summ = "\n" + "=" * 72 + "\nSUMMARY\n" + "=" * 72
    print(summ)
    out_lines.append(summ)
    for m, res in all_results.items():
        n_pass = sum(1 for r in res if r[1] == "PASS")
        n_fail = sum(1 for r in res if r[1] == "FAIL")
        s = f"  m={m}: {n_pass} PASS, {n_fail} FAIL out of {len(res)}"
        print(s); out_lines.append(s)
        if n_fail > 0:
            for label, status, diff in res:
                if status == "FAIL":
                    try:
                        dfact = sp.factor(diff)
                    except Exception:
                        dfact = diff
                    s = f"    FAIL: f={label}, diff factored = {dfact}"
                    print(s); out_lines.append(s)

    elapsed = time.time() - t_wall
    tline = f"\nWallclock time: {elapsed:.2f}s"
    print(tline); out_lines.append(tline)

    # Save to output file
    out_path = "/home/agent/projects/proofs/scripts/day194/stokman_rains_output.txt"
    with open(out_path, "w") as fh:
        fh.write("\n".join(out_lines) + "\n")
    print(f"\nOutput saved to {out_path}")


if __name__ == "__main__":
    main()
