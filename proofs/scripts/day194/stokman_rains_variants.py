"""
Day 194 PROVE (follow-up): Test THREE (four) variant conventions for the
Stokman-Rains Lemma-10-style identity in Hikita's level-1 AHA.

Original test (stokman_rains_check.py) FAILED at m=3,4:
   Y_{m-1} Y_m  ?=  t^{-1} (Pi T_1 T_2 ... T_{m-2})^2

Diagnosis: X-index mismatch (no scalar fixes it).  Rick may have miscopied
the DAHA identity from Stokman-Rains arXiv:2307.02385 Lemma 10.

Variants tested here:
  A: LHS = Y_{m-1} Y_m, RHS = t^{-1} (T_{m-2} ... T_1 Pi)^2   [reverse T-chain]
  B: LHS = Y_1 Y_2,     RHS = t^{-1} (Pi T_1 ... T_{m-2})^2   [swap LHS]
  C: LHS = Y_1 Y_2,     RHS = t^{-1} (T_{m-2} ... T_1 Pi)^2   [swap LHS, reverse]
  D: LHS = Y_1 Y_2,     RHS = t^{-1} (T_1 T_2 ... T_{m-2} Pi)^2   [inverse element]

Composition convention: op-string A_1 A_2 ... A_k applied to f means
    A_1 . (A_2 . (... (A_k . f)))
i.e. rightmost first.  This matches the existing apply_A in stokman_rains_check.

Test on f in {1, X_1, X_1 X_2} at m in {3, 4}.
"""

import sys
import time
import sympy as sp

sys.path.insert(0, '/home/agent/projects/proofs/scripts/day191')
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day194')

from e2_star_e2 import build_action, q, t


# -------- Operator builders for each variant --------

def apply_A_forward(F, m, Ti_apply, Pi_apply):
    """A = Pi . T_1 . T_2 ... T_{m-2}   [Pi on LEFT, T-chain forward]
    Rightmost first: T_{m-2}, T_{m-3}, ..., T_1, then Pi.
    """
    G = F
    for j in range(m - 2, 0, -1):
        G = Ti_apply(G, j)
    G = Pi_apply(G)
    return sp.expand(G)


def apply_A_reverse_T(F, m, Ti_apply, Pi_apply):
    """A = T_{m-2} . T_{m-3} ... T_1 . Pi   [Pi on RIGHT, reverse T-chain]
    Rightmost first: Pi, then T_1, T_2, ..., T_{m-2}.
    """
    G = F
    G = Pi_apply(G)
    for j in range(1, m - 1):
        G = Ti_apply(G, j)
    return sp.expand(G)


def apply_A_forward_T_Pi_right(F, m, Ti_apply, Pi_apply):
    """A = T_1 . T_2 ... T_{m-2} . Pi   [Pi on RIGHT, forward T-chain]
    Rightmost first: Pi, then T_{m-2}, T_{m-3}, ..., T_1.
    """
    G = F
    G = Pi_apply(G)
    for j in range(m - 2, 0, -1):
        G = Ti_apply(G, j)
    return sp.expand(G)


# -------- Test drivers --------

def test_variant(name, lhs_indices, apply_A, m, test_polys, out_lines):
    """
    lhs_indices = (i, j)  meaning LHS = Y_i . (Y_j . f)  (so Y_i Y_j on the left).
    """
    header = f"\n{'-'*72}\nVariant {name}: LHS = Y_{lhs_indices[0]} Y_{lhs_indices[1]}, m={m}\n{'-'*72}"
    print(header)
    out_lines.append(header)

    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)

    results = []
    for label, f in test_polys:
        t_start = time.time()
        i, j = lhs_indices
        Yj_f = Y_apply(f, j)
        lhs = Y_apply(Yj_f, i)

        Af = apply_A(f, m, Ti_apply, Pi_apply)
        AAf = apply_A(Af, m, Ti_apply, Pi_apply)
        rhs = sp.expand(AAf / t)

        diff = sp.expand(lhs - rhs)
        try:
            diff_simpl = sp.simplify(sp.cancel(diff))
        except Exception:
            diff_simpl = sp.cancel(diff)

        elapsed = time.time() - t_start
        if diff_simpl == 0:
            status = "PASS"
            eq_val = sp.expand(lhs)
            line = f"  [m={m}] {name} f={label}: PASS   ({elapsed:.2f}s)  equal value = {eq_val}"
        else:
            status = "FAIL"
            try:
                dfact = sp.factor(diff_simpl)
            except Exception:
                dfact = diff_simpl
            dstr = str(dfact)
            if len(dstr) > 200:
                dstr = dstr[:200] + " ... [truncated]"
            line = f"  [m={m}] {name} f={label}: FAIL   ({elapsed:.2f}s)  diff factored = {dstr}"

        print(line)
        out_lines.append(line)
        results.append((label, status))

    return results


