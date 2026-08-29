"""
TEST 4: P-recursive search.
Search for a linear recurrence
  sum_{i=0..order} p_i(k) b_{k+i} = 0
where p_i are polynomials in k of degree <= deg.

Also nonlinear: search for a convolution-type recurrence like
  b_{k+1} = (1/k) sum_j f(j,k) b_j b_{k-j+1}
"""
from sympy import Rational, Symbol, Matrix, zeros, Poly

b = [3, 27, 417, 7851, 164124, 3661389, 85384566]  # b_1..b_7

def search_precursive(seq, order, deg):
    """
    Search: sum_{i=0..order} sum_{j=0..deg} c_{i,j} · k^j · seq[k+i] = 0
    where k ranges over available indices.
    seq is 0-indexed; positions correspond to b_1, b_2, ...
    """
    n_unknowns = (order+1) * (deg+1)
    # Available k such that k+order+1 <= len(seq): k from 1 to len(seq)-order (index k-1)
    max_idx = len(seq) - order - 1  # last valid k-1 index
    n_eqs = max_idx + 1  # k = 1..max_idx+1 (or in indexed form: 0..max_idx)
    if n_eqs < n_unknowns:
        return None, "not enough equations"
    # Build matrix
    rows = []
    for kidx in range(n_eqs):
        k_val = kidx + 1  # actual k
        row = []
        for i in range(order+1):
            for j in range(deg+1):
                # b_{k+i} is seq at index (k+i)-1 = kidx + i
                row.append(Rational(k_val)**j * Rational(seq[kidx + i]))
        rows.append(row)
    M = Matrix(rows)
    ns = M.nullspace()
    return ns, None

print("=== P-recursive search on b_k ===")
found_any = False
for order in range(1, 5):
    for deg in range(0, 5):
        ns, err = search_precursive(b, order, deg)
        if err:
            continue
        if ns:
            # Report nontrivial recurrences
            for sol in ns:
                # Print as recurrence
                print(f"Order {order}, degree {deg}: null vector found:")
                idx = 0
                for i in range(order+1):
                    for j in range(deg+1):
                        coef = sol[idx]
                        if coef != 0:
                            print(f"    p_{i}(k) has k^{j} coefficient {coef}")
                        idx += 1
                found_any = True
                print()

if not found_any:
    print("No P-recursive recurrence found within (order<=4, degree<=4).")

# Try higher order/degree, just for completeness:
print("\n=== Higher-order attempt (order 3, deg 3) — needs 16 unknowns but only 4 equations ===")
# Not enough data actually. Let's see max feasible.
# Data: 7 terms. For order=r, we get 7-r equations (k=1..7-r). Unknowns: (r+1)(d+1).
# Need (r+1)(d+1) <= 7-r. Feasible (r,d):
print("Feasible (order, deg) with equations >= unknowns:")
for order in range(1, 7):
    for deg in range(0, 7):
        n_eqs = 7 - order
        n_unk = (order+1)*(deg+1)
        if n_eqs >= n_unk:
            print(f"  order={order}, deg={deg}: {n_eqs} eqs, {n_unk} unknowns")

# The best guarantee is (order=1, deg=2): 6 eqs, 6 unknowns — that's already tight.
# Basically no room. Report what we found.
