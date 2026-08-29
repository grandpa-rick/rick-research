"""Day 128 — Empirical test of d_{s*_μ} = d_{s_μ} at length ℓ(μ) = 4.

Rick proved this identity for ℓ(μ) ≤ 3 on Day 127. Before extending to ℓ = 4,
we test whether it even HOLDS at ℓ = 4.

Setup:
  d_λ = λ_1 + ⌊(|λ| - λ_1)/2⌋            (shape-degree)
  s_μ = ordinary Schur polynomial in N = 4 variables
  s*_μ = Okounkov-Olshanski shifted Schur polynomial
  d_{s_μ}   = d_μ
  d_{s*_μ}  = max_{λ : c^μ_λ ≠ 0} d_λ, where s*_μ = Σ c^μ_λ s_λ

The classical determinant formula (in N variables):
  s*_μ(x_1,...,x_N) = det[ (x_i + N - i)_{μ_j + N - j} ] / V(x)
where (a)_k = a(a-1)...(a-k+1) is the falling factorial and
V(x) = det[x_i^{N-j}] = Π_{i<j} (x_i - x_j).

We compute s*_μ symbolically in ℚ[x_1,...,x_4], then expand in Schur basis
by matching the antisymmetrised numerator against the Vandermonde-times-Schur
determinant identity: s_λ = det[x_i^{λ_j + N - j}] / V(x).

Equivalently, the numerator det[(x_i + N - i)_{μ_j + N - j}] is antisymmetric
under x-permutations, hence a Z-linear combination of a_δ = det[x_i^{α_j}] with
α_1 > α_2 > ... > α_N ≥ 0. Writing α_j = λ_j + N - j recovers λ.

Test partitions (all length 4):
  μ = (2,1,1,1)      predicted d_μ = 3
  μ = (2,2,1,1)      predicted d_μ = 4
  μ = (3,1,1,1)      predicted d_μ = 4
  μ = (2,2,2,1)      predicted d_μ = 4  (maximally degenerate)
"""
from sympy import symbols, expand, Poly, Rational, Integer, S
from itertools import permutations

N = 4
x = symbols('x1 x2 x3 x4')


def falling(a, k):
    """Falling factorial a(a-1)...(a-k+1)."""
    p = S.One
    for i in range(k):
        p *= (a - i)
    return expand(p)


def shifted_schur_numerator(mu):
    """Compute the antisymmetric numerator
       det[ (x_i + N - i)_{mu_j + N - j} ]
    as a polynomial in x_1,...,x_N.
    """
    # Pad mu to length N with zeros
    mu_p = list(mu) + [0] * (N - len(mu))
    assert len(mu_p) == N
    exps = [mu_p[j] + N - (j + 1) for j in range(N)]  # μ_j + N - j (1-indexed j)

    # Determinant expansion
    result = S.Zero
    for perm in permutations(range(N)):
        sign = 1
        for i in range(N):
            for j in range(i + 1, N):
                if perm[i] > perm[j]:
                    sign *= -1
        term = S.One
        for i in range(N):
            j = perm[i]
            # entry M_{ij} = (x_i + N - (i+1))_{exps[j]}
            term *= falling(x[i] + N - (i + 1), exps[j])
        result += sign * term
    return expand(result)


def extract_a_alpha_coeffs(P):
    """Given an antisymmetric polynomial P in x_1,...,x_N, decompose as
       P = Σ_{α_1 > α_2 > ... > α_N ≥ 0} c_α · a_α
    where a_α = det[x_i^{α_j}]. Return dict α -> c_α (nonzero only).

    Method: for any monomial x_1^{a_1} ... x_N^{a_N} with all a_i distinct, its
    contribution to the antisymmetriser is sign(sort) · a_{sort desc}. So we
    collect monomial coefficients where a_1 > a_2 > ... > a_N (these are the
    'leading' representatives) directly.
    """
    P = expand(P)
    poly = Poly(P, *x)
    coeffs = {}
    for monom, coef in poly.as_dict().items():
        # monom is (a1, a2, ..., aN)
        if all(monom[i] > monom[i + 1] for i in range(N - 1)):
            coeffs[monom] = coef
    return coeffs


def alpha_to_lambda(alpha):
    """Convert strict α = (α_1 > ... > α_N) to partition λ where α_j = λ_j + N - j."""
    lam = tuple(alpha[j] - (N - (j + 1)) for j in range(N))
    return lam


def d_shape(lam):
    """d_λ = λ_1 + ⌊(|λ| - λ_1)/2⌋. Uses λ_1 = max part (i.e. first entry after
       stripping trailing zeros, which is lam[0] for a partition)."""
    # Strip trailing zeros
    while lam and lam[-1] == 0:
        lam = lam[:-1]
    if not lam:
        return 0  # empty partition, |λ|=0, λ_1 = 0 -> d = 0
    lam1 = lam[0]
    absl = sum(lam)
    return lam1 + (absl - lam1) // 2


