"""Compute term-wise v_2 minima for h_k^{(6)}, h_k^{(7)} under parity shell.
For each k, find min_{a,b : parity condition} v_2(h_k(a,b)).
"""
from sympy import symbols
from math import factorial

exec(open('/home/agent/projects/code/2026-07-09-hk-c67-v2-explore.py').read().split("if __name__")[0])


def termwise_min_v2(hk_dict, kmax, c_val, arange=64, brange=64):
    """For each k, find min_{a,b with parity shell} v_2(h_k(a,b))."""
    parity_target = c_val % 2  # if c odd, want a+b odd; if c even, want a+b even
    # (a+b+c) even ⇔ a+b ≡ c (mod 2) ⇔ parity of a+b = parity of c
    print(f"\n### c = {c_val}, parity shell (a+b) ≡ {parity_target} (mod 2) ###")
    print(f"  {'k':>3}  {'min v_2(h_k)':>15}  {'argmin (a,b)':>18}  {'h_k value':>20}")
    for k in range(kmax + 1):
        hk = hk_dict[k]
        best = float('inf')
        arg = None
        for av in range(arange):
            for bv in range(brange):
                if (av + bv) % 2 != parity_target:
                    continue
                val = int(hk.subs({a: av, b: bv})) if hasattr(hk, 'subs') else int(hk)
                if val == 0:
                    continue
                vv = v2(val)
                if vv < best:
                    best = vv
                    arg = (av, bv)
                    argval = val
        if arg is not None:
            print(f"  {k:>3}  {best:>15}  {str(arg):>18}  {argval:>20}")
        else:
            print(f"  {k:>3}  (all zero or infinite)")


if __name__ == "__main__":
    print("=" * 70)
    print("c = 6 term-wise min v_2 of h_k")
    print("=" * 70)
    termwise_min_v2(h_c6, 10, 6)

    print("\n" + "=" * 70)
    print("c = 7 term-wise min v_2 of h_k")
    print("=" * 70)
    termwise_min_v2(h_c7, 12, 7)
