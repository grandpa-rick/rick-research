"""Test the fundamental identity for H_c in the boundary regime:

    H_c(a, b, j) * (a+c-j+2)_{j-c+1} * (b+c-j+1)_{j-c+1} = P_j(a, b, c)

for j > c-1, where P_j is the Sym-side polynomial (Day 86, via Aitken det).

If this holds, then the extension of (♦) to the boundary regime is a rational
function identity that ROUTINELY divides P_j by the excess Pochhammer factors.
"""
import sys
sys.path.insert(0, '/home/agent/projects/code')
from importlib import import_module
mod = import_module('2026-07-10-boundary-check')

tables = mod.build_e2_tables(max_j=16)


def main():
    print("Test: In boundary regime j > c-1, does the identity")
    print("      H_c(a,b,j) * (a+c-j+2)_m * (b+c-j+1)_m = P_j(a,b,c)")
    print("      hold?   [m = j-c+1, so m > 0]")
    print("=" * 78)
    for c_val in [4, 5, 6, 7]:
        for j in range(c_val, 2 * c_val):
            m = j - c_val + 1
            print(f"\n--- c={c_val}, j={j}, m={m} ---")
            mismatches = 0
            checked = 0
            for a_val in range(j + 2, j + 12):
                for b_val in range(j, a_val + 1):
                    Hc = mod.H_c_template(a_val, b_val, c_val, j, tables)
                    Pj = mod.P_j_direct(a_val, b_val, c_val, j, tables)
                    if Hc is None or Pj is None:
                        continue
                    pa = mod.rising_fact(a_val + c_val - j + 2, m)
                    pb = mod.rising_fact(b_val + c_val - j + 1, m)
                    lhs = Hc * pa * pb
                    checked += 1
                    if lhs != Pj:
                        mismatches += 1
                        if mismatches < 3:
                            print(f"    MISMATCH (a,b)=({a_val},{b_val}): "
                                  f"H_c*{pa*pb}={lhs} vs P_j={Pj}, ratio={lhs/Pj if Pj else 0}")
            print(f"    checked={checked}, mismatches={mismatches}, "
                  f"{'PASS' if mismatches == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
