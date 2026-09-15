"""Day 192: compute e_3 ⋆ e_r for r = 1, 2, 3, 4, 5 to guess general formula.

Predicted support (from e_1, e_2 patterns):
   e_3 ⋆ e_r supported on partitions (r+3), (r+2,1), (r+1,2), (r,3)
   (r >= 3; for r < 3, drop the last term).

Guessed form (extrapolating from e_2 ⋆ e_r):
   e_3 ⋆ e_r = sum_{k=0..min(3,r)} q^{-k(3-k)/?} * [coeffs]_t * e_{r+3-k, k}
   Note for e_2 ⋆ e_r we had q^{-k(2-k)} for k=0,1,2, which is q^0, q^{+1}(!?)... let me look again.
"""

import sympy as sp
import pickle
import time
from hikita_star import compute_ea_star_er, q, t


def qint(n):
    return sum(t**i for i in range(n))


def report(a, r, m):
    print(f"\n--- e_{a} ⋆ e_{r} at m={m} ---")
    t0 = time.time()
    exp = compute_ea_star_er(a, r, m, verbose=False)
    dt = time.time() - t0
    print(f"  [wallclock {dt:.1f}s]")

    nz = {}
    for lam, c in exp.items():
        cs = sp.simplify(c)
        if cs != 0:
            nz[lam] = cs
    for lam, c in nz.items():
        print(f"  e_{lam} = {sp.factor(c)}")
    print(f"  #nonzero = {len(nz)},  predicted min({a},{r})+1 = {min(a, r) + 1}")
    return nz


def main():
    all_data = {}

    # r = 1: expect 2 terms (should equal Thm 3.12 e_1⋆e_3)
    all_data[(3, 1)] = report(3, 1, 4)
    # r = 2: 3 terms
    all_data[(3, 2)] = report(3, 2, 5)
    # r = 3: 4 terms
    all_data[(3, 3)] = report(3, 3, 6)
    # r = 4: 4 terms (since min(3,4)+1 = 4)
    all_data[(3, 4)] = report(3, 4, 7)
    # r = 5: 4 terms
    # Warning: m=8 might be slow. Let's cap at m=7 (n=8, need m>=8 for all partitions).
    # Actually, we need m >= r+3 for full expansion. For r=5, need m >= 8. Might be slow.
    all_data[(3, 5)] = report(3, 5, 8)

    # Save
    with open('e3_er_data.pkl', 'wb') as f:
        pickle.dump({
            k: {str(lam): sp.srepr(c) for lam, c in nz.items()}
            for k, nz in all_data.items()
        }, f)

    # Print summary in the guessed pattern
    print("\n" + "=" * 72)
    print("SUMMARY: coefficients for k=0,1,2,3 in each e_3 ⋆ e_r")
    print("=" * 72)
    print("Notation: c_k(r) = coefficient of e_{r+3-k, k}")

    for r in [1, 2, 3, 4, 5]:
        print(f"\nr = {r}:")
        nz = all_data[(3, r)]
        for k in range(min(3, r) + 1):
            lam = (r + 3 - k,) if k == 0 else (r + 3 - k, k)
            # For lam=(a,b) with a>=b>0, want e_{a,b}. If b=0 use (a,).
            c = nz.get(lam, sp.Integer(0))
            print(f"  c_{k}(r) [e_{lam}] = {sp.factor(sp.simplify(c))}")


if __name__ == "__main__":
    main()
