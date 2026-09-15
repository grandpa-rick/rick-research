"""Day 192: compute e_3 ⋆ e_3 at m=6.
   Partitions of 6: (6), (5,1), (4,2), (4,1,1), (3,3), (3,2,1), (3,1,1,1),
   (2,2,2), (2,2,1,1), (2,1,1,1,1), (1^6).
   Rick's meta-conjecture: min(3,3)+1 = 4 nonzero e_lambda coefficients.
   Expected pattern (from e_a⋆e_b): coefficients supported on partitions
     (a+b), (a+b-1, 1), (a+b-2, 2), (a, b) = (6), (5,1), (4,2), (3,3).
"""

import sympy as sp
import pickle
import time
from hikita_star import compute_ea_star_er, print_expansion, q, t


def main():
    print("=" * 72)
    print("Compute e_3 ⋆ e_3 at m=6")
    print("=" * 72)
    t0 = time.time()
    exp = compute_ea_star_er(3, 3, 6, verbose=True)
    print(f"\n[wallclock] {time.time() - t0:.1f}s")

    print_expansion(exp, "e_3 ⋆ e_3 at m=6:")

    with open('e3_e3_m6.pkl', 'wb') as f:
        pickle.dump({str(k): sp.srepr(sp.simplify(v)) for k, v in exp.items()}, f)

    # Nonzero support
    print("\n----- NONZERO SUPPORT -----")
    nz = []
    for lam, c in exp.items():
        cs = sp.simplify(c)
        if cs != 0:
            nz.append((lam, cs))
            print(f"  e_{lam} = {sp.factor(cs)}")
    print(f"\n#nonzero terms: {len(nz)}")
    print(f"Meta-conjecture prediction (min(3,3)+1 = 4): {'PASS' if len(nz) == 4 else 'FAIL'}")

    # Sanity 1: at q=1
    print("\n----- SANITY q=1: should give e_{3,3} only (i.e., e_3 * e_3 as ordinary product) -----")
    for lam, c in exp.items():
        cs = sp.simplify(c.subs(q, 1))
        if cs != 0 or lam == (3, 3):
            print(f"  e_{lam} @ q=1: {sp.simplify(cs)}")


if __name__ == "__main__":
    main()
