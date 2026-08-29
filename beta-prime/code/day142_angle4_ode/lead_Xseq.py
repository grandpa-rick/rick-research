"""
Lead 2 — Identify the sequence -3, -18, -255, -4620, -94500.

These are [E_3^k T^{3k-1}] X (U,V)-independent leading coefficients of X = L·F_P/F_P.
Check ratios, factorizations, and OEIS.
"""

from sympy import Integer, Rational, factorial, factorint, sqrt, sympify
import urllib.request
import json


SEQ = [3, 18, 255, 4620, 94500]  # absolute values
SIGNED = [-3, -18, -255, -4620, -94500]


def factor_analysis():
    print("=" * 70)
    print("Prime factorizations of |a_k|")
    print("=" * 70)
    for k, a in enumerate(SEQ, 1):
        f = factorint(a)
        print(f"  k={k}: a_k = {a}  = {f}")

    print("\n" + "=" * 70)
    print("Ratios a_{k+1}/a_k")
    print("=" * 70)
    for i in range(len(SEQ)-1):
        r = Rational(SEQ[i+1], SEQ[i])
        print(f"  a_{i+2}/a_{i+1} = {SEQ[i+1]}/{SEQ[i]} = {r} = {float(r):.4f}")

    print("\n" + "=" * 70)
    print("Try dividing by natural denominators")
    print("=" * 70)
    for k, a in enumerate(SEQ, 1):
        print(f"  k={k}: a_k = {a}")
        print(f"    a_k / 3 = {Rational(a, 3)}")
        print(f"    a_k / (3k-1)! = {Rational(a, factorial(3*k-1))}")
        print(f"    a_k / (3k-1) = {Rational(a, 3*k-1)}")
        print(f"    a_k / k! = {Rational(a, factorial(k))}")
        print(f"    a_k / (3^k) = {Rational(a, 3**k)}")
        print(f"    a_k / (3^k · k!) = {Rational(a, 3**k * factorial(k))}")
        # a_k / (3k)! / something?
        print(f"    a_k · k! / (3k-1)! = {Rational(a * factorial(k), factorial(3*k-1))}")
        print()


def try_formula():
    print("=" * 70)
    print("Attempt formulas")
    print("=" * 70)
    # 3, 18, 255, 4620, 94500
    # 18 = 3·6
    # 255 = 3·85 = 5·51 = 3·5·17
    # 4620 = 4·1155 = 2²·3·5·7·11
    # 94500 = 2²·3³·5³·7
    # Look for growth like (3k-1)! ·  something / (something small)
    #
    # (3k-1)! for k=1..5: 2, 120, 40320, 39916800, ...
    # a_k / (3k-1)! : 3/2, 18/120=3/20, 255/40320=17/2688, ...
    # Simplify: 3/2, 3/20, 17/2688, ...
    for k, a in enumerate(SEQ, 1):
        r = Rational(a, factorial(3*k-1))
        print(f"  k={k}: a_k/(3k-1)! = {r}")

    print()
    for k, a in enumerate(SEQ, 1):
        r = Rational(a * factorial(k), factorial(3*k-1))
        print(f"  k={k}: a_k · k!/(3k-1)! = {r}")

    print("\n  Test: a_k = 3·(2k-1)!! · ??")
    # (2k-1)!! for k=1..5: 1, 3, 15, 105, 945
    # a_k/3: 1, 6, 85, 1540, 31500
    # (2k-1)!!: 1, 3, 15, 105, 945
    # ratios: 1/1, 6/3=2, 85/15=17/3, 1540/105=44/3, 31500/945=100/3
    # Not clean.
    for k, a in enumerate(SEQ, 1):
        dd = 1
        for j in range(1, k+1):
            dd *= (2*j - 1)
        r = Rational(a, 3 * dd)
        print(f"  k={k}: a_k / (3·(2k-1)!!) = {r}")

    # 1, 2, 17/3, 44/3, 100/3 — the k>=3 have 3 in denom. Multiply by 3:
    #  3, 6, 17, 44, 100. Not clean.

    print("\n  Test: a_k = C(3k, k) · something")
    from sympy import binomial
    for k, a in enumerate(SEQ, 1):
        b = binomial(3*k, k)
        r = Rational(a, b)
        print(f"  k={k}: a_k/C(3k,k) = {r}  (C(3k,k)={b})")

    print("\n  Test: a_k = (3k)! / (something)")
    for k, a in enumerate(SEQ, 1):
        r = Rational(factorial(3*k), a)
        print(f"  k={k}: (3k)!/a_k = {r} = {factorint(int(factorial(3*k)))} / {factorint(a)}")


def query_oeis(seq):
    """Query OEIS."""
    print("\n" + "=" * 70)
    print(f"Query OEIS for sequence: {seq}")
    print("=" * 70)
    q = ",".join(str(x) for x in seq)
    url = f"https://oeis.org/search?q={q}&fmt=json"
    print(f"  URL: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        if data.get('results'):
            for r in data['results'][:5]:
                print(f"  A{r['number']:06d}: {r.get('name', '')}")
                if 'formula' in r:
                    print(f"    Formula: {r['formula'][:200]}")
        else:
            print(f"  No results.")
    except Exception as e:
        print(f"  OEIS query failed: {e}")


def main():
    factor_analysis()
    try_formula()
    query_oeis(SEQ)
    query_oeis([SEQ[i]//3 for i in range(len(SEQ))])  # try divided by 3


if __name__ == '__main__':
    main()
