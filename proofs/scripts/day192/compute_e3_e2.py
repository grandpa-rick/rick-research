"""Day 192: compute e_3 ⋆ e_2 at m=5.
   Partitions of 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1).
   Rick's meta-conjecture: min(3,2)+1 = 3 nonzero e_lambda coefficients.
"""

import sympy as sp
import pickle
from hikita_star import compute_ea_star_er, print_expansion, q, t


def main():
    print("=" * 72)
    print("Compute e_3 ⋆ e_2 at m=5")
    print("=" * 72)
    exp = compute_ea_star_er(3, 2, 5, verbose=True)
    print_expansion(exp, "e_3 ⋆ e_2 at m=5:")

    with open('e3_e2_m5.pkl', 'wb') as f:
        pickle.dump({str(k): sp.srepr(v) for k, v in exp.items()}, f)

    # Nonzero support
    print("\n----- NONZERO SUPPORT -----")
    nz = []
    for lam, c in exp.items():
        cs = sp.simplify(c)
        if cs != 0:
            nz.append((lam, cs))
            print(f"  e_{lam} = {sp.factor(cs)}")
    print(f"\n#nonzero terms: {len(nz)}")
    print(f"Meta-conjecture prediction (min(3,2)+1 = 3): {'PASS' if len(nz) == 3 else 'FAIL'}")

    # Sanity 1: at q=1, should give e_3 * e_2 = e_{3,2}
    print("\n----- SANITY q=1: should give e_{3,2} only -----")
    for lam, c in exp.items():
        cs = sp.simplify(c.subs(q, 1))
        if cs != 0 or lam == (3, 2):
            print(f"  e_{lam} @ q=1: {sp.simplify(cs)}")

    # Sanity 2: q → ∞. Hikita Thm C(ii): leading term in q^0 is e_a ⋆_∞ e_b.
    # For q→∞ in Rick's expected form, the top e_5 coefficient dominates.
    print("\n----- Leading behaviour in 1/q -----")
    for lam, c in exp.items():
        cs = sp.simplify(c)
        if cs != 0:
            # Expand in 1/q, get leading behaviour
            cs_expand = sp.expand(cs)
            # power of q in numerator/denominator
            num, den = sp.fraction(sp.together(cs))
            deg_num = sp.Poly(num, q).degree() if not num.is_number else 0
            deg_den = sp.Poly(den, q).degree() if not den.is_number else 0
            print(f"  e_{lam}: deg_num = {deg_num}, deg_den = {deg_den}, "
                  f"leading q^{deg_num - deg_den} coeff = {sp.simplify(cs * q**(deg_den - deg_num)).subs(q, sp.oo) if deg_num - deg_den != 0 else sp.simplify(cs.subs(q, sp.oo))}")


if __name__ == "__main__":
    main()
