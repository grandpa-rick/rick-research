"""Compute e_3 ⋆ e_6 at m=9 for Day 193 verification.

Uses Day 192 framework. Output pickled + txt.
"""
import sys
import time
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day192')

from hikita_star import compute_ea_star_er, sanity_q1, print_expansion
import pickle
import sympy as sp

q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

if __name__ == "__main__":
    start = time.time()
    print("=" * 80)
    print("Day 193: Compute e_3 ⋆ e_6 at m=9")
    print("=" * 80)

    a, r, m = 3, 6, 9
    expansion = compute_ea_star_er(a, r, m, verbose=True)

    end = time.time()
    print(f"\nWallclock: {end - start:.1f}s")

    # Save results
    with open('/home/agent/projects/proofs/scripts/day193/e3_e6_m9.pkl', 'wb') as f:
        pickle.dump({(lam): c for lam, c in expansion.items()}, f)

    # Print nonzero
    print(f"\n--- e_3 ⋆ e_6 at m=9 (n={a+r}) ---")
    nonzero = 0
    for lam, c in expansion.items():
        cs = sp.simplify(c)
        if cs != 0:
            nonzero += 1
            print(f"  e_{lam} = {sp.factor(cs)}")
    print(f"  #nonzero = {nonzero}, predicted min(3,6)+1 = 4")

    # Sanity: q=1
    print(f"\n--- Sanity check: at q=1 ---")
    for lam, c in expansion.items():
        cs = sp.simplify(c.subs(q, 1))
        if cs != 0:
            print(f"  e_{lam} at q=1 = {cs}")

    # Verify Day 192 predictions
    print(f"\n--- Verify Day 192 predictions at r=6 ---")
    predictions = {
        (6, 3): sp.simplify(1/q**3),
        (7, 2): sp.simplify((q-1)*qint(r-1)/q**3),  # r-1=5, so [5]_t
        (8, 1): sp.simplify((q-1)*qint(r+1)*(q*qint(r) - t*qint(r-2))/(q**3 * qint(2))),  # r+1=7, r=6, r-2=4
    }
    for lam, pred in predictions.items():
        actual = expansion.get(lam, sp.Integer(0))
        diff = sp.simplify(actual - pred)
        print(f"  e_{lam}: predicted = {sp.factor(pred)}")
        print(f"  e_{lam}: actual    = {sp.factor(sp.simplify(actual))}")
        print(f"  diff = {diff}")
        print()
