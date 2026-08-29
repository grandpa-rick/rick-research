"""Day 124 KEY EXPERIMENT: verify that Pi* preserves (1,1,2)-filtration
MONOMIAL BY MONOMIAL.

If TRUE: Lemma 2 (Filtration Preservation for Psi) is trivial by linearity,
and the entire Main Conjecture reduces to a per-monomial statement about Pi*
in the e-basis. That would be a HUGE simplification.

Test hypothesis: for every e-monomial m = e_1^a1 e_2^a2 e_3^a3,
  weight(Pi*(m)) = weight(m) + 1.

Test for all monomials with u-degree up to N (larger than day123 tested).
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day124')

from pi_star_on_monomials import build_pi_star_matrix, weight_112_tuple

def main():
    for N in [4, 6, 8, 10]:
        print(f'\n\n===== Testing all e-monomials with u-degree <= {N} =====')
        input_monoms, pi_star = build_pi_star_matrix(N)
        all_ok = True
        strict = []  # weight increase < 1
        equal_bound = []  # weight increase = 1 (expected)
        exceeds = []  # weight increase > 1 (BAD)
        for m in input_monoms:
            w_in = weight_112_tuple(m)
            image = pi_star[m]
            w_out = max([weight_112_tuple(k) for k in image.keys()], default=-1)
            diff = w_out - w_in
            if diff > 1:
                exceeds.append((m, w_in, w_out))
                all_ok = False
            elif diff == 1:
                equal_bound.append((m, w_in, w_out))
            else:
                strict.append((m, w_in, w_out))
        print(f'  Total monomials: {len(input_monoms)}')
        print(f'  Weight increase = 1 (as hypothesized): {len(equal_bound)}')
        print(f'  Weight increase < 1: {len(strict)}')
        print(f'  Weight increase > 1 (VIOLATION!): {len(exceeds)}')
        if strict:
            print(f'  Strictly less cases:')
            for m, w_in, w_out in strict[:20]:
                print(f'    m = {m}: w_in={w_in}, w_out={w_out}')
        if exceeds:
            print(f'  VIOLATION cases:')
            for m, w_in, w_out in exceeds[:20]:
                print(f'    m = {m}: w_in={w_in}, w_out={w_out}')
        print(f'  Overall: {"CONJECTURE HOLDS" if all_ok else "!!!!!!! FAIL !!!!!!!"}')


if __name__ == '__main__':
    main()
