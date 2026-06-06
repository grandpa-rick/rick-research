"""Phase 2: check the q=0 limit of (ALG) on lower crystal lattice.

Concrete observation: in V(4) on v_3 (an on-slice element for k=2, since varepsilon=3 >= 2),
the algebra-level commutator [E^(2), B] v_3 has poles at q=0 in the lower crystal basis.
So the naive q->0 limit does NOT reproduce crystal-level [tilde-e^k, tilde-f] = 0 on slice.

This phase documents the failure mode and the structural reason.
"""

import sympy as sp
from phase1_verify import (qnum, qfact, qbinom,
                            E_action, F_action, Kinv_action, Edivk_action,
                            commutator_EkB_on_vr, add, sub, scale)

q = sp.Symbol('q')
zeta = sp.Symbol('zeta')

def show(d, k):
    print(f"\n=== V(d={d}), k={k} ===")
    for r in range(d+1):
        mu = d - 2*r
        eps = r
        phi = d - r
        slice_status = "on-slice" if eps >= k else ("boundary off-slice" if eps == k-1 else "deep off-slice")
        comm = commutator_EkB_on_vr(k, r, d)
        comm_simp = [sp.simplify(sp.together(c)) for c in comm]
        # Reduce mod q to see q=0 behavior — but if there are poles, we just print the expression.
        coeffs_str = []
        for j, c in enumerate(comm_simp):
            if c != 0:
                coeffs_str.append(f"v_{j}: {c}")
        result_str = "  +  ".join(coeffs_str) if coeffs_str else "0"
        print(f"  v_{r} (eps={eps}, phi={phi}, mu={mu}, {slice_status}):")
        print(f"    [E^(k), B] v_{r} = {result_str}")

if __name__ == "__main__":
    print("Tracking [E^(k), B] v_r in lower crystal basis of V(d).")
    print("Key observation: 'on-slice' elements (eps >= k) should crystal-level commute,")
    print("but algebra-level computation gives poles at q=0.")
    show(4, 2)
    show(6, 3)