def main():
    t_wall = time.time()
    out_lines = []
    hdr = ("Day 194 PROVE: Stokman-Rains variant test\n"
           "Trying to find a variant of the Lemma-10 identity that lifts.\n"
           "Test polys: f in {1, X_1, X_1*X_2},  m in {3, 4}.\n")
    print(hdr); out_lines.append(hdr)

    variants = [
        # (name, lhs_indices, apply_A_function, description)
        ("A", (None, None), apply_A_reverse_T,
         "Y_{m-1} Y_m == t^{-1} (T_{m-2} ... T_1 Pi)^2   [reverse T-chain]"),
        ("B", (1, 2), apply_A_forward,
         "Y_1 Y_2 == t^{-1} (Pi T_1 ... T_{m-2})^2   [forward T-chain]"),
        ("C", (1, 2), apply_A_reverse_T,
         "Y_1 Y_2 == t^{-1} (T_{m-2} ... T_1 Pi)^2   [reverse T-chain]"),
        ("D", (1, 2), apply_A_forward_T_Pi_right,
         "Y_1 Y_2 == t^{-1} (T_1 T_2 ... T_{m-2} Pi)^2   [Pi on right, forward T]"),
    ]

    summary = {}  # variant -> m -> list of (label, status)

    for name, lhs_indices, apply_A, desc in variants:
        s = f"\n{'='*72}\nVARIANT {name}: {desc}\n{'='*72}"
        print(s); out_lines.append(s)
        summary[name] = {}
        for m in [3, 4]:
            # Adjust LHS indices for variant A: (m-1, m)
            if name == "A":
                indices = (m - 1, m)
            else:
                indices = lhs_indices

            X_syms = sp.symbols(f'X1:{m+1}')
            test_polys = [
                ("1", sp.Integer(1)),
                ("X1", X_syms[0]),
                ("X1*X2", X_syms[0] * X_syms[1]),
            ]
            results = test_variant(name, indices, apply_A, m, test_polys, out_lines)
            summary[name][m] = results

    # Global summary
    hdr = "\n" + "=" * 72 + "\nGLOBAL SUMMARY (PASS/FAIL matrix)\n" + "=" * 72
    print(hdr); out_lines.append(hdr)

    line = f"  {'Variant':<10} {'m':<4} {'f=1':<8} {'f=X1':<8} {'f=X1*X2':<10}"
    print(line); out_lines.append(line)
    line = "  " + "-" * 42
    print(line); out_lines.append(line)

    passing_variants = []
    for name in ["A", "B", "C", "D"]:
        for m in [3, 4]:
            res = summary[name][m]
            row = {label: status for label, status in res}
            line = (f"  {name:<10} {m:<4} "
                    f"{row.get('1','?'):<8} "
                    f"{row.get('X1','?'):<8} "
                    f"{row.get('X1*X2','?'):<10}")
            print(line); out_lines.append(line)
        # Check global pass for this variant
        all_pass = all(
            all(status == "PASS" for _, status in summary[name][m])
            for m in [3, 4]
        )
        if all_pass:
            passing_variants.append(name)

    # Recommendation
    rec = "\n" + "=" * 72 + "\nRECOMMENDATION\n" + "=" * 72
    print(rec); out_lines.append(rec)
    if passing_variants:
        for v in passing_variants:
            line = (f"  Variant {v} PASSES at both m=3 and m=4 on all three test polys.\n"
                    f"  STRONG SIGNAL: likely the correct Stokman-Rains lift.\n"
                    f"  ACTION: test at higher m (m=5,6) and pursue as analytic proof route.")
            print(line); out_lines.append(line)
    else:
        line = ("  ALL variants A, B, C, D FAIL at m=3 and/or m=4.\n"
                "  RECOMMENDATION: abandon the Stokman-Rains lift for Path 3.\n"
                "  The X-index mismatch is a structural obstruction, not a convention error.")
        print(line); out_lines.append(line)

    elapsed = time.time() - t_wall
    tline = f"\nWallclock time: {elapsed:.2f}s"
    print(tline); out_lines.append(tline)

    out_path = "/home/agent/projects/proofs/scripts/day194/stokman_rains_variants_output.txt"
    with open(out_path, "w") as fh:
        fh.write("\n".join(out_lines) + "\n")
    print(f"\nOutput saved to {out_path}")


if __name__ == "__main__":
    main()
