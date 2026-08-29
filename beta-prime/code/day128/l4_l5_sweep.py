"""Day 128 — Sweep: d_{s*_μ} = d_{s_μ} for ALL length-4 μ with |μ| ≤ 12,
   and bonus sweep for ℓ(μ) = 5 with |μ| ≤ 10.

Conventions (from Rick):
  d_λ = λ_1 + ⌊(|λ| - λ_1)/2⌋
  s*_μ(x_1,...,x_N) = det[(x_i + N − i)_{μ_j + N − j}] / V(x)
  d_{s*_μ} = max_λ d_λ over λ with c^μ_λ ≠ 0 in Schur expansion s*_μ = Σ c^μ_λ s_λ.
For ℓ(μ) = k we use N = k variables.

Extends /home/agent/projects/beta-prime/code/day128/l4_test.py.
"""
from sympy import symbols, expand, Poly, S
from itertools import permutations


def falling(a, k):
    p = S.One
    for i in range(k):
        p *= (a - i)
    return expand(p)


def shifted_schur_numerator(mu, N, x):
    """det[ (x_i + N - i)_{mu_j + N - j} ] in N variables."""
    mu_p = list(mu) + [0] * (N - len(mu))
    assert len(mu_p) == N
    exps = [mu_p[j] + N - (j + 1) for j in range(N)]

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
            term *= falling(x[i] + N - (i + 1), exps[j])
        result += sign * term
    return expand(result)


def extract_a_alpha_coeffs(P, N, x):
    """Collect coefficients of a_α = det[x_i^{α_j}] via monomials with
       strictly decreasing exponents."""
    P = expand(P)
    poly = Poly(P, *x)
    coeffs = {}
    for monom, coef in poly.as_dict().items():
        if all(monom[i] > monom[i + 1] for i in range(N - 1)):
            coeffs[monom] = coef
    return coeffs


def alpha_to_lambda(alpha, N):
    return tuple(alpha[j] - (N - (j + 1)) for j in range(N))


def d_shape(lam):
    lam = list(lam)
    while lam and lam[-1] == 0:
        lam.pop()
    if not lam:
        return 0
    lam1 = lam[0]
    absl = sum(lam)
    return lam1 + (absl - lam1) // 2


def shifted_schur_expansion(mu, N, x):
    num = shifted_schur_numerator(mu, N, x)
    alpha_coeffs = extract_a_alpha_coeffs(num, N, x)
    lam_coeffs = {}
    for alpha, c in alpha_coeffs.items():
        lam = alpha_to_lambda(alpha, N)
        if c != 0:
            lam_coeffs[lam] = c
    return lam_coeffs


def display_lam(lam):
    lam = list(lam)
    while lam and lam[-1] == 0:
        lam.pop()
    return tuple(lam)


def partitions_of_length_exactly(k, max_size):
    """All partitions with exactly k nonzero parts and |μ| ≤ max_size.
       Yields μ as a tuple of length k, weakly decreasing, all parts ≥ 1."""
    def gen(k_left, max_part, size_left):
        if k_left == 0:
            if size_left >= 0:
                yield ()
            return
        # We need k_left more parts, each ≥ 1 and ≤ max_part, summing ≤ size_left.
        # Also need remaining k_left parts to fit: min sum = k_left (all 1's).
        if size_left < k_left:
            return
        lo = 1
        hi = min(max_part, size_left - (k_left - 1))
        for p in range(hi, lo - 1, -1):
            for rest in gen(k_left - 1, p, size_left - p):
                yield (p,) + rest
    for n in range(k, max_size + 1):
        for mu in gen(k, n, n):
            if sum(mu) == n:
                yield mu