def shifted_schur_expansion(mu):
    """Compute s*_μ = Σ c^μ_λ s_λ. Returns dict λ -> c^μ_λ (nonzero)."""
    num = shifted_schur_numerator(mu)
    alpha_coeffs = extract_a_alpha_coeffs(num)
    lam_coeffs = {}
    for alpha, c in alpha_coeffs.items():
        lam = alpha_to_lambda(alpha)
        # α strictly decreasing ⇒ λ is a (weak) partition; drop trailing zeros for display
        # Sanity: λ_i ≥ λ_{i+1} since α_i - (N-i) > α_{i+1} - (N-i-1) - 1 iff
        # α_i - α_{i+1} > 0 which is given.
        if c != 0:
            lam_coeffs[lam] = c
    return lam_coeffs


def display_lam(lam):
    """Strip trailing zeros for display."""
    lam = list(lam)
    while lam and lam[-1] == 0:
        lam.pop()
    return tuple(lam)


def run_tests():
    tests = [
        ((2, 1, 1, 1), 3),
        ((2, 2, 1, 1), 4),
        ((3, 1, 1, 1), 4),
        ((2, 2, 2, 1), 4),
    ]

    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    out("=" * 100)
    out(" Day 128 — ℓ=4 empirical test of d_{s*_μ} = d_{s_μ}")
    out("=" * 100)
    out(f" Working in N = {N} variables. Formulae as documented in module docstring.")
    out("")

    summary_rows = []
    all_pass = True

    for mu, pred in tests:
        out(f"μ = {mu}   predicted d_μ = {pred}")
        exp = shifted_schur_expansion(mu)

        # Build list of (λ_display, coef, d_λ, |λ|, λ_1)
        entries = []
        for lam, c in exp.items():
            lam_d = display_lam(lam)
            dl = d_shape(lam_d)
            entries.append((lam_d, c, dl, sum(lam_d), lam_d[0] if lam_d else 0))

        # Sort by d_λ descending, then |λ| descending
        entries.sort(key=lambda e: (-e[2], -e[3], e[0]))

        max_d = max((e[2] for e in entries), default=-1)
        max_lam1 = max((e[4] for e in entries), default=-1)
        max_size = max((e[3] for e in entries), default=-1)

        # Combinatorial upper-bound check
        mu_size = sum(mu)
        mu1 = mu[0]
        bound_ok = all(e[4] <= mu1 and e[3] <= mu_size for e in entries)

        for lam_d, c, dl, sz, l1 in entries:
            out(f"    λ = {str(lam_d):20s}  c = {str(c):>8s}   d_λ = {dl}   |λ|={sz}, λ_1={l1}")

        status = "PASS" if max_d == pred else "FAIL"
        if max_d != pred:
            all_pass = False
        out(f"  ⇒ d_{{s*_μ}} = {max_d}  (predicted {pred})   [{status}]")
        out(f"  ⇒ combinatorial bound  λ_1 ≤ μ_1 and |λ| ≤ |μ|:  "
            f"max λ_1 = {max_lam1} (≤ {mu1}?), max |λ| = {max_size} (≤ {mu_size}?)  "
            f"[{'OK' if bound_ok else 'VIOLATED'}]")
        out("")

        summary_rows.append((mu, pred, max_d, entries, status, bound_ok))

    # Summary table
    out("=" * 100)
    out(" SUMMARY TABLE")
    out("=" * 100)
    out(f" {'μ':<15} | {'pred d_μ':>8} | {'actual d_{s*_μ}':>16} | {'bound':>6} | {'status':>6}")
    out(" " + "-" * 70)
    for mu, pred, actual, entries, status, bound_ok in summary_rows:
        out(f" {str(mu):<15} | {pred:>8} | {actual:>16} | {'OK' if bound_ok else 'BAD':>6} | {status:>6}")
    out("")

    # Detailed FAIL reports
    for mu, pred, actual, entries, status, bound_ok in summary_rows:
        if status == "FAIL":
            out(f"  FAILURE at μ = {mu}:")
            out(f"    predicted d_μ = {pred}, actual d_{{s*_μ}} = {actual}")
            for lam_d, c, dl, sz, l1 in entries:
                if dl > pred:
                    out(f"    Witness λ = {lam_d} achieves d_λ = {dl} > {pred},  c^μ_λ = {c}")
            out("")

    if all_pass:
        out("VERDICT: all 4 test partitions PASS. Identity d_{s*_μ} = d_{s_μ} holds at ℓ=4 "
            "for these cases.")
    else:
        out("VERDICT: at least one FAIL. Identity does NOT extend uniformly to ℓ=4.")

    # Write output file
    txt_path = "/home/agent/projects/beta-prime/code/day128/l4_test.txt"
    with open(txt_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\n[wrote {txt_path}]")


if __name__ == "__main__":
    run_tests()
