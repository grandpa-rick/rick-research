"""Systematically search for a closed form for K_even(l, r) = K_{(2l, l+1+r, l+1-r)', (2^{2l+1})}."""

from math import comb
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
from kostka import kostka_mu_prime_2j


def K_even(l, r):
    mu = (2*l, l+1+r, l+1-r)
    return kostka_mu_prime_2j(mu)


def try_formulas():
    """Try various closed forms."""
    print("l  r   K   |  candidates")
    print("-" * 80)
    for l in range(1, 8):
        for r in range(l):
            K = K_even(l, r)
            n = 2*l+1  # or 2l+2
            # Various ideas:
            # 1) Difference of two ballot numbers with skipped label sum
            # 2) K = Sum_{s} something(l, r, s), where s is the skipped label 0..2l
            # 3) LGV determinant: 2x2 det of binomials

            # LGV: K_{mu', (1^n)} = f^{mu'} but for content (2^j) we can use Jacobi-Trudi in e:
            # s_mu = det(e_{mu'_i - i + j}). Then [s_mu] e_2^j: via evaluating on power sums.
            # Frobenius: K_{mu', (2^j)} = coefficient of s_mu in e_2^j
            #  = <e_2^j, s_mu> = <p_?, s_mu> ... but easier: K_{mu', (2^j)} = # ways to fill mu' with content 2^j.
            # For mu with 3 parts: use JT with column-conjugate: K_{mu', nu} = sum_{sigma} sign(sigma) e_{...}
            # There's an explicit formula:
            #   K_{lambda, (2^n)} = C_lambda where C is a determinant of binomials.

            # For lambda = mu' with mu = (m1, m2, m3), lambda has mu_1 = m1 parts,
            # each of size <= 3. It's tricky.

            # Alternative: use Kostka via Weyl formula.
            # K_{lambda, (2^n)} = # SSYT lambda with content (2, 2, ..., 2)
            # = coefficient formula...

            # Let's try a specific guess based on shape: since mu has 3 parts and
            # content is (2^n) with n = 2l+1, we can use:
            # K_{mu', (2^n)} = det[C(2, mu'_j - j + i)]_{i,j=1}^{ell(mu')}? No that's the wrong direction.

            # Jacobi-Trudi in e:
            #   s_mu = det(e_{mu'_i - i + j})_{i,j}
            # We have mu' of length mu_1 = m1. This gives mu_1 x mu_1 determinant. Too big.

            # Column JT: s_mu = det(h_{mu_i - i + j})_{i,j=1}^{len(mu)} (row JT)
            # For 3-part mu: s_mu = det [h_{m1}, h_{m1+1}, h_{m1+2}; h_{m2-1}, h_{m2}, h_{m2+1}; h_{m3-2}, h_{m3-1}, h_{m3}]
            # Then K_{mu', (2^j)} = <e_2^j, s_mu> = sum ... complex.

            # Simpler try:
            # Attempt: K_even(l, r) = 2 * ballot(2l+1, l-r) * (something)
            # Or use the Naruse "shifted" formula.

            # Try systematic: K = a*C(2l+1, l-r) + b*C(2l+1, l-r-1) + c*C(2l+1, l-r-2)
            # for some coefficients a, b, c depending only on l, r.
            row = (K, comb(2*l+1, l-r), comb(2*l+1, l-r-1) if l-r-1 >= 0 else 0, comb(2*l+1, l-r+1) if l-r+1 <= 2*l+1 else 0)
            print(f"{l} {r}  {K:5}  |  C(2l+1,l-r)={row[1]}, C(2l+1,l-r-1)={row[2]}, C(2l+1,l-r+1)={row[3]}")


def find_formula_via_solving():
    """Set up linear system: K = alpha1 * C(n, l-r) + alpha2 * C(n, l-r-1) + alpha3 * C(n, l-r-2)
    with n = 2l+1 or 2l+2 and (l-r) shifted."""
    print("\n=== Solving for coefficients ===\n")
    import numpy as np
    # For fixed l, try to fit K(r) as combination of ballot-type basis:
    for l in range(3, 8):
        n = 2*l+1
        R = list(range(l))
        Ks = [K_even(l, r) for r in R]
        # Basis: C(n, l-r-k) for various k
        basis_names = []
        basis_vals = []
        for k in [-2, -1, 0, 1, 2, 3]:
            vals = [comb(n, l - r - k) if 0 <= l-r-k <= n else 0 for r in R]
            basis_names.append(f'C({n},l-r-{k})')
            basis_vals.append(vals)
        M = np.array(basis_vals).T  # rows = r, cols = basis
        b = np.array(Ks)
        # try to find sparse solution
        try:
            sol, res, rank, sv = np.linalg.lstsq(M, b, rcond=None)
            recon = M @ sol
            err = np.max(np.abs(recon - b))
            print(f"l={l}: lsq solution: {[(basis_names[i], round(sol[i], 3)) for i in range(len(sol))]}, err={err}")
        except Exception as e:
            print(f"l={l}: error: {e}")


def try_two_binom_diff():
    """Look for K = alpha*C(A,B) - beta*C(A,B') where A, B, B' depend on (l, r).
    Try many (A, B, B') triples."""
    print("\n=== Look for K = C(A, B) - C(A, C) type formula ===\n")
    good = []
    for l in range(2, 7):
        for r in range(l):
            K = K_even(l, r)
            found = False
            for A in [2*l+1, 2*l+2, 2*l+3, 2*l]:
                for B in range(A+1):
                    for C_ in range(A+1):
                        val = comb(A, B) - comb(A, C_)
                        if val == K:
                            good.append((l, r, K, A, B, C_))
                            found = True
                            break
                    if found: break
                if found: break
    for g in good[:30]:
        l, r, K, A, B, C_ = g
        print(f"  l={l}, r={r}: K={K} = C({A}, {B}) - C({A}, {C_}) [B-l+r={B-l+r}, C-l+r={C_-l+r}]")


if __name__ == "__main__":
    try_formulas()
    find_formula_via_solving()
    try_two_binom_diff()