def sweep(length, max_size, out_lines):
    N = length
    x = symbols(' '.join(f'x{i+1}' for i in range(N)))
    if N == 1:
        x = (x,)

    def out(s=""):
        print(s)
        out_lines.append(s)

    out("=" * 100)
    out(f" SWEEP ℓ(μ) = {length},  |μ| ≤ {max_size},  N = {N} variables")
    out("=" * 100)

    all_mus = list(partitions_of_length_exactly(length, max_size))
    total = len(all_mus)
    passes = 0
    fails = []
    bound_violations = []

    for mu in all_mus:
        pred = d_shape(mu)
        exp = shifted_schur_expansion(mu, N, x)

        # Collect (λ, c, d_λ, |λ|, λ_1)
        entries = []
        for lam, c in exp.items():
            lam_d = display_lam(lam)
            dl = d_shape(lam_d)
            sz = sum(lam_d)
            l1 = lam_d[0] if lam_d else 0
            entries.append((lam_d, c, dl, sz, l1))

        max_d = max((e[2] for e in entries), default=-1)
        mu_size = sum(mu)
        mu1 = mu[0]

        # Bound check per-λ
        local_violations = [e for e in entries if not (e[4] <= mu1 and e[3] <= mu_size)]
        if local_violations:
            bound_violations.append((mu, local_violations))

        if max_d == pred:
            passes += 1
        else:
            offenders = [e for e in entries if e[2] > pred]
            fails.append((mu, pred, max_d, offenders, entries))

    out(f" Total tested: {total}")
    out(f" PASS: {passes}")
    out(f" FAIL: {len(fails)}")
    out(f" Bound violations: {len(bound_violations)}")
    out("")

    if fails:
        out(" -- FAILURE DETAILS --")
        for mu, pred, actual, offenders, entries in fails:
            out(f"  μ = {mu}   predicted d_μ = {pred}   actual d_{{s*_μ}} = {actual}")
            for lam_d, c, dl, sz, l1 in offenders:
                out(f"    OFFENDING λ = {lam_d}   c^μ_λ = {c}   d_λ = {dl} (> {pred})")
            out("")
    else:
        out(" No failures.")

    if bound_violations:
        out(" -- BOUND VIOLATION DETAILS --")
        for mu, viols in bound_violations:
            for lam_d, c, dl, sz, l1 in viols:
                out(f"  μ = {mu}   λ = {lam_d}   c = {c}   |λ|={sz} vs |μ|={sum(mu)},"
                    f"   λ_1={l1} vs μ_1={mu[0]}")
        out("")
    else:
        out(" No combinatorial bound violations (λ_1 ≤ μ_1 and |λ| ≤ |μ| holds for all c^μ_λ ≠ 0).")
    out("")

    return total, passes, fails, bound_violations


def main():
    out_lines = []

    def out(s=""):
        print(s)
        out_lines.append(s)

    out("=" * 100)
    out(" Day 128 — Broad sweep: d_{s*_μ} = d_μ at ℓ=4 (|μ|≤12) and ℓ=5 (|μ|≤10)")
    out("=" * 100)
    out("")

    t4, p4, f4, b4 = sweep(4, 12, out_lines)
    t5, p5, f5, b5 = sweep(5, 10, out_lines)

    out("=" * 100)
    out(" GRAND SUMMARY")
    out("=" * 100)
    out(f" ℓ=4, |μ|≤12: total={t4}, pass={p4}, fail={len(f4)}, bound_violations={len(b4)}")
    out(f" ℓ=5, |μ|≤10: total={t5}, pass={p5}, fail={len(f5)}, bound_violations={len(b5)}")
    out("")

    if not f4 and not f5 and not b4 and not b5:
        out(" VERDICT: All partitions PASS. Identity d_{s*_μ} = d_μ holds across sweep;"
            " combinatorial bounds hold.")
    else:
        out(" VERDICT: NOT clean — see details above.")

    txt_path = "/home/agent/projects/beta-prime/code/day128/l4_l5_sweep.txt"
    with open(txt_path, "w") as f:
        f.write("\n".join(out_lines) + "\n")
    print(f"\n[wrote {txt_path}]")


if __name__ == "__main__":
    main()
