"""
Log-concavity / log-convexity check for the b_k sequence.

For each k in 1..10 compute D_k = b_{k-1} * b_{k+1} - b_k^2 and report:
  - exact integer D_k
  - sign
  - log-concavity (D_k <= 0) and log-convexity (D_k >= 0)
  - ratios b_{k+1}/b_k and b_k^2 / (b_{k-1} b_{k+1})
Also compute the growth ratios r_k = b_{k+1}/b_k for k=0..10 and report trend.
"""

from sympy import Integer, Rational, nsimplify


def main() -> None:
    b = [
        Integer(1),
        Integer(3),
        Integer(27),
        Integer(417),
        Integer(7851),
        Integer(164124),
        Integer(3661389),
        Integer(85384566),
        Integer(2056373739),
        Integer(50751637140),
        Integer(1276862920140),
        Integer(32626363346505),
    ]

    n = len(b)
    print("b_k sequence (k = 0..%d):" % (n - 1))
    for k, v in enumerate(b):
        print(f"  b_{k:2d} = {v}")
    print()

    # Discriminants D_k
    print("Log-concavity / log-convexity check")
    print("D_k = b_{k-1} * b_{k+1} - b_k^2")
    print("Log-concave <=> D_k <= 0  (equivalently b_k^2 >= b_{k-1} b_{k+1})")
    print("Log-convex  <=> D_k >= 0")
    print()

    header = f"{'k':>3} {'D_k':>40} {'sign':>10} {'log-concave':>13} {'log-convex':>12} {'r_k=b_{k+1}/b_k':>18} {'b_k^2/(b_{k-1}b_{k+1})':>24}"
    print(header)
    print("-" * len(header))

    all_log_concave = True
    all_log_convex = True

    for k in range(1, n - 1):
        Dk = b[k - 1] * b[k + 1] - b[k] ** 2
        if Dk > 0:
            sign = "positive"
        elif Dk < 0:
            sign = "negative"
        else:
            sign = "zero"

        lc = Dk <= 0
        cvx = Dk >= 0
        if not lc:
            all_log_concave = False
        if not cvx:
            all_log_convex = False

        ratio = Rational(b[k + 1], b[k])
        # b_k^2 / (b_{k-1} b_{k+1})
        q = Rational(b[k] ** 2, b[k - 1] * b[k + 1])

        print(
            f"{k:>3} {str(Dk):>40} {sign:>10} {str(lc):>13} {str(cvx):>12} "
            f"{float(ratio):>18.6f} {float(q):>24.6f}"
        )

    print()
    print(f"All k in 1..{n - 2} log-concave? {all_log_concave}")
    print(f"All k in 1..{n - 2} log-convex?  {all_log_convex}")
    print()

    # Growth ratios r_k = b_{k+1}/b_k for k = 0..n-2
    print("Growth ratios r_k = b_{k+1} / b_k for k = 0..%d:" % (n - 2))
    rs = []
    for k in range(n - 1):
        r = Rational(b[k + 1], b[k])
        rs.append(r)
        print(f"  r_{k:2d} = {float(r):.6f}   (exact: {r})")

    # Trend of r_k
    diffs = [rs[k + 1] - rs[k] for k in range(len(rs) - 1)]
    incr = all(d > 0 for d in diffs)
    decr = all(d < 0 for d in diffs)
    if incr:
        trend = "monotone increasing"
    elif decr:
        trend = "monotone decreasing"
    else:
        trend = "neither monotone increasing nor decreasing"
    print()
    print(f"Trend of r_k: {trend}")
    print("Consecutive differences r_{k+1} - r_k:")
    for k, d in enumerate(diffs):
        print(f"  r_{k+1} - r_{k} = {float(d):.6f}")

    # Second-order: ratios of growth ratios
    print()
    print("Ratio of ratios rho_k = r_{k+1} / r_k (should tend to a limit if b_k algebraic):")
    for k in range(len(rs) - 1):
        rho = rs[k + 1] / rs[k]
        print(f"  rho_{k:2d} = {float(rho):.6f}")

    # Verdict
    print()
    print("=" * 60)
    print("VERDICT")
    print("=" * 60)
    if all_log_concave and not all_log_convex:
        print("Log-concave (strictly, for all tested k in 1..10).")
    elif all_log_convex and not all_log_concave:
        print("Log-convex (strictly, for all tested k in 1..10).")
    elif all_log_concave and all_log_convex:
        print("Both (all D_k = 0) -- geometric sequence.")
    else:
        print("Neither log-concave nor log-convex across the full range.")
    print(f"Growth-ratio trend: {trend}")


if __name__ == "__main__":
    main()
