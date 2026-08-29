from collections import defaultdict
from itertools import combinations
from sympy import symbols, expand, factor, Poly, simplify, prod, Rational, Integer, together, cancel


def bt(M):
    def vs(mu):
        L = len(mu) + 2
        b = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = b.copy()
            for i in p:
                n[i] += 1
            ok = True
            for i in range(L - 1):
                if n[i] < n[i + 1]:
                    ok = False
                    break
            if not ok:
                continue
            while n and n[-1] == 0:
                n.pop()
            if len(n) > 3:
                continue
            r.append(tuple(n))
        return r

    cu = defaultdict(int)
    cu[()] = 1
    T = {0: [((0, 0, 0), 1)]}
    for j in range(1, M + 1):
        nx = defaultdict(int)
        for mu, c in cu.items():
            for nu in vs(mu):
                nx[nu] += c
        cu = nx
        rs = []
        for mu, c in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, c))
        T[j] = rs
    return T


def fall(x, k):
    p = Integer(1)
    for i in range(k):
        p *= (x - i)
    return p


def ell(mu):
    return sum(1 for x in mu if x > 0)


def ds(a, b, c, j, T):
    y = (a + 2, b + 1, c)
    tot = Integer(0)
    for mu, kk in T[j]:
        ks = [mu[i] + (2 - i) for i in range(3)]
        M = [[fall(y[i], ks[l]) for l in range(3)] for i in range(3)]
        d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
             - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
             + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        tot += kk * d
    return expand(tot)


def main():
    a, b, c = symbols('a b c')
    T = bt(10)
    V = (a - b + 1) * (a - c + 2) * (b - c + 1)
    print("=" * 78)
    print("Lemma 1 verification: ds_j / V |_{a=-2} = b^{j-fall} (c-1)^{j-fall}")
    print("=" * 78)
    results = {}
    for j in range(3, 11):
        print()
        print(f"--- j = {j} ---")
        print(f"|S_{j}| = {len(T[j])}")
        print(f"partitions in S_{j} (mu, ell(mu), kappa):")
        u_cnt = 0
        u_mu = None
        u_k = None
        for mu, kk in T[j]:
            el = ell(mu)
            print(f"  mu={mu}  ell={el}  kappa={kk}")
            if el <= 2:
                u_cnt += 1
                u_mu = mu
                u_k = kk
        exp_mu = (j, j, 0)
        u_ok = (u_cnt == 1 and u_mu == exp_mu and u_k == 1)
        print(f"unique-partition claim (ell<=2 unique, ={exp_mu}, kappa=1): "
              f"{'PASS' if u_ok else 'FAIL'}  (found {u_cnt}, mu={u_mu}, kappa={u_k})")

        d = ds(a, b, c, j, T)
        q, r = Poly(d, a, b, c).div(Poly(V, a, b, c))
        rem_zero = (r.as_expr() == 0)
        print(f"ds_j divisible by V: {'YES' if rem_zero else 'NO'}")
        if not rem_zero:
            print(f"  remainder = {r.as_expr()}")
            results[j] = ("FAIL", "not divisible by V")
            continue
        qe = expand(q.as_expr())
        qa = expand(qe.subs(a, -2))
        rhs = Integer(1)
        for i in range(j):
            rhs *= (b - i)
        for i in range(j):
            rhs *= (c - 1 - i)
        rhs = expand(rhs)
        diff = expand(qa - rhs)
        if diff == 0:
            print(f"PASS: ds_{j}/V |_{{a=-2}} = b^fall_{j} * (c-1)^fall_{j}")
            print(f"  = {factor(qa)}")
            results[j] = ("PASS", u_ok)
        else:
            print(f"FAIL:")
            print(f"  got   = {factor(qa)}")
            print(f"  want  = {factor(rhs)}")
            print(f"  diff  = {factor(diff)}")
            results[j] = ("FAIL", f"diff={diff}"[:200])

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for j in range(3, 11):
        r = results.get(j, ("MISSING", None))
        print(f"  j = {j}: {r[0]}   unique-mu={r[1]}")


if __name__ == "__main__":
    main()
