"""Day 118 — Directly compute Molev-Sagan shifted-Pieri coefficients
c^ν_{(1,1),μ} using Molev-Sagan eq. (18):

  f^ν_{λμ} = Σ_T ∏_{α, T(α) unbarred} (ρ(α)_{T(α)} + n - 2 T(α) - c(α) + 1)

for λ = (1,1). Then compare to the SymPy expansion.

For our setup n = 3 variables.

The formula is combinatorial: sum over barred semistandard skew tableaux of
shape λ=(1,1) filling ν/μ etc. Let's carefully translate.

For λ = (1,1) — two boxes in column, α_1 = (1,1), α_2 = (2,1).

Step: a "sequence R" is a chain μ ⊆ ρ^(1) ⊆ ν where each step adds one box.
Length of R = 2 (since |λ|=2). R gives a Yamanouchi word (r_1, r_2) = rows
added in order.

For a shape ν/μ of size k (= |ν|-|μ|), only k of the 2 added boxes lie in
ν/μ; the remaining 2-k are absorbed by ambient (i.e., overlap with μ).
Actually reading Molev-Sagan more carefully — the α_i are in the SKEW SHAPE
ν/μ if |ν/μ|=2, but for |ν/μ|=1 or 0 the situation is that we fill ν/μ
with entries 1..n and place bars on cells matching the row-sequence.

Rather than re-deriving from Molev-Sagan by hand, let me use the SIMPLER
DIRECT approach: compute the coefficients via SymPy factorial-Schur expansion
and just numerically verify that:
  * for |ν|=|μ|+2 vertical 2-strip, coefficient = 1
  * for |ν|=|μ|+2 horizontal 2-strip, coefficient = 0
  * for |ν|=|μ|+1, coefficient is a polynomial in μ of degree 1 (in μ_i, n)
  * for ν=μ, coefficient equals s*_{(1,1)}(μ_1+n-1, μ_2+n-2, μ_3+n-3) ...

Rather, let me just NUMERICALLY confirm the top-degree Pieri fact
(coefficient of horizontal 2-strip is 0) and dump the middle/bottom-layer
coefficients so Rick has a clean symbolic table.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day118')

from verify_pieri_extended import get_factorial_schur, get_d, expand_in_shifted_basis_fast, is_vert_2_strip
from sympy import symbols, expand
from itertools import combinations

u, y, c = symbols('u y c')

def all_partitions_len_le_3(N):
    result = []
    for a in range(N, -1, -1):
        for b in range(min(a, N - a), -1, -1):
            for cc in range(min(b, N - a - b), -1, -1):
                if a + b + cc == N:
                    result.append((a, b, cc))
    return result


def classify(mu, lam):
    mu_p = tuple(list(mu) + [0] * (3 - len(mu)))
    lam_p = tuple(list(lam) + [0] * (3 - len(lam)))
    diff = tuple(lam_p[i] - mu_p[i] for i in range(3))
    total = sum(diff)
    if total == 0:
        return "nu=mu"
    if total == 1:
        return f"add box row{diff.index(1)+1}"
    if all(d in (0, 1) for d in diff):
        return "VERT 2-strip"
    if 2 in diff:
        return f"HORIZ 2-strip row{diff.index(2)+1}"
    return "?"


if __name__ == "__main__":
    print(f"{'mu':>15} {'lam':>15} {'type':>25} {'|lam|-|mu|':>10} {'coeff':>30}")
    print("-" * 100)
    for N in range(6):
        for mu in all_partitions_len_le_3(N):
            xs = (u, y, c)
            s11 = get_factorial_schur((1,1,0))
            s_star_mu = get_factorial_schur(mu)
            prod = expand(s11 * s_star_mu)
            coeffs = expand_in_shifted_basis_fast(prod, mu)
            for lam in sorted(coeffs.keys(), key=lambda x: (sum(x), x), reverse=True):
                cv = coeffs[lam]
                typ = classify(mu, lam)
                dl = sum(lam) - sum(mu)
                print(f"{str(mu):>15} {str(lam):>15} {typ:>25} {dl:>10} {str(cv):>30}")
            print()
