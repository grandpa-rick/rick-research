"""Day 124: Find explicit formula for top_w(Psi(e_1^a e_2^b e_3^c)).

Empirical observations from previous run:
- Psi(e_1^a) top = e_1^a (identity on pure e_1 monomials)
- Psi(e_3^c) top = e_3^c (identity on pure e_3 monomials)
- Psi(e_1^a e_3^c) top = e_1^a e_3^c
- Psi(e_1^a e_2 e_3^c) top = e_1^a e_2 e_3^c - (2c + 1) e_1^{a+1} e_3^c

So the KEY nontrivial computation is Psi(e_2^b e_3^c). Once we understand that,
Psi(e_1^a e_2^b e_3^c) top = e_1^a Psi(e_2^b e_3^c) top.

Let's compute top_w(Psi(e_2^b e_3^c)) for various (b, c).

We already saw:
  Psi(e_2) top = -e_1 + e_2
  Psi(e_2^2) top = 2 e_1^2 - 3 e_1 e_2 + e_2^2 - 3 e_3
  Psi(e_2^3) top = -6 e_1^3 + 11 e_1^2 e_2 - 6 e_1 e_2^2 + 25 e_1 e_3 + e_2^3 - 9 e_2 e_3
  Psi(e_2^4) top = 24 e_1^4 - 50 e_1^3 e_2 + 35 e_1^2 e_2^2 - 190 e_1^2 e_3 - 10 e_1 e_2^3 + 118 e_1 e_2 e_3 + e_2^4 - 18 e_2^2 e_3 + 27 e_3^2

Pattern for Psi(e_2^b) at top (weight = b):
  e_2^b + (b-choose-1) sign * some * e_1 e_2^{b-1} + ... etc.

Look at coefficient of e_2^{b-1} e_1: -1, -3, -6, -10 = -(b choose 2)?
  b=1: -1 = -(1 choose 2)? = 0 or -1? 1 choose 2 = 0. Not matching.
  b=2: -3
  b=3: -6, but wait we have 11 for e_1^2 e_2 not -6. Let me re-read:
  Psi(e_2^3) = -6 e_1^3 + 11 e_1^2 e_2 - 6 e_1 e_2^2 + ...
  So coeff of e_1 e_2^2 is -6 = -6.
  Psi(e_2^4) = ... - 10 e_1 e_2^3 + ...  So coeff of e_1 e_2^{b-1} in Psi(e_2^b):
    b=1: -1
    b=2: -3
    b=3: -6
    b=4: -10
  These are -(b+1) choose 2 = -b(b+1)/2? b=1: -1=-1. b=2: -3=-3. b=3: -6=-6. b=4: -10=-10. YES!

  Or negative triangular numbers: -T_b = -b(b+1)/2.

  Or: -1, -3, -6, -10 = -sum_{i=1}^{b} i. So coeff = -T_b.

Hmm, let me try: Psi(e_2)^b (Newton binomial)?
  (e_2 - e_1)^b at leading = e_2^b - b e_1 e_2^{b-1} + ...
  Coeff of e_1 e_2^{b-1} is -b. But actual is -T_b = -b(b+1)/2. Not matching.

Consider: Psi(e_2^b) = e_2^b - T_b e_1 e_2^{b-1} + ... this is like a
"deformed binomial" or convolution with triangular numbers.

Alternative: consider top_w(Psi(e_2^b)) as generating function.
Let f_b(x) = coeff of e_2^{b-k} e_1^k in top(Psi(e_2^b))  (fix c = 0).

Or think representation-theoretically. Recall in shifted symmetric world:
  E_j = sum_mu K_{mu', (2^j)} s*_mu (Rick's E_j).
  E_j top weight (1,1,2) = j (equals top weight of Psi(e_2^j) since Psi is filtration
  preserving and e_2^j has weight j).

So finding a formula for top_w(Psi(e_2^b)) gives an EXPLICIT formula for the
top part of E_j (though E_j itself is more complex due to lower-weight contributions).

Test: is top_w(Psi(e_2^b)) simply e_2^b MINUS the top parts of specific
elements we can identify?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Symbol, factor, simplify

from psi_filtration_test import build_psi_matrix, compute_psi
from pi_star_on_monomials import weight_112_tuple, dict_to_poly

e1, e2, e3 = symbols('e1 e2 e3')


def top_weight_part(f_dict, w):
    return {m: c for m, c in f_dict.items() if weight_112_tuple(m) == w}


def main():
    # Build up to N = 12 to get lots of data
    N = 10
    print(f'Building Psi matrix for N = {N}...')
    monoms, monom_idx, partitions, M_ord, M_star = build_psi_matrix(N)
    print('Done.')

    def Psi(m):
        f_dict = {m: Integer(1)}
        psi = compute_psi(f_dict, monoms, monom_idx, partitions, M_ord, M_star)
        return psi

    def top_of_psi(m):
        w = weight_112_tuple(m)
        psi = Psi(m)
        top = top_weight_part(psi, w)
        return dict_to_poly(top)

    print()
    print('=' * 70)
    print('Top(Psi(e_2^b e_3^c)) for various (b, c):')
    print('=' * 70)
    for c in range(0, 3):
        print(f'\n  c = {c}:')
        for b in range(0, 5):
            # e_2^b e_3^c: weight = b + 2c
            if b + 2*c > N:
                continue
            m = (0, b, c)
            top = top_of_psi(m)
            print(f'    b = {b}: top(Psi(e_2^{b} e_3^{c})) = {top}')

    # Look for a pattern in (b, c) - specifically the coefficients.
    # Conjecture (test): top_w(Psi(e_2^b e_3^c)) is a POLYNOMIAL in some
    # "shifted" combination.
    print()
    print('=' * 70)
    print('Look at ratio top(Psi(e_2^b e_3)) / e_3 vs top(Psi(e_2^b)):')
    print('=' * 70)
    for b in range(0, 4):
        if b + 2 > N:
            continue
        m_c = (0, b, 1)
        m_nc = (0, b, 0)
        top_c = top_of_psi(m_c)
        top_nc = top_of_psi(m_nc)
        # top_c should be divisible by e_3
        try:
            quo = expand(top_c / e3)
            quo = expand(quo * e3 - top_c)
            # cleaner: just polynomial division by e_3
            q_poly, r_poly = sp.div(sp.Poly(top_c, e3), sp.Poly(e3, e3))
            q = q_poly.as_expr()
            r = r_poly.as_expr()
            if r != 0:
                print(f'  b={b}: top(Psi(e_2^{b} e_3))/e_3 has remainder {r}')
            else:
                # Compare q with top_nc
                diff = expand(q - top_nc)
                print(f'  b={b}: top(Psi(e_2^{b}))/1 = {top_nc}')
                print(f'         top(Psi(e_2^{b} e_3))/e_3 = {q}')
                print(f'         diff (of e_3 factor part) = {diff}')
        except Exception as ex:
            print(f'  b={b}: error {ex}')


if __name__ == '__main__':
    main()
